---
video_id: Foc9R0dC2iI
title: EEVblog #262 - World's Simplest Soft Latching Power Switch Circuit
url: https://www.youtube.com/watch?v=Foc9R0dC2iI
source: youtube-asr
timestamps: {"0": 2, "1": 19, "2": 31, "3": 42, "4": 58, "5": 72, "6": 81, "7": 91, "8": 103, "9": 111, "10": 121, "11": 131, "12": 146, "13": 162, "14": 176, "15": 190, "16": 204, "17": 218, "18": 228, "19": 248, "20": 262, "21": 276, "22": 286, "23": 301, "24": 317, "25": 327, "26": 339, "27": 350, "28": 369, "29": 384, "30": 394, "31": 406, "32": 418, "33": 432, "34": 449, "35": 468, "36": 481, "37": 505, "38": 514, "39": 527, "40": 535, "41": 549, "42": 566, "43": 579, "44": 587, "45": 600, "46": 618, "47": 626, "48": 646, "49": 664, "50": 679, "51": 699, "52": 710, "53": 726, "54": 744, "55": 758, "56": 770, "57": 778, "58": 790, "59": 806, "60": 816, "61": 826, "62": 840, "63": 854, "64": 864, "65": 877, "66": 893, "67": 904, "68": 918, "69": 931, "70": 943, "71": 957, "72": 970, "73": 984, "74": 994, "75": 1007, "76": 1019, "77": 1029, "78": 1039}
---

**Dave Jones:** Hi, the humble toggle switch. You've seen them. You've used them on your projects to switch your projects off and on and seems pretty obvious when you design a product, well, I need to switch the power off and on, use a toggle switch, but when you go on into production, it's not always the best idea.

**Dave Jones:** I thought we'd take a look at it. Think you might find it rather interesting. Now, take my power supply project for example. I've got to switch the power to this thing off and on and it can be drawing a couple of amps.

**Dave Jones:** So, your switch has to be rated for that and of course, it's got to be a latching type switch like this. Now, these switches are great. They're simple, they work, they're easy.

**Dave Jones:** You've used them before, but are they the most economical solution? Not really because one off these things are two, three, I don't know, even five bucks for a you know, even a reasonable quality switch that can handle your switching current for your particular project.

**Dave Jones:** Or even if they're low current ones, getting ones that actually latch like that instead of the momentary push button ones that you might be using on your product or you've seen on other commercial products, they're much cheaper than these latching types.

**Dave Jones:** So, when you go into volume production, even from the one and low factory in China, you're going to be struggling to pick these things up for under a buck or something like that.

**Dave Jones:** Now, a dollar, that can buy you a hell of a lot of circuitry. It can buy you a microcontroller, whole bunch of passives and all sorts of active components and stuff like that.

**Dave Jones:** So, really, is the mechanical latch toggle switch the best way to go if you're trying to get the cost down on your product? Not really. So, today we're going to try and design a soft latching power circuit.

**Dave Jones:** Sounds simple enough, but let's see if we can do it. And one of the first things you start out with with any design like this, what are the requirements?

**Dave Jones:** Let's take a look at them. We've got zero power when off. We don't want the circuit to draw any power when it switches off, just like a regular toggle switch.

**Dave Jones:** Uh we want the one switch to do the on-off function. No separate on and off button. One switch. You want to lower the cost, simple, just like on regular commercial products.

**Dave Jones:** Three, standalone. We don't want the microcontroller in our system to actually have to switch the thing off or do any control or things like that. Sometimes um that's actually desirable, but in this case I don't want that.

**Dave Jones:** I want it completely standalone. Number four, we want it to use jelly bean parts only. We don't want to use specific or dedicated chips, hard to get parts. So, we're talking basic transistors, resistors, caps, diodes, that sort of stuff only.

**Dave Jones:** And we want it to have a minimal number of parts cuz we want to be elegant, don't we? Always. Now, if we just ignore our requirements for a second, look at the basic application of this for just a separate on-off switch.

