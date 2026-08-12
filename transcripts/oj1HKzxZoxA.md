---
video_id: oj1HKzxZoxA
title: EEVblog #331 - Mailbag
url: https://www.youtube.com/watch?v=oj1HKzxZoxA
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 26, "3": 37, "4": 53, "5": 62, "6": 78, "7": 88, "8": 101, "9": 116, "10": 132, "11": 147, "12": 162, "13": 178, "14": 184, "15": 203, "16": 222, "17": 247, "18": 262, "19": 275, "20": 287, "21": 301, "22": 311, "23": 331, "24": 346, "25": 356, "26": 377, "27": 391, "28": 411, "29": 431, "30": 441, "31": 457, "32": 469, "33": 483, "34": 497, "35": 509, "36": 523, "37": 536, "38": 556, "39": 572, "40": 583, "41": 597, "42": 621, "43": 640, "44": 654, "45": 668, "46": 676, "47": 684, "48": 701, "49": 718, "50": 735, "51": 750, "52": 773, "53": 793, "54": 808, "55": 817, "56": 831, "57": 845, "58": 858, "59": 875, "60": 887, "61": 897, "62": 905, "63": 924, "64": 935, "65": 951, "66": 963, "67": 977, "68": 987, "69": 1007, "70": 1025, "71": 1042, "72": 1050, "73": 1071, "74": 1087, "75": 1102, "76": 1109, "77": 1124, "78": 1134, "79": 1161, "80": 1185, "81": 1199, "82": 1209, "83": 1221, "84": 1235, "85": 1246, "86": 1264, "87": 1276, "88": 1286, "89": 1302, "90": 1311, "91": 1323, "92": 1337, "93": 1360, "94": 1368, "95": 1383, "96": 1393, "97": 1405, "98": 1415, "99": 1427, "100": 1440, "101": 1453, "102": 1468}
---

**Dave Jones:** Hi, welcome to the ever popular mailbag segment where I open my mail and well, I've got a mail bonanza. I've got six items. Now, as it turns out, I think somebody has swamped me here.

**Dave Jones:** I think these three are from the same person. And we've got to check it out. The Secret Australian Military Office. It got here. No worries. The Secret Australian Military Office.

**Dave Jones:** There we go. And uh this is also from uh Cowoon in Hong Kong as well. I mean, you know, I know Hong Kong's a big uh place, but yeah, number 68600 Koon.

**Dave Jones:** I think it's the same person. There you go. Electronics, Jeff. Thank you very much, Jeff. All right, let's have a look here. Ah, it's a it's a charger. Oh, that's right.

**Dave Jones:** And I think um I think he emailed me about this and wanted me to uh crack it open and uh have a look at it. So we might very well do that.

**Dave Jones:** It is an Australian uh charger. Doesn't have the new uh insulated thing. So technically you wouldn't be able to uh sell that here, but uh cheap and cheerful USB charger there.

**Dave Jones:** Probably from the one hung low factory. So, probably built down to the lowest price point. What do we have here? Ah, he sent me more. What do we got?

**Dave Jones:** A lithium ion battery. Longlasting high capacity power. What am I going to do with that? Thank you very much. Actually, might be able to use it for the new USB power supply.

**Dave Jones:** You'll see a video on that soon, I'm sure. Fee [ __ ] Yeah. Okay. Oh, yeah. Look. Oh, [ __ ] Is that a [ __ ] cat? No.

**Dave Jones:** Don't know. I don't know. Yeah. Right. 9 months warranty. Wow. You don't see that every day, do you? Here we go. And that is a um for a Motorola seal there for Motorola.

**Dave Jones:** Don't have a Motorola phone. What else am I going to do to that? Take it apart. Maybe I could uh uh decode the serial um if it's got one of those um uh ID chips in it.

**Dave Jones:** Maybe. Eh, who knows? Next. Here we go. What do we got? Oh, whole bunch of Oh, little brick little brick converters. So, this is a whole bunch of convertery stuff.

**Dave Jones:** Definitely ripped off boards. You can see the copper stuck to the uh the pads. stuck to the pins. And these are little converters, I guess. KSR3R33S. Um, but there are they potted?

**Dave Jones:** I don't know. They might not be. I'll try and crack one of those open with the knife and uh see what's inside. Looks like I can see a PCB in there.

