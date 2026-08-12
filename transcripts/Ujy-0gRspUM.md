---
video_id: Ujy-0gRspUM
title: EEVblog #808 - Fluke 196 Scopemeter Repair
url: https://www.youtube.com/watch?v=Ujy-0gRspUM
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 26, "3": 38, "4": 47, "5": 61, "6": 73, "7": 94, "8": 114, "9": 131, "10": 144, "11": 158, "12": 175, "13": 188, "14": 196, "15": 210, "16": 222, "17": 232, "18": 241, "19": 252, "20": 265, "21": 279, "22": 292, "23": 305, "24": 318, "25": 329, "26": 344, "27": 355, "28": 371, "29": 380, "30": 394, "31": 403, "32": 417, "33": 427, "34": 444, "35": 452, "36": 461, "37": 477, "38": 487, "39": 501, "40": 515, "41": 528, "42": 548, "43": 557, "44": 566, "45": 576, "46": 588, "47": 600, "48": 615, "49": 626, "50": 642, "51": 652, "52": 663, "53": 671, "54": 688, "55": 702, "56": 710, "57": 721, "58": 730, "59": 744, "60": 756, "61": 765, "62": 778, "63": 792, "64": 814, "65": 831, "66": 844, "67": 857, "68": 867, "69": 880, "70": 891, "71": 904, "72": 916, "73": 926, "74": 936, "75": 949, "76": 965, "77": 986, "78": 1004, "79": 1013, "80": 1032, "81": 1038, "82": 1055, "83": 1068, "84": 1078, "85": 1095, "86": 1109, "87": 1117, "88": 1135, "89": 1143, "90": 1157, "91": 1179, "92": 1185, "93": 1201, "94": 1210, "95": 1222, "96": 1235, "97": 1255, "98": 1269, "99": 1286, "100": 1299, "101": 1310, "102": 1325, "103": 1351, "104": 1365, "105": 1386, "106": 1401, "107": 1415, "108": 1431, "109": 1443, "110": 1469, "111": 1488, "112": 1498, "113": 1510, "114": 1521, "115": 1541, "116": 1559, "117": 1567, "118": 1577, "119": 1594, "120": 1609, "121": 1626, "122": 1637, "123": 1649, "124": 1663, "125": 1673, "126": 1687, "127": 1704, "128": 1716, "129": 1735, "130": 1746, "131": 1761, "132": 1773, "133": 1790, "134": 1809, "135": 1817, "136": 1830, "137": 1839, "138": 1851}
---

**Dave Jones:** Hi, welcome to a teardown and potential repair, I hope, of this Fluke 169 scopemeter uh kindly sent in by Ronald Bryant to the mailbag. Thank you very much, Ronald.

**Dave Jones:** It's a classic two-channel isolated scopemeter, 100 MHz, 1 gig sample per second. We've got a problem with the screen on it. So, let's rip it apart and see if we can fix this puppy.

**Dave Jones:** Now, it doesn't actually come with a battery and it's got one of those super duper recess DC power jacks in it. So, I unless you've got the correct type of power jack, the one I've got just doesn't fit in there.

**Dave Jones:** You got to have one of those special deep ones, but thankfully we can just take those two screws off there and we can get in like Flynn, no worries.

**Dave Jones:** And it's got one of these evil center negative power jacks on it. So, instead of the usual center positive. So, trap for young players. Anyway, I powered it up 17.5 volts on the external DC power jack.

**Dave Jones:** We don't have the internal battery, we don't need it. And you can see here is the fault. And we've got all these dark horizontal lines right across, but you can see everything's all the text is just fine.

**Dave Jones:** The vertical gradicules look auto. Everything's working just hunky-dory. So, there's something just wrong with those lines there. Now, this can be one of a couple of things. Now, the first problem could be mechanical due to the connections, however they connect this LCD in there uh by a you know, zebra strips or however it's connected in there.

