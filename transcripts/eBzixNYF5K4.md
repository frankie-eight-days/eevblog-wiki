---
video_id: eBzixNYF5K4
title: EEVblog #1049 - Mailbag
url: https://www.youtube.com/watch?v=eBzixNYF5K4
source: youtube-asr
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. I hope you had a good Christmas and you might even be watching this in the new year, so happy New Year. Let's get into it. We've got a Kickstarter time-sensitive and 1st of January. I better hurry.

**Dave Jones:** Thank you very much from Zepto bits. Um by the way, my Kickstarter is I just got the money in yesterday as if you follow me on Twitter you would have seen and now I've got to spend it all by

**Dave Jones:** buying um the stock. Well, I already have bought some stock and it's coming in. I'm not going to bit miffed. I'm not going to actually meet my promised deadline of December. Um it was very close, but they're like

**Dave Jones:** sending like today or tomorrow or something. So I just like there's just been little delays here and there and it's what can you do? Um anyway, so so yeah, it might be a few at least a few days late, maybe a week later or

**Dave Jones:** something depending. Anyway, um by the way, yes, I am you've no doubt seen in the previous video that I am going away for a good lot of uh January. No, I'm not running away with the Kickstarter money. Don't.

**Dave Jones:** Um I am going away, but I'm going to have some guest videos. There's been a lot of submissions for those. Um and I will be choosing some choice videos to show on the channel. There's going to be some really good ones, so stick around

**Dave Jones:** for that. Hope you enjoy it. Thank you very much. Oh, look. Oh, look. Thumbs up using using the the Dave logo, I guess. What do you call it? I don't know. The letter-based uh thing, which um is there's a few people using the

**Dave Jones:** letter-based concept. If you haven't seen it, I'll link it in at the end of this video if I remember. I'm sending you two optically isolated USB UART adapters. Thank you very much, Emma Johnson from Zepto. Geez, they're There's nothing in them.

**Dave Jones:** Geez, opto-isolated USB UART adapters, very handy if you need to isolate. Cool. We'll take Oh. Oh, yeah, they're both Yeah. They've just got different USB connectors on it and they've got my logo. Thank you very much. Let's take a

**Dave Jones:** look at them. As it turns out, Emil is currently over 500% funded on the Kickstarter. Fantastic and I'll link it in down below if you want to jump on the bandwagon and I recommend you do because these things are incredibly useful and

**Dave Jones:** being optically isolated, of course, nice isolation slots there. Excellent. Um, 3.3 and 5.5 volt jumper. Nice. Um, and of course, you power it from the external uh, supply. So, you got to hook up an extra, uh, cable in there to do it, but you can't

**Dave Jones:** blow up your computer or your circuit with any ground loops or anything like that. So, valuable to have one of these in your parts bin. Not parts bin, your I don't know, equipment shelf or whatnot. And there's not much on it.

**Dave Jones:** There's a couple of opto-isolators and a USB to, uh, UART adapter and that's about all she wrote. Yeah, it's got the proper isolation shots slots and everything else. And of course, the open source. Hey, it's different. There's an extra D in there.

**Dave Jones:** The D is not on that one. Oh. What? Anyway, oops. Anyway, that's cool. Check it out and you can either get one with the micro or the, uh, old style type, which is just big and rugged when you're hanging the

**Dave Jones:** thing off a bloody cable like I'm doing. If I'm hooking that up to, uh, you know, some serial pins on a product to extract the, uh, firmware from it or whatnot, then, you know, having a little micro USB is a bit dicky. Uh, one of

**Dave Jones:** these big A types is the go. Ah, there you go. It is supposed to have the uh, D the design notes principle of operation by the way which is excellent because in the data sheet here there's a full

**Dave Jones:** schematic for those playing along at home. There's not much to it but a very nice quick start guide and then table of contents and summary. So avoid ground loops all that sort of jazz. Neato. Works anywhere up to two meg

**Dave Jones:** board and IO levels from 1.8 to 5 volts. Thank you very much person unknown from Melbourne here in Australia, not Austria. Let's take a look.

**Dave Jones:** Here we go. By the way, videos coming up. I'm yeah with the Kickstarter and all the fulfillment crap I've got to deal with for that. It's limiting my time at the moment but I do hope to do probably another debunking

**Dave Jones:** video before I go away. Plus maybe another one or something like that. I'm not sure. I don't plan that far ahead here. Something to cut open. Okay, let's cut it open. Cool. What? Looks like serious bit of kit.

**Dave Jones:** Caution static sensitive type it's an assman. Assman assman ass ass American ass Check this out. It's obviously designed to go in the rack. Cuz there's a lot of wasted space on that puppy but it looks like some sort

**Dave Jones:** of ovenized yep oven crystal oscillator. Cool. 2.048 meg. Cool. We'll do a quick so the can is completely soldered together. That's a pain in the butt. Here's something to cut open. 2.048 megahertz crystal oven. It came from a system and I still don't

