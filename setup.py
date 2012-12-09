#!/usr/bin/env python
# -*- coding: "utf-8" -*-

#from distutils.command.build_py import build_py as _build_py
from setuptools import setup
#from distutils.core import setup
#from distutil2 import setup
import sys


def func_test():
    from os import path, environ,unlink
    import shutil
    import subprocess
    from json import load
    to_backup=False
    abort=True
    save= path.join(environ["HOME"] , ".pipy.stat.json")
    try:
        if path.exists(save):
            print("backuping previous saved stat in %s to %s.original" % (
                save,save) )
            shutil.move(save, "%s.original" % save)
            to_backup=True

        test_dl=subprocess.call([ "python","./pypi_get_stat.py",'-q', 'archery' ])
        with open(path.join(environ["HOME"] , ".pipy.stat.json")) as  f:
            res=load(f)
            if any(map(lambda d:d.get("name", "") == 'archery', res)):
                abort=False
            else:
                print(
                "This package does not work as is, please open a ticket %s" % e)
                print("Error")
    except Exception as e:
        abort=True
        print(
        "This package does not work as is, please open a ticket %s" % e)
        print("Error")
    finally:
        if to_backup:
            unlink(save)
            shutil.move("%s.original" %save, save)
            print("restoring original stats in %s.original to %s" % (
                save,save)  )
    return not abort

if "sdist" in sys.argv or "install" in sys.argv or "bdist_egg" in sys.argv:
    if func_test():
        print( "###test are successful")
    else:
        print("arg")
        raise Exception("Test did not passed")

setup(
        name='pypi-stat',
        version='1.2.5',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        url= 'https://github.com/jul/pypi-stat',
        packages=[],
        scripts = [ 'pypi_get_stat.py', 'pypi_graph_stat.py' ],
        license="PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2",
        description='solution for getting packages stat, and graphing them',
        install_requires=[
                "numpy => 1.5.0",
                "matplotlib",
                "argparse",
        ],
        long_description=open("README.rst").read(),
        classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python :: 2.6',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python',
          ],
)
