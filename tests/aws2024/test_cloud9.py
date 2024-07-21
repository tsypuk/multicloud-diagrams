from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codestar(self):
        # docs
        self.node_type = 'cloud9'

        # given
        mcd = MultiCloudDiagrams()

        # when
        cloud9_service_arn = 'arn:aws:cloud9:us-west-1:123456789012:service/cloud9/123'
        cloud9_service_name = 'Code Star'
        metadata = {
            'id': 1,
            'name': 'Dev env',
            'description': 'Development env',
            'type': 'ssh',
            'connectionType': 'CONNECT_SSH',
            'arn': 'ARN',
            'lifecycle': 'CREATING',
        }
        mcd.add_vertex(node_id=cloud9_service_arn, node_name=cloud9_service_name, node_type='cloud9', metadata=metadata)

        # then
        expected = {'id': 'vertex:cloud9:arn:aws:cloud9:us-west-1:123456789012:service/cloud9/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#C925D1;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.cloud9;',
                    'value': '<b>Name</b>: Code Star<BR><b>ARN</b>: '
                             'arn:aws:cloud9:us-west-1:123456789012:service/cloud9/123<BR>-----------<BR><b>id</b>: '
                             '1<BR><b>name</b>: Dev env<BR><b>description</b>: Development '
                             'env<BR><b>type</b>: ssh<BR><b>connectionType</b>: '
                             'CONNECT_SSH<BR><b>arn</b>: ARN<BR><b>lifecycle</b>: CREATING',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'cloud9', self.node_type)

        # docs
        self.mcd = mcd
