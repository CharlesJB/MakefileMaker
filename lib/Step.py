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

        # Step specific values, to set in _set_step_specific_values
        self.name = ""
        self.merge_status = False
        self.pair_status = False
        self.keep_pair_together_status = False
        self.design_status = False
        self._set_step_specific_values()
        self.config_files = config_files

        # Check if object is still valid
        self._valid()

        # Prepare config file
        self._set_default_params()
        self._parse_config()

    # To implement in each Step
    def get_step_specific_variables(self):
        return(None)

    # inputs and outputs are FileList
    def produce_recipe(self, inputs, outputs, keep_pair = False):
        self._validate_params(inputs, outputs)
        # Target
        target = " ".join(outputs.unlist(self.params['dir_name'], self.params['suffix']))
        dependencies = inputs
        if inputs is not None:
            dependencies = []
            for inpt in inputs:
                dependencies += inpt.unlist()
            dependencies  = " ".join(dependencies)
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
            for param in self.params:
                try:
                    new_param = config_parser.get(self.name, param)
                    self.params[param] = new_param
                except ConfigParser.NoSectionError:
                    # TODO: Add test for this case
                    try:
                        new_param = config_parser.get("DEFAULT", param)
                        self.params[param] = new_param
                    except ConfigParser.NoOptionError:
                        pass
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
        if inputs is not None:
            if not isinstance(inputs, list):
                msg += "inputs should be FileList."
                error = True
            else:
                for value in inputs:
                    if not isinstance(value, FileList):
                        msg += "inputs values should be FileList."
                        error = True
        if not isinstance(outputs, FileList):
            msg += "outputs should be a FileList."
            error = True
        else:
            if self.pair_status and outputs.get_paired_status():
                msg += "outputs cannot be paired when pair status is True."
                error = True
            if self.merge_status and outputs.get_file_count() > 1:
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
    def _set_step_specific_values(self):
        self.name = "DummyStep"
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
        self.params['dir_name'] = 'Dummy'
        self.params['suffix'] = '.txt'

    # To implement in each Step, if necessary
    def _validate_param_step_specific(self, inputs, outputs):
        error=False
        msg = "DummyStep - _validate_param_step_specific: "
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)
