---
video_id: KwWWyOs4KHI
title: EEVblog 1429 - Sony RX100 Camera Troubleshooting Part 2
url: https://www.youtube.com/watch?v=KwWWyOs4KHI
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 57, "3": 85, "4": 104, "5": 138, "6": 172, "7": 194, "8": 232, "9": 253, "10": 272, "11": 289, "12": 321, "13": 350, "14": 361, "15": 388, "16": 406, "17": 428, "18": 451, "19": 473, "20": 489, "21": 502, "22": 527, "23": 557, "24": 592, "25": 613, "26": 633, "27": 664, "28": 675, "29": 697, "30": 713, "31": 727, "32": 756, "33": 785, "34": 811, "35": 836, "36": 852, "37": 869, "38": 889, "39": 907, "40": 928, "41": 942, "42": 961, "43": 994, "44": 1014, "45": 1033, "46": 1050, "47": 1065, "48": 1078, "49": 1110, "50": 1121, "51": 1151, "52": 1179, "53": 1195, "54": 1219, "55": 1251, "56": 1267, "57": 1291, "58": 1305, "59": 1326, "60": 1349, "61": 1373, "62": 1404, "63": 1417, "64": 1439, "65": 1454, "66": 1476, "67": 1497, "68": 1520, "69": 1542, "70": 1566, "71": 1586, "72": 1613, "73": 1638, "74": 1671, "75": 1694, "76": 1714, "77": 1732}
---

**Dave Jones:** Just warning you now, there's going to be no conclusion to this video. There's like there's no way I'm fixing this today. It's just it's not going to happen. Hi, it's Sony RX100 Mark IV repair time again. And I just did that like 57-minute previous video. So, I thought I'd go back in there and take a look.

**Dave Jones:** But unfortunately, there's a fully charged battery. This is what happens today. Nothing. Wha wha wha It does not power on anymore. It's back to its original fault condition. What the? I cannot cop a break at all on these type of repairs. Murphy's like just kicks my ass every single time. So, I guess there's nothing left to do but simply take it apart again. Once again, I don't have to get the lens out, but I'll take it apart. I'll get to the main board and just see if there's like power

**Dave Jones:** on the main board and stuff. So, anyway, I'll take it apart. I'll spare the details. Watch the previous video if you want to see this thing taken apart. So, I'll get right in. Oh, and by the way, if you want to work on this safely and not get zapped like I did, then yeah, I actually found the flash capacitor. It's in here. You can actually probe these two here, and you don't even have to get through the It looks like that's just copper on the surface. It looks like it doesn't have

**Dave Jones:** any like resist or anything like that. So, there you go. If you want to discharge it, of course, I'll have to use a different meter than my BM786. So, what we need is a meter with a phantom voltage resistor auto voltage mode on it. So, let's get in there. And we'll probe that and that.

**Dave Jones:** And that will put a resistor across there, and it's already dropped it down to 8 volts. So, that is completely safe. And we'll probably get some recovery on that voltage there. Yeah, yeah, it's going up. It's recovering a bit, but of course that's completely safe to touch now. I don't have to worry about it. Um yeah, so that's what zapped me before. That will slowly drain away. Of course, you could use a resistor, whatever. Oh, sorry. I forgot to show you um but the ribbon cable uh in there for the LCD,

**Dave Jones:** that seemed to be in fine. So, yeah. All right, I'm back into the uh PCB here. Uh this is off to the sensor. We know the sensor works fine. Um this goes off to the uh the switch on the top, but that one looks that one looks for all the world like it's fine. But once again we'll just reseat them. You'd argue that one wasn't fully in. So, that looks pretty good. I don't know. Let's Let's whack a battery in and see if she um see if she powers up again. I'm powering

**Dave Jones:** it up without the LCD. Nope. Nope. I wonder if there's like a power on sequence to like reset it or something like that. I don't know. That That wouldn't surprise me if there is. Yeah. All right. So that's nothing. All right, let's call up the NI Virtual Bench and uh measure some voltages, shall we? Let's do that again.

**Dave Jones:** Nope. If I hold it down does anything happen? Nope. Anyway, do couple of little probies on here. Nope. Nope. Nope. I'm going to assume that's ground and uh No, we're getting There's nothing on this board. Zippity doodah. Once again, I don't want to have to get into that board again, that top board cuz I got to take everything off when I do that. It's like it's just dead. Like it it doesn't recognize the soft power button at all, but unfortunately, we can't get this thing out and then probe top

