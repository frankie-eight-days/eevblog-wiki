---
video_id: A_saS93Clgk
title: C++ for the Embedded Programmer
url: https://www.youtube.com/watch?v=A_saS93Clgk
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 33, "3": 47, "4": 57, "5": 68, "6": 81, "7": 94, "8": 107, "9": 121, "10": 135, "11": 146, "12": 156, "13": 169, "14": 183, "15": 198, "16": 213, "17": 224, "18": 241, "19": 259, "20": 272, "21": 285, "22": 308, "23": 320, "24": 334, "25": 350, "26": 362, "27": 377, "28": 395, "29": 408, "30": 420, "31": 435, "32": 451, "33": 463, "34": 478, "35": 490, "36": 505, "37": 516, "38": 528, "39": 547, "40": 561, "41": 574, "42": 587, "43": 600, "44": 612, "45": 626, "46": 637, "47": 651, "48": 668, "49": 679, "50": 694, "51": 706, "52": 721, "53": 734, "54": 748, "55": 762, "56": 777, "57": 797, "58": 812, "59": 828, "60": 842, "61": 855, "62": 870, "63": 884, "64": 899, "65": 914}
---

**Dave Jones:** Hello. So, here we have something I wanted to show you. I think it's quite cool, and I hope other people do, too. What I am going to show you is a an interesting way using C++ and a few techniques to simplify

**Dave Jones:** things like interfacing with pins. Um so, let's let's just dive straight into it. Okay. So, in this code over here, you have the C++ version in the left and the C Okay. So, here we have an LED, and all

**Dave Jones:** the configuration and all the everything is done in the construction of this object. It's It's part of the language. This variable existing means that the port and the power configuration and whatnot are set up. Um over here, they do the They do

**Dave Jones:** the same things. They set it up as well. Um but, you know, it's a bit more raw. You can see exactly what they're doing. And But, some people think this is a good thing. I I I think it's um I think

**Dave Jones:** it's neither here nor there because as long as the actual the the class is what it's called is set up properly, you don't need to know why what it's doing. And, you know, of course, there's edge cases here.

**Dave Jones:** Um but, definitely not in this example. Heh heh. So, first thing they do here is set up the clock, and this is immediately obvious. But, what isn't immediately obvious is what they're doing it for. In this case, I think it's

**Dave Jones:** obvious cuz it's an LED. It's called LED. So, they set up the clock, which is for the port, and then they they set up the port values, which is they set up the pin mask, they set up the whether it's an output or an input,

**Dave Jones:** they set up whether it's a push-pull driver, although you'd need to know that that meant push-pull. They set up the speed, um which is 50 MHz, which their user guide calls high speed, I think. And then they set up whether the

**Dave Jones:** pull-ups are or are on or the pull-downs are on, and they say no pull, which is bad English, but they've turned all the pull-ups off. And then they call a function to initialize the whole thing. So, all of this

**Dave Jones:** can be crammed into these two brackets here. And that's it. And you don't even need these brackets. It's automatic. So, then let's get to the while loop. And now I haven't actually done it in this this example on the left cuz I couldn't be

**Dave Jones:** bothered cuz it takes like 12 seconds and I'll do it in a second. Um but over here we've got something that's it's almost clear what it's doing, but it's not quite. You need to you still need to give it a bit of scrutiny. You know, you

**Dave Jones:** got to make sure the port number's right. You got to make sure that the pin number's right. You you're using this the right hash to find. You got to make sure you're using the right you know, the mask hash to find and the

**Dave Jones:** GPA 0 X hash to find. This is a pointer to a a block of GPA 0 which, you know, isn't actually all that relevant. What it is What is relevant is what GPA 0 and what pin you're trying to

**Dave Jones:** toggle. And you're not really thinking about that when you're trying to interpret what this means. Whereas in the solution over here, you are. You you know, if I toggle the pin, I just toggle the pin, you know, LED equals not LED.

**Dave Jones:** And that's toggling the pin. This happens to have defaults as inputs because that's the safest um in most cases. Um so, if I were to set it to an output, you would say mode output. And now it's doing the same thing. Now,

**Dave Jones:** these are like if you were to decompile these, these end up the same. But, you know, you would have to know what all these different hash to finds were to to to change this to be flexible to something else.

**Dave Jones:** For example, say I only wanted to have the LED on when a button was pressed. Now, this would be really easy in the solution over here. Very very trivial. So, all I would do is I'll create a thing for a button. The button is

**Dave Jones:** default input, of course. So, it works as is. And then I say if enter toggle LED. And let's make that even simpler. Let's just say the LED is equal to the the value of the button. Let's do that with

