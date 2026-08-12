---
video_id: lOs4A2OL2tM
title: EEVblog #1237 - Old School Teardown: HP3785A Jitter Analyser
url: https://www.youtube.com/watch?v=lOs4A2OL2tM
source: youtube-asr
---

**Dave Jones:** Hi, it's random teardown time for an item from my bunker. This one I got at the dumpster dive quite a few months back. I've done a video on that. Might have to link it in down below and at the

**Dave Jones:** end if you haven't seen it. Anyway, look at this gorgeous bit of kit. Hewlett-Packard. None of this Agilent or Keysight rubbish. 3785A jitter generator and receiver. Isn't it a thing of beauty? Look at the old school HP buttons on it.

**Dave Jones:** Oh. And sorry, I've got to turn it on before I take it apart cuz I got to show you the displays on it. Let's go. Oh. Big fan whir. Oh. I can see see the LEDs flickering. Can't see those in real life. That's the

**Dave Jones:** That's the shutter speed of the camera, but Oh, look. I got bubble LED displays. Oh, love them. So, this is quite a specialized bit of industry kit. It's not something that you'd find in a general lab. What is a jitter generator

**Dave Jones:** and receiver? Well, you all know about signal jitter where your signal can go just have a little bit of diddle wiggle wiggle wiggle yeah on it. And it jitters back and forth and that can cause data errors on on serial

**Dave Jones:** transmission systems among a whole heap of issues. Well, this particular jitter generator and receiver is designed to simulate and measure jitter as well. And basically our performance analyze telecommunication or or phone line based systems. Hence 120 ohm balanced lines

**Dave Jones:** here and stuff like that is designed for to meet the CCITT standards of the old CCITT telecommunication standards right up to DS3 or you might know that as like a T3 which I think this will go up to like 36

**Dave Jones:** megabits per second. So, you know, it's it's not vastly fast. It's designed for like old school telecommunications systems, but it's designed to like, you know, certify those, qualify them, test them, troubleshoot them, installations and designs of various telecommunication products. And I just

**Dave Jones:** love the old school buttons on these. They've got the classic click on it. Beautiful. So anyway, I won't pretend to know anything about like testing telecommunications systems and phone standards and all that sort of jazz. Anyway, this bit of kit is

**Dave Jones:** designed to measure and talk to that. It's got HPIB, of course, we could control it with the our new ethernet GPIB controller, but anyway, I just love the bubble displays. They're gorgeous. If you haven't seen those up close,

**Dave Jones:** they're actually like they are little LED displays in their little LED segments and they've got little like a lens bubbles on them that make them appear bigger than what they actually are. And these were very popular. You've seen them in

**Dave Jones:** various calculator, vintage calculator teardowns I've done over the years and stuff like that. And they they're just fantastic. Ooh, you can see my macro lens. Anyway, this does appear to work. So, you know, we're getting all the requisite displays. Oh, it looks good.

**Dave Jones:** It's responding to the key presses. When you actually power it up, it goes through a power on self-test and and yeah, it's so I presume like do not use until tested and calibrated. Last calibrated in '96. So, let's tear down this beautiful bit

**Dave Jones:** of kit and see what's what. I don't think we'll find much surface mount rubbish in here. There's the back for those playing along at home. It's got proper Look, you've got to pull these out, those latched switches, so you

**Dave Jones:** can't accidentally like drag cables around the back and and bump them. So, that's a nice attention to detail. I LIKE THAT. WOW, IT'S MADE IN THE OLD DART. I don't know my British viewers. This is fantastic. I didn't know HP made stuff

**Dave Jones:** in Britain. Um, if anyone's got the history of that, I I assume it's a HP product. It's not like some other one re-brands. It's got the H or the HP look and feel. So, yeah. Um, let us know the

**Dave Jones:** history of that. And for those who just like to see it in all its glory, well, this is looking like it could be easy. It looks like uh it's split into two halves, of course, top and bottom. Looks

