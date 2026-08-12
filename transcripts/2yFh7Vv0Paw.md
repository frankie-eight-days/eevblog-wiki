---
video_id: 2yFh7Vv0Paw
title: EEVblog #831 - Power A Micro With No Power Pin!
url: https://www.youtube.com/watch?v=2yFh7Vv0Paw
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 32, "3": 45, "4": 57, "5": 70, "6": 83, "7": 106, "8": 120, "9": 139, "10": 158, "11": 174, "12": 188, "13": 207, "14": 221, "15": 235, "16": 253, "17": 266, "18": 280, "19": 291, "20": 312, "21": 329, "22": 346, "23": 360, "24": 376, "25": 393, "26": 406, "27": 418, "28": 435, "29": 453, "30": 474, "31": 492, "32": 504, "33": 522, "34": 535, "35": 550, "36": 565, "37": 581, "38": 598, "39": 616, "40": 631, "41": 648, "42": 665, "43": 680, "44": 694, "45": 708, "46": 725, "47": 746, "48": 761, "49": 782, "50": 796, "51": 812, "52": 828, "53": 844, "54": 860, "55": 873, "56": 891, "57": 905, "58": 923, "59": 938, "60": 956, "61": 975, "62": 988, "63": 1006, "64": 1022, "65": 1039, "66": 1052, "67": 1066, "68": 1078, "69": 1093, "70": 1107, "71": 1121, "72": 1134, "73": 1149, "74": 1165, "75": 1180, "76": 1199, "77": 1209, "78": 1226, "79": 1239, "80": 1254, "81": 1273, "82": 1288, "83": 1302, "84": 1317, "85": 1330, "86": 1343, "87": 1355, "88": 1371, "89": 1387, "90": 1402, "91": 1417, "92": 1432, "93": 1445, "94": 1465, "95": 1482, "96": 1493, "97": 1508, "98": 1517, "99": 1528}
---

**Dave Jones:** Hi, I'm going to show you something a little bit unusual and a bit mind-blowing if you haven't seen this before. So, check it out. I've got a little 14-pin microcontroller here. It's a little MSP430G2321. Just a, you know, a basic little 8-pin

**Dave Jones:** micro flashing two LEDs back and forth. It's just programmed to do that on two of the IO pins. Nothing unusual here at all. We're powering it from a 3.3 V rail, hence why I've got one of these USB uh power bricks here you've seen

**Dave Jones:** recently. And they've got a bit of an unusual arrangement on the pins here. Pin one is actually the VCC pin or the positive power pins. So, I've got that. Here's pin one of the chip. It's going up to my positive rail there.

**Dave Jones:** And then pin 14 is actually the ground pin. So, you'll see that going down to there. That's going down to ground. So, I'm powering my chip from a 3.3 V rail. And then, of course, to have the micro

**Dave Jones:** actually work is to start up and work. the reset, which is pin 10 down here. So, it's hooked up. So, of course, if you disconnect the reset pin, it's not going to actually do anything. And you can sort of, you know, make it do weird and

**Dave Jones:** wonderful things if you try and float the reset pin. So, you've got to have the reset pin connected there. And the micro starts up. It's programmed just to flash the LEDs back and forth. And I've got two dropper resistors. So, using two

**Dave Jones:** of the IO pins. Nothing unusual, right? Well, look what happens if I remove the power pin. What do you think's going to happen? It should stop flashing, right? Look at that. It still works without the power pin. Why is it so?

**Dave Jones:** So, I call your attention to the title of all my shows. Why is it so? Why is it so? Now, I can assure you that there is no trickery involved here. I am not doing the breadboard isn't rigged underneath

**Dave Jones:** or anything weird like that. I disconnect my power little power brick here and it stops working. But you remove the power pin and the chip still works. I guarantee you no trickery. Stop the video here. Try and figure out what's actually going

**Dave Jones:** on and how is this chip being powered? Like I can disconnect it. There it is. Start it back up. It starts. But the power pin, the VCC, the one and only VCC power pin is not connected. Well, now of course for any circuit to work,

**Dave Jones:** let alone a complex microcontroller like this, we have to have a power loop somewhere. It has to be getting the power, right? There's you know, there's no battery in there. There's no capacitive element that might you know, super cap or anything to keep it

**Dave Jones:** charged. If you remove the power, it should stop working. Just like that. But it obviously works. So clearly there has to be some sort of you know, a power getting to this pin. Can you figure out where it's coming from?

