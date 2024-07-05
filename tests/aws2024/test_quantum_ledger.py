from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_db_migration(self):
        # docs
        self.node_type = 'quantum_ledger'

        # given
        mcd = MultiCloudDiagrams()

        # when
        quantum_ledger_service_arn = 'arn:aws:quantum_ledger:us-west-1:123456789012:quantum_ledger/glue/1'
        quantum_ledger_service_name = 'DB Migration'
        metadata = {
            'Name': 'Ledger1',
            'Arn': 'ARN',
            'State': 'ACTIVE',
            'CreationDateTime': '2024-06-05',
            'PermissionsMode': 'ALLOW_ALL',
            'DeletionProtection': True,
            'EncryptionDescription': {
                'KmsKeyArn': 'ARN',
                'EncryptionStatus': 'KMS_KEY_INACCESSIBLE',
                'InaccessibleKmsKeyDateTime': '2024-06-05'
            }
        }

        mcd.add_vertex(node_id=quantum_ledger_service_arn, node_name=quantum_ledger_service_name, node_type='quantum_ledger', metadata=metadata)

        # then
        expected = {'id': 'vertex:quantum_ledger:arn:aws:quantum_ledger:us-west-1:123456789012:quantum_ledger/glue/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.quantum_ledger_database;',
                    'value': '<b>Name</b>: DB Migration<BR><b>ARN</b>: '
                             'arn:aws:quantum_ledger:us-west-1:123456789012:quantum_ledger/glue/1<BR>-----------<BR><b>Name</b>: '
                             'Ledger1<BR><b>Arn</b>: ARN<BR><b>State</b>: '
                             'ACTIVE<BR><b>CreationDateTime</b>: '
                             '2024-06-05<BR><b>PermissionsMode</b>: '
                             'ALLOW_ALL<BR><b>DeletionProtection</b>: '
                             "True<BR><b>EncryptionDescription</b>: {'KmsKeyArn': 'ARN', "
                             "'EncryptionStatus': 'KMS_KEY_INACCESSIBLE', "
                             "'InaccessibleKmsKeyDateTime': '2024-06-05'}",
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'quantum_ledger', self.node_type)

        # docs
        self.mcd = mcd
