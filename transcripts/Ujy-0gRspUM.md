---
video_id: Ujy-0gRspUM
title: EEVblog #808 - Fluke 196 Scopemeter Repair
url: https://www.youtube.com/watch?v=Ujy-0gRspUM
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 30, "3": 43, "4": 61, "5": 73, "6": 88, "7": 102, "8": 118, "9": 131, "10": 147, "11": 160, "12": 177, "13": 191, "14": 206, "15": 220, "16": 232, "17": 246, "18": 261, "19": 274, "20": 290, "21": 302, "22": 318, "23": 333, "24": 347, "25": 359, "26": 373, "27": 386, "28": 402, "29": 417, "30": 432, "31": 447, "32": 459, "33": 474, "34": 487, "35": 504, "36": 519, "37": 532, "38": 548, "39": 561, "40": 574, "41": 588, "42": 608, "43": 620, "44": 633, "45": 648, "46": 663, "47": 679, "48": 696, "49": 709, "50": 718, "51": 731, "52": 750, "53": 765, "54": 782, "55": 799, "56": 816, "57": 836, "58": 850, "59": 867, "60": 880, "61": 892, "62": 907, "63": 922, "64": 935, "65": 949, "66": 965, "67": 984, "68": 1001, "69": 1015, "70": 1032, "71": 1047, "72": 1065, "73": 1082, "74": 1103, "75": 1113, "76": 1128, "77": 1141, "78": 1157, "79": 1171, "80": 1181, "81": 1194, "82": 1210, "83": 1224, "84": 1247, "85": 1267, "86": 1290, "87": 1307, "88": 1323, "89": 1355, "90": 1375, "91": 1396, "92": 1413, "93": 1426, "94": 1440, "95": 1459, "96": 1475, "97": 1491, "98": 1508, "99": 1521, "100": 1532, "101": 1548, "102": 1562, "103": 1577, "104": 1598, "105": 1620, "106": 1634, "107": 1649, "108": 1665, "109": 1678, "110": 1698, "111": 1714, "112": 1733, "113": 1751, "114": 1766, "115": 1782, "116": 1793, "117": 1805, "118": 1817, "119": 1830, "120": 1844, "121": 1855}
---

**Dave Jones:** Hi, welcome to a teardown and potential repair, I hope, of this Fluke 169 scopemeter uh kindly sent in by Ronald Bryant to the mailbag. Thank you very much, Ronald. It's a classic two-channel isolated scopemeter, 100 MHz, 1 gig

**Dave Jones:** sample per second. We've got a problem with the screen on it. So, let's rip it apart and see if we can fix this puppy. Now, it doesn't actually come with a battery and it's got one of those super

**Dave Jones:** duper recess DC power jacks in it. So, I unless you've got the correct type of power jack, the one I've got just doesn't fit in there. You got to have one of those special deep ones, but thankfully we can just take those two

**Dave Jones:** screws off there and we can get in like Flynn, no worries. And it's got one of these evil center negative power jacks on it. So, instead of the usual center positive. So, trap for young players. Anyway, I powered it up 17.5

**Dave Jones:** volts on the external DC power jack. We don't have the internal battery, we don't need it. And you can see here is the fault. And we've got all these dark horizontal lines right across, but you can see everything's all the text is

**Dave Jones:** just fine. The vertical gradicules look auto. Everything's working just hunky-dory. So, there's something just wrong with those lines there. Now, this can be one of a couple of things. Now, the first problem could be mechanical due to the connections, however they

**Dave Jones:** connect this LCD in there uh by a you know, zebra strips or however it's connected in there. It could be hot bar attachment or whatever. We don't know until we get in there, teardown and take a look. And just like in science with

**Dave Jones:** Occam's razor, I'm going to put forward Dave's razor where if you've got a fault and it's you're not sure whether it's you know, equally likely to be mechanical or electrical, go for mechanical. And of course, it could actually be electrical. It could

