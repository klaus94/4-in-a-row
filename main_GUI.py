#!/ usr/binenv python
# -*- coding : utf -8 -*-

import random as r
import re
from Tkinter import *
import Tkinter
import tkMessageBox


#################### SPIEL FUNKTIONEN ##############################
####################################################################

def zeichne(aktSp, x, y):
	global f
	global spielende
	#Symbolwahl
	if (aktSp == "X"):
		symFarbe = "red"
	else:
		symFarbe = "yellow"
	x0 = (x+1)*ab + g*x
	y0 = (y+1)*ab + g*y
	x1 = x0 + g
	y1 = y0 + g
	oval = C.create_oval(x0, y0, x1, y1, fill=symFarbe)
	C.pack()

	if (pruefeEnde(f) != ""):
		tkMessageBox.showinfo("Spielende", pruefeEnde(f))
		spielende = True
		print spielende
		root.quit()


def pruefeEnde(f):
		endeErkannt = ""
	
		pruefFeld = []					#2D --> 1D
		for x in range(0,7):
			for y in range(0,6):
				pruefFeld.append(f[x][y])
			pruefFeld.append("|")				#Kennzeichnung einer Spalte
		pruefStr = "".join(pruefFeld)			#Feld --> String
		#print pruefStr							#Kontrolle, fuer String
	
		for sp in "XO":							#fuer beide spieler
			if (sp == "O"):
				farbe = "gelb"
			else:
				farbe = "rot"

			if ("%s%s%s%s"%(sp,sp,sp,sp) in pruefStr):					#senkrecht
				endeErkannt = "Sieg fuer %s (senkrecht)"%(farbe)
		
			pattern = r'%s......%s......%s......%s'%(sp,sp,sp,sp)		#waagerecht		
			filtered = re.search(pattern,pruefStr)
			if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):		#wenn gefunden --> typ wird "_sre.SRE_ ..."
				endeErkannt = "Sieg fuer %s (waagerecht)"%(farbe)
		
			pattern = r'%s.......%s.......%s.......%s'%(sp,sp,sp,sp)	#diagonal nach rechts unten:	z.B.: XOXO|...XOO|....XO|.....X
			filtered = re.search(pattern,pruefStr)
			if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
				endeErkannt = "Sieg fuer %s (diagonal \\)"%(farbe)
		
			pattern = r'%s.....%s.....%s.....%s'%(sp,sp,sp,sp)			#diagonal nach rechts oben:		z.B.: X|....XO|...XOO|..XOXO
			filtered = re.search(pattern,pruefStr)
			if (str(type(filtered)) == "<type '_sre.SRE_Match'>"):
				endeErkannt = "Sieg fuer %s (diagonal /)"%(farbe)
	
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
	

def siegMoeglich(stufe):
	global f
	global bew

	faktor = 1
	if stufe == 2:
		faktor = -1

	gesetzt = False

	for symbol in "OX":								#fuer Computer und Spieler
		for spalte in range(0,7):					#jede spalte
			for y in range(0,6):					#SETZEN
				if ((y+1 == 6 or f[spalte][y+1] != ".") and f[spalte][y] == "."):	
					f[spalte][y] = symbol
					gesetzt = True
					break
			if (pruefeEnde(f) != ""):				#wenn es einen Sieger geben wuerde
				if symbol == "O":
					bew[spalte] += faktor * pow(2,2*(4-stufe))	#stufe 1: 32
				elif symbol == "X":
					bew[spalte] += pow(2,(4-stufe))	#stufe 1: 16
			if stufe < 3:							#rekursiv Pruefen
				siegMoeglich(stufe+1)
			if (gesetzt):							#nur zug rueckgaengig wenn gesetzt wurde
				f[spalte][y] = "."					#rueckgaengig
				gesetzt = False


def setzen(symbol, spalte):
	global f
	for y in range(0,6):							#test von oben
		if (y+1 == 6 or f[spalte][y+1] != "."):
			f[spalte][y] = symbol
			zeichne(symbol, spalte, y)
			break
			