**Dave Jones:** know what the day 100 announcement that saved it EEPROM EEPROM and played back when anyone rang the line that were connected. Anyway, there's a whole bunch a multiplicity of time in units. God, it sounds like a straight out of a patent application,

**Dave Jones:** doesn't it? Geez, time and information path extracted. Pretty comprehensive stuff on how that this timing board is tied into the system and it works. So, yeah, this is for some you know, telecoms thing or whatnot. Um, gee. Yeah, this is just

**Dave Jones:** nuts. As I said, there's not a huge amount on it. And yes, we do have the schematic. Hang on. But anyway, here's the VCXO module down here and it's basically just apply power and Bob's your uncle, right? Get's the output and then you've just

**Dave Jones:** got some output drivers here which then just drive 100 ohm balanced lines to spread across the rack or the you know, the system or whatever they're powering. So, nothing fancy there at all. And that's all she wrote on here.

**Dave Jones:** So, there you go. Got some voltage regulation. You know, it's all very neat and tidy. I love how they heat shrinked it and they cable tied it there. Beautiful. And there's your output drivers down there. It has to be this long cuz it's designed to go

**Dave Jones:** into a rack. So, for those playing along at home, there's the data. Vectron Labs. Ah. Made in the United States of America. And it's all sealed inside. We may have to blast. Now, I could try and get the soldering iron on there, of

**Dave Jones:** course, but you need a like a huge grunty soldering iron cuz that it's a massive heating. So, it's easier just to get in there with a screwdriver and just crack the solder open. It's well, it it's a bit medieval, but like we don't

**Dave Jones:** want to reuse this anyway. so, you know. Well, inside an ovenized oscillator, it's not going to be spectacular. It's just going to be some foam cuz it needs insulation, and some sort of, you know, hard cell foam type insulation. And

**Dave Jones:** there's just going to be a regular boring, you know, large crystal oscillator module, which is carefully hand-selected and manufactured by nude virgins, of course, and then tweaked and calibrated by, well, graybeard nude virgins. And the heater coil, of course, and then feed

**Dave Jones:** back to maintain the Can we Oh. Maintain. Oh, hello. Hello. To maintain the temperature, of course, cuz it's it's a temperature controlled. Oh, there we go. Really old school. Look at that. Oh, I see a precision That looks like a precision resistor

**Dave Jones:** down there. Very low tempco resistor. The black one. And then, of course, there's some of our hard cell foam insulation. And yeah, they've got it taped like the entire core is just taped down in there. So, we've just got the controller board, and

**Dave Jones:** then there'll be an an ovenized There'll be like an oven element, a heater element down in there, and the crystal. And then some Yeah, it's just some temperature feedback. All right, there we go. We've extracted the package. And that was that is that an adjustment

**Dave Jones:** screw? So, that was what the screw was in the back of the physically in the back end of the case. There was a screw, so you could get in there and tweak it. So, can we cut into this puppy?

**Dave Jones:** It's not like a physics package in a rubidium oscillator. It's just a Oh, there we go. Geez, wonder what the date on this would be. I'm thinking eight, you know, sometime in the '80s. Crack it open. Oh, there we go. Geez,

**Dave Jones:** that's actually more serious than what I Oh, damn. I think I just might have broke some wires or something that is really fascinating. Wow. And that is that just electrical tape? I think that's just electrical tape. Uh, I got to go clean this up. This is

**Dave Jones:** horrible. Anyway, you can see that the uh temperature of this thing is just like burned inside that. So, anyway, it it contained it. It did its job. It probably worked for like 20 years at you know, these things might operate at you

**Dave Jones:** know, 50 60° or something like that. You want them to operate above the maximum ambient ambient temperature which might be say you know, 45 or you know, 50 inside a rack or you know, something like that. Um so, yeah, that could have

**Dave Jones:** been operating at I don't know, could have been operating at 70 80°. Who knows? And if that was electrical tape, well, it's kind of well, no, I don't know. What is it It's like paint or something? Actually, they what Ah, look at that.

**Dave Jones:** Wires wrapped around the case. Is that the heating element? That could be the heating element. Wow. Some sort of nichrome resistance wire or whatnot. And wow, I I just thought they were like ridges in electrical tape. That's what it looked like at first

**Dave Jones:** glance. And then I poked it with a knife and went No, I got to try to find a seam to peel it off, but no. They're actually you know, they're all on there wound a bit how you doing, but uh I got to screw

**Dave Jones:** off the end and ta-da. Oh, we're in like Flynn. Wow, look at that. So, yep. And so, we got two uh two wires Well, okay. Got two going in there. Could one be a sensor? Could that be a sensor perhaps? One of them's the

**Dave Jones:** coil, one of them's the sensor? Don't know, but there you go. There's the There's the oscillator circuit. It's, you know, probably some variation of a Colpitts or something like that. Liberal application of the Silastic down in there. And, tada! I told you.

