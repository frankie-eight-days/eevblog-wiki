---
video_id: CK5nbC_dBWk
title: Siglent Signal Generator FAIL
url: https://www.youtube.com/watch?v=CK5nbC_dBWk
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 39, "3": 51, "4": 64, "5": 79, "6": 100, "7": 116, "8": 128, "9": 139, "10": 152, "11": 175, "12": 184, "13": 197, "14": 207, "15": 220, "16": 233, "17": 251, "18": 269, "19": 284, "20": 297, "21": 311, "22": 325, "23": 341, "24": 358, "25": 380, "26": 393, "27": 403, "28": 416, "29": 432, "30": 448, "31": 471, "32": 482, "33": 492, "34": 503, "35": 511, "36": 523, "37": 535, "38": 544, "39": 565, "40": 578, "41": 591, "42": 607, "43": 617, "44": 632, "45": 643, "46": 658, "47": 673, "48": 686, "49": 701, "50": 710, "51": 725, "52": 743, "53": 758}
---

**Dave Jones:** Hi, check this out. We've got the Siglent SDG 2122X uh true waveform generator. It's pretty cool little uh value for money bang per buck device. You've seen me do a teardown of this, which I'll link in down below or whatever, but check this out.

**Dave Jones:** Switch it on. And Come on. Come on. You can do it. You can do it. Hello. McFly. McFly. Um it's stuffed. It's rooted. It's deader than a dead dingo's donger.

**Dave Jones:** Um it Look, there it is. Like the the button there is illuminated and nothing. So, it seems to go through the boot process and it's just died in the ass.

**Dave Jones:** What What? I I don't recall having done anything to it. Um last time I used it and it worked and then I went to use it again and it's bloody rooted.

**Dave Jones:** Unbelievable. Going to have to take a look at it. Well, I don't know. Should we blame number 02 and 01? Um perhaps. Hmm, anyway, um let's Whip It's got a bloody screw on the bottom, doesn't it?

**Dave Jones:** Yeah, course it does. Unbelievable. Ah, that doesn't fit. Take the one lousy screw off the back. And Come on. There we go. We're in like Flynn. Now, because we we saw it actually power up before, so it went through the boot process.

**Dave Jones:** Um And oh, is there any update on the Siglent trademark Siglent rust? No? No? It's looking good. It's looking clean as a whistle. Anyway, um because you saw it powered up, it kind of went through the the boot sequence with the splash screen and everything.

**Dave Jones:** Um so, I'm going to presume that the power supply is probably okay, but of course, golden rule of troubleshooting, thou shall test voltages. So, uh we'll check the voltages here.

**Dave Jones:** There's probably I'm not sure what they are off the top of our head, but uh we can get in there and measure those puppies. That's probably a ground and uh what, you might have a couple of different rails in there.

**Dave Jones:** By the looks of it, hmm. All right, let's go in here. There's actually um we don't particularly Oh, there's a LED on. That's handy. Uh we don't particularly care about this side uh cuz the main processor over here, it's got its own power up here.

**Dave Jones:** So, let's uh just check that. What do we expect? 5 V, 3.3? Let's find out. 6.48. Okay, maybe there's an onboard 5 V reg. Maybe. Huh, I would have expected a digital level rail coming out of that.

**Dave Jones:** Now, of course, the first thing I should have done is check for visuals and things like that. Make sure every nothing's obviously blown. I kind of sort of did that in my uh subconscious head.

**Dave Jones:** And uh no, everything looks fine. And then, of course, give it a bit of a sniff. And uh you know, like check heat sinks and things like that. Just be careful like you wouldn't touch live heat sinks and stuff like that in there.

**Dave Jones:** No touchy um in the mains side of things, but you know, if you have like secondary heat sinks and stuff like that, uh check those to make sure they're not getting too hot.

**Dave Jones:** You know, you can get the uh get the old finger down here. That one there's that little SO8 package SO8. It's probably a uh a little uh linear reg or something like that, but it's not hot at all.

**Dave Jones:** Um I don't know, you know, we got like a heartbeat-y type LED down there. So, that's really interesting. Got another heartbeat LED over here doing the business. Um So, yeah.

**Dave Jones:** Like but our screen is screen is dead and we've got no response from the silly buttons. What the hell? Now, this is interesting. They got that same 6.5 V tap um also going over to the analog board over here.

**Dave Jones:** Even though they're supposed to be like uh isolated like opto Are they opto-isolated? No, they're probably not. I can't remember the teardown, but it actually They got a serial interface between the two, but maybe they're not It doesn't look like there's any like a row of optos there.

**Dave Jones:** So, maybe they're not. Um okay, so I was just um exclaiming that the two grounds were actually connected like this between the two and of course you wouldn't have that if it was uh optically isolated between there.

**Dave Jones:** Um so, yeah. Uh that's Well, anyway, we're getting 6. 1/2 V on there. It is pretty close to precisely 6.5 V. So, I'm inclined to think that it's probably the intended value.

**Dave Jones:** When it's like exactly pretty close to exactly like a round value like that, then you know, it sounds legit, smells legit. But I just initially expected like uh 3.3 or 5.

**Dave Jones:** Okay, I found myself a 5 V test test point like right down on the What is that? Some little programming serial Is that the serial header or whatever? But it's labeled 5 V, so you always look for labels and bingo.

**Dave Jones:** So, that's fine. Um Yeah, okay. But because we've got a big-ass uh TI uh applications processor micro down in there, it probably needs like 1.8 or one of those stupid modern rails.

**Dave Jones:** So, what we do there is keep it on our ground and you can probably see down in there there's a couple of sort uh 323 packages down there, so we'll probe those puppies and have a look.

