from aws_cdk import App as CdkApp, SecretValue, Stack
from constructs import Construct
from aws_cdk.aws_codebuild import BuildSpec
from aws_cdk.aws_amplify_alpha import App as AmplifyApp, GitHubSourceCodeProvider

class AmplifyFrontendStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Define the Amplify App
        amplify_app = AmplifyApp(
            self, "RateMyCourses", # this "id" will be used as the Amplify app name
            source_code_provider=GitHubSourceCodeProvider(
                owner="jfm-code",
                repository="rate-my-courses",
                oauth_token=SecretValue.secrets_manager("jfm-PAT-token") # have to use AWS secret manager
            )
        )

        # Add environment variables and branch
        amplify_app.add_environment("VUE_APP_API_URL", "http://127.0.0.1:5000")
        amplify_app.add_branch(
            "dev-mi",
            # have to use prebuild to cd to the frontend folder, cause we can use repo name only for the above field
            build_spec=BuildSpec.from_object_to_yaml({
                "version": "1.0",
                "frontend": {
                    "phases": {
                        "preBuild": {
                            "commands": [
                                "cd ratemycourses-frontend",  # Navigate to subdirectory
                                "npm install"  # Install dependencies
                            ]
                        },
                        "build": {
                            "commands": [
                                "npm run build"  # Build the frontend
                            ]
                        }
                    },
                    "artifacts": {
                        "baseDirectory": "ratemycourses-frontend/build",  # Specify output folder
                        "files": [
                            "**/*"
                        ]
                    },
                    "cache": {
                        "paths": [
                            "node_modules/**/*"
                        ]
                    }
                }
            })
        )

# Initialize the CDK application
app = CdkApp()
AmplifyFrontendStack(app, "AmplifyFrontendStack")
app.synth()
