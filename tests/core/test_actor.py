from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_actor(self):
        # docs
        self.node_type = 'actor'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="777abc",
                       node_name='User',
                       node_type='actor',
                       hide_id=True)

        # then
        # docs
        self.mcd = mcd
