from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_outpost(self):
        # docs
        self.node_type = 'outpost'

        # given
        mcd = MultiCloudDiagrams()

        # when
        outpost_arn = 'arn:aws:outpost:us-west-1:123456789012:outpost/123'
        outpost_name = 'Registry for images'
        metadata = {
            'OutpostId': '123',
            'OwnerId': '123456789012',
            'OutpostArn': '123456789012',
            'SiteId': 'local',
            'Name': 'state-building',
            'LifeCycleStatus': 'enabled',
            'AvailabilityZone': 'us-west-1a',
            'AvailabilityZoneId': '1a',
            'SupportedHardwareType': 'RACK'
        }
        mcd.add_vertex(node_id=outpost_arn, node_name=outpost_name, node_type='outpost', metadata=metadata)

        # then
        expected = {'id': 'vertex:outpost:arn:aws:outpost:us-west-1:123456789012:outpost/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.outposts;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:outpost:us-west-1:123456789012:outpost/123<BR>-----------<BR><b>OutpostId</b>: '
                             '123<BR><b>OwnerId</b>: 123456789012<BR><b>OutpostArn</b>: '
                             '123456789012<BR><b>SiteId</b>: local<BR><b>Name</b>: '
                             'state-building<BR><b>LifeCycleStatus</b>: '
                             'enabled<BR><b>AvailabilityZone</b>: '
                             'us-west-1a<BR><b>AvailabilityZoneId</b>: '
                             '1a<BR><b>SupportedHardwareType</b>: RACK',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'outpost', self.node_type)

        # docs
        self.mcd = mcd
