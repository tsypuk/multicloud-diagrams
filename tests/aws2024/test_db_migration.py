from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_db_migration(self):
        # docs
        self.node_type = 'db_migration'

        # given
        mcd = MultiCloudDiagrams()

        # when
        timestream_service_arn = 'arn:aws:db_migration:us-west-1:123456789012:db_migration/glue/1'
        timestream_service_name = 'DB Migration'
        metadata = {
            'SourceDB': 'RDS:instance1',
            'DestinationDB': 'RDS:instance2',
            'SchemaConvertion': 'SCHEMA1',
            'ConcurrencyLevel': 4,
            'CDCEnabled': True
        }

        mcd.add_vertex(node_id=timestream_service_arn, node_name=timestream_service_name, node_type='db_migration', metadata=metadata)

        # then
        expected = {'id': 'vertex:db_migration:arn:aws:db_migration:us-west-1:123456789012:db_migration/glue/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.database_migration_service;',
                    'value': '<b>Name</b>: DB Migration<BR><b>ARN</b>: '
                             'arn:aws:db_migration:us-west-1:123456789012:db_migration/glue/1<BR>-----------<BR><b>SourceDB</b>: '
                             'RDS:instance1<BR><b>DestinationDB</b>: '
                             'RDS:instance2<BR><b>SchemaConvertion</b>: '
                             'SCHEMA1<BR><b>ConcurrencyLevel</b>: 4<BR><b>CDCEnabled</b>: True',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'db_migration', self.node_type)

        # docs
        self.mcd = mcd
