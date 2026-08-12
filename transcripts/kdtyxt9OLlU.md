---
video_id: kdtyxt9OLlU
title: EEVblog #465 - LED LCD Panel Teardown
url: https://www.youtube.com/watch?v=kdtyxt9OLlU
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I thought we'd have a look at what's inside one of these LED LCD monitor panels. This is the one I got from the dumpster dive, 27 in absolutely massive. It was cracked as you saw in the

**Dave Jones:** previous dumpster diving video, but what's inside this thing? Well, we'll find out. And yes, look it is kind of warped there. Something yeah, seriously happened to this thing when that photocopier was or that laser printer was dumped on it during in inside the

**Dave Jones:** dumpster. What a bummer, but anyway, I've never actually taken apart one of these um LCD panels before really and this is a LED one. It hasn't got the cold cathode fluorescent lamp in it. So, it's going to have some pretty good LED strips and

**Dave Jones:** maybe you know a diffuser plate something like that some sort of diffusion technology to get a nice even backlight on the thing. So, I expect probably you know to I'm not sure they have it on all sides, but maybe on

**Dave Jones:** two sides like this they'll have some LED strips or something like that and diffuser plates and all sorts of stuff. So, let's uh crack this thing open or before we do have a look at the PCB here. And there's the main chipset on this

**Dave Jones:** thing. It's a CMOCM32716A. Not going to bother looking it up, but there's some uh series termination resistors there and that comes from the main connector which comes from the control board. So, that you know, that's the input and then

**Dave Jones:** this must fan out to all the other driver chips which then go into these um flat flex cables down here and there they're all soldered on with a hot bar technique. So, they come across with a hot bar down there and actually press

**Dave Jones:** down on these and they and it solders these flat flex strips down onto the board there. Very common technique for this sort of thing. So, let's Well, there's nothing much else on the board. There's a little uh low dropout rig there or something.

**Dave Jones:** There's something else here. That's a CMO CM502. I'm not even going to bother to look these up. Um not too fussy. I'm Oh, look at that. That looks interesting. Looks like that's been Ah, look. Has that fried? Has that been fried or has it been

**Dave Jones:** reworked? I don't know. Something's gone wrong there. Maybe that is what That's all that was wrong with this thing. I mean, it is actually uh shattered the panel, but that's maybe why it was originally dumpster dived or dumpster tossed to

**Dave Jones:** begin with. It's almost as if something's gone horribly wrong with that chip there. I think maybe that's uh died a very sad death. I think. So, maybe Yep, that's what the reason that this thing's been tossed out perhaps.

**Dave Jones:** Who knows? Anyway, let's not speculate about that. Some DC to DC converter stuff. Big inductor here. Lots of parallel uh caps here. Tons of them. Really getting the uh inductance down there and uh there's not much else on

**Dave Jones:** the board. So, let's take it out and flip it over. One of the interesting things though is this is a pretty darn long board. It's like 55 cm long. So, you know, um they they've really gone to town there. Of course, um you'd have no

**Dave Jones:** problems having this assembled through the assembly machine usually cuz length usually isn't a problem. It's usually height um inside, you know, certain width inside the pick and place assembly machine, but usually they can do any size length like this, but sometimes you will

**Dave Jones:** not some bare board manufacturers won't be able to make a panel that big and they interestingly I can't see any uh breakout tabs, V grooving or anything like that. That board looks fully routed on all edges. So, it looks like that

**Dave Jones:** just that individual board has gone through the pick and place assembly process or more likely they would have done like a well, it's a fully routed board and then they've done like a custom jig like they would have had like

**Dave Jones:** they would have you know, made a custom a plastic jig or something like that to hold the board in place and they would have had multiple channels like this. So, you know, maybe they had five boards stacked up like that and five boards

**Dave Jones:** then move their way through the pick and place assembly machine, but let's flip this sucker over and let's see what's on the bottom side. Well, that's surprising folks. Look at that, absolutely nothing on the back there. No extra drivers or

**Dave Jones:** anything like that. Just a whole bunch of a parallel a traces running the full length of this thing. So, a there's got to be some more circuitry on the back of this panel. That chip ain't going to handle

**Dave Jones:** everything folks. You know, I'm not actually sure which order to get this out. There were a couple of screws along the here, but that's it. There's no other screws like along the side down here. It seems to be held in

**Dave Jones:** place by some clips. So, sort of getting there and sort of lever it out and a it looks like should just pop out. Well, that's the a that's the plan anyway.

