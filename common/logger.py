import logging


def configure_logger(debug: bool) -> None:
    logging.basicConfig(
        format='[%(levelname)s - %(asctime)s] %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG if debug else logging.INFO)
