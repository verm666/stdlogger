#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
from Queue import Queue
from threading import Thread
import sys
import os

class StdLogger(object):
    def __init__(self, kind='stdout', **kwargs):
        m = __import__('outputs.' + kind, globals(), locals(), ['Output'], -1)
        self.output = m.Output(**kwargs)
        self.q = Queue() # TODO: Think about limits (In MBs)
        self.porter = Thread(target=self.processing, args=())
        self.porter.daemon = True
        self.porter.start()

    def run(self):
        for line in sys.stdin:
            print("READ FROM STDIN: %s" % line)
            self.q.put(line)

    def processing(self):
        while True:
            line = self.q.get()
            self.output.processing(line)
            self.q.task_done()
