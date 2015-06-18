from nose.tools import *
from Steps.Align import *
from lib.IOManager import *

VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_CONFIG="raw_data/valid.ini"
IO_MANAGER = IOManager(VALID_SAMPLESHEET)

def test_symlinks_step_constructor():
    align = Align([VALID_CONFIG])
    eq_(align.name, "Align")
    eq_(align.params['dir_name'], "align")
    eq_(align.pair_status, True)
    eq_(align.merge_status, False)
    eq_(align.keep_pair_together_status, False)
    eq_(align.get_step_specific_variables(), None)
    inputs = IO_MANAGER.generate_inputs(False, False, False, True)
    outputs = IO_MANAGER.generate_outputs(False, False, False, True)
    eq_(len(inputs), len(outputs))
    exp = "align/test1.bam: test1_R1 test1_R2\n"
    exp += "\tbwa mem \\\n"
    exp += "\t\tgenome.fa\\\n"
    exp += "\t\t$^ \\\n"
    exp += "\t\t\ samtools view -bSh - > $@"
    eq_(align.produce_recipe(inputs[0], outputs[0]), exp)
    exp = "align/test2.bam: test2_R1 test2_R2\n"
    exp += "\tbwa mem \\\n"
    exp += "\t\tgenome.fa\\\n"
    exp += "\t\t$^ \\\n"
    exp += "\t\t\ samtools view -bSh - > $@"
    eq_(align.produce_recipe(inputs[1], outputs[1]), exp)
