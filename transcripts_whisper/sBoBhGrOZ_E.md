---
video_id: sBoBhGrOZ_E
title: EEVblog 1433 - More Adventures in Sony RX100 Repair (Part 3)
url: https://www.youtube.com/watch?v=sBoBhGrOZ_E
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 22, "2": 31, "3": 52, "4": 64, "5": 78, "6": 98, "7": 117, "8": 135, "9": 156, "10": 170, "11": 190, "12": 208, "13": 228, "14": 246, "15": 264, "16": 283, "17": 299, "18": 319, "19": 334, "20": 355, "21": 375, "22": 389, "23": 409, "24": 431, "25": 453, "26": 468, "27": 489, "28": 508, "29": 529, "30": 554, "31": 570, "32": 589, "33": 619, "34": 649, "35": 649, "36": 679, "37": 739, "38": 739, "39": 799, "40": 829, "41": 829, "42": 888, "43": 918, "44": 948, "45": 978, "46": 1008, "47": 1038, "48": 1068, "49": 1098, "50": 1128, "51": 1158, "52": 1188, "53": 1218, "54": 1248, "55": 1278, "56": 1308, "57": 1338, "58": 1368, "59": 1398, "60": 1428, "61": 1458, "62": 1518, "63": 1818, "64": 1848, "65": 1872, "66": 1890, "67": 1902, "68": 1920, "69": 1938, "70": 1956, "71": 1970, "72": 1992, "73": 2008, "74": 2026, "75": 2046, "76": 2068, "77": 2098, "78": 2112, "79": 2140, "80": 2162, "81": 2180, "82": 2202, "83": 2222, "84": 2244, "85": 2262, "86": 2286, "87": 2308, "88": 2322, "89": 2338, "90": 2362, "91": 2386, "92": 2410, "93": 2426, "94": 2442, "95": 2458, "96": 2482, "97": 2510, "98": 2530, "99": 2554, "100": 2578, "101": 2598, "102": 2622, "103": 2638, "104": 2650, "105": 2666, "106": 2686, "107": 2702, "108": 2722, "109": 2734, "110": 2754, "111": 2778, "112": 2794, "113": 2814, "114": 2830, "115": 2846, "116": 2870, "117": 2886, "118": 2902, "119": 2922, "120": 2938, "121": 2954, "122": 2970, "123": 2986, "124": 3010, "125": 3030, "126": 3050, "127": 3074, "128": 3086, "129": 3102, "130": 3123, "131": 3139, "132": 3155, "133": 3171, "134": 3187, "135": 3207, "136": 3223, "137": 3243, "138": 3259, "139": 3283, "140": 3299, "141": 3319, "142": 3335, "143": 3355, "144": 3371, "145": 3383, "146": 3399, "147": 3419, "148": 3435, "149": 3455, "150": 3467, "151": 3487, "152": 3507, "153": 3527, "154": 3539, "155": 3559, "156": 3579, "157": 3595, "158": 3611, "159": 3627, "160": 3647, "161": 3667, "162": 3687, "163": 3703, "164": 3739, "165": 3759, "166": 3779, "167": 3803, "168": 3823, "169": 3839, "170": 3851, "171": 3871, "172": 3891, "173": 3911, "174": 3923, "175": 3943, "176": 3959, "177": 3979, "178": 3999, "179": 4015, "180": 4035, "181": 4051, "182": 4063, "183": 4083, "184": 4099, "185": 4119, "186": 4139, "187": 4151, "188": 4175}
---

**Dave Jones:** Hi, back onto the repair for the Sony RX100 Mark IV camera. I've done two previous videos, so this is number three. The TLDR is that, well, the camera's rooted. I kind of, sort of, fixed it in the first video by taking it all apart, putting it back together, and it seemed to work for like a day, and then came back the next day and it just didn't work again.

**Dave Jones:** So, at the current state of this thing, I've taken it back apart, I've got a battery in there, which is good, and it doesn't, the power button just doesn't switch anything on. But if I plug in external battery pack here, and I press that, it should come on orange.

**Dave Jones:** Yep, sometime later, so it flashes orange, but it only flashes the orange once when I press that. So, I have no idea what that means. I don't have the screen plugged in, so maybe that's it, I don't know. But, like, I don't know.

**Dave Jones:** I tried that before, and it just didn't work. So, anyway, leaving the screen off, that's that connector there, because it's really annoying. Anyway, let's go into the schematic, and let's have another crack at this thing, shall we? So, we've got the schematic here.

**Dave Jones:** This is the power block. Well, this is like the block, system block diagram. There's a more detailed schematic further down, as we saw in the previous video. And, if we have a look over here, here's our battery terminal. It's got positive and negative.

**Dave Jones:** It's got the sense wire. So, that's battery temp. I don't, you know, it's got nothing to do with that. Anyway, our battery unreg comes into here. So, it goes through this flex board, and then it comes into system 1052 board, which I believe is, like, the main board that we're looking at.

**Dave Jones:** So, it's got the processor, everything. You can see that, like, it's got a USB interface chip. It's got a DC to DC converter chip here. There's another chip there, IC8400 front panel control processor. And then we've got the IC6000, which is the big chip, which we saw on there like that.

**Dave Jones:** That's the big daddy there, which is not just these pins. It's across multiple sheets and everything. And, as you can see, the unregulated battery, it goes into the USB interface. Eh, I don't, you know, let's follow the money down here, shall we? It goes into the front processor we don't care about.

**Dave Jones:** But then, we do care about this. It goes into this voltage detection. Uh, thing, by Q. It's a transistor, um, given the designator Q. So, a voltage detection and then a charge detection as well. So, if there's something wrong in there, then, yeah, you'd expect it not to boot up.

**Dave Jones:** Um, at, at this time, we don't know. I have, I have no clue why it, like, it came good and then didn't work again. I don't know. We could be chasing a red herring down a rabbit hole here. Um, but, hey, I want to at least try and measure the voltage on here.

**Dave Jones:** See if the voltage is getting from the battery to that board. So, uh, yeah, let's do that. So, Q3001, so we can find that, Q3001, ta-da, there it is, I love it. Um, search is good when these documents are searchable, they're fantastic, otherwise it's a real pain.

**Dave Jones:** Um, so, yeah, it looks like we have, uh, a couple of MOSFET jobbies here and it doesn't go directly, this is battery unreg going in here. It doesn't go directly in, it goes via a 1 meg, um, and then over, this is Q3001 over here.

**Dave Jones:** So, alright, uh, and X system reset. So I soon, like, nothing comes from, so I don't know, I haven't traced out the soft switch yet, which is the one on the top, the soft, uh, power button. Maybe, maybe I should do that. Now, there is a bat sense switch here.

