#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vector_dict.VectorDict import VectorDict as vd,convert_tree
from vector_dict.SparseMatrix import SparseMatrix


from os import path, environ
from json import load
from datetime import datetime as dt
from matplotlib import dates
from optparse import OptionParser
from numpy import array

##################### WORKFLOW ######################
###### parsing
###### querying
###### plotting
#####################################################

################# PARSING CLI #################################################
parser = OptionParser()
_key = ['total_dl' ]
parser.add_option("-k", dest="key",
    help='''keys to plot in stored stats amongst av_dl, total_dl, min_dl','max_dl' ''' ,
    action = 'append' ,
)

parser.add_option("-f",'--from', dest="_from",
    help='min date from which to plot', default = ''
)

parser.add_option("-t",'--to', dest="_to",
    help='maximum date to which to plot',
    default = dt.now().date().isoformat()
)

parser.add_option("-o",'--output', dest="_dest",
    help="""
    filename of the output image. Don't create output directory if non existant.
If this is enabled output in TK backend is desactivated.
    """,
    action='store'
)
parser.add_option("-p",'--package', dest="_package",
    help='packages for wich to graph',
    action='append'
    )

(options, args) = parser.parse_args()

#################### QUERYING DATA ############################################



my_filter = lambda sequence : filter(
        lambda r :  options._to >= r['date'] > options._from ,sequence
    )
all_filter = my_filter
if options._package:
    all_filter = lambda sequence : filter(
        lambda x : x["name"] in options._package, my_filter(sequence)
    )

_key = options.key  or _key
save=path.join(environ["HOME"], ".pipy.stat.json" )
result = load(open(save))

res = reduce( vd.__add__,
    map(
        lambda x : convert_tree(
            {
                x["name"] : dict(
                    date =[ dates.date2num(dt.strptime(x['date'],"%Y-%m-%d")) ],
                )
            }) + convert_tree(
                {  x['name'] :
                    dict( ( key, [  int(x[key]) ] ) for key in _key)
            }) + convert_tree( {
                x["name"] : {
                    'release' :  { x["last_release"] :
                    [ x['last_upload'] ] }
                    }}
            ),
            sorted(
                all_filter(
                    result
                ),
                key = lambda r : r["name"]
            )
    )
)

options._package = res.keys()

################## PLOTTING ############################################################
import matplotlib
matplotlib.use(options._dest and "Agg" or "TkAgg")

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
K = 1000
YMAX_BUG=80*K

total_plot = len(res)
fig = plt.figure(figsize = ( 8 , total_plot * 3  ))
min_date, max_date = None,None

ax1 = None
ax = None

for cursor, (name, data) in enumerate(res.iteritems()):
    if cursor != 0 :
        ax = fig.add_subplot( (100 * total_plot) + (10) + (cursor + 1), sharex=ax1)
    else:
        ax = fig.add_subplot(total_plot * 100 + 11 )
        ax1= ax

    _plot = []
    for key in _key:
        min_date = min_date and \
            min( min(data["date"]), min_date) or \
            min(data["date"])
        max_date = max_date and \
            max( max(data["date"]), max_date) or \
            max(data["date"])

    ymax=0
    for key in _key:
        ymax = max(max(data[key]), ymax)
        _plot += [ ax.plot_date( array(data["date"]), array(data[key], int),  '.-' , label = key) ]
    if ymax > YMAX_BUG:
        ax.yaxis.set_major_formatter(FuncFormatter(
            lambda x, pos: ('%.1f')%(x*1e-3))
        )
        ax.set_ylabel('K (1E3)')

        
        

    ax.legend(  loc=2,)

    for label, date in data["release"].iteritems():
        ax.annotate( "release\n" + label,
            xy = (
                dates.date2num(dt.strptime(date[0][0:10],"%Y-%m-%d"  )),
                ax.get_ybound()[0] + 1
            ),
            horizontalalignment='center', verticalalignment='center',
            xytext = (
                 dates.date2num(dt.strptime(date[0][0:10],"%Y-%m-%d"  )),
                 sum(ax.get_ybound())  / 2
            ),
            arrowprops=dict(facecolor='black')
        )

    plt.xlim([ min_date, max_date])

    ax.set_title( "Statistic for %s" % (name) )

fig.autofmt_xdate()
plt.autoscale(axis = 'y')
plt.subplots_adjust( top = 0.95, bottom=0.12, left=0.12,right=.95)
plt.draw()

if options._dest:
    plt.savefig( options._dest )
else:
    plt.show()

