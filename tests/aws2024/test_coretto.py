from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_coretto(self):
        # docs
        self.node_type = 'coretto'

        # given
        mcd = MultiCloudDiagrams()

        # when
        coretto_service_arn = 'arn:aws:coretto:us-west-1:123456789012:service/coretto/123'
        coretto_service_name = 'Coretto'
        metadata = {
            'name': 'Coretto',
            'arn': 'ARN',
            'description': 'Detailed desc',
            'clientRequestToken': 'CHECK_TOKEN',
            'createdTimeStamp': '2024-07-19',
            'status': 'active'
        }
        mcd.add_vertex(node_id=coretto_service_arn, node_name=coretto_service_name, node_type='coretto', metadata=metadata)

        # then
        expected = {'id': 'vertex:coretto:arn:aws:coretto:us-west-1:123456789012:service/coretto/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.corretto;',
                    'value': '<b>Name</b>: Coretto<BR><b>ARN</b>: '
                             'arn:aws:coretto:us-west-1:123456789012:service/coretto/123<BR>-----------<BR><b>name</b>: '
                             'Coretto<BR><b>arn</b>: ARN<BR><b>description</b>: Detailed '
                             'desc<BR><b>clientRequestToken</b>: '
                             'CHECK_TOKEN<BR><b>createdTimeStamp</b>: '
                             '2024-07-19<BR><b>status</b>: active',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'coretto', self.node_type)

        # docs
        self.mcd = mcd
