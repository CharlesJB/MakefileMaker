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
        self.steps[step.name] = step
        self.dependencies[step.name] = dependency_name
        self._validate_step(step.name, "register_step: ")

    def produce_makefile(self, step_name):
        self._validate_step_name(step_name, "get_makefile: ")

        # Extract variables
        current_step = self.steps[step_name]
        design_status = self.steps[step_name].design_status
        keep_pair_together = self.steps[step_name].keep_pair_together_status
        dependency = self.dependencies[step_name]
        dir_name = current_step.params['dir_name']
        suffix = current_step.params['suffix']

        if dependency is not None and dependency is not "raw_data":
            input_dir = self.steps[dependency].params['dir_name']
            input_suffix = self.steps[dependency].params['suffix']

        # Get IO
        merged = self.get_merged(step_name)
        paired = self.get_paired(step_name)
        merge = self.get_merge(step_name)
        pair = self.get_pair(step_name)
        if not design_status:
            outputs = self.io_manager.generate_outputs(merged, paired, merge, pair)
        elif keep_pair_together:
            outputs = self.io_manager.generate_inputs(merged, paired, merge, pair)
        else:
            outputs = self.io_manager.generate_outputs_design()
        # TODO: Unit tests
        if dependency is "raw_data":
            inputs = self.io_manager.generate_inputs_raw_data(merge, pair)
        elif dependency is not None:
            if not design_status:
                inputs = self.io_manager.generate_inputs(merged, paired, merge, pair)
            else:
                inputs = self.io_manager.generate_inputs_design()
        if dependency is "raw_data" or dependency is not None:
            if len(inputs) != len(outputs):
                msg = "produce_makefile: len(inputs) != len(outputs)."
                sys.stderr.write(msg)
                sys.exit(1)

        makefile = ""
        # 1. Step specific variables
        makefile += "# Step specific variables\n"
        makefile += step_name.upper() + "_DIR_NAME=" + dir_name + "\n"
        spv = current_step.get_step_specific_variables()
        if spv is not None:
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
        makefile += ".PHONY: " + step_name + "_dir " + step_name + "\n"
        makefile += step_name + "_dir: $(" + step_name.upper() + "_DIR_NAME)\n"
        makefile += "\n"
        makefile += step_name + ": $(" + step_name.upper() + "_TARGETS)" + "\n"
        makefile += "\n"
 
        # 4. Recipes
        makefile += "# Recipes\n"
        for i,_ in enumerate(outputs):
            if dependency is not None:
                current_input = inputs[i].add_prefix(input_dir + "/").add_suffix(input_suffix)
                makefile += current_step.produce_recipe(current_input, outputs[i]) + "\n"
            else:
                makefile += current_step.produce_recipe(None, outputs[i]) + "\n"
            makefile += "\n"
        makefile += dir_name + ":\n"
        makefile += "\tmkdir $@"

        return(makefile)

    def get_merge(self, step_name):
        self._validate_step_name(step_name, "get_merge: ")
        return(self.steps[step_name].merge_status)

    def get_pair(self, step_name):
        self._validate_step_name(step_name, "get_pair: ")
        return(self.steps[step_name].pair_status)

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
        if dependency is not None and dependency is not "raw_data":
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
