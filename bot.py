#Every thing written by ceo@wdnmd
import telegram
import requests
from telegram.ext import CommandHandler, Updater

# �ڴ˴���д����API����
TOKEN = '�������'

# ����һ��updater����
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# ���崦������ĺ���
def qq(update, context):
    # ��ȡ�û����͵Ĳ���
    parameter = context.args[0]
    # ����API��ȡ���
    url = 'https://zy.xywlapi.cc/qqapi?qq=' + parameter
    result = requests.get(url).text
    # ��������͸��û�
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def qqphone(update, context):
    parameter = context.args[0]
    url = 'https://zy.xywlapi.cc/qqphone?phone=' + parameter
    result = requests.get(url).text
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def qqlol(update, context):
    parameter = context.args[0]
    url = 'https://zy.xywlapi.cc/qqlol?qq=' + parameter
    result = requests.get(url).text
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def lolname(update, context):
    parameter = context.args[0]
    url = 'https://zy.xywlapi.cc/lolname?name=' + parameter
    result = requests.get(url).text
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def qqlm(update, context):
    parameter = context.args[0]
    url = 'https://zy.xywlapi.cc/qqlm?qq=' + parameter
    result = requests.get(url).text
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def wb(update, context):
    parameter = context.args[0]
    url = 'https://zy.xywlapi.cc/wbapi?id=' + parameter
    result = requests.get(url).text
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def wbphone(update, context):
    parameter = context.args[0]
    url = 'https://zy.xywlapi.cc/wbphone?phone=' + parameter
    result = requests.get(url).text
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="��ӭʹ�ô�bot����bot����������/qq��/qqphone��/qqlol��/lolname��/qqlm��/wb��/wbphone")

# ����������
dispatcher.add_handler(CommandHandler('qq', qq))
dispatcher.add_handler(CommandHandler('qqphone', qqphone))
dispatcher.add_handler(CommandHandler('qqlol', qqlol))
dispatcher.add_handler(CommandHandler('lolname', lolname))
dispatcher.add_handler(CommandHandler('qqlm', qqlm))
dispatcher.add_handler(CommandHandler('wb', wb))
dispatcher.add_handler(CommandHandler('wbphone', wbphone))
dispatcher.add_handler(CommandHandler('start', start))

# ����������
updater.start_polling()

