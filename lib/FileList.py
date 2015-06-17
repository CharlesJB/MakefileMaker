#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-08

import sys
import os

class FileList:
    def __init__(self, file_list):
        self.file_list = file_list
        self._valid()

    def get_file_count(self):
        return(len(self.file_list))

    def get_paired_status(self):
        if len(self.file_list[0][1]) == 0:
            return(False)
        else:
            return(True)

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

    def unlist(self, dir_name = None, suffix = None):
        if not dir_name is None:
            if not isinstance(dir_name, basestring) or len(dir_name) < 1:
                msg = "unlist: dir_name must be None of a basetring of len > 0."
                sys.stderr.write(msg)
                sys.exit(1)
        if not suffix is None:
            if not isinstance(suffix, basestring) or len(suffix) < 1:
                msg = "unlist: suffix must be None of a basetring of len > 0."
                sys.stderr.write(msg)
                sys.exit(1)
        files = []
        for file_list in self.file_list:
            file1 = file_list[0]
            if not dir_name is None:
                file1 = dir_name + "/" + file1
            if not suffix is None:
                file1 = file1 + suffix
            files.append(file1)
            file2 = file_list[1]
            if len(file2) > 0:
                if not dir_name is None:
                    file2 = dir_name + "/" + file2
                if not suffix is None:
                    file2 = file2 + suffix
                files.append(file2)
        return(files)

    def split(self, merge, pair):
        results = []
        if not merge and not pair:
            for file_name in self.unlist():
                results.append(FileList([[file_name, '']]))
        elif merge and not pair:
            files_R1 = self._unlist_file(0)
            files_R2 = self._unlist_file(1)
            r1 = []
            for file_name in files_R1:
                r1.append([file_name, ''])
            results.append(FileList(r1))
            if len(files_R2) > 0:
                r2 = []
                for file_name in files_R2:
                    r2.append([file_name, ''])
                results.append(FileList(r2))
        elif not merge and pair:
            for file_list in self.file_list:
                results.append(FileList([[file_list[0], file_list[1]]]))
        else:
            results = [self]
        return(results)

    def _unlist_file(self, idx):
        files = []
        for file_list in self.file_list:
            if len(file_list[idx]) > 0:
                files.append(file_list[idx])
        return(files)

    def _valid(self):
        correct = True
        msg = ""
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
