#! /usr/bin/env python
# encoding: utf-8

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

    opt.load('compiler_c')
    opt.load('python')


def configure(conf):
    print('Configuring YaFFT in ' + conf.path.abspath())

    # Debug variant
    conf.setenv('debug')

    conf.load('compiler_c')
    conf.load('python')
    conf.load('swig')
    conf.env.CFLAGS = ['-g', '-O0', '-Wall', '-std=c99']
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

    source_files = [x for x in bld.path.ant_glob('**/*.c', excl=['build/'])]
    source_files.append('swig/yafft.i')

    bld.shlib(features='pyext',
              source=source_files,
              target='_yafft',
              swig_flags='-python -Wall',
              includes='. src')


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
    from test import test_suite
    test_suite.run()
