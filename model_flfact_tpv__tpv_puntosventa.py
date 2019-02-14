# @class_declaration interna_tpv_puntosventa #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_puntosventa(modelos.mtd_tpv_puntosventa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_puntosventa #
class flfact_tpv_tpv_puntosventa(interna_tpv_puntosventa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_puntosventa #
class tpv_puntosventa(flfact_tpv_tpv_puntosventa, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_puntosventa_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
