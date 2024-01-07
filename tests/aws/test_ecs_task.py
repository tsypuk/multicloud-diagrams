from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_ecs_service(self):
        # docs
        self.node_type = 'ecs_task'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ecs_task_arn = 'arn:aws:ecs:eu-west-1:123456789012:task/fargate-cluster/562320f29dbdc94'
        ecs_task_name = 'arn:aws:ecs:eu-west-1:123456789012:task/fargate-cluster/562320f29dbdc94'
        metadata = {
            "ecs.cpu-architecture": "x86_64",
            "availabilityZone": "eu-west-1a",
            "connectivity": "CONNECTED",
            "cpu": "512",
            "memory": "2048",
            "platformVersion": '1.4.0',
            "platformFamily": 'Linux',
            "version": 5,
            "ephemeralStorage_sizeInGiB": 20,
        }
        mcd.add_vertex(node_id=ecs_task_arn, node_name=ecs_task_name, node_type='ecs_task', metadata=metadata)

        # then
        expected = {'id': 'vertex:ecs_task:arn:aws:ecs:eu-west-1:123456789012:task/fargate-cluster/562320f29dbdc94',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D45B07;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.ecs_task;',
                    'value': '<b>Name</b>: '
                             'arn:aws:ecs:eu-west-1:123456789012:task/fargate-cluster/562320f29dbdc94<BR><b>ARN</b>: '
                             'arn:aws:ecs:eu-west-1:123456789012:task/fargate-cluster/562320f29dbdc94<BR>-----------<BR><b>ecs.cpu-architecture</b>: '
                             'x86_64<BR><b>availabilityZone</b>: '
                             'eu-west-1a<BR><b>connectivity</b>: CONNECTED<BR><b>cpu</b>: '
                             '512<BR><b>memory</b>: 2048<BR><b>platformVersion</b>: '
                             '1.4.0<BR><b>platformFamily</b>: Linux<BR><b>version</b>: '
                             '5<BR><b>ephemeralStorage_sizeInGiB</b>: 20',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ecs_task', self.node_type)

        # docs
        self.mcd = mcd
