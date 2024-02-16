from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "6928189124:AAGjOHYVN3GmppoPCiLuTwuit6rBa-4jUDY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280103226").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mrag2408:FWsWe727LzF00j9v@cluster0.hhyhf6l.mongodb.net/?retryWrites=true&w=majority")
