#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

from lib.Step import *

class Symlinks(Step):
    def _set_step_specific_values(self):
        self.name = "Symlinks"
        self.merge_status = False
        self.pair_status = False

    def _get_command(self, dependencies, outputs):
        command = ""
        command += "\tln -sf $< $@"
        return(command)

    def _set_default_params(self):
        self.params['raw_dir'] = 'raw_data'
        self.params['dir_name'] = 'data'
        self.params['suffix'] = '.fastq.gz'

    def _validate_param_step_specific(self, inputs, outputs):
        pass