**Dave Jones:** It's just a regular Joe Blog's Well, it's not a regular Joe Blog's crystal. As I said, um it's manufactured and by and tweaked and hand selected by gray-bearded nude virgins. And there you go. Got 79° C written on it. 12 puff for

**Dave Jones:** those playing along at home. And it's a Y 4200. So, that'll be a 2.048 MHz crystal, I assume. I don't think they've got a divide by Oh, they might have a divide by two on there. Who knows? But,

**Dave Jones:** uh yeah. No, that's probably a 2.048 MHz crystal. Really good one. As I said, hand selected, hand cut, everything else. Hand measured and probably aged almost certainly aged in and everything else. And we've got ourselves a trimmer cap.

**Dave Jones:** There you go. There's the trimmer cap in the end of it. Get in there from outside the case and go your tongue at the right angle. And you can trim your 2.048 MHz oscillator. Of course, the whole idea of an oven

**Dave Jones:** controlled oscillator, why they go to this sort of trouble to actually keep it at a particular temperature is because crystals are inherently very stable when you keep them at a particular temperature. Even your crap ones. You know, you one you buy for 10 cents

**Dave Jones:** at the Shenzhen market can be very good if you keep it at exactly the same temperature and drive voltage. And then you don't shock it. You don't move it. You don't orient it cuz I've done a video, I might

**Dave Jones:** have to link it in, about the orientation of the crystal. You can actually use them as gravity detectors and I've actually demonstrated that uh principle. So, as long as you don't touch it, they're generally pretty good. But, of

**Dave Jones:** course, this one would be super selected, super aged. And then you've got aging and all sorts of characteristics like that which go into it, of course. But, yeah, I've done like a lot of characterization of the stability, the long-term

**Dave Jones:** stability of crystal oscillator modules. That was part of my job back in the day. And it's a very interesting thing how they how if you just go like that on the side of it, you can reset, effectively reset the drift characteristic of a

**Dave Jones:** particular crystal. It's really fascinating. So, any sort of shock or vibration or anything like that. But, there you go. That's an ovenized oscillator with the heater element on the outside and a temperature sensor. And they just, you know, they have a

**Dave Jones:** feedback loop and keep that controlled at by what looks like 79° C. And by having that actually written on there, 79 C, they've obviously that's what it was, you know, tested at and aged at or whatever. And that's probably what they're running

**Dave Jones:** at in here. So, I don't know what the temperature variation, you know, you try to get within keep it within, say, you know, half a degree or something like that. If you generally, you know, at a couple of degrees, then

**Dave Jones:** you know, wobbles all over the place. Not you're going to get output stability is going to be dependent upon the temperature. So, it's going to drift with the temperature. So, the more accurately you can control the temperature, the more stable your crystal is. So,

**Dave Jones:** that's basically how it works. Cool. Old school ovenized oscillator. Awesome. Now, let's have a quick look at the DAG 100, the ass man. DAG 100's brilliant. Anyway, I like the I like the pushable indicators here. And this is supposedly Is that a little

**Dave Jones:** Is that a speaker on the front monitor? Yes, it is. Um and some volume there. So, this is a rack mount uh voice uh recording thing apparently. And there you go. We've got ourselves a uh line isolation transformer on the back by the

**Dave Jones:** looks of it. Crack it open. I guess that's what you'd pretty much what you'd expect here. Speaker uh PCB mounted. So, it just uh I thought it was mounted on the front panel, but it's not. And we've got little uh Is that a little amp? Is

**Dave Jones:** it? I don't know. I can't read that. I can't read this stuff on the camcorder screen anymore. Ridiculous. Anyway, we've got a nice DC-to-DC converter. Oh, I can salvage that one. No worries. Made in Germany. Sweet. And we've got

**Dave Jones:** ourselves a power amp there, but everything else is 4000 series CMOS except basically for these two puppies up here. Mostek. Anyway, we have date codes like, you know, early '80s stuff happening here. '86. Uh mid Yeah, '86. But uh check out This

**Dave Jones:** is an Intel D2912. That's a PCM filter chip. And there's a Mostek. There's a blast from the past. Uh that's an MK5156. And that's a PCM codec. So, we've got our PCM codec and our PCM filter. But um

**Dave Jones:** where is the EPROM that was talked about for storing this? What's that? I can only presume that that thing which has got like LO1. The rest is just a date code. Um and and it's socketed. Don't know why the uh 4093's socketed there,

**Dave Jones:** but uh anyway, that one I assume must be the serial uh PROM chip that holds the recorded message. Must be. There's nothing else on here. There's nothing on the other side of the board. That's it. Hi to all my Romanian viewers. This one

**Dave Jones:** you're no doubt familiar with. We've had it a couple of times on the blog. And sorry I haven't uh I've already opened this cuz I've actually been using it for like a month. Um and those on the forum

