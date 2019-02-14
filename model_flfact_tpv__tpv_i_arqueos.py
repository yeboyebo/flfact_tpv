# @class_declaration interna_tpv_i_arqueos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_i_arqueos(modelos.mtd_tpv_i_arqueos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_i_arqueos #
class flfact_tpv_tpv_i_arqueos(interna_tpv_i_arqueos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_i_arqueos #
class tpv_i_arqueos(flfact_tpv_tpv_i_arqueos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_i_arqueos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
