from unittest import TestCase

from multicloud_diagrams import extract_actors_and_participants


class Test(TestCase):

    def test_extract_actors_and_participants(self):
        testcases = [
            {"name": "process",
             "file_name": "../samples/process.plantuml",
             "expected": ([], ['SQS', 'LambdaFunction2', 'Storage'])
             },
            {"name": "same_entity_diff_elements2",
             "file_name": "../samples/same_entity_diff_elements2.plantuml",
             "expected": (['Donald'], ['stage1', 'S3Bucket'])
             },
            {"name": "same_entity_diff_elements",
             "file_name": "../samples/same_entity_diff_elements.plantuml",
             "expected": (['Donald'], ['stage1', 'S3Bucket', 'stage2', 'SNS', 'SQS'])
             },
            {"name": "file_upload",
             "file_name": "../samples/file_upload.plantuml",
             "expected": (['Donald'], ['S3Bucket', 'LambdaFunction1', 'SNS', 'SQS'])
             },
            {"name": "features",
             "file_name": "../samples/features.plantuml",
             "expected": ([], ['S3Bucket', 'LambdaFunction1', 'SNS', 'SQS', 'LambdaFunction2', 'Storage'])
             },
            {"name": "features",
             "file_name": "../samples/features.plantuml",
             "expected": ([], ['S3Bucket', 'LambdaFunction1', 'SNS', 'SQS', 'LambdaFunction2', 'Storage'])
             },
        ]

        for case in testcases:
            with open(case["file_name"], 'r') as file:
                sequence_diagram = file.read()
            actual = extract_actors_and_participants(sequence_diagram)
            self.assertEqual(
                case["expected"],
                actual,
                "failed test {} expected {}, actual {}".format(case["name"], case["expected"], actual),
            )
