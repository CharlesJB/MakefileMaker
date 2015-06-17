from nose.tools import *
from lib.Step import *
from lib.FileList import *

VALID_CONFIG_FILE_1 = "raw_data/valid_dummy_1.ini"
VALID_CONFIG_FILE_2 = "raw_data/valid_dummy_2.ini"

FILE_1_R1 = '1_R1'
FILE_1_R2 = '1_R2'
FILE_2_R1 = '2_R1'
FILE_2_R2 = '2_R2'
FILE_LIST_UNPAIRED_1 = FileList([[FILE_1_R1, '']])
FILE_LIST_PAIRED_1 = FileList([[FILE_1_R1, FILE_1_R2]])
FILE_LIST_PAIRED_2 = FileList([[FILE_2_R1, FILE_2_R2]])
FILE_LIST_2_FILES = FileList([[FILE_1_R1, ''], [FILE_2_R1, '']])

def test_dummy_step_constructor():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    eq_(ds.name, "DummyStep")
    eq_(isinstance(ds.params, dict), True)
    eq_(len(ds.params), 2)
    eq_(ds.params['dummy_param_1'], 'dummy_param_1_1')
    eq_(ds.params['dummy_param_2'], 'dummy_param_1_2')
    eq_(ds.config_files, [VALID_CONFIG_FILE_1])

def test_dummy_step_constructor_2_config_files():
    ds = DummyStep([VALID_CONFIG_FILE_1, VALID_CONFIG_FILE_2])
    eq_(ds.name, "DummyStep")
    eq_(isinstance(ds.params, dict), True)
    eq_(len(ds.params), 2)
    eq_(ds.params['dummy_param_1'], 'dummy_param_2_1')
    eq_(ds.params['dummy_param_2'], 'dummy_param_2_2')
    eq_(ds.config_files, [VALID_CONFIG_FILE_1, VALID_CONFIG_FILE_2])

def test_dummy_step_constructor_no_config_files():
    ds = DummyStep([])
    eq_(ds.name, "DummyStep")
    eq_(isinstance(ds.params, dict), True)
    eq_(len(ds.params), 2)
    eq_(ds.params['dummy_param_1'], 'dummy_param_default_1')
    eq_(ds.params['dummy_param_2'], 'dummy_param_default_2')
    eq_(ds.config_files, [])

@raises(SystemExit)
def test_dummy_step_constructor_invalid_config_file():
    DummyStep(VALID_CONFIG_FILE_1)

def test_dummy_step_get_name():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    eq_(ds.get_name(), "DummyStep")

def test_dummy_step_get_dir_name():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    eq_(ds.get_dir_name(), "Dummy")

def test_dummy_step_get_pair_status():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    eq_(ds.get_pair_status(), True)

def test_dummy_step_get_merge_status():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    eq_(ds.get_merge_status(), True)

def test_dummy_step_get_keep_pair_together_status():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    eq_(ds.get_keep_pair_together_status(), False)

def test_dummy_step_get_step_specific_variables():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    eq_(ds.get_step_specific_variables(), "ABC=DEF")

def test_dummy_step_produce_recipe():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    recipe = ds.produce_recipe(FILE_LIST_PAIRED_2, FILE_LIST_UNPAIRED_1)
    eq_(recipe, 'Dummy/1_R1.txt: 2_R1 2_R2\n\t@echo $@\n\t@echo $^\n')

def test_dummy_step_produce_recipe_empty_input():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    recipe = ds.produce_recipe(None, FILE_LIST_UNPAIRED_1)
    eq_(recipe, 'Dummy/1_R1.txt:\n\t@echo $@\n\t@echo $^\n')

@raises(SystemExit)
def test_dummy_step_produce_recipe_invalid_input_length():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    recipe = ds.produce_recipe(FILE_LIST_PAIRED_1, FILE_LIST_2_FILES)

@raises(SystemExit)
def test_dummy_step_produce_recipe_invalid_input_class():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    recipe = ds.produce_recipe([FILE_LIST_PAIRED_1], FILE_LIST_UNPAIRED_1)

@raises(SystemExit)
def test_dummy_step_produce_recipe_invalid_output_class():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    recipe = ds.produce_recipe(FILE_LIST_PAIRED_1, [FILE_LIST_UNPAIRED_1])

@raises(SystemExit)
def test_dummy_step_produce_recipe_invalid_output_merge():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    recipe = ds.produce_recipe(FILE_LIST_PAIRED_1, FILE_LIST_2_FILES)

@raises(SystemExit)
def test_dummy_step_produce_recipe_invalid_output_pair():
    ds = DummyStep([VALID_CONFIG_FILE_1])
    recipe = ds.produce_recipe(FILE_LIST_PAIRED_1, FILE_LIST_PAIRED_1)
