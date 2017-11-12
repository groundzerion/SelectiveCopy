#!/usr/bin/env python

# Zadaniem programu jest kopiowanie wybranego typu plikow rekursywnie z katalogu zrodlowego
# do katalogu docelowego
#
# Sposob uzycia:
#
# selcopy [rozszerzenie] [katalog zrodlowy] [katalog docelowy]
#
# mailto: ziolo2@gmail.com

import os, sys, shutil

liczba_skopiowanych = 0

# glowna petla programu
if len(sys.argv) != 4: #sprawdzenie czy uzytkownik wprowadzil poprawna ilosc argumentow
    print('''Sposob uzycia: \n selcopy [rozszerzenie] [katalog zrodlowy] [katalog docelowy]''')
    exit()

else:
    extension = sys.argv[1]
    source_dir = sys.argv[2]
    target_dir = sys.argv[3]

for directory, subdirectories, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.'+extension):
            currentFilePath = os.path.join(directory,file)
            shutil.copy(currentFilePath, target_dir)
            print('Skopiowano: '+currentFilePath)
            liczba_skopiowanych +=1

print('\nPODSUMOWANIE:\nStatus: zakonczono powodzeniem \nLiczba skopiowanych plikow z rozszerzeniem ' + extension + ' to: '+str(liczba_skopiowanych))




