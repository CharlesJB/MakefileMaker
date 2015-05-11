#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-04-30

import sys
import os

from lib.FileList import *

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

    def get_file_list(self, name):
        if name not in self.raw_files_r1:
            return None
        else:
            fastq1 = self.raw_files_r1[name]
            fastq2 = self.raw_files_r2[name]
            file_list = []
            for i, _ in enumerate(fastq1):
                file_list.append([fastq1[i], fastq2[i]])
            return(FileList(file_list, name))

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
