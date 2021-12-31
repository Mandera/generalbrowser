
from generalbrowser.base.clientmodel import GeneralClientModel
from generalbrowser.assets.account.clientpage import _SignedInPage


class AccountClientModel(GeneralClientModel):
    _page_cls = _SignedInPage

    def __init__(self, email):
        self.email = email
