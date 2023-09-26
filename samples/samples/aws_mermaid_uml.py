from multicloud_diagrams import MultiCloudDiagrams
from samples.samples.aws_service_end_2_end import prepare_end2end


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    prev_file = f'../output/output.{prefix}.end2end.drawio'
    result_file = f'../output/output.{prefix}_uml.end2end.drawio'

    mcd.read_coords_from_file(prev_file)
    prepare_end2end(mcd)

    mcd.read_uml_from_file('uml.mermaid')

    mcd.export_to_file(result_file)


if __name__ == "__main__":
    main()
