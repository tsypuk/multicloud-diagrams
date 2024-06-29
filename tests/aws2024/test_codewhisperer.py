from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codewhisperer(self):
        # docs
        self.node_type = 'codewhisperer'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codewhisperer_arn = 'arn:aws:codewhisperer:us-west-1:123456789012:codewhisperer/123'
        codewhisperer_name = 'Code Whisperer'
        metadata = {
            'initialLang': 'java',
            'LOC': 247,
            'page-size': 400,
            'context-size': 40000
        }
        mcd.add_vertex(node_id=codewhisperer_arn, node_name=codewhisperer_name, node_type='codewhisperer', metadata=metadata)

        # then
        expected = {'id': 'vertex:codewhisperer:arn:aws:codewhisperer:us-west-1:123456789012:codewhisperer/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codewhisperer;',
                    'value': '<b>Name</b>: Code Whisperer<BR><b>ARN</b>: '
                             'arn:aws:codewhisperer:us-west-1:123456789012:codewhisperer/123<BR>-----------<BR><b>initialLang</b>: '
                             'java<BR><b>LOC</b>: 247<BR><b>page-size</b>: '
                             '400<BR><b>context-size</b>: 40000',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codewhisperer', self.node_type)

        # docs
        self.mcd = mcd
