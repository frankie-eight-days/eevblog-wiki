---
video_id: kdtyxt9OLlU
title: EEVblog #465 - LED LCD Panel Teardown
url: https://www.youtube.com/watch?v=kdtyxt9OLlU
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 25, "3": 45, "4": 60, "5": 73, "6": 95, "7": 115, "8": 123, "9": 134, "10": 148, "11": 157, "12": 174, "13": 190, "14": 204, "15": 217, "16": 247, "17": 272, "18": 290, "19": 305, "20": 316, "21": 324, "22": 348, "23": 366, "24": 382, "25": 392, "26": 406, "27": 418, "28": 433, "29": 447, "30": 453, "31": 465, "32": 479, "33": 488, "34": 495, "35": 507, "36": 524, "37": 537, "38": 558, "39": 584, "40": 596, "41": 607, "42": 629, "43": 641, "44": 660, "45": 686, "46": 703, "47": 719, "48": 730, "49": 745, "50": 760, "51": 777, "52": 792, "53": 809, "54": 818, "55": 837, "56": 855, "57": 867, "58": 884, "59": 898, "60": 912, "61": 931, "62": 945, "63": 966, "64": 981, "65": 997, "66": 1021, "67": 1034, "68": 1049, "69": 1058, "70": 1072, "71": 1088, "72": 1098, "73": 1110, "74": 1132, "75": 1152, "76": 1167, "77": 1182, "78": 1195, "79": 1211, "80": 1222, "81": 1233, "82": 1246, "83": 1262, "84": 1276, "85": 1296, "86": 1308, "87": 1320, "88": 1335, "89": 1353, "90": 1377, "91": 1392, "92": 1406, "93": 1420, "94": 1436, "95": 1454, "96": 1471, "97": 1483, "98": 1501, "99": 1513, "100": 1524, "101": 1548, "102": 1559, "103": 1573, "104": 1600, "105": 1612, "106": 1625, "107": 1636, "108": 1655, "109": 1676, "110": 1689, "111": 1709, "112": 1722, "113": 1735, "114": 1753, "115": 1766, "116": 1777, "117": 1791, "118": 1803, "119": 1819, "120": 1837, "121": 1859, "122": 1871, "123": 1882, "124": 1888, "125": 1897, "126": 1911, "127": 1924, "128": 1945, "129": 1958, "130": 1978, "131": 1991, "132": 1998, "133": 2016, "134": 2030}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I thought we'd have a look at what's inside one of these LED LCD monitor panels. This is the one I got from the dumpster dive, 27 in absolutely massive.

**Dave Jones:** It was cracked as you saw in the previous dumpster diving video, but what's inside this thing? Well, we'll find out. And yes, look it is kind of warped there.

**Dave Jones:** Something yeah, seriously happened to this thing when that photocopier was or that laser printer was dumped on it during in inside the dumpster. What a bummer, but anyway, I've never actually taken apart one of these um LCD panels before really and this is a LED one.

**Dave Jones:** It hasn't got the cold cathode fluorescent lamp in it. So, it's going to have some pretty good LED strips and maybe you know a diffuser plate something like that some sort of diffusion technology to get a nice even backlight on the thing.

**Dave Jones:** So, I expect probably you know to I'm not sure they have it on all sides, but maybe on two sides like this they'll have some LED strips or something like that and diffuser plates and all sorts of stuff.

**Dave Jones:** So, let's uh crack this thing open or before we do have a look at the PCB here. And there's the main chipset on this thing. It's a CMOCM32716A. Not going to bother looking it up, but there's some uh series termination resistors there and that comes from the main connector which comes from the control board.

**Dave Jones:** So, that you know, that's the input and then this must fan out to all the other driver chips which then go into these um flat flex cables down here and there they're all soldered on with a hot bar technique.

**Dave Jones:** So, they come across with a hot bar down there and actually press down on these and they and it solders these flat flex strips down onto the board there.

**Dave Jones:** Very common technique for this sort of thing. So, let's Well, there's nothing much else on the board. There's a little uh low dropout rig there or something. There's something else here.

