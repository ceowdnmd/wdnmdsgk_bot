#Every thing written by ceo@wdnmd
import telegram
import requests
from telegram.ext import CommandHandler, Updater

# 在此处填写您的API令牌
TOKEN = '你的令牌'

# 创建一个updater对象
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# 定义处理命令的函数
def qq(update, context):
    # 获取用户发送的参数
    parameter = context.args[0]
    # 调用API获取结果
    url = 'https://zy.xywlapi.cc/qqapi?qq=' + parameter
    result = requests.get(url).text
    # 将结果发送给用户
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
    context.bot.send_message(chat_id=update.effective_chat.id, text="欢迎使用此bot，此bot有如下命令/qq，/qqphone，/qqlol，/lolname，/qqlm，/wb，/wbphone")

# 添加命令处理函数
dispatcher.add_handler(CommandHandler('qq', qq))
dispatcher.add_handler(CommandHandler('qqphone', qqphone))
dispatcher.add_handler(CommandHandler('qqlol', qqlol))
dispatcher.add_handler(CommandHandler('lolname', lolname))
dispatcher.add_handler(CommandHandler('qqlm', qqlm))
dispatcher.add_handler(CommandHandler('wb', wb))
dispatcher.add_handler(CommandHandler('wbphone', wbphone))
dispatcher.add_handler(CommandHandler('start', start))

# 启动机器人
updater.start_polling()

