"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "5948661"))
API_HASH = getenv("API_HASH", "ed081430c75f3e0b9a95b3b5d461fa73")
BOT_TOKEN = getenv("BOT_TOKEN", "")
SESSION_STRING = getenv("SESSION_STRING", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "CozmoUpdates")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CozmoSupport_Official")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ALKnowledgeHub")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1773779239").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
