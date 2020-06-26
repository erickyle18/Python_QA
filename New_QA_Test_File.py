import zipfile
from lxml import etree

import xml.etree.ElementTree as ET

def extract_xml(docx_file_1):
    with open(docx_file_1, 'rb') as f:
        zip = zipfile.ZipFile(f,mode='r')
        xml_content = zip.read('word/document.xml')
        #print(type(xml_content))
    return xml_content



def main():
    xml_file = extract_xml('C:\\Users\\eisaac\\Desktop\\packPython2\\TD_ST.docx')

    xml_file = xml_file.decode('utf-8')
    
    
    print(xml_file)
    

    #root = ET.fromstring(xml_file)
    #print(root)
    #print(ET.tostring(root))
    #root = ET.tostringlist(root)
    
    #print('\n')
    #print(root)


    
    
    



main()
    
