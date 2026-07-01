# Template za situaciju

> Logička struktura koju svaka situacija treba da zadovolji da bih mogao reći "spremna je za vođenje". Ovo nije forma priče nego kontrolna lista sastojaka: priču prave igrači za stolom, ja pripremam materijal iz kojeg priča može nastati. Template dolazi od GM-a (nije iz source booka) i služi i kao olakšica za pripremu i kao stvar na koju se mogu osloniti kad moram nešto izmisliti u letu. Vremenom se dopunjava.

Situacija može biti velika (više lokacija, više NPC-jeva, splet beatova) ili sasvim mala (jedan susret na ulici). Struktura je uvijek ista, samo se skalira. Velika situacija popuni svaku rubriku bogato, mala svaku svede na rečenicu ili dvije. Nijedna rubrika ne smije ostati prazna: ako za neku nemam ništa, situacija još nije spremna.

## 1. Razlog ili tema
Svaka situacija postoji radi nečega. Da li je to shoping, backstory momenat nekog lika, čista zabava, pritisak frakcije, prilika za zaradu. Situacija bez određenog smjera je zapravo samo šum koji neće uraditi ništa osim zbuniti igrače.
- Jedna rečenica: zašto ova situacija postoji i šta donosi kampanji.
- Jedna rečenica: šta ostaje iza nje kad prođe (novi kontakt, otvorena lokacija, dug, neprijatelj, informacija, predmet).

## 2. Lokacije
Svaka situacija ima jednu ili više lokacija. Svaka lokacija treba imati svoju temu i svoj luna park:
- **Tema:** vizuelni identitet i osjećaj mjesta (zvuk, miris, svjetlo), po [[Fantasy City Creation Method]].
- **Luna park:** bar jedna aktivnost koju igrači tu mogu raditi. Ako je lokacija prvenstveno RP mjesto (razgovori, pregovori), treba više od jedne aktivnosti, da se zabave i igrači kojima ta RP scena nije fokus.
- Lokacija za višekratnu upotrebu dobije svoju `loc_` notu u `campaign/<setting>/locations/`, a situacija je samo linkuje. Usputna mjesta (raskrsnica, most, uličica) ostaju u fajlu situacije, ali i njima dam bar jednu stvar koja se tu može raditi.

## 3. Story beats
Svaka situacija ima svoje story beatove, momente koji guraju radnju.
- **Glavni story beat** je vezan za plot situacije i progresira radnju dalje. To je kičma situacije: ono što se dešava i oko čega se svi vrte.
- Glavni beat **mora imati više mogućnosti za kraj**, u zavisnosti kako se situacija odvije. Igrači ne moraju uvijek uspjeti u svojim namjerama, pa se pripremam za više ishoda: uspjeh, neuspjeh, djelimičan uspjeh, i bar jedno treće nešto (igrači stanu na stranu koju nisam očekivao, prodaju informaciju, odu). Nijedan kraj nije propisan; ovo su pripremljene mogućnosti, ne scenarij.
- **Sporedni beatovi** dolaze uglavnom od NPC-jeva (vidi dolje) i od samog mjesta. Pale se i gase po potrebi.

## 4. NPC-jevi
Svaka situacija treba da ima neke NPC-jeve sa kojima je moguće interaktovati.
- **Svaki NPC**, i najsitniji, ima svoj kratak opis (kako izgleda i zvuči, da se može odglumiti i docarati igračima), svoj **want** (šta hoće u ovoj situaciji, razlog zašto nešto radi) i svoj **need** (šta mu zapravo treba; često to ni sam ne zna).
- **Bitni NPC-jevi** uz to imaju svoje story beatove: razrađen slijed djelovanja. Šta radi prvo, šta kad naiđe na otpor, dokle je spreman ići, kad odustaje.
- NPC beatovi se **izvode iz njegovog want-a i need-a**, ne obratno. Prvo znam šta hoće i šta mu treba, pa iz toga slijedi kako se ponaša i koje su mu dalje akcije. Svaki NPC ima want, ali samo bitni dobiju razrađenu strukturu djelovanja.
- NPC koji će se vraćati dobije karticu u `campaign/<setting>/npcs/`, a situacija je linkuje.

## Skeleton (copy-paste)

```
# <Ime situacije>

- Tip: (strong start / encounter / secret / faction move / reaction)
- Obim: mala | srednja | velika
- Nivo: ...
- Vezano za: [[...]]

## Razlog ili tema
## Kuka  [PLAYER]
## Lokacije  (svaka: tema + luna park)
## NPC-jevi  (svaki: opis + want + need; bitni: story beats iz want-a)
## Story beats
### Glavni beat  (više mogućih krajeva)
### Sporedni beatovi
## Reakcije svijeta
## Šta ostaje iza situacije
```

## Checklist prije nego proglasim situaciju spremnom
- [ ] Razlog ili temu znam reći u jednoj rečenici.
- [ ] Svaka lokacija ima temu i bar jednu aktivnost (RP lokacija više od jedne).
- [ ] Glavni story beat ima bar tri moguća kraja (uspjeh, neuspjeh, treće nešto).
- [ ] Svaki NPC ima opis, want i need.
- [ ] Bitni NPC-jevi imaju story beatove izvedene iz svog want-a i need-a.
- [ ] Ništa nije propisan ishod; igrači prave priču.

## Veze
- [[Fantasy City Creation Method]] (teme i atrakcije lokacija)
- [[kronicar_method]] (širi proces pripreme)
- `campaign/<setting>/situations/README.md` (brzi format za sitna sjemena; ovaj template je za situacije koje dobiju svoj fajl)
- Prvi primjer po ovom template-u: [[sit_the_last_lot]]