**Dave Jones:** Here we go, folks. Ta-da! Uh uh popped back in. Bummer. There it is. Uh got it. Finally. Aha! There's our white uh reflective back in. I would say or is that a No, I would have Well, yeah, white reflective. I

**Dave Jones:** guess they're not going to make it silver. So, that's so that the uh light reflects back evenly off the back of that. So, there we go. Yeah, but quite a nice So, I'm not sure what that is. Not sure what material that is.

**Dave Jones:** Probably has a high reflectivity. Be great for my white balance. I can set Actually, yeah, I might keep that. I'm assuming it's a pure white. It looks pure white to me. Could use that as a nice white balance card for my camera.

**Dave Jones:** That'd be neat. So, we have that and now we have Aha! And this has a nice I'll get the macro lens out out in a minute. You won't be able to see this, but that This has a nice

**Dave Jones:** back in on and this has an etched pattern on the back of it here. I can feel the etched pattern on it like little little dots they are. Tiny little dots and these are So, I still can't see the

**Dave Jones:** LEDs in here. Um which is really kind of unusual. There they are. Go. There we go. There's our LED strip all the way along the bottom. Should have known that. There's our connector. There we go. There's our LED connector and

**Dave Jones:** there's the LED strip all the way. So, it's only one side. I was I was wrong. I thought it'd be on both um edges, but it's all it's coming from the Is that the top or the bottom? I'm

**Dave Jones:** not sure now. Anyway, um it's just coming from the top or bottom. That's a really neat LED strip though. Um presumably, I'm going to do Oh, I'm going to take that out. Um they're obviously not going to be in Oh, are

**Dave Jones:** they in series? How many LEDs are on there? If you wire them in series, and you uh you know, 3 V per LED, that's going to be an awfully high voltage uh array. Otherwise, if they're parallel, they have to have a current sharing

**Dave Jones:** resistor, and I Oh, yeah. Yes. Oh, no. No, that's silk screen. I'll get in there with the macro. I thought I saw a current sharing resistor for each one, but there's not. I don't think it's on the bottom. So, I'm going to assume

**Dave Jones:** that they're all in series. Well, we can measure that later. That's going to be fun if it is. We'll get out the high voltage power supply, and power this sucker up. By the way, I didn't get the part number on this one. Made in China.

**Dave Jones:** It's a Chi Mei Optoelectronics brand panel. Whether or not it's you know, just a rebadged from one of the major manufacturers, I've got no idea. If you've got any details on that, I guess I could Google it, but I won't bother at

**Dave Jones:** the moment. If you do have any details on exactly who manufactured this and what plant, uh please leave it in the comments. So, this is our light guide, and these are, you know, fairly simple in terms of their

**Dave Jones:** construction. I'm not sure of the exact material, some sort of, you know, polycarbonate or something like that. Nicely machined edge here, which goes along the LEDs at the bottom here, and at the top, they've got a white strip on

**Dave Jones:** there, which is the same as the reflective strip which sits on the back here, which you saw before. This one here. So, here's our reflective strip. Sits on the back like that, and then of course, the light shines in here, and

**Dave Jones:** then it bounces off Well, due to total internal reflection, it acts as a light guide, and it's reflecting in and out in and out all the way it will bounce in off the top and bottom edges until it hits all these

**Dave Jones:** little dots on the top which we'll take a look at and they're the thing that actually reflects the light then out the front like this. And we can see that on this Dave CAD drawing here. We've got our LEDs at the side here this LED

**Dave Jones:** strip. This is our reflective film that white reflective film on the back. These are little dots. I presume they're like a chemical etched or something on the back of there. I'm not sure how they actually manufacture the tiny little dots on the

**Dave Jones:** back but anyway yeah this effectively works as a light guide so the light shines into here it'll be the correct thickness and they choose the correct angle led blah blah blah into get the total internal reflection in there as

**Dave Jones:** best they can so the light bounces all the way around in here and sometimes they'll hit these little dots here well a lot of the time they'll hit these little dots here and then the light goes out the front like that at various

**Dave Jones:** angles of course it doesn't just all magically go straight out like that and that's what produces the light coming out. So this is how they can get a an even light coming out across the whole panel from just an edge lit down

**Dave Jones:** here and there's multiple ways to do it with you know either you have ones on multiple sides or you have like all four sides but I think most of these days only use the one side like this. So

