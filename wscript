#! /usr/bin/env python
# encoding: utf-8

from waflib.Build import BuildContext

APPNAME = 'YaFFT'
VERSION = '0.1'

top = '.'
out = 'build'


def options(opt):
    opt.add_option('--variant',
                   action='store',
                   choices=['debug', 'release'],
                   default='debug',
                   help='build variant (debug/release) [default: debug]')
    opt.add_option('--test',
                   action='store_true',
                   help='build tests')
    opt.add_option('--example',
                   action='store_true',
                   help='build examples')

    opt.load('compiler_c')
    opt.load('python')


def configure(conf):
    print('Configuring YaFFT in ' + conf.path.abspath())

    conf.env.TEST = conf.options.test

    # Debug variant
    conf.setenv('debug')

    conf.load('compiler_c')
    conf.load('python')
    conf.load('swig')
    conf.env.CFLAGS = ['-g', '-O0', '-Wall', '-std=c99']
    conf.env.TEST = conf.options.test
    conf.env.EXAMPLE = conf.options.example
    conf.check_python_headers()
    conf.check_python_version((2, 5, 0))
    if conf.check_swig_version() < (3, 0, 0):
        conf.fatal('Swig version must be >= 3.0.0')

    conf.write_config_header('debug/config.h', remove=False)

    # Release variant
    conf.setenv('release', env=conf.env.derive())  # start with a copy

    conf.env.CFLAGS = ['-O2', '-Wall', '-std=c99']

    conf.write_config_header('release/config.h')


def build(bld):
    if not bld.variant:
        bld.fatal('Build variant not specified')
    print('Build variant: ' + bld.variant)

    source_files = [x for x in bld.path.ant_glob('src/**/*.c')]

    # Shared library
    bld.shlib(source=source_files[:],
              target='yafft',
              includes='src')

    # SWIG interface for tests
    if bld.env.TEST:
        source_files.append('swig/yafft.i')
        bld.shlib(features='pyext',
                  source=source_files[:],
                  target='_yafft',
                  swig_flags='-python -Wall',
                  includes='. src')

    # Program for examples
    if bld.env.EXAMPLE:
        bld.program(source='example/sine.c',
                    target='example/sine',
                    use='yafft',
                    includes='src',
                    lib='m')


def init(ctx):
    from waflib.Options import options
    from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext
    from waflib.Configure import ConfigurationContext
    for y in (BuildContext, CleanContext, InstallContext, UninstallContext, ConfigurationContext):
        name = y.__name__.replace('Context', '').lower()

        class tmp(y):
            cmd = name
            variant = options.variant


def test(ctx):
    if not ctx.env.TEST:
        ctx.fatal('Test flag not specified during configuration')
    from test import test_suite
    test_suite.run()


class TestSubclass(BuildContext):
        cmd = 'test'
        fun = 'test'
