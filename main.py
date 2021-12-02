import click

from common.day_factory import DayFactory, UnimplementedDayException


@click.group()
def cli():
    pass


@cli.command('day', short_help='Print AOC 2021 answer')
@click.argument('day_index', nargs=1, type=click.INT)
@click.option('--example', is_flag=True)
def day(day_index, example):
    try:
        day_logic = DayFactory.get(day_index, example)
        print(f"Day 1 Part 1: {day_logic.part1()}")
        print(f"Day 1 Part 2: {day_logic.part2()}")
    except UnimplementedDayException as e:
        raise click.ClickException(str(e))


if __name__ == '__main__':
    cli()