**Dave Jones:** be some sort of, you know, horizontal driver chip or something like that. We don't know how these things are driven, whether has a controller built into the LCD itself, whether or not it's built into the the processor and chipset driving this

**Dave Jones:** thing. It's got a separate graphics chip. We're not sure until we do the teardown. And there's actually a third option, which is the least likely in that it could be some video mapping video memory mapping issue. I a fault

**Dave Jones:** with the video memory. And this was, you know, not an uncommon fault for really old gear that used a processor and then separate memory and then it would probably have separate video memory chip, for example. Could be something

**Dave Jones:** wrong with the separate video memory chip, but incredibly unlikely, almost to the point of not even considering it because the video memory in something like this would be, you know, inside the processor itself. And everything's fine with the text and

**Dave Jones:** every, you know, it's just it's incredibly unlikely, but I thought I'd mention it. So, the first thing we want to do is a bit of percussive maintenance here. And that's a classic engineering term, percussive maintenance. I'm trying to

**Dave Jones:** put some flex on this, but jeez, this is pretty tough, these Fluke scopemeters. They're built like a brick dunny. And yeah, I don't like our chances. But anyway, doesn't seem to be anything like that. And opening this puppy up is really

**Dave Jones:** easy. You take off the bottom boot, two screws, two screws down the bottom here, and then the whole cover lifts off. It's designed to lift off because the battery is user replaceable. The BP190 battery just sits in there. It's like a triangle

**Dave Jones:** arrangement of cells arranged in a triangle shape. And there's the header connection for the custom battery in this thing, which we don't have. But we've got some shielding there, so let's see if we can take it apart, get access

**Dave Jones:** to the uh LCD. And I'll tell you what, I hate screws that aren't magnetic. You know, I've got one of these magnetizer demagnetizer, uh very handy. If you don't have one, have one. And we can't pick up the bloody screws. Yet, I can

**Dave Jones:** pick up this huge heavy bit, no problems at all, but no. And here we go. We're in like Flynn. I took off uh some of the shields here, and you can let's have a look um at because this is like a teardown. Let's

**Dave Jones:** have a look at uh the input amp here. Look at this. Is that uh I don't know. Look, what have they done there? They've tried to put some Did you hide it? I don't know. It's probably some uh

**Dave Jones:** fluke custom uh front end would be my guess, but look at the isolation slots here. Very nice. No problems there at all. And big isolation slot here separating the um uh multimeter section from the uh oscilloscope section. This will be an

**Dave Jones:** identical channel up on that channel two up here. We've got a decent looking uh Japanese relay there. It all looks uh nice and neat and tidy. And uh we've got uh a looks like a uh converter and a

**Dave Jones:** massive opto isolator here by the looks of it for the uh data transfer. So, this would be the isolation for the uh power. So, they've just got an isolated uh uh power converter there in some custom package. I got no idea

**Dave Jones:** what that is. VDTN9. Hmm. And here's the multimeter section. Once again, we've got some uh isolation slots. It's all done uh nice and dandy. Looks like we've got a uh MOV on the input there. OP97. Couple of little uh

**Dave Jones:** SOICs, and well, that's about all she wrote, unless there's something on the bottom side. And once again, they're isolating the power across there, but I don't see any uh look Well, presumably, this one is the uh data. So, I you know, I could

**Dave Jones:** be wrong with about that, but uh that's more likely. So, I don't see anything apart from that. So, they must be getting the data across there as well, somehow. There's nothing fancy happening with the chips on the multimeter

**Dave Jones:** section. It's all uh jelly bean stuff. Some 4HC4051s, you know, like it's all basic. Look at that though. That that cap in there looks a little bit how you doing. A bit budged in. Don't like the look of

**Dave Jones:** that. Got the wrong footprint or something? And no surprises for finding a Fluke part in there because this is a Fluke Philips uh scopemeter, of course. So, that'll be some sort of uh Philips custom front end. Now, as far

