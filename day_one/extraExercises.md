Exercise 1. Avoiding Duplicates.

Avoiding Duplicates In this exercise, you will create a program that reads words from the user until the user enters “quit”. After the user enters a blank line your program should dis- play each word entered by the user exactly once. The words should be displayed in the same order that they were entered. 
For example, if the user enters:
```
first 
second 
first
third 
second
```

then your program should display: 
```
first 
second 
third
```

Exercise 2. Shuffling a Deck of Cards.

A standard deck of playing cards contains 52 cards. Each card has one of four suits along with a value. The suits are normally spades, hearts, diamonds and clubs while
the values are 2 through 10, Jack, Queen, King and Ace.
Each playing card can be represented using two characters. The first character is
the value of the card, with the values 2 through 9 being represented directly. The characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack, Queen, King and Ace respectively. The second character is used to represent the suit of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for clubs. The following table provides several examples of cards and their two-character representations.

```
Card               Abbreviation
Jack of spades     Js
Two of clubs       2c
Ten of diamonds    Td
Ace of hearts      Ah 
Nine of spades     9s
```

Begin by writing a function named createDeck. It will use loops to create a complete deck of cards by storing the two-character abbreviations for all 52 cards into a list. Return the list of cards as the function’s only result. Your function will not take any parameters.

Write a second function named shuffle that randomizes the order of the cards in a list. One technique that can be used to shuffle the cards is to visit each element in the list and swap it with another random element in the list. You must write your own loop for shuffling the cards. You cannot make use of Python’s built-in shuffle function.
Use both of the functions described in the previous paragraphs to create a main program that displays a deck of cards before and after it has been shuffled. Ensure that your main program only runs when your functions have not been imported into another file.


Exercise 3. Random Lottery Numbers.

In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random selection of 6 numbers for a lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates. Display the numbers in ascending order.

Exercise 4. Formatting a List.

When writing out a list of items in English, one normally separates the items with commas. In addition, the word “and” is normally included before the last item, unless the list only contains one item. Consider the following four lists:
```
apples
apples and oranges
apples, oranges and bananas
apples, oranges, bananas and lemons
```
Write a function that takes a list of strings as its only parameter. Your function should return a string that contains all of the items in the list formatted in the manner described previously as its only result. While the examples shown previously only include lists containing four elements or less, your function should behave correctly for lists of any length. Include a main program that reads several items from the user, formats them by calling your function, and then displays the result returned by the function.

