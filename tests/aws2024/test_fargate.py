from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_fargate(self):
        # docs
        self.node_type = 'fargate'

        # given
        mcd = MultiCloudDiagrams()

        # when
        fargate_service_arn = 'arn:aws:fargate:eu-west-1:123456789012:fargate/1'
        fargate_service_name = 'fargate'
        metadata = {
            'compatibilities': 'FARGATE',
            'pidMode': 'host',
            'ipcMode': 'task',
            'requiresCompatibilities': 'FARGATE',
            'cpu': '1vCPU',
            'memory': '2048',
        }

        mcd.add_vertex(node_id=fargate_service_arn, node_name=fargate_service_name, node_type='fargate', metadata=metadata)

        # then
        expected = {'id': 'vertex:fargate:arn:aws:fargate:eu-west-1:123456789012:fargate/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.fargate;',
                    'value': '<b>Name</b>: fargate<BR><b>ARN</b>: '
                             'arn:aws:fargate:eu-west-1:123456789012:fargate/1<BR>-----------<BR><b>compatibilities</b>: '
                             'FARGATE<BR><b>pidMode</b>: host<BR><b>ipcMode</b>: '
                             'task<BR><b>requiresCompatibilities</b>: FARGATE<BR><b>cpu</b>: '
                             '1vCPU<BR><b>memory</b>: 2048',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'fargate', self.node_type)

        # docs
        self.mcd = mcd
