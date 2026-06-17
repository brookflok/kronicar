# campaign/sharn — živo stanje kampanje

Ovaj sloj drži ono što se mijenja kako se igra: igrače i njihove likove, njihovu organizaciju, NPC-jeve koje su upoznali, stanje velikih sila i banku situacija. Odvojen je od `settings/sharn/` (knjiški kanon, statičan) i `method/` (kako radimo).

**Sistem ove kampanje: D&D 5e.** Sve mehaničko (klase, CR, stat blokovi, predmeti) radim po 5e; Sharn knjiga (3.5) je isključivo lore/setting. Format: **kampanja** (oneshot već odigran), likovi na 5. levelu. Jezgro: party vodi **Inquisitive privatnu detektivsku agenciju** (vidi `organization/`).

## Pravilo (najvažnije): situacije, ne priče
Ovdje **ne pišemo priče niti unaprijed sklopljene zaplete**. Pišemo **situacije koje se mogu desiti**: sile u pokretu, tajne koje se mogu otkriti, kuke, i reakcije svijeta ("ako party uradi X, svijet reaguje Y"). Priču prave igrači za stolom. Mi samo postavljamo pozornicu i držimo je živom.

Ovo je u skladu sa Kroničar metodom: fronts + grim portents (situacije u pokretu), secrets & clues (činjenice koje se mogu otkriti, apstraktne od izvora), strong starts (situacije za ubaciti). Ništa se ne smatra "stvarnim" dok se ne desi za stolom.

## Folderi
- `party/` — igrači i njihovi PC-jevi, lične motivacije i kuke (po jedan fajl po liku).
- `organization/` — vlastita organizacija party-ja u Sharnu (tretira se kao frakcija kojom oni upravljaju).
- `npcs/` — NPC-jevi koje je party upoznao ili koji su bitni za sto (odnos, stanje); razlikuje se od knjiškog rostera u `settings/`.
- `factions/` — velike sile kao **fronts** (goal + tri grim portents + napredak + odnos prema party-ju). Motor situacija u pokretu.
- `situations/` — banka potencijalnih situacija (NE priča). Iz nje se sklapaju sesije.
- `log/` — sažeci odigranih sesija / timeline, za kontinuitet.
- `world/` — player-facing canon o cijelom Khorvaireu (998 YK) koji igrači imaju, plus DM sistematizacija. Nadograđuje 3.5 Sharn knjigu na sadašnje stanje.
- `threads.md` — živa lista otvorenih niti/questova/plotova (potencijal, ne razriješeno).

## Tok do gotove sesije
`situations/` + `party/` + `factions/` → primijeni **Kroničar metodu** (`method/03_method/kronicar_method.md`, DIO F) povlačeći sadržaj iz `settings/sharn/03_master/` → gotova sesija u **`output/sharn/`**.

## Pravila pisanja (kao svuda)
Bosanski tekst, imena i mehanički termini na engleskom. `[PLAYER]`/`[DM]` oznake. Pravilo provjere: Sharn činjenice iz izvora; izmišljeno za sto označi `[HOMEBREW]`.
