from argparse import ArgumentParser, Namespace


class ArgParser:
    def __init__(self):
        # Create Parser
        self.parser: ArgumentParser = ArgumentParser()

        # Build Specific Types
        self.parser.add_argument("--initialize", action="store_true", help="Build Infra Initialize")

        # Save Values
        self.name: Namespace = self.parser.parse_args()

