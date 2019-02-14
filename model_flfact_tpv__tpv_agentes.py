# @class_declaration interna_tpv_agentes #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_agentes(modelos.mtd_tpv_agentes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_agentes #
class flfact_tpv_tpv_agentes(interna_tpv_agentes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_agentes #
class tpv_agentes(flfact_tpv_tpv_agentes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_agentes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
