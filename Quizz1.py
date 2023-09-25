## Add Jokers and Fallback-Questions 

##Usage of Classes for learning purposes...

### First Class - Player
## A player has 2 attributes. name and difficulty. Difficulty is chosen by the player itself: 1..easy, 2..medium, 3..hard
## Ideas for implementations( The player has 2 Jokers. To call for a Joker enter J for "Joker". The moment a player calls a Joker, a fallback-question Q3/Q1 is no longer a fallback-question.)

### Second Class - Game
## iterates through chosen library, depends on topic and difficulty


##Operationg System Library, for functions visit https://docs.python.org/3/library/os.html
# used for clearing the command line with os.system('cls')
## ascii_lowercase imports abcdefghijklmnopqrstuvwxyz
import os
from string import ascii_lowercase
import random

## global Variables
available_jokers=["Publikumsjoker","50/50"]


setup_gametopic1="Technik"
setup_gametopic2="Harry Potter"

###Topic1
Level_1_Topic1={"Das US-Militär schuf 1942 das 'Manhattan Project'. Was war das Ziel der beteiligten Wissenschaftler?":
                 ["der Bau der Atombombe","der Bau einer Weltraumrakete","die erste Mondlandung","ein sehr kleines Speichergerät, um geheime Dateien leichter austauschen zu können"],
                 "Die erste brachbare elektrische Lampe wurde 1879 patentiert. Wem gehörte das Patent, obwohl stritting war, wer die Glühbirne erfand?":
                 ["Thomas Edison","James Watt","Nikola Tesla","Heinrich Göbel"],
                 "Welcher Astronaut flog am 12.April 1961 als erster Mensch überhaut ins All?":
                 ["Juri Gagarin","Neil Armstrong","Buzz Aldrin","Sergej Krikaljov"],
                 "Aus wie vielen Bit besteht ein Byte?":
                 ["8","24","64","124"],
                 "Eine Pferdestärke ist die Kraft, die benötigt wird, um ein bestimmtes Gewicht in einer Sekunde um einen Meter zu bewegen. Wie hoch ist dieses Gewicht?":
                 ["75 kg","25 kg","100 kg","50 kg"]}

Level_2_Topic1={"Wie lautet der Oberbegriff für die physischen Komponenten eines datenverarbeitenden Systems ?":
                 ["Hardware","Software","Daten","Programme"],
                 "Wie viele Megabyte sind ein Terabyte ":
                 ["1.000.000","100.000","10.000","1.000"],
                "Auf welchem optischen Prinzip basiert die Technik der Lichtleitung in Glasfaserkabeln?":
                 ["Reflexion","Streuung","Beugung","Brechung"],
                 "Welche dieser Abkürzungen steht für Wechselstrom?":
                 ["AC","WS","DC","PS"],
                  "1984 wurde versucht das 'Tetromino'-Puzzle auf den Computer zu übertragen. Das Puzzle wurde verbessert und für den Computer programmiert. Wie heißt der Programmierer ?":
                 ["Aleksej Pajitnov","Shigeru Miyamoto","Hironubu Sakaguchi","Gunpei Yokoi"]}

Level_3_Topic1={"Welche Technik hat die Erfindung des Transistors 1948 ermöglicht?":
                 ["Halbleiter","Elektromotor","Generator","Rotationswandler"],
                 "Woraus wird das beispielsweise für die Chipherstellung benötigte Silizium gewonnen?":
                 ["Sand","Bauxit","Basalt","Löss"],
                 "Welche Strahlung empfängt die Wärmebildkamera ":
                 ["Infrarotstrahlung","Röntgenstrahlung","UV-Strahlung","Beta-Minusstrahlung"],
                 "Was ist die Masse von einem Photon":
                 ["ein Photon hat keine Masse","9,11 * 10^(-31) kg","1,67 * 10^(-27) kg"," 0.0005 g"],
                 "Eine Entgleisung ist ein Eisenbahnunfall, bei dem ein Schienenfahrzeug seine spurführende Bahn, das Gleis, unkontrolliert verlässt. Nach welchem Wissenschaftler wurde die Gleichung zur Beechnung des Entgleisungskoeffizienten benannt.":
                 ["Gleichung nach Nadal","Gleichung nach Djokovic","Gleichung nach Federer","Gleichung nach Hertz "]}

