from multicloud_diagrams import MultiCloudDiagrams
from samples.samples.aws_service_end_2_end import prepare_end2end


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    prev_file = f'../output/output.{prefix}_plantuml.end2end.drawio'

    mcd.read_coords_from_file(prev_file)
    prepare_end2end(mcd)

    mcd.read_uml_mappings('uml_mapping.yml')

    style = {
        'orthogonalLoop': '1',
        'edgeStyle': 'orthogonalEdgeStyle',
        'curved': '1',
        'startArrow': 'oval',
        'endArrow': 'classicThin',
        'dashed': '1',
        'strokeColor': '#0000FF',
        'strokeWidth': '3',
        'fontSize': '22'
    }

    label_style = {
        'labelBackgroundColor': 'none',
        'fontColor': '#00FF00',
        'fontStyle': 0,
        'fontSize': 14
    }
    mcd.read_uml_from_file('features.plantuml', edge_style=style, label_style=label_style)

    result_file = f'../output/output.{prefix}_features.drawio'
    mcd.export_to_file(result_file)


if __name__ == "__main__":
    main()
