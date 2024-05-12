from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_exchange(self):
        # docs
        self.node_type = 'exchange'

        # given
        mcd = MultiCloudDiagrams()

        # when
        exchange_service_arn = 'arn:aws:exchange:us-west-1:123456789012:service/exchange/data'
        exchange_service_name = 'Exchange'
        metadata = {
            "serviceName": "datasync",
            "clusterArn": "arn:aws:exchange:eu-west-1:123456789012:/exchange",
            "serviceRegistries": "arn:aws:exchange:eu-west-1:123456789012:service/exchange",
            "status": "ACTIVE",
            "launchType": "SFTP connection",
        }
        mcd.add_vertex(node_id=exchange_service_arn, node_name=exchange_service_name, node_type='exchange', metadata=metadata)

        # then
        expected = {'id': 'vertex:exchange:arn:aws:exchange:us-west-1:123456789012:service/exchange/data',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.data_exchange;',
                    'value': '<b>Name</b>: Exchange<BR><b>ARN</b>: '
                             'arn:aws:exchange:us-west-1:123456789012:service/exchange/data<BR>-----------<BR><b>serviceName</b>: '
                             'datasync<BR><b>clusterArn</b>: '
                             'arn:aws:exchange:eu-west-1:123456789012:/exchange<BR><b>serviceRegistries</b>: '
                             'arn:aws:exchange:eu-west-1:123456789012:service/exchange<BR><b>status</b>: '
                             'ACTIVE<BR><b>launchType</b>: SFTP connection',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'exchange', self.node_type)

        # docs
        self.mcd = mcd
