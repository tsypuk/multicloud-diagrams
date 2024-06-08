from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_app_runner(self):
        # docs
        self.node_type = 'app_runner'

        # given
        mcd = MultiCloudDiagrams()

        # when
        apprunner_service_arn = 'arn:aws:app_runner:us-west-1:123456789012:service/app_runner/123'
        appruner_service_name = 'App Runner'
        metadata = {
            "serviceName": "app_runner",
            'Cpu': '2',
            'Memory': '1024',
            'Protocol': 'TCP | HTTP',
            'Path': '/root/domain',
            'Interval': 123,
            'Timeout': 123,
            'HealthyThreshold': 123,
            'UnhealthyThreshold': 123,
            'Type': 'BRANCH',
            'Runtime': 'PYTHON_3 | NODEJS_18',
            'BuildCommand': 'poetry install'
        }
        mcd.add_vertex(node_id=apprunner_service_arn, node_name=appruner_service_name, node_type='app_runner', metadata=metadata)

        # then
        expected = {'id': 'vertex:app_runner:arn:aws:app_runner:us-west-1:123456789012:service/app_runner/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.app_runner;',
                    'value': '<b>Name</b>: App Runner<BR><b>ARN</b>: '
                             'arn:aws:app_runner:us-west-1:123456789012:service/app_runner/123<BR>-----------<BR><b>serviceName</b>: '
                             'app_runner<BR><b>Cpu</b>: 2<BR><b>Memory</b>: '
                             '1024<BR><b>Protocol</b>: TCP | HTTP<BR><b>Path</b>: '
                             '/root/domain<BR><b>Interval</b>: 123<BR><b>Timeout</b>: '
                             '123<BR><b>HealthyThreshold</b>: 123<BR><b>UnhealthyThreshold</b>: '
                             '123<BR><b>Type</b>: BRANCH<BR><b>Runtime</b>: PYTHON_3 | '
                             'NODEJS_18<BR><b>BuildCommand</b>: poetry install',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'app_runner', self.node_type)

        # docs
        self.mcd = mcd
