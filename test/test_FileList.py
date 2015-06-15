from nose.tools import *
from lib.FileList import *

class NullWriter:
    def write(self, s):
        pass
sys.stderr = NullWriter()

# TESTS: FileList

VALID_NAME = "valid_name"
VALID_FILELIST_FULL = [['a','b'],['c','d']]
# TODO: the next one should be invalid
VALID_FILELIST_EMPTY_KEY_2 = [['a','b'],['c','']]
INVALID_FILELIST_EMPTY = []
INVALID_FILELIST_NO_KEYS = [['a','b'],[]]
INVALID_FILELIST_EMPTY_KEY_1 = [['a','b'],['','d']]
INVALID_FILELIST_KEY_LENGTH = [['a','b'],['c']]
INVALID_FILELIST_KEY_TYPE = [['a','b'],['c', 1]]

def test_filelist_constructor_valid_params():
    fl = FileList(VALID_FILELIST_FULL)
    eq_(fl.file_list, VALID_FILELIST_FULL)

def test_filelist_constructor_valid_params_empty_2():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2)
    eq_(fl.file_list, VALID_FILELIST_EMPTY_KEY_2)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_type():
    FileList(1)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_empty():
    FileList(INVALID_FILELIST_EMPTY)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_no_keys():
    FileList(INVALID_FILELIST_NO_KEYS)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_empty_key_1():
    FileList(INVALID_FILELIST_EMPTY_KEY_1)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_key_length():
    FileList(INVALID_FILELIST_KEY_LENGTH)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_key_type():
    FileList(INVALID_FILELIST_KEY_TYPE)

def test_filelist_get_files_valid_index_two_file():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2)
    files = fl.get_files(0)
    eq_(files, VALID_FILELIST_EMPTY_KEY_2[0])

def test_filelist_get_files_valid_index_one_file():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2)
    files = fl.get_files(1)
    eq_(files, ['c'])

@raises(SystemExit)
def test_filelist_get_files_invalid_index():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2)
    fl.get_files(2)

def test_filelist_unlist_full():
    fl = FileList(VALID_FILELIST_FULL)
    eq_(fl.unlist(), ['a','b','c','d'])

def test_filelist_unlist_partial():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2)
    eq_(fl.unlist(), ['a','b','c'])