# @class_declaration interna_tpv_comandas #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_comandas(modelos.mtd_tpv_comandas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_comandas #
class flfact_tpv_tpv_comandas(interna_tpv_comandas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_comandas #
class tpv_comandas(flfact_tpv_tpv_comandas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_comandas_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
