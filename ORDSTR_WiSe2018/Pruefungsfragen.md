# Prüfungsfragen

1. Ordnungen:
    * Potenzen, Dominanzordnung
    * Wohlordnung
    * lexikographische Ordnung
    * lineare Erweiterung
2. funktorielle Abbildungen, Dimensionsabb.
    * Beispiele aus der VL
3. (Aktions-) Netzwerke:
    * jeweils mit Beispielen:
        - Schreibtischtäter, Logistiker, Pfadnetzwerk
    * Konstruktion von ANWn aus NWn:
        - Id-Loops ergänzen etc.
    * Reduktionen von (A)NWn:
        - Reduktionsmorphismus
    * Unterstrukturen:
        - Präordnungen sind die Unterstrukturen von ANWn
        - Kleenscher Stern:
            - kleinste Unterstruktur, Erzeuger
    * azyklische Netzwerke:
        - azyklische Erweiterungen
        - ANW azyklisch => die zugehörige Präordnung ist antisymmetrisch
        - Reduktion eines ANWs azyklisch => induziert eine Ordnung
4. Measurement Setups:
    * Intuition:
        - G: Was ich messe
        - M: Wie ich messe
        - Delta: wie ich messe
    * Verbände:
        - relatives vs. absolutes Messen
5. Skalen-Manipulations-Satz
    * wann ist die Vereinigung zweier azyklischer Kantenmengen azyklisch?
    * Anwendung:
        - Idee: Wähle Teilmenge einer Ordnung, die man dann nach belieben
            linearisiert
        - Betrachte Ordnung `(L, <=)`:
            * Teilmenge P von L
            * `R := <` auf L
            * S ist lin. strikte Ordnung auf P mit `R \cap PxP` liegt in S
            * dann ist `T = R \cup S` azyklisch im ANW zu P
            * dann ist `T^(*)` Ordnung auf L, hat lin. Erw. U auf L
            * es folgt:
                - S in T in T^(*) in U
            * und somit: `S = U\cap PxP`
        - Also kurz:
            1. `R \cap PxP` auf S erweitern
            2. U bestimmen
