# -*- coding: utf-8 -*-
"""
Created on Wed May 14 08:22:51 2014

@author: peterb
"""
name="Peter"
for v in vCards:
    if name in str(v):
        print v['fn']['text']
#    if v.has_key('fn'):
#        if (v['fn'].has_key('text')) and v['fn']['text']:
#            if (name in v['fn']['text']):
#                print v['fn']['text']
#    