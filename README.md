# 2D tile-map generator



## Autor

Autorem powyższego programu jest Kacper Skrodzki.

## Cel projektu

Celem tego projektu było stworzenie prostego generatora dwuwymiarowych map kafelkowych. Generator taki po przyjęciu danych o wymiarach żądanej mapy ma graficznie przedstawić wygenerowany wynik oraz ma umożliwić zapis oraz wczytanie danej mapy.

## Opis zewnętrzny - funkcjonalności

Generator działa jako aplikacja okienkowa. Po uruchomieniu pliku z interfejsem użytkownika generator pozwala użytkownikowi na załadowanie pliku ze swojej maszyny lub wygenerowanie mapy o podanych przez użytkownikach wymiarach lub skorzystania z domyślnego wymiaru 50 x 50 pikseli. Dodatkowo program pozwala użytkownikowi na wprowadzenie seed-u, czyli ustalenia w jakiej pozycji startowej ma działać generator losowy.

Generacja odbywa się proceduralnie przy użyciu szumów Perlina.

Po ukazaniu wygenerowanej mapy w interfejsie użytkownik ma możliwość powiększyć widzoczną mapę dla przejżystości odczytu oraz ma możliwość zapisania wygenerowanej mapy w formacie PNG.

## Opis wewnętrzny - klasy

Klasa TileMap:
    Odpowiada za samą kreację mapy i przetrzymania jej danych. Przy inicjalizacji zostaje utworzona pusta mapa jako tablica trójwymiarowa o wymiarach "wysokość" x "szerokość" x 3 zapisana samymi zerami. Struktura tablicy została specjalnie tak wybrana, aby można było użyć kodu RGB w celu zapisania informacji o danych kolorach pikseli.

Klasa Terrain:
    Klasa odpowiadająca za reprezentację inforamcji o danym terenie. Przechowuje kolor terenu zapisany w kodzie RGB oraz przechowuje kluczowe wartości minimalne trzech współczynników: wysokości, wilgotności i temperatury potrzebne do przydzielania odpowiedniego typu terenu dla danej pozycji na mapie.

Klasa Ui_MainWindow:
    Klasa odpowiadająca za układ widżetów w aplikacji okienkowej. Automatycznie generowana przy pomocy narzędzia Qt Designer.

Klasa MapGeneratorWindow:
    Klasa dziedzicząca po klasie QMainWindow. Odpowiada za obsługę widżetów aplikacji oraz jej uruchomienie i wyświetlenie. Ponadto obsługuje akcję zapisu i wczytaniu mapy oraz możliwość powiększania wygenerowanej mapy.

## Instrukcja użytkowania

Aby móc korzystać w pełni z opracowanego generatora należy zapoznać się z niniejszą instrukcją.

Po pierwsze, należy uruchomić skrypt zawarty w pliku "gui.py". Dzięki temu uruchomi się interfejs użytkownika.

Po otworzeniu się aplikacji użytkownik ujrzy przy górnej krawędzi trzy okienka na dane wejściowe do gneracji, odpowiednio podpisane. Obok tych pól na prawo znajduję się przycisk "Generate Map" odpowiadający za generację mapy. Na pasku narzędzi znajdują się dwa przyciski odpwiednio do zapisu obecnej mapy i do wczytania mapy z maszyny. Te dwa działania można też znaleźć w menu "File" znajdującym się w lewym górnym rogu okienka. Pod tym wszystkim znajduje się suwak do przybliżania mapy oraz zaznaczona przestzeń, w której pojawi się obraz mapy.

# Generacja mapy

Aby wygenerować mapę należy przycisnąć przycisk "Generate Map" i odczekać cierpliwie na wygenerowanie się mapy (przy dużych rozmiarach może to potrwać chwilkę).

Domyślnie program generuje mapy o wymiarach 50 x 50 z losowym seedem. Aby zmienić rozmiar generowanej mapy należy wypełnić pola "Height" oraz "Width". Pole "Seed" jest opcjonalne. Pola "Height", "Width" i "Seed" mają ustawiony limit liczbowy wynoszący od 1 do 9999. Po wypełnieniu pól należy przycisnąć przycisk "Generate Map" i odczekać cierpliwie.

