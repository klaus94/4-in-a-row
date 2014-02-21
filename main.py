#!/ usr/binenv python
# -*- coding : utf -8 -*-

#4 gewinnt - nun gegen den Computer

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
		symbol = "O"
	else:
		symbol = "X"
	print "\n\nSpieler %i - %s ist am Zug (%s)\n\n"%(aktSp+1, spieler[aktSp], symbol)
	print "\t\t1  2  3  4  5  6  7"
	for y in range(0,6):			#0 bis 5 (von oben nach unten)
		print "\t\t",				#--> etwas einruecken
		for x in range(0,7):		#0 bis 6 (von links nach rechts)
			print f[x][y] + " ",	#feldinhalt anzeigen + leerzeichen
		print ""					#neue zeile
	print ""				


def pruefeEnde():				#prueft, ob das Spiel zuende ist
	global f
	endeErkannt = ""
	
	
	pruefFeld = []		#2D --> 1D
	for x in range(0,7):
		for y in range(0,6):
			pruefFeld.append(f[x][y])
	pruefStr = "".join(pruefFeld)			#Feld --> String
	#print pruefStr							#Kontrolle, fuer String
	
	for sp in "XO":							#fuer beide spieler
		if ("%s%s%s%s"%(sp,sp,sp,sp) in pruefStr):				#senkrecht
			endeErkannt = "Sieg fuer %s (senkrecht)"%(sp)
			
		pattern = r'%s.....%s.....%s.....%s'%(sp,sp,sp,sp)		#waagerecht: z.B.: XO....XO....XO....XO		
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):	#wenn gefunden --> typ wird "_sre.SRE_ ..."
			endeErkannt = "Sieg fuer %s (waagerecht)"%(sp)
		
		pattern = r'%s......%s......%s......%s'%(sp,sp,sp,sp)	#diagonal nach rechts unten: z.B.: OXOX...OXX....OX.....O
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = "Sieg fuer %s (diagonal)"%(sp)
		
		pattern = r'%s....%s....%s....%s'%(sp,sp,sp,sp)			#diagonal nach rechts oben:	z.B.: O....OX...OXX..OXOX
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = "Sieg fuer %s (diagonal)"%(sp)	
	return endeErkannt
	

#Fragt Spieler, wohin er setzen will
def spielerZug():
	global f
	eingabeRichtig = False
	symbol = "X"						#Spieler hat immer das X						
	while not (eingabeRichtig):					#solange die eingabe nicht richtig war
		spalte = raw_input("In welches Feld soll gesetzt werden? ")
		if (spalte in "1234567" and spalte != ""):
			spalte = int(spalte)
			spalte -= 1								#f...von 0 bis 6; eingabe von 1 bis 7
			
			for y in range(0,6):					#test von oben
			#[boden]		[auf letzten stein]		[nicht ins oberste, wenn reihe voll]
				if ((y+1 == 6 or f[spalte][y+1] != ".") and f[spalte][y] == "."):
					eingabeRichtig = True
					f[spalte][y] = symbol
					break
					
					
def computerZug():
	#INIT
	global f
	os.system("sleep 1")					#Wartezeit
	gefunden = False
	symbol = "O"							#Computer hat immer das O
	
	#Strategie 1: moeglichst weit rechts setzen
	'''
	spalte = 0
	while (gefunden == False):											
		if (f[spalte][0] == "."):
			gefunden = True
		else:
			spalte += 1
	'''
	#Strategie 2: Prioritaeten: 1)Selbst gewinnen 2)Niederlage verhindern 3)eigene Fallen bauen 4)Fallen von Gegner verhindern
	
	
	#SETZEN
	for y in range(0,6):					#test von oben
		if (y+1 == 6 or f[spalte][y+1] != "."):
			f[spalte][y] = symbol
			break


def main():
	#INIT:
	spieler = ["",""]
	spieler[0] = raw_input("Name Spieler: ")
	spieler[1] = "COM"
	
	global f							#main() kann f veraendern
	for x in range(0,7):				#0 bis 6
		f[x] = [".",".",".",".",".","."]
	
	#SPIEL:
	aktSp = r.randint(0,1)				#aktueller Spieler...Bestimmen, welcher Spieler beginnt	
	while (pruefeEnde() == ""):			#solange das Spiel laeuft
		zeichne(aktSp, spieler)
		if (aktSp == 0):
			spielerZug()
		else:
			computerZug()
		
		#Spielerwechsel
		if (aktSp == 0):
			aktSp = 1
		elif (aktSp == 1):
			aktSp = 0
	zeichne(aktSp, spieler)				#"Siegerfoto" --> kein Abbruch bevor 4 in einer Reihe
	print pruefeEnde()

main()
