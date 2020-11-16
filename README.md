# controlling-pc-mouse-using-image-analysis-with-PIL-UI-with-pygame
controlling your mouse using your pc camera solely, using Pythons imaging library(PIL), user interface using pygame.
the software retrieve images from your pc camera and searches for a specific color(that is chosen by the user), if the color is recognized -the mouse curser would move acrrodingly to its position in refrence to the center of the selected screen area.

This app allows you to control the mouse using your PC camera and an object of your choice;
choose an object that has the color you would like to use - to calibrate it to the mouse moovement. **some colors might work better than others.

Open your PC camera, then open the app

the main screen of the app acts as a monitor for the user. to set up all the features you would need to use some of the keys in your keyboard. **the user needs 
to click with the mouse within the screen- this would allow the software to recieve the input of the pressed keyboard keys..

**the initial screen would not be calibrated and different sizes of one protion of your screen will apear.


first aim your camera to a position where you have some of your background in fewst colors possible ( background of a wall is very good) (you would not need the whole range/width of the cameras perspective - as when you calibrate the area of interest you would use a smaller area ).

1. with your mouse point at the middle of the area you would want to work on and then press "p" on your keyboard, you will see the montor screen changes and will show
only the area you selected.

2. 'To calibrate the center, with your 'a' (Left), 'd' (right), 'x' (down), 'w' (up), keys on your keyboard move the red circle to the middle of the monitor screen and then press 's'. 
you may then press z to make the centering circle disappear and reappear- as it is not longer required to be seen while calibration is done.

3. to set up the color of your choice for mouse movement press the 't' key - a yellow circle will apear on your monitor. take the object and place it where the yellow circle appears when pressing 't' - and press the 't' key again to calibrate the color. 
to sum- place your object where the yellow circle appears (middle of screen) and click the 't' key again, now the color of your choice is calibrated.

calibration test - to check if the calibration is good and the background isnt to similar to the color of your choice- remove your object from the background and press the 'n' key once.
The 'n' key does one scan that would appear as red circles, covering larger areas in circular positions. if a red circle turns blue and the scanning stops suddenly it means the calibration is not good and you should change your background or color of choice. if non of the circles turned blue and the scanning was completed, continue to the next step.


4. now you may press the key 'm' to start infinite scanning, once you would like to move the mouse pick up your object and place it in the scanning area, corresponding to the monitor center- the  mouse will move- if you placed your object farther to the right from the center of the selected center - the mouse would move farther right..

to stop infinite scanning mode press the key 'o' until scanning stops.
to terminate the program press the 'y' key.
to calibrate a color for mouse click use the 'l' key and calibrate similarly to the calibration in step 3.
