from nose.tools import *
from lib.SampleManager import *

class NullWriter:
    def write(self, s):
        pass
sys.stderr = NullWriter()

# TESTS: FileList

VALID_NAME = "valid_name"
VALID_FILELIST_FULL = [['a','b'],['c','d']]
VALID_FILELIST_EMPTY_KEY_2 = [['a','b'],['c','']]
INVALID_FILELIST_EMPTY = []
INVALID_FILELIST_NO_KEYS = [['a','b'],[]]
INVALID_FILELIST_EMPTY_KEY_1 = [['a','b'],['','d']]
INVALID_FILELIST_KEY_LENGTH = [['a','b'],['c']]
INVALID_FILELIST_KEY_TYPE = [['a','b'],['c', 1]]

def test_filelist_constructor_valid_params():
    fl = FileList(VALID_FILELIST_FULL, VALID_NAME)
    eq_(fl.file_list, VALID_FILELIST_FULL)
    eq_(fl.name, VALID_NAME)

def test_filelist_constructor_valid_params_empty_2():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2, VALID_NAME)
    eq_(fl.file_list, VALID_FILELIST_EMPTY_KEY_2)
    eq_(fl.name, VALID_NAME)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_type():
    FileList(1, VALID_NAME)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_empty():
    FileList(INVALID_FILELIST_EMPTY, VALID_NAME)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_no_keys():
    FileList(INVALID_FILELIST_NO_KEYS, VALID_NAME)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_empty_key_1():
    FileList(INVALID_FILELIST_EMPTY_KEY_1, VALID_NAME)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_key_length():
    FileList(INVALID_FILELIST_KEY_LENGTH, VALID_NAME)

@raises(SystemExit)
def test_filelist_constructor_invalid_file_list_key_type():
    FileList(INVALID_FILELIST_KEY_TYPE, VALID_NAME)

@raises(SystemExit)
def test_file_constructor_invalid_name_type():
    FileList(VALID_FILELIST_FULL, 1)

@raises(SystemExit)
def test_file_constructor_invalid_name_length():
    FileList(VALID_FILELIST_FULL, "")

def test_filelist_get_files_valid_index_two_file():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2, VALID_NAME)
    files = fl.get_files(0)
    eq_(files, VALID_FILELIST_EMPTY_KEY_2[0])

def test_filelist_get_files_valid_index_one_file():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2, VALID_NAME)
    files = fl.get_files(1)
    eq_(files, ['c'])

@raises(SystemExit)
def test_filelist_get_files_invalid_index():
    fl = FileList(VALID_FILELIST_EMPTY_KEY_2, VALID_NAME)
    fl.get_files(2)

def test_filelist_get_name():
    fl = FileList(VALID_FILELIST_FULL, VALID_NAME)
    eq_(fl.get_name(), VALID_NAME)


# TESTS: SampleManager

# constructor
VALID_SAMPLESHEET_FULL = "raw_data/valid_samplesheet.txt"
VALID_SAMPLESHEET_IDENTICAL_NAMES = "raw_data/valid_samplesheet_identical_names.txt"
VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL = "raw_data/valid_samplesheet_no_fastq2_partial.txt"
VALID_SAMPLESHEET_NO_FASTQ2 = "raw_data/valid_samplesheet_no_fastq2.txt"
INVALID_SAMPLESHEET_NO_FASTQ1 = "raw_data/invalid_samplesheet_no_fastq1.txt"
INVALID_SAMPLESHEET_NO_FASTQ2 = "raw_data/invalid_samplesheet_no_fastq2.txt"
INVALID_SAMPLESHEET_NO_NAME = "raw_data/invalid_samplesheet_no_name.txt"
EXP_VALUES_FASTQ1_FULL = [["raw_data/a1_1.fastq.gz"], ["raw_data/a2_1.fastq.gz"]]
EXP_VALUES_FASTQ2_FULL = [["raw_data/a1_2.fastq.gz"], ["raw_data/a2_2.fastq.gz"]]
EXP_VALUES_FASTQ1_IDENTICAL_NAMES = [["raw_data/a1_1.fastq.gz", "raw_data/a2_1.fastq.gz"]]
EXP_VALUES_FASTQ2_IDENTICAL_NAMES = [["raw_data/a1_2.fastq.gz", "raw_data/a2_2.fastq.gz"]]
EXP_VALUES_FASTQ2_PARTIAL = [["raw_data/a1_2.fastq.gz"], ['']]
EXP_VALUES_NO_FASTQ2 = [[''], ['']]
EXP_KEYS_DIFFERENT = ['test1', 'test2']
EXP_KEYS_SAME = ['test1']

