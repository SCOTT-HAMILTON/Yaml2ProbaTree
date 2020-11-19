import click
from Yaml2ProbaTree.yaml2probatree import yaml2tikz

@click.command()
@click.argument('input_yaml', type=click.Path(), required=False)
def cli(input_yaml):
    print(yaml2tikz(input_yaml_file=input_yaml))
