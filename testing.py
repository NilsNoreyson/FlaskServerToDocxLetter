# -*- coding: utf-8 -*-
"""
Created on Wed May 14 08:22:51 2014

@author: peterb
"""
letter_data={'date': '15.05.2014', 'recipient': {'fax': '', 'tel': u'+49 15782576830', 'firstname': u'Matthias', 'prefix': '', 'address': {}, 'department': '', 'organization': '', 'surname': u'B\xf6pple', 'email': u'matthias.boepple@student.uni-tuebingen.de'}, 'sender': {'fax': [u'07071-29-5963'], 'tel': u'07071-29-77633', 'firstname': u'Peter', 'prefix': u'Dipl. Phys.', 'address': {u'country': u'Germany', u'region': None, u'street': u'Memelweg 9', u'zipcode': u'72072', u'locality': u'T\xfcbingen'}, 'department': u'IPC - AG Weimar', 'organization': u'Universit\xe4t T\xfcbingen', 'surname': u'Bonanati', 'email': u'peter.bonanati@ipc.uni-tuebingen.de'}}
#letter_data={'date': '15.05.2014', 'recipient': {'fax': '', 'tel': u'A', 'firstname': u'Andreas', 'prefix': '', 'address': u'A', 'department': '', 'organization': '', 'surname': u'Fiedler', 'email': u'andreas.fiedler@ipc.uni-tuebingen.de'}, 'sender': {'fax': [u'07071-29-5963'], 'tel': u'07071-29-77633', 'firstname': u'Peter', 'prefix': u'Dipl. Phys.', 'address': {u'country': u'Germany', u'region': None, u'street': u'Memelweg 9', u'zipcode': u'72072', u'locality': u'T\xfcbingen'}, 'department': u'IPC - AG Weimar', 'organization': u'Universit\xe4t T\xfcbingen', 'surname': u'Bonanati', 'email': u'peter.bonanati@ipc.uni-tuebingen.de'}}
#letter_data=jsonToLetterData(testData)

#print letter_data

basic = Template(source="IPC_DATA", filepath='IPC_ger_Letter.odt')
print('TemplateDone')
basic_generated = basic.generate(o=letter_data).render()
print('filled Done')
odt_data=basic_generated.getvalue()
print('generated Done')

f = tempfile.NamedTemporaryFile(delete=False,mode='wb',dir=os.path.join(topPath,'static'))
print("%s.odt"%f.name)

f.write(odt_data)

f.close()