**Dave Jones:** That's a CMO CM502. I'm not even going to bother to look these up. Um not too fussy. I'm Oh, look at that. That looks interesting. Looks like that's been Ah, look.

**Dave Jones:** Has that fried? Has that been fried or has it been reworked? I don't know. Something's gone wrong there. Maybe that is what That's all that was wrong with this thing.

**Dave Jones:** I mean, it is actually uh shattered the panel, but that's maybe why it was originally dumpster dived or dumpster tossed to begin with. It's almost as if something's gone horribly wrong with that chip there.

**Dave Jones:** I think maybe that's uh died a very sad death. I think. So, maybe Yep, that's what the reason that this thing's been tossed out perhaps. Who knows? Anyway, let's not speculate about that.

**Dave Jones:** Some DC to DC converter stuff. Big inductor here. Lots of parallel uh caps here. Tons of them. Really getting the uh inductance down there and uh there's not much else on the board.

**Dave Jones:** So, let's take it out and flip it over. One of the interesting things though is this is a pretty darn long board. It's like 55 cm long. So, you know, um they they've really gone to town there.

**Dave Jones:** Of course, um you'd have no problems having this assembled through the assembly machine usually cuz length usually isn't a problem. It's usually height um inside, you know, certain width inside the pick and place assembly machine, but usually they can do any size length like this, but sometimes you will not some bare board manufacturers won't be able to make a panel that big and they interestingly I can't see any

**Dave Jones:** uh breakout tabs, V grooving or anything like that. That board looks fully routed on all edges. So, it looks like that just that individual board has gone through the pick and place assembly process or more likely they would have done like a well, it's a fully routed board and then they've done like a custom jig like they would have had like they would have you know, made a custom

**Dave Jones:** a plastic jig or something like that to hold the board in place and they would have had multiple channels like this. So, you know, maybe they had five boards stacked up like that and five boards then move their way through the pick and place assembly machine, but let's flip this sucker over and let's see what's on the bottom side.

**Dave Jones:** Well, that's surprising folks. Look at that, absolutely nothing on the back there. No extra drivers or anything like that. Just a whole bunch of a parallel a traces running the full length of this thing.

**Dave Jones:** So, a there's got to be some more circuitry on the back of this panel. That chip ain't going to handle everything folks. You know, I'm not actually sure which order to get this out.

**Dave Jones:** There were a couple of screws along the here, but that's it. There's no other screws like along the side down here. It seems to be held in place by some clips.

**Dave Jones:** So, sort of getting there and sort of lever it out and a it looks like should just pop out. Well, that's the a that's the plan anyway. Here we go, folks.

**Dave Jones:** Ta-da! Uh uh popped back in. Bummer. There it is. Uh got it. Finally. Aha! There's our white uh reflective back in. I would say or is that a No, I would have Well, yeah, white reflective.

**Dave Jones:** I guess they're not going to make it silver. So, that's so that the uh light reflects back evenly off the back of that. So, there we go. Yeah, but quite a nice So, I'm not sure what that is.

**Dave Jones:** Not sure what material that is. Probably has a high reflectivity. Be great for my white balance. I can set Actually, yeah, I might keep that. I'm assuming it's a pure white.

**Dave Jones:** It looks pure white to me. Could use that as a nice white balance card for my camera. That'd be neat. So, we have that and now we have Aha!

**Dave Jones:** And this has a nice I'll get the macro lens out out in a minute. You won't be able to see this, but that This has a nice back in on and this has an etched pattern on the back of it here.

**Dave Jones:** I can feel the etched pattern on it like little little dots they are. Tiny little dots and these are So, I still can't see the LEDs in here. Um which is really kind of unusual.

**Dave Jones:** There they are. Go. There we go. There's our LED strip all the way along the bottom. Should have known that. There's our connector. There we go. There's our LED connector and there's the LED strip all the way.

**Dave Jones:** So, it's only one side. I was I was wrong. I thought it'd be on both um edges, but it's all it's coming from the Is that the top or the bottom?

**Dave Jones:** I'm not sure now. Anyway, um it's just coming from the top or bottom. That's a really neat LED strip though. Um presumably, I'm going to do Oh, I'm going to take that out.

