

# Pravila agencije (Sharn)

Ovo je kompletan sistem za vođenje vlastite inquisitive (detektivske) agencije u Sharnu. Sistem je D&D 5e. Ton je grounded noir, ne uredska komedija. Sve je objašnjeno do kraja: ako nešto nije napisano, ne podrazumijeva se. Oznaka [HOMEBREW] znači da to ne postoji u izvornoj knjizi (Acquisitions Incorporated) nego smo sami napravili za ovu kampanju.

Imena (ljudi, mjesta, kuće, predmeti, vještine, mehanika) ostaju na engleskom. Objašnjenja su na bosanskom.

Povezani fajlovi: koncept i pozadina agencije su u `agencija.md`; sažeci izvora su u `method/02_summaries/ai_summary_00..09` i `ai_summary_master`; sile i situacije se vode u `factions/` i `situations/`.

---

## 0. Kako čitati ovaj dokument i osnovni pojmovi

- **Agencija** je organizacija kojom party upravlja zajedno. Sve odluke o agenciji (zapošljavanje, nadogradnje, koji slučaj uzeti, kako potrošiti novac) donose svi igrači ravnopravno, i u igri i za stolom. Kad se igrači ne slože, to je dio igre (vidi ulogu Lead Investigator za mehaniku razrješenja).
- **Tier (rang agencije)** je nivo razvoja agencije, od 1 do 4. Tier diže gotovo sve: doseg po gradu, broj osoblja, dostupne nadogradnje ureda, skalu slučajeva i mjesečni trošak. Tier se ne kupuje novcem; raste kroz reputaciju i priču (vidi §1 i §2).
- **Standing** je opisno ime trenutnog tiera (npr. tier 1 = "Nova agencija").
- **Reputacija** se vodi kroz pet odvojenih frakcijskih tragova (vidi §2). Reputacija je gorivo koje vodi ka novom tieru.
- **Uloga (position)** je posao koji lik obavlja unutar agencije (vidi §4). Svaki lik bira tačno jednu ulogu. Uloga je nezavisna od klase i backgrounda.
- **Osoblje (staff)** su NPC zaposleni agencije (vidi §3).
- **Slučaj (case)** je posao koji agencija prima od klijenta; to je glavni izvor prihoda (vidi §7).
- **Provjera (check)** uvijek znači standardnu 5e ability check, attack roll ili saving throw. Kad piše "DC 15 Investigation", to je Intelligence (Investigation) provjera protiv Difficulty Class 15.
- Kad piše "1/dan" misli se "jednom dnevno, ponovo dostupno u zoru (dawn)". "1/long rest" znači obnavlja se nakon long resta. "1/7 dana" znači ponovo dostupno tek u zoru sedmog dana.

---

## 1. Tieri agencije (rang i napredak)

Agencija ima četiri tiera. Tabela ispod pokazuje šta svaki tier donosi. Brojevi osoblja su **kumulativni dodaci** (na svaki novi tier dobijaš to osoblje povrh starog). Mjesečni trošak je objašnjen u §6.


| Tier | Standing          | Doseg (vidi §5)                           | Novo osoblje (vidi §3)                        | Nadogradnje ureda (vidi §5/§8)          | Case-task slotova (§7.5) | Mjesečni trošak (§6) |
| ---- | ----------------- | ----------------------------------------- | --------------------------------------------- | --------------------------------------- | ------------------------ | -------------------- |
| 1    | Nova agencija     | Dura (Underlook i okolina)                | office manager, 2 runnera, 1 specijalist      | starter ured                            | 1                        | 120 gp               |
| 2    | Poznato ime       | jedna cijela četvrt + Lower City          | +4 runnera, +1 specijalist, mreža informanata | cosmetic, expansion, mobility, security | 2                        | 180 gp               |
| 3    | Ugledna agencija  | veći dio Sharna + Central Plateau         | +8 runnera, +2 specijalista                   | arcane, defensive, slobodni izbor       | 3                        | 360 gp               |
| 4    | Institucija grada | cijeli Sharn, Skyway, Cogs, prekogranično | +16 runnera, +4 specijalista                  | arcane, slobodni izbor, secret          | 4                        | 600 gp               |


**Kako se diže tier (story milestone uz reputaciju).** Tier se ne diže automatski na nivou likova. DM ga diže na narativnom trenutku (kraj velikog slučaja, riješen sukob s rivalom, javni uspjeh) kad je agencija skupila dovoljno reputacije. Reputacija je uslov, milestone je okidač. Konkretni prag (smjernica za DM-a, [HOMEBREW]):

- **Tier 1 → 2:** najmanje **dva** reputacijska traga na +2 ("Poznati") ili više, plus jedan zaokružen slučaj koji je agenciju javno etablirao.
- **Tier 2 → 3:** najmanje **tri** traga na +3 ("Cijenjeni"), ili bilo koji jedan trag na +5 ("Saveznik"), plus milestone (npr. slučaj koji je dotakao jednu od velikih sila grada).
- **Tier 3 → 4:** većina tragova visoko (tri ili više na +4), agencija je priznata sila u gradu, plus veliki narativni preokret (npr. slučaj koji mijenja odnos snaga u Sharnu).

DM smije dignuti ili spustiti ove pragove ako priča to traži. Tier se može i **pasti** ako agencija doživi javni skandal ili niz neuspjeha (vidi §6 default i §2).

**Šta se dešava na novom tieru.** Kad agencija pređe u novi tier: (1) dobija novo osoblje iz tabele; (2) svaka uloga lika napreduje na rang novog tiera i dobija nove sposobnosti i predmete (vidi §4); (3) otvaraju se nove kategorije nadogradnji ureda (vidi §8); (4) raste doseg (§5); (5) mijenja se mjesečni trošak (§6); (6) postaju dostupni veći slučajevi (§7).

---

## 2. Reputacija (pet frakcijskih tragova)

Reputacija se ne vodi kao jedan broj nego kao **pet odvojenih tragova**, jer u Sharnu rad za jedne ljudi ljuti druge. Svaki trag je ljestvica od **−3 do +5**.

**Pet tragova:**

