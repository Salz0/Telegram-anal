from pyrogram import Client as PyroClient
import datetime
from collections import Counter
from numpy import inf
from pyrogram.types import User, Message


class Client(PyroClient):
    client = None

    def __init__(
        self,
        name: str,
        api_id: int | str = None,
        api_hash: str = None,
        ipv6: bool = False,
        proxy: dict = None,
        test_mode: bool = False,
        bot_token: str = None,
        session_string: str = None,
        in_memory: bool = None,
        phone_number: str = None,
        phone_code: str = None,
        password: str = None,
        plugins: dict = None,
        no_updates: bool = None,
        takeout: bool = None,
        hide_password: bool = True,
    ):
        super().__init__(
            name=name,
            api_id=api_id,
            api_hash=api_hash,
            ipv6=ipv6,
            proxy=proxy,
            test_mode=test_mode,
            bot_token=bot_token,
            session_string=session_string,
            in_memory=in_memory,
            phone_number=phone_number,
            phone_code=phone_code,
            password=password,
            plugins=plugins,
            no_updates=no_updates,
            takeout=takeout,
            hide_password=hide_password,
        )

    async def chat_id_by_name(self, chat_name) -> int:
        async for dialog in self.get_dialogs():
            if (
                dialog.chat.title or f"{dialog.chat.first_name} {dialog.chat.last_name}"
            ) == chat_name:
                return dialog.chat.id

    async def chat_history_agen(self, chat_id, n=inf):
        """Creates an async generator of messages, that may contain a reactions"""
        async for message in self.get_chat_history(chat_id=chat_id, limit=n):
            yield message
            now = message.date.date()
            if datetime.datetime(now.year, now.month, now.day) < datetime.datetime(
                2021, 12, 30
            ):
                break

    async def get_message_reactions(self, chat_name, n=inf) -> Message:
        chat_id: int = await self.chat_id_by_name(chat_name)
        counter = 0
        async for message in self.chat_history_agen(chat_id, n=n):
            if all(
                [
                    message.reactions,
                    message.forward_date is None,
                    message.media is None,
                    message.from_user,
                ]
            ):
                yield message
                counter += 1

    async def count_user_text_messages(
        self, chat_name: str, username_list: list[User], n=inf
    ) -> Counter:
        chat_id: int = await self.chat_id_by_name(chat_name)
        message_counter = Counter()
        async for message in self.chat_history_agen(chat_id, n=n):
            if all(
                [
                    message.forward_date is None,
                    message.media is None,
                    message.from_user,
                    message.from_user.username in username_list,
                ]
            ):
                position: int = username_list.index(message.from_user.username)
                message_counter.update([username_list[position]])
            print(f"Message Counter: {message_counter}", end="\r")
        return message_counter
