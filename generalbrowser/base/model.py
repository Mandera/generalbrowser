
from generallibrary import SigInfo


class GeneralModel:
    """ Server model methods. """
    _client_model_cls = ...

    def create_client_model(self):
        """ Create a client model class for server models attributes.
            Recursively creates ClientModels for attrs that might be another model. """
        kwargs = {}
        for name in SigInfo(self._client_model_cls.__init__).names:
            if name == "self":
                continue
            attr = getattr(self, name)
            if isinstance(attr, GeneralModel):
                attr = attr.create_client_model()
            kwargs[name] = attr

        return self._client_model_cls(**kwargs)

