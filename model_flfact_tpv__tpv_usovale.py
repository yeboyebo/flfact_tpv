# @class_declaration interna_tpv_usovale #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_usovale(modelos.mtd_tpv_usovale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_usovale #
class flfact_tpv_tpv_usovale(interna_tpv_usovale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_usovale #
class tpv_usovale(flfact_tpv_tpv_usovale, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_usovale_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
