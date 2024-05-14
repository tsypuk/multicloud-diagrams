from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_eks(self):
        # docs
        self.node_type = 'xray'

        # given
        mcd = MultiCloudDiagrams()

        # when
        xray_service_arn = 'arn:aws:xray:us-west-1:123456789012:service/xray/tracing'
        xray_service_name = 'End-to-End-Tracing'
        metadata = {
            "serviceName": "service-xray",
            "clusterArn": "arn:aws:xray:eu-west-1:123456789012:service/tracing",
            "serviceRegistries": "arn:aws:xray:eu-west-1:123456789012:service/srv-t",
            "status": "ACTIVE",
            "includeFragments": "true",
            "sampling": 25,
            "platformVersion": "LATEST",
            "platformFamily": "Linux",
        }
        mcd.add_vertex(node_id=xray_service_arn, node_name=xray_service_name, node_type='xray', metadata=metadata)

        # then
        expected = {'id': 'vertex:xray:arn:aws:xray:us-west-1:123456789012:service/xray/tracing',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.x_ray;fillColor=#759C3E;gradientColor=none;',
                    'value': '<b>Name</b>: End-to-End-Tracing<BR><b>ARN</b>: '
                             'arn:aws:xray:us-west-1:123456789012:service/xray/tracing<BR>-----------<BR><b>serviceName</b>: '
                             'service-xray<BR><b>clusterArn</b>: '
                             'arn:aws:xray:eu-west-1:123456789012:service/tracing<BR><b>serviceRegistries</b>: '
                             'arn:aws:xray:eu-west-1:123456789012:service/srv-t<BR><b>status</b>: '
                             'ACTIVE<BR><b>includeFragments</b>: true<BR><b>sampling</b>: '
                             '25<BR><b>platformVersion</b>: LATEST<BR><b>platformFamily</b>: '
                             'Linux',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'xray', self.node_type)

        # docs
        self.mcd = mcd