**Dave Jones:** I don't know. See, there's so many. So many things that you have to trace here, like, you know, I can think of scenarios, just off the top of my head, where it could be any one of these different things. I could probably come up with half a dozen different scenarios that would cause it not to, like, to, you know, not power on like this.

**Dave Jones:** But obviously, if we feed 5 volts into the board via the, um, external USB, it, uh, you know, at least the processor, there's voltage on the board, the processor, the soft power button, it's doing something, um, things like that. So, yeah, I mean, it could be something there, so we can find Q3000.

**Dave Jones:** Anyway, let's just find Q3001. Here we go. It's got the overlay. Beautiful. Sony. Hats off. That is the bottom side of the board. Yeah. Here's the top side. Here's the top side. Murphy. Of course it's on the bottom side, where I can't probe it.

**Dave Jones:** Of course! I, like, and we've seen how, if you try and take this thing out of here, then the ribbon cables pop out, and it's just, I, it's just, no, no, no, it's, it's really horrid. I was hoping that would be on the top, but of course it's not.

**Dave Jones:** Anyway, maybe we can measure something else. Like, what's, what's IC4302 in there? Like, you know, like, can we at least see that there's voltage getting on the board there? Bloody double-sided loads like this, and, you know, BGA, BGAs, BGAs up the wazoo. Okay.

**Dave Jones:** Oops, sorry, I didn't show you that. Yeah, I had the wrong screen switched in. BGAs up the wazoo here. Like, BGA over here, over here, over here. Like, yeah, nah, thanks. That's a real pain. And there's a giant one on the bottom as well.

**Dave Jones:** IC6000 is IC9012. Massive thing on the bottom. So that, wow, that is really a board and a half. I at least want to see if I can probe something on the top. That's what I'm looking for. I want to see that it gets from the battery, through the contacts, through, at least onto this PCB.

**Dave Jones:** Otherwise, well, that's why it's not powering up. Right, so I'm going to rule out probing that transistor on the bottom. What about this thing on the top here? What about IC4302? That looks like it does something important. Surrounded by all these inductories and these capacitators.

**Dave Jones:** IC4302, it's a PST8623. Sounds like a lot of power. Sounds like a lot of power. Sounds like a lot of power. Looks like a little regulator jobby. And, no, it's a reset. Actually, that looks pretty important, doesn't it? That's reg, unreg, that's the one coming from the battery, isn't it?

**Dave Jones:** Yes. Oh, no, that's bat unreg. So bat unreg goes into here, and then reg unreg comes out of this USB interface chip. Oh, okay. So, it could be, like, yeah, okay. So, reg unreg goes all the way over here to the DC-to-DC controller.

**Dave Jones:** And, over to here, there's also a fuse there. It wouldn't be that fuse, because a USB V-bus is obviously coming in. No, now I'm thinking that's the, like, like the USB accessory. No, because there's another USB power on down here. Oh, see, there's, like, so many.

**Dave Jones:** And then, then you've got some diode or in here for the X power on. And the, and... The X power on accessory, I assume ACK is accessory, and then X USB power on, and I, like, that's all over the shelf. See how you can spend hours and hours, even though, even when you've got the full schematics like this.

**Dave Jones:** Um, yeah, like, and as I said, I could figure out a dozen different ways that this could fail. So, you've got to, you know, it's, you've got to pick your obvious ones first. Like, things that you can measure easily, measure them. As simple as that.

**Dave Jones:** Thou shalt. Thou shalt measure voltages, unless they're hard. Um, and then, yeah, measure the easy ones first. Ah-ha! There we go. X power on. That's got to be. It's on-off. It says on-off. That's got to be. That is the tactile switch. Okay, so we know the tactile switch works.

**Dave Jones:** We know the lead under it works, because that's, like, the power, it looks like, is that a dual lead? Yeah, it's, yeah, because they're, they're similar proximity. So, you know. You know that those leads, it's probably a, like, a bi-color, uh, thing. Uh, D, no, they've got separate D's on them, but, yeah, um, yeah, I think it does come up different colors or whatever.

**Dave Jones:** So, that's the orange lead that we saw before USB VBUS detect. So, it was obvious, so when we press the button, it, after a couple, like, three or four seconds or something, then that lead came on, right? So, we know that all this flex board here is all okay, because this switch goes over to X.

**Dave Jones:** So, we know that there's an X-power on, so, if we copy and find that, right, X-power on, what, yeah, okay, so it goes through, and then S-triple-O-one. What's S-triple-O-one and a depression? Ah, uh, I have to think about that a bit more. Uh, where else does it go?

**Dave Jones:** Yeah, it goes down here. Oh, X-power on, uh, uh, Piro. X-power on, one X-power on, bleh, bleh, bleh, no, no, we want, we could probably put a space after that to search for just X-power on, because there's X-power ons with lots of numbers after them.

**Dave Jones:** X-power on, here it is, yeah, alright, so that comes through, that little diode, all jobby there, okay, and then we've got a link here, and it, and that becomes X-power on, uh, P-I-R-O, whatever that is, power, I, I don't know. So, the switch comes on.

**Dave Jones:** It pulls that shocky diode low, and then you can also do that with the X-power accessory, that makes sense, okay, so if either of those go low, it switches the camera on, so you can remotely switch it on via the external, and then it becomes this, okay, so we could search for, we could search for C-3-double-O-four, I mean, if that's on the top, right, if that's on the top, we can find that, okay.

**Dave Jones:** Except, there's another one? Oh, no, that's on the, no, okay, so this is the real schematic, the other, as I said, was the, um, like a block diagram kind of thing, oh, it's not gonna, oh, there it is, there it is, right up the top, there, that's on, not, no, that's on a different board, that's on the bottom board, that's the SD card board, that's useless for us, that's even more inaccessible than the bottom side of that top board there, so, no, screw that, alright, so we're back to here again, are we?

**Dave Jones:** Okay, so we're back to here, and then, of course, this will all be fine, I, Murphy will guarantee that all this is fine, um, right, so that, that goes, pyro becomes, that becomes, so, x-power on pyro becomes x-power on one, oh, come on, give me a break, really?

**Dave Jones:** Okay, so, x-power on one, how did anyone make heads or tails of that? How did anyone make heads or tails designing this? Wow, really? x-power on one, okay, there goes the front panel audio process, so, no, we don't give a rats about that, there it is again, okay, so, yep, alright, yes, okay, the block diagram showed that better, so we just wasted all our time, should have believed the block diagram, so, yeah, ah, okay, where's that, is there any capacitor?

**Dave Jones:** No, that's it, alright, okay, well, that's, uh, no, that just takes us to the front, no, like a said, Murphy guaranteed that was a red herring, I don't know, well, is this 5650, is this findable? Can we do, can we do this? Because maybe, ah, it's on the bottom side, no, I see it right down in the corner down there, yeah, it's on the bottom side, yeah, no, that's, that's no good either, interesting to know what the bat sense switch is, like, I didn't know that it detected that the battery was, like, it had a, you

