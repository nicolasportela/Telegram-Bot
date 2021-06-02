#!/usr/bin/python3
"""Telegram bot for Hack Day: Checker challenge Holberton project"""

import os
import requests
from telegram.ext import Updater, CommandHandler, ConversationHandler, \
                         MessageHandler, Filters


INPUT_TEXT = 0
INPUT_TEXT2 = 1


def start(update, context):
    """start command"""
    update.message.reply_text('Hey, holbie! So stressful, huh? 😀\nDon\'t worry. Here I am to help you retrieve useful information from the Holberton School Checker API.\n\nEnter /help for more info about SuperHolbie and available commands at the moment.')


def helpcommand(update, context):
    """help command"""
    update.message.chat.send_message(disable_web_page_preview=1, parse_mode='HTML', text='<b>Usage and full description of available commands at the moment:</b>\n\n/start - Shows a welcome message with a quick summary about SuperHolbie.\n\n/end - Ends a conversation if there is one running. It stops SuperHolbie from listening and lets you enter a new command.\n\n/help - Shows extra info about SuperHolbie: demo, source code, documentation, contact and available commands at the moment.\n\n/project - Retrieves information about any Holberton School project: name, tasks, GitHub directory and GitHub repository. Additionally, it gives you the option to get extra info about any task: correction mode and GitHub file.\n\n<b>- Demo:</b>\nhttps://bit.ly/3wLJckb\n\n<b>- Source code and documentation:</b>\nhttps://bit.ly/3iePlBh\n\n<b>- Contact:</b>\nnicolasportelam@gmail.com')


def project(update, context):
    """project command"""
    update.message.chat.send_message(parse_mode='HTML', text='<b>Please, tell me a project\'s ID number.</b>\nYou can find any ID in the Holberton intranet "My projects" section.\n\nEnter /end to end conversation.')
    return INPUT_TEXT


def input_text(update, context):
    """function to take text given by the user
    and send feedback about projects"""
    text = update.message.text
    chat = update.message.chat
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
        chat.send_message(parse_mode='HTML', text='<b>No project found.</b> Please, enter a correct ID or /end to end conversation.')
    else:
        dic = r2.json()
        projname = dic.get('name')
        chat.send_message(parse_mode='HTML',
                          text='<b>Project\'s name:</b>\n{}'.format(projname))
        tasks = dic.get('tasks')
        chat.send_message(parse_mode='HTML', text='<b>Number of tasks (mandatory + advanced):</b> {}'.format(len(tasks)))
        tasknumber = 0
        for item in tasks:
            tasktitle = item.get('title')
            taskid = item.get('id')
            chat.send_message(parse_mode='HTML',
                              text='<b>- Task {}:</b> {}\n(ID number: {})'
                              .format(tasknumber, tasktitle, taskid))
            tasknumber = tasknumber + 1
        projdir = item.get('github_dir')
        if projdir != "":
            chat.send_message(parse_mode='HTML',
                              text='<b>GitHub directory:</b>\n<code>{}</code>'
                              .format(projdir))
        else:
            chat.send_message(parse_mode='HTML',
                              text='<b>GitHub directory:</b> No directory')
        projrepo = item.get('github_repo')
        if projrepo != "":
            chat.send_message(parse_mode='HTML',
                              text='<b>GitHub repository:</b>\n<code>{}</code>'
                              .format(projrepo))
        else:
            chat.send_message(parse_mode='HTML',
                              text='<b>GitHub repository:</b> No repository')
        chat.send_message(parse_mode='HTML', text='<b>Would you like to get extra info about some of those tasks?</b>\nIf so, tell me a task\'s ID number (available above); otherwise, enter /end to end conversation.')
        return INPUT_TEXT2


def input_text2(update, context):
    """function to take text given by the user and send feedback about tasks"""
    text2 = update.message.text
    chat2 = update.message.chat
    header2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

    url = 'https://intranet.hbtn.io/users/auth_token.json'
    parameters = {"api_key": os.environ['HBTNAPIKEY'],
                  "email": os.environ['HBTNEMAIL'],
                  "password": os.environ['HBTNPASSWORD'],
                  "scope": "checker"}
    r = requests.post(url, params=parameters,
                      allow_redirects=False,
                      headers=header2).json()
    token = r.get('auth_token')

    url3 = 'https://intranet.hbtn.io/tasks/{}.json?auth_token={}'
    r3 = requests.get(url3.format(text2, token),
                      allow_redirects=False,
                      headers=header2)
    if r3.status_code != 200:
        chat2.send_message(parse_mode='HTML', text='<b>No task found.</b> Please, enter a correct ID (available above) or /end to end conversation.')
    else:
        dic2 = r3.json()
        tasktitle2 = dic2.get('title')
        chat2.send_message(parse_mode='HTML',
                           text='<b>Task\'s name:</b> {}'
                           .format(tasktitle2))
        taskchecker = dic2.get('checker_available')
        if taskchecker is True:
            chat2.send_message(parse_mode='HTML',
                               text='<b>Correction mode:</b> Checker')
        else:
            chat2.send_message(parse_mode='HTML',
                               text='<b>Correction mode:</b> manual review')
        url4 = 'https://intranet.hbtn.io/projects/{}.json?auth_token={}'
        projid = dic2.get('project_id')
        r4 = requests.get(url4.format(projid, token),
                          allow_redirects=False,
                          headers=header2).json()
        projname2 = r4.get('name')
        chat2.send_message(parse_mode='HTML',
                           text='<b>Project\'s name:</b>\n{}'
                           .format(projname2))
        taskfile = dic2.get('github_file')
        if taskfile != "":
            chat2.send_message(parse_mode='HTML',
                               text='<b>GitHub file/s:</b>\n<code>{}</code>'
                               .format(taskfile))
        else:
            chat2.send_message(parse_mode='HTML',
                               text='<b>GitHub file/s:</b> No file/s')
        taskdir = dic2.get('github_dir')
        if taskdir != "":
            chat2.send_message(parse_mode='HTML',
                               text='<b>GitHub directory:</b>\n<code>{}</code>'
                               .format(taskdir))
        else:
            chat2.send_message(parse_mode='HTML',
                               text='<b>GitHub directory:</b> No directory')
        taskrepo = dic2.get('github_repo')
        if taskrepo != "":
            chat2.send_message(parse_mode='HTML', text='<b>GitHub repository:</b>\n<code>{}</code>'.format(taskrepo))
        else:
            chat2.send_message(parse_mode='HTML',
                               text='<b>GitHub repository:</b> No repository')
        chat2.send_message(parse_mode='HTML', text='<b>Any other task?</b>\nIf so, tell me its ID number (available above); otherwise, enter /end to end conversation.')


def end(update, context):
    """end command"""
    update.message.reply_text('See you soon, holbie 💪')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(token=os.environ['TGTOKEN'],
                      use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('help', helpcommand))

    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('project', project)],
        states={INPUT_TEXT: [MessageHandler(~Filters.command, input_text)],
                INPUT_TEXT2: [MessageHandler(~Filters.command, input_text2)]},
        fallbacks=[CommandHandler('end', end)],
    ))

    updater.start_polling()
    updater.idle()
