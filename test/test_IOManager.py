from nose.tools import *
from lib.IOManager import *
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

# TODO: This should be invalid in FileList
VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL = "raw_data/valid_samplesheet_no_fastq2_partial.txt"
VALID_RAW_FILES_NO_FASTQ2_PARTIAL = {}
VALID_RAW_FILES_NO_FASTQ2_PARTIAL[VALID_NAME_1] = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL).get_file_list(VALID_NAME_1)
VALID_RAW_FILES_NO_FASTQ2_PARTIAL[VALID_NAME_2] = SampleManager(VALID_SAMPLESHEET_NO_FASTQ2_PARTIAL).get_file_list(VALID_NAME_2)

EXP_FASTQ1_TEST1_NO_FASTQ2_PARTIAL = EXP_FASTQ1_TEST1_FULL
EXP_FASTQ1_TEST2_NO_FASTQ2_PARTIAL = EXP_FASTQ1_TEST2_FULL
EXP_FASTQ2_TEST1_NO_FASTQ2_PARTIAL = EXP_FASTQ2_TEST1_FULL
EXP_FASTQ2_TEST2_NO_FASTQ2_PARTIAL = ''

def test_outputmanager_constructor_valid_params_fastq2_full():
    om = IOManager(VALID_RAW_FILES_FULL)
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
    om = IOManager(VALID_RAW_FILES_NO_FASTQ2)
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
    om = IOManager(VALID_RAW_FILES_NO_FASTQ2_PARTIAL)
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

# Generate IO
VALID_SAMPLESHEET_IO = "raw_data/valid_samplesheet_IO.txt"
SAMPLE_MANAGER_IO = SampleManager(VALID_SAMPLESHEET_IO)
VALID_RAW_FILES_IO = {}
VALID_RAW_FILES_IO['C2PT'] = SAMPLE_MANAGER_IO.get_file_list('C2PT')
VALID_RAW_FILES_IO['C2PF'] = SAMPLE_MANAGER_IO.get_file_list('C2PF')
VALID_RAW_FILES_IO['C1PT'] = SAMPLE_MANAGER_IO.get_file_list('C1PT')
VALID_RAW_FILES_IO['C1PF'] = SAMPLE_MANAGER_IO.get_file_list('C1PF')
IO_MANAGER = IOManager(VALID_RAW_FILES_IO)

## generate_input
### C2PT
EXP_INPUT_C2PT_FFFF = [FileList([['C2PT_1_R1', '']]), FileList([['C2PT_1_R2', '']]), FileList([['C2PT_2_R1', '']]), FileList([['C2PT_2_R2', '']])]
EXP_INPUT_C2PT_FFFT = [FileList([['C2PT_1_R1', 'C2PT_1_R2']]), FileList([['C2PT_2_R1', 'C2PT_2_R2']])]
EXP_INPUT_C2PT_FFTF = [FileList([['C2PT_1_R1', ''], ['C2PT_2_R1', '']]), FileList([['C2PT_1_R2', ''], ['C2PT_2_R2', '']])]
EXP_INPUT_C2PT_FTFF = [FileList([['C2PT_1', '']]), FileList([['C2PT_2', '']])]
EXP_INPUT_C2PT_TFFF = [FileList([['C2PT_R1', '']]), FileList([['C2PT_R2', '']])]
EXP_INPUT_C2PT_FFTT = [FileList([['C2PT_1_R1', 'C2PT_1_R2'], ['C2PT_2_R1', 'C2PT_2_R2']])]
EXP_INPUT_C2PT_TFFT = [FileList([['C2PT_R1', 'C2PT_R2']])]
EXP_INPUT_C2PT_FTTF = [FileList([['C2PT_1', ''],['C2PT_2', '']])]
EXP_INPUT_C2PT_TTFF = [FileList([['C2PT', '']])]
### 2 files, not paired: C2PF
EXP_INPUT_C2PF_FFFF = [FileList([['C2PF_1', '']]), FileList([['C2PF_2', '']])]
EXP_INPUT_C2PF_FFFT = [FileList([['C2PF_1', '']]), FileList([['C2PF_2', '']])]
EXP_INPUT_C2PF_FFTF = [FileList([['C2PF_1', ''], [ 'C2PF_2', '']])]
EXP_INPUT_C2PF_FTFF = [FileList([['C2PF_1', '']]), FileList([['C2PF_2', '']])]
EXP_INPUT_C2PF_TFFF = [FileList([['C2PF', '']])]
EXP_INPUT_C2PF_FFTT = [FileList([['C2PF_1', ''], ['C2PF_2', '']])]
EXP_INPUT_C2PF_TFFT = [FileList([['C2PF', '']])]
EXP_INPUT_C2PF_FTTF = [FileList([['C2PF_1', ''], [ 'C2PF_2', '']])]
EXP_INPUT_C2PF_TTFF = [FileList([['C2PF', '']])]
### 1 file, paired: C1PT
EXP_INPUT_C1PT_FFFF = [FileList([['C1PT_R1', '']]), FileList([['C1PT_R2', '']])]
EXP_INPUT_C1PT_FFFT = [FileList([['C1PT_R1', 'C1PT_R2']])]
EXP_INPUT_C1PT_FFTF = [FileList([['C1PT_R1', '']]), FileList([['C1PT_R2', '']])]
EXP_INPUT_C1PT_FTFF = [FileList([['C1PT', '']])]
EXP_INPUT_C1PT_TFFF = [FileList([['C1PT_R1', '']]), FileList([['C1PT_R2', '']])]
EXP_INPUT_C1PT_FFTT = [FileList([['C1PT_R1', 'C1PT_R2']])]
EXP_INPUT_C1PT_TFFT = [FileList([['C1PT_R1', 'C1PT_R2']])]
EXP_INPUT_C1PT_FTTF = [FileList([['C1PT', '']])]
EXP_INPUT_C1PT_TTFF = [FileList([['C1PT', '']])]
### 1 file, not paired: C1PF
EXP_INPUT_C1PF_FFFF = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_FFFT = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_FFTF = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_FTFF = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_TFFF = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_FFTT = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_TFFT = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_FTTF = [FileList([['C1PF', '']])]
EXP_INPUT_C1PF_TTFF = [FileList([['C1PF', '']])]

