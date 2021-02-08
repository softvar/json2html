# -*- coding: utf-8 -*-
import os, sys

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from functools import wraps
from time import time
from json2html import *

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print 'func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts)
        return result
    return wrap

@timing
def run(nesting=1000):
    benchdata = {}
    current_head = benchdata
    for i in xrange(nesting):
        current_head["test"] = {}
        current_head = current_head["test"]
    current_head["finally"] = "glob"
    json2html.convert(benchdata)

sys.setrecursionlimit(100000)
run(int(sys.argv[1]) if len(sys.argv) > 1 else 1000)