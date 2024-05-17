from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_access_analyzer(self):
        # docs
        self.node_type = 'access_analyzer'

        # given
        mcd = MultiCloudDiagrams()

        # when
        access_analyzer_service_arn = 'arn:aws:access_analyzer:us-west-1:123456789012:service/access_analyzer'
        access_analyzer_service_name = 'AWS Access Analyzer'
        metadata = {
            "serviceName": "access_analyzer",
            "clusterArn": "arn:aws:access_analyzer:eu-west-1:123456789012:service/access_analyzer",
            "status": "ACTIVE",
            "findings": 12,
            "critical": 2,
            "minor": 10,
        }
        mcd.add_vertex(node_id=access_analyzer_service_arn, node_name=access_analyzer_service_name, node_type='access_analyzer', metadata=metadata)

        # then
        expected = {'id': 'vertex:access_analyzer:arn:aws:access_analyzer:us-west-1:123456789012:service/access_analyzer',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#BF0816;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.access_analyzer;',
                    'value': '<b>Name</b>: AWS Access Analyzer<BR><b>ARN</b>: '
                             'arn:aws:access_analyzer:us-west-1:123456789012:service/access_analyzer<BR>-----------<BR><b>serviceName</b>: '
                             'access_analyzer<BR><b>clusterArn</b>: '
                             'arn:aws:access_analyzer:eu-west-1:123456789012:service/access_analyzer<BR><b>status</b>: '
                             'ACTIVE<BR><b>findings</b>: 12<BR><b>critical</b>: '
                             '2<BR><b>minor</b>: 10',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'access_analyzer', self.node_type)

        # docs
        self.mcd = mcd