**Dave Jones:** Yeah. Yeah, I got the board. There you go. Not potted at all. Or actually, hang on. No. Yep. There we go. Got it. And there it is. It's an MP23 07, I think it is.

**Dave Jones:** So, we'll have to look that one up. And this looks like it's got some gunk on the top of that inductor there. No point taking it off, but uh yeah, nothing fancy there at all.

**Dave Jones:** Boring is batshit, I'm afraid. And I just checked that uh MP2307 is a monolithic uh power converters step down converter. Nothing uh fancy at all you know uh 90 something% uh efficiency uh peak efficiency um you know down to it can have 0.9 volts to 20 something odd uh volts output and well it's not exciting at all.

**Dave Jones:** Um, I think Jeff was it um I think he mentioned he wanted me to uh test these on the dummy load, but um quite frankly h couldn't be bothered.

**Dave Jones:** And here's the power adapter. 5 vols 1 amps. So it's a 5V uh universal input 100 to 240 volts. Made in China power adapter. Woohoo. Should be a real treat inside.

**Dave Jones:** So, what I'm going to do with this crappy adapter, I will just leave it for a uh future tear down because I predict this is going to be one steaming pile of dog turd.

**Dave Jones:** So, we'll leave that. I think it probably deserves its own uh episode with u a decent analysis of it and a bit of reverse engineering and testing perhaps. So, um yeah, I'm not going to bother with these.

**Dave Jones:** So, yeah, thank you very much, Jeff. And let's go into more mail. But I have taken apart this battery though. And I just snipped off this plastic surround. And tada.

**Dave Jones:** We looks like we have some protection circuitry in there. Now, somewhat surprisingly, this actually looks quite decent. It looks like it's got uh at least a couple of devices on there.

**Dave Jones:** So, a couple of the probably a couple of MOSFETs and a controller in there would be my guess. And uh so it's quite surprised in this FA [ __ ] battery.

**Dave Jones:** There we go. Tada. Let's have a look at what we got here. And I'm looking through my beautiful Mantis Elite microscope here. It's really a gem. It does work.

**Dave Jones:** It's sometimes a bit tricky to uh get on video here, but there you go. There's a 8 pin device, an 8230C. Uh little bit hard to Google that one, but I came up with an IR uh H8230C 9.4 amp 200V.5 ohm end channel MOSFET.

**Dave Jones:** And that's exactly what I expected in there. And there's a six pin SOT 23. You can't really read the markings on that. And even if I did, it probably wouldn't tell us much.

**Dave Jones:** Um, it'd be very difficult to find out what that device is. And this one here, we'll have to flip it around, but it's an 8205A. And I Googled that and what popped up was a uh Seikko brand uh battery management um IC and I thought, oh, bingo.

**Dave Jones:** Got it. um you know it's a multi-ell uh battery protection uh chip that you know detects over charge and over discharge and all that sort of stuff. Um but it's not the same because it is that was a 16 pin package and this one is only a little eight pin package.

**Dave Jones:** So um anyway uh something's wrong there. I reckon we've got a little uh six pin controller, two uh different MOSFETs. This one's an N channel. This one would be a P channelannel MOSFET.

**Dave Jones:** And uh they've, you know, they've done a decent job there. That is a proper battery protection board. So there you go. The FA [ __ ] battery um actually has decent protection built in.

**Dave Jones:** Go figure. I'm as surprised as you are. Now, next one here is from Russia. Hi to all my viewers in Russia. This is awesome. And uh it comes from male.

**Dave Jones:** I won't even try and pronounce that last name. But uh thank you very much male. Very good uh uh Russian name there. From Moscow with a K. Is that how people from Moscow spell Moscow in English?

**Dave Jones:** I don't know. Interesting. And uh down here, let's put it to Australia. And then I presume that is Russian for Australia. I can only presume. Excellent. Didn't know that.

**Dave Jones:** stamps. Check it out. There's Russia 2009. I have no idea what it says up the top, but there's obviously some sort of domed uh sort of, you know, building there with a dome on it.

**Dave Jones:** Looks pretty important somewhere in Russia, presumably. So, cool. Thank you very much. Let's open it up and have a look. All right. Have we had something from Russia before?