**Dave Jones:** know, switch that detected whether or not it's in, ah, so, bat sense switch becomes unreg mon, which then goes into, yeah, the audio processor, what's the audio processor, that's the second time we've seen the audio processor, is it? Oh, what's the deal with the audio processor?

**Dave Jones:** Just from a system design point of view, why would an audio processor, like, be involved, front panel, oh, no, front control, okay, no, so it's front control and an audio processor, they've combined it, there you go, that's why, okay, and, yes, and here it is, it takes bat unreg, reg unreg, bat sense switch, it's got everything, backup VDD, regulator ground, it's got, it's got the whole shebang, wow, okay, so, I see 8400, so, where's that, and it's on the bottom, of course, it's on the bottom, yep,

**Dave Jones:** it's on the bottom, see, what's things like, you know, this reset, here, right, and X-Wake, and stuff like that, like, that, that sounds kind of, sort of, important, doesn't it? Oh, that's the one on the top, there you go, it's that one right down there, there you go, so, maybe, if we start probing around that area, it's gotten to the point where, yeah, let's just, let's just start probing, because this is just, this

**Dave Jones:** is boring, trying to follow the money here, let's just change the auto range there, let's just fix it to 10 volts, so we just don't have to dick around, auto ranging, because auto ranging can be a bit, a bit of a, bit of a dick around, you can waste your time doing it, there you go, 4.26 volts, that sounds an awful lot like the battery voltage, doesn't it?

**Dave Jones:** Or battery, or 5 volts minus the diode, diode-y drop, right, so there's voltage on that board, there you go, alright, well, what I'm going to do, disconnect that, so there's now no external power, I still don't even know what point I was probing there, which pin, I didn't even bother to check, I just started randomly probing, but, of course, you expect voltage on the board when there's 5 volt USB coming in, 3.9,

**Dave Jones:** ta-da, we're in a chicken dinner, see, random probing around helps, so there's definitely voltage coming onto the board, 3.9, so I measured the voltage before, yeah, it was like 4.15 or something, 4.2, it was, you know, it's a fresh battery, it's a reasonably fully charged battery, so, yeah, so we're getting voltage onto the board, no problems whatsoever, okay, so the battery's all connected, everything's hunky-dory, but that transistory,

**Dave Jones:** Sony are so nice, they've even put, look, drain, gate, source on the overlay, this is designed for servicing, they've, you know, they went out of their way to do that, that is great, so you didn't have to look up the data sheet of the chip or know what it is or whatever, it's just, yeah, there was the drain, okay, there's the gate, that's just, that's absolutely fantastic, see, but the problem with this fault,

**Dave Jones:** is that it worked, like, like, we had the exact same fault as we've got now, it wouldn't power it on, we took it apart, we put it back together, and it worked again, it worked for like a day, you saw it, so this is not like, oh, yeah, okay, we're blowing a tranny in here or something, right, it's, it's not that, you know, something's, like, because it, that is the least likely scenario, that a part's blowing, so I wouldn't go suspecting parts,

**Dave Jones:** willy-nilly, like, there was something in the process of taking it apart and putting it back together that made it reset, and of course we speculated that in the previous video about the backup battery and stuff like that, causing that sort of problem, but I guess, like, can we measure the backup battery, I don't think so, because it's right down on one of those flexors in there, we'd have to take it all apart again, but there's definitely voltage getting to the board from that battery, so,

**Dave Jones:** yeah, and I, yeah, I find it hard, I think it's unlikely that a component is just blown, like that, because otherwise we wouldn't have been able to get it working by putting it back together, it worked fine, and we know why the screen scrolling thing happened, that was, you know, an open pin on the LCD connector when I put it back, or, you know, some dirt or some other grubby thing on there, making bad contact, it was floating, yeah, so the last thing I'd do is, would be sucking parts off,

**Dave Jones:** here, you just, no, no, no, no, no, no, something, there's something trickier, there's something trickier to this, and it's annoying, because it'd be relatively straightforward to troubleshoot this if you can access this, but the physical part about this is that, you know, just the way it's assembled and everything, and it's just, it just makes it really difficult, but we know it's getting onto the board, so, oh boy, so,

**Dave Jones:** so, Q4301, so, we do know that much, okay, so that's a switch, after your VDD out reset thing, so we know that's getting the voltage, right, we know that's getting the business, so, let's go and have a look, right, there's the source, the drain is down here, so X-Wake is the one that had the voltage on it, okay, and then, to drive

**Dave Jones:** that, it has to be driven by this reset switch here, so this symbol here shows that reg, unreg comes in, this is an in arrow, that way, right, so that comes into here, the source, this, this, this transistor must be turned on, because we're getting X-Wake here, we're getting the voltage, so reg, unreg, you'll find that the source and the drain would be the same voltage, I mean, we can probe that, all right, I'm going for

**Dave Jones:** a finer probe, this time, one of these fluke jobbies with the spring-loaded thing, so let's go in here, let's re-measure that, 3.93, no whackers, 4.13, it's not, there's some drop on that, and our gate, 3.76, right, so there you go, that makes sense, when we're measuring the gate, okay, so we're getting our reg, unreg in here, and

**Dave Jones:** then we're measuring the gate voltage here, right, but that's because our 10 megaohm input, we were reading under, because you get the voltage drop between the 1 megaohm gate source resistor here, and the gate, so, yeah, no, that needs to go to ground, to switch on that MOSFET, and the reason that we got the voltage over here, I don't know, but it was lower, which means that, you know,

**Dave Jones:** if the transistor was, well, it's obviously not switched on, but if it was switched on, X wake would be pretty darn close to X reg, whereas it was, yeah, what, 3.7 or whatever, so, that's, that's not it, but still, I don't even know if I'm chasing the right thing, I'm not sure if that's supposed to be on or not, or when that, when this reset thing happens, all I can do is try and probe this at the same time as trying to switch it on, so I need my three hands, problem is, the power button moves the whole damn thing,

**Dave Jones:** yeah, it changes just a little smidge when I push the button, it does something, but, yeah, it's not, obviously not switching that on, so that's, you know, yeah, it's got nothing to do with it, really, I don't know, I'm just probing stuff because I can, this is sad, right, so maybe I can measure the lithium battery in situ, so let's give this a go, BT900 lithium battery backup VDD,

**Dave Jones:** makes sense, let's try backup VDD, maybe, if backup V, if the battery's dead, and backup VDD is not there, it doesn't power up, maybe if the battery dies, it does not power up, and why it came good that day, I don't know, it charged itself, I don't, because it's not rechargeable, I don't think it's a rechargeable jobby, I think it's just a primary, backup VDD, here we go, backup VDD, ever VDD, I mean, how many,

