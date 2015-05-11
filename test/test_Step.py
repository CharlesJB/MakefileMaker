from nose.tools import *
from lib.Step import *
from lib.FileList import *

VALID_CONFIG_FILE_1 = "raw_data/valid_dummy_1.ini"
VALID_CONFIG_FILE_2 = "raw_data/valid_dummy_2.ini"
DUMMY_PARAM_1_1 = 'dummy_param_1'
DUMMY_PARAM_2_1 = 'dummy_param_2'
DUMMY_PARAM_1_2 = 'dummy_param_3'
DUMMY_PARAM_2_2 = 'dummy_param_4'

FILE_1_R1 = 'dependency_1_R1'
FILE_1_R2 = 'dependency_1_R2'
VALID_DEPENDENCY_NAME_1 = 'dependency_name_1'
VALID_DEPENDENCIES_PAIRED = {}
VALID_FILE_LIST_1 = FileList([[FILE_1_R1, FILE_1_R2]], VALID_DEPENDENCY_NAME_1)
VALID_DEPENDENCIES_PAIRED[VALID_DEPENDENCY_NAME_1] = VALID_FILE_LIST_1

VALID_OUTPUTS_1 = ['valid_output_1']

EXP_RECIPE_1 = VALID_OUTPUTS_1[0] + ": "
EXP_RECIPE_1 += FILE_1_R1 + " "
EXP_RECIPE_1 += FILE_1_R2 + "\n"
EXP_RECIPE_1 += "\t@echo $@\n"
EXP_RECIPE_1 += "\t@echo $^\n"

def test_dummy_step_constructor():
    ds = DummyStep()
    eq_(ds.name, "DummyStep")
    eq_(isinstance(ds.params, dict), True)
    eq_(len(ds.params), 2)
    eq_(ds.params['param1'], 1)
    eq_(ds.params['param2'], 2)
    eq_(ds.dependency_names, [VALID_DEPENDENCY_NAME_1])
    eq_(ds.config_files, [])

def test_dummy_step_get_name():
    ds = DummyStep()
    eq_(ds.get_name(), "DummyStep")

def test_dummy_step_add_config_file():
    ds = DummyStep()
    eq_(ds.config_files, [])
    ds.add_config_file(VALID_CONFIG_FILE_1)
    eq_(ds.config_files, [VALID_CONFIG_FILE_1])
    ds.add_config_file(VALID_CONFIG_FILE_2)
    eq_(ds.config_files, [VALID_CONFIG_FILE_1, VALID_CONFIG_FILE_2])

def test_dummy_produce_recipe_valid_params():
    ds = DummyStep()
    recipe = ds.produce_recipe(VALID_DEPENDENCIES_PAIRED, VALID_OUTPUTS_1)
    eq_(recipe, EXP_RECIPE_1)
