#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

from lib.Step import *

class Merge(Step):
    def _set_step_specific_values(self):
        self.name = __name__.split('.')[1]
        self.merge_status = True
        self.pair_status = False

    def _get_command(self, dependencies, outputs):
        command = "samtools merge $^ > $@"
        return(command)

    def _set_default_params(self):
        self.params['dir_name'] = 'align'
        self.params['suffix'] = '.merged.bam'

    def _validate_param_step_specific(self, inputs, outputs):
        pass