**Dave Jones:** like we just do a half turn uh screw on here and that might just lift off. That'd be great. All right, so I expect this to be uh jam-packed full of boards and probably uh quite difficult to get

**Dave Jones:** them out, but let's have a It's going to come off. Yep, no extra screws under there and they were half turned, by the way. Oh, that No, isn't that nice? Look at that. Rack base here, we can just take that out and we

**Dave Jones:** get out all THE INDIVIDUAL BOARDS. OH, I thought it'd be like much larger ones, but that's beautiful. It's even got thoughtfully provided teardown instructions to remove the power supply, take out these screws marked with the black rings. Awesome. And you can

**Dave Jones:** immediately see the benefits of the old school design here. Not only from a servicing and aspect point of view, you just take off these uh panels here and each board has uh levers you can just uh lift out like that and the boards come

**Dave Jones:** out. You can replace them, you can work on them, but we got the test points all along the top here. So, that's just uh it's absolutely brilliant. So, fantastic from a servicing point of view, but from a design point of view as well, they

**Dave Jones:** divide up all the functions onto separate boards and they'd each have their own separate schematic, they'd each have their own separate revision. So, if you wanted to, you know, modify the clock board, you had to revise that, you're only revising the one board. You

**Dave Jones:** can segregate the design, you can uh give them to different design engineers. Even the boards can even go to different board layout engineers. And you can like they just compartmentalize the design of this sort of thing when space really

**Dave Jones:** isn't a problem. Like back then, the size of the instrument didn't hugely matter a lot. Yeah, maybe, you know, back then I'm sure you probably could have used some surface mount technology, some sort of you know more advanced

**Dave Jones:** stuff back then and made it more compact, but you know you just didn't need to. So dividing your design up like this just has awesome benefits. So yeah, well then two, four, six, eight, 10 different boards. Interestingly, if you

**Dave Jones:** have a look up here, there's another card edge connector up there. So that seems to go right down to the bottom. So maybe that's a test card access. You can put in some sort of production test card. That wouldn't

**Dave Jones:** surprise me they would have built that into the design of this thing. Maybe it's a like a troubleshooting repair card or something like that. You can put this in it can run diagnostics. It's probably access the main bus which it no

**Dave Jones:** doubt be on the bottom of the board. We'd have to start taking out the boards to have a look at that. But uh yeah, and of course there's no getting away running a ribbon cable. They've done the right angle thing. That's going over

**Dave Jones:** there. That'll be for your GPIB. So it's just easier to run the ribbon than it is to try and design a right angle connector and then get it out the back. That'll be a pain in the butt. So ribbon

**Dave Jones:** all the way with LBJ. And then got a separate board on the front here. That's obviously like front panel, probably just front panel controller. I don't think that'll be a main processing or anything like that. Probably just a

**Dave Jones:** small auxiliary processor here for you know doing the front panel, all the switches, all the LEDs. They've got some encoders and things like that. So I I think probably a Although like how much processing is there in this thing.

**Dave Jones:** Color-coded levers. So, I'm sure the service manual for this thing would have been like, "Pull out the yellow card." You know, fantastic. Attention to detail. They don't do this anymore. This is brilliant. It's why I love these vintage teardowns. This is

**Dave Jones:** great. Metal threaded inserts into wood? Is it? For the divider, for the board? Anyway, that is gorgeous. This is the board from the far side of the unit, which I'll call it next to that riser board. We have a date code, 37th week 85

**Dave Jones:** for the firmware here. So, obviously, this is some sort of processor board. We'll take a closer look. Love the gold cap ceramic packages here. Fantastic. And this went over This is the ribbon cable that goes up to the GPIB up there.

**Dave Jones:** So, one of those would be the GPIB controller, no doubt. Check out the rechargeable battery, made in the United States of America. USA, USA, USA. That is crystal socket porn. Look at that. Oh. Now, of course, the problem with HP gear