**Dave Jones:** How can you do that? Well, we've got our input here and our output power here, and we have a pass transistor. It In this case, it's a P-channel bipolar, but you can use a MOSFET as well, which we'll do in our final one.

**Dave Jones:** And you've got a latching transistor down the bottom. Now, if you have a look at the first case, when you initially power this circuit up, this transistor is not going to be on because there's no base current flowing through here.

**Dave Jones:** It's like that that chicken and egg kind of situation. If there's no base current this for there to be base current flowing through here like this to turn this transistor on, this transistor down here needs to be switched on first.

**Dave Jones:** And of course, it's not. So, you have the on switch here. When you turn on the on switch, current flows down through there like that, and switches on that transistor.

**Dave Jones:** And then the voltage Well, the current flows through here, and then it's can then switch on this transistor down here like this, which then latches it. So, you only have to press that on switch very briefly, and that will latch quickly because it's in parallel with this switch.

**Dave Jones:** It'll keep that switch turned on, keep this transistor turned on, and bingo, you've latched your power on. Simple. And how do you turn it off? Well, you just turn off this transistor down here by uh shorting its to ground.

**Dave Jones:** That'll switch it off. This gets no base current, nothing goes through, end of story. So, that's how you can use um that's a basic circuit for switching on and off, but we don't want two switches, and we want we want to use one switch.

**Dave Jones:** So, it's a bit more complicated. So, what we're going to do for starters is to replace our bipolar transistor with a P-channel MOSFET. Works exactly the same, except it's got lower on resistance.

**Dave Jones:** They're just nicer, more readily available. So, I'm going to use a MOSFET, but you could still use a bipolar transistor if you really wanted to. And because it's a MOSFET, um we, you know, you don't want the gate here flapping in the breeze around like that.

**Dave Jones:** Bad idea. So, we're just going to tie it to the input here, so it just keeps the uh gate of the transistor stable when it's switched off. And we've got our same uh NPN bipolar transistor down here, and it works exactly the same, it latches the same way.

**Dave Jones:** We could put our on switch across here and our off switch and it would work. But, we want the one switch to toggle off and on. We're going to add some extra stuff over here.

**Dave Jones:** We'll start out with a basic understanding of what we want this one toggle switch to do. And I've just uh diagrammatically drawn it as two separate switches here just for starters.

**Dave Jones:** If we've got our on switch, the the base of this transistor, we need to switch this transistor on somehow. So, you'd have a pull-up resistor back to the input here.

**Dave Jones:** So, the input voltage is always there. When you hit this switch, you want this transistor to turn on, the latch thing will happen, and everything's sweet. And then, you want this same node because effectively these two nodes here, you want them to switch between one and the other or toggle between one and the other.

**Dave Jones:** So, when the So, when the circuit the soft latch circuit is off, you want this point here in your circuit to be, if our switch is on this base here, we want it to be high to the input.

**Dave Jones:** And then, once this thing switches on, we want this thing to go low like this so that then we can short out the base to ground, switch it off.

**Dave Jones:** How are we going to do it? So, what I've done here is I've left our imaginary green circuit there in place, and I've drawn in the new real black circuit here to replace these two switches with this one switch.

**Dave Jones:** And it's doing exactly the same thing I said before. When this pass transistor is off, the circuit's off, and you want to switch it on, you want this one switch to act as the on switch.

**Dave Jones:** Here's this resistor up here pulled high to the input like that. So, if the circuit's off, and you want to switch it on by pressing the button, then current will flow through this resistor, through the switch, through the base of this transistor, latching it on.

**Dave Jones:** And Bob's your uncle. And then, what happens is this lat- this transistor down here will switch on and then pull this point here to ground. So, now you can see that that's what we wanted before.

**Dave Jones:** We wanted this point to toggle from high to low when it's switched on. And that's exactly what it's going to do, toggle from high to low. And then, and assuming it's your circuit's been working for a while, it's been switched on, and this you want to use the same button to switch it off, then this is pulled to ground.

**Dave Jones:** This point here is effectively grounded like that. So, when you press it, it shorts out the base and switches the whole thing off. Bingo! You've got some basic on-off functionality with a single switch.

