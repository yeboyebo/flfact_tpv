# @class_declaration interna_tpv_pagoscomanda #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_pagoscomanda(modelos.mtd_tpv_pagoscomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_pagoscomanda #
class flfact_tpv_tpv_pagoscomanda(interna_tpv_pagoscomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_pagoscomanda #
class tpv_pagoscomanda(flfact_tpv_tpv_pagoscomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_pagoscomanda_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