**Dave Jones:** is that it all uses HP part numbers for everything. So, this 1822293 date code, 42nd week 83 for those playing along at home. Motorola job. HP famously ordered, most of their parts with HP part numbers on them. So, it could be a standard, you

**Dave Jones:** know, Z80 processor, you know, it could be like a standard anything, but HP would order such volume, and they their internal systems demanded that they have part numbers for everything. Of course, you know, we got some standard 74 series logic and stuff

**Dave Jones:** like that, but yeah, HP part numbers for There it is again. So, you can actually look these up. There are databases of uh HP part numbers and cross references and stuff like that. So, you know, I I won't

**Dave Jones:** go to town here. One thing you don't see anymore is look at these tags. These are serial number and revision tags soldered onto the board. That's brilliant. And of course, you get a bunch of test points right up the top

**Dave Jones:** of the board. No point having them down the bottom cuz you want to troubleshoot this thing while it's in the chassis. And a reset button, fantastic. 45° PCB traces, highly overrated. And it's very interesting to note that there's no cutouts here in the card edge

**Dave Jones:** sockets. They don't like extend down to the bottom of the board. That means if you have a look down on the motherboard, as we will eventually, you'll no doubt see that the that the card edge socket on the board

**Dave Jones:** though actually won't have like an end stop on it. It'll like just be out and so the connector will probably stop here and here and the board just extends out the edge of the connector. Neat. Now, if we lift up the second board here, you

**Dave Jones:** can see that we got three cables on this and one of these cables here is Well, in fact, I think Yeah, I think both of them might be all three of them might be buggering off to other boards here. I think pretty sure

**Dave Jones:** this one goes down to one of the other boards. So, here's where signal integrity starts to matter. They couldn't get that signal from there down to the bottom of the edge connector through the motherboard and back up to

**Dave Jones:** the other board. So, they ran a a coax there. Nice. All you relay aficionados are wetting your pants now. Look at these Teledyne relays in metal can package. Ah. Thing of beauty. And is that chip there? Is that a Harris

**Dave Jones:** Technology logo? So, that really is something. There's a whole array of relays and some sort of IC. I'm not sure why. So, the relays are K and the ICs are U, of course. U36 down there. And there's a whole bunch of

**Dave Jones:** those on there. I don't know. Does this board have a name? Does it have a purpose? I don't know. I don't have the service manual for this. Haven't looked it up. But no. No. It's the card with no name. But

**Dave Jones:** obviously, uh Those two chippies under there, little ceramic jobs. They get a bit warm-sky and they put the thermal paste on there and a nice-looking uh spring-loaded heat sink. No vintage teardown's complete without RCA. One really cool feature of

**Dave Jones:** these little black things here, these are actually jumper links with little inserts. There you go. So, you can take them out, get in there, you can measure uh currents, and you can break into circuits and and things like that. Of

**Dave Jones:** course, it's it's not a layout reason. They could have just put the trace straight across there. There's a specific design, servicing, you know, troubleshooting, debug, measurement reason to have that. Oh, I bent the pin. Jeez, they're a real pain to insert

**Dave Jones:** back, let me tell you. And we've had a bit of Harry Hacker here. You can see that you one of those RCA jobs up there. This one's soldered perfectly, but this one over here, someone's had a hack at

**Dave Jones:** that. You can see the flux residue and like a couple of pins around here have flux residue, couple of pins up there. Just a few pins around. So, this one's definitely been hand touched up. Maybe someone was troubleshooting and just getting a bit

**Dave Jones:** desperate. I'll resolder some joints. And here's the board that that first coax went to, went down into here. Here we got some pretty stock standard-looking Omron relays. So, once again, I don't think these don't have a functional It's got

**Dave Jones:** masks. Whatever that is. Reference set. High Q standard option. Maybe that, you know, option on the product or whatever. Um yeah, anyway, I don't know. Look, I'm not going to go into design detail and get out the if you even can get the

