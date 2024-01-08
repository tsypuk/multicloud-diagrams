from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_mobile_client(self):
        # docs
        self.node_type = 'mobile_client'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="mobile",
                       node_name='Android',
                       node_type='mobile_client')

        # then
        expected = {'id': 'vertex:mobile_client:mobile',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;strokeColor=#232F3E;fillColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.mobile_client;labelBackgroundColor=none;',
                    'value': '<b>Name</b>: Android<BR><b>ID</b>: mobile',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'mobile_client', 'mobile_client')

        # docs
        self.mcd = mcd
