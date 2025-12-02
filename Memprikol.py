from .. import loader

# meta developer: @Itachi_Uchiha_sss

@loader.tds
class Memprikol(loader.Module):
    """Голосовые сообщения от Mempack"""

    strings = {"name": " Memprikol"}

    async def молчатьcmd(self, message):
        """| Молчать нахуй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/64",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ахтcmd(self, message):
        """| Ахтунг Ахтунг"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/65",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def молчать2cmd(self, message):
        """| Молчать 2"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/66",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def изиcmd(self, message):
        """| Изи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/68",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def какcmd(self, message):
        """| Как?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/69",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def непонcmd(self, message):
        """| Непонял"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/70",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def чтоcmd(self, message):
        """| Что блять?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/71",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нахcmd(self, message):
        """| Нахуй я сюда пришёл?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/72",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def ненадаcmd(self, message):
        """| Не лезь"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/73",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нихуясебеcmd(self, message):
        """| Нихуя себе"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/74",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def никитаcmd(self, message):
        """| Привет я Никита"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/75",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def болгаркаcmd(self, message):
        """| Распили болгаркой"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/76",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def завалисьcmd(self, message):
        """| Закрой пиздак"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/77",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def банcmd(self, message):
        """| Ну это БАН"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/78",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def смехcmd(self, message):
        """| Смех ПАПАНИ"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/79",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def побрейcmd(self, message):
        """| Побрей очко"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/80",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def какатьcmd(self, message):
        """| Хочу КАКАТЬ"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/81",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def заебалcmd(self, message):
        """| Заебал палить"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/82",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def сукаcmd(self, message):
        """| Сука убью нахуй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/83",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def попускcmd(self, message):
        """| Ну ты попуск ваще"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/84",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def ярикcmd(self, message):
        """| Ярик пиздец"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/85",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def бляcmd(self, message):
        """| БЛЯТЬ"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/86",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def словянcmd(self, message):
        """| Словянский сэкс шоп"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/87",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def снюсcmd(self, message):
        """| Покупаю снюс"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/88",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def уничтожуcmd(self, message):
        """| Я вас уничтожу"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/89",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def каждыйcmd(self, message):
        """| Каждый раз"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/90",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def владcmd(self, message):
        """| Привет я Влад"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/91",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нахуйcmd(self, message):
        """| Ваши претензии поняты"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/92",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def дибилcmd(self, message):
        """| Дибил"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/93",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def очкоcmd(self, message):
        """| Ты засадишь мне в очко"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/94",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def полуcmd(self, message):
        """| Полу рак полу хуй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/95",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def банька2cmd(self, message):
        """| Банька парилка"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/96",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def дрочилаcmd(self, message):
        """| Дрочила"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/97",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def хентайcmd(self, message):
        """| Хентай хуйня"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/98",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def хуяришьcmd(self, message):
        """| Куда хуяришь блять?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/99",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ландышиcmd(self, message):
        """| Ландыши первые"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/100",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ландыши2cmd(self, message):
        """| Ландыши вторые"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/101",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def верблюдcmd(self, message):
        """| На горе стоит верблюд"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/102",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def фрифаерcmd(self, message):
        """| Играю во фрифаер"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/103",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def обэмеcmd(self, message):
        """| Обэме"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/104",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def деcmd(self, message):
        """| Чичинде"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/105",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пидорасcmd(self, message):
        """| Система пидораса"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/106",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def открывайcmd(self, message):
        """| Открывай ублюдок"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/107",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def сука2cmd(self, message):
        """| Сука"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/108",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def матьcmd(self, message):
        """| Твоя мать"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/109",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def порcmd(self, message):
        """| Очень красивый звук"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/110",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def коньcmd(self, message):
        """| Украли коня(укр ver)"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/111",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def япиздатcmd(self, message):
        """| Я пиздатый"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/112",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def гитлерcmd(self, message):
        """| Я гитлер"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/113",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def салоcmd(self, message):
        """| Отдай САЛО"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/114",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def пидорас2cmd(self, message):
        """| Пидорас 2"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/115",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пидорас3cmd(self, message):
        """| Пидорас 3"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/116",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def собакcmd(self, message):
        """| Я ебу собак"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/117",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пробитиеcmd(self, message):
        """| Есть пробитие"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/118",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def базаcmd(self, message):
        """| 415-база"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/119",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def смcmd(self, message):
        """| Заюзаете узнаете"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/120",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def рофлcmd(self, message):
        """| Господин эта рофл?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/121",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def алахcmd(self, message):
        """| Алах над нами"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/122",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def слухайcmd(self, message):
        """| Слушай а ловко ты придумал(укр ver)"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/123",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def мать2cmd(self, message):
        """| Хорошая женщина"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/124",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def арабcmd(self, message):
        """| Что-то на арабском"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/125",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def выcmd(self, message):
        """| Вы меня оск"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/126",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def законcmd(self, message):
        """| Вы нарушаете закон"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/127",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def шиcmd(self, message):
        """| Сумашедший"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/128",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def словаcmd(self, message):
        """| Свобода слова"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/129",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def молчать3cmd(self, message):
        """| Молчать 3"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/130",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
    
    async def дойчcmd(self, message):
        """| Немецкий знаете?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/131",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def оплатиcmd(self, message):
        """| Сафонов оплатить"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gachi_mych/132",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return