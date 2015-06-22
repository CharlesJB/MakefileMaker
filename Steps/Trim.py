#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

from lib.Step import *

class Trim(Step):
    def _set_step_specific_values(self):
        self.name = __name__.split('.')[1]
        self.merge_status = False
        self.pair_status = False
        self.keep_pair_together_status = True

    def _get_command(self, dependencies, outputs):
        dir_name = self.params['dir_name']
        suffix = self.params['suffix']
        command = "\tjava -jar ${TRIMMOMATIC_JAR} \\\n"
        if dependencies[0].get_paired_status():
            command += "\t\tPE --phred" + str(self.params['phred']) + " \\\n"
            command += "\t\t" + dependencies[0].unlist()[0]
            if dependencies[0].get_paired_status():
                command += " " + dependencies[0].unlist()[1]
            command += " \\\n"
            base_output = dir_name + "/" + outputs.unlist()[0]
            command += "\t\t" + base_output + suffix + " \\\n"
            command += "\t\t" + base_output + ".unpaired" + suffix + " \\\n"
            base_output = dir_name + "/" + outputs.unlist()[1]
            command += "\t\t" + base_output + suffix + " \\\n"
            command += "\t\t" + base_output + ".unpaired" + suffix + " \\\n"
        else:
            command += "\t\tSE --phred" + str(self.params['phred']) + " \\\n"
            command += "\t\t" + dependencies[0].unlist()[0] + " \\\n"
            command += "\t\t" + outputs.unlist()[0] + " \\\n"
        command += "\t\tILLUMINACLIP:" + self.params['adaptors']
        command += ":" + self.params['ILLUMINACLIP'] + " \\\n"
        command += "\t\tMINLEN:" + str(self.params['MINLEN']) + " \\\n"
        command += "\t\tTRAILING:" + str(self.params['TRAILING'])
        return(command)

    def _set_default_params(self):
        self.params['dir_name'] = 'trim'
        self.params['suffix'] = '.trim.fastq.gz'
        self.params['adaptors'] = 'adaptors.fa'
        self.params['phred'] = 33
        self.params['MINLEN'] = 36
        self.params['TRAILING'] = 30
        self.params['ILLUMINACLIP'] = '2:30:10'

    def _validate_param_step_specific(self, inputs, outputs):
        pass