**Dave Jones:** It could be hot bar attachment or whatever. We don't know until we get in there, teardown and take a look. And just like in science with Occam's razor, I'm going to put forward Dave's razor where if you've got a fault and it's you're not sure whether it's you know, equally likely to be mechanical or electrical, go for mechanical.

**Dave Jones:** And of course, it could actually be electrical. It could be some sort of, you know, horizontal driver chip or something like that. We don't know how these things are driven, whether has a controller built into the LCD itself, whether or not it's built into the the processor and chipset driving this thing.

**Dave Jones:** It's got a separate graphics chip. We're not sure until we do the teardown. And there's actually a third option, which is the least likely in that it could be some video mapping video memory mapping issue.

**Dave Jones:** I a fault with the video memory. And this was, you know, not an uncommon fault for really old gear that used a processor and then separate memory and then it would probably have separate video memory chip, for example.

**Dave Jones:** Could be something wrong with the separate video memory chip, but incredibly unlikely, almost to the point of not even considering it because the video memory in something like this would be, you know, inside the processor itself.

**Dave Jones:** And everything's fine with the text and every, you know, it's just it's incredibly unlikely, but I thought I'd mention it. So, the first thing we want to do is a bit of percussive maintenance here.

**Dave Jones:** And that's a classic engineering term, percussive maintenance. I'm trying to put some flex on this, but jeez, this is pretty tough, these Fluke scopemeters. They're built like a brick dunny.

**Dave Jones:** And yeah, I don't like our chances. But anyway, doesn't seem to be anything like that. And opening this puppy up is really easy. You take off the bottom boot, two screws, two screws down the bottom here, and then the whole cover lifts off.

**Dave Jones:** It's designed to lift off because the battery is user replaceable. The BP190 battery just sits in there. It's like a triangle arrangement of cells arranged in a triangle shape.

**Dave Jones:** And there's the header connection for the custom battery in this thing, which we don't have. But we've got some shielding there, so let's see if we can take it apart, get access to the uh LCD.

**Dave Jones:** And I'll tell you what, I hate screws that aren't magnetic. You know, I've got one of these magnetizer demagnetizer, uh very handy. If you don't have one, have one.

**Dave Jones:** And we can't pick up the bloody screws. Yet, I can pick up this huge heavy bit, no problems at all, but no. And here we go. We're in like Flynn.

**Dave Jones:** I took off uh some of the shields here, and you can let's have a look um at because this is like a teardown. Let's have a look at uh the input amp here.

**Dave Jones:** Look at this. Is that uh I don't know. Look, what have they done there? They've tried to put some Did you hide it? I don't know. It's probably some uh fluke custom uh front end would be my guess, but look at the isolation slots here.

**Dave Jones:** Very nice. No problems there at all. And big isolation slot here separating the um uh multimeter section from the uh oscilloscope section. This will be an identical channel up on that channel two up here.

**Dave Jones:** We've got a decent looking uh Japanese relay there. It all looks uh nice and neat and tidy. And uh we've got uh a looks like a uh converter and a massive opto isolator here by the looks of it for the uh data transfer.

**Dave Jones:** So, this would be the isolation for the uh power. So, they've just got an isolated uh uh power converter there in some custom package. I got no idea what that is.

**Dave Jones:** VDTN9. Hmm. And here's the multimeter section. Once again, we've got some uh isolation slots. It's all done uh nice and dandy. Looks like we've got a uh MOV on the input there.

**Dave Jones:** OP97. Couple of little uh SOICs, and well, that's about all she wrote, unless there's something on the bottom side. And once again, they're isolating the power across there, but I don't see any uh look Well, presumably, this one is the uh data.

**Dave Jones:** So, I you know, I could be wrong with about that, but uh that's more likely. So, I don't see anything apart from that. So, they must be getting the data across there as well, somehow.

**Dave Jones:** There's nothing fancy happening with the chips on the multimeter section. It's all uh jelly bean stuff. Some 4HC4051s, you know, like it's all basic. Look at that though. That that cap in there looks a little bit how you doing.

**Dave Jones:** A bit budged in. Don't like the look of that. Got the wrong footprint or something? And no surprises for finding a Fluke part in there because this is a Fluke Philips uh scopemeter, of course.

