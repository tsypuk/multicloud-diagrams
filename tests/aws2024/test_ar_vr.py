from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_ar_vr(self):
        # docs
        self.node_type = 'ar_vr'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ar_vr_arn = 'arn:aws:ar_vr:us-west-1:123456789012:ar_vr/123'
        ar_vr_name = 'Registry for images'
        metadata = {
            'CreationTime': '2024-22-06',
            'FailureReason': 'Connection Loss',
            'FailureCode': '153',
            'HumanLoopStatus': 'Completed',
            'HumanLoopName': 'MainRender',
        }
        mcd.add_vertex(node_id=ar_vr_arn, node_name=ar_vr_name, node_type='ar_vr', metadata=metadata)

        # then
        expected = {'id': 'vertex:ar_vr:arn:aws:ar_vr:us-west-1:123456789012:ar_vr/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F34482;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ar_vr;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:ar_vr:us-west-1:123456789012:ar_vr/123<BR>-----------<BR><b>CreationTime</b>: '
                             '2024-22-06<BR><b>FailureReason</b>: Connection '
                             'Loss<BR><b>FailureCode</b>: 153<BR><b>HumanLoopStatus</b>: '
                             'Completed<BR><b>HumanLoopName</b>: MainRender',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ar_vr', self.node_type)

        # docs
        self.mcd = mcd
