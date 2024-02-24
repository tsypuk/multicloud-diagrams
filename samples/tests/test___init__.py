from datetime import datetime
from unittest import TestCase

from multicloud_diagrams import extract_info
from multicloud_diagrams import prepare_path


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

    def test_prepare_path(self):
        testcases = [
            {
                "name": "Relative ../output folder",
                "history_dir": "history",
                "file_path": '../output/output.prod_plantuml.https.adr.drawio',
                "now": datetime(2021, 9, 1, 12, 30, 45),
                "expected": '../output/history/2021/09/output.prod_plantuml.https.adr.20210901.123045.drawio'
            },
            {
                "name": "Absolute ",
                "history_dir": "history",
                "file_path": '/tmp/output/output.prod_plantuml.https.adr.drawio',
                "now": datetime(2024, 1, 1, 12, 30, 45),
                "expected": '/tmp/output/history/2024/01/output.prod_plantuml.https.adr.20240101.123045.drawio'
            }
        ]
        for case in testcases:
            actual = prepare_path(case["history_dir"], case["file_path"], case["now"])
            self.assertEqual(
                case["expected"],
                actual,
                "failed test {} expected {}, actual {}".format(
                    case["name"], case["expected"], actual
                ),
            )
