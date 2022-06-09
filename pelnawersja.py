#to dodać na sam początek całości kodu
#musicie też mieć najpierw zainstalowany moduł keyboard (aby to zrobić:
#otwórzcie pole komend (windows+cmd) i wpiszcie "pip install keyboard")
import os
import keyboard
import time
import random


def odnowienie_planszy():
    os.system("cls")
    for wiersz in plansza:
        for kolumna in wiersz:
            print(kolumna,end="")
        print()
    print("Ilosc zyc: " , ludzik.pobierz_zycia())
    print("Punkty: ", ludzik.pobierz_wynik())


def dzialanie(klawisz):
    ludzik.ruch(klawisz)
    odnowienie_planszy()
    time.sleep(1/20)


def wstaw_zniszczalne_bloczki(liczbabloczkow):
    zmiennaPomocna = 0
    while zmiennaPomocna < liczbabloczkow:
        wylosowana1 = random.randint(1, wymiar_x - 1)
        wylosowana2 = random.randint(1, wymiar_y - 1)
        if wylosowana1 == 1 and wylosowana2 == 1:
            plansza[wylosowana1][wylosowana2] == ' '
        elif wylosowana1 == 1 and wylosowana2 == 2:
            plansza[wylosowana1][wylosowana2] == ' '
        elif wylosowana1 == 2 and wylosowana2 == 1:
            plansza[wylosowana1][wylosowana2] == ' '
        elif plansza[wylosowana1][wylosowana2] == ' ':
            plansza[wylosowana1][wylosowana2] = 'H'
            zmiennaPomocna += 1

def wstaw_drzwi(wymiar_x,wymiar_y):
    czy = True #czy udalo sie wstawic dzrwi
    while czy:
        x_d= random.randint(1,wymiar_x-1)   ##pozycja drzwi
        y_d= random.randint(1,wymiar_y-1)
        if plansza[x_d][y_d] == 'H':
            czy=False
        return {x_d,y_d}


