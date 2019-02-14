# @class_declaration interna_tpv_secuenciascomanda #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_secuenciascomanda(modelos.mtd_tpv_secuenciascomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_secuenciascomanda #
class flfact_tpv_tpv_secuenciascomanda(interna_tpv_secuenciascomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_secuenciascomanda #
class tpv_secuenciascomanda(flfact_tpv_tpv_secuenciascomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_secuenciascomanda_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
