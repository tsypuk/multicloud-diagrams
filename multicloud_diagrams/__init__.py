import xml.etree.ElementTree as ET


class MultiCloudDiagrams():
    def __init__(self):
        self.mxfile = ET.Element('mxfile', host="multicloud-diagrams",
                                 agent="PIP package multicloud-diagrams to generate MultiCloud Diagrams resources into draw.io compatible format @Roman Tsypuk 2023",
                                 type="MultiCloud")
        self.diagram = ET.SubElement(self.mxfile, 'diagram', id="diagram_1", name="AWS components")
        self.mxGraphModel = ET.SubElement(self.diagram, 'mxGraphModel', dx="1015", dy="661", grid="1", gridSize="10",
                                          guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                          pageScale="1", pageWidth="850", pageHeight="1100", math="0", shadow="0")
        self.root = ET.SubElement(self.mxGraphModel, 'root')
        self.mxCellID0 = ET.SubElement(self.root, 'mxCell', id="0")
        self.mxCellID1 = ET.SubElement(self.root, 'mxCell', id="1", parent="0")
