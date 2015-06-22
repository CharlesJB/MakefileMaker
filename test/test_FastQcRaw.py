from nose.tools import *
from Steps.FastQcRaw import *
from lib.IOManager import *

VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_CONFIG="raw_data/valid.ini"
IO_MANAGER = IOManager(VALID_SAMPLESHEET)

def test_fastqcraw_step_constructor():
    fastqcraw = FastQcRaw([VALID_CONFIG])
    eq_(fastqcraw.name, "FastQcRaw")
    eq_(fastqcraw.params['dir_name'], "qc/raw")
    eq_(fastqcraw.pair_status, False)
    eq_(fastqcraw.merge_status, False)
    eq_(fastqcraw.keep_pair_together_status, False)
    eq_(fastqcraw.get_step_specific_variables(), None)
    inputs = IO_MANAGER.generate_inputs(False, False, False, False)
    outputs = IO_MANAGER.generate_outputs(False, False, False, False)
    eq_(len(inputs), len(outputs))
    exp = "qc/raw/test1_R1/fastqc_report.html: test1_R1\n"
    exp += "\tfastqc \\\n"
    exp += "\t\t-o $(dir $@) \\\n"
    exp += "\t\t-t 1 \\\n"
    exp += "\t\t$<"
    eq_(fastqcraw.produce_recipe(inputs[0], outputs[0]), exp)
    exp = "qc/raw/test1_R2/fastqc_report.html: test1_R2\n"
    exp += "\tfastqc \\\n"
    exp += "\t\t-o $(dir $@) \\\n"
    exp += "\t\t-t 1 \\\n"
    exp += "\t\t$<"
    eq_(fastqcraw.produce_recipe(inputs[1], outputs[1]), exp)
    exp = "qc/raw/test2_R1/fastqc_report.html: test2_R1\n"
    exp += "\tfastqc \\\n"
    exp += "\t\t-o $(dir $@) \\\n"
    exp += "\t\t-t 1 \\\n"
    exp += "\t\t$<"
    eq_(fastqcraw.produce_recipe(inputs[2], outputs[2]), exp)
    exp = "qc/raw/test2_R2/fastqc_report.html: test2_R2\n"
    exp += "\tfastqc \\\n"
    exp += "\t\t-o $(dir $@) \\\n"
    exp += "\t\t-t 1 \\\n"
    exp += "\t\t$<"
    eq_(fastqcraw.produce_recipe(inputs[3], outputs[3]), exp)
