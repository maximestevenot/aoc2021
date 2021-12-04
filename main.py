import logging

import click

from common.day_factory import DayFactory, UnimplementedDayException
from common.logger import configure_logger


@click.group()
def cli():
    pass


@cli.command('day', short_help='Print AOC 2021 answer')
@click.argument('day_index', nargs=1, type=click.INT)
@click.option('--example', is_flag=True)
@click.option('--debug', is_flag=True)
def day(day_index, example, debug):
    configure_logger(debug)
    logger = logging.getLogger()
    try:
        logger.debug(f"Get logic for day {day_index}")
        day_logic = DayFactory.get(day_index, example)
    except UnimplementedDayException as e:
        raise click.ClickException(str(e))

    logger.debug("Compute Part 1")
    click.echo(f"Day 1 Part 1: {click.style(day_logic.part1(), fg='blue', bold=True)}")
    logger.debug("Compute Part 2")
    click.echo(f"Day 1 Part 2: {click.style(day_logic.part2(), fg='blue', bold=True)}")


if __name__ == '__main__':
    cli()
