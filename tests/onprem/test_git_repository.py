from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestDockerInIsolation(TestRendering):

    def test_git_repository(self):
        # docs
        self.node_type = 'git_repository'

        # given
        mcd = MultiCloudDiagrams()

        # when
        arn = 'arn:aws:code:eu-west-1:123456789012:repo/123'
        metadata = {
            'name': 'my-repo',
            'image': '123456789012.dkr.ecr.eu-west-1.amazonaws.com/cluster/myapp:v2-22-00',
            'imageDigest': 'sha256:5562sfsf60a6d1aaed5c2bb227d3d4ec14c755bdb446349b',
        }
        mcd.add_vertex(node_id=arn, node_name='git_repository', node_type='git_repository', metadata=metadata)

        # then
        expected = {'id': 'vertex:git_repository:arn:aws:code:eu-west-1:123456789012:repo/123',
                    'parent': '1',
                    'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;align=left;strokeColor=none;fillColor=#00BEF2;shape=mxgraph.azure.git_repository;',
                    'value': '<b>Name</b>: git_repository<BR><b>ID</b>: '
                             'arn:aws:code:eu-west-1:123456789012:repo/123<BR>-----------<BR><b>name</b>: '
                             'my-repo<BR><b>image</b>: '
                             '123456789012.dkr.ecr.eu-west-1.amazonaws.com/cluster/myapp:v2-22-00<BR><b>imageDigest</b>: '
                             'sha256:5562sfsf60a6d1aaed5c2bb227d3d4ec14c755bdb446349b',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'git_repository', 'git_repository')

        # docs
        self.mcd = mcd
