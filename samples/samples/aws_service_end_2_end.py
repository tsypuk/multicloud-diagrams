from multicloud_diagrams import MultiCloudDiagrams


def prepare_end2end(mcd):
    producer_func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:producer-lambda'
    metadata = {
        "CodeSize": 1234,
        "Handler": "main",
        "Layers": 0,
        "Memory": 128,
        "PackageType": "Zip",
        "Runtime": "go1.x",
        "Timeout": 30,
        "TracingConfig": "{'Mode': 'Active'}",
        "Version": "$LATEST"
    }
    mcd.add_vertex(node_id=producer_func_arn, node_name='producer-lambda', node_type='lambda_function', metadata=metadata)

    consumer_func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:consumer-lambda'
    mcd.add_vertex(node_id=consumer_func_arn, node_name='consumer-lambda', node_type='lambda_function')

    dynamo_arn = 'arn:aws:dynamodb:eu-west-1:123456789012:table/table1'
    mcd.add_vertex(node_id=dynamo_arn, node_name='table1', node_type='dynamo')

    sns_arn = 'arn:aws:sns:eu-west-1:123456789012:internal.fifo'
    metadata = {
        "Owner": 123456789,
        "SubscriptionsConfirmed": 3,
        "SubscriptionsPending": 0
    }
    mcd.add_vertex(node_id=sns_arn, node_name='internal', node_type='sns', metadata=metadata)

    sqs_arn = 'arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo'
    metadata = {
        "DelaySeconds": 0,
        "FifoQueue": "TRUE",
        "ReceiveMessageWaitTimeSeconds": 0,
        "SqsManagedSseEnabled": "false",
        "VisibilityTimeout": 30
    }
    mcd.add_vertex(node_id=sqs_arn, node_name='events', node_type='sqs', metadata=metadata)

    sqs_arn2 = 'arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events2.fifo'
    mcd.add_vertex(node_id=sqs_arn2, node_name='events2', node_type='sqs')

    s3_arn = 'arn:aws:s3:::bucket_name/key_name'
    mcd.add_vertex(node_id=s3_arn, node_name='key_name', node_type='s3')

    mcd.add_link(src_node_id=f'lambda_function:{producer_func_arn}', dst_node_id=f'sns:{sns_arn}')
    mcd.add_link(src_node_id=f'lambda_function:{producer_func_arn}', dst_node_id=f's3:{s3_arn}')
    mcd.add_link(src_node_id=f'sns:{sns_arn}', dst_node_id=f'sqs:{sqs_arn}')
    mcd.add_link(src_node_id=f'sns:{sns_arn}', dst_node_id=f'sqs:{sqs_arn2}')
    mcd.add_link(src_node_id=f'sqs:{sqs_arn}', dst_node_id=f'lambda_function:{consumer_func_arn}')
    mcd.add_link(src_node_id=f'lambda_function:{consumer_func_arn}', dst_node_id=f'dynamo:{dynamo_arn}')


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    roles_file = f'../output/output.{prefix}.end2end.drawio'

    mcd.read_coords_from_file(roles_file)
    prepare_end2end(mcd)

    mcd.export_to_file(roles_file)


if __name__ == "__main__":
    main()