**Dave Jones:** order. I'm stick the screen back in just in case. I don't know. That's the first thing it detects or whatever. Okay, that's in there again. It doesn't look like it's in all the way, but that's in as far as I can push it. Keep Well, can I flip it over? Yeah, I can flip it over. There you go. No worries. That'll keep it insulated. Nope.

**Dave Jones:** It's just died. Like seriously, I didn't do anything to it after that video. All I did was just leave it for a bit like Well, overnight and like it it worked when I saw it it worked when I reassembled the thing and I just left it overnight and and it's come back and it's just failed. I can show you that battery's good.

**Dave Jones:** Here you go. 4.14 volts. I know it's negative so all the electrons have fallen out, but um I don't know. What a pain in the ass. Bloody Murphy. Anyway, as for the scrolling um screen thing, it's got to be the connection cable. Well, there there's two faults.

**Dave Jones:** One is that it scrolls and B is that um it also is upside down. So and that it did not flip when I flipped the camera. And normally that um happens when you flip uh you know, the screen's normally like this and you flip the screen over like that. Now, there's um so let's talk about that one first. There's only two ways to actually detect that whether the screen is flipped up or not. One is to have an accelerometer do that and it can't be in the camera. It's got to be

**Dave Jones:** in the screen, right? Because otherwise you it wouldn't be able to detect that the screen's flipped up while the camera's stayed in exactly the same position. Or it could have some sort of sensor contact micro switchy thing that actually detects that the screen's gone up. Once it goes up to a certain angle, um then it flips, but I don't see how that would be possible. So, it's most likely some sort of accelerometer, but it's got to be in the screen. So, that means it's got to go via this ribbon cable here.

**Dave Jones:** Now, of course, this is all the connections for the LCD. We know all the data lines are working, all the clock lines, everything's fine, except it's scrolling. So, there's got to be some sort of vertical sync signal here.

**Dave Jones:** Horizontal If if they got a vertical sync signal, they probably have a like a horizontal sync, or that could be just the clock. I don't know the interface for this one. I Yeah, it's got to have like a vertical sync pin. But then, that doesn't explain why the accelerator is dead. So, it's almost as if like Okay, let's assume that there's a vertical sync pin on here, right? Then, we know that Okay, that could be flapping around in the breeze. Could be floating, and that's causing the problem that we're seeing.

**Dave Jones:** That could be due to gunk You know, like a bad contact. Could be due to a broken trace as well. But then, we've got the accelerometer problem. So, let's assume it's a bad contact. We can maybe clean it, get some isopropyl in there, expect it, and and stuff like that. At least the ribbon cable, anyway. Get some ice, flood the connector with isopropyl and all that.

**Dave Jones:** Give it a good shake around. But then, like the odds of the vertical sync failing, and also maybe some connection for the accelerometer or something. I Like all like both being like bad contact, unless they're both up one end of the cable or something. We can't solve that problem until we solve the problem of this stupid thing turning on.

**Dave Jones:** So, we're going to have to go to the service manual. Now, thank you to somebody who sent me the service manual. Unfortunately, that was like a Mark 1 version of it, but I was actually able to get the service manual for the Mark 4 model. And but I had to pay for this. I paid a whopping five Yankee bucks for this. So, yeah. Click like down below.

**Dave Jones:** I've got to get my money back for this video in ad revenue. And I do believe this is the updated one. So, anyway, look, self-diagnosis function. Like I I not looked at this, but this is this is pretty great. Okay, identifying parts and then I could have just got the service manual and figured out how to take this thing apart properly. I was lucky that I I didn't actually damage anything taking it apart and putting it back together.

**Dave Jones:** So, board assemblies, it's it's got everything. I mean, Sony service manuals are so comprehensive. Um it's absolutely fantastic. Wish they'd just put them on their website. Like, why not? version. But, here's you know, here's all the flex flat flex, you know, they tell you how to do the connectors and everything.

**Dave Jones:** And then they've got like just great diagrams of this thing. Thickness of the sheet, I don't know what like software they're using there and stuff like that. They've got quite a few of those, but anyway, they do explain how to do all this.

