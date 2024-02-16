from multicloud_diagrams import MultiCloudDiagrams
from samples.samples.aws_service_end_2_end import prepare_end2end


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    prev_file = f'../output/output.{prefix}_plantuml.https.adr.drawio'

    mcd.read_coords_from_file(prev_file)
    prepare_end2end(mcd)
    mcd.read_uml_mappings('uml_mapping.yml')

    label_style = {
        'labelBackgroundColor': 'none',
        'fontColor': '#FF3333',
        'fontStyle': 0,
        'fontSize': 14
    }
    style = {
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

    mcd.read_uml_from_http(md_http_endpoint="https://raw.githubusercontent.com/tsypuk/multicloud-diagrams/main/samples/samples/ADR.MD", start_line=11, base="process", edge_style=style, label_style=label_style)
    mcd.read_uml_from_http(md_http_endpoint="https://raw.githubusercontent.com/tsypuk/multicloud-diagrams/main/samples/samples/ADR.MD", start_line=37, base="load", edge_style=style, label_style=label_style)

    mcd.export_to_file(prev_file)


if __name__ == "__main__":
    main()