**Dave Jones:** as the rest of this puppy goes, we've got ourselves a uh little optical uh isolation data port on the side there. There you go. That'll be uh transmit and receive there. And this is a big DC-to-DC converter, obviously. Not sure

**Dave Jones:** what that puppy is under there. I think I see a Philips uh number. So, let's take a look at that. And we've got ourselves a main processor up here. That looks like Motorola. And once again, we've got one of the like What?

**Dave Jones:** What is that? It's almost like it like a heat sink. Like a thermal heat sink pad or something like that. But, there's no heat sink on it. Anyway, Fluke custom chip. And a Fluke custom chip made by Motorola. It could be an

**Dave Jones:** off-the-shelf uh processor. I mean, here's our flash memory for it up here. Could just be uh you know, custom uh branded for Fluke because companies almost any chip company will do that. They'll let you put your own uh part number. They'll

**Dave Jones:** silk screen the top of it anything you want if you order, you know, 10,000 or 100,000 of them or something. They'll put anything on there you want. And they've called it the Garfield. Or I'll call it the Garfield anyway. And there's

**Dave Jones:** the other Fluke custom chip. Uh it's got IBM 0001 on there. Maybe made by IBM perhaps. What we've got on this side, we've got ourselves a membrane here going down. This will not be the LCD that that goes

**Dave Jones:** nowhere. So it's just a a thing to like just hold it in place. So that is not for the LCD. Don't get excited. I believe that's just going down for the the flat flex going down to the membrane

**Dave Jones:** keypad on the front. The LCD is under here. We can see the backlight there. And we flip it around. Ta-da! You might be able to just see some chippies under there. So we got an old school LCD module. So almost certainly the fault is

**Dave Jones:** on there. 99.999% sure, I think. And you'll notice all these test pads down here. It looks like they duplicate and go into the contacts. The reason that they've got these test pads in here is so that in production

**Dave Jones:** when they test this board they can have a better nails which comes down with pogo pins onto all these so they don't have to physically insert cables in there to actually test this thing. And that's just much quicker and more

**Dave Jones:** efficient during the production testing phase. And is that some fuse protection there on the battery pack? Looks like it. And there's our high voltage backlight inverter circuit there which goes out to the cable over this side of the wall here.

**Dave Jones:** So we'll just take out a few more screws here, couple of uh standoffs and ta-da! We are in like Flynn. And here we've got the bottom of the board too. There we go. That's That's how they're getting the data

**Dave Jones:** across from the multimeter. There we go. So those top top two must be the data bricks, not the opto isolators. And I was wondering why the holes didn't quite line up for these shields. They don't go all the way through so you can actually

**Dave Jones:** leave those metal shields in place when you take the board out. And the metal work came off easily. This thing is very well designed, by the way. Oh, and yep, look, we have rubber seal O-ring seal right around the edges.

**Dave Jones:** Beautiful for, you know, water ingress and also handy for blast protection if you overload the inputs and things like that. So, very nicely designed this Fluke Philips meter. Love it. Anyway, no surprises for finding Hitachi LCD driver chipsets on here. Hitachi

**Dave Jones:** practically own, maybe they still own the LCD driver market, I don't know. But, yeah, they're one of the leaders. So, let's go to the data sheet for these things. There's a little bit of active stuff happening around in here, but I

**Dave Jones:** don't expect a fault in one of these things cuz once again, these are probably, you know, quadrants of the LCD. So, I don't expect any, you know, we're going to have horizontal lines. I more expect something with maybe You can

**Dave Jones:** see all the pins going out here. Probably some maybe some zebra strips or some hot bar flat flex attachments going to the board. So, I suspect it's more likely, once again, to be a mechanical thing happening, probably. I don't know if

**Dave Jones:** it's all over here, but anyway, we'll have a look when we pop that thing out. That's more likely than being an active fault, I think anyway. Could be wrong. Hey, I'll tell you what, someone's had a go at this, and look at this. These are

