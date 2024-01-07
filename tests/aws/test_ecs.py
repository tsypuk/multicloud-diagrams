from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_ecs(self):
        # docs
        self.node_type = 'ecs'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ecs_arn = 'arn:aws:ecs:eu-west-1:12345689012:cluster/fargate-cluster'
        ecs_name = 'Prod-cluster'
        metadata = {
            "runningTasksCount": 50,
            "pendingTasksCount": 0,
            "activeServicesCount": 50,
            "status": "ACTIVE",
        }
        mcd.add_vertex(node_id=ecs_arn, node_name=ecs_name, node_type='ecs', metadata=metadata)

        # then
        expected = {'id': 'vertex:ecs:arn:aws:ecs:eu-west-1:12345689012:cluster/fargate-cluster',
                    'parent': '1',
                    'style': 'outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ecs;',
                    'value': '<b>Name</b>: Prod-cluster<BR><b>ARN</b>: '
                             'arn:aws:ecs:eu-west-1:12345689012:cluster/fargate-cluster<BR>-----------<BR><b>runningTasksCount</b>: '
                             '50<BR><b>pendingTasksCount</b>: 0<BR><b>activeServicesCount</b>: '
                             '50<BR><b>status</b>: ACTIVE',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ecs', self.node_type)

        # docs
        self.mcd = mcd
