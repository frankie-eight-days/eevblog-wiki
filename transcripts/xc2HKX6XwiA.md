---
video_id: xc2HKX6XwiA
title: EEVblog #649 - Power Designs 2005 PSU Teardown
url: https://www.youtube.com/watch?v=xc2HKX6XwiA
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 24, "3": 40, "4": 55, "5": 78, "6": 92, "7": 102, "8": 121, "9": 141, "10": 158, "11": 171, "12": 183, "13": 194, "14": 203, "15": 216, "16": 226, "17": 239, "18": 250, "19": 262, "20": 275, "21": 291, "22": 305, "23": 325, "24": 334, "25": 348, "26": 362, "27": 374, "28": 392, "29": 409, "30": 425, "31": 442, "32": 458, "33": 471, "34": 488, "35": 505, "36": 526, "37": 535, "38": 548, "39": 561, "40": 573, "41": 595, "42": 606, "43": 614, "44": 623, "45": 633, "46": 643, "47": 659, "48": 669, "49": 680, "50": 694, "51": 707, "52": 726, "53": 740, "54": 748, "55": 762, "56": 773, "57": 791, "58": 802, "59": 813, "60": 821, "61": 837, "62": 851, "63": 866, "64": 883, "65": 891, "66": 905, "67": 917, "68": 937, "69": 955, "70": 967, "71": 979, "72": 993, "73": 1006, "74": 1018, "75": 1035, "76": 1053, "77": 1061}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We're going to take a look at an interesting power supply today. It's from a company called Power Designs Inc. in New York and it's a precision power source.

**Dave Jones:** It's a model 2005 and just as the name suggests it is a precision power supply and you can tell just look at these funky dials here with a nice precision vernier.

**Dave Jones:** The feeling that is just unbelievable and uh that's got a 100 microvolts adjust range by the way and you can basically just dial in the voltage you want here 5.000.

**Dave Jones:** Yes and then you can adjust it by I'm not sure if it's plus minus 100 microvolts or plus minus 50 volts but a 50 microvolts but yeah, a real precision power supply and it's incredibly it's not just precise in terms of actual precision.

**Dave Jones:** When you talk about a precision power supply it basically means it's stable. Hence the light up here for the oven on the thing. Yes, it's got an oven stabilized zener reference in it and that's why the stability is .001% plus 100 microvolts over an 8-hour period or basically 1 microvolt per week or better than that.

**Dave Jones:** So it's a really nice stable supply and low noise and ripple to less than 100 microvolts peak-to-peak. Now the vintage of this thing hold on to your hat 1964.

**Dave Jones:** That's what's on the schematic that I've got. I don't suspect this one was manufactured then. I'm not sure we won't know until we take it apart and maybe we might be able to get a date code out of it.

**Dave Jones:** I don't know. Maybe not though because there's no like you know ICs in this thing. It's all transistorized. Yes, it's a solid state precision power source and these are actually quite popular on eBay and And there's a like a a big forum EV blog forum thread on them and people love these sort of things.

**Dave Jones:** And it really is actually quite nice with that, you know, to dial in the voltage like that is just beautiful. And basically we've got oven light, that's the thermostat light, and that analog meter really understates the precision of this thing cuz once you actually calibrate it, there's a calibration trim pot on the back that you can, you know, a little multi-turn pot on the back.

**Dave Jones:** You can calibrate it but once it's calibrated and the oven's on and it's stable and everything else then, you know, the precision is quite remarkable on this thing. So, yeah, I mean we've got switchable volts current metering.

**Dave Jones:** We've got a shorting switch on the front which allows you to set the current limit. That's only a single turn pot, but that actually feels really quite nice. And but the big feature of this, of course, is the voltage.

**Dave Jones:** You can just dial it in. Look at that. You can dial it into 1 mV and then, as I said, 100 µV adjustment beyond that. So, it's very nice and it's got a range doubler on it.

**Dave Jones:** You can actually, normally it's from 0 to 10 V, 0 to 500 mA, but you can switch it to 10 to 20 V and that just this light here comes on, adds 10 V onto whatever.