**Dave Jones:** both of them. In this version here, it is quite obvious what's happening. You're saying LED equals the value of enter. And let's just call it enter button. Over here, I have a to set up the clock if it's on

**Dave Jones:** a different port. So, let's We've already done that. We're going to use the same port cuz I can't be bothered. So, uh we're going to do this. GPIO structure two. Let's uh do do do do do do. So,

**Dave Jones:** and we're going to call it over here. They've got a port number. I'm going to do a hash define cuz that's what they did previously and this is what it's normal. Button port equals three. And and yes, that is how this is meant

**Dave Jones:** to be. And then let's say hash define button pin equals four. So, port three pin four or port C pin four. So, then we do that. And there we go. So, I just screwed up this. And that there kind of flies my point.

**Dave Jones:** It's hard to manage this code. But, you know, we're going to we're going to get there. First, we're going to need to make a temporary variable. We're going to have to call it button state equals false. Why not have an initial

**Dave Jones:** value? And then we're going to have to find what the the the API has for the read of GPIO. So, let's have a look what they have here. Data bit. Sure, that sounds right. Yep, this is it. Wait,

**Dave Jones:** does it return the value? I don't know. Okay, so then we just save the value of the button from the read function. I assume this is how we're going to do it. Got to make a pin mask, I think.

**Dave Jones:** And then we're going to do the button pin. Now, if you forget to change this, it won't work. And that's part of the problem. In this solution over here, the C++ one, you can't forget. It's embedded in the

**Dave Jones:** type. Over here, you can easily forget. There's lots of things you got to check. All right. So, then we've got to set the value of the the LED to the value of the button. So, then we just say if button state

**Dave Jones:** equals true, then we want to set the bit. Set the pin. False, we want to clear the pin. And there you go. Now, we've got two sets of equivalent code. And, you know, depending on the version of C you're using, you might have to

**Dave Jones:** have this at the start. Um So, let's put it up there. And, you know, this would obviously be outside somewhere in another file. So, let's have it as is. And And, you know, that's redundant. So, let's simplify it

**Dave Jones:** a little bit. So are those brackets, those curly braces. We don't need those. Okay. So, we've cut the fat from it, and let's compare them. Believe it or not, these are doing the same thing. Although, this one over

**Dave Jones:** here is slightly more efficient because it only does the it it it only changes things as needed as opposed to over here where you're setting up absolutely everything and making no assumptions about initial value. But, you know, I'm getting distracted. Here we have how

**Dave Jones:** many lines? We got 136 to So, we've got about 36 lines. When you include those hash defines, 37. I'm kind of removing white space. Um let's say 35 cuz I just removed some. Not all that readable. And, you know, when you have code that's

**Dave Jones:** verbose like this, you need to add comments. So, that would that would pad up the line count even further. So, um you know, this could be anywhere between 30 and 70 in the case of these guys if you used

**Dave Jones:** comments like ST where most of it's most of the the C file the source file is is comments. Um versus over here where let's face it that is three lines of code and there's nothing to forget. There's nothing to

**Dave Jones:** check. The only thing you have to do is make one leap of faith that the the pin class knows what it's doing. And if you can do that, I mean you can do extensive testing to do that. But if

**Dave Jones:** you can do that then you don't have to worry about all this. You can do 1/10 the work. Okay. Well, hope you found this interesting. Um there's a lot more to this. Once you have a library like this you only you

**Dave Jones:** know you have the library use it forever. So that's what this is. It's one of my reused libraries now. So I've just noticed an error in my code the C code which um you know it would have been

**Dave Jones:** very obvious in this three lines. There's not a lot to check really. You know you've got a button which you know let's make it a bit more clear mode input and you've got an LED which is mode output.

**Dave Jones:** Very clear. Is this should have been an input. The button's an input. There you go. The verbosity of this kind of hid that from me so I didn't notice. And that's kind of my point. Although that sounds like I set this up

**Dave Jones:** and I I'm not that smart. The coolest thing about this code here is you can use this on any platform. Doesn't matter if it's an AVR. Doesn't matter if it's a PIC. Doesn't matter if it's an ARM Cortex M4 STM32F0XX

**Dave Jones:** which is what we're using here. All of the platform specific code is abstracted away so that the actual program logic is the same on every platform. It's platform agnostic. Just adding a little bit to what we talked about before. This is one

**Dave Jones:** of of use cases of of the C++ approach I showed before. Okay, so I'm only going to go over this very briefly because if we go into the depths of this um it is much too much for this video.

