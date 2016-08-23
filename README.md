For this project, your mission is to write a program that plays the game of Hangman. So cool, huh?

Objectives.
The project is structured to sharpen your knowledge with functions, strings, lists and dictionaries,  programing designs, problem solving, code reusability, and development. 
You can extend your program to use files, multiple classes and even graphics. The main program is however basic without the extensions.

How to play.
When the user plays Hangman, the computer first selects a secret word at random from a list built into the program. The program then prints out a row of dashes—one for each letter in the secret word—and asks the user to guess a letter. If the user guesses a letter that is in the word, the word is redisplayed with all instances of that letter shown in the correct positions, along with any letters correctly guessed on previous turns. If the letter does not appear in the word, the user is charged with an incorrect guess. 
The user keeps guessing letters until either:
the user has correctly guessed all the letters in the word or
 the user has made eight incorrect guesses. 
Two sample runs that illustrate the play of the game are shown in Figure 1 on the next page. When it is played by children, the real fascination (a somewhat morbid fascination, I suppose) from Hangman comes from the fact that incorrect guesses are recorded by drawing an evolving picture of the user being hanged at a scaffold. For each incorrect guess, a new part of a stick-figure body—first the head, then the body, then each arm, each leg, and finally each foot—is added to the scaffold until the hanging is complete. For example, the three diagrams below show the drawing after the first incorrect guess (just the head), the third (the head, body, and left arm), and the diagram at the tragic end of a losing game:


In order to write the program that plays Hangman, you should design and test your program in three parts. The first part consists of getting the interactive part of the game working without any graphics at all and with a fixed set of secret words. The second part consists of creating a separate file(or maybe in same file) that maintains the scaffold diagrams and adds features accordingly. The final part requires you to replace the supplied version of the secret word list with one that reads words from a file(not necessarily from a file). The rest of this handout describes these three parts in more detail.

Figure 1. Two sample runs of the Hangman program (console only):


Note that your program only needs to be able to play the Hangman game once through (i.e., the player guessing one word), but it should be pretty easy to extend your program to allow the player to play multiple rounds (i.e., guessing a word multiple times). 

Part I—Playing a console-based game
In the first part of this project your job is to write a program that handles the user interaction component of the game—everything except the graphical display. To solve the problem, your program must be able to:
Choose a random word to use as the secret word. That word is chosen from a word list, as described in the following paragraph. 
Keep track of the user’s partially guessed word, which begins as a series of dashes and then gets updated as correct letters are guessed. 
Implement the basic control structure and manage the details (ask the user to guess a letter, keep track of the number of guesses remaining, print out the various messages, detect the end of the game, and so forth). 
Representing the list of words from which you can choose a word at random. For the first two parts of the project, you will simply make use of simple strings(words) from a self-created list you to test your program. (A lexicon is very much like a dictionary, but does not necessarily include definitions, which makes it a more appropriate name for a class that provides a list of words with no associated meanings.) 
In Part III(This is a project extension), you will replace the definition we’ve provided with one that reads a list of words from a data file. The strategy of creating a temporary implementation that provides enough functionality to implement the rest of the program is a common technique in programming. Such temporary implementations are usually called stubs. In this project, there is no starter code and  this is thus the real test of problem solving. 

A game that used this implementation of a small list would quickly become uninteresting because there are only few words available. Even so, it will allow you to develop the rest of the program and then come back and improve this part later. Part I is a string manipulation problem using the string functions learnt. The sample runs in Figure 1 should be sufficient to illustrate the basic operation of the game, but the following points may help to clarify a few issues:
You should accept the user’s guesses in either lower or upper case, even though all letters in the secret words are written in uppercase.
If the user guesses something other than a single letter, your program should tell the user that the guess is illegal and accept a new guess.
If the user guesses a correct letter more than once, your program should simply do nothing. Guessing an incorrect letter a second time should be counted as another wrong guess. (In each case, these interpretations are the easiest way to handle the situation, and your program will probably do the right thing even if you don’t think about these cases in detail.)
Remember to finish Part I before moving on to Part II. Part II is arguably more fun, but it is essential to develop large programs in manageable stages.

Part II—Adding graphics
For Part II, your task is simply to extend the program you have already written so that it now keeps track of the Hangman graphical display. Although you might want to spice things up in your extensions, the simple version of the final picture for the unfortunate user who has run out of guesses looks like this:

The easy way to go around it is to create a file, let’s say hangman_pics.py. The file should only contain different symbol strings(pictures) (8 of them) of a man hang at different levels. 
Hint: Import the file in your main hangman file and make use of the pictures at the appropropriate  levels. This will make your code look cleaner, be more comprehensive and better in design.

Part III—Reading the lexicon from a data file.

This part of the project is not compulsory but it is pretty cool, please make the effort.
Learn a few file functions and incorporate your file skills here. Create a separate file that contains a lot of words(as many as possible. You can download files online with over a thousand words). Instead of checking words from your self-created list, now check them from your lexicon, probably no word guessed will be missing this time. 

Yaaay!!!! You are halfway through the course!!!! Congratulations!!!!


# Advanced-Tracks-Activity-
Solved activities/koans
