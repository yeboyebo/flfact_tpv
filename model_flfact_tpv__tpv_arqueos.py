# @class_declaration interna_tpv_arqueos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_arqueos(modelos.mtd_tpv_arqueos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_arqueos #
class flfact_tpv_tpv_arqueos(interna_tpv_arqueos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_arqueos #
class tpv_arqueos(flfact_tpv_tpv_arqueos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_arqueos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
