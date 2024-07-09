import xml.etree.ElementTree as ET
import json
import re


# Function to read and parse XML file
def read_xml_file(file_path):
    with open(file_path, 'r') as file:
        xml_content = file.read()
    return ET.fromstring(xml_content)


# Function to remove points from style
def modify_style(style):
    # Use regex to remove points attribute from the style string
    style = re.sub(r'points=\[\[.*?\]\];', '', style)
    # Replace align=center with align=left
    style = style.replace('align=center', 'align=left')
    return style


def get_last_id(root):
    mx_cells = root.findall(".//mxCell")
    if mx_cells:
        last_cell = mx_cells[-1]
        return last_cell.get("id")
    else:
        return None


def extract_data_to_json(root):
    # Extract the mxCell element with the desired attributes
    id = get_last_id(root)
    mx_cell = root.find(f".//mxCell[@id='{id}']")
    if mx_cell is not None:
        style = mx_cell.get("style")
        style = modify_style(style)
        geometry = mx_cell.find("mxGeometry")
        if geometry is not None:
            width = geometry.get("width")
            height = geometry.get("height")
        else:
            width = height = None

        # Regular expression to extract the value of shape
        pattern = r'resIcon=([^;]+);'

        # Search for the pattern in the input string
        match = re.search(pattern, style)

        # Extract and print the value if found
        if match:
            shape_value = match.group(1)
            print(shape_value)

        # Create the JSON structure
        data = {
            "style": style,
            "width": width,
            "height": height
        }

        # Convert to JSON string
        json_data = json.dumps(data, indent=4)
        return json_data
    else:
        return "mxCell with id='3' not found."


if __name__ == '__main__':
    # Read and parse the XML file
    file_path = 'draft.drawio'
    root = read_xml_file(file_path)

    # Extract data and convert to JSON
    json_output = extract_data_to_json(root)

    print(json_output)
