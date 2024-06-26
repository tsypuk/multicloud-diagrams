from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_lex(self):
        # docs
        self.node_type = 'lex'

        # given
        mcd = MultiCloudDiagrams()

        # when
        lex_arn = 'arn:aws:lex:us-west-1:123456789012:lex/123'
        lex_name = 'Registry for images'
        metadata = {
            'botId': '1',
            'botName': 'demo-bot',
            'description': 'fintech audit',
            'roleArn': 'ARN',
            'idleSessionTTLInSeconds': 60,
            'botStatus': 'Available',
            'botType': 'Bot',
            'botMembers': 4
        }
        mcd.add_vertex(node_id=lex_arn, node_name=lex_name, node_type='lex', metadata=metadata)

        # then
        expected = {'id': 'vertex:lex:arn:aws:lex:us-west-1:123456789012:lex/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lex;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:lex:us-west-1:123456789012:lex/123<BR>-----------<BR><b>botId</b>: '
                             '1<BR><b>botName</b>: demo-bot<BR><b>description</b>: fintech '
                             'audit<BR><b>roleArn</b>: ARN<BR><b>idleSessionTTLInSeconds</b>: '
                             '60<BR><b>botStatus</b>: Available<BR><b>botType</b>: '
                             'Bot<BR><b>botMembers</b>: 4',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'lex', self.node_type)

        # docs
        self.mcd = mcd
