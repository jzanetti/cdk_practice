from aws_cdk import Stack, aws_lambda
from constructs import Construct

class HelloWorldStack(Stack):
    """Hello world CDK example

    Args:
        Stack (_type_): _description_
    """
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # The code that defines your stack goes here
        _ = aws_lambda.Function(
            self, "HelloHandler",
            runtime = aws_lambda.Runtime.PYTHON_3_7,
            code = aws_lambda.AssetCode("lambda"),
            handler="hello.handler"
        )
        