**Dave Jones:** Um they're obviously not going to be in Oh, are they in series? How many LEDs are on there? If you wire them in series, and you uh you know, 3 V per LED, that's going to be an awfully high voltage uh array.

**Dave Jones:** Otherwise, if they're parallel, they have to have a current sharing resistor, and I Oh, yeah. Yes. Oh, no. No, that's silk screen. I'll get in there with the macro.

**Dave Jones:** I thought I saw a current sharing resistor for each one, but there's not. I don't think it's on the bottom. So, I'm going to assume that they're all in series.

**Dave Jones:** Well, we can measure that later. That's going to be fun if it is. We'll get out the high voltage power supply, and power this sucker up. By the way, I didn't get the part number on this one.

**Dave Jones:** Made in China. It's a Chi Mei Optoelectronics brand panel. Whether or not it's you know, just a rebadged from one of the major manufacturers, I've got no idea. If you've got any details on that, I guess I could Google it, but I won't bother at the moment.

**Dave Jones:** If you do have any details on exactly who manufactured this and what plant, uh please leave it in the comments. So, this is our light guide, and these are, you know, fairly simple in terms of their construction.

**Dave Jones:** I'm not sure of the exact material, some sort of, you know, polycarbonate or something like that. Nicely machined edge here, which goes along the LEDs at the bottom here, and at the top, they've got a white strip on there, which is the same as the reflective strip which sits on the back here, which you saw before.

**Dave Jones:** This one here. So, here's our reflective strip. Sits on the back like that, and then of course, the light shines in here, and then it bounces off Well, due to total internal reflection, it acts as a light guide, and it's reflecting in and out in and out all the way it will bounce in off the top and bottom edges until it hits all these little dots on the top which we'll take

**Dave Jones:** a look at and they're the thing that actually reflects the light then out the front like this. And we can see that on this Dave CAD drawing here. We've got our LEDs at the side here this LED strip.

**Dave Jones:** This is our reflective film that white reflective film on the back. These are little dots. I presume they're like a chemical etched or something on the back of there.

**Dave Jones:** I'm not sure how they actually manufacture the tiny little dots on the back but anyway yeah this effectively works as a light guide so the light shines into here it'll be the correct thickness and they choose the correct angle led blah blah blah into get the total internal reflection in there as best they can so the light bounces all the way around in here and sometimes they'll hit these little dots here well

**Dave Jones:** a lot of the time they'll hit these little dots here and then the light goes out the front like that at various angles of course it doesn't just all magically go straight out like that and that's what produces the light coming out.

**Dave Jones:** So this is how they can get a an even light coming out across the whole panel from just an edge lit down here and there's multiple ways to do it with you know either you have ones on multiple sides or you have like all four sides but I think most of these days only use the one side like this.

**Dave Jones:** So that's effectively how these things work. Very simple but then you need some extra stuff on top of here to really like you need an extra diffuser plate and extra stuff on here as we'll no doubt see to then get a nice even diffused light out because otherwise if you just had this you'd actually see little bright you know spots you'd see all the dots if you don't have the

**Dave Jones:** diffuser plate and other technology which will be on on top of here. There you go you can see the little individual dots there. Absolutely tiny and yeah, as I said, I'm not sure how they're actually manufactured, whether they're you know, chemical etched, laser etched or you know, something else.

**Dave Jones:** I don't know. If you got any got any uh um info on how they actually manufacture those dots on there, please leave it in the comments. And then below that, we have a nice diffusion layer.

**Dave Jones:** Look at that. So, actually this is where a lot of the technology could be in this diffusion film here. You can see it, you know, it's it is quite diffuse.

**Dave Jones:** So, there could be more technology in this uh thin diffusion layer here than in this polycarbonate bit here. So, I don't know. If anyone has any exact details and stuff like that, please let us know.

**Dave Jones:** Oh, look, there's another Look at that. There's another very You can just see my fingers. Well, it actually turns up much better on camera. Looks like it has lots of magic in there.

**Dave Jones:** Tie me kangaroo down, sport. Tie me kangaroo down. This film is very interesting, folks. Look at this. At a really shallow angle like this, it is quite transparent. You can see my watch and my screwdriver through there.

