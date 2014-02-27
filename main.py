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


def pruefeEnde(f):					#prueft, ob das Spiel zuende ist
	endeErkannt = ""
	
	pruefFeld = []		#2D --> 1D
	for x in range(0,7):
		for y in range(0,6):
			pruefFeld.append(f[x][y])
		pruefFeld.append("|")				#Kennzeichnung einer Spalte
	pruefStr = "".join(pruefFeld)			#Feld --> String
	#print pruefStr							#Kontrolle, fuer String
	
	for sp in "XO":							#fuer beide spieler
		if ("%s%s%s%s"%(sp,sp,sp,sp) in pruefStr):					#senkrecht
			endeErkannt = "Sieg fuer %s (senkrecht)"%(sp)
		
		pattern = r'%s......%s......%s......%s'%(sp,sp,sp,sp)		#waagerecht		
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):		#wenn gefunden --> typ wird "_sre.SRE_ ..."
			endeErkannt = "Sieg fuer %s (waagerecht)"%(sp)
		
		pattern = r'%s.......%s.......%s.......%s'%(sp,sp,sp,sp)	#diagonal nach rechts unten:	z.B.: XOXO|...XOO|....XO|.....X
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = "Sieg fuer %s (diagonal \\)"%(sp)
		
		pattern = r'%s.....%s.....%s.....%s'%(sp,sp,sp,sp)			#diagonal nach rechts oben:		z.B.: X|....XO|...XOO|..XOXO
		filtered = re.search(pattern,pruefStr)
		if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
			endeErkannt = "Sieg fuer %s (diagonal /)"%(sp)
	
	if (endeErkannt == ""):					#wenn kein Sieger erkannt
		unentschieden = True
		for i in pruefStr:					#kein leeres Feld mehr enthalten
			if (i == "."):
				unentschieden = False
				break
		if (unentschieden):					#--> unentschieden erkannt
			endeErkannt = "Unentschieden"
		
	return endeErkannt


def inhaltKorrekt(spalte):
	global f
	
	if (f[spalte][0] == "."):
		return True
	else:
		return False


def setzen(symbol, spalte):
	global f
	for y in range(0,6):							#test von oben
		if (y+1 == 6 or f[spalte][y+1] != "."):
			f[spalte][y] = symbol
			break


#Fragt Spieler, wohin er setzen will
def spielerZug():
	global f
	spalte = 1										#wert --> eingang schleife
	formalKorrekt = False
			
	while not (inhaltKorrekt(spalte-1) and formalKorrekt):		#solange die eingabe nicht richtig war
		formalKorrekt = False
		spalte = raw_input("In welches Feld soll gesetzt werden? ")
		if (spalte in "1234567" and spalte != ""):
			formalKorrekt = True
			spalte = int(spalte)
		else:
			spalte = 1								#beliebiger Wert, damit kein Fehler bei Fkt. inhaltKorrekt()
							
	setzen("X", spalte-1)							#f...von 0 bis 6; eingabe von 1 bis 7
					
	
					
#Strategie: Prioritaeten: 1)Selbst gewinnen 2)Niederlage verhindern 3)eigene Fallen bauen 4)Fallen von Gegner verhindern					
def computerZug():
	#INIT
	global f
	os.system("sleep 1")							#Wartezeit
	bew = [0,0,0,0,0,0,0]							#bew... Bewertungsfeld
	gesetzt = False
	
	#Prioritaet 1) und 2) direkten eigenen Sieg erkennen bzw. gegnerischen verhindern
	for symbol in "OX":								#fuer Computer und Spieler
		for spalte in range(0,7):					#jede spalte
			for y in range(0,6):					#SETZEN
				if ((y+1 == 6 or f[spalte][y+1] != ".") and f[spalte][y] == "."):	
					f[spalte][y] = symbol
					gesetzt = True
					break
			if (pruefeEnde(f) != ""):				#wenn es einen Sieger geben wuerde
				if (symbol == "O"):
					bew[spalte] += 2				#BEWertung eigener Sieg					!!!
				elif (symbol == "X"):
					bew[spalte] += 1				#BEWertung Sieg Gegner verhindern		!!!
			if (gesetzt):							#nur zug rueckgaengig wenn gesetzt wurde
				f[spalte][y] = "."					#rueckgaengig
				gesetzt = False
		
	print bew
	if (bew == [0,0,0,0,0,0,0]):
		spalte = r.randint(0,6)
	else:
		for spalte in range(0,7):						#In das hoechst bewertete Feld setzen
			if (bew[spalte] == max(bew)):
				break
		
	
	#SETZEN
	setzen("O", spalte)


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
	while (pruefeEnde(f) == ""):			#solange das Spiel laeuft
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
	print pruefeEnde(f)

if __name__ == "__main__":				#kann nur als eigenstaendiges Programm ausgefuert werden (nicht durch Import)
	main()
