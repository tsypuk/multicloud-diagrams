from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestDockerInIsolation(TestRendering):

    def test_docker(self):
        # docs
        self.node_type = 'docker'

        # given
        mcd = MultiCloudDiagrams()

        # when
        arn = 'arn:aws:ecs:eu-west-1:123456789012:container/cluster/777/123'
        metadata = {
            'name': 'my-app',
            'image': '123456789012.dkr.ecr.eu-west-1.amazonaws.com/cluster/myapp:v2-22-00',
            'imageDigest': 'sha256:5562sfsf60a6d1aaed5c2bb227d3d4ec14c755bdb446349b',
            'runtimeId': '56832234bec86b30201dbdc94-11149226',
            'lastStatus': 'RUNNING',
            'healthStatus': 'UNKNOWN',
            'cpu': '512',
            'memory': '1024'
        }
        mcd.add_vertex(node_id=arn, node_name='docker', node_type='docker', metadata=metadata)

        # then
        expected = {'id': 'vertex:docker:arn:aws:ecs:eu-west-1:123456789012:container/cluster/777/123',
                    'parent': '1',
                    'style': 'sketch=0;aspect=fixed;html=1;points=[];align=center;image;fontSize=12;image=img/lib/mscae/Docker.svg;',
                    'value': '<b>Name</b>: docker<BR><b>ID</b>: '
                             'arn:aws:ecs:eu-west-1:123456789012:container/cluster/777/123<BR>-----------<BR><b>name</b>: '
                             'my-app<BR><b>image</b>: '
                             '123456789012.dkr.ecr.eu-west-1.amazonaws.com/cluster/myapp:v2-22-00<BR><b>imageDigest</b>: '
                             'sha256:5562sfsf60a6d1aaed5c2bb227d3d4ec14c755bdb446349b<BR><b>runtimeId</b>: '
                             '56832234bec86b30201dbdc94-11149226<BR><b>lastStatus</b>: '
                             'RUNNING<BR><b>healthStatus</b>: UNKNOWN<BR><b>cpu</b>: '
                             '512<BR><b>memory</b>: 1024',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'docker', 'docker')

        # docs
        self.mcd = mcd
