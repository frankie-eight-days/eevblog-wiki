---
video_id: w0XTHBN-IIg
title: EEVblog #1239 - Mailbag
url: https://www.youtube.com/watch?v=w0XTHBN-IIg
source: youtube-asr
---

**Dave Jones:** Hi, and welcome to everyone's favorite segment, mailbag. Let's get right into it. Hi to all my Spanish viewers in Madrid in particular. And this one's Alvaro Sel- Selma? Selma? Something like that. But let's crack it open. And see what we got in here. We have a

**Dave Jones:** plug pack. Do we want to do a teardown on the plug pack? Problem is Oh no, this one you can open. Well, I was going to say the problem with plug packs is that you usually can't open them. Usually they're

**Dave Jones:** ultrasonically welded shut or glued shut. And you've got to get the Dremel out or you've got to like crack them. You can You can actually in some cases like you know, tap them with a hammer or whatever or screwdriver and and crack

**Dave Jones:** them open that way. But it's got one of those funny Yankee plugs on it. What's this about? Congrats on building such a great channel. Thank you very much. It's a thank you to all my viewers who have built the channel, really. Um

**Dave Jones:** yeah, I make the content, but nobody watches. It's not really a channel, is it? If somebody makes videos on YouTube and nobody watches, are they really there? I sent you a garbage PSU that's touted as a switch mode power supply, but

**Dave Jones:** actually resets brownout my Atomic Pi board as soon as it draws 1.5 amps. Yeah, um took some measurements with the IR thermometer. Some components got up to 140° C. Wow. The closed case can go up to 95° C. Too hot to That's Yeah, that's

**Dave Jones:** insane. Like you'll burn yourself. Let's do a quick 2-minute teardown of a dodgy power supply. I'll also link in at the end, if I remember it, a teardown of like an Apple fake Apple power supply or reverse engineer a fake Apple power

**Dave Jones:** supply. And that's That's a really interesting video. It shows, you know, how cheap they can make those supplies and kind of sort of get away with it. Mary King Enterprises sounds legit. AD 1805B for those playing along at

**Dave Jones:** home. Uh 13.5 W maximum. Yeah, I'm just set to I they tell you 5.15. Very uh common to set uh 5 W supplies to a greater than that, either 5.25 or 5.15 or something over 5 W just to uh compensate for the drop in

**Dave Jones:** the no doubt dicky leads in this thing. As I said, quite uncommon to find screws in this thing. So, it's only got two. So, presumably yep, that's going to lift up. Here we go. Oh, we're in like Flynn. Oh, doesn't

**Dave Jones:** that look crusty? Look at Oh, I was going to say, is that Oh, yeah, they've they've got a cut out in there. I was going to say, is that like squished on top of that? Wow. Somebody's got in there with a file. And

**Dave Jones:** have they? Yep. That's hilarious. So, we've got our mains input here. There's our bridge rectifier. Up. Hello. It's only three. W- Where's the Where's the fourth one? Um Bueller? Bueller? Anyway, Elite brand main DC filter cap. Is that a bit I don't know. Thought that

**Dave Jones:** was a bit puffy there. Maybe not. Uh QC passed by F. That's You don't want to see that. Which Which tester are you? Oh, I'm F. That's terrific. Is there any any little bulge in that? Maybe. Maybe a slight

**Dave Jones:** bulge in that. I reckon she's on the way out. Actually, I'm very surprised they bothered with the silastic down there. I'm just Why put it right there? I'm not sure. Uh but they got to round the cap just to

**Dave Jones:** stop it flapping around in the breeze. And well, it's actually fused as the brown wire coming over. That's actually a heat shrink um M 205 I'm sorry, yeah, an M20 Is that No, 3AG fuse. Wow. Well, I'll tell you what,

**Dave Jones:** I've seen worse than this. So, it's like typical of what you'd expect in a cheap One Hung Low brand plug pack. They got decent separation between the primary and the secondary there. No slot cutouts, but you know, that's okay.

