from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_application_composer(self):
        # docs
        self.node_type = 'application_composer'

        # given
        mcd = MultiCloudDiagrams()

        # when
        application_composer_service_arn = 'arn:aws:application_composer:us-west-1:123456789012:service/application_composer/123'
        application_composer_name = 'Application Composer'
        metadata = {
            'env': 'Prod',
            'entities': 50,
            'style': 'standard',
            'connections': 'dotted',
        }
        mcd.add_vertex(node_id=application_composer_service_arn, node_name=application_composer_name, node_type='application_composer', metadata=metadata)

        # then
        expected = {'id': 'vertex:application_composer:arn:aws:application_composer:us-west-1:123456789012:service/application_composer/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.application_composer;',
                    'value': '<b>Name</b>: Application Composer<BR><b>ARN</b>: '
                             'arn:aws:application_composer:us-west-1:123456789012:service/application_composer/123<BR>-----------<BR><b>env</b>: '
                             'Prod<BR><b>entities</b>: 50<BR><b>style</b>: '
                             'standard<BR><b>connections</b>: dotted',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'application_composer', self.node_type)

        # docs
        self.mcd = mcd
