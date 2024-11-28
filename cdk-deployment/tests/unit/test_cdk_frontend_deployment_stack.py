import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_frontend_deployment.cdk_frontend_deployment_stack import CdkFrontendDeploymentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_frontend_deployment/cdk_frontend_deployment_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkFrontendDeploymentStack(app, "cdk-frontend-deployment")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
