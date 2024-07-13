from multicloud_diagrams import MultiCloudDiagrams


def main():
    mcd = MultiCloudDiagrams(hide_id=True)

    prefix = 'prod'
    result_file = f'../output/output.{prefix}_layers.drawio'
    mcd.read_coords_from_file(result_file)
    mcd.add_layer("services")
    mcd.augment_from_yaml('l1-services.yml')

    mcd.add_layer("data")
    mcd.augment_from_yaml('l2-data.yml')

    mcd.add_layer("streaming")
    mcd.augment_from_yaml('l3-stream.yml')

    mcd.export_to_file(result_file)


if __name__ == "__main__":
    main()
