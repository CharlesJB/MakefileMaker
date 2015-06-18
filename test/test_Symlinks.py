from nose.tools import *
from Steps.Symlinks import *
from lib.IOManager import *

VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_CONFIG="raw_data/valid.ini"
IO_MANAGER = IOManager(VALID_SAMPLESHEET)

def test_symlinks_step_constructor():
    symlink = Symlinks([VALID_CONFIG])
    eq_(symlink.get_name(), "Symlinks")
    eq_(symlink.params['raw_dir'], "raw_data")
    eq_(symlink.params['dir_name'], "data")
    eq_(symlink.get_pair_status(), False)
    eq_(symlink.get_merge_status(), False)
    eq_(symlink.get_keep_pair_together_status(), False)
    eq_(symlink.get_step_specific_variables(), None)
    inputs = IO_MANAGER.generate_inputs_raw_data(False, False)
    outputs = IO_MANAGER.generate_outputs(False, False, False, False)
    eq_(len(inputs), len(outputs))
    exp = "data/test1_R1.fastq.gz: raw_data/a1_1.fastq.gz\n"
    exp += "\tln -sf $< $@"
    eq_(symlink.produce_recipe(inputs[0], outputs[0]), exp)
    exp = "data/test1_R2.fastq.gz: raw_data/a1_2.fastq.gz\n"
    exp += "\tln -sf $< $@"
    eq_(symlink.produce_recipe(inputs[1], outputs[1]), exp)
    exp = "data/test2_R1.fastq.gz: raw_data/a2_1.fastq.gz\n"
    exp += "\tln -sf $< $@"
    eq_(symlink.produce_recipe(inputs[2], outputs[2]), exp)
    exp = "data/test2_R2.fastq.gz: raw_data/a2_2.fastq.gz\n"
    exp += "\tln -sf $< $@"
    eq_(symlink.produce_recipe(inputs[3], outputs[3]), exp)