**Dave Jones:** and Twitter would have uh seen this already. It's Radu uh Motisan's new environmental monitor, the A3. He's done previously done the radiation monitor, but this one is the do-all end-all kitchen sink model. Um it's a complete environmental monitor. It does

**Dave Jones:** radiation, formaldehyde, particulates, 2.5 micron particulates. Uh it does temperature, uh pressure, uh I'm forgetting some stuff. Anyway, air quality monitor as well as radiation. It's awesome. So, let's take a quick look at it, and I've been running this for a month at my lab. Um

**Dave Jones:** and let's have a look at some data. Cool. So, this is Radu's new environmental monitor A3. It comes in uh different types. So, this is the ethernet interface one, but they also have the uh Wi-Fi interface version, and

**Dave Jones:** both of them work very well. And here's inside of it. We've got the laser um scanning uh particulate sensor here, which has a little uh scanning laser in it. And it's got a little uh port on the back where it sucks in the air, of

**Dave Jones:** course. And a little micro fan inside there. So, it actually it sucks it in. The air flow just comes through over here and out the other side. It's not very noisy at all. I've got one uh running at home in the back room, and it

**Dave Jones:** Yeah, you can hear like in the middle of the night, you can just hear it. So, you wouldn't want to, you know, have it on your bedside table or something like that, but it's certainly not loud. And of course, we've got our

**Dave Jones:** uh Geiger-Müller uh tube in there. And then we've got our uh formaldehyde sensor here, and our CO2 sensor down here. And of course, these are all uh factory calibrated and characterized and whatnot. And uh Radu did send me a

**Dave Jones:** characterization uh sheet on one of these that has been um Um, know, independently uh lab certified and all that sort of stuff and there's a couple of whatnots on the bottom and that puppy right down in there is the Bosch VOC sensor and you

**Dave Jones:** can see the slots around there. It's just on the outlet of the fan so the so it's well placed, well designed just to get the air flow directly over that. Awesome. And we'll have a quick look at the software interface which we've seen

**Dave Jones:** before but there's also this new cool dashboard view which is a worth checking out. Gives you an over like a summary and overlay summary of the of all the different sensors inside this thing for different time spans and

**Dave Jones:** here's the data for my lab. Isn't it great? I'll link it in down below if you want to check out the live data. And we've got a little microphone down in there as well because it also measures noise. It must be doing some sort of

**Dave Jones:** like you know averaging you know, heavy duty averaging and stuff like that cuz you don't want knocks and bangs of doors to you know, really register on this thing. So that it'll be done in software no doubt. So Radu's

**Dave Jones:** done a fantastic job developing this over the years and I'm not aware of any like really major competing solution for this and it's not cheap but if you're after comprehensive environmental monitoring for your location or a remote location or whatnot

**Dave Jones:** then this thing is pretty much the duck's guts I think. Check it out. Thank you very much. Silan, silent V, Stoyanov. I'm from Bulgaria. Hello to all my Bulgarian viewers. Let's check out what's inside. Is that it?

**Dave Jones:** Fancy a VU meter. Turn it on. Give a power to the USB port 5 to 20 5 to 20 or 5 to 20 volts. Oh, right. Okay. Is it a project Um Celin's done. So, here's the VU meter. I'm actually not

**Dave Jones:** sure if Celin um actually uh produces and manufactures this or not. Anyway, I'll link it in down below. sketchremote.com schremote.com. So, let's power it on and see what happens. Hey, hello. For EVBlog by sketchremote.com. Oh, there it is. Ah, I

**Dave Jones:** like the decay on the Hello. No microphone built in. Ah. At least have At least have one on the board, I reckon, and have a jumper link that you can uh uh actually connect to it. Anyway, I Is that

**Dave Jones:** Is that an SD card under there? I think that's an SD card slot. Um updating the firmware, perhaps. Well, it turns out this thing's a real comprehensive beasty, and I've hooked it up to the PC, but I got a

**Dave Jones:** connection error, but I was warned that I was supposed to install the drivers, but I have a problem installing the drivers, so I don't know what what what what. So, I'd really like to play around with this thing uh some more cuz it does

**Dave Jones:** have some cool visualization uh stuff in the software, but I don't know like it's probably a PEBCAK. I'm doing something wrong with the drivers, but I tried for a bit. Um not going to spend any more time on it at this stage,

**Dave Jones:** but it does look Suffice to say, it does look very cool. And there's that is you can see the uh touchscreen in there. So, let's have a look. View modes. Oh, maybe we can set it up in here. Here we go.

**Dave Jones:** May we Oh, there we Maybe we don't Oh, analog VU meter. Look at that. Maybe we don't have to uh use the software. That's cool, but the software I think allows us to do more stuff or whatnot. But uh there you go.

**Dave Jones:** How do we get the view options? There we go. And you can set up your uh channels and stuff like that. Um it supports left and right stuff. I'm just feeding it in from the road Mikey but back

