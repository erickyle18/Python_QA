import zipfile
#from lxml import etree

import xml.etree.ElementTree as ET

def get_word_xml(docx_filename):
    with open(docx_filename, 'rb') as f:
        zip = zipfile.ZipFile(f)
        xml_content = zip.read('word/document.xml')
    return xml_content

def get_xml_tree(xml_string):
    return etree.fromstring(xml_string)


def get_td_elements(pretty_string_1):

    #parser = ET.XMLParser(encoding="utf-8")
    pretty_string_2 = ET.tostring(pretty_string_1, encoding=None)
    
    #tree = ET.parse(pretty_string_2,parser=parser)
    #root = tree.getroot()
    #for child in root.iter('w:pPr')
        #print(ET.tostring(child))


def main():
    new_infile = get_word_xml('JuniperST.docx')

    string_infile = get_xml_tree(new_infile)
    
    #Comment out the line below for unit testing.
    #print(etree.tostring(string_infile, pretty_print=True,encoding='utf8').decode('utf8'))

    pretty_string_0 = get_td_elements(string_infile)

  
  



main()
