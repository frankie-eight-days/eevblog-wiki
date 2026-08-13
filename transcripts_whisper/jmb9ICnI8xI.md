---
video_id: jmb9ICnI8xI
title: Dumpster Tektronix 475 Oscilloscope Repair - Part 1
url: https://www.youtube.com/watch?v=jmb9ICnI8xI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 23, "2": 39, "3": 57, "4": 75, "5": 98, "6": 111, "7": 128, "8": 155, "9": 174, "10": 191, "11": 207, "12": 239, "13": 259, "14": 275, "15": 303, "16": 323, "17": 343, "18": 363, "19": 387, "20": 407, "21": 423, "22": 451, "23": 471, "24": 487, "25": 503, "26": 523, "27": 539, "28": 559, "29": 583}
---

**Dave Jones:** Hi, it's repair time! We've got a classic Tektronix 475 200 MHz band with analogue scope. Dates from 1972, was sold until the early 80s, and it's still a fantastic analogue scope. So I scored this from that big dumpster find, which I'll link in at the end and down below,

**Dave Jones:** if you haven't seen that, where I've got a whole bunch of stuff. This was the only scope I got out of the lot, but yeah, it looks nice. A few little, don't know, a few little things on the screen there. I'm not sure what the deal is there.

**Dave Jones:** Little marks, like, are they sort of like moisture or water marks inside the front cover or something? Anyway, looks in pretty good nick. It's got the delayed sweep time base, of course, with the verniers. Ah, beautiful. Thing of beauty. So a scope like this is still very useful today.

**Dave Jones:** And let's have a look on the side here. 09, faulty, stuck in XY mode. JF, oh well, you know, JF tested it, it must be stuck in XY mode. So let's power it up and see what the fault is. This is not, for those of you who want to know,

**Dave Jones:** this is an all solid state scope. So it's all transistors, none of that tube rubbish. Oh, I just noticed. Aw, jeez, that's a bit rude. Look at that. Aw, it's broken. Knob's broken. Damn. And these are what was in the pouch. They're actually Department of the Army, Navy and the Air Force, 79.

**Dave Jones:** So most likely this one dates from 1979. And we do have the schematics and everything else for it. And you can just download them all. For most of these, you know, tech scopes, you can get all the service manuals. And there's like a Tektronix Yahoo group out there.

**Dave Jones:** So if you're looking to buy one of these old analog tech scopes, there's like, you know, tons of help out there. And people available willing to help you out actually, you know, fix these things. Just join the groups. All right, so let's give it a burl.

**Dave Jones:** Plugged it in. Power on. Hey, we've got light. Times 10 mag on. So, whoa, something just went pop. Sniff. Yep. Yep. Yep. I think we released the magic smoke. Damn. And I just powered it up again, and I heard another. I was just trying to see if there's any trace whatsoever.

**Dave Jones:** Turned it up, and I heard another sort of louder pop this time. So, well, yeah, there we go. It just popped. So what is that? Like a high voltage arc over or something? It almost sounds like that, rather than like a cap blowing.

**Dave Jones:** It seems fairly consistent. It's happened three times in a row now. So what I'll do is I'll stick my microphone near it. Let's do it again. See if we get that pop. Yep, there it goes. Ha ha, sweet! This is hilarious. Something wrong with this manual?

**Dave Jones:** Then jot down the dope about it on this form, tear it out, fold it, and drop it in the mail. And where do you send it to? You send it to the commander, U.S. Army Communications and Electronics Material Readiness Command. Ha! Materiel? Materiel.

**Dave Jones:** Hmm. Fort Monmouth, New Jersey. So you take the screws out the back, and it should pull out. Awesome. Check it out. And there's the vertical amplifier section. You can see the two channels over here. 200 meg bandwidth. All the adjustment trimmer caps. And you can see that the

**Dave Jones:** shafts go through here. So these here are the position controls and of course you've got your vertical controls there, just a big block inside here. Substantial heatsinks on those. Haven't looked at the schematic. Are they your traditional fret-fet front end? Why you'd have some

