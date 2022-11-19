import datetime
from collections import Counter

from dotenv import load_dotenv
from pyrogram.types import Reaction, Message

from .client import Client

load_dotenv()


def weigh_counter_values(counter1: Counter, counter2: Counter) -> dict:
    assert len(counter1) == len(counter2), Exception(
        f"Non-identical datasets ({len(counter1)} != {len(counter2)}"
    )
    assert set(counter1.keys()) == set(counter2.keys()), Exception(
        "Non-identical datasets"
    )
    fin = dict()
    for name in list(counter1.keys()):
        fin[name] = float(f"{counter1[name] / counter2[name] * 100:5f}")
    return fin


def register_text_message_reaction(
    message: Message, reaction_counter: Counter, search_emojis: list
) -> Counter:
    _ = message.date.date()
    if datetime.datetime(_.year, _.month, _.day) < datetime.datetime(2021, 12, 30):
        return reaction_counter
    if not all(
        [
            message.reactions,
            message.forward_date is None,
            message.media is None,
            message.from_user,
        ]
    ):
        return reaction_counter
    reactions_obj, date = message.reactions, message.date.date()
    target_reactions: list[Reaction] = [
        x for x in reactions_obj.reactions if x.emoji in search_emojis
    ]
    # logger.info(f"{message.text or message.reply=}")
    if target_reactions is []:
        return reaction_counter
    print(
        f"Scrolling messages [date, message]: {message.date.date()} {message.text or message.reply}",
        end="\r",
    )
    for target_reaction in target_reactions:
        # logger.info(f"{target_reaction=}")
        for ii in range(target_reaction.count):
            reaction_counter.update([message.from_user.username])
    return reaction_counter


def add_msg_to_user_counter(message: Message, message_counter: Counter):
    if all([message.forward_date is None, message.media is None, message.from_user]):
        message_counter.update([message.from_user.username])
    return message_counter


async def measure_top_reactions(
    client: Client, chat_name: str, search_emojis=None
) -> dict:  # "Чат всіх випускників УАЛ"
    if search_emojis is None:
        search_emojis = ["😁", "🤣"]
    reaction_counter, message_counter = Counter(), Counter()
    async with client:
        chat_id = await client.chat_id_by_name(chat_name)
        async for message in client.chat_history_agen(
            chat_id=chat_id, datetime_until=datetime.datetime(2021, 12, 30)
        ):
            reaction_counter: Counter = register_text_message_reaction(
                message, reaction_counter, search_emojis
            )
            print(f"Reaction Counter: {reaction_counter}", end="\r")
            message_counter = add_msg_to_user_counter(message, message_counter)

        print(f"Message Counter: {message_counter}")
        react_list = list(reaction_counter.keys())
        for x in list(message_counter.keys()):
            if x not in react_list:  # Don't include people without a tag
                del message_counter[x]
            if x is None or message_counter[x] < 40:
                del message_counter[x]
                del reaction_counter[x]
        wcv = weigh_counter_values(reaction_counter, message_counter)
        print(f"Weighed Counter values: {wcv}")
        return wcv
        # plot_bars_from_dict(weighed_counter)
        # plot_normal_distribution(list(weighed_counter.values()))
