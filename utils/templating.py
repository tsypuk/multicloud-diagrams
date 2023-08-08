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


def xml_to_string(data):
    rough_string = Et.tostring(data, 'utf-8').decode('utf-8')
    parsed = minidom.parseString(rough_string.replace('\n', ''))
    indentation = " " * 4  # Use 4 spaces for indentation
    newline = "\n"  # Use newline character
    non_empty_lines = [line for line in parsed.toprettyxml(indent=indentation, newl=newline).splitlines() if line.strip()]
    return '\n'.join(non_empty_lines)


class TestRendering(TestUtilities):

    def tearDown(self) -> None:
        provider = self.get_provider_by_service_name(self.node_type)
        if 'fallback' == provider:
            provider = 'core'
        node_type = self.node_type
        if node_type not in self.supported_vertex:
            node_type = 'fallback_vertex'
        self.mcd.export_to_file(f'docs/docs/{provider}-components/output/drawio/{node_type}.drawio')
        self.create_index_html()

    def create_index_html(self):
        tree = Et.ElementTree(self.mcd.mx_file)
        data = tree.findall("./*/*/*/")[2]
        data_full = deepcopy(tree.findall(".")[0].__copy__())

        del data.attrib['style']
        del data.attrib['value']

        resource_type = self.node_type
        if resource_type not in self.supported_vertex:
            resource_type = 'fallback_vertex'

        provider = self.get_provider_by_service_name(self.node_type)
        if 'fallback' == provider:
            provider = 'core'
        output_file_name = f'docs/docs/{provider}-components/{resource_type}.md'
        node_details = self.supported_vertex[resource_type]

        context = {
            'xml_full': xml_to_string(data_full),
            'xml_node': xml_to_string(data),
            'desc': node_details['desc'],
            'version': node_details['version'],
            'style': node_details['style'],
            'width': node_details['width'],
            'height': node_details['height'],
            'node_type': resource_type,
            'provider': provider,
        }
        if 'details' in node_details:
            context['details'] = node_details['details']

        pairs = node_details['style'].split(';')
        # Split each pair into key and value using '=' as the separator
        context['styles'] = [pair.split('=') for pair in pairs]

        with open(output_file_name, 'w') as f:
            output_md = render_template('template.MD', context)
            f.write(output_md)