**Dave Jones:** I love it. But I know what you're saying. Dave, this is analog circuitry. Operates really, really fast. And a button press is really, really slow cuz it's human. Well, unless you're a superhero, uh if you press, you're going to hold down, effectively hold down this button, ignoring switch bounce and things like that.

**Dave Jones:** You're going to hold it down for, you know, 100 milliseconds, quarter of a second, something like that, even if you press it really quick. So, this thing is actually going to oscillate off and on, off and on, off and on.

**Dave Jones:** You don't want that. We're going to have to slow it down. How can we do that? Easy. We'll add a capacitor in here to ground. That should do the trick.

**Dave Jones:** So, let's take a closer look at that. I have taken out the imaginary green stuff, and this is our real final circuit that I think's going to do the trick.

**Dave Jones:** Or it should do, in theory. Now, uh it works exactly the same as before. When you push this switch, if the circuit's off, this transistor's off, push push this switch, it switches this base current on, latches this, and you supply to your circuit.

**Dave Jones:** And now, this capacitor here starts out at zero, and it starts to charge up in voltage based on the RC time constant plus the base current flow through there cuz this is a um this is an NPN bipolar transistor.

**Dave Jones:** There's going to be some base current flowing in there as well. But anyway, that will charge that capacitor up. So, uh it won't immediately switch back off cuz this point will still be high.

**Dave Jones:** It'll still be high for I don't know, depending on the RC time constant, you might point 0.5 seconds or something like that that you want this point to be high.

**Dave Jones:** And then, once it reaches a threshold voltage of the transistor, it will switch the transistor on and pull that to ground. And if you're still holding down that switch after this transistor switches on, well, it's going to oscillate exactly like before.

**Dave Jones:** But, assuming you can push it quicker than half a second whatever your time constant is, then this transistor will be fully on. And then, this the functionality of this switch changes from an on button to an off button.

**Dave Jones:** I love it. So, I've gone and put some real values in here. 100k pull up, 100k pull up for the base here. It's relatively high, but stick with me.

**Dave Jones:** And we've got 100k here, and we've got a 1 meg and a 22 mic here. Should roughly do the trick. I think we need to build this up. I think this circuit, because we're using uh BJTs here, could be a bit critical in terms of getting the ratio between cuz this value needs to be high unless you've got a massive cap here.

**Dave Jones:** You've only got a very small amount of base current. This resistor has to be high, and there's going to be a balance between these values. So, could be a little bit tricky unless you went to MOSFETs, but I'm going to try and build this up with BJTs and a MOSFET pass transistor up here.

**Dave Jones:** See how it goes. Breadboard time. And here's my circuit built up on the breadboard for my MOSFET here. I've got an IRF 9110. Um that won't be the final one I use in my circuit, but that's what I had to hand, so I'm going to use one of those.

**Dave Jones:** Basically, I want this to operate from a very low uh voltage, a single lithium ion cell. So, 4.2 volts maximum down to 3 volts or something like that. So, you really need to pick a MOSFET with a very low VGS, um that has a particular on the maximum on resistance you want for a certain low VGS voltage.

**Dave Jones:** So, you can't just use any one off the shelf if you're picking like a if you need a low voltage supply like we using for my power supply for example.

**Dave Jones:** And I'm just using transistors or 2N3904 bog standard stuff. I've using a 47 micro cap. I didn't have a 22 to hand. So, let's give it a go. Let's switch this thing on and bingo, there it is.

**Dave Jones:** It automatically switches on and I press the button and it switches off. Press the button, switches on. Too easy. And that works a treat. And if I hold it down, it should oscillate just like we said at the frequency set by that RC time constant.

**Dave Jones:** So, let me actually replace that 22 that 47, sorry, with say a 10 micro and let's see what happens. There we go. There we go. It's oscillating much quicker.

**Dave Jones:** Now, it's going to be still works, but it's going to be a little probably a little bit touchier. There you go. So, yeah, that's it. The higher value is going to do the trick there.

