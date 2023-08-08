from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestHttpVertexInIsolation(TestRendering):

    def test_http(self):
        # docs
        self.node_type = 'http'

        # given
        mcd = MultiCloudDiagrams()

        # when
        arn = 'https://somedomain.com'
        metadata = {
            "Owner": "organization1",
            "authorizer": "auth0",
            "Throttling": 500
        }
        mcd.add_vertex(node_id=arn, node_name='mock_data', arn=arn, node_type='http', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:http:https://somedomain.com',
            'parent': '1',
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.http_protocol;fillColor=#5294CF;gradientColor=none;',
            'value': '<b>Name</b>: mock_data<BR><b>ARN</b>: '
                     'https://somedomain.com<BR>-----------<BR><b>Owner</b>: '
                     'organization1<BR><b>authorizer</b>: auth0<BR><b>Throttling</b>: 500',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'mock_data', 'http')

        # docs
        self.mcd = mcd