**Dave Jones:** that's effectively how these things work. Very simple but then you need some extra stuff on top of here to really like you need an extra diffuser plate and extra stuff on here as we'll no doubt see to then get a nice even

**Dave Jones:** diffused light out because otherwise if you just had this you'd actually see little bright you know spots you'd see all the dots if you don't have the diffuser plate and other technology which will be on on top of here. There

**Dave Jones:** you go you can see the little individual dots there. Absolutely tiny and yeah, as I said, I'm not sure how they're actually manufactured, whether they're you know, chemical etched, laser etched or you know, something else. I don't know. If you got any got any uh um info

**Dave Jones:** on how they actually manufacture those dots on there, please leave it in the comments. And then below that, we have a nice diffusion layer. Look at that. So, actually this is where a lot of the technology could be in this

**Dave Jones:** diffusion film here. You can see it, you know, it's it is quite diffuse. So, there could be more technology in this uh thin diffusion layer here than in this polycarbonate bit here. So, I don't know. If anyone has any exact details and stuff like

**Dave Jones:** that, please let us know. Oh, look, there's another Look at that. There's another very You can just see my fingers. Well, it actually turns up much better on camera. Looks like it has lots of magic in there. Tie me kangaroo down, sport. Tie me

**Dave Jones:** kangaroo down. This film is very interesting, folks. Look at this. At a really shallow angle like this, it is quite transparent. You can see my watch and my screwdriver through there. But, if I move it up to be directly vertical to it,

**Dave Jones:** it absolutely vanishes and as I bring it down the angle again, very shallow angle again, you can see it's transparent again. But, you bring it up, that's like 90° to it, completely opaque. Look at that. And that only

**Dave Jones:** works in the what I'll call the the Y direction here like this. If I actually spin it around on the X direction like that, it actually vanishes. No, that's not just a trick of the camera or the light reflection. I

**Dave Jones:** can't see that either. So, you go over the top and yeah, so in the X direction, it is only transparent at shallow Y angles like that. Interesting. So, it's no surprise that the LED strips are along this bottom edge like this. So,

**Dave Jones:** that is really quite fascinating. And no, it's not uh polarized if I, you know, uh move the, you know, watch around like that or anything like that. I did a quick little uh bit of research on this film stuff

**Dave Jones:** and uh it turns out it's called uh prism film or lens film. Or if you get it from uh 3M, who's the main uh patent holder on this stuff, it's called brightness enhancement uh film or BEF. And it's 3M

**Dave Jones:** micro replication technology. And it basically uh well, it says it recycles the off- axis light. So, as I said before, all this light, the light source, these are the individual dots down here that are, you know, uh shooting all this light out in multiple

**Dave Jones:** directions, it just helps channel that and improve and boost the brightness. Um if you only got one piece up to 60%, two pieces up to 120%. So, it it increases the brightness um as well as um you know, channeling it all directly

**Dave Jones:** outwards. As you can see, it improves brightness, contrast, uniformity, and energy efficiency. Very vital part of these LCD displays. And that's exactly how they work. Some of it gets recycled back depending on, "Oh, you're a bad angle. Sorry, you're coming back in."

**Dave Jones:** And some of it might even bounce outside the little prisms. And that explains why, by the way, that we could actually see through it at a shallow angle in this direction and this direction like this and of co- and we couldn't see

**Dave Jones:** anything in this direction because they're only manufactured in, you know, a long sheet like that. So, the direction Ooh, and we actually have some data as well. Here's the gain of it and you can see at the larger angles it just completely

**Dave Jones:** drops off like this either side of that. So, here you go. Those into all your light and optics uh physics stuff. You can have a field day with this and as I said 3M hold like a lot of the patents

**Dave Jones:** are on this stuff, but it seems that some of those are expiring so there's other manufacturers are coming into the play as well using their own technology and you can get different types of got a standard on the ears round tip wave, you

**Dave Jones:** know, and they all have various properties. I have no idea which this one is, but it is definitely one of these prism films or BEFs. And what's our final layer on here? Tada! So, we're not done yet. There we go. We

**Dave Jones:** have three layers of material. I'm not sure that's sort of that doesn't look to be that doesn't look like it does anything at all. Just maybe a little extra diffusion layer or something like that. Doesn't seem to be

**Dave Jones:** doing anything special. Anyway, so we've got three layers of diffusion, you know, slash you know, reflective reactive type of material plus our LED panel as well plus our light guide panel as well. So, absolutely fascinating construction of pretty much

