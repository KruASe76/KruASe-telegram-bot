# KruASe-telegram-bot

My first Telegram bot


## Secret Santa

Mechanism that provides random draw for Secret Santa event
- Participant names and their ids are specified in the [`participants.yml`](participants.yml) file
- Protection against multiple call by a single user
- Protection against calls from not participants


## Used libraries

- [aiogram (v3)](https://pypi.org/project/aiogram/) as Telegram Bot API
- [PyYAML](https://pypi.org/project/PyYAML/) to process YAML configuration
