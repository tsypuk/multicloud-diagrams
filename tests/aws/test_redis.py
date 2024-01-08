from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_redis_service(self):
        # docs
        self.node_type = 'redis'

        # given
        mcd = MultiCloudDiagrams()

        # when
        kafka_arn = 'arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94'
        kafka_name = 'arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94'
        metadata = {
            "connectivity": "CONNECTED",
            "cluster_nodes": "3",
            "volume": "15GB",
        }
        mcd.add_vertex(node_id=kafka_arn, node_name=kafka_name, node_type='redis', metadata=metadata)

        # then
        expected = {'id': 'vertex:redis:arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94',
                    'parent': '1',
                    'style': 'sketch=0;aspect=fixed;html=1;points=[];align=left;image;fontSize=12;image=img/lib/mscae/Cache_Redis_Product.svg;',
                    'value': '<b>Name</b>: '
                             'arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94<BR><b>ARN</b>: '
                             'arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94<BR>-----------<BR><b>connectivity</b>: '
                             'CONNECTED<BR><b>cluster_nodes</b>: 3<BR><b>volume</b>: 15GB',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'redis', self.node_type)

        # docs
        self.mcd = mcd
