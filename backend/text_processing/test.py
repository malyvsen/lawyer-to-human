from pprint import PrettyPrinter
from text_processing.analysis import analysis
from text_processing.document import Document
from text_processing.sentence import Sentence
from text_processing.word import Word


def test_doc(text=None):
    result = Document.from_text(test_text if text is None else text)

    current_doc = result
    while current_doc is not None:
        print(str(current_doc))
        print()
        current_doc = current_doc.summary

    return result


def test_analysis(text=None):
    result = analysis(test_text if text is None else text)
    printer = PrettyPrinter()
    printer.pprint(result)
    return result


test_text = '''﻿Informacja dla pracowników zawierająca obowiązujące normy prawne dotyczące równego traktowania w zatrudnieniu

Artykuł Kodeksu pracy
Treść normy
Art. 9 § 4 
Postanowienia układów zbiorowych pracy i innych opartych na ustawie porozumień zbiorowych, regulaminów oraz statutów określających prawa i obowiązki stron stosunku pracy, naruszające zasadę równego traktowania w zatrudnieniu, nie obowiązują.
Art. 112
Pracownicy mają równe prawa z tytułu jednakowego wypełniania takich samych obowiązków; dotyczy to w szczególności równego traktowania mężczyzn i kobiet w zatrudnieniu.
Art. 113
Jakakolwiek dyskryminacja w zatrudnieniu, bezpośrednia lub pośrednia, w szczególności ze względu na płeć, wiek, niepełnosprawność, rasę, religię, narodowość, przekonania polityczne, przynależność związkową, pochodzenie etniczne, wyznanie, orientację seksualną, a także ze względu na zatrudnienie na czas określony lub nieokreślony albo w pełnym lub w niepełnym wymiarze czasu pracy - jest niedopuszczalna.
Art. 18 § 3
Postanowienia umów o pracę i innych aktów, na podstawie których powstaje stosunek pracy, naruszające zasadę równego traktowania w zatrudnieniu są nieważne. Zamiast takich postanowień stosuje się odpowiednie przepisy prawa pracy, a w razie braku takich przepisów - postanowienia te należy zastąpić odpowiednimi postanowieniami niemającymi charakteru dyskryminacyjnego. 
Art. 183a
§ 1. Pracownicy powinni być równo traktowani w zakresie nawiązania i rozwiązania stosunku pracy, warunków zatrudnienia, awansowania oraz dostępu do szkolenia w celu podnoszenia kwalifikacji zawodowych, w szczególności bez względu na płeć, wiek, niepełnosprawność, rasę, religię, narodowość, przekonania polityczne, przynależność związkową, pochodzenie etniczne, wyznanie, orientację seksualną, a także bez względu na zatrudnienie na czas określony lub nieokreślony albo w pełnym lub w niepełnym wymiarze czasu pracy.
§ 2. Równe traktowanie w zatrudnieniu oznacza niedyskryminowanie w jakikolwiek sposób, bezpośrednio lub pośrednio, z przyczyn określonych w § 1.
§ 3. Dyskryminowanie bezpośrednie istnieje wtedy, gdy pracownik z jednej lub z kilku przyczyn określonych w § 1 był, jest lub mógłby być traktowany w porównywalnej sytuacji mniej korzystnie niż inni pracownicy.
§ 4. Dyskryminowanie pośrednie istnieje wtedy, gdy na skutek pozornie neutralnego postanowienia, zastosowanego kryterium lub podjętego działania występują lub mogłyby wystąpić niekorzystne dysproporcje albo szczególnie niekorzystna sytuacja w zakresie nawiązania i rozwiązania stosunku pracy, warunków zatrudnienia, awansowania oraz dostępu do szkolenia w celu podnoszenia kwalifikacji zawodowych wobec wszystkich lub znacznej liczby pracowników należących do grupy wyróżnionej ze względu na jedną lub kilka przyczyn określonych w § 1, chyba że postanowienie, kryterium lub działanie jest obiektywnie uzasadnione ze względu na zgodny z prawem cel, który ma być osiągnięty, a środki służące osiągnięciu tego celu są właściwe i konieczne.
§ 5. Przejawem dyskryminowania w rozumieniu § 2 jest także:
1) działanie polegające na zachęcaniu innej osoby do naruszenia zasady równego traktowania w zatrudnieniu lub nakazaniu jej naruszenia tej zasady,
2) niepożądane zachowanie, którego celem lub skutkiem jest naruszenie godności pracownika i stworzenie wobec niego zastraszającej, wrogiej, poniżającej, upokarzającej lub uwłaczającej atmosfery (molestowanie).
§ 6. Dyskryminowaniem ze względu na płeć jest także każde niepożądane zachowanie o charakterze seksualnym lub odnoszące się do płci pracownika, którego celem lub skutkiem jest naruszenie godności pracownika, w szczególności stworzenie wobec niego zastraszającej, wrogiej, poniżającej, upokarzającej lub uwłaczającej atmosfery; na zachowanie to mogą się składać fizyczne, werbalne lub pozawerbalne elementy (molestowanie seksualne).
§ 7. Podporządkowanie się przez pracownika molestowaniu lub molestowaniu seksualnemu, a także podjęcie przez niego działań przeciwstawiających się molestowaniu lub molestowaniu seksualnemu nie może powodować jakichkolwiek negatywnych konsekwencji wobec pracownika.
Art. 183b
§ 1. Za naruszenie zasady równego traktowania w zatrudnieniu, z zastrzeżeniem § 2-4, uważa się różnicowanie przez pracodawcę sytuacji pracownika z jednej lub kilku przyczyn określonych w art. 183a § 1, którego skutkiem jest w szczególności:
1) odmowa nawiązania lub rozwiązanie stosunku pracy,
2) niekorzystne ukształtowanie wynagrodzenia za pracę lub innych warunków zatrudnienia albo pominięcie przy awansowaniu lub przyznawaniu innych świadczeń związanych z pracą,
3) pominięcie przy typowaniu do udziału w szkoleniach podnoszących kwalifikacje zawodowe
- chyba że pracodawca udowodni, że kierował się obiektywnymi powodami.
§ 2. Zasady równego traktowania w zatrudnieniu nie naruszają działania, proporcjonalne do osiągnięcia zgodnego z prawem celu różnicowania sytuacji pracownika, polegające na:
1) niezatrudnianiu pracownika z jednej lub kilku przyczyn określonych w art. 183a § 1, jeżeli rodzaj pracy lub warunki jej wykonywania powodują, że przyczyna lub przyczyny wymienione w tym przepisie są rzeczywistym i decydującym wymaganiem zawodowym stawianym pracownikowi,
2) wypowiedzeniu pracownikowi warunków zatrudnienia w zakresie wymiaru czasu pracy, jeżeli jest to uzasadnione przyczynami niedotyczącymi pracowników bez powoływania się na inną przyczynę lub inne przyczyny wymienione w art. 183a § 1,
3) stosowaniu środków, które różnicują sytuację prawną pracownika, ze względu na ochronę rodzicielstwa lub niepełnosprawność,
4) stosowaniu kryterium stażu pracy przy ustalaniu warunków zatrudniania i zwalniania pracowników, zasad wynagradzania i awansowania oraz dostępu do szkolenia w celu podnoszenia kwalifikacji zawodowych, co uzasadnia odmienne traktowanie pracowników ze względu na wiek.
§ 3. Nie stanowią naruszenia zasady równego traktowania w zatrudnieniu działania podejmowane przez określony czas, zmierzające do wyrównywania szans wszystkich lub znacznej liczby pracowników wyróżnionych z jednej lub kilku przyczyn określonych w art. 183a § 1, przez zmniejszenie na korzyść takich pracowników faktycznych nierówności, w zakresie określonym w tym przepisie.
§ 4.  Nie stanowi naruszenia zasady równego traktowania ograniczanie przez kościoły i inne związki wyznaniowe, a także organizacje, których etyka opiera się na religii, wyznaniu lub światopoglądzie, dostępu do zatrudnienia, ze względu na religię, wyznanie lub światopogląd jeżeli rodzaj lub charakter wykonywania działalności przez kościoły i inne związki wyznaniowe, a także organizacje powoduje, że religia, wyznanie lub światopogląd są rzeczywistym i decydującym wymaganiem zawodowym stawianym pracownikowi, proporcjonalnym do osiągnięcia zgodnego z prawem celu zróżnicowania sytuacji tej osoby; dotyczy to również wymagania od zatrudnionych działania w dobrej wierze i lojalności wobec etyki kościoła, innego związku wyznaniowego oraz organizacji, których etyka opiera się na religii, wyznaniu lub światopoglądzie.
Art. 183c
§ 1. Pracownicy mają prawo do jednakowego wynagrodzenia za jednakową pracę lub za pracę o jednakowej wartości.
§ 2. Wynagrodzenie, o którym mowa w § 1, obejmuje wszystkie składniki wynagrodzenia, bez względu na ich nazwę i charakter, a także inne świadczenia związane z pracą, przyznawane pracownikom w formie pieniężnej lub w innej formie niż pieniężna.
§ 3. Pracami o jednakowej wartości są prace, których wykonywanie wymaga od pracowników porównywalnych kwalifikacji zawodowych, potwierdzonych dokumentami przewidzianymi w odrębnych przepisach lub praktyką i doświadczeniem zawodowym, a także porównywalnej odpowiedzialności i wysiłku.
Art. 183d
Osoba, wobec której pracodawca naruszył zasadę równego traktowania w zatrudnieniu, ma prawo do odszkodowania w wysokości nie niższej niż minimalne wynagrodzenie za pracę, ustalane na podstawie odrębnych przepisów.
Art. 183e
§ 1. Skorzystanie przez pracownika z uprawnień przysługujących z tytułu naruszenia zasady równego traktowania w zatrudnieniu nie może być podstawą niekorzystnego traktowania pracownika, a także nie może powodować jakichkolwiek negatywnych konsekwencji wobec pracownika, zwłaszcza nie może stanowić przyczyny uzasadniającej wypowiedzenie przez pracodawcę stosunku pracy lub jego rozwiązanie bez wypowiedzenia.
§ 2. Przepis § 1 stosuje się odpowiednio do pracownika, który udzielił w jakiejkolwiek formie wsparcia pracownikowi korzystającemu z uprawnień przysługujących z tytułu naruszenia zasady równego traktowania w zatrudnieniu.
Art. 292
§ 1. Zawarcie z pracownikiem umowy o pracę przewidującej zatrudnienie w niepełnym wymiarze czasu pracy nie może powodować ustalenia jego warunków pracy i płacy w sposób mniej korzystny w stosunku do pracowników wykonujących taką samą lub podobną pracę w pełnym wymiarze czasu pracy, z uwzględnieniem jednak proporcjonalności wynagrodzenia za pracę i innych świadczeń związanych z pracą, do wymiaru czasu pracy pracownika.
§ 2. Pracodawca powinien, w miarę możliwości, uwzględnić wniosek pracownika dotyczący zmiany wymiaru czasu pracy określonego w umowie o pracę.
Art. 94 
pkt 2b
Pracodawca jest obowiązany w szczególności:
przeciwdziałać dyskryminacji w zatrudnieniu, w szczególności ze względu na płeć, wiek, niepełnosprawność, rasę, religię, narodowość, przekonania polityczne, przynależność związkową, pochodzenie etniczne, wyznanie, orientację seksualną, a także ze względu na zatrudnienie na czas określony lub nieokreślony albo w pełnym lub w niepełnym wymiarze czasu pracy.
Art. 943
§ 1. Pracodawca jest obowiązany przeciwdziałać mobbingowi.
§ 2. Mobbing oznacza działania lub zachowania dotyczące pracownika lub skierowane przeciwko pracownikowi, polegające na uporczywym i długotrwałym nękaniu lub zastraszaniu pracownika, wywołujące u niego zaniżoną ocenę przydatności zawodowej, powodujące lub mające na celu poniżenie lub ośmieszenie pracownika, izolowanie go lub wyeliminowanie z zespołu współpracowników.
§ 3. Pracownik, u którego mobbing wywołał rozstrój zdrowia, może dochodzić od pracodawcy odpowiedniej sumy tytułem zadośćuczynienia pieniężnego za doznaną krzywdę.
§ 4. Pracownik, który wskutek mobbingu rozwiązał umowę o pracę, ma prawo dochodzić od pracodawcy odszkodowania w wysokości nie niższej niż minimalne wynagrodzenie za pracę, ustalane na podstawie odrębnych przepisów.
§ 5. Oświadczenie pracownika o rozwiązaniu umowy o pracę powinno nastąpić na piśmie z podaniem przyczyny, o której mowa w § 2, uzasadniającej rozwiązanie umowy.
'''
