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


test_text = 'W ostatnich latach wiele firm zaczęło wdrażać narzędzia AI (Artificial Intelligence), ale zwykle są to projekty o małej skali, np. wirtualni asystenci. Te pierwsze doświadczenia pozwalają na zaznajomienie się z technologią AI i zdobycie podstawowej wiedzy o dostępnych narzędziach, ich możliwościach i ograniczeniach. „Dlatego w najbliższych latach można oczekiwać wzrostu liczby dużych wdrożeń aplikacji wykorzystujących mechanizmy AI” – uważa Nima Negahban, CTO w firmie Kinetica specjalizującej się w opracowywaniu systemów analitycznych o wysokiej wydajności. Potencjał technologii AI i uczenia maszynowego w zestawieniu z aktualnymi warunkami jest niestety przereklamowany, a większość firm ma problemy z określeniem realnych korzyści biznesowych, które można osiągnąć, inwestując w te technologie. Największe bariery popularyzacji to brak doświadczeń i wiedzy, jak efektywnie wdrożyć narzędzia wykorzystujące AI, a także brak przekonania, że zasoby danych zgromadzone w firmie mają wysoką wiarygodność i jakość. Stąd też sceptyczne podejście do projektów związanych z wprowadzeniem mechanizmów AI. Większość informacji o nowych narzędziach i aplikacjach wykorzystujących AI koncentruje się na przedstawieniu ich możliwości i korzyści biznesowych. Jednak w praktyce, żeby to osiągnąć, najczęściej niezbędna jest analiza i przebudowa zgromadzonych w firmie zbiorów danych, aby były spójne, wyczyszczone ze śmieci i odpowiednio powiązane. Dopiero wówczas sztuczna inteligencja będzie mogła efektywnie wesprzeć procesy biznesowe. W 2017 r. Vanson Bourne na zlecenie Teradata przeprowadził badania ankietowe, których wyniki przedstawiono w raporcie „State of Artificial Intelligence for Enterprises”. Wśród przedsiębiorstw widać dość duży entuzjazm, jeśli chodzi o potencjalne zastosowania AI. Aż 80% ankietowanych firm deklaruje, że już inwestuje lub planuje inwestycje w tego typu technologie, a 30% planuje ich zwiększenie w najbliższych trzech latach. Głównym motywem jest przekonanie, że AI może zwiększyć ich konkurencyjność na rynku. Jednocześnie aż 91% respondentów widzi poważne bariery i problemy hamujące wdrożenia technologii AI. 40% przewiduje, że największą barierą może być brak odpowiedniej infrastruktury IT, 30%, że jest to brak pracowników mających wysokie kwalifikacje do zarządzania systemami AI, a 33% uważa, że dostępne na rynku narzędzia i aplikacje są dopiero w początkowej fazie rozwoju i nie zostały praktycznie sprawdzone. Co ciekawe, tylko 19% ankietowanych ma wątpliwości, czy zastosowanie AI może przynieść korzyści biznesowe, a 20% obawia się, że automatyzacja może spowodować utratę pracy i źle wpłynąć na morale pracowników. Jedną z poważnych barier zastosowań systemów AI, w szczególności w firmach podlegających restrykcyjnym przepisom prawnym, jest wykazanie, w jaki sposób mechanizmy sztucznej inteligencji doprowadziły do podjęcia określonych decyzji. Opracowanie rozwiązań umożliwiających przeprowadzenie audytu działania systemu opartego na AI ma tu zasadnicze znaczenie. Jeśli np. autonomiczny samochód lub system dozowania leków spowoduje zagrożenie dla ludziego życia wskutek niewłaściwej decyzji oprogramowania AI, to trzeba mieć mechanizmy pozwalające na efektywną analizę przyczyn tej sytuacji i wyeliminowanie błędów. Obecnie systemy wykorzystujące sztuczną inteligencję mają często formę „czarnej skrzynki”, ale analiza ich działania jest bardzo trudna lub nawet niemożliwa. Mechanizmy AI i uczenia maszynowego są już wykorzystywane w praktyce przez dostawców oprogramowania bezpieczeństwa. Na przykład firma MobileIron do najnowszej wersji narzędzia MobileIron Threat Defense wprowadziła mechanizmy analizy behawioralnej mające na celu wykrywanie podejrzanych zachowań aplikacji i aktywności w sieci. Wykorzystują one uczenie maszynowe, co pozwala na ciągłe ulepszanie ich funkcjonowania i zwiększanie efektywności ochrony przed zagrożeniami. Sophos do oprogramowania chroniącego punkty końcowe wprowadził mechnizmy głębokiego uczenia, które mają być podstawą do stworzenia systemu bezpieczeństwa opartego na predykcji zagrożeń – „predictive security”, jak określają przedstawiciele producenta. Citrix Analytics, oprogramowanie do zarządzania zasobami urządzeń działających w sieci, zostało wyposażone w mechanizmy analizy zachowań użytkowników wykorzystujące uczenie maszynowe do podziału użytkowników na kategorie o różnym poziomie ryzyka, które są systematycznie aktualizowane zgodnie ze zbieranymi przez system kolejnymi danymi. IBM opracował chmurową aplikację MaaS360 Watson, która ułatwia administratorom IT analizę masowych informacji generowanych przez urządzenia końcowe, ich użytkowników i aplikacje. Wykorzystuje ona technologie AI i uczenia maszynowego do zwiększenia poziomu bezpieczeństwa, produktywności oraz ułatwienia zarządzania aplikacjami mobilnymi. Trend Micro oferuje narzędzie Writing Style DNA do ochrony przed atakami na biznesową pocztę elektroniczną. Wykorzystuje ono mechanizmy sztucznej inteligencji do stworzenia wzorca stylu pisania użytkownika obejmującego ponad 7000 cech. Po wykryciu wiadomości, która wygląda na próbę podszycia się pod jej deklarowanego nadawcę, język wiadomości jest porównywany z modelem opracowanym przy wykorzystaniu AI, a do nadawcy, adresata i działu IT jest wysyłane ostrzeżenie. F-Secure wprowadziło narzędzie Rapid Detection & Response, które wykorzustując mechanizmy sztucznej inteligencji, pozwala nie tylko wykryć potencjalne zagrożenia, ale też wskazać podatne na nie zasoby i ocenić poziom ryzyka. Każda zarejestrowana anomalia w aktywności aplikacji i ruchu danych jest badana, aby odfiltrować fałszywe alarmy, a wykryte zagrożenia zostają zgłoszone firmie lub dostawcy usług wraz ze szczegółowymi wskazówkami dotyczącymi zalecanego sposobu reakcji.'


difficult_text = '''﻿Informacja dla pracowników zawierająca obowiązujące normy prawne dotyczące równego traktowania w zatrudnieniu

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
