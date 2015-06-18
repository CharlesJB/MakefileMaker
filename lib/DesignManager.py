#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-08

import sys
import os

class DesignManager:
    def __init__(self, design_file):
        self.reset()
        self.params["design_file"] = design_file
        self._parse_design_file()
        self._valid()

    def reset(self):
        self.params = {}
        self.exp_dict = {}
        self._tokens_count = 0
        self._file_names = []
        self._header = ""

    def get_design_names(self):
        return(self.exp_dict.keys())

    def get_groups(self, design_name):
        return(self.exp_dict[design_name].keys())

    def get_group_names(self, design_name, group_name):
        return(self.exp_dict[design_name][group_name])

    def _parse_design_file(self):
        design_file = self.params["design_file"]
        header = False
        exp_name_indexes = {}
        for line in open(design_file):
            tokens = line.strip().split()
            if header == False:
                self._validate_header(line)
                self._header = line
                for i, name in enumerate(tokens):
                    if i > 0:
                        exp_name_indexes[int(i)] = name
                        self.exp_dict[name] = {}
                header = True
            else:
                self._validate_line(line)
                for i, j in enumerate(tokens):
                    file_name = tokens[0]
                    if i > 0:
                        if int(j) > 0:
                            exp_name = exp_name_indexes[int(i)]
                            if int(j) not in self.exp_dict[exp_name]:
                                self.exp_dict[exp_name][int(j)] = []
                            self.exp_dict[exp_name][int(j)].append(file_name)

    def _validate_header(self, header):
        error = False
        msg = ""

        tokens = header.strip().split()
        self._tokens_count = len(tokens)
        if len(tokens) < 2:
            msg += "_validate_header: design file must have at least 2 columns.\n"
            error = True
        token_list = []
        for token in tokens:
            if not self._validate_string(token):
                msg += "_validate_header: exp_name "
                msg += token
                msg += " is not in a valid format.\n"
                error = True
            if token in token_list:
                msg += "_validate_header: all exp_name must be unique.\n"
                error = True
            token_list.append(token)
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_line(self, line):
        error = False
        msg = ""

        tokens = line.strip().split()
        if len(tokens) != self._tokens_count:
            msg += "_validate_line: number of element in line not equal to number of elements in header.\n"
            error = True
        for i, token in enumerate(tokens):
            if i == 0:
                if not self._validate_string(token):
                    msg += "_validate_line: file_name "
                    msg += token
                    msg += " is not in a valid format.\n"
                    error = True
                if token in self._file_names:
                    msg += "_validate_line: all file_name must be unique.\n"
                    error = True
                else:
                    self._file_names.append(token)
            else:
                try:
                    int(token)
                except:
                    msg += "_validate_line: groups must be an integer value.\n"
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _validate_string(self, string):
        correct = True
        if not isinstance(string, basestring):
            correct = False
        elif len(string) < 1:
            correct = False
        return(correct)

    def _valid(self):
        if len(self.exp_dict) == 0:
            sys.stderr.write("Error. Design file is empty.\n")
            sys.exit(1)
        for exp in self.exp_dict.values():
            if len(exp) == 0:
                sys.stderr.write("Error. All exp_name in design file must have at least 1 file_name with a group value > 0.\n")
                sys.exit(1)