**Dave Jones:** what I expected. I expected there to be a lot of technology in the in the LED diffusion of this. Yeah, here we go. Here's where we can see our cracked panel, folks. Hi. I can see myself. It's very reflective.

**Dave Jones:** There you go. And not sure if you can see those cracks. But yeah. Probably getting some of it in there, but yeah, it's cracked all up here. All the glass is cracked. Everything. Well, I shouldn't run my finger over that.

**Dave Jones:** Sorry. Yeah, all you Apple fanboys getting excited. Sorry, I'm not an Apple fan. This was given to me by a fan who came to visit the lab, who works at Apple. So, that's why I'm wearing it. And it's kind of it's all right. I like

**Dave Jones:** it, even though it is Apple. But, uh yeah, now we can see all our little individual pixels in there. But, we've got our cracked well and truly cracked glass panel. So, here we go. I can take out the plastic

**Dave Jones:** surround on that. Came out very nicely, but you can see how it's all You can probably see how it's all cracked. Yeah, you can see all the crack marks up there. And we saw that in the previous video, but yep.

**Dave Jones:** There's all our uh Here's there our tiny little driver chips. Well, they're actually huge driver chips, but uh uh tiny in size. The uh trace spacing down in there is incredibly small. But yeah, so we've got uh 1 2 3 4 5 6 7 8 for the uh

**Dave Jones:** uh X direction, and uh 1 2 3 over there for the Y. And it is interesting to note that there was no extra layer in there. That's it. That's the front uh That's the front panel of the thing. So, the

**Dave Jones:** actual panel itself is uh Oh, yeah, I can see the cracks in it now if I look at this panel at the right angle. There we go. You can see them all the way down there. So, this So, the

**Dave Jones:** actual LCD panel itself is uh the entire front surface. There's no way I I expected there to be an extra protective film on there. But, it's not. It's all It's all embedded and integrated. Although this film does seem to be an

**Dave Jones:** extra layer stuck on there. So, maybe I can attempt to peel that off. Perhaps. I don't know, but there's a lot of layers that go into the construction of these panels, let me tell you. They're uh Yeah. Yeah. Yeah, this could take a

**Dave Jones:** while. All right, here we go. I got it. I got it. There we go.

**Dave Jones:** That's the front. Uh protective film, some sort of polycarbonate. And yes, that is the top polarizing film. Check out my Fluke 87 as I turn it around. Ta-da, it vanishes. So, that's the top polarizing film. There'll also be a polarizing film on

**Dave Jones:** the bottom of the LCD as well. So, yeah, that extra layer on the top here, that'll also be the second polarizing filter on the back. And then, if we go in, we can start seeing all of our pixels. Fantastic.

**Dave Jones:** Look at that. Ah, beautiful. That's actually rather fascinating, folks. This is with my times 10 macro lens, and you can start to see the individual red, green, and blue pixels in there. And they would, of course, as this is a TFT

**Dave Jones:** screen, they'd all have their individual driver transistors. And then, all of this what looks like our purple stuff here, these are all the actual traces leading up to there. So, there's like, you know, 100 little traces in there

**Dave Jones:** going up to your individual um columns there. And there you go. That's one of the driver chips. Take a look at the trace spacing. I'll zoom in on that in a second, but those Yeah, there's They're all traces in there, folks.

**Dave Jones:** They're all traces. Look at them. All the traces coming out here, wrapping around, going up there, out of here, driving each individual uh column in this case cuz these are the uh X drivers. So, here you go. Novatek.

**Dave Jones:** And there's the part number on that sucker. And look at the traces. My times 10 macro lens is not good enough to get down there and look at those traces. I can see some of them. You can see some

**Dave Jones:** of them in here. This is where the uh data's uh coming in, probably. But all the output drivers for the individual pixels, nah. Can't see a damn thing. And it's not surprising, really, because if you do the math, uh there's eight of these

**Dave Jones:** chips um driving all of the columns. And of course, this is I believe this is a full HD uh 1920 by uh 1080 uh panel. So, we're talking 240 traces each one of those chips has to drive. Count them, folks.

**Dave Jones:** Uh I can just see them. Just. If you watch this thing in HD, you can probably just see the individual traces in there. That's insane. So, there you go. If I bring that in and out of focus, you can just see the individual

**Dave Jones:** traces. Absolutely tiny. Woo! And you can see how these flat flexes are all uh sandwiched inside the uh polycarbonate I presume uh polycarbonate uh layers or some such in there. You can see the traces going around there and then right up there to

