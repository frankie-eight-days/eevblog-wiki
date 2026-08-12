---
video_id: pG9m4fN71rQ
title: EEVblog 1713 - CRAZY Density Magnetic Core Memory from Space Shuttle!
url: https://www.youtube.com/watch?v=pG9m4fN71rQ
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 28, "3": 50, "4": 65, "5": 95, "6": 109, "7": 125, "8": 136, "9": 145, "10": 160, "11": 179, "12": 191, "13": 201, "14": 211, "15": 219, "16": 229, "17": 250, "18": 260, "19": 267, "20": 280, "21": 291, "22": 302, "23": 312, "24": 322, "25": 335, "26": 346, "27": 358, "28": 371, "29": 382, "30": 391, "31": 410, "32": 432, "33": 441, "34": 448, "35": 463, "36": 475, "37": 485, "38": 496, "39": 509, "40": 525, "41": 539, "42": 551, "43": 566, "44": 580, "45": 599, "46": 612, "47": 623, "48": 637, "49": 652, "50": 669, "51": 690, "52": 700, "53": 715, "54": 728, "55": 741, "56": 756, "57": 770, "58": 781, "59": 798, "60": 805, "61": 822, "62": 838, "63": 850, "64": 863, "65": 874, "66": 884, "67": 900, "68": 919, "69": 930, "70": 944, "71": 954, "72": 965, "73": 977, "74": 989, "75": 999}
---

**Dave Jones:** Hi, long time viewers will recognize this board. This is a magnetic core memory from about 1970 and I did a video on this 8 years ago looking at this.

**Dave Jones:** It was originally a mail bag one, but then I spun the video out onto my second channel and it was very popular. And magnetic core memory was the standard type of memory from probably the mid-50s through to like the mid-70s sort of late 70s still being used.

**Dave Jones:** Even still being used into the 80s, but they weren't manufacturing it back then. And this board stores a whopping 400 words of 64-bit. So, there's actually 100 by 64 tiny little ferrite rings in there and each ferrite ring stores one bit of information and it's double-sided.

**Dave Jones:** Look at that. Fantastic. So, this is how memory modules were up until like the mid-70s they used magnetic core memory. Let me show you this up close. So, I have to get the macro lens out.

**Dave Jones:** So, in addition to some very poor solder joints there, that's terrible Miro. Here are the individual ferrite rings and hopefully you can see those and you can see that there's actually three wires running through each little ferrite toroidal ring there and one is the X wire, one is the Y wire so on a regular XY grid and the third wire is the sense wire and that's how

**Dave Jones:** you can read data back out of these. And I'll shift my focus up there to the top of the screen and back down to the bottom. Sorry, it's really hard to get these things in focus all the time and it's better if I show you how this works by going to the videotape.

**Dave Jones:** Let's go. So, to show you how this actually works, I found this really cool the National Megalab. They've got a really cool like simulator animation kind of thing. The National Megalab is funded by the National Science Foundation, the state of Florida.

**Dave Jones:** Thank you very much, Floridians, for this. Excellent. So, this tutorial illustrates how magnetic core memory works. It set up took a little bit like chocolate donuts strung in a chain-link fence.

**Dave Jones:** The donut shapes are ferrite cores. Ferrite is a ceramic made primarily of iron oxide that needs to be magnetized magnetized or demagnetized. I'm not sure if they ever used any secret sauce in them.

**Dave Jones:** I don't think they had to, really. It was, you know, just basic iron oxide type stuff. And of course, you can just permanently magnetize iron and then you can demagnetize it as well, just like you can magnetize your screwdriver and demagnetize it.

**Dave Jones:** Okay, so what we're going to do is we're going to set a value of one in this bottom left corner down here. It's currently set to a zero. So, we have to put So, we have to select this particular row here, obviously, X row and this particular Y column here, of course.

**Dave Jones:** And then, we put a pulse of current through that. So, if we set that value to one like this, then if we hit that, you'll see that it's putting and it's flipped it in the direction like that.