###Topic2
Level_1_Topic2={ "Wie heißt der Autor von Harry Potter ?":
                 ["J.K. Rowling","J.R.R. Tolkien","Stephen King","Sebastian Fitzek"],
                 "Mit welchem ​​Zauber hat Harry Lord Voldemort getötet?":
                 ["Expelliarmus","Patronum Expecto","Avada Kedavra","Accio"],
                 "Wie viele Harry Potter Bände gibt es":
                 ["7","6","5","8"],
                 "Welches magische Talent teilt Harry mit Voldemort?":
                 ["Ein Parselmund sein","Ein Animagus sein","Ein Auror sein","Ein Todesser sein"],
                 "Wie heißt Hagrids dreiköpfiger Hund, der den Stein der Weisen schützt?":
                 ["Flaumig","Hedwig","Nagini","Fluffy"],
                "Wovor hat Ron Weasley ganz besonders große Angst?":
                 ["Spinnen","Ratten","Schlangen ","Katzen"]}

Level_2_Topic2={"Beim ersten Treffen des Duell-Clubs rief Draco Malfoy welches Tier mit dem Zauber 'Serpensortia' herbei?":
                 ["Schlange","Drache","Frosch","Fledermaus"],
                 "Harry Potter stammt aus einer der ältesten Zaubererfamilien. Was wurde über Generationen hinweg in seiner Familie vererbt?":
                 ["der Tarnumhang","zweiter Vorname","die Karte des Rumtreibers","Dobby, der Hauself"],
                 "Wer hat einen Zentauren davor bewahrt, von Professor Umbridge im Verbotenen Wald erwürgt zu werden?":
                 ["Grawp","Buckbeak","Hagrid","Luna"],
                 "Wie heißt Hagrids dreiköpfiger Hund, der den Stein der Weisen schützt?":
                 ["Flaumig","Hedwig","Nagini","Fluffy"],
                 "Wie hieß der Hauself der schwarzen Familie?":
                 ["Kreacher","Dobby","Winky","Hockey"],
}

Level_3_Topic2={"'Witz über alle Maßen ist der größte Schatz des Menschen' lautet das Motto von welchem ​Haus?":
                 ["Ravenclaw","Gryffindor","Hufflepuff","Slytherin"],
                 "Welche Position spielt Harry in seinem Quidditch-Team?":
                 ["Sucher","Hüter","Chaser","Klatscher"],
                 "Albus Dumbledore hat welchen Horkrux zerstört?":
                 ["Marvolo Gaunts Ring","Slytherins Medaillon","nagini","Hufflepuffs Tasse"],
                 "Wie heißt das von Dementoren bewachte Zaubergefängnis ?":
                 ["Askaban","Sabaneta","Shell Cottage","Winkelgasse"],
                 "Wie heißt der Trank, der es einer Person ermöglicht, die Gestalt einer anderen Person oder Kreatur anzunehmen?":
                 ["Vielsafttrank","Weinrautenessenz","Murtlap-Essenz","Euphorie-Elixier"]}


# Definig the faculty of a number
def fak(n):
  if n <=1:
    return 1
  else:
    return (n*fak(n-1))

