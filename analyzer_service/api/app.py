import logging
from functools import partial


from aiohttp.web_app import Application
from configargparse import Namespace

from analyzer_service.utils.pg import setup_pg

# По умолчанию размер запроса к aiohttp ограничен 1 мегабайтом:
# https://docs.aiohttp.org/en/stable/web_reference.html#aiohttp.web.Application
# Размер запроса со 10 000 жителей и 2000 связей (с учетом максимальной длины
# строк и кодировки json с параметром ensure_ascii=True) может занимать
# ~63 мегабайт:
MEGABYTE = 1024 ** 2
MAX_REQUEST_SIZE = 70 * MEGABYTE

log = logging.getLogger(__name__)


def create_app(args: Namespace) -> Application:
    """
    Создает экземпляр приложения, готового к запуску.
    """
    app = Application(
        client_max_size=MAX_REQUEST_SIZE,

    )

    # Подключение на старте к postgres и отключение при остановке
    app.cleanup_ctx.append(partial(setup_pg, args=args))

    return app
