from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codepipeline(self):
        # docs
        self.node_type = 'codepipeline'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codepipeline_service_arn = 'arn:aws:codepipeline:us-west-1:123456789012:service/codepipeline/123'
        codepipeline_service_name = 'Code Pipeline'
        metadata = {
            'name': 'Build Image',
            'roleArn': 'ARN',
            'artifactStore': 'S3',
            'version': 1,
            'triggers': 'CodeStarSourceConnection',
            'executionMode': 'QUEUED',
            'pipelineType': 'V1'
        }
        mcd.add_vertex(node_id=codepipeline_service_arn, node_name=codepipeline_service_name, node_type='codepipeline', metadata=metadata)

        # then
        expected = {'id': 'vertex:codepipeline:arn:aws:codepipeline:us-west-1:123456789012:service/codepipeline/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codepipeline;',
                    'value': '<b>Name</b>: Code Pipeline<BR><b>ARN</b>: '
                             'arn:aws:codepipeline:us-west-1:123456789012:service/codepipeline/123<BR>-----------<BR><b>name</b>: '
                             'Build Image<BR><b>roleArn</b>: ARN<BR><b>artifactStore</b>: '
                             'S3<BR><b>version</b>: 1<BR><b>triggers</b>: '
                             'CodeStarSourceConnection<BR><b>executionMode</b>: '
                             'QUEUED<BR><b>pipelineType</b>: V1',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codepipeline', self.node_type)

        # docs
        self.mcd = mcd
