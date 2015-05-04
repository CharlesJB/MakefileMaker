from nose.tools import *
from lib.StepManager import *

class NullWriter:
    def write(self, s):
        pass
sys.stderr = NullWriter()

# TESTS: FileList

VALID_FILELIST_FULL = [['a','b'],['c','d']]
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

# TESTS: Step

VALID_NAME = "valid_name"
VALID_DIR = "valid_dir"
VALID_DEPENDENCIES = [FileList([['a','b'],['c','d']])]
VALID_OUTPUTS = [FileList([['e','f'],['g','h']])]
VALID_PAIR = True
VALID_MERGE = False

def test_step_constructor_valid_params():
    ok_(Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE))

@raises(SystemExit)
def test_step_constructor_invalid_name_type():
    Step(1, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_name_length():
    Step("", VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_dir_type():
    Step(VALID_NAME, 1, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    
@raises(SystemExit)
def test_step_constructor_invalid_dir_length():
    Step(VALID_NAME, "", VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_dependencies_type():
    Step(VALID_NAME, VALID_DIR, 1, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_empty_dependencies():
    Step(VALID_NAME, VALID_DIR, [], VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_outputs_type():
    Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, 1, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_empty_outputs():
    Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, [], VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_pair_type():
    Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, 1, VALID_MERGE)

@raises(SystemExit)
def test_step_constructor_invalid_merge_type():
    Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, 1)

def test_step_get_name():
    step = Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_name(), VALID_NAME)

def test_step_get_dir():
    step = Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_dir(), VALID_DIR)

def test_step_get_dependencies():
    step = Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_dependencies(), VALID_DEPENDENCIES)

def test_step_get_outputs():
    step = Step(VALID_NAME, VALID_DIR, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_outputs(), VALID_OUTPUTS)