**Dave Jones:** Even if it even if those parts aren't in English, doesn't matter. But, here's all the different assemblies. Fantastic. Like, it'd be awesome if these things were available for free on the Sony website. I mean, people would be buying Sony gear like crazy. Well, Joe Average doesn't care, but they'd get a good rep, you know? Check out all these exploded views. Like, you know, that's the heat sink assembly and stuff. It's just It's fantastic. Look, shows you how the flat flexes lay out and stuff. Remove the

**Dave Jones:** screws, disengage the screws, how to get everything apart. Oh, wow. Like, it's probably it has you know, where to put all the tape and stuff like that. There's the ring and there's the lens assembly. Anyway, what I'm really interested in is the schematic to basically show me what that top control board does. Um you know, and how that's like soft power function works. Cuz we've got to solve that. Obviously, like there there's some sort of intermittent thing there or something like that. So, anyway, I Oh, man, I could spend hours

**Dave Jones:** just looking No schematic. Wha- wha- wha- wha- I've been diddled. Out of my five bucks. There is another version of this though, so I might download that one as well. So, let me I'll get back to you. Sure enough, yep, there's another 80-page service manual here. Let's have a squeeze. Okay, so this has got all the parts list. This has the block diagrams, the frame schematics, and the schematics. So, there you go. It's two different documents. So, 180 pages. Look at all this. Look at the bomb. Wow, that's

**Dave Jones:** incredible. Ah, man, imagine if you could just download this from the Sony website. Ah, ah, but look at these block diagrams. This is absolutely fantastic. Wow, hats off to Sony for actually producing these. These are brilliant. Okay, flexible board battery terminal.

**Dave Jones:** Okay, here we go. Right, so this is interesting. Check it out. We have the battery terminal on there, but we also have there's the lithium backup battery. That's what's obviously reset it. When we disconnected all this, took the whole thing apart, it obviously lost all its factory settings.

**Dave Jones:** And that had to do with the well, the lithium battery is on the flexible board. I I simply didn't see that. I don't know. Did you see that in the previous video? I I didn't notice it. But anyway, yeah, that lithium battery. So, resetting that like reset the thing. It made it work. So, maybe if we like disconnect that again, we can at least get it maybe reset it again and back up and running. But then why it failed again just sitting there overnight, I have no idea. But at least we can

**Dave Jones:** potentially get that back up and running. So, I'd be surprised if that didn't work. That's that bottom side like um two-pin layout. It was yeah, two-pin power. That's what we measured. It must have had a third one on there.

**Dave Jones:** Um so, if we can just disconnect that, which is the one on the underside of this connector, so I think even if we have to like lift the board out, it's not a problem. So, yeah, hopefully we can get back in there and let that that's going to be the first thing I'm doing. I want to just want to get this booted up again. And I'm going to disconnect that again and see if that actually kicks it back into action.

**Dave Jones:** I can take it out without taking the board out, but then plugging it back in without taking the board out, no. So, yeah, let me take the board out. Got to take that bracket off again. I want to keep all the ribbons intact.

**Dave Jones:** Got it We can power it up like that, actually, but I don't know what this little tiny ribbon over here good does. I don't think that matters. It's not making electrical connection. No. So, this is just a push on.

**Dave Jones:** So, I still don't know where the battery is. It's in there somewhere, is it? Ah, bugger. I just pulled out that as well. I'm going to have to push that back in. Actually, I can't remember. Where did that one come from? Is there a connected deep down on the back side down in there? Ah, god. I'm going to have to go watch my previous teardown video. Yeah, sure enough. Watch my own video and the back of that board does have a friction connector on it.

**Dave Jones:** It's not a bar one. So, um yeah, I like I can't see it. Maybe if I I don't know. I need a light directly down. I'm probably going to design like a like a custom ring light for this, I think, for my Tagarno microscope that sort of just attaches to the bottom here and just comes out wide so I can like light up directly. Like I've got lights from I've done videos on this. Got lights from either side, light from the front here, but technically nothing

**Dave Jones:** coming down. Even if I turn on the Tagarno internal light like that, it's coming down at an angle. It doesn't go directly down. So, yeah, having that, the ability to do that, would be nice. But anyway, anyway, I'll fiddle around with this and I should be able to do this using feeler vision just to feel that it's gone back in cuz if it goes in and you you know, a bit of trouble sort of tugging it back out, then you know it's you know it's in. So,

