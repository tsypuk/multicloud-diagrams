from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_web_client(self):
        # docs
        self.node_type = 'web_client'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="web",
                       node_name='Chrome v.52',
                       node_type='web_client',
                       hide_id=True)

        # then
        expected = {'id': 'vertex:web_client:web',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.client;labelBackgroundColor=none;',
                    'value': '<b>Name</b>: Chrome v.52',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'web_client', 'web_client')

        # docs
        self.mcd = mcd