**Dave Jones:** So, if we had 5.000 dialed in, that'd be 15 V. And on the back panel here, you can see that calibration trim pot there. Yeah, you don't want to go around with that.

**Dave Jones:** There's no date code on the back, unfortunately. I've just got model 2005. Serial number is 602190. And by the way, if you are going to buy these on eBay, just be aware they are a fixed 110 V unit.

**Dave Jones:** So, I've if I want to run it here, I've got to run it from a conversion transformer. I don't believe there's any internal switch to convert it over to 240.

**Dave Jones:** And it's got both an AC line fuse and a DC fuse on the output of the transformer on the thing. So, bit of extra protection there. Remote voltage sensing here, very nice.

**Dave Jones:** These are just strapped across in place, but of course with a precision power supply like this, you want to actually be able to sense the voltage right at your load and that's what these sense terminals are.

**Dave Jones:** I mean, there's no point having a nice precise 5.000 volts on the output of your power supply if then you're going to drop some voltage over a couple of uh you know, feet of cable going to your product under test.

**Dave Jones:** So, you know, a precision power supply pretty essential to have these sense terminals on them. All right, let's crack this thing open and uh it's going to be very, very old school in here, of course.

**Dave Jones:** I mean, we're talking, you know, mid-60s. The schematic actually shows it was revised around 90 uh 67 Geez. Hadn't even landed on the moon then. Unbelievable. But uh you know, this thing can still hold its own today.

**Dave Jones:** Um and uh by the way, this one does work, but uh it's not um in spec. Like, it's not even close. Like, I dial in 5.00 and I'm getting out like 5.3 or something like that.

**Dave Jones:** Ta-da! Let's take a look. Woohoo! Oh, yeah. First thing, look at this very nice impression under the case, by the way, and then a TO3 package inside of there and that's an RCA brand RC1700.

**Dave Jones:** Never heard of it before, but it's a big chunky old school PNP power transistor in TO3 package. Nice. And we can refer to the schematic here. Look at this.

**Dave Jones:** Uh 1964. Can you believe it? Wow. And uh I'll link in this PDF that this was scanned in. I found it on Paul Raco's uh website and he's the one who scanned it in.

**Dave Jones:** So, thank you very much, Paul. And there's the pass transistor there, classic Darlington configuration, of course. You need the Darlington to get the extra gain because you're only using a crappy bipolar transistor with really low gain there.

**Dave Jones:** So, you really need to have that Darlington configuration to get the performance of the thing. And so, nothing special, but all the power is being dissipated in that RC 1700 on on the side of the case there.

**Dave Jones:** You can basically see that there's not a huge amount in this, nor that nor would you expect there to be really. It's just your basic linear supply. But look at all these precision resistors over here with all your dials and then you've got your calibration and vernier trim adjust.

**Dave Jones:** You've got your thermostat here. So, everything inside that line there is ovenized. So, you've got your heater up here and thermostat control. And then, yeah, look we've got a current mirror there and one of those will be our Zener reference down in there buried.

**Dave Jones:** But the interesting thing to note about this power supply is that it doesn't sort of make sense at first glance. And the reason for that is because the negative is up here.

**Dave Jones:** Here's the negative terminal up the top and the positive is down the bottom. So, basically everything is flipped around. So, pretty much you have to turn it upside down to get a more like conventional configuration on this thing and then it makes a bit more sense.

**Dave Jones:** So, yeah, they've drawn it a bit weird. I don't know. So, when it's upside down like that, you can see that basically the positive output here goes basically directly over here through to the transformer.

**Dave Jones:** So, all of your your regulation, your pass element is done on your negative output here and here it is. There's your pass element down there. So, it's all done on the low side, not your more traditional high side.

**Dave Jones:** But, really that's neither here nor there whether you use a high side or low side pretty much. But, basically the way they're getting the really low noise here, basic NPN pass element which basically means it's going to be super super stable regardless of capacitive load or anything else.

**Dave Jones:** And it's just a nice stable configuration to use. So, it's not particularly efficient doing it that way, but your side benefit is that it is ridiculously stable. So, that's how they can get the confidence in this thing, the low noise, the ultra stability, everything else.

