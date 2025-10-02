# scrapping for xml sheet 
import os

os.chdir(r"C:\Users\DELL\OneDrive\Documents\769952.xml")

import xml.etree.ElementTree as ET
tree = ET.parse("769952.xml")
root = tree.getroot()


