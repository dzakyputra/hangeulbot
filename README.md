# hangeulbot

<p align="center">
<img align="center" src="https://s4.gifyu.com/images/hangeul1.gif" alt="Learn Hangeul" />
</p>

<br>

Read the full tutorial in my Medium article [here](https://towardsdatascience.com/create-a-telegram-bot-to-help-you-learn-a-new-language-aef10607b5f9?source=friends_link&sk=da043bfdb17b9559af7a75321cf30e72).

You can check the bot in [here](https://t.me/learnhangeulbot), type `/word` command to get a word and an audio file.

## Prerequisites

- [Google Text-to-Speech API](https://cloud.google.com/text-to-speech)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc)
- [requests](https://requests.readthedocs.io/en/master)
- [pandas](https://pandas.pydata.org/)

You can install all the libraries using this command.

```
pip install -r requirements.txt
```

## Steps
### Preparing Dataset
Before we can use the bot, make sure you run the `database.py` first so that we have the `dictionary.csv` and the audio files. Make sure you already set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to your credential path.

```
python database.py
```

### Run the bot
Make sure to change `YOUR_BOT_TOKEN` in `main.py` to your bot's token before running the command below.

```
python main.py
```
