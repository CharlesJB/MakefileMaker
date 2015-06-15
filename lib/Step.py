#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

import ConfigParser
from lib.FileList import *

class Step:
    def __init__(self, config_files):
        self.params = {}
        self._set_default_params()

        # Step specific values, to set in _set_step_specific_values
        self.name = ""
        self.dir_name = ""
        self.merge_status = False
        self.pair_status = False
        self.keep_pair_together_status = False
        self._set_step_specific_values()

        # Prepare config file
        self.config_files = config_files
        self._parse_config()

        # Check if object is still valid
        self._valid()

    def get_name(self):
        return(self.name)

    def get_dir_name(self):
        return(self.dir_name)

    def get_merge_status(self):
        return(self.merge_status)

    def get_pair_status(self):
        return(self.pair_status)

    def get_keep_pair_together_status(self):
        return(self.keep_pair_together_status)

    # To implement in each Step
    def get_step_specific_variables(self):
        pass

    # To implement in each Step
    def get_target(self):
        pass

    # To implement in each Step
    def get_phony_target(self):
        pass

    # inputs and outputs are list of FileList
    def produce_recipe(self, inputs, outputs):
        self._validate_params(inputs, outputs)
        # Target
        target = self._list_files(outputs)
        dependencies  = self._list_files(inputs)
        if len(dependencies) > 0:
            recipe = target + ": " + dependencies + "\n"
        else:
            recipe = target + ":\n"
        recipe += self._get_command(inputs, outputs)
        return(recipe)

    def _parse_config(self):
        config_parser = ConfigParser.ConfigParser()
        if len(self.config_files) > 0:
            for config_file in self.config_files:
                config_parser.read(config_file)
            if self.name in config_parser.sections():
                for param in self.params.keys():
                    try:
                        new_param = config_parser.get(self.name, param)
                        self.params[param] = new_param
                    except ConfigParser.NoOptionError:
                        pass

    def _list_files(self, file_lists):
        result = []
        for file_list in file_lists:
            result += file_list.unlist()
        return(" ".join(result))

    def _valid(self):
        error = False
        msg = "Step: _valid: "
        if not isinstance(self.config_files, list):
            msg += "config_files should be a list.\n"
            error = True
        elif len(self.config_files) < 1:
            msg += "config_files should have at least one entry"
        else:
            for config_file in self.config_files:
                if not self._check_string(config_file):
                    msg += "A config file entry is not a valid string."
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_params(self, inputs, outputs):
        msg = "Step: _validate_params: "
        error = False
        if not isinstance(inputs, list):
            msg += "inputs/outputs should be list."
            error = True
        else:
            if not isinstance(inputs, list):
                msg += "inputs should be a list."
                error = True
            else:
                for inpt in inputs:
                    if not isinstance(inpt, FileList):
                        msg += "inputs must be FileList."
                        error = True
            if not isinstance(outputs, list):
                msg += "outputs should be a list."
                error = True
            elif len(outputs) < 1:
                msg += "outputs should have at least one entry"
            else:
                for output in outputs:
                    if not isinstance(output, FileList):
                        msg += "outputs must be FileList."
                        error = True
                    if self.get_pair_status() and output.get_paired_status():
                        msg += "outputs cannot be paired when pair status is True."
                        error = True
                    if self.get_merge_status() and output.get_file_count() > 1:
                        msg += "outputs FileList cannot contain more than 1 file when merge status is True."
                        error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

        self._validate_param_step_specific(inputs, outputs)

    def _check_string(self, string):
        if not isinstance(string, basestring):
            return(False)
        if len(string) < 1:
            return(False)
        return(True)

class DummyStep(Step):
    # To implement in each Step
    def get_step_specific_variables(self):
        return("ABC=DEF")

    # To implement in each Step
    def get_target(self):
        return("TARGET_DUMMY=dummy.txt")

    # To implement in each Step
    def get_phony_target(self):
        return("dummy: $(TARGET_DUMMY)")

    # To implement in each Step
    def _set_step_specific_values(self):
        self.name = "DummyStep"
        self.dir_name = "Dummy"
        self.merge_status = True
        self.pair_status = True
        self.keep_pair_together_status = False

    # To implement in each Step
    def _get_command(self, dependencies, outputs):
        command = ""
        command += "\t@echo $@\n"
        command += "\t@echo $^\n"
        return(command)

    # To implement in each Step
    def _set_default_params(self):
        self.params['dummy_param_1'] = 'dummy_param_default_1'
        self.params['dummy_param_2'] = 'dummy_param_default_2'

    # To implement in each Step, if necessary
    def _validate_param_step_specific(self, inputs, outputs):
        error=False
        msg = "DummyStep - _validate_param_step_specific: "
        if len(outputs) != 1:
            msg += "outputs must be of length 1."
            error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)