**Dave Jones:** It's starting to go in like your magnetic rule of thumb, you remember that? So, it was going in one direction and then it flipped it in the other. So, the original value was zero and changed it to a one.

**Dave Jones:** So, let's actually So, we've stored a one in the magnetic field in that ferrite ring. So, let's say we want to set the value back to one because we just read it out, which can be destructive.

**Dave Jones:** So, we want to read it back in. So, we'll set it to one again, and let's click on that. Again, you'll notice that it went in that direction and it didn't flip directions there.

**Dave Jones:** So, it original value was one and it remains at one. And we can set that back to zero. You'll see it goes in that direction and then it flips in that direction.

**Dave Jones:** Cool, huh? So, yeah, it's you're effectively changing the magnetic field inside each individual ferrite ring, and because it's localized in the toroid, um you can have that really um high packing density that we're seeing here, and they're not going to uh the field's not going to really bleed into the other ring because it's not going through the hole like that.

**Dave Jones:** That's what she said. Okay, so what we're going to do now is we're going to read a value. Uh we'll do the bottom uh left one again here, but we've got a waveform of the sense line here.

**Dave Jones:** So, it's got 0 V in the middle, and if and if we're getting a positive voltage on the sense line, it'll go up. If we're getting a negative voltage, it'll go down.

**Dave Jones:** So, let's read back. Let's see what waveform we get when we read back a value of one, shall we? And remember when I said this is destructive memory, so we're going to actually kill that bit, and we have to write it back.

**Dave Jones:** But, if we've got a one in there, let's read it. Boom, it goes up, whoop, like that, and then a Well, you saw that it actually uh rewrote that bit back after reading.

**Dave Jones:** So, basically, we're writing in a zero and reading the sense line at the same time. The value was one, but it's now a zero, and then you'll have to restore.

**Dave Jones:** So, you've read the value, you can process that, do whatever you want, um and then but then you have to restore that value of one back. So, let's now read a value that has a zero in it, like this, okay?

**Dave Jones:** And you'll notice how it had the big hump before. It is no more big hump anymore because it was set to zero, and the sense line read back the zero.

**Dave Jones:** Um so, basically, nothing uh changed. So, value was zero, and it remained zero. So, only if there was a one in there have you destroyed that value, and then you have to write it back.

**Dave Jones:** For the zeros, you actually get a freebie. So, yeah, that can save some processing, some memory access time. So, it is essentially random access time memory. I did It just occurred to me.

**Dave Jones:** So, it's rat. It's rat memory. Random access time. Cuz you don't know whether it's a zero or one. And if it's a one, then you have to actually spend the time writing that back.

**Dave Jones:** So, you've got to have that extra process there, but you don't have to do that for a zero. So, let's read that value again, but let's read it from this one here, which has a one, this ring here, which has a one, and boom, you get that.

**Dave Jones:** And then, you've got to write it back. So, If you want to know how fast these memories were, well, it varies a lot, but basically, you know, like a megahertz would be like a really quick jobby.

**Dave Jones:** I don't know. Leave it in the comments if you know of like quicker core magnetic core memories like this. But yeah, I think, you know, upper limit like a meg or two, maybe.

**Dave Jones:** You can see that all those wires are like just individually hand wired, hand soldered through, and then they've got like big long sections like this that then just like the X wires just go right through to the other section there.

**Dave Jones:** I'm It's rather remarkable. So, this has a total of 3.2 kilobytes of memory or 25,600 bits spread over these four separate areas on both sides there. Pretty impressive. And I can just with my Mark 1 eyeball make out each little individual ferrite ring, ferrite toroid in there.

**Dave Jones:** But I was in the bunker the other day, and look what I found. I don't think I've done a video on this, and I don't remember where I got this from.

**Dave Jones:** Obviously, someone sent it to me. So, thank you very much. Maybe it's in a mail bag somewhere. If you can find it, let me know, and I'll link it in down below.

