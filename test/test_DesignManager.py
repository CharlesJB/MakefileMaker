from nose.tools import *
from lib.DesignManager import *

class NullWriter:
    def write(self, s):
        pass
sys.stderr = NullWriter()

# TESTS: DesignManager

VALID_DESIGN_2_COLUMNS_1_GROUP = "raw_data/valid_design_2_columns_1_group.txt"
VALID_DESIGN_2_COLUMNS_2_GROUPS = "raw_data/valid_design_2_columns_2_groups.txt"
VALID_DESIGN_3_COLUMNS = "raw_data/valid_design_3_columns.txt"
INVALID_DESIGN_HEADER_LENGTH = "raw_data/invalid_design_header_length.txt"
INVALID_DESIGN_EXP_NAME_LENGTH = "raw_data/invalid_design_exp_name_length.txt"
INVALID_DESIGN_EXP_NAME_DUPLICATE = "raw_data/invalid_design_exp_name_duplicate.txt"
INVALID_DESIGN_LINE_LENGTH_TOO_SHORT = "raw_data/invalid_design_line_length_too_short.txt"
INVALID_DESIGN_LINE_LENGTH_TOO_LONG = "raw_data/invalid_design_line_length_too_long.txt"
INVALID_DESIGN_FILE_NAME_LENGTH = "raw_data/invalid_design_file_name_length.txt"
INVALID_DESIGN_FILE_NAME_DUPLICATE = "raw_data/invalid_design_file_name_duplicate.txt"
INVALID_DESIGN_GROUP_TYPE = "raw_data/invalid_design_group_type.txt"
INVALID_DESIGN_EMPTY_FILE = "raw_data/invalid_design_empty_file.txt"
INVALID_DESIGN_EMPTY_FILE = "raw_data/invalid_design_empty_file.txt"
INVALID_DESIGN_EXP_NO_GROUP = "raw_data/invalid_design_exp_no_group.txt"

def test_design_manager_constructor_valid_design_2_columns_1_group():
    dm = DesignManager(VALID_DESIGN_2_COLUMNS_1_GROUP)
    eq_(len(dm.exp_dict.keys()), 2)
    eq_("Exp1" in dm.exp_dict.keys(), True)
    eq_("Exp2" in dm.exp_dict.keys(), True)
    eq_(isinstance(dm.exp_dict["Exp1"], dict), True)
    eq_(isinstance(dm.exp_dict["Exp2"], dict), True)
    eq_(dm.exp_dict["Exp1"].keys(), [1])
    eq_(dm.exp_dict["Exp1"][1], ['test1'])
    eq_(dm.exp_dict["Exp2"].keys(), [1])
    eq_(dm.exp_dict["Exp2"][1], ['test2'])

def test_design_manager_constructor_valid_design_2_columns_2_group():
    dm = DesignManager(VALID_DESIGN_2_COLUMNS_2_GROUPS)
    eq_(len(dm.exp_dict.keys()), 2)
    eq_("Exp1" in dm.exp_dict.keys(), True)
    eq_("Exp2" in dm.exp_dict.keys(), True)
    eq_(isinstance(dm.exp_dict["Exp1"], dict), True)
    eq_(isinstance(dm.exp_dict["Exp2"], dict), True)
    eq_(dm.exp_dict["Exp1"].keys(), [1, 2])
    eq_(dm.exp_dict["Exp1"][1], ['test1'])
    eq_(dm.exp_dict["Exp1"][2], ['test2'])
    eq_(dm.exp_dict["Exp2"].keys(), [1, 2])
    eq_(dm.exp_dict["Exp2"][1], ['test2'])
    eq_(dm.exp_dict["Exp2"][2], ['test1'])

def test_design_manager_constructor_valid_design_3_columns():
    dm = DesignManager(VALID_DESIGN_3_COLUMNS)
    eq_(len(dm.exp_dict.keys()), 3)
    eq_("Exp1" in dm.exp_dict.keys(), True)
    eq_("Exp2" in dm.exp_dict.keys(), True)
    eq_("Exp3" in dm.exp_dict.keys(), True)
    eq_(isinstance(dm.exp_dict["Exp1"], dict), True)
    eq_(isinstance(dm.exp_dict["Exp2"], dict), True)
    eq_(isinstance(dm.exp_dict["Exp3"], dict), True)
    eq_(dm.exp_dict["Exp1"].keys(), [1])
    eq_(dm.exp_dict["Exp1"][1], ['test1'])
    eq_(dm.exp_dict["Exp2"].keys(), [1])
    eq_(dm.exp_dict["Exp2"][1], ['test2'])
    eq_(dm.exp_dict["Exp3"][1], ['test1'])
    eq_(dm.exp_dict["Exp3"][2], ['test2'])

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_header_length():
    DesignManager(INVALID_DESIGN_HEADER_LENGTH)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_exp_name_length():
    DesignManager(INVALID_DESIGN_EXP_NAME_LENGTH)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_exp_name_duplicate():
    DesignManager(INVALID_DESIGN_EXP_NAME_DUPLICATE)

#INVALID_DESIGN_FILE_NAME_LENGTH = "raw_data/invalid_design_file_name_length.txt"
#INVALID_DESIGN_FILE_NAME_DUPLICATE = "raw_data/invalid_design_file_name_duplicate.txt"
#INVALID_DESIGN_GROUP_TYPE = "raw_data/invalid_design_group_type.txt"
@raises(SystemExit)
def test_design_manager_constructor_invalid_design_line_length_too_short():
    DesignManager(INVALID_DESIGN_LINE_LENGTH_TOO_SHORT)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_line_length_too_long():
    DesignManager(INVALID_DESIGN_LINE_LENGTH_TOO_LONG)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_file_name_length():
    DesignManager(INVALID_DESIGN_FILE_NAME_LENGTH)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_file_name_duplicate():
    DesignManager(INVALID_DESIGN_FILE_NAME_DUPLICATE)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_group_type():
    DesignManager(INVALID_DESIGN_GROUP_TYPE)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_empty_file():
    DesignManager(INVALID_DESIGN_EMPTY_FILE)

@raises(SystemExit)
def test_design_manager_constructor_invalid_design_no_groups():
    DesignManager(INVALID_DESIGN_EXP_NO_GROUP)
