from __future__ import print_function

class Output(object):
    """
    Class to redirect logs from stdout to stdout (example class)
    """

    def __init__(self, **kwargs):
        pass
    def processing(self, line):
        """
        Processing line (write to stdout)
        """

        print(line, end="")