**Dave Jones:** the clips. This is how they're supposed to look like, right? These are the clips that compress the LCD onto the board. So, this is why I'm thinking that there's zebra strips under here. But, look, you can see it looks like somebody

**Dave Jones:** has twisted these back. And look, all the ones along the side here are not they're not sort of, you know, bent over to put force down. There's only like one top and bottom. What the hell? So, what I'm going to do is apply

**Dave Jones:** power again and see if I can power this uh power this thing up and uh hopefully we can yep, okay. I haven't hooked up the backlight, but we've still got the uh still got the lines on the Well, you

**Dave Jones:** probably can't see it, but we have got the lines on the screen there. So, now I can hopefully go around and apply some pressure to that to see if it's a uh pressure problem. Oh, and the metal work

**Dave Jones:** uh fell out holding the membrane keypad in there. There it is. So, I'll put that back. Yeah, by the way, that was of course it was obviously the uh LCD uh cable here and the membrane uh cable. Okay, so let's see if we can get this

**Dave Jones:** puppy Let's apply power. Hopefully, it'll boot up. There we go. We've got our horizontal lines. So, aha, look. See that top bit? Look, there's some data missing. And yes, I'm careful not to touch the uh high-voltage backlight. It's all like uh

**Dave Jones:** isolated. So, uh this could be hard to get Oh, I saw a line come and go there. I saw a line come and go. I swear I did. There's got to be something in this. Yeah. Hmm, I might just go in there and

**Dave Jones:** uh reseat all of those uh tabs. Just bend them all back and see if it works. Unfortunately, not. I've bent them all physically back in place. You saw a couple of lines come and go there. But uh still not sure. Yeah, I saw just what

**Dave Jones:** Yeah, a line or two come and go. There's something mechanical there, but hmm, might have to take the LCD apart. And as it turns out, Fluke actually offer the complete service manual for this thing on their website. Fantastic.

**Dave Jones:** Why can't all manufacturers do that? It includes the full schematics as well for everything except the LCD module, which they say uh in the troubleshooting procedure, please connect a new LCD to see if the LCD is the problem. The LCD is not

**Dave Jones:** repairable. Oh, thanks for that. But check it out. I can make those lines come and go with pressure on this board. I was doing it a second ago. Trust me.

**Dave Jones:** Yes. Yeah, there we go. There we go. I can make them come and go. You can see on the right-hand side there. I can make them come and go with pressure on that board. There we go. Ta-da! There's got to be some sort of

**Dave Jones:** contact issue. So, we have some LCD voltage troubleshooting test points in the procedure here, but it's not going to be that. They're over here somewhere, probably on those test pads we saw before, but it's not going to be that. I reckon it's something down

**Dave Jones:** in here. It's something in the drive. I don't think it's any of the control signals cuz the as you saw like the text and everything, the gratical, everything getting over fine, which means that the you know, almost certainly this serial

**Dave Jones:** interface is just fine and dandy. So, our Hitachi chipset here, here's the data sheet. It's actually a 80 column driver. So, of course you can use these for both the horizontal and the vertical they're using here. Obviously, these

**Dave Jones:** ones are the horizontal. You can tell by their physical location going down here on the horizontal part of the screen to drive the lines like that. And then we've got the three column drivers here. So, curiously, we've only got

**Dave Jones:** unless there's another one on the bottom there, we've only got three here, you know, 3 8s a 240 by 240 resolution screen. That's what it must be. So, I'm just going to try and separate the LCD part from the main PCB

**Dave Jones:** here, and I've bent all the uh clips back so we should be able to lift that out. Not sure if I have to take the backlight out. I don't think so. That could be separate so but I'm concerned cuz I think these weren't

**Dave Jones:** there was only like two or three of these that were clipped over. It looks like somebody had pulled them back so somebody had a crack at fixing this thing and they couldn't you know had the same idea I do and they couldn't fix it.

