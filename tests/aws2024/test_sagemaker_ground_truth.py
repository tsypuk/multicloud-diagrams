from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_sagemaker_ground_truth(self):
        # docs
        self.node_type = 'sagemaker_ground_truth'

        # given
        mcd = MultiCloudDiagrams()

        # when
        sagemaker_ground_truth_arn = 'arn:aws:sagemaker_ground_truth:us-west-1:123456789012:sagemaker_ground_truth/123'
        sagemaker_ground_truth_name = 'Registry for images'
        metadata = {
            'DataSource': {
                'S3DataSource': {
                    'ManifestS3Uri': 'arn:aws:s3:::content_bucket'
                },
                'SnsDataSource': {
                    'SnsTopicArn': 'arn:aws:sns:eu-west-1:123456789012:internal.fifo'
                }
            },
            'DataAttributes': {
                'ContentClassifiers': [
                    'FreeOfAdultContent',
                ]
            },
            'StoppingConditions': {
                'MaxHumanLabeledObjectCount': 123,
                'MaxPercentageOfInputDatasetLabeled': 123
            },
            'TaskTitle': 'Explore car parts',
            'TaskDescription': 'Human-based detection',
            'NumberOfHumanWorkersPerDataObject': 4,
            'TaskTimeLimitInSeconds': 600,
            'TaskAvailabilityLifetimeInSeconds': 3600,
            'MaxConcurrentTaskCount': 5,
        }
        mcd.add_vertex(node_id=sagemaker_ground_truth_arn, node_name=sagemaker_ground_truth_name, node_type='sagemaker_ground_truth', metadata=metadata)

        # then
        expected = {'id': 'vertex:sagemaker_ground_truth:arn:aws:sagemaker_ground_truth:us-west-1:123456789012:sagemaker_ground_truth/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sagemaker_ground_truth;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:sagemaker_ground_truth:us-west-1:123456789012:sagemaker_ground_truth/123<BR>-----------<BR><b>DataSource</b>: '
                             "{'S3DataSource': {'ManifestS3Uri': 'arn:aws:s3:::content_bucket'}, "
                             "'SnsDataSource': {'SnsTopicArn': "
                             "'arn:aws:sns:eu-west-1:123456789012:internal.fifo'}}<BR><b>DataAttributes</b>: "
                             "{'ContentClassifiers': "
                             "['FreeOfAdultContent']}<BR><b>StoppingConditions</b>: "
                             "{'MaxHumanLabeledObjectCount': 123, "
                             "'MaxPercentageOfInputDatasetLabeled': 123}<BR><b>TaskTitle</b>: "
                             'Explore car parts<BR><b>TaskDescription</b>: Human-based '
                             'detection<BR><b>NumberOfHumanWorkersPerDataObject</b>: '
                             '4<BR><b>TaskTimeLimitInSeconds</b>: '
                             '600<BR><b>TaskAvailabilityLifetimeInSeconds</b>: '
                             '3600<BR><b>MaxConcurrentTaskCount</b>: 5',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'sagemaker_ground_truth', self.node_type)

        # docs
        self.mcd = mcd