**Dave Jones:** Well, it's pretty obvious, isn't it? There's another 3.3 volt input over here on the reset pin. But it's not a power pin. It's a reset pin. Sure enough if we pull that what? It stops. There you go. But still why is it so? So clearly

**Dave Jones:** something very unusual is going on here and this microcontroller is being powered through the reset pin instead of the power pin. Now look, I've got no power pin connected there. There again, pin one is not connected at all. But

**Dave Jones:** I've got the reset pin hooked up to my decade resistance box here and I've got it set to zero ohms. So it's just like the link I had there before. Now look what happens when I actually increase the resistance? Let's go to 1 K,

**Dave Jones:** 2 K, 3 K. You can see it getting a bit dimmer. There we go, but the micro is still working. But you can see that these uh LEDs uh are being uh dimmed by the resi- effectively a resistor in

**Dave Jones:** series with this reset pin here. But it's still working and 10 Oh. And once you get to 10 K, you know, it really it's probably Yeah, I think it's dead. It's dead on 10 K. So, let's play around with this a bit more and uh

**Dave Jones:** experiment. I've put a pull-up resistor on the reset pin. I've actually put a 2.2 meg resistor on there. Just happened to have that handy. Really incredibly high value, right? And I've put my uh power pin back. Sure enough, if I remove

**Dave Jones:** the power pin, okay, it's not going to work cuz there's too much voltage dropped across that 2.2 meg resistor. Clearly, we're not going to power the micro. And we're via whatever mechanisms happening here, we're not going to be

**Dave Jones:** able to power the LEDs. But look what happens if we plug in any other pin, any other IO pin. Look. Bingo. It magically starts working again. So, we can actually try the next IO pin here. This IO pin here. This one

**Dave Jones:** Oh, no, we're using that one. How about this IO pin down here? We can power this micro through any virtually any pin on here. Amazing. Is your mind blown? Why is it so? What is going on here? Is

**Dave Jones:** this some sort of like evil voodoo? I mean, is there something really bizarre about this MSP430 chip? Well, the answer is no. So, this can actually be a trap for young players when you're actually uh building up your uh breadboard or PCB

**Dave Jones:** prototype or whatever, and you accidentally forget to apply power to your VCC pin, your micro, or other types of chips as well, 74 series logic, all that sort of jazz, they can do exactly the same thing. They can still be

**Dave Jones:** powered via their other pins. So, your circuit can appear to work, and then you can have some intermittent fault where, well, a combination of the inputs might cause it not to work. But, still, if you haven't seen this before, if you don't

**Dave Jones:** know the mechanism behind this, it's like magic. What's going on? How is this possible? Now, if you're unfamiliar with the phenomenon that's going on here, then the data sheet, unfortunately, is not going to tell you diddly squat. And you can, trust me, you

**Dave Jones:** can go search through all, like, this is like a 58-page data sheet. It's not hundreds, but it's, you know, it's a fairly comprehensive data sheet. You can even go down here to the schematic for each individual pin, and you can see

**Dave Jones:** that, well, I don't know. What Look, can you see any mechanism in there that allows you to power the chip through the IO pins? None whatsoever. And you can keep going through here until the cows come home. And even if you go over to

**Dave Jones:** the MSP430, uh, user's guide here, 644 pages, trust me, if you look through all of these 644 pages, you won't find any hint at all about what's going on here. So, what do we have to do? Well, you

**Dave Jones:** either have to know this, or you have to luck upon a manufacturer's data sheet who actually supplies some info on this. You can search for the word diode, and there's this little bizarre thing here that says diode current at any device

**Dave Jones:** pin, plus minus 2 milliamps, the absolute maximum rating. And that's the only hint to what's going on here. Let's go over to another random micro controller you might be familiar with, the ATmega8 AVR microcontroller. Aha, here's the magic. All IO pins have

**Dave Jones:** protection diodes to both VCC and ground as indicated in this diagram. Here is the IO pin and these are your input protection diodes. And you'll notice that they're actually reverse biased, so they're never actually on unless you overdrive the inputs. This arrow up

**Dave Jones:** here, for example, is showing that it's going up to the VCC pin, the positive rail. And of course this one's going down to the ground pin of the chip. These diodes are actually inside the chip and sometimes they have a series

**Dave Jones:** resistor in there as well. And this is how they protect the input pins on most, almost, you know, let's say almost all CMOS devices will have these input protection diodes. That's how if you touch the pin, you know, you zap it with

**Dave Jones:** a high voltage, it's going to the diode is going to conduct because it's above the rail or below it and it's going to clamp that energy and dissipate it in the diode. So that's how they actually protect modern devices, be they complex