**Dave Jones:** So, that'll be some sort of uh Philips custom front end. Now, as far as the rest of this puppy goes, we've got ourselves a uh little optical uh isolation data port on the side there.

**Dave Jones:** There you go. That'll be uh transmit and receive there. And this is a big DC-to-DC converter, obviously. Not sure what that puppy is under there. I think I see a Philips uh number.

**Dave Jones:** So, let's take a look at that. And we've got ourselves a main processor up here. That looks like Motorola. And once again, we've got one of the like What?

**Dave Jones:** What is that? It's almost like it like a heat sink. Like a thermal heat sink pad or something like that. But, there's no heat sink on it. Anyway, Fluke custom chip.

**Dave Jones:** And a Fluke custom chip made by Motorola. It could be an off-the-shelf uh processor. I mean, here's our flash memory for it up here. Could just be uh you know, custom uh branded for Fluke because companies almost any chip company will do that.

**Dave Jones:** They'll let you put your own uh part number. They'll silk screen the top of it anything you want if you order, you know, 10,000 or 100,000 of them or something.

**Dave Jones:** They'll put anything on there you want. And they've called it the Garfield. Or I'll call it the Garfield anyway. And there's the other Fluke custom chip. Uh it's got IBM 0001 on there.

**Dave Jones:** Maybe made by IBM perhaps. What we've got on this side, we've got ourselves a membrane here going down. This will not be the LCD that that goes nowhere. So it's just a a thing to like just hold it in place.

**Dave Jones:** So that is not for the LCD. Don't get excited. I believe that's just going down for the the flat flex going down to the membrane keypad on the front.

**Dave Jones:** The LCD is under here. We can see the backlight there. And we flip it around. Ta-da! You might be able to just see some chippies under there. So we got an old school LCD module.

**Dave Jones:** So almost certainly the fault is on there. 99.999% sure, I think. And you'll notice all these test pads down here. It looks like they duplicate and go into the contacts.

**Dave Jones:** The reason that they've got these test pads in here is so that in production when they test this board they can have a better nails which comes down with pogo pins onto all these so they don't have to physically insert cables in there to actually test this thing.

**Dave Jones:** And that's just much quicker and more efficient during the production testing phase. And is that some fuse protection there on the battery pack? Looks like it. And there's our high voltage backlight inverter circuit there which goes out to the cable over this side of the wall here.

**Dave Jones:** So we'll just take out a few more screws here, couple of uh standoffs and ta-da! We are in like Flynn. And here we've got the bottom of the board too.

**Dave Jones:** There we go. That's That's how they're getting the data across from the multimeter. There we go. So those top top two must be the data bricks, not the opto isolators.

**Dave Jones:** And I was wondering why the holes didn't quite line up for these shields. They don't go all the way through so you can actually leave those metal shields in place when you take the board out.

**Dave Jones:** And the metal work came off easily. This thing is very well designed, by the way. Oh, and yep, look, we have rubber seal O-ring seal right around the edges.

**Dave Jones:** Beautiful for, you know, water ingress and also handy for blast protection if you overload the inputs and things like that. So, very nicely designed this Fluke Philips meter. Love it.

**Dave Jones:** Anyway, no surprises for finding Hitachi LCD driver chipsets on here. Hitachi practically own, maybe they still own the LCD driver market, I don't know. But, yeah, they're one of the leaders.

**Dave Jones:** So, let's go to the data sheet for these things. There's a little bit of active stuff happening around in here, but I don't expect a fault in one of these things cuz once again, these are probably, you know, quadrants of the LCD.

**Dave Jones:** So, I don't expect any, you know, we're going to have horizontal lines. I more expect something with maybe You can see all the pins going out here. Probably some maybe some zebra strips or some hot bar flat flex attachments going to the board.

**Dave Jones:** So, I suspect it's more likely, once again, to be a mechanical thing happening, probably. I don't know if it's all over here, but anyway, we'll have a look when we pop that thing out.

