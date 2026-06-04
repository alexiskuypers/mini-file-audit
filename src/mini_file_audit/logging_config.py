import logging
from pathlib import Path


def configure_logging() -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=log_dir / "app.log",
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(filename)s:%(lineno)d | %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
    )


def main() -> None:
    configure_logging()
    logging.info("start audit")
    logger = logging.getLogger(__name__)

