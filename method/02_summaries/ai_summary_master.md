<!-- IZVOR: Acquisitions Incorporated (WotC 2019), cijela knjiga | konsolidovani sažetak | sintetizira ai_summary_00..09 -->
# Acquisitions Incorporated — master sažetak cijele knjige

Konsolidovani pregled cijele knjige, kao osnova za izradu pravila za "agencije" igrača. Detalji su u `ai_summary_00` do `ai_summary_09`. Sistem je **[D&D 5e]**; setting je Forgotten Realms. Za nas: strukturu i koncepte uzeti gotovo doslovno, mehaniku (DC, spellove, attunement, novac) prevesti na našu igru (D&D 3.5 / Eberron / Sharn), homebrew označiti [HOMEBREW].

## Šta knjiga radi
Pretvara avanturašku družinu u **organizaciju (franšizu)** koja raste paralelno s likovima. Družina dobije teritoriju, sjedište, osoblje i svaki igrač uzme **company position** (poslovnu ulogu) s posebnim sposobnostima i magičnim predmetima. Tako organizacija postaje stalni motor priče i "četvrti stub" igre uz exploration, social, combat. Ton je uredska komedija, ali skelet pravila radi i bez šale.

## Struktura knjige (i gdje je u sažecima)
- **Ch1** (`ai_summary_00`): koncept, osnivači/lore, Fast Franchise Generator (random tabele za brzo stvaranje).
- **Ch2** — srž pravila:
  - `ai_summary_01`: Rank, teritorija, osoblje, headquarters feature, troškovi.
  - `ai_summary_02` + `ai_summary_03`: osam company pozicija.
  - `ai_summary_04`: franchise tasks i downtime.
- **Ch3** — player options:
  - `ai_summary_05` + `ai_summary_06`: backgrounds i savjeti po klasi (flavor, bez mehanike).
  - `ai_summary_07`: nova rasa Verdan, novi spellovi (+ Royalty Component), Factions and Rivals.
- **Ch4 + App A** (`ai_summary_08`): avantura Orrery (uvod), Acq Inc NPC-evi, House Dran.
- **App B-E** (`ai_summary_09`): monsters, Iconic Faction/Franchise Features, vozila, Orrery, trinketi.

## Skelet sistema organizacije (jezgro za naša pravila)

### 1. Rank i napredak
Četiri ranka, jedan po tieru (DM može vezati za priču). Svaki rank diže: teritoriju, broj osoblja, broj istovremenih taskova, dostupne HQ feature, i multiplikator troška.

| Rank | Nivoi | Teritorija | Osoblje (kumulativno novo) | Tasks | HQ kategorije (nove) | Trošak × |
|------|-------|-----------|----------------------------|-------|----------------------|----------|
| 1 | 1-4 | Settlement (~10 mi) | Majordomo, 2 untrained, 1 skilled | 1 | Starter HQ | ×1 |
| 2 | 5-10 | Small territory (~50 mi) | +4 untrained, +1 skilled, +10 crew | 2 | cosmetic, expansion, transportation, weapon | ×1.5 |
| 3 | 11-16 | Large territory | +8 untrained, +2 skilled, +10 crew | 3 | arcane, defensive, franchise choice | ×3 |
| 4 | 17-20 | Limited extraplanar | +16 untrained, +4 skilled, +20 crew | 4 | arcane, franchise choice, secret | ×5 |

Pravilo tona: **sve odluke o organizaciji donose svi igrači ravnopravno** (Group Dynamic).

### 2. Osoblje
Plate uključene u mjesečni trošak; proficiency bonus = **2 + rank**.
- **Majordomo** (vodi sjedište, jedini NPC koji smije uzeti poziciju), **untrained** ("subemployees"), **skilled** ("interns", mogu pratiti družinu ili raditi taskove), **crew** (pokreću/održavaju mobilni HQ).

### 3. Headquarters
Starter HQ → nadograđuje se po tieru: cosmetic, expansion, transportation (~30 mi/dan po ranku, uz slabost), weapon (siege), arcane, defensive (šteta 10/rank, DC 12+rank), franchise choice, secret (DC 25). Lifestyle u HQ-u besplatan: poor→wealthy po ranku.

### 4. Troškovi
Mjesečno = **baseline × rank multiplikator**, modifikovano "Running a Franchise" taskom. Baseline od 15 gp (kola) do 12.000 gp (palata). Default: dug +15% kazne; dvije rate zaredom = posljedice u priči.

### 5. Company positions (osam uloga — najjači dio za sto)
Svaki lik mora uzeti tačno jednu. Daju proficiency, opremu, feature po ranku, i magični predmet (attunement van limita, vezan za lika, vlasništvo organizacije).
- **Cartographer** (rute/mape/vozila; Tale of Safe Travel)
- **Decisionist** (vođa, ekstra glas; Coin of Decisionry)
- **Documancer** (ugovori/dokumenti; Documancy Satchel, scrollovi)
- **Hoardsperson** (blago/resursi; Living Loot Satchel)
- **Loremonger** (znanje; Whisper Jar; **-20% troška** na r3)
- **Obviator** (uklanja prepreke/proučava neprijatelje; Read the Opposition)
- **Occultant** (ubistva/karma; occultant abacus)
- **Secretarian** (ljudi/kupci/marketing; Sending Stone)

### 6. Franchise tasks i downtime
Osoblje radi poslove u pozadini (research, crafting, social, kriminal, marketing). Limit = rank. Provjere baca igrač. Razbija se na scene; komplikacije i rivali kao adventure seeds.

### 7. Rivali (motor priče)
Pet fakcija + alat za brzo pravljenje: **Iconic Faction Features** i **Iconic Franchise Features** (modularni add-on na bilo koji statblock). Tipovi rivala: korporativni (Dran Enterprises), tajne ubice (Noble Knife), idealisti bez profita (Silver Sliver), osvetnička kosmička prijetnja (The Six).

### 8. Tematske začine
- **Royalty Component** (`ai_summary_07`): brendirani spellovi koji pri kastanju pune kasu firme (~1 gp/slot level). Odlično za organizaciju baziranu na novcu.
- Fast Franchise Generator (`ai_summary_00`): random tabele za brzo stvaranje naše i rivalskih agencija.

## ⚠ Rupe u izvornom .md
1. **Detaljni write-upi 10 franchise/downtime aktivnosti NEDOSTAJU** (Ch2 kraj, .md linije 1309-1318 daju samo nazive). Posebno fali **Running a Franchise** (određuje mjesečni modifikator troška). Vidi `ai_summary_04`.
2. Puni statblockovi/opisi nisu ekstrahovani za: rasu **Verdan**, sedam novih spellova, App B čudovišta, App C vozila, App D Orrery komponente, App E trinkete. Imena/efekti uglavnom poznati, ali za egzaktne brojeve treba ponovo izvući stranice iz PDF-a (`_tools/.venv/bin/python _tools/extract.py`).

## Plan za sljedeći korak (pravila za igrače)
Uzeti skelet (rank → teritorija → osoblje → HQ → troškovi → 8 pozicija → taskovi → rivali), prevesti flavor i magične predmete u Eberron/Sharn (House Sivis za sending/ugovore, House Cannith za constructe, Dragonmarked houses/Boromar/Daask/Aurum kao rivali, changeling rival po uzoru na Portentiu), prilagoditi mehaniku našem sistemu. Prije finalizacije popuniti rupu #1 (aktivnosti) iz PDF-a.
