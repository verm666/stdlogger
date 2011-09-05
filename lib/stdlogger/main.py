#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os

class StdLogger(object):
    def __init__(self, kind='stdout', **kwargs):
        m = __import__('outputs.' + kind, globals(), locals(), ['Output'], -1)
        self.output = m.Output(**kwargs)

    def run(self):
        line = sys.stdin.readline()
        while line:
            self.output.processing(line)
            line = sys.stdin.readline()
