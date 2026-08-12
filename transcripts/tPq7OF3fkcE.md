---
video_id: tPq7OF3fkcE
title: EEVblog #507 - The First ARM Processor Computer - Acorn Archimedes A3000
url: https://www.youtube.com/watch?v=tPq7OF3fkcE
source: youtube-asr
---

**Dave Jones:** Hi. Yes, it's vintage computer time again. And yes, we're going back to the '80s, my favorite decade. And we're going to the UK this time around to take a look at the Acorn Archimedes A3000 personal computer. Dates from about 1989

**Dave Jones:** or thereabouts. There is an Archimedes version the A started with the A or the 300 model. This is That was 1987. This is a 1989 model. So, we're talking about, you know, 23, 24 years ago. Quite some time

**Dave Jones:** back. Developed by Acorn computers in the UK. They were very popular. This is the BBC Micro branded model and it was the last BBC microcomputer ever made. They started back in the '70s as a Well, not really spin-off as a competing to

**Dave Jones:** Sinclair computers. The guy who founded Acorn actually used to work for Sinclair and went, "Well, bugger that. I'm headed off to form my own company, Acorn." And if you want to get all the really great detail on that, watch a movie called

**Dave Jones:** Micro Men. It's fantastic. Highly recommended. And this is one of their Well, the last BBC micro machine. Now, one of the most famous things about this is that this was uses the first ARM microprocessor. Cuz a lot of people

**Dave Jones:** Well, everyone's familiar with the ARM micro, right? It's used in all your phones. It's used in everything these days. But a lot of people don't know it actually came from developed originally by Acorn computers back in the '80s. And

**Dave Jones:** it started with the ARM 2 processor. There was no ARM Well, there was an ARM 1, but it never made it into a production machine. So, this one uses the ARM 2 architecture. And ARM stands for Acorn RISC machine. Go figure. So,

**Dave Jones:** anyway, this should be really interesting and it doesn't work. Supposedly, I got it from eBay and it said there's no video output on it. So, hopefully, it'll turn into a repair video as well as a teardown. You know I

**Dave Jones:** hate it when I buy stuff on eBay and they just work. Unbelievable. I want something that doesn't work for a change. Let's go find out. And here it is as a all-in-one unit very similar to the Amiga, of course, and the Atari ST of

**Dave Jones:** the day. Now, the previous version to this in '97, the 300 model, it was a separate keyboard and more of your square box type thing. This is the A3000, which is the complete integrated unit. And interestingly, I like the fact that it

**Dave Jones:** basically copied the IBM PC AT keyboard layout. Really, it's essentially identical except they got caps lock down here instead of control up here, but you know, it's essentially identical. I assume that would have been a decision to make it, you know, appear more more

**Dave Jones:** professional. Everyone was copying IBM back in the '80s and everything they did. So, this sort of AT-style keyboard form factor became a bit of a de facto standard. And as detailed in the movie The Micro Men, this is a BBC Micro

**Dave Jones:** Computer, the British Broadcasting Corporation, the TV network. They gave the contract to Acorn back in the '80s to develop a microcomputer for a new TV show they were going to do because, you know, micro personal computer revolution was all the rage and

**Dave Jones:** they gave them the contract famously over Clive Sinclair, much to the Clive's disgust, of course, and that makes the premise of a lot of the premise of the Micro Men movie. And if you believe the history, one of the

**Dave Jones:** reasons they chose the name Acorn is because they wanted it to be before Apple in any directory. There you go. Well, they failed because Acorn are no longer around and Apple are going great guns. Go figure. Although their legacy

**Dave Jones:** does still live on, that ARM processor is now used in, you know, 95% of the world's mobile phones. And unfortunately, this one is engraved with the name of the school, the Bigelow Platos School here in Sydney that it

**Dave Jones:** came from. Bummer. Anyone know how to get remove scratches like that? You can buff it out. I don't know. I'll just leave it there, I think. We've got our vent holes on the top here. I have no idea how warm

**Dave Jones:** this sucker gets, but on the side here, we've got a 3 and 1/2 inch floppy and nothing else on the other side except the power switch. But on the back here, curiously, check out the expansion connector. Uses the classic DIN 41612 connector that's

**Dave Jones:** used in the VME bus, sort of, you know, the industry standard industrial expansion connector. I love that. I don't know how many others micros of the age actually used the the 41612 connector. Analog RGB monitor, mono video out, headphone port, parallel

