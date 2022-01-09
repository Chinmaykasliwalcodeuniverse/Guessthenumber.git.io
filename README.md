![ckc-unique-abstract-geometric-vector-260nw-2023024259](https://user-images.githubusercontent.com/96693041/148673911-a46694d7-8653-40b3-b31a-24a8aa21b249.jpg)
# Guess The Number
 


𝟙  ⓶  ⑥ ⁶ ㏣ ㋃ ㍜ ⓸ ❹ ➃ ➍ Ч ч ♶

![Logo](https://media.giphy.com/media/r7FYh3xQvTlbLexZT3/giphy.gif) ##  Requirements

| objects             | requirement                                                                |
| ----------------- | ------------------------------------------------------------------ |
|  installation |  modules |
|  modules | Speak modules |
|  Wikipedia | Browser |



## 💻 Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`Python, modules `

`VS CODE`




![Logo](https://media.giphy.com/media/IedrY2VP5IO5ivDQAD/giphy.gif) 


## 🚀 About Me
I'm a full stack developer...
🎮Game developer....
👨‍💻software developer


## Documentation
```bash
while(userguess != randnumber):
     userguess = int(input("enter your guess:\n"))
     guesses +=1
     if(userguess==randnumber):
        print("you guesses it right")
     else:
         if(userguess>randnumber):
          print("you guessed it wrong enter a smaller number") 
         else:
             print("you guessed it wrong enter a a larger number")


```
```bash

with open("hiscore.txt" , "r") as f:
    hiscore = int(f.read())

```
The game is simple. The user has to guess the randomly generated number that lies between the range from 1 to 100. That’s it.

Is the game that simple?

Yeah, it is.

But, there is one thing that we have to provide to the users to guess the number. That’s hints. We have to provide a message to the user saying the current guessed number is less than the correct number or the current guessed number is greater than the correct number. So that users will know in which direction they have to go.

We can make it more exciting by adding extra features like maximum number of chances to guess, increasing the range, setting a timer, etc..,

Creating the basic working game is mandatory. After it, we can add more features as discussed. So, we are going to create the basic version of the game in this section. And then we will move to add new features.

I want you to try creating the game without blindly copying the code. So, I am going to explain the algorithm first. It will help you to code yourself or understand the code quickly.

Let’s see the algorithm to create the Number guessing game.

Algorithm
Make sure you understand the algorithm before moving to the coding part.

Define the range of the numbers. By default, it’s 1-100 but you can change it as you prefer.
Generate a random integer from the above range (1-100).
Start the game by displaying the user a message saying “Guess the number from X to Y”. You may update the message as you wish.
Initialize a variable to 0 to count the total number of chances that the user has taken to guess the number correctly.
Write an infinite loop.
Ask the user to guess the number.
If the current guessed number is equal to the randomly generated number, then congratulate the user with a message as you like. An example would be “-> Hurray! You got it in 5 steps!”.
Break the loop after congratulating the user.
If the current guessed number is less than the randomly generated number, then give a message to the user saying “-> Your number is less than the random number” or a custom message having the same meaning.
If the current guessed number is greater than the randomly generated number, then give a message to the user saying “-> Your number is greater than the random number” or a custom with the same meaning.
Finally, increment the chances that the user has taken to guess.
You would have got code in your mind after seeing the algorithm. Don’t worry even if you don’t get the complete code. But, make sure you understand the above algorithm.

It’s time to get our hands to work with code. Get into the code without further ado.
The range is defined inside the __init__ method so that it can be used across the class methods.
We can easily change it in one place that changes across the app accordingly.
There is a separate method to generate the random number which follows the principle of “separate the concerns”. Here, our method has little code, but it might increase in the future.
Finally, we have used class so that every method that’s related to the game will reside inside it. And it can be easily reused in some other apps.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_Website-000?style=for-the-badge&logo=ko-fi&logoColor=white)]( https://chinmaykasliwalcodeuniverse.github.io/ChinmayKasliwal.github.io/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chinmay-kasliwal-jain-34ab421b5)

[![instagram](https://img.shields.io/badge/instagram-1DA1F2?style=for-the-badge&logo=instagram&logoColor=red)](https://instagram.com/chinmay_kasliwal03?utm_medium=copy_link)


## 🛠 Skills
 PYTHON


##  🙏🏾 Support

For support, email chnmaykkasliwal3@gmail.com or join our linkedin account.