**Dave Jones:** VDDs and other crap have we got in here, it's unbelievable, once again, it's this audio processor chippy, right, that's front, front control and audio, well, front control processor, right, backup VDD, it goes directly, what's, what's an ever VDD, it's, it's ever, it's always on, it's forever on, anyway, D5100, so one end of D5100, we can measure, what are the odds it's going to be on the top of the board,

**Dave Jones:** bottom of the board, it's bottom, of course, it's the bottom of the bloody board, I can't see it in there, but of course, it is, there it is, D5100, right there, where, where, where else does it go, this capacitator here, something, there's got to be a VR in there, which then pops to the top side, these aren't mirror image, are they, oh, it's program locked up, I think the program's locked up, using the edge browser,

**Dave Jones:** I don't normally use edge, it's just because it's like, for screen, I only do it for like screen captures and stuff, oh, jeez, come on, oh, the whole document's gone, trying to measure ever VDD, that's not going to help us, because if, only if the diode was in the other direction, so that's not going to help us at all, backup VDD needs to come across here, like, I, I don't want to have to take the thing apart, it's such a pain in the ass, don't have to take it apart and physically try and get access to the battery or the ribbon cable for that thing,

**Dave Jones:** so I'm trying to do it on the board, and I'm probably a glutton for punishment, it doesn't, that schematic's wrong, backup VDD, right, there, there, goes into the diode, but the, goes into the cathode of the diode, but the other one didn't show that, right, it shows that it also goes into the chip, but it doesn't, look, backup VDD also goes into

**Dave Jones:** the IC8400, and according to the actual schematic, oh, it does not, right, that means it goes in, no, no, no, no, that's, it, it should, this shows the IC, it doesn't show the sheet for the IC, it's not like it's going into the page, right, it shows it going into the processor, and it doesn't, according to the actual schematic, it goes nowhere, so that doesn't make sense, that does not make sense at all, why would a backup battery

**Dave Jones:** go into a reversed biased diode like that, that makes no sense, now, it makes sense that this ever VDD would then diode, or, no, no, even that doesn't make sense, because if that powers through there like that, then it, it's going to charge the battery, and I don't think it's a rechargeable jobby, there's no other info on it, there's no part number or anything like that, but it's got to be a primary, and

**Dave Jones:** it, it, that, yeah, that, that schematic makes no sense, aha, backup VDD also goes through R101, a 220 ohm jobby, right, that's interesting, right, so backup VDD, yeah, we've seen that, oh, okay, C84, there you go, C8414, okay, so C8414, okay, so C8414,

**Dave Jones:** okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414, okay, so C8414,

**Dave Jones:** oh, 3.1, okay, right, so nothing activates until we get the, what, huh, ah, maybe it's that switch, you remember that we said there was like some, um, battery switch or something, that maybe, yeah, if you don't insert the, but no, why would the backup battery die, I don't understand why the backup battery would be disconnected from, if you take out the main battery, that doesn't make sense, okay, so C8414,

**Dave Jones:** makes sense. Yeah, sure enough with the battery out, we get diddly squat. So I'll push the battery back in, and ta-da! That seems like a backup battery voltage to me, doesn't it? So it looks like that lithium backup battery is gonski, because when you take out the battery like this, there's nothing there

**Dave Jones:** on that resistor, which then feeds into that diode, and then it also goes off to that chip as well. So, and the 3 volts being pretty much what you'd expect from a lithium battery. That was actually coming from the diode there, from this battery

**Dave Jones:** here. So that's like it only dropped like .1 volts or something. You know, because there was no load on it, and it was like a silicon. It was a shocky jobby, and yeah. So, it's, there you go, the backup battery. So, where the hell is it hidden?

**Dave Jones:** It's in a ribbon down there somewhere. So based on the schematic, it does actually seem to be like a rechargeable battery. So, because it's got the diode, which then back feeds it in there, through that, what was it, 220 ohm resistor? Or something like that.

**Dave Jones:** So, it's gone. So, like, I can maybe understand why we took it apart, put it back together, and then it suddenly worked for a little while? Maybe? The battery was like accepting some charge, and now it's like got nothing on it? I don't know.

**Dave Jones:** We need to actually, problem is, we now have to take the boards out, and get back in there, and get access to the battery. And of course, I'm not gonna have like a replacement for it. So, I don't know, can we like temporarily, maybe we can like

**Dave Jones:** temporarily bodge something in, and see if it like powers up, if it has that battery source there? Um, I mean, it's very poor design. That it doesn't power up with that backup battery. It should power up, and just lose the contents. Um, that should be it.

**Dave Jones:** It should stop the camera working. That's really poor. But, yeah, at least we've got something to work with now. The battery's gone. That seems obvious, doesn't it? Yeah, so, it's all gonna have to come out again. I really should have, like, that's something I really should have spotted.

**Dave Jones:** On the first teardown. But as you, um, saw, like, I did not see, at all, um, the backup battery. Um, in the first, uh, first teardown at all. It just, I don't know, I couldn't, I don't even think I saw it on the, like, the, on

**Dave Jones:** when I watched it again. Um, yeah, so it's in there somewhere. So let's, let's get all this out again. Is that it there? That's our battery. There you go, I see something round. I see something round. And battery-like. There you go. That's gotta be it.

**Dave Jones:** Right? No wonder we didn't see it, because it's, like, kind of, like, yeah, it's, it's taped in there. Right? That is taped in there. So we should be able to access that. Actually. Can I get, like, a scalpel in there? And can I, that's just, like, that's just, like,

**Dave Jones:** taped in. There we go. Is that it? Yeah, I think that was... Yeah, that was, uh, just glued down or something. There. There it is. Got him. Got him. That's a, uh, that's a welded tab jobby, and it's soldered down in place. Hmm.

**Dave Jones:** Indonesia, huh? Anyway, we can actually get now directly on there and probe that sucker, and I think you'll find that... Sheesh. It's Gonski. Yep. There you go. So, I, like, come on. It's, it's gotta be it. It's sort of, it, that's the only really thing, like, that explains

**Dave Jones:** why it would, like, maybe, like, come good, like, once, um, you know, for, like, a period of hours, and then just die, uh, completely. The battery still had, you know, it was large enough to, you know, haven't taken its last gasps or something.

**Dave Jones:** So, anyway, let's desolder that sucker. And this is interesting. Look. It's bounced back. It's coming back. It's rejuvenating itself. What? We, we measure, we, we probe that, and we will get NAF all. So, I don't know. It's maybe, like, is there something else gone in there that's

