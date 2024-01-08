from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_actor(self):
        # docs
        self.node_type = 'rectangle'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="rect1",
                       node_name='microservice1',
                       node_type='rectangle')

        # then
        expected = {'id': 'vertex:rectangle:rect1',
                    'parent': '1',
                    'style': 'rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=none;',
                    'value': '<b>Name</b>: microservice1<BR><b>ID</b>: rect1',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'mock_data', 'rectangle')

        # docs
        self.mcd = mcd