class Gracz:
    def __init__(self):
        self.wynik = 0
        self.pozycjax = 1
        self.pozycjay = 1
        self.zycia = 3

        self.prawo = "d"
        self.lewo = "a"
        self.gora = "w"
        self.dol = "s"

    def pobierz_wynik(self):
        return self.wynik

    def pobierz_pozycjax(self):
        return self.pozycjax

    def pobierz_pozycjay(self):
        return self.pozycjay

    def pobierz_zycia(self):
        return self.zycia

    def spawn_ludzik(self):
        plansza[self.pozycjax][self.pozycjay] = "P"


    #strać życie przy kontakcie z przeciwnikiem
    def zmien_zycie(self, liczba):
        self.zycia -= 1

    def zmien_wynik(self, liczba):
        self.wynik += liczba

    def ruch(self, klawisz):
        if plansza[self.pozycjax][self.pozycjay]=="B":
            # ruch w lewo
            if klawisz == "a":
                if plansza[self.pozycjax][self.pozycjay - 1] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = 'o'
                    plansza[self.pozycjax][self.pozycjay - 1] = 'P'
                    self.pozycjay -= 1
            # ruch w prawo
            elif klawisz == "d":
                if plansza[self.pozycjax][self.pozycjay + 1] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = 'o'
                    plansza[self.pozycjax][self.pozycjay + 1] = 'P'
                    self.pozycjay += 1
            # ruch w dol
            elif klawisz == "s":
                if plansza[self.pozycjax + 1][self.pozycjay] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = 'o'
                    plansza[self.pozycjax + 1][self.pozycjay] = 'P'
                    self.pozycjax += 1
            # ruch w gore
            elif klawisz == "w":
                if plansza[self.pozycjax - 1][self.pozycjay] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = 'o'
                    plansza[self.pozycjax - 1][self.pozycjay] = 'P'
                    self.pozycjax -= 1
        else:
            # ruch w lewo
            if klawisz == "a":
                if plansza[self.pozycjax][self.pozycjay - 1] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = ' '
                    plansza[self.pozycjax][self.pozycjay - 1] = 'P'
                    self.pozycjay -= 1
            # ruch w prawo
            elif klawisz == "d":
                if plansza[self.pozycjax][self.pozycjay + 1] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = ' '
                    plansza[self.pozycjax][self.pozycjay + 1] = 'P'
                    self.pozycjay += 1
            # ruch w dol
            elif klawisz == "s":
                if plansza[self.pozycjax + 1][self.pozycjay] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = ' '
                    plansza[self.pozycjax + 1][self.pozycjay] = 'P'
                    self.pozycjax += 1
            # ruch w gore
            elif klawisz == "w":
                if plansza[self.pozycjax - 1][self.pozycjay] == ' ':
                    plansza[self.pozycjax][self.pozycjay] = ' '
                    plansza[self.pozycjax - 1][self.pozycjay] = 'P'
                    self.pozycjax -= 1

    def tracenie_zycia(self):
        if self.zycia>0:
            self.zycia -= 1
            plansza[self.pozycjax][self.pozycjay] = ' '
            self.pozycjax = 1
            self.pozycjay = 1
            self.spawn_ludzik()
            # bomba.poziom_bomby=czas_wybuchu_bomby+1
        else:
            self.game_over()


    def game_over(self):
        os.system("cls")
        print('  ________                         ______')
        print(' |               /\      |\\    /| |')
        print(' |              /  \     | \\  / | |')
        print(' |   _____     /    \    |  \\/  | |___')
        print(' |  |     |   /______\   |      | |')
        print(' |        |  /        \  |      | |')
        print(' |________| /          \ |      | |______')
        print(" ")
        print('  ________                ______  _______')
        print(' |        | \\          / |       |       |')
        print(' |        |  \\        /  |       |       |')
        print(' |        |   \\      /   |___    |_______|')
        print(' |        |    \\    /    |       |    \\')
        print(' |        |     \\  /     |       |     \\')
        print(' |________|      \\/      |______ |      \\')
        time.sleep(10)

class Przeciwnik:

    def __init__(self):
        self.pozycjax_przeciwnik = 0
        self.pozycjay_przeciwnik = 0
        self.kierunek = 0
        self.zycie = 1

    def spawn_przeciwnik(self, plansza):
        self.kierunek = random.randint(0, 3)
        x = 0
        while x < 1:
            self.pozycjay_przeciwnik = random.randint(4,wymiar_y-1)
            self.pozycjax_przeciwnik = random.randint(4,wymiar_x-1)
            if plansza[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik] == " ":
                plansza[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik] = "Q"
                x += 1
            else:
                x = 0
    def smierc_przeciwnik(self):
        self.zycie=0
        plansza[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik]=" "
        ludzik.wynik+=200

    def ruch_przeciwnik(self, tablica):
        if self.zycie==1:
            #ruch w lewo
            if self.kierunek == 0:
                if tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik - 1] == " ":
                    tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik] = " "
                    tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik - 1] = "Q"
                    self.pozycjay_przeciwnik -= 1
                elif tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik - 1] == "P":
                    ludzik.tracenie_zycia()
                else:
                    self.kierunek = random.randint(1, 3)
            #ruch w prawo
            if self.kierunek == 1:
                if tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik + 1] == " ":
                    tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik] = " "
                    tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik + 1] = "Q"
                    self.pozycjay_przeciwnik += 1
                elif tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik + 1] == "P":
                    ludzik.tracenie_zycia()
                else:
                    self.kierunek = int(random.choice("023"))
            #ruch w góre
            if self.kierunek == 2:
                if tablica[self.pozycjax_przeciwnik - 1][self.pozycjay_przeciwnik] == " ":
                    tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik] = " "
                    tablica[self.pozycjax_przeciwnik - 1][self.pozycjay_przeciwnik] = "Q"
                    self.pozycjax_przeciwnik -= 1
                elif tablica[self.pozycjax_przeciwnik-1][self.pozycjay_przeciwnik] == "P":
                    ludzik.tracenie_zycia()
                else:
                    self.kierunek = int(random.choice("013"))
            #ruch w dół
            if self.kierunek == 3:
                if tablica[self.pozycjax_przeciwnik + 1][self.pozycjay_przeciwnik] == " ":
                    tablica[self.pozycjax_przeciwnik][self.pozycjay_przeciwnik] = " "
                    tablica[self.pozycjax_przeciwnik + 1][self.pozycjay_przeciwnik] = "Q"
                    self.pozycjax_przeciwnik += 1
                elif tablica[self.pozycjax_przeciwnik+1][self.pozycjay_przeciwnik] == "P":
                    ludzik.tracenie_zycia()
                else:
                    self.kierunek = random.randint(0, 2)