# Przybliżanie mapy

Przybliżanie mapy polega na przesuwaniu suwaka "Scale of map" nad mapą w prawo. Maksymalnie można przybliżyć mapę ośmiokrotnie. Warto nadmienić, żeby przybliżenie zadziałało należy przesunąć kursorem rączkę suwaka na wybrane pole i go puścić.

# Zapis mapy

Aby zapisać mapę należy kliknąć opcję "Save Map". Można to zrobić z paska narzędzi albo z menu "File". Po wciśnięciu przycisku otworzy się nowe okno, w którym można wybrać miejsce zapisu i nazwę pliku z mapą. Program automatycznie zapisuje plik w formacie PNG, więc proszę wpisać w polu nazwy samą nazwę pliku bez rozszerzenia typu.

UWAGA: Zapisany jest ORYGINAŁ mapy, a nie jego przybliżony obraz.

# Wczytanie mapy

Aby wczytać mapę należy kliknąć opcję "Load Map". Można to zrobić z paska narzędzi albo z menu "File". Po wciśnięciu przycisku otworzy się nowe okno, w którym można wybrać który plik należy wczytać. Program przymuje różne formaty plików graficznych (PNG, JPEG, itd.), ale zalecam użycie formatu PNG.

## Wnioski i przemyślenia

Temat projektu okazał się ciekawym zagadnieniem. Przyjemnie było sobie poczytać o różnych sposobach proceduralnej generacji map do gier wideo. Dużą inspiracją był oczywiście Minecraft i jego generacja świata, która też bazuje w dużej mierze na szumach Perlina. Ponadto w internecie znalazłem wiele wątków dotyczących tematu mojego projektu. Nawet znalazłem stronę z takim przykładowym generatorem zrobionym w Unity.

Dużą pomocą w projekcie było to iż znalazłem bibliotekę obsługującą generację szumów Perlina oraz ogólna ilość bibliotek użytach w tym projekcie. Skróciły one czas pisania kodu tego programu. Nie żeby generator szumó Perlina był skomplikowany do zaimplementowania, ale jak już ktoś wyłożył matematkę i to udostępnił, to czemu nie skorzystać?

Jednakże nawet z taką ilością bibliotek wiążę się pewna odpowiedzialność i bolączka. Mianowicie, większość czasu poświęciłem na czytaniu dokumentacji bibliotek, badaniu różnych rozwiązań na dane problemy, na przykład jak przchowywać mapę. A szczególnie trudności zaczęły się w trakcie implementacji GUI.

Samo pobranie odpowiednich narzędzi zajęło mi jeden dzień, gdzyż pracując na środowisku Linuxowym na Windowsie nie wiedziałem, że trzeba pobrać XSerwer, aby umożliwić wyświetalanie zawartości przez podsystem. Nie skojarzyłem faktu iż na Teamsach jest filmik dotyczący tego zagadnienia, lecz w samym filmiku o GUI nie było o tym mowy, a gdy wyskoczył, na przykład, błąd segmentacji w przypadku PySide2 to zacząłem szukać rozwiązania tego błędu, a nie szukania ogólnie jak to działa na środowiskach.

Koniec końców udało się rozwiązać ten problem - po prostu przeszedłem na czystego Windowsa. Jednakże to nie koniec problemów z GUI, gdyż Qt jest dla mnie obce i ciężko było się połapać co, gdzie i jak. Ale przy pomocy Youtube-a, dokumentacji PyQt6, Stack OverFlow-a lub innych podobnych serwisów oraz cierpliwej analizie przykładów udało się osiągnąć to co chciałem.

To co chciałem zaimplementować to zaimplementowałem. Udało się tyle zrobić na ile na to pozwolił czas. Jestem całkiem zadowolony ze swojej pracy i obym mógł dalej się rozwijać. Na pewno wyciągnąłem jeden bardzo ważny wniosek: dokumentacja to dobry poradnik do tego jak coś zrobić.
