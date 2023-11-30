#!/usr/bin/python3
"""This script calls the API to retrieve the data and dumps into a file."""
import datetime as dt

from logger import logger
from utils import dump_data_from_api

# Format the name of the output file
FMT = "%Y-%m-%d-%H-%M"
FOLDER_PATH = "./history"

args = [
    (
        "retrieve station status",
        "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel@parisdata/records?limit=-1",
        lambda time: f'{FOLDER_PATH}/station_status__{time.strftime(FMT)}.json'
        ),
    (
        "retrieve station information",
        "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json",
        lambda time: f'{FOLDER_PATH}/station_information__{time.strftime(FMT)}.json',
        ),
]


if __name__ == "__main__":
    logger.info("------")
    time = dt.datetime.now()
    for message, url, get_output in args:
        logger.info(message)
        output_path = get_output(time)
        dump_data_from_api(url, output_path)
    logger.info("------")