# Defining a function to round a number to a decimal point
def rounding(n,q):
    number=n
    digits=0
    before_comma=0
    rounded_number=0
    list=[]
    #counts the digits of the number
    #// floor division, rounds the result to the nearest whole number 12//5 --> 2
    while number !=0:
        number//=10
        digits+=1

    #cheks if input is correct
    if q>digits:
        return "False Input. q cannot be bigger than number of digits!!"
    
    #example: n=1234.56 --> generates list=[0.56,4,30,200,1000]
    #% modulus operator, returns the rest of a devision 13 % 5 --> 3
    for nth_digit in range(digits):
        x=int( (n / 10**nth_digit) % 10) *10**nth_digit
        list.append(x)
        before_comma += x
    list.insert(0,n-before_comma)

    #example for n=1234.56 and q=3 --> cheks if 34 > 50 , 
    # if TRUE--> list doesnt change and rounded number contains added numbers of list FROM index q TO last element of list
    # if FALSE--> list changes at index q (here+100) and rounded number contains added numbers of list FROM index q TO last element of list
    if list[q-1] < 0.5*(10**(q-1)):
        for a in range(q,digits+1):
            rounded_number+=list[a]
    elif list[q-1] >= 0.5*(10**(q-1)):
        list[q]=list[q]+(10**(q-1))
        for a in range(q,digits+1):
            rounded_number+=list[a]
        
    return rounded_number

# list of Prizes from prizes[0]-->smallest to prizes[4]-->biggest
prizes=[0,rounding(1000000/fak(7),2), rounding(1000000/fak(6),3),rounding(1000000/fak(5),4), rounding(1000000/fak(3),6),rounding(1000000/fak(1),7)]


## First Class
## Add QUITTING AND JOKER FUNCTION !!
class Player:

  def __init__(self, name,topic,difficulty=1):
    self.name= name
    self.difficulty= difficulty
    self.topic=topic

  def joker(self,Joker):
    if a == "P":
      available_jokers.remove("Publikumsjoker")
    elif a== "50":
      available_jokers.remove("50/50")
    else:
      print("Ihre Eingabe ist falsch.Bitte versuchen Sie es erneut !")

  def quitting(self):
    pass


## Second Class
class Game:

  def Questions(self,user_topic):
    for num, (question, alternatives) in enumerate(user_topic.items(), start=1):
      print(f"\Frage {num}:")
      print(f"{question}")
      correct_answer = alternatives[0]
      labeled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives,len(alternatives))))
      for label, alternative in labeled_alternatives.items():
          print(f"  {label}) {alternative}")

      answer_label = input("\Antwort? ")
      answer = labeled_alternatives.get(answer_label)

      if answer == correct_answer:
          print(" Richtig! \n")
      else:
          print(f"Die Antwort ist {correct_answer!r}, nicht {answer!r}")
          print(f"Sie haben {prizes[num-1]} Vietnamesische Dong gewonnen!")
          break
      if answer == correct_answer and num == 5:
        print(f"Sie haben gewonnen. Sie sind stolzer besitzer von {prizes[-1]} Vietnamesischen Dong")


## This functions checks if input is correct. For user_difficulty: Allowed are numbers 1,2 and 3;For user_topic: Allowed are "T","G" or "M"

def check_user_difficulty(user_difficulty):
    try:
        player1_difficulty=int(user_difficulty)
        if player1_difficulty !=1 and player1_difficulty !=2 and player1_difficulty!=3 :
            print("Eingegebenes Level nicht korrekt. Wählen Sie Level1 --> 1, Level2 --> 2 oder Level3 --> 3 aus!")
            player1_difficulty=input("Auf welchem Level wollen Sie dieses Quizz spielen ? (1/2/3)")
            check_user_difficulty(player1_difficulty)
    except ValueError:
        print("Eingabe ist keine Zahl! Versuchen Sie es erneut!")
        player1_difficulty=input("Auf welchem Level wollen Sie dieses Quizz spielen ? (1/2/3)")
        check_user_difficulty(player1_difficulty)
   
def check_user_topic(user_topic):
      global Expertengebiet
      if user_topic !=setup_gametopic1[0] and user_topic !=setup_gametopic2[0] :
          print("Eingabe nicht korrekt. Wählen Sie '{first_letter_1}' für {first} oder '{first_letter_2}' für {second} ".format(first=setup_gametopic1,second=setup_gametopic2,first_letter_1=setup_gametopic1[0],first_letter_2=setup_gametopic2[0]))
          Expertengebiet= input("\nAuf welchem der folgenden Gebiete sind Sie Experte? {first_topic} oder {second_topic}? ({first_letter_topic1}/{first_letter_topic2})".format(first_topic=setup_gametopic1,second_topic=setup_gametopic2,first_letter_topic1=setup_gametopic1[0],first_letter_topic2=setup_gametopic2[0]))
          check_user_topic(Expertengebiet)
      else:
        if user_topic == setup_gametopic1[0]:
          Expertengebiet=setup_gametopic1
        else: 
          user_topic == setup_gametopic2[0]
          Expertengebiet= setup_gametopic2


