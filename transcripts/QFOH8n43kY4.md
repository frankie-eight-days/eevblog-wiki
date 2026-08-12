---
video_id: QFOH8n43kY4
title: EEVblog #544 - Fluke 5450A Resistance Calibrator Teardown
url: https://www.youtube.com/watch?v=QFOH8n43kY4
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We've got another vintage bit of gear today and it's from a cal lab, something you wouldn't ordinarily get your hands on. It's a resistance transfer standard. It's the Fluke 5450A straight from the mid 80s, I think 85,

**Dave Jones:** 86 vintage, something like that. This would be the transfer standard used for calibrating multimeters back then. It's obsolete now, but you know, it's still not a bad bit of kit and look at the size of it. It is absolutely enormous and

**Dave Jones:** designed to either go into a rack or be a bench mounted like this and basically it is nothing more than a bunch of precision resistors in a box. That's pretty much all it is. Yes, it's got a big LED display on here which

**Dave Jones:** shows you the value, but it doesn't actually measure anything. All it is is basically a bit of automated gear for automated testing of multimeters in a typical calibration lab and the way it works is it's a four-terminal capability, two or

**Dave Jones:** four-terminal measurement. It's got really schmicko precision resistors inside and when you calibrate this thing itself, then you actually program in the exact value of the calibration resistors in here. So, this doesn't actually measure its own internal resistors. It

**Dave Jones:** can't actually do that, but what it can do is actually display the value. What use is that? I hear you ask. Well, in automated measurement with the upside down all the electrons are going to fall out GPIB on the bottom, you can

**Dave Jones:** automate the testing this and it can read the value out of this to know exactly what value the calibration resistor is in here and then it compare it with the device under test, and so on. So, it's a really just a very fancy

**Dave Jones:** automated relay switching box, and it could be interesting inside. Not only in the type and construction of the precision uh resistors, calibration reference standard resistors in this thing, but uh yeah, in the way of physical construction and stuff like

**Dave Jones:** that, keep out noise, leakage, all that sort of stuff in the analog section of it. Could be really interesting. So, you know I say on the EVBlog, don't turn it on, take it apart. And if we take a look

**Dave Jones:** at the specs here for it, I mean, it's, you know, compared to uh sort of modern multimeters, um it really wouldn't be uh suitable for, say, calibrating a modern, well, I don't probably not anyway, calibrating, say, a modern Agilent

**Dave Jones:** 34461A 6 and 1/2 digit multimeter or an equivalent digital multimeter. I mean, we're looking at, you know, nominal tolerances here of 50 ppm, uh something like that. Absolute uncertainty is actually quite good, you know, down in the order of uh 5 ppm or under for like

**Dave Jones:** 24 hours or 1 year, you know, 12 13 uh ppm. And uh they're the various uh test currents, but, you know, compared with say my uh precision resistor uh box I've got here, which is just got a couple of

**Dave Jones:** $20 resistors in a a modern uh modern Vishay resistor. There's the uh part number. Let's get the best one on here, which is the 10K one. You know, we're talking 0.005% or uh 50 ppm accuracy. So, it's sort of,

**Dave Jones:** you know, in the same order as this. And if you compare the uh stability, like, for example, a 90-day stability, you're only talking, you know, 3 ppm or something like that, really quite good. And temperature coefficient here, 1.5

**Dave Jones:** ppm per degree C. And if you compare that to here, this is like, you know, 2 ppm per degree C. So, uh it it's not a huge amount better than just a modern, uh you know, precision, uh resistor from the likes of Vishay

**Dave Jones:** that you can buy for like a 20-odd dollars. But, you know, in practice, I'd bet my money on the resistors in this box any day of the week. So, this is basically a single-purpose resistance, uh calibrator only designed for

**Dave Jones:** calibrating the resistance or calibration checking the resistance ranges of multimeters. That's it. Doesn't do anything else. Unlike, you know, modern multifunction calibrators that can do everything. Uh you know, AC/DC, uh voltage, resistance, current, all sorts of stuff like a Fluke 5700 or

**Dave Jones:** a 50A multifunction calibrator, for example. So, they're they're pretty much, uh made something like this, uh obsolete. I'm not sure of a cal lab that would, uh still be running, uh one of these things, a 5450A. But, if you are

