---
video_id: az4B2o4Kcsc
title: EEVblog #918 - REPAIR: Sony Pyxis GPS
url: https://www.youtube.com/watch?v=az4B2o4Kcsc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 52, "4": 68, "5": 87, "6": 108, "7": 129, "8": 145, "9": 159, "10": 179, "11": 197, "12": 212, "13": 231, "14": 247, "15": 261, "16": 285, "17": 310, "18": 322, "19": 334, "20": 360, "21": 376, "22": 394, "23": 416, "24": 436, "25": 453, "26": 466, "27": 483, "28": 502, "29": 517, "30": 536, "31": 555, "32": 576, "33": 596, "34": 618, "35": 638, "36": 661, "37": 678, "38": 700, "39": 717, "40": 736, "41": 751, "42": 769, "43": 784, "44": 808, "45": 823, "46": 838, "47": 850, "48": 868, "49": 883, "50": 898, "51": 916, "52": 952}
---

**Dave Jones:** Hi, in the previous mailbag video, David Voss kindly sent in this Sony FIXUS IPS 360 GPS from 1991. It's an absolute classic, and what I didn't mention in that video is that there is a fault with it. So I thought we'd actually take a look at it, not really because I want to use this thing,

**Dave Jones:** because it's, like, huge and, well, it's not obsolete, it could still give you a GPS, you know, reading and things like that, but yeah, it's... compared to today's modern GPS is what you can get in your phone or just a regular E-Trek scum, an E-Trek or something like that from 15 years ago, it doesn't even compare.

**Dave Jones:** But I thought it'd be interesting to do some troubleshooting of this thing and see if we can get it working. Now the fault is I've got four AA batteries in there, I've got it all hooked up, here's the power switch on the side,

**Dave Jones:** and it should, yep, there we go, it goes beep, comes on, that's in the position mode, so you can see the corresponding keys there, and we can put it in nav mode and stuff like that. But of course the fault is, is that we're getting absolutely nothing on the LCD there,

**Dave Jones:** and having a look at different angles, like, there's just not a thing there. So it seems to work, apart from that, because, you know, we're getting like a response, the LEDs are changing, it's beeping, it means the processor's working, everything's doing just fine,

**Dave Jones:** it uses a Hitachi H8 processor, as we saw in the teardown in the mailbag, it's got a Xilinx Z80 series processor up in the main receiver up here, but all that stuff's running on the H8, but nothing on the screen. And usually these LCD modules don't die, so we've got a Sanyo chipset on the back.

**Dave Jones:** The first thing I did, of course, is reseat the flatflex cable, look, inspect for, you know, any broken wires inside there and things like that, and I couldn't see anything, I haven't buzzed out every single connection over there for the flatflex, but yeah, I don't, it doesn't look like there's any issue there,

**Dave Jones:** so there's something else going on, possibly in terms of the bias voltage for the LCD, perhaps that could have failed, could be one of the LCD drivers failed, I hope not, because I won't have replacements for it, but anyway, let's go through troubleshooting, step by step.

**Dave Jones:** Now the first thing I've done is just disconnect this receiver, put that out of the way, because that's not what, we're focused on just the processor and the LCD here. So I've repowered it up, and it basically, as you'd expect, without the receiver there,

**Dave Jones:** it'll give you some sort of error, but, multiple beeps, error, position mode, but it still goes between the various modes. And, but it won't go back to position mode because, well, it knows that there's no receiver there. So anyway, it's still working, so I'd still expect to see something on the LCD with that disconnected.

**Dave Jones:** Anyway, with that disconnected, we can take this top board off here, that's got the super cap on it for the battery replacement, looks like there's some power supply stuff here, dead giveaway is of course the large tracers coming in and out, cap either side,

**Dave Jones:** so they're going to have an input to bypass cap, output bypass cap, so that's probably a regulator, might be another regulator package up there as well, because we've got a big output surface mount electrolytic cap there. So yeah, that looks like some power supply stuff,

**Dave Jones:** and of course, the first rule of troubleshooting, thou shalt test voltages. And it looks like there's a lot more power supply stuff here, I took this top board off, and there's nothing on the bottom there. So, but here's our, looks like we've got a DC input jack down here,

**Dave Jones:** and we've got a little transformer, so that's going to be some sort of switcher, and sure enough, that RF5RD part there, I wasn't able to get a data sheet, but I think it's a Ricoh, and it appears to be a step-up DC to DC converter with regulator,

**Dave Jones:** so yeah, that's what you'd expect under the transformer there. Now nothing on there is immediately familiar, so yeah, I'm not going to attack that first, I'm going to do the easy stuff that I know. But what we are going to look for is the easy stuff,

