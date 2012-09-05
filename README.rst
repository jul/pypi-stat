All the docs are on 
http://pypi-stat.readthedocs.org
and when rtds don't work fall back here
http://packages.python.org/pypi-stat/
Source:
http://github.com/jul/pypi-stat
Ticket
http://github.com/jul/pypi-stat/issues


Getting stats
=============
usage::

    usage: pypi_get_stat.py [-h] [-q] [package_name [package_name ...]]

    Gathers download stats from pypi regarding the download information of the
    geiven package. Print them, and stores them in a file for further use. If no
    package name are provided, it will try to get all packages known from
    previously fetched stats. -q will print less output (only warnings and errors)

    positional arguments:
        package_name  package name to be retrieved

    optional arguments:
        -h, --help    show this help message and exit
        -q, --quiet   less verbose output


Graphing stats
==============
usage::
   
   usage: pypi_graph_stat.py [options]

    options:
      -h, --help            show this help message and exit
      -k KEY                keys to plot in stored stats amongst av_dl, total_dl,
                            min_dl','max_dl'
      -f _FROM, --from=_FROM
                            min date from which to plot
      -t _TO, --to=_TO      maximum date to which to plot
      -o _DEST, --output=_DEST
                                 filename of the output image. Don't create output
                            directory if non existant. If this is enabled output
                            in TK backend is desactivated.
      -p _PACKAGE, --package=_PACKAGE
                            packages for wich to graph

You'll need matplotlib and numpy to plot the graphs. Read the doc (installation 
section) for more informations.

Changelog
=========

* fighting debian and my typos
* fixing a dependency. I really like the install fails before test mechanisms
but if nobody opens a ticket I won't be able to know that it fails. 