**Dave Jones:** aware of a any cal lab still using them for a specific, uh purpose, please chime in. But, uh yeah, basically, here is the, uh control panel for it. It's designed for two- and four-wire measurement. It's got a two-wire

**Dave Jones:** compensation function, which basically just doesn't do anything fancy. It just adds a uh a pre-entered, uh pre-measured, and pre-entered value on top of the actual internal calibration, uh value in there. So, it just adds a stored number, uh basically,

**Dave Jones:** to the value. And, of course, in four-wire mode, you would just hook this directly onto your multimeter. The sense wires go to the sense terminals of your multimeter. The output goes to the input terminals of your multimeter. That's it.

**Dave Jones:** It's also got a ground, uh shield, which you can turn off and on, external guard, for when you're actually calibrating this thing. And, I won't go into the whole, uh way you would actually calibrate this in terms of, uh shielding

**Dave Jones:** and everything else. But, can be really, really important that external, uh guard shield. That's just not just mains earth willy-nilly. It's, you know has very specific uh requirements in terms of noise reduction for calibrating this thing and then all you do is you just

**Dave Jones:** choose your range and that's it. Um it's pretty basic. It's got a multiplier. So it can only select values of 1 ohm, 10 ohms, 100 ohms in each decade up to 100 megaohms, but you can actually multiply that by 1.9. So if you wanted a

**Dave Jones:** 1.9 K standard resistor, press that button with that one and you would get 1.9 K. It has switched the relays internally clunk clunk and you'd get 1.9 K reference resistor across there. And that's pretty much all there is to it.

**Dave Jones:** It also allows you to display the PPM error, but once again, it's not actually measuring anything. It is just displaying a pre-recorded value in there and that's all it does on the 2 4 6 8 digit display here. It can show

**Dave Jones:** the output value or the percentage error for there. And that's all there is to it. As I said, it's dumb. This display is not reading anything. Just showing you a pre-stored value. On the back, nothing fancy of course. Mains input, IEEE-488,

**Dave Jones:** GPIB standard plus a set of rear terminals on the back for when it's mounted into a rack or something like that. Once again, these are really going to These are low EMF uh connectors in there. You can see they're

**Dave Jones:** probably some sort of a tellurium copper or something like that. Really schmicko. I don't know. What are they worth? Like 100 bucks each to get a replacement set of those? And it's made in the United States of America. Still has the

**Dave Jones:** calibration void seal intact. But the thing has been opened. As you can see, it was calibrated by the Fluke Metrology Lab, but it has been opened. So inside this thing um is going to be I think when we open it

**Dave Jones:** up, we're not going to find anything fancy at all. We're just going to find some uh a whole lot of digital stuff, which of course drives the GPIB and the seven-segment displays on the front. Nothing doing there. That has, you know,

**Dave Jones:** nothing to do with the actual real operation of this unit. What we're interested in is all the the precision reference resistors in here and the relay switching and all that. That will be probably triple shielded or something ridiculous like that. And uh

**Dave Jones:** it will probably be laid out quite well because this thing, you know, if you if you open this thing and you breathe on it, um you know, you're probably going to have to recalibrate the thing. I mean, especially when you're talking or if you

**Dave Jones:** touch it. You know, all the grease from your fingers and stuff like that. Probably not if you breathe on it, but you know, the oils from your fingers, if they get on and contaminate the analog board in here. Oh, here we go.

**Dave Jones:** Yeah, contaminate that analog. Aha, tada. Look at that. And there it is. Check that out. It's actually quite big. I've had to prop the thing up vertically on my bench here to take a look. And as I was saying,

**Dave Jones:** um the uh oils and stuff from your fingers, if they contaminate the analog circuitry in here, as I said, you know, here it is behind all the um shielding in here. Leakage sensitive printed circuit assembly, use special handling. There you go. Because when

**Dave Jones:** you're talking about a 100 meg, you know, a precision reference resistor, which is, you know, 0.005% accurate or something, it doesn't take much in terms of leakage for that value to change. All right, let's just pluck a number out

**Dave Jones:** of our ass to see what sort of scale magnitude we need to get in parallel with our 100 megaohm reference resistor for, you know, it to start being a problem. I chose my Casio FX-61F because it has a parallel button, the only