**Dave Jones:** give that a whirl. No, didn't have any luck. I'm going to I think I'm going to have to take out the SD card. Um oh, damn. Uh Okay, those ribbons are out. Flippity do dah. SD module. Fantastic. So, I can get back in there now and connect ah reconnect that ribbon. Don't know how I pulled it out.

**Dave Jones:** Bit of tape flapping around in the breeze there. I can see it now. Yeah, you can't, but I can. Yeah, ideally you'd take the battery compartment out as well, but nah, screw that. Have a go, you mug. Come on. Think I got it. That went back in pretty easy.

**Dave Jones:** I think it's in there. Feels like it's in there. Once again, it's just feel a vision. I can't actually see it. Uh I'll just reassemble. Both love and hate flat flex. Is that Is that possible? Oh, the bloody ribbon cable's come out again.

**Dave Jones:** Just wondering, could that be the cause of the problem? Did that cable like slip out or something? And uh I don't know. I I can definitely feel that is in. Definitely felt the friction. Got to use your feel a vision.

**Dave Jones:** Your mark one feel a vision system. Now, I'll be extra careful to put this back in this time without touching that bloody ribbon. Maybe that's what some of the tape is for. Maybe I can just temporarily tape that back. Yeah, there you go.

**Dave Jones:** Just tape that sucker back out of the way. Power cable back in. All right, all the ribbon cable's back. And now, let's do the infamous ribbon cable. Oh, I didn't even look at the schematic for that sync line. I I was too excited. I was too excited to even clean that with isopropyl.

**Dave Jones:** I don't know. I I just want to really get this going. I'll leave this taped up here. I'll leave this taped out of the way like this because I'm sure I'm going to have to diddle with this board again. In fact, it looks pretty askew.

**Dave Jones:** So, but I just want to I'm going to see if I'm able to I need a bit of ins- I need insulator under there. Let's give that a whirl. And where's our power button? Nope. What what what what? Of course it doesn't work.

**Dave Jones:** Zippity doodah. Yeah, I don't know if I got the patience today to investigate this any further. Oh. There's an accelerometer there. There you go. Got him. Um that's not the one in the screen, but look, up up here it's uh yeah, um no, H and uh right, so it's got backlight. So, the LCD and it you know, it doesn't show sync up there. We actually need the pin out of the of the LCD, but up like that that's inconsequential.

**Dave Jones:** The scrolling problem. Um it it it's the boot problem that is the problem. It pitching your sensor. There you go. It's an SE 7701. Focus drive motor, LED drive. Wireless LAN, CPU, camera DSP, AV single processor. Is that Are they pin numbers?

**Dave Jones:** AD1 W31, I guess they are. Of course that'll be one of those BGA jobbies. Um so, image sensor right? So, the image sensor, that's all serial. So, we want LCD. Here we go. Yep, H drive, V drive. So, it's got horizontal and vertical.

**Dave Jones:** Yeah. So, there you go. And uh of course the flexible to the No, that's to the viewfinder electronic viewfinder unit pin 6 or 26 over here. So anyway, yes, there is a vertical sync VD vertical drive, I guess they call it.

**Dave Jones:** And yeah, so obviously the clock works, the horizontal works, all the data works, all your three data all of your three groups of data up here, red, green, and blue, they all work fine. Your power works fine cuz the screen works. It's just lost vertical.

**Dave Jones:** Uh sync. So that would be that line there that it must be open. And that's what happens when the line opens. So yeah, just dodgy contact or something like that. But there's no accelerometer in this LCD unit, is there?

**Dave Jones:** So how are they detecting that the screen's flipped up? Is it some register? Maybe like the LCD actually has the We'd have to look for the LCD board schematic, I guess. But yeah, like as I said, like it's it's not a hinge thing. And and the camera can stay completely still, not move the camera, and you flip the screen up, and and it detects that the screen flips. So obviously, there's an accelerometer or some sort of switch in the LCD that detects once it gets to a certain point,

**Dave Jones:** it flips up. Anyway, that's neither here nor there. I like I think we can fix that like, you know, it could be a broken ribbon, dodgy contact, whatever. Cuz it was obviously working fine before I took it apart. Well, no, it wasn't.

