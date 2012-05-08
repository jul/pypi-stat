#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
mixed query on stat file
"""
from os import environ, path
from json import load
from vector_dict.VectorDict import VectorDict as krut
from vector_dict.VectorDict import convert_tree as kruter
import datetime as dt
import time

__all__ = [ 'all_package', "data_for" ]
def generate(
    _map = lambda x : x,
    _reduce = lambda x,y : x+y, 
    _filter = lambda x: True
    ):
    saved=path.join(environ["HOME"], ".pipy.stat.json"  )
    with open(saved) as f:
        return  reduce( 
            _reduce,
            map( 
                _map,
                filter(
                    _filter,
                    sorted( 
                        load(f), 
                        key = lambda x : x["date"], reverse = True
                    )
                )
            )
        )
def date_to_js_timestamp(_date_str):
    """convert YYYY-MM-DD in javascript timestamp format"""
    return int( 
            time.mktime( 
                dt.date( 
                    *[ int(i) for i in _date_str.split("-") ]
                ).timetuple()
            )*1000
    )
    
all_package = lambda : generate(lambda x : set( [  x['name'] ]  ),set.union)
data_for = lambda package,key : generate(
    lambda x : [ ( 
            date_to_js_timestamp( x['date']),
            x[key]
        ) ],
    list.__add__,
    lambda x : x['name'] ==  package 
)
#data_for = lambda package : generate( 
#    lambda x : 
#print all_package()
#print stat_list()


   

