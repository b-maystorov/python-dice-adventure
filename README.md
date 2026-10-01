# Python Dice Adventure

Python Dice Adventure ist ein kleines terminalbasiertes RPG, das Schritt für Schritt in Python entwickelt wird.

Das Projekt hat ursprünglich als einfaches Würfel- und Kampfsystem angefangen und wird aktuell zu einem größeren RPG ausgebaut. Ziel ist es, verschiedene Python-Konzepte praktisch anzuwenden und gleichzeitig ein Spiel zu entwickeln, das später immer weiter erweitert werden kann.

## Aktueller Stand

Der Spieler kann aktuell:

- einen Namen wählen
- eine Rasse auswählen
- eine Klasse auswählen
- einen Charakter mit unterschiedlichen Stats erstellen
- gegen einen Gegner kämpfen
- die eigenen Stats während des Kampfes anzeigen
- aus einem Kampf fliehen

Aktuell verfügbare Rassen:

- Human
- Elf
- Dwarf
- Orc

Aktuell verfügbare Klassen:

- Warrior
- Mage
- Rogue
- Hunter
- Paladin
- Necromancer

Die gewählte Klasse bestimmt die Grundwerte des Charakters. Die Rasse verändert diese Werte anschließend noch einmal.

Ein Elf Mage hat dadurch zum Beispiel andere Werte als ein Human Mage oder ein Dwarf Warrior.

## Stats

Das Spiel verwendet momentan folgende Charakterwerte:

- Strength
- Dexterity
- Intelligence
- Vitality
- Luck

Aus diesen Stats werden weitere Kampfwerte berechnet.

Zum Beispiel:

```text
Vitality -> maximale Lebenspunkte
Dexterity -> Armor Class
Primary Stat -> Attack Bonus
Primary Stat -> Damage Die
Die Klassen verwenden unterschiedliche Primärattribute.
Warrior      -> Strength
Paladin      -> Strength

Rogue        -> Dexterity
Hunter       -> Dexterity

Mage         -> Intelligence
Necromancer  -> Intelligence

Dadurch können verschiedene Klassen später unterschiedliche Spielstile bekommen.
Kampfsystem
Das Spiel verwendet ein einfaches rundenbasiertes Kampfsystem.
Während eines Kampfes kann der Spieler aktuell:
1. Attack
2. View Stats
3. Run

Für einen Angriff wird ein d20 gewürfelt.
d20 + Attack Bonus

Das Ergebnis wird mit der Armor Class des Gegners verglichen.
Wenn der Angriff erfolgreich ist, wird anschließend der entsprechende Schadenswürfel verwendet.
Objektorientierte Programmierung
Das Projekt verwendet objektorientierte Programmierung.
Wichtige Klassen sind zum Beispiel:
Player
Enemy
Stats

Warrior
Mage
Rogue
Hunter
Paladin
Necromancer

Human
Elf
Dwarf
Orc

Der Player besitzt eine Rasse, eine Klasse und eigene Stats.
Dadurch müssen nicht für jede Kombination eigene Klassen wie ElfMage oder OrcWarrior erstellt werden.
Beispiel:
player = Player(    name="Hero",    race=Elf(),    char_class=Mage(),)


Das Projekt verwendet damit hauptsächlich Composition, um verschiedene Teile des Charakters miteinander zu verbinden.
Projektstruktur
python-dice-adventure/
├── main.py
├── character_creation.py
├── combat.py
├── player.py
├── enemy.py
├── classes.py
├── races.py
├── stats.py
├── dice.py
│
├── tests/
│   ├── test_classes.py
│   ├── test_dice.py
│   ├── test_enemy.py
│   ├── test_player.py
│   └── test_races.py
│
└── .github/
    └── workflows/
        └── ci.yml

Verwendete Technologien
Das Projekt verwendet aktuell:
- Python 3
- Object-Oriented Programming
- Python Dataclasses
- Python Properties
- Modules und Imports
- Virtual Environments
- pytest
- Git
- GitHub
- GitHub Actions
- Continuous Integration
Tests
Das Projekt verwendet pytest für automatisierte Tests.
Aktuell werden unter anderem getestet:
- Würfelfunktionen
- Klassen-Stats
- Rassen-Boni
- Player-Erstellung
- Player-Stats
- Lebenspunkte
- Damage
- Enemy-Verhalten
Die Tests können mit folgendem Befehl gestartet werden:
python -m pytest -v

Continuous Integration
GitHub Actions führt die Tests automatisch aus, wenn Änderungen zum Repository gepusht werden oder ein Pull Request erstellt wird.
Dadurch kann geprüft werden, ob neue Features bereits vorhandene Funktionen beschädigen.
Spiel starten
Zuerst die virtuelle Umgebung aktivieren:
source .venv/bin/activate

Danach das Spiel starten:
python main.py

Geplante Erweiterungen
Das aktuelle System bildet hauptsächlich die Grundlage des Spiels.
Später sollen weitere Funktionen ergänzt werden, zum Beispiel:
- Critical Hits
- Class Abilities
- Race Passives
- Experience Points
- Level System
- weitere Gegner
- Boss Gegner
- Waffen
- Rüstung
- Inventory
- Loot
- Healing
- Mana
- Spells
- Status Effects
- mehrere Kämpfe hintereinander
- Dungeon System
- Save und Load
Ziel des Projekts
Das Projekt dient gleichzeitig als praktisches Python-Lernprojekt.
Dabei werden unter anderem folgende Themen geübt:
- Python Grundlagen
- Funktionen
- Klassen und Objekte
- Object-Oriented Programming
- Composition
- Dataclasses
- Properties
- Module
- Testing
- Git
- GitHub
- GitHub Actions
- CI
- strukturierte Softwareentwicklung
Das Spiel wird schrittweise weiterentwickelt und soll mit der Zeit mehr RPG-Mechaniken und komplexere Systeme bekommen.
```# Python Dice Adventure

