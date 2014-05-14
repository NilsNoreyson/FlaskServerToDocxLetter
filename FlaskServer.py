# -*- coding: utf-8 -*-
"""
Created on Tue May 13 14:28:23 2014

@author: peterb
"""

from flask import Flask,jsonify,request, make_response
from relatorio.templates.opendocument import Template
import os
from ipc_data import letter_data

import tempfile
topPath=os.path.dirname(os.path.realpath(__file__))





app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/createLetter',methods=['POST'])
def createLetter():
    encoding='ascii'
    if not request.json:
        abort(400)
    for dataSet in request.json.keys():
        print dataSet
        for field in request.json[dataSet].keys():
            try:
                #letter_data[dataSeta.encode(encoding)][field.decode(encoding)]=request.json[dataSet][field].decode(encoding)
                print(letter_data[dataSet][field])
                letter_data[dataSet][field]=request.json[dataSet][field]
                #print("\t-%s,%s"%(field,request.json[dataSet][field]))
            except:
                pass
                
    print letter_data
            
    



    basic = Template(source="IPC_DATA", filepath='IPC_ger_Letter.odt')
    basic_generated = basic.generate(o=letter_data).render()
    odt_data=basic_generated.getvalue()
    
    f = tempfile.NamedTemporaryFile(delete=False,mode='wb',dir=os.path.join(topPath,'static'))
    print(f.name)
    
    f.write(odt_data)
    
    response=make_response(odt_data)
    
    response.headers["Content-Disposition"] = "attachment; filename=Letter.odt"
    
#    data = request.get_json(force=True)
#    email    = json.get('email','')
    #print response
    #return response
    
    return jsonify({'status': 'OK','filename':os.path.basename(f.name)})


@app.route('/download/<filename>')
def download(filename):
    
                



#    basic = Template(source="IPC_DATA", filepath='IPC_ger_Letter.odt')
#    basic_generated = basic.generate(o=letter_data).render()
#    odt_data=basic_generated.getvalue()
    filename=os.path.join(topPath,'static',filename)
    f=open(filename,'rb')
    odt_data=f.read()
    #file('IPC_FULL.odt', 'wb').write(odt_data)
    
    response=make_response(odt_data)
    
    response.headers["Content-Disposition"] = "attachment; filename=Letter.odt"
    
#    data = request.get_json(force=True)
#    email    = json.get('email','')
    return response
    #return jsonify({'status': 'OK'})

    
if __name__ == '__main__':
    app.run(port=80)