**Dave Jones:** 3.3 V, bingo. Uh and probe the tab, and that's the five. Five and 3.3, no wackers. So supplies are fine. I mean, we can get in there and like with the scope and like check for like ripple in it, but it's it's a linear reg, like it's not going to be a problem.

**Dave Jones:** So unless like on the high side of those regulators there's 6.5 V output, maybe there's excess ripple on there, and it might be causing something, but meh, you know.

**Dave Jones:** Don't think it matters. All right, so I'm actually going to assume that there's no Well, could be still could be a hardware issue, but like because the damn thing boots, right?

**Dave Jones:** And and our rails in there are fine. There might be a lower rail for the micro or whatever, but obviously like it's getting to the boot screen. Like you can't do that without the micro booting up.

**Dave Jones:** So it's like it's it's like the bootloader is fine, but then it's not loading the application program at the end of it or something like that. So you know, either there's an issue with the flash memory that's holding the application program and the boot memory is somewhere else.

**Dave Jones:** There it is. So yeah, I'm I'm suspecting that something to like Well, I think to progress with this, we really need to get in the bootloader and have a look, and that's probably what that four-pin one down there.

**Dave Jones:** I just checked my teardown video, and I don't believe that I actually got a serial probe on there and actually check to find like a RS232 boot uh on there or a serial uh UART boot interface, but there's most likely to be one, so going to Oh, maybe I did probe those.

**Dave Jones:** And I didn't find anyway, I think I need to find some sort of uh serial boot thing. I mean, it does have an SD card uh slot down in the back there, a little micro SD, but uh that it didn't come with anything.

**Dave Jones:** So, that's presumably, you know, to do the factory maybe the factory bootloader or, you know, the diagnostics or testing. Maybe they put a testing SD card in there or something like that.

**Dave Jones:** Um some automated testing or whatnot. But, anyway, I like it's most likely anyway, that could be those pins, could be these ones along here, could be those ones. I don't know.

**Dave Jones:** I'm going to have to find a serial port. And we should at least get some boot sequence. If we can find that serial port, then booting this thing up, I mean, it gets to here.

**Dave Jones:** Gets to the splash screen, so there's almost certainly going to be some boot code coming out of it. So, maybe we can find a uh clue in there. All right, before we hook up our scope probe, just make sure we've got the right ground, cuz that's a trap for young players.

**Dave Jones:** So, I'm going to go from the uh circuit that we know to be the circuit ground down here to the earth terminal on the back, and everything's hunky-dory. So, we can just, you know, clamp our crow probe onto the side there.

**Dave Jones:** Yes, it's a crow probe, not this scope probe rubbish. Now, am I blind? I'm on this uh the new Siglent scope, might as well use the new uh 1104 four-channel XE uh jobby.

**Dave Jones:** Uh great bang for buck. Um which haven't reviewed yet, sorry. Super busy and now it's the holiday period and the Kickstarter. Anyway, um I didn't um see a way to actually visually see on the channel whether or not you've got the times 10 probe set up or not.

**Dave Jones:** So, it just gave you the 1 V per division. You didn't know what it was actually set to. It would have been nice to have the annunciator like um at ID'd in there.

**Dave Jones:** Anyway, all right, so what we need to do is start probing up its clacker and just have the crow probe ground on there. There we go. So, up, is there anything there?

**Dave Jones:** Nothing there. Hello. There we go. Found it. Straight off the bat. Look at that. Let me uh we can single shot capture that and let me reboot this. Yeah, look at that.

**Dave Jones:** There you go. Well, we've got something. We got one. There you go. That's serial if I've ever seen it. Bingo, found it. It's that uh header along the bottom there like that.

**Dave Jones:** So, that pin there, pin two, is it? Pin one is 5 V. Presumably, pin four is ground. Double-check that. Pin two is the output. Bingo, we can hook that up to our uh RS-232 board.

**Dave Jones:** Well, it's not RS-232 cuz it's not RS-232 signals levels, is it? TTL-based. You know what I mean. TTL signal levels, 0 to 5 V stuff. Acceptance. Not that. 1 2 3.

**Dave Jones:** 3.3. Rubbish. Yeah, modern crap. And of course, for something like this, that a typical boot dummy dumping in a product like this, if you've seen previous teardown videos where I've done it, it's a ton of text.

**Dave Jones:** It's not something you want to be de- decoding, around decoding on your scope. It's just pointless. So, get yourself a like a serial interface board like this one's very handy and then just plug it up and use a serial terminal program on a PC or whatnot.

**Dave Jones:** Sorry to go completely medieval on the screen capture here. Just recording the screen, but bingo, we're in like Flynn, 115 K board, of course, 8N1, your usual stuff that you get.

**Dave Jones:** Usual interface standard you get. Here we go, UBI max sequence number, boom boom. So, like everything's booting up. Right, available PEBs. I don't know what PEBs are. Uh problem that exist before because of PEBCAK.

**Dave Jones:** Um image sequence number, is that like image? I don't know. I No, that's the Okay, so that's a unit is UBI universal boot interface, I believe, something like that.

**Dave Jones:** I don't know all the details of all this uh newfangled software stuff, but uh no, create create create log. Um anyway, skippy command is uh starting device command GPIB USB in it.

**Dave Jones:** USB core registered new interface. Uh it's all it all seems to be happening. Um So, I don't know. Then we get down here and start task. User interface. That's it.

**Dave Jones:** So, like, the process is working. So, like, what's the What's the story? Um It's just, you know, the user interface does not start. And, of course, we don't get uh the keyboard, can't do anything with the key front panel keypad or anything like that.

**Dave Jones:** So, I don't know. Anyone getting got any ideas? Um hm, leave it in the comments.
