from unittest import TestCase

from multicloud_diagrams import MultiCloudDiagrams


class TestMultiCloudDiagramsAWSVertecies(TestCase):

    def test_drawio_preambula(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        roots = tree.findall(".")
        root = roots[0]

        # then
        self.assertEqual(1, len(roots))
        self.assertEqual('mxfile', root.tag)
        self.assertEqual('multicloud-diagrams', root.attrib['host'])
        self.assertEqual('PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license.',
                         root.attrib['agent'])
        self.assertEqual('MultiCloud', root.attrib['type'])