from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codestar(self):
        # docs
        self.node_type = 'codestar'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codestar_service_arn = 'arn:aws:codestar:us-west-1:123456789012:service/codestar/123'
        codestar_service_name = 'Code Star'
        metadata = {
            'name': 'CodeStarProject',
            'id': '777',
            'arn': 'ARN',
            'description': 'Detailed desc',
            'clientRequestToken': 'CHECK_TOKEN',
            'createdTimeStamp': '2024-07-19',
            'projectTemplateId': 'java',
            'status': 'active'
        }
        mcd.add_vertex(node_id=codestar_service_arn, node_name=codestar_service_name, node_type='codestar', metadata=metadata)

        # then
        expected = {'id': 'vertex:codestar:arn:aws:codestar:us-west-1:123456789012:service/codestar/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codestar;',
                    'value': '<b>Name</b>: Code Star<BR><b>ARN</b>: '
                             'arn:aws:codestar:us-west-1:123456789012:service/codestar/123<BR>-----------<BR><b>name</b>: '
                             'CodeStarProject<BR><b>id</b>: 777<BR><b>arn</b>: '
                             'ARN<BR><b>description</b>: Detailed '
                             'desc<BR><b>clientRequestToken</b>: '
                             'CHECK_TOKEN<BR><b>createdTimeStamp</b>: '
                             '2024-07-19<BR><b>projectTemplateId</b>: java<BR><b>status</b>: '
                             'active',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codestar', self.node_type)

        # docs
        self.mcd = mcd
