from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codecommit(self):
        # docs
        self.node_type = 'codecommit'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codecommit_service_arn = 'arn:aws:codecommit:us-west-1:123456789012:service/codecommit/123'
        codecommit_service_name = 'Code Commit'
        metadata = {
            'accountId': 'TestAcc',
            'repositoryId': 45,
            'repositoryName': 'SpringBootApp',
            'repositoryDescription': 'Main Backend processing app',
            'defaultBranch': 'main',
            'creationDate': '2024-07-01',
            'cloneUrlHttp': 'http://domain.com/testacc',
            'cloneUrlSsh': 'ssh://domain.com/testacc',
            'Arn': 'ARN',
            'kmsKeyId': 'KMS-ARN'
        }
        mcd.add_vertex(node_id=codecommit_service_arn, node_name=codecommit_service_name, node_type='codecommit', metadata=metadata)

        # then
        expected = {'id': 'vertex:codecommit:arn:aws:codecommit:us-west-1:123456789012:service/codecommit/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codecommit;',
                    'value': '<b>Name</b>: Code Commit<BR><b>ARN</b>: '
                             'arn:aws:codecommit:us-west-1:123456789012:service/codecommit/123<BR>-----------<BR><b>accountId</b>: '
                             'TestAcc<BR><b>repositoryId</b>: 45<BR><b>repositoryName</b>: '
                             'SpringBootApp<BR><b>repositoryDescription</b>: Main Backend '
                             'processing app<BR><b>defaultBranch</b>: '
                             'main<BR><b>creationDate</b>: 2024-07-01<BR><b>cloneUrlHttp</b>: '
                             'http://domain.com/testacc<BR><b>cloneUrlSsh</b>: '
                             'ssh://domain.com/testacc<BR><b>Arn</b>: ARN<BR><b>kmsKeyId</b>: '
                             'KMS-ARN',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codecommit', self.node_type)

        # docs
        self.mcd = mcd
