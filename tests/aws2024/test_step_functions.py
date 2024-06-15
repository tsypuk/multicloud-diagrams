from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_step_functions(self):
        # docs
        self.node_type = 'step_functions'

        # given
        mcd = MultiCloudDiagrams()

        # when
        step_functions_service_arn = 'arn:aws:step_function:us-west-1:123456789012:service/step_function/1'
        step_functions_service_name = 'Step Functions'
        metadata = {
            'stateMachineArn': 'arn:aws:step_function:us-west-1:123456789012:service/step_function/machine1',
            'name': 'JobPoller',
            'status': 'ACTIVE',
            'roleArn': 'arn:aws:iam:us-west-1:123456789012:iam/roles/1',
            'type': 'STANDARD',
        }
        mcd.add_vertex(node_id=step_functions_service_arn, node_name=step_functions_service_name, node_type='step_functions', metadata=metadata)

        # then
        expected = {'id': 'vertex:step_functions:arn:aws:step_function:us-west-1:123456789012:service/step_function/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#E7157B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.step_functions;',
                    'value': '<b>Name</b>: Step Functions<BR><b>ARN</b>: '
                             'arn:aws:step_function:us-west-1:123456789012:service/step_function/1<BR>-----------<BR><b>stateMachineArn</b>: '
                             'arn:aws:step_function:us-west-1:123456789012:service/step_function/machine1<BR><b>name</b>: '
                             'JobPoller<BR><b>status</b>: ACTIVE<BR><b>roleArn</b>: '
                             'arn:aws:iam:us-west-1:123456789012:iam/roles/1<BR><b>type</b>: '
                             'STANDARD',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'step_functions', self.node_type)

        # docs
        self.mcd = mcd