def spielerZug(spalte):
	global f
	if (f[spalte-1][0] == "."):				
		setzen("X", spalte-1)						#f...von 0 bis 6; eingabe von 1 bis 7
					
					
def computerZug():
	global f
	global bew										#bew... Bewertungsfeld
	bew = [0,0,0,0,0,0,0]					

	siegMoeglich(1)									#Erstellung bew-Feld (4 Stufen voraus)

	spalte = r.randint(0,6)
	while bew[spalte] != max(bew) or inhaltKorrekt(spalte) == False:
		spalte = r.randint(0,6)

	setzen("O", spalte)
		
		
##################### SPIELER ZUG ##########################################
############################################################################

def klick1():
	spielerZug(1)
	if not(spielende):
		computerZug()
	
def klick2():
	spielerZug(2)
	if not(spielende):
		computerZug()
	
def klick3():
	spielerZug(3)
	if not(spielende):
		computerZug()
	
def klick4():
	spielerZug(4)
	if not(spielende):
		computerZug()
	
def klick5():
	spielerZug(5)
	if not(spielende):
		computerZug()
	
def klick6():
	spielerZug(6)
	if not(spielende):
		computerZug()
	
def klick7():
	spielerZug(7)
	if not(spielende):
		computerZug()	
	
###################### FORM ERSTELLEN ########################################
##############################################################################

ab = 5		#Abstand
g = 50		#Groesse

root = Tkinter.Tk()
root.geometry(str(8*ab+7*g)+"x"+str(7*ab+6*g+25))

#blauer Hintergrund
C = Tkinter.Canvas(root, bg="blue", height=7*ab+6*g+25, width=8*ab+7*g)
C.pack()

#Buttons:
y0 = (6*g) + (7*ab)		#immer gleich

knopf1 = Tkinter.Button(root, bg="#999999", font = "Ubuntu", text="1", command = klick1)
x0 = ab + g/2 - 10
knopf1.place(x=x0, y=y0, height=20, width=20)

knopf2 = Tkinter.Button(root, bg="#999999", font = "Ubuntu", text="2", command = klick2)
x0 = 2*ab + g+g/2 - 10
knopf2.place(x=x0, y=y0, height=20, width=20)

knopf3 = Tkinter.Button(root, bg="#999999", font = "Ubuntu", text="3", command = klick3)
x0 = 3*ab + 2*g+g/2 - 10
knopf3.place(x=x0, y=y0, height=20, width=20)

knopf4 = Tkinter.Button(root, bg="#999999", font = "Ubuntu", text="4", command = klick4)
x0 = 4*ab + 3*g+g/2 - 10
knopf4.place(x=x0, y=y0, height=20, width=20)

knopf5 = Tkinter.Button(root, bg="#999999", font = "Ubuntu", text="5", command = klick5)
x0 = 5*ab + 4*g+g/2 - 10
knopf5.place(x=x0, y=y0, height=20, width=20)

knopf6 = Tkinter.Button(root, bg="#999999", font = "Ubuntu", text="6", command = klick6)
x0 = 6*ab + 5*g+g/2 - 10
knopf6.place(x=x0, y=y0, height=20, width=20)

knopf7 = Tkinter.Button(root, bg="#999999", font = "Ubuntu", text="7", command = klick7)
x0 = 7*ab + 6*g+g/2 - 10
knopf7.place(x=x0, y=y0, height=20, width=20)


	
######################## INIT #####################################
###################################################################	

f = [0,1,2,3,4,5,6]					#leeres Feld f erzeugen (x-werte)
bew = [0, 0, 0, 0, 0, 0, 0]			#Berwertungsfeld
spielende = False


for x in range(0,7):
	f[x] = [".",".",".",".",".","."]



#ENDE:
#zeichne(aktSp, spieler)				#"Siegerfoto" --> kein Abbruch bevor 4 in einer Reihe
#print pruefeEnde(f)


root.mainloop()