
from generalbrowser.assets.base.client import GeneralClient


class AccountClient(GeneralClient):
    def register(self, email, password):
        """ :param MainframeClient self: """
        return self.post(endpoint="account", email=email, password=password)

    def signin(self, email, password):
        """ :param MainframeClient self: """
        return self.get(endpoint="account", email=email, password=password)

    def is_signed_in(self):
        """ :param MainframeClient self: """
        return self.get(endpoint="account")

    def signout(self):
        """ :param MainframeClient self: """
        return self.post(endpoint="account")


