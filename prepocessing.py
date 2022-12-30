import os
import sys
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
import string
import re
#function opsional
def pindah(label):
    global nomor
    nomor = label

def clearscreen():
    os.system('cls')

def keluar():
    clearscreen()
    sys.exit()

def ulang():
    ulang = input("Kembali ke menu ? [y/n] ")
    if ulang == "y" or ulang == "Y" :
        pindah(0)
        clearscreen()
    elif ulang == "n" or ulang == "N" :
        clearscreen()
        keluar()
    else :
        keluar()

#menu
nomor = 0

while True :

    if nomor == 0 :
        clearscreen()
        print ("|---------------------------------------|")
        print ("|         Aplikasi Prepocessing         |")
        print ("|---------------------------------------|")
        print ("|---------------------------------------|")
        print ("|              Menu Utama               |")
        print ("|---------------------------------------|")
        print ("|1. Tokenizing                          |")
        print ("|2. Filtering                           |")
        print ("|3. Case Folding                        |")
        print ("|4. Exit                                |")
        print ("|---------------------------------------|")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            pindah(1)
        elif pilih == 2 :
            pindah(2)
        elif pilih == 3 :
            pindah(3)
        else :
            keluar()
     
#submenu
    elif nomor == 1 :
        clearscreen()
        print ("|---------------------------------------|")
        print ("|         Aplikasi Prepocessing         |")
        print ("|---------------------------------------|")
        print ("|---------------------------------------|")
        print ("|            Menu Tokenizing            |")
        print ("|---------------------------------------|")
        print ("|1. split word                          |")
        print ("|2. hitung frekuensi token(with graphic)|")
        print ("|3. kembali                             |")
        print ("|4. exit                                |")
        print ("|---------------------------------------|")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            kalimat = input("Masukkan Kalimat : ")
            tokens = nltk.tokenize.word_tokenize(kalimat)
            print(tokens)
            ulang()
        elif pilih == 2 :
            kalimat = input("Masukkan Kalimat : ")
            kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()
            tokens = nltk.tokenize.word_tokenize(kalimat)
            kemunculan = nltk.FreqDist(tokens)
            print(kemunculan.most_common())
            kemunculan.plot(30,cumulative=False)
            plt.show()
            ulang()
        elif pilih == 3 :
            ulang()
            clearscreen()
        elif pilih == 4 :
            keluar()
        else :
            print("pilihan tidak tersedia")
            ulang()
            

    elif nomor == 2 :
        clearscreen()
        print ("|------------------------------------------|")
        print ("|          Aplikasi Prepocessing           |")
        print ("|------------------------------------------|")
        print ("|------------------------------------------|")
        print ("|             Menu Filtering               |")
        print ("|------------------------------------------|")
        print ("|1. stopword removed default               |")
        print ("|2. stopword removed dinamis               |")
        print ("|3. hapus imbuhan kata                     |")
        print ("|4. kembali                                |")
        print ("|5. exit                                   |")
        print ("|------------------------------------------|")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            factory = StopWordRemoverFactory()
            stopword = factory.create_stop_word_remover()
            kalimat = input("Masukkan Kalimat : ")
            kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()
            stop = stopword.remove(kalimat)
            tokens = nltk.tokenize.word_tokenize(stop)
            print(tokens)
            ulang()
        elif pilih == 2 :
            rs = input("Masukkan stopword : ")
            kalimat = input("Masukkan Kalimat : ")
            stop_factory = StopWordRemoverFactory().get_stop_words() #load default stopword
            more_stopword = [rs] #load dinamis stopword
            data = stop_factory + more_stopword #menggabungkan stopword
            dictionary = ArrayDictionary(data)
            str = StopWordRemover(dictionary)
            tokens = nltk.tokenize.word_tokenize(str.remove(kalimat))
            print(tokens)
            ulang()
        elif pilih == 3 :
            kalimat = input("Masukkan Kalimat : ")
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()
            hasil = stemmer.stem(kalimat)
            print(hasil)
            ulang()
        elif pilih == 4 :
            ulang()
            clearscreen()
        elif pilih == 5 :
            keluar()
        else :
            print("pilihan tidak tersedia")
            ulang()

    elif nomor == 3 :
        clearscreen()
        print ("|------------------------------------------|")
        print ("|          Aplikasi Prepocessing           |")
        print ("|------------------------------------------|")
        print ("|------------------------------------------|")
        print ("|             Menu Case Folding            |")
        print ("|------------------------------------------|")
        print ("|1. menghapus angka                        |")
        print ("|2. menghapus tanda baca                   |")
        print ("|3. menghapus white space                  |")
        print ("|4. kembali                                |")
        print ("|5. exit                                   |")
        print ("|------------------------------------------|")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            kalimat = input("Masukkan Kalimat : ")
            hasil = re.sub(r"\d+", "", kalimat)
            print(hasil)
            ulang()
        elif pilih == 2 :
            kalimat = input("Masukkan Kalimat : ")
            hasil = kalimat.translate(str.maketrans("","",string.punctuation))
            print(hasil)
            ulang()
        elif pilih == 3 :
            kalimat = input("Masukkan Kalimat : ")
            hasil = kalimat.strip()
            print(hasil)
            ulang()
        elif pilih == 4 :
            ulang()
            clearscreen()
        elif pilih == 5 :
            keluar()
        else :
            print("pilihan tidak tersedia")
            ulang()
        