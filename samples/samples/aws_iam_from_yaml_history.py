from multicloud_diagrams import MultiCloudDiagrams


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    output_file = f'../output/output.{prefix}.iam-roles-from-yaml.drawio'
    mcd.read_coords_from_file(output_file)

    # Read cloud resources declared in yaml format
    mcd.augment_from_yaml('augmented_resources.yaml')
    mcd.update_history_repo(output_file)


if __name__ == "__main__":
    main()
