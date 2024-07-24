from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_tools_and_sdks(self):
        # docs
        self.node_type = 'tools_and_sdks'

        # given
        mcd = MultiCloudDiagrams()

        # when
        tools_and_sdks_service_arn = 'arn:aws:tools_and_sdks:us-west-1:123456789012:service/tools_and_sdks/123'
        tools_and_sdks_name = 'Tools and  SDKs'
        metadata = {
            'sdk': 'aws',
            'version': '1.5.21',
        }
        mcd.add_vertex(node_id=tools_and_sdks_service_arn, node_name=tools_and_sdks_name, node_type='tools_and_sdks', metadata=metadata)

        # then
        expected = {'id': 'vertex:tools_and_sdks:arn:aws:tools_and_sdks:us-west-1:123456789012:service/tools_and_sdks/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.tools_and_sdks;',
                    'value': '<b>Name</b>: Tools and  SDKs<BR><b>ARN</b>: '
                             'arn:aws:tools_and_sdks:us-west-1:123456789012:service/tools_and_sdks/123<BR>-----------<BR><b>sdk</b>: '
                             'aws<BR><b>version</b>: 1.5.21',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'tools_and_sdks', self.node_type)

        # docs
        self.mcd = mcd