**Dave Jones:** I've already tried doing that a few times now. So, this is a an example of what you could use what I was talking about before with um this is a general implementation of a keypad using um these keys. That's key zero, the zero

**Dave Jones:** key, 1 2 3, and then there's the dot point at the end. And I've called it numpad cuz in this case it talks to the computer's numpad, but in in the microcontroller it talks to a bunch of buttons. And And the way the way we did

**Dave Jones:** that is exactly the same before. We define a pin. We define the port, which is um not as relevant on the computer, but it is very relevant on the microcontroller. And we define what character is being um pressed. Um this is the the code which

**Dave Jones:** is accepted for decimal point, and you don't really need to worry about it, but these are the pins like we had before. And the advantage of defining pins like this is then you can feed them into other um things. I call them like

**Dave Jones:** kernels, but I don't I don't really know what to call them, but I feed this into my button my my templated button, and then it acts like a button with debouncing and events. So, you know, it has like a long press event. It

**Dave Jones:** automatically adds it to whatever button you just defined. So, this button here will respond to I think it's just a single press um depending on what the button kernel was. But changing it to something that accepts repeats is as easy as doing that. Um

**Dave Jones:** it's not a huge code change. If you wanted to change it to something that's logic, you know, the opposite logic, you know, it's literally just changing it like that. And this is the I think the advantage of approaching

**Dave Jones:** um programming like this in this templated manner. If people really want me to go into the depths of this, you'll have to there'll have to be a lot of you because it's very difficult to explain without having like a multi-hour video. But, um

**Dave Jones:** basically this is one of the examples and I'll just basically show it running. Um it's just going to update the numpad that would be scheduled by a timer. Probably not running the timer, but scheduled by it and then

**Dave Jones:** it sleeps for 10 milliseconds. That's all we're doing here. So, this is off obviously platform specific, but the actual interface is totally platform agnostic as in the function call update and and these these parameters here are identical with the exception of

**Dave Jones:** obviously you don't have numpad characters like that on a microcontroller, but um in this case we're accepting a maximum of 12 inputs. That's what this random number is and I'll just run it now. Ha! That's funny. I broke my code trying to

**Dave Jones:** make it simpler for the video. So, I am I simplified my code a little too much for the video. A weird thing about the way Windows key codes are is zero is referenced to 30 um the way that the reading the key

**Dave Jones:** character is and that's what this is. So, if I add zero to all the numbers that then it worked. That's a weird thing about Windows. I don't know. It's kind of weird. Anyway, so here we go. 0.25 enter.

**Dave Jones:** Um enter's just submit in this case. I've just set it to clear it, but 0.8 enter 1 2.0 2.5 8 and enter and basically as you can see it's it's just behaving like a numpad. It does the conversion on the fly

**Dave Jones:** to your floating point. What is displayed at the top is the um floating point number. The implementation here the only platform specific stuff is this this debugging information here. Okay, so neither of these examples are part of the C++ or the C standard library. Both

**Dave Jones:** of these are basically examples of libraries that you know, you could potentially use for one of your projects. Um this is my library and it's part of the micro supply code which um is open source of course and this is the

**Dave Jones:** ST microelectronics. Is that it? Code and this is this comes with many of the IDEs that support ST chips with their compilers or you download it yeah. So again these aren't part of the standard library this is not you know

**Dave Jones:** that the C++ language doesn't have a pin a pin type but given a bit of a bit of effort not really a lot you can generate your own things like like my class here and you know it cuts the work down by a

**Dave Jones:** tenth over the long run. So please keep in mind that behind the scenes here both the ST example and my example both have things going on. So in my case the um what's going on is you have these

**Dave Jones:** functions which you define and you don't actually have to write the template meta programming you can just fill in a block and in the case of ST you have um this huge library and I'll I'll just open it up now. And in the case of ST

**Dave Jones:** you have all this stuff. So if you were to change the the platform this was on you'd have to rewrite everything inside the the function parentheses. So um the the line count for the general implementation of pin is something like

**Dave Jones:** 130 and the line count for the GPIO functions by ST um is very hard to count because of all the comments but I suppose you need the comments to understand it so I'm going to count them is something like 500 that's what that's

**Dave Jones:** what we end up with. So in both cases you know it's not magic you do have things happening behind the scene for example this thing manages whether the GPIO port is on or off and that's all automatic but over here you have to do it manually

**Dave Jones:** but both both things they end up doing the same thing. They do turn on the GPIO they do set the the state and the mode and speed and whether there are pull-up resistors. They both do that. Again, it's not magic.
