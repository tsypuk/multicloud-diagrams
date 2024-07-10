from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_elastic_load_balancing(self):
        # docs
        self.node_type = 'elastic_load_balancing'

        # given
        mcd = MultiCloudDiagrams()

        # when
        elastic_load_balancing_service_arn = 'arn:aws:elastic_load_balancing:us-west-1:123456789012:elastic_load_balancing/1'
        elastic_load_balancing_service_name = 'Elastic Load Balancing'
        metadata = {
            'CrossZoneLoadBalancing': {
                'Enabled': True
            },
            'AccessLog': {
                'Enabled': True,
                'S3BucketName': 'logs',
                'EmitInterval': 2,
                'S3BucketPrefix': 'prod'
            },
            'ConnectionDraining': {
                'Enabled': True,
                'Timeout': 2048
            },
            'ConnectionSettings': {
                'IdleTimeout': 1024
            },
        }

        mcd.add_vertex(node_id=elastic_load_balancing_service_arn, node_name=elastic_load_balancing_service_name, node_type='elastic_load_balancing', metadata=metadata)

        # then
        expected = {'id': 'vertex:elastic_load_balancing:arn:aws:elastic_load_balancing:us-west-1:123456789012:elastic_load_balancing/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;',
                    'value': '<b>Name</b>: Elastic Load Balancing<BR><b>ARN</b>: '
                             'arn:aws:elastic_load_balancing:us-west-1:123456789012:elastic_load_balancing/1<BR>-----------<BR><b>CrossZoneLoadBalancing</b>: '
                             "{'Enabled': True}<BR><b>AccessLog</b>: {'Enabled': True, "
                             "'S3BucketName': 'logs', 'EmitInterval': 2, 'S3BucketPrefix': "
                             "'prod'}<BR><b>ConnectionDraining</b>: {'Enabled': True, 'Timeout': "
                             "2048}<BR><b>ConnectionSettings</b>: {'IdleTimeout': 1024}",
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'elastic_load_balancing', self.node_type)

        # docs
        self.mcd = mcd