**Dave Jones:** the voltage test points first, if we can find them. So let's have a look. Hello! Looks like we've got minus 5 volts there. Is that? Yeah, that's plus 5, is it? And nothing else, buzzer. That's not going to help us. Oh, and by the way, you'll notice that minus 5 volts comes from this connector here,

**Dave Jones:** which was used to connect through to this board, and you might see something familiar, or I certainly do, a 7660 voltage inverter there, or a capacitor voltage inverter slash doubler. So it's either doubling that, or usually it's generating a negative output. So that would explain plus 5, minus 5 going into that connector.

**Dave Jones:** So our negative is most likely going to be the negative of our battery over here. That one looks like a big fat ground down there. You bet your bottom dollar it is. So we can either probe it from there or from that point there,

**Dave Jones:** but it's not convenient, doesn't have a via, so you can't get your probe off there and it could slip. Just be careful, trap for young players, don't want to short something out. Alright, so here we go, let's power this thing up, and we're going to measure...

**Dave Jones:** oop, that's quite loud and disturbing. And let's measure our plus 5. Yeah, our plus 5 is good, no worries. Minus 5. Wah, wah, wah, wah. So if we follow the money on that minus 5 volt rail there, it's no surprise it's coming out there.

**Dave Jones:** There we go, it's coming out of our 7660 inverter. But hang on, before we go off half-caught, we've got another couple of test points in here. This one's actually, I believe that's Vdig, so that'll be Vdigital, so that could be 3.3 or something like that.

**Dave Jones:** And this one in here's got the VRF, voltage reference, so that's pointing to that one in there. So I'm going to just have a quick measure of those two. We know our minus 5 volts isn't there, but our plus 5 is still there.

**Dave Jones:** So let's measure our voltage reference, 1.43, I don't know what it's supposed to be. But that's alright, there's something there. And Vdig. Well, there's nothing on Vdig either. Hmm. And you'll notice that Vdig is also coming from this, oh, is it coming from that top board?

**Dave Jones:** No, here's the connectors, it's going to that. Oh okay, yes, sorry, yes, it's going, no, that's going to that. Sorry, yes, it's going, no, that's going over to the GPS receiver connector. So yeah, that could actually be on the GPS receiver, so we might plug that in and try it again.

**Dave Jones:** And let's measure that again with the GPS receiver plugged in. Aha, Vdig is now 5.1 volts, no worries. So yes, my hunch was correct, it needed this receiver board plugged in before it would feed back, so that regulation's over on here, even though the test point is over here.

**Dave Jones:** So now the only thing we've got to trace is the one thing, one known fault we've got is the negative 5 volt rail, so back to that top board. Now the pin out of this 7660 voltage inverter here seems to be a bit strange,

**Dave Jones:** because normally pin 8 is the power here, and look, we've got this big trace coming in to this pin 7, and then we've got the, well, our output here, that goes off to our cap, okay? So that's no worries, it's going off to the negative of that cap,

**Dave Jones:** so that's normal. If the output was a negative supply, that's exactly what you'd expect to find. So that's okay, but then this comes back to pin 6 here, what's going on? And usually then there's a cap between the switching cap, it's got 7660 on it, it's doing voltage inversion,

**Dave Jones:** it's got to be a 7660, but it's not, doesn't look like the standard pin out, it's weird. Anyway, you could go crazy trying to reverse engineer that, and well, you don't have to, you're just chasing a red herring down a rabbit hole, probably.

**Dave Jones:** So we know that we're not getting our negative 5 volts, well, what's the problem? Well, here's one, here's our output cap, could be our output cap, could be our switching cap, perhaps I would suspect the caps over the 7660 inverter there, whatever the hell pin out it is.

**Dave Jones:** So yeah, I would, first protocol is I would suck those off and measure the value. Let's do the minus 5 volt output cap, wah wah wah wah, 600 nanofarads, it's supposed to be 22 mic, fail. So we'll replace that one there with a 22 mic cap,

**Dave Jones:** and we can measure the voltage across that, wah, still failed. So that cap was definitely dead, so we've replaced it, and we're still not getting our negative 5 volt rail out, and I'll just show you that, 5 volts in, and we're getting exactly the same as before.

**Dave Jones:** So we found a dead cap, but that is not it. Hmm, keep going, suspect the other cap now. So I've sucked out the other one there, which I'm guessing is the switching cap, and it's supposed to be 10 mic, and wah wah wah wah, 1.1 mic.

