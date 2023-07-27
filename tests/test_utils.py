from unittest import TestCase


class TestUtilities(TestCase):

    def verify_mx_cell(self, mx_cell, expected):
        self.assertEqual('mxCell', mx_cell.tag)
        self.assertEqual(expected, mx_cell.attrib)