1. **Sharn Watch** (gradska straža i zakon). Diže se kad agencija pomaže pravdi, predaje krivce, sarađuje s Watchom. Pada kad agencija krije dokaze, štiti kriminalce, sramoti Watch.
2. **[[house-tharashk|House Tharashk]] (Finders' Guild)** (dominira inquisitive zanatom preko Mark of Finding). Diže se kad agencija poštuje guildu, dijeli zasluge, prihvata njihove standarde. Pada kad im preotima poslove i klijente ili javno pokaže da je bolja.
3. **Podzemlje** ([[boromar-vs-daask|Boromar Clan]], [[boromar-vs-daask|Daask]], [[house-tarkanan|House Tarkanan]], Tyrants, sitni kriminal). Diže se kad agencija ćuti, "izgubi" dokaze, radi usluge ili ostaje neutralna. Pada kad ruši kriminalne poslove i predaje ljude Watchu.
4. **Obična klijentela** (radnici, trgovci, Lower i Middle City). Diže se kad agencija pošteno radi za male ljude, naplaćuje razumno, štiti slabe. Pada kad iznevjeri klijenta ili radi samo za bogate.
5. **Elita / Upper & Skyway** (plemstvo, bogati trgovci, gornje kule). Diže se diskrecijom, riješenim osjetljivim slučajevima, vezama. Pada kad agencija pravi skandal među bogatima ili djeluje "ispod njihovog nivoa".

**Šta znače brojevi (bandovi):**


| Vrijednost | Band           | Šta znači                                                           |
| ---------- | -------------- | ------------------------------------------------------------------- |
| +5         | Saveznik       | Frakcija aktivno pomaže agenciji, daje slučajeve, prešuti probleme. |
| +3 do +4   | Cijenjeni      | Agenciju poštuju; lakši pristup, bolje cijene, sitne usluge.        |
| +1 do +2   | Poznati        | Znaju za vas i misle pozitivno; otvaraju se vrata.                  |
| 0          | Neutralni      | Ne znaju vas ili im je svejedno. Svi tragovi kreću od 0.            |
| −1 do −2   | Na lošem glasu | Sumnjičavi su; otežavaju posao, dižu cijene, šire glasine.          |
| −3         | Neprijatelj    | Aktivno rade protiv agencije (vidi §9).                             |


**Kako se tragovi pomjeraju.** Pomjera ih DM, najčešće za **±1** po značajnom događaju ili zaokruženom slučaju. Veliki, javni ishod može pomjeriti za **±2**. Pravilo nije automatsko; DM gleda fikciju. Jedan slučaj često diže jedan trag i spušta drugi (npr. predaš ubicu Watchu: Watch +1, Podzemlje −1). Vidi §7.4 za reputacijski ishod slučaja.

**Veza s tierom.** Pragovi za napredak tiera su u §1. Reputacija je jedini "resurs" koji vodi rast; novac ne kupuje tier.

**Početno stanje (start kampanje).** Svi tragovi su na 0, osim po DM odluci. Kragzov orden ("zlatni bodež") i veteranska prošlost mogu opravdati Watch na **+1**, ali i njegov framovani otkaz može to poništiti; DM odlučuje na Session 0.

---

## 3. Osoblje (staff)

Agencija ima NPC zaposlene. **Plate su uključene u mjesečni trošak** (§6), ne plaćaju se odvojeno. Svaki član osoblja ima **proficiency bonus = 2 + tier agencije** (tj. +3 na tieru 1, +4 na tieru 2, +5 na tieru 3, +6 na tieru 4). Na svaki novi tier staro osoblje se može otpustiti i zamijeniti novim po potrebi.

Vrste osoblja:

### 3.1 Office Manager (jedan, od tiera 1)

Vodi ured i svakodnevicu agencije. Rijetko izlazi na teren. Proficient je u Persuasion plus dvije vještine po izboru DM-a. DM mu treba dati ime, ličnost i pozadinu (on je stalni NPC za stolom). Office manager vodi finansije i plaća mjesečni trošak ako ima novca (vidi §6).

- **Posebno pravilo:** office manager smije zauzeti jednu **ulogu** (§4) ako party želi popuniti ulogu koju niko od likova ne uzima. On je jedini NPC koji smije imati ulogu. Nijedan drugi NPC ne može.

### 3.2 Runneri / pisari (untrained hirelings)

Opšti rad: trčanje poruka, nošenje, čišćenje, sitna legwork potraga, čuvanje ureda. **Ne bore se** i **ne idu u avanture s partyjem.** Mogu raditi case-taskove (§7.5) niskog rizika. DM imenuje bar jednog vođu grupe i daje grupi zajednički karakter (npr. "banda bivših vojnika", "djeca iz iste četvrti"). Tier 1 daje 2, tier 2 dodaje 4 (ukupno 6), tier 3 dodaje 8 (ukupno 14), tier 4 dodaje 16 (ukupno 30).

### 3.3 Specijalisti (skilled hirelings)

Imaju jednu ili više proficiency (vještina, oružje ili alat). Party opisuje koncept specijaliste i bira po jednu proficiency za svakog; DM ih dorađuje. Specijalisti mogu:

- **Pratiti party na teren:** najviše **jedan** specijalista po terenu, CR otprilike pola tiera agencije (CR 1/2 na tieru 1, CR 1 na tieru 2, itd.). DM odlučuje da li ostaje lojalan po situaciji.
- **Raditi case-taskove** (§7.5).
Specijalista radi samo jednu stvar u datom trenutku. Tier 1 daje 1, tier 2 dodaje 1 (ukupno 2), tier 3 dodaje 2 (ukupno 4), tier 4 dodaje 4 (ukupno 8).

### 3.4 Mreža informanata (od tiera 2) [HOMEBREW reskin]

Na tieru 2 agencija razvija mrežu imenovanih informanata po wardovima Sharna (zamjena za Acq Inc "crew", koji je služio mobilnoj bazi koja nama ne treba). Informanti su "oči i uši" agencije: ne bore se, rijetko izlaze iz svog kraja, ali daju glasine i osmatranje. Mehanički, mreža:

- omogućava **Word on the Street** i slične sposobnosti uloge Liaison (§4.4) da rade šire i pouzdanije;
- daje DM-u izvor da partyju "procuri" trag između sesija;
- može se koristiti kao case-task "Upit informantu" (§7.5).
DM imenuje 3 do 5 informanata s ličnošću i krajem koji pokrivaju. Mreža raste s tierom (širi se na nove četvrti kako raste doseg).

---

## 4. Uloge (positions)

Svaki lik bira **tačno jednu** ulogu i ne može je mijenjati osim uz veliki narativni razlog (DM odluka). Uloga daje: (a) **proficiency** (vještine ili alat), (b) **position proficiency** (poseban bonus kad lik radi specifične poslove svoje uloge: lik dodaje svoj proficiency bonus na te provjere), (c) **sposobnosti po tieru**, i (d) **liniju predmeta** koja raste po tieru. Sposobnosti i predmeti svake uloge su navedeni unutar te uloge; opšta pravila za predmete su odmah ispod, a low-magic varijanta je u §8.5.

**Opšta pravila predmeta uloge.** Predmeti koje uloga daje su vlasništvo agencije. Traže attunement, ali se **NE broje** u limit od tri attuned predmeta. Vezani su samo za lika kojem su dati; ne rade za druge i vraćaju se agenciji ako lik ode. Ovi predmeti dižu moć likova (high-magic). Ako DM želi low-magic igru, koristi **low-magic toggle** (§8.5): svaki predmet zamijeni masterwork mundanim alatom (advantage na pripadajuću provjeru) ili sposobnošću 1/dan.

**Rang uloge = tier agencije.** Kad agencija pređe u novi tier, svaka uloga lika napreduje na taj rang i dobija sposobnosti i predmete navedene za taj tier.

Postoji osam uloga. Igrači biraju koje uzimaju (ne moraju sve biti popunjene; nepopunjenu korisnu ulogu može uzeti office manager, §3.1). Slijedi šta svaka radi i kako radi.

---

### 4.1 Lead Investigator

**Šta radi.** Vodi agenciju i slučajeve, dodjeljuje zadatke, drži moral, i razrješava kad se party ne slaže. Lice agencije prema klijentima i vlastima.
**Proficiency.** Bira jednu: Persuasion, Intimidation ili Insight.
**Position proficiency.** Dodaje proficiency bonus na provjere da utiče na grupnu odluku, procijeni popularnost neke osobe ili običaja, ili digne moral osoblja.
**Predmet.** *Command Token* (veliki metalni žeton sa znakom agencije; flavor po izboru, npr. orden "zlatni bodež").

- **Tier 1, Final Say.** Kad agencija glasa o nekoj odluci, predočiš *Command Token* i tvoj glas vrijedi **dvostruko**.
- **Tier 2.** *Token* postaje common magic item. (a) **Absentee Ballot:** ako je član party-ja odsutan, ti odlučuješ kako bi on glasao i dobijaš njegov glas; ako se glasalo dok si ti bio odsutan, smiješ tražiti ponovno brojanje i dodati svoja dva glasa. (b) **Read the Room:** kad neko u krugu 10 ft donosi odluku ili baca žeton, kao bonus action možeš suptilno navesti ishod; ta osoba primjećuje manipulaciju samo uspješnom DC 13 Insight provjerom.
- **Tier 3.** (a) **Better Odds:** kao action, "pitaš" *Token* o konkretnom planu i uz uspješnu DC 15 Arcana provjeru saznaš koja je od dvije opcije primjerenija; 1/dan. (b) **Inspired Decision:** kad ozbiljna agencijska odluka prođe onako kako si glasao, održiš kratak govor (DC 15 Persuasion); na uspjeh svaki član agencije po izboru koji te čuje dobija advantage na sljedeću provjeru, napad ili saving throw u narednom satu; 1/long rest.
- **Tier 4.** (a) **Tri glasa:** predočiš *Token* da dobiješ treći glas pri glasanju; 1/7 dana. (b) **Clandestine Kit:** *Token*-komplet krije ekstradimenzionalni prostor za jedan tool kit (bonus action ubaciš/izvadiš; pretres ga nalazi tek DC 20 Investigation/Perception) i može kastati *charm person* (save DC 15) 1/dan.

---

### 4.2 Archivist

**Šta radi.** Vodi sve zapise agencije, istražuje lore, historiju i presedane, identifikuje ljude i činjenice, veza je s Morgrave University i bibliotekama.
**Proficiency.** Bira jednu: artisan's tools (jedna vrsta), navigator's tools, vehicles (land) ili vehicles (water). Dobija odgovarajući komplet plus mastilo i pero.
**Position proficiency.** Dodaje proficiency bonus na provjere da analizira rad agencije, procijeni historijske zapise ili dešifruje kodove.
**Predmet.** *Record Stone* (glasoviti spis u stilu House Sivis: snima i reprodukuje govor bez ograničenja kapaciteta).

- **Tier 1, Record Stone.** Common magic item. Snima tuđe iskaze i tvoja zapažanja brzinom govora i reprodukuje ih istom brzinom. Pokretanje reprodukcije je action.
- **Tier 2.** (a) **Need to Know:** kao action izabereš jednog humanoida kojeg vidiš i baciš DC 15 Investigation; na uspjeh saznaš: njegovo ime, do tri aliasa korištena u zadnjih mjesec dana, glavnu profesiju i njegove skill proficiencies; 1/long rest, najviše jednom po istom biću. (b) **Archive Query:** kao bonus action pitaš *Record Stone* o nekoj temi i baciš DC 15 History; na uspjeh ti reprodukuje snimak o toj temi koji je negdje, nekad napravio drugi archivist; 1/dan.
- **Tier 3.** (a) **Best Practices:** tvoje poznavanje najbolje prakse smanjuje **mjesečni trošak agencije za 20%** (§6). Uz to, jedna soba u uredu postaje tvoja i dobija jednu cosmetic feature, a ured dobija jednu secret feature povrh redovnih. (b) **Warning Index:** *Record Stone* može raditi kao *wand of enemy detection*; 1/dan.
- **Tier 4.** (a) **Efficient Upgrades:** ured dobija jednu security/weapon feature i jednu cosmetic feature povrh redovnih. (b) **Deep Archive:** šapneš ime jednog od ovih spellova u *Record Stone* da ga kastaš: *detect evil and good*, *detect magic*, *detect poison and disease*, *find traps*, *identify*, *locate animals or plants*; 1/dan.

---

### 4.3 Forensic Artificer

**Šta radi.** Pregleda dokaze, identifikuje supstance, otrove i magični trag, čita metode protivnika, pravi sitne naprave (House Cannith flavor).
**Proficiency.** Tinker's tools ili alchemist's supplies (po izboru; dobija komplet).
**Position proficiency.** Dodaje proficiency bonus na provjere da pročita taktiku neprijatelja, uoči skrivenu prijetnju ili zastraši protivnika čije je slabosti ranije procijenio (vidi Read the Opposition).
**Predmet.** *Investigator's Lenses* (naočale/monokl/lupa) i, kasnije, *Field Kit*.

- **Tier 1, Read the Opposition.** Kao bonus action izabereš biće koje vidiš i baciš DC 15 Insight; na uspjeh saznaš tri detalja po izboru o tom biću (npr. ciljevi, bonds, ideali, mane, borbena taktika, finansije, lokacija jazbine, saveznici, neprijatelji); 1/long rest, najviše jednom po istom biću.
- **Tier 2.** (a) **Substance Analysis:** kao action svojim alatom identifikuješ bilo koju nepoznatu supstancu (uključujući alhemijske predmete, napitke i druge magične supstance); 1/long rest. (b) **Investigator's Lenses:** uncommon magic item; kao bonus action učiniš da rade kao *eyes of minute seeing* ili *eyes of the eagle* (biraš; izbor se ne mijenja do sljedeće zore).
- **Tier 3.** (a) **Advanced Preparations:** postaviš sebi jedno pitanje i baciš DC 15 History; na uspjeh se "prisjetiš" informacije koju si mogao istražiti o slučaju ranije (može biti jasna, nejasna ili u obliku zagonetke, DM bira); 1/long rest. (b) **Field Kit:** dobiješ *Travel Alchemical Kit* (minijaturni alchemist's supplies + poisoner's kit; dobijaš proficiency s poisoner's kit). Koristiš ga bez vađenja; pri pretresu se nalazi tek DC 20 Investigation/Insight.
- **Tier 4.** (a) **Enhanced Lenses:** rare; rade kao *oboje* (eyes of the eagle i eyes of minute seeing). Uz to, fokusiraš leće za advantage na jedan weapon attack (bez akcije); ako pogodiš, baciš jednu dodatnu weapon damage kockicu; 1/dan. (b) **Obviate:** kad koristiš Read the Opposition i promašiš provjeru, ipak saznaš jedan detalj (DM bira); i smiješ koristiti Read the Opposition više puta na isto biće, ali nakon toga ne možeš ponovo na to biće do long resta.

---

### 4.4 Liaison / Front of House

**Šta radi.** Prima klijente, vodi javnu sliku agencije, gradi reputaciju i brending, upravlja informantima, zapošljava.
**Proficiency.** Bira jednu: gaming set, musical instrument ili disguise kit (dobija odgovarajući komplet).
**Position proficiency.** Dodaje proficiency bonus na provjere da uvjeri sumnjičavu gomilu u dobre namjere, požuri osoblje/informante, ili smisli slogan/legendu.
**Predmet.** *Sending Stone* (u stilu House Sivis) i, kasnije, *Contact File*.

- **Tier 1, Sending Stone.** Uncommon magic item. Radi kao sending stone, ali nema par; omogućava kontakt s uredom agencije, poznatim liaison kontaktima i najbližim kontaktom u mreži. Za uspostavu veze baciš DC 15 Arcana; 1/dan.
- **Tier 2.** (a) **Contact File:** uncommon; kad nekog prvi put sretneš, njegovi podaci i gruba skica se magično upišu na karticu; pristup kartici je bonus action; ima i neiscrpnu zalihu brošura agencije. (b) **Word on the Street:** kad agencija počne veliki slučaj, baciš DC 15 History; na uspjeh saznaš do tri glasine o ljudima ili organizacijama uključenim u slučaj (preko mreže informanata).
- **Tier 3.** (a) **Calling Cards:** kad nekom daš karticu iz *Contact File*, ta osoba te može kontaktirati kao da je kastala *sending*; kartica gubi moć nakon 7 dana, najviše pet aktivnih kartica; ti možeš kastati *sending* svakome ko ima tvoju karticu, 1/7 dana. (b) **Vetted Rumors:** kad koristiš Word on the Street, DM ti kaže koji su dijelovi glasine netačni (ne nužno i istinu iza njih).
- **Tier 4.** (a) **Always Hiring:** kao action u naseljenom kraju baciš DC 15 Persuasion da nađeš NPC koji odmah pruža neku uslugu za standardnu cijenu; na uspjeh ti informacija o kandidatu dođe nekim zgodnim putem; taj najam se plaća odvojeno (nije u mjesečnom trošku); 1/long rest. (b) **Charming Introduction:** kad daš humanoidu karticu iz *Contact File*, možeš na njega kastati *charm person* (save DC 15); spell se prekida ako izgubi karticu.

---

### 4.5 Tracker

**Šta radi.** Osmatranje i praćenje, rute kroz vertikalni lavirint Sharna, prevoz (skycoach, lightning rail, liftovi), mape grada i okoline.
**Proficiency.** Cartographer's tools plus vehicles (land) ili vehicles (water) po izboru. Dobija cartographer's supplies, map case, spyglass i bojene tinte.
**Position proficiency.** Dodaje proficiency bonus na provjere da pravi ili čita mape, traži puteve, ili procijeni rutu na opasnost.
**Predmet.** *Spyglass* (kasnije *Spyglass of Clairvoyance*) i *Map Case*.

- **Tier 1, Requisition Transit.** Na početku zadatka možeš rekvirirati skroman prevoz (skycoach prolaz, jahaće životinje, kola); štetu ili gubitak agencija plaća.
- **Tier 2.** (a) *Spyglass of Clairvoyance:* common; kao action gledaš u tačku do 1 milje koja ti zaklanja pogled (kula, brijeg) i uz DC 15 Wisdom provjeru cartographer's tools mapiraš prirodni teren u krugu 3 milje oko te tačke (samo teren, ne bića/strukture); 1/dan. (b) **Safe Route:** ritual od 45 minuta s cartographer's tools i 50 gp komponenti; ti i do šest bića s opremom putujete kroz Border Ethereal do poznate lokacije dohvatljive za jedan dan; po DM odluci putnici mogu dobiti short ili long rest.
- **Tier 3.** (a) **Shortcut Map:** kao action baciš DC 15 Perception; na uspjeh nađeš mapu prečice koja prepolovi vrijeme putovanja; ako uspiješ za 5+, dobiješ i advantage na sljedeću provjeru putovanja kroz to područje u narednom satu; 1/long rest. (b) **Lead Map:** kao action baciš DC 15 Perception i nađeš mapu vezanu za trenutni slučaj ili koja inspiriše novi; 1/7 dana.
- **Tier 4.** (a) **Master Atlas:** uncommon; advantage na Intelligence ili Wisdom provjere vezane za geografiju i lokacije. (b) **Greater Safe Route:** Safe Route sad pokriva do tri dana puta i može uključiti veliku imovinu (do 2.000 lb tereta).

---

### 4.6 Notary

**Šta radi.** Ugovori, registracija, pravni dokumenti, kodovi; brine da je sve pravno obavezujuće (House Sivis flavor).
**Proficiency.** Calligrapher's supplies (dobija komplet, ledger, sealing wax, pečat ograničenog ovlaštenja, scroll case).
**Position proficiency.** Dodaje proficiency bonus na provjere da organizuje lore, analizira službene ili arkane dokumente, ili iznese pravno obavezujući stav.
**Predmet.** *Document Satchel* (kasnije s funkcijama holdinga i humidora).

- **Tier 1, Gift of Words.** Tečno vladaš jezikom dokumenata: advantage na Intelligence provjere za dešifrovanje kodova i sličnih skripti; DM ti smije davati hintove za zagonetke i tragove koji uključuju pisanje.
- **Tier 2.** (a) *Document Satchel:* common; magično šalje i prima dokumente preko Sivis message stanice i proizvodi gotove standardne ugovore na zahtjev. (b) **Read the Client:** kastaš *augury* s omenima iz perspektive klijenta ili poslodavca; 1/7 dana.
- **Tier 3.** (a) **Satchel of Holding:** uncommon; jedan pretinac radi kao *bag of holding*; uz to izvučeš *spell scroll* of *comprehend languages* (nestaje kad se iskoristi ili nakon 10 minuta); 1/dan. (b) **Forgery Kit:** dobiješ proficiency s forgery kit, koji je uvijek u satchelu.
- **Tier 4.** (a) **Scroll Humidor:** rare; ekstradimenzionalni prostor drži do 30 dokumenata ili *spell scrolls* (ubacivanje je action, vađenje bonus action). (b) **Scroll Service:** kao action zatražiš *spell scroll* spella do 3. nivoa; uz DC 15 Arcana se pojavi u satchelu, samo ti ga koristiš (nestaje nakon upotrebe ili 10 minuta); na uspjeh 1/7 dana, na promašaj 1/dan.

---

### 4.7 Bursar

**Šta radi.** Vodi novac agencije, evidence lockup (pohrana dokaza), nabavku opreme i procjenu vrijednosti (House Kundarak flavor za sef).
**Proficiency.** Jeweler's tools (dobija komplet i ledger), plus do 5 gp sitne opreme za skladištenje.
**Position proficiency.** Dodaje proficiency bonus na provjere da se cjenka za robu i usluge, procijeni kvalitet opreme i blaga, ili analizira lokalne resurse.
**Predmet.** *Evidence Satchel* (kasnije sa secret chest i portable hole kapacitetom).

- **Tier 1, What a Deal.** Iskoristiš mrežu dobavljača da kupiš jedan predmet s tabela Mounts and Vehicles ili Trade Goods (PHB ch.5) i dostaviš ga u ured za jedan dan; uz DC 15 Persuasion ispregovaraš 50% popusta. Na promašaj ne možeš ponovo do long resta; nakon dva uspjeha ne možeš ponovo do sljedećeg tiera.
- **Tier 2.** (a) *Evidence Satchel:* uncommon; radi kao *bag of holding* povezan sa sigurnim sefom (Kundarak); kao action prebaciš bilo koju količinu sredstava agencije nazad u satchel uz DC 15 Sleight of Hand. (b) **Comfortable Means:** održavaš wealthy lifestyle besplatno.
- **Tier 3.** (a) **Vault Link:** satchel radi kao replika sanduka za *Leomund's secret chest* (rare); spell ne može isteći. (b) **That Thing You Need:** kao bonus action baciš DC 15 Sleight of Hand i izvučeš predmet s Adventuring Gear tabele (PHB ch.5) vrijednosti do 15 gp i koji stane u sanduk; nakon pet pokušaja izvlačenja ne možeš više do sljedeće zore.
- **Tier 4.** (a) **Deep Vault:** sanduk dobija kapacitet *portable hole* (prečnik 6 ft, dubina 10 ft). (b) **Expensive Thing:** That Thing You Need sad izvlači predmet do 250 gp.

---

### 4.8 Coroner

**Šta radi.** Pregleda mrtve, utvrđuje uzrok i "vrijednost" smrti za agenciju, čita omene oko toga ko treba živjeti ili umrijeti (mrtvozornik; Aureon/Blood of Vol flavor).
**Proficiency.** Bira jednu: cook's utensils, leatherworker's tools ili weaver's tools (ili reskin "embalmer's tools" uz DM dozvolu). Dobija komplet, merchant's scale, pet vodootpornih torbica i *occultant abacus* ("brojanica" s perlama u obliku lobanja).
**Position proficiency.** Dodaje proficiency bonus na provjere da zastraši biće blizu smrti, utvrdi koja je bolest ili otrov ubio biće, ili objasni odakle to tijelo.
**Predmet.** *Occultant Abacus* ("brojanica").

- **Tier 1, Read the Kill.** Tokom 1 minute proučiš biće koje je neko iz agencije ubio u zadnja 24 sata i daš ubici jednu **d10**; ubica je može dodati na jedan attack roll, ability check ili saving throw u narednom satu; 1/long rest. Ako nije jasno ko je zadao smrtni udarac, biraš nasumično.
- **Tier 2.** (a) **Death's Ledger:** brojanica postaje uncommon; držeći je u 5 ft od bića ubijenog u zadnja 24 sata, kastaš *augury* (pitanje ne mora biti vezano za leš); 1/dan. (b) **Bring Out Your Dead:** Read the Kill se obnavlja i na short rest.
- **Tier 3.** (a) **Bead of Instant Karma:** rare; kao reakciju ciljaš biće koje vidiš a koje će baciti ability check, attack roll ili saving throw i daješ mu advantage ili disadvantage; perla se obnavlja u zoru. (b) **Death's Omen:** kao bonus action izabereš ranjeno biće koje vidiš i baciš DC 15 Insight; na uspjeh saznaš da li bi njegova trenutna smrt imala neutralne, negativne ili pozitivne posljedice za tebe i agenciju (ako se razlikuje, saznaš oboje).
- **Tier 4.** (a) **Bead of Diverted Karma:** very rare; kad neko biće koje vidiš baca s disadvantage, kao reakciju daješ jednu **d10** drugom biću koje vidiš (dodaje je na bilo koji roll u narednoj minuti); perla se obnavlja u zoru. (b) **Correct the Balance:** unutar 7 dana od nečije smrti, kao action baciš DC 15 Religion da otkriješ kako poništiti ili ublažiti posljedice te smrti; na uspjeh 1/7 dana, na promašaj 1/dan.

---

## 5. Doseg po Sharnu (teritorija)

Doseg određuje gdje agencija ima kontakte, kredibilitet i pristup slučajevima. Sharn je vertikalan grad kula, podijeljen na četvrti (Dura, Tavick's Landing, Menthis Plateau, Central Plateau, Northedge, Cliffside) plus Skyway (leteći distrikt elite) i the Cogs (industrijska utroba). Svaka četvrt ima Upper, Middle i Lower nivo.

- **Tier 1, Dura.** Agencija djeluje u Duri (baza Underlook u Middle Duri, plus Lower Dura gdje je sirotište) i neposrednoj okolini. Ovdje imaju kontakte i poznaju teren.
- **Tier 2, jedna četvrt + Lower City.** Doseg se širi na cijelu jednu susjednu četvrt i na Lower City nivoe kroz više kula. Mreža informanata (§3.4) pokriva te krajeve.
- **Tier 3, veći dio Sharna.** Doseg pokriva većinu grada, uključujući Central Plateau (vlast, sudovi) i Middle wardove širom grada. Povremen pristup Skywayu.
- **Tier 4, cijeli Sharn i dalje.** Doseg pokriva cijeli grad, Skyway elitu, dubine Cogsa, i slučajeve van Sharna (prekogranično preko Khorvairea, čak i planarne tragove preko Tharashk dragonshard ruta).

**Efekat dosega (kako radi).** Slučajevi i klijenti izvan trenutnog dosega su teži ili nedostupni: agencija nema lokalne kontakte ni kredibilitet, pa DM nameće disadvantage na socijalne i istražne provjere u tom kraju, više troškove (bez lokalnih informanata sve se plaća), ili trvenje s lokalnim silama (npr. Watch ili Tharashk koji vas tamo ne poznaju). Agencija smije fizički otići bilo gdje; doseg govori gdje radi kao priznata agencija, ne gdje smije kročiti.

---

## 6. Ekonomija (mjesečni trošak i finansije)

### 6.1 Mjesečni trošak

Svaki mjesec agencija plaća trošak iz tabele u §1: **120 gp (tier 1), 180 gp (tier 2), 360 gp (tier 3), 600 gp (tier 4).** Taj iznos pokriva kiriju ureda u Underlooku, plate cijelog osoblja, operativne troškove i licencne takse. (Brojevi su Acq Inc baseline za "settlement enterprise" 120 gp pomnožen rank multiplikatorom 1 / 1.5 / 3 / 5.)

Modifikatori mjesečnog troška:

- Ako je aktivna **Archivist Best Practices** (§4.2, tier 3), trošak je **−20%**.
- Određene nadogradnje ureda ili reputacijski bandovi mogu po DM odluci sniziti ili dignuti trošak (npr. odlična reputacija kod Obične klijentele donosi sitne poslove koji pokrivaju dio režije).

### 6.2 "Vođenje agencije" mjesečni test [HOMEBREW]

Jednom mjesečno agencija radi jedan management test koji predstavlja kako je tekao mjesec. (Ovo zamjenjuje Acq Inc aktivnost "Running a Franchise", čiji detaljan opis nedostaje u izvoru, vidi `ai_summary_04`.) Test baca office manager ili lik koji nadgleda finansije, koristeći prikladnu vještinu (najčešće Persuasion, Investigation ili relevantan tool), **DC 15**. Ishod mijenja trošak tog mjeseca:


| Rezultat        | Efekat na trošak tog mjeseca                             |
| --------------- | -------------------------------------------------------- |
| Uspjeh za 10+   | −25% (efikasan mjesec, sitni poslovi pokrili dio režije) |
| Uspjeh          | trošak kako je naveden                                   |
| Promašaj        | +25% (prekoračenja, mito, popravke)                      |
| Promašaj za 10+ | +50% i jedna komplikacija (DM uvodi problem ili rivala)  |


### 6.3 Odakle dolazi novac

Glavni prihod su **slučajevi** (§7). Sporedni prihodi: sitni poslovi mreže informanata, usluge (npr. Bursar What a Deal), i povremeni reputacijski bonusi. Ako agenciji ponestane novca, to je znak da je vrijeme za novi slučaj.

### 6.4 Default (neplaćanje) i posljedice

Ako agencija ne može platiti mjesečni trošak, dug prelazi u sljedeći mjesec uz **+15% kazne**. Promašaj jedne rate je upozorenje. **Dvije rate zaredom** pokreću eskalaciju u priči: prijetnja deložacijom iz Underlooka, dolaze utjerivači duga, ili jedna od sila grada (najvjerovatnije House Tharashk ili neki zajmodavac) nudi "pomoć" sa skrivenom cijenom i agendom. Trajni neuspjeh može oboriti tier (§1).

**Napomena za start kampanje:** party je na startu nezavisan i bez vanjskog pritiska (sve su dobili herojstvom s vozom). Default posljedice koje uključuju sile grada DM uvodi tek kako pritisak prirodno raste kroz igru, ne odmah.

---

## 7. Slučaj (case framework)

Slučaj je osnovna jedinica posla i glavni prihod agencije. Svaki slučaj prolazi kroz iste faze.

### 7.1 Intake (prijem)

Klijent dolazi s problemom. Agencija dogovara **opseg posla**, **retainer (avans)** koji se plaća odmah, i **honorar (fee)** koji se plaća po uspješnom završetku. Retainer je standardno **25% honorara** i ne vraća se, čak i ako slučaj propadne. Intake je prilika za RP (procjena klijenta, sumnja, cjenkanje).

### 7.2 Skala honorara

Honorar zavisi od veličine slučaja i klijenta. Dostupnost veće skale je vezana za tier i doseg (§5) i za reputaciju kod relevantne klijentele (§2).


| Skala slučaja    | Primjeri                                              | Honorar (raspon)   | Tipično dostupno od |
| ---------------- | ----------------------------------------------------- | ------------------ | ------------------- |
| Sitni            | izgubljen predmet, nevjeran supružnik, sitna prevara  | 25 do 75 gp        | tier 1              |
| Standardni       | krađa, nestala osoba, prevara, ucjena                 | 100 do 400 gp      | tier 1 do 2         |
| Veliki           | ubistvo, zavjera, frakcijska intriga                  | 500 do 2.000 gp    | tier 2 do 3         |
| Gradski/planarni | slučaj koji dira velike sile, prekogranično, planarno | 2.500 do 10.000 gp | tier 3 do 4         |


DM bira tačan iznos unutar raspona prema riziku, klijentu i reputaciji (bolja reputacija kod date klijentele znači viši kraj raspona).

### 7.3 Troškovi i komplikacije

Tokom slučaja agencija sama plaća **troškove** (mito, prevoz, oprema, plaćanje informanata). DM ih drži razumnim. Svaki slučaj može povući **komplikaciju** ili **rivala** (vidi §9): neko gleda, neko se umiješa, ili se otkrije veza s većom silom. Komplikacije su sjeme za nove situacije; idu u `situations/`.

### 7.4 Ishod i reputacija

Na kraju slučaja DM određuje ishod i pomjera reputacijske tragove (§2):

- **Uspjeh:** relevantni trag +1 (ili +2 za veliki, javni uspjeh).
- **Neuspjeh ili skandal:** relevantni trag −1.
- **Sukob interesa:** jedan trag +1, drugi −1 (npr. zadovoljiš Watch, naljutiš Podzemlje).
DM bira koje tragove slučaj dira na osnovu toga za koga je rađen i kako je riješen.

### 7.5 Case-taskovi (lagani downtime) [HOMEBREW]

Dok party radi na slučaju (između ili tokom sesija), osoblje i uloge mogu paralelno raditi pozadinske zadatke. Broj **istovremenih** case-taskova je ograničen tierom (1 / 2 / 3 / 4, vidi §1). Svaki task zauzme dodijeljeno osoblje dok ne završi i traje obično jedan radni dan (8 sati). Provjeru uvijek baca igrač (svojim modifikatorom ili modifikatorom osoblja). Meni (ovo je namjerno lagan sloj, bez pune ekonomije zadataka):


| Task                      | Provjera                             | Ishod na uspjeh                            | Ishod na promašaj                                |
| ------------------------- | ------------------------------------ | ------------------------------------------ | ------------------------------------------------ |
| Osmatranje (surveillance) | Stealth ili Perception, DC 13        | dnevnik kretanja mete, 1 korisno zapažanje | ništa, ili meta primijeti pratnju (komplikacija) |
| Canvass terena            | Persuasion ili Investigation, DC 13  | 1 trag ili svjedok                         | ništa, ili lažni trag                            |
| Arhivska istraga          | Investigation ili History, DC 15     | 1 činjenica ili presedan                   | ništa                                            |
| Upit informantu           | Persuasion, DC 12 (+ sitno plaćanje) | 1 glasina (pouzdanost varira)              | dezinformacija, ili informant traži uslugu       |
| Lab analiza               | tool check, DC 15                    | identifikovana supstanca ili dokaz         | nejasan rezultat                                 |


DM smije dodati nove taskove po istom obrascu (jedna provjera, jedan jasan ishod).

---

## 8. Ured u Underlooku (HQ) i nadogradnje

Starter ured (tier 1) je skroman prostor u Underlooku (Middle Dura): prijemna soba, jedna do dvije radne sobe, mali arhiv. DM i igrači zajedno crtaju tlocrt. Na svaki tier od 2 naviše otključavaju se kategorije nadogradnji (vidi tabelu u §1). Svaku nadogradnju biraju igrači zajedno s DM-om. Sve nadogradnje su uključene u mjesečni trošak (ne plaćaju se posebno), osim ako DM odluči da neka skupa nadogradnja digne baseline (§6).

### 8.1 Kategorije i kad se otključavaju

- **Tier 2:** cosmetic, expansion, mobility, security (biraš onoliko koliko ti tier daje; po Acq Inc obrascu, jedna po kategoriji).
- **Tier 3:** arcane, defensive, plus jedan slobodan izbor iz nižih kategorija (ili pojačanje postojeće).
- **Tier 4:** arcane, plus jedan slobodan izbor, plus secret.

### 8.2 Primjeri nadogradnji (s konkretnim efektom)

- **Cosmetic / branding:** dotjeran ured, prepoznatljiv znak, izložene zasluge. Efekat je situacijski i ograničen (npr. impresionira klijenta jednom), DM presuđuje; može dignuti reputaciju kod date klijentele ili sniziti trošak nekih taskova.
- **Expansion (proširenje):** udvostruči prostor (nova soba, sprat ili podrum). Omogućava smještaj više osoblja i novih nadogradnji.
- **Mobility (transit aranžman) [HOMEBREW reskin]:** stalni dogovor za brz prevoz (rezervisani skycoach, veza na lightning rail stanici, privatni lift). Smanjuje vrijeme kretanja po gradu i daje advantage na provjere bijega ili hitnog dolaska, 1/dan.
- **Security (zaštita) [HOMEBREW reskin za "weapon"]:** brave, zamke, čuvani ulaz, sigurna soba. Daje konkretan odbrambeni efekat na ured: nametne uljezu jedan efekat (npr. alarm, zaključavanje, otrovna brava) sa save DC **12 + tier**, ili šteta najviše **10 po tieru** jednom cilju (5 za AoE).
- **Arcane:** jedinstvena magična crta ureda (npr. liku se omogući da iz ureda kasta jedan spell do 6. nivoa 1/dan; ili stalni glas-poruka sistem; ili soba za ispitivanje s detect-efektom). DM odobrava.
- **Defensive:** poveća izdržljivost ureda ili doda zaštitni efekat (npr. dva efekta iz *guards and wards*). Štetni efekti ograničeni kao kod Security.
- **Secret (tajna):** crta koju primijeti tek DC **25** Investigation/Perception (npr. tajni izlaz koji garantuje bijeg; tajna soba-laboratorija; skriveni sef koji čuva dokaze i zalihe).

### 8.3 Tipične detektivske sobe (preporučeni izbori)

Arhiv (bonus na Archivist taskove), forenzički lab (bonus na Forensic taskove i Lab analizu), soba za ispitivanje (advantage na Intimidation/Insight pri ispitivanju u uredu), sigurna kuća (skrovište van baze), sending stanica (pouzdaniji Sending Stone), osmatračnica, tajni izlaz. DM dodjeljuje konkretan mehanički efekat svakoj po obrascu iznad.

### 8.4 Mobilni ured (opcija)

Acq Inc dozvoljava mobilnu bazu (brod, kip koji hoda, voz). Za ovu kampanju to **nije** default (baza je fiksni ured u Underlooku). Ako kasnije poželite mobilnu opciju (npr. agencijski skycoach kao pokretni ured), DM je tretira kao posebnu transportation nadogradnju s vlastitom slabošću; pravilo je tu, ali se ne koristi dok ne zatreba.

### 8.5 Low-magic toggle (za predmete uloga i magične nadogradnje)

Magični predmeti uloga i arcane nadogradnje dižu ukupnu moć (high-magic). Ako DM vodi low-magic igru: svaki predmet uloge zamijeni ili (a) masterwork mundanim alatom koji daje **advantage** na pripadajuću provjeru, ili (b) sposobnošću **1/dan** bez predmeta. Arcane nadogradnje ureda se izostave ili svedu na 1/dan efekt. Ovako mehanika uloga i dalje radi, ali bez gomilanja magičnih predmeta.

---

## 9. Rivali i pritisak

Sukob s rivalima je motor priče. Konkretne situacije i frontovi (ciljevi, koraci) vode se u `factions/` i `situations/` po pravilu "situacije, ne priče"; ovdje je samo mehanički okvir.

### 9.1 Iconic Faction Features (brzi rivali)

Da bilo koji statblock postane prepoznatljiv pripadnik neke sile, dodaj mu jednu ili više "iconic features" (sve sa save DC **13**; vidi `ai_summary_09` za originale). Reskin za našu kampanju:

- **House Tharashk operativac:** *Corporate Focus* (advantage vs charm i u Wis/Cha nadmetanjima), *Freeze Assets* (1/dan paraliza na 1 rundu), *Hostile Takeover* (1/dan reakcija: preusmjeri tuđi napad na drugu metu).
- **[[corrupt-watch|korumpirani Watch]]:** koristi *Noble Knife* set kao "iskusni gradski ubica/agent" (Noble Strike = frightened; Ready to Fight = advantage vs surprised; Reality Slip = reakcija: pomjeri se i napadni).
- **Boromar / Daask mišić:** *The Six* set ili obični thug/bandit captain s jednom feature (npr. *Something Feels Off*: 1/dan disadvantage na napad na njega).
- **[[the-pilfered-wand|The Pilfered Wand]] (Kragzov nemesis):** vođa Vikari (zakya rakshasa) dobija pun set + svoje rakshasa sposobnosti; niži članovi po jedna feature.

### 9.2 Iconic Position Features (rivalske agencije)

Rivalska agencija ima svoje uloge. Dodaj NPC-u brzu borbenu verziju uloge (sve save DC 13): npr. rivalski **Forensic** (Read the Opposition: meta dobija advantage napadača do kraja svoje runde), rivalski **Liaison** (Charming Introduction: vizitka kao *charm person*), itd. (Vidi `ai_summary_09` za listu.)

### 9.3 Kako pritisak raste

Na startu agencija nema vanjskog pritiska. Kako reputacija raste i slučajevi diraju velike sile, pritisak se pojavljuje prirodno: Tharashk vidi konkurenta, Watch ovisno o saradnji postaje saveznik ili prepreka, Podzemlje pamti ko im je rušio poslove. Default (§6.4) i reputacijski tragovi (§2) su poluge kojima DM uvodi taj pritisak.

---

## 10. Session 0: kako pojednostaviti (toggle lista)

Pun sistem je gore. Ako želite lakšu verziju za sto, isključite ili svedite po želji:

- **Reputacija:** umjesto pet tragova, vodite jedan opšti skor "Reputacija agencije" (−3 do +5).
- **Case-taskovi (§7.5):** izostavite ih; sav posao se dešava za stolom.
- **Mjesečni test (§6.2):** izostavite; plaćajte fiksni mjesečni trošak bez varijacije.
- **Doseg (§5):** tretirajte kao flavor, bez mehaničkih penala.
- **Predmeti uloga (§4):** koristite low-magic toggle (§8.5).
- **Ekonomija:** ako ne želite bookkeeping, pređite na "uzmi slučaj kad treba novac" bez praćenja mjesečnih rata.
Sve ostalo (uloge, osoblje, tieri, ured) radi i u skraćenoj verziji.

---

## 11. Napomene i poznate rupe u izvoru

- Mehanika je preuzeta iz Acquisitions Incorporated (D&D 5e) i prilagođena Sharnu/Eberronu. Imena predmeta i flavor su reskinovani; brojevi i efekti su zadržani osim gdje piše [HOMEBREW].
- **Detaljni opisi Acq Inc downtime/franchise aktivnosti nedostaju u izvoru** (vidi `ai_summary_04`). Zato su "Vođenje agencije" (§6.2) i case-taskovi (§7.5) napisani kao [HOMEBREW].
- Puni statblockovi rivala (rakshasa, faction NPC-evi) i magičnih predmeta nisu ovdje; izvuci ih iz Monster Manuala / Eberron knjiga ili PDF-a po potrebi.
- Promjene balansa rješavamo na Session 0 i kroz igru. Ovo je živi dokument; ažurira se kako kampanja raste.