**Dave Jones:** commercial calculator in existence that ever did, I think. Oh, beautiful. Anyway, um 100 meg in parallel with, let's say, 100 gig, 100 gigaohms. Okay? Let's have a look what we get. Look at that, 99.9 meg. We're still outside of our

**Dave Jones:** tolerance. And if we go divided by 100 meg like that, there we go, subtract one, and uh let's shift that, and times 100, what do we get in percentage there? We're talking, you know, 0.1%. Okay, so that's we're we're just, you know, outside of

**Dave Jones:** our point uh 05% or better. Just just forget about it. So, even 100 gigaohms in parallel with uh that 100 megaohm reference resistor gives us that 0.1% error way out. We need something in the order of, you know, even like

**Dave Jones:** teraohms, even a one teraohm can actually affect this thing. And of course, that's aside from noise issues. I mean, we're at 100 meg at 1 V, you're only talking 10 nanoamps. I mean, you know, it's it's naff all, half a bee's dick. So,

**Dave Jones:** really any noise that gets into this thing can be a real pain in the ass. That's why that um switchable earth terminal on the front panel is such a big deal. So, this is really interesting. They've actually got a relay table here, which

**Dave Jones:** shows you which relays uh energized for each of the particular ranges, a relay map. Look at that, that's just gorgeous engineering right there. So, there's 34 relays inside this thing, and it even gives you the Fluke part numbers for the

**Dave Jones:** different uh relay types there. We've got ourselves what looks like the transformer box in here and the internal voltage selections are in there. And look at this, thoughtfully provided two spare fuses in little holders on the side, accessible. Ah, it's a

**Dave Jones:** thing of beauty. And really there's nothing exciting in there at all. We've just got some range selection switches for the mains range and there's the mains transformer down there. But you know, the main point is it is inside its own shielded box.

**Dave Jones:** They're not taking any chances. And as far as the digital board goes, well, our care factor is around about 0 + 50 ppm. I mean, it's not that exciting at all. We've got a Z80 CPU down here and we've got some ROMs and

**Dave Jones:** some memory and well, whoop-di-do. I mean, all it's doing there's some jumpers down there. Now, that's some programmable jumpers, but really you know, we don't care. Ribbon cable going off to the front LED matrix display and really we don't care.

**Dave Jones:** You don't need much horsepower at all to drive a GPIB and uh then you know, a driver display and store a value. So Check out that monster mains filter cap though. That's absolutely insane. Manufactured by Sprague Compulytics. Geez, Sprague, are they still around? I

**Dave Jones:** don't know, but that's a 22,000 microfarad 15-volt cap plus 85° C rated. Geez, look at the size of it. What the hell do they need that for? It's absolutely enormous for the relay switching I guess. Clunk. And we have

**Dave Jones:** ourselves a date code. Well, it's actually 1970s. Look, copyright 1979 John Fluke Manufacturing Co. So, this model dates at least back to then. I mean, the user manual I got says, I double-checked that, 1984. It doesn't say anything

**Dave Jones:** less than that, but we've got ourselves a date code. We're looking at, you know, 1989 vintage. That could have been changed, but look, you know, we've got 88 vintage parts. Bit of dust on this sucker, but yeah, so this thing was manufactured in

**Dave Jones:** late '80s. You know, '89 maybe 1990. All right, let's lift the skirt up. This is what we want to see. I better not breathe on this thing. I better not sneeze because we could be in trouble if I do that. I definitely

**Dave Jones:** won't be touching anything inside here. I have a poke around with the plastic stick. I was wondering why there's a hole in there. Well, the hole is a finger lift. Look at that. There we go. And I'll try not to

**Dave Jones:** spit when I talk to. I try not to get too excited and salivate over this thing. Here we go. Tada! Holy dooly, look at that. Oh, look at those relays. Look at the resistors. Oh. If we take a look at the relays here,

**Dave Jones:** company I've never heard of, Potter and Brumfield. To Google. Sure enough, Potter and Brumfield still exist, but well, the brand does, but it's now owned by TE Connectivity. And yes, they still make relays. Go figure. And as we've saw before on

**Dave Jones:** the front panel, there are various types of relays in here. This one is a 4.5 V DC one. Yeah, double pole double throw, is it? And on the analog board, we've got ourselves copyright 1983. And down here, we've got ourselves a

**Dave Jones:** bunch of unusual looking Coto reed relays. Of course, Coto, one of the best brands in the business in terms of you know, low leakage, high performance relays and these would specifically be low leakage types. Had a quick look over

