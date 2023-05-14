from multicloud_diagrams import MultiCloudDiagrams


def prepare_data_model(mcd):
    # DynamoDB Table
    table_name = "prod-dynamo-table"
    dynamo_metadata = {
        "Capacity mode": "PAY_PER_REQUEST",
        "DeletionProtectionEnabled": False,
        "ItemCount": 10000,
        "Replicas": 0,
        "TableSizeBytes": 99999
    }
    table_arn = "arn:aws:dynamodb:eu-west-1:123456789:table/prod-dynamo-table"

    mcd.add_vertex(id=table_arn, node_name=table_name, arn=table_arn, node_type='dynamo', metadata=dynamo_metadata)

    # DynamoDB Stream
    stream_arn = "arn:aws:dynamodb:eu-west-1:123456789:table/prod-dynamo-table/stream"
    stream_metadata = {
        "LatestStreamLabel": "2023-04-14T08:29:21.074",
        "StreamViewType": "NEW_AND_OLD_IMAGES"
    }
    mcd.add_vertex(id=stream_arn, node_name="2023-14-12T08:29:21.074", arn=stream_arn, node_type='dynamo_stream', metadata=stream_metadata)
    mcd.add_link(f'dynamo:{table_arn}', f'dynamo_stream:{stream_arn}', action=['DynamoDBStream'])

    # KeySchema
    rows_keys = ['recordId : HASH']
    mcd.add_list(f'Schema:{table_name}', rows=rows_keys)
    mcd.add_link(f'dynamo:{table_arn}', f'Schema:{table_name}:list', action=['Key Schema'])


def main():
    prefix = 'prod'

    mcd = MultiCloudDiagrams()
    data_file = f'../output/output.{prefix}.dynamo.drawio'
    mcd.read_coords_from_file(data_file)

    prepare_data_model(mcd)
    mcd.export_to_file(data_file)


if __name__ == "__main__":
    main()
