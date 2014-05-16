# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:13:54 2014

@author: peterb
"""
import json
import datetime


testString='{"sender":{"count":1,"first":0,"searchonly":false,"records":[{"name":"Dipl. Phys. Peter Bonanati","firstname":"Peter","surname":"Bonanati","prefix":"Dipl. Phys.","organization":"Universität Tübingen","department":"IPC - AG Weimar","birthday":"1983-02-23","uid":"00000000520C971F0B4BC54DB80796D6D8A174AD0100D55DC2685850C545B986B30DABB5F61C0000000190930000","changed":{"date":"2014-05-14 11:30:16","timezone_type":3,"timezone":"UTC"},"ID":"MDAwMDAwMDA1MjBDOTcxRjBCNEJDNTREQjgwNzk2RDZEOEExNzRBRDAxMDBENTVEQzI2ODU4NTBDNTQ1Qjk4NkIzMERBQkI1RjYxQzAwMDAwMDAxOTA5MzAwMDA","email:work":["peter.bonanati@ipc.uni-tuebingen.de"],"email:other":["peter.stueber@ipc.uni-tuebingen.de"],"phone:home":["070715668956"],"phone:mobile":["01633628843"],"phone:work":["07071-29-77633"],"phone:workfax":["07071-29-5963"],"address:work":[{"street":"Memelweg 9","locality":"Tübingen","zipcode":"72072","region":null,"country":"Germany"}]}]},"recipient":{"count":1,"first":0,"searchonly":false,"records":[{"name":"Dipl. Phys. Peter Bonanati","firstname":"Peter","surname":"Bonanati","prefix":"Dipl. Phys.","organization":"Universität Tübingen","department":"IPC - AG Weimar","birthday":"1983-02-23","uid":"00000000520C971F0B4BC54DB80796D6D8A174AD0100D55DC2685850C545B986B30DABB5F61C0000000190930000","changed":{"date":"2014-05-14 11:30:16","timezone_type":3,"timezone":"UTC"},"ID":"MDAwMDAwMDA1MjBDOTcxRjBCNEJDNTREQjgwNzk2RDZEOEExNzRBRDAxMDBENTVEQzI2ODU4NTBDNTQ1Qjk4NkIzMERBQkI1RjYxQzAwMDAwMDAxOTA5MzAwMDA","email:work":["peter.bonanati@ipc.uni-tuebingen.de"],"email:other":["peter.stueber@ipc.uni-tuebingen.de"],"phone:home":["070715668956"],"phone:mobile":["01633628843"],"phone:work":["07071-29-77633"],"phone:workfax":["07071-29-5963"],"address:work":[{"street":"Memelweg 9","locality":"Tübingen","zipcode":"72072","region":null,"country":"Germany"}],"sourceid":"SharedFolders_shared_ipc_intern"}]},"event":"plugin.ipc_brief.created"}'
testData={'date': '15.05.2014', 'recipient': {'fax': '', 'tel': u'+49 15782576830', 'firstname': u'Matthias', 'prefix': '', 'address': {}, 'department': '', 'organization': '', 'surname': u'B\xf6pple', 'email': u'matthias.boepple@student.uni-tuebingen.de'}, 'sender': {'fax': [u'07071-29-5963'], 'tel': u'07071-29-77633', 'firstname': u'Peter', 'prefix': u'Dipl. Phys.', 'address': {u'country': u'Germany', u'region': None, u'street': u'Memelweg 9', u'zipcode': u'72072', u'locality': u'T\xfcbingen'}, 'department': u'IPC - AG Weimar', 'organization': u'Universit\xe4t T\xfcbingen', 'surname': u'Bonanati', 'email': u'peter.bonanati@ipc.uni-tuebingen.de'}}


class LetterData(dict):
    pass

def getFieldNameOdt(name):
    fieldMapCodeToTemplate={'firstname':'firstname',
          'surname':'surname',
          'prefix':'prefix',
          'address':'address',
          'street':'street',
          'locality':'locality',
          'zipcode':'zipode',
          'region':'region',
          'country':'country',
          'organization':'organization',
          'department':'department',
          'tel':'tel',
          'fax':'fax',
          'email':'email'
          }
    return fieldMapCodeToTemplate[name]

def getFieldNameJson(name):
    fieldMapCodeToJson={
          'firstname':'firstname',
          'surname':'surname',
          'prefix':'prefix',
          'address:work':'address:work',
          'address:':'address:',
          'street':'street',
          'locality':'locality',
          'zipcode':'zipode',
          'region':'region',
          'country':'country',
          'organization':'organization',
          'department':'department',
          'phone:work':'phone:work',
          'phone:':'phone:',
          'fax':'phone:workfax',
          'email:work':'email:work',
          'email:':'email:'}
    return fieldMapCodeToJson[name]


emptyContact={'tel': '',
     'surname': '',
     'firstname': '',
     'fax': '',
     'prefix': '',
     'address': {'country': '', 'region': '',' street': '', 'zipcode': '', '': ''},
     'department': '',
     'organization': '',
     'email': ''
     }

def getValueFromJson(data,name):
    name=getFieldNameJson(name)
    if data.has_key(name):
        return data[name]
    else:
        return ""


def jsonToDict(jsonData):
    letterData=json.loads(testString)
    return letterData

def jsonToLetterData(dataDict):
    letterData={'sender':{},
                'recipient':{}}
    index=0
    for source in ['recipient','sender']:
        tempDict=emptyContact
        data=dataDict[source]['records']
        data=data[index]
        
        
        tempDict[getFieldNameOdt('firstname')]=getValueFromJson(data,'firstname')
        print(getValueFromJson(data,'firstname'))
        tempDict[getFieldNameOdt('surname')]=getValueFromJson(data,'surname')
        tempDict[getFieldNameOdt('prefix')]=getValueFromJson(data,'prefix')
        

        tempDict[getFieldNameOdt('organization')]=getValueFromJson(data,'organization')
        tempDict[getFieldNameOdt('department')]=getValueFromJson(data,'department')

        
        
        ###address extraction
        tempDict[getFieldNameOdt('address')]={}
        if data.has_key(getFieldNameJson('address:work')):
            addKey=getFieldNameJson('address:work')
        else:
            addKeys=[addKey for addKey in data.keys() if (getFieldNameJson('address:') in addKey)]
            if len(addKeys):
                addKey=addKeys[0]
            else:
                addKey=None
#        print "addKey"
#        print addKey
        if addKey:
            addData=data[addKey][index]
            tempDict[getFieldNameOdt('address')]=addData
            
        else:
            pass
                
        
        
        ###telefon number extraction
        if data.has_key(getFieldNameJson('phone:work')):
            phoneKey=getFieldNameJson('phone:work')
        else:
            phoneKeys=[phoneKey for phoneKey in data.keys() if (getFieldNameJson('phone:') in phoneKey)]
            if len(phoneKeys):
                phoneKey=phoneKeys[0]
            else:
                pass
        if phoneKey:
            phoneData=data[phoneKey][index]
            tempDict[getFieldNameOdt('tel')]=phoneData
        else:
            pass
        
        
        
        ###fax number extraction
        try:
            if data.has_key(getFieldNameJson('fax')):
                faxData=getValueFromJson(data,'fax')
            else:
                faxData=''
        except:
            faxData=''

        tempDict[getFieldNameOdt('fax')]=faxData
        
        
        ###email extraction
        if data.has_key(getFieldNameJson('email:work')):
            key=getFieldNameJson('email:work')
        else:
            keys=[key for key in data.keys() if (getFieldNameJson('email:') in key)]
            if len(keys):
                key=keys[0]
            else:
                key=None
        if key:
            emailData=data[key][index]
            tempDict[getFieldNameOdt('email')]=emailData
        else:
            tempDict[getFieldNameOdt('email')]=None
            
            
    
        
        letterData[source]=tempDict.copy()
    today = datetime.date.today()
    
    letterData['date']=today.strftime('%d.%m.%Y')

    return letterData

if __name__=="__main__":  
    #dataDict=jsonToDict(testString)
    #letter_data=jsonToLetterData(testData)
    #print letter_data
    pass
