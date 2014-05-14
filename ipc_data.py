# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:13:54 2014

@author: peterb
"""

class LetterData(dict):
    pass


letter_data = LetterData(
    toData={'CompanyName':'Soap and more',
                        'Department':'IPC',
                        'FirstName': 'Peter',
                         'LastName': 'Bonanati',
                         'Title': 'Dipl. Phys.',
                         'Address': {'Street': 'Memelweg 9',
                                     'Zip': 72072,
                                     'City': 'Tuebingen'},
                          'Tel' : {'Tel':"070715668956",
                                   'Fax':"07071456575" },
                           'EMail':'Peter.Bonanati@gmail.com'},
    fromData={'CompanyName':'Universitaet Tübingen',
                        'Department':'IPC',
                        'FirstName': 'Peter',
                         'LastName': 'Bonanati',
                         'Title': 'Dipl. Phys.',
                         'Address': {'Street': 'Memelweg 9',
                                     'Zip': 72072,
                                     'City': 'Tuebingen'},
                          'Tel':{'Tel':"070715668956",
                                 'Fax':"07071456575" },
                           'EMail':'Peter.Bonanati@gmail.com'},
    )