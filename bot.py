#!/usr/bin/python3
"""Telegram bot for Hack Day: Checker challenge Holberton project"""

import os
import requests
from telegram.ext import Updater, CommandHandler, ConversationHandler, \
                         MessageHandler, Filters


INPUT_TEXT = 0


def start(update, context):
    """start command"""
    update.message.reply_text('Hey, holbie! So stressful, huh? 😀\nDon\'t worry. Here I am to help you retrieve useful information from the Holberton School Checker API.\n\nAvailable commands at the moment:\n\n/project - retrieves information about any project: name, tasks, GitHub directory and GitHub repository')


def project(update, context):
    """project command"""
    update.message.reply_text('Please, tell me a project\'s ID number.\nYou can find any ID in the Holberton intranet "My projects" section.')
    return INPUT_TEXT


def input_text(update, context):
    """function to take text given by the user and send feedback"""
    text = update.message.text
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

    url = 'https://intranet.hbtn.io/users/auth_token.json'
    parameters = {"api_key": os.environ['HBTNAPIKEY'],
                  "email": os.environ['HBTNEMAIL'],
                  "password": os.environ['HBTNPASSWORD'],
                  "scope": "checker"}
    r = requests.post(url, params=parameters,
                      allow_redirects=False,
                      headers=header).json()
    token = r.get('auth_token')
    url2 = 'https://intranet.hbtn.io/projects/{}.json?auth_token={}'
    r2 = requests.get(url2.format(text, token),
                      allow_redirects=False,
                      headers=header)
    if r2.status_code != 200:
        chat = update.message.chat
        if text == "end" or text == "End" or text == "END" or text == "EnD" \
           or text == "eND" or text == "ENd" or text == "eNd" or text == "enD":
            chat.send_message('See you soon, holbie')
            return ConversationHandler.END
        else:
            chat.send_message('No project found. Please, enter a correct ID or tell me "end" to end conversation.')
    else:
        dic = r2.json()
        name = dic.get('name')
        chat = update.message.chat
        chat.send_message('Project\'s name: {}'.format(name))
        tasks = dic.get('tasks')
        chat.send_message('Number of tasks (mandatory + advanced): {}'.format(len(tasks)))
        tasktitle = []
        tasknumber = 0
        for item in tasks:
            tasktitle = item.get('title')
            chat.send_message('Task {}- {}'.format(tasknumber, tasktitle))
            tasknumber = tasknumber + 1
        if (item.get('github_dir') != ""):
            chat.send_message('GitHub directory: {}'.
                              format(item.get('github_dir')))
        else:
            chat.send_message('GitHub directory: No directory')
        if (item.get('github_repo') != ""):
            chat.send_message('GitHub repository: {}'.
                              format(item.get('github_repo')))
        else:
            chat.send_message('GitHub repository: No repository')
        return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(token=os.environ['TGTOKEN'],
                      use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('project', project)],
        states={INPUT_TEXT: [MessageHandler(Filters.text, input_text)]},
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
