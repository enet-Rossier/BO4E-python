"""
Contains Betrag class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.waehrungscode import Waehrungscode


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Betrag(COM):
    """
    Die Komponente wird dazu verwendet, Summenbeträge (beispielsweise in Angeboten und Rechnungen) als Geldbeträge
    abzubilden. Die Einheit ist dabei immer die Hauptwährung also Euro, Dollar etc…

    .. raw:: html

        <object data="../_static/images/bo4e/com/Betrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Betrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Betrag.json>`_

    """

    typ: Annotated[Literal[ComTyp.BETRAG], Field(alias="_typ")] = ComTyp.BETRAG

    wert: Optional[Decimal] = None
    """Gibt den Betrag des Preises an."""
    waehrung: Optional["Waehrungscode"] = None
    """Die entsprechende Waehrung"""
