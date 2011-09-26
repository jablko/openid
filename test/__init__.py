import os, sys, untwisted
from testify import *
from twisted.internet import reactor
from untwisted import db

db.connect = lambda *args, **kwds: None

run = reactor.run
reactor.run = lambda: None

sys.path.insert(0, os.path.dirname(__file__) + '/..')

execfile(os.path.dirname(__file__) + '/../openid')

def sdfg(cbl):
  cbl()

  reactor.callLater(2, reactor.stop)
  run()
