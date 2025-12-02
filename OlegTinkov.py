from .. import loader

# meta developer: @Itachi_Uchiha_sss

@loader.tds
class OlegTinkov(loader.Module):
    """Голосовые сообщения от Олега Тинькова"""

    strings = {"name": " OlegTinkov"}

    async def мнепохуйcmd(self, message):
        """| Мне похуй я так чувствую"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/188",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def уменяcmd(self, message):
        """| У меня не так много друзей"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/190",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def прихирелcmd(self, message):
        """| Я реально прихирел"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/191",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def окэйcmd(self, message):
        """| Сомнительно ну окэй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/192",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def ошибсяcmd(self, message):
        """| Я ошибся, я могу один раз ошибится"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/193",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ерундаcmd(self, message):
        """| Натянутое на глобус такая ерунда"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/194",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def разницаcmd(self, message):
        """| Ну вот какая разница?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/195",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def неинтересноcmd(self, message):
        """| Мне это не интересно"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/196",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def преступленияcmd(self, message):
        """| Ты совершил преступления"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/197",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def грешникcmd(self, message):
        """| Я великий грешник"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/198",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def страдатьcmd(self, message):
        """| Ты должен страдать"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/199",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def крутоcmd(self, message):
        """| Круто да это ж круто"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/200",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def выродокcmd(self, message):
        """| Выродок говно ваш ССР"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/201",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def осознатьcmd(self, message):
        """| 48 часов чтобы осознать"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/202",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return