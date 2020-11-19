import click
from Yaml2ProbaTree.yaml2probatree import Yaml2ProbaTree

@click.command()
@click.option('-d', '--debug', is_flag=True)
@click.argument('input_yaml', type=click.Path(), required=False)
def cli(input_yaml, debug):
    yaml2probatree = Yaml2ProbaTree(debug)
    print(yaml2probatree.yaml2tikz(input_yaml_file=input_yaml))
