#
# C++ expression writer
#
# This file is part of Myokit
#  Copyright 2011-2018 Maastricht University, University of Oxford
#  Licensed under the GNU General Public License v3.0
#  See: http://myokit.org
#
from myokit.formats.ansic import AnsiCExpressionWriter


class CppExpressionWriter(AnsiCExpressionWriter):
    """
    This :class:`ExpressionWriter <myokit.formats.ExpressionWriter>` translates
    myokit :class:`expressions <myokit.Expression>` to their C++ equivalent.
    """
    pass
