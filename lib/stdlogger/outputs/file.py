#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import time

class Output(object):

    """
    Class for redirect logs to file.
    """

    def __init__(self, **kwargs):
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

        # set current date (used in 'date-based' and 'date-size-based' rotation.
        # see self.__rotate__()
        self.r_date = int(time.strftime("%Y%m%d")) # "run date"

    def __rotate__(self, kind='date'):
        """
        Size-based, date-based or both rotation
        """

        if kind == "size":
        # Size-based rotation
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

        elif kind == "date":
            # Date-based rotation
            c_date = int(time.strftime("%Y%m%d")) # "current date"
            if (self.r_date != c_date):
                os.rename(self.filename, self.filename + "." + str(c_date))
                self.file.close()
                self.file = open(self.filename, 'a')
                self.r_date = c_date

        elif kind == "date_size":
            pass

    def processing(self, line):
        """
        Processing line (write line to file/rotate files)
        """

        self.file.write(line)
        self.__rotate__()
