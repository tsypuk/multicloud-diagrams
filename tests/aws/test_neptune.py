from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_neptune(self):
        # docs
        self.node_type = 'neptune'

        # given
        mcd = MultiCloudDiagrams()

        # when
        neptune_arn = 'arn:aws:rds:us-east-2:123456789012:db:my-neptune-instance-1'
        neptune_name = 'UsersGraph'
        metadata = {
            "data": 96000,
            'BackupRetentionPeriod': 123,
            'CharacterSetName': 'UTF-8',
            'DatabaseName': 'UsersGraph',
            'Endpoint': 'my-neptune-instance-1.cluster-ro-123456789012.us-east-1.neptune.amazonaws.com:8182',
            'ReaderEndpoint': 'my-neptune-instance-1.cluster-ro-123456789012.us-east-1.neptune.amazonaws.com:8182',
            'MultiAZ': True,
            'Engine': 'Neptune',
            'EngineVersion': 'v8',
            'StorageEncrypted': True,
            'IAMDatabaseAuthenticationEnabled': True,
            'CopyTagsToSnapshot': True,
            'DeletionProtection': False,
            'CrossAccountClone': False,
        }
        mcd.add_vertex(node_id=neptune_arn, node_name=neptune_name, node_type='neptune', metadata=metadata)

        # then
        expected = {'id': 'vertex:neptune:arn:aws:rds:us-east-2:123456789012:db:my-neptune-instance-1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.neptune;',
                    'value': '<b>Name</b>: UsersGraph<BR><b>ARN</b>: '
                             'arn:aws:rds:us-east-2:123456789012:db:my-neptune-instance-1<BR>-----------<BR><b>data</b>: '
                             '96000<BR><b>BackupRetentionPeriod</b>: '
                             '123<BR><b>CharacterSetName</b>: UTF-8<BR><b>DatabaseName</b>: '
                             'UsersGraph<BR><b>Endpoint</b>: '
                             'my-neptune-instance-1.cluster-ro-123456789012.us-east-1.neptune.amazonaws.com:8182<BR><b>ReaderEndpoint</b>: '
                             'my-neptune-instance-1.cluster-ro-123456789012.us-east-1.neptune.amazonaws.com:8182<BR><b>MultiAZ</b>: '
                             'True<BR><b>Engine</b>: Neptune<BR><b>EngineVersion</b>: '
                             'v8<BR><b>StorageEncrypted</b>: '
                             'True<BR><b>IAMDatabaseAuthenticationEnabled</b>: '
                             'True<BR><b>CopyTagsToSnapshot</b>: '
                             'True<BR><b>DeletionProtection</b>: '
                             'False<BR><b>CrossAccountClone</b>: False',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'neptune', self.node_type)

        # docs
        self.mcd = mcd
