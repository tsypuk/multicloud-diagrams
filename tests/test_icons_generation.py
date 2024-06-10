import json

from multicloud_diagrams import MultiCloudDiagrams
from utils.utils import TestUtilities


def modify_content_between_markers(file_path, start_marker, end_marker, new_content):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    skip = False
    added_content = False

    for line in lines:
        if start_marker in line:
            skip = True
            new_lines.append(line)
            new_lines.append(new_content + '\n')
            added_content = True
            continue
        if end_marker in line and skip:
            skip = False
        if not skip:
            new_lines.append(line)
        if end_marker in line and added_content:
            # new_lines.append(line)
            added_content = False

    with open(file_path, 'w') as file:
        file.writelines(new_lines)


class TestIconsGeneration(TestUtilities):

    def test_datasync(self):
        # load aws provider nodes
        file_path = './multicloud_diagrams/providers/aws.json'

        # Open and load the JSON file
        with open(file_path, 'r') as file:
            aws_provider_nodes = json.load(file)

        # Print all keys of the aws_provider_nodes
        md_content = ''
        for aws_service in aws_provider_nodes.keys():
            print(aws_service)
            service_data = aws_provider_nodes.get(aws_service, {})
            # Print the content for verification
            print(json.dumps(service_data, indent=4))

            # prepare icons md text
            md_content += f"![{aws_service}.jpg](https://github.com/tsypuk/multicloud-diagrams/raw/main/docs/icons/jpg/{aws_service}.jpg?raw=True)"

            # given
            mcd = MultiCloudDiagrams()

            # when
            mcd.add_vertex(node_id=aws_service, node_name=aws_service, node_type=aws_service, hide_name=True)

            mcd.export_to_file(f'./tmp/drawio/{aws_service}.drawio')

        # update index.md file
        # Define the file path and markers
        file_path = './docs/index.md'
        start_marker = '## Icons'
        end_marker = '---'

        # Call the function to modify content
        modify_content_between_markers(file_path, start_marker, end_marker, md_content)
