import xml.etree.ElementTree as ET
import os
import pandas as pd
list_balises = ['name', 'desc', 'nbs', 'date_s', 'station']


def tostr(s):
    if s is None:
        return ''
    else:
        return str(s)+'\n'


for file in os.listdir("xml/"):
    file = 'xml/'+file
    print(file)
    if file.endswith(".xml"):
        tree = ET.parse(file)
        root = tree.getroot()
        df=pd.DataFrame(columns=list_balises+['names'])

        for sauvetages in root:

            for sauvetage in sauvetages:
                d={}
                for balise in list_balises:
                    d[balise]=sauvetage.find(balise).text
                d['names']=[]
                i=sauvetage.find('names')
                for j in i.findall('entry'):
                    d['names'].append(j.text)
                df=df.append(d,ignore_index=True)
        df.to_csv(file[:-4]+'.csv',index=True,sep="\t")
        