**Dave Jones:** Well, last I used it, it was it was working fine. Then I took it apart and reassembled it, and the vertical screen came back. But why why the battery thing? Oh, they got a thermistor in there. That's the overheat. That is the bane of every digital SLR. Right, so underneath this, we have our These are our actual schematics. So the other was like block level stuff. But this is here's the real deal. That's a CMOS imager. There you go. That's the imager itself. It it's a

**Dave Jones:** Sony sensor, I put Yeah, Sony make sensors for most of the cameras out there, don't they? Yeah, companies will advertise it as, you know, you get one of those little webcamy things, they'll advertise it as having like a Sony sensor because they're the best. Anyway, that's that's a big 1-in jobby. I was trying to see if you find a serial interface. No. No, this is great. I mean, just imagine having, you know, if you really were keen to spend the hours to fix your Sony products, these things

**Dave Jones:** are just fantastic. LCD module. Yeah, vertical, yes, pin 26 as we saw before. Yep. Yep, but there doesn't seem to be a There's a test pin. I wonder what happens when you do the test pin. You short the test pin.

**Dave Jones:** Normally they leave it open, but back light X What's X S clock and X reset? Is that sensor? Cuz the clocks were somewhere else, I thought. Yeah. Yeah. D clock, so what's X S clock and X reset? I don't know. It's renamed AVS clock and XP EFV reset. Oh, jeez. Okay.

**Dave Jones:** There's an ambient sensor output as well. Light get light gate. So, it's got a light sensor ambient light sensor. There's your pitch yaw sensor. Sounds serious, doesn't it, when they call it pitch yaw? You're flying. There you go, for you antenna aficionados there. Manual ring rotation sensor. There you go. So, there's the optocouplers for the rotation for the for the ring. Pop-up detect. Pop No, that's the um that's the viewfinder pop-up, I would imagine.

**Dave Jones:** Right? Strobe No, strobe. No. No, that's for your flash. Right, so your strobe is your flash. Um so, yeah. So, it detects when the flash pops up and it, you know, Yeah, yes, it only charges the capacitor when you I think when you uh pop the flash up.

**Dave Jones:** Or it might keep it pre-charged, so then when you pop the flash up, whoops, it's ready to go. But anyway, the sensor needs to know whether or not the flash is popped up, whether or not to automatically activate it in auto flash mode, cuz it it's not dumb enough to like flash it while it's pressed down and it's inside the body. It's got another three axial acceleration sensor. So yeah, I could like spend hours going through this in detail. A roll sensor.

**Dave Jones:** God, how many roll sensor amp? It's got gyro roll. Like it's How many bloody sensors accelerometer type sensors does it have? There's the eye piece sensor. So I think I mentioned that last video, when you put your eye up to it.

**Dave Jones:** LCD rotation detect. So that's on the flexible board. Okay. I I don't Okay, so it's not built into the LCD, it's on the SE1010 flexible board. Yeah, so we could search for that somewhere else, but the LCD rotation detect, obviously um yeah, it it didn't work.

**Dave Jones:** So there you go. It looks like it does like with another chip. It's not a light sensor, cuz when the screen's always in there, because you can pop it up 90° and it doesn't flip it. So it's only when you pop it up like a 100 and 180 that it actually does that. But anyway, I'm not I'm not worried about that. For those wondering how they do their flash charging, there you go.

**Dave Jones:** There's your big ass cap. 330 V. That's the thing that zapped me. 46 mic. It should driving transistor. So it's all happening now. NFC interface. Blah blah blah blah blah. DC to DC converter. Over voltage protector. Now we're getting into the process CPU. I I like how they've compartmentalized block blocklatized?

**Dave Jones:** The Words obviously not going to pop out of my head. The individual functions here. And that's how how draw schematic symbols, by the way. Um yeah, especially when you got big complex ones like this, separate them into functional blocks like this. It just It makes your life a lot easier. Um you know, you wouldn't have like the if Sometimes it's better to have like the actual pinout of the chip, other times no. You want especially for complex chips, you'll have functional things like this. When it gets to a certain

**Dave Jones:** point in chip size where yeah, it's better to do all that. Makes more sense. Yep, and that just keeps going and going and going and going and going. E-fuse.

**Dave Jones:** Wow, that chip's got everything. Is that a fully custom ASIC? Like wow, wow. CPU, GPIO, like it just keeps bare. It's got bare, etc. Power, CPU, camera, DSP, AV signal processor, lens control, my Yeah, it's It's got everything in this chip. Oh man, these schematics go on forever.

