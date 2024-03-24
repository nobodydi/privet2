from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "6917556221:AAEcDrW1CWI1-IHqphbutfaSoaCiwdtd1nQ")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6842001658").split()))

# --------------- Channel ------------ #
FORWARD_IDS = -1002032823792
MOVIES_ID = -1002017670110
SERIES_ID = -1002092615913
