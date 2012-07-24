#!/usr/bin/env pyrhon
# -*- coding: "utf-8" -*-

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup
import sys


#test()
def test():
    from os import path, environ,unlink
    import shutil
    import subprocess
    from json import load
    to_backup=False
    save= path.join(environ["HOME"] , ".pipy.stat.json")
    try:
        if path.exists(save):
            print("backuping previous saved stat in %s" % save)
            to_backup=True
            shutil.move(save, "%s.original" % save)

        test_dl=subprocess.call([ "./pypi_get_stat.py",'-q', 'archery' ])
        print( test_dl )

        with open(path.join(environ["HOME"] , ".pipy.stat.json")) as  f:
            res=load(f)
            if any(map(lambda d:d.get("name", "") == 'archery', res)):
                print( "success")
            else:
                raise Exception(
                "This package does not work as is, please open a ticket %s" % e)
    except Exception as e:
        raise Exception(
        "This package does not work as is, please open a ticket %s" % e)
        print("Error")
    finally:
        if to_backup:
            unlink(save)
            shutil.move("%s.original" %save, save)

if "install" in sys.argv or "bdist_egg" in sys.argv:
    test()
setup(
        name='pypi-stat',
        version='1.2.2',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        bugtrack_url='https://github.com/jul/pypi-stat/issues',
        url= 'https://github.com/jul/pypi-stat',
        packages=[],
        scripts = [ 'pypi_get_stat.py', 'pypi_graph_stat.py' ],
        license='LICENSE.txt',
        description='solution for getting packages stat, and graphing them',
        requires=['numpy', 'matplotlib','archery' ],
        classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
)
