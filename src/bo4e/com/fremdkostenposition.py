"""
Contains Fremdkostenposition
"""

from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .kostenposition import Kostenposition

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Fremdkostenposition(Kostenposition):
    """
    Eine Kostenposition im Bereich der Fremdkosten

    .. raw:: html

        <object data="../_static/images/bo4e/com/Fremdkostenposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Fremdkostenposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.FREMDKOSTENPOSITION], Field(alias="_typ")] = (
        ComTyp.FREMDKOSTENPOSITION  # type:ignore[assignment]
    )

    # optional attributes (additional to those from Kostenposition)
    marktpartnername: Optional[str] = None
    """Der Name des Marktpartners, der die Preise festlegt, bzw. die Kosten in Rechnung stellt"""

    marktpartnercode: Optional[str] = None
    """Die Codenummer (z.B. BDEW-Codenummer) des Marktpartners, der die Preise festlegt / die Kosten in Rechnung stellt"""

    gebietcode_eic: Optional[str] = None
    """EIC-Code des Regel- oder Marktgebietes eingetragen. Z.B. '10YDE-EON------1' für die Regelzone TenneT"""
    # todo: see issue https://github.com/Hochfrequenz/BO4E-python/issues/147 for EIC validation

    link_preisblatt: Optional[str] = None
    """Link zum veröffentlichten Preisblatt"""
