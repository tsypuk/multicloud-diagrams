from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_sqs(self):
        # docs
        self.node_type = 'api_gw'

        # given
        mcd = MultiCloudDiagrams()

        # when
        api_gw_arn = 'esf19s3pag'
        metadata = {
            "api_key_source": "HEADER",
            "endpoint_configuration": "{'types': ['EDGE']}"
        }

        mcd.add_vertex(node_id=api_gw_arn, node_name='APIGW integration with DynamoDB', node_type='api_gw', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:api_gw:esf19s3pag',
            'parent': '1',
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.api_gateway;fillColor=#D9A741;gradientColor=none;',
            'value': '<b>Name</b>: APIGW integration with DynamoDB<BR><b>ARN</b>: '
                     'esf19s3pag<BR>-----------<BR><b>api_key_source</b>: '
                     "HEADER<BR><b>endpoint_configuration</b>: {'types': ['EDGE']}",
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'APIGW integration with DynamoDB', 'api_gw')

        # docs
        self.mcd = mcd