**Dave Jones:** There you go. Anyway, I think it's really quite cool. So, I'll link it in down below if you want to check it out. Apparently, it does claim on the website it does like a silly scope you know type stuff as well. So, you

**Dave Jones:** know, it's all just in software basically. Of course, it'll only be like audio type bandwidth but isn't that hunky-dory? Not sure if this has a name on it but it's from Finland. Hi to all my Finnish viewers. Let's

**Dave Jones:** crack this one open and see. It's a bit It's a bit mangled from the old Finnish post. Was that done locally here? I don't know. But yeah, it has seen better days this package.

**Dave Jones:** Got some solder wick. Got some old parts. Magna Card. Oh, more solder wick. Thank you very much. I can always do with solder wick. Um it's just got some What is it? So, I've got some random miscellaneous parts. I replaced the main

**Dave Jones:** board for I still don't know what a Magna Card 200 is. Um to Google but look they've got the LCD driver under there. And presumably it looks like it's just a maybe is it a you know 7106 panel driver

**Dave Jones:** or whatnot but we've got ourselves the micro on there. What's that puppy? That's an NEC D80 7 49. Like that's like an 8080 compatible chip. So, there you go like old school stuff. And I I assume really but like

**Dave Jones:** what does it do? No, that just uses a Philips PCF 2112 uh LCD um display controller. That's all it is. Just dedicated controller. It's got external Whoa. External cap Two caps? What are they? You know, runs it like an

**Dave Jones:** uh else RC oscillator uh perhaps or something like that. So, I we don't have any knowledge of this at all. Anyone? Bueller? Okay, does anyone know what that is? Looks like some form of spark gap perhaps. Once again, Bueller?

**Dave Jones:** Bueller? Hmm. Hello to all my viewers in the old dart, in particular M Tandy, great last name, um from Hatfield in the UK, of course, which is the old dart. The UK is the United Kingdom. The capital No, that's not the Like, what do

**Dave Jones:** you call it? The capital of the Commonwealth? The head of the Commonwealth? Whatever. Australia's part of the Commonwealth thing. Dear Ev, really enjoyed the show. Thank you very much. Enclosed, please find a transmitter and receiver a J electronic

**Dave Jones:** radio safe rated wireless emergency wireless emergency stop. What? Remove from a warehouse automation system. All right. Okay. So, you can just have an emergency stop button. It's not an emergency stop button. Um I'm forwarding both of these, so feel free

**Dave Jones:** to take them apart. What you find inside may surprise us. Ooh. So, Michael reckons what we're about to find inside one of these industrial controllers uh may surprise us. Hmm. Anyway, yeah, they're wireless. No wireless antenna Like, the antenna

**Dave Jones:** built in, I guess. Yep. Hmm. OH, I COMPLETELY missed the coax um BNC on there on the front of the bloody unit. So, well, like, "Where's the antenna? Where's Wally?" Jeez, right in front of me. Kind of like

**Dave Jones:** that uh that construction. So, let's open up a bit more and see what we've got in there. A little daughter board. Yeah, it's going to use like an off-the-shelf wireless module cuz it's already like uh you know, certified and

**Dave Jones:** everything else. So, they're not going to dick around doing that themselves cuz these industrial controllers price point really doesn't matter. And I really like the interconnection system. Check it out here. They've got these uh like card edge contact things, which then you

**Dave Jones:** might be able to see the contacts along the boards in there. And then when that just clips together, that makes contact on there. Dual edge, is it? No. No, it's uh single-sided. It's You can have a contact on either side of the board

**Dave Jones:** there there. But, that is just a really nice bit of engineering. Um take note of something like that. That is just brilliant. You know, the boards in there, no wiring, no nothing. Just clip it on, and then it interconnects with

**Dave Jones:** all these uh screw terminals on here. Fantastic. Aha, one of my favorite construction technique so far. I'm sure I've mentioned this in uh various videos. Yeah, I might have mentioned like the Raspberry Pi cluster or something like that. Just by the way,

**Dave Jones:** yeah, maybe I'll get around to it one day. I don't know. Um but yeah, you cut slots in the board like that and then just put the board over and then just solder board-to-board. And they've made a cube out of that. They put some

**Dave Jones:** plastic on there for good measure. Um maybe just to hold in place while they uh solder the thing. And cuz that wouldn't be supplying any structural, you know, integrity while the after you've soldered those things on. And that is a really cheap and simple method

**Dave Jones:** for creating a cube uh board construction like that. That is really jazzy. I like it. Anyway, we've got some input uh some input protection or output protection resistors or whatnot. Um Jeez, I have to desolder all that to get

**Dave Jones:** to the part. Anyway, it's not here we're not we're more interested in the physical construction details of this thing rather than going in having look at the individual chips and whatnot. I couldn't really give a rat's ass. But you know, they got some optos and

**Dave Jones:** things like that for driving, you know, their various outputs inputs and outputs. So you know, some sort of alarm system driving some relay and as I said just some sort of off-the-shelf uh module for the um comms. And there you