**Dave Jones:** I don't know. Anyway, it's worth a shot. So let's see if we can lift this off, shall we? Yes, I've turned the power off. In case you're wondering. There we go.

**Dave Jones:** Come on. You can do it. Pop out. Pop out. There we go. Yep, zebra strips. Hang on. Aha, as I suspected. Not only is there zebra strip for the for the vertical here, vertical drivers, they're not the problem but look what

**Dave Jones:** we've got on the horizontal. Ta-da. Hot bar. There we go. I reckon that's our problem. Now it goes under different names but uh hot bar is one of them. I I call it hot bar because what they do is they like

**Dave Jones:** get literally a hot bar across here. It's like a like a huge big wedge soldering iron tip and they apply pressure down in there and it solders those in Look at those pain in the ass little individual contacts. You should be able

**Dave Jones:** to see them in HD here but uh yeah, I reckon we've got bad contacts in there. Almost guarantee it. All right, watch the magic. If we put pressure on the vertical over here we can start see Look, da da da da da

**Dave Jones:** da. We can make the various parts of the vertical line up. Okay? So if we put pressure on the whole thing, there we go. We can get most of it. So, that's the zebra strip. Zebra strip's just fine, but what we want to test is

**Dave Jones:** the horizontal in here. So, I'll try and put most pressure on here and get my poker. Aha! Look at that. I'm applying pressure down in there to those hot bar attachments. You can see them move. Look at that.

**Dave Jones:** There you go. What a bastard. Got you. Now, as you can see, there's actually two surfaces. One is between the flat flex and the PCB down like this, and the other is between the flat flex and the LCD glass itself. And both of those have

**Dave Jones:** an adhesive conductive solder paste or whatever under them. So, when the hot bar actually goes across there, it melts the adhesive and forms the solder connection as well. So, I don't like my chances of redoing something like this. It's very fine

**Dave Jones:** pitch, but anyway, we might have a shot at it. But, what I'm going to do is just apply pressure along here to like I did it before. I was applying pressure on the PCB and we're getting some change.

**Dave Jones:** So, it's most likely to be along there. If it's on the glass, well, that's a different thing again. It I don't know that it's likely to be both. So, if I go across the top of the glass like that without trying to put pressure

**Dave Jones:** on the Oh, maybe, but I I think I'm actually putting pressure on You saw it change in a different location. So, I think I might be putting pressure on the board there. So, I don't think the connections are on the glass.

**Dave Jones:** I think they're between the flex and the PCB. So, that's the one I want to try and reheat and reflow and try and repair. Now, I've never actually repaired one of these hot bar attachments and I've heard that they're real tricky and well, it's

**Dave Jones:** better if you have the right gear. I don't have the right gear, but what I do have is my hot air gun. Going to set it to maybe 240 or thereabouts or to do it and I found a pencil with

**Dave Jones:** I should actually get one with a new rubber tip, but I'm going to actually use like a soft I don't want to go over there with my plastic pointer and use that. I think that's going to be a bit

**Dave Jones:** hard. I want something a little bit softer than that. I've taped back the LCD to give me a bit of room. So, I'm going to have to get in there and heat it up and maybe just roll the um,

**Dave Jones:** eraser across. Actually, what I can do is flip the end on that to get myself the good end. Why didn't I think of that before? There we go. So, hopefully I can get in there with that and use that once it's heated up. Just

**Dave Jones:** roll it maybe a bit. Rub it across. No pun intended and see if we can reflow this thing, but I I don't like our chances. I you know, so I'm going to have a go. Here we go. Going to heat it

**Dave Jones:** up. And not all at once. Just move it back and forth. I have no Once again, I have no feel for this cuz I've never done one before. So, I don't know. I don't even know if this will work. I've no idea, but

**Dave Jones:** hey, it's worth a shot. It's a freebie and uh It's worth having a go. Have a go, you mug. Come on. And we don't want to try to try and avoid heating up the the top glass. One up there. So, we don't want to do

