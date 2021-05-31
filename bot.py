#!/usr/bin/python3
"""Telegram bot for Hack Day: Checker challenge Holberton project"""

import os
import requests
from telegram.ext import Updater, CommandHandler, ConversationHandler, \
                         MessageHandler, Filters


INPUT_TEXT = 0
INPUT_TEXT2 = 0


def start(update, context):
    """start command"""
    update.message.reply_text('Hey, holbie! So stressful, huh? 😀\nDon\'t worry. Here I am to help you retrieve useful information from the Holberton School Checker API.\n\nAvailable commands at the moment:\n\n/project - retrieves information about any project: name, tasks, GitHub directory and GitHub repository. Optionally, it is possible to get extra information about any of that project tasks: correction mode and GitHub file.')


def project(update, context):
    """project command"""
    update.message.reply_text('Please, tell me a project\'s ID number.\nYou can find any ID in the Holberton intranet "My projects" section.')
    return INPUT_TEXT


def input_text(update, context):
    """function to take text given by the user and send feedback"""
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
        if text == "end" or text == "End" or text == "END" or text == "EnD" \
           or text == "eND" or text == "ENd" or text == "eNd" or text == "enD":
            chat.send_message('See you soon, holbie')
            return ConversationHandler.END
        else:
            chat.send_message('No project found. Please, enter a correct ID or tell me "end" to end conversation.')
    else:
        dic = r2.json()
        projname = dic.get('name')
        chat.send_message('Project\'s name: {}'.format(projname))
        tasks = dic.get('tasks')
        chat.send_message('Number of tasks (mandatory + advanced): {}'
                          .format(len(tasks)))
        tasknumber = 0
        for item in tasks:
            tasktitle = item.get('title')
            taskid = item.get('id')
            chat.send_message('Task {}- {}\n(ID number: {})'.
                              format(tasknumber, tasktitle, taskid))
            tasknumber = tasknumber + 1
        projdir = item.get('github_dir')
        if projdir != "":
            chat.send_message('GitHub directory: {}'.format(projdir))
        else:
            chat.send_message('GitHub directory: No directory')
        projrepo = item.get('github_repo')
        if projrepo != "":
            chat.send_message('GitHub repository: {}'.format(projrepo))
        else:
            chat.send_message('GitHub repository: No repository')
        chat.send_message('Would you like to get extra info about some of those tasks? If yes, tell me its ID number (available above); otherwise, tell me "end" to end conversation.')
        return INPUT_TEXT2


def input_text2(update, context):
    """function 2 to take text given by the user and send feedback"""
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

    if text2 == "end" or text2 == "End" or text2 == "END" or text2 == "EnD" \
       or text2 == "eND" or text2 == "ENd" or text2 == "eNd" or text2 == "enD":
        chat2.send_message('See you soon, holbie')
        return ConversationHandler.END
    else:
        url3 = 'https://intranet.hbtn.io/tasks/{}.json?auth_token={}'
        r3 = requests.get(url3.format(text2, token),
                          allow_redirects=False,
                          headers=header2)
        if r3.status_code != 200:
            if text2 == "end" or text2 == "End" or text2 == "END" \
               or text2 == "EnD" or text2 == "eND" or text2 == "ENd" \
               or text2 == "eNd" or text2 == "enD":
                chat2.send_message('See you soon, holbie')
                return ConversationHandler.END
            else:
                chat2.send_message('No task found. Please, enter a correct ID or tell me "end" to end conversation.')
        else:
            dic2 = r3.json()
            tasktitle2 = dic2.get('title')
            chat2.send_message('Task\'s name: {}'.format(tasktitle2))
            taskchecker = dic2.get('checker_available')
            if taskchecker == 'true':
                chat2.send_message('Correction mode: Checker')
            else:
                chat2.send_message('Correction mode: manual review')
            url4 = 'https://intranet.hbtn.io/projects/{}.json?auth_token={}'
            projid = dic2.get('project_id')
            r4 = requests.get(url4.format(projid, token),
                              allow_redirects=False,
                              headers=header2).json()
            projname2 = r4.get('name')
            chat2.send_message('Project\'s name: {}'.format(projname2))
            taskfile = dic2.get('github_file')
            if taskfile != "":
                chat2.send_message('GitHub file: {}'.format(taskfile))
            else:
                chat2.send_message('GitHub file: No file')
            taskdir = dic2.get('github_dir')
            if taskdir != "":
                chat2.send_message('GitHub directory: {}'.format(taskdir))
            else:
                chat2.send_message('GitHub directory: No directory')
            taskrepo = dic2.get('github_repo')
            if taskrepo != "":
                chat2.send_message('GitHub repository: {}'.format(taskrepo))
            else:
                chat2.send_message('GitHub repository: No repository')
            return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(token=os.environ['TGTOKEN'],
                      use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('project', project)],
        states={INPUT_TEXT: [MessageHandler(Filters.text, input_text)],
                INPUT_TEXT2: [MessageHandler(Filters.text, input_text2)]},
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
