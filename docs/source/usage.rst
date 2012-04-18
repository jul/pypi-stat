pypi_get_stat usage :
=====================

.. literalinclude::
    pypi_get_stat.rst

Interest ? 

Pypi stats are a daily snapshot of the cumulated information. In order to make
time plot, we need this scripts to be called in a crontab. 

Daily data are therefore stored in ~/.pypi.stat.json and available for future use. 


If no packages are given in input, the script will try all packages already 
fetched and whose name are seen in .pypi.stat.json

For crontab I should make a silent version

pypi_graph_stat usage :
=====================