**Dave Jones:** data sheet, couldn't find the exact one, but I found a 1240 series one let contact leakage in you know, up in the order of power at 10 to the power of 14 and I think I've done a video way way

**Dave Jones:** back on relay matrices for measuring high value resistors. I will try and find that and link it in. And now precision resistors in this thing, check them out. They are manufactured well, I assume they're manufactured by Fluke. They've got

**Dave Jones:** individual part numbers or Fluke part numbers I presume and look at they've got two in this case 40.5 k point double 05% you know, I technology I don't know some sort of wire wound. And the point of low 5% does

**Dave Jones:** seem to be the best that they've got in here we can see but some are you know, point 01 the ones that you know, aren't as critical is another couple up there point 01 point double 05 for 4k ones 1.8k.

**Dave Jones:** Once you get down in those values point one there's another 162 ohms for example and here we go these low value 40 ohm ones point 05% each but take a look at the configuration. What we've got here is four paralleled 40 ohm resistors so

**Dave Jones:** that gives us a 10 ohm better than point and then that 10 ohms in series with another 10 ohm there and then we've got a then that is in series with 262 ohms in parallel and check out the

**Dave Jones:** configuration. It's you know, it's all over the shop. They've got some complex arrangement here, that's for sure. And then we've got some 280 ohms in parallel, and then we've got uh 1.62 Ks here, and then that's branching off there, and no, and then 1.8k. So,

**Dave Jones:** this really long string of precision resistors. Look at that, isn't that pornographic? Special low leakage Coto relays. Well, of course, on the very high side resistor values. This one is uh you probably can't see that, but that's 81 meg. There it is, and it looks

**Dave Jones:** like that is you can check the arrangement down in here of this string with the relay switching in there, and they're 4.5 meg a pop, and these ones here Yeah, these are all 4 and 1/2 meg getting down to 450k here. So, this part

**Dave Jones:** of the circuit is where our leakage really matters. And you can see that they've conveniently marked the uh tap points. I mean, there's the 19-meg tap there. So, when you include that 1.9 multiplier, when you switch that button

**Dave Jones:** on the front for the 1.9 multiplier, there we go. That tap for the 10-meg range, that's the tap it's going to use, and then there's the 10-meg tap there, and so on down the string. There's the 1.9 meg tap, there's the 1-meg tap. And

**Dave Jones:** you can bet your bottom dollar that they know the leakage of this board down in here, and the solder it it's got that crinkly solder resist coating on it. Fluke really would have done their homework on that, you

**Dave Jones:** can bet your bottom dollar. But, of course, when you get to the really top end of the range, the 100 meg, the PCB itself is not good enough. You get too much leakage. What do you have to do?

**Dave Jones:** You have to have special low leakage insulators like that, with the copper removed from around there and then you have to run insulated point-to-point wires like that right into special output relays like this. They couldn't those Koto ones that we looked at

**Dave Jones:** weren't even good enough. These are electro brand ones. Wow, look at those. How much do they cost each or did cost each? There we go. Electro brand another one I've never heard of R8538. Couldn't find any info on that on a

**Dave Jones:** first pass except that Electro were bought out by Hamlin. So, you know, I'm not sure if you can still buy those. So, check it out. We've got the input coming over here switching through here once again on these

**Dave Jones:** isolated standoffs here all point-to-point wiring. They cannot use the PCB. This wire down there is sneaking off through a hole in the board. Nah, only air is good enough for this. And for those who love their connectors, look at that low EMF

**Dave Jones:** tellurium copper, no doubt. And in all the excitement over the pornographic relays, I missed this little kludge. Look at this. A 7805 linear regulator that was supposed to just probably be freestanding in the board there or maybe you know, attached

**Dave Jones:** to the back panel there. They've Look, it looks like they've done a staggered offset. Maybe they didn't get the PCB right to line up with the chassis or vice versa. So, they've I don't know. They've done a kludge there mounting it up off the

**Dave Jones:** board and there's a there's a seal pad in there to insulate it from the back, but jeez, look at that. And they've done gone to the trouble to add a flat flex there. Unbelievable. I mean, it's not a

