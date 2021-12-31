
from generalbrowser.base.server import GeneralServer
from generallibrary import deco_optional_suppress


class AccountServer(GeneralServer):
    """ Register new account.
        Sign in.
        Sign out.
        See if signed in. """
    _account_cls = ...

    @deco_optional_suppress(Exception, return_bool=False)
    def account(self, error=True):
        """ Return account or None if error is False. """
        # Raise HttpResponse? If not signed in
        return self._account_cls.objects.get(pk=self.session("account_pk"))

    def signin(self, account):
        self.session(account_pk=account.pk)

    def signout(self):
        self.session(account_pk=None)




