---
video_id: qHbkw0Gm7pk
title: EEVblog #1087 - UNBELIEVABLE Alesis Studio Monitor Fault!
url: https://www.youtube.com/watch?v=qHbkw0Gm7pk
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 27, "3": 41, "4": 56, "5": 71, "6": 84, "7": 98, "8": 111, "9": 125, "10": 138, "11": 150, "12": 169, "13": 183, "14": 199, "15": 221, "16": 237, "17": 260, "18": 277, "19": 293, "20": 312, "21": 328, "22": 340, "23": 357, "24": 371, "25": 389, "26": 405, "27": 418, "28": 431, "29": 445, "30": 460, "31": 477, "32": 493, "33": 509, "34": 522, "35": 537, "36": 555, "37": 573, "38": 589, "39": 601, "40": 615, "41": 630, "42": 644, "43": 655, "44": 670, "45": 684, "46": 702, "47": 716, "48": 732, "49": 753, "50": 772, "51": 795, "52": 806, "53": 819, "54": 837, "55": 856, "56": 871, "57": 885, "58": 900, "59": 918, "60": 931, "61": 948, "62": 963, "63": 984, "64": 994, "65": 1005, "66": 1022, "67": 1036, "68": 1050, "69": 1065, "70": 1079, "71": 1094, "72": 1109, "73": 1123, "74": 1138, "75": 1150}
---

**Dave Jones:** Hi, I thought we'd take a look at my Alesis M1 Active 520 USB studio monitor speaker. Um, these are the speakers that I use for all of my video editing and have done for uh, many years now. And I

**Dave Jones:** like it not only cuz they're they small and compact, the 520 means it's a 5-in main driver here, but I like it for the fact that A, it's got the volume and power switch on the front and I'm

**Dave Jones:** always using this and I don't have to dick around with like the software or an external box or anything like that. Um, it's got the headphones on the front which I use for podcasting and it's USB as the name

**Dave Jones:** says. It's actually a USB interface as well, which is handy. It just means that there's, you know, one less box on my bench. I don't need an external DAC or to use the crappy sound card inside the computer. So, I rather like these.

**Dave Jones:** There's not too many like USB monitor speakers on the market and they don't make this one anymore. They do make the 320 USB which is a 3-in driver version, but anyway, and I do like the fact that it uses

**Dave Jones:** nice beefy XLR connectors for the to go to the other speaker. All of the driver is inside this one. The other one is just a speaker. It's got bass boost and a rear port on the thing. And also

**Dave Jones:** totally, I really like these cuz I do video editing where like speech is everything. Like I don't have any music. I don't do any music editing or anything like that. And apparently the crossover in these has been designed to avoid the

**Dave Jones:** mid-range of the voice. So, you know, they're potentially a bit better than some others on the market in terms of voice reproduction and stuff like that. Anyway, I think they're a cool little monitor speaker, but there's a problem

**Dave Jones:** with this one and that when I turn it on, it's supposed to have a funky blue light across here. There's obviously a LED backlight and this is just like a light pipe and it's supposed to turn red when it clips, but I I don't think I've

**Dave Jones:** ever seen that cuz I've never overdriven these things. But yeah, it's supposed to have a funky blue light. So, it doesn't anymore. But it still sounds fine, but I thought I'd just crack it open cuz I haven't opened these before.

**Dave Jones:** So, we'll do a teardown and have a look what's wrong with that LED light, shall we?

**Dave Jones:** Now, what I'm interested in is that little board tucked up under there that has the power switch and the connection to the LED and the LED pipe. So, we'll remove the knob there and we can get down into the nut down in there.

**Dave Jones:** I need a socket driver for that. Now, a pair of needle nose pliers should be right. Actually, as it turns out, I'm not the least bit interested in that. It doesn't even have the LED. There's actually another lead here actually going down into the

**Dave Jones:** same hole down in there which goes to the LED. So, that's the one I'm interested in. It's a dual color. Only two wires going in, but there's both red and blue. Nothing there. But if we put it backwards,

**Dave Jones:** then there you go. It lights up red. But blue is the problem. Hmm. Can we get that off? All right. Oh, yeah. Ta-da. We're in like Flynn. All right. The LEDs have to be tucked up and hot snotted all within there, which

