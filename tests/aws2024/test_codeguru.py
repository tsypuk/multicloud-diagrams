from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_bedrock(self):
        # docs
        self.node_type = 'codeguru'

        # given
        mcd = MultiCloudDiagrams()

        # when
        codeguru_arn = 'arn:aws:codeguru:us-west-1:123456789012:codeguru/123'
        codeguru_name = 'CodeGuru'
        metadata = {
            'Name': 'Pull request review',
            'CodeReviewArn': 'ARN',
            'RepositoryName': 'app1',
            'Owner': 'team1',
            'ProviderType': 'GitHub',
            'State': 'Completed',
            'StateReason': 'fix PR comments',
            'Type': 'PullRequest',
            'SourceCodeType': {
                'CommitDiff': {
                    'SourceCommit': '7fa554'
                }
            }
        }
        mcd.add_vertex(node_id=codeguru_arn, node_name=codeguru_name, node_type='codeguru', metadata=metadata)

        # then
        expected = {'id': 'vertex:codeguru:arn:aws:codeguru:us-west-1:123456789012:codeguru/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codeguru_2;',
                    'value': '<b>Name</b>: CodeGuru<BR><b>ARN</b>: '
                             'arn:aws:codeguru:us-west-1:123456789012:codeguru/123<BR>-----------<BR><b>Name</b>: '
                             'Pull request review<BR><b>CodeReviewArn</b>: '
                             'ARN<BR><b>RepositoryName</b>: app1<BR><b>Owner</b>: '
                             'team1<BR><b>ProviderType</b>: GitHub<BR><b>State</b>: '
                             'Completed<BR><b>StateReason</b>: fix PR comments<BR><b>Type</b>: '
                             "PullRequest<BR><b>SourceCodeType</b>: {'CommitDiff': "
                             "{'SourceCommit': '7fa554'}}",
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'codeguru', self.node_type)

        # docs
        self.mcd = mcd