**Dave Jones:** microcontrollers that we're looking at here or standard 74, you know, HC double O series logic. Go look at the data sheet for that, you'll find exactly the same input protection. So let's take a look at say a 74HC double O uh

**Dave Jones:** quad NAND chip. Now, they all are going to have ESD protection like this. You can actually see it written there, but very few data sheets are actually going to show you diagrammatically the actual diodes in this. There's nothing in here from NXP.

**Dave Jones:** Go over to this ON Semi data sheet, there's nothing in there either, no diodes. The diodes incorporated data sheet, nothing here. TI, nothing here at all. We go to Fairchild, nothing in their data sheet. What we have to go to is a

**Dave Jones:** ST micro data sheet, and bingo, they have it. There it is, the input and output equivalent circuit. Look, even they've got the diodes on the output and the input protection diodes, exactly the same. In this case, they have a series

**Dave Jones:** protection resistor, exactly the same as inside, you know, microcontrollers and almost all CMOS chips like this. That's what they use for protection, and that's what's at play here. In bloody input protection diodes. Real trap for young players. So, back to this NXP one for a

**Dave Jones:** second, even though they may not show it, they actually do tell you. Look, right up the front of the data sheet, inputs include clamp diodes. Bingo. And you'll actually notice that they actually give you a little application hint here as well. This enables the use

**Dave Jones:** of current limiting resistors, i.e. a series resistor on the input pin to the chip to interface the inputs to voltages in excess of VCC, because they'll be automatically clamped by the ESD input protection diodes. So, you can actually use these diodes here,

**Dave Jones:** and you can actually have an input resistor on here, and you can use these and actually overdrive the inputs safely as long as you don't exceed the maximum diode current. And that's why we saw back in the TI MSP430 microcontroller,

**Dave Jones:** the absolute maximum diode current rating of any pin plus minus 2 milliamps. Long as you don't exceed that, you can actually overdrive the inputs using a series input protection resistor. Just a neat little application there, just in case you need it.

**Dave Jones:** So, what we've actually got here is a diode protection input on each and every pin. For example, the reset pin we originally played with here, it's just like any other pin, it's got the diode protection, so we can power the chip

**Dave Jones:** through there and it goes into physically the VCC pin inside. So, yeah, we get a voltage drop, but the chip is still going to work. So, let's actually measure that. We've got ground here and our power supply up here, of course, is

**Dave Jones:** 3.37 volts. There it is and we'll measure our floating pin here, our floating VCC pin. Nothing's connected to it, but we're powering it through one of the random IO pins here. Let's measure. The power pin, there it is, 2.65 volts

**Dave Jones:** because we're getting about 0.6 volts diode drop here and the internal silicon is still seeing that 2.66 volts, which is more than enough for the microcontroller to still keep working. So, every single pin has a diode going to the VCC pin. So, it's going to look

**Dave Jones:** like this. So, we can power this chip through virtually any one of the other pins and that's what we showed up here. So, it's actually no different to taking a diode and putting it in series with the power rail. It's exactly the same

**Dave Jones:** thing except that diode is built in as protection on each and every pin. But wait, the mind blow doesn't stop there. Watch this. Not only can we remove the power pin, we can remove the ground pin. Woah, this is heavy.

**Dave Jones:** So, you might be thinking, "Ah, Dave, I know all about these ESD protection diodes and it's clearly the one going down to the negative rail down here that's doing the trick just like it did on the positive one here, but

**Dave Jones:** where? Where is it? How? We've only got one ground pin here. We've disconnected it. It's not like we've got any other pin here tied to ground. Remember, we've still got the 2.2 mega resistor going up to plus 3.3 volts.

**Dave Jones:** What's going on here? Where's the Where's the diode? Where's the ground? So, this is a little bit of a red herring here. Pause the video and see if you can figure out how this chip is still working. So, were you able to figure it out?

**Dave Jones:** Well, yes, it's a diode, but it's not the internal diode inside the chip this time, not the ESD protection diode. We've got two diodes on the outside here. Look at this, they're called LEDs. If I remove one of them,

**Dave Jones:** oh, it stopped working. What? Now, this is a rather quirky example where because we're alternating two digital outputs like this, i.e. when one output is high, the other is low. It's the software is not setting the output to high

**Dave Jones:** impedance. So, to switch the LED off, it actually sets this output low, high, low, high, right? So, it's actually driving the output. And when it drives the output low, we actually have a ground on this pin, but this actually

**Dave Jones:** goes through our circuit, so we are actually applying ground on this pin via the diode drop there and the resistor, but it's still just enough to make the chip work. I mean, it's completely out of spec and everything else. And let's

