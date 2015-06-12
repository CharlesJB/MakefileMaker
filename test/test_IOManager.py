from nose.tools import *
from lib.OutputManager import *
from lib.SampleManager import *

# constructor

VALID_NAME_1 = "test1"
VALID_NAME_2 = "test2"

VALID_SAMPLESHEET_FULL = "raw_data/valid_samplesheet.txt"
VALID_RAW_FILES_FULL = {}
VALID_RAW_FILES_FULL[VALID_NAME_1] = SampleManager(VALID_SAMPLESHEET_FULL).get_file_list(VALID_NAME_1)
VALID_RAW_FILES_FULL[VALID_NAME_2] = SampleManager(VALID_SAMPLESHEET_FULL).get_file_list(VALID_NAME_2)

EXP_FASTQ1_TEST1_FULL = 'raw_data/a1_1.fastq.gz'
EXP_FASTQ1_TEST2_FULL = 'raw_data/a2_1.fastq.gz'
EXP_FASTQ2_TEST1_FULL = 'raw_data/a1_2.fastq.gz'
EXP_FASTQ2_TEST2_FULL = 'raw_data/a2_2.fastq.gz'

VALID_SAMPLESHEET_NO_FASTQ2 = "raw_data/valid_samplesheet_no_fastq2.txt"
VALID_RAW_FILES_NO_FASTQ2 = {}
VALID_RAW_FILES_NO_FASTQ2[VALID_NAME_1] = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2).get_file_list(VALID_NAME_1)
VALID_RAW_FILES_NO_FASTQ2[VALID_NAME_2] = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2).get_file_list(VALID_NAME_2)

EXP_FASTQ1_TEST1_NO_FASTQ2 = EXP_FASTQ1_TEST1_FULL
EXP_FASTQ1_TEST2_NO_FASTQ2 = EXP_FASTQ1_TEST2_FULL
EXP_FASTQ2_TEST1_NO_FASTQ2 = ''
EXP_FASTQ2_TEST2_NO_FASTQ2 = ''

VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL = "raw_data/valid_samplesheet_no_fastq2_partial.txt"
VALID_RAW_FILES_NO_FASTQ2_PARTIAL = {}
VALID_RAW_FILES_NO_FASTQ2_PARTIAL[VALID_NAME_1] = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL).get_file_list(VALID_NAME_1)
VALID_RAW_FILES_NO_FASTQ2_PARTIAL[VALID_NAME_2] = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL).get_file_list(VALID_NAME_2)

EXP_FASTQ1_TEST1_NO_FASTQ2_PARTIAL = EXP_FASTQ1_TEST1_FULL
EXP_FASTQ1_TEST2_NO_FASTQ2_PARTIAL = EXP_FASTQ1_TEST2_FULL
EXP_FASTQ2_TEST1_NO_FASTQ2_PARTIAL = EXP_FASTQ2_TEST1_FULL
EXP_FASTQ2_TEST2_NO_FASTQ2_PARTIAL = ''

VALID_SAMPLESHEET_IDENTICAL_NAMES = "raw_data/valid_samplesheet_identical_names.txt"
VALID_RAW_FILES_IDENTICAL_NAMES = {}
VALID_RAW_FILES_IDENTICAL_NAMES[VALID_NAME_1] = SampleManager(VALID_SAMPLESHEET_IDENTICAL_NAMES).get_file_list(VALID_NAME_1)

# generate_outputs
VALID_DIR_NAME = "valid_dir_name"
VALID_SUFFIX = ".valid_suffix"
VALID_PAIR_TRUE = True
VALID_PAIR_FALSE = False
VALID_MERGE_TRUE = True
VALID_MERGE_FALSE = False

VALID_NAME_1 = "test1"
VALID_NAME_2 = "test2"

def test_outputmanager_constructor_valid_params_fastq2_full():
    om = OutputManager(VALID_RAW_FILES_FULL)
    eq_(isinstance(om.raw_files, dict), True)
    eq_(len(om.raw_files), 2)
    eq_(om.raw_files.keys(), [VALID_NAME_1,VALID_NAME_2])
    eq_(isinstance(om.raw_files[VALID_NAME_1], FileList), True)
    eq_(isinstance(om.raw_files[VALID_NAME_2], FileList), True)
    eq_(om.raw_files[VALID_NAME_1].file_list[0][0], EXP_FASTQ1_TEST1_FULL)
    eq_(om.raw_files[VALID_NAME_1].file_list[0][1], EXP_FASTQ2_TEST1_FULL)
    eq_(len(om.raw_files[VALID_NAME_1].file_list[0]), 2)
    eq_(om.raw_files[VALID_NAME_2].file_list[0][0], EXP_FASTQ1_TEST2_FULL)
    eq_(om.raw_files[VALID_NAME_2].file_list[0][1], EXP_FASTQ2_TEST2_FULL)
    eq_(len(om.raw_files[VALID_NAME_2].file_list[0]), 2)

