from unittest import TestCase

from multicloud_diagrams import extract_resource_from_endpoint


class Test(TestCase):

    def test_extract_resource_from_endpoint(self):
        testcases = [
            {"name": "http",
             "input": "http://some.domain.com/dir/dir2/resource.MD",
             "expected": 'resource.MD'
             },
            {"name": "https",
             "input": "https://some.domain.com/dir/dir2/resource.MD",
             "expected": 'resource.MD'
             }
        ]
        for case in testcases:
            actual = extract_resource_from_endpoint(case["input"])
            self.assertEqual(
                case["expected"],
                actual,
                "failed test {} expected {}, actual {}".format(
                    case["name"], case["expected"], actual
                ),
            )
