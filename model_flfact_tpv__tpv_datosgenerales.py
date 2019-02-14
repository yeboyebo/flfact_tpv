# @class_declaration interna_tpv_datosgenerales #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_datosgenerales(modelos.mtd_tpv_datosgenerales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_datosgenerales #
class flfact_tpv_tpv_datosgenerales(interna_tpv_datosgenerales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_datosgenerales #
class tpv_datosgenerales(flfact_tpv_tpv_datosgenerales, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_datosgenerales_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