**Dave Jones:** huge amount of current, obviously, but I you know, your guess is good as mine. Who goofed up there? So, you can really see the arrangement of the resistors here. I mean, here's our 10 ohm tap, 19 ohm tap, 100 ohm tap, 190 ohm tap,

**Dave Jones:** uh and so forth up there. Blah blah blah. It goes around like that. Comes down here like this. But, what did it say? Is Well, there's our com. That That says com down there. There's our common terminal. But, I don't see the 1 ohm

**Dave Jones:** tap. It's not there. And if you're curious, uh 10 ohms the spec for that or the nominal tolerance is uh 500 ppm or a .05% um in terms of absolute uncertainty, we're down to about, you know, 40 50

**Dave Jones:** ppm, something like that. So, that's basically to get that uh .05%, we're looking at uh 5 mΩ uh maximum error there. So, in terms of, you know, relay switching, going all the way through the wire into the front panel and all that

**Dave Jones:** sort of stuff, um that stuff Well, it doesn't have to be better than that. But, in terms of the uh you know, the stability, I mean, you can calibrate the uncertainty out of all that. But, um you know, still, it's got to be very very

**Dave Jones:** low. These relays have to be ultra-reliable in terms of uh contact resistance. So, I don't have the uh schematic for this one to hand. If anyone does, if anyone actually has the service manual which has the front end

**Dave Jones:** schematic in it, then uh that would be fantastic. The uh actual, you know, so we can see the actual relay arrangement. Wouldn't surprise me if they, you know, parallel paralleled up some relay contacts or something like that for

**Dave Jones:** these really low order ranges. I can't imagine where the 1 ohm range is actually. Haven't found it yet. Mhm. Shielded can. Wonder what's under there. Silly me. I did find the schematic in the um in the operational manual for

**Dave Jones:** this thing. It was right at the back. I swore I checked it and it wasn't in there. But, duh, it is. And tada, here's the schematic for the um analog section here with all the relay switching and the wiring and

**Dave Jones:** everything else. Fantastic, all beautifully hand-drawn as you got back in those old days. So, let's take a look at the string here. Here we go. Here's our 1-ohm resistor and our 1.9-ohm resistor up here, which we haven't found

**Dave Jones:** yet. I bet they're under that can, for sure. And there you go, there's the, uh, four paralleled, uh, 40-ohm resistors that we got before. And then all the various, uh, points. There's our common terminal, so that's sort of on the So, these lower value

**Dave Jones:** resistors are on the flip side of that. And then we went up the chain, went up the chain, and we can switch various configurations of these resistors through to a high and low bus, very similar to, uh, what I've done in a, um,

**Dave Jones:** a previous, uh, relay switching matrix, which I said I'll link in, and I'll try and do that. Um, and going all the way over to our final output, and check it out. There we go. Sure enough, they've identified on the

**Dave Jones:** schematic. Look, they've put a circle around that, which indicates to the PCB designer, you know, that is to be marked off the PCB. I'm not sure, over here, number one, so we're obviously got some detail we'll have to look at, but, uh,

**Dave Jones:** yeah, that indicates that that's raised off the PCB, and this is all just wiring. And there we go, they've got 4401 cable, they're specifying the type used over there. So, all these high impedance, uh, parts are all mounted off

**Dave Jones:** the board. And it looks like I might be right in that they do use multiple, uh, relay contacts in parallel for the one and 1.9-ohm ranges. Check it out. There we go, three in parallel on each line, just to get that contact resistance down

**Dave Jones:** and to within a manageable, uh, you know, tolerance variation over to switching life of the relay. There you go. Unless noted otherwise, there's our note for our points down there. Here we go. Teflon standoffs. There we go. Seven places resistors are specially

**Dave Jones:** matched set. There we go. R5 to R39. So, R5, yep. All of these are five through to R Well, R5, R6, yes. So, all of these are specially matched. So, yeah, they don't just roll off the assembly line. They're probably

**Dave Jones:** individually hand tested, hand you know, hand measured and sorted by, you know, someone rubbing their gray beard as they do it, sorting them into the individual bins and then, you know, putting a bit of spit and polish on each

**Dave Jones:** one. Oh, beautiful. And you can see the beautiful soldered ends of the cans of those resistors there. Oh, just absolutely beautiful. Gold-plated pins. Oh, each manufactured and hand assembled by nude virgins in Utopia land. Just beautiful. If anyone

