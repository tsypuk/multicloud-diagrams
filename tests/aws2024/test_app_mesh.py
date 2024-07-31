from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_vpc(self):
        # docs
        self.node_type = 'app_mesh'

        # given
        mcd = MultiCloudDiagrams()

        # when
        app_mesh_service_arn = 'arn:aws:app_mesh:us-west-1:123456789012:service/app_mesh/123'
        app_mesh_name = 'App Mesh'
        metadata = {
            'x-ray-enabled': 'true',
            'eks-configuration': 'cong/data/settings.json',
            'gatewayARN': "ARN"
        }
        mcd.add_vertex(node_id=app_mesh_service_arn, node_name=app_mesh_name, node_type='app_mesh', metadata=metadata)

        # then
        expected = {'id': 'vertex:app_mesh:arn:aws:app_mesh:us-west-1:123456789012:service/app_mesh/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.app_mesh;',
                    'value': '<b>Name</b>: App Mesh<BR><b>ARN</b>: '
                             'arn:aws:app_mesh:us-west-1:123456789012:service/app_mesh/123<BR>-----------<BR><b>x-ray-enabled</b>: '
                             'true<BR><b>eks-configuration</b>: '
                             'cong/data/settings.json<BR><b>gatewayARN</b>: ARN',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'app_mesh', self.node_type)

        # docs
        self.mcd = mcd
