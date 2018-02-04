from xml.etree import ElementTree

def parse(roo,h):
    if "color" in roo.attrib:
        d[roo.attrib['color']] += h
    for child in roo:
        parse(child, h+1)

line = input().strip()

root = ElementTree.fromstring(line)

d = {
    'red' : 0,
    'blue' : 0,
    'green' : 0
}

parse(root, 1)
print(d['red'], d['green'], d['blue'])
