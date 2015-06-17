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
        self.config_files = config_files

        # Check if object is still valid
        self._valid()

        # Prepare config file
        self._parse_config()

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
    def get_targets(self, outputs):
        pass

    # To implement in each Step
    def get_phony_target(self):
        pass

    # inputs and outputs are list of FileList
    def produce_recipe(self, inputs, outputs):
        self._validate_params(inputs, outputs)
        # Target
        target = " ".join(outputs.unlist())
        dependencies = inputs
        if inputs != "":
            dependencies  = " ".join(inputs.unlist())
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
        if not isinstance(inputs, FileList) and inputs != "":
            msg += "inputs/outputs should be FileList."
            error = True
        if not isinstance(outputs, FileList):
            msg += "outputs should be a FileList."
            error = True
        else:
            if self.get_pair_status() and outputs.get_paired_status():
                msg += "outputs cannot be paired when pair status is True."
                error = True
            if self.get_merge_status() and outputs.get_file_count() > 1:
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
    def get_targets(self, outputs):
        return("TARGET_DUMMY=dummy.txt")

    # To implement in each Step
    def get_phony_target(self):
        return("dummy: $(TARGET_DUMMY)")

    # To implement in each Step
    def _set_step_specific_values(self):
        self.name = "DummyStep"
        self.dir_name = "Dummy"
        self.suffix = ".txt"
        self.merge_status = True
        self.pair_status = True
        self.keep_pair_together_status = False

    # To implement in each Step
    def _get_command(self, dependencies, outputs):
        command = "\t@echo $@\n"
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
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)