**Dave Jones:** the row driver uh thing. Let's see if we can zoom in on that. So, you can really see those traces on the inside of the panel down in there. And then it comes up and there's our There's our row driver chip.

**Dave Jones:** You can just see the number down in there. I don't know. If you can find info on that, I'd be very surprised, but you never know. You never know what Google I One Anyway, I wonder who uh Novatek

**Dave Jones:** is. Whether or not they're just you know, manufacturing the uh flat flex assembly or whatever, or uh they have more to do with it. I don't know. And you might ask, "Well, what is that pattern up there doing?" Absolutely

**Dave Jones:** nothing, folks. I don't know. Maybe they're just doing some uh uh um equalization to put some extra copper in there. So, I don't know. It doesn't curl or do something else funny. I don't know. They've taken a few liberties

**Dave Jones:** there, that's for sure. And my first guess would have been that they are uh test pads, of course, but uh uh you can't uh access them because they got the film on top. So, um I don't know. Maybe um uh

**Dave Jones:** during the manufacturing phase before the final film is put on the uh top, perhaps. That's all I can think of. And if we have a look down in the bottom corner down here, check it out. You can see the individual

**Dave Jones:** traces going in, or it's actually it's really hard, but uh you can you can see the individual My screwdriver is massive here. See the individual traces running up. And we should be able to see the uh red, green, and blue individual uh

**Dave Jones:** TFT transistors. And there you go, folks. Looking through my uh microscope, really difficult cuz I've got my camera with the macro lens right up to the eyepiece of my microscope. Uh not fully equipped for this sort of stuff, but you

**Dave Jones:** can see the individual red, green, and blue pixels in there. Not a problem at all. Beautiful. There's more of them down in there. I've got to uh shine my torch right across this thing at a very shallow angle there to get this shot,

**Dave Jones:** but that's amazing. Look at that. There you go. That is the bottom corner of the panel. You can really see that quite clearly now. Individual red, green, blue filters and uh the driving transistors are all integrated. So, if you go into all the

**Dave Jones:** theory of how these TFTs actually work, and there's, you know, slightly different uh manufacturing uh uh processes and things between manufacturers. They all They're all going to have their own uh bit of secret sauce in there somehow, but you can see

**Dave Jones:** those traces coming in from the bottom there and then driving the uh the rows on the bottom there. It's It's on an angle. It's on a 45° angle here, of course. And uh but it it is rather It is rather fascinating. Oops, I've

**Dave Jones:** moved it. Let's just move across and uh There you go. Sorry about uh the movement here. I'm just trying to hold my camera and tripod in place while uh focusing this microscope. But that is incredibly interesting, folks. And on the front side of this, you can

**Dave Jones:** see that they've got some sort of blue gunk around the outside, whether or not that's sort of part of the bonding process for all the various uh layers, I'm not entirely sure. And on one corner of the panel here, look at

**Dave Jones:** that. Looks like we have some sort of test connector. Now, I won't actually go into detail on how the liquid crystal TFT panel itself actually works. There's plenty of tutorials and with great graphics and everything out there to

**Dave Jones:** explain the operation of these things. But and in terms of how the liquid crystals work and all that sort of thing. But basically what we've got is the diffusion plate at the back, the white light as we've seen. It generates like an even

**Dave Jones:** white light at the back of this panel. And then as we saw on the underside here, we have a polarization layer. So that actually creates polarized light light which then enters the TFT panel itself. And then the TFT panel, the

**Dave Jones:** individual pixels in there, red, green, and blue, they have red, green, and blue filters. Well, they're not the pixels. Three of those red, green, and blue elements make up one pixel or one picture element. And then when you apply

**Dave Jones:** an electric field across each pixel element, a red, green, or blue one of those, then you can individu ally turn on or off the polarization of the light passing through the individual red, green, and blue elements. And so

**Dave Jones:** you can actually block or allow the light to come through those red, green, and blue filters. And then we've got a final polarization filter on the top here. And then that's the light that ultimately comes out. You can turn on

**Dave Jones:** each of those things. So all it is is either allowing the light to come through from the backlight or not for each one of those 19 20 by 1080 for a full HD screen red, green, and blue picture elements. And

**Dave Jones:** it's you know, it's remarkable just the density in the technology in these panels. Absolutely phenomenal as you saw in terms of the trace spacing and things like that. Well, I tell you what, these LEDs seem to be very, very

