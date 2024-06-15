from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_outpost(self):
        # docs
        self.node_type = 'lake_formation'

        # given
        mcd = MultiCloudDiagrams()

        # when
        outpost_arn = 'arn:aws:lake_formation:us-west-1:123456789012:lake_formation/123'
        outpost_name = 'Registry for images'
        metadata = {
            'CatalogId': '1234567890',
            'InstanceArn': 'arn:aws:lake_formation:us-west-1:123456789012:lake_formation/123',
            'ApplicationArn': 'arn:aws:app:us-west-1:123456789012:app/123',
            'ExternalFiltering': {
                'Status': 'ENABLED',
                'AuthorizedTargets': [
                    'arn:aws:iam:us-west-1:123456789012:iam/123222',
                ]
            },
            'ShareRecipients': [
                {
                    'DataLakePrincipalIdentifier': 'enabled'
                },
            ],
        }
        mcd.add_vertex(node_id=outpost_arn, node_name=outpost_name, node_type='lake_formation', metadata=metadata)

        # then
        expected = {'id': 'vertex:lake_formation:arn:aws:lake_formation:us-west-1:123456789012:lake_formation/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lake_formation;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:lake_formation:us-west-1:123456789012:lake_formation/123<BR>-----------<BR><b>CatalogId</b>: '
                             '1234567890<BR><b>InstanceArn</b>: '
                             'arn:aws:lake_formation:us-west-1:123456789012:lake_formation/123<BR><b>ApplicationArn</b>: '
                             'arn:aws:app:us-west-1:123456789012:app/123<BR><b>ExternalFiltering</b>: '
                             "{'Status': 'ENABLED', 'AuthorizedTargets': "
                             "['arn:aws:iam:us-west-1:123456789012:iam/123222']}<BR><b>ShareRecipients</b>: "
                             "[{'DataLakePrincipalIdentifier': 'enabled'}]",
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'lake_formation', self.node_type)

        # docs
        self.mcd = mcd
