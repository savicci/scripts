## Rasa based chatbot integrated with discord.

### Setup done from:
- https://www.geeksforgeeks.org/chatbots-using-python-and-rasa/
- https://realpython.com/how-to-make-a-discord-bot-python/


### Json data
list of tournaments. Tournament contains list of teams.
Team contains list of players

### How to use
* Create conda env
```shell
    conda create -n rasa
    conda activate rasa
    pip install -r requirements.txt
```

* Create .env file with following contents

```
DISCORD_TOKEN=<your_bot_token>
DISCORD_GUILD=<your_guild_name, like RasaBasedChatbotGKProject>
```

### Actions to take

1. Ask which matches are playing.
2. Asks if user likes esport, and if yes which game. If lol or cs then gives links to pages.
3. 