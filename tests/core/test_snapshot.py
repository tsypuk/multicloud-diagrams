import json

from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_snapshot(self):
        # docs
        self.node_type = 'snapshot'

        # given
        mcd = MultiCloudDiagrams()
        mcd.read_coords_from_file('docs/docs/core-components/output/drawio/snapshot.drawio')

        snapshot = json.dumps(
            {
                "200": {
                    "responseParameters": {
                        "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization'",
                        "method.response.header.Access-Control-Allow-Methods": "'OPTIONS,GET,POST'",
                        "method.response.header.Access-Control-Allow-Origin": "'*'"
                    },
                    "statusCode": "200"
                }
            }, indent=4)

        # when
        mcd.add_snapshot(table_name='Integration Response', snapshot=snapshot)

        # then
        expected = {
            'id': 'vertex:Integration Response:list',
            'parent': '1',
            'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;'
                     'resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
            'value': '<b>Integration Response</b>',
            'vertex': '1'
        }
        expected_list = [
            {'id': '0'},
            {'id': '1', 'parent': '0'},
            {'id': 'vertex:Integration Response:list',
             'parent': '1',
             'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;'
                      'resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
             'value': '<b>Integration Response</b>',
             'vertex': '1'},
            {'id': 'vertex:Integration Response:row:1',
             'parent': 'vertex:Integration Response:list',
             'style': 'text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;'
                      'overflow=hidden;portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;',
             'value': '{\n'
                      '    "200": {\n'
                      '        "responseParameters": {\n'
                      '            "method.response.header.Access-Control-Allow-Headers": '
                      '"\'Content-Type,X-Amz-Date,Authorization\'",\n'
                      '            "method.response.header.Access-Control-Allow-Methods": '
                      '"\'OPTIONS,GET,POST\'",\n'
                      '            "method.response.header.Access-Control-Allow-Origin": '
                      '"\'*\'"\n'
                      '        },\n'
                      '        "statusCode": "200"\n'
                      '    }\n'
                      '}',
             'vertex': '1'}
        ]
        self.verify_list(expected=expected, mx_file=mcd.mx_file, resource_name='LSI:users_to_model-users-idx', expected_list=expected_list)

        # docs
        self.mcd = mcd
