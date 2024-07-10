from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_auto_scaling2(self):
        # docs
        self.node_type = 'auto_scaling2'

        # given
        mcd = MultiCloudDiagrams()

        # when
        auto_scaling2_service_arn = 'arn:aws:auto_scaling2:eu-west-1:123456789012:auto_scaling2/1'
        auto_scaling2_service_name = 'Lightsail'
        metadata = {
            'name': 'Instance1',
            'arn': 'ARN',
            'supportCode': 'java',
            'createdAt': '2024-07-08',
            'location': {
                'availabilityZone': 'az-1',
                'regionName': 'us-east-1',
            },
            'resourceType': 'Instance',
        }

        mcd.add_vertex(node_id=auto_scaling2_service_arn, node_name=auto_scaling2_service_name, node_type='auto_scaling2', metadata=metadata)

        # then
        expected = {'id': 'vertex:lightsail:arn:aws:lightsail:eu-west-1:123456789012:lightsail/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lightsail;',
                    'value': '<b>Name</b>: Lightsail<BR><b>ARN</b>: '
                             'arn:aws:lightsail:eu-west-1:123456789012:lightsail/1<BR>-----------<BR><b>name</b>: '
                             'Instance1<BR><b>arn</b>: ARN<BR><b>supportCode</b>: '
                             'java<BR><b>createdAt</b>: 2024-07-08<BR><b>location</b>: '
                             "{'availabilityZone': 'az-1', 'regionName': "
                             "'us-east-1'}<BR><b>resourceType</b>: Instance",
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'auto_scaling2', self.node_type)

        # docs
        self.mcd = mcd