**Dave Jones:** That's more likely than being an active fault, I think anyway. Could be wrong. Hey, I'll tell you what, someone's had a go at this, and look at this. These are the clips.

**Dave Jones:** This is how they're supposed to look like, right? These are the clips that compress the LCD onto the board. So, this is why I'm thinking that there's zebra strips under here.

**Dave Jones:** But, look, you can see it looks like somebody has twisted these back. And look, all the ones along the side here are not they're not sort of, you know, bent over to put force down.

**Dave Jones:** There's only like one top and bottom. What the hell? So, what I'm going to do is apply power again and see if I can power this uh power this thing up and uh hopefully we can yep, okay.

**Dave Jones:** I haven't hooked up the backlight, but we've still got the uh still got the lines on the Well, you probably can't see it, but we have got the lines on the screen there.

**Dave Jones:** So, now I can hopefully go around and apply some pressure to that to see if it's a uh pressure problem. Oh, and the metal work uh fell out holding the membrane keypad in there.

**Dave Jones:** There it is. So, I'll put that back. Yeah, by the way, that was of course it was obviously the uh LCD uh cable here and the membrane uh cable.

**Dave Jones:** Okay, so let's see if we can get this puppy Let's apply power. Hopefully, it'll boot up. There we go. We've got our horizontal lines. So, aha, look. See that top bit?

**Dave Jones:** Look, there's some data missing. And yes, I'm careful not to touch the uh high-voltage backlight. It's all like uh isolated. So, uh this could be hard to get Oh, I saw a line come and go there.

**Dave Jones:** I saw a line come and go. I swear I did. There's got to be something in this. Yeah. Hmm, I might just go in there and uh reseat all of those uh tabs.

**Dave Jones:** Just bend them all back and see if it works. Unfortunately, not. I've bent them all physically back in place. You saw a couple of lines come and go there.

**Dave Jones:** But uh still not sure. Yeah, I saw just what Yeah, a line or two come and go. There's something mechanical there, but hmm, might have to take the LCD apart.

**Dave Jones:** And as it turns out, Fluke actually offer the complete service manual for this thing on their website. Fantastic. Why can't all manufacturers do that? It includes the full schematics as well for everything except the LCD module, which they say uh in the troubleshooting procedure, please connect a new LCD to see if the LCD is the problem.

**Dave Jones:** The LCD is not repairable. Oh, thanks for that. But check it out. I can make those lines come and go with pressure on this board. I was doing it a second ago.

**Dave Jones:** Trust me. Yes. Yeah, there we go. There we go. I can make them come and go. You can see on the right-hand side there. I can make them come and go with pressure on that board.

**Dave Jones:** There we go. Ta-da! There's got to be some sort of contact issue. So, we have some LCD voltage troubleshooting test points in the procedure here, but it's not going to be that.

**Dave Jones:** They're over here somewhere, probably on those test pads we saw before, but it's not going to be that. I reckon it's something down in here. It's something in the drive.

**Dave Jones:** I don't think it's any of the control signals cuz the as you saw like the text and everything, the gratical, everything getting over fine, which means that the you know, almost certainly this serial interface is just fine and dandy.

**Dave Jones:** So, our Hitachi chipset here, here's the data sheet. It's actually a 80 column driver. So, of course you can use these for both the horizontal and the vertical they're using here.

**Dave Jones:** Obviously, these ones are the horizontal. You can tell by their physical location going down here on the horizontal part of the screen to drive the lines like that. And then we've got the three column drivers here.

**Dave Jones:** So, curiously, we've only got unless there's another one on the bottom there, we've only got three here, you know, 3 8s a 240 by 240 resolution screen. That's what it must be.

**Dave Jones:** So, I'm just going to try and separate the LCD part from the main PCB here, and I've bent all the uh clips back so we should be able to lift that out.

**Dave Jones:** Not sure if I have to take the backlight out. I don't think so. That could be separate so but I'm concerned cuz I think these weren't there was only like two or three of these that were clipped over.