**Dave Jones:** But this is an Ampex jobby jobby from Ampex Memory Products Division. Ampex, of course, you know, make famously make like invented tape-to-tape recorders and you know, stuff like that.

**Dave Jones:** But they were into computers and memory and stuff like that as well. This is their memory products division. But watch this. If I take off the SHIELD OFF IT, WOW!

**Dave Jones:** LOOK at the density of this thing. I'm not sure if you're seeing that on your 4K tellies, but yeah, I can sort of, you know, as I said, mark one eyeball, just make out each little ferrite ring there.

**Dave Jones:** There's no way I can do it on this one. This bad boy is uh the on on the label, it's a 16K. I don't know if that's 16K bytes or 16K words, I don't know.

**Dave Jones:** Um so I haven't actually tried to count up the individual um ferrite rings in here. But wow, uh we're going to need some serious magnification to look at this board.

**Dave Jones:** This is just incredible. And it is a single-sided one. It's just got shielding on the bottom. And there's the driver chips. 1976 uh date code. So yeah, that's uh you know, mid-70s sort of uh back when they didn't get much more dense than this at the time.

**Dave Jones:** And you can see, look at all the individual bundles of wires. Somebody had to or some machine, I don't know, somebody had to wire these things. Look at the density of all this.

**Dave Jones:** Oh, it's just insane. So there you go. It's an Ampex model 1600, but I couldn't readily find any uh info on this. Um but the 5 volts and uh plus 15 volts.

**Dave Jones:** And it's got non-flight. So was this used in some sort of uh like flight hardware either space hardware or military hardware. If anyone recognizes this uh tag, please leave it in the comments down below.

**Dave Jones:** You can say say it's a 16K memory PCB. And of course, one of the good things about uh ferrite core memory is that they're not susceptible to uh you know, any sort of, you know, cosmic radiation, nuclear blast, and things like that.

**Dave Jones:** These things are going to be super duper reliable, and this probably still has, all these decades later, still has whatever was programmed into these things. Cuz they the magnetic field in those ferrites wouldn't really dissipate very quickly.

**Dave Jones:** I don't know if you know how quickly these things dissipate, but I do believe it's still be in there. But unfortunately, these are destructive memories. So, to read them out, you actually have to destroy the information, unfortunately, and then you've got to write it back.

**Dave Jones:** So, if you don't have a mechanism to write it back reliably, reading it out is a one-shot deal. And you can just see them like wired in there, and a big huge big board-to-board interconnects here.

**Dave Jones:** I don't know what it goes off to, but but these are obviously your Y drivers. Probably, you know, you probably won't find any data on those. And then those ones up the side here, these would be your X drivers, like that.

**Dave Jones:** And so, all that circuitry up the top, that's probably the sense wires up there. So, that'd be your sensing. So, so you've got X and Y drivers here, and that'd be all the sensing up there that does the readout.

**Dave Jones:** Okay, I've got my macro lens, and I won't adjust anything. Here is the old board, the 400-word one, and I'm going to put in the 16K word board, and see that is the density difference.

**Dave Jones:** I didn't adjust anything. That is in So, like I can't even see the individual individual ferrite rings on the camcorder screen. And if I zoom in any further, it's just going to, you know, it's just going to go out of focus, I think.

**Dave Jones:** Yep. Okay, I'm under the microscope. Unfortunately, this is only 1080p, so this will be upscaled to 4K. But this is the old board, of course. You can see how sparse they are.

**Dave Jones:** These ferrite rings are not anywhere near each other. And you can see the green wires running diagonally. They're the sense lines going diagonally through these, and then you've got the X running across this direction, of course, and then the Y running across here.

**Dave Jones:** So you really do need some sort of magnification to actually see like the individual ferrite rings in here really, but anyway, I'll keep exactly the same zoom level, and let's go for the big daddy here.

