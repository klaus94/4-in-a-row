#!/ usr/binenv python
# -*- coding : utf -8 -*-

def zeichne(f):
	for y in range(0,6):			#0 bis 5
		print "\t\t",				#--> etwas einruecken
		for x in range(0,7):		#0 bis 6
			print f[x][y],			#feldinhalt anzeigen
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
		zeichne(f)
		#Eingabe...
		break

main()
