---
video_id: lypYZxIDBDs
title: EEVblog #135 - Kindle Case Mythbusting
url: https://www.youtube.com/watch?v=lypYZxIDBDs
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 27, "3": 39, "4": 50, "5": 68, "6": 95, "7": 110, "8": 124, "9": 137, "10": 153, "11": 163, "12": 192, "13": 205, "14": 220, "15": 231, "16": 241, "17": 252, "18": 267, "19": 276, "20": 285, "21": 302, "22": 324, "23": 341, "24": 351, "25": 371, "26": 385, "27": 395, "28": 406, "29": 415, "30": 428, "31": 440, "32": 456, "33": 477, "34": 489, "35": 500, "36": 509, "37": 520, "38": 531, "39": 541, "40": 555, "41": 573, "42": 583, "43": 596, "44": 604, "45": 621, "46": 633, "47": 645, "48": 658, "49": 674, "50": 693, "51": 706, "52": 721, "53": 731, "54": 751, "55": 769, "56": 793, "57": 807, "58": 821, "59": 833, "60": 848, "61": 857, "62": 869, "63": 888, "64": 900, "65": 908, "66": 919}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I've seen reports in the last couple of days about the Amazon Kindle 3.

**Dave Jones:** There's been a problem with it. People who have bought one of these genuine Amazon covers for it, the one without the light, they're saying that the things are resetting all the time.

**Dave Jones:** Thousands of people apparently are getting this problem and Amazon have actually been replacing them. They will replace it, but apparently sometimes it doesn't even fix the problem. So, there's something going on here and people have asked me to check it out.

**Dave Jones:** So, let's do just that. Now, I don't actually have one of these covers that doesn't have the light. This is a friend of mine loaned this to me and it's got the LED light on it.

**Dave Jones:** Now, apparently this cover does not cause this lockup problem, but I figure it's a good enough representation cuz I've looked at the photos and it looks like the attachments and everything which we'll go into are identical except for the fact that they're painted on this one.

**Dave Jones:** So, on the non-light version. So, that's not going to stop me investigating not having the exact cover. I think we can do some reasonable investigation without it. Now, the first thing I want to look at are these contacts here because I saw this on slashdot or via slashdot, somebody had actually noticed that on the case that this problem is, they're they're not the brass tabs like this or

**Dave Jones:** they're still brass, but they're actually covered black. They're completely painted over in black paint. They're not gold like this, but apart from that, they're actually identical retention clips. This one up here slides and they're the same shape and everything, but they're painted black.

**Dave Jones:** Now, this person noticed that it had after uh continual insertion and removal of the Kindle, it had started some of the paint had started to wear off and was exposing some of the metal.

**Dave Jones:** Now, they actually measured the resistance between these two terminals and they actually measured something. Well, that turned out to be incorrect. It was actually 2 megaohms they measured, but apparently I think they were touching the probes at the time.

**Dave Jones:** So, there's there was no I've heard that there is no issue on actual resistance between these two terminals on the cover in question. And even though this isn't the case in question, just for completeness, I will actually measure the resistance between the two terminals on here.

**Dave Jones:** And as you can see on this version, it's it's open basically. So, that's what it should be on the real version as well. So, there's no electrical contact between here.

**Dave Jones:** So, the prevailing theory is that these contacts are wearing away and or they're touching something internally to the Kindle. Now, we'll actually have a look at this. I've actually taken my Kindle apart and we'll actually investigate whether or not these contacts, if they're totally exposed, can actually short something inside the Kindle which can cause it to lock up or reset or something like that.

**Dave Jones:** Now, just to show you up close what this contact is actually like. This is the bottom contact here and as you can see, it's a curved piece of brass like this and the case under question is an identical one, but it's painted black.

**Dave Jones:** So, that's the bottom contact and this one here is the top contact. And as you can see, it's brass also, but it it slides like that to accommodate the that actually allows it to lock the Kindle to lock in place so that it doesn't fall out.

**Dave Jones:** So, these are identical on the other case. So, let's see if these can actually short out anything inside the Kindle at all. Now, let's actually take a look at the mechanism itself, okay?

**Dave Jones:** The Kindle goes into this bottom slot down here at an angle like that, and then it clips into through the two slots on the side of the Kindle into this top one.

**Dave Jones:** And as you can see, it can't fall out at all. No problems. It's kind of a neat little design. I don't mind it at all. And then to release it, you simply slide that back and it pops out like that.

**Dave Jones:** And let's flip it over and take a good look at these particular uh hooks in some detail, shall we? Now, here's the bottom hook down whoops. If I can get that to focus.