# generate_outputs
VALID_DIR_NAME = "valid_dir_name"
VALID_SUFFIX = ".valid_suffix"
VALID_PAIR_TRUE = True
VALID_PAIR_FALSE = False
VALID_MERGE_TRUE = True
VALID_MERGE_FALSE = False

VALID_NAME_1 = "test1"
VALID_NAME_2 = "test2"

# Expected: Full samplesheet, pair = False, merge = False
FILE_1_R1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1_R1" + VALID_SUFFIX
FILE_2_R1 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_1_R1" + VALID_SUFFIX
FILE_1_R2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1_R2" + VALID_SUFFIX
FILE_2_R2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_1_R2" + VALID_SUFFIX

EXPECTED_FSS_PF_MF = []
EXPECTED_FSS_PF_MF.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_FSS_PF_MF.append(FileList([[FILE_2_R1, FILE_2_R2]], VALID_NAME_2))

# Expected: Full samplesheet, pair = True, merge = False
FILE_1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1" + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_1" + VALID_SUFFIX

EXPECTED_FSS_PT_MF = []
EXPECTED_FSS_PT_MF.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_FSS_PT_MF.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: Full samplesheet, pair = False, merge = True
FILE_1_R1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_R1" + VALID_SUFFIX
FILE_2_R1 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_R1" + VALID_SUFFIX
FILE_1_R2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_R2" + VALID_SUFFIX
FILE_2_R2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_R2" + VALID_SUFFIX

EXPECTED_FSS_PF_MT = []
EXPECTED_FSS_PF_MT.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_FSS_PF_MT.append(FileList([[FILE_2_R1, FILE_2_R2]], VALID_NAME_2))

# Expected: Full samplesheet, pair = True, merge = True
FILE_1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + VALID_SUFFIX

EXPECTED_FSS_PT_MT = []
EXPECTED_FSS_PT_MT.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_FSS_PT_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: identical names samplesheet, pair = False, merge = False
FILE_1_R1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1_R1" + VALID_SUFFIX
FILE_2_R1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_2_R1" + VALID_SUFFIX
FILE_1_R2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1_R2" + VALID_SUFFIX
FILE_2_R2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_2_R2" + VALID_SUFFIX

EXPECTED_INSS_PF_MF = []
EXPECTED_INSS_PF_MF.append(FileList([[FILE_1_R1, FILE_1_R2], [FILE_2_R1, FILE_2_R2]], VALID_NAME_1))

# Expected: identical names samplesheet, pair = True, merge = False
FILE_1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1" + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_2" + VALID_SUFFIX

EXPECTED_INSS_PT_MF = []
EXPECTED_INSS_PT_MF.append(FileList([[FILE_1, ""], [FILE_2, ""]], VALID_NAME_1))

# Expected: identical names samplesheet, pair = False, merge = True
FILE_R1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_R1" + VALID_SUFFIX
FILE_R2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_R2" + VALID_SUFFIX

EXPECTED_INSS_PF_MT = []
EXPECTED_INSS_PF_MT.append(FileList([[FILE_R1, FILE_R2]], VALID_NAME_1))

# Expected: identical names samplesheet, pair = True, merge = True
FILE = VALID_DIR_NAME + "/" + VALID_NAME_1 + VALID_SUFFIX

EXPECTED_INSS_PT_MT = []
EXPECTED_INSS_PT_MT.append(FileList([[FILE, ""]], VALID_NAME_1))

# Expected: samplesheet no fastq2, pair = False, merge = False
FILE_1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1_R1" + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_1_R1" + VALID_SUFFIX

EXPECTED_SSNF2_PF_MF = []
EXPECTED_SSNF2_PF_MF.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PF_MF.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: samplesheet no fastq2, pair = True, merge = False
FILE_1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1" + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_1" + VALID_SUFFIX

