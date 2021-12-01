import click

from common.day_factory import DayFactory, UnimplementedDayException


@click.group()
def cli():
    pass


@cli.command('day', short_help='Print AOC 2021 answer')
@click.argument('day_index', nargs=1, type=click.INT)
def day(day_index):
    try:
        print(DayFactory.get(day_index).get_answer())
    except UnimplementedDayException as e:
        raise click.ClickException(str(e))


if __name__ == '__main__':
    cli()