**Dave Jones:** But, in terms of absolute reference stability, of course, that's all determined by your ovenized reference oscillator here. These days you wouldn't need an ovenized oscillator. You could get a precision, you know, reference solid state reference source, you know, a Benny Berry does Zena reference or whatever.

**Dave Jones:** And, you know, Bob's your uncle. Too easy. But, back then, yeah, let's whack it in an oven. Now, if you take a look inside this thing, I mean, crazy old school construction here.

**Dave Jones:** Look at all the loomed wiring. Look, like loomed every like centimeter or two. Absolutely brilliant with wires branching out at the exact point that they need to branch out at.

**Dave Jones:** It's a thing of beauty. Really is. And, here, this big and nice red can here is our oven amplifier oven stable. It's a reference amplifier oven and it's got its own particular part name.

**Dave Jones:** And, yeah, all your circuitry is built into there plus your heater. Your heater would probably be at the bottom, I would guess. I'm not going to destructively tear down that sucker.

**Dave Jones:** It's just not worth it. This thing is interesting. At first glance, It looks like a pot, you know, a big old school pot. But what the hell is it doing mounted on this tag board Well, not tag board, but a sort of Actually, I don't even offhand I don't even know the name for these boards with the eyelets in them like that.

**Dave Jones:** I mean, it's a Yeah, I don't know. Please, somebody jump in. Somebody older than I am with a really big gray beard Sprague capacitors. We'll take a look at those.

**Dave Jones:** But yeah, that almost looks like a pot with its three terminals down in there, and I'm not sure what that thing's doing at all. I have to cross-check on the schematic.

**Dave Jones:** And sure enough, I found it. It's actually R12 down in here. So, it is actually a trimmer on the board. So, there's no access on the outside of the case.

**Dave Jones:** So, that must have been trimmed with the bottom of the case. Presumably, you can just take the bottom of the case off. Otherwise, they would have had to trim that before they installed the board.

**Dave Jones:** And of course, yes, I was right. Four screws on the bottom. Ta-da! Lift it off, and bingo, we're in like Flynn. Oh, and that's just more beautiful than looking in the top side.

**Dave Jones:** That side was a bit ugly, actually. But this is beautiful. Look at these upside-down metal can transistors here. And point to point to these standoffs that you know, eyelets on the other side that have component leads going through them.

**Dave Jones:** So, this is basically a double-side mount board. Beautiful. Look at this transistor over here has its own little heat sink on it. Nice little fin heat sink. Here's our oven reference.

**Dave Jones:** They've got a cap bodged onto that a little tin in there. And bingo, here is our trim pot. There we go, accessible from the bottom side of the board.

**Dave Jones:** So, maybe I can trim that thing back into spec. Hmm. And here we go. Let's give this a whirl, shall we? I've got it set to 5.000 V. And as you can see, 5.162.

**Dave Jones:** So, uh the trimmer on the backside here, I can adjust that. And basically, we're getting, yeah, a very small adjustment range with the trimmer on the back. So, I'll put that in about the middle.

**Dave Jones:** And sorry, could you see that? No, probably not. And then we'll have a trim of this one. I haven't actually given this a go. Here we go. Yeah. That's feeling very Oh, no, it doesn't quite go all the way down.

**Dave Jones:** Doesn't quite go all the way down. Let me try the backside. Again. No, I don't think. No, that's as low as No, unfortunately, that's as low as we're going to get it.

**Dave Jones:** We're out of spec, so yeah. Well, this won't be a troubleshooting recal video. I was just hoping that we might be able to do that. Aha. What's this trimmer here?

**Dave Jones:** Nothing precision like this one. This one's nice wire, huge wire wound pot. And it just feels beautiful when you turn these wire wound pots. You can just feel the wiper scraping over the wires.

**Dave Jones:** Lovely. No, I just checked the schematic. This pot down here is R27 over here. I love Sorry, R27 over here. I love this diagram. It's just beautiful. It really is.

**Dave Jones:** R27 is part of the current sense circuit there. So, no, I'm afraid there's something else. By the way, when you're testing any gear, especially really old gear like this, just be aware of any any corrosion inside the contacts of these things.

