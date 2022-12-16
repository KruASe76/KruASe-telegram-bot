from dataclasses import dataclass
from os import path
from typing import Dict
import pickle
import yaml

from misc.constants import config_path, participants_path


@dataclass
class Config:
    santa_participants: Dict[int, str]
    santa_map: Dict[int, str]


if path.exists(config_path):
    with open(config_path, "rb") as config_file:
        config = pickle.load(config_file)
else:
    with open(participants_path, "r", encoding="utf-8") as participants_file:
        config = Config(
            santa_participants=yaml.load(participants_file, yaml.FullLoader),
            santa_map={}
        )


def save_config():
    with open(config_path, "wb") as config_file:
        pickle.dump(config, config_file)
