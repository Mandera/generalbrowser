

from generalbrowser.assets.account.client import AccountClient
from generalbrowser.assets.account.clientpage import GeneralSigninPage


client = AccountClient(domain="http://127.0.0.1:8000")
client.create_page()
