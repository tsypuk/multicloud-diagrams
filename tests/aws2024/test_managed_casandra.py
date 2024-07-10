from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_managed_casandra(self):
        # docs
        self.node_type = 'managed_casandra'

        # given
        mcd = MultiCloudDiagrams()

        # when
        managed_casandra_service_arn = 'arn:aws:managed_casandra:us-west-1:123456789012:managed_casandra/glue/1'
        managed_casandra_service_name = 'Managed Casandra'
        metadata = {
            'tableName': 'string',
            'resourceArn': 'ARN',
            'creationTimestamp': '2024-03-03',
            'status': 'CREATING',
        }

        mcd.add_vertex(node_id=managed_casandra_service_arn, node_name=managed_casandra_service_name, node_type='managed_casandra', metadata=metadata)

        # then
        expected = {'id': 'vertex:managed_casandra:arn:aws:managed_casandra:us-west-1:123456789012:managed_casandra/glue/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.managed_apache_cassandra_service;',
                    'value': '<b>Name</b>: Managed Casandra<BR><b>ARN</b>: '
                             'arn:aws:managed_casandra:us-west-1:123456789012:managed_casandra/glue/1<BR>-----------<BR><b>tableName</b>: '
                             'string<BR><b>resourceArn</b>: ARN<BR><b>creationTimestamp</b>: '
                             '2024-03-03<BR><b>status</b>: CREATING',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'managed_casandra', self.node_type)

        # docs
        self.mcd = mcd
