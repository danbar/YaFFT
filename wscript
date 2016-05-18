#! /usr/bin/env python
# encoding: utf-8

from test import test_suite

APPNAME = 'YaFFT'
VERSION = '0.1'

top = '.'
out = 'build'

def options(ctx):
    ctx.add_option('--foo', action='store', default=False, help='Silly test')

def configure(ctx):
    print('→ configuring the project in ' + ctx.path.abspath())

def build(ctx):
    pass

def test(ctx):
    test_suite.run()

