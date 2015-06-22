from nose.tools import *
from Steps.Trim import *
from lib.IOManager import *

VALID_SAMPLESHEET = "raw_data/valid_samplesheet.txt"
VALID_CONFIG="raw_data/valid.ini"
IO_MANAGER = IOManager(VALID_SAMPLESHEET)

def test_trim_step_constructor():
    trim = Trim([VALID_CONFIG])
    eq_(trim.name, "Trim")
    eq_(trim.params['dir_name'], "trim")
    eq_(trim.pair_status, False)
    eq_(trim.merge_status, False)
    eq_(trim.keep_pair_together_status, True)
    eq_(trim.get_step_specific_variables(), None)
    inputs = IO_MANAGER.generate_inputs(False, False, False, True)
    outputs = IO_MANAGER.generate_outputs_pair(False, False, False, True)
    eq_(len(inputs), len(outputs))
    exp = "trim/test1_R1.trim.fastq.gz trim/test1_R2.trim.fastq.gz: test1_R1 test1_R2\n"
    exp += "\tjava -jar ${TRIMMOMATIC_JAR} \\\n"
    exp += "\t\tPE -phred33 \\\n"
    exp += "\t\ttest1_R1 test1_R2 \\\n"
    exp += "\t\ttrim/test1_R1.trim.fastq.gz \\\n"
    exp += "\t\ttrim/test1_R1.unpaired.trim.fastq.gz \\\n"
    exp += "\t\ttrim/test1_R2.trim.fastq.gz \\\n"
    exp += "\t\ttrim/test1_R2.unpaired.trim.fastq.gz \\\n"
    exp += "\t\tILLUMINACLIP:adaptors.fa:2:30:10 \\\n"
    exp += "\t\tMINLEN:36 \\\n"
    exp += "\t\tTRAILING:30"
    eq_(trim.produce_recipe(inputs[0], outputs[0]), exp)
    exp = "trim/test2_R1.trim.fastq.gz trim/test2_R2.trim.fastq.gz: test2_R1 test2_R2\n"
    exp += "\tjava -jar ${TRIMMOMATIC_JAR} \\\n"
    exp += "\t\tPE -phred33 \\\n"
    exp += "\t\ttest2_R1 test2_R2 \\\n"
    exp += "\t\ttrim/test2_R1.trim.fastq.gz \\\n"
    exp += "\t\ttrim/test2_R1.unpaired.trim.fastq.gz \\\n"
    exp += "\t\ttrim/test2_R2.trim.fastq.gz \\\n"
    exp += "\t\ttrim/test2_R2.unpaired.trim.fastq.gz \\\n"
    exp += "\t\tILLUMINACLIP:adaptors.fa:2:30:10 \\\n"
    exp += "\t\tMINLEN:36 \\\n"
    exp += "\t\tTRAILING:30"
    eq_(trim.produce_recipe(inputs[1], outputs[1]), exp)
