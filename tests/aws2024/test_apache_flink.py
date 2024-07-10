from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_apache_flink(self):
        # docs
        self.node_type = 'apache_flink'

        # given
        mcd = MultiCloudDiagrams()

        # when
        apache_flink_arn = 'arn:aws:apache_flink:us-west-1:123456789012:apache_flink/123'
        apache_flink_name = 'Registry for images'
        metadata = {
            'ApplicationName': 'DemoAppProcesor',
            'RuntimeEnvironment': 'FLINK-1_8',
            'InputSchema': {
                'RecordFormat': {
                    'RecordFormatType': 'JSON'
                }
            },
            'FlinkApplicationConfiguration': {
                'CheckpointConfiguration': {
                    'ConfigurationType': 'DEFAULT',
                    'CheckpointingEnabled': True,
                    'CheckpointInterval': 60,
                    'MinPauseBetweenCheckpoints': 10
                },
                'ParallelismConfiguration': {
                    'ConfigurationType': 'DEFAULT',
                    'Parallelism': 3,
                    'ParallelismPerKPU': 10,
                    'AutoScalingEnabled': True
                }
            }
        }
        mcd.add_vertex(node_id=apache_flink_arn, node_name=apache_flink_name, node_type='apache_flink', metadata=metadata)

        # then
        expected = {'id': 'vertex:apache_flink:arn:aws:apache_flink:us-west-1:123456789012:apache_flink/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.managed_service_for_apache_flink;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:apache_flink:us-west-1:123456789012:apache_flink/123<BR>-----------<BR><b>ApplicationName</b>: '
                             'DemoAppProcesor<BR><b>RuntimeEnvironment</b>: '
                             "FLINK-1_8<BR><b>InputSchema</b>: {'RecordFormat': "
                             "{'RecordFormatType': "
                             "'JSON'}}<BR><b>FlinkApplicationConfiguration</b>: "
                             "{'CheckpointConfiguration': {'ConfigurationType': 'DEFAULT', "
                             "'CheckpointingEnabled': True, 'CheckpointInterval': 60, "
                             "'MinPauseBetweenCheckpoints': 10}, 'ParallelismConfiguration': "
                             "{'ConfigurationType': 'DEFAULT', 'Parallelism': 3, "
                             "'ParallelismPerKPU': 10, 'AutoScalingEnabled': True}}",
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'apache_flink', self.node_type)

        # docs
        self.mcd = mcd
