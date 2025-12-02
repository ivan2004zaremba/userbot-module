from .. import loader

# meta developer: @Itachi_Uchiha_sss

@loader.tds
class Dota2pack(loader.Module):
    """Dota 2 pack"""

    strings = {"name": "Dota2pack"}

    async def наколениcmd(self, message):
        """| На колени на колени(Василиса)"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/315",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def гунарcmd(self, message):
        """| Гунар пошёл ты нахуй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/316",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def отецcmd(self, message):
        """| Отец дай мне немного своего семени"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/324",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def MonsterKillcmd(self, message):
        """| Монстр килл"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/318",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def Unstoppablecmd(self, message):
        """| Unstoppable"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/319",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нахуй5cmd(self, message):
        """| Нахуй от Пуджа"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/320",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def некстлвлcmd(self, message):
        """| Зе некст лвл плей"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/321",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return