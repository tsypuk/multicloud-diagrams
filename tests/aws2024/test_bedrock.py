from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_bedrock(self):
        # docs
        self.node_type = 'bedrock'

        # given
        mcd = MultiCloudDiagrams()

        # when
        bedrock_arn = 'arn:aws:bedrock:us-west-1:123456789012:bedrock/123'
        bedrock_name = 'Registry for images'
        metadata = {
            'modelArn': 'ARN',
            'modelName': 'titanic',
            'jobName': 'calculate survivors',
            'jobArn': 'ARN',
            'baseModelArn': 'ARN',
            'customizationType': 'CONTINUED_PRE_TRAINING',
            'modelKmsKeyArn': 'ARN',
            'hyperParameters': {
                'K1': 'V1'
            },
            'trainingDataConfig': {
                's3Uri': 'URI'
            },
        }
        mcd.add_vertex(node_id=bedrock_arn, node_name=bedrock_name, node_type='bedrock', metadata=metadata)

        # then
        expected = {'id': 'vertex:bedrock:arn:aws:bedrock:us-west-1:123456789012:bedrock/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:bedrock:us-west-1:123456789012:bedrock/123<BR>-----------<BR><b>modelArn</b>: '
                             'ARN<BR><b>modelName</b>: titanic<BR><b>jobName</b>: calculate '
                             'survivors<BR><b>jobArn</b>: ARN<BR><b>baseModelArn</b>: '
                             'ARN<BR><b>customizationType</b>: '
                             'CONTINUED_PRE_TRAINING<BR><b>modelKmsKeyArn</b>: '
                             "ARN<BR><b>hyperParameters</b>: {'K1': "
                             "'V1'}<BR><b>trainingDataConfig</b>: {'s3Uri': 'URI'}",
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'bedrock', self.node_type)

        # docs
        self.mcd = mcd
