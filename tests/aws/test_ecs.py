from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_ecs(self):
        # docs
        self.node_type = 'ecs'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ecs_arn = 'arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc'
        ecs_name = 'Nginx_Container'
        metadata = {
            "serviceName": "service-fg-svc",
            "clusterArn": "arn:aws:ecs:eu-west-1:123456789012:cluster/rules-dev-fargate-cluster",
            "serviceRegistries": [
                {
                    "registryArn": "arn:aws:servicediscovery:eu-west-1:123456789012:service/srv-t"
                }
            ],
            "status": "ACTIVE",
            "desiredCount": 1,
            "runningCount": 1,
            "pendingCount": 0,
            "launchType": "FARGATE",
            "platformVersion": "LATEST",
            "platformFamily": "Linux",
            "taskDefinition": "arn:aws:ecs:eu-west-1:123456789012:task-definition/service-fg-task:15",
        }
        mcd.add_vertex(node_id=ecs_arn, node_name=ecs_name, node_type='ecs', metadata=metadata)

        # then
        expected = {'id': 'vertex:ecs:arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc',
                    'parent': '1',
                    'style': 'outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ecs;',
                    'value': '<b>Name</b>: Nginx_Container<BR><b>ARN</b>: '
                             'arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc<BR>-----------<BR><b>serviceName</b>: '
                             'service-fg-svc<BR><b>clusterArn</b>: '
                             'arn:aws:ecs:eu-west-1:123456789012:cluster/rules-dev-fargate-cluster<BR><b>serviceRegistries</b>: '
                             "[{'registryArn': "
                             "'arn:aws:servicediscovery:eu-west-1:123456789012:service/srv-t'}]<BR><b>status</b>: "
                             'ACTIVE<BR><b>desiredCount</b>: 1<BR><b>runningCount</b>: '
                             '1<BR><b>pendingCount</b>: 0<BR><b>launchType</b>: '
                             'FARGATE<BR><b>platformVersion</b>: LATEST<BR><b>platformFamily</b>: '
                             'Linux<BR><b>taskDefinition</b>: '
                             'arn:aws:ecs:eu-west-1:123456789012:task-definition/service-fg-task:15',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'Client Certificate', self.node_type)

        # docs
        self.mcd = mcd
