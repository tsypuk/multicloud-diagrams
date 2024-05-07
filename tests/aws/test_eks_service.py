from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_eks_service(self):
        # docs
        self.node_type = 'eks_service'

        # given
        mcd = MultiCloudDiagrams()

        # when
        eks_service_arn = 'arn:aws:eks:us-west-1:123456789012:service/eks-cluster/service-svc'
        eks_service_name = 'Nginx_Service'
        metadata = {
            "serviceName": "service-svc",
            "clusterArn": "arn:aws:eks:eu-west-1:123456789012:cluster/eks-cluster",
            "serviceRegistries": "arn:aws:servicediscovery:eu-west-1:123456789012:service/srv-t",
            "status": "ACTIVE",
            "desiredCount": 1,
            "runningCount": 1,
            "pendingCount": 0,
            "launchType": "EC2",
            "platformVersion": "LATEST",
            "platformFamily": "Linux",
            "deployment": "arn:aws:eks:eu-west-1:123456789012:deployment/service:15",
        }
        mcd.add_vertex(node_id=eks_service_arn, node_name=eks_service_name, node_type='eks_service', metadata=metadata)

        # then
        expected = {'id': 'vertex:eks_service:arn:aws:eks:us-west-1:123456789012:service/eks-cluster/service-svc',
                    'parent': '1',
                    'style': 'sketch=0;aspect=fixed;html=1;align=left;image;fontSize=12;image=img/lib/mscae/Info.svg;labelBackgroundColor=none;',
                    'value': '<b>Name</b>: Nginx_Service<BR><b>ID</b>: '
                             'arn:aws:eks:us-west-1:123456789012:service/eks-cluster/service-svc<BR>-----------<BR><b>serviceName</b>: '
                             'service-svc<BR><b>clusterArn</b>: '
                             'arn:aws:eks:eu-west-1:123456789012:cluster/eks-cluster<BR><b>serviceRegistries</b>: '
                             'arn:aws:servicediscovery:eu-west-1:123456789012:service/srv-t<BR><b>status</b>: '
                             'ACTIVE<BR><b>desiredCount</b>: 1<BR><b>runningCount</b>: '
                             '1<BR><b>pendingCount</b>: 0<BR><b>launchType</b>: '
                             'EC2<BR><b>platformVersion</b>: LATEST<BR><b>platformFamily</b>: '
                             'Linux<BR><b>deployment</b>: '
                             'arn:aws:eks:eu-west-1:123456789012:deployment/service:15',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'eks_service', self.node_type)

        # docs
        self.mcd = mcd