**Dave Jones:** There's the beer optocoupler down the bottom there. Yep, there she is. That'd be a One Hung Low brand, too. Whatever they could get at the Shenzhen market that week. And those caps, I don't know the brand cuz it's on the

**Dave Jones:** other side, but bulgy, there you go. There's one of your problems. So, yeah, they just got too hot under the collar, literally, under that heat sink there. A little bit of folded metal work, just soldered down. So, you know, it's only

**Dave Jones:** flapping around in the breeze a little bit. Didn't bother soldering down the other side. Nah, no worries. What what would your vibration resonant mode be on that? See, you know, like you're designing something like this for a professional application. If you had

**Dave Jones:** to have it for whatever reason, flapping around in the breeze like that, you would put a little accelerometer on there, and then you'd, you know, sweep this over the entire vibrational frequency range, based on what type of transport you've got, you know, whether

**Dave Jones:** it's going by plane, rail, road, or air, or whatever. And cuz there are different standards for different types of transports, by the way, in case you didn't know. I don't remember the standards off the top of my head

**Dave Jones:** anymore, but yeah, oh. No, yeah, it had it has a little tab down in there, but it's not soldered down, so it's only in the one location. And then you put a little low-mass accelerometer on there, and shape this thing and in multiple

**Dave Jones:** axes, and you try and find the vibrational mode of that to see if it's going to be an issue. And given that we're already off on that tangent, if you want to know what one of those accelerometers look like, I've still got

**Dave Jones:** a couple. PCB Piezotronics is one of the big players in the market, and this is one of the little low mass accelerometers. These are an ICP type so you've got to have a basically a constant current supply for

**Dave Jones:** the thing. I might maybe you know, thumbs up if you want me to do a video looking at these little accelerometers. Anyway, there's a little accelerometer weighs bugger all and you can actually often you will just actually superglue

**Dave Jones:** these down to the surface like that and you can even get smaller ones from these because you don't want the mass of this plus your cable to upset the resonant mode and you know, stuff like that. Anyway, the cables on these are very

**Dave Jones:** cool as well. Little tiny low mass low tri-ball electric effect too by the way and these of course can come with like calibration sheets. I don't does this one have it? Oh yeah, this got some caliber completely faded calibration data.

**Dave Jones:** Anyway, you can get these with calibration sheets which uh give you the exact value and the uh response as well over the give a given frequency range. So anyway, uh give me a thumbs up if you want me to do a separate video let's

**Dave Jones:** making a little power supply cuz I don't think I have a power supply for it. Anyway, a little constant current thing with just like an AC tap off to get the signal out and maybe we can go all old

**Dave Jones:** school and use my old HP dynamic signal analyzer and get some responses of that and like coherence responses because you often like you'll put this on here as well and you'll put another one on your platform and then

**Dave Jones:** you can actually get a what's called a coherence plot which shows basically how much of the vibration in here is due to the original vibrational signal and you know, there's there's all sorts of cool stuff you can do. So anyway, I

**Dave Jones:** from memory what's a decent coherence value? Like you know, point nine five you're doing pretty well, I think. So yeah, we could uh power this up and put a load on it and stuff like that. But, you know, these

**Dave Jones:** output caps are clearly starting to go. So, the ESR, the uh equivalent series resistance or internal resistance uh rises. So, you get heating up in those, which accelerates the effect of drying out the electrolyte in there, and everything warms up, and it's yeah, it's

**Dave Jones:** I don't know whether or not that is I I'm not going to like plot the efficiency and all sorts of stuff. I I don't know. It's just par for the course in these cheap-ass power supplies. Actually, wow, I'm surprised. There's a

**Dave Jones:** There's a decent amount of copper in that. They They didn't skimp. Okay, I'll power it up. Here we go. 5.23. Okay, let's put 1.5 amps on it. 5.3. Jumped up to 5.3 volts. Oh, that's not very good. Let me get the thermal

**Dave Jones:** camera. Okay, that's just on idle there, and um the emissivity is going to uh it suck a bit with the uh aluminum thing. But, anyway, right down you know, we're talking 45 46 just sitting there. And if we put on our 1.5 amps, let's see

