"""
Contains Energieherkunft class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.erzeugungsart import Erzeugungsart


# pylint: disable=no-name-in-module


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Energieherkunft(COM):
    """
    Abbildung einer Energieherkunft

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energieherkunft.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energieherkunft JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Energieherkunft.json>`_

    """

    typ: Annotated[Literal[ComTyp.ENERGIEHERKUNFT], Field(alias="_typ")] = ComTyp.ENERGIEHERKUNFT

    erzeugungsart: Optional["Erzeugungsart"] = None
    """Art der Erzeugung der Energie."""
    anteil_prozent: Optional[Decimal] = None
    """Prozentualer Anteil der jeweiligen Erzeugungsart."""
