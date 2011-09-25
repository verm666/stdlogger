from __future__ import print_function
from time import time
from socket import getfqdn, gethostname

class Output(object):
    """
    Class to redirect logs from stdout to graylog2 server
    """

    def __init__(self, graylog_server='127.0.0.1', graylog_port='12011', host=getfqdn(gethostname())):

        # connection settings
        self.graylog_server = graylog_server
        self.graylog_port = graylog_port

        # GELF settings
        self.version = '1.0'
        self.host = host
        self.level = level

        self.socket = socket(AF_INET,SOCK_DGRAM)

    def _send(message):
        z = zlib.compress(message)
        self.socket.sendto(z,(self.graylog_server,self.graylog_port))

    def processing(self, line):
        """
        Processing line (send line to Graylog2 server)
        """
        timestamp = int(time())
        short_message = strip(line)
        message = {
            'version': self.version,
            'host': self.host,
            'facility': self.facility,
            'level': level,
            'timestamp': timestamp,
            'short_message': short_message
        }
        try:
            self._send(message)
        except:
            printf("ERROR sending message")
