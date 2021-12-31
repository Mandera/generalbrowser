
from django.db import models

from generalbrowser.base.model import GeneralModel
from generalbrowser.assets.account.clientmodel import AccountClientModel


class Account(GeneralModel):
    _client_model_cls = AccountClientModel

    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email