**Dave Jones:** if she starts getting hotter. So, it's the main primary side switcher there that's getting hot. 120 on the on the secondary side there. Sorry if you can't Sorry about any glare. But, uh yeah, that primary side That's uh 174.

**Dave Jones:** Uh 174° that got up to. It's cooling down now. I've turned off the Now, I can smell it. Oh, no. Uh wish this was Smell-O-Vision. Anyway, thank you, Alvaro, for sending that in. It's uh yeah, not terrific. But, uh you

**Dave Jones:** know, these plug packs, they're just built down to a price, and often the thermal uh performance isn't great. Not quality components in there. Over time, they die, and they'll just uh they're Got one from Australia. Thank you very

**Dave Jones:** much, uh Kievers. I Kangaroo Valley here in uh New South Wales. So, let's crack it open. Anyway, let's straight through the tab at the front there. Hi Dave, I saw this going in the dumpster at work and thought it might

**Dave Jones:** make a good 2-minute teardown. Excellent. So, this was going Let's see what was going into the dumpster. In its original box, by the looks of it. I guess nobody wanted anymore. Um mobile rack to serial ATA. Ah, Jay, yeah, I got

**Dave Jones:** one of those. There's not much in them. There's just like a um uh for serial ATA? Yeah. Okay. No, I had one for an IDE one or something like that. There's not much in them. 2-minute teardown. So, I'm sure a

**Dave Jones:** lot of people are familiar with these. These are It's just a serial ATA interface. It's got a cage like this. Your hard drive just uh screws in there like that, and there's your uh ATA interface down there, and uh we've got a

**Dave Jones:** bit of insulating tape on the back there, and not much else. Just goes over to a custom non-standard uh pinout here on a nice, um you know, the old uh kind of like Centronics type uh parallel interface. Nice big reliable uh you

**Dave Jones:** know, board-to-board interconnect thing. That just goes straight in there. There's a little little fiddly piss-ant fan in that thing. Oh, jeez, that'd be horrid, wouldn't it? That'd wear a bit, and up to yeah, signal integrity be damned, of

**Dave Jones:** course. They don't care. None of that uh controlled impedance rubbish. Just goes straight over. Yeah, because it's not an IDE to SATA interface. So, this is just purely a connector interface. With, you know, they don't care about uh your

**Dave Jones:** controlled impedance cuz these are quite high bandwidth um the serial SATA connections. And no, they don't I I think they care there. That's just a that looks like double-sided board to me. No ground plane in there. So, none

**Dave Jones:** of that strip line controlled impedance rubbish. So, it just goes straight over. It's pretty how you doing. But, someone really wanted their hot snot in there. This one, I'm not sure who it's from. Electronic Samples from Landmark Global

**Dave Jones:** in UK. All right, so some company's obviously sent me something pretty how you doing packaging. Trust they wanted There there, I don't think there's much padding in this thing. Um it's it's really dodgy as. Wow. Oh, look at this.

**Dave Jones:** Car stereo. That's a 2-minute teardown. What What What brand is that? CD changer compatible Is that like a a one hung low brand? Audio Ford audio system. Okay, it's a genuine Ford stereo car stereo. 2-minute teardown. It's a Visteon Ford audio

**Dave Jones:** system 6000 NE. For those playing along at home, probably suitable for 2-minute teardown. Some viewers in Europe may recognize this unit as a type uh were very common in early Ford cars manufacturing '97 to 2006. Unfortunately, the system is broken. No

**Dave Jones:** worries. Um the unlock if we can get it going uh the unlock key is in there. And apparently, it had access to the CAN bus. Um usually I Yeah, usually they don't have access to the CAN bus, do they?

**Dave Jones:** That's interesting. Hmm. Anyway, let's crack it open. Wow, I haven't taken apart a car CD player for ages. What was that? Like well, I'm talking like probably several decades. Um when back when they were a thing. Oh, what was that movie that had uh one of

