"""
Contains Zaehler class
"""

from decimal import Decimal

# pylint: disable=unused-argument
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.geraet import Geraet
    from ..com.zaehlwerk import Zaehlwerk
    from ..enum.befestigungsart import Befestigungsart
    from ..enum.messwerterfassung import Messwerterfassung
    from ..enum.registeranzahl import Registeranzahl
    from ..enum.sparte import Sparte
    from ..enum.zaehlerauspraegung import Zaehlerauspraegung
    from ..enum.zaehlergroesse import Zaehlergroesse
    from ..enum.zaehlertyp import Zaehlertyp
    from ..enum.zaehlertypspezifikation import ZaehlertypSpezifikation
    from .geschaeftspartner import Geschaeftspartner

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Zaehler(Geschaeftsobjekt):
    """
    Object containing information about a meter/"Zaehler".

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zaehler.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehler JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Zaehler.json>`_

    """

    typ: Annotated[Literal[BoTyp.ZAEHLER], Field(alias="_typ")] = BoTyp.ZAEHLER
    zaehlernummer: Optional[str] = None
    """Nummerierung des Zählers,vergeben durch den Messstellenbetreiber"""
    sparte: Optional["Sparte"] = None
    """Strom oder Gas"""
    zaehlerauspraegung: Optional["Zaehlerauspraegung"] = None
    """Spezifikation die Richtung des Zählers betreffend"""
    zaehlertyp: Optional["Zaehlertyp"] = None
    """Typisierung des Zählers"""
    zaehlwerke: Optional[list["Zaehlwerk"]] = None
    registeranzahl: Optional["Registeranzahl"] = None
    """Spezifikation bezüglich unterstützter Tarif"""
    zaehlerkonstante: Optional[Decimal] = None
    """Zählerkonstante auf dem Zähler"""
    eichung_bis: Optional[pydantic.AwareDatetime] = None
    """Bis zu diesem Datum (exklusiv) ist der Zähler geeicht."""
    letzte_eichung: Optional[pydantic.AwareDatetime] = None
    """Zu diesem Datum fand die letzte Eichprüfung des Zählers statt."""
    zaehlerhersteller: Optional["Geschaeftspartner"] = None
    """Der Hersteller des Zählers"""
    ist_fernschaltbar: Optional[bool] = None
    """Fernschaltung"""
    messwerterfassung: Optional["Messwerterfassung"] = None
    """Messwerterfassung des Zählers"""
    zaehlertypSpezifikation: Optional["ZaehlertypSpezifikation"] = None
    """Besondere Spezifikation des Zählers"""
    befestigungsart: Optional["Befestigungsart"] = None
    """Befestigungsart"""
    zaehlergroesse: Optional["Zaehlergroesse"] = None
    """Größe des Zählers"""
    geraete: Optional[list["Geraet"]] = None
    """Liste der Geräte, die zu diesem Zähler gehören, bspw. Smartmeter-Gateway"""
