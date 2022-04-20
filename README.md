# bbs-auto-bot [OUTDATED/UNMAINTAINED]
A bot that autos PvE content in Bleach Brave Souls so you don't have to

This bot is still in alpha development stage, meaning this bot doesn't have a GUI yet. it's still command line based. While it works just fine, there's a few extra steps needed to get it running. As of now, it only works with story mode farming. More will be added later

## Prerequisites:
Have python installed. You can grab the installer, if you don't have it already, [here](https://www.python.org/downloads/)

## How to run:
1. Download the files of this repo
   - Locate the green button at the top of this page that says **'code'** or something similar
   - Click it, then click the download zip option
2. Extract the zip file and open the folder it was extracted to
3. Click the address bar (where you see some folder names, with the last one being the name of the folder you are currently in) and copy the text. We will need it in a bit.
4. Open a command prompt window
   - open start menu
   - search command prompt
   - click it to open a new window
5. Navigate to where the bot files are located
   - type `cd ` (including the space)
   - right click to paste the text we copied earlier
   - press enter
6. In the folder where the files are, open the file `ticketLimit.txt` and change the number to however many tickets you want the bot to spend
7. Open your emulator, and open the bleach brave souls application
8. In the command prompt window, type `python farmbot.py` and press enter to run the bot

That's it!
Once you have it running, it'll run in the background and do all it needs to do. For subsequent runs you will only need to start at step 3.

## A few things to note:
- You will need to have a character that can auto the story content. Any level 200 character should do just fine. As this is not a mod, if your character can't auto the content, the bot cannot help you with that.

- Your emulator window needs to be the window in focus and not covered by any other windows or minimised.

- As the bot uses simulated clicks to work, you can't really use your PC while it runs, since it will keep clicking out of whatever you're doing. It's designed to be left running, e.g while you're asleep or at work

- You need to be on the story page (where you see the actual numbered story quests) for it to work. It will handle transitioning from there, but it needs to start there.

- If it doesn't initially work (nothing appears to be happening), it's probably due to window size, a limitation of the image recognition software I'm using.
  - Easiest way to fix this would be to open the game in the emulator and make sure it's on the homepage (where you see your team, as well as the quests and brave battles buttons)
  - Then you wanna modify `findTest.py` (right click the file and open using notepad)
  - Find the line that has the line `usePath = "assets\story_previous_area_button.png"` and replace it with `usePath = "assets\homepage_quest_button.png"`
  - run `python findTest.py` and it'll start printing in the console either `Not found` or some coordinates.
  - If it's the latter, you're good to go. If it's the former, resize the window until it starts printing coordinates, allowing a few seconds between resizes. Once you get coordinates, you can go back to running `python farmbot.py` and it should work

- Also note that you need to change the number in `ticketLimit.txt` to reflect how many tickets you want the bot to spend.

- Finally, as mentioned earlier, this is alpha software, some bugs are to be expected. Fortunately, bugs in this bot simply mean it will stop working. It cannot do erroneous clicks like accidentaly entering brave battles or spending orbs, as it does not have the functionality to do so (the biggest benefit to using image recognition, and the whole reason I chose this over coordinate and based macros that most emulators have built in)

Feel free to raise issues telling me if something goes wrong, and I will have a look! Also, expect more features to be added down the line. Enjoy!
