from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_data_pipeline(self):
        # docs
        self.node_type = 'data_pipeline'

        # given
        mcd = MultiCloudDiagrams()

        # when
        data_pipeline_arn = 'arn:aws:data_pipeline:us-west-1:123456789012:data_pipeline/123'
        data_pipeline_name = 'Registry for images'
        metadata = {
            'pipelineId': '123',
            'name': 'Demo-pipeline',
            'key': 'Field1',
            'stringValue': 'test',
            'refValue': 'ARN',
            'description': 'Details',
        }
        mcd.add_vertex(node_id=data_pipeline_arn, node_name=data_pipeline_name, node_type='data_pipeline', metadata=metadata)

        # then
        expected = {'id': 'vertex:data_pipeline:arn:aws:data_pipeline:us-west-1:123456789012:data_pipeline/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.data_pipeline;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:data_pipeline:us-west-1:123456789012:data_pipeline/123<BR>-----------<BR><b>pipelineId</b>: '
                             '123<BR><b>name</b>: Demo-pipeline<BR><b>key</b>: '
                             'Field1<BR><b>stringValue</b>: test<BR><b>refValue</b>: '
                             'ARN<BR><b>description</b>: Details',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'data_pipeline', self.node_type)

        # docs
        self.mcd = mcd