**Dave Jones:** loading it down? Don't know what the deal is. I'm just gonna solder that back on. It's not close, but it's, it's good enough. I don't think it's shorted. There you go. We've still got some voltage on that. So, it's, yeah, it's recovering, 'cause I'll shorten that, I'll shorten the poor bastard out when I

**Dave Jones:** was, uh, putting it back in. But, let's, let's put the battery in there. Yeah, 2.47. I don't know why we'll get nothing. 4. So, that's gonna slowly charge that sucker. I'm actually going to try and switch this on. Just for kicks. I mean, it's got absolutely nothing plugged into it.

**Dave Jones:** No. No, it doesn't like that, does it? That's slowly creeping up there. I don't think that's charging from the battery. I think that's just electrochemistry recovering. Anyway, the point is, it, it does seem to be retaining a charge there. So, what's going on?

**Dave Jones:** So, if we follow the money here, RTC ground becomes REG ground, okay? So, backup VDD is the thing that we want to actually follow the money on. But, just remember REG ground. Here, yeah, we know about that. Here it is. Here. And, it goes over to the battery, and it shows the battery.

**Dave Jones:** Actually, going to, that's like chassis. That's like, you know, chassis ground kind of thing. So, BT900, if we zoom in on that, there's our lithium battery. Oh, it doesn't actually tell you, right? It, it must be connected through, like, the chassis ground must be the battery

**Dave Jones:** ground, right? Because there, there's only one, like, there's not, no extra wire on there, is there? So, BT214, and yet, sure enough, the negative of the battery is connected through to the battery, the lithium battery that powers the camera. That's it. Straight on to the thing.

**Dave Jones:** That's the terminal. Straight there, and that just goes through to pin 1 like that, and we know that that is a rechargeable jobby through that 220 ohm resistor. There's silly buggers at play there. 2.56788. Yep. And, uh, that is recovering due to the chemistry, and if we plug that

**Dave Jones:** in, it's not actually charging up any quicker. So, our battery is not charging when you plug in that, and it's supposed to, and it's not supposed to do it when it's switched on. It's supposed to do it when it's switched off. Right? So, I reckon,

**Dave Jones:** if we follow the money back on that, I don't know, we might find something. Um, is, is that it? It's, it's not the battery at fault. Uh, it looks like it may be the charging for the battery. But it's basically through that, uh, diody, isn't it?

**Dave Jones:** There it is there. Back up VDD. That's that pin 1. So that's coming from the flex. So the flex goes into that 220 ohm resistor there. Uh, can we measure that, um, 220 ohm? Can't see how the 220 ohm's gone, Ski, but you never know.

**Dave Jones:** You're lucky in the big city. Let's get back in there with two smaller probes. I'm gonna stick with my, yeah, there we go. Yeah. No worries. So, that's no problem. There you go. So the diode's okay. The resistor's okay. That, that resistor's not playing, uh, silly

**Dave Jones:** buggers, is it? So that would be charging up the battery, and the battery's over there at 3.03. So, okay, 3.03. And if I, uh, disconnect the battery and measure it fairly straight away, we've got nothing. Why do we suddenly get nothing on our battery?

**Dave Jones:** Why? What the heck's going on there? Am I not making contact? Pretty sure I'm making contact. There's nothing on that battery. Uh, am I, am I remembering that incorrectly? There's something 2.59 volts. What, uh, what's going on? What? Why, why can't I? It's making absolute

**Dave Jones:** fool out of me. And we know it's connected through to, right? It's connected across one of the ground pins and then to the 220 ohm resistor there. One side of it. It doesn't matter which side of it you measure. We know it's okay.

**Dave Jones:** Is this just not in? It's in as far as it goes. It doesn't go in any further than that. I have access to the pins. It's, there you go. It's measuring 2.6. There's 2.6 volts there. There's nothing. This is the, um, temp, um,

**Dave Jones:** thing, right? That's, that's the temp pin. We knew it was pin 1. Was the, was the one ground next, was the ground next to it? It's not this one over here. There's no voltage! There you go! That's gotta be it, right? That's gotta be it.

**Dave Jones:** Is it something to do, is the ribbon busted? Let's go to, let's go to the continuity. Nothing. Positive of the battery. Nothing. What's going on? They're both busted? What? Negative. Goes to this pad here, right? Yeah, which is the one next to it?

**Dave Jones:** Is, which is the one next to pin 1? There, so pin 2, 3, and 4. And then the positive of the battery is supposed to go through, through the flex. Down to here! Neither of them have continuity. What the? Let's get, let's get physical.

**Dave Jones:** Physical. I wanna get physical. Okay, that's the positive. That's the negative. There's no negative. What the? How can the negative not be there? Like, that's a massive trace. That cannot be broken. Oh, well, actually no, it's only small going from the battery. There's the traces.

**Dave Jones:** Running down in there. Is it? Oh, oh, hang on. Hey! Hello? Oh, yeah, look! Yeah! Ah, the whole thing's broken! The whole thing's broken! Yep! Yep, okay, it's still sticking there! You can see it! Oh, wow! Okay! No wonder, look! Yeah! Yeah, look!

**Dave Jones:** It's entirely cracked! Wow! Now, I wonder if that happened during, during my brutal teardown, but, like, assuming that this is actually the fault, right? Assuming that this is the problem stopping it booting up, then, um, yeah! Then, um, it must have happened before I tore it down, right?

**Dave Jones:** Maybe because this was bent over on a very hard radius, like a 90 degree radius. Maybe it just cracked due to, like, um, material fatigue or something. Because it doesn't, this part, like, it's not like it flexes. Well, I guess my, there's a bit of, when you put the battery in,

**Dave Jones:** like, there's some, there's some, like, pressure, pressure on that whole assembly, like, there is, yeah, yeah, actually, there is pressure on that whole assembly. Every time you push the battery in, right? So that, that, that whole assembly moves. Okay, so, yeah, okay! There's some strain on that

**Dave Jones:** flat flex. Maybe it's just, it's just broken. But there it is! Yeah! I was wondering how, you know, like, there it is, you can see it cracked. Ah, you little bastard! Okay. Come on, it's gotta be it, right? Surely Murphy's had enough with me, that

**Dave Jones:** that's gotta be, he's tortured me enough! Bloody Murphy. Right? And there has to be, that, that, that's gotta be it. That's gotta be stopping that powering up. Is, that, that's not a copper return? No, no, because we've already measured that power gets to the board.

**Dave Jones:** Okay, so it's only, it's only the, we can go back to our video tape. Look at 'em all. I love just looking at flex, ah, boards. They're just absolutely fantastic. Anyway, here it is, right? Yeah, yeah, so it obviously, like, the battery, yeah, the ground doesn't go up there.

**Dave Jones:** The ground doesn't go up there. But that part, that part right there, right across there, both tracks, that's the point it failed. Probably 'cause the, yeah, there's probably more stress on the, like, the outer part, I don't know, mechanical engineers tell us? Like, when a, when a

