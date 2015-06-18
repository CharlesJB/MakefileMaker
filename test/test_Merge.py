from nose.tools import *
from Steps.Merge import *
from lib.IOManager import *

VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_CONFIG="raw_data/valid.ini"
IO_MANAGER = IOManager(VALID_SAMPLESHEET)

def test_merge_step_constructor():
    merge = Merge([VALID_CONFIG])
    eq_(merge.name, "Merge")
    eq_(merge.params['dir_name'], "align")
    eq_(merge.pair_status, False)
    eq_(merge.merge_status, True)
    eq_(merge.keep_pair_together_status, False)
    eq_(merge.get_step_specific_variables(), None)
    inputs = IO_MANAGER.generate_inputs(False, False, False, True)
    outputs = IO_MANAGER.generate_outputs(False, False, False, True)
    eq_(len(inputs), len(outputs))
    exp = "align/test1.merged.bam: test1_R1 test1_R2\n"
    exp += "samtools merge $^ > $@"
    eq_(merge.produce_recipe(inputs[0], outputs[0]), exp)
    exp = "align/test2.merged.bam: test2_R1 test2_R2\n"
    exp += "samtools merge $^ > $@"
    eq_(merge.produce_recipe(inputs[1], outputs[1]), exp)
