# Telegram analysis ✨ 

Telegram analysis is a python package that helps you have fun and make sense of different chat data you have. 
Based on pyrogram, its mission is to help you have fun with Telegram and it's functions.
Whether it is about playing with your group chat dialogs or analysing the group dynamic of your business, personal chats or even your saved messages.

Be creative and build on top of ready solutions! 🧠

Current functionality (version 0.1.1):

✨🌠 `wordcloud_json()`Create fun wordclouds out of chats 

💬🗣 `who_breaks_silence_json()` Analyze who tends to break the silence in the chats and write first

🤍❤ `measure_top_reactions()` measure who's messages are most reacted to and choose specific reactions!


___
### Installation:
```
pip install telegram-anal
```

### 🛠 Setup:

This library uses Pyrogram for handling Telegram, so you will need to authenticate standardly by:
1. Create an app and copy your api_id and api_hash from https://my.telegram.org/

### Example:
```python
import asyncio
from telenal.client import Client
from telenal.reactions import measure_top_reactions
from telenal.teleplotter import plot_bars_from_dict


async def main():
    client = Client("my_account", "your_api_id", "your_api_hash")
    tops = await measure_top_reactions(
        client,
        chat_name="Family chat :)",
        search_emojis=["😁", "💪", "👍"],
    )
    plot_bars_from_dict(tops)  # <-- get a bar chart out of the box


if __name__ == "__main__":
    asyncio.run(main())

```

The library is newly born and needs creative and energetic support. Feel free to contribute!

Ideas for future functionality:

1. Analyze your activity based on sent chatting to identify your chatting patterns
2. Save messages deleted by someone that texted you and save the secret they wanted to hide
3. Measure user profiles to identify persons' most popular tones (NLP may be needed)
4. Predict when a user is prone to leave a community based on real cases (ML)

Remember to have fun! :)

This software is made purely for fun. Any illegal or amoral misuse of the software does not make the authors responsible for the consequences. 

Yours,
Vlad Bilyk
