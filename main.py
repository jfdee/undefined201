from logic.getters import get_bot_connect
from logic.consts import (NEXT_COMMAND_BY_PREV_COMMAND, BOT_RESPONSE_BY_NEXT_COMMAND, END_COMMAND)


bot = get_bot_connect()


class Chat:
    objects = []

    def __init__(self, chat_id: int, ):
        self.chat_id = chat_id
        self.issue_name = ''
        self.issue_type = ''
        self.issue_priority = ''
        self.next_command = 'issue_name'
        Chat.objects.append(self)

    def set_attr(self, name, value):
        setattr(self, name, value)

    @classmethod
    def get_by_chat_id(cls, chat_id):
        for instance in cls.objects:
            if instance.chat_id == chat_id:
                return instance


@bot.message_handler(commands=['create'])
def create(message):
    Chat(chat_id=message.chat.id)
    bot.send_message(message.chat.id, 'Наименование')
    return


@bot.message_handler(commands=['help'])
def help_command(message):
    response_message = f'/create - создать\n' \
                       f'/help - справка'
    bot.send_message(message.chat.id, response_message)
    return


@bot.message_handler(content_types=['text'])
def text(message):
    chat_id = message.chat.id
    instance = Chat.get_by_chat_id(chat_id)
    if not instance:
        return
    instance.set_attr(name=instance.next_command, value=message.text)
    instance.next_command = NEXT_COMMAND_BY_PREV_COMMAND[instance.next_command]
    bot.send_message(chat_id, BOT_RESPONSE_BY_NEXT_COMMAND[instance.next_command])


if __name__ == '__main__':
    bot.infinity_polling()
