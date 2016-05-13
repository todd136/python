#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
        def start_element(self, name, element):
                print('sax: start element %s attris: %s' % (name, str(element)))

        def end_element(self, name):
                print('sax: end element %s ' % name)

        def char_data(self, element):
                print('sax: char_data  %s' % str(element))

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