**Dave Jones:** the characters always carrying around I think it was his Was it his Kenwood stereo system? Oh, it was hilarious. I'm going to have to try and think of it and put it in. It was great. Anyway, the 6000 CD RDS on RDS Eon. I'm RDS on I was

**Dave Jones:** thinking MOSFET. Like to me that's RDS on, right? Anyway, CD changer compatible. You got to have the external CD player. T A P T Y like proprietary limited. I yeah, wow. Oh. It's It's a bit how you doing? And

**Dave Jones:** monster buttons. Wow. I it's yeah, huge. Anyway, yeah they all have these security key codes because well, back in the day you know, people used to steal car stereos. Break into your car just to steal your car stereo. It was a thing. So you'd

**Dave Jones:** have these removable ones with the pull out handle and you'd carry it with you. It would Trust me, that was a thing in the 80s. I do want to get a throat rip in here. Think that's going to be you small fry.

**Dave Jones:** Who's first? Ah, shh. You did not JUST DO THAT. THAT WAS A BLUFF HUNT. YOU OWE ME A BLUFF HUNT. SO ANYWAY, ALL THESE CUSTOM connector jobbies all go into your wiring harness and they're sort of like semi-compatible

**Dave Jones:** wiring harnesses and things like that. So you can buy like generic CD like you know, CD systems these days and they come with like a different harnesses depending on the car you've got. All right, let's go in here if we can get this top

**Dave Jones:** cover off. You got to Hang on. Got to give them a bit of a whack. There we go. Is that it? We're in. There's our CD mechanism. Geez, can't see much else. All the rest of all the good stuff is on the bottom. And of

**Dave Jones:** course, one thing you're going to find in a car is a good compliant mechanism. So Oh yeah. Oh yeah, baby. Look at that. That's fantastic. It's nice and stiff. You got to love us good stiffy mechanism. I could play with

**Dave Jones:** that all day. And four screws and that comes out easy peasy lemon squeezy. There you go. There's the bottom of it for those playing along at home. For you CD mechanism aficionados, well, there you go. Is it like it's a Pioneer uses

**Dave Jones:** Pioneer chipset? So, I presume it's a it's a complete Pioneer design player. But it's got made by Visteon in Portugal. Hi my Portuguese viewers. Wow. Um okay. Who on earth is Visteon? Anyone knows the history of that? Let us know.

**Dave Jones:** Front panel just popped off with a couple of tabs. Look at this. Phenolic base single-sided. Not that a double-sided FR4 rubbish. Ah, spared no expense. That's actually quite interesting that they use a combination of a ribbon connector interface and then these very nice

**Dave Jones:** uh pressure contact. That's interesting. Anyway, that's very cool. And there you go. That's inside the thing. That down there, that's an ST jobby. Not sure what like you know a single chip custom design solution for this. There I

**Dave Jones:** really like the the right angle board like that. Looks like that's just soldered in and pins directly soldered in there. So, that's a nice interface. And of course the single in-line or staggered pin single in-line audio packages which you

**Dave Jones:** find in every single car audio system. They're just yeah, they're and of course they're Philips. Philips like own the market. And of course they use the die cast die cast metal chassis down there for the heat sink. That's about all she

**Dave Jones:** wrote. Is there any thermal compound in there or they just put in a uh like a little sill putty thing. And then there's really not much else going on down here. There's a receiver down here. I'm not sure what that's uh

**Dave Jones:** uh is that some sort of audio interface? That's No, that goes to your CD uh mechanism, I think. And that's another ST job down there. In fact, this is all ST. ST as far as the eye can see. Wow, they

**Dave Jones:** got design wins everywhere. Except for the audio stuff, which of course Philips been winning for decades. ST do uh are in that market uh these days? I don't know if they were back then. I needs to know what is behind

**Dave Jones:** there. Yeah, they just got a uh just got a uh pad. Yeah, there we go. There's a metal backing. They've just got a some sort of sill putty kind of That's that's a bit crusty. It's a very fibrous

