from mylib.bot import scrape
import click


@click.command()
@click.option("--name", help="web page we want to scrape")
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", fg="white", bg="black"))


if __name__ == "__main__":
    cli()
