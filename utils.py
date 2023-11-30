#!/usr/bin/python3
"""This script calls the API to retrieve the data and dumps into a file."""
import json
import requests

from logger import logger


def dump_data_from_api(url, output_path):
    """
    Dump API Response into a json file
    """
    try:
        response = requests.get(url);
        status_code = response.status_code;
        status_msg = 'Successful' if status_code == 200 else f'Unsuccessful {status_code}';
        logger.info(f"request status: {status_msg}")
        if status_code == 200:
            data = response.json();
            with open(output_path, 'w') as output:
                json.dump(data, output)
            logger.info("Successful dumping")
    except Exception as e:
        logger.error('Unexpected failure', exc_info=e)