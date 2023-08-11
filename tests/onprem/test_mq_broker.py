from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestHttpVertexInIsolation(TestRendering):

    def test_mq_broker(self):
        # docs
        self.node_type = 'mq_broker'

        # given
        mcd = MultiCloudDiagrams()

        # when
        arn = 'mq.eventbroker.somedomain.com'
        metadata = {
            "Nodes": 4,
            "Active Master": 1,
            "Errors": 3,
            "Storage": "4G",
            "Client": 15
        }
        mcd.add_vertex(node_id=arn, node_name='broker', node_type='mq_broker', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:mq_broker:mq.eventbroker.somedomain.com',
            'parent': '1',
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B0084D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;'
                     'verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.mq_broker;',
            'value': '<b>Name</b>: broker<BR><b>ID</b>: '
                     'mq.eventbroker.somedomain.com<BR>-----------<BR><b>Nodes</b>: '
                     '4<BR><b>Active Master</b>: 1<BR><b>Errors</b>: 3<BR><b>Storage</b>: '
                     '4G<BR><b>Client</b>: 15',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'broker', 'mq_broker')

        # docs
        self.mcd = mcd
