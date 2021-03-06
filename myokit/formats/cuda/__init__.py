#
# Provides an export to a CUDA kernel
#
# This file is part of Myokit
#  Copyright 2011-2018 Maastricht University, University of Oxford
#  Licensed under the GNU General Public License v3.0
#  See: http://myokit.org
#
from _exporter import CudaKernelExporter
from _ewriter import CudaExpressionWriter
from myokit.formats import ansic


# Importers
# Exporters
_exporters = {
    'cuda-kernel': CudaKernelExporter,
}


def exporters():
    """
    Returns a list of all exporters available in this module.
    """
    return dict(_exporters)


# Expression writers
_ewriters = {
    'cuda': CudaExpressionWriter,
}


def ewriters():
    """
    Returns a list of all expression writers available in this module.
    """
    return dict(_ewriters)


# Keywords
keywords = list(ansic.keywords)
# TODO: Append CUDA keywords
