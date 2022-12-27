import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def basic_add(a, b):
    result = a + b
    return result

def try_add(a, b):
    try:
        result = a + b
    except TypeError as e:
        logger.error(str(e))
    return result

def add(a, b):
    try:
        result = a + b
    except TypeError:
        logger.exception("TypeError occurred")
    else:
        return result

