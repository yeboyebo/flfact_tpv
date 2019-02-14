# @class_declaration interna_tpv_lineasvale #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_lineasvale(modelos.mtd_tpv_lineasvale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_lineasvale #
class flfact_tpv_tpv_lineasvale(interna_tpv_lineasvale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_lineasvale #
class tpv_lineasvale(flfact_tpv_tpv_lineasvale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_lineasvale_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
