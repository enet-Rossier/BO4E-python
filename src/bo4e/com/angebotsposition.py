"""
Contains Angebotsposition class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .betrag import Betrag
    from .menge import Menge
    from .preis import Preis

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Angebotsposition(COM):
    """
    Unterhalb von Angebotsteilen sind die Angebotspositionen eingebunden.
    Hier werden die angebotenen Bestandteile einzeln aufgeführt. Beispiel:
    Positionsmenge: 4000 kWh
    Positionspreis: 24,56 ct/kWh
    Positionskosten: 982,40 EUR

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Angebotsposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.ANGEBOTSPOSITION], Field(alias="_typ")] = ComTyp.ANGEBOTSPOSITION

    positionsbezeichnung: Optional[str] = None
    """Bezeichnung der jeweiligen Position des Angebotsteils"""
    positionspreis: Optional["Preis"] = None
    """Preis pro Einheit/Stückpreis des angebotenen Artikels."""

    positionsmenge: Optional["Menge"] = None
    """Menge des angebotenen Artikels (z.B. Wirkarbeit in kWh), in dieser Angebotsposition"""
    positionskosten: Optional["Betrag"] = None
    """Kosten (positionspreis * positionsmenge) für diese Angebotsposition"""

    # for a preis = menge*times validation we first need to resolve
    # https://github.com/Hochfrequenz/BO4E-python/issues/126
