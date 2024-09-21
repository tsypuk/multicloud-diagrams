from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_quicksight(self):
        # docs
        self.node_type = 'quicksight'

        # given
        mcd = MultiCloudDiagrams()

        # when
        quicksight_service_arn = 'arn:aws:quicksight:us-west-1:123456789012:service/quicksight/1'
        quicksight_service_name = 'QuickSight'
        metadata = {
            'DashboardId': 'Custom Dataset',
            'Name': 'Aggregation of Req/rate',
            'Status': 'CREATION_SUCCESSFUL'
        }
        mcd.add_vertex(node_id=quicksight_service_arn, node_name=quicksight_service_name, node_type='quicksight', metadata=metadata)

        # then
        expected = {'id': 'vertex:quicksight:arn:aws:quicksight:us-west-1:123456789012:service/quicksight/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.quicksight;',
                    'value': '<b>Name</b>: QuickSight<BR><b>ARN</b>: '
                             'arn:aws:quicksight:us-west-1:123456789012:service/quicksight/1<BR>-----------<BR><b>DashboardId</b>: '
                             'Custom Dataset<BR><b>Name</b>: Aggregation of '
                             'Req/rate<BR><b>Status</b>: CREATION_SUCCESSFUL',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'quicksight', self.node_type)

        # docs
        self.mcd = mcd
