# @class_declaration interna_tpv_causasmovimiento #
import importlib

from YBUTILS.viewREST import helpers

from models.flfact_tpv import models as modelos


class interna_tpv_causasmovimiento(modelos.mtd_tpv_causasmovimiento, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfact_tpv_tpv_causasmovimiento #
class flfact_tpv_tpv_causasmovimiento(interna_tpv_causasmovimiento, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration tpv_causasmovimiento #
class tpv_causasmovimiento(flfact_tpv_tpv_causasmovimiento, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfact_tpv.tpv_causasmovimiento_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