**Dave Jones:** Now, you'll note that I've actually got no load on this thing. So, this is assuming a circuit with absolutely zero load. And by the way, I was operating that at 4 volts there.

**Dave Jones:** So, let's wind the wick down and see how low it will go with this particular MOSFET. So, there we go. We're at 3 volts. So, we'll power that on and try it at 3 volts.

**Dave Jones:** It switches on and it switches off. It requires me to hold down the switch for a bit longer. That's the thing. It'll miss if I press that off button really quick, it'll actually miss that.

**Dave Jones:** I need to hold it down for a bit more for a bit longer than I do to switch it on. I can do a really quick on, but I can't do a quick off.

**Dave Jones:** There you go. You could actually call that a feature. And let's have a look at the output voltage on the scope here. That's 500 mV per division. So, we're getting our 3 V out there or just under.

**Dave Jones:** And if we switch it off, it look, the output voltage doesn't actually go to ground. It's at 500 mV. Now, I'm measuring the output with the meter there, and you'll notice that it's dropping.

**Dave Jones:** So, that is the capacitor charged up to the base emitter voltage of the transistor that it's on, and then it's discharging through the extra resistors there. So, that will actually eventually get down to ground.

**Dave Jones:** That's because there is no load. And of course, that makes perfect sense because when you switch this off, this capacitor is charged up to the base emitter voltage up here.

**Dave Jones:** So, the only play when this transit when you press the button and you actually switch this transistor off here, the voltage up here goes to uh it switches off.

**Dave Jones:** So, it's got to discharge through these resistors here, and that's what's causing it to stay on. But, you'll find that if we stick a load on here, say 10K or something like that, it should just vanish and go to zero instantly.

**Dave Jones:** But, that's the disadvantage of this circuit with no load or a very light load. And we'll try that again with our 10K load. Let's switch it on and switch it off.

**Dave Jones:** Bang, right down to zero. No problems. Let's set our trigger point in the middle there and capture that switching off to see if it switches off cleanly. Yep, not a problem whatsoever.

**Dave Jones:** And we might as well capture that switching on as well. So, let's go. Bang, There it is. No problems at all. And one small note, just remember these MOSFETs have a built-in parasitic reverse diode like that, in case that matters in your circuit.

**Dave Jones:** And if you remember one of our requirements for the circuit was that it actually takes zero power when it's off. Does it? Yep, it does. There we go. It's eventually going to go down to practically zero microamps.

**Dave Jones:** There you go. It draws naff all. Half a bee's dick. So, there you have it. I think that's probably the simplest uh discrete standalone soft latch power switch you could possibly do.

**Dave Jones:** I could be wrong, but I'm going to claim that. Damn it, why not? Uses all jelly bean parts, two uh NPN transistors. It doesn't use NPN and PNP like some of the other solutions I've seen.

**Dave Jones:** The best solution I've seen before this is a three-transistor one plus the MOSFET as well. And well, it seems to work reasonably well. There are other solutions, I'm sure, but I rather like this one.

**Dave Jones:** It's kind of neat. We could probably do it uh differently using uh MOSFETs um if we wanted to, but I'm using uh bipolar transistors here. And this is a standalone one.

**Dave Jones:** There are other ways you can do these sort of things where you can switch them off using a microcontroller, like if you've got an automated uh if you want your software to be able to switch off the unit to go into power save mode after a certain amount of time.

**Dave Jones:** Well, that's a different thing again, but this is just a standalone circuit using one very low-cost momentary push-button switch. And I love it. Is it the simplest solution possible?

**Dave Jones:** Well, I don't know. I think it's pretty darn close. If you know of something better, uh jump on the forum and uh and share your thoughts. And uh if you like the video, give it a thumbs up.

**Dave Jones:** And in this video, I won't bother experimenting with values and stuff like that, just to show you which parts are critical and non-critical and how they interact. I'll leave that one up to you.

**Dave Jones:** Get the breadboard out, play around. And for those who hate me tapping on the whiteboard, JUST FOR YOU. CATCH YOU NEXT TIME.
