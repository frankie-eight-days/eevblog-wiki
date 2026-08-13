---
video_id: QwBelbAYo2Q
title: Engineering Notation on 121GW Software
url: https://www.youtube.com/watch?v=QwBelbAYo2Q
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 42, "3": 74, "4": 90, "5": 108, "6": 122, "7": 143, "8": 171}
---

**Dave Jones:** Hey everyone, just a quick video. I've been trying to add SI units to the 121GW multimeter app and I found a neat way to do it and I thought I'd show some people, so here it is. So, the old way of displaying the number would just be doing a quick value to string and

**Dave Jones:** if I run that, running, running, running, loading, loading, loading, it will take a moment to get a sample. If you do that, then you get these kind of weird, pointless numbers and while they are correct, that is 6 millivolts, you don't have any like, millisine or micro

**Dave Jones:** or whatever. So I created a class which I can wrap around any loading point or double number which will allow me to just do this. I just put it as an SI value and I do a two string and that's it. And then, as you can see, we've got the millivolts and it's sitting

**Dave Jones:** around 4 to 7 millivolts now and at the top, when I trigger the multimeter, give it some noise, then it goes up to the reading. So, this will work for micro, pico, mega, whatever and all I had to do was create this class here.

**Dave Jones:** So we just have this lookup table here which has the SI engineering notation units here, the pico, nano, micro, milli, kila, mega, giga and tera and the power of 10 value which is effectively multiplied by the value. And then we have the two string function.

**Dave Jones:** This is just a function that can be run at any time and it takes the value that you want to convert to a string and if it's zero, it returns immediately because why waste time detecting what unit it is if it's not zero.

**Dave Jones:** And then it goes through the different units and determines which unit, which SI, I don't know what to call them, bracket or something, it fits into and then it rounds the value to a certain number of significant figures, gets that as a string.

**Dave Jones:** If the result of that is zero, it just returns without the label. If it isn't zero, then it adds the suffix, pico, nano, micro, milli, giga or whatnot. Just a quick update on the function I showed before. I removed the way it behaved before because it allocated an SI value object on the heap and that's a bit slower than

**Dave Jones:** just running a static function, so just a small change, nothing major and that's basically all this does. So with this one function here, it makes all the labels for all the graphs have the suffixes of engineering notation.
