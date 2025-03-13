import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ET.ParseError:
        print(f"Error: Failed to parse XML from {filename}.")
        return None
