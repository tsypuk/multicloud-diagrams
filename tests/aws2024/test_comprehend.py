from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_comprehend(self):
        # docs
        self.node_type = 'comprehend'

        # given
        mcd = MultiCloudDiagrams()

        # when
        comprehend_arn = 'arn:aws:comprehend:us-west-1:123456789012:comprehend/123'
        comprehend_name = 'Comprehend'
        metadata = {
            'DatasetArn': 'ARN',
            'DatasetName': 'location service',
            'DatasetType': 'TRAIN',
            'DatasetS3Uri': 'ARN',
            'Description': 'lat, lon data',
            'Status': 'CREATING',
            'Message': 'check the status',
            'NumberOfDocuments': 4,
        }
        mcd.add_vertex(node_id=comprehend_arn, node_name=comprehend_name, node_type='comprehend', metadata=metadata)

        # then
        expected = {'id': 'vertex:comprehend:arn:aws:comprehend:us-west-1:123456789012:comprehend/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.comprehend;',
                    'value': '<b>Name</b>: Comprehend<BR><b>ARN</b>: '
                             'arn:aws:comprehend:us-west-1:123456789012:comprehend/123<BR>-----------<BR><b>DatasetArn</b>: '
                             'ARN<BR><b>DatasetName</b>: location service<BR><b>DatasetType</b>: '
                             'TRAIN<BR><b>DatasetS3Uri</b>: ARN<BR><b>Description</b>: lat, lon '
                             'data<BR><b>Status</b>: CREATING<BR><b>Message</b>: check the '
                             'status<BR><b>NumberOfDocuments</b>: 4',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'comprehend', self.node_type)

        # docs
        self.mcd = mcd
