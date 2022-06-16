"""
Utils for XML Conversion
"""
from xml.etree import ElementTree

def parse_xml(xml_element: ElementTree.Element):
    """
    Responsible for converting XML to json
    """
    result = {}
    child_elements = list(xml_element)
    if child_elements:
        result[xml_element.tag] = []
        for child in list(xml_element):
            result[xml_element.tag].append(parse_xml(child))
    else:
        result[xml_element.tag] = xml_element.text or ''
    return result

def convert_xml_to_dict(file):
    """
    Parses XML file and returns a dictionary 
    """
    xml_tree: ElementTree = ElementTree.parse(file)
    return parse_xml(xml_element=xml_tree.getroot())