**Dave Jones:** cable, when that cable flexes over, like that, when it folds, when that battery folds over and upside down into there, there's a 90 degree bend on that. And then if you got the whole assembly going wiggle, wiggle, wiggle, yeah, in there, each time you take out the batteries, there's more stress on the

**Dave Jones:** outer part, or the inner part. But anyway, the outer part is broken. It's just sheared, like, half of it. It's just sheared across both tracks. Gonski. So therefore, the only took me, like, an hour and a half to find this. Right? I, with, with careful

**Dave Jones:** view, or a careful inspection, or just lucky inspection, I could have found this. The first time I took it apart, I could have found it in ten minutes, and, you know, boom. Right, oh, problem, let's fix that. Does that fix the problem? I'm assuming this is

**Dave Jones:** gonna fix the problem. I'm assuming it's not booting up 'cause there's no battery there. Right? So, yeah, it's just coming together completely. That's interesting, huh? You bastard, look at it. Look, look at it. Here we go, here's some fail porn. There you go, demonetized, you can see

**Dave Jones:** both the traces under there, coming out. Geez, wow, look at that. So, um, how do I fix a flat flex like this? Uh, well, unfortunately, so the traces are on this side, so that makes it a bit harder to access in situ. Here you go, yeah, it's just a very,

**Dave Jones:** I couldn't think of a more inconvenient spot for there to be a fail to try and repair that. That is, and it's right on the bend, too. So any, and it's on the underside of the bend. I can't, Matthew, again, I couldn't believe, like,

**Dave Jones:** there's, like, it couldn't possibly be in a worse location for that to happen. That's just terrible, Muriel. As a bodge, if you were really desperate, you could run wires direct from there up to the bottom of the main board, but once again, you've come a gutter, because you've got to go to the bottom,

**Dave Jones:** you've got to solder onto the bottom of the main board, right in here. Bet you could, right? You could, like, if you could, if you thought that you could tuck the, uh, wires away and stuff like that, but even if you use really fine mod wire, this fit-to-envelope

**Dave Jones:** design is really tight, um, so I don't, yeah, you're, you're probably not gonna, uh, do that easily. Oh, oh, yeah, yeah, yeah, yeah, got it, got it, got it, got it, that's right, it was taped down, that's right, I remember. Need to watch my own video, it was taped down.

**Dave Jones:** Alright, so, no wuckers, um, we can get in there, and we can, uh, we can of course now zoom-y, zoom-y, right in there, I can see that break, that's terrible Muriel, ta-da! What a mongrel, huh? What an absolute mongrel. Both traces broken, wow.

**Dave Jones:** Right, how do I actually get that off? It's got, like, a copper thing on the back, it's got a whole copper clip going over, maybe I get that tape off, that black tape, that black stuff looks like tape holding it in, oh no,

**Dave Jones:** there's a screw, there's one screw, alright, I'll take that out, I'll, uh, I love how they use practically all the same, almost all the same screws in this thing. That didn't do anything. Complex little assembly in its own right, I mean, that's just,

**Dave Jones:** that's, you know, just that whole battery system is just crazy complex. The door, and the hinges, and the flat flex, and the way, you know, the battery holder, and then this thing on the side, which, I don't know what the heck's that's doing, um, that big metal, like, it's almost like that's

**Dave Jones:** a little die-cast metal bit, and I, what's all this, copper on the back? It's a hugely complex thing, I can't believe that they didn't have a team that went through and just optimized, you know, optimized assembly and stuff. No wonder this is an expensive camera,

**Dave Jones:** imagine trying to assemble this and all the different parts required, wow. Starting to think all this stuff in here is, is bonded, like, I took the tape off the back, nothing's coming off, everything seems like, I don't know, at least adhesive bonded in there,

**Dave Jones:** it seems really annoying, I'm, like, you know, I can get into these, but there's not enough purchase down there to sort of, maybe I could try and do a Firewire link over, but, oh man, it's gonna be ugly, can chop out some of the plastic there,

**Dave Jones:** maybe, don't need the plastic, chop it out, no worries, and they're so close together, the pitch is just incredibly small there, in fact, I can tell you what the pitch is, it's hard getting both of those in there, but there you go, that's .1 millimeters,

**Dave Jones:** uh, sorry, .01 millimeters, ha, that's, that's one millimeter, so, there's ten divisions in there, so that, like, yeah, the pin pitch is naff all, ha, ha, trace pitch, sorry, is naff all, so, yeah, that's not, that's not fun. I almost think it's going to be easier to simply put

**Dave Jones:** some tiny mod wires, I know it's a horrible bodge, but I think it's actually gonna be easier to put, like, some mod wires just from here, and just solder it onto the, solder onto the main flex here. See, the problem is, like, just scraping off the, uh, polyamide

**Dave Jones:** coating on the traces there is gonna be difficult, it's not something you can easily do, like, technically I can get an iron down in there, but they're so bloody close together, like, just even scraping that flat flex, you're not gonna be able to do anything, so, it's really

**Dave Jones:** intolerant, robust stuff, except when it, when it breaks like that, uh, when it turns brittle and just breaks. Yeah, I don't, I don't like my chances of even, like, putting, like, links back on there, it's just, doesn't really seem doable. Put mod wires over there, over to this ribbon, and once again,

**Dave Jones:** I've got, I've got the same problem as scraping away the ribbon, but at least I have more chance here. Get, you know, even if I've got room to get down, I probably do, in theory, I've got room to get down there and scrape off

**Dave Jones:** the, uh, polyamide coating on top of the traces there, but even if I did that, I'd have to put little tiny links in there, how are they gonna stand up to the flexing? I don't know, but anyway, trying to scrape off, you really

**Dave Jones:** have to, like, do a physical abrasion type thing, with the, um, with the scalpel or whatnot, but I've got no physical backing to do that on, really. Like, it, uh, it's awful, at least, at least this big one over here, right, I can at least put something hard under there, and

**Dave Jones:** uh, then get on there with the scalpel, and try and scrape it off, so I'm gonna give that a go. So I'll get that on a surface there, it's just awful job trying to do this, imagine if you had to repair a multi-fine pitch thing.

**Dave Jones:** It's just, ah, it's really awful stuff. For those who think you can do it with a soldering iron, you've got very little luck as well. See if the Swiss Army knife is, am I through to the copper? Oh yeah, yeah, I'm through, it looked like

**Dave Jones:** it went all the way through, I think I'm through, I think I scraped away, depends on the type of knife you have, my Swiss Army knife just seems to be better at that. That's the, that's the gold surface, right? Yeah, yeah, yeah it is, you have to get in a certain