czas_odliczanie_bomby=3
czas_wybuchu_bomby=6


class Bomba():
    def __init__(self):
        self.pozycjax_bomby = 0
        self.pozycjay_bomby = 0
        self.czas_do_eksplozji = 3
        self.poziom_bomby = 1
        self.stan_istnienia_bomby=0

#stan istnienia bomby poniżej to nasz sposób na odliczanie jak długo będą trwały
#różne jej czynności, w ten sposób będziemy to modyfikować
    def istnienie_bomby(self,drzwi):
        #spoczynek
        if self.stan_istnienia_bomby==0:
            self.pozycjax_bomby=0
            self.pozycjay_bomby=0
        #postawienie bomby
        elif self.stan_istnienia_bomby==1:
            plansza[ludzik.pozycjax][ludzik.pozycjay] = "B"
            self.pozycjax_bomby=ludzik.pozycjax
            self.pozycjay_bomby=ludzik.pozycjay
            self.stan_istnienia_bomby+=1
        #odliczanie
        elif self.stan_istnienia_bomby<=czas_odliczanie_bomby:
            if plansza[ludzik.pozycjax][ludzik.pozycjay]==plansza[self.pozycjax_bomby][self.pozycjay_bomby]:
                plansza[self.pozycjax_bomby][self.pozycjay_bomby]="B"
            else:
                plansza[self.pozycjax_bomby][self.pozycjay_bomby]="o"
            self.stan_istnienia_bomby+=1
        #wybuch
        elif self.stan_istnienia_bomby<=czas_wybuchu_bomby:
            if self.poziom_bomby == 1:
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby] == "B":
                    ludzik.tracenie_zycia()
                plansza[self.pozycjax_bomby][self.pozycjay_bomby] = "E"
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]=="P":
                    ludzik.tracenie_zycia()
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]=="Q":
                    if liczba_przeciwnikow>0:
                        if plansza[przeciwnik.pozycjax_przeciwnik][przeciwnik.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                            przeciwnik.smierc_przeciwnik()
                        elif liczba_przeciwnikow>1:
                            if plansza[przeciwnik2.pozycjax_przeciwnik][przeciwnik2.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                przeciwnik2.smierc_przeciwnik()
                            elif liczba_przeciwnikow>2:
                                if plansza[przeciwnik3.pozycjax_przeciwnik][przeciwnik3.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                    przeciwnik3.smierc_przeciwnik()
                                elif liczba_przeciwnikow>3:
                                    if plansza[przeciwnik4.pozycjax_przeciwnik][przeciwnik4.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                        przeciwnik4.smierc_przeciwnik()
                                    elif liczba_przeciwnikow>4:
                                        if plansza[przeciwnik5.pozycjax_przeciwnik][przeciwnik5.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                            przeciwnik5.smierc_przeciwnik()
                                        elif liczba_przeciwnikow>5:
                                            if plansza[przeciwnik6.pozycjax_przeciwnik][przeciwnik6.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                                przeciwnik6.smierc_przeciwnik()
                                            elif liczba_przeciwnikow>6:
                                                if plansza[przeciwnik7.pozycjax_przeciwnik][przeciwnik7.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                                    przeciwnik7.smierc_przeciwnik()
                                                elif liczba_przeciwnikow>7:
                                                    if plansza[przeciwnik8.pozycjax_przeciwnik][przeciwnik8.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                                        przeciwnik8.smierc_przeciwnik()
                                                    elif liczba_przeciwnikow>8:
                                                        if plansza[przeciwnik9.pozycjax_przeciwnik][przeciwnik9.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                                            przeciwnik9.smierc_przeciwnik()
                                                        elif liczba_przeciwnikow>9:
                                                            if plansza[przeciwnik10.pozycjax_przeciwnik][przeciwnik10.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby-1]:
                                                                przeciwnik10.smierc_przeciwnik()
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] == "H":
                    ludzik.wynik+=50
                    if(self.pozycjax_bomby==drzwi[0] and (self.pozycjay_bomby - 1)==drzwi[1]):
                        plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] == "D"
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] != "X" and plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] != "D" :
                    plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] = "E"
                if plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]=="P":
                    ludzik.tracenie_zycia()
                if plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]=="Q":
                    if liczba_przeciwnikow>0:
                        if plansza[przeciwnik.pozycjax_przeciwnik][przeciwnik.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                            przeciwnik.smierc_przeciwnik()
                        elif liczba_przeciwnikow>1:
                            if plansza[przeciwnik2.pozycjax_przeciwnik][przeciwnik2.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                przeciwnik2.smierc_przeciwnik()
                            elif liczba_przeciwnikow>2:
                                if plansza[przeciwnik3.pozycjax_przeciwnik][przeciwnik3.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                    przeciwnik3.smierc_przeciwnik()
                                elif liczba_przeciwnikow>3:
                                    if plansza[przeciwnik4.pozycjax_przeciwnik][przeciwnik4.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                        przeciwnik4.smierc_przeciwnik()
                                    elif liczba_przeciwnikow>4:
                                        if plansza[przeciwnik5.pozycjax_przeciwnik][przeciwnik5.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                            przeciwnik5.smierc_przeciwnik()
                                        elif liczba_przeciwnikow>5:
                                            if plansza[przeciwnik6.pozycjax_przeciwnik][przeciwnik6.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                                przeciwnik6.smierc_przeciwnik()
                                            elif liczba_przeciwnikow>6:
                                                if plansza[przeciwnik7.pozycjax_przeciwnik][przeciwnik7.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                                    przeciwnik7.smierc_przeciwnik()
                                                elif liczba_przeciwnikow>7:
                                                    if plansza[przeciwnik8.pozycjax_przeciwnik][przeciwnik8.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                                        przeciwnik8.smierc_przeciwnik()
                                                    elif liczba_przeciwnikow>8:
                                                        if plansza[przeciwnik9.pozycjax_przeciwnik][przeciwnik9.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                                            przeciwnik9.smierc_przeciwnik()
                                                        elif liczba_przeciwnikow>9:
                                                            if plansza[przeciwnik10.pozycjax_przeciwnik][przeciwnik10.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby-1][self.pozycjay_bomby]:
                                                                przeciwnik10.smierc_przeciwnik()
                if plansza[self.pozycjax_bomby - 1][self.pozycjay_bomby] == "H":
                    ludzik.wynik+=50
                    if((self.pozycjax_bomby-1)==drzwi[0] and (self.pozycjay_bomby)==drzwi[1]):
                        plansza[self.pozycjax_bomby-1][self.pozycjay_bomby] == "D"
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] != "X" and plansza[self.pozycjax_bomby-1][self.pozycjay_bomby] != "D" :
                    plansza[self.pozycjax_bomby][self.pozycjay_bomby-1] = "E"
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]=="P":
                    ludzik.tracenie_zycia()
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]=="Q":
                    if liczba_przeciwnikow>0:
                        if plansza[przeciwnik.pozycjax_przeciwnik][przeciwnik.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                            przeciwnik.smierc_przeciwnik()
                        elif liczba_przeciwnikow>1:
                            if plansza[przeciwnik2.pozycjax_przeciwnik][przeciwnik2.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                przeciwnik2.smierc_przeciwnik()
                            elif liczba_przeciwnikow>2:
                                if plansza[przeciwnik3.pozycjax_przeciwnik][przeciwnik3.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                    przeciwnik3.smierc_przeciwnik()
                                elif liczba_przeciwnikow>3:
                                    if plansza[przeciwnik4.pozycjax_przeciwnik][przeciwnik4.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                        przeciwnik4.smierc_przeciwnik()
                                    elif liczba_przeciwnikow>4:
                                        if plansza[przeciwnik5.pozycjax_przeciwnik][przeciwnik5.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                            przeciwnik5.smierc_przeciwnik()
                                        elif liczba_przeciwnikow>5:
                                            if plansza[przeciwnik6.pozycjax_przeciwnik][przeciwnik6.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                                przeciwnik6.smierc_przeciwnik()
                                            elif liczba_przeciwnikow>6:
                                                if plansza[przeciwnik7.pozycjax_przeciwnik][przeciwnik7.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                                    przeciwnik7.smierc_przeciwnik()
                                                elif liczba_przeciwnikow>7:
                                                    if plansza[przeciwnik8.pozycjax_przeciwnik][przeciwnik8.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                                        przeciwnik8.smierc_przeciwnik()
                                                    elif liczba_przeciwnikow>8:
                                                        if plansza[przeciwnik9.pozycjax_przeciwnik][przeciwnik9.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                                            przeciwnik9.smierc_przeciwnik()
                                                        elif liczba_przeciwnikow>9:
                                                            if plansza[przeciwnik10.pozycjax_przeciwnik][przeciwnik10.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby][self.pozycjay_bomby+1]:
                                                                przeciwnik10.smierc_przeciwnik()
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby + 1] == "H":
                    ludzik.wynik+=50
                    if(self.pozycjax_bomby==drzwi[0] and (self.pozycjay_bomby + 1)==drzwi[1]):
                        plansza[self.pozycjax_bomby][self.pozycjay_bomby + 1] == "D"
                if plansza[self.pozycjax_bomby][self.pozycjay_bomby + 1] != "X" and plansza[self.pozycjax_bomby][self.pozycjay_bomby + 1] != "D" :
                    plansza[self.pozycjax_bomby][self.pozycjay_bomby + 1] = "E"
                if plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]=="P":
                    ludzik.tracenie_zycia()
                if plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]=="Q":
                    if liczba_przeciwnikow>0:
                        if plansza[przeciwnik.pozycjax_przeciwnik][przeciwnik.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                            przeciwnik.smierc_przeciwnik()
                        elif liczba_przeciwnikow>1:
                            if plansza[przeciwnik2.pozycjax_przeciwnik][przeciwnik2.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                przeciwnik2.smierc_przeciwnik()
                            elif liczba_przeciwnikow>2:
                                if plansza[przeciwnik3.pozycjax_przeciwnik][przeciwnik3.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                    przeciwnik3.smierc_przeciwnik()
                                elif liczba_przeciwnikow>3:
                                    if plansza[przeciwnik4.pozycjax_przeciwnik][przeciwnik4.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                        przeciwnik4.smierc_przeciwnik()
                                    elif liczba_przeciwnikow>4:
                                        if plansza[przeciwnik5.pozycjax_przeciwnik][przeciwnik5.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                            przeciwnik5.smierc_przeciwnik()
                                        elif liczba_przeciwnikow>5:
                                            if plansza[przeciwnik6.pozycjax_przeciwnik][przeciwnik6.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                                przeciwnik6.smierc_przeciwnik()
                                            elif liczba_przeciwnikow>6:
                                                if plansza[przeciwnik7.pozycjax_przeciwnik][przeciwnik7.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                                    przeciwnik7.smierc_przeciwnik()
                                                elif liczba_przeciwnikow>7:
                                                    if plansza[przeciwnik8.pozycjax_przeciwnik][przeciwnik8.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                                        przeciwnik8.smierc_przeciwnik()
                                                    elif liczba_przeciwnikow>8:
                                                        if plansza[przeciwnik9.pozycjax_przeciwnik][przeciwnik9.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                                            przeciwnik9.smierc_przeciwnik()
                                                        elif liczba_przeciwnikow>9:
                                                            if plansza[przeciwnik10.pozycjax_przeciwnik][przeciwnik10.pozycjay_przeciwnik]==plansza[self.pozycjax_bomby+1][self.pozycjay_bomby]:
                                                                przeciwnik10.smierc_przeciwnik()
                if plansza[self.pozycjax_bomby + 1][self.pozycjay_bomby] == "H":
                    ludzik.wynik+=50
                    if((self.pozycjax_bomby+1)==drzwi[0] and (self.pozycjay_bomby)==drzwi[1]):
                        plansza[self.pozycjax_bomby+1][self.pozycjay_bomby] == "D"
                if plansza[self.pozycjax_bomby+1][self.pozycjay_bomby] != "X" and plansza[self.pozycjax_bomby+1][self.pozycjay_bomby] != "D" :
                    plansza[self.pozycjax_bomby + 1][self.pozycjay_bomby] = "E"
                self.stan_istnienia_bomby+=1
        #zakończenie cyklu
        elif self.stan_istnienia_bomby==czas_wybuchu_bomby+1:
            plansza[self.pozycjax_bomby][self.pozycjay_bomby] = " "
            if plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] == "E":
                plansza[self.pozycjax_bomby][self.pozycjay_bomby - 1] = " "
            if plansza[self.pozycjax_bomby - 1][self.pozycjay_bomby] == "E":
                plansza[self.pozycjax_bomby - 1][self.pozycjay_bomby] = " "
            if plansza[self.pozycjax_bomby][self.pozycjay_bomby + 1] == "E":
                plansza[self.pozycjax_bomby][self.pozycjay_bomby + 1] = " "
            if plansza[self.pozycjax_bomby + 1][self.pozycjay_bomby] == "E":
                plansza[self.pozycjax_bomby + 1][self.pozycjay_bomby] = " "
            self.pozycjax_bomby = 0
            self.pozycjay_bomby = 0
            self.stan_istnienia_bomby = 0


    def spawn_bomba(self,pozycjaxludzika, pozycjayludzika):
        if self.stan_istnienia_bomby==0:
            self.stan_istnienia_bomby=1


#wymiary planszy, można zmieniać je tutaj
#OBA WYMIARY MUSZĄ BYĆ NIEPARZYSTE!!!!!
wymiar_x=15
wymiar_y=33

liczba_zniszczalnych_bloczkow = 70

liczba_przeciwnikow=7
#max 10, dla więcej nie ma kodu

plansza=[]
rzad = []


#kod poniżej ma tworzyć bazową planszę
#w kodzie poniżej są tylko niezniszczalne bloczki
#kod poniżej

#górna krawędź
for i in range(0,wymiar_y):
    rzad.append("X")
plansza.append(rzad)
rzad=[]

#środek planszy
polowa_y_minus_1=(wymiar_y-1)/2
for i in range(2,wymiar_x):
    if i%2==1:
        for j in range(0,int(polowa_y_minus_1)):
            rzad.append("X")
            rzad.append(" ")
    else:
        rzad.append("X")
        for k in range(2,wymiar_y):
            rzad.append(" ")
    rzad.append("X")
    plansza.append(rzad)
    rzad=[]

#dolna krawędź
for i in range(0,wymiar_y):
    rzad.append("X")
plansza.append(rzad)
rzad=[]


#wstawianie do planszy zniszczalnych bloczkow - wywolanie funkcji
wstaw_zniszczalne_bloczki(liczba_zniszczalnych_bloczkow)
(drzwi_x,drzwi_y)=wstaw_drzwi(wymiar_x,wymiar_y)
drzwi=[drzwi_x,drzwi_y]

######debug
#plansza[2][2]='H'
#drzwi=[2,2]
####
ludzik=Gracz()
ludzik.spawn_ludzik()



if liczba_przeciwnikow>0:
    przeciwnik = Przeciwnik()
    przeciwnik.spawn_przeciwnik(plansza)
    if liczba_przeciwnikow>1:
        przeciwnik2 = Przeciwnik()
        przeciwnik2.spawn_przeciwnik(plansza)
        if liczba_przeciwnikow>2:
            przeciwnik3 = Przeciwnik()
            przeciwnik3.spawn_przeciwnik(plansza)
            if liczba_przeciwnikow>3:
                przeciwnik4 = Przeciwnik()
                przeciwnik4.spawn_przeciwnik(plansza)
                if liczba_przeciwnikow>4:
                    przeciwnik5 = Przeciwnik()
                    przeciwnik5.spawn_przeciwnik(plansza)
                    if liczba_przeciwnikow>5:
                        przeciwnik6 = Przeciwnik()
                        przeciwnik6.spawn_przeciwnik(plansza)
                        if liczba_przeciwnikow>6:
                            przeciwnik7 = Przeciwnik()
                            przeciwnik7.spawn_przeciwnik(plansza)
                            if liczba_przeciwnikow>7:
                                przeciwnik8 = Przeciwnik()
                                przeciwnik8.spawn_przeciwnik(plansza)
                                if liczba_przeciwnikow>8:
                                    przeciwnik9 = Przeciwnik()
                                    przeciwnik9.spawn_przeciwnik(plansza)
                                    if liczba_przeciwnikow>9:
                                        przeciwnik10 = Przeciwnik()
                                        przeciwnik10.spawn_przeciwnik(plansza)

bomba=Bomba()

for wiersz in plansza:
    for kolumna in wiersz:
        print(kolumna,end="")
    print()



keyboard.add_hotkey("a",lambda: dzialanie("a"))
keyboard.add_hotkey("d",lambda: dzialanie("d"))
keyboard.add_hotkey("w",lambda: dzialanie("w"))
keyboard.add_hotkey("s",lambda: dzialanie("s"))
keyboard.add_hotkey("space",lambda: bomba.spawn_bomba(ludzik.pobierz_pozycjax(),ludzik.pobierz_pozycjay()))



while ludzik.pobierz_zycia()>0:

    if liczba_przeciwnikow>0:
        przeciwnik.ruch_przeciwnik(plansza)
        if liczba_przeciwnikow>1:
            przeciwnik2.ruch_przeciwnik(plansza)
            if liczba_przeciwnikow>2:
                przeciwnik3.ruch_przeciwnik(plansza)
                if liczba_przeciwnikow>3:
                    przeciwnik4.ruch_przeciwnik(plansza)
                    if liczba_przeciwnikow>4:
                        przeciwnik5.ruch_przeciwnik(plansza)
                        if liczba_przeciwnikow>5:
                            przeciwnik6.ruch_przeciwnik(plansza)
                            if liczba_przeciwnikow>6:
                                przeciwnik7.ruch_przeciwnik(plansza)
                                if liczba_przeciwnikow>7:
                                    przeciwnik8.ruch_przeciwnik(plansza)
                                    if liczba_przeciwnikow>8:
                                        przeciwnik9.ruch_przeciwnik(plansza)
                                        if liczba_przeciwnikow>9:
                                            przeciwnik10.ruch_przeciwnik(plansza)

    bomba.istnienie_bomby(drzwi)

    odnowienie_planszy()
    time.sleep(2/3)
ludzik.game_over()
