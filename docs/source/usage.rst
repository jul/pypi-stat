pypi_get_stat usage :
=====================

.. literalinclude::
    pypi_get_stat.rst

Interest ? 

 * pypi stats are a daily snapshot of the cumulated information. In order to make
time plot, we need this scripts to be called in a crontab and stored passed data. 
 * Daily data are stored in ~/.pypi.stat.json and available for future use. 
 * If no packages are given in input, the script will try all packages already 
fetched and whose name are seen in .pypi.stat.json

TODO For crontab I should make a silent version

pypi_graph_stat usage :
=======================

.. literalinclude::
    pypi_grah_stat.rst

Graphing for a package with a direct output in tk
*************************************************


``pypi_graph_stat.py -p VectorDict``


Result : 



..  image:: image/sample1.png

Graphing all known package in a file
************************************

 pypi_graph_stat.py -o docs/source/image/sample2.png


..  image:: image/sample2.png

Graphing all keys for two packages
**********************************

 pypi_graph_stat.py -k av_dl -k min_dl -k max_dl -k total_dl -p VectorDict -p pypi-stat

..  image:: image/sample3.png

Graphing between two dates
**************************

 pypi_graph_stat.py -f 2012-04-01 -t 2012-04-15 -p VectorDict 

..  image:: image/sample4.png


