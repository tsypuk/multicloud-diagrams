from multicloud_diagrams import MultiCloudDiagrams
from samples.samples.aws_service_end_2_end import prepare_end2end


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'

    mcd.add_layer("services")
    mcd.augment_from_yaml('l1-services.yml')

    # mcd.add_layer("data")
    # mcd.augment_from_yaml('l2-data.yml')

    result_file = f'../output/output.{prefix}_layers.drawio'
    mcd.export_to_file(result_file)


if __name__ == "__main__":
    main()