**Dave Jones:** But, if I move it up to be directly vertical to it, it absolutely vanishes and as I bring it down the angle again, very shallow angle again, you can see it's transparent again.

**Dave Jones:** But, you bring it up, that's like 90° to it, completely opaque. Look at that. And that only works in the what I'll call the the Y direction here like this.

**Dave Jones:** If I actually spin it around on the X direction like that, it actually vanishes. No, that's not just a trick of the camera or the light reflection. I can't see that either.

**Dave Jones:** So, you go over the top and yeah, so in the X direction, it is only transparent at shallow Y angles like that. Interesting. So, it's no surprise that the LED strips are along this bottom edge like this.

**Dave Jones:** So, that is really quite fascinating. And no, it's not uh polarized if I, you know, uh move the, you know, watch around like that or anything like that. I did a quick little uh bit of research on this film stuff and uh it turns out it's called uh prism film or lens film.

**Dave Jones:** Or if you get it from uh 3M, who's the main uh patent holder on this stuff, it's called brightness enhancement uh film or BEF. And it's 3M micro replication technology.

**Dave Jones:** And it basically uh well, it says it recycles the off- axis light. So, as I said before, all this light, the light source, these are the individual dots down here that are, you know, uh shooting all this light out in multiple directions, it just helps channel that and improve and boost the brightness.

**Dave Jones:** Um if you only got one piece up to 60%, two pieces up to 120%. So, it it increases the brightness um as well as um you know, channeling it all directly outwards.

**Dave Jones:** As you can see, it improves brightness, contrast, uniformity, and energy efficiency. Very vital part of these LCD displays. And that's exactly how they work. Some of it gets recycled back depending on, "Oh, you're a bad angle.

**Dave Jones:** Sorry, you're coming back in." And some of it might even bounce outside the little prisms. And that explains why, by the way, that we could actually see through it at a shallow angle in this direction and this direction like this and of co- and we couldn't see anything in this direction because they're only manufactured in, you know, a long sheet like that.

**Dave Jones:** So, the direction Ooh, and we actually have some data as well. Here's the gain of it and you can see at the larger angles it just completely drops off like this either side of that.

**Dave Jones:** So, here you go. Those into all your light and optics uh physics stuff. You can have a field day with this and as I said 3M hold like a lot of the patents are on this stuff, but it seems that some of those are expiring so there's other manufacturers are coming into the play as well using their own technology and you can get different types of got a

**Dave Jones:** standard on the ears round tip wave, you know, and they all have various properties. I have no idea which this one is, but it is definitely one of these prism films or BEFs.

**Dave Jones:** And what's our final layer on here? Tada! So, we're not done yet. There we go. We have three layers of material. I'm not sure that's sort of that doesn't look to be that doesn't look like it does anything at all.

**Dave Jones:** Just maybe a little extra diffusion layer or something like that. Doesn't seem to be doing anything special. Anyway, so we've got three layers of diffusion, you know, slash you know, reflective reactive type of material plus our LED panel as well plus our light guide panel as well.

**Dave Jones:** So, absolutely fascinating construction of pretty much what I expected. I expected there to be a lot of technology in the in the LED diffusion of this. Yeah, here we go.

**Dave Jones:** Here's where we can see our cracked panel, folks. Hi. I can see myself. It's very reflective. There you go. And not sure if you can see those cracks. But yeah.

**Dave Jones:** Probably getting some of it in there, but yeah, it's cracked all up here. All the glass is cracked. Everything. Well, I shouldn't run my finger over that. Sorry. Yeah, all you Apple fanboys getting excited.

**Dave Jones:** Sorry, I'm not an Apple fan. This was given to me by a fan who came to visit the lab, who works at Apple. So, that's why I'm wearing it.

**Dave Jones:** And it's kind of it's all right. I like it, even though it is Apple. But, uh yeah, now we can see all our little individual pixels in there. But, we've got our cracked well and truly cracked glass panel.

**Dave Jones:** So, here we go. I can take out the plastic surround on that. Came out very nicely, but you can see how it's all You can probably see how it's all cracked.

