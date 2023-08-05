from multicloud_diagrams import MultiCloudDiagrams


def prepare_data_model(mcd):
    # DynamoDB Table definition based on AWS specification
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_table.html
    dynamo_table = {
        'AttributeDefinitions': [
            {
                'AttributeName': 'first',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'second',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'third',
                'AttributeType': 'B'
            },
        ],
        'TableName': 'prod-dynamo-table',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'
            },
        ],
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'firstIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'IndexSizeBytes': 777,
                'ItemCount': 123,
            },
            {
                'IndexName': 'secondIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'alternativeKey',
                        'KeyType': 'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'IndexSizeBytes': 777,
                'ItemCount': 123,
            }
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'string',
                'KeySchema': [
                    {
                        'AttributeName': 'string',
                        'KeyType': 'HASH'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL',
                    'NonKeyAttributes': [
                        'string',
                    ]
                },
                'IndexSizeBytes': 123,
                'ItemCount': 123,
                'IndexStatus': 'ACTIVE',
                'ProvisionedThroughput': {
                    'NumberOfDecreasesToday': 123,
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                }
            },
        ],
        'StreamSpecification': {
            'StreamEnabled': True,
            'StreamViewType': 'NEW_IMAGE'
        },
        'LatestStreamLabel': "2023-04-14T08:29:21.074",
        'LatestStreamArn': "arn:aws:dynamodb:eu-west-1:123456789:table/prod-dynamo-table/stream",
        'Replicas': [
            {
                'RegionName': 'string',
                'ReplicaStatus': 'ACTIVE',
                'ReplicaStatusDescription': 'string',
                'ReplicaStatusPercentProgress': 'string',
                'KMSMasterKeyId': 'string',
                'ProvisionedThroughputOverride': {
                    'ReadCapacityUnits': 123
                },
                'GlobalSecondaryIndexes': [
                    {
                        'IndexName': 'string',
                        'ProvisionedThroughputOverride': {
                            'ReadCapacityUnits': 123
                        }
                    },
                ],
                'ReplicaTableClassSummary': {
                    'TableClass': 'STANDARD'
                }
            },
        ],
        'RestoreSummary': {
            'SourceBackupArn': 'string',
            'SourceTableArn': 'string',
            'RestoreInProgress': False
        },
        'SSEDescription': {
            'Status': 'ENABLED',
            'SSEType': 'KMS',
            'KMSMasterKeyArn': 'string',
        },
        'DeletionProtectionEnabled': True
    }

    table_arn = dynamo_table['TableArn']
    table_name = dynamo_table['TableName']
    metadata = {
        'DeletionProtectionEnabled': dynamo_table['DeletionProtectionEnabled'],
        'ItemCount': dynamo_table['ItemCount'],
        'TableSizeBytes': dynamo_table['TableSizeBytes']
    }

    mcd.add_vertex(node_id=table_arn, node_name=table_name, arn=table_arn, node_type='dynamo', metadata=metadata)

    # DynamoDB Stream
    stream_arn = dynamo_table['LatestStreamArn']
    stream_metadata = {
        "LatestStreamLabel": dynamo_table['LatestStreamLabel'],
        "StreamViewType": dynamo_table['StreamSpecification']['StreamViewType']
    }
    mcd.add_vertex(node_id=stream_arn, node_name=dynamo_table['LatestStreamLabel'], arn=stream_arn, node_type='dynamo_stream', metadata=stream_metadata)
    mcd.add_link(f'dynamo:{table_arn}', f'dynamo_stream:{stream_arn}', action=['DynamoDBStream'])

    # KeySchema
    rows_keys = []
    for attribute in dynamo_table['KeySchema']:
        rows_keys.append(attribute['AttributeName'] + ' : ' + attribute['KeyType'])
    mcd.add_list(table_name=f'Schema:{table_name}', rows=rows_keys)
    mcd.add_link(f'dynamo:{table_arn}', f'Schema:{table_name}:list', action=['Key Schema'])

    # Attributes
    rows = []
    for attribute in dynamo_table['AttributeDefinitions']:
        rows.append(attribute['AttributeName'] + ' : ' + attribute['AttributeType'])
    mcd.add_list(table_name=f'Attributes:{table_name}', rows=rows)
    mcd.add_link(src_node_id=f'dynamo:{table_arn}', dst_node_id=f'Attributes:{table_name}:list', action=['AttributeDefinitions'])

    # Local Secondary Indexes
    if 'LocalSecondaryIndexes' in dynamo_table:
        attributes = []
        for attribute in dynamo_table['LocalSecondaryIndexes']:
            attributes.append('IndexName: ' + attribute['IndexName'])
        mcd.add_list(table_name=f'LSIs:{table_name}', rows=attributes)
        mcd.add_link(f'dynamo:{table_arn}', f'LSIs:{table_name}:list', action=['index: LSI'])

        for attribute in dynamo_table['LocalSecondaryIndexes']:
            attributes = []
            index_name = attribute['IndexName']
            attributes.append('IndexName: ' + index_name)
            attributes.append('IndexSizeBytes: ' + str(attribute['IndexSizeBytes']))
            attributes.append('ItemCount: ' + str(attribute['ItemCount']))
            attributes.append('ProjectionType: ' + attribute['Projection']['ProjectionType'])

            rows_schema = '{ '
            for schema_attribute in attribute['KeySchema']:
                rows_schema += (schema_attribute['AttributeName'] + ': ' + schema_attribute['KeyType'] + ',')
            rows_schema = rows_schema.rstrip(rows_schema[-1]) + '}'
            attributes.append('Schema: ' + rows_schema)

            mcd.add_list(table_name=f'LSI:{table_name}-{index_name}', rows=attributes)
            mcd.add_link(f'LSIs:{table_name}:list', f'LSI:{table_name}-{index_name}:list', action=[f'LSI : {index_name}'])

    # Global Secondary Indexes
    if 'GlobalSecondaryIndexes' in dynamo_table:
        rows = []
        for attribute in dynamo_table['GlobalSecondaryIndexes']:
            rows.append('IndexName: ' + attribute['IndexName'])
        mcd.add_list(table_name=f'GSIs:{table_name}', rows=rows)
        mcd.add_link(f'dynamo:{table_arn}', f'GSIs:{table_name}:list', action=['index: GSI'])

        for attribute in dynamo_table['GlobalSecondaryIndexes']:
            rows = []
            index_name = attribute['IndexName']
            rows.append('IndexName: ' + index_name)
            rows.append('IndexSizeBytes: ' + str(attribute['IndexSizeBytes']))
            rows.append('IndexStatus: ' + attribute['IndexStatus'])
            rows.append('ItemCount: ' + str(attribute['ItemCount']))
            rows.append('RCU: ' + str(attribute['ProvisionedThroughput']['ReadCapacityUnits']))
            rows.append('WCU: ' + str(attribute['ProvisionedThroughput']['WriteCapacityUnits']))
            rows.append('ProjectionType: ' + attribute['Projection']['ProjectionType'])

            rows_schema = '{ '
            for schema_attribute in attribute['KeySchema']:
                rows_schema += (schema_attribute['AttributeName'] + ': ' + schema_attribute['KeyType'] + ',')
            rows_schema = rows_schema.rstrip(rows_schema[-1]) + '}'
            rows.append('Schema: ' + rows_schema)

            mcd.add_list(table_name=f'GSI:{table_name}-{index_name}', rows=rows)
            mcd.add_link(f'GSIs:{table_name}:list', f'GSI:{table_name}-{index_name}:list', action=[f'GSI : {index_name}'])


def main():
    prefix = 'prod'

    mcd = MultiCloudDiagrams()
    data_file = f'../output/output.{prefix}.dynamo.drawio'
    mcd.read_coords_from_file(data_file)

    prepare_data_model(mcd)
    mcd.export_to_file(data_file)


if __name__ == "__main__":
    main()
