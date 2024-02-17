from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "6315381025:AAHQbodUGYQ2r6q1Fi0cjbeFelhn_4s2zAY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280103226").split()))

# --------------- Channel ------------ #
FORWARD_IDS = -1001652627420
MOVIES_ID = -1002045076727
SERIES_ID = -1002142358903
