'''2-Implement a class called player that represents a cricket player.The Player calss should have a method called play() which prints "The player is playing cricket.Derive two classes, Batsman and Bowler,from the Player class.Override the play() method in each derived class to print"The batsman is batting" and "The bowler id bowling", respectively.Write a program to create objects of both the Batsman and bowler classes and cell the play() method for each object,''' 

#define the base class player
class player:
   def play(self):
      print("The player is playing cricket.")

#define the derived class Batsman
class Batsman(player):
   def play(self):
     print("The batsman is batting.")

#define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling")

#creat objects of batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()



