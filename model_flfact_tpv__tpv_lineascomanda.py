# @class_declaration interna_tpv_lineascomanda #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_lineascomanda(modelos.mtd_tpv_lineascomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_lineascomanda #
class flfact_tpv_tpv_lineascomanda(interna_tpv_lineascomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_lineascomanda #
class tpv_lineascomanda(flfact_tpv_tpv_lineascomanda, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_lineascomanda_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