**Dave Jones:** printer, 9-pin serial port, and Econet, which I guess was a modem interface. And there's some sort of serial number card in there. I don't know what's what's going on there. We'll find out when we open that sucker. And no IEC

**Dave Jones:** power connector, just a fixed cord. And there's also a big expansion slot on the back here, which has nothing fitted, obviously, but you could get mighty ports and you know, various other expansion. I think there was even a

**Dave Jones:** ethernet option or something like that as well. And there's one thing you won't find on the back here, though, which was, of course, any big high-powered machine like this for its day, of course, used a graphical user interface.

**Dave Jones:** Where's the mouse port? Well, it's on the bottom. And there it is, tucked away in there. I mean, it's a little DIN plug in there, and that's pretty horrid. I mean, you know, almost as if like it's an afterthought. Oh,

**Dave Jones:** we'll just whack it on the bottom instead of the back. I don't know what they were thinking there at all. Just crazy. You also see that there's a removable cover here with a space for two AA batteries, but there's no

**Dave Jones:** contacts fitted in here at all. So, I guess that didn't have the option, and that was for the battery-backed memory option. And as you can see now, they're relatively serious about the airflow on this thing. There's some fixed plastic

**Dave Jones:** standoff feet molded into the case down here. Presumably, this was for an expansion that part of the expansion connector, the 41612 expansion connector up there. And yeah, vent holes, so the power supply's going to all be in this

**Dave Jones:** part, and they wanted to get some airflow through the thing cuz these things use quite a bit of power. And for the efficientados playing along at home, there's the serial number. Designed and manufactured in the UK by Acorn

**Dave Jones:** Computers, Cambridge, England. Fantastic. Copyright 1989. Good year. Apparently, 2 meg of RAM fitted and power on no video. So, I don't know when that note was written and how long it's been in that state or even if that's right at all.

**Dave Jones:** Only one way to find out. Power it up. Yeah, yeah, I'm going to break my own rule by turning on before I tear it down. Sue me. I've got the scope hooked up to the mono composite video output,

**Dave Jones:** so let's switch it on and see if it uh see if it works. No. We saw that go high, but uh that's just stuck there. We're getting no composite. It I do hear a beep, but there's uh there's no video coming out of this

**Dave Jones:** thing. I don't hear the disk drive or anything. So, excellent. This gives us a chance to crack this sucker open and uh maybe do some troubleshooting. That's the plan anyway and uh no that's a good fault to have like well

**Dave Jones:** good and bad good in that you know we've got a defined fault no video but why has it got no video? Is it part of the Is it uh the video circuitry at fault? Is it the uh um

**Dave Jones:** Is it the digital part, you know, if the ROM's gone bad? Um all sorts of stuff that it could be. Couldn't be as simple as the power supply, of course. That's the first thing we're going to check. First rule of troubleshooting, thou

**Dave Jones:** shalt check voltages. As it turns out, the designers have been very nice and they've given us these tabs here which allow us to just snap that whoop top cover off. That was the floppy driver going a bit how you doing there but uh

**Dave Jones:** that should just lift off and that's really quite neat. Yeah, the floppies are flopping around in the breeze. No pun intended but there you go. Very nice. Not too dusty, either. So, pretty uh standard construction technique for the day and

**Dave Jones:** for this uh model uh you know style of machine the all-in-one integrated uh keyboard the slightly sloping keyboard which just lifts out to reveal the board underneath there the main board. It's just got one single main board. We've

**Dave Jones:** got some uh a bit of expansion that looks like our memory expansion board there. We've got our the Econet uh module on the back and separate power supply board with a safety cover over that. And the good part about this machine is that we can

**Dave Jones:** get the full service manual and technical reference manual for it with the full schematics as well. Fantastic. So, I'll link those down below and it looks like they're not just crappy scans, either. It looks like they're from the original digital format, which

**Dave Jones:** is great. Now, we'll take a look at this in uh more detail later, I think, but I just want to I'm going to lift the keyboard out here and have a basic look around to see if there's anything

**Dave Jones:** obvious, and then we might power it up and just measure the supply voltages as a first step. Check this out. The battery has gone kaput and leaked all over this board. Look at that horrible green all in the

**Dave Jones:** contacts of the chips down here, and even when I pulled out the keyboard uh uh flat flex here, you can see that I think possibly some of the contact has come off there. So, uh that's that's pretty horrible. And well, it's likely

**Dave Jones:** that's the reason this sucker is not going to work at all. That is I'd be surprised if that didn't have any effect on this thing whatsoever, but we should at least power it up and see that the supply voltage is correct, but this

