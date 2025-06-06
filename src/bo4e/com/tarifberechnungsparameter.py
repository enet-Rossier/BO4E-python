"""
Contains Tarifberechnungsparameter class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.messpreistyp import Messpreistyp
    from ..enum.tarifkalkulationsmethode import Tarifkalkulationsmethode
    from .preis import Preis
    from .tarifpreis import Tarifpreis

# yes. there is no description in the official docs.
# https://github.com/Hochfrequenz/BO4E-python/issues/328

# pylint: disable=too-few-public-methods, empty-docstring, too-many-instance-attributes


@postprocess_docstring
class Tarifberechnungsparameter(COM):
    """
    In dieser Komponente sind die Berechnungsparameter für die Ermittlung der Tarifkosten zusammengefasst.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifberechnungsparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifberechnungsparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Tarifberechnungsparameter.json>`_

    """

    typ: Annotated[Literal[ComTyp.TARIFBERECHNUNGSPARAMETER], Field(alias="_typ")] = ComTyp.TARIFBERECHNUNGSPARAMETER

    berechnungsmethode: Optional["Tarifkalkulationsmethode"] = None
    """Gibt an, wie die Einzelpreise des Tarifes zu verarbeiten sind"""
    ist_messpreis_in_grundpreis_enthalten: Optional[bool] = None
    """True, falls der Messpreis im Grundpreis (GP) enthalten ist"""

    ist_messpreis_zu_beruecksichtigen: Optional[bool] = None
    """
    True, falls bei der Bildung des Durchschnittspreises für die Höchst- und Mindestpreisbetrachtung der Messpreis mit
    berücksichtigt wird
    """

    messpreistyp: Optional["Messpreistyp"] = None
    """Typ des Messpreises"""

    kw_inklusive: Optional[Decimal] = None
    """Im Preis bereits eingeschlossene Leistung (für Gas)"""
    # todo: type decimal is most likely wrong: https://github.com/Hochfrequenz/BO4E-python/issues/327

    kw_weitere_mengen: Optional[Decimal] = None
    """Intervall, indem die über "kwInklusive" hinaus abgenommene Leistung kostenpflichtig wird (z.B. je 5 kW 20 EURO)"""
    # todo: type decimal is most likely wrong: https://github.com/Hochfrequenz/BO4E-python/issues/327

    hoechstpreis_n_t: Optional["Preis"] = None
    """Höchstpreis für den Durchschnitts-Arbeitspreis NT"""
    hoechstpreis_h_t: Optional["Preis"] = None
    """Höchstpreis für den Durchschnitts-Arbeitspreis HT"""
    mindestpreis: Optional["Preis"] = None
    """Mindestpreis für den Durchschnitts-Arbeitspreis"""
    zusatzpreise: Optional[list["Tarifpreis"]] = None
    """Liste mit zusätzlichen Preisen, beispielsweise Messpreise und/oder Leistungspreise"""
