# @class_declaration interna_tpv_tiendas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_tiendas(modelos.mtd_tpv_tiendas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_tiendas #
class flfact_tpv_tpv_tiendas(interna_tpv_tiendas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_tiendas #
class tpv_tiendas(flfact_tpv_tpv_tiendas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_tiendas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
