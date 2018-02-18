#!/usr/bin/env python3
from tkinter import *
import random

class risiko:
    def dadi(rosso, blu, numeroDadi):
        res = 0
        rosso.sort(reverse=1)
        blu.sort(reverse=1)
        for i in range(0, numeroDadi):
            res = res + (rosso[i] > blu[i])
        return res

    def euristicRisiko(numeroDadiRossi, numeroDadiBlu, accuratezza):
        print("Probabilità con", numeroDadiRossi, "dadi di attacco e", numeroDadiBlu, "dadi di difesa")
        print("")
        print("loading...")
        res = [0, 0, 0, 0]
        accuratezza = 10 ** accuratezza
        numeroDadi = min(numeroDadiRossi, numeroDadiBlu)
        for i in range(accuratezza):
            rosso = []
            blu = []
            for j in range(numeroDadiRossi):
                rosso.append(random.randint(1, 6))
            for j in range(numeroDadiBlu):
                blu.append(random.randint(1, 6))
            if risiko.dadi(rosso, blu, numeroDadi) == 0:
                res[0] = res[0] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 1:
                res[1] = res[1] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 2:
                res[2] = res[2] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 3:
                res[3] = res[3] + 1
            else:
                print("error")
        for i in range(numeroDadi, 3):
            res.pop()
        for i in range(0, len(res)):
            res[i] = res[i] * 100 / accuratezza
            print("Probabilità di uccidere", i, "truppe:", res[i], "%")
        return res

    def euristicRisikoDatiDadiAttacco(rosso, numeroDadiBlu, accuratezza):
        numeroDadiRossi = len(rosso)
        print("")
        print("Probabilità con", rosso, "come dadi di attacco e", numeroDadiBlu, "dadi di difesa")
        print("")
        print("loading...")
        res = [0, 0, 0, 0]
        accuratezza = 10 ** accuratezza
        numeroDadi = min(numeroDadiRossi, numeroDadiBlu)
        for i in range(accuratezza):
            blu = []
            for j in range(numeroDadiBlu):
                blu.append(random.randint(1, 6))
            if risiko.dadi(rosso, blu, numeroDadi) == 0:
                res[0] = res[0] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 1:
                res[1] = res[1] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 2:
                res[2] = res[2] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 3:
                res[3] = res[3] + 1
            else:
                print("error")
        for i in range(numeroDadi, 3):
            res.pop()
        for i in range(0, len(res)):
            res[i] = res[i] * 100 / accuratezza
            print("Probabilità di uccidere", i, "truppe:", res[i], "%")
        return res


    def euristicRisikoDatiDadiDifesa(numeroDadiRossi, blu, accuratezza):
        numeroDadiBlu = len(blu)
        print("")
        print("Probabilità con", numeroDadiRossi, "dadi di attacco e", blu, "come dadi di difesa dadi di difesa")
        print("")
        print("loading...")
        res = [0, 0, 0, 0]
        accuratezza = 10 ** accuratezza
        numeroDadi = min(numeroDadiRossi, numeroDadiBlu)
        for i in range(accuratezza):
            rosso = []
            for j in range(numeroDadiRossi):
                rosso.append(random.randint(1, 6))
            if risiko.dadi(rosso, blu, numeroDadi) == 0:
                res[0] = res[0] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 1:
                res[1] = res[1] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 2:
                res[2] = res[2] + 1
            elif risiko.dadi(rosso, blu, numeroDadi) == 3:
                res[3] = res[3] + 1
            else:
                print("error")
        for i in range(numeroDadi, 3):
            res.pop()
        for i in range(0, len(res)):
            res[i] = res[i] * 100 / accuratezza
            print("Probabilità di uccidere", i, "truppe:", res[i], "%")
        return res


print("Salve. Benvenuto nel chopperScript per sapere le probabilità di lancio a risiko")
while 1:
    print("------------------------------------------")
    print("Premi 0 per conoscere le priorità a priori")
    print("1 per conoscere le probabilità dati i dadi da attacco")
    print("2 per conoscere le priorità dati i dadi di difesa")
    x = int(input())
    while x not in range(0, 3):
        print("non era tra 0,1 o 2...")
        x = int(input())
    if x == 0:
        print("Inserisci il numero di dadi rossi (tra 1 e 3):")
        a1 = int(input())
        while a1 not in range(1, 4):
            print("non era tra 1 e 3... riprova:")
            a1 = int(input())
        print("Inserisci il numero di dadi blu (tra 1 e 3):")
        a2 = int(input())
        while a2 not in range(1, 4):
            print("non era tra 1 e 3... riprova:")
            a2 = int(input())
        risiko.euristicRisiko(a1, a2, 5)
    elif x == 1:
        rosso = []
        print("Inserisci il numero di dadi rossi (tra 1 e 3):")
        a1 = int(input())
        while a1 not in range(1, 4):
            print("non era tra 1 e 3... riprova:")
            a1 = int(input())
        print("Inserisci il numero di dadi blu (tra 1 e 3):")
        a2 = int(input())
        while a2 not in range(1, 4):
            print("non era tra 1 e 3... riprova:")
            a2 = int(input())
        for i in range(0, a1):
            print("valore dado", i+1)
            x1 = int(input())
            while x1 not in range(1, 7):
                print("non era tra 1 e 6... riprova:")
                x1 = int(input())
            rosso.append(x1)
        risiko.euristicRisikoDatiDadiAttacco(rosso, a2, 5)
    elif x == 2:
        blu = []
        print("Inserisci il numero di dadi rossi (tra 1 e 3):")
        a1 = int(input())
        while a1 not in range(1, 4):
            print("non era tra 1 e 3... riprova:")
            a1 = int(input())
        print("Inserisci il numero di dadi blu (tra 1 e 3):")
        a2 = int(input())
        while a2 not in range(1, 4):
            print("non era tra 1 e 3... riprova:")
            a2 = int(input())
        for i in range(0, a2):
            print("valore dado", i+1)
            x1 = int(input())
            while x1 not in range(1, 7):
                print("non era tra 1 e 6... riprova:")
                x1 = int(input())
            blu.append(x1)
        risiko.euristicRisikoDatiDadiDifesa(a1, blu, 5)