**Dave Jones:** efficient, folks. They're uh uh incredibly bright. That's what just my multimeter uh diode tester uh doing that. You can really see the pattern emerging now. And that, too.

**Dave Jones:** Three just lit. But, that's absolutely incredible from my uh multimeter. And that LED board was quite a mongrel to get out, too. It was all stuck down with uh double-sided adhesive tape on there. And uh but, this is a very, very

**Dave Jones:** long board, folks. Just keeps going and going and going and going and going. That's one hell of a strip. And for those playing along at home, 61 cm long. And you can see the uh traces on the back of that. They've got

**Dave Jones:** a pattern on there. I soldered a couple of uh wires on here just so that we can uh have a go. There's basically two uh ground pins in there. Basically, plus uh four uh signal pins. And there we have it, folks. I've got

**Dave Jones:** one strip fully lit up. That's at 10 milliamps using my Keithley uh 225 current source. Let me uh put constant exposure on that. And let me uh change the wick a bit. Let's go down to That's eight, seven,

**Dave Jones:** six. That's one milliamp Oh, sorry. That's uh There we go. We're 1 milliamp there, folks. That's not much at all. I mean, let's even go down less than 1 milliamp. That is 0.1 milliamps. Should still be able to see

**Dave Jones:** that. And of course, if I turn my uh lab lights off, that might help a bit, but you can still see, hopefully, those lit up on camera there. And that's at 0.1 milliamps. Unbelievable. So, let's turn it all the way back up to

**Dave Jones:** 9.99 9.99 milliamps. And uh that is super duper bright. I like it. And uh of course, it takes a reasonable amount of voltage to do that. And uh but I can do that because I've got my uh I've got my Keithley current source over

**Dave Jones:** here, which I'll show you. So, of course, it's really handy having this uh Keithley current source. Not only can you dial in the uh constant current you want, but you can dial in the maximum voltage there as well. So, I

**Dave Jones:** don't know what the maximum current is. I mean, that is 10 milliamps, and that's quite bright, but obviously not bright enough to uh do the panel. If I had the data sheet for these things, I'd know. I mean, I can go up to that's 90

**Dave Jones:** milliamps. That's pretty much uh the maximum that my Keithley uh current source can go up to, but that's incredibly bright. All right. So, what happens if I put 20 milliamps through this thing and then put on the light guide with the

**Dave Jones:** diffusion layer on there. Obviously, I haven't got everything lined up. It's not perfect. I'd have to put it all back in there. Eh, doesn't do much at all. That's pretty boring, actually. There's the uh backside of the diffusion

**Dave Jones:** layer down there. But yeah, anyway, I have to do some better uh experiments with this thing. I could like take out individual layers. So, if you want me to see it do it like a separate video on that, I uh I probably can cuz I I've now

**Dave Jones:** got uh all the stuff to experiment with that, and it could be rather interesting taking out the individual layers and seeing what effect they actually have on the uh on the total uh diffusion of this thing. So, anyway, that's a quick look inside

**Dave Jones:** one of these modern uh LCD uh monitors or one of these uh LED uh backlight ones. So, lots of technology in the uh diffusion layers and all that sort of stuff. That that technology has advanced a lot. If you

**Dave Jones:** remember sort of a notebook LCD screens from uh you know, many years ago, or not that many years ago, only 10 years ago or something, you know, you get the bright spots where you could see the Well, they didn't have LED technology

**Dave Jones:** back then, of course. They uh would have the um cold uh cathode uh stuff. But, you know, I mean, uh you would see the hot spots and everything on the side and it wasn't really nice and even and

**Dave Jones:** diffuse like these are. Um you know, you take for granted that uh you just get these nice diffuse things these days. Well, spare a thought for the technology that goes into all these uh layers and stuff. And if you do

**Dave Jones:** have data sheets on uh uh all this uh layer material and everything, please uh post it cuz that would be uh fascinating. And there's tons of technology, which of course, you know, 30 years of progress or something has

**Dave Jones:** gone into uh LCD technology like this. Just absolutely incredible. The tolerances and you know, full HD and uh it's just absolutely amazing stuff. But, anyway, I hope you liked that. And if you want me to play around uh with it

**Dave Jones:** some more, please let me know all this uh diffusion stuff. And if you want to discuss it, jump on over to the EEVblog forum. If you like Teardown Tuesday, you know what to do. Catch you next time.
