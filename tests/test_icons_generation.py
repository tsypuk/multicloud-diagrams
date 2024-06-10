import json

from multicloud_diagrams import MultiCloudDiagrams
from utils.utils import TestUtilities


class TestIconsGeneration(TestUtilities):

    def test_datasync(self):
        ## load aws provider nodes
        file_path = '../multicloud_diagrams/providers/aws.json'

        # Open and load the JSON file
        with open(file_path, 'r') as file:
            aws_provider_nodes = json.load(file)

        # Print all keys of the aws_provider_nodes
        for aws_service in aws_provider_nodes.keys():
            print(aws_service)
            service_data = aws_provider_nodes.get(aws_service, {})
            # Print the content for verification
            print(json.dumps(service_data, indent=4))

            # given
            mcd = MultiCloudDiagrams()

            # when
            mcd.add_vertex(node_id=aws_service, node_name=aws_service, node_type=aws_service, hide_name=True)

            mcd.export_to_file(f'../docs/icons/drawio/{aws_service}.drawio')
        # docs
        self.mcd = mcd