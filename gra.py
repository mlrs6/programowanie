def start_game():
    print("=== CIENIE PRZEZNACZENIA ===")
    print("Obudziłeś się w świecie ogarniętym chaosem. W oddali widzisz zniszczone miasto, a za sobą majaczy las pełen cieni.")
    print("Na swojej klatce piersiowej zauważasz tajemniczy znak przypominający półksiężyc.")
    print("Przed tobą pojawia się tajemnicza postać w czarnej pelerynie.")
    print("\nPostać mówi: 'Twoje przeznaczenie wzywa cię Samuraju. Czy stawisz mu czoła?'")
    pierwszy_wybor()

def pierwszy_wybor():
    print("\nCo robisz?")
    print("1. Zadajesz pytanie: 'Kim jesteś?'")
    print("2. Ignorujesz postać i ruszasz w stronę lasu.")
    print("3. Podnosisz kamień, by rzucić w postać.")
    wybor = input("Wybierz [1/2/3]: ")

    if wybor == "1":
        spotkanie()
    elif wybor == "2":
        idz_do_lasu()
    elif wybor == "3":
        atak()
    else:
        pierwszy_wybor()

def spotkanie():
    print("\nPostać odpowiada: 'Jestem cieniem twojego przeznaczenia. Nie możesz uciec.'")
    print("1. Pytasz: 'Kim jesteś? Co mam zrobić?'")
    print("2. Ignorujesz jego słowa i idziesz dalej.")
    wybor = input("Wybierz [1/2]: ")

    if wybor == "1":
        print("\nPostać mówi: 'W lesie znajdziesz odpowiedzi, ale pamiętaj – każda decyzja ma swoją cenę.'")
        idz_do_lasu()
    elif wybor == "2":
        print("\nOdchodzisz, ale czujesz, że coś cię obserwuje. Las posiada jakąś magiczną aurę.")
        idz_do_lasu()
    else:
        spotkanie()

def idz_do_lasu():
    print("\nWchodzisz do mrocznego lasu. Powietrze staje się chłodne, a drzewa zdają się mówić mrocznym językiem.")
    print("Po kilku minutach marszu trafiasz na skrzyżowanie dróg.")
    print("1. Idziesz w lewo, gdzie słyszysz szum wody.")
    print("2. Idziesz w prawo, gdzie widzisz tajemnicze światło.")
    print("3. Zatrzymujesz się i próbujesz znaleźć wskazówki w okolicy.")
    wybor = input("Wybierz [1/2/3]: ")

    if wybor == "1":
        sciezka_rzeka()
    elif wybor == "2":
        sciezka_rzeka()
    elif wybor == "3":
        przeszukanie_lasu()
    else:
        idz_do_lasu()

def sciezka_rzeka():
    print("\nIdziesz w stronę szumu wody i docierasz do rzeki.")
    print("Widzisz tam zaniedbaną łódź przycumowaną do starego pomostu.")
    print("1. Idziesz na pomost.")
    print("2. Wchodzisz do łodzi i przepływasz rzekę.")
    print("3. Zatrzymujesz się i odpoczywasz nad rzeką.")
    wybor = input("Wybierz [1/2/3]: ")

    if wybor == "1":
        print("\nMusisz szybko dopłynąć na drugą stronę, ale tracisz siły. Widzisz zbliżający się do ciebie cień")
        print("Wskakujesz do wody.")
        print("Udaje ci się przepłynąć, ale jesteś bardzo wyczerpany.")
        sciezka_rzeka()
    elif wybor == "2":
        print("\nUdaje ci się przepłynąć łódką na drugą stronę.")
        sciezka_rzeka()
    elif wybor == "3":
        print("\nPodczas odpoczynku czujesz, że cień jest bardzo blisko i nie ma szansy na ucieczke.")
        print("Twoja dusza zostaje pochłonięta.")
    else:
        sciezka_rzeka()

def sciezka_rzeka():
    print("\nIdziesz w stronę tajemniczego światła i znajdujesz starożytne ruiny.")
    print("W środku widzisz dwa zwoje: jeden biały, zaś drugi czarny.")
    print("1. Podnosisz biały zwój.")
    print("2. Podnosisz czarny zwój.")
    print("3. Zostawiasz zwoje i przeszukujesz ruiny.")
    wybor = input("Wybierz [1/2/3]: ")

    if wybor == "1":
        print("\nZwój biały rozjaśnia twoją duszę dając ci moce i siłe do walki z cieniem.")
        print("Pokojnujesz cień, który okazał się władcą starożytnego księżyca.")
    elif wybor == "2":
        print("\nZwój czarny podchłania twoje serce i stajesz się nowym władcą Krwawego Księżyca.")
        print("Teraz ty kradniesz ludziom dusze.")
    elif wybor == "3":
        print("\nPodczas przeszukiwania ruin znajdujesz starożytną księgę opisującą pochodzenie Krwawego Księżyca.")
        print("Dzięki tej wiedzy nauczyłeś się magii i twoja wiedza pozwala na obalenie władcy.")
    else:
        sciezka_rzeka()

def przeszukanie_lasu():
    print("\nSzukając wskazówek, znajdujesz symbol wyryty w drzewie. Wygląda jak twój znak na klatce pieriowej.")
    print("Czujesz, że musisz podążać za tajemniczą ścieżką.")
    print("1. Podążasz za ścieżką.")
    print("2. Ignorujesz symbol i wracasz na ścieżkę.")
    wybor = input("Wybierz [1/2]: ")

    if wybor == "1":
        sciezka_rzeka()
    elif wybor == "2":
        idz_do_lasu()
    else:
        przeszukanie_lasu()

def atak():
    print("\nRzucasz kamieniem w postać, ale on rozpływa się w powietrzu.")
    print("Nagle czujesz, że coś chłodnego dotyka twojej dłoni. Cień pochłania twoją duszę.")
    print("Twoja dusza została skradziona na wieki.")

# Uruchomienie gry
start_game()