**Dave Jones:** So yep, that one's dead too, I have to replace that. Alright, let's try that one. I've replaced the 22 mic cap and the 10 mic cap there around that weird 7660, and ha ha ha! Winner winner, chicken dinner! Look at that, there you go, it was the 7660 inverter.

**Dave Jones:** No antenna unit, oh we can fix that. Alright, let's try the whole thing now. Sony GPS receiver, waiting acquisition. Well, we'll be waiting for a while for the acquisition there, because I'm in the middle of a concrete building here, don't even have any windows to look out from.

**Dave Jones:** But there you go, that is fixed, and of course we can flip that over and measure that. Good measure, just make sure that's fixed. Got our 5 volts going in, and bingo, minus 4.7, good enough for Australia, coming out, beauty. So I was a bit curious as to exactly what was going on with this 7660,

**Dave Jones:** and I traced it out, and this is what I got. Pin 4 is the plus 5 volts that we measured on the other main board down here at that test point. Pin 8 is actually the ground that we measured on the other test point, the negative of the battery.

**Dave Jones:** And 5 and 6 is the switching cap. And then, oh sorry, I forgot to have the minus 5 volts there. And then we've got a resistor between 2 and 3 here, and one's not connected, so... Now because we found two faulty caps on there,

**Dave Jones:** it looks like we've fixed the problem. I would also suspect the third one, but if you're going to do that, then, well, you've got to start suspecting everything over on this GPS receiver as well. A lot of them might have come from the same batch,

**Dave Jones:** are they the same value, 22s? Yeah, could be. They could have even come from the same reel. So yeah, I wouldn't be trusting those. So yeah, anyway, we fixed the problem, which is what we wanted to do. We wanted to track that down, but just be aware that you could

**Dave Jones:** actually go further and test that, and I'd have to take it outside and test the GPS, which I might do actually and see if it works. And yeah, well, okay, I'll put it back together. Alright, I'll go outside, need some vitamin D anyway.

**Dave Jones:** Looks like it's a 4-channel receiver. We've got 4 satellites on there, not getting anything in here. But look at this. A lock could take 20 to 30 minutes for the initialization. You wouldn't want to be in a hurry. Check it out. Looks like we have a lock on number 7.

**Dave Jones:** Lucky 7. That's what L stands for. So the others have yet to lock in. Oh, come on, you can do it. Alright, what I'm going to do is initialize the receiver because it could have last been on the other side of the planet.

**Dave Jones:** In fact, it was. So yes, clear, recall. What do I do? Yes. Clear. Clear. Okay, it's certainly changed satellite numbers now, so we'll see what happens. No, tried another set and it doesn't seem to be picking up anything. I only managed to get that one, so

**Dave Jones:** I'm not sure what's going on anyway. It's starting to rain here. I might have to get back indoors. So there you have it. I was able to actually get lock onto one satellite, so I'm not actually sure what's going on here with this 4 channel system and how the

**Dave Jones:** initialization works and stuff like that. The manual does say it can take up to 30 minutes, but I'm going to call that a relative win. If it can lock onto one satellite, then it's at least kind of doing the business. The receiver's still kind of working, and it wouldn't

**Dave Jones:** show that if it didn't actually get the data and was able to lock onto that one satellite anyway. So there you have it. I hope you enjoyed that little troubleshooting thing. Thank you very much to Dave for sending that one in. That was interesting.

**Dave Jones:** We at least fixed it as far as the fault that we wanted to fix, which was the LCD display. It turned out to be the good old capacitor, electrolytic capacitor again, as was seen in previous videos. Often you're not that lucky though. It could have been an LCD driver or something like that, but

**Dave Jones:** unlikely that it was. From the get-go it was most likely to be something relatively simple like that. Could have been the LCD itself, old age might have, you know, something might have happened to it or something like that. But my initial guess, like the bias

**Dave Jones:** voltage and stuff like that driving the LCD, so that negative rail that they were getting there, that was doing some of that business. So there you go. Yeah, I could trace it further, as I suspect you might suspect other caps on the board, so as a matter of course

**Dave Jones:** you might rip them off, test them, things like that. But as I said there were plenty in this receiver here, and well, this thing is, what, 25 years old? So yeah, it's not a real useful GPS anymore, but eh, interesting. So I hope you enjoyed that little

**Dave Jones:** troubleshooting video. If you did, please give it a big thumbs up. As always, links to the forum to discuss it down below or just leave it in the YouTube or blog comments. Catch you next time. And here's another good example why it's not a

**Dave Jones:** bad idea to have a couple of multimeters lying around.
