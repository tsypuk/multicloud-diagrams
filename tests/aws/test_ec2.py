from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_ec2(self):
        # docs
        self.node_type = 'ec2'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ec2_arn = 'arn:i-1234567890abcdef0'
        ec2_name = 'Test Instance'
        metadata = {
            "AmiLaunchIndex": 0,
            "ImageId": "ami-0abcdef1234567890",
            "InstanceId": "i-1234567890abcdef0",
            "InstanceType": "t3.nano",
            "KeyName": "my-key-pair",
            "LaunchTime": "2022-11-15T10:48:59+00:00",
            "Monitoring": {
                "State": "disabled"
            },
            "Placement": {
                "AvailabilityZone": "us-east-2a",
                "GroupName": "",
                "Tenancy": "default"
            },
            "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal",
            "PrivateIpAddress": "10-0-0-157",
            "ProductCodes": [],
            "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com",
            "PublicIpAddress": "34.253.223.13",
            "SubnetId": "subnet-04a636d18e83cfacb",
            "VpcId": "vpc-1234567890abcdef0",
            "Architecture": "x86_64",
            "Hypervisor": "xen"
        }
        mcd.add_vertex(node_id=ec2_arn, node_name=ec2_name, node_type='ec2', metadata=metadata)

        # then
        expected = {'id': 'vertex:ec2:arn:i-1234567890abcdef0',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ec2;',
                    'value': '<b>Name</b>: Test Instance<BR><b>ARN</b>: '
                             'arn:i-1234567890abcdef0<BR>-----------<BR><b>AmiLaunchIndex</b>: '
                             '0<BR><b>ImageId</b>: ami-0abcdef1234567890<BR><b>InstanceId</b>: '
                             'i-1234567890abcdef0<BR><b>InstanceType</b>: '
                             't3.nano<BR><b>KeyName</b>: my-key-pair<BR><b>LaunchTime</b>: '
                             "2022-11-15T10:48:59+00:00<BR><b>Monitoring</b>: {'State': "
                             "'disabled'}<BR><b>Placement</b>: {'AvailabilityZone': 'us-east-2a', "
                             "'GroupName': '', 'Tenancy': 'default'}<BR><b>PrivateDnsName</b>: "
                             'ip-10-0-0-157.us-east-2.compute.internal<BR><b>PrivateIpAddress</b>: '
                             '10-0-0-157<BR><b>ProductCodes</b>: []<BR><b>PublicDnsName</b>: '
                             'ec2-34-253-223-13.us-east-2.compute.amazonaws.com<BR><b>PublicIpAddress</b>: '
                             '34.253.223.13<BR><b>SubnetId</b>: '
                             'subnet-04a636d18e83cfacb<BR><b>VpcId</b>: '
                             'vpc-1234567890abcdef0<BR><b>Architecture</b>: '
                             'x86_64<BR><b>Hypervisor</b>: xen',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'Client Certificate', self.node_type)

        # docs
        self.mcd = mcd
