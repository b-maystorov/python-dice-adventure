# Python Dice Adventure

Python Dice Adventure ist ein kleines terminalbasiertes RPG, das ich als Python-Lernprojekt entwickle.

Das Projekt hat als einfaches Würfelspiel angefangen und wurde inzwischen um Charaktererstellung, verschiedene Rassen und Klassen, ein Stat-System, rundenbasierten Kampf, Tests und CI erweitert.

## Features

- 4 Rassen: Human, Elf, Dwarf, Orc
- 6 Klassen: Warrior, Mage, Rogue, Hunter, Paladin, Necromancer
- individuelles Stat-System
- rundenbasierter Kampf
- verschiedene Primärattribute je nach Klasse
- automatisierte Tests mit pytest
- GitHub Actions CI

## OOP

Das Projekt verwendet objektorientierte Programmierung.

Ein Spieler besteht aus mehreren Komponenten wie:

```text
Player
├── Race
├── Character Class
└── Stats
```

Dadurch können unterschiedliche Kombinationen wie `Elf Mage` oder `Dwarf Warrior` erstellt werden, ohne für jede Kombination eine eigene Klasse zu benötigen.

## Technologien

- Python 3
- Object-Oriented Programming
- Dataclasses
- pytest
- Git & GitHub
- GitHub Actions
- Continuous Integration

## Starten

```bash
source .venv/bin/activate
python main.py
```

Tests ausführen:

```bash
python -m pytest -v
```

## Geplant

Das Spiel soll schrittweise erweitert werden, unter anderem mit:

- Class Abilities
- Critical Hits
- XP und Leveling
- weiteren Gegnern
- Inventory und Loot
- Waffen und Rüstung
- Dungeon-System

Das Projekt dient vor allem dazu, Python, OOP, Testing und saubere Softwarestruktur praktisch zu lernen.