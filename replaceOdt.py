# -*- coding: utf-8 -*-
"""
Created on Mon May 12 15:24:07 2014

@author: peterb
"""

#!python
from relatorio.templates.opendocument import Template
from ipc_data import letter_data
basic = Template(source="IPC_DATA", filepath='IPC_ger_Letter.odt')
basic_generated = basic.generate(o=letter_data).render()
file('IPC_FULL.odt', 'wb').write(basic_generated.getvalue())