**Dave Jones:** Let's go see if we can In fact, it has problem. Focus, in focus, you bastard. Come on. Come on. You can do it. Focus. That is the same zoom level.

**Dave Jones:** It is the same zoom level. Look at that. That's nuts. These things are practically touching. Well, no, no, they're not actually touching, but that's got a lot of jeez, that's got a lot of dust.

**Dave Jones:** Let me go to a non-dusty area. There you have it. I've actually got to tilt this board a bit, too, try and keep the microscope from like like unfocusing on this thing, but you can see that they're not quite touching, right?

**Dave Jones:** So I have zoomed in a bit. They're not quite touching. My poker looks enormous, but you can see that the green will be the sense line here. It's interesting that they've like joined those.

**Dave Jones:** Looks like they had that split, and then they joined that. That's interesting, isn't it? But they don't go diagonally anymore with the sense line. The sense line is going vertically through vertically or horizontally, depending on which way you want to look at it.

**Dave Jones:** And of course, you got your regular horizontal lines going through. You got your regular vertical lines, and then you got your giant wire bundles up here. Look at this.

**Dave Jones:** This is just nuts-o. Imagine trying to like cable loom that. That is just insane. Let's see if I can get in there a bit further. It's hard to That's as far as my Tektronix microscope will go.

**Dave Jones:** So, yeah. Each one of those ferrite rings is one bit of memory. And as I said, they've probably still got the data actually stored in them. But to read them out, unfortunately, it will be destructive.

**Dave Jones:** So, it's a one-shot deal. But so, to get this extra density, they've actually overlapped the They've put them on an angle and overlapped those ferrite rings there. That's just That's just crazy.

**Dave Jones:** And they're not touching because the wires will sort of like, you know, self separate them. But wow. Wow, that is really something. Is it not? So, can you count up how many are in that grid?

**Dave Jones:** Yeah, these things are so small that the microscope like loses focus on the you know, the the focus area. Just It It just can't do it. It just can't do it.

**Dave Jones:** Anyway, there you go. That is one bank. So, if you can count those, I I should be able to count those. I will I will count these in the edit and I'll overlay it on the screen.

**Dave Jones:** We've then got 80 banks minus, curiously, like why they just left this out, I don't know. 80 banks. So, there's eight by 10 high. So, 80 minus eight. So, they've got 72 banks there.

**Dave Jones:** So, 72 banks of ferrite memory. That's just That's crazy. So, yeah, these are Ampex. So, those are X and Y drivers there. Ampex jobbies. Like, good luck trying to find I don't even think I'd bother searching for those, really.

**Dave Jones:** Yeah, it looks like it's the same for both X and Y. Is it? Yes. Yes, the same jobbie. But, those uh sense ones up the top, as I said, they would be the uh sense lines.

**Dave Jones:** So, oh they're a Fairchild jobbie. Might be able to get those. 75 uh 234. Anyway, I hope you enjoyed that fascinating look at magnetic core memory from the mid '50s through to, uh you know, early to mid '70s.

**Dave Jones:** Then they they were still making them after that for legacy uh systems, but nobody was seriously using them um after, you know, wouldn't be a choice after um that once solid state memory.

**Dave Jones:** But, they do have their advantages. They're extremely robust and uh they're not susceptible to any, you know, cosmic rays and probably nuclear um you know, EMP pulses and all that um sort of stuff.

**Dave Jones:** These are just absolutely fascinating. I reckon the magnetic information is there's a good chance that it's still in there if you wanted to read it out. So, if you've got any clue um where this thing was made, it's flight something.

**Dave Jones:** So, it was used in some sort of flight hardware. Doesn't quite seem like it's built down to like size and weight for like a space-based uh one, really, but you never know.

**Dave Jones:** Anyway, the Ampex 1600, there you go. Um 16K. And um yeah, I should be able to put up the total in bits here once I count them in the edit.

**Dave Jones:** Anyway, if you like that video, please give it a big thumbs up. As always, discuss it down below. Catch you next time.
