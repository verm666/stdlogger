from __future__ import print_function
from time import time
from socket import getfqdn, gethostname, socket, AF_INET, SOCK_DGRAM
from StringIO import StringIO
import zlib
import json

class Output(object):
    """
    Class to redirect logs from stdout to graylog2 server
    """

    def __init__(self, graylog_server='127.0.0.1', graylog_port=12011,
                        level=1, facility='local1',
                        max_buffer_size=1400,
                        host=getfqdn(gethostname())):

        # connection settings
        self.graylog_server = graylog_server
        self.graylog_port = graylog_port

        # GELF settings
        self.version = '1.0'
        self.host = host
        self.level = level
        self.facility = facility

        self.socket = socket(AF_INET,SOCK_DGRAM)
        self.buf = StringIO()
        self.max_buffer_size = max_buffer_size

    def send(self, message):
        z = zlib.compress(json.dumps(message))
        self.buf.write(z)
        print("Current buffer size: %i" % self.buf.len)
        if self.buf.len >= self.max_buffer_size:
            self.socket.sendto(self.buf.getvalue(),(self.graylog_server,self.graylog_port))
            self.buf.truncate(0)

    def processing(self, line):
        """
        Processing line (send line to Graylog2 server)
        """
        timestamp = int(time())
        short_message = line.strip()
        message = {
            'version': self.version,
            'host': self.host,
            'facility': self.facility,
            'level': self.level,
            'timestamp': timestamp,
            'short_message': short_message
        }
        #try:
        self.send(message)
        #except:
        #    print("ERROR sending message")