def test_outputmanager_constructor_valid_params_fastq2_no_fastq2():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2)
    eq_(isinstance(om.raw_files, dict), True)
    eq_(len(om.raw_files), 2)
    eq_(om.raw_files.keys(), [VALID_NAME_1,VALID_NAME_2])
    eq_(isinstance(om.raw_files[VALID_NAME_1], FileList), True)
    eq_(isinstance(om.raw_files[VALID_NAME_2], FileList), True)
    eq_(om.raw_files[VALID_NAME_1].file_list[0][0], EXP_FASTQ1_TEST1_NO_FASTQ2)
    eq_(om.raw_files[VALID_NAME_1].file_list[0][1], EXP_FASTQ2_TEST1_NO_FASTQ2)
    eq_(len(om.raw_files[VALID_NAME_1].file_list[0]), 2)
    eq_(om.raw_files[VALID_NAME_2].file_list[0][0], EXP_FASTQ1_TEST2_NO_FASTQ2)
    eq_(om.raw_files[VALID_NAME_2].file_list[0][1], EXP_FASTQ2_TEST2_NO_FASTQ2)
    eq_(len(om.raw_files[VALID_NAME_2].file_list[0]), 2)

def test_outputmanager_constructor_valid_params_fastq2_no_fastq2_partial():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2_PARTIAL)
    eq_(isinstance(om.raw_files, dict), True)
    eq_(len(om.raw_files), 2)
    eq_(om.raw_files.keys(), [VALID_NAME_1,VALID_NAME_2])
    eq_(isinstance(om.raw_files[VALID_NAME_1], FileList), True)
    eq_(isinstance(om.raw_files[VALID_NAME_2], FileList), True)
    eq_(om.raw_files[VALID_NAME_1].file_list[0][0], EXP_FASTQ1_TEST1_NO_FASTQ2_PARTIAL)
    eq_(om.raw_files[VALID_NAME_1].file_list[0][1], EXP_FASTQ2_TEST1_NO_FASTQ2_PARTIAL)
    eq_(len(om.raw_files[VALID_NAME_1].file_list[0]), 2)
    eq_(om.raw_files[VALID_NAME_2].file_list[0][0], EXP_FASTQ1_TEST2_NO_FASTQ2_PARTIAL)
    eq_(om.raw_files[VALID_NAME_2].file_list[0][1], EXP_FASTQ2_TEST2_NO_FASTQ2_PARTIAL)
    eq_(len(om.raw_files[VALID_NAME_2].file_list[0]), 2)

# Expected: Full samplesheet, pair = False, merge = False
FILE_1_R1 = VALID_NAME_1 + "_1_R1"
FILE_2_R1 = VALID_NAME_2 + "_1_R1"
FILE_1_R2 = VALID_NAME_1 + "_1_R2"
FILE_2_R2 = VALID_NAME_2 + "_1_R2"

