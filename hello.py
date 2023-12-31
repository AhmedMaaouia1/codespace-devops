#!/usr/bin/env python
import click
import glob


@click.command()
@click.option(
    "--path",
    prompt="Path to search for csv files",
    help="This is the path to search for files: /tmp",
)
@click.option(
    "--ftype", prompt="Pass in the type of file", help="Pass in the file type: i.e csv"
)
def search(path, ftype):
    """This is a tool that search for patterns like *.csv"""
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(click.style("Found Matches:", fg="red"))
    for result in results:
        click.echo(click.style(f"{result}", bg="yellow", fg="white"))


if __name__ == "__main__":
    path_value = click.prompt("Path to search for csv files", type=str)
    ftype_value = click.prompt("Pass in the type of file", type=str)
    search(path=path_value, ftype=ftype_value)
