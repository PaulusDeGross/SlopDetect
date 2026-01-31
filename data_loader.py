import os
import subprocess
import logging
import sys


class DataLoader:
    logger = logging.getLogger(__name__)

    def __init__(self):
        pass

    def run_custom_preparation(self, config):
        """
        Checks config for custom data preparation scripts and runs them if needed

        :param config:
        :return:
        """
        prep_config = config.get("data", {}).get("custom_preparations")

        if not prep_config.get("enabled", False):
            return

        target_file = prep_config.get("skip_if_exists")
        if target_file and os.path.exists(target_file):
            self.logger.info(f"Data preparation skipped. Found existing file: {target_file}")
            return

        command = prep_config.get("command")
        if command:
            self.logger.info(f"Running custom data preparation: {command}")
            try:
                subprocess.run(command, shell=True, check=True)
                self.logger.info(f"Custom preparation finished successfully")
            except subprocess.CalledProcessError as e:
                self.logger.error(f"Data preparation script failed with error: {e}")
                sys.exit(1)  # Stop the pipeline if data prep fails
            except Exception as e:
                self.logger.error(f"Unexpected error executing command: {e}")
                sys.exit(1)