**Dave Jones:** big-ass heatsink on those, I don't know. But looks like we've got some all that wiring coming off there. Another big-ass heatsink. Big grounding strap there going off to the side of the case. And copyright 1971, Tektronix Inc. Fantastic bit of graffiti inside there.

**Dave Jones:** There's nothing though that looks obviously blown. But the vertical board is not our concern. Notice, look, got some little wafer switches in there. Wow! Making contact with the board. What? Why? And here's your horizontal side of things over here, but look at this.

**Dave Jones:** This is the power switch. This rod going through there and then onto just your regular toggle switch on there with your mains voltage adjustment. That's brilliant. They obviously had another option here for a second switch as well. And this is all your high voltage and power supply stuff.

**Dave Jones:** And it's more likely to be something on here, but no visual indicators of course. You're looking for anything blown, like there's a fuse over here, it's intact. And the capacitors are on the other side of the board, they're actually connected in here. You can see

**Dave Jones:** those large solder joints, they're the huge filter caps on the other side. Nothing looks blown there. So everything's, you know, looks fairly decent. So there's your beam finder. Is that it yet? That's your beam finder I believe down there. And everything looks hunky-dory.

**Dave Jones:** So the good thing about this though, is that all that black silkscreen on there, or either it's a black silkscreen or it's actually in the copper there. You can see ground plus 50 volts and 50 volts unregulated up the top there. So first rule of troubleshooting, thou shalt measure

**Dave Jones:** voltages. Okay, first I'll measure that 50 volt unregulated section. Oh, 67 volts. That's a bit high. Whoa, yeah. That's a bit how you're doing. Ha ha! Something's, yep. Something's wrong with the power supply. Okay, test point marked 50 volts. Yep, it's 50 volts, but let's get the other rails.

**Dave Jones:** I don't want to leave this powered up for too long. For example, like there's plus 5 there. There's lots of rails everywhere. Plus 5, plus 8, minus 8, plus 50, I think that was 20 somewhere. Let's do that again. Oh yeah, 8.6 on the 5 volt rail.

**Dave Jones:** Yeah. That's not good. 8 volts. Whoa! Yep. It's good, but nah, something's going bang. This is one sick puppy. One of the problems with these old designs, look at all these old tagged tantalums here, here, down here. They're all over the shop. Over here, and this horizontal board here.

**Dave Jones:** You know, it's just got tagged tantalums. Like dozens and dozens of them all over the shop. The multicolored ones over here. Oh, and these are of course famous for you know, catching on fire, blowing, shorting out. Yeah, tagged tants. A lot of people servicing

**Dave Jones:** old gear will just replace all tagged tants, as they're called, tagged tants. You know, tagged tantalums. As a matter of course. You can see the big caps down in there. Once again, we've got some graffiti on those. I'm not sure who's been, you know, whether or not that was part of the

**Dave Jones:** original test back in 79 or whatnot. And of course these manuals are fantastic. The block diagram and the theory of operation of how it all works. Absolutely brilliant. They make them like they used to. Although I just recently found out that Siglent actually release

**Dave Jones:** service manuals, minus the schematics unfortunately, for their scopes. And you know, it's not as good as the old tech and other manufacturers' manuals back in the day, but anyway, it's noteworthy. Here is the block diagram of the power supply. So here's our, we've got a 110 volt rail,

**Dave Jones:** 50 volt rail, 15 regulated, unregulated, plus 5, minus 8, and minus 15. Actually that 50 volt unregulated one could be okay. Anyway, like, because you know, it's got to be above 50 volts, so that's all right. So let's do the 110 volt rail.

**Dave Jones:** Yeah, 111. That works. So there, yeah, so our 50 volt is good. Our 15 volt is good. Our 8 volt is, minus 8 volt is good. Minus 15 volts? No, our minus 15 volt is cactus. Our 5 volt rail is cactus. There's our CRT, for all you CRT

**Dave Jones:** aficionados. And the driver board for that looks all right. Love how they've got the big copper braid there. Tinned copper braid. Like welded to the case of that power amp or whatever it is down in there. That's terrific. Well done. Anyway, that looks quite

**Dave Jones:** jazzy. And you can see these coils down in here. That's actually a delay line, and that's how you get your delayed sweep.
