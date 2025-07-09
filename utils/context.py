from collections import ChainMap

from promplate import ChainContext
from reactivity.hmr.proxy import Proxy


class ReactiveContext(ChainContext):
    def __init__(self, least=None, *maps):
        super().__init__(least, *maps)
        self.maps[:] = [Proxy(ChainMap(*self.maps))]
