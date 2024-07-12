from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_textract(self):
        # docs
        self.node_type = 'textract'

        # given
        mcd = MultiCloudDiagrams()

        # when
        textract_service_arn = 'arn:aws:textract:eu-west-1:123456789012:textract/1'
        textract_service_name = 'textract'
        metadata = {
            'AdapterId': 7,
            'AdapterName': 'ENG text detection',
            'CreationTime': '2024-11-07',
            'Description': 'full text scanning',
            'FeatureTypes': 'TABLES',
            'AutoUpdate': 'ENABLED',
            'Tags': 'PROD'
        }

        mcd.add_vertex(node_id=textract_service_arn, node_name=textract_service_name, node_type='textract', metadata=metadata)

        # then
        expected = {'id': 'vertex:textract:arn:aws:textract:eu-west-1:123456789012:textract/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.textract;',
                    'value': '<b>Name</b>: textract<BR><b>ARN</b>: '
                             'arn:aws:textract:eu-west-1:123456789012:textract/1<BR>-----------<BR><b>AdapterId</b>: '
                             '7<BR><b>AdapterName</b>: ENG text detection<BR><b>CreationTime</b>: '
                             '2024-11-07<BR><b>Description</b>: full text '
                             'scanning<BR><b>FeatureTypes</b>: TABLES<BR><b>AutoUpdate</b>: '
                             'ENABLED<BR><b>Tags</b>: PROD',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'textract', self.node_type)

        # docs
        self.mcd = mcd
