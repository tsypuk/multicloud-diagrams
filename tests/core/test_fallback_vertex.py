from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_fallback_vertex(self):
        # docs
        self.node_type = 'non_existing_super_cloud_service'

        # given
        mcd = MultiCloudDiagrams()

        # when
        arn = 'arn:aws:non_existing_super_cloud_service:eu-west-1:123456789012:mock_data'
        metadata = {
            "Owner": 123456789012,
            "CDC Offset": 3,
            "Throttling": 100
        }
        mcd.add_vertex(node_id=arn, node_name='non_existing_super_cloud_service', node_type='non_existing_super_cloud_service', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:non_existing_super_cloud_service:arn:aws:non_existing_super_cloud_service:eu-west-1:123456789012:mock_data',
            'parent': '1',
            'style': 'sketch=0;aspect=fixed;html=1;points=[];align=left;image;fontSize=12;image=img/lib/mscae/Info.svg;',
            'value': '<b>Name</b>: non_existing_super_cloud_service<BR><b>ID</b>: '
                     'arn:aws:non_existing_super_cloud_service:eu-west-1:123456789012:mock_data<BR>-----------<BR><b>Owner</b>: '
                     '123456789012<BR><b>CDC Offset</b>: 3<BR><b>Throttling</b>: 100',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'mock_data', 'fallback_vertex')

        # docs
        self.mcd = mcd
