# Simpl Authenticator

WAMP Authenticator Component for SIMPL

## Installation

    $ pip install git+ssh://git@learninglab.githost.io:lldev-team/simpl-authenticator.git@master#egg=authenticator

## Setup environment

    $ mkvirtualenv simpl-authenticator
    $ pip install -e .

## Development versioning

Install `bumpversion`:

    $ pip install bumpversion

Then, to release a new version, increment the version number with:

    $ bumpversion patch

Then push to the repo:

    $ git push && git push --tags