**Dave Jones:** measure it, and we might see something unusual here. So, let's actually go in and take a look at our ground pin here. So, I'm I'm on the real circuit ground down here, but let's measure it and see what we get.

**Dave Jones:** 1.4 volts, and what? It just stopped. It flashed for a second at 1.4, and then jumped up to 1.9 volts, you saw it. It was the chip was on such uh you know, a low margin of operation, well outside its recommended 1.8 volts

**Dave Jones:** minimum voltage but it was still able to work but just putting the 10 meg of our 10 meg input impedance of our meter here was enough to actually cause the thing to stop working and of course it won't

**Dave Jones:** start up again until we physically go in there and connect the ground. So we go in there, tap it again and it starts working but as soon as you load that down it changed it just a smidge. Whoa, boom. And I can actually stop that

**Dave Jones:** working just by touching that pin there. There we go. Pin go. It's so on edge but we can actually use that negative pin input protection diode to power the chip as well and then it won't be influenced by you know external

**Dave Jones:** borderline factors like that, okay? So let's start up our chip, it's working and let's just connect one of the other inputs here to ground if I can get the damn thing in the breadboard. There it is, okay. So we connected one of the

**Dave Jones:** other input pins to ground and now if we actually measure it, the ground pin, you'll find bingo, it's actually raised by 0.23 volts. So it's not 0.6 volts, we're actually getting about 0.2 volts across that input protection diode there. So because we've

**Dave Jones:** grounded one of these inputs here it's able to actually effectively ground via a diode drop the ground pin of the chip. But why are we getting 0.2 volts across this diode on the ground pin when we actually ground

**Dave Jones:** this input and the current is actually flowing through the ground pin and we get 0.6 volts across the one on the positive rail. Once again, I'll let you pause the video, see if you can figure it out before I tell you.

**Dave Jones:** Well, here's the answer. It all has to do with how much current is flowing through the LED and where the current is flowing from. Let's take our original example where we've disconnected the 3.3 V power pin here and we're powering it

**Dave Jones:** through some other IO pin like this reset pin, but as we saw it can be any other pin. Well, we've got our 3.3 V rail. Our current is flowing through here, so it's flowing through the internal uh protection diode. And it's

**Dave Jones:** also So, it's powering the chip as well. So, I guess you could say you know, this is the chip power consumption because it's a microcontroller. You know, it's very small. You know, it's reasonably small. It might depends on the uh

**Dave Jones:** frequency it's running at and you know, all that sort of stuff to do with processor power consumption, but it's also flowing So, it's flowing down there powering the micro, but it's also flowing out the IO pin and down through

**Dave Jones:** the LED. We've got a 1K drop resistor in there. So, 3.3 minus uh 0.6 V, you know, minus 1.8 V maybe for the LED. You know, we're talking about like 1 mA through the LED. 1 mA reasonable amount of

**Dave Jones:** current. So, we're actually going to get that you know, typical 0.6 V across that diode there. Now, let's look at the other example where we're using the ground pin protection diode. This is it here and we've disconnected our the

**Dave Jones:** ground pin on our chip and we're using one of the other IO pins. It doesn't matter which one it is once again. So, we've grounded this pin here. Okay, so this is our protection diode. This is uh the load of the processor that I uh

**Dave Jones:** talked about it before which is frequency dependent everything else. And we've uh connected up our 3.3 V rail directly onto our proper power pin here. Well, now the current is split. The current for the LED actually flows from

**Dave Jones:** directly from the pin out here and down through the LED and likewise it'll go through the other LED and it bypasses the protection diode. So, the only current flowing through the protection diode now is the processor current and

**Dave Jones:** it's obviously lower than what the LED was taking because we're getting only 0.2 volts of drop drop across there now because if you remember your diode basics, you don't get a constant 0.6 volts across a diode. You do after a certain

**Dave Jones:** current, but there's a curve but the diode curve ensures that at very low currents you actually get low voltage drops like the 0.2 volts we're seeing and we'll be able to measure these currents. So, in the case of the missing negative ground pin,

**Dave Jones:** let's actually disconnect it. It's still working, but let me use one of the IO pins. There we go, it's turned off. You'll switch notice it'll switch back on. So, let's connect it down to the ground and you'll notice that the

**Dave Jones:** current is only about you know, look, about 0.8 microamps. It's bugger all. So, that microcontroller is obviously like, you know, going to sleep between those you know, alternate things. It's extremely low power. It's not taking anything at all because the current for

