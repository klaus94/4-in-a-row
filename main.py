#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os

def zeichne(f):
	print "\t\t1  2  3  4  5  6  7"
	for y in range(0,6):			#0 bis 5 (von oben nach unten)
		print "\t\t",				#--> etwas einruecken
		for x in range(0,7):		#0 bis 6 (von links nach rechts)
			print f[x][y] + " ",	#feldinhalt anzeigen + leerzeichen
		print ""					#neue zeile
	

def pruefeEnde(): 
	return False

def main():
	spieler = ["",""]
	spieler[0] = raw_input("Name Spieler 1: ")
	spieler[1] = raw_input("Name Spieler 2: ")
	
	f = [0,1,2,3,4,5,6]					#leeres Feld f erzeugen (x-werte)
	for x in range(0,7):				#0 bis 6
		f[x] = [".",".",".",".",".","."]
			
	while not (pruefeEnde()):			#solange das Spiel laeuft
		os.system("clear")				#alles leeren
		zeichne(f)
		#Eingabe...
		break

main()
