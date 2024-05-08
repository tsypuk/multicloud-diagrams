from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_backup(self):
        # docs
        self.node_type = 'backup'

        # given
        mcd = MultiCloudDiagrams()

        # when
        backup_arn = 'arn:aws:backup:us-west-1:123456789012:service/backup'
        backup_name = 'Full Dynamo&RDS backup'
        metadata = {
            "serviceName": "backup",
            "Entities": "Dynamo,RDS",
            "status": "ACTIVE",
            "desiredCount": 1,
            "schedule": "none",
            "pendingCount": 0,
            "platformVersion": "LATEST",
            "platformFamily": "Linux",
            "deployment": "arn:aws:backup:eu-west-1:123456789012:deployment/backup:15",
        }
        mcd.add_vertex(node_id=backup_arn, node_name=backup_name, node_type='backup', metadata=metadata)

        # then
        expected = {'id': 'vertex:backup:arn:aws:backup:us-west-1:123456789012:service/backup',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.backup;',
                    'value': '<b>Name</b>: Full Dynamo&RDS backup<BR><b>ARN</b>: '
                             'arn:aws:backup:us-west-1:123456789012:service/backup<BR>-----------<BR><b>serviceName</b>: '
                             'backup<BR><b>Entities</b>: Dynamo,RDS<BR><b>status</b>: '
                             'ACTIVE<BR><b>desiredCount</b>: 1<BR><b>schedule</b>: '
                             'none<BR><b>pendingCount</b>: 0<BR><b>platformVersion</b>: '
                             'LATEST<BR><b>platformFamily</b>: Linux<BR><b>deployment</b>: '
                             'arn:aws:backup:eu-west-1:123456789012:deployment/backup:15',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'eks', self.node_type)

        # docs
        self.mcd = mcd
