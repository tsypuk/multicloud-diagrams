from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestGitInIsolation(TestRendering):

    def test_git_code(self):
        # docs
        self.node_type = 'github_code'

        # given
        mcd = MultiCloudDiagrams()

        # when
        arn = 'arn:aws:code:eu-west-1:123456789012:repo/123'
        metadata = {
            'name': 'my-code',
            'codeDigest': 'sha256:5562sfsf60a6d1aaed5c2bb227d3d4ec14c755bdb446349b',
        }
        mcd.add_vertex(node_id=arn, node_name='github_code', node_type='github_code', metadata=metadata)

        # then
        expected = {'id': 'vertex:github_code:arn:aws:code:eu-west-1:123456789012:repo/123',
                    'parent': '1',
                    'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;align=left;strokeColor=none;fillColor=#00BEF2;shape=mxgraph.azure.github_code;pointerEvents=1;',
                    'value': '<b>Name</b>: github_code<BR><b>ID</b>: '
                             'arn:aws:code:eu-west-1:123456789012:repo/123<BR>-----------<BR><b>name</b>: '
                             'my-code<BR><b>codeDigest</b>: '
                             'sha256:5562sfsf60a6d1aaed5c2bb227d3d4ec14c755bdb446349b',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'github_code', 'github_code')

        # docs
        self.mcd = mcd
