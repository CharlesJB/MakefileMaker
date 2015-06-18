from nose.tools import *
from Steps.Sort import *
from lib.IOManager import *

VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_CONFIG="raw_data/valid.ini"
IO_MANAGER = IOManager(VALID_SAMPLESHEET)

def test_sort_step_constructor():
    sort = Sort([VALID_CONFIG])
    eq_(sort.name, "Sort")
    eq_(sort.params['dir_name'], "align")
    eq_(sort.pair_status, False)
    eq_(sort.merge_status, False)
    eq_(sort.keep_pair_together_status, False)
    eq_(sort.get_step_specific_variables(), None)
    inputs = IO_MANAGER.generate_inputs(False, False, False, True)
    outputs = IO_MANAGER.generate_outputs(False, False, False, True)
    eq_(len(inputs), len(outputs))
    exp = "align/test1.sort.bam: test1_R1 test1_R2\n"
    exp += "samtools sort \\\n"
    exp += "-O bam \\\n"
    exp += "-T $@.tmp \\\n"
    exp += "-@ 1\\\n"
    exp += "$< > $@"
    eq_(sort.produce_recipe(inputs[0], outputs[0]), exp)
    exp = "align/test2.sort.bam: test2_R1 test2_R2\n"
    exp += "samtools sort \\\n"
    exp += "-O bam \\\n"
    exp += "-T $@.tmp \\\n"
    exp += "-@ 1\\\n"
    exp += "$< > $@"
    eq_(sort.produce_recipe(inputs[1], outputs[1]), exp)
