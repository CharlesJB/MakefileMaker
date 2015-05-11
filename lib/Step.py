#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-04-30

import sys
import os

import ConfigParser
from lib.FileList import *

class Step:
    def __init__(self):
        self.name = self.get_name()
        self.config_files = []
        self.params = {}
        self._set_default_params()
        self.dependency_names = []
        self._set_dependency_names()

    def add_config_file(self, config_file):
        if self._check_string(config_file):
            self.config_files.append(config_file)

    # dependencies is a dict of FileList
    def produce_recipe(self, dependencies, outputs):
        self._validate_params(dependencies, outputs)
        self._parse_config()
        recipe = ''
        recipe += " ".join(outputs) + ": "
        for file_list in dependencies.values():
            recipe += " ".join(file_list.unlist())
        recipe += "\n"
        recipe += self._get_command(dependencies, outputs)
        return(recipe)

    def _parse_config(self):
        config_parser = ConfigParser.ConfigParser()
        if len(self.config_files) > 0:
            for config_file in self.config_files:
                config_parser.read(config_file)
            if self.name in config.sections():
                for param in self.params.keys():
                    try:
                        new_param = config_parser.get(self.name, param)
                        self.params[param] = new_param
                    except ConfigParser.NoOptionError:
                        pass

    def _validate_params(self, dependencies, outputs):
        msg = "Step: _validate_params: "
        error = False
        if not isinstance(dependencies, dict):
            msg += "dependencies should be a dict.\n"
            error = True
        else:
            for name in dependencies.keys():
                if name not in self.dependency_names:
                    msg += name + " is not an exepted dependency for step "
                    msg += self.step_name + "\n"
                    error = True
            for file_list in dependencies.values():
                if not isinstance(file_list, FileList):
                    msg += "dependencies entries must be FileList\n"
                    error = True
        if not isinstance(outputs, list):
            msg += "outputs should be a list.\n"
            error = True
        else:
            for output in outputs:
                if not self._check_string(output):
                    msg += str(output) + " is incorrectly formatted.\n"
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _check_string(self, string):
        if not isinstance(string, basestring):
            return(False)
        if len(string) < 1:
            return(False)
        return(True)

class DummyStep(Step):
    def get_name(self):
        return("DummyStep")

    def _get_command(self, dependencies, outputs):
        command = ""
        command += "\t@echo $@\n"
        command += "\t@echo $^\n"
        return(command)

    def _set_default_params(self):
        self.params['param1'] = 1
        self.params['param2'] = 2

    def _set_dependency_names(self):
        self.dependency_names.append('dependency_name_1')