**Dave Jones:** light. Okay, see if I can do the same thing. Okay, yep, I've exposed some of that, so I've exposed both of that, now I can maybe get a fine pitch iron in there. First thing you're gonna wanna do, put some fluxy on it.

**Dave Jones:** Okay, I'm gonna tape this in place. There we go, we've got some take on to that. Nice, okay. Flux bent, even though there is flux in mine, believe it or not, there's five cores in this, ah, nought point, what is it? Nought point three eight.

**Dave Jones:** Nought point three eight millimeter solder, there's apparently five cores of flux in it, I think. Yeah, five cores of flux. How the hell do they get in there? Ah, the oompa loompas, the flux at this solder factory. I don't know, magic. There we go, beautiful.

**Dave Jones:** Ah, thing of beauty. Joy forever, look at that. Bobby Dessler. Alright, mod wire. Beautiful little mod. Look at that. Now, whether or not, whether or not these wires are gonna fit, we can cover that with insulation if there's anything conductive on top, gotta watch for the metal case and everything like that.

**Dave Jones:** You gotta be careful you don't come and guts her there. But we can cover that with some insulation, so, um, what I wanna do, so now, I can just, I can solder that directly over now, but now it's a matter of, ah, like, form-fitting the wires.

**Dave Jones:** Like, actually, probably can't do that until it's all reassembled, and I kinda sorta know how much, like, play I've got, and stuff like that. Um, so, it's not, yeah, yeah, like, how to form the wires. So you're better off, like, cutting, figuring out how they, how the wires form, first,

**Dave Jones:** in there, and then cutting and stripping them, and soldering onto the battery, I think. So, yeah, anyway, so this one here, I know we've got the same color, probably should've used different colors, doesn't matter. So yeah, but this one's, obviously, of course, that's our

**Dave Jones:** battery positive, so that goes to the case over here, which is our left-hand, ah, pin over there. So, yeah, I mean, I could fold it back in, but then, where does the SD cardboard go in relation to this? I can't remember. It screws on there, and, ugh, I don't know.

**Dave Jones:** I'm tempted, right, I think I'll put this back in the camera now, and I will attempt, sort of, partial reassembly, just to see where I'm at, um, with, like, in, in regard to how I can form these leads. Right, so that goes in there.

**Dave Jones:** SD cardboard is the biggie. I probably should've had the wires coming out the other direction, rather than out the bottom, ah, the top, like that. So, it looks like, right, we can probably form the wires down through here, and around, and over under,

**Dave Jones:** like that, over under, kind of thing, and off to the side of the board, because the board's going to be in there like that, and then we should have enough gap to pop them out there, I think. So, something like that, ugh. But, you know, here's where, if you cut it wrong,

**Dave Jones:** like, you've just, you know, you kind of have to, like, start again, from scratch, so that's really rather annoying. And, yeah, I shouldn't have put those on the bo- coming out the bottom like that, maybe. And, ah, this is the smallest mob wire I can got.

**Dave Jones:** Oh, like, I can go smaller. If you want smaller mod wire, you can, um, you know, get a multi-stranded cable, and you can strip it, and get little individual strands out of there, and that's a good way to, ah, get yourself some mod wire.

**Dave Jones:** Um, but, of course, it's not insulated. It doesn't have the, ah, but, yeah, this is the smallest, um, insulated mob wire I've got. For those playing along at home, it's 30 AWG, OK Industry wire. That's just, like, my standard mod wire. I think I'm gonna have to just hold my tongue at the right angle and guess that.

**Dave Jones:** Now, of course, when you strip these, you want to hold on to them. Geez, I hope all this works. I hope all this effort's not for zip. That would suck, wouldn't it? OK, we've tinned those. OK, let's go for broke. So, we've done our little mod.

**Dave Jones:** Now we've got to flip our battery back down into its little holder. Yeah, ah, I think I cut them too short. Damn it. Maybe. Maybe. Has that actually gone down flat? I don't know. A ribbon I've had a problem with in the past.

**Dave Jones:** And I've broken one of them. Yeah, yeah, I've broken one of them. Yeah. OK. Yeah, so I soldered that down too far. Um, yeah, I didn't account for the coming over the top. Yeah, I had to simply do, I'm gonna have to desolder that.

**Dave Jones:** Nah, I'm gonna have to do it again. So that fitted back down. I've got that fitted back down. And I've got the wires coming out. I'll screw that board back in, I think. There we go. So that board's back in. I've got two wires coming out.

**Dave Jones:** That are probably not gonna be long enough now. Tell you what, I'm gonna worry about all that later. I'm just gonna, ah, no, 'cause this goes on the underside of the board, doesn't it? Goes on the underside of the board. Goes on the underside of the flippy.

**Dave Jones:** Like this. So it connects in like that. So, yeah, ah, man. This is, this is nutso. Yeah, yeah, I needed finer mod wire, and I should have made it longer. That, yeah, that was dumb. I shouldn't have, I should have soldered them onto the battery, fitted the battery first,

**Dave Jones:** had the wires coming out, and then once they were out, then I should have put everything back together, and then cut to size, and then figure out where to do the scrape. Um, but then you've gotta have a hard surface to scrape it against.

**Dave Jones:** So, you know, like, but here I've conveniently got the board. Um, yeah, I should have done that. That was dumb. Now, regretting that. Alright, that was obvious, with hindsight. 2.46, okay, so that bottom one is negative. So I'll just mark that, so I don't goof that up.

**Dave Jones:** Maybe it's just long enough. Maybe. Now, the problem is, when I fold this like this, it comes back like, no, no, they're definitely not long enough. Um, right, when it folds over like that. I mean, you know, look, there's no reason why I couldn't, like,

**Dave Jones:** solder, like, the ground down to, like, here, or something. Like that. Like, there's no reason why you can't take, like, a shortcut like that. Uh, for example. Um, because it's only battery. It doesn't matter. But to test that, I've gotta put the, uh, ribbon cables

**Dave Jones:** back in and test the continuity. Uh, I think I've taken some trace off there too. Alright, so what I'm gonna do, yeah, I'm just gonna have to scrape some more off. There's my teeniest, tiniest heat shrink. We'll give that a go. Couldn't be bothered using the hot air gun.

**Dave Jones:** Soldering iron's good enough for Australia. Adds a bit more bulk, but nah, she'll be right. Stuff those wires somewhere. Okay, so I've got those wires attached. Um, I reckon that can stay. Oh, yeah, that one's a bit how you do it. Anyway, we'll see.

**Dave Jones:** We'll see. Let me see if I can get this back together. And, uh, yeah. See what we can do. Alright, so this has to go under here first, I think. So that's our battery. That's a real pain in the ass connector, let me tell ya.

**Dave Jones:** Now the battery connector. This is ridiculous. Be careful, this is the one I soldered to. So it's getting flexed to buggery. Then you got the top panel connector. And this is just, really is crazy stuff. You'd get used to this, I guess, if you were doing it every day.