### C2PT
def test_iomanager_generate_input_C2PT_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', False, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PT_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_FFFF[i].file_list)

def test_iomanager_generate_input_C2PT_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', False, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C2PT_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_FFFT[i].file_list)

def test_iomanager_generate_input_C2PT_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', False, False, True, False)
    eq_(len(obs), len(EXP_INPUT_C2PT_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_FFTF[i].file_list)

def test_iomanager_generate_input_C2PT_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', False, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PT_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_FTFF[i].file_list)

def test_iomanager_generate_input_C2PT_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', True, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PT_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_TFFF[i].file_list)

def test_iomanager_generate_input_C2PT_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', False, False, True, True)
    eq_(len(obs), len(EXP_INPUT_C2PT_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_FFTT[i].file_list)

def test_iomanager_generate_input_C2PT_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', True, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C2PT_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_TFFT[i].file_list)

def test_iomanager_generate_input_C2PT_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', False, True, True, False)
    eq_(len(obs), len(EXP_INPUT_C2PT_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_FTTF[i].file_list)

def test_iomanager_generate_input_C2PT_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PT', True, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PT_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PT_TTFF[i].file_list)

### C2PF
def test_iomanager_generate_input_C2PF_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', False, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PF_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_FFFF[i].file_list)

def test_iomanager_generate_input_C2PF_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', False, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C2PF_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_FFFT[i].file_list)

def test_iomanager_generate_input_C2PF_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', False, False, True, False)
    eq_(len(obs), len(EXP_INPUT_C2PF_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_FFTF[i].file_list)

def test_iomanager_generate_input_C2PF_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', False, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PF_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_FTFF[i].file_list)

def test_iomanager_generate_input_C2PF_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', True, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PF_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_TFFF[i].file_list)

def test_iomanager_generate_input_C2PF_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', False, False, True, True)
    eq_(len(obs), len(EXP_INPUT_C2PF_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_FFTT[i].file_list)

def test_iomanager_generate_input_C2PF_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', True, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C2PF_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_TFFT[i].file_list)

def test_iomanager_generate_input_C2PF_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', False, True, True, False)
    eq_(len(obs), len(EXP_INPUT_C2PF_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_FTTF[i].file_list)

def test_iomanager_generate_input_C2PF_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C2PF', True, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C2PF_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C2PF_TTFF[i].file_list)

### C1PT
def test_iomanager_generate_input_C1PT_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', False, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PT_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_FFFF[i].file_list)

def test_iomanager_generate_input_C1PT_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', False, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C1PT_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_FFFT[i].file_list)

def test_iomanager_generate_input_C1PT_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', False, False, True, False)
    eq_(len(obs), len(EXP_INPUT_C1PT_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_FFTF[i].file_list)

def test_iomanager_generate_input_C1PT_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', False, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PT_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_FTFF[i].file_list)

def test_iomanager_generate_input_C1PT_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', True, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PT_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_TFFF[i].file_list)

def test_iomanager_generate_input_C1PT_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', False, False, True, True)
    eq_(len(obs), len(EXP_INPUT_C1PT_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_FFTT[i].file_list)

def test_iomanager_generate_input_C1PT_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', True, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C1PT_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_TFFT[i].file_list)

def test_iomanager_generate_input_C1PT_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', False, True, True, False)
    eq_(len(obs), len(EXP_INPUT_C1PT_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_FTTF[i].file_list)

def test_iomanager_generate_input_C1PT_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PT', True, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PT_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PT_TTFF[i].file_list)

### C1PF
def test_iomanager_generate_input_C1PF_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', False, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PF_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_FFFF[i].file_list)

def test_iomanager_generate_input_C1PF_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', False, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C1PF_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_FFFT[i].file_list)

def test_iomanager_generate_input_C1PF_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', False, False, True, False)
    eq_(len(obs), len(EXP_INPUT_C1PF_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_FFTF[i].file_list)

def test_iomanager_generate_input_C1PF_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', False, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PF_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_FTFF[i].file_list)

def test_iomanager_generate_input_C1PF_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', True, False, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PF_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_TFFF[i].file_list)

def test_iomanager_generate_input_C1PF_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', False, False, True, True)
    eq_(len(obs), len(EXP_INPUT_C1PF_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_FFTT[i].file_list)

def test_iomanager_generate_input_C1PF_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', True, False, False, True)
    eq_(len(obs), len(EXP_INPUT_C1PF_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_TFFT[i].file_list)

def test_iomanager_generate_input_C1PF_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', False, True, True, False)
    eq_(len(obs), len(EXP_INPUT_C1PF_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_FTTF[i].file_list)

def test_iomanager_generate_input_C1PF_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_input('C1PF', True, True, False, False)
    eq_(len(obs), len(EXP_INPUT_C1PF_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_INPUT_C1PF_TTFF[i].file_list)

### Invalid name
@raises(SystemExit)
def test_iomanager_generate_input_invalid_name():
    IO_MANAGER.generate_input('FFFF', False, False, False, False)

@raises(SystemExit)
def test_iomanager_generate_input_invalid_name_empty():
    IO_MANAGER.generate_input('', False, False, False, False)

### Invalid cases: FTFT & TFTF & FTTT & TFTT & TTFT & TTTF & TTTT
@raises(SystemExit)
def test_iomanager_generate_input_invalid_case_FTFT():
    IO_MANAGER.generate_input('C2PT', False, True, False, True)

@raises(SystemExit)
def test_iomanager_generate_input_invalid_case_TFTF():
    IO_MANAGER.generate_input('C2PT', True, False, True, False)

@raises(SystemExit)
def test_iomanager_generate_input_invalid_case_FTTT():
    IO_MANAGER.generate_input('C2PT', False, True, True, True)

@raises(SystemExit)
def test_iomanager_generate_input_invalid_case_TFTT():
    IO_MANAGER.generate_input('C2PT', True, False, True, True)

@raises(SystemExit)
def test_iomanager_generate_input_invalid_case_TTFT():
    IO_MANAGER.generate_input('C2PT', True, True, False, True)

@raises(SystemExit)
def test_iomanager_generate_input_invalid_case_TTTF():
    IO_MANAGER.generate_input('C2PT', True, True, True, False)

@raises(SystemExit)
def test_iomanager_generate_input_invalid_case_TTTT():
    IO_MANAGER.generate_input('C2PT', True, True, True, True)

## generate_output
### C2PT
EXP_OUTPUT_C2PT_FFFF = [FileList([['C2PT_1_R1', '']]), FileList([['C2PT_1_R2', '']]), FileList([['C2PT_2_R1', '']]), FileList([['C2PT_2_R2', '']])]
EXP_OUTPUT_C2PT_FFFT = [FileList([['C2PT_1', '']]), FileList([['C2PT_2', '']])]
EXP_OUTPUT_C2PT_FFTF = [FileList([['C2PT_R1', '']]), FileList([['C2PT_R2', '']])]
EXP_OUTPUT_C2PT_FTFF = [FileList([['C2PT_1', '']]), FileList([['C2PT_2', '']])]
EXP_OUTPUT_C2PT_TFFF = [FileList([['C2PT_R1', '']]), FileList([['C2PT_R2', '']])]
EXP_OUTPUT_C2PT_FFTT = [FileList([['C2PT', '']])]
EXP_OUTPUT_C2PT_TFFT = [FileList([['C2PT', '']])]
EXP_OUTPUT_C2PT_FTTF = [FileList([['C2PT', '']])]
EXP_OUTPUT_C2PT_TTFF = [FileList([['C2PT', '']])]
### 2 files, not paired: C2PF
EXP_OUTPUT_C2PF_FFFF = [FileList([['C2PF_1', '']]), FileList([['C2PF_2', '']])]
EXP_OUTPUT_C2PF_FFFT = [FileList([['C2PF_1', '']]), FileList([['C2PF_2', '']])]
EXP_OUTPUT_C2PF_FFTF = [FileList([['C2PF', '']])]
EXP_OUTPUT_C2PF_FTFF = [FileList([['C2PF_1', '']]), FileList([['C2PF_2', '']])]
EXP_OUTPUT_C2PF_TFFF = [FileList([['C2PF', '']])]
EXP_OUTPUT_C2PF_FFTT = [FileList([['C2PF', '']])]
EXP_OUTPUT_C2PF_TFFT = [FileList([['C2PF', '']])]
EXP_OUTPUT_C2PF_FTTF = [FileList([['C2PF', '']])]
EXP_OUTPUT_C2PF_TTFF = [FileList([['C2PF', '']])]
### 1 file, paired: C1PT
EXP_OUTPUT_C1PT_FFFF = [FileList([['C1PT_R1', '']]), FileList([['C1PT_R2', '']])]
EXP_OUTPUT_C1PT_FFFT = [FileList([['C1PT', '']])]
EXP_OUTPUT_C1PT_FFTF = [FileList([['C1PT_R1', '']]), FileList([['C1PT_R2', '']])]
EXP_OUTPUT_C1PT_FTFF = [FileList([['C1PT', '']])]
EXP_OUTPUT_C1PT_TFFF = [FileList([['C1PT_R1', '']]), FileList([['C1PT_R2', '']])]
EXP_OUTPUT_C1PT_FFTT = [FileList([['C1PT', '']])]
EXP_OUTPUT_C1PT_TFFT = [FileList([['C1PT', '']])]
EXP_OUTPUT_C1PT_FTTF = [FileList([['C1PT', '']])]
EXP_OUTPUT_C1PT_TTFF = [FileList([['C1PT', '']])]
### 1 file, not paired: C1PF
EXP_OUTPUT_C1PF_FFFF = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_FFFT = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_FFTF = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_FTFF = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_TFFF = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_FFTT = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_TFFT = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_FTTF = [FileList([['C1PF', '']])]
EXP_OUTPUT_C1PF_TTFF = [FileList([['C1PF', '']])]

### C2PT
def test_iomanager_generate_output_C2PT_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', False, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_FFFF[i].file_list)

def test_iomanager_generate_output_C2PT_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', False, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_FFFT[i].file_list)

def test_iomanager_generate_output_C2PT_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', False, False, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_FFTF[i].file_list)

def test_iomanager_generate_output_C2PT_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', False, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_FTFF[i].file_list)

def test_iomanager_generate_output_C2PT_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', True, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_TFFF[i].file_list)

def test_iomanager_generate_output_C2PT_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', False, False, True, True)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_FFTT[i].file_list)

def test_iomanager_generate_output_C2PT_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', True, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_TFFT[i].file_list)

def test_iomanager_generate_output_C2PT_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', False, True, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_FTTF[i].file_list)

def test_iomanager_generate_output_C2PT_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PT', True, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PT_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PT_TTFF[i].file_list)

### C2PF
def test_iomanager_generate_output_C2PF_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', False, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_FFFF[i].file_list)

def test_iomanager_generate_output_C2PF_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', False, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_FFFT[i].file_list)

def test_iomanager_generate_output_C2PF_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', False, False, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_FFTF[i].file_list)

def test_iomanager_generate_output_C2PF_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', False, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_FTFF[i].file_list)

def test_iomanager_generate_output_C2PF_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', True, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_TFFF[i].file_list)

def test_iomanager_generate_output_C2PF_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', False, False, True, True)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_FFTT[i].file_list)

def test_iomanager_generate_output_C2PF_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', True, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_TFFT[i].file_list)

def test_iomanager_generate_output_C2PF_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', False, True, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_FTTF[i].file_list)

def test_iomanager_generate_output_C2PF_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C2PF', True, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C2PF_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C2PF_TTFF[i].file_list)

### C1PT
def test_iomanager_generate_output_C1PT_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', False, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_FFFF[i].file_list)

def test_iomanager_generate_output_C1PT_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', False, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_FFFT[i].file_list)

def test_iomanager_generate_output_C1PT_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', False, False, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_FFTF[i].file_list)

def test_iomanager_generate_output_C1PT_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', False, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_FTFF[i].file_list)

def test_iomanager_generate_output_C1PT_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', True, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_TFFF[i].file_list)

def test_iomanager_generate_output_C1PT_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', False, False, True, True)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_FFTT[i].file_list)

def test_iomanager_generate_output_C1PT_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', True, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_TFFT[i].file_list)

def test_iomanager_generate_output_C1PT_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', False, True, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_FTTF[i].file_list)

def test_iomanager_generate_output_C1PT_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PT', True, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PT_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PT_TTFF[i].file_list)

### C1PF
def test_iomanager_generate_output_C1PF_FFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', False, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_FFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_FFFF[i].file_list)

def test_iomanager_generate_output_C1PF_FFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', False, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_FFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_FFFT[i].file_list)

def test_iomanager_generate_output_C1PF_FFTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', False, False, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_FFTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_FFTF[i].file_list)

def test_iomanager_generate_output_C1PF_FTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', False, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_FTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_FTFF[i].file_list)

def test_iomanager_generate_output_C1PF_TFFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', True, False, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_TFFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_TFFF[i].file_list)

def test_iomanager_generate_output_C1PF_FFTT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', False, False, True, True)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_FFTT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_FFTT[i].file_list)

def test_iomanager_generate_output_C1PF_TFFT_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', True, False, False, True)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_TFFT))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_TFFT[i].file_list)

def test_iomanager_generate_output_C1PF_FTTF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', False, True, True, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_FTTF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_FTTF[i].file_list)

def test_iomanager_generate_output_C1PF_TTFF_full_sample_sheet():
    obs = IO_MANAGER.generate_output('C1PF', True, True, False, False)
    eq_(len(obs), len(EXP_OUTPUT_C1PF_TTFF))
    for i in range(0, len(obs)):
        eq_(obs[i].file_list, EXP_OUTPUT_C1PF_TTFF[i].file_list)

### Invalid name
@raises(SystemExit)
def test_iomanager_generate_output_invalid_name():
    IO_MANAGER.generate_output('FFFF', False, False, False, False)

@raises(SystemExit)
def test_iomanager_generate_output_invalid_name_empty():
    IO_MANAGER.generate_output('', False, False, False, False)

### Invalid cases: FTFT & TFTF & FTTT & TFTT & TTFT & TTTF & TTTT
@raises(SystemExit)
def test_iomanager_generate_output_invalid_case_FTFT():
    IO_MANAGER.generate_output('C2PT', False, True, False, True)

@raises(SystemExit)
def test_iomanager_generate_output_invalid_case_TFTF():
    IO_MANAGER.generate_output('C2PT', True, False, True, False)

@raises(SystemExit)
def test_iomanager_generate_output_invalid_case_FTTT():
    IO_MANAGER.generate_output('C2PT', False, True, True, True)

@raises(SystemExit)
def test_iomanager_generate_output_invalid_case_TFTT():
    IO_MANAGER.generate_output('C2PT', True, False, True, True)

@raises(SystemExit)
def test_iomanager_generate_output_invalid_case_TTFT():
    IO_MANAGER.generate_output('C2PT', True, True, False, True)

@raises(SystemExit)
def test_iomanager_generate_output_invalid_case_TTTF():
    IO_MANAGER.generate_output('C2PT', True, True, True, False)

@raises(SystemExit)
def test_iomanager_generate_output_invalid_case_TTTT():
    IO_MANAGER.generate_output('C2PT', True, True, True, True)
