from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read("config.ini")


mongo_user = config.get("DB", "USER")
mongo_pass = config.get("DB", "PASSWORD")
mongo_name = config.get("DB", "DB_NAME")
domain = config.get("DB", "DOMAIN")

connect(host=f"""mongodb+srv://{mongo_user}:{mongo_pass}@{domain}/{mongo_name}?retryWrites=true&w=majority""", ssl=True)
