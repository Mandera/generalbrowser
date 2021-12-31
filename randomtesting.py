


import json

from generalbrowser.assets.account.clientmodel import AccountClientModel


x = [
    AccountClientModel("hi_there"),
    AccountClientModel("yo"),
    AccountClientModel(AccountClientModel("uhh")),
]

print(json.dumps(x))  # HERE ** Loads next