**Dave Jones:** service manual for this. I'm sure it's out there somewhere. If anyone has it, if I can't find If I find it, I'll link it in. If I can't find it and can If somebody has it, please send it. So, that cuz people love

**Dave Jones:** to check out the service manuals and it will no doubt be an absolute thing of beauty and a joy forever. Let me tell you. I I guarantee it. Is it the on? And we can see the sockets down in there. As

**Dave Jones:** I said, yep. They've got the ends cut out so the boards you don't have to like you can just make them square boards. Nice. You get more on a panel. They've even put plastic guide protectors on there for the cables so that the cables

**Dave Jones:** don't get caught on any sharp edges on the metal work. Once again, attention to detail is incredible in this thing. More attention to detail. You take out this board because this coax had to travel all this way right across they decided

**Dave Jones:** just to put a little tie in for that. That's absolutely fantastic and looks like Oh. We're going to get some more large socket porn. Look at that. Look at that. So, there's not a huge amount on that. Just a bunch of discrete over

**Dave Jones:** here. We've got some They They actually Yeah, they'd be uh they'd be oscillators. Really? Like, you know, Colpitts variation type oscillator with various crystals. They'd be for the different bit rates, but they've devoted an entire board to that pretty much. Wow. Uh-huh,

**Dave Jones:** those white things, they're the uh they're the fuses on each board. And it actually has a label on the top of this saying each board uh may be individually fused for its own protection. Neat. And there it is. It's got a glass top on it.

**Dave Jones:** Never seen a fuse like that before. But look at this. They put room for a spare. Aw. Wow. Well done, the design engineers at Hewlett-Packard. That is ridiculously good. Oh, I know what orn is now. It just dawned on me now that all the

**Dave Jones:** boards said the same thing. Orange. They can They knew at the PCB design stage that they were going to put orange levers on there. That is ridiculous. Is this This one has yell for yellow, but it's actually green. Oops.

**Dave Jones:** Goof. Re-spin the board. Oh, some of that newfangled HC rubbish. Anyway, we've got more of those uh ceramic dip packages over there with the heat sinks. Bunch of uh chippies down here. Bunch of digital stuff. Geez. Are there any

**Dave Jones:** Portuguese fabs left? Anyone? Bueller? Bueller? When was the last time you saw a Portuguese manufactured chip? Anyway, some big ass carbon resistors up there. Tons of metal can packages. Meh. Oh, now we're stepping up the coax action. Look at that. That goes off to

**Dave Jones:** one of the uh BNCs on the front panel. More socket porn. More spare fuse porn. Ah, this just This video is demonetized. Maybe I wasn't paying attention, but I don't think I had uh saw Tag Tantalums here before.

**Dave Jones:** Tag Tantalums, look at this. The uh 10 amp plague. So, anyway, yeah, they they're notorious for catching on fire, the old tag tents. Yep. Does anyone use them anymore? And this looks like a output driver board cuz we've got more

**Dave Jones:** big coax's going to the BNC's on the front. Oh, they've got the correct color. They've got it. Red. Well done. Anyway, there's another just pin cable. What's that a little Is that a little output transformer, perhaps? What's the designator on that?

**Dave Jones:** There is none. Huh. Anyway, and they're getting more serious about their tag tents. That's some pretty decent size ones. But, yeah, I don't know. Some sort of output driver board. Meh. And more. It's got to do a bit more than that. Huh.

**Dave Jones:** That's not an output driver board. That's an output driver board. Yeah, got a whole bunch of the double ceramic chobies over here with the two big coax's going off to the front there. And yeah, even even the poor little can packages over

**Dave Jones:** here had to get some little flowery heat sinks. Aren't they cute? Those little packages. Yeah, little bit hot ski, so they just whack some fins on there. Once again, I think that's probably some sort of transformer. Oh, that could

