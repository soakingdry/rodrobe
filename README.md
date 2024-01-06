# RoDrobe


![GitHub repo size](https://img.shields.io/github/repo-size/soakingdry/rodrobe)
![GitHub issues](https://img.shields.io/github/issues/soakingdry/rodrobe)
![GitHub stars](https://img.shields.io/github/stars/soakingdry/rodrobe)
![GitHub forks](https://img.shields.io/github/forks/soakingdry/rodrobe)


Rodrobe is a discord roblox clothing bot for your group and  comes with many features which
can be used to increase your income if used correctly

## Features
  - Clothing uploader
  - Group clothing stealer
  - Auto robux to USD converter with configurable rates

    (Shows for every command with robux amount displayed + the sales notifier )
  - Clothing downloader
  - Watermark Remover
  - Sales notifier
  - Group Balance viewer
  - Popular items scraper / reuploader

## Commands
Check out the [documentation](https://github.com/soakingdry/rodrobe/tree/main/docs/commands) (located in the "docs" folder if the link doesn't work) for a description on what each command does and how to use them


## Installation
1) Install [python 3.11](https://www.python.org/downloads/release/python-3115/)
2) Open your terminal and run the following:
```console
$ git clone https://github.com/soakingdry/rodrobe
$ cd rodrobe
$ pip3 install -r requirements.txt
```
3) Open the file named `.toml.example` and fill in the fields appropriately (example)
-  it is adviced not to use your main account for the UPLOADER cookie since there is a risk of termination

```toml
[group]
holder_cookie = "holder account cookie here"
# dont use your main account or the uploader
uploader_cookie = "uploader account cookie"
# your group id
group_id = 0

[discord]
# the webhook used for sales notifications
sales_webhook = ""
# prefix of the bot.. slash commands may be supported in the future
bot_prefix = "!"
bot_whitelist = [1,21231] # put the whitelisted discord ids in here
# discord bot token
bot_token = ""

[assets]
# The robux price for a shirt/pant which will be used when a shirt/pant is republished
item_price = 5
# # The robux price for a t-shirt which will be used when a tshirt is republished
tshirt_price = 5

# This checks if an asset has been cached by rodrobe.If the asset is cached then rodrobe will ignore the asset
# This config only applies to the sgroup and scrape command.
ignore_duplicates=true

[other]
debug_mode=false
# The time the program will retry after if it a ratelimit occurs
ratelimit_wait_time=4
```
4) Rename the  `.toml.example` file to `.toml` once you have filled in the appropriate fields
5) Create a file called `description.txt` in the `config` folder and write a description. This will be used for when the bot uploads clothing
6) Run this main.py file
```console
$ python3 main.py
```

## TODO:
   - Proxy support
   - Make uploader & holder accounts global instead of initializing them repeatedly
   - Script to clear cache
   - Switch to async and refactor alot of code