**Dave Jones:** is going to be a pretty horrible repair. Uh look at that. And of course, one thing you'll notice is that the battery is missing. So, clearly, you know, it hasn't just rusted and fallen off. I don't find it in here. So, somebody has

**Dave Jones:** had a crack at this thing, and well, they've opened it up, and maybe the battery did fall out or something. They've gone, "Ugh, that's not repairable." and just thrown up their hands in disgust, but that's pretty awful leakage. Look at

**Dave Jones:** that. And all of the date codes on our chip here seem to indicate a rough manufacture date of early 1990. I mean, here's the two processor. There it is. Woohoo, in all its glory. And basically, everything is like early '90s, but if we have a

**Dave Jones:** look over here at the ROMs on this thing, they've got 1992 on them. So, I can only presume that, you know, this thing didn't hang around for manufacture that long. Then, they wouldn't be using chips that old, I doubt it. So, I reckon

**Dave Jones:** maybe someone has got in there and replaced some new RISC OS well, RISC OS 3 ROMs at a later date after manufacture. So, as a rudimentary first test, we're going to measure the supply coming out of this thing. There's only a

**Dave Jones:** single red and black 5 volts coming out of here. There's a earth connection, but that's it. So, pretty much it's it's all 5 volt logic on this sucker. So, hey, there we go. 4.97. Spot on. So, yeah, it doesn't work. So, yeah, maybe

**Dave Jones:** look, you know, we've got ROM yeah, all sorts of corrosion in the contact on these ROMs down here. I mean, I'm surprised I'd be surprised if they're still intact. Looks like, you know, mouse circuitry around there, but yeah, that's just it's not going to work

**Dave Jones:** if the ROMs aren't working, that's for sure. And there's plenty of custom ASIC devices. As I said, there's the ARM Acorn processor manufactured by by VLSI. And if we have a look, there's plenty of VLSI stuff around here.

**Dave Jones:** There's another one. It's got a looks like a memory controller there. Custom Acorn memory controller. What? And they as usual in the looks like they've given them names very common back in the day. Arabella. There we go. Whatever that is. Like that's a

**Dave Jones:** like expansion or something. I don't know. I haven't actually read the technical description of this thing. Parallel interface, something like that. And then we've got the Albion chip, which looks like it handles the parallel printer port stuff plus other stuff. And you

**Dave Jones:** don't see memory in those single inline packages anymore these days. Unbelievable. And of course, they've got an expansion board up here. That's for an extra 1 meg. So, there's 1 meg on the main board plus one on the expansion.

**Dave Jones:** But, it was capable of expanding far beyond that. Just in case you get lost around the circuit. So, I'm not even going to bother probing around here, you know, the main oscillator or something, see if the processor is running. Really,

**Dave Jones:** you know, if you want to restore this, you've got to clean up that anyway. So, you may as well do that as a first pass. There's a couple of more screws down here. There's one little retaining clip there and uh

**Dave Jones:** that pops out. Looks like no damage on the bottom. So, we look to be okay there. There is some uh surface mount action happening on the bottom. We've got some surface mount resistors there, the odd cap. That's interesting. And I'm

**Dave Jones:** definitely going to want to get these ROM chips out. They go in this order, 1 2 3 4. They're nicely numbered for me, so I know to put them back in the right place. And yeah, we've got some

**Dave Jones:** corrosion on those pins. That's no good. Oh. Yeah, some of the pins in the socket look uh pretty awful, in fact. We might need entirely new sockets on this thing, I think. And of course, I can put these ROMs in my uh

**Dave Jones:** EPROM programmer and read out the contents as well to see if they're okay. I don't know. I presume you can get maybe the ROM dumps on the internet uh somewhere like that if the chips had actually failed. But uh these are mask

**Dave Jones:** uh ROMs, so it's not like they're um EPROMs. And the contents um these will be much more reliable than the windowed uh EPROM type, which can actually um uh have their uh charge bleed out over time. So, these ones still should work a

**Dave Jones:** treat, but those sockets are horrible. And that is truly horrible. Look at that. You can see that one half of the dual wiper contact in there is just uh it's just completely fallen out. Absolutely atrocious. Another one's just

**Dave Jones:** uh completely rotted away. Uh thankfully, the pins on the ROM chips look fine. So, I think if I just uh clean those up, then they shouldn't be a problem. I mean, they the pins on the IC obviously uh

