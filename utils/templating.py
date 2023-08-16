from xml.dom import minidom
import xml.etree.ElementTree as Et
from jinja2 import Environment, FileSystemLoader
from copy import deepcopy

from utils.utils import TestUtilities


def render_template(template_filename, context):
    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(searchpath="./"),
        trim_blocks=True)

    return template_environment.get_template(template_filename).render(context)


def delete_first_line(text):
    lines = text.splitlines()
    if lines:
        del lines[0]
    return '\n'.join(lines)


def xml_to_string(data):
    rough_string = Et.tostring(data, 'utf-8').decode('utf-8')
    parsed = minidom.parseString(rough_string.replace('\n', ''))
    indentation = " " * 4  # Use 4 spaces for indentation
    newline = "\n"  # Use newline character
    non_empty_lines = [line for line in delete_first_line(parsed.toprettyxml(indent=indentation, newl=newline)).splitlines() if line.strip()]
    return '\n'.join(non_empty_lines)


class TestRendering(TestUtilities):

    def set_node_type(self):
        self.provider = self.get_provider_by_service_name(self.node_type)
        if self.check_nodes_without_markdown_generation():
            if self.node_type not in self.supported_vertex:
                self.node_type = 'fallback_vertex'
        if 'fallback' == self.provider:
            self.provider = 'core'

    def check_nodes_without_markdown_generation(self):
        result = True
        for name in self.no_rendering:
            result = result and name not in self.node_type
        return result

    def tearDown(self) -> None:
        self.set_node_type()
        self.mcd.export_to_file(f'docs/docs/{self.provider}-components/output/drawio/{self.node_type}.drawio')
        if self.check_nodes_without_markdown_generation():
            self.create_md_from_template()

    def create_md_from_template(self):
        tree = Et.ElementTree(self.mcd.mx_file)
        data = tree.findall("./*/*/*/")[2]
        data_full = deepcopy(tree.findall(".")[0].__copy__())
        style = data.attrib['style']
        del data.attrib['style']
        del data.attrib['value']

        output_file_name = f'docs/docs/{self.provider}-components/{self.node_type}.md'
        node_details = self.supported_vertex[self.node_type]

        context = {
            'xml_full': xml_to_string(data_full),
            'xml_node': xml_to_string(data),
            'style': style,
            'node_type': self.node_type,
            'provider': self.provider,
        }

        if 'desc' in node_details:
            context['desc'] = node_details['desc']

        if 'version' in node_details:
            context['version'] = node_details['version']

        if 'details' in node_details:
            context['details'] = node_details['details']

        if 'width' in node_details:
            context['width'] = node_details['width']

        if 'height' in node_details:
            context['height'] = node_details['height']

        pairs = style.split(';')
        # Split each pair into key and value using '=' as the separator
        context['styles'] = [pair.split('=') for pair in pairs]

        with open(output_file_name, 'w') as f:
            output_md = render_template('template.MD', context)
            f.write(output_md)
