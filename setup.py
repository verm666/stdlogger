from distutils.core import setup

setup(name='Stdlogger',
      version='1.0',
      description='Redirect logs from stdin to stdout / file / syslog / etc',
      author='Eduard Snesarev',
      author_email='verm666@gmail.com',
      url='https://github.com/verm666/stdlogger',
      packages=['stdlogger', 'stdlogger.outputs'],
      scripts=['bin/stdlogger']
     )
