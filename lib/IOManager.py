#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-08

import sys
import os

from lib.FileList import *

class OutputManager:
    def __init__(self, raw_files):
        self.raw_files = raw_files
        self.paired = False
        self.merged = False
        self._valid()

    def get_files_1(self, name = None, merge = False):
        return(self._get_files(0, name, merge))

    def get_files_2(self, name = None, merge = False):
        return(self._get_files(1, name, merge))

    def generate_outputs(self,  pair = False, merge = False):
        self._validate_outputs_param(pair, merge)
        self._validate_flags(pair, merge)
        self.paired = pair
        self.merged = merge

        outputs = {}
        for name in self.raw_files.keys():
            outputs[name] = self._generate_output(name)
        return(outputs)

    def _get_files(self, idx, name, merge):
        if name is None:
            fastq_list = self.raw_files
        elif name in self.raw_files:
            fastq_list = { name: self.raw_files[name] }
        else:
            return(None)

        to_return = []
        for file_list in fastq_list.values():
            if idx == 0:
                to_return += file_list.unlist_file1(merge)
            else:
                to_return += file_list.unlist_file2(merge)

        return(to_return)

    def _generate_output(self, name):
        output = []
        merge = self.merged
        pair = self.paired

        file_list = self.raw_files[name]

        if merge == False:
            for i,file_pair in enumerate(file_list.file_list):
                output.append([])
                if pair == False:
                    file_1 = name + "_" + str(i+1) + "_R1"
                    file_2 = ""
                    if len(file_pair[1]) > 0:
                        file_2 = name + "_" + str(i+1) + "_R2"
                if pair == True:
                    file_1 = name + "_" + str(i+1)
                    file_2 = ""
                output[i] += [file_1, file_2]
        if merge == True:
            if pair == False:
                file_1 = name + "_R1"
                file_2 = ""
                if len(file_list.file_list[0][1]) > 0:
                    file_2 = name + "_R2"
            if pair == True:
                file_1 = name
                file_2 = ""
            output.append([file_1, file_2])
        return(FileList(output, name))

    def _valid(self):
        error = False
        msg = ""
        if not isinstance(self.raw_files, dict):
            msg += "OutputManager, _valid: raw_files should be a dict.\n"
            error = True
        elif len(self.raw_files) < 1:
            msg += "OutputManager, _valid: raw_files should have at least 1 FileList.\n"
            error = True
        else:
            for file_list in self.raw_files.values():
                if not isinstance(file_list, FileList):
                    msg += "OutputManager, _valid: raw_files entries should be FileList.\n"
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_outputs_param(self, pair, merge):
        error = False
        msg = "OutputManager: generate_outputs invalid params:\n"
        if not isinstance(pair, bool):
            msg += "pair is incorrect\n"
            error = True
        if not isinstance(merge, bool):
            msg += "merge is incorrect\n"
            error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_flags(self, pair, merge):
        error = False
        msg = ""
        if self.paired == True and pair == False:
            msg += "OutputManager: pair param is False but previous call of generate_outputs set it to True.\n"
            error = True
        if self.merged == True and merge == False:
            msg += "OutputManager: merge param is False but previous call of generate_outputs set it to True.\n"
            error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _check_string(self, string):
        correct = True
        if not isinstance(string, basestring):
            correct = False
        elif len(string) < 1:
            correct = False
        return(correct)
