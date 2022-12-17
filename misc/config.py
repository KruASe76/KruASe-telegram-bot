from dataclasses import dataclass
from os import path
import pickle
import yaml

from misc.constants import config_path, participants_path


@dataclass
class Config:
    users: set[int]
    santa_participants: dict[int, str]
    santa_map: dict[int, int]


if path.exists(config_path):
    with open(config_path, "rb") as config_file:
        conf: Config = pickle.load(config_file)
else:
    with open(participants_path, "r", encoding="utf-8") as participants_file:
        conf = Config(
            users=set(),
            santa_participants=yaml.load(participants_file, yaml.FullLoader),
            santa_map={}
        )


def save_config():
    with open(config_path, "wb") as config_file:
        pickle.dump(conf, config_file)
