from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_aurora_service(self):
        # docs
        self.node_type = 'aurora'

        # given
        mcd = MultiCloudDiagrams()

        # when
        aurora_arn = 'arn:aws:aurora:eu-west-1:123456789012'
        aurora_name = 'arn:aws:aurora:eu-west-1:123456789012/MainDB'
        metadata = {
            "records": "224000",
            "engine": "InnoDB",
            "volume": "2048Mb",
            "cpu": "512",
            "memory": "2048",
            "version": 5.72,
        }
        mcd.add_vertex(node_id=aurora_arn, node_name=aurora_name, node_type='aurora', metadata=metadata)

        # then
        expected = {'id': 'vertex:aurora:arn:aws:aurora:eu-west-1:123456789012',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.aurora;',
                    'value': '<b>Name</b>: '
                             'arn:aws:aurora:eu-west-1:123456789012/MainDB<BR><b>ARN</b>: '
                             'arn:aws:aurora:eu-west-1:123456789012<BR>-----------<BR><b>records</b>: '
                             '224000<BR><b>engine</b>: InnoDB<BR><b>volume</b>: '
                             '2048Mb<BR><b>cpu</b>: 512<BR><b>memory</b>: 2048<BR><b>version</b>: '
                             '5.72',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ecs_task', self.node_type)

        # docs
        self.mcd = mcd