**Dave Jones:** go. As I said, that could be an off-the-shelf uh module or they've got it designed and certified by uh someone else. Um although you know, it doesn't looks pretty customy um to me. So anyway, they're like they could have

**Dave Jones:** subcontracted that out. Little uh mask uh ROM mask flash or whatever ROM, you know, it's fairly recent this thing. Um and just all your requisite uh uh opto um drivers and stuff like that. But that's cool. I like that. And of course

**Dave Jones:** Hatano. Can't say I'm familiar with Hatano brand. Hm. Anyway, but that is awesome construction. I love that. So that's the surprise. It wasn't a huge amount of surprise to me um but if you've seen or opened these types of industrial

**Dave Jones:** uh controllers before then uh you know, you would would have seen similar types of construction before. But just being able to have you know, just those blocks. Look, I mean there's no apart from the of course you got to

**Dave Jones:** have the coax in there for the um uh antenna, but apart from that there is no wiring at all inside that thing. Brilliant. What do all my viewers in San Jose? I love San Jose. Uh Osco. Wiggle wiggle. Not sure if a

**Dave Jones:** wheel not sure if it's a silent G or not. Anyway, from O Drive Robotics. Cool. So, robotics type stuff, I'm guessing. Uh go the gaffer tape. Gaffer tape for the win. Let's slice and dice her open. I'm sending you a demo of a project I've

**Dave Jones:** been working on for the past 3 years. Wow, an open-source low-cost servo motor for robotics. Is it like a kickstartery type thing? Jeez, what stuff in here. Wow. Oh, that's like a propeller. That's a serious propeller attachment for what I'm guessing is a very serious

**Dave Jones:** motor controller. Wow, awesome. All right, well, I'll I won't bother unwrapping. Let's take a look. Whoa, this is heavy. We have a serious bit of kit here for you uh motor aficionados. Oh, look at that. We've got ourselves nice-looking rotary encoder on

**Dave Jones:** there. Wow. So, I've got a rotary encoder attached to the motor. That's very interesting. We'll have a read of why he's doing that. Some kind of optimization thing or something. And look, they're obviously designed that looks like a you

**Dave Jones:** know model plane propeller uh type interface. And this is like a probably a model plane, you know, a big model plane grade uh motor on this thing. Wow. Let's read the note. And check out this driver board. Whoa,

**Dave Jones:** this is uh looks to be handmade, this one. Got ourselves a genuine bodged wire on there, too, going across there. And uh this is some serious business. Check out the uh heat sinks on the uh draw on the

**Dave Jones:** uh the probably the H-bridge uh driver [ __ ] down in there. And what sort of processor is that? Some some sort of army type thing. It's always an arm thing these days, isn't it? It's all the rage with the young

**Dave Jones:** kiddies. This looks grunty, like kilowatt grunty. Wow. Um let's read the note. Hi Dave, I'm sending you a demo of a project I've been working on for the last 3 years, an open-source low-cost servo motor controller for robotics.

**Dave Jones:** This lowers the price and barrier to entry to using high-performance motor control for hobbyists and startups. Industrial servo motor electronics are very expensive. I'm sure they are, even though I'm not in the field. I can pretty much guarantee they are.

**Dave Jones:** Usually $300 per axis. Wow, sometimes more. At the same time, there there are very inexpensive brushless motors from China, originally for hobby remote control airplanes. Yep. And the driver electronics for those are also dirt cheap. From my experience working

**Dave Jones:** at ABB Robotics, aha, I know that the precision control is all in the software and the marginal cost of the software, yep, is effectively free. So, there had to be a way to make a cheap but still precise version of an industrial servo

**Dave Jones:** motor controller. And it turns out I was right. It's called the ODrive. Um how cheap? Uh the motor, 30 bucks for a 1,600 W motor. The encoder is $10 uh for the for a resolution of 2,400 counts per

**Dave Jones:** rev. Wow. Cool. So, demo demo instructions. Clamp the motor test jigs to a table. Important. Oh dear. Um I don't know if I got clamps here in the lab, that's more at home kind of thing. Hmm. Use caution. This system can put

**Dave Jones:** out greater than 3 kW. Well, I don't even have a 3 kW supply here. My main supply is only 20 uh 2.4 kW. Uh connect to 12 20 V apply power. Don't touch the motor during the calibration sequence. Aha,

**Dave Jones:** the first 6 seconds. So, when it boots up, all the software is in the magic. Does it I presume that it Can you like take the rotary encoder off later and then just drive that particular motor and then you've got the properties of that

**Dave Jones:** particular motor, I'm assuming. Is that how it works? Cuz you don't want to leave the encoder Do you want to you know, cuz if you have to leave the encoder on when the thing's running, then that's a bit inconvenient, cuz like

**Dave Jones:** where do you stick your encoder at that point? We've got it on the shaft here, but you know, you could have something coming off, of course, but that's not nearly as convenient. So, I'm going to assume that it

