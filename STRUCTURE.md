# Struktura biblioteke

Ovaj root je biblioteka koja drži više settinga i jednu zajedničku metodu. (Folder se trenutno zove "Sharn", preimenovaćemo ga kasnije.)

```
.
├── CLAUDE.md        persona i proces (Kroničar)
├── STRUCTURE.md     ovaj fajl
├── _tools/          alati: .venv + extract.py (izvlačenje teksta iz PDF-a)
│
├── method/          METODA: ponovo upotrebljiv GM zanat (knjige o pisanju sesija/kampanja)
│   ├── 00_source/     method PDF-ovi
│   ├── 01_batches/    izvučen tekst po poglavlju (batch_XX.md)
│   ├── 02_summaries/  vjeran sažetak po batchu (summary_XX.md)
│   └── 03_method/     kronicar_method.md, method_index.md, sources_traceability.md
│
├── settings/        SADRŽAJ: po jedan podfolder za svaki setting
│   └── sharn/
│       ├── 00_source/     setting PDF
│       ├── 01_batches/
│       ├── 02_summaries/
│       └── 03_master/     master_summary, index, glossary, cross_references
│
├── campaign/        ŽIVO STANJE: po jedan podfolder za svaku kampanju/setting
│   └── sharn/
│       ├── party/         igrači i PC-jevi, lične kuke
│       ├── organization/  vlastita organizacija party-ja
│       ├── npcs/          NPC-jevi na tabli (odnosi, stanje)
│       ├── factions/      velike sile kao fronts (goal + grim portents)
│       ├── situations/    banka potencijalnih situacija (NE priča)
│       ├── log/           sažeci odigranih sesija
│       ├── world/         player-facing canon (Stanje Khorvairea 998 YK) + DM sistematizacija
│       └── threads.md     žive niti / otvoreni plotovi
│
└── output/          PROIZVODI: po jedan podfolder za svaki setting
    └── sharn/            gotove sesije, kampanjski lukovi, NPC kartice...
```

## Sloj kampanje (campaign/)
`settings/` je statičan knjiški kanon. `campaign/` je živo stanje koje se mijenja svake sesije: ko su igrači, šta je njihova organizacija, koga su upoznali, gdje stoje velike sile, i banka situacija. **Pravilo: ovdje se prave situacije koje se mogu desiti, ne priče.** Iz `campaign/` + metode nastaju gotove sesije u `output/`.

## Kako teče posao
- **Setting knjiga** (npr. Sharn): pipeline `00_source → 01_batches → 02_summaries → 03_master`. Rezultat je navigabilna referenca.
- **Method knjiga**: isti prednji pipeline (`00_source → 01_batches → 02_summaries`), ali master je `03_method/` sa **jednom ujedinjenom Kroničar metodom** (sintetizovano iz svih method knjiga, svaki korak tagovan i traceable do izvora).
- **Output**: pokrenem Kroničar metodu (forma + proces) koristeći setting master kao sadržaj (meso), pa snimim gotov materijal u `output/<setting>/`.

## Pravila koja uvijek vrijede
- Sav izlazni tekst na bosanskom; vlastita imena i mehanički termini na engleskom.
- Pravilo provjere: ništa se ne izmišlja iz izvora; nepokriveno se označi `[HOMEBREW]` ili se kaže da knjiga to ne pokriva.
- Oznake `[PLAYER]` i `[DM]`.

## Trenutni status
- `settings/sharn/` — kompletno obrađeno (9 batcheva, 9 sažetaka, master).
- `method/` — kompletno obrađeno. Dvije knjige (*Return of the Lazy Dungeon Master* i *Sly Flourish's Fantastic Locations*) prošle kroz pipeline (10 batcheva, 9 sažetaka), i izgrađena je `03_method/kronicar_method.md` (ujedinjena metoda) + `method_index.md` + `sources_traceability.md`.
- `output/sharn/` — prazno, čeka prvi deliverable (sesija, kampanjski luk, NPC kartica, location writeup).