EXPECTED_SSNF2_PT_MF = []
EXPECTED_SSNF2_PT_MF.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PT_MF.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: samplesheet no fastq2, pair = False, merge = True
FILE_1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_R1" + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_R1" + VALID_SUFFIX

EXPECTED_SSNF2_PF_MT = []
EXPECTED_SSNF2_PF_MT.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PF_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: samplesheet no fastq2, pair = True, merge = True
FILE_1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + VALID_SUFFIX

EXPECTED_SSNF2_PT_MT = []
EXPECTED_SSNF2_PT_MT.append(FileList([[FILE_1, ""]], VALID_NAME_1))
EXPECTED_SSNF2_PT_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: samplesheet no fastq2 partial, pair = True, merge = False
FILE_1_R1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1_R1" + VALID_SUFFIX
FILE_1_R2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_1_R2" + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_1_R1" + VALID_SUFFIX

EXPECTED_SSNF2P_PF_MF = []
EXPECTED_SSNF2P_PF_MF.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_SSNF2P_PF_MF.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: samplesheet no fastq2 partial, pair = True, merge = False
EXPECTED_SSNF2P_PT_MF = EXPECTED_SSNF2_PT_MF

# Expected: samplesheet no fastq2 partial, pair = False, merge = True
FILE_1_R1 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_R1" + VALID_SUFFIX
FILE_1_R2 = VALID_DIR_NAME + "/" + VALID_NAME_1 + "_R2" + VALID_SUFFIX
FILE_2 = VALID_DIR_NAME + "/" + VALID_NAME_2 + "_R1" + VALID_SUFFIX

EXPECTED_SSNF2P_PF_MT = []
EXPECTED_SSNF2P_PF_MT.append(FileList([[FILE_1_R1, FILE_1_R2]], VALID_NAME_1))
EXPECTED_SSNF2P_PF_MT.append(FileList([[FILE_2, ""]], VALID_NAME_2))

# Expected: samplesheet no fastq2 partial, pair = True, merge = True
EXPECTED_SSNF2P_PT_MT = EXPECTED_SSNF2_PT_MT

def test_samplemanager_constructor_valid_sample_sheet():
    sm = SampleManager(VALID_SAMPLESHEET_FULL)
    eq_(sm.raw_files_r1.keys(), EXP_KEYS_DIFFERENT)
    eq_(sm.raw_files_r1.values(), EXP_VALUES_FASTQ1_FULL)
    eq_(sm.raw_files_r2.keys(), EXP_KEYS_DIFFERENT)
    eq_(sm.raw_files_r2.values(), EXP_VALUES_FASTQ2_FULL)

def test_samplemanager_constructor_valid_sample_sheet_no_fastq2():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2)
    eq_(sm.raw_files_r1.keys(), EXP_KEYS_DIFFERENT)
    eq_(sm.raw_files_r1.values(), EXP_VALUES_FASTQ1_FULL)
    eq_(sm.raw_files_r2.keys(), EXP_KEYS_DIFFERENT)
    eq_(sm.raw_files_r2.values(), EXP_VALUES_NO_FASTQ2)

def test_samplemanager_constructor_valid_sample_sheet_no_fastq2_partial():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL)
    eq_(sm.raw_files_r1.keys(), EXP_KEYS_DIFFERENT)
    eq_(sm.raw_files_r1.values(), EXP_VALUES_FASTQ1_FULL)
    eq_(sm.raw_files_r2.keys(), EXP_KEYS_DIFFERENT)
    eq_(sm.raw_files_r2.values(), EXP_VALUES_FASTQ2_PARTIAL)

def test_samplemanager_constructor_valid_sample_sheet_identical_names():
    sm = SampleManager(VALID_SAMPLESHEET_IDENTICAL_NAMES)
    eq_(sm.raw_files_r1.keys(), EXP_KEYS_SAME)
    eq_(sm.raw_files_r1.values(), EXP_VALUES_FASTQ1_IDENTICAL_NAMES)
    eq_(sm.raw_files_r2.keys(), EXP_KEYS_SAME)
    eq_(sm.raw_files_r2.values(), EXP_VALUES_FASTQ2_IDENTICAL_NAMES)