**Dave Jones:** different uh type of metal which wasn't attacked nearly as well as these sockets, but that's just That's just garbage, yep. Got definitely going to need entirely new sockets on this. Have to desolder them out and oh, look, it's almost pretty. Look at the

**Dave Jones:** colors. Wonderful. Now, the real problem with this sort of corrosion, of course, is that it can get under the solder mask of the PCB and it can start attacking the, uh, copper traces as well. And well, if that's the case, we've got a

**Dave Jones:** big bus on the, uh, on the ROMs here and uh, you know, could be all she wrote, you know, unless you want to go around with, uh, mod wires and all sorts of stuff, but if it has made it through to

**Dave Jones:** those traces, yeah, I don't like our chances, but maybe, you know, we could replace the Have to clean it up, of course, and then if we replace the sockets, um, we might be able to and the, uh, keyboard connector, we might be able to

**Dave Jones:** at least get the thing to boot, you know, maybe there's something around here which is really that That resistor just popped straight off there. Better find out what value it was. Anyway, we've got the service manual, but yeah, I don't like the

**Dave Jones:** chances of the mouse port working here, that's for sure. Well, first of all, I'm going to get in there with some, uh, isopropyl alcohol and, uh, just try and get a lot of the, uh, surface contaminant off with a very stiff This

**Dave Jones:** is one of these conductive, uh, brushes, so just want to try and get as much of the crud off as I can.

**Dave Jones:** You can see all the crud that which is really, uh, rubbing off there, but then I'm going to run over it with some of this, uh, flux clean stuff, but really it's looking pretty crusty. Now, we're going to get

**Dave Jones:** this socket out. I've cut out the internal uh supports there, and you can do it the old-fashioned way, just wiggle it uh back and forth, fatigue those pins, and then you can pull out the pins one by one from the bottom side.

**Dave Jones:** Otherwise, you could use a proper uh desoldering tool. And of course, once we've uh tried attempted to get all the gunk off, we're going to have to use some sort of uh corrosion inhibitor to uh stop it corroding even further, but

**Dave Jones:** uh as you can see, it looks like it's the corrosion's already gone pretty far. So, really, you know, you've got to repair the damage and then and stop it long-term. The long-term prospects of this thing are uh just hopeless. And you

**Dave Jones:** can see how it looks like some of the corrosion has started under the solder mask there. So, yeah, the connections might still be in place if we're lucky across these traces, but you never know where one has broken. But, yeah, you could clean it up

**Dave Jones:** and fix it um and possibly get the machine working, but the long-term prospects of this thing uh just uh don't even want to contemplate it. Now, unfortunately, I can already measure that there are breaks in these traces and more than one, too. Unfortunately,

**Dave Jones:** that should be buzzing out from that pin to that pin cuz there's a lot of common pins on these um ROMs, of course. And some of them, I can see they're electrically supposed to be connected. Don't even need to look at

**Dave Jones:** the circuit for it. And there's no continuity there at all. So, clearly, the corrosion has eaten away at the copper traces under there, and I don't even want to think what's under there. It's surface stuff. I don't know. It's

**Dave Jones:** just all It's all horrible. You know, as I said, you might be able to get the thing to boot if you uh put the ROMs back in, of course, desoldered all the uh pins, put in some new sockets, put the ROMs back in, uh

**Dave Jones:** buzzed out every single connection, and then repaired the ones that are faulty with either at the board level like this. You could do that before you install the sockets or you could use mod wires on the back or something like something ugly like

**Dave Jones:** that, but there's a well, there's various ways to repair PCB traces, but no, I'm afraid to say this one is a bit of a loser. I'm I'm not sure whether or not it's worth the effort to resurrect this thing.

**Dave Jones:** Anyway, I'm I'm going to I'm definitely not going to get it working today. That's for sure. So, sorry about this. I thought it would be an electronics troubleshooting issue, not a corrosion repair issue, which it it clearly is

**Dave Jones:** because the thing is not going to boot with all those corroded pins, which just fell out of the ROMs. That's clearly why it it didn't boot at all and generate didn't generate any video. Although, I haven't looked at the

**Dave Jones:** circuit what actually generates video whether or not you know, there's like a a blank video there without the processor booting or something like that. I I don't know, but anyway, that's a loser. Sorry, folks. Anyway, if you got any

**Dave Jones:** good ideas, good suggestions for this thing, maybe I can get it up and running in a follow-up video, but bummer. If you want to discuss it, jump on over to the EV blog forum. That's the place to do it.

**Dave Jones:** Catch you next time.
