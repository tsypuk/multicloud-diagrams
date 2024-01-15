from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_elastic_search(self):
        # docs
        self.node_type = 'elasticsearch_service'

        # given
        mcd = MultiCloudDiagrams()

        # when
        elastic_arn = 'arn:aws:elastic-search:eu-west-1:123456789012:document/test-table'
        elastic_name = 'Index for Photos'
        metadata = {
            "indexes": 12,
            "Volume": "45GB",
        }
        mcd.add_vertex(node_id=elastic_arn, node_name=elastic_name, node_type='elasticsearch_service', metadata=metadata)

        # then
        expected = {'id': 'vertex:elasticsearch_service:arn:aws:elastic-search:eu-west-1:123456789012:document/test-table',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.elasticsearch_service;fillColor=#F58534;gradientColor=none;',
                    'value': '<b>Name</b>: Index for Photos<BR><b>ARN</b>: '
                             'arn:aws:elastic-search:eu-west-1:123456789012:document/test-table<BR>-----------<BR><b>indexes</b>: '
                             '12<BR><b>Volume</b>: 45GB',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'elasticsearch_service', self.node_type)

        # docs
        self.mcd = mcd