**Dave Jones:** It looks like somebody had pulled them back so somebody had a crack at fixing this thing and they couldn't you know had the same idea I do and they couldn't fix it.

**Dave Jones:** I don't know. Anyway, it's worth a shot. So let's see if we can lift this off, shall we? Yes, I've turned the power off. In case you're wondering. There we go.

**Dave Jones:** Come on. You can do it. Pop out. Pop out. There we go. Yep, zebra strips. Hang on. Aha, as I suspected. Not only is there zebra strip for the for the vertical here, vertical drivers, they're not the problem but look what we've got on the horizontal.

**Dave Jones:** Ta-da. Hot bar. There we go. I reckon that's our problem. Now it goes under different names but uh hot bar is one of them. I I call it hot bar because what they do is they like get literally a hot bar across here.

**Dave Jones:** It's like a like a huge big wedge soldering iron tip and they apply pressure down in there and it solders those in Look at those pain in the ass little individual contacts.

**Dave Jones:** You should be able to see them in HD here but uh yeah, I reckon we've got bad contacts in there. Almost guarantee it. All right, watch the magic. If we put pressure on the vertical over here we can start see Look, da da da da da da.

**Dave Jones:** We can make the various parts of the vertical line up. Okay? So if we put pressure on the whole thing, there we go. We can get most of it.

**Dave Jones:** So, that's the zebra strip. Zebra strip's just fine, but what we want to test is the horizontal in here. So, I'll try and put most pressure on here and get my poker.

**Dave Jones:** Aha! Look at that. I'm applying pressure down in there to those hot bar attachments. You can see them move. Look at that. There you go. What a bastard. Got you.

**Dave Jones:** Now, as you can see, there's actually two surfaces. One is between the flat flex and the PCB down like this, and the other is between the flat flex and the LCD glass itself.

**Dave Jones:** And both of those have an adhesive conductive solder paste or whatever under them. So, when the hot bar actually goes across there, it melts the adhesive and forms the solder connection as well.

**Dave Jones:** So, I don't like my chances of redoing something like this. It's very fine pitch, but anyway, we might have a shot at it. But, what I'm going to do is just apply pressure along here to like I did it before.

**Dave Jones:** I was applying pressure on the PCB and we're getting some change. So, it's most likely to be along there. If it's on the glass, well, that's a different thing again.

**Dave Jones:** It I don't know that it's likely to be both. So, if I go across the top of the glass like that without trying to put pressure on the Oh, maybe, but I I think I'm actually putting pressure on You saw it change in a different location.

**Dave Jones:** So, I think I might be putting pressure on the board there. So, I don't think the connections are on the glass. I think they're between the flex and the PCB.

**Dave Jones:** So, that's the one I want to try and reheat and reflow and try and repair. Now, I've never actually repaired one of these hot bar attachments and I've heard that they're real tricky and well, it's better if you have the right gear.

**Dave Jones:** I don't have the right gear, but what I do have is my hot air gun. Going to set it to maybe 240 or thereabouts or to do it and I found a pencil with I should actually get one with a new rubber tip, but I'm going to actually use like a soft I don't want to go over there with my plastic pointer and use that.

**Dave Jones:** I think that's going to be a bit hard. I want something a little bit softer than that. I've taped back the LCD to give me a bit of room.

**Dave Jones:** So, I'm going to have to get in there and heat it up and maybe just roll the um, eraser across. Actually, what I can do is flip the end on that to get myself the good end.

**Dave Jones:** Why didn't I think of that before? There we go. So, hopefully I can get in there with that and use that once it's heated up. Just roll it maybe a bit.

**Dave Jones:** Rub it across. No pun intended and see if we can reflow this thing, but I I don't like our chances. I you know, so I'm going to have a go.

**Dave Jones:** Here we go. Going to heat it up. And not all at once. Just move it back and forth. I have no Once again, I have no feel for this cuz I've never done one before.

**Dave Jones:** So, I don't know. I don't even know if this will work. I've no idea, but hey, it's worth a shot. It's a freebie and uh It's worth having a go.