**Dave Jones:** Yeah, you can see all the crack marks up there. And we saw that in the previous video, but yep. There's all our uh Here's there our tiny little driver chips.

**Dave Jones:** Well, they're actually huge driver chips, but uh uh tiny in size. The uh trace spacing down in there is incredibly small. But yeah, so we've got uh 1 2 3 4 5 6 7 8 for the uh uh X direction, and uh 1 2 3 over there for the Y.

**Dave Jones:** And it is interesting to note that there was no extra layer in there. That's it. That's the front uh That's the front panel of the thing. So, the actual panel itself is uh Oh, yeah, I can see the cracks in it now if I look at this panel at the right angle.

**Dave Jones:** There we go. You can see them all the way down there. So, this So, the actual LCD panel itself is uh the entire front surface. There's no way I I expected there to be an extra protective film on there.

**Dave Jones:** But, it's not. It's all It's all embedded and integrated. Although this film does seem to be an extra layer stuck on there. So, maybe I can attempt to peel that off.

**Dave Jones:** Perhaps. I don't know, but there's a lot of layers that go into the construction of these panels, let me tell you. They're uh Yeah. Yeah. Yeah, this could take a while.

**Dave Jones:** All right, here we go. I got it. I got it. There we go. That's the front. Uh protective film, some sort of polycarbonate. And yes, that is the top polarizing film.

**Dave Jones:** Check out my Fluke 87 as I turn it around. Ta-da, it vanishes. So, that's the top polarizing film. There'll also be a polarizing film on the bottom of the LCD as well.

**Dave Jones:** So, yeah, that extra layer on the top here, that'll also be the second polarizing filter on the back. And then, if we go in, we can start seeing all of our pixels.

**Dave Jones:** Fantastic. Look at that. Ah, beautiful. That's actually rather fascinating, folks. This is with my times 10 macro lens, and you can start to see the individual red, green, and blue pixels in there.

**Dave Jones:** And they would, of course, as this is a TFT screen, they'd all have their individual driver transistors. And then, all of this what looks like our purple stuff here, these are all the actual traces leading up to there.

**Dave Jones:** So, there's like, you know, 100 little traces in there going up to your individual um columns there. And there you go. That's one of the driver chips. Take a look at the trace spacing.

**Dave Jones:** I'll zoom in on that in a second, but those Yeah, there's They're all traces in there, folks. They're all traces. Look at them. All the traces coming out here, wrapping around, going up there, out of here, driving each individual uh column in this case cuz these are the uh X drivers.

**Dave Jones:** So, here you go. Novatek. And there's the part number on that sucker. And look at the traces. My times 10 macro lens is not good enough to get down there and look at those traces.

**Dave Jones:** I can see some of them. You can see some of them in here. This is where the uh data's uh coming in, probably. But all the output drivers for the individual pixels, nah.

**Dave Jones:** Can't see a damn thing. And it's not surprising, really, because if you do the math, uh there's eight of these chips um driving all of the columns. And of course, this is I believe this is a full HD uh 1920 by uh 1080 uh panel.

**Dave Jones:** So, we're talking 240 traces each one of those chips has to drive. Count them, folks. Uh I can just see them. Just. If you watch this thing in HD, you can probably just see the individual traces in there.

**Dave Jones:** That's insane. So, there you go. If I bring that in and out of focus, you can just see the individual traces. Absolutely tiny. Woo! And you can see how these flat flexes are all uh sandwiched inside the uh polycarbonate I presume uh polycarbonate uh layers or some such in there.

**Dave Jones:** You can see the traces going around there and then right up there to the row driver uh thing. Let's see if we can zoom in on that. So, you can really see those traces on the inside of the panel down in there.

**Dave Jones:** And then it comes up and there's our There's our row driver chip. You can just see the number down in there. I don't know. If you can find info on that, I'd be very surprised, but you never know.

**Dave Jones:** You never know what Google I One Anyway, I wonder who uh Novatek is. Whether or not they're just you know, manufacturing the uh flat flex assembly or whatever, or uh they have more to do with it.

