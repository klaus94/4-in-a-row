#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os
import random as r
import re

f = [0,1,2,3,4,5,6]					#leeres Feld f erzeugen (x-werte)


#zeichnet das aktuelle Spielfeld
def zeichne(aktSp, spieler):
	global f
	os.system("clear")				#alles leeren
	#Symbolwahl
	if (aktSp == 1):
		symbol = "X"
	else:
		symbol = "O"
	print "\n\nSpieler %i - %s ist am Zug (%s)\n\n"%(aktSp+1, spieler[aktSp], symbol)
	print "\t\t1  2  3  4  5  6  7"
	for y in range(0,6):			#0 bis 5 (von oben nach unten)
		print "\t\t",				#--> etwas einruecken
		for x in range(0,7):		#0 bis 6 (von links nach rechts)
			print f[x][y] + " ",	#feldinhalt anzeigen + leerzeichen
		print ""					#neue zeile
	print ""		

#Fragt Spieler, wohin er setzen will
def spielerZug(aktSp):
	global f
	eingabeRichtig = False						
	while not (eingabeRichtig):					#solange die eingabe nicht richtig war
		spalte = raw_input("In welches Feld soll gesetzt werden? ")
		if (spalte in "1234567" and spalte != ""):
			spalte = int(spalte)
			spalte -= 1								#f...von 0 bis 6; eingabe von 1 bis 7
			
			if (aktSp == 1):						#Symolwahl
				symbol = "X"
			else:
				symbol = "O"
		
			for y in range(0,6):					#test von oben
					#[boden]		[auf letzten stein]		[nicht ins oberste, wenn reihe voll]
				if ((y+1 == 6 or f[spalte][y+1] != ".") and f[spalte][y] == "."):
					f[spalte][y] = symbol
					eingabeRichtig = True
					break


#prueft, ob das Spiel zuende ist
def pruefeEnde():
	global f
	endeErkannt = ""
	
	#erstellen eines Prueffeldes, mit dem einfach bestimmt werden kann, ob 4 Steine in einer Reihe liegen
	pruefFeld = []
	for x in range(0,7):
		for y in range(0,6):
			pruefFeld.append(f[x][y])
	pruefStr = "".join(pruefFeld)			#Feld --> String
	#print pruefStr							#Kontrolle, fuer String
	
	for sp in "XO":							#fuer beide spieler
		#senkrecht:
		if ("%s%s%s%s"%(sp,sp,sp,sp) in pruefStr):
			endeErkannt = "Sieg fuer %s (senkrecht)"%(sp)
			
		#waagerecht:		z.B.: XO....XO....XO....XO
		pattern = r'%s.....%s.....%s.....%s'%(sp,sp,sp,sp)			
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):		#wenn gefunden --> typ wird "_sre.SRE_ ..."
			endeErkannt = "Sieg fuer %s (waagerecht)"%(sp)
		
		#diagonal nach rechts unten:			z.B.: OXOX...OXX....OX.....O
		pattern = r'%s......%s......%s......%s'%(sp,sp,sp,sp)
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = "Sieg fuer %s (diagonal)"%(sp)
		
		#diagonal nach rechts oben:				z.B.: O....OX...OXX..OXOX
		pattern = r'%s....%s....%s....%s'%(sp,sp,sp,sp)
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = "Sieg fuer %s (diagonal)"%(sp)
		
	return endeErkannt
	


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
	while (pruefeEnde() == ""):			#solange das Spiel laeuft
		zeichne(aktSp, spieler)
		spielerZug(aktSp)
		
		#Spielerwechsel
		if (aktSp == 0):
			aktSp = 1
		elif (aktSp == 1):
			aktSp = 0
	zeichne(aktSp, spieler)
	print pruefeEnde()

main()
