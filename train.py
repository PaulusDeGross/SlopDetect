import yaml
import logging
from data_loader import DataLoader

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def load_config(config_path):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def main():
    config_path = "config.yml"
    try:
        config = load_config(config_path)
        logger.info(f"Configuration loaded from {config_path}")
    except FileNotFoundError:
        logger.error(f"Config file not found at {config_path}")
        return

    loader = DataLoader()

    loader.run_custom_preparation(config)


if __name__ == "__main__":
    main()
