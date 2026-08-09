import logging

logger = logging.getLogger("assistant")

logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

logger.addHandler(handler)

logger.propagate = False
