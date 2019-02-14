# @class_declaration interna_tpv_claveacceso #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_claveacceso(modelos.mtd_tpv_claveacceso, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_claveacceso #
class flfact_tpv_tpv_claveacceso(interna_tpv_claveacceso, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_claveacceso #
class tpv_claveacceso(flfact_tpv_tpv_claveacceso, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_claveacceso_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