**Dave Jones:** That There is a fuse in there. There's a 1 amp jobby in there. And oh, yeah, there's another one as well, 0.63 amps. 24 volts. You could get a fuse blow Oh, another one over here, 2.5 amps, 32 Wow, there's three fuses inside this thing.

**Dave Jones:** There you go. Got a couple of little regulators there. I squared C, DC to DC converter. It's all happening. Still haven't found like the battery. Oh, battery unreg. Is that it? Voltage detect. Battery unregulated, battery sense, switch. See, could be something like that.

**Dave Jones:** Like it's not detecting that the battery's in there, so therefore it's just not even though power's supplied, it's not powering like It could be anything that's stopping this thing powering on. X power on, X power on accessories. Looks like they had a component in there and they've jumped it over. X power on P row, whatever that is.

**Dave Jones:** Like EF Oh, we're back to the EFV again, are we? We didn't Let's see. So, I've missed the battery. Uh 0.4 V regulator. Wow, what do they need a 0.4 V regulator for? Holy mackerel, 0.4 V + 1.2 + 1.8. If you think you got power rail problems, spare a thought for the Sony designers.

**Dave Jones:** 0.4 V, 1.2 V, 1.8 V, 2.5 V, 1.1 V, and there's more. I've seen other regulators, 3.1.8 and 3.3. And that's just this one page. Wow, and there's more, is there? Is that another 1.1? What is that? That was a different 1.1. That's another switched 1.1.

**Dave Jones:** Nuts. No, well, that's it. Um I didn't find the battery. Oh, the battery It's in there somewhere. I I really But check check this out. Look, they got pin outs. They got pin outs. Ah, beautiful. Anyway, there's the There's that uh battery board with the uh flex, and it's got tiny little coin cell lithium on there.

**Dave Jones:** That'll be so Would it be soldered in? Maybe. Oh, yeah, there you go. It's got those those extra That's where the battery goes on that pin one there. Tiny little pin one goes over to the uh coin cell there, and then it shares a ground. Wow, but anyway, um yeah, I It's like cuz we measured that.

**Dave Jones:** Like, we were getting We were getting power on there. The coin cell shouldn't matter. If the coin cell's not there, it should still boot. Um it'd just wipe the um wipe the CMOS memory, that's all. It'd just wipe the settings, which it did. It the whole thing just factory reset. Um but no, we we actually measured that. We were getting voltage on there. It it it wasn't a problem. So, we're getting voltage onto that. These are all gorgeous. Look, they've even got the pin numbers overlaid on there and

**Dave Jones:** the component designators. It's a thing of beauty. It's a joy forever. Beautiful. Look at this. Look at this. Look at the board overlays. It's just It's fantastic. Anyway, that pornographic, really. Demonetized. Anyway, there's our There's our main processor, isn't it? Yeah. There's our main processor.

**Dave Jones:** Have they got individual pins? Yep. Look, individual balls. Look at that. Look at that. This thing has balls. Wow. The engineers who put together this service manual, it's just brilliant. It's absolutely brilliant. Look, we can get all those You know, so we measured a few of those caps and stuff and like nothing was getting over there. I'm I'm I'm going to call it quits. This video's long enough, I'm sure. So, this will be like It's just a part two follow-up look at that and maybe Yeah, I'll spend some

**Dave Jones:** time, go through the manuals in more detail and find where and how the power system and boot system works cuz obviously there's something wrong there, but why it I I I didn't touch it. It was just sitting there overnight. It was working when I finished that video and then I come back the next day and it didn't work anymore. It would not boot.

**Dave Jones:** Yet, it booted every time I was doing that video and there were more boots that you didn't see. They in the edit cuz the edit was I edited out a lot of stuff from that video even though it was 57 minutes long. It was like 2 hours of footage or something. It just booted every time and then all of a sudden came in the next day and it didn't boot. If you got any idea why it would do that.

**Dave Jones:** I'll put a link to the service manual down below so you can have a squeeze for yourself if you're curious and just you know, just drool over all of the uh There there 2015 official release. Wow, is it that old the camera? Yeah, probably. Yeah, it's up to Mark 7 now.

**Dave Jones:** This is the Mark 4 jobbie. Anyway, I'll make these available and you can see for yourself. Wow. All right. Anyway, hope you enjoyed that. If you did, give it a thumbs up. Catch you next time.
