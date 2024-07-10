from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_local_zones(self):
        # docs
        self.node_type = 'local_zones'

        # given
        mcd = MultiCloudDiagrams()

        # when
        local_zones_service_arn = 'arn:aws:local_zones:eu-west-1:123456789012:local_zones/1'
        local_zones_service_name = 'Local Zones'
        metadata = {
            'State': 'available',
            'OptInStatus': 'opt-in-not-required',
            'RegionName': 'eu-west-1',
            'ZoneName': 'eu-west-1-az-1',
            'ZoneId': 'az-1',
            'GroupName': 'europe',
            'NetworkBorderGroup': 'ng-europe-1',
            'ZoneType': 'Local',
            'ParentZoneName': 'eu-west-1',
            'ParentZoneId': 'eu-west-1'
        }

        mcd.add_vertex(node_id=local_zones_service_arn, node_name=local_zones_service_name, node_type='local_zones', metadata=metadata)

        # then
        expected = {'id': 'vertex:local_zones:arn:aws:local_zones:eu-west-1:123456789012:local_zones/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.local_zones;',
                    'value': '<b>Name</b>: Local Zones<BR><b>ARN</b>: '
                             'arn:aws:local_zones:eu-west-1:123456789012:local_zones/1<BR>-----------<BR><b>State</b>: '
                             'available<BR><b>OptInStatus</b>: '
                             'opt-in-not-required<BR><b>RegionName</b>: '
                             'eu-west-1<BR><b>ZoneName</b>: eu-west-1-az-1<BR><b>ZoneId</b>: '
                             'az-1<BR><b>GroupName</b>: europe<BR><b>NetworkBorderGroup</b>: '
                             'ng-europe-1<BR><b>ZoneType</b>: Local<BR><b>ParentZoneName</b>: '
                             'eu-west-1<BR><b>ParentZoneId</b>: eu-west-1',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'local_zones', self.node_type)

        # docs
        self.mcd = mcd