**Dave Jones:** Have a go, you mug. Come on. And we don't want to try to try and avoid heating up the the top glass. One up there. So, we don't want to do that.

**Dave Jones:** We just want the lower PCB one down here. And I've no idea no feel for how long to leave that because the board's got to heat up. The board has thermal mass, of course.

**Dave Jones:** And uh cuz there's no thermal mass in the flat flex, so not worried about that, but uh maybe But the way There we go. Whoa, yeah, I'm starting to Oh, yep, yep.

**Dave Jones:** Too much heat. Too much heat. Yep, I'm starting to uh melt some of the flat flex. Oops. Yeah, I think I applied way too much heat there in the first go.

**Dave Jones:** Hope I haven't damaged the ribbon. Hmm, let's put it back together. Eh. I Yeah, I reckon 10% chance of fixing it. Okay, here we go. As I said, don't like our chances.

**Dave Jones:** But we'll give it a burl. Hello? Hello? Maybe I I I think I Am I out of alignment there? But wow! Did that fix it? Completely. Wow, look at that top part.

**Dave Jones:** It's just a matter of uh Wow! Oh, silly me, still had the LCD taped back here, and you're probably screaming at me. Um so, the the vertical wasn't uh lined up.

**Dave Jones:** So, oops. Um so, I've put that back, and uh let's power it up again. There we go. Whoa, I've got one little pesky line No, no, no. Yeah, is that the trace?

**Dave Jones:** I got some vertical happening there, but wow, that's mostly fixed. Is that like a cursor line, or is that a line on the LCD? That's not fixed. Oh, wow, but I got it.

**Dave Jones:** I GOT IT. WOW, I I'd actually be happy like that even if that line was still through it. Awesome. We don't win a chicken dinner. So, I might just whack that back in the frame for a bit of alignment.

**Dave Jones:** And just in case I get it, don't forget to wipe all your grubby paw prints off the front of the glass. Cuz that would suck. You put it back together, you're all proud of the repair, and there's your bloody big paw print right in the middle of it.

**Dave Jones:** No, I actually tried to reflow that connection again, and I think that line is supposed to be there. So, it's probably a cursor, but look, we've got this pesky vertical line now.

**Dave Jones:** So, that's a real that's a real bummer. I'm not sure what's going on there. Um maybe there's some contamination under the uh zebra strip there, perhaps. So, I just cleaned all the contacts along there and the zebra strip as well, and hopefully um I can get that puppy working again.

**Dave Jones:** Let's give it another try. I can just power this thing up. And push it on. No, still there. What's the deal? Couple of minutes ago, it was uh all um it was just one vertical line, wasn't it?

**Dave Jones:** Very thin one, just like that horizontal one there. Now, it seems to be wider, so uh-huh, look. Looks like we've got another pesky vertical line that's come back right through there.

**Dave Jones:** I've actually put I've bent a couple of the tabs back on the frame here, so it's all putting the original pressure back on there. And these are the cursors, don't worry about those.

**Dave Jones:** I just turned on cursor mode. I can operate the keyboard. Now, there we go. Oh, I think I can turn cursor mode off. There we go. So, we can see a see a line through there.

**Dave Jones:** And then we've still got this line, but as I said, I re heated maybe could be on the glass contact or something like that. Might require some or maybe I just didn't get it second on the second reflow or maybe it's just not possible to get it, but uh looks like maybe one that I missed originally um is not showing up, but I don't know about the black vertical

**Dave Jones:** stripe. That's a real pain. Damn bloody Murphy. We almost had it. We almost had it. Maybe with a bit more fiddling I can do it. I think it's essentially just a vertical alignment, a position alignment in this direction.

**Dave Jones:** So, you've just got to get it right in the sweet spot and we should be able to get that vertical line to vanish, but we've still got that one pesky horizontal line.

**Dave Jones:** Oh, people are going to hate me if I don't finish this and get it 100% perfect. My apologies if I can't ahead of time. Well, I fixed the horizontal ones.

