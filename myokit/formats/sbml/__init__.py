#
# Provides SBML support
#
# This file is part of Myokit
#  Copyright 2011-2018 Maastricht University, University of Oxford
#  Licensed under the GNU General Public License v3.0
#  See: http://myokit.org
#
from _importer import SBMLImporter, SBMLError  # noqa


# Importers
_importers = {
    'sbml': SBMLImporter,
}


def importers():
    """
    Returns a dict of all importers available in this module.
    """
    return dict(_importers)

# Exporters
# Expression writers
