#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-01

import sys
import os

class FileList:
	def __init__(self, file_list):
		self._validate_file_list(file_list)
		self.file_list = file_list

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

	def _validate_file_list(self, file_list):
		correct = True
		msg = ""
		if not isinstance(file_list, list):
			msg += "FileList: file_list param should be a list.\n"
			correct = False
		else:
			if len(file_list) < 1:
				msg += "FileList: file_list does not contain entry.\n"
				correct = False
			else:
				for key in file_list:
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

class Step:
	def __init__(self, name, dir, dependencies, outputs, pair_data = False, merge_data = False):
		self.params = {}
		self.params["name"] = name
		self.params["dir"] = dir
		self.params["pair_data"] = pair_data
		self.params["merge_data"] = merge_data

		self.dependencies = dependencies
		self.outputs = outputs

		self._valid()

	def get_name(self):
		return(self.params["name"])

	def get_dir(self):
		return(self.params["dir"])

	def get_dependencies(self):
		return(self.dependencies)

	def get_outputs(self):
		return(self.outputs)

	def _valid(self):
		error = False
		msg = ""
		if not isinstance(self.params["name"], basestring):
			msg += "Step: param \"name\" not a basestring.\n"
			error = True
		elif len(self.params["name"]) < 1:
			msg += "Step: param \"name\" must be at least one char long.\n"
			error = True
		if not isinstance(self.params["dir"], basestring):
			msg += "Step: param \"dir\" not a basestring.\n"
			error = True
		elif len(self.params["dir"]) < 1:
			msg += "Step: param \"dir\" must be at least one char long.\n"
			error = True
		if not isinstance(self.dependencies, list):
			msg += "Step: param \"dependencies\" should be a list.\n"
			error = True
		elif len(self.dependencies) < 1:
			msg += "Step: param \"dependencies\" should contains at least one FileList.\n"
			error = True
		else:
			for dependency in self.dependencies:
				if not isinstance(dependency, FileList):
					msg += "Step: param \"dependencies\" entries should be FileList.\n"
					error = True
		if not isinstance(self.outputs, list):
			msg += "Step: param \"outputs\" should be a list.\n"
			error = True
		elif len(self.outputs) < 1:
			msg += "Step: param \"outputs\" should contains at least one FileList.\n"
			error = True
		else:
			for output in self.outputs:
				if not isinstance(output, FileList):
					msg += "Step: param \"outputs\" entries should be FileList.\n"
					error = True
		if not isinstance(self.params["pair_data"], bool):
			msg += "Step: param \"pair_data\" not a basestring.\n"
			error = True
		if not isinstance(self.params["merge_data"], bool):
			msg += "Step: param \"merge_data\" not a basestring.\n"
			error = True
		if error == True:
			sys.stderr.write(msg)
			sys.exit(1)