EXPECTED_FSS_PF_MF = []
EXPECTED_FSS_PF_MF.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_FSS_PF_MF.append(FileList([[FILE_2_R1, FILE_2_R2]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_false_merge_false_full_samplesheet():
    om = OutputManager(VALID_RAW_FILES_FULL)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_FSS_PF_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_FSS_PF_MF[0].name)
    eq_(outputs[VALID_NAME_2].file_list, EXPECTED_FSS_PF_MF[1].file_list)
    eq_(outputs[VALID_NAME_2].name, EXPECTED_FSS_PF_MF[1].name)

# Expected: Full samplesheet, pair = True, merge = False
FILE_1_R1 = VALID_NAME_1 + "_1"
FILE_1_R2 = ""
FILE_2_R1 = VALID_NAME_2 + "_1"
FILE_2_R2 = ""

EXPECTED_FSS_PT_MF = []
EXPECTED_FSS_PT_MF.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_FSS_PT_MF.append(FileList([[FILE_2_R1, FILE_2_R2]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_true_merge_false_full_samplesheet():
    om = OutputManager(VALID_RAW_FILES_FULL)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_FSS_PT_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_FSS_PT_MF[0].name)
    eq_(outputs[VALID_NAME_2].file_list, EXPECTED_FSS_PT_MF[1].file_list)
    eq_(outputs[VALID_NAME_2].name, EXPECTED_FSS_PT_MF[1].name)

# Expected: Full samplesheet, pair = False, merge = True
FILE_1_R1 = VALID_NAME_1 + "_R1"
FILE_2_R1 = VALID_NAME_2 + "_R1"
FILE_1_R2 = VALID_NAME_1 + "_R2"
FILE_2_R2 = VALID_NAME_2 + "_R2"

EXPECTED_FSS_PF_MT = []
EXPECTED_FSS_PF_MT.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_FSS_PF_MT.append(FileList([[FILE_2_R1, FILE_2_R2]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_false_merge_true_full_samplesheet():
    om = OutputManager(VALID_RAW_FILES_FULL)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_FSS_PF_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_FSS_PF_MT[0].name)
    eq_(outputs[VALID_NAME_2].file_list, EXPECTED_FSS_PF_MT[1].file_list)
    eq_(outputs[VALID_NAME_2].name, EXPECTED_FSS_PF_MT[1].name)

# Expected: Full samplesheet, pair = True, merge = True
FILE_1 = VALID_NAME_1
FILE_2 = VALID_NAME_2

EXPECTED_FSS_PT_MT = []
EXPECTED_FSS_PT_MT.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_FSS_PT_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_true_merge_true_full_samplesheet():
    om = OutputManager(VALID_RAW_FILES_FULL)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_FSS_PT_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_FSS_PT_MT[0].name)
    eq_(outputs[VALID_NAME_2].file_list, EXPECTED_FSS_PT_MT[1].file_list)
    eq_(outputs[VALID_NAME_2].name, EXPECTED_FSS_PT_MT[1].name)

# Expected: identical names samplesheet, pair = False, merge = False
FILE_1_R1 = VALID_NAME_1 + "_1_R1"
FILE_2_R1 = VALID_NAME_1 + "_2_R1"
FILE_1_R2 = VALID_NAME_1 + "_1_R2"
FILE_2_R2 = VALID_NAME_1 + "_2_R2"

EXPECTED_INSS_PF_MF = []
EXPECTED_INSS_PF_MF.append(FileList([[FILE_1_R1, FILE_1_R2], [FILE_2_R1, FILE_2_R2]], VALID_NAME_1))

def test_outputmanager_generate_outputs_pair_false_merge_false_identical_samplesheet():
    om = OutputManager(VALID_RAW_FILES_IDENTICAL_NAMES)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_INSS_PF_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_INSS_PF_MF[0].name)

# Expected: identical names samplesheet, pair = True, merge = False
FILE_1 =VALID_NAME_1 + "_1"
FILE_2 =VALID_NAME_1 + "_2"

EXPECTED_INSS_PT_MF = []
EXPECTED_INSS_PT_MF.append(FileList([[FILE_1, ""], [FILE_2, ""]], VALID_NAME_1))

def test_outputmanager_generate_outputs_pair_true_merge_false_identical_samplesheet():
    om = OutputManager(VALID_RAW_FILES_IDENTICAL_NAMES)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_INSS_PT_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_INSS_PT_MF[0].name)

# Expected: identical names samplesheet, pair = False, merge = True
FILE_R1 = VALID_NAME_1 + "_R1"
FILE_R2 = VALID_NAME_1 + "_R2"

EXPECTED_INSS_PF_MT = []
EXPECTED_INSS_PF_MT.append(FileList([[FILE_R1, FILE_R2]], VALID_NAME_1))

def test_outputmanager_generate_outputs_pair_false_merge_true_identical_samplesheet():
    om = OutputManager(VALID_RAW_FILES_IDENTICAL_NAMES)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_INSS_PF_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_INSS_PF_MT[0].name)

# Expected: identical names samplesheet, pair = True, merge = True
FILE = VALID_NAME_1

EXPECTED_INSS_PT_MT = []
EXPECTED_INSS_PT_MT.append(FileList([[FILE, ""]], VALID_NAME_1))

def test_outputmanager_generate_outputs_pair_true_merge_true_identical_samplesheet():
    om = OutputManager(VALID_RAW_FILES_IDENTICAL_NAMES)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_INSS_PT_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_INSS_PT_MT[0].name)

# Expected: samplesheet no fastq2, pair = False, merge = False
FILE_1 = VALID_NAME_1 + "_1_R1"
FILE_2 = VALID_NAME_2 + "_1_R1"

EXPECTED_SSNF2_PF_MF = []
EXPECTED_SSNF2_PF_MF.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PF_MF.append(FileList([[FILE_2, ""]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_false_merge_false_samplesheet_no_fastq2():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2_PF_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2_PF_MF[0].name)

# Expected: samplesheet no fastq2, pair = True, merge = False
FILE_1 = VALID_NAME_1 + "_1"
FILE_2 = VALID_NAME_2 + "_1"

EXPECTED_SSNF2_PT_MF = []
EXPECTED_SSNF2_PT_MF.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PT_MF.append(FileList([[FILE_2, ""]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_true_merge_false_samplesheet_no_fastq2():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2_PT_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2_PT_MF[0].name)

# Expected: samplesheet no fastq2, pair = False, merge = True
FILE_1 = VALID_NAME_1 + "_R1"
FILE_2 = VALID_NAME_2 + "_R1"

EXPECTED_SSNF2_PF_MT = []
EXPECTED_SSNF2_PF_MT.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PF_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_false_merge_true_samplesheet_no_fastq2():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2_PF_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2_PF_MT[0].name)

# Expected: samplesheet no fastq2, pair = True, merge = True
FILE_1 = VALID_NAME_1
FILE_2 = VALID_NAME_2

EXPECTED_SSNF2_PT_MT = []
EXPECTED_SSNF2_PT_MT.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PT_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_true_merge_true_samplesheet_no_fastq2():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2_PT_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2_PT_MT[0].name)

# Expected: samplesheet no fastq2 partial, pair = True, merge = False
FILE_1_R1 = VALID_NAME_1 + "_1_R1"
FILE_1_R2 = VALID_NAME_1 + "_1_R2"
FILE_2 =VALID_NAME_2 + "_1_R1"

EXPECTED_SSNF2P_PF_MF = []
EXPECTED_SSNF2P_PF_MF.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_SSNF2P_PF_MF.append(FileList([[FILE_2, ""]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_false_merge_false_samplesheet_no_fastq2_partial():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2_PARTIAL)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2P_PF_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2P_PF_MF[0].name)

# Expected: samplesheet no fastq2 partial, pair = True, merge = False
EXPECTED_SSNF2P_PT_MF = EXPECTED_SSNF2_PT_MF

def test_outputmanager_generate_outputs_pair_true_merge_false_samplesheet_no_fastq2_partial():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2_PARTIAL)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2P_PT_MF[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2P_PT_MF[0].name)

# Expected: samplesheet no fastq2 partial, pair = False, merge = True
FILE_1_R1 = VALID_NAME_1 + "_R1"
FILE_1_R2 = VALID_NAME_1 + "_R2"
FILE_2 =VALID_NAME_2 + "_R1"

EXPECTED_SSNF2P_PF_MT = []
EXPECTED_SSNF2P_PF_MT.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_SSNF2P_PF_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

def test_outputmanager_generate_outputs_pair_false_merge_true_samplesheet_no_fastq2_partial():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2_PARTIAL)
    outputs = om.generate_outputs(VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2P_PF_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2P_PF_MT[0].name)

# Expected: samplesheet no fastq2 partial, pair = True, merge = True
EXPECTED_SSNF2P_PT_MT = EXPECTED_SSNF2_PT_MT

def test_outputmanager_generate_outputs_pair_true_merge_true_samplesheet_no_fastq2_partial():
    om = OutputManager(VALID_RAW_FILES_NO_FASTQ2_PARTIAL)
    outputs = om.generate_outputs(VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[VALID_NAME_1].file_list, EXPECTED_SSNF2P_PT_MT[0].file_list)
    eq_(outputs[VALID_NAME_1].name, EXPECTED_SSNF2P_PT_MT[0].name)

@raises(SystemExit)
def test_outputmanager_generate_outputs_invalid_pair_type():
    om = OutputManager(VALID_RAW_FILES_FULL)
    om.generate_outputs('a', VALID_MERGE_TRUE)

@raises(SystemExit)
def test_outputmanager_generate_outputs_invalid_merge_type():
    om = OutputManager(VALID_RAW_FILES_FULL)
    om.generate_outputs(VALID_PAIR_TRUE, 'a')
