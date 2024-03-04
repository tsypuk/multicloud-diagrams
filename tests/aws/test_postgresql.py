from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_postgresql_service(self):
        # docs
        self.node_type = 'postgresql'

        # given
        mcd = MultiCloudDiagrams()

        # when
        postgresql_arn = 'arn:aws:postgresql:eu-west-1:123456789012'
        postgresql_name = 'arn:aws:postgresql:eu-west-1:123456789012/MainDB'
        metadata = {
            "records": "224000",
            "engine": "16.2",
            "volume": "2048Mb",
            "cpu": "512",
            "memory": "2048",
            "version": 5.72,
        }
        mcd.add_vertex(node_id=postgresql_arn, node_name=postgresql_name, node_type='postgresql', metadata=metadata)

        # then
        expected = {'id': 'vertex:postgresql:arn:aws:postgresql:eu-west-1:123456789012',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.postgre_sql_instance;fillColor=#2E73B8;gradientColor=none;',
                    'value': '<b>Name</b>: '
                             'arn:aws:postgresql:eu-west-1:123456789012/MainDB<BR><b>ARN</b>: '
                             'arn:aws:postgresql:eu-west-1:123456789012<BR>-----------<BR><b>records</b>: '
                             '224000<BR><b>engine</b>: 16.2<BR><b>volume</b>: '
                             '2048Mb<BR><b>cpu</b>: 512<BR><b>memory</b>: 2048<BR><b>version</b>: '
                             '5.72',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'postgresql', self.node_type)

        # docs
        self.mcd = mcd
