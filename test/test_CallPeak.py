from nose.tools import *
from Steps.PeakCall import *
from lib.IOManager import *

VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_CONFIG="raw_data/valid.ini"
VALID_DESIGN="raw_data/valid_design_2_columns_2_groups.txt"
IO_MANAGER = IOManager(VALID_SAMPLESHEET, VALID_DESIGN)

def test_peakcall_step_constructor():
    peak_call = PeakCall([VALID_CONFIG])
    eq_(peak_call.name, "PeakCall")
    eq_(peak_call.params['dir_name'], "peaks")
    eq_(peak_call.pair_status, False)
    eq_(peak_call.merge_status, False)
    eq_(peak_call.keep_pair_together_status, False)
    eq_(peak_call.design_status, True)
    eq_(peak_call.get_step_specific_variables(), None)
    inputs = IO_MANAGER.generate_inputs_design()
    outputs = IO_MANAGER.generate_outputs_design()
    eq_(len(inputs), len(outputs))
    exp = "peaks/Exp2_peaks.narrowPeak: test2 test1\n"
    exp += "\tmacs2 callpeak \\\n"
    exp += "\t\t-t test2 \\\n"
    exp += "\t\t-c test1 \\\n"
    exp += "\t\t-f BAM \\\n"
    exp += "\t\t-g hs"
    eq_(peak_call.produce_recipe(inputs[0], outputs[0]), exp)
    exp = "peaks/Exp1_peaks.narrowPeak: test1 test2\n"
    exp += "\tmacs2 callpeak \\\n"
    exp += "\t\t-t test1 \\\n"
    exp += "\t\t-c test2 \\\n"
    exp += "\t\t-f BAM \\\n"
    exp += "\t\t-g hs"
    eq_(peak_call.produce_recipe(inputs[1], outputs[1]), exp)