**Dave Jones:** that. We just want the lower PCB one down here. And I've no idea no feel for how long to leave that because the board's got to heat up. The board has thermal mass, of course. And uh cuz there's no thermal mass in the flat

**Dave Jones:** flex, so not worried about that, but uh maybe But the way There we go. Whoa, yeah, I'm starting to Oh, yep, yep. Too much heat. Too much heat. Yep, I'm starting to uh melt some of the flat flex. Oops. Yeah,

**Dave Jones:** I think I applied way too much heat there in the first go. Hope I haven't damaged the ribbon. Hmm, let's put it back together. Eh. I Yeah, I reckon 10% chance of fixing it. Okay, here we go. As I said, don't

**Dave Jones:** like our chances. But we'll give it a burl. Hello? Hello? Maybe I I I think I Am I out of alignment there? But wow! Did that fix it? Completely. Wow, look at that top part. It's just a matter of uh

**Dave Jones:** Wow! Oh, silly me, still had the LCD taped back here, and you're probably screaming at me. Um so, the the vertical wasn't uh lined up. So, oops. Um so, I've put that back, and uh let's power it up again.

**Dave Jones:** There we go. Whoa, I've got one little pesky line No, no, no. Yeah, is that the trace? I got some vertical happening there, but wow, that's mostly fixed. Is that like a cursor line, or is that a line on the

**Dave Jones:** LCD? That's not fixed. Oh, wow, but I got it. I GOT IT. WOW, I I'd actually be happy like that even if that line was still through it. Awesome. We don't win a chicken dinner. So, I might just whack that back in the

**Dave Jones:** frame for a bit of alignment. And just in case I get it, don't forget to wipe all your grubby paw prints off the front of the glass. Cuz that would suck. You put it back together, you're all proud of the

**Dave Jones:** repair, and there's your bloody big paw print right in the middle of it. No, I actually tried to reflow that connection again, and I think that line is supposed to be there. So, it's probably a cursor, but look, we've got

**Dave Jones:** this pesky vertical line now. So, that's a real that's a real bummer. I'm not sure what's going on there. Um maybe there's some contamination under the uh zebra strip there, perhaps. So, I just cleaned all the contacts along there and

**Dave Jones:** the zebra strip as well, and hopefully um I can get that puppy working again. Let's give it another try. I can just power this thing up.

**Dave Jones:** And push it on. No, still there. What's the deal? Couple of minutes ago, it was uh all um it was just one vertical line, wasn't it? Very thin one, just like that horizontal one there. Now, it seems to

**Dave Jones:** be wider, so uh-huh, look. Looks like we've got another pesky vertical line that's come back right through there. I've actually put I've bent a couple of the tabs back on the frame here, so it's all putting the original pressure back on there. And

**Dave Jones:** these are the cursors, don't worry about those. I just turned on cursor mode. I can operate the keyboard. Now, there we go. Oh, I think I can turn cursor mode off. There we go. So, we can see a

**Dave Jones:** see a line through there. And then we've still got this line, but as I said, I re heated maybe could be on the glass contact or something like that. Might require some or maybe I just didn't get it second on the second reflow or maybe

**Dave Jones:** it's just not possible to get it, but uh looks like maybe one that I missed originally um is not showing up, but I don't know about the black vertical stripe. That's a real pain. Damn bloody Murphy. We almost had it.

**Dave Jones:** We almost had it. Maybe with a bit more fiddling I can do it. I think it's essentially just a vertical alignment, a position alignment in this direction. So, you've just got to get it right in the sweet spot and we should be able to

**Dave Jones:** get that vertical line to vanish, but we've still got that one pesky horizontal line. Oh, people are going to hate me if I don't finish this and get it 100% perfect. My apologies if I can't ahead of time. Well, I fixed the

