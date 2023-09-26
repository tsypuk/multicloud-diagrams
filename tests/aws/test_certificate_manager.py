from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_dynamo(self):
        # docs
        self.node_type = 'certificate_manager'

        # given
        mcd = MultiCloudDiagrams()

        # when
        cert_manager_arn = 'arn:aws:acm:us-west-1:123456789012:certificate/cd2e'
        cert_manager_name = 'Client Certificate'
        metadata = {
            'Domain': 'client1.domain.tld',
            'Type': 'Imported',
            'Public Key info': 'RSA 2048',
            'Signature algorithm': 'SHA-256 with RSA'
        }
        mcd.add_vertex(node_id=cert_manager_arn, node_name=cert_manager_name, node_type='certificate_manager', metadata=metadata)

        # then
        expected = {'id': 'vertex:certificate_manager:arn:aws:acm:us-west-1:123456789012:certificate/cd2e',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F8624;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.certificate_manager;',
                    'value': '<b>Name</b>: Client Certificate<BR><b>ARN</b>: '
                             'arn:aws:acm:us-west-1:123456789012:certificate/cd2e<BR>-----------<BR><b>Domain</b>: '
                             'client1.domain.tld<BR><b>Type</b>: Imported<BR><b>Public Key '
                             'info</b>: RSA 2048<BR><b>Signature algorithm</b>: SHA-256 with RSA',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'Client Certificate', self.node_type)

        # docs
        self.mcd = mcd
