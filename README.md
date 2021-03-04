# Lista 7 - Języki programowania wysokiego poziomu

**Python (7) - funkcje - działadnie na parametrach**

(1) Aby zamienić zawartość 2 zmiennych (np. a i b) trzeba się posłużyć
zmienną pomocniczą c wpisując w nią tymczasowo wartość np. a. Napisz
program z ustalonymi zmiennymi całkowitymi a i b. Wyświetl a i b, zamień
ich zawartość i wyświetl nowe a i b.

(2) Spróbuj napisać funkcję zmien(a, b) która ma zamienić zawartość wprowadzonych parametrów. Wyświetl zamienione zmienne WEWNĄTRZ funkcji i PO ZASTOSOWANIU funkcji. Czy udało się zamienić parametry?

(3) Spróbuj powtórzyć (2) przekazując do funkcji zamien listę 2-elementową.
Wyświetl, po zamianie, listę wewnątrz funkcji i na zewnątrz. Czy udało się
zamienić elementy listy?

(4) Napisz funkcję odwroc(lista), która odwraca listę, np:
l = [1, 5, 4, 3] i po zastosowaniu funkcji l = [3, 4, 5, 1]. Sprawdź czy funkcja
działa.

(5) (Sortowanie bąbelkowe) Napisz funkcję sortuj(lista) która porządkuje listę lista rosnąco. Przetestuj tworząć listę 10-elementową liczb losowych
z zakresu [1..100].
Stwórz teraz listę kilkuelementową składającą się ze słów. Zastosuj na niej
funkcję sortuj i wyświetl na nowo listę. Co się stało? Przeanalizuj dlaczego.

(6) Stosując sortuj z poprzedniego zadania, napisz program w którym użytkownik wprowadza do zmiennej jakieś zdanie składające się ze słów i spacji.
Następnie ma być wyświetlone zdanie składjące się z tych samych słów ale
posortowanych alfabetycznie. Wreszcie ma być wyświetlone zdanie składające się z tych samych słów w kolejności od najkrótszych do najdłuższych
(jeśli słowa są tej samej długości nie jest ważne w jakiej kolejności są wyświetlane).
Np. dla ’Dzisiaj jest bardzo piękna pogoda’ na wyjść: bardzo Dzisiaj jest
piękna pogoda
jest bradzo piękna pogoda Dzisiaj

(7) (DODATKOWE) Stosując funkcje ord i chr wygeneruj listę składającą
się ze 100 ’losowych’ słów (od 3 do 8 liter). Posortuj uzyskaną listę alfabetycznie.
Zmień generowanie listy, tak aby conajmniej co 3 litery pojawiała się samogłoska i tak aby słowa nie zawierały podwójnych liter (obok siebie), czyli
nie chcemy np. appot (dwa razy p) ale apotp jest w porządku. Posortuj taką
listę alfabetycznie.
