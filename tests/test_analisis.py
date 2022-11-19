import os
from collections import Counter

from telenal.analysis import who_breaks_silence_json, wordcloud_json


def test_who_breaks_silence_json():
    assert who_breaks_silence_json("D:/Telegram-anal/Real_life_jsons/yana.json") == Counter({'Яна': 25, 'Влад': 28})


def test_wordcloud_json():
    here = os.getcwd().split("Telegram-anal")[0].replace("\\", "/")

    wordcloud_ = wordcloud_json(f"{here}Telegram-anal/Real_life_jsons/sample_chat.json", language="english", plot=False)
    assert wordcloud_.words_['fund'] == 0.6559139784946236

    # TODO: write an error where an html chat is input
    # assert wordcloud_json("/Real_life_jsons/sample_chat.json", language="english", plot=False) ==
