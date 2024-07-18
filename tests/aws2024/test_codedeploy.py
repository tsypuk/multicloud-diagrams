from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_codedeploy(self):
        # docs
        self.node_type = 'codedeploy'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codedeploy_service_arn = 'arn:aws:codedeploy:us-west-1:123456789012:service/codedeploy/123'
        codedeploy_service_name = 'Code Deploy'
        metadata = {
            'deploymentGroupInfo': 'Apps and Front',
            'applicationName': 'Blogs',
            'deploymentGroupId': 3,
            'deploymentGroupName': 'ALB+CloudFront',
            'deploymentConfigName': 'from_cloud_formation',
            'ec2TagFilters': 'PROD',
        }
        mcd.add_vertex(node_id=codedeploy_service_arn, node_name=codedeploy_service_name, node_type='codedeploy', metadata=metadata)

        # then
        expected = {'id': 'vertex:codedeploy:arn:aws:codedeploy:us-west-1:123456789012:service/codedeploy/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codedeploy;',
                    'value': '<b>Name</b>: Code Deploy<BR><b>ARN</b>: '
                             'arn:aws:codedeploy:us-west-1:123456789012:service/codedeploy/123<BR>-----------<BR><b>deploymentGroupInfo</b>: '
                             'Apps and Front<BR><b>applicationName</b>: '
                             'Blogs<BR><b>deploymentGroupId</b>: 3<BR><b>deploymentGroupName</b>: '
                             'ALB+CloudFront<BR><b>deploymentConfigName</b>: '
                             'from_cloud_formation<BR><b>ec2TagFilters</b>: PROD',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codedeploy', self.node_type)

        # docs
        self.mcd = mcd
