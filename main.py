import sys
import time

from loguru import logger

from toonalysis.database import Toons
from toonalysis.scraper import Scraper


def log_formatter(record) -> str:
    match record['level'].name:
        case 'ERROR':
            if record['exception']:
                return '<white>[{time:YYYY-MM-DD HH:mm:ss}]</> <red>[{module}.{function}.{line} - {level: <8}]</> {message}\n{exception}\n'
            else:
                return '<white>[{time:YYYY-MM-DD HH:mm:ss}]</> <red>[{module}.{function}.{line} - {level: <8}]</> {message}\n'
        case 'CRITICAL':
            if record['exception']:
                return '<white>[{time:YYYY-MM-DD HH:mm:ss}]</> <red>[{module}.{function}.{line} - {level: <8}]</> {message}\n{exception}\n'
            else:
                return '<white>[{time}]</> <red>[{module}.{function}.{line} - {level: <8}]</> {message}\n'
        case 'TRACE':
            return '<white>[{time:YYYY-MM-DD HH:mm:ss}] [{module: <5}]</> <blue>{level: <8}</> {message}\n'
        case _:
            return '<white>[{time:YYYY-MM-DD HH:mm:ss}]</> <green>{level: <8}</> {message}\n'


@logger.catch
def main():
    with Scraper() as scraper, Toons() as toons:
        while True:
            for toon in scraper.get_toons():
                toons.add_or_update(toon)
                logger.info('Toon found: {}', toon.to_document())
            
            time.sleep(10)


if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stderr, level='TRACE', format=log_formatter)

    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as exc:
        logger.opt(exception=exc).critical("error in main")
