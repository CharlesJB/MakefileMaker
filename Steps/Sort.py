#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

from lib.Step import *

class Sort(Step):
    def _set_step_specific_values(self):
        self.name = __name__.split('.')[1]
        self.merge_status = False
        self.pair_status = False

    def _get_command(self, dependencies, outputs):
        command = "\tsamtools sort \\\n"
        command += "\t\t-O bam \\\n"
        command += "\t\t-T $@.tmp \\\n"
        command += "\t\t-@ " + str(self.params['threads']) + " \\\n"
        command += "\t\t$< > $@"
        return(command)

    def _set_default_params(self):
        self.params['dir_name'] = 'align'
        self.params['suffix'] = '.sort.bam'
        self.params['threads'] = 1

    def _validate_param_step_specific(self, inputs, outputs):
        pass
