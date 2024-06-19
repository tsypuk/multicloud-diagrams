from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_elastic_beanstalk(self):
        # docs
        self.node_type = 'elastic_beanstalk'

        # given
        mcd = MultiCloudDiagrams()

        # when
        elastic_beanstalk_arn = 'arn:aws:elastic_beanstalk:us-west-1:123456789012:elastic_beanstalk/123'
        elastic_beanstalk_name = 'Registry for images'
        metadata = {
            'EnvironmentName': 'Production',
            'EnvironmentId': '1',
            'ApplicationName': 'events-processor',
            'VersionLabel': 'v2',
            'SolutionStackName': 'web-tier',
            'TemplateName': 'cdk',
            'Description': 'Processing onboarding events',
            'EndpointURL': 'https://mydomain.com',
            'CNAME': 'mydomain',
            'Status': 'Ready',
            'AbortableOperationInProgress': True,
            'Health': 'Green',
            'HealthStatus': 'Ok',

        }
        mcd.add_vertex(node_id=elastic_beanstalk_arn, node_name=elastic_beanstalk_name, node_type='elastic_beanstalk', metadata=metadata)

        # then
        expected = {'id': 'vertex:elastic_beanstalk:arn:aws:elastic_beanstalk:us-west-1:123456789012:elastic_beanstalk/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_beanstalk;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:elastic_beanstalk:us-west-1:123456789012:elastic_beanstalk/123<BR>-----------<BR><b>EnvironmentName</b>: '
                             'Production<BR><b>EnvironmentId</b>: 1<BR><b>ApplicationName</b>: '
                             'events-processor<BR><b>VersionLabel</b>: '
                             'v2<BR><b>SolutionStackName</b>: web-tier<BR><b>TemplateName</b>: '
                             'cdk<BR><b>Description</b>: Processing onboarding '
                             'events<BR><b>EndpointURL</b>: https://mydomain.com<BR><b>CNAME</b>: '
                             'mydomain<BR><b>Status</b>: '
                             'Ready<BR><b>AbortableOperationInProgress</b>: '
                             'True<BR><b>Health</b>: Green<BR><b>HealthStatus</b>: Ok',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'elastic_beanstalk', self.node_type)

        # docs
        self.mcd = mcd