**Dave Jones:** kind of, you know, sill putty is a trademark. Um it's just the It's become like a generic thing like Xerox. I don't think that's a switching converter cuz that's only a 16-V uh cap there. What brand have they got on

**Dave Jones:** that? Can't see it. Anyway, yeah, I think that's just an input uh choke and uh filtering. There's another money shot. Look at that. Oh, it goes up and down and all around. Oh. Bobby Dazzler. Hello to all my viewers

**Dave Jones:** in Kentucky. Um that's in the United States of America. JOHN UH MONACO, thank you very much. Um what's in here? Well, I kind of know because the description kind of gives it away. I won't tell you cuz the whole point of

**Dave Jones:** mail bag is like it's all uh it's all secretive. Let's go. Note on top, thoughtfully provided. Which means, you know, if you put note on top, maybe I'll read it first, maybe I won't. Depends. It's lucky dip. I

**Dave Jones:** really enjoy your videos. THANK YOU. OH. OH, it's it's John's attempt. Thank you very much, John. It's John's attempt at something that I have here behind. No, do I? Yes. It might be in the shot somewhere. Anyway, it's John

**Dave Jones:** Play pack. It's John's attempt at doing this. Oh. OH. WOOHOO! THIS LOOKS full on. I'm like a kid in a candy store. What is it? What is it? This is actually quite a brilliant replica. Look at this. It's the time circuits. Fantastic.

**Dave Jones:** Oh, that's beautiful. I love WOW! YEAH, IT'S EVEN YOU KNOW, IT'S GOT THE STAGGERED configuration correct. Looks like it's got the all the colors correct. It's It's actually got the proper stick on like Dymo type labels. These aren't actually Dymo ones, but

**Dave Jones:** they are like they're not silk-screened on. They're They're They're actually stuck on. Oh, that's great. That's better than the one I've got here, which is okay and I had to like uh have a custom frame for it and

**Dave Jones:** everything. And this one failed. I had to replace one of the chips. I might link in that video at the end. I was uh troubleshooting this. It's powered from an Arduino. It's all kind of like messy. Whereas this, this is brilliant.

**Dave Jones:** Self-contained 5-V uh 2-A input uh DC barrel jack. So, I can just like leave that running on the on the bench here. Bobby dazzler. Wow, this really looks fantastic. Apparently, the case is 3D printed. That is like endwise. So, this would be

**Dave Jones:** this front end would have been flat on the uh bench, but you can see the stickers on there. That's just brilliant. It's staggered. So, yeah, 3D printed. Well, not exactly like the original time circuits, it's built to scale and painted. It certainly is. I

**Dave Jones:** would not know that is 3D printed. That's just fantastic. But if you look close enough, you can actually see the layers in there. Wow, that's terrific. So, here we go. Time circuits on. Ah, flux capacitor. Fluxing. Engine running. And I do believe it's got the

**Dave Jones:** original dates on there. Well done. Anyway, using ATmega328 and a DS3231 RTC battery backup. Displays are driven by a whole tech LED driver. Excellent. Designed the boards in KeyCAD, had them made by JLC. Took about Display board took about 12 hours to layout due to its

**Dave Jones:** complexity. Well, first time using KeyCAD. Excellent. Well, let's go in and take a look. It's written using the Arduino IDE. Excellent. And I'm sure you can I assume it's like open source. You can get all the stuff. This is awesome.

**Dave Jones:** Thank you very much, John. And on the back we can just start set the time up and down as well. But there's no like USB interface to like diddle with it. And then if you just press set, it just cycles through

**Dave Jones:** or up and then you can save it just cycles through. Oh, looks like we can adjust the brightness as well. Brightness. So, if I set that level. Oh, yeah. Nice. Wow, this is pretty great. Yeah, look at that.

**Dave Jones:** You can see all the layering in there. That's brilliant. And I won't take the thing fully apart cuz it's a little bit uh little bit complicated to keep it all together. Look at all those screws, but you got three separate uh front panel

