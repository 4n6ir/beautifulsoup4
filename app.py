#!/usr/bin/env python3
import os

import aws_cdk as cdk

from beautifulsoup4.beautifulsoup4_stack import Beautifulsoup4Stack

app = cdk.App()

Beautifulsoup4Stack(
    app, 'Beautifulsoup4StackUSE1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

Beautifulsoup4Stack(
    app, 'Beautifulsoup4StackUSE2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

Beautifulsoup4Stack(
    app, 'Beautifulsoup4StackUSW2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('Alias','Extensions')
cdk.Tags.of(app).add('GitHub','https://github.com/4n6ir/beautifulsoup4.git')

app.synth()