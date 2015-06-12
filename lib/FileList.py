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

    def unlist(self):
        files = []
        for file_list in self.file_list:
            files.append(file_list[0])
            if len(file_list[1]) > 0:
                files.append(file_list[1])
        return(files)

    # TODO: Unit Tests
    def unlist_file1(self):
        return(self._unlist_file(0))

    def unlist_file2(self):
        return(self._unlist_file(1))

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
