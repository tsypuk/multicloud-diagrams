from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_sumerian(self):
        # docs
        self.node_type = 'sumerian'

        # given
        mcd = MultiCloudDiagrams()

        # when
        sumerian_arn = 'arn:aws:sumerian:us-west-1:123456789012:sumerian/123'
        sumerian_name = 'Registry for images'
        metadata = {
            'src-model': 'local.3d',
            'resolution': '16:9',
            'bitrate': 50,
        }
        mcd.add_vertex(node_id=sumerian_arn, node_name=sumerian_name, node_type='sumerian', metadata=metadata)

        # then
        expected = {'id': 'vertex:sumerian:arn:aws:sumerian:us-west-1:123456789012:sumerian/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sumerian;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:sumerian:us-west-1:123456789012:sumerian/123<BR>-----------<BR><b>src-model</b>: '
                             'local.3d<BR><b>resolution</b>: 16:9<BR><b>bitrate</b>: 50',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'sumerian', self.node_type)

        # docs
        self.mcd = mcd
