#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

from lib.Step import *

class FastQcRaw(Step):
    def _set_step_specific_values(self):
        self.name = __name__.split('.')[1]
        self.merge_status = False
        self.pair_status = False

    def _get_command(self, dependencies, outputs):
        basename = outputs.unlist()[0].split('/')[-1].split('.')[0]
        command = "\tfastqc \\\n"
        command += "\t\t-o $(dir $@) \\\n"
        command += "\t\t-t " + str(self.params['threads']) + " \\\n"
        command += "\t\t$<"
        return(command)

    def _set_default_params(self):
        self.params['dir_name'] = 'qc/raw'
        self.params['suffix'] = '/fastqc_report.html'
        self.params['threads'] = '1'

    def _validate_param_step_specific(self, inputs, outputs):
        pass
