"""
Contains Konzessionsabgabe
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.abgabeart import AbgabeArt


# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Konzessionsabgabe(COM):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Konzessionsabgabe verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Konzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Konzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Konzessionsabgabe.json>`_

    """

    typ: Annotated[Literal[ComTyp.KONZESSIONSABGABE], Field(alias="_typ")] = ComTyp.KONZESSIONSABGABE

    satz: Optional["AbgabeArt"] = None
    """Art der Abgabe"""

    kosten: Optional[Decimal] = None
    """Konzessionsabgabe in E/kWh"""

    kategorie: Optional[str] = None
    """Gebührenkategorie der Konzessionsabgabe"""
