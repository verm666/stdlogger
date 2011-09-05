#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
import os

class Output(object):

    """
    Class for redirect logs to file.
    """

    def __init__(self, **kwargs):
        print("[DEBUG] : %s" % str(kwargs))
        # set filename
        if 'filename' not in kwargs:
            raise ValueError("param 'filename' is required")
        self.filename = kwargs['filename']
        try:
            self.file = open(self.filename, 'a')
        except IOError:
            print("Could not open file: %s" % self.filename)

        # set max_size
        if 'max_size' not in kwargs:
            self.max_size = 2048
        else:
            self.max_size = int(kwargs['max_size'])

        # set count
        if 'count' not in kwargs:
            self.count = 10
        else:
            self.count = int(kwargs['count'])

    def __rotate__(self):
        """
        Size based and date based rotation
        """

        # Size based rotation
        size = os.path.getsize(self.filename)
        if size >= self.max_size:
            for i in range(self.count - 1, 0, -1):
                try:
                    os.rename(self.filename + "." + str(i), self.filename + "." + str(i + 1))
                except OSError:
                    pass

            os.rename(self.filename, self.filename + ".1")
            self.file.close()
            self.file = open(self.filename, 'a')

        # Data based rotation
        # TODO: Do it.

    def processing(self, line):
        """
        Processing line (write line to file/rotate files)
        """

        self.file.write(line)
        self.__rotate__()