**Dave Jones:** is a bummer. And they just go into the light pipe, but yeah, I assume it's just a dual back to back they back to back red and blue LED. Okay, so what I've done is just put the power supply into constant current mode

**Dave Jones:** 5 volts compliance or output voltage, that's just the technical term and 10 milliamps. So, because the 121 multimeter is only capable of a couple of milliamps due to the 2. aha. There we go, blue. Tada! No problems whatsoever. If I change the polarity,

**Dave Jones:** red. So, there you go. What current will it operate down to? And if I set it to 1 milliamp, which is the absolute minimum resolution of the power supply, obviously having the I think it's about 2.2 K or something in

**Dave Jones:** series with the inside the multimeter wasn't enough to light that up. That's a rather weird one. So, that's okay. Unless there's like an intermittent contact I'm not seeing, our problem seems to be down there. There's our connector for the driving

**Dave Jones:** that LED. So, there's a little little TO-92 next to that. Is that Is that driving that thing and switching the polarity? That could be the culprit. Hey, I just decided to plug it back in. Switch Look. Look. There we go.

**Dave Jones:** It's come good. Is it just a dicky connection, but it went off on its own? Yeah, it's No, no, it's fading, is it? Yeah, there's something something not good there. I swear it was brighter before. Is that my imagination?

**Dave Jones:** Something weird's going on. So, I It's I don't think it's a It's not a connection issue. Let me give it a bit of a give it a bit of a bit of a wiggle. Yeah, no. Nothing to do with the

**Dave Jones:** connections. So, it's got to be electrical. This sucker's electrical. Yeah, it's definitely switching off and on. It was off a second ago, trust me. And it just flickered back on and there is some like some sort of flickering in there as

**Dave Jones:** well. So, I don't know. I depends on how they're driving this thing. We might have to reverse engineer the circuit, but oh, we've got some blue there. Just switched off. What I'm doing now is actually overloading the thing

**Dave Jones:** to the hilt. I'm feeding in a 1 kHz sine wave and overload and I don't even get the red clipping anymore. But, I'm not driving driving the speaker here, but I was actually driving the speaker before at full volume and I didn't get the red

**Dave Jones:** clip. So, I think that part of it is buggered, too. But, yeah, just switched off and on. Zippity doo dah, this thing like changes all the time. That's the problem with uh uh like faults like this. If you can't consistently re-

**Dave Jones:** produce it, then it can often be hard to track them down. But, we know there's something wrong with that uh uh LED driver thing. Both it looks like both the power and the clip aspect to it. So, it's time to start measuring stuff. So,

**Dave Jones:** what we're going to do is take a look around uh this op amp down here, the drive transistor, the three pins. There's our connector that goes off to the LED. You can see that the collector and the emitter

**Dave Jones:** directly goes across the LED. So, it actually uh shorts that out, but basically goes across a diode here into um pin seven of this uh op amp here. So, the op amp's powered from 30 V there. The interesting thing about this is that

**Dave Jones:** there's it's actually switched off at the moment. If we switch it on, there we go. Um it's exactly the same. So, that op amp is always uh powered up cuz this is not a mains power switch. It's basically a uh soft power switch.

**Dave Jones:** It's directly across the LED and that's when it's um So, this is when it's off, it's -1.5. And then it's -2.9 basically when I switch that power on. So, in theory, that should be enough, but I've got the LED disconnected at the

**Dave Jones:** moment. And I've got the LED connected, switch it on. There you go, 2 V. It's obviously not enough to drive that blue LED. There's something in the circuitry that's starving the supply, the current supply on this thing, I think. And

**Dave Jones:** that's why we can't see it. Just measure a diode up here. 0.7, no worries. That goes through to the base of the driver down there. That's not a problem cuz it's all in circuit, but we're basically getting that 0.7. Yes, I

**Dave Jones:** know the battery indicator's on here. I know what I'm doing. I'm a professional. Welcome to Dave CAD Reverse Engineering. Please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. Here's our two LEDs.

**Dave Jones:** They're are back-to-back like this, anode cathode. I've done them with the correct polarity. Blue's opposite polarity like that. One side of them's going down to ground. That transistor there actually shorts them out. We'll see why in a second. And it goes through

**Dave Jones:** a LED dropper resistor here to an op amp. Now, I've actually measured this and when the power is both off and on, we've got negative 15 V. Basically, saturated at 14.7. It's saturated at the negative rail. So, that