@raises(SystemExit)
def test_samplemanager_constructor_invalid_sample_sheet_no_name():
    SampleManager(INVALID_SAMPLESHEET_NO_NAME)

@raises(SystemExit)
def test_samplemanager_constructor_invalid_sample_sheet_no_fastq1():
    SampleManager(INVALID_SAMPLESHEET_NO_FASTQ1)

@raises(SystemExit)
def test_samplemanager_constructor_invalid_sample_sheet_no_fastq1():
    SampleManager(INVALID_SAMPLESHEET_NO_FASTQ2)

def test_samplemanager_generate_outputs_pair_false_merge_false_full_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_FULL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_FSS_PF_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_FSS_PF_MF[0].name)
    eq_(outputs[1].file_list, EXPECTED_FSS_PF_MF[1].file_list)
    eq_(outputs[1].name, EXPECTED_FSS_PF_MF[1].name)

def test_samplemanager_generate_outputs_pair_true_merge_false_full_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_FULL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_FSS_PT_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_FSS_PT_MF[0].name)
    eq_(outputs[1].file_list, EXPECTED_FSS_PT_MF[1].file_list)
    eq_(outputs[1].name, EXPECTED_FSS_PT_MF[1].name)

def test_samplemanager_generate_outputs_pair_false_merge_true_full_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_FULL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_FSS_PF_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_FSS_PF_MT[0].name)
    eq_(outputs[1].file_list, EXPECTED_FSS_PF_MT[1].file_list)
    eq_(outputs[1].name, EXPECTED_FSS_PF_MT[1].name)

def test_samplemanager_generate_outputs_pair_false_merge_true_full_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_FULL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_FSS_PT_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_FSS_PT_MT[0].name)
    eq_(outputs[1].file_list, EXPECTED_FSS_PT_MT[1].file_list)
    eq_(outputs[1].name, EXPECTED_FSS_PT_MT[1].name)

def test_samplemanager_generate_outputs_pair_false_merge_false_identical_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_IDENTICAL_NAMES)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_INSS_PF_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_INSS_PF_MF[0].name)

def test_samplemanager_generate_outputs_pair_true_merge_false_identical_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_IDENTICAL_NAMES)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_INSS_PT_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_INSS_PT_MF[0].name)

def test_samplemanager_generate_outputs_pair_false_merge_true_identical_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_IDENTICAL_NAMES)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_INSS_PF_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_INSS_PF_MT[0].name)

def test_samplemanager_generate_outputs_pair_true_merge_true_identical_samplesheet():
    sm = SampleManager(VALID_SAMPLESHEET_IDENTICAL_NAMES)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_INSS_PT_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_INSS_PT_MT[0].name)

def test_samplemanager_generate_outputs_pair_false_merge_false_samplesheet_no_fastq2():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2_PF_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2_PF_MF[0].name)

def test_samplemanager_generate_outputs_pair_true_merge_false_samplesheet_no_fastq2():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2_PT_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2_PT_MF[0].name)

def test_samplemanager_generate_outputs_pair_false_merge_true_samplesheet_no_fastq2():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2_PF_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2_PF_MT[0].name)

def test_samplemanager_generate_outputs_pair_true_merge_true_samplesheet_no_fastq2():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2_PT_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2_PT_MT[0].name)

def test_samplemanager_generate_outputs_pair_false_merge_false_samplesheet_no_fastq2_partial():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2P_PF_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2P_PF_MF[0].name)

def test_samplemanager_generate_outputs_pair_true_merge_false_samplesheet_no_fastq2_partial():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_FALSE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2P_PT_MF[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2P_PT_MF[0].name)

def test_samplemanager_generate_outputs_pair_false_merge_true_samplesheet_no_fastq2_partial():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_FALSE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2P_PF_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2P_PF_MT[0].name)

def test_samplemanager_generate_outputs_pair_true_merge_true_samplesheet_no_fastq2_partial():
    sm = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL)
    outputs = sm.generate_outputs(VALID_DIR_NAME, VALID_SUFFIX, VALID_PAIR_TRUE, VALID_MERGE_TRUE)
    eq_(outputs[0].file_list, EXPECTED_SSNF2P_PT_MT[0].file_list)
    eq_(outputs[0].name, EXPECTED_SSNF2P_PT_MT[0].name)

