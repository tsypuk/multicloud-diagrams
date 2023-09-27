from multicloud_diagrams import MultiCloudDiagrams
from samples.samples.aws_service_end_2_end import prepare_end2end


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    prev_file = f'../output/output.{prefix}.end2end.drawio'
    result_file = f'../output/output.{prefix}_uml.end2end.drawio'

    mcd.read_coords_from_file(prev_file)
    prepare_end2end(mcd)

    mcd.read_uml_mappings('uml_mapping.yml')
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
    mcd.read_uml_from_file('file_upload.mermaid', style=style1)

    style2 = {
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

    mcd.read_uml_from_file('process.mermaid', style=style2)

    mcd.export_to_file(result_file)


if __name__ == "__main__":
    main()
