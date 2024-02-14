# Scribbl - The $30 full-featured smartwatch
> NOTE: This project is still considered a work-in-progress. Keep an eye out for new improvements and features!

## Features
- Bluetooth 5 LE
- 2.4GHz Wi-Fi
- Type-c connector
- Touchscreen
- Gyroscope and accelerometer
- Fully programmable!

## Directions
### These directions are rather lengthy, but only because I explained each step in a lot of detail. If you think you get it, you probably do.

To build the Scribbl watch, first consult the bill of materials below. You will need to order 2 parts (about $30 before tax, as of Feb 2024) and have access to a 3D printer.

> 💡 3D printers are actually more commonplace than you might think - your local school or library probably has one. If not, you can always pay to have the parts printed for you through an online service. If you own a 3D printer, you will likely know that filament is dirt cheap, hence why the project is so heavily reliant on it.

⬇️ First, download the watch case I have designed. You can find the model files under the STL folder and labeled as "container.stl" and "cover.stl". You will also need to download "pin.stl" (__which will be printed multiple times__ - I recommend 4, but skip down a bit for more info). The model is designed to "just fit" - the tolerances have been carefully set so that all parts fit snugly together and there are no screws required. Additionally, download the watch strap designed by ibudmen and linked below. You will need a Thingiverse account to use the customizer, or you can download the .scad file (also copied under the STL folder) and use a suitable program to modify it as described below.

🖨️ Next, print the model. If you are an experienced printer, simply know that just about any settings will do - have fun. Otherwise, I will now explain in depth how to 3D print an object. First, download a program like Cura (what I use, it's free and open source). Next, simply drag and drop your .stl file into the program. You may see some settings on the right - you shouldn't need to mess with them to print this well. Click the blue "Slice" button in the bottom right corner. "Slicing" the print means splitting it up into thin layers which will be printed layer-by-layer by the printer. When you're done, save the file (bottom right corner) to an external SD/MicroSD card that you will then put in the printer. If you are borrowing a printer, please read the instructions for that printer or ask someone to assist you in getting the print started. Honestly, most printers should be fairly intuitive to use after you put the MicroSD card in.

Getting tired of reading yet? Because I'm getting a bit tired of writing this!

🔬 The next step is to place the Waveshare board (or display module, whatever you want to call it) into the cover model. This way it will be easier to fit. Place the battery in the case, taking care to note where extra space is given for the wire. Plug the battery into the matching port on the Waveshare board, and attach the 2 pieces together (taking care to note where the USB-C port goes). Almost there!

😡 Finally, after all that, you still have one last challenge to overcome - the pins. I designed them to account for error by the 3D printer, so they are larger than they should be by default. Trim off (carefully) with scissors any excess that printed funny (fatter than the rest) and repeat this until the pin is just wider than the space between the pegs (technically called the "lugs") that are designed to accept it on the watch. You will likely mess up several times, so I recommend you print 4 pins or more to start. They cost $0.00 to print (according to Cura), so don't feel bad. Next, put 1 pin into each of the half-watch-bands and force the straps into the lugs.

:tada: You now have a $30 watch with all of the modern tech you'd expect!


## Materials
#### Must be bought
- [Touch-display + chip combo](https://cad.onshape.com/documents/df6f08e5f62cd6d70542b14d/w/1ab66002cb82fdc373f192e6/e/c2b169e66e06287716c78e38) - $22
  - This can be bought from Waveshare directly, but I recommend getting it from [Amazon](https://www.amazon.com/gp/product/B0CM6JCJ2H/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) as it is roughly the same price after shipping/tax.
  - [Battery](https://www.amazon.com/dp/B0BJPG4B72?psc=1&smid=A3FKMD6P089KQA&ref_=chk_typ_imgToDp) - $10
    - You can use a different battery, but it needs to have an MX1.25 connector and you will have to redesign the case. Honestly, it's not worth it as larger capacity batteries are also much larger in size.
#### 3D printed
-  [Watch Case (3 parts)](https://cad.onshape.com/documents/df6f08e5f62cd6d70542b14d/w/1ab66002cb82fdc373f192e6/e/c2b169e66e06287716c78e38)
    - You will also need to print several of the pins I designed as well. Due to slight inaccuracies in 3D printing, I have designed them to be larger than needed. Simply cut a little bit off until the pins are just longer than the width between the slots on the watch they fit into.
-  [Watch strap (not designed by me)](https://www.thingiverse.com/thing:87132)
    - Use customizer (click "customize" in the bottom left corner of the model page) with 22mm width, 1.2 pin radius, pick your length
