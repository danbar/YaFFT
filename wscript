#! /usr/bin/env python
# encoding: utf-8

APPNAME = 'YaFFT'
VERSION = '0.1'

top = '.'
out = 'build'

def options(opt):
    opt.add_option('--foo', action='store', default=False, help='Silly test')

    opt.load('compiler_c')
    opt.load('python')

def configure(conf):
    print('Configuring YaFFT in ' + conf.path.abspath())

    conf.load('compiler_c')
    conf.load('python')
    conf.load('swig')

    conf.check_python_version((2,4,2)) # TODO
    conf.check_python_headers()
    if conf.check_swig_version() < (1, 2, 27): # TODO
        conf.fatal('this swig version is too old')

def build(bld):
    print('Building YaFFT in ' + bld.path.abspath())

    bld.shlib(features='pyext',
              source='src/yafft.c swig/yafft.i',
              target='_yafft',
              cflags='-std=c99',
              swig_flags='-python -Wall',
              includes='. src')

def test(ctx):
    from test import test_suite
    test_suite.run()

