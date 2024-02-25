from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_chime_voice_connector(self):
        # docs
        self.node_type = 'chime_voice_connector'

        # given
        mcd = MultiCloudDiagrams()

        # when
        chime_arn = 'arn:aws:chime:us-east-1:123456789012:vc/xxxsomeid'

        metadata = {
            'name': 'asterisk',
            'CreationDate': '2023-11-11',
            'Encryption': "Enabled",
            'OutboundHostName': "xxxsomeid.voiceconnector.chime.com",
            'AllowedHostList': "122.122.xxx.xxx",
            'CallsPerSecond': "5",
            'UserAuth': "Enabled",
            'port': '5060',
            'CallingPlan': 'NO',
            'PhoneNumbers': '+XXXXXXXXXXX',
            'Logging': 'Enabled',
            'KinesisVideo': 'Disabled'
        }

        mcd.add_vertex(node_id=chime_arn, node_name='chime_voice_connector', node_type='chime_voice_connector', metadata=metadata)

        # then
        expected = {'id': 'vertex:chime_voice_connector:arn:aws:chime:us-east-1:123456789012:vc/xxxsomeid',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;gradientColor=#FF5252;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.chime;',
                    'value': '<b>Name</b>: chime_voice_connector<BR><b>ARN</b>: '
                             'arn:aws:chime:us-east-1:123456789012:vc/xxxsomeid<BR>-----------<BR><b>name</b>: '
                             'asterisk<BR><b>CreationDate</b>: 2023-11-11<BR><b>Encryption</b>: '
                             'Enabled<BR><b>OutboundHostName</b>: '
                             'xxxsomeid.voiceconnector.chime.com<BR><b>AllowedHostList</b>: '
                             '122.122.xxx.xxx<BR><b>CallsPerSecond</b>: 5<BR><b>UserAuth</b>: '
                             'Enabled<BR><b>port</b>: 5060<BR><b>CallingPlan</b>: '
                             'NO<BR><b>PhoneNumbers</b>: +XXXXXXXXXXX<BR><b>Logging</b>: '
                             'Enabled<BR><b>KinesisVideo</b>: Disabled',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'chime_voice_connector', 'chime_voice_connector')

        # docs
        self.mcd = mcd