**Dave Jones:** knows if Fluke actually made these resistors themselves or still do, roll their own specially resistors, please let us know. So, I reckon the one What is it? The 1 ohm and 1.9 ohm resistors are under this can down in

**Dave Jones:** here. Does it have an extra relay down in there? I don't know. I haven't looked at the schematic yet. Dare I open this sucker? It's almost sacrilegious, isn't it? It's just Up. Up. Couple of big standoffs on there.

**Dave Jones:** And uh Yeah, I mean, as I said, you know, even at the 10 ohm range, only talking what was it? Uh 5 milliohms or something to get within that 0.05% band and uh really it's even going to be Well, it's an

**Dave Jones:** order of magnitude, actually, less for Oh, look at those. Yes, wire-wound resistors on card. Look at that. Now, I'm sorry that it's not easy to get in here, but look at the wire-wound resistor. That looks like one big wide

**Dave Jones:** strap on a clear you can actually see through it. You can see that's like a some sort of a you know a Perspex you know acrylic sort of a a sheet that they've wound that on, but you can see that that's tape wrapped

**Dave Jones:** over there and look individually serial numbered down in there. Oh, yeah, these things are definitely manufactured by nude virgins in Utopia land, that's for sure. And individually tested by gray beards, no doubt. Look at that. Beautiful. They would have been

**Dave Jones:** manufactured in house by Fluke, I'm guessing. And check out the dual terminals coming off that thing both there and there on that side. They've just tapped these off individually right at the point they Beautiful. Yeah, so that's probably some form of nichrome

**Dave Jones:** resistor well, you know, wire as in like a flat um strip wire and they've just wound that around that plastic see-through former there and then they've just soldered. Sorry, it's very difficult to get in there, but then there there we go. You can see the strap

**Dave Jones:** coming over and then soldered directly onto that dual point contact there. One of the interesting things to notice is that they have socketed all of these low value relays. By low value, I mean used on the low side of the resistor low

**Dave Jones:** value resistance side of the reference string in there. And I I would have thought that wouldn't have been the go. You would have soldered these directly onto the board, but that certainly makes them replaceable and I'm sure those

**Dave Jones:** sockets are worth a fortune and gold plated to the hill. And you might be wondering why it was shielded like this. Well, this sucker is a coil in there. You don't want anything getting in there because as we saw before these are precision

**Dave Jones:** wire wound resistors. These are already shielded on one end of the can there. So, once again, it's interesting to see the progression in the contact and resistor technology as you go up. Right down at the low end here, special

**Dave Jones:** shielded wire wound, you know, hand manufactured wire wound resistors down in here and multi-contact relays down in here to ensure the tolerance of that. And then we've got some fairly beefy ones for the low value resistors on the

**Dave Jones:** precision string along here. So, once again, you really need good top quality low contact resistance relays, possibly multiple contacts along there. As you go up, you know, in the tens of ohms, the hundreds of ohms sort of range. And then

**Dave Jones:** as you get up into the killer ohm range, you can go for these uh smaller contact resistance By smaller, I mean physically smaller relays. So, you know, probably not as great a or as lower contact resistance as the other relays along here. Not

**Dave Jones:** nearly as critical on these lower ranges down here. And then you get up to these Coto reed relays on the sort of the mega ohm range up here where contact resistance doesn't matter at all. It's down in the noise. You can't even

**Dave Jones:** measure it. What matters right up at this end is the insulation resistance of the relay which wouldn't have mattered for all these ones down here. Who gives a rat's ass what the insulation resistance of these relays is when it's

**Dave Jones:** in parallel with, you know, 1 ohm, 10 ohms, hundreds of ohms. But when you're in parallel with, you know, 10 meg, 100 meg, things like that. As I said, you know, terra ohms, giga ohms, you know, hundreds of giga

**Dave Jones:** ohms up into the terra ohms region actually matters. So, that's why you need those very high insulation resistance values up here from contact to contact, you know, in terms of up to up to the point where it's not necessarily the relay that

**Dave Jones:** dominates, it's becomes the PCB that dominates itself, the surface of the PCB. As I said, you know, oils from hands, contaminants from the air, other stuff. There's no fans in this thing, so you know, nothing's actually blowing through this thing, but dust has

**Dave Jones:** accumulated to the point where down in this section with the really high values, we needed more special relays, reed relays again, and then Teflon standoffs on the board, so we can't rely on the PCB anymore right up at the high