**Dave Jones:** PCBs down there, obviously. And then just your little Arduino board down there. I did you know, ATmega time circuits control version 2.0. Excellent. That is brilliant. Thank you very much, John. That is a superb, absolutely superb implementation. I love

**Dave Jones:** the texture on it, too. It's got that metal textured finish. And And you really would think that, you know, this is pretty darn close. It's not far off the original. I'd happily, if I actually had a real DeLorean, which if I had millions

**Dave Jones:** and millions of bucks, yes, I would actually buy myself a genuine uh uh uh time machine DeLorean, and I you know, I'd have no problems having that in there. Well done. Hats off. That's going straight to the pool room. Now, this one

**Dave Jones:** comes from e-con systems in India. It didn't have mailbag on it. Put mailbag, PO Box 7949, Box Hill New South Wales, 2153, Australia, not Austria. Um and yeah, I did open it, and it was obviously a mailbag, so let's take a

**Dave Jones:** look. And it's a It is a There is. There it is, a USB 3 camera system, one of these little important go to developer software tools. I've got the Find all the docu- I've got a serial number, so that I can Anyway, I won't.

**Dave Jones:** It's tiny. There's a little USB 3 camera in here. I'll show you. So, e-con systems is actually an Indian company, and this is their new see3cam um CU30 series. This one's actually the uh CU38. No, it doesn't cost 10 bucks. Our volume

**Dave Jones:** pricing starts from about uh 70 bucks. They just put that on there because it's an engineering sample. Nudge, nudge. Wink, wink. Let's take a look at it. Oh, got a name bonus lens. Oh, no, that is the lens. That's just a cover. Okay, so

**Dave Jones:** this is based on the uh on semi AR0330 sensor, and we can have a look. We'll be able to see that. If we pop the little dust cover off, there's the there's the little sensor down in there. Nothing too interesting to see. Anyway,

**Dave Jones:** this is supposed to be a uh low-light uh camera module, USB 3, 60 frames per second, full HD. I won't go into uh huge amount of detail on there, but uh yeah, it's supposed to be uh you know,

**Dave Jones:** requires no drivers, just uh all directly supported via Windows. And as we saw, it comes with a little lens, and that looks very well that looks reasonably wide angle, doesn't it? And I believe this is like an M

**Dave Jones:** Is this an M12 mount? And that'll just screw Oh. That should just screw in there. Geez. Having a hard time getting that lined up, but there we go. We're in, and well, I'll plug it in, USB-C, not that micro rubbish. Going to put it

**Dave Jones:** in all the way. And low-light camera. Um d- d- I presume it's like probably like designed for security or something like that, cuz it uh with a wide-ish I presume that's going to be a wide-ish angle lens. So, don't have any

**Dave Jones:** I don't think I have details on the lens. Let's check it out. That looks like an onboard microphone. It even says mic. In fact, it's got two of them. So, uh yeah, stereo mics, does it? Presumably it uh

**Dave Jones:** it's going to output uh stereo. So, that's very handy having a built-in mic. So, yeah, you know, you could build this into your own little custom enclosure. Wouldn't be hard to get a little plastic box and just do a

**Dave Jones:** uh cutout in that. Just a minute job, and you're done. And uh USB-C interface, so you could 3D print, you know, a custom enclosure. That'd be pretty trivial. So, we're on the e-con systems page here, and I'm actually a bit confused

**Dave Jones:** about what module I actually got because on the top here, it says it's the CAM30. On the bottom, it says it's the 132, which I assume is part of the 130 series. Anyway, they have a whole bunch of different ones for all sorts of

**Dave Jones:** various industrial applications, different form factors, lens configurations, all sorts of stuff. They've got a frame safe camera. What's a frame safe camera? Like I I don't know. I I'm sure people will know. Oh, yeah, no, I've got frame safe cameras. They're

**Dave Jones:** cool. Um anyway, yeah, there's stereo vision ones as well. If you're into stereo vision, uh Cypress uh dev kits. They've got industrial cameras. That looks nice. That's got like an S-mount uh lens adapter on it, very nice. And um

