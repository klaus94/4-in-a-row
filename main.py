#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os
import random as r
import re

f = [0,1,2,3,4,5,6]					#leeres Feld f erzeugen (x-werte)


#zeichnet das aktuelle Spielfeld
def zeichne(spieler):
	global f
	os.system("clear")				#alles leeren
	#Symbolwahl
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
	eingabeRichtig = False						
	while not (eingabeRichtig):					#solange die eingabe nicht richtig war
		spalte = raw_input("In welches Feld soll gesetzt werden? ")
		if (spalte in "1234567" and spalte != ""):
			spalte = int(spalte)
			spalte -= 1								#f...von 0 bis 6; eingabe von 1 bis 7
			eingabeRichtig = True
	setze(aktSp, spalte)


#prueft, ob das Spiel zuende ist
def pruefeEnde():
	global f
	endeErkannt = False
	
	#erstellen eines Prueffeldes, mit dem einfach bestimmt werden kann, ob 4 Steine in einer Reihe liegen
	pruefFeld = []
	for x in range(0,7):
		for y in range(0,6):
			pruefFeld.append(f[x][y])
	pruefStr = "".join(pruefFeld)			#Feld --> String
	print pruefStr
	
	for sp in "XO":							#fuer beide spieler
		#senkrecht:
		if ("%s%s%s%s"%(sp,sp,sp,sp) in pruefStr):
			endeErkannt = True
			
		#waagerecht:		z.B.: XO....XO....XO....XO
		pattern = r'%s.....%s.....%s.....%s'%(sp,sp,sp,sp)			
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):		#wenn gefunden --> typ wird "_sre.SRE_ ..."
			endeErkannt = True
		
		#diagonal nach rechts unten:			z.B.: OXOX...OXX....OX.....O
		pattern = r'%s......%s......%s......%s'%(sp,sp,sp,sp)
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = True
		
		#diagonal nach rechts oben:				z.B.: O....OX...OXX..OXOX
		pattern = r'%s....%s....%s....%s'%(sp,sp,sp,sp)
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = True
		
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
	while not (pruefeEnde()):			#solange das Spiel laeuft
		zeichne(aktSp)
		spielerZug(aktSp)
		
		#Spielerwechsel
		if (aktSp == 0):
			aktSp = 1
		elif (aktSp == 1):
			aktSp = 0

main()
