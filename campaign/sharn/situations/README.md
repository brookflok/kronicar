# situations/: banka potencijalnih situacija (NE priča)

Srce ovog sloja. Ovdje stoje **situacije koje se mogu desiti**, modularno i kratko, spremne da se ubace gdje ima smisla. Nije zaplet, nije scenarij sa ishodom. Iz ove banke (+ `party/` + `factions/`) sklapam gotove sesije u `output/sharn/`.

Svaka situacija je mala, apstraktna od toga GDJE/KAKO će se javiti, i ima jasnu kuku. Ne odlučujem kako će se završiti, to rade igrači.

## Tipovi situacija (slobodno miješaj)
- **Strong-start seeds**: događaj koji može otvoriti scenu/sesiju (uokviren + kuka + blizu akcije). Npr. "Tijelo pada s tornja u Clifftopu, u ruci stišće amulet sa Daask oznakom."
- **Floating secrets & clues**: kratke činjenice koje se MOGU otkriti (10-ak), apstraktne od izvora.
- **Faction moves**: potencijalni grim portent neke sile (povezano sa `factions/`).
- **Reactions**: "ako party uradi X, svijet reaguje Y" (živi svijet iz metode).
- **Encounter seeds**: situacije vezane za Sharn lokaciju (povuci aspekte iz settings mastera).

## Brzi format za sjemena (`_seeds.md` i sitnice)
```
## <Kratko ime situacije>
- Tip: (strong start / secret / faction move / reaction / encounter)
- Kuka: (jedna rečenica)
- Vezano za: (district / frakcija / NPC / PC nit, reference)
- Aspekti / sastojci: (par tagova, ne pasusi)
- [DM] šta je istina ispod: (opciono, tajna; bez propisanog ishoda)
```

## Puni template za situacije sa svojim fajlom
Svaka situacija koja dobije svoj fajl (`sit_*.md`, `case_*.md`) slijedi [[situation_template]]
(method/03_method/situation_template.md): razlog ili tema, lokacije sa temom i luna parkom,
story beats sa više mogućih krajeva, i NPC-jevi sa opisom, want-om i need-om (bitni dobiju
svoje beatove izvedene iz want-a). Tamo je i copy-paste skeleton i checklist.

## Status
U banci: tri uvodna noir slučaja ([[case_the_cold_key]], [[case_forget_the_cogs]],
[[case_glass_seance]]) plus [[case_the_kept_word]], [[case_the_dezina_consignment]],
[[case_the_reclaimers]] i splet ([[_braid]], [[_braid_dhakaan]]); sjemena u [[_seeds]];
samostalne situacije: [[sit_the_last_lot]].