**Dave Jones:** is the correct polarity. If this is not -15 V, the LED dropper, that's the correct polarity for the blue LED relative to ground here. Because this is ground is actually a higher potential than -15 V, the blue LED is going to light up.

**Dave Jones:** Simple. And likewise, if uh happens, I haven't uh like reverse engineered all this side. This is obviously coming from the clipping uh circuit, and as soon as it uh clips and wants to turn on the LED, it then drives this high like this, and

**Dave Jones:** that just drives the red LED like that, down to ground. So, plus 15 V, boom. And And the blue uh LED is um back to front, but it's not presented with a high voltage cuz it's going to be limited by

**Dave Jones:** the uh 1.8 V on the LED uh the drop on the uh red LED here, and vice versa, so they don't damage each other. So, there's no problem at all. So, what's this uh doing here? Well, I haven't uh seen where this goes off to,

**Dave Jones:** but somewhere on the uh power board. So, obviously, when you uh switch the power off, this actually uh turns on the transistor and then shorts it out. Oops, sorry. I forgot to draw in That's actually a Zener like that.

**Dave Jones:** Otherwise, um the polarity would be backwards on this. This has to have uh breakdown in order to do that. Anyway, uh when you switch the thing off, it just uh turns on this transistor via this uh pull up here, and

**Dave Jones:** then just switches uh both LEDs off. It doesn't matter what the op amp can be doing. It could be flapping around in the breeze over here, um oscillating the buggery, and it's not going to matter cuz this transistor is going to

**Dave Jones:** permanently short out both of those LEDs. So, when you turn it off, the LEDs go Both LEDs go off. So, this is uh pretty basic stuff. I mean, we could actually remove that transistor, and it should work cuz it's basically going uh

**Dave Jones:** negative plus minus uh 15 V there. If we actually suck that out, then um it it It's like it must work. So, I've actually measured the output voltage here. It is 14.7 V, but that's without the LED plugged in. So, let's plug the

**Dave Jones:** LED in, and And if we still get 14.7 V here, minus 14.7 V, that blue LED must come on if it doesn't, then there's obviously something wrong with this uh transistor here, which is um uh maybe partially on and then causing that blue

**Dave Jones:** LED to go off. And that kind of makes sense cuz we're getting seeing it going all higgledy-piggledy. So, you know, it's something something in here. I suspect it's not the op amp. Let's measure that. There you go, -13 volts

**Dave Jones:** and the blue LED, I can show you, is not on. So, therefore, that transistor must be conducting and uh causing that uh blue LED to switch off. We should be able to see that here if we actually probe the base voltage.

**Dave Jones:** -1.3 Huh. That's interesting. What's going on? I'm going to suck out that There we go, got it out. Let's test it. Base-emitter There we go, 0.76. And uh the good thing about the 15-V diode range here is we

**Dave Jones:** can swap that around and actually test the reverse breakdown, the emitter-base breakdown voltage. Data sheet says six, but it's a highly variable number. There you go, 7.7. So, it breaks down. So, I don't know. It's okay. Okay, this is getting ridiculous. I

**Dave Jones:** sucked that transistor out and the output of the op amp is -13.2 volts and I've got the LED connected and there's the voltage across the LED. There it is there. -1.9 and the blue LED's not on. What gives? There's no other path.

**Dave Jones:** There, that's ridiculous. Well, you can see it yourself here. There's the uh ground. There's the the which is the LED. Here's the other side of the LED. It goes over to this trace here. There's no transistor in there.

**Dave Jones:** Remember, this is a single sided board. Goes into a dropper resistor and through the pin seven of the op amp and pin seven of the op amp is minus 13. 2 volts relative to the blue LED should turn on.

**Dave Jones:** It doesn't. Well, I think I'm done. There's nothing wrong with that circuit at all. The only conclusion I can come to is that there's something wrong with the LED in there. Wow. Wow. Yes, I've measured the resistor. It's

**Dave Jones:** 1.5K. 13 volts. Do the math. There's the mongrel. It's embedded inside the plastic like this. So, it's some sort of I don't know. It's almost like it Oh, no. Is that Is that epoxyed in there? Or something. Anyway, it had all hot snot around here.

**Dave Jones:** I've cut all that off. But yeah, it's um it's well and truly stuck in there. It's integrated in the whole thing. Obviously, the rest of it's just a light pipe. Um so, I did There's one thing I can try. Um rather than just bodging

