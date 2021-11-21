# Biased Sphinx-Ball

## How to build the artefact
1. Get the following technical equipment:
2. Get your laser cutting file from here: https://de.makercase.com/ (we choose the polygonbox with 14,6 cm diameter/height and 6mm thickness)
3. Download the file, open it in a vector graphic programm (if you have nothing else available, PowerPoint works). To the side of the box, add holes for: speaker, micorophone, powersupply, and display. To do this, take the measurements of the units beforehand.
4. For a nice look, you may add a name logo and graphics as you like.
5. Do the cutting (we worked with a laser cutting machine)
6. Put the different parts together: We used wood glue to stick the individual parts together. Don't glue on the last side, e.g. the top, to be able to manipulate the hardware inside.
7. For some of the hardware components, you may have to do some soldering before you can install them. (Watch this, to know how: https://www.youtube.com/watch?v=6rmErwU5E-k )
8. Connect the Display, the gyro sensor, the speaker and the microphone with your Raspberry Pi and put all of it in the box. For a detailed instruction click [here](#how-too-wire-everything-correct).
9. Close the model with the last part.
10. Voila!


## How to wire everything correct

Hardware we used:
- Raspberry Pi 3 Model B+ 
- Gyroscope: MPU6050
- Display: Grove-LCD RGB Backlight V4.0

To connect the Gyroscope and the Display we used the [I<sup>2</sup>C](https://en.wikipedia.org/wiki/I%C2%B2C) bus.
The I<sup>2</sup>C consist of two pins, the SDA & SCL. Sadly the Pi only has only one SDA and SCL pin, therefore
we need to add one I<sup>2</sup>C bus to the Pi. We followed [this](https://www.laub-home.de/wiki/Raspberry_Pi_multiple_I2C_bus) instruction.
Connect the display to the Pi and the gyroscope and enjoy!

## Nice to know
[Markdown](https://www.markdownguide.org/basic-syntax/)

[JSON](https://developer.mozilla.org/de/docs/Learn/JavaScript/Objects/JSON#json_struktur)

