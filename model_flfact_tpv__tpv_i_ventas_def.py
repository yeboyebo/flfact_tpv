# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration flfact_tpv #
from YBLEGACY.constantes import *


class flfact_tpv(interna):

    def flfact_tpv_getDesc(self):
        return "descripcion"

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.flfact_tpv_getDesc()


# @class_declaration head #
class head(flfact_tpv):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
