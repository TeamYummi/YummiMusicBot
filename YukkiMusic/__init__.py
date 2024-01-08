#
# Copyright (C) 2021-2022 by TeamYummi@Github, < https://github.com/TeamYummi >.
#
# This file is part of < https://github.com/TeamYummi/YummiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYummi/YummiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from YummiMusic.core.bot import YummiBot
from YummiMusic.core.dir import dirr
from YummiMusic.core.git import git
from YummiMusic.core.userbot import Userbot
from YummiMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YummiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
