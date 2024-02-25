from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_chime(self):
        # docs
        self.node_type = 'chime_sdk'

        # given
        mcd = MultiCloudDiagrams()

        # when
        chime_arn = 'arn:aws:chime_sdk:us-east-1:123456789012:vc/xxxsomeid'

        metadata = {
            'name': 'sdk',
            'CreationDate': '2023-11-11',
            'CallDetails': "enabled",
            'SipRules': "none",
            'Analytics': 'Enabled',
            'KinesisVideo': 'Disabled',
            'VoiceConnector': 'Enabled',
            'VoiceConnectorTermination': 'Enabled',
            'VoiceConnectorStreaming': 'Enabled',
            'S3Recording': 'Enabled'
        }

        mcd.add_vertex(node_id=chime_arn, node_name='chime_sdk', node_type='chime_sdk', metadata=metadata)

        # then
        expected = {'id': 'vertex:chime_sdk:arn:aws:chime_sdk:us-east-1:123456789012:vc/xxxsomeid',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;gradientColor=#FF5252;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.chime_sdk;',
                    'value': '<b>Name</b>: chime_sdk<BR><b>ARN</b>: '
                             'arn:aws:chime_sdk:us-east-1:123456789012:vc/xxxsomeid<BR>-----------<BR><b>name</b>: '
                             'sdk<BR><b>CreationDate</b>: 2023-11-11<BR><b>CallDetails</b>: '
                             'enabled<BR><b>SipRules</b>: none<BR><b>Analytics</b>: '
                             'Enabled<BR><b>KinesisVideo</b>: Disabled<BR><b>VoiceConnector</b>: '
                             'Enabled<BR><b>VoiceConnectorTermination</b>: '
                             'Enabled<BR><b>VoiceConnectorStreaming</b>: '
                             'Enabled<BR><b>S3Recording</b>: Enabled',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'chime_sdk', 'chime_sdk')

        # docs
        self.mcd = mcd
