#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-01

import sys
import os
from lib.FileList import *

class StepInfos:
    def __init__(self, step_name, dir_name, dependency_names, outputs, pair_data = False, merge_data = False):
        self.params = {}
        self.params["step_name"] = step_name
        self.params["dir_name"] = dir_name
        self.params["pair_data"] = pair_data
        self.params["merge_data"] = merge_data

        self.dependency_names = dependency_names
        self.outputs = outputs

        self._valid()

    def get_step_name(self):
        return(self.params["step_name"])

    def get_dir_name(self):
        return(self.params["dir_name"])

    def get_dependency_names(self):
        return(self.dependency_names)

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
        if not isinstance(self.dependency_names, list):
            msg += "StepInfos: param \"dependency_names\" should be a list.\n"
            error = True
#        elif len(self.dependencies) < 1:
#            msg += "StepInfos: param \"dependencies\" should contains at least one FileList.\n"
#            error = True
        else:
            for dependency in self.dependency_names:
                if not isinstance(dependency, basestring):
                    msg += "StepInfos: param \"dependency_names\" entries should be basestring.\n"
                    error = True
        if not isinstance(self.outputs, dict):
            msg += "StepInfos: param \"outputs\" should be a list.\n"
            error = True
        elif len(self.outputs) < 1:
            msg += "StepInfos: param \"outputs\" should contains at least one FileList.\n"
            error = True
        else:
            for output in self.outputs.values():
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


