from multicloud_diagrams import MultiCloudDiagrams
from samples.samples.aws_service_end_2_end import prepare_end2end


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    prev_file = f'../output/output.{prefix}_plantuml_2_entities_2uml.end2end.drawio'

    mcd.read_coords_from_file(prev_file)
    prepare_end2end(mcd)

    mcd.read_uml_mappings('same_entity_diff_elements.yaml')
    label_style = {
        'labelBackgroundColor': 'none',
        'fontColor': '#FF3333',
        'fontStyle': 0,
        'fontSize': 14
    }
    edge_style = {
        'orthogonalLoop': '1',
        'edgeStyle': 'orthogonalEdgeStyle',
        'curved': '1',
        'startArrow': 'oval',
        'endArrow': 'classicThin',
        'dashed': '1',
        'strokeColor': '#FF3333',
        'strokeWidth': '1',
        'fontSize': '22'
    }
    label_style2 = {
        'labelBackgroundColor': 'none',
        'fontColor': '#0A0CA4',
        'fontStyle': 0,
        'fontSize': 14
    }
    edge_style2 = {
        'orthogonalLoop': '1',
        'edgeStyle': 'orthogonalEdgeStyle',
        'curved': '1',
        'startArrow': 'oval',
        'endArrow': 'classicThin',
        'dashed': '1',
        'strokeColor': '#0A0CA4',
        'strokeWidth': '1',
        'fontSize': '22'
    }
    mcd.read_uml_from_file('same_entity_diff_elements.plantuml', edge_style=edge_style, label_style=label_style)
    mcd.read_uml_from_file('same_entity_diff_elements2.plantuml', edge_style=edge_style2, label_style=label_style2)

    mcd.export_to_file(prev_file)


if __name__ == "__main__":
    main()
