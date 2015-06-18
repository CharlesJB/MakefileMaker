#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2015-05-11

import sys
import os

from lib.Step import *

class PeakCall(Step):
    def _set_step_specific_values(self):
        self.name = __name__.split('.')[1]
        self.design_status = True

    def _get_command(self, dependencies, outputs):
        command = "\tmacs2 callpeak \\\n"
        command += "\t\t-t "
        command += " ".join(dependencies[0].unlist())
        command += " \\\n"
        command += "\t\t-c "
        command += " ".join(dependencies[1].unlist())
        command += " \\\n"
        command += "\t\t-f BAM \\\n"
        command += "\t\t-g " + self.params['gsize']
        if self.params['extra'] is not None:
            command += " \\\n"
            command += "\t\t" + self.params['extra']
        return(command)

    def _set_default_params(self):
        self.params['dir_name'] = 'peaks'
        self.params['suffix'] = '_peaks.narrowPeak'
        self.params['gsize'] = "hs"
        self.params['extra'] = None

    def _validate_param_step_specific(self, inputs, outputs):
        pass
