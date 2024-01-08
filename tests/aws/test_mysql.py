from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_mysql_service(self):
        # docs
        self.node_type = 'mysql'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mysql_arn = 'arn:aws:mysql:eu-west-1:123456789012'
        mysql_name = 'arn:aws:mysql:eu-west-1:123456789012/MainDB'
        metadata = {
            "records": "224000",
            "engine": "InnoDB",
            "volume": "2048Mb",
            "cpu": "512",
            "memory": "2048",
            "version": 5.72,
        }
        mcd.add_vertex(node_id=mysql_arn, node_name=mysql_name, node_type='mysql', metadata=metadata)

        # then
        expected = {'id': 'vertex:mysql:arn:aws:mysql:eu-west-1:123456789012',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.mysql_db_instance;fillColor=#2E73B8;gradientColor=none;labelBackgroundColor=none;',
                    'value': '<b>Name</b>: '
                             'arn:aws:mysql:eu-west-1:123456789012/MainDB<BR><b>ARN</b>: '
                             'arn:aws:mysql:eu-west-1:123456789012<BR>-----------<BR><b>records</b>: '
                             '224000<BR><b>engine</b>: InnoDB<BR><b>volume</b>: '
                             '2048Mb<BR><b>cpu</b>: 512<BR><b>memory</b>: 2048<BR><b>version</b>: '
                             '5.72',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ecs_task', self.node_type)

        # docs
        self.mcd = mcd
