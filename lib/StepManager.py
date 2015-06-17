#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-01

import sys
import os
from lib.IOManager import *
from lib.Step import *

class StepManager:
    def __init__(self, io_manager):
        self.steps = {}
        self.dependencies = {}
        self.io_manager = io_manager
        self._valid()

    def register_step(self, step, dependency_name):
        if not isinstance(step, Step):
            msg = "register_step: invalid step class."
            sys.stderr.write(msg)
            sys.exit(1)
        self._validate_dependencies(dependency_name, "register_step: ")
        self.steps[step.get_name()] = step
        self.dependencies[step.get_name()] = dependency_name
        self._validate_step(step.get_name(), "register_step: ")

    def produce_makefile(self, step_name):
        self._validate_step_name(step_name, "get_makefile: ")

        # Extract variables
        current_step = self.steps[step_name]
        dependency = self.dependencies[step_name]
        dir_name = current_step.get_dir_name()
        suffix = current_step.suffix
        if dependency is not None:
            input_dir = self.steps[dependency].get_dir_name()
            input_suffix = self.steps[dependency].suffix

        # Get IO
        merged = self.get_merged(step_name)
        paired = self.get_paired(step_name)
        merge = self.get_merge(step_name)
        pair = self.get_pair(step_name)
        outputs = self.io_manager.generate_outputs(merged, paired, merge, pair)
        if dependency is not None:
            inputs = self.io_manager.generate_inputs(merged, paired, merge, pair)
            if len(inputs) != len(outputs):
                msg = "produce_makefile: len(inputs) != len(outputs)."
                sys.stderr.write(msg)
                sys.exit(1)

        makefile = ""
        # 1. Step specific variables
        makefile += "# Step specific variables\n"
        makefile += step_name.upper() + "_DIR_NAME=" + dir_name + "\n"
        makefile += current_step.get_step_specific_variables() + "\n"
        makefile += "\n"

        # 2. Targets
        makefile += "# Targets\n"
        for file_list in outputs:
            for file_name in file_list.unlist():
                makefile += step_name.upper() + "_TARGETS+="
                makefile += dir_name + "/" + file_name + suffix + "\n"
        makefile += "\n"

        # 3. Phony targets
        makefile += "# Phony targets\n"
        makefile += ".PHONY: " + step_name + "\n"
        makefile += step_name + ": $(" + step_name.upper() + "_TARGETS)" + "\n"
        makefile += "\n"
 
        # 4. Recipes
        makefile += "# Recipes\n"
        for i,_ in enumerate(outputs):
            if dependency is not None:
                makefile += current_step.produce_recipe(inputs[i], outputs[i], input_dir, input_suffix) + "\n"
            else:
                makefile += current_step.produce_recipe(None, outputs[i], None, None) + "\n"
            makefile += "\n"

        return(makefile)

    def get_merge(self, step_name):
        self._validate_step_name(step_name, "get_merge: ")
        return(self.steps[step_name].get_merge_status())

    def get_pair(self, step_name):
        self._validate_step_name(step_name, "get_pair: ")
        return(self.steps[step_name].get_pair_status())

    def get_merged(self, step_name):
        self._validate_step_name(step_name, "get_merged: ")
        dependency = self.dependencies[step_name]
        if dependency is None:
            return(False)
        if self.get_merge(dependency):
            return(True)
        if self.get_merged(dependency):
            return(True)
        return(False)

    def get_paired(self, step_name):
        self._validate_step_name(step_name, "get_paired: ")
        dependency = self.dependencies[step_name]
        if dependency is None:
            return(False)
        if self.get_pair(dependency):
            return(True)
        if self.get_paired(dependency):
            return(True)
        return(False)

    def _validate_dependencies(self, dependency, base_msg):
        error = False
        msg = base_msg
        if dependency is not None:
            if not isinstance(dependency, basestring) or len(dependency) < 1:
                msg += "dependency must be a basestring."
                error = True
            elif dependency not in self.dependencies:
                msg += "missing dependency " + dependency + "."
                error = True
        if error:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_step(self, step_name, base_msg):
        error = False
        msg = base_msg
        # Valid merge
        if self.get_merged(step_name) and self.get_merge(step_name):
            msg += "error in step " + step_name + ", cannot merge twice."
            error = True
        # Valid pair
        if self.get_paired(step_name) and self.get_pair(step_name):
            msg += "error in step " + step_name + ", cannot pair twice."
            error = True
        if error:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_step_name(self, step_name, base_msg):
        msg = base_msg
        if step_name not in self.steps:
            msg += "Invalid step_name."
            sys.stderr.write(msg)
            sys.exit(1)

    def _valid(self):
        error = False
        msg = "StepManager object is in invalid state.\n"
        if not isinstance(self.io_manager, IOManager):
            msg += "self.io_manager is not a IOManager.\n"
            error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_list_of_strings(self, list_of_strings, base_msg):
        error = False
        msg = base_msg
        if not isinstance(list_of_strings, list):
            msg += "param should be a list.\n"
            error = True
        else:
            for name in list_of_strings:
                if len(name) < 1:
                    msg += "key length should be greater than 0.\n"
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)
