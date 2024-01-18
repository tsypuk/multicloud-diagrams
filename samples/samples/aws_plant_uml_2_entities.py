from multicloud_diagrams import MultiCloudDiagrams
from samples.samples.aws_service_end_2_end import prepare_end2end


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    prev_file = f'../output/output.{prefix}_plantuml_2_entities.end2end.drawio'

    mcd.read_coords_from_file(prev_file)
    prepare_end2end(mcd)

    mcd.read_uml_mappings('same_entity_diff_elements.yaml')
    label_style = {
        'labelBackgroundColor': 'none',
        'fontColor': '#FF3333',
        'fontStyle': 0,
        'fontSize': 14
    }
    style1 = {
        'orthogonalLoop': '1',
        'edgeStyle': 'orthogonalEdgeStyle',
        'curved': '1',
        'startArrow': 'oval',
        'endArrow': 'classicThin',
        'dashed': '1',
        'strokeColor': '#FF3333',
        'strokeWidth': '3',
        'fontSize': '22'
    }
    mcd.read_uml_from_file('same_entity_diff_elements.plantuml', edge_style=style1, label_style=label_style)

    result_file = f'../output/output.{prefix}_plantuml_2_entities.end2end.drawio'
    mcd.export_to_file(result_file)


if __name__ == "__main__":
    main()
