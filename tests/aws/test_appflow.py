from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_appflow(self):
        # docs
        self.node_type = 'appflow'

        # given
        mcd = MultiCloudDiagrams()

        # when
        appflow_service_arn = 'arn:aws:appflow:us-west-1:123456789012:service/appflow/migration'
        appflow_service_name = 'Data Migration'
        metadata = {
            "serviceName": "appflow",
            "clusterArn": "arn:aws:appflow:eu-west-1:123456789012:cluster/appflow",
            "serviceRegistries": "arn:aws:appflow:eu-west-1:123456789012:service/appflow",
            "status": "ACTIVE",
            "desiredCount": 1,
            "runningCount": 1,
            "pendingCount": 0,
            "launchType": "EC2",
            "platformVersion": "LATEST",
            "platformFamily": "Linux",
            "deployment": "arn:aws:appflow:eu-west-1:123456789012:deployment/appflow:15",
        }
        mcd.add_vertex(node_id=appflow_service_arn, node_name=appflow_service_name, node_type='appflow', metadata=metadata)

        # then
        expected = {'id': 'vertex:appflow:arn:aws:appflow:us-west-1:123456789012:service/appflow/migration',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.appflow;',
                    'value': '<b>Name</b>: Data Migration<BR><b>ARN</b>: '
                             'arn:aws:appflow:us-west-1:123456789012:service/appflow/migration<BR>-----------<BR><b>serviceName</b>: '
                             'appflow<BR><b>clusterArn</b>: '
                             'arn:aws:appflow:eu-west-1:123456789012:cluster/appflow<BR><b>serviceRegistries</b>: '
                             'arn:aws:appflow:eu-west-1:123456789012:service/appflow<BR><b>status</b>: '
                             'ACTIVE<BR><b>desiredCount</b>: 1<BR><b>runningCount</b>: '
                             '1<BR><b>pendingCount</b>: 0<BR><b>launchType</b>: '
                             'EC2<BR><b>platformVersion</b>: LATEST<BR><b>platformFamily</b>: '
                             'Linux<BR><b>deployment</b>: '
                             'arn:aws:appflow:eu-west-1:123456789012:deployment/appflow:15',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'appflow', self.node_type)

        # docs
        self.mcd = mcd
