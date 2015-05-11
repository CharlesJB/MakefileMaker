from nose.tools import *
from lib.SampleManager import *

class NullWriter:
    def write(self, s):
        pass
sys.stderr = NullWriter()

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
    
def test_samplemanager_get_file_list_valid_name():
    sm = SampleManager(VALID_SAMPLESHEET_FULL)
    fl = sm.get_file_list("test1")
    eq_(isinstance(fl, FileList), True)
    eq_(isinstance(fl.unlist(), list), True)
    eq_(fl.unlist()[0], "raw_data/a1_1.fastq.gz")
    eq_(fl.unlist()[1], "raw_data/a1_2.fastq.gz")
 
def test_samplemanager_get_file_list_absent_name():
    sm = SampleManager(VALID_SAMPLESHEET_FULL)
    fl = sm.get_file_list("test3")
    eq_(fl, None)