**Dave Jones:** maybe does some calibration and stores it for that particular motor, perhaps. That'd be cool. Tell you what I don't like is the screw terminals here. Just soldered onto one half of there. Like I like maybe they're designed for bigger

**Dave Jones:** ones, cuz they're massive holes on there. Bigger bolt hole ones or something. I'm not sure, but then he's just soldered in the pin base ones there. That's a bit how you do it. But, I'm sure this is just

**Dave Jones:** like a you know, a Well, he says it's a prototype, doesn't he? Yes, I a demo of a project, yeah. So, you know, I'm sure that production ones wouldn't have this. Anyway, it's designed to drive two motors and an auxiliary thing here,

**Dave Jones:** which we've just got hooked up to a dummy load resistor. Don't know why. And it turns out I did actually have some clamps here. Not terrific, but I'm sure they're only going to spin up for like the 6 seconds that he said it uses to

**Dave Jones:** calibrate this. So, it should be more than good enough. Fingers crossed. Have I got the polarity correct? Black, black, yeah, negative, positive. I think so. Apply I've got set to 15 V maximum. Let's power it up.

**Dave Jones:** Hello. Beeping. Ah. They're slowly turning. It's doing its calibration. I expected them to go But ah. Is that it? Didn't even do a full rotation. Ah. Okay. Um maybe you can explain in the comments why it's like I would have expected a full

**Dave Jones:** rotational calibration, but maybe just the small steps is enough. Well, I can feel the feel the backlash on that if I try and try and move it. Anyway, I can hook it up to a PC and send serial commands.

**Dave Jones:** Okay, I've got the PC hooked up here. It's 115 uh cable and I'm going to type in try this command. I have no idea what it does, but uh let's give it a whirl. Hang on. Press enter.

**Dave Jones:** Ah. Ah. Didn't do anything. Ah. Hmm. So, I'm not sure why that's working, but thank you very much Oscar from odriverobotics.com. I'll link it in down below for all you motor aficionados who are into motor controllers. I know that

**Dave Jones:** well, David is. He's He's done his own motor controllers and stuff like that. Open source one. Check it out. Um and of course, he works for ABB robotics. Probably knows what he's doing. So, this could be a good way

**Dave Jones:** to get a real precise industrial servo motor using a cheap brushless motor and an encoder. I don't think it works as I mentioned before that you take the encoder off and it calibrates it for that particular motor. I I think you

**Dave Jones:** need the the rotary encoder on there, but gee, yeah. I don't know, but I can I want to see it like spin up fast. Got to clamp down on everything. Anyway, check it out odriverobotics.com. This could be cool. Thank you very much

**Dave Jones:** Edward Frost from Canadagua New York, somewhere in New York. Um I already opened this one cuz it didn't have mailbag on it and I thought it was I haven't actually looked at it but then I realized ah it's probably a mailbag or

**Dave Jones:** something so let's have a look. Oh, it's a coil. Dude, I have greetings. I pulled this unique item out of a light dimmer 110 V. Remove the shrink wrap coil to see what it was. Could you identify what it is called and how it is

**Dave Jones:** does it work? Mailbaggy. Terrific. That's the new name of the segment, mailbaggy. Mail badge. Something like that. Anyway, Edward asked a very interesting question. He found this inside a light dimmer circuit and it had shrink wrap over the top and

**Dave Jones:** he wondered what it was and how what it's called and how it works. Well, let's take a look at it, shall we? Now, anyone with any real basic component knowledge of electronics should know that this is an inductor but

**Dave Jones:** if you're a beginner, of course you're not going to know what this is. It's basically just a coil of wire wrapped around a ferrite core and that creates an inductor. You don't need the ferrite core but the ferrite core actually helps

**Dave Jones:** concentrate the magnetic field and I won't go into inductors but they um store uh energy in their magnetic field and then you can store that and then release it. Now, uh usually in an electronic dimmer circuit, you probably you don't need an

**Dave Jones:** inductor for the functionality of it. It uses a triac in there typically and you don't actually need the inductor. So, what's the inductor in there for? I'll put up a a a circuit. I'll pull one up on uh Google images or whatever. So, full

**Dave Jones:** credit to whoever did this circuit. And it's basically you can use this without the inductor. You can simply short it out and it'll still work exactly the same. So, what's the inductor actually in there for? Well, it's actually

**Dave Jones:** working as what's called a choke. And and it suppresses radiated RFI or radio frequency interference coming back out from the triac switching element in the circuit itself. And that's the purpose of this particular inductor here. But this particular inductor is

**Dave Jones:** actually rather interesting. Look. Here at the end, the the wire like it goes around, it goes You can follow it all the way through, all the way through, all the way with LBJ, and it comes the end and then it

**Dave Jones:** wraps back around and goes back. Now, this is actually what's called a bifilar wound inductor. And what that means is that it basically just loops back on itself and the return path follows the path coming in. So, if the current's

