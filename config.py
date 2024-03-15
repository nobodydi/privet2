from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "7123033255:AAFISvx0AgicXfg9b2uU3UZecZEu5JKG2aU")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6590736889").split()))

# --------------- Channel ------------ #
FORWARD_IDS = -1002058670786
MOVIES_ID = -1002049821764
SERIES_ID = -1002065900653