**Dave Jones:** I don't think so. By the way, um I do like postcards. So, if you want to send in postcards, by all means, send me postcards. It's flat. So, this is going to be interesting.

**Dave Jones:** What do we got here? Hello. Martini Gold, a new taste. What? What have we got here? I should read the note. Let's read the note first. Hang on. No, there.

**Dave Jones:** Oh, yes, there is. Here we go. Tada. Hello there from Soviet Russia. This is male from zepptobars. There you go. Check them out. I am working on my own microcontroller, but there is still a long way till I would have pre-production chips for you.

**Dave Jones:** So, this time I am sending multimedia package from special edition of Playboy magazine. So, you can tear it down right now. By the way, it geeks found out how to flash working Linux there.

**Dave Jones:** So, when this magazine came out, geeks were buying all out special Playboys across the Moscow. Sellers were probably slightly surprised. Oh boy. Oh dear. Oh dear. Oh dear. Let's have a look.

**Dave Jones:** What is this? Oh. Oh, it's one of these electronic cards. It's playing. Uh. Uh-oh. Right. Yeah. I don't think we should play this any further. I'm a bit concerned.

**Dave Jones:** This is awesome. This is like a full-on video card. Sorry about the reflection there. Well, I'm like, well, my fears were unfounded. This is like literally just an ad.

**Dave Jones:** It's a multimedia ad which they put inside the Playboy magazine, too. And it's got a built-in graphic screen, everything. It's reflective. You can see me. And that's just incredible.

**Dave Jones:** The circuit board is underneath here. And uh we're going to have to tear this thing down. I that that has got tear down Tuesday written all over it. So, I'm going to save that.

**Dave Jones:** Thank you very much, ma. I'm going to save that for a tear down Tuesday. Definitely don't want to waste that on a mailbag. That's just freaking awesome. All right.

**Dave Jones:** Jeez, all this stuff to tear down. Oh, man. I wish I could do it on the mailbag, but really, we don't have time. I got to get uh through the mail here.

**Dave Jones:** And if you want to send me stuff, send it to that crazy Aussie bloke, P Box 7949, Bulham Hills, BC, New South Wales 2153, Australia, not Austria. This one doesn't need Australia on it because it's Australia Post.

**Dave Jones:** There it is. Comes from Australia. So, looks like it comes from Dandong in Victoria. Excellent. And uh no name. There you go. Nothing. So, let's rip it open. They've got one of these lift and pull tabs.

**Dave Jones:** [Music] Tada. What? Oh god, a whole bunch of stuff in here. What do we got, man? Looks like there's no Is there a note? Hi Dave. Just stuff that may be of use.

**Dave Jones:** Parts. Cool. Still no name. That's awesome. Just random stuff. All right. Random boards. Thank you very much. Oh, big Spartan device on there. We'll have a look at these.

**Dave Jones:** So, let's open them up. They're random. What are they? Okay, they're some sort of plug-in moduly thing. And uh just that's a big BGA. And yeah, lots of random modules from something he doesn't say.

**Dave Jones:** We've got uh some memory memory and some plug-in boards. And this one's from Cisco Systems. Copyright 2000. It's reasonably old. So, some sort of Cisco networky type controller. We've got a massive BGA here.

**Dave Jones:** We've got a PLCC up here. A couple of uh large pin count quad flat packs and the XYlinks uh what's that? It's a XCV50 and a couple of unpopulated footprints here.

**Dave Jones:** Presumably some sort of memory. Some DC toDC converter stuff down here. And it's designed to plug into something. So, it's maybe some sort of add-on board or controller board.

**Dave Jones:** And the main device is a Conexent. and I hadn't heard of them before, but uh Google them and they're a spin-off of uh the old Rockwell uh group apparently.

**Dave Jones:** So, um yeah, they do uh you know, custom uh LSI devices like this um audio uh video and you know, compression and all that sort of uh stuff. So, you know, it's some sort of uh it's an edge stream.

**Dave Jones:** It's a VP uh224A. And if you Google that, you just get a whole bunch of those, you know, online Asian Chinese suppliers. There's no data sheets, no nothing that I could easily find.

**Dave Jones:** So there you go. And uh these other boards, um I'm not sure what they're actually out of. Some sort of Cisco systems thing, but uh these might be useful for uh I don't know, scrapping some parts out of or something like that.

