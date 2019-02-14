# @class_declaration interna_tpv_cantidadpago #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_cantidadpago(modelos.mtd_tpv_cantidadpago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_cantidadpago #
class flfact_tpv_tpv_cantidadpago(interna_tpv_cantidadpago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_cantidadpago #
class tpv_cantidadpago(flfact_tpv_tpv_cantidadpago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_cantidadpago_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
