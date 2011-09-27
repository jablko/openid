import os, sys, untwisted
from testify import *
from twisted.internet import reactor
from untwisted import db

class connect:
  def __init__(ctx, *args, **kwds):
    pass

db.connect = connect

@untwisted.call
class random:
  pass

__import__('random').random = random

run = reactor.run
reactor.run = lambda: None

sys.path.insert(0, os.path.dirname(__file__) + '/..')

globals = {}
execfile(os.path.dirname(__file__) + '/../openid', globals)

def sdfg(cbl):
  cbl()

  reactor.callLater(2, reactor.stop)
  run()
