.. _formats/mathml:

******
MathML
******

Export of model equations to a Content and Presentation MathML is provided by
the mathml module. In addition, a general purpose MathML parsing method is
included.

API
===

.. module:: myokit.formats.mathml

.. autofunction:: parse_mathml

.. autofunction:: parse_mathml_rhs

.. autofunction:: exporters

.. autoclass:: HTMLExporter
    :members:
    :inherited-members:

.. autoclass:: XMLExporter
    :members:
    :inherited-members:

.. autofunction:: ewriters

.. autoclass:: MathMLExpressionWriter
    :members:
    :inherited-members:
    
.. autoclass:: MathMLError
    :members:
