#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-08

import sys
import os

#from lib.FileList import *
from lib.SampleManager import *
from lib.DesignManager import *

# 4 letter code to represent the IO status of current step:
# merged: sample was merged on a previous step
# paired: sample was paired on a previous step
# merge: sample will be merged in current step
# pair: sample will be paired in current step
## merged/paired/merge/pair
## FFFF
## FFFT
## FFTF
## FTFF
## TFFF
## FFTT
## TFFT
## FTTF
## TTFF

# code count_status/pair_status of the raw data for a sample:
# count_status refers to files that are splitted (i.e.: on multiple lane)
# pair_status refers to paired files (paired_end sequencing)
## C2PT: 2 or more files , paired
## C2PF: 2 or more files, not paired
## C1PT: 1 file, paired
## C1PF: 1 file, not paired

class IOManager:
    def __init__(self, sample_sheet, design_file = None):
        self.sample_manager = SampleManager(sample_sheet)
        self.design_manager = None
        if design_file is not None:
            self.design_manager = DesignManager(design_file)
        self.raw_files = self.sample_manager.get_raw_files()
        self._validate_raw_files()

    # TODO: Unit tests
    def generate_inputs_raw_data(self, merge, pair):
        raw_files = []
        for file_list in self.raw_files.values():
            for file_name in file_list.split(merge, pair):
                raw_files.append([file_name])
        return(raw_files)

    def generate_inputs(self, merged, paired, merge, pair):
        inputs = []
        for name in self.raw_files.keys():
            for inpt in self._generate_input(name, merged, paired, merge, pair):
                inputs.append([inpt])
        return(inputs)

    def generate_outputs(self, merged, paired, merge, pair):
        outputs = []
        for name in self.raw_files.keys():
            outputs += self._generate_output(name, merged, paired, merge, pair)
        return(outputs)

    def generate_outputs_pair(self, merged, paired, merge, pair):
        outputs = []
        for name in self.raw_files.keys():
            outputs += self._generate_input(name, merged, paired, merge, True)
        return(outputs)

    def generate_inputs_design(self):
        if self.design_manager is not None:
            inputs = []
            for design_name in self.design_manager.get_design_names():
                inputs.append(self._generate_input_design(design_name))
            return(inputs)
        return(None)

    def generate_outputs_design(self):
        if self.design_manager is not None:
            outputs = []
            for design_name in self.design_manager.get_design_names():
                outputs.append(FileList([[design_name, '']]))
            return(outputs)
        return(None)

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

    def _validate_raw_files(self):
        error = False
        msg = ""
        if not isinstance(self.raw_files, dict):
            msg += "IOManager, _valid: raw_files should be a dict.\n"
            error = True
        elif len(self.raw_files) < 1:
            msg += "IOManager, _valid: raw_files should have at least 1 FileList.\n"
            error = True
        else:
            for file_list in self.raw_files.values():
                if not isinstance(file_list, FileList):
                    msg += "IOManager, _valid: raw_files entries should be FileList.\n"
                    error = True
        if error == True:
            sys.stderr.write(msg)
            sys.exit(1)

    def _generate_input_design(self, design_name):
        inpt = []
        dm = self.design_manager
        for group in self.design_manager.get_groups(design_name):
            group_names = dm.get_group_names(design_name, group)
            file_list = []
            for name in group_names:
                file_list.append([name, ''])
            inpt.append(FileList(file_list))
        return(inpt)

    def _generate_input(self, name, merged, paired, merge, pair):
        if name not in self.raw_files:
            msg = "_generate_input: invalid name"
            sys.stderr.write(msg)
            sys.exit(1)

        if paired and pair or merged and merge:
            msg = "_generate_input: invalid combination of arguments."
            sys.stderr.write(msg)
            sys.exit(1)

        results = []
        paired_status = self.raw_files[name].get_paired_status()
        count = self.raw_files[name].get_file_count()

        # C2PT
        if count > 1 and paired_status:
            # FFFF
            if not merged and not paired and not merge and not pair:
                for i in range(1, count + 1):
                    file_R1 = name + "_" + str(i) + "_R1"
                    file_R2 = name + "_" + str(i) + "_R2"
                    file_list_R1 = FileList([[file_R1, '']])
                    file_list_R2 = FileList([[file_R2, '']])
                    results.append(file_list_R1)
                    results.append(file_list_R2)
            # FFFT
            elif not merged and not paired and not merge and pair:
                for i in range(1, count + 1):
                    file_R1 = name + "_" + str(i) + "_R1"
                    file_R2 = name + "_" + str(i) + "_R2"
                    file_list = FileList([[file_R1, file_R2]])
                    results.append(file_list)
            # FFTF
            elif not merged and not paired and merge and not pair:
                files_R1 = []
                files_R2 = []
                for i in range(1, count + 1):
                    files_R1.append([name + "_" + str(i) + "_R1", ''])
                    files_R2.append([name + "_" + str(i) + "_R2", ''])
                file_list_R1 = FileList(files_R1)
                file_list_R2 = FileList(files_R2)
                results.append(file_list_R1)
                results.append(file_list_R2)
            # FTFF
            elif not merged and paired and not merge and not pair:
                for i in range(1, count + 1):
                    file_1 = name+ "_" + str(i)
                    file_list = FileList([[file_1, '']])
                    results.append(file_list)
            # TFFF
            elif merged and not paired and not merge and not pair:
                file_R1 = name + "_R1"
                file_R2 = name + "_R2"
                file_list_R1 = FileList([[file_R1, '']])
                file_list_R2 = FileList([[file_R2, '']])
                results.append(file_list_R1)
                results.append(file_list_R2)
            # FFTT
            elif not merged and not paired and merge and pair:
                files = []
                for i in range(1, count + 1):
                    file_R1 = name + "_" + str(i) + "_R1"
                    file_R2 = name + "_" + str(i) + "_R2"
                    files.append([file_R1, file_R2])
                file_list = FileList(files)
                results.append(file_list)
            # TFFT
            elif merged and not paired and not merge and pair:
                file_R1 = name + "_R1"
                file_R2 = name + "_R2"
                file_list = FileList([[file_R1, file_R2]])
                results.append(file_list)
            # FTTF
            elif not merged and paired and merge and not pair:
                files = []
                for i in range(1, count + 1):
                    file_1 = name+ "_" + str(i)
                    files.append([file_1, ''])
                file_list = FileList(files)
                results.append(file_list)
            # TTFF
            elif merged and paired and not merge and not pair:
                file_1 = name
                file_list = FileList([[file_1, '']])
                results.append(file_list)

        # C2PF
        elif count > 1 and not paired_status:
            # FFFF & FFFT & FTFF
            if not merged and not merge:
                for i in range(1, count + 1):
                    file_1 = name+ "_" + str(i)
                    file_list = FileList([[file_1, '']])
                    results.append(file_list)
            # FFTF & FFTT & FTTF
            elif not merged and merge:
                files = []
                for i in range(1, count + 1):
                    file_1 = name+ "_" + str(i)
                    files.append([file_1, ''])
                file_list = FileList(files)
                results.append(file_list)
            # TFFF & TFFT & TTFF
            elif merged and not merge:
                file_1 = name
                file_list = FileList([[file_1, '']])
                results.append(file_list)

        # C1PT
        elif count == 1 and paired_status:
            # FFFF & FFTF & TFFF
            if not paired and not pair:
                file_R1 = name + "_R1"
                file_R2 = name + "_R2"
                file_list_R1 = FileList([[file_R1, '']])
                file_list_R2 = FileList([[file_R2, '']])
                results.append(file_list_R1)
                results.append(file_list_R2)
            # FFFT & FFTT & TFFT
            elif not paired and pair:
                file_R1 = name + "_R1"
                file_R2 = name + "_R2"
                file_list = FileList([[file_R1, file_R2]])
                results.append(file_list)
            # FTFF & FTTF & TTFF
            elif paired and not pair:
                file_1 = name
                file_list = FileList([[file_1, '']])
                results.append(file_list)

        # C1PF
        elif count == 1 and not paired_status:
            file_1 = name
            file_list = FileList([[file_1, '']])
            results.append(file_list)

        return(results)


    def _generate_output(self, name, merged, paired, merge, pair):
        if name not in self.raw_files:
            msg = "_generate_output: invalid name"
            sys.stderr.write(msg)
            sys.exit(1)

        if paired and pair or merged and merge:
            msg = "_generate_output: invalid combination of arguments."
            sys.stderr.write(msg)
            sys.exit(1)

        results = []
        paired_status = self.raw_files[name].get_paired_status()
        count = self.raw_files[name].get_file_count()

        to_merge = merged or merge
        to_pair = paired or pair

        # C2PT
        if count > 1 and paired_status:
            # FFFF
            if not to_merge and not to_pair:
                for i in range(1, count + 1):
                    file_R1 = name + "_" + str(i) + "_R1"
                    file_R2 = name + "_" + str(i) + "_R2"
                    file_list_R1 = FileList([[file_R1, '']])
                    file_list_R2 = FileList([[file_R2, '']])
                    results.append(file_list_R1)
                    results.append(file_list_R2)

            # FFFT & FTFF
            elif not to_merge and to_pair:
                files = []
                for i in range(1, count + 1):
                    file_1 = name+ "_" + str(i)
                    file_list = FileList([[file_1, '']])
                    results.append(file_list)

            # FFTF & TFFF
            elif to_merge and not to_pair:
                file_R1 = name + "_R1"
                file_R2 = name + "_R2"
                file_list_R1 = FileList([[file_R1, '']])
                file_list_R2 = FileList([[file_R2, '']])
                results.append(file_list_R1)
                results.append(file_list_R2)

            # FFTT & TFFT & FTTF & TTFF
            elif to_merge and to_pair:
                file_1 = name
                file_list = FileList([[file_1, '']])
                results.append(file_list)

        # C2PF
        if count > 1 and not paired_status:
            # FFFF & FFFT & FTFF
            if not to_merge:
                for i in range(1, count + 1):
                    file = name + "_" + str(i)
                    file_list = FileList([[file, '']])
                    results.append(file_list)

            # FFTF & TFFF & FFTT & TFFT & FTTF & TTFF
            elif to_merge:
                file_1 = name
                file_list = FileList([[file_1, '']])
                results.append(file_list)

        # C1PT
        if count == 1 and paired_status:
            # FFFF & FFTF & TFFF
            if not to_pair:
                file_R1 = name + "_R1"
                file_R2 = name + "_R2"
                file_list_R1 = FileList([[file_R1, '']])
                file_list_R2 = FileList([[file_R2, '']])
                results.append(file_list_R1)
                results.append(file_list_R2)

            # FFFT & FTFF & FFTT & TFFT & FTTF & TTFF
            elif to_pair:
                file_1 = name
                file_list = FileList([[file_1, '']])
                results.append(file_list)

        # C1PF
        elif count == 1 and not paired_status:
            file_1 = name
            file_list = FileList([[file_1, '']])
            results.append(file_list)

        return(results)
