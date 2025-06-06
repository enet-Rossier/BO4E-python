"""
Contains Region class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.regionskriterium import Regionskriterium


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Region(Geschaeftsobjekt):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Region.svg" type="image/svg+xml"></object>

    .. HINT::
        `Region JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Region.json>`_

    """

    typ: Annotated[Literal[BoTyp.REGION], Field(alias="_typ")] = BoTyp.REGION
    bezeichnung: Optional[str] = None
    """Bezeichnung der Region"""

    positiv_liste: Optional[list["Regionskriterium"]] = None
    """Positivliste der Kriterien zur Definition der Region"""

    negativ_liste: Optional[list["Regionskriterium"]] = None
    """Negativliste der Kriterien zur Definition der Region"""
