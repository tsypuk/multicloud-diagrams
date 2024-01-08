from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_kafka_service(self):
        # docs
        self.node_type = 'kafka'

        # given
        mcd = MultiCloudDiagrams()

        # when
        kafka_arn = 'arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94'
        kafka_name = 'arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94'
        metadata = {
            "connectivity": "CONNECTED",
            "topics": "13",
            "messages": "2048",
        }
        mcd.add_vertex(node_id=kafka_arn, node_name=kafka_name, node_type='kafka', metadata=metadata)

        # then
        expected = {'id': 'vertex:kafka:arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.managed_streaming_for_kafka;',
                    'value': '<b>Name</b>: '
                             'arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94<BR><b>ARN</b>: '
                             'arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94<BR>-----------<BR><b>connectivity</b>: '
                             'CONNECTED<BR><b>topics</b>: 13<BR><b>messages</b>: 2048',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'kafka', self.node_type)

        # docs
        self.mcd = mcd
