from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_app_sync(self):
        # docs
        self.node_type = 'app_sync'

        # given
        mcd = MultiCloudDiagrams()

        # when
        app_sync_service_arn = 'arn:aws:app_sync:us-west-1:123456789012:service/app_sync/123'
        app_sync_service_name = 'App Sync'
        metadata = {
            "serviceName": "app_sync",
            'userPoolId': '123',
            'awsRegion': 'eu-west-1',
            'defaultAction': 'ALLOW',
            'appIdClientRegex': '123*',
            'authenticationType': 'API_KEY |AMAZON_COGNITO_USER_POOLS',
            'xrayEnabled': True
        }
        mcd.add_vertex(node_id=app_sync_service_arn, node_name=app_sync_service_name, node_type='app_sync', metadata=metadata)

        # then
        expected = {'id': 'vertex:app_sync:arn:aws:app_sync:us-west-1:123456789012:service/app_sync/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.appsync;',
                    'value': '<b>Name</b>: App Sync<BR><b>ARN</b>: '
                             'arn:aws:app_sync:us-west-1:123456789012:service/app_sync/123<BR>-----------<BR><b>serviceName</b>: '
                             'app_sync<BR><b>userPoolId</b>: 123<BR><b>awsRegion</b>: '
                             'eu-west-1<BR><b>defaultAction</b>: '
                             'ALLOW<BR><b>appIdClientRegex</b>: '
                             '123*<BR><b>authenticationType</b>: API_KEY '
                             '|AMAZON_COGNITO_USER_POOLS<BR><b>xrayEnabled</b>: True',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'app_sync', self.node_type)

        # docs
        self.mcd = mcd
