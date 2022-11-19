# coding: utf8
import os

from telenal.analysis import wordcloud_json

here = os.getcwd().split("Telegram-anal")[0].replace("\\", "/")
wordcloud_json(
    f"{here}Telegram-anal/Real_life_jsons/sample_chat.json",
    language="english",
    plot=True,
    max_words=80
)
