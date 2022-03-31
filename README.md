# wordle-solver
As I was playing Wordle one day, I thought to myself, "What would happen if you knew every word ever and was able to make no mistakes at all? So I made one!




## How To Use
Pull the GitHub repository and then begin editing ```wordle_solver.py```. In the project there are three main objects: ```Game```, ```Lab``` and ```RoboPlayer``.





## Game Example
If you run this:
```python
wordle_game: Game = Game(RoboPlayer(first_word='irate', second_word='nymph'))
wordle_game.start()
```
The console outputs this:
![Game Picture](https://github.com/faroukcharkas/wordle-solver/blob/master/assets/game_picture.png?raw=true)





## Lab Example
If you run this:
```python
wordle_lab: Lab = Lab(iterations=25, first_word='adieu', second_word='lucky')
wordle_lab.run()
```
The console outputs this:
![Lab Picture](https://github.com/faroukcharkas/wordle-solver/blob/master/assets/lab_picture.png?raw=true)





## Objects In-Depth

```RoboPlayer(str first_word, str second_word)```  ----   This is the robotic player of the game. Only to be used with the ```Game``` object. All output from this object is tagged ```[PLYR]``` in the console. Pass in an optional ```first_word``` and ```second_word``` argument to give the Wordle game a default first and second guess.

```Game(RoboPlayer player)```  ----  is the game version of the Wordle solver. Will log everything, and provide real-time guesses. Not built to test out Wordle combinations, but merely as entertainment. If you would like to run Wordle games at a larger scale use the ```Lab``` object. Pass in a ```RoboPlayer``` object to configure the game.

```Lab(int iterations, str first_word, str second_word)```  ----   is the lab version of the Wordle solver. Will not log everything, just data. Built to test out Wordle combinations at a large scale. Logs a run-by-run output. If you want to watch the computer guess, use the ```Game``` object. Pass in ```iterations``` for how many times you want the game to run. Pass in the optional ```first_word``` and ```second_word``` arguments to give the worlde system a default first and second guess to use everytime.