**Dave Jones:** Beautiful. I just uh did some more reflow and some more pressure on there. And it looks like they're gone, hopefully. Although maybe this one around here is still lurking along here.

**Dave Jones:** Perhaps. I'm not sure, but yeah. Anyway, I got rid of the middle one. I just can't quite get the vertical alignment here. It's really pesky. I GOT IT. You bloody beauty.

**Dave Jones:** Look at it. It was incredibly touchy to its uh well, horizontal position here um which gives the vertical uh columns here. And I uh had to muck around with it 10 times before I got that vertical uh strip to go away.

**Dave Jones:** So, it's really, really touchy. And then you have to hold it in place and then try and put the bezel on. And wow, the alignment has to be bang on.

**Dave Jones:** So, but look, I think it's fixed. I think it's fixed. Let's go to the meter. Uh look at that. But I don't like I don't like our chances of this thing uh staying like that.

**Dave Jones:** I suspect it might still develop a problem, but winner, winner, chicken dinner. Wow, I didn't put my odds very high of uh fixing that, but hey, you know, had a go, got lucky.

**Dave Jones:** Oh, here we go. It's back together. Fingers crossed. Let's power it up. And well, helps if I turn the switch on. Here we go. You hear a relay click there, which is interesting.

**Dave Jones:** Um when you actually switch the thing off and on, there's a relay before you hit the soft power button. So, that's rather interesting. UH YES. YES. I thought that was the line there.

**Dave Jones:** Uh no, is it? Yes. Uh there's a line showing up again. Damn it. Yep. Would you believe it? Murphy gets you every time. Damn it. Well, I'm not too fussed about that.

**Dave Jones:** I'm not going to take it back apart and endure that um uh vertical alignment uh thing. And uh no, no, I'm going to be happy with that and call it quits.

**Dave Jones:** And wouldn't you believe it? Murphy again. The scope doesn't work after repairing the LCD. I can't get anything on the bloody thing. Just flatline. Although, the meter seems to work just fine.

**Dave Jones:** Least on ohms, anyway. Slow as a wet week on the auto range in there, but yeah, that's bang on. And the voltage is pretty bang on, too. Check it out.

**Dave Jones:** There's Yeah, that's I've checked it with another meter. That's bang on. I can't get my calibrator over here easily cuz I'm tethered to this bloody power supply. Anyway, yeah, um the multimeter seems to work the scope.

**Dave Jones:** Nope, not a sausage on that scope, and I've got no idea what the problem is. Both channels, just absolutely nothing. So, maybe it had multiple looks like it had multiple faults, the LCD.

**Dave Jones:** Anyway, we fixed the bloody LCD. Winner. I'm going to call that repaired because, well, if this scope did work, it would have been repaired. Yeah, Mercia will get you with that sort of thing, but we did get a bit of bad luck in the end there with that line coming back up.

**Dave Jones:** As you saw, it was fine when I put it back together, and then when I screwed the whole thing on, the line came back. So, you know, yeah, if you were keen enough, you would dick around, but I I wouldn't bother about that horizontal line that's off the you know, the main waveform window practically right at the bottom, so I wouldn't worry about something like that.

**Dave Jones:** But, yeah, repairing these hot bar things can be really quite tricky. So, yeah, just be careful with the amount of heat you put on there, but you can actually repair them.

**Dave Jones:** Hot air and the end of a rubber eraser on the end of a rubber pencil seems to work a treat. Just, you know, roll it across like that. As you can see, I did a bit of wearing out there.

**Dave Jones:** Didn't like the heat, but yeah, just roll it across or push it across like that, and uh yeah, you can fix these things. So, pretty happy with that, but shame it didn't work.

**Dave Jones:** Maybe I can have another look at the scope meter but yeah, I'm going to call it quits for this video and call that one a win. Awesome. So, if you want to discuss it, jump on over to the EVblog forum.

**Dave Jones:** Links down below and leave YouTube comments and blog comments and all that sort of jazz. Hope you enjoyed it. Catch you next time.
