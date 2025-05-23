"""
Contains AufAbschlagProOrt class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .aufabschlagstaffelproort import AufAbschlagstaffelProOrt


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class AufAbschlagProOrt(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang
    mit örtlichen Gültigkeiten abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/AufAbschlagProOrt.json>`_

    """

    typ: Annotated[Literal[ComTyp.AUFABSCHLAGPROORT], Field(alias="_typ")] = ComTyp.AUFABSCHLAGPROORT

    postleitzahl: Optional[str] = None
    """Die Postleitzahl des Ortes für den der Aufschlag gilt."""
    ort: Optional[str] = None
    """Der Ort für den der Aufschlag gilt."""
    netznr: Optional[str] = None
    """Die ene't-Netznummer des Netzes in dem der Aufschlag gilt."""
    staffeln: Optional[list["AufAbschlagstaffelProOrt"]] = None
    """Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung."""
