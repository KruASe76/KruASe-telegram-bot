from os import path
import pickle
from dataclasses import dataclass

from constants import config_path, names_path


@dataclass
class Config:
    santa_participants: list[str]
    santa_used_ids: list[int]


if path.exists(config_path):
    with open(config_path, "rb") as config_file:
        config = pickle.load(config_file)
else:
    with open(names_path, "r", encoding="utf-8") as names_file:
        config = Config(
            santa_participants=list(filter(lambda s: s, names_file.read().split("\n"))),
            santa_used_ids=[]
        )


def save_config():
    with open(config_path, "wb") as config_file:
        pickle.dump(config, config_file)
