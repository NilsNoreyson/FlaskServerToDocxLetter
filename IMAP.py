# -*- coding: utf-8 -*-
"""
Created on Tue May  6 11:08:58 2014

@author: peterb
"""


#IMAP COMMUNICATION
import imaplib

#Encode and decode MIME quoted-printable data
import quopri

#to parse the XML Vacrd object
import xml.etree.ElementTree as ET




SERVER='krypton.ipc.uni-tuebingen.de'
PORT=993
USER='peter.stueber'
PASSWORD='au7sujh7'
#FOLDER='Shared Folders/shared.ipc-intern'
#FOLDER='Shared Folders/shared.ipc-companies'
FOLDER='Shared Folders/shared.crm'

def getTag(vCardTag):
    return vCardTag.split('}')[1]


def openIMAPConnection(server,port,user,password,folder):
    M = imaplib.IMAP4_SSL(server,port)

    M.login(user,password)
    M.select(folder,True)
    
    return M

def closeIMAP(IMAP):
    IMAP.close()
    IMAP.logout()


def getIDS(IMAP):
    typ, data = IMAP.search(None, 'ALL')
    ids=data[0].split()
    return ids


def getIdVcards(i,IMAP):
    typ, data = IMAP.fetch(i, '(RFC822)')
    text=data[0][1]

    text=text.strip().split('\n')
    text=[t.strip('\r') for t in text]
    ok=False
    
    vcardKolab=[]
    for t in  text:
        if t.startswith('<?xml'):
            ok=True
            
        if ok:        
            vcardKolab.append(t)
            #print t
    
        if t.strip().startswith('</vcards>'):
            ok=False
        
    data='\n'.join(vcardKolab)
    data=quopri.decodestring(data)
    
    return data


def parseVCard(data):
    root = ET.fromstring(data)

    di={}
    for el in root[0]:
        #print neighbor.tag,neighbor.text
        t=getTag(el.tag)
        subDict={}
        for e in el:
            sT=getTag(e.tag)
            
            if sT!="parameters":
                #print t,sT,e.text
                subDict[sT]=e.text
        di[t]=subDict
    return di

init=False
if __name__=="__main__":
    if init:
        IMAP=openIMAPConnection(SERVER,PORT,USER,PASSWORD,FOLDER)
        ids=getIDS(IMAP)
        vCards=[]
        for id in ids:
            data=getIdVcards(id,IMAP)
            vCards.append(parseVCard(data))
    