**Dave Jones:** be for the 120 ohm balanced line, perhaps. That would make sense. And there's the base of the unit. It's all pretty much just power and like some like main signals, not any of the high frequency stuff. As I said, that all

**Dave Jones:** goes over the coax. And by high frequency, I mean, you know, tens of megs. There's the power supply board for you power supply aficionados. We've got a switch mode supply. You can tell up there. We've got little heat sink. That's all insulated

**Dave Jones:** individual devices on there. We could probably have a look at those. Ooh, no. Oh, no, diodes. Oh, look before you yap on, Dave. They're obviously diodes. Look at that. Fantastic. So, that's that's our Is that a bridge rectifier?

**Dave Jones:** Terrific. Anyway, some more custom transformers happening down here and the caps. What brand? They'd be genuine. Oh, Sprague. Sprague. Sprague fanboys go wild. We've got ITT. Geez, there's a few different wins and Nippon Chemicon, of course. There's a few different wins and

**Dave Jones:** Kemet. And Kemet caps. Ah, it's all over the place, but they're all top-notch brands, of course. That's why it's still working after all these years. Oh, there's a there. Couple of little custom down there. Look at that. They're quite neat.

**Dave Jones:** Wow. Really going to town on that custom supply. And please forgive me for not getting out the display controller board, but yeah, there's screws in there which you have to get out the rest of the chassis. So, that one is not hugely

**Dave Jones:** serviceable like the other ones. Unfortunately, you got to get the you know, you got to take out the whole cage and everything. So, yeah, nothing special. We've seen all the good stuff. So, there you go. I hope you enjoyed a

**Dave Jones:** look at that 3785A jitter generator and receiver teardown. It's absolutely brilliant. They just don't make them like this anymore. More. Oh, well, you know, some companies do. Depends. Like if you've got the room, big industrial stuff and things like that. You know,

**Dave Jones:** you still do plug-in cards. It's quite common. And then you segregate your design into the different blocks and things like that. Then your design team can work on the different parts and you can modify different parts and you can

**Dave Jones:** isolate problems by replacing boards at the troubleshooting stage and things like that. But, yeah, like in test gear and stuff like that anymore, like it's just it's just not a thing. And this thing's just wonderful. I wonder how

**Dave Jones:** many of these things they actually sold in the end. If anyone knows like how popular these things were, did every single, you know, telecoms tech in the business have one of these back in the day and carted out in the field and, you

**Dave Jones:** know, set up measurements, let us know. I'm sure there's somebody out there who's extensively used one of these. Can service one of these puppies in next to no time, let me tell you. I love these quarter-turn screws.

**Dave Jones:** Is it still going to work? Course it will. Beautiful. See if we get anything out of it. Well, we have a 2.048 meg clock out. Winner, winner, chicken dinner. And then 8 meg, well, 8.448 meg actually, and option. Don't know

**Dave Jones:** what option is. And we don't have the option. 34 meg, 34.368 for those playing along at home. Well, I'm pretty much embarrassing myself trying to use this thing. You know, I I just can't get this manual control to

**Dave Jones:** adjust the generated jitter. And we can like set through the data. So, if we do that, of course it vanishes through the word. So, we put it through the clock and we generate our clock, no problems at all. But then how do we generate our

**Dave Jones:** jitter on the clock? I might have to RTFM, but yeah, I don't even know. I forgot the manual. Anyway, I'm trying. I'm doing my best. I'm randomly pushing buttons like a monkey and uh well, not much is happening.

**Dave Jones:** Nothing's happening, actually. So, if you like that video and if you like just random bunker teardowns, then please give this video a big thumbs up, share it and all that sort of stuff because you got to share it these days because

**Dave Jones:** well, YouTube doesn't do a very good job of that. Anyway, as always, comment down below or over in the EVBlog forum. And I'll have high-res teardown photos of this. I always take photos with my macro camera, my macro lens. And yeah,

**Dave Jones:** high-res photos over on the EVBlog.com, which links to my Flickr account. Catch you next time.
