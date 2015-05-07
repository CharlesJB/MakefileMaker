#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-04-30

import sys
import os

class FileList:
    def __init__(self, file_list, name):
        self.file_list = file_list
        self.name = name
        self._valid()

    def get_files(self, i):
        try:
            files = self.file_list[i]
        except:
            msg = "FileList.get_files: invalid index.\n"
            sys.stderr.write(msg)
            sys.exit(1)
        if len(files[1]) == 0:
            to_return = []
            to_return.append(files[0])
            return(to_return)
        return(files)

    def get_name(self):
        return(self.name)

    def _valid(self):
        correct = True
        msg = ""
        if not isinstance(self.name, basestring):
            msg += "FileList: name param should be a string.\n"
            correct = False
        elif len(self.name) < 1:
            msg += "FileList: name param should be at least 1 character long.\n"
            correct = False
        if not isinstance(self.file_list, list):
            msg += "FileList: file_list param should be a list.\n"
            correct = False
        else:
            if len(self.file_list) < 1:
                msg += "FileList: file_list does not contain entry.\n"
                correct = False
            else:
                for key in self.file_list:
                    if self._validate_key(key) == False:
                        msg += "FileList: At least one key is incorrectly formatted.\n"
                        correct = False
        if correct == False:
            sys.stderr.write(msg)
            sys.exit(1)
        

    def _validate_key(self, key):
        correct = True
        if not isinstance(key, list):
            correct = False
        elif len(key) != 2:
            correct = False
        else:
            for entry in key:
                if not isinstance(entry, basestring):
                    correct = False
            if len(key[0]) < 1:
                correct = False
        return(correct)

# This is a class to parse samplesheets.
#
# Samplesheets are a way to give more human readable names to files and to
# specify which files are paired together (if any).
#
# A samplesheet is a tab-delimited file with at least 3 columns:
#    * name
#    * fastq1
#    * fastq2
#
# The name of each column must be present in the header of the file but are not
# case sensitive.
#
# There must be a column named fastq2 but it does not have to contain a value in
# the following lines. fastq1 and fastq2 should only be used for paired files,
# otherwise use only fastq1.
#
# The name column will be used to create the prefix for all the output of the
# pipeline. It should thus be short and allow to match uniquely to a specific
# condition.
#
# Multiple lines can have the same name: this correspond to the case where the
# reads were splitted on multiple lanes or that multiple files were created
# during the demultiplexing step.
#
# The files with the same name will be merged in the final output.
class SampleManager:
    def __init__(self, samplesheet):
        self.reset()
        self.params["samplesheet"] = samplesheet
        self._parse_samplesheet()
        self._valid()

    def reset(self):
        self.params = {}
        self.raw_files_r1 = {}
        self.raw_files_r2 = {}
        self.idx = {}

    def generate_outputs(self, dir_name, suffix, pair, merge):
        outputs = []
        for name in self.raw_files_r1.keys():
            outputs.append(self._generate_output(name, dir_name, suffix, pair, merge))
        return(outputs)

    def _generate_output(self, name, dir_name, suffix, pair, merge):
        output = []
        pair1 = self.raw_files_r1[name]
        pair2 = self.raw_files_r2[name]
        if merge == False:
            count = 1
            for i, _ in enumerate(pair1):
                current_name_1 = dir_name + "/"
                current_name_1 += name + "_" + str(count)
                current_name_2 = ""
                if pair == False:
                    current_name_1 += "_R1"
                    if len(pair2[i]) > 0:
                        current_name_2 = current_name_1[:-1] + "2"
                        current_name_2 += suffix
                current_name_1 += suffix
                output.append([current_name_1, current_name_2])
                count += 1
        else:
            current_name_1 = dir_name + "/"
            current_name_1 += name
            current_name_2 = ""
            if pair == False:
                current_name_1 += "_R1"
                if len(pair2[0]) > 0:
                    current_name_2 = current_name_1[:-1] + "2"
                    current_name_2 += suffix
            current_name_1 += suffix
            output.append([current_name_1, current_name_2])
        return(FileList(output, name))

    def _validate_outputs_param(self, dir_name, suffix, pair, merge):
        error = False
        msg = "SampleManager: generate_outputs invalid params:\n"
        if not self._check_string(dir_name):
            msg += "dir_name is incorrect.\n"
            error = True
        if not self._check_string(suffix):
            msg += "suffix is incorrect.\n"
            error = True
        if not isinstance(pair, bool):
            msg += "pair is incorrect\n"
            error = True
        if not isinstance(merge, bool):
            msg += "merge is incorrect\n"
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

    def _parse_samplesheet(self):
        samplesheet = self.params["samplesheet"]
        header = False
        colnames = []
        for line in open(samplesheet):
            # Parse header
            if header == False:
                for col in line.split():
                    colnames.append(col.lower())
                    header = True
                self._check_colnames(colnames)
                self.idx['name'] = colnames.index('name')
                self.idx['fastq1'] = colnames.index('fastq1')
                self.idx['fastq2'] = colnames.index('fastq2')
            # Parse other lines
            else:
                self._add_line(line)

#    def _parse_config(self):
#        if self.params["config"] is not None:
#            config = self.params["config"]
#            if "symlinks" in config.sections():

    def _check_colnames(self, colnames):
        error = False
        msg = ""
        if "name" not in colnames:
            msg += "Error: name column absent from header\n"
            error = True
        if "fastq1" not in colnames:
            msg += "Error: fastq1 column absent from header\n"
            error = True
        if "fastq2" not in colnames:
            msg += "Error: fastq2 column absent from header\n"
            error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _add_line(self, line):
        # Prepare the tokens
        tokens = line.split('\t')
        tokens[-1] = tokens[-1].strip()
        name = tokens[self.idx['name']]
        fastq1 = tokens[self.idx['fastq1']]
        fastq2 = tokens[self.idx['fastq2']]

        # Add file paths
        if name not in self.raw_files_r1:
            self.raw_files_r1[name] = []
        self.raw_files_r1[name].append(fastq1)
        if name not in self.raw_files_r2:
            self.raw_files_r2[name] = []
        self.raw_files_r2[name].append(fastq2)

    def _valid(self):
        error = False
        msg = "SampleManager in invalid state:\n"
        # Check if some all variable have same amount of content
        if (self.raw_files_r1.keys() != self.raw_files_r2.keys()):
            msg += "raw_files keys are not identical.\n"
            error = True
        # Check if all filename exist
        for files in self.raw_files_r1.values():
            for file in files:
                if os.path.isfile(file) == False:
                    msg += "  File not found:" + file + "\n"
                    error = True
        for files in self.raw_files_r2.values():
            for file in files:
                if len(file) > 0 and not os.path.isfile(file):
                    msg += "  File not found:" + file + "\n"
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)
