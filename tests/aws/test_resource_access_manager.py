from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_appflow(self):
        # docs
        self.node_type = 'resource_access_manager'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ram_service_arn = 'arn:aws:resource_access_manager:us-west-1:123456789012:service/resource_access_manager/'
        ram_service_name = 'resource_access_manager'
        metadata = {
            "serviceName": "resource_access_manager",
            "clusterArn": "arn:aws:resource_access_manager:eu-west-1:123456789012:cluster/resource_access_manager",
            "serviceRegistries": "arn:aws:resource_access_manager:eu-west-1:123456789012:service/resource_access_manager",
            "status": "ACTIVE",
            "platformVersion": "LATEST",
            "deployment": "arn:aws:resource_access_manager:eu-west-1:123456789012/resource_access_manager:15",
        }
        mcd.add_vertex(node_id=ram_service_arn, node_name=ram_service_name, node_type='resource_access_manager', metadata=metadata)

        # then
        expected = {'id': 'vertex:resource_access_manager:arn:aws:resource_access_manager:us-west-1:123456789012:service/resource_access_manager/',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.resource_access_manager;',
                    'value': '<b>Name</b>: resource_access_manager<BR><b>ARN</b>: '
                             'arn:aws:resource_access_manager:us-west-1:123456789012:service/resource_access_manager/<BR>-----------<BR><b>serviceName</b>: '
                             'resource_access_manager<BR><b>clusterArn</b>: '
                             'arn:aws:resource_access_manager:eu-west-1:123456789012:cluster/resource_access_manager<BR><b>serviceRegistries</b>: '
                             'arn:aws:resource_access_manager:eu-west-1:123456789012:service/resource_access_manager<BR><b>status</b>: '
                             'ACTIVE<BR><b>platformVersion</b>: LATEST<BR><b>deployment</b>: '
                             'arn:aws:resource_access_manager:eu-west-1:123456789012/resource_access_manager:15',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'resource_access_manager', self.node_type)

        # docs
        self.mcd = mcd
