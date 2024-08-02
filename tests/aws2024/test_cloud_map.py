from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_vpc(self):
        # docs
        self.node_type = 'cloud_map'

        # given
        mcd = MultiCloudDiagrams()

        # when
        cloud_map_service_arn = 'arn:aws:cloud_map:us-west-1:123456789012:service/cloud_map/123'
        cloud_map_name = 'Cloud map'
        metadata = {
            'x-ray-enabled': True,
            'eks-services-rendering': True,
            'serverless-rendering': True
        }
        mcd.add_vertex(node_id=cloud_map_service_arn, node_name=cloud_map_name, node_type='cloud_map', metadata=metadata)

        # then
        expected = {'id': 'vertex:cloud_map:arn:aws:cloud_map:us-west-1:123456789012:service/cloud_map/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloud_map;',
                    'value': '<b>Name</b>: Cloud map<BR><b>ARN</b>: '
                             'arn:aws:cloud_map:us-west-1:123456789012:service/cloud_map/123<BR>-----------<BR><b>x-ray-enabled</b>: '
                             'True<BR><b>eks-services-rendering</b>: '
                             'True<BR><b>serverless-rendering</b>: True',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'cloud_map', self.node_type)

        # docs
        self.mcd = mcd
