# @class_declaration interna_tpv_movivale #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_movivale(modelos.mtd_tpv_movivale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_movivale #
class flfact_tpv_tpv_movivale(interna_tpv_movivale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_movivale #
class tpv_movivale(flfact_tpv_tpv_movivale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_movivale_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
