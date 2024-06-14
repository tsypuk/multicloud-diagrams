from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_glue(self):
        # docs
        self.node_type = 'glue'

        # given
        mcd = MultiCloudDiagrams()

        # when
        step_glue_service_arn = 'arn:aws:glue:us-west-1:123456789012:service/glue/1'
        step_glue_service_name = 'Glue'
        metadata = {
            'stateMachineArn': 'arn:aws:glue:us-west-1:123456789012:service/step_function/machine1',
            'JobMode': 'NOTEBOOK',
            'ExecutionProperty': {
                'MaxConcurrentRuns': 123
            },
            'MaxRetries': 5,
            'AllocatedCapacity': 1024,
            'Timeout': 250,
            'MaxCapacity': 10.0,
            'WorkerType': 'G.1X'
        }
        mcd.add_vertex(node_id=step_glue_service_arn, node_name=step_glue_service_name, node_type='glue', metadata=metadata)

        # then
        expected = {'id': 'vertex:glue:arn:aws:glue:us-west-1:123456789012:service/glue/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.glue;',
                    'value': '<b>Name</b>: Glue<BR><b>ARN</b>: '
                             'arn:aws:glue:us-west-1:123456789012:service/glue/1<BR>-----------<BR><b>stateMachineArn</b>: '
                             'arn:aws:glue:us-west-1:123456789012:service/step_function/machine1<BR><b>JobMode</b>: '
                             "NOTEBOOK<BR><b>ExecutionProperty</b>: {'MaxConcurrentRuns': "
                             '123}<BR><b>MaxRetries</b>: 5<BR><b>AllocatedCapacity</b>: '
                             '1024<BR><b>Timeout</b>: 250<BR><b>MaxCapacity</b>: '
                             '10.0<BR><b>WorkerType</b>: G.1X',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'glue', self.node_type)

        # docs
        self.mcd = mcd
