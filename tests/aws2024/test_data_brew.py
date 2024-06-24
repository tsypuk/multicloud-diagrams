from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_data_brew(self):
        # docs
        self.node_type = 'data_brew'

        # given
        mcd = MultiCloudDiagrams()

        # when
        data_brew_arn = 'arn:aws:data_brew:us-west-1:123456789012:data_brew/123'
        data_brew_name = 'Registry for images'
        metadata = {
            'DatasetName': 'population',
            'EncryptionMode': 'SSE-S3',
            'Name': 'Demo Project',
            'Type': 'RECIPE',
            'LogSubscription': 'ENABLE',
            'MaxCapacity': 3,
            'MaxRetries': 5,
            'CompressionFormat': 'SNAPPY',
            'Format': 'PARQUET',
            'MaxOutputFiles': 128,
            'DataCatalogId': 'xraf12asf',
            'DatabaseName': 'crawler',
            'TableName': 'Dataset1',

        }
        mcd.add_vertex(node_id=data_brew_arn, node_name=data_brew_name, node_type='data_brew', metadata=metadata)

        # then
        expected = {'id': 'vertex:data_brew:arn:aws:data_brew:us-west-1:123456789012:data_brew/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.glue_databrew;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:data_brew:us-west-1:123456789012:data_brew/123<BR>-----------<BR><b>DatasetName</b>: '
                             'population<BR><b>EncryptionMode</b>: SSE-S3<BR><b>Name</b>: Demo '
                             'Project<BR><b>Type</b>: RECIPE<BR><b>LogSubscription</b>: '
                             'ENABLE<BR><b>MaxCapacity</b>: 3<BR><b>MaxRetries</b>: '
                             '5<BR><b>CompressionFormat</b>: SNAPPY<BR><b>Format</b>: '
                             'PARQUET<BR><b>MaxOutputFiles</b>: 128<BR><b>DataCatalogId</b>: '
                             'xraf12asf<BR><b>DatabaseName</b>: crawler<BR><b>TableName</b>: '
                             'Dataset1',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'data_brew', self.node_type)

        # docs
        self.mcd = mcd
