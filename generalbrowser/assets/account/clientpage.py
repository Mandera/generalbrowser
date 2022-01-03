
from generalgui import Label, Button, Page, Entry, Password
from generalbrowser.base.clientpage import GeneralModelPage, GeneralClientPage


class _SigninPage(GeneralClientPage):
    """ General sign in Page. """
    def __init__(self, parent):
        self.label = Label(self, "Welcome")

        self.email = Entry(self)
        self.password = Password(self, hidden=True)

        self.email.text = "tests@gmail.com"
        self.password.text = "hellothere"

        buttons = Page(self)
        self.button_signin = Button(buttons, "Sign in", parent.signin)
        self.button_register = Button(buttons, "Register", parent.register)


class _SignedInPage(GeneralModelPage):
    def __init__(self, model, parent):
        self.label = Label(self, f"Signed in as {self.model.email}", side="left")
        self.button_signout = Button(self, "Sign out", self.account_page.signout, side="left")


class AccountPage(GeneralClientPage):
    def __init__(self, parent=None):
        self.sign_in_page = _SigninPage(parent=self)

        self.signed_in_page = _SignedInPage


        response = self.client.is_signed_in()
        if response.status_code == 200:
            self.hook_signin_success(response=response)

    def hook_signin_success(self, response):
        self.exists = False

        account = self.client.deserialize(response=response)[0]
        account.create_page(parent=self.mainpage)

    # def hook_signin_success(self, response): ...

    def signin(self):
        email = self.sign_in_page.email.text
        password = self.sign_in_page.password.text
        response = self.client.signin(email=email, password=password)
        if response.status_code == 200:
            self.hook_signin_success(response=response)
        else:
            self.sign_in_page.label.text = response.text
        return response

    def register(self):
        email = self.sign_in_page.email.text
        password = self.sign_in_page.password.text
        response = self.client.register(email=email, password=password)
        self.sign_in_page.label.text = response.text
        return response

    def signout(self):
        response = self.client.signout()
        if response.status_code == 200:
            self.sign_in_page.exists = True
            self.signed_in_page.exists = False
        return response
