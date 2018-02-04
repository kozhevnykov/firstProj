from xml.etree import ElementTree

# col = [blue, red, green]

"""def ff(child):
    if child[0]"""

line = input().strip()
root = ElementTree.fromstring(line)

for child in root:
    print(child.attrib['color'])

