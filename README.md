# SES (Sam-Edward-System)
A temporary name for a system similar to SMITE’s VGS, Overwatch’s communication ping system, or similar functions for the purpose of communicating without relying on the players’ voice or auditory perception. Hopefully, we can include all of those for the sake of more customization.

## Current Goal 
To send a message across the network to clients specified as the same party with customized controls using either series of buttons like VGS, a communication wheel similar to one from Overwatch, or simply a specified key combination or keystroke. Naturally, this would mean that the other end must be able to receive it and display it on the screen, preferably as an overlay similar to Overwolf, Steam, or Discord.

## Steps to Achieving the Goal
- [X] Create a simple app that detects your specified keystroke even if your window focus is on your game.
- [X] Output the detections (example: pressing numpad 6 three times while in a game)
- [X] Allow user customization to say something else such as “The enemy is on the left.” instead of “numpad 6 has been pressed” as well as allowing other commands such as VGS or communication wheel (which involve using the mouse).
- [X] Create server and client so that it may send messages over.
- [X] Experiment and improve functionality and add more customizations.
- [ ] ~~Allow the output to show as an overlay rather than in a terminal or any external window.~~

___________________________________

To use the app, type python3 main.py while in the directory.
If it say no module named 'pynput' then type 'pip install pynput'
Similarlly, use 'pip3 install discord-webhook' if it say it lacks this.
