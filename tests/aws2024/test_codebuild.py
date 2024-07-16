from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codebuild(self):
        # docs
        self.node_type = 'codebuild'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codeabuild_service_arn = 'arn:aws:codebuild:us-west-1:123456789012:service/codebuild/123'
        codeabuild_service_name = 'Code Build'
        metadata = {
            'name': 'Build Java src',
            'arn': 'ARN',
            'description': 'SpringBoot app',
            'source': 'CODECOMMIT',
            'gitCloneDepth': 10,
            'fetchSubmodules': True,
            'auth': 'OAUTH',
            'reportBuildStatus': True,
        }
        mcd.add_vertex(node_id=codeabuild_service_arn, node_name=codeabuild_service_name, node_type='codebuild', metadata=metadata)

        # then
        expected = {'id': 'vertex:codebuild:arn:aws:codebuild:us-west-1:123456789012:service/codebuild/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codebuild;',
                    'value': '<b>Name</b>: Code Build<BR><b>ARN</b>: '
                             'arn:aws:codebuild:us-west-1:123456789012:service/codebuild/123<BR>-----------<BR><b>name</b>: '
                             'Build Java src<BR><b>arn</b>: ARN<BR><b>description</b>: SpringBoot '
                             'app<BR><b>source</b>: CODECOMMIT<BR><b>gitCloneDepth</b>: '
                             '10<BR><b>fetchSubmodules</b>: True<BR><b>auth</b>: '
                             'OAUTH<BR><b>reportBuildStatus</b>: True',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codebuild', self.node_type)

        # docs
        self.mcd = mcd
