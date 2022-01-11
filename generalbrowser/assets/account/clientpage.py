
from generalgui import Label, Button, Page, Entry, Password
from generalbrowser.assets.base.clientpage import GeneralModelPage, GeneralClientPage


class _SigninForm(GeneralClientPage):
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


class _GeneralAccountPage(GeneralModelPage):
    def __init__(self, model, parent):
        self.status_page = Page(self)
        self.label = Label(self.status_page, f"Signed in as {self.model.email}", side="left")
        self.button_signout = Button(self.status_page, "Sign out", self.get_parent().signout, side="left")


class GeneralSigninPage(GeneralClientPage):
    def __init__(self, parent=None):
        self.sign_in_page = _SigninForm(parent=self)
        self.signed_in_page = None

        self.signin(use_form=False)  # See if stored in session

    def hook_signin_success(self, response): ...

    def signin(self, use_form=True):
        if use_form:
            email = self.sign_in_page.email.text
            password = self.sign_in_page.password.text
            response = self.client.signin(email=email, password=password)
        else:
            response = self.client.is_signed_in()

        if response.status_code == 200:
            from generalbrowser.assets.account.clientmodel import AccountClientModel
            account = self.client.deserialize(response=response, scope=locals())[0]

            self.sign_in_page.exists = False
            self.signed_in_page = account.create_page(parent=self.mainpage)

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
        else:
            self.sign_in_page.label.text = response.text
        return response
