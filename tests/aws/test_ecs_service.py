from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_ecs_service(self):
        # docs
        self.node_type = 'ecs_service'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ecs_service_arn = 'arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc'
        ecs_service_name = 'Nginx_Service'
        metadata = {
            "serviceName": "service-fg-svc",
            "clusterArn": "arn:aws:ecs:eu-west-1:123456789012:cluster/rules-dev-fargate-cluster",
            "serviceRegistries": "arn:aws:servicediscovery:eu-west-1:123456789012:service/srv-t",
            "status": "ACTIVE",
            "desiredCount": 1,
            "runningCount": 1,
            "pendingCount": 0,
            "launchType": "FARGATE",
            "platformVersion": "LATEST",
            "platformFamily": "Linux",
            "taskDefinition": "arn:aws:ecs:eu-west-1:123456789012:task-definition/service-fg-task:15",
        }
        mcd.add_vertex(node_id=ecs_service_arn, node_name=ecs_service_name, node_type='ecs_service', metadata=metadata)

        # then
        expected = {'id': 'vertex:ecs_service:arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D45B07;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.ecs_service;',
                    'value': '<b>Name</b>: Nginx_Service<BR><b>ARN</b>: '
                             'arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc<BR>-----------<BR><b>serviceName</b>: '
                             'service-fg-svc<BR><b>clusterArn</b>: '
                             'arn:aws:ecs:eu-west-1:123456789012:cluster/rules-dev-fargate-cluster<BR><b>serviceRegistries</b>: '
                             'arn:aws:servicediscovery:eu-west-1:123456789012:service/srv-t<BR><b>status</b>: '
                             'ACTIVE<BR><b>desiredCount</b>: 1<BR><b>runningCount</b>: '
                             '1<BR><b>pendingCount</b>: 0<BR><b>launchType</b>: '
                             'FARGATE<BR><b>platformVersion</b>: LATEST<BR><b>platformFamily</b>: '
                             'Linux<BR><b>taskDefinition</b>: '
                             'arn:aws:ecs:eu-west-1:123456789012:task-definition/service-fg-task:15',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ecs_service', self.node_type)

        # docs
        self.mcd = mcd
