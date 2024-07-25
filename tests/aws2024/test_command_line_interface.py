from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_command_line_interface(self):
        # docs
        self.node_type = 'command_line_interface'

        # given
        mcd = MultiCloudDiagrams()

        # when
        command_line_interface_service_arn = 'arn:aws:command_line_interface:us-west-1:123456789012:service/command_line_interface/123'
        command_line_interface_name = 'CLI'
        metadata = {
            'version': '2.0.1',
            'extensions': 'enabled',
        }
        mcd.add_vertex(node_id=command_line_interface_service_arn, node_name=command_line_interface_name, node_type='command_line_interface', metadata=metadata)

        # then
        expected = {'id': 'vertex:command_line_interface:arn:aws:command_line_interface:us-west-1:123456789012:service/command_line_interface/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.command_line_interface;',
                    'value': '<b>Name</b>: CLI<BR><b>ARN</b>: '
                             'arn:aws:command_line_interface:us-west-1:123456789012:service/command_line_interface/123<BR>-----------<BR><b>version</b>: '
                             '2.0.1<BR><b>extensions</b>: enabled',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'command_line_interface', self.node_type)

        # docs
        self.mcd = mcd
