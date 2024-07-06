from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_timestream(self):
        # docs
        self.node_type = 'redshift'

        # given
        mcd = MultiCloudDiagrams()

        # when
        redshift_service_arn = 'arn:aws:redshift:us-west-1:123456789012:redshift/db/1'
        redshift_service_name = 'Redshift'
        metadata = {
            'DBName': 'TestData',
            'ClusterIdentifier': 'test-cluder',
            'ClusterType': 'permanent',
            'AvailabilityZone': 'az-2',
            'PreferredMaintenanceWindow': '2H',
            'AutomatedSnapshotRetentionPeriod': 2,
            'ManualSnapshotRetentionPeriod': 3,
            'Port': 123,
            'AllowVersionUpgrade': True,
            'NumberOfNodes': 4,
            'PubliclyAccessible': True
        }

        mcd.add_vertex(node_id=redshift_service_arn, node_name=redshift_service_name, node_type='redshift', metadata=metadata)

        # then
        expected = {'id': 'vertex:redshift:arn:aws:redshift:us-west-1:123456789012:redshift/db/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.redshift;',
                    'value': '<b>Name</b>: Redshift<BR><b>ARN</b>: '
                             'arn:aws:redshift:us-west-1:123456789012:redshift/db/1<BR>-----------<BR><b>DBName</b>: '
                             'TestData<BR><b>ClusterIdentifier</b>: '
                             'test-cluder<BR><b>ClusterType</b>: '
                             'permanent<BR><b>AvailabilityZone</b>: '
                             'az-2<BR><b>PreferredMaintenanceWindow</b>: '
                             '2H<BR><b>AutomatedSnapshotRetentionPeriod</b>: '
                             '2<BR><b>ManualSnapshotRetentionPeriod</b>: 3<BR><b>Port</b>: '
                             '123<BR><b>AllowVersionUpgrade</b>: True<BR><b>NumberOfNodes</b>: '
                             '4<BR><b>PubliclyAccessible</b>: True',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'redshift', self.node_type)

        # docs
        self.mcd = mcd
