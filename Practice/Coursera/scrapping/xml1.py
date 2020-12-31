import xml.etree.ElementTree as ET
data = '''<person>
        <name>Rhithick</name>
        <phone type="std">9629666576</phone>
        <email hide="yes"/>
        </person>'''
tree = ET.fromstring(data)
print(tree)
print(tree.find('name').text)
print(tree.find('phone').get('type'))
