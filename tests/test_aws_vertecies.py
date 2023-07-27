from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as et

from utils.utils import TestUtilities


class Test_MCD_AWS_Vertex_Isolation(TestUtilities):

    def test_dynamo(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        table_arn = 'arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table'
        table_name = 'prod-dynamo-table'
        metadata = {
            'DeletionProtectionEnabled': True,
            'ItemCount': 900,
            'TableSizeBytes': 123
        }
        mcd.add_vertex(id=table_arn, node_name=table_name, arn=table_arn, node_type='dynamo', metadata=metadata)


        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_vertex_in_isolation(mx_cells)

        expected = {
            'id': 'vertex:dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
            'value': '<b>Name</b>: prod-dynamo-table<BR><b>ARN</b>: arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table <BR>-----------<BR><b>DeletionProtectionEnabled</b>: True<BR><b>ItemCount</b>: 900<BR><b>TableSizeBytes</b>: 123',
            'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.dynamo_db;fillColor=#2E73B8;gradientColor=none;',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_mx_cell(mx_cells[2], expected)

    def test_sqs(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        sqs_arn = 'arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo'
        metadata = {
            "DelaySeconds": 0,
            "FifoQueue": "TRUE",
            "ReceiveMessageWaitTimeSeconds": 0,
            "SqsManagedSseEnabled": "false",
            "VisibilityTimeout": 30
        }
        mcd.add_vertex(id=sqs_arn, node_name='int-eu-live-events.fifo', arn=sqs_arn, node_type='sqs', metadata=metadata)

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_vertex_in_isolation(mx_cells)

        expected = {
            'id': 'vertex:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo',
            'value': '<b>Name</b>: int-eu-live-events.fifo<BR><b>ARN</b>: arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo <BR>-----------<BR><b>DelaySeconds</b>: 0<BR><b>FifoQueue</b>: TRUE<BR><b>ReceiveMessageWaitTimeSeconds</b>: 0<BR><b>SqsManagedSseEnabled</b>: false<BR><b>VisibilityTimeout</b>: 30',
            'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;fillColor=#F58534;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_mx_cell(mx_cells[2], expected)

    def test_sns(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        sns_arn = 'arn:aws:sns:eu-west-1:123456789012:internal.fifo'
        metadata = {
            "Owner": 123456789012,
            "SubscriptionsConfirmed": 3,
            "SubscriptionsPending": 0
        }
        mcd.add_vertex(id=sns_arn, node_name='internal.fifo', arn=sns_arn, node_type='sns', metadata=metadata)

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_vertex_in_isolation(mx_cells)

        expected = {
            'id': 'vertex:sns:arn:aws:sns:eu-west-1:123456789012:internal.fifo',
            'value': '<b>Name</b>: internal.fifo<BR><b>ARN</b>: arn:aws:sns:eu-west-1:123456789012:internal.fifo <BR>-----------<BR><b>Owner</b>: 123456789012<BR><b>SubscriptionsConfirmed</b>: 3<BR><b>SubscriptionsPending</b>: 0',
            'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_mx_cell(mx_cells[2], expected)


    def test_lambda(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        func_arn = 'arn:aws:lambda:eu-west-1:123456789:function:producer-lambda'
        metadata = {
            "CodeSize": 1234,
            "Handler": "main",
            "Layers": 0,
            "Memory": 128,
            "PackageType": "Zip",
            "Runtime": "go1.x",
            "Timeout": 30,
            "TracingConfig": "{'Mode': 'Active'}",
            "Version": "$LATEST"
        }
        mcd.add_vertex(id=func_arn, node_name='producer-lambda', arn=func_arn, node_type='lambda_function', metadata=metadata)

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_vertex_in_isolation(mx_cells)

        expected = {
            'id': 'vertex:lambda_function:arn:aws:lambda:eu-west-1:123456789:function:producer-lambda',
            'value': "<b>Name</b>: producer-lambda<BR><b>ARN</b>: arn:aws:lambda:eu-west-1:123456789:function:producer-lambda <BR>-----------<BR><b>CodeSize</b>: 1234<BR><b>Handler</b>: main<BR><b>Layers</b>: 0<BR><b>Memory</b>: 128<BR><b>PackageType</b>: Zip<BR><b>Runtime</b>: go1.x<BR><b>Timeout</b>: 30<BR><b>TracingConfig</b>: {'Mode': 'Active'}<BR><b>Version</b>: $LATEST",
            'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;shape=mxgraph.aws3.lambda_function;prIcon=server;fillColor=#F58534;gradientColor=none;html=1;',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_mx_cell(mx_cells[2], expected)


