import asyncio
from telenal.client import Client
from telenal.reactions import measure_top_reactions
from telenal.teleplotter import plot_bars_from_dict


async def main():
    client = Client("my_account", "your_api_hash", "your_api_hash")
    tops = await measure_top_reactions(
        client,
        chat_name="Family chat :)",
        search_emojis=["😁", "💪", "👍"],
    )
    plot_bars_from_dict(tops)  # <-- get a bar chart out of the box


if __name__ == "__main__":
    asyncio.run(main())
