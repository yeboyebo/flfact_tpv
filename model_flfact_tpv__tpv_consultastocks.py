# @class_declaration interna_tpv_consultastocks #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_consultastocks(modelos.mtd_tpv_consultastocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_consultastocks #
class flfact_tpv_tpv_consultastocks(interna_tpv_consultastocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_consultastocks #
class tpv_consultastocks(flfact_tpv_tpv_consultastocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_consultastocks_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
