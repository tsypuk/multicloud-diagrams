from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_elastic_fabric_adapter(self):
        # docs
        self.node_type = 'elastic_fabric_adapter'

        # given
        mcd = MultiCloudDiagrams()

        # when
        elastic_fabric_adapter_arn = 'arn:aws:elastic_fabric_adapter:us-west-1:123456789012:elastic_fabric_adapter/123'
        elastic_fabric_adapter_name = 'Registry for images'
        metadata = {
            'network-info.efa-info.maximum-efa-interfaces': 4,
            'network-info.efa-supported': True,
            'Attachment': {
                'AttachmentId': 777,
                'DeleteOnTermination': True,
                'DeviceIndex': 1,
                'NetworkCardIndex': 3,
                'InstanceId': 'x75759g9s-re',
                'InstanceOwnerId': 'EJ',
                'Status': 'attached'
            }
        }
        mcd.add_vertex(node_id=elastic_fabric_adapter_arn, node_name=elastic_fabric_adapter_name, node_type='elastic_fabric_adapter', metadata=metadata)

        # then
        expected = {'id': 'vertex:elastic_fabric_adapter:arn:aws:elastic_fabric_adapter:us-west-1:123456789012:elastic_fabric_adapter/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_fabric_adapter;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:aws:elastic_fabric_adapter:us-west-1:123456789012:elastic_fabric_adapter/123<BR>-----------<BR><b>network-info.efa-info.maximum-efa-interfaces</b>: '
                             '4<BR><b>network-info.efa-supported</b>: True<BR><b>Attachment</b>: '
                             "{'AttachmentId': 777, 'DeleteOnTermination': True, 'DeviceIndex': "
                             "1, 'NetworkCardIndex': 3, 'InstanceId': 'x75759g9s-re', "
                             "'InstanceOwnerId': 'EJ', 'Status': 'attached'}",
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'elastic_fabric_adapter', self.node_type)

        # docs
        self.mcd = mcd