**Dave Jones:** I don't know. And you might ask, "Well, what is that pattern up there doing?" Absolutely nothing, folks. I don't know. Maybe they're just doing some uh uh um equalization to put some extra copper in there.

**Dave Jones:** So, I don't know. It doesn't curl or do something else funny. I don't know. They've taken a few liberties there, that's for sure. And my first guess would have been that they are uh test pads, of course, but uh uh you can't uh access them because they got the film on top.

**Dave Jones:** So, um I don't know. Maybe um uh during the manufacturing phase before the final film is put on the uh top, perhaps. That's all I can think of. And if we have a look down in the bottom corner down here, check it out.

**Dave Jones:** You can see the individual traces going in, or it's actually it's really hard, but uh you can you can see the individual My screwdriver is massive here. See the individual traces running up.

**Dave Jones:** And we should be able to see the uh red, green, and blue individual uh TFT transistors. And there you go, folks. Looking through my uh microscope, really difficult cuz I've got my camera with the macro lens right up to the eyepiece of my microscope.

**Dave Jones:** Uh not fully equipped for this sort of stuff, but you can see the individual red, green, and blue pixels in there. Not a problem at all. Beautiful. There's more of them down in there.

**Dave Jones:** I've got to uh shine my torch right across this thing at a very shallow angle there to get this shot, but that's amazing. Look at that. There you go.

**Dave Jones:** That is the bottom corner of the panel. You can really see that quite clearly now. Individual red, green, blue filters and uh the driving transistors are all integrated. So, if you go into all the theory of how these TFTs actually work, and there's, you know, slightly different uh manufacturing uh uh processes and things between manufacturers.

**Dave Jones:** They all They're all going to have their own uh bit of secret sauce in there somehow, but you can see those traces coming in from the bottom there and then driving the uh the rows on the bottom there.

**Dave Jones:** It's It's on an angle. It's on a 45° angle here, of course. And uh but it it is rather It is rather fascinating. Oops, I've moved it. Let's just move across and uh There you go.

**Dave Jones:** Sorry about uh the movement here. I'm just trying to hold my camera and tripod in place while uh focusing this microscope. But that is incredibly interesting, folks. And on the front side of this, you can see that they've got some sort of blue gunk around the outside, whether or not that's sort of part of the bonding process for all the various uh layers, I'm not entirely sure.

**Dave Jones:** And on one corner of the panel here, look at that. Looks like we have some sort of test connector. Now, I won't actually go into detail on how the liquid crystal TFT panel itself actually works.

**Dave Jones:** There's plenty of tutorials and with great graphics and everything out there to explain the operation of these things. But and in terms of how the liquid crystals work and all that sort of thing.

**Dave Jones:** But basically what we've got is the diffusion plate at the back, the white light as we've seen. It generates like an even white light at the back of this panel.

**Dave Jones:** And then as we saw on the underside here, we have a polarization layer. So that actually creates polarized light light which then enters the TFT panel itself. And then the TFT panel, the individual pixels in there, red, green, and blue, they have red, green, and blue filters.

**Dave Jones:** Well, they're not the pixels. Three of those red, green, and blue elements make up one pixel or one picture element. And then when you apply an electric field across each pixel element, a red, green, or blue one of those, then you can individu ally turn on or off the polarization of the light passing through the individual red, green, and blue elements.

**Dave Jones:** And so you can actually block or allow the light to come through those red, green, and blue filters. And then we've got a final polarization filter on the top here.

**Dave Jones:** And then that's the light that ultimately comes out. You can turn on each of those things. So all it is is either allowing the light to come through from the backlight or not for each one of those 19 20 by 1080 for a full HD screen red, green, and blue picture elements.

**Dave Jones:** And it's you know, it's remarkable just the density in the technology in these panels. Absolutely phenomenal as you saw in terms of the trace spacing and things like that.

**Dave Jones:** Well, I tell you what, these LEDs seem to be very, very efficient, folks. They're uh uh incredibly bright. That's what just my multimeter uh diode tester uh doing that.

**Dave Jones:** You can really see the pattern emerging now. And that, too. Three just lit. But, that's absolutely incredible from my uh multimeter. And that LED board was quite a mongrel to get out, too.