**Dave Jones:** oh, look, they got Nvidia cameras up here. Wow, they've got tons of stuff. Wow. Just e-con systems. Wow. Apparently, yeah, they're not just a reseller, they manufacture these. They design and manufacture these. So, yeah, very cool. Anyway, I'm rather a little

**Dave Jones:** bit confused. Um so, I thought, "Look, this one does actually come with the CU30 low light one." Um it says it's the CU38 on the paperwork, but I I don't know. It doesn't look like the right board, right? That does not look like that's

**Dave Jones:** not the correct board with the microphones and everything. So, that's really kind of weird. That's not it. This one looks like it is, though. Low light USB camera with and without enclosure. That looks like the right Yeah, that looks like the right one.

**Dave Jones:** Actually, this one's actually called the Conversa. All right. So, it doesn't actually have a model number. It's oh, Ecam houses Ecam 36 electronic rolling shutter uncompressed blah blah blah. I think this is the one we've got. So, it's all very confusing.

**Dave Jones:** Wow. Anyway, it'll do full HD at yep, 60 frames per second. It'll do three 3.4 megapixels at 48 frames per second. It'll do three megapixels at 60 frames per second. Geez, that's pretty good. I mean it's a backward compatible with USB 2. I like

**Dave Jones:** that. Well, let's plug it in and see. So, you're wondering what I'm shooting with here at the moment. This is my webcam. It's not actually a webcam. It's my old one of my old B-roll cameras, the Canon HF M300.

**Dave Jones:** So, that's what I'm shooting at well, you don't want my face. And it's night time here. So, there's very little there's no light coming in the window. It's haven't got a studio light turned on or anything. So, let's just plug it in, shall we?

**Dave Jones:** See what pops up. Is it going to go boo boo boo? Light comes on.

**Dave Jones:** Windows just did that. Not sure if you heard that. Okay, I'm going to add a video device. It's It shows up. I won't show you this cuz it'll be like inception kind of thing. There it is. Woo. Device

**Dave Jones:** video. So, I'm using XSplit. It just shows up as the Ccam 30 CU38. So, let me switch over to that. So, I'm going to add that and there it is. Boom. We're in like Flynn. So, it's not auto focusing.

**Dave Jones:** Check check check one two. Okay, I'm now using the Ccam 30 stereo microphone. It's at the same distance as my desktop mic here about 30 cm away. Talking directly into it. I presume it's going to have the stereo

**Dave Jones:** mics. VU meter shows it's a bit lower than my road mic though. So, I might have to again that up in editing software. And if I adjust that lens, wow. It's flickering. It's picking up the flicker from those LED lights

**Dave Jones:** which none of my other cameras pick up. That's terrible, Mevo. Not impressed by that. So, there we go. I can adjust the I guess the I guess it's got to get to a loosey-goosey where it's in focus. Gets

**Dave Jones:** to a loosey-goosey point on the thread. So, you'd have to maybe Loctite that in place. Otherwise, it might vibrate out of focus. But apart from that, there you go. Yeah, I'd say that that's like 60 frames per second. That's really good updating.

**Dave Jones:** Yes, that is a bean bag. My electronics bean bag. Winner, winner, chicken dinner. Um yeah, okay. Low light, I'm not in like it flickers. I uh Maybe I can adjust the settings. Okay, that wasn't full HD, by the way.

**Dave Jones:** I've I've fixed that. Okay, auto brightness uh white balance gain. This can't show you this, sorry. But anti-flicker is not an option in my settings. Got the usual just the usual camera stuff um showing up here. It's terrible. Anyway,

**Dave Jones:** the these are By the way, these are just some new lights that I had uh installed. Um like all like Whoa. Whoa, something just crashed. Whoa, okay. So, that crashed. I'm not sure what happened there. Um I'll add video source again. Here it is.

**Dave Jones:** Uh XSplit still running. So, it's not that. It It looks like it was the It was the device. C930. Yep, there we go. It's back. Don't know what happened there. Sorry. Just checking to see if my Canon camcorder

