#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

from lib.Step import *

class Align(Step):
    def _set_step_specific_values(self):
        self.name = "Align"
        self.merge_status = False
        self.pair_status = True

    def _get_command(self, dependencies, outputs):
        command = ""
        command += "\tbwa mem \\\n"
        command += "\t\t" + self.params['genome'] + "\\\n"
        command += "\t\t$^ \\\n"
        command += "\t\t\ samtools view -bSh - > $@"
        return(command)

    def _set_default_params(self):
        self.params['dir_name'] = 'align'
        self.params['suffix'] = '.bam'
        self.params['genome'] = 'genome.fa'

    def _validate_param_step_specific(self, inputs, outputs):
        pass
