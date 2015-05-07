#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-01

import sys
import os
from lib.SampleManager import *

#class FileList:
#    def __init__(self, file_list, name):
#        self.file_list = file_list
#        self.name = name
#        self._valid()
#
#    def get_files(self, i):
#        try:
#            files = self.file_list[i]
#        except:
#            msg = "FileList.get_files: invalid index.\n"
#            sys.stderr.write(msg)
#            sys.exit(1)
#        if len(files[1]) == 0:
#            to_return = []
#            to_return.append(files[0])
#            return(to_return)
#        return(files)
#
#    def get_name(self):
#        return(self.name)
#
#    def _valid(self):
#        correct = True
#        msg = ""
#        if not isinstance(self.name, basestring):
#            msg += "FileList: name param should be a string.\n"
#            correct = False
#        elif len(self.name) < 1:
#            msg += "FileList: name param should be at least 1 character long.\n"
#            correct = False
#        if not isinstance(self.file_list, list):
#            msg += "FileList: file_list param should be a list.\n"
#            correct = False
#        else:
#            if len(self.file_list) < 1:
#                msg += "FileList: file_list does not contain entry.\n"
#                correct = False
#            else:
#                for key in self.file_list:
#                    if self._validate_key(key) == False:
#                        msg += "FileList: At least one key is incorrectly formatted.\n"
#                        correct = False
#        if correct == False:
#            sys.stderr.write(msg)
#            sys.exit(1)
#        
#
#    def _validate_key(self, key):
#        correct = True
#        if not isinstance(key, list):
#            correct = False
#        elif len(key) != 2:
#            correct = False
#        else:
#            for entry in key:
#                if not isinstance(entry, basestring):
#                    correct = False
#            if len(key[0]) < 1:
#                correct = False
#        return(correct)

class StepInfos:
    def __init__(self, step_name, dir_name, dependencies, outputs, pair_data = False, merge_data = False):
        self.params = {}
        self.params["step_name"] = step_name
        self.params["dir_name"] = dir_name
        self.params["pair_data"] = pair_data
        self.params["merge_data"] = merge_data

        self.dependencies = dependencies
        self.outputs = outputs

        self._valid()

    def get_step_name(self):
        return(self.params["step_name"])

#    def get_names(self):

    def get_dir_name(self):
        return(self.params["dir_name"])

    def get_dependencies(self):
        return(self.dependencies)

    def get_outputs(self):
        return(self.outputs)

    def _valid(self):
        error = False
        msg = ""
        if not isinstance(self.params["step_name"], basestring):
            msg += "StepInfos: param \"step_name\" not a basestring.\n"
            error = True
        elif len(self.params["step_name"]) < 1:
            msg += "StepInfos: param \"step_name\" must be at least one char long.\n"
            error = True
        if not isinstance(self.params["dir_name"], basestring):
            msg += "StepInfos: param \"dir_name\" not a basestring.\n"
            error = True
        elif len(self.params["dir_name"]) < 1:
            msg += "StepInfos: param \"dir_name\" must be at least one char long.\n"
            error = True
        if not isinstance(self.dependencies, list):
            msg += "StepInfos: param \"dependencies\" should be a list.\n"
            error = True
        elif len(self.dependencies) < 1:
            msg += "StepInfos: param \"dependencies\" should contains at least one FileList.\n"
            error = True
        else:
            for dependency in self.dependencies:
                if not isinstance(dependency, FileList):
                    msg += "StepInfos: param \"dependencies\" entries should be FileList.\n"
                    error = True
        if not isinstance(self.outputs, list):
            msg += "StepInfos: param \"outputs\" should be a list.\n"
            error = True
        elif len(self.outputs) < 1:
            msg += "StepInfos: param \"outputs\" should contains at least one FileList.\n"
            error = True
        else:
            for output in self.outputs:
                if not isinstance(output, FileList):
                    msg += "StepInfos: param \"outputs\" entries should be FileList.\n"
                    error = True
        if not isinstance(self.params["pair_data"], bool):
            msg += "StepInfos: param \"pair_data\" not a basestring.\n"
            error = True
        if not isinstance(self.params["merge_data"], bool):
            msg += "StepInfos: param \"merge_data\" not a basestring.\n"
            error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)


class StepManager:
    def __init__(self, sample_manager):
        self.steps = []
        self.step_names = []
        self.sample_manager = sample_manager
        self._valid()

    def register_step(self, step_name, suffix, dir_name, dependency_names, pair_data, merge_data):
        self._validate_register_params(step_name, suffix, dir_name, dependency_names)
#        outputs = self._generate_outputs(step_name, suffix, dir_name, pair_data, merge_data)
        step_infos = StepInfos(step_name, dir_name, dependencies, outputs, pair_data, merge_data)
        self.steps.append(step_infos)
        self.step_names.append(step_name)

#    def _generate_outputs(self, step_name, names, suffix, dir_name, dependencies, pair_data, merge_data):

    def _valid(self):
        error = False
        msg = "StepManager object is in invalid state.\n"
        if not isinstance(self.steps, list):
            msg += "self.steps is not a list.\n"
            error = True
        else:
            for step in self.steps:
                if not isinstance(step, StepInfo):
                    msg += "step in self.steps is not a StepInfo\n"
                    error = True
        if not isinstance(self.step_names, list):
            msg += "self.step_names is not a list.\n"
            error = True
        else:
            for step_name in self.step_names:
                if not isinstance(step_name, basestring):
                    msg += "step_name in self.step_names is not a string.\n"
                    error = True
                elif len(step_name) < 1:
                    msg += "step_name in self.step_names should be at least 1 character.\n"
                    error = True
        if not isinstance(self.sample_manager, SampleManager):
            msg += "self.sample_manager is not a SampleManager.\n"

    def _validate_register_params(self, step_name, names, suffix, dir_name, dependency_names):
        error = False
        msg = ""
        if not isinstance(step_name, basestring):
            msg += "register_step: step_name param should be a string.\n"
            error = True
        elif len(step_name) < 1:
            msg += "register_step: step_name length should be greater than 0.\n"
            error = True
        if not isinstance(names, list):
            msg += "register_step: names should be a list.\n"
            error = True
        else:
            for name in names:
                if not isinstance(name, basestring):
                    msg += "register_step: name in names should be string.\n"
                    error = True
                elif len(name) < 1:
                    msg += "register_step: name in names length should be greater than 0.\n"
                    error = True
        if not isinstance(suffix, basestring):
            msg += "register_step: suffix param should be a string.\n"
            error = True
        elif len(step_name) < 1:
            msg += "register_step: suffix length should be greater than 0.\n"
            error = True
        if not isinstance(dir_name, basestring):
            msg += "register_step: dir_name param should be a string.\n"
            error = True
        elif len(dir_name) < 1:
            msg += "register_step: dir_name length should be greater than 0.\n"
            error = True
        if not isinstance(dependency_names, list):
            msg += "register_step: dependency_names param should be a list.\n"
            error = True
        else:
            for name in dependency_names:
                if len(name) < 1:
                    msg += "register_step: dependency_names key length should be greater than 0.\n"
                    error = True
                if name not in self.step_names:
                    msg += "register_step: dependency "
                    msg += name
                    msg += " is not registered.\n"
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)
