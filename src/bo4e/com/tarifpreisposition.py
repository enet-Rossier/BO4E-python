"""
Contains Tarifpreisposition class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.preistyp import Preistyp
    from ..enum.waehrungseinheit import Waehrungseinheit
    from .preisstaffel import Preisstaffel


@postprocess_docstring
class Tarifpreisposition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Tarifpreisposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.TARIFPREISPOSITION], Field(alias="_typ")] = ComTyp.TARIFPREISPOSITION

    preistyp: Optional["Preistyp"] = None
    """Angabe des Preistypes (z.B. Grundpreis)"""
    einheit: Optional["Waehrungseinheit"] = None
    """Einheit des Preises (z.B. EURO)"""
    bezugseinheit: Optional["Mengeneinheit"] = None
    """Größe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr"""
    preisstaffeln: Optional[list["Preisstaffel"]] = None
    """Hier sind die Staffeln mit ihren Preisenangaben definiert"""

    mengeneinheitstaffel: Optional["Mengeneinheit"] = None
    """Gibt an, nach welcher Menge die vorgenannte Einschränkung erfolgt (z.B. Jahresstromverbrauch in kWh)"""