**Dave Jones:** another LED, what I can do is just snip the leads here, actually reverse them, and then I'll have a red power LED all the time and a blue one otherwise. Um for well, a non-blue one cuz there's something wrong with the blue. I mean,

**Dave Jones:** it It could be something, you know, it's something weird going on with the die. I don't know. A little micro attachment, little bond wire um issue or something like that. No idea. Anyway, this is fascinating. Watch this. I'm going to put another 1K

**Dave Jones:** resistor in parallel with the 1K on there. So, power's turned on. You notice that LED's off. Like nothing I physically do to it can make it come on. But watch this. I'm going to put 1K across there and it's on, right? And I disconnect it

**Dave Jones:** and it See, it stayed on for a bit. And I actually got it before I got it to like latch on. There's something weird that's happened with that LED. Oh, and it stays on. It stays on. It flickers.

**Dave Jones:** It flickers. Right? And I've monitoring the voltage. Um, the voltage is the same. Look, flickers on and off. I'm not touching anything. It's not Oh. No, it's it's not physical. Look, it's electrical. Wow. The last thing I would

**Dave Jones:** have expected. Inside I can't if it's blowing, fair enough. But some sort of electrical problem that we can solve by basically putting more current through it. Like that. So, to fix this I could just technically change the value of that

**Dave Jones:** resistor and everything's hunky-dory. But like it's just going to get worse. Like it could certainly get worse. Almost guaranteed. Look at that. I What? Unbelievable fault. Seriously, how lucky are we to find a fault like that? That is just that's insanely rare. So, after

**Dave Jones:** all that there really wasn't um a problem. I don't think there's a problem with the circuit at all. Yeah, and of course, you know, you'll go down the rabbit hole cuz like we were able to light the LED up and you know, you just

**Dave Jones:** assume okay, it's connected. It's not a physical, you know, I jiggled the wires and stuff. It was fine and dandy. So, you know, the LED works. So, it must be a problem with the LED driver. So, you go down that rabbit hole chasing a

**Dave Jones:** bloody red herring. And then you come back up the rabbit hole only to find the damn LED's at fault. Unbelievable. This thing is hilarious. It's just it's off. It's on. There you go. Back to front and got a

**Dave Jones:** nice red power LED. I like it. The blue clip LED. Who cares? I don't use the clip functionality anyway. I Yeah, I could have like wired in a proper blue LED. But then physical around and all that sort of stuff. It was easier just

**Dave Jones:** to reverse the damn thing. And yes, I know that the blue LED in reverse is actually protecting the reverse voltage of the red LED, so that may be a problem in the future, but now deal with that. Maybe I could add like another

**Dave Jones:** uh LED inside in parallel on the wires or or something like that. Um but I don't care. I like having this as a red. It differentiates it as, you know, one that's been hacked. And I soldered that poor innocent back in. And then

**Dave Jones:** sorry I suspected you, and there you go. We've got a nice red power LED. I like it. Fixed. Winner winner chicken dinner. So there you go. I hope you liked that one. We were very lucky to find a like a

**Dave Jones:** rather obscure problem like that, something wrong inside the LED. If you've seen this, had any good ideas, like I've seen them fail inside, maybe like an intermittent bond wire contact, but it seemed to be electrical. Maybe cast past current through it is making

**Dave Jones:** it like, you know, like a little uh diode connection inside, like a little point contact diode connection or or something's really, you know, there's a something physically wrong inside that thing that manifests itself um in terms of current. You put more current through

**Dave Jones:** it, it's fine. It sort of stays there. It almost like latches kind of thing for a bit, and then uh switches back on. So that was absolutely fascinating. And if you remember back in the video, we where we were passing current through that

**Dave Jones:** thing, lighting it up, that kind of gave us an indication. It didn't work um down at those lower currents. I probably should have like, you know, like sort of uh smelled a rat back then, but like hey, the LED came on. Let's,

**Dave Jones:** you know, you know, hurry, let's follow the circuit, you know, boom. That that problem's checked. So it's real obvious in hindsight, isn't it? Um but that's where it leads you. And yes, ironically, I'm going to go edit this

**Dave Jones:** video right now using this puppy. So, if you like that and found it interesting, please give it a big thumbs-up and as always discuss down below. Catch you next time.