**Dave Jones:** Look, it can be a bit dicky. You've really got to make sure you get it right and stable before you start trimming these things. But you really can like dial this up just one digit.

**Dave Jones:** There. There we go, another digit. I mean, you know, it's pretty close. So, and then you can go the next digit up to three, four, five. You know, so it's all working hunky-dory.

**Dave Jones:** It's just a little bit out of cow, that's all. Bummer, I can't pull it back in with the standard controls. And this main Sprague filter cap here, check this out.

**Dave Jones:** Really old school, but do we have ourselves a date code? Look, 6552 on the outer plastic shield and on the inner can 6543. So, we we could be talking 1965.

**Dave Jones:** Woohoo! And some more Sprague capacitors there, really old school. Look, you can tell 100 MFD. And that is microfarads. Yes, they didn't use them you know, the mu symbol back then.

**Dave Jones:** It was yeah, MFD, MF, microfarad. And you'll notice this in the data sheet as well for the thing. You'll see the specs like the stability stick spec for example is you know, .001% plus plus 100 MV.

**Dave Jones:** And that's not millivolts, it's actually microvolts. So, yeah, that's just old school talk. And check out some of that switch mechanism in there. I mean, you know, jeez, you'd want to if you're going to do these, you'd want to go in in there and get some contact cleaner.

**Dave Jones:** I don't think you know, I've rotated and you want to rotate these things a whole bunch of time as well as well as using some contact cleaner on the things.

**Dave Jones:** But yeah, that's not my problem here. I've already I haven't cleaned them, but I've already rotated them and stuff like that. So, obviously there's something else wrong that doesn't allow me to trim it within range.

**Dave Jones:** We've got ourselves a combination of precision resistors in here plus plus your more common just your regular run-of-the-mill carbon ones where you know, temp co and precision isn't critical.

**Dave Jones:** Check out those tiny little diodes in there. They're probably like little point contact germanium's or something like that. And just because I can on my new Canon HFG30 camcorder, that's which has twice the zoom of my other one with my times 10 macro lens, there we go.

**Dave Jones:** Oh, that's fun. Woohoo! Look at that. Beautiful. Although not exactly the best uh subject really. A old school uh big wire uh point-to-point wired device like this thing. Not exactly a great test for my uh new camera and macro capability.

**Dave Jones:** But just take a look at how that wire is just, you know, nicely wrapped through there properly and then soldered pro- they really knew how to, you know, wire stuff back then.

**Dave Jones:** And the wiring looms, I mean, look at that. Just beautiful. But I just find it really fascinating like the double-sided board construction there with these eyelets and the point-to-point wiring on the bottom.

**Dave Jones:** And it just, yeah, it really brings back old school memories, that's for sure. And uh yeah, this was, you know, pretty uh state bit of a state-of-the-art power supply back in the mid-'60s, that's for sure.

**Dave Jones:** Anyway, that's just a brief look inside this uh power designs 2005 precision power source. And it really is very nice. There's our current limit. We can set it. Look at that.

**Dave Jones:** There we go. Turn it in. It seems to be working, but uh yeah, just slightly out of spec, which is a little bit of a bummer. You'll see that oven light actually uh switch off there at some point when it cycles through the uh thermostat light.

**Dave Jones:** But uh yeah, I just love these things. It's just very nice. It just oozes precision, the front panel. It's just beautiful. That was a very quick teardown. And by the way, with my new uh Canon camera here, it's actually showing the total time elapsed since I started shooting.

**Dave Jones:** I've shot uh 24 minutes and 28 29 30 seconds worth of footage. So, that's enough. I mean, I don't want to tear it down any further. There's nothing interesting, but I might do a follow-up video with this if people are interested in trying to bring the thing back into spec.

**Dave Jones:** So, I hope you like that little teardown Tuesday for some vintage stuff. I mean, this was before even I was born, and I'm pretty old. So, there you go.

**Dave Jones:** If you like it, please give it a thumbs up. And as always, you want to discuss it, jump on over to the EEVblog forum or EEVblog.com. Catch you next time.
