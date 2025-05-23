"""
Contains PreisblattKonzessionsabgabe class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .preisblatt import Preisblatt

if TYPE_CHECKING:
    from ..enum.kundengruppeka import KundengruppeKA


# pylint: disable=too-few-public-methods


@postprocess_docstring
class PreisblattKonzessionsabgabe(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung von allgemeinen Abgaben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattKonzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattKonzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/PreisblattKonzessionsabgabe.json>`_

    """

    typ: Annotated[Literal[BoTyp.PREISBLATTKONZESSIONSABGABE], Field(alias="_typ")] = (
        BoTyp.PREISBLATTKONZESSIONSABGABE  # type: ignore[assignment]
    )
    # required attributes (additional to those of Preisblatt)
    kundengruppe_k_a: Optional["KundengruppeKA"] = None
    """Kundegruppe anhand derer die Höhe der Konzessionabgabe festgelegt ist"""

    # there are no optional attributes (additionally to those of Preisblatt)
