from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_web_client(self):
        # docs
        self.node_type = 'ruby_client'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="ruby",
                       node_name='Ruby v.4.0.1',
                       node_type='ruby_client',
                       hide_id=True)

        # then
        expected = {'id': 'vertex:ruby_client:ruby',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.android;fillColor=#AE1F23;gradientColor=none;',
                    'value': '<b>Name</b>: Ruby v.4.0.1',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ruby', 'ruby_client')

        # docs
        self.mcd = mcd
