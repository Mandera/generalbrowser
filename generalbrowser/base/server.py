
from rest_framework.response import Response
from django.http import HttpResponse

from generalbrowser.base.client_and_server import _GeneralClientAndServer
from generallibrary import getBaseClassNames, dumps


class GeneralServer(_GeneralClientAndServer):
    """ Server methods to talk to client. """
    def __init__(self):
        assert "APIView" in getBaseClassNames(self)  # from rest_framework.views import APIView

    def session(self, *args, **kwargs):
        """ Set session values with kwargs and return session values with args.

            :param rest_framework.views.APIView or GeneralServer self: """
        for key, value in kwargs.items():
            self.request.session[key] = value
        return [self.request.session[key] for key in args]

    @property
    def data(self):
        """ Dictionary of POST values.

            :param rest_framework.views.APIView or GeneralServer self: """
        return self.request.POST.dict()

    def extract_data(self, *keys, default=...):
        """ Returns tuple with values of given keys, error for missing keys unless default is specified. """
        if default is Ellipsis:
            return tuple(self.data[key] for key in keys)
        else:
            return tuple(self.data.get(key, default) for key in keys)

    @staticmethod
    def serialize(*models):
        """ Todo: Send client models in header instead? That way we can serialize inside success method instead.
            Convert django models to client models. """
        client_models = [model.create_client_model() for model in models]
        return HttpResponse(dumps(client_models), headers={"testing": 5})
        # return HttpResponse(dumps(client_models), content_type="application/octet-stream", headers={"testing": 5})

    @staticmethod
    def success(msg=None, files=None, code=None):
        if files:
            filename, file = next(iter(files.items()))
            response = HttpResponse(file, content_type="application/octet-stream")
            response["Content-Disposition"] = f'attachment; filename={filename}'
        else:
            response = Response(msg)
        if code is not None:
            response.status_code = code
        return response