**Dave Jones:** Not terribly exciting. I'm not uh going to go into it too much. Some sort of controller E1 uh controller. Yeah, a network E1 network connection. Something like that perhaps.

**Dave Jones:** I'm I'm not sure. Not really up on all that sort of stuff. Thank you very much anonymous person for sending in some random boards. And the last one for today is a box.

**Dave Jones:** I love boxes like this. Beautiful. Doesn't fit in my PO box, though. So, I get a little card and I've got to go to the counter and actually pick the thing up.

**Dave Jones:** Um, and it's from the United States of America from Steven Galant. Thank you very much, Stephen. He's from Kohl's in California. I've been to Koh'sbad and um uh they got a pretty horrible rocky beach there from what I remember.

**Dave Jones:** And I got food poisoning at the Cooh's bad Hilton Hotel that ruined my entire trip to the US. knocked me out for two weeks. Bloody Hilton Hotel. I think it was a dodgy chicken.

**Dave Jones:** So, anyway, let's open this sucker up. And uh so, thank you very much, Steven. The uh I never got to the uh Lego world. I think there's Legoland in Cooh's bad in uh California.

**Dave Jones:** Never got there. I started my road trip from uh Carl'sbad and I went all the way up to uh uh all the way up to Silicon Valley. So up uh Highway One.

**Dave Jones:** Tada. Here we go. We have a letter. Hi Dave. Saw your mail segment. A bit of skydive gear to control your camera. So as with my AAD was just reached the end of his life and decided to send it to you.

**Dave Jones:** It's an AAD. Of course it will probably continue to work for some time. Older designs use gas filled tubes, mechanical gain, and springs to move the reserve parachute release pin.

**Dave Jones:** Interesting. An example is the FXC model 12,000. 12,000. God. The modern AAD device such as the Cypress Cybernetic parachute release system. Cool. Use an MPU and electrical charge to fire a cutting blade to cut the reserve parachute pin loop.

**Dave Jones:** This releases the spring-loaded pilot shoot that attracts extracts the reserve. Wow. I thought I had no idea. I I'm not into uh skydiving. I you know, I'd much rather fly the perfectly usable plane than uh jump out of it, but uh I can certainly appreciate it.

**Dave Jones:** Um and I had no idea that there were electronics or mechanical things controlling the reserve parachute pin. I just thought it was a, you know, well, I thought there was just a manual pin which you just pulled out and your reserve shoot came out.

**Dave Jones:** Seems to be more complex than that. Maybe I can take it apart. Look for a manual on the internet. Cool. Anything else in there? No, that's it. This is the uh box from Digi Key.

**Dave Jones:** Of course, this is the famous Digi Key uh shredded material. And anyway, got lots of static there when you pull off sticky tape from this. So, once again, I've got another tear down Tuesday item.

**Dave Jones:** I'm not going to do it on the mailbag. God. Anyway, this is Jeez, that's that's pretty heavy part of the heavy part of the kit. So, I assume we got to find a manual.

**Dave Jones:** So, that's some sort of that's some sort of pin. It's got some wires going to it. And there's a button. Right. Wrong. Little dude with his uh little parachuters dude there with his hat on.

**Dave Jones:** Brilliant. Right or wrong. Yeah. Well, some people say jumping out of a plane is wrong, but uh I'll do it one day. Be fun. And uh Cyprus. There you go.

**Dave Jones:** Made in Germany. Hi to all my German viewers. Brilliant. We'll have to look up the uh manual for that one. Manufactured 7th month 99. So, it uh is reasonably old.

**Dave Jones:** But there you go. It It will certainly be worth a tear down. Okay, let's try and get this thing to do something. I'll follow Steven's instructions in here. Click the button when it red lead lights.

**Dave Jones:** There we go. Press it again. No. Yeah. Press it again. Three. Four. And we got a countdown. Look at that. And what happens does something here. It cuts the something activates presum like there's a cutter in there that I assume your cord you shoot your cord goes through that and uh it actually cuts it.

**Dave Jones:** I presume that's what Steven's implying here. It releases it cuts the fires a cutting blade to cut the reserve parachute pin loop. Oh, what? Terribly disappointing. A what? Well, I've downloaded the user guide for this thing.

