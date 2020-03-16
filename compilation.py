import re
from prettytable import PrettyTable

t =  PrettyTable(["ChaineEntre", "Pile","Action"])

def premierTerminalDansLaChaine(s):
	for terminal in terminaux:
		if s.find(terminal) == 0 :
			return terminal

def premierNonTerminalDansLaPile(s):
	for nonterminal in nonTerminaux:
		if pile.find(nonterminal) == 0 :
			return nonterminal

def indicePremierNonTerminalDansLaPile(s):
	indicePlusPetit = 10000
	for nonterminal in nonTerminaux:
		if s.find(nonterminal) <indicePlusPetit and s.find(nonterminal)!= -1 :
			indicePlusPetit = s.find(nonterminal)
	return indicePlusPetit


grammaire = [	
				["<programme>", "main(){<liste_declarations><liste_instructions>}"],	
				["<liste_declarations>", "<une_declaration><liste_declarations>", ""],
				["<une_declaration>", "<type>id"],
				["<liste_instructions>", "<une_instruction><liste_instructions>", ""],
				["<une_instruction>", "<affectation>", "<test>"],
				["<type>", "int", "float"],
				["<affectation>", "id=nombre;"],
				["<test>", "if<condition><une_instruction>else<une_instruction>"],
				["<condition>", "id <operateur> nombre"],
				["<operateur>", "<", ">", "=", "!="]
			]

terminaux=["main(){", "}", "id", "int", "float", "=" , "nombre", "if", "else",";", "<", ">", "!=", "$"]

nonTerminaux= ["<programme>","<liste_declarations>","<une_declaration>",
				 "<liste_instructions>","<une_instruction>","<type>","<affectation>",
				 "<test>","<condition>", "<operateur>"]

table_analyse =  {
	"<programme>main(){" 		:"main(){<liste_declarations><liste_instructions>}",
	"<liste_declarations>}" 	:"",
	"<liste_declarations>id" 	:"",
	"<liste_declarations>int" 	:"<une_declaration><liste_declarations>",
	"<liste_declarations>float" :"<une_declaration><liste_declarations>",
	"<liste_declarations>if" 	:"",
	"<une_declaration>int" 		:"<type>id",
	"<une_declaration>float" 	:"<type>id",
	"<liste_instructions>}" 	:"",
	"<liste_instructions>id" 	:"<une_instruction><liste_instructions>",
	"<liste_instructions>if" 	:"<une_instruction><liste_instructions>",
	"<une_instruction>id" 		:"<affectation>",
	"<une_instruction>if" 		:"<test>",
	"<test>if" 					:"if<condition><une_instruction>else<une_instruction>",
	"<type>int" 				:"int",
	"<type>float"				:"float",
	"<affectation>id" 			:"id=nombre;",
	"<condition>id" 			:"id<operateur>nombre",
	"<operateur>=" 				:"=",
	"<operateur><" 				:"<",
	"<operateur>>" 				:">",
	"<operateur>!=" 			: "!="
	
	
}

pile = "<programme>$"

chaineInput = "main(){id=nombre;}$"
chaineInput = raw_input("het chaine")
action=""
while (chaineInput != "$" or pile != "$" ):

	if (indicePremierNonTerminalDansLaPile(pile) == 0 ):
		pnt = premierNonTerminalDansLaPile(pile)
		pt = premierTerminalDansLaChaine(chaineInput)
		try:
			action = "VIDE" if len(table_analyse[pnt+pt])==0 else table_analyse[pnt+pt] 
			t.add_row([chaineInput ,  pile, pnt +" ::= "+ action  ]  )
			pile = table_analyse[pnt+pt] + pile[len(pnt):]
		except :
			print t
			print "Erreur : Chaine Refuse!"
	else:
		pt = premierTerminalDansLaChaine(chaineInput)
		if( pt == pile[0:len(pt)] ):
			t.add_row([chaineInput ,  pile, ""])
			pile = pile[len(pt):]
			chaineInput = chaineInput[len(pt):]
			action =""
		else :
			print t
			print "Erreur : Chaine Refuse!"

			a = raw_input()
	
t.add_row([chaineInput ,  pile, ""  ]  )
print t
print "Chaine accepte"


	