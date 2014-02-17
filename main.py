#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os
import random as r

f = [0,1,2,3,4,5,6]					#leeres Feld f erzeugen (x-werte)


#zeichnet das aktuelle Spielfeld
def zeichne(spieler):
	global f
	os.system("clear")				#alles leeren
	#Symolwahl
	if (spieler == 1):
		symbol = "X"
	else:
		symbol = "O"
	print "\n\n%s ist am Zug (%s)\n\n"%(spieler, symbol)
	print "\t\t1  2  3  4  5  6  7"
	for y in range(0,6):			#0 bis 5 (von oben nach unten)
		print "\t\t",				#--> etwas einruecken
		for x in range(0,7):		#0 bis 6 (von links nach rechts)
			print f[x][y] + " ",	#feldinhalt anzeigen + leerzeichen
		print ""					#neue zeile
	print ""


#fuehrt den Zug aus
def setze(aktSp, spalte):
	global f
	
	#Symolwahl
	if (aktSp == 1):
		symbol = "X"
	else:
		symbol = "O"
		
	for y in range(0,6):			#test von oben
		if (y+1 == 6 or f[spalte][y+1] != "."):
			f[spalte][y] = symbol
			break
		

#Fragt Spieler, wohin er setzen will
def spielerZug(aktSp):
	global f
	spalte = "9"								#wert fuer spalte, damit while schleife greift
	while not (spalte in range(0,7)):			#solange die eingabe nicht richtig war
		spalte = int(raw_input("In welches Feld soll gesetzt werden? "))
		spalte -= 1								#f...von 0 bis 6; eingabe von 1 bis 7
	setze(aktSp, spalte)


#prueft, ob das Spiel zuende ist
def pruefeEnde(): 
	return False


def main():
	#INIT:
	spieler = ["",""]
	spieler[0] = raw_input("Name Spieler 1: ")
	spieler[1] = raw_input("Name Spieler 2: ")
	
	global f							#main() kann f veraendern
	for x in range(0,7):				#0 bis 6
		f[x] = [".",".",".",".",".","."]
	
	#SPIEL:
	aktSp = r.randint(0,1)				#aktueller Spieler...Bestimmen, welcher Spieler beginnt	
	while not (pruefeEnde()):			#solange das Spiel laeuft
		zeichne(spieler[aktSp])
		spielerZug(aktSp)
		
		#Spielerwechsel
		if (aktSp == 0):
			aktSp = 1
		elif (aktSp == 1):
			aktSp = 0

main()
