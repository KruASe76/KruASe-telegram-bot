# KruASe-telegram-bot

My first Telegram bot


## Secret Santa

Mechanism that provides random draw for Secret Santa event
- Participant names and their ids are specified in the [`participants.yml`](participants.yml) file
- Protection against multiple call by a single user
- Protection against calls from not participants


## Used libraries

- [aiogram (v3.0.0b6)](https://pypi.org/project/aiogram/3.0.0b6/) as Telegram Bot API
- [PyYAML](https://pypi.org/project/PyYAML/) to process YAML configuration
