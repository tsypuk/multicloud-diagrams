from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_direct_connect(self):
        # docs
        self.node_type = 'direct_connect'

        # given
        mcd = MultiCloudDiagrams()

        # when
        direct_connect_service_arn = 'arn:aws:direct_connect:us-west-1:123456789012:direct_connect/glue/1'
        direct_connect_service_name = 'Glue'
        metadata = {
            'ownerAccount': '123456789012',
            'connectionId': '777',
            'connectionName': 'Vodafone-telco',
            'connectionState': 'available',
            'region': 'us-west-1',
            'location': 'San Diego',
            'bandwidth': '5G',
            'vlan': 9099,
            'partnerName': 'ISP locator',
            'lagId': '2WAN+',
            'awsDevice': 'pfsense:ID:775',
            'jumboFrameCapable': True,
            'awsDeviceV2': 'enabled',
        }
        mcd.add_vertex(node_id=direct_connect_service_arn, node_name=direct_connect_service_name, node_type='direct_connect', metadata=metadata)

        # then
        expected = {'id': 'vertex:direct_connect:arn:aws:direct_connect:us-west-1:123456789012:direct_connect/glue/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;',
                    'value': '<b>Name</b>: Glue<BR><b>ARN</b>: '
                             'arn:aws:direct_connect:us-west-1:123456789012:direct_connect/glue/1<BR>-----------<BR><b>ownerAccount</b>: '
                             '123456789012<BR><b>connectionId</b>: 777<BR><b>connectionName</b>: '
                             'Vodafone-telco<BR><b>connectionState</b>: '
                             'available<BR><b>region</b>: us-west-1<BR><b>location</b>: San '
                             'Diego<BR><b>bandwidth</b>: 5G<BR><b>vlan</b>: '
                             '9099<BR><b>partnerName</b>: ISP locator<BR><b>lagId</b>: '
                             '2WAN+<BR><b>awsDevice</b>: '
                             'pfsense:ID:775<BR><b>jumboFrameCapable</b>: '
                             'True<BR><b>awsDeviceV2</b>: enabled',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'direct_connect', self.node_type)

        # docs
        self.mcd = mcd
