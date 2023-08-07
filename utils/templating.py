from xml.dom import minidom
import xml.etree.ElementTree as Et
from jinja2 import Environment, FileSystemLoader

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
    return parsed.toprettyxml()


class TestRendering(TestUtilities):

    def tearDown(self) -> None:
        self.mcd.export_to_file(f'docs/docs/aws-components/output/drawio/{self.node_type}.drawio')
        self.create_index_html()

    def create_index_html(self):
        tree = Et.ElementTree(self.mcd.mx_file)
        data = tree.findall("./*/*/*/")[2]
        data_full = tree.findall(".")[0]

        del data.attrib['style']
        del data.attrib['value']

        output_file_name = f'docs/docs/aws-components/{self.node_type}.md'
        node_details = self.supported_vertex[self.node_type]

        context = {
            'xml_full': xml_to_string(data_full),
            'xml_node': xml_to_string(data),
            'desc': node_details['desc'],
            'version': node_details['version'],
            'style': node_details['style'],
            'width': node_details['width'],
            'height': node_details['height'],
            'node_type': self.node_type
        }

        with open(output_file_name, 'w') as f:
            output_md = render_template('template.MD', context)
            f.write(output_md)