**Dave Jones:** That's not all the way in, is it? So as you can see, I've soldered a 220 ohm resistor onto there like that. Onto that diode. And I'm hoping that does the business. Um, that's the plan. Anyway, so, fingers crossed. Uh, I've gotta anchor down that wire

**Dave Jones:** because as I, uh, like, move, you know, flex and move this board back into position and stuff like that, it's just gonna completely come gutter. So I really need to, um, stick that, stick that down. So, probably some super glue or something. Something needs, it needs to stick on there somehow.

**Dave Jones:** Okay. It's back together. I think let's put a battery in. And let's see what happens. Okay. Press the power button. Nothing. Hold it down. Nothing. Although it might need time to recharge. A rechargeable battery. Assuming it's all still connected. Let me plug in the

**Dave Jones:** USB. Wah, wah, wah, wah. Doesn't work. After all that work. Zippity-doo-dah. Did I forget something? Don't think so. I just cannot cop a break, can I? So, unfortunately, it's, like I said, it's difficult to, um, like, measure things in here after you've reassembled.

**Dave Jones:** You've just gotta reassemble it and hope that you've done the right stuff and it's worked. But, in this case, nope. We've come a gutter and nothing happens again. I don't even get the orange, uh, lead anymore. Right? From, from the USB. So, I don't know, I don't know what's going on.

**Dave Jones:** I'll, I'll measure that USB current, actually. There you go. It's actually drawing 1.4 milliamps. So, if I press the button, does it do anything? If I hold the button down, does it do anything? Nope. Does absolutely nothing. So, that's, that could be trickle-charging

**Dave Jones:** the battery, could it? Or that's just other standby stuff happening in there, really? Is, is that an, yep, yep, that's, that's genuine. Oh, there we go. So, when I plug it in, it draws 150. I presume that's, like, charging the battery. It realizes, oh, no, the battery's

**Dave Jones:** pretty full and it switches off. That's another hour, at least, down the drain. Uh, well, not down the drain, because we did find a fault on this thing, and I did my best to repair it. Um, and I put it back together and it's just,

**Dave Jones:** it's doing nothing now. So, almost back to square one of trying to get all this stuff out while leaving it connected and then measuring voltages. And I've, that's it. I'm, I'm done for the day. Um, my time has run out. I gotta go home.

**Dave Jones:** So, that's it. Give me a big pity thumbs up. Whilst I connected this over to here, there is, I can't see a trace going off from there to the IC, which is the direct backup, because it doesn't go through the reverse bias diode, right?

**Dave Jones:** So, I'm thinking that there is a via down in pin one there. So, pin one is isolated. So, I've gotta short out that 220 ohm there. So, that might kick it back into action. That's what I'm thinking, anyway. Okay, what I'm gonna do now is I'm gonna

**Dave Jones:** look across, well, measure the voltage across C8414, because this is supposed to be the capacitor that is across VDD backup, like actually on that backup VDD pin, D3 there. So, if you're not getting voltage on there, that's what I suspect is not causing

**Dave Jones:** it to boot up. So, if we can measure the voltage across C8414, then we can verify whether or not voltage is getting there. I have actually measured voltage on the board. I am actually getting my 2.9 volts or whatever. It is on the board.

**Dave Jones:** So, that part of it's working. So, I need to peel back some of this thermal pad to reveal the capacitor down in here somewhere. Once again, the problem here is that I can't probe on the underside of here without plugging in the actual connector, because that's where

**Dave Jones:** the battery voltage comes from. I just don't have the flat-flex length. Here's the flat-flex. We've got to connect it over to here. So, that's really annoying, because the capacitor I want to measure is that one down in that tiny little bugger down in there.

**Dave Jones:** And that is the input pin to the micro down here that detects the backup battery voltage. So, and I can't measure it in situ unless the board's flipped over. And I have actually measured that I am getting the voltage on here at the end of the resistor.

**Dave Jones:** But whether or not it's coming over to that pin. So, all I can do really is I can try and measure, actually, I'll measure the continuity there. Okay, the only thing I can really do now is join, short out those two pads in there,

**Dave Jones:** join this back. That's pretty much all I can do. So, I'll give that a burl. It's really hard to, it's so hard to get in there with the iron. It's just, it's crazy hard. And then, trying to support the board as well. You can see the

**Dave Jones:** board support I'm using. I've got a PCB-ite. None of that PC-bite. Put a hyphen in the right place. And, yeah, and then this is, then the camera's propped up on the multimeter here. And, it's just, yeah, it's nuts. It's nuts. Anyway, yeah, this is what you have to do.

**Dave Jones:** Because I don't want to have to keep taking the board out every single time. I want to do work on it. It's just, yeah, it's crazy. And then, when it's in, you just can't probe anything. It's nuts. Did I get it? I think I got it.

**Dave Jones:** I think I got it. I think I bridged that. That's a bit of how you're doing, but I think I might have got it. I don't know. I'll just try it. Let's see if I can buzz that. Shall we? Yes. Got it. Haha.

**Dave Jones:** Alright. I'll flip it back, plug it all back together, and see if I, see if it does anything. The super glue, by the way, on my wire in there worked really nicely to glue that in place. And, so, that's all solid. So, I can flip the board in and out.

**Dave Jones:** And, the other wire down in here is holding on really well because it's connected through to that big, fat, meaty ground trace running through there. So, yeah, no worries. So, I can sort of, like, handle the board now. So, it's really, it's really quite okay

**Dave Jones:** now. So, let me put it all back together. I'll get back to you. Alright. It's in. Let's see if I can do anything with it. Again, wah, wah, wah, wah. Nope. It's plugging in our cable. Oh. I don't have everything plugged back in at the moment.

**Dave Jones:** I don't have the, um, SD card. So, that could be a thing. Hey! That's actually holding more charge than it did before. For longer. It actually dissipated to zero. That is progress. That is progress. Because when I plugged in the USB before, it was, um, it initially

**Dave Jones:** surged to, like, 150, 180 milliamps or something. And then within seconds, it, it sort of dropped down. Like, five seconds, it dropped down to, like, one milliamp. Standby. So, obviously, it's charging the battery at the moment. So, that's interesting. So, like, I don't have the LCD plugged in.

**Dave Jones:** I don't have the SD card plugged in. Okay. So, I'm pleased with that. Let me put the SD card ribbon cables back in and the LCD in. And try it again. I think it's reassembled. Just the battery. Nah. Battery plus. USB. 160 milliamps.

**Dave Jones:** 180. Nah. It's dropped down to one again. Nah. I'm back to where I started. That was progress for a minute. Nah. Can't cop a break. ♪ ♪ ♪ ♪
