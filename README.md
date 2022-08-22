# DiscordBot
I created my own Discord bot for my discord channel. Bot can moderate and play YouTube music. 

I have a separate TOKEN.txt file

# Requirements
You'll need to install the following modules/libraries in console:
```sh
pip install youtube_dl
pip install discord
```

You'll also need to create a Bot Application on Discord's Developer Portal - https://discord.com/developers/docs/intro

You'll also need to download and set up ffmpeg, but you can see the whole process of doing that in the tutorial video - https://ffmpeg.org/download.html

# Features
## Music
- The bot uses youtube_dl to stream the music, but doesn't download the music file onto the computer
- The bot can only play 1 song at a time and can queue songs.
- The bot can pause, resume, and skip music
- The bot can show the queue

## Moderation
- The bot can show how the member changed his message
- The bot can show the content of the deleted message
- The bot can autorole
- The bot can clear chat messages, by default 10 messages
- The bot can mute member
- The bot can say "hi"
- The bot can kick, ban and unban members

## Help
The bot can show list of commands

## ErrorHandler
Shows what kind of problem has arisen and how to solve it
