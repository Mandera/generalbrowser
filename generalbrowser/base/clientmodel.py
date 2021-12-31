
import json

from generallibrary import SigInfo, AutoInitBases


class GeneralClientModel(dict, metaclass=AutoInitBases):
    _page_cls = ...

    def __init__(self, **kwargs):
        self.update(cls_name=type(self).__name__)

    # def __repr__(self):
    #     attrs = {name: getattr(self, name) for name in SigInfo(type(self).__init__).names if name != "self"}
    #     return f"<{type(self).__name__}: {attrs}>"

    def create_page(self, parent=None):
        return self._page_cls(model=self, parent=parent)