**Dave Jones:** It was all stuck down with uh double-sided adhesive tape on there. And uh but, this is a very, very long board, folks. Just keeps going and going and going and going and going.

**Dave Jones:** That's one hell of a strip. And for those playing along at home, 61 cm long. And you can see the uh traces on the back of that. They've got a pattern on there.

**Dave Jones:** I soldered a couple of uh wires on here just so that we can uh have a go. There's basically two uh ground pins in there. Basically, plus uh four uh signal pins.

**Dave Jones:** And there we have it, folks. I've got one strip fully lit up. That's at 10 milliamps using my Keithley uh 225 current source. Let me uh put constant exposure on that.

**Dave Jones:** And let me uh change the wick a bit. Let's go down to That's eight, seven, six. That's one milliamp Oh, sorry. That's uh There we go. We're 1 milliamp there, folks.

**Dave Jones:** That's not much at all. I mean, let's even go down less than 1 milliamp. That is 0.1 milliamps. Should still be able to see that. And of course, if I turn my uh lab lights off, that might help a bit, but you can still see, hopefully, those lit up on camera there.

**Dave Jones:** And that's at 0.1 milliamps. Unbelievable. So, let's turn it all the way back up to 9.99 9.99 milliamps. And uh that is super duper bright. I like it. And uh of course, it takes a reasonable amount of voltage to do that.

**Dave Jones:** And uh but I can do that because I've got my uh I've got my Keithley current source over here, which I'll show you. So, of course, it's really handy having this uh Keithley current source.

**Dave Jones:** Not only can you dial in the uh constant current you want, but you can dial in the maximum voltage there as well. So, I don't know what the maximum current is.

**Dave Jones:** I mean, that is 10 milliamps, and that's quite bright, but obviously not bright enough to uh do the panel. If I had the data sheet for these things, I'd know.

**Dave Jones:** I mean, I can go up to that's 90 milliamps. That's pretty much uh the maximum that my Keithley uh current source can go up to, but that's incredibly bright.

**Dave Jones:** All right. So, what happens if I put 20 milliamps through this thing and then put on the light guide with the diffusion layer on there. Obviously, I haven't got everything lined up.

**Dave Jones:** It's not perfect. I'd have to put it all back in there. Eh, doesn't do much at all. That's pretty boring, actually. There's the uh backside of the diffusion layer down there.

**Dave Jones:** But yeah, anyway, I have to do some better uh experiments with this thing. I could like take out individual layers. So, if you want me to see it do it like a separate video on that, I uh I probably can cuz I I've now got uh all the stuff to experiment with that, and it could be rather interesting taking out the individual layers and seeing what effect

**Dave Jones:** they actually have on the uh on the total uh diffusion of this thing. So, anyway, that's a quick look inside one of these modern uh LCD uh monitors or one of these uh LED uh backlight ones.

**Dave Jones:** So, lots of technology in the uh diffusion layers and all that sort of stuff. That that technology has advanced a lot. If you remember sort of a notebook LCD screens from uh you know, many years ago, or not that many years ago, only 10 years ago or something, you know, you get the bright spots where you could see the Well, they didn't have LED technology back then, of course.

**Dave Jones:** They uh would have the um cold uh cathode uh stuff. But, you know, I mean, uh you would see the hot spots and everything on the side and it wasn't really nice and even and diffuse like these are.

**Dave Jones:** Um you know, you take for granted that uh you just get these nice diffuse things these days. Well, spare a thought for the technology that goes into all these uh layers and stuff.

**Dave Jones:** And if you do have data sheets on uh uh all this uh layer material and everything, please uh post it cuz that would be uh fascinating. And there's tons of technology, which of course, you know, 30 years of progress or something has gone into uh LCD technology like this.

**Dave Jones:** Just absolutely incredible. The tolerances and you know, full HD and uh it's just absolutely amazing stuff. But, anyway, I hope you liked that. And if you want me to play around uh with it some more, please let me know all this uh diffusion stuff.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum. If you like Teardown Tuesday, you know what to do. Catch you next time.
