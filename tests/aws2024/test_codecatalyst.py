from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codecatalyst(self):
        # docs
        self.node_type = 'codecatalyst'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codecatalyst_service_arn = 'arn:aws:codecatalyst:us-west-1:123456789012:service/codecatalyst/123'
        codecatalyst_name = 'Code Catalyst'
        metadata = {
            'spaceName': 'Java',
            'name': 'spring boot app',
            'displayName': 'Controller BMS',
            'description': 'Management system'
        }
        mcd.add_vertex(node_id=codecatalyst_service_arn, node_name=codecatalyst_name, node_type='codecatalyst', metadata=metadata)

        # then
        expected = {'id': 'vertex:codecatalyst:arn:aws:codecatalyst:us-west-1:123456789012:service/codecatalyst/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codecatalyst;',
                    'value': '<b>Name</b>: Code Catalyst<BR><b>ARN</b>: '
                             'arn:aws:codecatalyst:us-west-1:123456789012:service/codecatalyst/123<BR>-----------<BR><b>spaceName</b>: '
                             'Java<BR><b>name</b>: spring boot app<BR><b>displayName</b>: '
                             'Controller BMS<BR><b>description</b>: Management system',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codecatalyst', self.node_type)

        # docs
        self.mcd = mcd
