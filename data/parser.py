from dataclasses import dataclass
from argparse_dataclass import ArgumentParser
@dataclass
class Options:
    verbose: bool
    other_flag: bool
parser = ArgumentParser(Options)
print(parser.parse_args([]))
Options(verbose=False, other_flag=False)
print(parser.parse_args(["--verbose", "--other-flag"]))
Options(verbose=True, other_flag=True)