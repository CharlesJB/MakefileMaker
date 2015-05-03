#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-01

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
			del(files[1])
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

import sys
import os

# Tests
if __name__ == "__main__":
	test_count = 0
	fail_count = 0
	error_messages = "Failed tests: \n"

	class NullWriter:
		def write(self, s):
			pass
	sys.stderr = NullWriter()

	##############################
	print("")
	print("Starting unit tests for class: FileList")
	print("")

	valid_file_list = [['a','b'],['c','d']]
	valid_file_list_empty2 = [['a','b'],['c','']]

	###############
	test_name = "Constructor - valid params"
	try:
		fl = FileList(valid_file_list)
		print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - valid params empty key value 2"
	try:
		fl = FileList(valid_file_list_empty2)
		print(test_name + "\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid file_list type"
	try:
		fl = FileList(1)
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		fail_count += 1
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid empty file_list"
	try:
		fl = FileList([])
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		fail_count += 1
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid empty file_list key"
	try:
		fl = FileList([['a','b'],[]])
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		fail_count += 1
		print(test_name + "\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid file_list key length"
	try:
		fl = FileList([['a','b'],['c']])
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		fail_count += 1
		print(test_name + "\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid file_list key type"
	try:
		fl = FileList([['a','b'],['c',1]])
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		fail_count += 1
		print(test_name + "\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid file_list key value 1 length"
	try:
		fl = FileList([['a','b'],['','d']])
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		fail_count += 1
		print(test_name + "\t[FAIL]")
	except SystemExit:
		print(test_name + "\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t[FAIL]")
	test_count += 1

	###############
	test_name = "get_files - valid index 2 files"
	try:
		fl = FileList(valid_file_list_empty2)
		files = fl.get_files(0)
		if len(files) != 2:
			fail_count += 1
			msg = test_name + ":\tIncorrect files length.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t[FAIL]")
		elif files[0] != 'a':
			fail_count += 1
			msg = test_name + ":\tIncorrect files[0] value.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t[FAIL]")
		elif files[1] != 'b':
			fail_count += 1
			msg = test_name + ":\tIncorrect files[1] value.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t[FAIL]")
		else:
			print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "get_files - valid index 1 file"
	try:
		fl = FileList(valid_file_list_empty2)
		files = fl.get_files(1)
		if len(files) != 1:
			fail_count += 1
			msg = test_name + ":\tIncorrect files length.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t[FAIL]")
		elif files[0] != 'c':
			fail_count += 1
			msg = test_name + ":\tIncorrect files[1] value.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t[FAIL]")
		else:
			print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "get_files - invalid index"
	try:
		fl = FileList(valid_file_list)
		files = fl.get_files(2)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

	##############################
	print("")
	print("Starting unit tests for class: Step")
	print("")

	valid_name = "valid_name"
	valid_dir = "valid_dir"
	valid_dependencies = [FileList([['a','b'],['c','d']])]
	valid_outputs = [FileList([['e','f'],['g','h']])]
	valid_pair = True
	valid_merge = False

	###############
	test_name = "Constructor - valid params"
	try:
		step = Step(valid_name, valid_dir, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

#	except Exception,e:
#		print(e)

	###############
	test_name = "Constructor - invalid name type"
	try:
		Step(1, valid_dir, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid name length"
	try:
		Step("", valid_dir, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid dir type"
	try:
		Step(valid_name, 1, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid dir length"
	try:
		Step(valid_name, "", valid_dependencies, valid_outputs, valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid dependencies type"
	try:
		Step(valid_name, valid_dir, "", valid_outputs, valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid empty dependencies"
	try:
		Step(valid_name, valid_dir, [], valid_outputs, valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid dependencies key type"
	try:
		Step(valid_name, valid_dir, [FileList([['a','b'],['c','d']]),3], valid_outputs, valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t[FAIL]")
	test_count += 1


	###############
	test_name = "Constructor - invalid outputs type"
	try:
		Step(valid_name, valid_dir, valid_dependencies, "", valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid empty outputs"
	try:
		Step(valid_name, valid_dir, valid_dependencies, [], valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid outputs key type"
	try:
		Step(valid_name, valid_dir, valid_dependencies, [FileList([['a','b'],['c','d']]),3], valid_pair, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid pair type"
	try:
		Step(valid_name, valid_dir, valid_dependencies, valid_outputs, 1, valid_merge)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "Constructor - invalid merge type"
	try:
		Step(valid_name, valid_dir, valid_dependencies, valid_outputs, valid_pair, 1)
		fail_count += 1
		msg = test_name + ":\tShould have raised an error.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	except SystemExit:
		print(test_name + "\t\t\t[OK]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised, but not SystemExit.\n"
		error_messages += msg
		print(test_name + "\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "get_name"
	try:
		step = Step(valid_name, valid_dir, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		if step.get_name() == valid_name:
			print(test_name + "\t\t\t\t\t\t[OK]")
		else:
			fail_count += 1
			msg = test_name + ":\tIncorrect name returned.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t\t\t[FAIL]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "get_dir"
	try:
		step = Step(valid_name, valid_dir, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		if step.get_dir() == valid_dir:
			print(test_name + "\t\t\t\t\t\t\t[OK]")
		else:
			fail_count += 1
			msg = test_name + ":\tIncorrect dir returned.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t\t\t\t[FAIL]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "get_dependencies"
	try:
		step = Step(valid_name, valid_dir, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		if step.get_dependencies() == valid_dependencies:
			print(test_name + "\t\t\t\t\t[OK]")
		else:
			fail_count += 1
			msg = test_name + ":\tIncorrect dependencies returned.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t\t[FAIL]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t\t[FAIL]")
	test_count += 1

	###############
	test_name = "get_outputs"
	try:
		step = Step(valid_name, valid_dir, valid_dependencies, valid_outputs, valid_pair, valid_merge)
		if step.get_outputs() == valid_outputs:
			print(test_name + "\t\t\t\t\t\t[OK]")
		else:
			fail_count += 1
			msg = test_name + ":\tIncorrect output returned.\n"
			error_messages += msg
			print(test_name + "\t\t\t\t\t\t[FAIL]")
	except:
		fail_count += 1
		msg = test_name + ":\tError raised.\n"
		error_messages += msg
		print(test_name + "\t\t\t\t\t\t[FAIL]")
	test_count += 1

	###############
	print("")
	if fail_count > 0:
		print(" [" + str(fail_count) + " of " + str(test_count) + "] test(s) failed.")
		print("")
		print(error_messages)
	else:
		print(" [" + str(test_count) + "] tests worked correctly.")
	print("")
