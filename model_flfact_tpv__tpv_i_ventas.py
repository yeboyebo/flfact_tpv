# @class_declaration interna_tpv_i_ventas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_i_ventas(modelos.mtd_tpv_i_ventas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_i_ventas #
class flfact_tpv_tpv_i_ventas(interna_tpv_i_ventas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_i_ventas #
class tpv_i_ventas(flfact_tpv_tpv_i_ventas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_i_ventas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
