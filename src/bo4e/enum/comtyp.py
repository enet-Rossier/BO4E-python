# pylint:disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class ComTyp(StrEnum):
    """
    Auflistung sämtlicher existierender Komponenten.

    .. HINT::
        Die Unterscheidung zwischen Komponenten und Geschäftsobjekten ist, dass Komponenten immer in einem Geschäftsobjekt enthalten sind.
        Komponenten sind also immer Teil von einem Geschäftsobjekt und können nicht alleine existieren.
    """

    ADRESSE = "ADRESSE"
    ANGEBOTSPOSITION = "ANGEBOTSPOSITION"
    ANGEBOTSTEIL = "ANGEBOTSTEIL"
    ANGEBOTSVARIANTE = "ANGEBOTSVARIANTE"
    AUFABSCHLAG = "AUFABSCHLAG"
    AUFABSCHLAGPROORT = "AUFABSCHLAGPROORT"
    AUFABSCHLAGREGIONAL = "AUFABSCHLAGREGIONAL"
    AUFABSCHLAGSTAFFELPROORT = "AUFABSCHLAGSTAFFELPROORT"
    AUSSCHREIBUNGSDETAIL = "AUSSCHREIBUNGSDETAIL"
    AUSSCHREIBUNGSLOS = "AUSSCHREIBUNGSLOS"
    BETRAG = "BETRAG"
    DIENSTLEISTUNG = "DIENSTLEISTUNG"
    ENERGIEHERKUNFT = "ENERGIEHERKUNFT"
    ENERGIEMIX = "ENERGIEMIX"
    FREMDKOSTENBLOCK = "FREMDKOSTENBLOCK"
    FREMDKOSTENPOSITION = "FREMDKOSTENPOSITION"
    GEOKOORDINATEN = "GEOKOORDINATEN"
    KATASTERADRESSE = "KATASTERADRESSE"
    KONFIGURATIONSPRODUKT = "KONFIGURATIONSPRODUKT"
    KONTAKTWEG = "KONTAKTWEG"
    KONZESSIONSABGABE = "KONZESSIONSABGABE"
    KOSTENBLOCK = "KOSTENBLOCK"
    KOSTENPOSITION = "KOSTENPOSITION"
    KRITERIUMWERT = "KRITERIUMWERT"
    LASTPROFIL = "LASTPROFIL"
    MARKTGEBIETINFO = "MARKTGEBIETINFO"
    MENGE = "MENGE"
    POSITIONSAUFABSCHLAG = "POSITIONSAUFABSCHLAG"
    PREIS = "PREIS"
    PREISGARANTIE = "PREISGARANTIE"
    PREISPOSITION = "PREISPOSITION"
    PREISSTAFFEL = "PREISSTAFFEL"
    RECHNUNGSPOSITION = "RECHNUNGSPOSITION"
    REGIONALEGUELTIGKEIT = "REGIONALEGUELTIGKEIT"
    REGIONALEPREISGARANTIE = "REGIONALEPREISGARANTIE"
    REGIONALEPREISSTAFFEL = "REGIONALEPREISSTAFFEL"
    REGIONALERAUFABSCHLAG = "REGIONALERAUFABSCHLAG"
    REGIONALETARIFPREISPOSITION = "REGIONALETARIFPREISPOSITION"
    REGIONSKRITERIUM = "REGIONSKRITERIUM"
    SIGMOIDPARAMETER = "SIGMOIDPARAMETER"
    STANDORTEIGENSCHAFTENGAS = "STANDORTEIGENSCHAFTENGAS"
    STANDORTEIGENSCHAFTENSTROM = "STANDORTEIGENSCHAFTENSTROM"
    STEUERBETRAG = "STEUERBETRAG"
    TAGESPARAMETER = "TAGESPARAMETER"
    TARIFBERECHNUNGSPARAMETER = "TARIFBERECHNUNGSPARAMETER"
    TARIFEINSCHRAENKUNG = "TARIFEINSCHRAENKUNG"
    TARIFPREIS = "TARIFPREIS"
    TARIFPREISPOSITION = "TARIFPREISPOSITION"
    TARIFPREISPOSITIONPROORT = "TARIFPREISPOSITIONPROORT"
    TARIFPREISSTAFFELPROORT = "TARIFPREISSTAFFELPROORT"
    TARIFZEIT = "TARIFZEIT"
    TARIFZEITENZEITSCHEIBE = "TARIFZEITENZEITSCHEIBE"
    UNTERSCHRIFT = "UNTERSCHRIFT"
    VERBRAUCH = "VERBRAUCH"
    VERTRAGSKONDITIONEN = "VERTRAGSKONDITIONEN"
    VERTRAGSTEIL = "VERTRAGSTEIL"
    VERWENDUNGSZWECKPROMARKTROLLE = "VERWENDUNGSZWECKPROMARKTROLLE"
    ZAEHLWERK = "ZAEHLWERK"
    ZAEHLZEITREGISTER = "ZAEHLZEITREGISTER"
    ZEITRAUM = "ZEITRAUM"
    ZEITREIHENWERT = "ZEITREIHENWERT"
    ZUSTAENDIGKEIT = "ZUSTAENDIGKEIT"
