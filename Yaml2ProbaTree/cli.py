import click
from Yaml2ProbaTree.yaml2probatree import yaml2tikz

@click.command()
@click.argument('input_yaml', type=click.Path())
def cli(input_yaml):
    print(yaml2tikz(input_yaml))
