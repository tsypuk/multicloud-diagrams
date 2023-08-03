import json
import os
import subprocess
from datetime import datetime

from multicloud_diagrams import MultiCloudDiagrams


def get_git_tag() -> str:
    latest_tag = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).strip().decode("utf-8")
    return latest_tag


def get_commit_hash() -> str:
    latest_commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode("utf-8")
    return latest_commit_hash


def get_build_time() -> str:
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime


def main():
    # given
    project_folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(project_folder, 'landscape.json')

    with open(path, 'r') as file:
        json_data = json.load(file)

    mcd = MultiCloudDiagrams()
    mcd.read_coords_from_file('../landscape.drawio')

    git_tag = get_git_tag()

    build_time = get_build_time()

    rows = [
        f"Build Time: {build_time}",
        f"MultiCloud-Diagrams version: {git_tag}",
        f"Supported nodes: {len(json_data)}",
        f"HASH: {get_commit_hash()[:16]}"
    ]

    # when-then
    mcd.add_list(table_name='Build Details Landscape', rows=rows)

    for resource in json_data:
        meta = None
        if 'metadata' in resource['data']:
            meta = resource['data']['metadata']
        mcd.add_vertex(id=resource['data']['arn'], node_name=resource['data']['name'], arn=resource['data']['arn'], node_type=resource['resource_type'], metadata=meta)
    mcd.export_to_file('../landscape.drawio')


if __name__ == "__main__":
    main()