**Dave Jones:** Here is the bottom hook down here. And as you can see, there are four contacts. Now, these contacts are the um serial interface. And there they are in the order.

**Dave Jones:** The top pin is uh the uh TX. The next one is RX, then ground, and then there's a mystery pin, which we'll find out what that is in a minute.

**Dave Jones:** Now, this is the RS232 um UART serial interface to the uh internal monitor program for the main um microcontroller and the kernel. And um there's been a few hacks, people um accessing that sort of data to try and hack the Kindle.

**Dave Jones:** But that's what we're concerned about, these four pins in here and the theory that we're going to try and bust here that or confirm that the uh that somehow the metal this big metal contact down here shorts out um several one or several or all of those pins in there or contact something else to reset the Kindle.

**Dave Jones:** Now, the other um one up here is just a single contact. Now, if we take a look at this, okay? Let's get some focus on that. There's actually a flex uh membrane with a single connection with a single screw and then a single contact like that.

**Dave Jones:** So, this one's very simple. We've only got one contact to worry about up there. So, we've got four down the bottom, one up the top. Let's find out what they do.

**Dave Jones:** Focus on the bottom one here and thankfully four screws allow us to completely remove this top connector. And as you can see, the contacts are actually um staggered. These ones connect to the PCB, but the other ones in there are staggered so that it actually connects the ground and the other pin first and then the other two later.

**Dave Jones:** And that's a common concept inside connectors. Here's the actual board with the four contacts. These are the pads that uh make contact with the uh pins we saw. And as you can see, this one is actually uh grounded.

**Dave Jones:** This the um second pin from the bottom there is ground. So, all this exposed uh gold-plated copper all along this outer point here is all connected to the ground.

**Dave Jones:** So, we don't have to worry about that pin which comes through the the actual retention clip from the case shorting out uh that ground because it's going to you know, touching anything there.

**Dave Jones:** As you can see, there's nothing else in there at all for it to short to. So, the only thing it can possibly short to is physically inside these two connectors.

**Dave Jones:** Here inside these four contacts inside the connector. So, let's actually plug that up. Now, if you see, this will actually flip directly over like this and it will plug in like this.

**Dave Jones:** This is what it will actually go in like when you plug it in. So, you put it in like that. I can't get it. And then it flips around and it looks like it does make contact with all four of those pins.

**Dave Jones:** I've got the connector in here. Now, let's see which pins actually make contact with the outer lug, shall we? The bottom one does, no problems at all. The top one does.

**Dave Jones:** And so does uh RX. But it looks like that's it. It looks like when it's plugged in like that, uh the top one TX, the transmit pin, as you'd expect, does not make contact because uh that can actually drain the battery if um that's transmitting if that pin is transmitting something out, you don't want to be shorting that to ground.

**Dave Jones:** So, um but that could happen. So, we'll try that as part of our experiment to see if that causes the problem. But we know when you plug this in, three of those bottom pins are grounded.

**Dave Jones:** Now, to make our experiment a bit easier, what I've done is I've attached a wire to this terminal up here just to allow us to do some um hands-free actual clipping onto that terminal and a ground point here as well.

**Dave Jones:** Now, I'll prove that this one is actually a ground point by uh measuring between here and the second bottom pin, which as you can see, it's uh 0 ohms.

**Dave Jones:** So, it's actually that's part of the grounded circuit. And we'll start out by just measuring the base states of all these pins on this connector, okay? This one down the bottom is uh almost 1.8 volts, okay?

**Dave Jones:** The second one is obviously ground cuz it's connected up there. We've proven that. And the third one's also uh 1.8 volts. And the top one is 1.8 volts as well.

**Dave Jones:** And the Kindle is on, by the way. It's actually switched on. There it is. And from experiments other people have done, I do know that the top two uh pins up here are transmit and receive.

**Dave Jones:** As I've said, transmit, receive, and ground the RS-232 UART uh interface here. So, I'm not going to concern with those pins, but this bottom pin um I it has me uh concerned.

**Dave Jones:** I want to know what this pin actually is. My guess is this bottom pin down here is actually an input. Now, the reason I suspect this is because I reckon this metal contact down here makes contact with these pins down here and outputs a voltage on this top pin.

**Dave Jones:** Cuz we know it has to drive this LED. Now, the Kindle's turned on, so it must output a voltage across here and here, but we've already measured this pin up here and we're getting nothing.

