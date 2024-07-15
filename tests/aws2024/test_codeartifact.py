from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codeartifact(self):
        # docs
        self.node_type = 'codeartifact'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codeartifact_service_arn = 'arn:aws:codeartifact:us-west-1:123456789012:service/codeartifact/123'
        codeartifact_service_name = 'Code Artifact'
        metadata = {
            'name': 'Images Registry',
            'administratorAccount': 'Test',
            'domainName': 'test.com',
            'domainOwner': 'root',
            'arn': 'ARN',
            'description': 'build images are available',
            'externalConnections': 'maven'
        }
        mcd.add_vertex(node_id=codeartifact_service_arn, node_name=codeartifact_service_name, node_type='codeartifact', metadata=metadata)

        # then
        expected = {'id': 'vertex:codeartifact:arn:aws:codeartifact:us-west-1:123456789012:service/codeartifact/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codeartifact;',
                    'value': '<b>Name</b>: Code Artifact<BR><b>ARN</b>: '
                             'arn:aws:codeartifact:us-west-1:123456789012:service/codeartifact/123<BR>-----------<BR><b>name</b>: '
                             'Images Registry<BR><b>administratorAccount</b>: '
                             'Test<BR><b>domainName</b>: test.com<BR><b>domainOwner</b>: '
                             'root<BR><b>arn</b>: ARN<BR><b>description</b>: build images are '
                             'available<BR><b>externalConnections</b>: maven',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codeartifact', self.node_type)

        # docs
        self.mcd = mcd
