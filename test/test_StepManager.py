from nose.tools import *
from lib.StepManager import *
from lib.SampleManager import *

# Valid IOManager
VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
SAMPLE_MANAGER = SampleManager(VALID_SAMPLESHEET)
VALID_RAW_FILES = {}
VALID_RAW_FILES['test1'] = SAMPLE_MANAGER.get_file_list('test1')
VALID_RAW_FILES['test2'] = SAMPLE_MANAGER.get_file_list('test2')
IO_MANAGER = IOManager(VALID_RAW_FILES)

# Valid Steps
VALID_CONFIG_FILE = "raw_data/valid_dummy_1.ini"
# 1. merge
class TestStep1(Step):
    def get_step_specific_variables(self):
        return("ABC=DEF")
    def _set_step_specific_values(self):
        self.name = "Step1"
        self.merge_status = True
        self.pair_status = False
    def _get_command(self, dependencies, outputs):
        return("\ttouch $@")
    def _set_default_params(self):
        self.params['dir_name'] = "Step1"
        self.params['suffix'] = ".txt"
    def _validate_param_step_specific(self, inputs, outputs):
        pass

step1 = TestStep1([VALID_CONFIG_FILE])
# 2. pair
class TestStep2(Step):
    def _set_step_specific_values(self):
        self.name = "Step2"
        self.merge_status = False
        self.pair_status = True
    def _get_command(self, dependencies, outputs):
        return("\ttouch $@")
    def _set_default_params(self):
        self.params['dir_name'] = "Step2"
        self.params['suffix'] = ".csv"
    def _validate_param_step_specific(self, inputs, outputs):
        pass

step2 = TestStep2([VALID_CONFIG_FILE])

# TODO
# 3. depend 2
class TestStep3(Step):
    def get_step_specific_variables(self):
        return("")
    def _set_step_specific_values(self):
        self.name = "Step3"
        self.merge_status = False
        self.pair_status = False
    def _get_command(self, dependencies, outputs):
        return("\ttouch $@")
    def _set_default_params(self):
        self.params['dir_name'] = "Step3"
    def _validate_param_step_specific(self, inputs, outputs):
        pass

step3 = TestStep3([VALID_CONFIG_FILE])
# 4. Merge #2
class TestStep4(Step):
    def get_step_specific_variables(self):
        return("")
    def _set_step_specific_values(self):
        self.name = "Step4"
        self.merge_status = True
        self.pair_status = False
    def _get_command(self, dependencies, outputs):
        return("touch $@")
    def _set_default_params(self):
        self.params['dir_name'] = "Step4"
    def _validate_param_step_specific(self, inputs, outputs):
        pass

step4 = TestStep4([VALID_CONFIG_FILE])
# 5. Pair #2
class TestStep5(Step):
    def get_step_specific_variables(self):
        return("")
    def _set_step_specific_values(self):
        self.name = "Step5"
        self.merge_status = False
        self.pair_status = True
    def _get_command(self, dependencies, outputs):
        return("touch $@")
    def _set_default_params(self):
        self.params['dir_name'] = "Step5"
    def _validate_param_step_specific(self, inputs, outputs):
        pass

step5 = TestStep5([VALID_CONFIG_FILE])

def test_step_manager_constructor_valid_io():
    sm = StepManager(IO_MANAGER)
    eq_(sm.io_manager, IO_MANAGER)

@raises(SystemExit)
def test_step_manager_constructor_invalid_io():
    StepManager(1)

def test_step_manager_register_step():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, None)
    eq_(sm.steps["Step1"], step1)
    eq_(sm.dependencies["Step1"], None)

def test_step_manager_register_multiple_steps():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, None)
    sm.register_step(step2, "Step1")
    sm.register_step(step3, "Step2")
    eq_(sm.steps["Step1"], step1)
    eq_(sm.dependencies["Step1"], None)
    eq_(sm.steps["Step2"], step2)
    eq_(sm.dependencies["Step2"], "Step1")
    eq_(sm.steps["Step3"], step3)
    eq_(sm.dependencies["Step3"], "Step2")