**Dave Jones:** So, there must be some sense circuit which switches that in, and my guess is that it's the bottom pin down here. Let's check it out. Now, I'm measuring the top output here relative to ground.

**Dave Jones:** And we'll short out the two pins down the bottom, and let's see what we get on our output, shall we? Look at that, bingo! 3.9 V. Disconnect. And there you go.

**Dave Jones:** So, obviously, this bottom pin is controlling the output on here to drive the LED. So, that proves my theory that this contact down here shorts um the bottom pin and ground, which switches on the LED output.

**Dave Jones:** And just for completeness, let's use the oscilloscope here to see what the output is like. Is it a AC or is it a DC signal? So, I'll just let's just short the two pins out here, and bingo, there it is.

**Dave Jones:** 1 2 3.9 odd volts, exactly what we measured on the meter. So, it is definitely a uh DC signal. And let's see what happens when we hook up a white LED.

**Dave Jones:** Uh in this case, it's a uh Lumi LEDs uh 1-W LED directly up with no dropper resistor, straight on the terminals, and let's switch it on and see what happens.

**Dave Jones:** Yep, it works, but take a look. We're getting 250 mA, huge. Well, okay. Clearly, the um output here, the switched output controlled by the input, is uh not current limited cuz uh clearly, the LED they're running up here is not uh 200 mA.

**Dave Jones:** So, I would have expected 20 mA or something like that. But, let's see what the short circuit current is. So, I've got this on the uh 10-A range, and let's switch the output on, shall we?

**Dave Jones:** As you can see, it shuts down pretty quick. Let's try that on the milliamp range. And it jumps right up there and it's it looks like it's output short circuit protected.

**Dave Jones:** So, no problems at all. It won't switch on and as you can see, it's still functional. The whole Kindle still works, so not a problem. So, it doesn't matter even if you short out um this output here, it makes no difference at all.

**Dave Jones:** In fact, if you actually hold it on here and look at the output, it actually hiccups. There it is. It switches on, then off and it self protects itself.

**Dave Jones:** No problems at all. And now that we've proven that it can survive a direct short across the output when it's on, let's try just shorting out all of the pins down here on this bottom connector just in case it shorts out the TX pin and all sorts of things because that's what some people claim is that these connections are somehow shorting out inside to something.

**Dave Jones:** So, let's short them all out. I've got some alfoil here, by the way. So, let's put that on there across all the pins. You can't see that, but I've actually I've shorted out all the pins there and does it still operate?

**Dave Jones:** Yes, it does. It hasn't locked up at all. And that's what people claim. It resets, locks up, it'll take ages to reset. It's clearly not doing that. So, it survives shorting out all those pins and even if we connect this output here, okay, let's go to the top here, hold this on here and short it to all the pins down the bottom here.

**Dave Jones:** Short it down to everything. It's still operates. No problems at all. And if you try all combinations of inputs down here, um it doesn't matter what you actually do, what you short out, it makes no difference whatsoever.

**Dave Jones:** All the combinations and all and it still works. So, clearly, there is no issue at all with these contact pins shorting out anything inside this Kindle. So, there you have it.

**Dave Jones:** I think we've conclusively busted the myth that it's this problem is being caused by these metal tabs wearing off the black paint and somehow shorting something inside the inside the Kindle.

**Dave Jones:** Granted, we've only had a sample size of one here, but from a technical point of view, I can't see how shorting out any of these any of the external connectors in here can cause a problem.

**Dave Jones:** We You saw it. We drew 250 milliamps, quarter of an amp from this sucker, and it didn't reset, it didn't lock up, it didn't do anything. So, that was a pretty worst-case scenario, I think.

**Dave Jones:** We shorted all the pins out, and as you saw, the clearance around the the keyhole connectors here means that there's no way that those connectors can touch any of the other circuitry.

**Dave Jones:** So, myth busted. It's not that. So, what is it? Well, I don't know. My next best guess would be ESD, electrostatic discharge, maybe caused by the case or something like that coupling into the contact terminals, but why it only happens on the non-LED version.

**Dave Jones:** This is the LED funky little pop-out one. Apparently, it doesn't happen on this. There's But, the identical version of this with the black paint painted tabs, it happens on.

**Dave Jones:** Why? I don't know. I've tried some ESD stuff. Can't kill it at all, but I need to do further investigation on that to try and figure it out. But, I don't know.

**Dave Jones:** It's definitely not the tabs. So, I hope that's cleared that up. All those comments on Slashdot and everything else, people thinking it was that. Sorry, I don't think so.

**Dave Jones:** I'll keep you updated if I find anything further.