Python Dice Adventure ist ein kleines terminalbasiertes RPG, das ich Schritt für Schritt mit Python entwickle.

Das Projekt hat als einfaches Würfel- und Kampfsystem angefangen und wurde inzwischen um Charaktererstellung, verschiedene Rassen und Klassen, ein Stat-System, automatisierte Tests und eine CI-Pipeline erweitert.

## Features

Aktuell unterstützt das Spiel:

- Charaktername auswählen
- 4 Rassen: Human, Elf, Dwarf, Orc
- 6 Klassen: Warrior, Mage, Rogue, Hunter, Paladin, Necromancer
- unterschiedliche Stats je nach Klasse und Rasse
- rundenbasierten Kampf
- Stats während des Kampfes anzeigen
- aus Kämpfen fliehen

## Stat-System

Der Charakter besitzt folgende Werte:

- Strength
- Dexterity
- Intelligence
- Vitality
- Luck

Aus diesen Stats werden weitere Kampfwerte berechnet.

```text
Vitality     -> Maximum Health
Dexterity    -> Armor Class
Primary Stat -> Attack Bonus
Primary Stat -> Damage Die
```

Die Klassen verwenden unterschiedliche Primärattribute:

```text
Warrior / Paladin      -> Strength
Rogue / Hunter         -> Dexterity
Mage / Necromancer     -> Intelligence
```

## OOP-Struktur

Das Projekt verwendet objektorientierte Programmierung.

Ein `Player` besteht unter anderem aus einer Rasse, einer Klasse und eigenen Stats.

```python
player = Player(
    name="Hero",
    race=Elf(),
    char_class=Mage(),
)
```

Dadurch können unterschiedliche Kombinationen erstellt werden, ohne für jede Kombination eine eigene Klasse zu benötigen.

## Projektstruktur

```text
python-dice-adventure/
├── main.py
├── character_creation.py
├── combat.py
├── player.py
├── enemy.py
├── classes.py
├── races.py
├── stats.py
├── dice.py
├── tests/
└── .github/workflows/ci.yml
```

## Technologien

Verwendet werden aktuell:

- Python 3
- Object-Oriented Programming
- Dataclasses
- Properties
- pytest
- Git
- GitHub
- GitHub Actions
- Continuous Integration

## Tests

Die automatisierten Tests laufen mit `pytest`.

```bash
python -m pytest -v
```

Aktuell werden unter anderem Klassen, Rassen, Player-Stats, Gegner und Würfelfunktionen getestet.

## Spiel starten

```bash
source .venv/bin/activate
python main.py
```

## Geplante Erweiterungen

Als Nächstes sollen unter anderem folgende Features ergänzt werden:

- Critical Hits
- Class Abilities
- Experience und Level System
- weitere Gegner
- Waffen und Rüstung
- Inventory und Loot
- Spells
- Dungeon-System
- Save / Load

## Ziel des Projekts

Das Projekt dient als praktisches Python-Lernprojekt.

Dabei übe ich unter anderem OOP, Testing, Git, CI und eine saubere modulare Projektstruktur.