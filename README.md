# SuperHolbie

SuperHolbie is a Telegram bot initially made for the Holberton School "Hack day: Checker challenge!" project. Its purpose is putting into practice some knowledges related to the usage of APIs, through the integration of the Holberton School Checker API to retrieve information related to the program.

It has been entirely developed and written in Linux system and Python language and makes use of the python-telegram-bot library and the Telegram Bot API tools provided by Telegram. SuperHolbie is able to be used in every Telegram platforms (web app, Android, iOS, Mac, Windows, Linux) and has been deployed using the services of Heroku servers.

### Table of contents
1. [Installation and Usage](#1)
   1. [Devs](#11)
   2. [Users](#12)
   3. [Usage](#13)
   4. [Examples](#14)
   5. [Demo](#15)
2. [Roadmap](#2)
3. [Author and Contributors](#3)
4. [Documentation](#4)

## 1. Installation and Usage <a name="1"></a>

### i. Devs <a name="11"></a>
In order to run locally and start using the bot from the point of view of devs, it is so simple as:

**First**. Clone this repository in a Linux environment: `git clone https://github.com/nicolasportela/Telegram-Bot.git`\
**Second**. Install the python-telegram-bot library: `pip install python-telegram-bot`\
**Third**. Run its main file (bot\.py) from the command line as any Python or executable file: `python3 bot.py` or `./bot.py`, respectively (to stop it, run Ctrl+C).\
**Fourth**. While running, open a chat with [SuperHolbie](http://t.me/SuperHolbieBot) in Telegram and press "start" button to start to use it.

\
**Before starting, you must consider:** 
* You need to be a Holberton School member in order to get some keys required to retrieve information from its API, represented in the source code by environment variables: HBTNAPIKEY (Holberton API key), HBTNEMAIL (Holberton account e-mail), HBTNPASSWORD (Holberton account password).
* You need to ask for your own Telegram bot token: [instructions here](https://core.telegram.org/bots#creating-a-new-bot). It is represented in the source code by the environment variable named TGTOKEN.
* "Procfile" and "requirements.txt" are files required by Heroku to deployment. You may not need them if you won't deploy your bot or if you will do it using other services.

### ii. Users <a name="12"></a>
In order to start using the bot from the point of view of users, you will need a Telegram account and then, it is so simple as:

**First.** Open a chat with [SuperHolbie](http://t.me/SuperHolbieBot) in Telegram.\
**Second.** Press "start" button to start to use it.

### iii. Usage <a name="13"></a>
A Telegram bot consists on an automatized software ready to respond according to commands, messages and requests entered by users or other automatized processes. In this sense, SuperHolbie is able to respond to the following commands at the moment:

* `/start`: Shows a welcome message with a quick summary about SuperHolbie.
* `/end`: Ends a conversation if there is one running. It stops SuperHolbie from listening and lets you enter a new command.
* `/help`: Shows extra info about SuperHolbie: demo, source code, documentation and available commands at the moment.
* `/project`: Receives a Holberton School project's ID (integer number) as input from user and retrieves information about that project: name, tasks, GitHub directory and GitHub repository. It alerts if the ID entered is not valid and asks for a new one. Additionally, after retrieving information from a valid project's ID, the user is prompted to optionally enter a tasks's ID (integer number) from that project to retrieve extra information about any of its tasks: correction mode and GitHub file/s. In the same way, if the tasks's ID entered is not valid, the bot asks for a new one.

### iv. Examples <a name="14"></a>

![SuperHolbie screenshots](https://lh3.googleusercontent.com/pw/ACtC-3csAW175HlvTRJxOV3MFyRZmHWE-m06jhX3HBaf54IV49T92fWMnPui4TK5ysvJ0G3x9p3wmyxnZAJgJjQKQBnVUsOphqpfU_YsGl_eqcJwoXVndii7V_KqGmVdyUGYRSxiF8gWACsvNt7JfixQk9_1=w1154-h923-no?authuser=0)

### v. Demo <a name="15"></a>

[![SuperHolbie Demo](https://lh3.googleusercontent.com/pw/ACtC-3cdyRZxTqbf51OP1-m6qVBsvywc_JQSK9xwdJqyGfBlgrKKf3MjnyUJrtDALMuLWJqBAwFosJevWCpxEv39j4igthFYHIdzhc0Pecfd5LEwTVNbFYubvDXezfnrdhzoTkLKvN9lLiCLVgFzwjTn1Kte=w1160-h655-no?authuser=1)](https://youtu.be/x2P-HbK8G2Y "SuperHolbie Demo")

## 2. Roadmap <a name="2"></a>
SuperHolbie is in early stage of development. In this sense, it is planned to develop the following features:
* Ability to receive variable number of arguments.
* Inline bot mode implementation.
* Webhook implementation.
* Commands which allow to retrieve personal information from the Checker API.
* Useful tools for devs.

## 3. Author and Contributors <a name="3"></a>
* Author: [Nicolás Portela](https://github.com/nicolasportela)
* Contributors:
  * [Atenea Castillo](https://github.com/AteCastillo)
  * [Luciana Sarachu](https://github.com/luciana-sarachu)
  * [Pedro Arbilla](https://github.com/parbilla)
  * [Roberto Ribeiro](https://github.com/ribeiro-uy)
  * [Sebastián Olmos](https://github.com/olmoshbtn)

## 4. Documentation <a name="4"></a>
* [Telegram Bots](https://core.telegram.org/bots)
* [Telegram Bot API](https://core.telegram.org/bots/api)
* [python-telegram-bot library](https://python-telegram-bot.org)
* [Holberton School Checker API and project](https://intranet.hbtn.io/projects/434) (requires authentication)

<br>