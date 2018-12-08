from text_processing.document import Document

text = 'W ostatnich latach wiele firm zaczęło wdrażać narzędzia AI (Artificial Intelligence), ale zwykle są to projekty o małej skali, np. wirtualni asystenci. Te pierwsze doświadczenia pozwalają na zaznajomienie się z technologią AI i zdobycie podstawowej wiedzy o dostępnych narzędziach, ich możliwościach i ograniczeniach. „Dlatego w najbliższych latach można oczekiwać wzrostu liczby dużych wdrożeń aplikacji wykorzystujących mechanizmy AI” – uważa Nima Negahban, CTO w firmie Kinetica specjalizującej się w opracowywaniu systemów analitycznych o wysokiej wydajności. Potencjał technologii AI i uczenia maszynowego w zestawieniu z aktualnymi warunkami jest niestety przereklamowany, a większość firm ma problemy z określeniem realnych korzyści biznesowych, które można osiągnąć, inwestując w te technologie. Największe bariery popularyzacji to brak doświadczeń i wiedzy, jak efektywnie wdrożyć narzędzia wykorzystujące AI, a także brak przekonania, że zasoby danych zgromadzone w firmie mają wysoką wiarygodność i jakość. Stąd też sceptyczne podejście do projektów związanych z wprowadzeniem mechanizmów AI. Większość informacji o nowych narzędziach i aplikacjach wykorzystujących AI koncentruje się na przedstawieniu ich możliwości i korzyści biznesowych. Jednak w praktyce, żeby to osiągnąć, najczęściej niezbędna jest analiza i przebudowa zgromadzonych w firmie zbiorów danych, aby były spójne, wyczyszczone ze śmieci i odpowiednio powiązane. Dopiero wówczas sztuczna inteligencja będzie mogła efektywnie wesprzeć procesy biznesowe. W 2017 r. Vanson Bourne na zlecenie Teradata przeprowadził badania ankietowe, których wyniki przedstawiono w raporcie „State of Artificial Intelligence for Enterprises”. Wśród przedsiębiorstw widać dość duży entuzjazm, jeśli chodzi o potencjalne zastosowania AI. Aż 80% ankietowanych firm deklaruje, że już inwestuje lub planuje inwestycje w tego typu technologie, a 30% planuje ich zwiększenie w najbliższych trzech latach. Głównym motywem jest przekonanie, że AI może zwiększyć ich konkurencyjność na rynku. Jednocześnie aż 91% respondentów widzi poważne bariery i problemy hamujące wdrożenia technologii AI. 40% przewiduje, że największą barierą może być brak odpowiedniej infrastruktury IT, 30%, że jest to brak pracowników mających wysokie kwalifikacje do zarządzania systemami AI, a 33% uważa, że dostępne na rynku narzędzia i aplikacje są dopiero w początkowej fazie rozwoju i nie zostały praktycznie sprawdzone. Co ciekawe, tylko 19% ankietowanych ma wątpliwości, czy zastosowanie AI może przynieść korzyści biznesowe, a 20% obawia się, że automatyzacja może spowodować utratę pracy i źle wpłynąć na morale pracowników. Jedną z poważnych barier zastosowań systemów AI, w szczególności w firmach podlegających restrykcyjnym przepisom prawnym, jest wykazanie, w jaki sposób mechanizmy sztucznej inteligencji doprowadziły do podjęcia określonych decyzji. Opracowanie rozwiązań umożliwiających przeprowadzenie audytu działania systemu opartego na AI ma tu zasadnicze znaczenie. Jeśli np. autonomiczny samochód lub system dozowania leków spowoduje zagrożenie dla ludziego życia wskutek niewłaściwej decyzji oprogramowania AI, to trzeba mieć mechanizmy pozwalające na efektywną analizę przyczyn tej sytuacji i wyeliminowanie błędów. Obecnie systemy wykorzystujące sztuczną inteligencję mają często formę „czarnej skrzynki”, ale analiza ich działania jest bardzo trudna lub nawet niemożliwa. Mechanizmy AI i uczenia maszynowego są już wykorzystywane w praktyce przez dostawców oprogramowania bezpieczeństwa. Na przykład firma MobileIron do najnowszej wersji narzędzia MobileIron Threat Defense wprowadziła mechanizmy analizy behawioralnej mające na celu wykrywanie podejrzanych zachowań aplikacji i aktywności w sieci. Wykorzystują one uczenie maszynowe, co pozwala na ciągłe ulepszanie ich funkcjonowania i zwiększanie efektywności ochrony przed zagrożeniami. Sophos do oprogramowania chroniącego punkty końcowe wprowadził mechnizmy głębokiego uczenia, które mają być podstawą do stworzenia systemu bezpieczeństwa opartego na predykcji zagrożeń – „predictive security”, jak określają przedstawiciele producenta. Citrix Analytics, oprogramowanie do zarządzania zasobami urządzeń działających w sieci, zostało wyposażone w mechanizmy analizy zachowań użytkowników wykorzystujące uczenie maszynowe do podziału użytkowników na kategorie o różnym poziomie ryzyka, które są systematycznie aktualizowane zgodnie ze zbieranymi przez system kolejnymi danymi. IBM opracował chmurową aplikację MaaS360 Watson, która ułatwia administratorom IT analizę masowych informacji generowanych przez urządzenia końcowe, ich użytkowników i aplikacje. Wykorzystuje ona technologie AI i uczenia maszynowego do zwiększenia poziomu bezpieczeństwa, produktywności oraz ułatwienia zarządzania aplikacjami mobilnymi. Trend Micro oferuje narzędzie Writing Style DNA do ochrony przed atakami na biznesową pocztę elektroniczną. Wykorzystuje ono mechanizmy sztucznej inteligencji do stworzenia wzorca stylu pisania użytkownika obejmującego ponad 7000 cech. Po wykryciu wiadomości, która wygląda na próbę podszycia się pod jej deklarowanego nadawcę, język wiadomości jest porównywany z modelem opracowanym przy wykorzystaniu AI, a do nadawcy, adresata i działu IT jest wysyłane ostrzeżenie. F-Secure wprowadziło narzędzie Rapid Detection & Response, które wykorzustując mechanizmy sztucznej inteligencji, pozwala nie tylko wykryć potencjalne zagrożenia, ale też wskazać podatne na nie zasoby i ocenić poziom ryzyka. Każda zarejestrowana anomalia w aktywności aplikacji i ruchu danych jest badana, aby odfiltrować fałszywe alarmy, a wykryte zagrożenia zostają zgłoszone firmie lub dostawcy usług wraz ze szczegółowymi wskazówkami dotyczącymi zalecanego sposobu reakcji.'

doc = Document.from_text(text)

print(f'Original text - {len(doc.sentences)} sentences, {len(doc.lemma_count.count)} unique words:')
print(text)
print()
print(f'Summary - {len(doc.summary.sentences)} sentences, {len(doc.summary.lemma_count.count)} unique words:')
print(str(doc.summary))