**Dave Jones:** flowing in this direction up this wire right at the end, it'll the current flows back in the other direction right next to it. So, the magnetic field created by that current effectively cancels itself out as it goes all the way with LBJ right along

**Dave Jones:** there in and back out. So, what that does is it effectively gives this inductor, which normally has self-inductance because it's an inductor, it effectively gives it a self-inductance of zero because it canceled the inductance cancels out itself. But it still has the property of

**Dave Jones:** uh storing and releasing a magnetic field. And then in this particular case, we'd have to get into uh the difference between common mode and differential mode inductance and that sort of thing. But suffice it to say a bifilar wound

**Dave Jones:** inductor like this has effective inductance in the common mode but not in a differential mode configuration. So, that's why it's useful for suppressing RFI interference. So, thank you very much Ed with that is an interesting question and the answer is surprisingly

**Dave Jones:** this does nothing to the operation of the actual light dimmer itself. But, it's a nice engineering touch to have this in there to reduce all the switching basically the switching noise coming from the switching triac element inside there.

**Dave Jones:** And yeah, and I if you bought it from China and they're on eBay for a dollar delivered your light dimmer, it's probably not going to have one of these cuz that's just extra component cost and then it just spews out radiates out and

**Dave Jones:** via conducted mode all this switching interference. So, that's why a good one will have one of these installed. I think this one's been sitting here for a while. Sorry, M. Pritchard from uh uh Pow- Powys in the UK again, the old

**Dave Jones:** dark once again. So, let's check it out. Here it is. Hi Dave, I'm closing the device that's been sitting in his attic for at least a decade doing bugger all. United States patent. Yeah, 21st century automotive product protec-

**Dave Jones:** automotive protection. Uh electro shield anode rust protector. One of those rust protector thingamabobs. Um sacrificial um anode basically. They're a sacrificial anode type thing. Um there's not much in them. So, my apologies to fellow YouTuber um Ain't Big Ain't Clever who I'll link in

**Dave Jones:** down below and at the end of this video who has actually done a video on this electro shield remote anode [ __ ] Yeah, can you smell it? I can, too. Um and he's gone to the effort to reverse

**Dave Jones:** engineer the circuit on this so we can just maybe can we crack it open? Is it already opened? I'm going to stab my hand here, aren't I? That won't be pretty on camera, but basically there's nothing wrong with anode protection on

**Dave Jones:** cars and boats and other things. They do actually work, but they're sac God, doesn't spring off. Screwing there or something? Anyway, they are sacrificial anodes, whereas this is an electronic woo-woo device and it's got LEDs that tell you which anode

**Dave Jones:** is like, you know, utter utter Oh, there we go. It's a spring. There you go. They've got a bloody What's the What is that woo-woo? Why have they got Why have they got that sort of What is that coil doing in there?

**Dave Jones:** That is That is the remote end anode what? Like What? It that This is absolutely Oh, there we go. Yeah, there's the trick. And we've got more woo-woo [ __ ] coil inside here and let's flip this out.

**Dave Jones:** And Anyway, I won't reverse engineer that, but there's no sacrificial element at all that that that actually gets eaten away. So, let's have a quick look at the circuit here. What have we got? We've got Is that a a triple five going

**Dave Jones:** to have a triple five timer, of course, cuz there's got to have a LED that flashes to pretend it's actually doing something. Look, they're both in series. Anode one and anode two are in series so it doesn't matter whether you got one or

**Dave Jones:** two anodes. I don't know how you have multiple anodes, whatever. Um And it's look, um it's just powered from the input. We've got a diode over there. Sorry. Um diode reverse diode protection. Well, at least they did something. Um and then just 780

**Dave Jones:** 9 7809 voltage regulator powering the 555 timer. So, that's got nothing to do at all with anything. Um so, it just flashes it's just a LED flasher. That's all it damn well is. And then here, we've got two 78L

**Dave Jones:** 05s just driving the output through our woo-woo coil there going to the other side. So, basically it's just like you're connecting up the power to a run at a small amount of whatever amount of current you're doing from like

**Dave Jones:** what? What? No. No, this is like how is this going to do jack all? Like hooking a battery up to your car at one end and just expecting it to do something. Where's the sacrificial element? This is complete and utter

**Dave Jones:** rubbish. We've got another woo-woo ring down here. And like it's just ridiculous. What? What? And I don't get it. If you If you can explain how this magic woo-woo works um as a as a like a sacri ficial anode or

**Dave Jones:** prevents rust protection on your car or boat or whatnot, then leave it in the comments. But that smells like complete and utter woo-woo [ __ ] to me. Thanks ain't big, ain't clever. I'll link in his video down below. Haven't

**Dave Jones:** watched the whole thing yet, but I'm sure it's hilarious. He exposes this thing. And yeah. What? What? What? What? Catch you next time.