**Dave Jones:** the LEDs is not flowing through that ground pin. So, we're measuring the current out of there. It's incredibly low. But now, let's go back to the original example where we're actually using the positive one. So, let's disconnect the

**Dave Jones:** positive rail there. Let's hook it up to any of the IO pins. Let's say this one here and let's see what we get. Look at that, 1.45 milliamps. That's our diode current because all of the diode current is a

**Dave Jones:** plus the processor current that, you know, 0.8 microamps is flowing through that positive protection diode we saw before. So, it's still the chip is still within operational voltage range. It only needs 1.8 volts to work. It's still getting 3.1 volts. So, that's why the

**Dave Jones:** thing continues to work. In this case, powered through that negative uh pin protection diode. And just for kicks, I'm going to show you a bit of a more practical uh scenario where you can come a gutser. You can make an absolute

**Dave Jones:** fool of yourself. Big trap for young players here. What I've got is I've added a second chip here. I've added a uh CD uh 4060. It's a 4000 series uh CMOS. I like this little uh part. I've always liked it ever since I was a kid.

**Dave Jones:** It's got basically a built-in uh oscillator which you can use with either an RC uh oscillator or you can use with an external crystal oscillator. And it's basically a binary ripple counter output. So, I've just put um uh some resistors and uh caps in here

**Dave Jones:** just to get, you know, a frequency that uh you know, we can actually see. And I'm just tapping three of the outputs here and feeding those into input pins to the microcontroller over here. So, you can see those uh three red wires

**Dave Jones:** going over there. And I've just hooked on three LEDs onto these ones as well. So, this is uh Q4, Q5, and Q6. And you can see that counting up in binary there. And uh the VCC pin to the micro,

**Dave Jones:** we've disconnected it. There it is. It is not hooked up at all. Uh and I just forgot to show the uh pull-up resistor on here. So, we've got a pull-up resistor. It's 100K. There's no way we can power the chip through and power

**Dave Jones:** these LEDs uh through that 100K resistor. So, the power has to be provided through the three input pins to the microcontrollers, these red wires going over. And you'll notice that uh when it's counting up, okay, where our chip is working just fine because we're

**Dave Jones:** powering it through the input protection diodes which are effectively um a big OR gate there. So, if this input is uh at logic high, i.e. the LED is on, so we're getting basically uh 3.3 V into there, then it's enough to power the

**Dave Jones:** chip. Same with this one, same with this one. So, if any one of these LEDs is on, the our microcontroller will be powered, but you'll wait until they all switch off. What happens? Woah, our micro switches off. There's no

**Dave Jones:** more power. It can't provide it through here. Our VCC pin's disconnected, and our circuit stops. And then it restarts once one of these inputs goes high. Magic. So, this is actually a real practical scenario where a lot of even

**Dave Jones:** experienced engineers come a gutser because there might be something you might have built your breadboard circuit wrong. Your PCB, uh for example, you might have uh you might have a might have forgotten to solder one of the power pins, be well, be it a power pin

**Dave Jones:** or a ground pin or something. And you build up your circuit, and it can appear to work just like it is now, okay? It's working, but then all of that occasionally it'll just glitch and reset or do something weird or

**Dave Jones:** something like that. So, this is actually a not that uncommon uh scenario or a fault in a prototype circuit where you forget to have the power pin. And if you forget the power pin, your circuit can still work, as I've spent the last 20 minutes

**Dave Jones:** demonstrating. So, there you go. Just watch out for this. Remember the golden rule of troubleshooting, thou shall measure voltages. That includes ground and power pins, cuz I've shown both scenarios where removing the ground pin and removing the VCC pin can still

**Dave Jones:** result in your circuit, your micro, or it can be a you know, whatever chip it is, even this uh 4060 will have the same thing. We could power this chip and so forth. So, there you go. You just got to

**Dave Jones:** be careful of ESD protection diodes. They can be very useful. I showed a scenario we can actually use them to your advantage, but in some cases, um, they can actually really cause a big troubleshooting headache if you forget

**Dave Jones:** your power pin or your ground pin. So, there you go. Just watch out for it next time. I hope you enjoyed that. This was a lot longer than what I expected. I thought it'd be quick and easy, but, you

**Dave Jones:** know, I did go through a lot of different art scenarios there. I hope you found that really interesting. If you did, please give it a big thumbs up. I don't have a wide enough zoom here, but there's a thumb. There it is. Give

**Dave Jones:** it a big thumbs up. And as always, comments down below, subscribe, yeah, all that sort of jazz. Catch you next time.
