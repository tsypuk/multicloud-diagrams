from unittest import TestCase

from multicloud_diagrams import extract_info


class Test(TestCase):

    def test_extract_info(self):
        result = extract_info("S3Bucket-->LambdaFunction1: LifeConfig Rule invokes lambda function")
        self.assertEqual(('S3Bucket', 'LambdaFunction1', 'LifeConfig Rule invokes lambda function'), result)

    def test_extract_info_2(self):
        testcases = [
            {"name": "-->",
             "input": "S3Bucket --> LambdaFunction1: LifeConfig Rule invokes lambda function",
             "expected": ('S3Bucket', 'LambdaFunction1', 'LifeConfig Rule invokes lambda function')
             },
            {"name": "->>",
             "input": "LambdaFunction1 ->> SNS: Send Event to SNS that file processing is finished",
             "expected": ('LambdaFunction1', 'SNS', 'Send Event to SNS that file processing is finished')
             },
            {"name": "->",
             "input": "SQS -> LambdaFunction2: poll message from SQS and invoke consumer lambda function",
             "expected": ('SQS', 'LambdaFunction2', 'poll message from SQS and invoke consumer lambda function')
             },
            {"name": "-->>",
             "input": "LambdaFunction2 -->> Storage: Update DynamoDB Table. Save image status.",
             "expected": ('LambdaFunction2', 'Storage', 'Update DynamoDB Table. Save image status.')
             },
            {"name": "--> nospace",
             "input": "S3Bucket-->LambdaFunction1: LifeConfig Rule invokes lambda function",
             "expected": ('S3Bucket', 'LambdaFunction1', 'LifeConfig Rule invokes lambda function')
             },
            {"name": "->> nospace",
             "input": "LambdaFunction1->>SNS: Send Event to SNS that file processing is finished",
             "expected": ('LambdaFunction1', 'SNS', 'Send Event to SNS that file processing is finished')
             },
            {"name": "-> nospace",
             "input": "SQS->LambdaFunction2: poll message from SQS and invoke consumer lambda function",
             "expected": ('SQS', 'LambdaFunction2', 'poll message from SQS and invoke consumer lambda function')
             },
            {"name": "-->> nospace",
             "input": "LambdaFunction2-->>Storage: Update DynamoDB Table. Save image status.",
             "expected": ('LambdaFunction2', 'Storage', 'Update DynamoDB Table. Save image status.')
             },

            {"name": "--> nolabel",
             "input": "S3Bucket-->LambdaFunction1",
             "expected": ('S3Bucket', 'LambdaFunction1', '')
             },
            {"name": "->> nolabel",
             "input": "LambdaFunction1->>SNS",
             "expected": ('LambdaFunction1', 'SNS', '')
             },
            {"name": "-> nolabel",
             "input": "SQS->LambdaFunction2",
             "expected": ('SQS', 'LambdaFunction2', '')
             },
            {"name": "-->> nolabel",
             "input": "LambdaFunction2-->>Storage",
             "expected": ('LambdaFunction2', 'Storage', '')
             },

        ]

        for case in testcases:
            actual = extract_info(case["input"])
            self.assertEqual(
                case["expected"],
                actual,
                "failed test {} expected {}, actual {}".format(
                    case["name"], case["expected"], actual
                ),
            )
