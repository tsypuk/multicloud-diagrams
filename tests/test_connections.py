from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities
import xml.etree.ElementTree as Et


class TestMCDConnections(TestUtilities):

    def test_dynamo(self):
        # given
        mcd = MultiCloudDiagrams()

        sqs_arn = 'arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo'
        sqs_metadata = {
            "FifoQueue": "TRUE",
        }
        func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:consumer_lambda'
        func_metadata = {
            "CodeSize": 1234,
            "Memory": 128,
        }

        # when
        mcd.add_vertex(node_id=func_arn, node_name='consumer_lambda', node_type='lambda_function', metadata=func_metadata)
        mcd.add_vertex(node_id=sqs_arn, node_name='int-eu-live-events.fifo', node_type='sqs', metadata=sqs_metadata)
        mcd.add_link(src_node_id=f'lambda_function:{func_arn}', dst_node_id=f'sqs:{sqs_arn}', action=['Action1, Action2'])

        # then
        expected_sqs = {
            'id': 'vertex:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo',
            'parent': '1',
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;'
                     'dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;',
            'value': '<b>Name</b>: int-eu-live-events.fifo<BR><b>ARN</b>: '
                     'arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo<BR>-----------<BR><b>FifoQueue</b>: '
                     'TRUE',
            'vertex': '1'}

        expected_lambda = {
            'id': 'vertex:lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:consumer_lambda',
            'parent': '1',
            'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;shape=mxgraph.aws3.lambda_function;'
                     'prIcon=server;fillColor=#F58534;gradientColor=none;html=1;',
            'value': '<b>Name</b>: consumer_lambda<BR><b>ARN</b>: '
                     'arn:aws:lambda:eu-west-1:123456789012:function:consumer_lambda<BR>-----------<BR><b>CodeSize</b>: '
                     '1234<BR><b>Memory</b>: 128',
            'vertex': '1'}

        expected_connection = {
            'edge': '2',
            'id': 'edge:lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:consumer_lambda:to:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo',
            'parent': '1',
            'source': 'vertex:lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:consumer_lambda',
            'style': 'jettySize=auto;html=1;startArrow=none;endArrow=none;',
            'target': 'vertex:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo'}

        expected_label = {
            'connectable': '0',
            'id': 'label:lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:consumer_lambda:to:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo',
            'parent': 'edge:lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:consumer_lambda:to:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo',
            'style': 'edgeLabel;html=1;align=left;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;',
            'value': 'Action1, Action2',
            'vertex': '1'}

        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.assertEqual(6, len(mx_cells))
        self.verify_mx_cell(mx_cells[0], expected={'id': '0'})
        self.verify_mx_cell(mx_cells[1], expected={'id': '1', 'parent': '0'})

        if 'style' in expected_sqs:
            del expected_sqs['style']
        expected_sqs['style'] = self.supported_vertex['sqs']['style']

        if 'style' in expected_lambda:
            del expected_lambda['style']
        expected_lambda['style'] = self.supported_vertex['lambda_function']['style']

        self.verify_mx_cell(mx_cells[2], expected_lambda)
        self.verify_mx_cell(mx_cells[3], expected_sqs)
        self.verify_mx_cell(mx_cells[4], expected_connection)
        self.verify_mx_cell(mx_cells[5], expected_label)

        # vertex lambda_function
        children = mx_cells[2].findall("./*")
        mx_geometry = children[0]

        self.verify_mx_geometry(children)
        self.assertEqual(self.supported_vertex['lambda_function']['height'], mx_geometry.attrib['height'])
        self.assertEqual(self.supported_vertex['lambda_function']['width'], mx_geometry.attrib['width'])

        # vertex sqs
        children = mx_cells[3].findall("./*")
        mx_geometry = children[0]
        self.verify_mx_geometry(children)
        self.assertEqual(self.supported_vertex['sqs']['height'], mx_geometry.attrib['height'])
        self.assertEqual(self.supported_vertex['sqs']['width'], mx_geometry.attrib['width'])

        # edge lambda_function-2-sqs
        self.verify_mx_geometry(mx_cells[4].findall("./*"))

        # label
        self.verify_mx_geometry(mx_cells[5].findall("./*"))

        # mcd.dump()
