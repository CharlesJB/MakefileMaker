from nose.tools import *
from lib.StepManager import *
from lib.SampleManager import *

class NullWriter:
    def write(self, s):
        pass
sys.stderr = NullWriter()

# TESTS: StepInfos

VALID_STEP_NAME = "valid_step_name"
VALID_NAME = "valid_name"
VALID_DIR_NAME = "valid_dir_name"
VALID_DEPENDENCIES = [FileList([['a','b'],['c','d']], VALID_NAME)]
VALID_OUTPUTS = [FileList([['e','f'],['g','h']], VALID_NAME)]
VALID_PAIR = True
VALID_MERGE = False

def test_step_infos_constructor_valid_params():
    ok_(StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE))

@raises(SystemExit)
def test_step_infos_constructor_invalid_step_name_type():
    StepInfos(1, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_step_name_length():
    StepInfos("", VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_dir_name_type():
    StepInfos(VALID_STEP_NAME, 1, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    
@raises(SystemExit)
def test_step_infos_constructor_invalid_dir_name_length():
    StepInfos(VALID_STEP_NAME,  "", VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_dependencies_type():
    StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, 1, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_empty_dependencies():
    StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, [], VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_outputs_type():
    StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, 1, VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_empty_outputs():
    StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, [], VALID_PAIR, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_pair_type():
    StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, 1, VALID_MERGE)

@raises(SystemExit)
def test_step_infos_constructor_invalid_merge_type():
    StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, 1)

def test_step_infos_get_step_name():
    step = StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_step_name(), VALID_STEP_NAME)

def test_step_infos_get_dir_name():
    step = StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_dir_name(), VALID_DIR_NAME)

def test_step_infos_get_dependencies():
    step = StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_dependencies(), VALID_DEPENDENCIES)

def test_step_infos_get_outputs():
    step = StepInfos(VALID_STEP_NAME, VALID_DIR_NAME, VALID_DEPENDENCIES, VALID_OUTPUTS, VALID_PAIR, VALID_MERGE)
    eq_(step.get_outputs(), VALID_OUTPUTS)


# TESTS: StepManager

VALID_STEP_NAME_1 = "valid_step_name_1"
VALID_STEP_NAME_2 = "valid_step_name_2"
VALID_DIR_NAME = "valid_dir_name"
VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_SAMPLE_MANAGER = SampleManager(VALID_SAMPLESHEET)
VALID_PAIR_TRUE = True
VALID_PAIR_FALSE = False
VALID_MERGE_TRUE = True
VALID_MERGE_FALSE = False

def test_step_infos_manager_constructor_valid_params():
    sm = StepManager(VALID_SAMPLE_MANAGER)
    eq_(sm.steps, [])
    eq_(sm.step_names, [])
    eq_(isinstance(sm.sample_manager, SampleManager), True)