**Dave Jones:** So, let's take a look at it. And here it is. Design philosophy. The Cyprus device. Cypress, which is the acronym for cybernetic parachute release system, is an automatic activation device which meets all the needs and wishes of today's sky divers.

**Dave Jones:** Once it's installed, you can't hear it. You can't feel it and you can't see it. Aha. Operation is quite simple. Just switch it on in the morning prior to the first jump and then forget about it.

**Dave Jones:** It's not necessary to switch it off. Do it itself. The weather is constantly checked by Cyprus over the day, measuring the air pressure twice a minute. This means that the unit is always calibrated to the precise ground level.

**Dave Jones:** Well, you'd hope so. It's an emergency activation device that activates your reserve shoot presumably just before you uh go splat. So uh expert Cyprus is designed in such a way that won't restrict a sky diver in any way.

**Dave Jones:** Even with extreme maneuvers during exit and in freef fall, it'll cope with it. What whatever you can think of under canopy like stalls, spiral turns, down planes. Oh, these all sound fun.

**Dave Jones:** Excellent. It won't interfere with any normal activities. Only freef fall. Here we go. Only freef fall in very low altitude will cause the Cyprus to take action. In this situation, Cyprus will activate the reserve approximately 4.5 seconds prior to impact.

**Dave Jones:** 1 2 3 4 splat. Well, jeez, that's not much time. I don't know how what uh how many feet that is. They they always work in feet, I think, these sky divers.

**Dave Jones:** Do they? I'm not sure. Is that the uh de facto standard unit? So, yeah. Four and a half seconds. Jeez. before you hit the uh the the ground and go splat.

**Dave Jones:** That's uh not much margin for error there. So, you'd want to be pretty confident that this thing is uh uh you know is actually calibrated. So, jeez 4 and a half seconds.

**Dave Jones:** And here we go. Here's the tech specs for this thing. It's uh I I think this is the model I've got. I don't know. It might be a newer one, but I I think it's pretty identical.

**Dave Jones:** uh working temperature range here + 63 to minus20 centigrade. Of course, you know, you're up high, it's it can get pretty cold up there. So, this thing is going to be designed really well.

**Dave Jones:** Ultra high reliability unit. So, this will make for an interesting uh tear down. It's completely waterproof uh to 1.5 uh m as well. Battery life is uh 500 jumps approximately 2 years.

**Dave Jones:** I would presume that uh it has like a lithium primary battery in there. That would uh be my assumption. And you got to change it every couple of years and it functions for 14 hours and then switches off because all it's got to do is read the sensors and things like that and uh you know me measure the altitude uh sensor and the speed um sensor and uh or if

**Dave Jones:** it's the same uh thing and it gets a rate of change and once you hit if you're going fast at where is it? Let's have a look down here.

**Dave Jones:** It activates activation altitude. There we go. Approximately 225 m or 750 ft. So, if you get to that altitude and you're still going at greater than or equal to 13 m/s or 29 mph, bang.

**Dave Jones:** It's going to, you know, it knows you're about to go splat. And I guess it doesn't want to kill itself either. So, uh, it's going to activate the reserve.

**Dave Jones:** Shoot. Jeez. if you haven't done that already, of course. So, this is like an emergency backup thing. So, it will actually cut that cord and activate your reserve chute.

**Dave Jones:** And hopefully, I don't know, can any sky divers out maybe uh Steven can tell us, you know, can you stop in 750 ft with your reserve shoot, which is smaller than normal, I believe.

**Dave Jones:** I guess you can. There you go. So this will actually be interesting because it's got an operational life here of total lifetime of 12 years from date of manufacturer plus 3 months maximum.

**Dave Jones:** Um so that it's designed for a 12 year operational life you know three or four battery changes or something like that. So this will be really high quality construction in here.

**Dave Jones:** You know, vibration proof, shockproof, you know, all sorts of, you know, designed for extreme temperature ranges and so it'll be a make for a really interesting tear down. Can't wait.

**Dave Jones:** Tear down Tuesday material. Definitely. Thank you very much, Steven from Cooh's Bad. Anyway, that's the mailbag all done and dusted. Got man more tear down Tuesday items than I can poke a stick at.

**Dave Jones:** Hope you liked it. Catch you next time. [Music]