**Dave Jones:** shows those lights flickering. No, it does not. None of my cameras pick up the light flicker. Yeah, anyway, I didn't even know those lights flickered. So, that's interesting. Um I know, I just got them installed as part of like a government program. They

**Dave Jones:** come around and replace your troughs with these LED panels. They all They all the correct color temperature, 5,000 K, but they flicker. But that that hasn't been a problem. That's not a problem on my other cameras, on my studio cameras or

**Dave Jones:** you know, my old camcorder here. Yeah, not exactly blown away by the quality there. That's 1280 by 720. You know, it's supposed to have auto white balance and auto exposure and all that. Anyway, it it is fixed focus.

**Dave Jones:** It's not an auto focus camera, so you got to twiddle the lens to get it right. That's That's reasonably wide angle though. You can see it's You can see the frame of the window there. That's the uh It's got some fish eye on that. So,

**Dave Jones:** it is pretty wide angle though. I think that's probably I'm going to guess 12-14 mm or something like that in 35-mm equivalent. Anyway, it is wide angle. It is sort of a fishy lens in the middle. If I take

**Dave Jones:** that around like that, you'll see the door frame straighten up there. There you go. And bring it to the rotate around to the edge and it gets fishy fishy eyed. So, but that's normal. It's to be expected with a lens.

**Dave Jones:** And it does it up the top as well, of course, cuz it's a symmetrical lens. Anyway, you you get expect that. That's just, you know, a typical on your wide angle lens. Some are better, but you got to pay like, you know, a huge top dollar

**Dave Jones:** for a a massive lens that, you know, can go down to like 12 or 14 mm without much sort of like fish eye effect. It's really actually quite difficult. So, you see you get sort of that, you know, wide

**Dave Jones:** angle GoPro-y type look. 2304 by 1536. Supposed to do 48 frames per second. Oh, yeah. There you go. It's really good now and the lights aren't flickering. Lights not flickering anymore. Okay, so that's better. Yeah, that's better. Of

**Dave Jones:** course it's going to be dark on this side because like the window's there and there's no sun from the outside. So, actually that's doing that's pretty reasonable. As long as it doesn't lock up again. Maybe I I bought resolution or something

**Dave Jones:** I was using before caused it to lock up. As a calculator test on the bench top, that's pretty good. Course it's all you know, it's all fish eyed but you can get different lenses. So, that's that's really quite

**Dave Jones:** sharp. You get the lens as I said lens is a bit loosey goosey in that particular spot. Geez, that's pretty jazzy. It's getting a little bit warm by the way. Yeah, I'm liking that at the high resolution. So, what did I say? I

**Dave Jones:** mean I'm only recording this at uh full HD. So, sorry. Um you're you're not going to see the the full quality of it here. But that is uh 2304 by 1296 resolution. So, that's like an oddball type one at 60 frames per second. Pretty

**Dave Jones:** jazzy. Oh, we're we're we're we're getting the flicker again. Getting the flicker over here. It's uh you turned off the lights. Oh, yeah. No, it's it's come back. Flicker's come back. Why? Well, I can focus focus really close.

**Dave Jones:** Still getting sharp. As I said, the light is not very good in here. Light is really poor. I can get my studio lights out though. Here we go. If we get a couple of studio lights in here, look at

**Dave Jones:** that. It's quite nice. Little bit of jerkiness there. So, not sure what the deal is. Yeah, to get that resolution. Actually, you know, you'd expect better update rate in lower light. There's full HD 1920 by 1080 60 frames

**Dave Jones:** per second. Yeah, have a look at that. Can I get it to focus? Wow, look at that. I'm right down onto that. Like 5 mm away or something. That's that's nuts. There you go. Brilliant. Got to change the

**Dave Jones:** focus when I'm further away. That's all right. So, there you go. If you're into uh little camery modules, E-con Systems might be worth a look cuz they've got a massive range of stuff. Anyway, check it out.