def test_step_manager_register_same_step_multiple_time():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, None)
    sm.register_step(step1, None)
    eq_(sm.steps["Step1"], step1)
    eq_(sm.dependencies["Step1"], None)
    sm.register_step(step2, None)
    eq_(sm.steps["Step2"], step2)
    eq_(sm.dependencies["Step2"], None)
    sm.register_step(step2, "Step1")
    eq_(sm.steps["Step2"], step2)
    eq_(sm.dependencies["Step2"], "Step1")

@raises(SystemExit)
def test_step_manager_register_name_invalid_step_class():
    sm = StepManager(IO_MANAGER)
    sm.register_step("step1", None)

@raises(SystemExit)
def test_step_manager_register_name_invalid_dependency_class():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, ["a"])

@raises(SystemExit)
def test_step_manager_register_name_invalid_dependency_not_present():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step2, "Step1")

@raises(SystemExit)
def test_step_manager_register_name_invalid_already_merged():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, None)
    sm.register_step(step2, "Step1")
    sm.register_step(step4, "Step1")

@raises(SystemExit)
def test_step_manager_register_name_invalid_already_paired():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, None)
    sm.register_step(step2, "Step1")
    sm.register_step(step5, "Step2")

def test_step_manager_get_makefile_step_1():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, None)
    exp = '# Step specific variables\n'
    exp += 'STEP1_DIR_NAME=Step1\n'
    exp += 'ABC=DEF\n'
    exp += '\n'
    exp += '# Targets\n'
    exp += 'STEP1_TARGETS+=Step1/test1_R1.txt\n'
    exp += 'STEP1_TARGETS+=Step1/test1_R2.txt\n'
    exp += 'STEP1_TARGETS+=Step1/test2_R1.txt\n'
    exp += 'STEP1_TARGETS+=Step1/test2_R2.txt\n'
    exp += '\n'
    exp += '# Phony targets\n'
    exp += '.PHONY: Step1_dir Step1\n'
    exp += 'Step1_dir: $(STEP1_DIR_NAME)\n'
    exp += '\n'
    exp += 'Step1: $(STEP1_TARGETS)\n'
    exp += '\n'
    exp += '# Recipes\n'
    exp += 'Step1/test1_R1.txt:\n'
    exp += '\ttouch $@\n'
    exp += '\n'
    exp += 'Step1/test1_R2.txt:\n'
    exp += '\ttouch $@\n'
    exp += '\n'
    exp += 'Step1/test2_R1.txt:\n'
    exp += '\ttouch $@\n'
    exp += '\n'
    exp += 'Step1/test2_R2.txt:\n'
    exp += '\ttouch $@\n'
    exp += '\n'
    exp += 'Step1:\n'
    exp += '\tmkdir $@'
    eq_(sm.produce_makefile("Step1"), exp)

def test_step_manager_get_makefile_step_2():
    sm = StepManager(IO_MANAGER)
    sm.register_step(step1, None)
    sm.register_step(step2, "Step1")
    exp = '# Step specific variables\n'
    exp += 'STEP2_DIR_NAME=Step2\n'
    exp += '\n'
    exp += '# Targets\n'
    exp += 'STEP2_TARGETS+=Step2/test1.csv\n'
    exp += 'STEP2_TARGETS+=Step2/test2.csv\n'
    exp += '\n'
    exp += '# Phony targets\n'
    exp += '.PHONY: Step2_dir Step2\n'
    exp += 'Step2_dir: $(STEP2_DIR_NAME)\n'
    exp += '\n'
    exp += 'Step2: $(STEP2_TARGETS)\n'
    exp += '\n'
    exp += '# Recipes\n'
    exp += 'Step2/test1.csv: Step1/test1_R1.txt Step1/test1_R2.txt\n'
    exp += '\ttouch $@\n'
    exp += '\n'
    exp += 'Step2/test2.csv: Step1/test2_R1.txt Step1/test2_R2.txt\n'
    exp += '\ttouch $@\n'
    exp += '\n'
    exp += 'Step2:\n'
    exp += '\tmkdir $@'
    eq_(sm.produce_makefile("Step2"), exp)