**Dave Jones:** end. And that, as you progress all the way through, you've got different challenges at each design stage. Fantastic. So, I hope you found that rather interesting. I certainly did. And you know, there's more technology which goes into actually designing an analog

**Dave Jones:** section like this for one of these precision precision calibrators. Not only just designing, but manufacturing the precision resistors themselves. And as I said, if anyone has any info on manufacturing Fluke manufacturing their own precision resistors in here, please

**Dave Jones:** let us know. So, there you go. I love looking in high-end gear like this. You always find nice little you know, design tweaks here and there to get these things you know, to get the operational performance of these units. And this

**Dave Jones:** isn't even bleeding edge these days. I mean, this is late 70s, you know, early to mid 80s technology designed to calibrate multimeters of that era. You know, it it's probably maybe not even good enough to you know, calibrate a

**Dave Jones:** modern six and a half digit multimeter like the Agilent one I've got there. So, there you go. Unbelievably fascinating. I love this sort of stuff. And if you want to discuss it, best place to do it is the

**Dave Jones:** EEVblog forum, link below. As always, I'll link in any available data sheets and the manual for this thing, which has some beautifully drawn circuit diagrams for this thing. In terms of like all the digital stuff, all hand drawn, just beautiful. Really is, I

**Dave Jones:** love it. And here it is working connected to my Agilent 34461A 6 and 1/2 digit bench meter and I haven't been warmed up for long, but it doesn't seem to drift what neither of them seem to drift much at all, really.

**Dave Jones:** So, this is on the 1K. So, as you can see, it's got programmed in as the calibration value is a 1.000066K and we're reading 1.000086. Not quite bang on, but you wouldn't expect it based on the tolerance and I can uh

**Dave Jones:** change the range there and you can see it seems to be on the high side for various I can go auto range here, but often it doesn't quite get the auto range quite right. And as you can see, this always

**Dave Jones:** seems to read on the high side of things. And point there you know, there it is 10 meg.

**Dave Jones:** Oh, that one's reading actually lower than what we're getting on here, but as you can see, bit of noise on there, probably have to do some extra power line cycles. And at 100 meg, it's reading low, but on

**Dave Jones:** most of the low ranges, it certainly seems to be measuring slightly on the high side of things. That one's almost bang on. If you see, the auto range doesn't quite work when it's on this thing when it's quite when it's right

**Dave Jones:** near to the full scale there. So, we can actually change that. There we go. That one's reading slightly low, but most of the mid-range stuff seems to be reading slightly high. Now we're getting into tricky real tricky business down in the

**Dave Jones:** uh 10 ohm range down in there. But, uh as you can see, it's um still within spec. Let's take uh 1 K. Well, you know, it's it's within margins of this entire uh uh test setup. Let me give you an

**Dave Jones:** example here. Let's um do this one and see how far we're out in terms of uh percentage. So, we're looking at 1.000085, for example, divided by 1.000066. And we're looking at that, subtract 1, change the register there, and we're

**Dave Jones:** looking at uh times change that to percentage, and we're looking at um you know, round about point double oh, uh let's say point around it to point double oh two percent or uh 20 ppm. And that is within that is better the difference

**Dave Jones:** there are 20 uh roughly 20 ppm or point double oh two percent is within the 24-hour accuracy spec of my Agilent bench meter here. So, as you can see, um you know, which one's right, which one's wrong? Uh

**Dave Jones:** you know, we we just don't know. We would have to uh take this to a standards uh cal lab that has an order of magnitude or better better than this uh Agilent unit and certainly um at least maybe four times better, say, than

**Dave Jones:** this unit itself to actually have it recalibrated. Uh it doesn't have a cal sticker on it. I have no idea when it was last uh actually calibrated and these values actually programmed into the thing. Have no idea. So, who

**Dave Jones:** knows? It may not have It might have been 10, 15 years ago. I don't know. It may have been a couple of years ago. Got no idea. Anyway, it does uh work, but hey, um because the resistors are ultra

**Dave Jones:** stable in this thing, um we could just have this re- recalibrated. We just hook it up, take it to a standards calibration and program in the new values and bang, I'm sure it's not going to drift a sausage. So, as always, if

**Dave Jones:** you enjoyed it, give it a thumbs up. Catch you next time.