**Dave Jones:** horizontal ones. Beautiful. I just uh did some more reflow and some more pressure on there. And it looks like they're gone, hopefully. Although maybe this one around here is still lurking along here. Perhaps. I'm not sure, but yeah. Anyway, I got

**Dave Jones:** rid of the middle one. I just can't quite get the vertical alignment here. It's really pesky. I GOT IT. You bloody beauty. Look at it. It was incredibly touchy to its uh well, horizontal position here um which gives the vertical uh columns here. And

**Dave Jones:** I uh had to muck around with it 10 times before I got that vertical uh strip to go away. So, it's really, really touchy. And then you have to hold it in place and then try and put the bezel on. And

**Dave Jones:** wow, the alignment has to be bang on. So, but look, I think it's fixed. I think it's fixed. Let's go to the meter. Uh look at that. But I don't like I don't like our chances of this thing uh

**Dave Jones:** staying like that. I suspect it might still develop a problem, but winner, winner, chicken dinner. Wow, I didn't put my odds very high of uh fixing that, but hey, you know, had a go, got lucky. Oh, here we go. It's back together.

**Dave Jones:** Fingers crossed. Let's power it up. And well, helps if I turn the switch on. Here we go. You hear a relay click there, which is interesting. Um when you actually switch the thing off and on, there's a relay before you hit

**Dave Jones:** the soft power button. So, that's rather interesting. UH YES. YES. I thought that was the line there. Uh no, is it? Yes. Uh there's a line showing up again. Damn it. Yep.

**Dave Jones:** Would you believe it? Murphy gets you every time. Damn it. Well, I'm not too fussed about that. I'm not going to take it back apart and endure that um uh vertical alignment uh thing. And uh no, no, I'm

**Dave Jones:** going to be happy with that and call it quits. And wouldn't you believe it? Murphy again. The scope doesn't work after repairing the LCD. I can't get anything on the bloody thing. Just flatline. Although, the meter seems to work just

**Dave Jones:** fine. Least on ohms, anyway. Slow as a wet week on the auto range in there, but yeah, that's bang on. And the voltage is pretty bang on, too. Check it out. There's Yeah, that's I've checked it with another meter. That's bang on. I

**Dave Jones:** can't get my calibrator over here easily cuz I'm tethered to this bloody power supply. Anyway, yeah, um the multimeter seems to work the scope. Nope, not a sausage on that scope, and I've got no idea what the problem is.

**Dave Jones:** Both channels, just absolutely nothing. So, maybe it had multiple looks like it had multiple faults, the LCD. Anyway, we fixed the bloody LCD. Winner. I'm going to call that repaired because, well, if this scope did work, it would have been

**Dave Jones:** repaired. Yeah, Mercia will get you with that sort of thing, but we did get a bit of bad luck in the end there with that line coming back up. As you saw, it was fine when I put it back together, and then

**Dave Jones:** when I screwed the whole thing on, the line came back. So, you know, yeah, if you were keen enough, you would dick around, but I I wouldn't bother about that horizontal line that's off the you know, the main waveform window

**Dave Jones:** practically right at the bottom, so I wouldn't worry about something like that. But, yeah, repairing these hot bar things can be really quite tricky. So, yeah, just be careful with the amount of heat you put on there, but you can

**Dave Jones:** actually repair them. Hot air and the end of a rubber eraser on the end of a rubber pencil seems to work a treat. Just, you know, roll it across like that. As you can see, I did a bit of

**Dave Jones:** wearing out there. Didn't like the heat, but yeah, just roll it across or push it across like that, and uh yeah, you can fix these things. So, pretty happy with that, but shame it didn't work. Maybe I can have another look at the scope meter

**Dave Jones:** but yeah, I'm going to call it quits for this video and call that one a win. Awesome. So, if you want to discuss it, jump on over to the EVblog forum. Links down below and leave YouTube comments and blog

**Dave Jones:** comments and all that sort of jazz. Hope you enjoyed it. Catch you next time.