## Start of the Game, Player has to input Name, Age(0-100) and Level of difficulty (1-3)
player1_name=input("Geben Sie Ihren Namen ein!")

player1_difficulty=input("Auf welchem Level wollen Sie dieses Quizz spielen ? (1/2/3)")
check_user_difficulty(player1_difficulty)


## Game description for the player
os.system("cls")

## Jokers can be added for further improvement of the Game
#print("\nWillkommen bei DEM Quizz. Das elftbeliebtestebeliebteste Quizz der südlichen Hemispähre.\n Das Quizz ist wie folgt aufgebaut:\n\n 1) Es werden 5 Fragen gestellt. Die erste und dritte Frage sind Sicherheitsfragen, das heisst, dass nach erfolgreicher Beantwortung der ersten bzw. dritten Frage ein Preisgeld garantiert ist. Eine Ausnahme bei den Sicherheitsfragen bilden die Joker.\n\n 2)Sie erhalten 2 Joker: den Publikumsjoker, sowie den 50/50 Joker. Wird der erste Joker verwendet, ist Frage 3 kein Sicherheitsfrage mehr. Wird der zweite Joker verwenden, haben Sie keine Sicherheitsfrage mehr.\n\n 3) Preisgelder werden folgenermaßen vergeben:\n 1 Frage: {prize1} Vietnamesische Dong\n 2 Frage: {prize2} Vietnamesische Dong\n 3 Frage: {prize3} Vietnamesische Dong\n 4 Frage: {prize4} Vietnamesische Dong\n 5 Frage: {prize5} Vietnamesische Dong     ".format(prize1=prizes[1],prize2=prizes[2],prize3=prizes[3],prize4=prizes[4],prize5=prizes[5]))
print("\nWillkommen bei DEM Quizz. Das elftbeliebtestebeliebteste Quizz der südlichen Hemispähre.\nFolgende Preisgelder können je nach Fortschritt gewonnen werden: \n 1 Frage: {prize1} Vietnamesische Dong\n 2 Frage: {prize2} Vietnamesische Dong\n 3 Frage: {prize3} Vietnamesische Dong\n 4 Frage: {prize4} Vietnamesische Dong\n 5 Frage: {prize5} Vietnamesische Dong     ".format(prize1=prizes[1],prize2=prizes[2],prize3=prizes[3],prize4=prizes[4],prize5=prizes[5]))

## Asks player for wanted Topic
Expertengebiet= input("\nAuf welchem der folgenden Gebiete sind Sie Experte?{first} oder {second}? ({first_letter_1}/{first_letter_2})".format(first=setup_gametopic1,second=setup_gametopic2,first_letter_1=setup_gametopic1[0],first_letter_2=setup_gametopic2[0]))
check_user_topic(Expertengebiet)

player1=Player(player1_name,Expertengebiet,player1_difficulty) 

os.system("cls")

print("Los gehts, {Name}!. Das Quizz auf dem Gebiet '{Gebiet}' auf Level {Level} wird geladen!".format(Name=player1.name, Gebiet= player1.topic, Level=player1.difficulty))
input("Drücken Sie eine beliebige Taste für 'weiter' !")

os.system("cls")


## Loading the Questions from Game class, dependend on chosen Topic --> jumps to class 2,3 or 4

chosing_topic={setup_gametopic1:
               [Level_1_Topic1,Level_2_Topic1,Level_3_Topic1],
               setup_gametopic2:
               [Level_1_Topic2,Level_2_Topic2,Level_3_Topic2],
               }

library_chosen_topic=chosing_topic[player1.topic][int(player1.difficulty)-1]
Game().Questions(library_chosen_topic)

