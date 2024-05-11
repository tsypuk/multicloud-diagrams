from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_datasync(self):
        # docs
        self.node_type = 'datasync'

        # given
        mcd = MultiCloudDiagrams()

        # when
        datasync_service_arn = 'arn:aws:datasync:us-west-1:123456789012:service/datasync/data'
        datasync_service_name = 'Data Sync'
        metadata = {
            "serviceName": "datasync",
            "clusterArn": "arn:aws:datasync:eu-west-1:123456789012:/datasync",
            "serviceRegistries": "arn:aws:datasync:eu-west-1:123456789012:service/datasync",
            "status": "ACTIVE",
            "launchType": "Data Transfer",
            "platformVersion": "LATEST",
            "platformFamily": "Linux",
        }
        mcd.add_vertex(node_id=datasync_service_arn, node_name=datasync_service_name, node_type='datasync', metadata=metadata)

        # then
        expected = {'id': 'vertex:datasync:arn:aws:datasync:us-west-1:123456789012:service/datasync/data',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.datasync;',
                    'value': '<b>Name</b>: Data Sync<BR><b>ARN</b>: '
                             'arn:aws:datasync:us-west-1:123456789012:service/datasync/data<BR>-----------<BR><b>serviceName</b>: '
                             'datasync<BR><b>clusterArn</b>: '
                             'arn:aws:datasync:eu-west-1:123456789012:/datasync<BR><b>serviceRegistries</b>: '
                             'arn:aws:datasync:eu-west-1:123456789012:service/datasync<BR><b>status</b>: '
                             'ACTIVE<BR><b>launchType</b>: Data '
                             'Transfer<BR><b>platformVersion</b>: '
                             'LATEST<BR><b>platformFamily</b>: Linux',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'datasync', self.node_type)

        # docs
        self.mcd = mcd
