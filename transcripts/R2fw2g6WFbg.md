---
video_id: R2fw2g6WFbg
title: EEVblog 1477 - TEARDOWN! - NEW Tektronix 2 Series Oscilloscope
url: https://www.youtube.com/watch?v=R2fw2g6WFbg
source: youtube-asr
---

**Dave Jones:** Hi, it's world exclusive teardown time. We've got the brand new Tektronix 2 series oscilloscope released today. Links down below and this one what is a qualification build. So, there might be slight differences with the final production version. I haven't heard I

**Dave Jones:** don't think so, but just be aware of that. This one was actually hand carried over here by Tektronix and I'll link up here and down below my initial reaction video to this and also a talk with Andy Ted about the design of this thing. We

**Dave Jones:** talked for about 40 minutes just before he had to hop on a plane about the design and build of this thing. So, let's check it out. Isn't that just gorgeous? I love the stand on this thing. It's just fantastic. And yes, we

**Dave Jones:** will tear down the optional battery pack for this thing as well. So, let's get rid of the stand and let's get into it. And the cover for the battery pack here, this actually fits into a slot on the

**Dave Jones:** battery pack. So, yeah, it's just off. We've got the Visa mounts of course and these are the battery pack clip ones as well, but I guess you could use those for mounting if you really wanted to. But, you know, these are

**Dave Jones:** standard Visa mounts. So, absolutely brilliant. So, you can see the tablet-like form factor of this thing even though it's not actually a tablet scope. It's more of a new concept thin portable bench scope which you can you know, mount on various Visa mounts and

**Dave Jones:** then you can convert it into a portable scope if you want using the external battery pack. So, it looks like it's going to be really easy to get into. It just got some torque screws around here and they did say that one of their

**Dave Jones:** design aspects of this thing is that it it is all single board construction. So, and that may have led to design decisions like the lack of the tech TPI probe interface here cuz you like most likely would have required a

**Dave Jones:** second you know, board in there just for the uh connections, uh for the active uh probes, and also why they went with the membrane keypad instead of uh your regular buttons, which then have to be deeper and then probably on a uh

**Dave Jones:** secondary board. But, let's find out by taking it apart. And, looks like these are all self-tappers into plastic, so that's a bit disappointing. I expected some metal threaded inserts there. Come on. I mean, you know, this is not

**Dave Jones:** bottom-of-the-barrel pricing, although, yeah, for tech it is. So, it's just going to lift off? Don't know. Have I forgotten any? Is there another one in the middle? What's going on? Uh is there a sneaky bugger under there? There's four sneaky buggers under there.

**Dave Jones:** Look at that. Is that like a big heat sink under there or something? It just seems weird, and they're offset from the center, so it's almost as if a it's like an operational PCB heat sink thing instead of like being an external

**Dave Jones:** design, it's driven by the PCB layout in there. That'd be my guess. So, this is where the PCB designer might have actually uh driven the or had to feed back to the mechanical case designers what they actually wanted. Um

**Dave Jones:** so, anyway, there we go. There we go. Okay, ready. Ta-da! But, no, I'm wrong. What? No, I'm not wrong, actually. Um I just expected to see a big uh like metal work under here, but you can see that the screws have uh

**Dave Jones:** gone into You can see the all the bypass caps in there and all those uh vias, those tiny little vias. That, of course, will be the main FPGA under there. Could be the acquisition No, the acquisition engine's probably down here near the

**Dave Jones:** front end like this, but there you go. That is um an entire single-board construction. Isn't that Isn't that neat and groovy? And it's actually um smaller than this whole thing, because I'm sure one of the uh complaints will be this

**Dave Jones:** thing, "Oh, why do I need an external battery pack?" Um that was my one of my original thoughts as well. Um well, it's not only for a capacity reason. I mean, this thing is, you know, it is relatively thin. But there are, of

**Dave Jones:** course, tablet oscilloscopes on the market that actually um have internal batteries, and they actually work as tablet oscilloscopes. Cuz by the time you add the battery pack to this thing, it is quite thick. It's no longer sort of a tablet-y uh form factor. So, ooh,

**Dave Jones:** there you go. Got a pin sticking up there. What's that doing? Huh. They've got another pin over here as well. And uh by the way, that is not actually connected through to any sort of uh you know, shielding on the back.

**Dave Jones:** There's no nickel screening. Um this doesn't look uh you know, conductive or or screened at all. The back plastic on that. So, that's interesting. Um but of course, you got the back side of the board, not the front side. But from an a

**Dave Jones:** EMC point of view, that's just rather interesting, isn't it? But uh we do have uh the shield on the uh front end though, but that's a that's a very narrow front end. Wow. And you can see this uh button side here. This is where

**Dave Jones:** all the membrane buttons are. You can see that if they used the one PCB, then they would have that you couldn't have any components on there at all. You would have to like all the circuitry would have to be on this part of the

**Dave Jones:** board. And you'd have to leave at least on the uh top side anyway, you'd have to leave the you'd have to mount all this on the bottom. So, there's obviously a whole bunch of chips down here. This is

**Dave Jones:** the uh logic analyzer inputs. All the logic analyzer stuff. You could have mounted it on the back side. So, they could have Maybe they could have done it. I don't know. I'd have to actually get the PCB files and actually, you

**Dave Jones:** know, play around with and spend a lot of time playing around with this thing from a uh you know, a layout engineer uh point of view. But you can see that the USBs are on the front, but even then,

**Dave Jones:** like, yeah, you would have had to clear out the entire front part of this PCB here uh to get your buttons just on the uh front on the single board. If you're, you know, was so desperate to get this

**Dave Jones:** as a single board uh construction, then which they obviously were. Um I've been told it is single board, and it looks like it. Looks like they don't have anything else under it. So, we'll take it all out and have a squeeze, of

**Dave Jones:** course, but um yeah. Anyway, this is interesting. Here's our big grounding point over here cuz here's our big, you know, they're serious about their mains earth connection, and it gives you a warning when you boot the thing up. Um I

**Dave Jones:** don't know don't know if you can disable it. It's rather annoying, actually. Please ensure the earth terminal is connected, blah blah blah blah blah. But, anyway, they've gone to town on that. Look at that. That's absolutely uh beautiful. It's all heat shrunk down

**Dave Jones:** there. But, this was one of my uh original uh things that I thought about, and you'll see this in my other my reaction uh video, I believe. And, like, why does it have to be on the side? Why

**Dave Jones:** couldn't you have had it on the back? There are some scenarios where having the power connector on the side like this um is beneficial, but there's other uh ones where you don't want it sticking out the side. You want it coming out the

**Dave Jones:** back, or you want at least a right angle connector, but it's not a right angle connector. It's actually the one supplied is um the just an inline jobby like that. But, I guess the good news about that is if you bugger up your

**Dave Jones:** connector, you can actually replace it. So, I do hope they actually sell this um as a replacement part um and or make it, you know, obviously um easily serviceable. So, yeah. So, that is one of the things I

**Dave Jones:** wanted to check. Like, I would have been disappointed if this was a a right angle uh PCB mount uh thing because, like, you know, like a big part of this, especially if you're doing it every day, the uh fatigue of actually uh you know,

**Dave Jones:** actually connecting this connector in and out, it could wear out over time. Of course, that is a distinct possibility, but I did notice it was actually uh screwed in there like that. So, no worries. But uh yeah, they've got

**Dave Jones:** actually a quite a significant amount of space around here and up the top as well. So, I guess in theory, you know, you could have shoved some like 18650s or or something up there for those who are complaining about yeah, why doesn't have

**Dave Jones:** building batteries? Well, you know, technically it would have been possible, but this thing's like a 50-odd watts. I think the brick is about 60 watts watts or so uh maximum. I haven't measured the actual power draw, but yeah, you're not

**Dave Jones:** going to get much uh usage out of this if you just put some 18650s along here or something like that. You know, you could have maybe had like a plastic cover on top of this and then a thin

**Dave Jones:** layer of uh pouch cells or something like that, but then the design gets a bit tricky and then you've got to have, you know, then you can't get the screws through to do this uh sort of stuff and

**Dave Jones:** uh technically I'm a bit disappointed with uh this because these VESA mounts are probably expected like a big bit of metalwork in here, but it's not. It's just the uh back plastic uh backing and uh no metal threaded inserts for these

**Dave Jones:** screws. But, you know, this thing doesn't weigh, you know, a heck of a lot just on its own like this. So, putting it on a VESA arm, it's not a huge amount of stress this plastic's going to take

**Dave Jones:** it. It's just I just expected like a metal bracket in there or something. But, you know, you want to get the weight down. So, yeah, fair enough. And attention to detail here by the PCB designer. Backside flip latch like this.

**Dave Jones:** Um you can almost see this coming about because uh the PCB designer went oh yeah, people are going to come a gasser uh with this one thinking that oh you know, we're going to flip it like this or we're going to pull it out or

**Dave Jones:** whatever. But no, it's a backside flippity-doodah like that. So, really appreciate that as a PCB designer. And the shield for the front end, it just uh lifts off. They've got a whole bunch of uh clips in here, but it just clips off.

**Dave Jones:** And interestingly, um they really didn't need these raised bumps on here. I guess they might have uh changed. I guess that was uh designed and thought about at the time when they didn't know exactly what uh you know, front panel BNC connector

**Dave Jones:** that they're going to use. But you can see that it's not raised there at all. It's the same as the uh ground the center pin is the same as the surrounding pins there. So it doesn't really protrude at all. So maybe they

**Dave Jones:** designed that to change made a change to that that um you know, a bomb changed to that BNC connector later and it doesn't have a big center pin sticking out, which is what you'd need these things for. And they do come out quite a long

**Dave Jones:** way. But yeah, they're actually not needed. This is going to be a very simplistic front end. In fact, I haven't seen one like a 500 meg front end this small because it is software bandwidth uh definable of course. So anywhere from

**Dave Jones:** 70 megahertz up to 500 meg. Uh we've got a relay here and we've got our input resistor here and a couple of you know, passive jobbies and stuff like that. But yeah, it looks like this is not going to

**Dave Jones:** probably not going to be a huge amount on the other side because well, it only goes covers this little small section here. It's really remarkable. But you know, that's the advancement in technology over the years. I'd love to

**Dave Jones:** compare this with like the original MSO uh 2000. Unfortunately, I used to have one of those donkeys years ago, but I don't anymore. So unfortunately, uh maybe I can see some get some teardown photos or something. But I don't think

**Dave Jones:** it went to 500 meg. But yeah, uh these newfangled front ends. So from a product design point of view, I can really appreciate wanting to have this all-on-one board and not have to dick around and have board interconnects and

**Dave Jones:** everything else uh to lower the price. And you can see how that decision might have driven uh some of the design decisions. I mean, once we get this out uh you know, we might see, okay, well, maybe they didn't have room for the uh

**Dave Jones:** tech interface cuz that will be one of the big uh complaints about this as well. All the other series had them and the original uh the MSO 2000 which this one is actually replacing completely. I don't believe they're selling it after

**Dave Jones:** this is actually released as of today that I'm releasing this video then yeah, it it had tech TPI interface. So that will be a big complaint but a lot of those decisions will be driven from you know, they made the call. We want

**Dave Jones:** this single board construction so therefore it's going to drive these design decisions like the buttons and the TPI interface and other things. And I always appreciate the PCB and mechanical teams working together. You can see that they went to the effort to just do a little

**Dave Jones:** routed out bit there just to allow these cables to come out even though they didn't need to they've just gone to the effort there. Nice. So from a servicing point of view if they are going to actually service

**Dave Jones:** these things then yeah, like you've just got a couple of connectors around the outside like this. It's very clean. Looks like we've got the backlight connectors or is that touch or whatever. I don't know. But yeah, we've got just a couple of

**Dave Jones:** connectors around the outside like this and nice attention to detail about how to get them off and I think once all these screws come out it's just going to pop open and it's going to be a very simplistic and clean design and I really

**Dave Jones:** appreciate that. So it looks like under here we are actually going to get a metal bracket because this I can see it bend under and I can see some metal under there. There's another one poking up here and that'll hold the screen in

**Dave Jones:** so that's actually acting as cuz it's dissipating a fair bit of power and it's got the passive cooling vents on here like this which aren't anywhere near the metal but you know, it doesn't really matter and it looks like

**Dave Jones:** that yeah, they're going to get away with one PCB so maybe they that they got so sick of like maybe the complexity of existing builds in like the MSO 2000 or something that they went right. We're going ultra simplistic one board for

**Dave Jones:** everything and it looks like possibly one big metal bracket for everything as well, which does the heat sinking and does the mounting of the screen and the pressure and all sorts of stuff. So, I think we're going to see this clean,

**Dave Jones:** simple design manifest itself in the rest of this. And this is a stark contrast to other scope designs we have torn apart which have then a back metal case and a front metal case and then they've got a

**Dave Jones:** bit of metal work for here and there and everywhere. So, now I'm taking out all the ones labeled PT, but there's two others here labeled M3. So, I'm going to assume that that is the heat sinking there. So, I'm not going to take out

**Dave Jones:** those. I'm just going to take out the PTs around here and I think our whole board and front panel assembly should lift out. So, here we go. I've got all the PT screws out and will this sucker lift out? No. No. Have

**Dave Jones:** I missed one? Or I might have to take out these M3s and they're numbered one and two. But there's no B and C rings. So, um yeah. Come on. And these are metal threaded inserts as I suspected cuz I reckon

**Dave Jones:** there's a heat sink under that bad boy. Let's try it again, shall we? No, I still CAN'T LIFT IT. OH, SILLY ME. I'VE GOT TO undo this and the whole bracket's going to come out. Dolt. Aha, that actually clips out of

**Dave Jones:** the front like that. So, yep, yep, yep, there it is. That's kind of obvious when you think about it. I've put those screws back there. I completely forgot my knobs. Always remember your knobs. Very important. So, this bad boy should now

**Dave Jones:** just lift off. That's the that's the theory anyway. Tada. Here you go. Beautiful. Look at that. Yep, one big metal bracket. I was right. And that's all she wrote. And oh, interestingly, there's our fans. Okay, we've got three

**Dave Jones:** lots of RF connecting sponge here, which connect down to the metal backing plate of your LCD, which is in there like that. So, we've got two blower fans in here, and they blow out the top. Aha, so that explains what this top cavity here

**Dave Jones:** is for. It's for ventilation. So, that's just to get the air out. That makes sense now. Yeah, no worries. So, these two metal pins are stuck into the plastic standoff like that. And they do actually go into the back case. So,

**Dave Jones:** they're like alignment pins. Although, that one's That one's not exactly round. So, yeah, but that helps when you put in the back case on, I guess. But, you know, these would all fall into place. Ooh, you've got to rub those. I'm not

**Dave Jones:** sure why they went to that effort there for that alignment. But, obviously, someone in production went, "Hey, you know, it'd be really nice if we had these for alignment when we're actually putting the things down." Or maybe they've got extra alignment pins for No,

**Dave Jones:** it wouldn't be for test fixture after you've put the board in. Maybe no. No. Mhm. Our BNCs do actually have the locking nuts. Look at that. That's interesting. And then they've got um yeah, like a metal standoff thing.

**Dave Jones:** That's That's fascinating, isn't it? And they're soldered down into the PCB. So, that gets extra rigidity. So, huge bonus points for the mechanical designer that, which takes some stress off the PCBs. If these were just, you know, sticking

**Dave Jones:** right out of the PCB, it would have been a bit how you doing. But, no, they've gone to that effort. And they've got these cutouts in here like this with these little prongs, which then just hold the nut in place. So,

**Dave Jones:** hats off to the mechanical designer that came up with that. I don't think I've seen that before. And that just um like is like an anti-vibration thing to stop the nut coming off. That's rather neat, although it's only friction on the top

**Dave Jones:** surface of that flat nut. It's not rigid-y or anything, but jeez, that's pretty neat, isn't it? And sure enough, there's your two metal threaded insert standoffs um M1 and M2. Sure enough, yeah, that just extends down there. They've got this welded onto here on the

**Dave Jones:** bottom side. So, they didn't actually stamp that out. I would have expected them to sort of like stamp it out like they're doing down here. They've obviously got another heatsink down here, not as important as this jobby. Um but yeah, they've like they've

**Dave Jones:** stamped that in like pressed it in. They haven't done the same here. So, but obviously this would be a low lower thermal resistance than what they're doing over here, but that's interesting. So, that's your main FPGA. There's your

**Dave Jones:** memories. So, let me get all that off, but yeah, that's neat, huh? And extra direct shielding going straight over like that. They've put these as press contacts going down this. So, once it's all screwed in to place, it's going to

**Dave Jones:** make some extra RFI contact over here. Neat. And sure enough, you take off these two screws here and it drops away and we've got the entire PCB. And yeah, you can see how these are welded here and it's a thicker plate than just the

**Dave Jones:** thinner backing plate we've got here. So, this would have a much lower thermal resistance. They did this they would have determined that yeah, they needed a lower thermal resistance to the heatsink backplate in here than they did with this one down here. So,

**Dave Jones:** let's check it out. Ta-da! We're in. Look at this. No surprises for finding Design Link zinc FPGA here. We'll have a look at that in a minute. But obviously I we've got two ADCs here. These are off-the-shelf national semiconductor

**Dave Jones:** jobbies. We've got our memory here. Now, this thing only has 10 meg of memory. I don't know if that's a limitation. We have to look up the part number of these, see what the total memory is here. Then we'd have our boot memory for

**Dave Jones:** the FPGA, do we? And then we've got an application processor down here. We'll have a squiz at and they're the two ones that they heat sink and not not bother heat sinking the ADCs here. So, just off the shelf,

**Dave Jones:** very little in the way of custom technology, although I do believe there's a custom tech front-end logic under here. Unfortunately, this is just evil. Um, this plate here doubles as the shield and that's all soldered down. So, to get in there, I'm going to have to

**Dave Jones:** desolder this thick heavy plate here and hope I don't damage a front-end. Better do it on channel four or something just in case I goof it. So, would it have been possible to move all these parts from here and have a real button in the

**Dave Jones:** face? Well, you know, look, I mean, there's plenty of room left around here to shuffle all these components up and stuff. I don't know yet. Have to keep your routing short from your front-end, but certainly that could have been

**Dave Jones:** shuffled over. But then, the problem is you've dictated that you've got your connectors on this side of the board. So, you'd I know, you can still drop them down. And then, nah, not really. Like you really Like you could have. I can understand why

**Dave Jones:** they've gone for the membrane keyboard. Now, this is interesting. They've got like two rings in here with annotation must cover and may cover. So, obviously, this is the real time clock and this is the battery. So, this is the positive

**Dave Jones:** terminal of the battery on the back side of that. And so, obviously, they don't want this shorting out to the metal works. So, that's just a note from the designer that, you know, look, make sure this terminal doesn't get shorted to

**Dave Jones:** anything. So, but there's no like, you know, tape or plastic sheet or anything like that to stop it shorting. They're just, you know, a note at the design stage. Just make sure, you know, it's not close. And then they've got the same

**Dave Jones:** note down in here. This is the battery terminals and that the battery pack pack plugs into. So, yeah, you definitely don't want that. But once again, like there's no, you know, plastic insulation, so they just determine that the standoff distance is fine and yeah,

**Dave Jones:** that's fine and dandy. But this is the kind of detail that you'd put on your PCB just to aid the other teams, like the mechanical designers who are designing the metal work backing plate and stuff like that and the, you know, production team who

**Dave Jones:** are figuring out how this thing's going to be assembled for an optimal cost and tested and all that sort of jazz. And, you know, just these notes help to make sure that, you know, you don't goof up something down further down the chain

**Dave Jones:** that was out of the control of the PCB designers. So, that's a just a nice little bit of cross-design team engineering there. Well, I'm getting there. Trying to extract this front front end can, but uh it ain't pretty.

**Dave Jones:** Hang on, I think I got it. I don't think I lifted any pads. Ah, winner winner chicken dinner. And there's a single-chip custom ASIC solution for the front end. Like, single chip, that's amazing. 500 MHz bandwidth all in that one custom ASIC chip, the

**Dave Jones:** Tech 026. Now, this is actually used in, believe it not, the What is it? The $500 Tech TBS 2000 series. And I believe it's also used in the Tech 3 series as well. Although, I haven't done a teardown of

**Dave Jones:** that, but I believe it is. And but the higher-end Tech ones have a much, cuz they got higher bandwidth, they got a much newer ASIC in there. It's your typical 500 meg bandwidth variable gain amp. Now, of course, the front end of this,

**Dave Jones:** of course, is software-licensable upgradeable from 70 MHz to 500 MHz. And yeah, I know. All of them do it. I don't actually know though if it's actually done internally at the front end or whether or not it's done after the um, sampling. But anyway,

**Dave Jones:** single chip solution. Uh, there is no 75 ohm input impedance um, on this. So, we've just got that solid state relay uh, that we saw on the other side. And basically um, it's just a like a variable gain amplifier and attenuator

**Dave Jones:** on the uh, front end. So, it's just a differential output here. Looks like it goes through an N the A LISN filter here and a match length pair. They match it to the other lengths over here. That's why it's got a wiggle wiggle

**Dave Jones:** wiggle the air in there to make sure uh, that the skew timing between channels is the same. And it goes up to our off-the-shelf National Instruments ADC and Bob's your uncle. Um, it's not much to it. Modern 500 meg scope. Geez, when

**Dave Jones:** I was a boy. All right, we haven't done a 4K screen capture in a while. So, let's have a look at some high-res photos available on my EEBlog Flickr account linked in down below. It's where I always put my teardown photos. If you

**Dave Jones:** don't want to see the high-res stuff. But this is high-res and I can zoom in. As we saw before, there's not much on the bottom side here. You know, there's a few chippies up here. Of course, there's all the passive bypass in the

**Dave Jones:** stuff like that. We've got some regulator action going on here. You can tell that's a regulator by the caps around there uh, like that. You know, we're doing like transistor array down here um, doing something. And uh, we've

**Dave Jones:** got some output fusing stuff down here. This is for the uh, generator down here. So, the generator is output uh, fuse. That doesn't look like a resettable jobby. So, um, it doesn't mean it's going to blow if you

**Dave Jones:** short the output. I think it's more designed if you feed something back in. You know, this is like these will find its way to student labs and yeah, that sort of thing happens. Anyway, that'd be like the 50 ohm output impedance there.

**Dave Jones:** Uh, you know, probably got some driver stuff here. I don't know. Anyway, this is the um, ASIC. They've actually got a custom generator ASIC. And this is the backside of the ASIC, which we'll have a look at and well, you know, there's not

**Dave Jones:** a huge amount. Of course, we saw the bottom of the analog front end here. We've got our relay here. That's our solid state relay. None of that mechanical rubbish. So, no clunk for all you clunk fanboys. And that's the AC

**Dave Jones:** bypass caps. So, that's what that relay obviously does. It does your AC DC bypassing. And everything else is done in chip. All your attenuation, all your amplification, everything else. They do conveniently have like test points here, 3 volts and stuff like that. So, that's

**Dave Jones:** nice. That looks like our touch interface there. And here's our power input from the side connector here. And that's some protection little protection array or something perhaps. Then we've got an interface here with no connections on this bottom side. So, I

**Dave Jones:** don't know. They might be some sort of test interface. I don't think they're JTAG cuz JTAG's over here. So, you got the chippies up there. Don't know what they're doing. I couldn't be bothered. I'm not going to go into huge amount of

**Dave Jones:** detail on the minor stuff. We'll just look at the interesting stuff. That is our battery connection interface with our alignment pin there. Nice jobbie. And this would all be part of our front panel membrane keypad interface here. So, they're just doing some matrix

**Dave Jones:** switching or something there perhaps. And some protection stuff as well. This is our digital input here. I've just got bypassing here. So, that's pretty much all she wrote like for the bottom side. So, let's go to the top side. You can

**Dave Jones:** see why they really wanted to put it all all on one board. It is very neat. Of course, everything is the Zylinx Zynq here. This is an ultra scale jobbie. We'll take a look at the data sheet in a

**Dave Jones:** minute. But interestingly, you'll notice that it's actually siliconed down. And so is the ASIC for the signal generator. This is the ADG 395C. And that's their custom ASIC uh for the their 50 MHz arbitrary waveform generator. So, that

**Dave Jones:** pretty much does everything in here and there's the uh sig gen out there. And K, is that a relay there? Oh, look at that, shielded relay, too. And this most likely also handles the pattern generator output here. It's not

**Dave Jones:** a hugely complex pattern generator, but it runs almost certainly in there, surely. Um and the probe compensation uh output here. Although, we've got some separate chips here for probe compensation, so I don't know. Haven't checked the features. Maybe it just does

**Dave Jones:** like, you know, 1-kHz output or whatever. And I checked this again, it's not silicon, it's actually um hot snot uh glue or some sort of hot snotty type thing. And um this would have been added after they uh reflowed the chip because

**Dave Jones:** you want the chip floating when it reflows so that the surface tension of all the balls just pulls it um exactly into place. So, they would have added this for uh mechanical strength afterwards, either for uh you know, thermal cycling of the chip cuz

**Dave Jones:** this one and the other one are the two that have uh the heating. That would just help uh take the stress off the solder balls, it'll transfer the stress from the metal package to the PCB. That's the plan, anyway. How effective

**Dave Jones:** that is, I don't know. Has anyone got data on that? Let us know. So, this is where all the magic happens, the Xilinx Zynq UltraScale+ um a part number there. And this is 935 Yankee bucks one off on uh Mouser, so

**Dave Jones:** it's pretty beastly. Um of course, they're not uh paying that, they get them in significant volume, but still, they'd be paying, you know, hundreds of dollars each uh for this chip. And uh we won't go into huge amount of detail, but let's

**Dave Jones:** have a look what it's got. So, it's got an ARM Cortex-A53, and that's what they're using for the applications processor on this thing. Um it's a quad-core or dual-core um up to 1.5 gig as well for the core, so it's pretty

**Dave Jones:** schmicky. It's got a media processing engine, a floating point unit, and an accelerator coherency port. And all the application memory will actually be inside of here as well. And it's also got a separate real-time processing unit RPU as well. And this is

**Dave Jones:** the block diagram that Tektronix gave me. It doesn't tell a huge amount here, but basically, yeah, FPGAs. So, they do mention the RPU here, the real-time processing unit. So, presumably they use that for I don't like the screen updating or something

**Dave Jones:** like that, but they use the A53 core. It looks like they might use two of them. And then they we've got the a look in a second. We've actually got a DDR4 memory on this sucker. So, but like that's maybe the external

**Dave Jones:** memory controller down here. Maybe they haven't shown it. But basically, the digital input comes straight through comparators into the FPGA. So, that's going into the fabric. That all makes sense. It says there's a display engine in there, which is the one we looked at,

**Dave Jones:** and it does everything else. It does the 1280 by 800 display, does the touchscreen, outputs to the wave gen. It does It's all in that one chip. There's some more detail. Mali 400 base GPU, everything else, DMA controllers,

**Dave Jones:** serial transceivers. It's got everything. But let's have a look at the variant that we have because the variant you have determines the price. You can pay 10 times the price for a different variant that has 10 times the memory and

**Dave Jones:** transistors on there. So, yeah, there can be a huge difference. Anyway, so we've got the ZU4CG here, and that's that one there, 192,000 system logic cells, 175,000 flip-floppies, look up tables, 87,000. When I was a boy. And it's got 16 16

**Dave Jones:** gigabits per second transceivers. Wow. And it can do like a PCI Gen3 * 16 interface as well. So, it's got 2.6 meg of distributed RAM in there. And it's got this ultra RAM as well. It's got 13 megabits of ultra RAM.

**Dave Jones:** So, they'd be using this internal memory for all of the application memory and stuff like that. So, that'll be running the Linux OS or whatever they're running in there. The application memory and stuff like that. And they wouldn't be

**Dave Jones:** doing any sample memory in there because there's 10 meg samples plus the digital ones as well. So, we'll have a look at the external memory. So, you can see the external memory here. And it's Micron jobby. And we can decode that. They have

**Dave Jones:** a nice little decoder on their website. UNFORTUNATELY, IT'S BACK LIKE it's upside down. All the electrons are going to fall out. Look, the FPGA code FPGA code is on the bottom. And they make you put it on the top here. I

**Dave Jones:** I No. Anyway, it's this jobby down here. And we've got the data sheet for that. And there you go. These are 512 meg bytes. But because this is an 8-bit scope, that's per sample, not including any like high-res mode or anything like

**Dave Jones:** that. So, 512 meg samples per chip. We've got four chips. So, that's two gig samples of memory hardware they got in here. But it's only 10 meg sample memory that they've got. Of course, granted, you've got to have memory for

**Dave Jones:** your digital channels as well cuz this is mixed signal. So, you got to get your four input channels plus your 16. Well, which is equivalent to another two channels. So, effectively like six channels, for example. And then you have

**Dave Jones:** got to allow for your boxcar averaging mode as well, which gives you your higher resolution and stuff like that. So, but I they seem to have a lot of memory left over a lot of sample memory left over. So maybe they've designed it

**Dave Jones:** in so in the future they can be competitive, you know, 5 10 years down the track when this scope is still selling they want to be you know, like compete all the competitions gone to 100 Meg or something maybe they can up it

**Dave Jones:** and they should be able to like reconfigure that if you don't have the digital turned on you should be able to like get more sample memory. So there's two gig samples not two gigabits two gig samples of memory possible in the

**Dave Jones:** hardware on this thing. They only give you 10 Meg samples. So it's all about product positioning and where it fits in and they sort of like crippled deliberately crippled the products pricing features and everything else bandwidth to fit in you know, they

**Dave Jones:** don't want to eat away at the different levels of product that they got and every manufacturer does it. And down here here's our eMMC memory that we saw on the block diagram and that's handling the application part of stuff. So they're using the

**Dave Jones:** internal RAM here. They don't need any you know, program RAM. So that's all internal but the program is running externally and that's where your firmware is your flash update everything else. And we've got a call for pricing oh end of life scheduled for

**Dave Jones:** obsolescence and we will be discontinued. Maybe it's a slight it's not the exact variant. I'm sure they wouldn't have picked an obsolete part. Let's have a look at the data sheet. Here we go 4 gigabit eMMC eMMC nothing

**Dave Jones:** special man whatever. Anyway, we've got some chunky bypassing around here which you need for fpgas when you boot these suckers up they go and they gulp all your current and if you don't you get your bypassing right. I've mentioned this in previous videos

**Dave Jones:** that that's why Xilinx and other FPGA vendors have entire application notes like 100 pages long of how to power your FPGA. It's that important. Um yeah, obviously uh we got switching converter over here over here. That's a big-ass

**Dave Jones:** inductor there. Um and then uh this is our uh VCO, is it? Anyway, suffice it to say that you do need a lot of stuff to power this beast. So, analog-to-digital converters, no custom uh stuff unlike what they have. I'll link in the

**Dave Jones:** application down below. I believe it's the tech 049 acquisition um engine which has a custom their own custom ASIC. We're on the higher-end uh models on the four and above, not on the three series. I think the three series might use this

**Dave Jones:** same one. Don't quote me on that, but yeah, anyway, they're just using off-the-shelf National Semiconductor jobby, two of them here. Um these are actually uh dual ADCs um to handle the four channels. So, let's take a look at

**Dave Jones:** those. And they are ADC08D1520s. Low-power 8-bit dual 1.5 gig sample per second or single 3 gig sample per second AD uh converters. So, they're they're dual, but they um have to multiplex them. So, if you want the faster rate,

**Dave Jones:** um yeah, it's going to be using both of them. Now, interestingly, the spec for this two series is only 2.5 gig samples per second for the uh single channel or two channel uh configuration um or 1.25, half of that of course, for the um four

**Dave Jones:** channel configuration where they uh use the chip. Now, that's actually less than that's significantly under um the spec for this chip. They could actually do 3 gig samples per second. They doing that for noise reasons? They doing that for

**Dave Jones:** architecture sampling um reasons? I like uh processing um all their existing software, maybe to match their higher-end um series sample rates and stuff. Don't know, but it's capable of a bit better. Applications, digital oscilloscopes. What a coincidence. So,

**Dave Jones:** 7.4 uh effective number of bits, that's what EANOB is um at 747 48 MHz input. So, we've only got 500 MHz bandwidth. So, it should actually do a bit better than that at 500 meg bandwidth. So, that's not too shabby.

**Dave Jones:** And they only consume a maximum of 2 W here. So, you can see why they didn't really need to heat sync those and they're running it at a lower sample rate. So, it's probably only, you know, chewing up 1 W and a quarter or

**Dave Jones:** something like that per device. There's the architecture there. They just switch the these puppies and use both of them for if you want a double the sample rate and LVDS pairs differential pairs is what we saw on the output there. And you

**Dave Jones:** can see those differential pairs as we mentioned coming out of the front end and going up there snaking through. And this is interesting, check this out. They've actually got a resistor and a cap in parallel on one one big pad

**Dave Jones:** there. So, I I don't know like that I don't they want to keep them close, nice and cozy. I I don't know. It's pretty groovy though. Don't know if that'll be in the production version or not. And here's

**Dave Jones:** your external trigger input here. So, they've probably just got some like comparator action and stuff like that going on there, nothing fancy. That'll be going straight into the FPGA. So, this is our PLL here, our clock generator for all this business. I don't

**Dave Jones:** see the crystal on there. Is that on the bottom side? Anyway, that is this ultra low jitter network synchronizer two frequency domain blah blah blah blah blah. So, that's what's generating all of our sample clock. And because this is a

**Dave Jones:** lower end model, we're not going to have a real precision crystal oscillator in there. Actually, where is the oscillator? I'm having a Stevie Wonder moment. And up in the top corner here, this is our power external power input here. And we've

**Dave Jones:** obviously got some switching MOSFETs here. And that's about all she wrote. And And top side just had that extra stuff over there, but yeah, there's not much doing. As far as the digital input here goes, these are National

**Dave Jones:** Semiconductor jobbies, but I don't know. It's got a weird ass SMD part code on it, but yeah, they're just comparator inputs, so programmable three. I don't know if it has programmable threshold levels cuz I don't have the ability to

**Dave Jones:** enable the digital stuff to actually see on this thing. I'd have to you'd have to RTFM on that sort of stuff. But yeah, the output of the comparators here just goes directly into the FPGA. So there you go. That's pretty much it for the

**Dave Jones:** teardown of the new Tektronix 2 Series oscilloscope. And I really like the single board construction, how they've how they've constructed the whole thing and the thermals of it and stuff like that. I know there's a lot of people who

**Dave Jones:** complain that oh, the battery should have been internal, but remember, it's not designed to be a tablet, it's designed to be a both a bench and a portable scope. So anyway, there's reasons that went into that. So Oh, I

**Dave Jones:** have to forgot. Teardown of the battery pack. Hang on. And we'll do a quick teardown of the battery pack here. And I know this will probably get complaints from people how it's too big. One of my complaints is

**Dave Jones:** that it rattles. So yeah. Anyway, once again, I've got a pre-production qualification build and it could be different. Anyway, there's the battery in this thing. It does actually have a check on it. That's pretty groovy. And of course, yes, these

**Dave Jones:** things are expensive, but you'll probably be able to get you know, third-party ones once this comes out. I don't know if it's compatible with any other Tektronix products. Anyway, it is designed to be under the 100 watt hour

**Dave Jones:** limit, which is I believe the carry-on limit for most aircraft. So they deliberately designed the capacity to be under that. So yeah, you can basically carry it with one battery in here and you can have one carry a one battery in

**Dave Jones:** your carry-on bag. So, that's pretty groovy. Anyway, you can see down in there like that. They've got two batteries and you could say, "Yeah, it's all a big waste of space and you know, stuff like that." But, I do actually

**Dave Jones:** like how they've designed this to be like grip like that. So, you can just hold the thing like that. But, yeah, once it's on the tablet, it does make it pretty chunky. Anyway, I do like the attention to detail here how I mentioned

**Dave Jones:** that this is the cover for the back of the oscilloscope. They went to the effort to put a little cutout out in there so that you can store it in there so you don't lose it. Winner. And I thought that pin was like

**Dave Jones:** an alignment pin. But, no, they it actually makes contact up there. So, it's a like a big-ass grounding pin and it makes contact first. That would be for protection reasons. So, yeah, nice touch there. Anyway, this should should

**Dave Jones:** lift off. Let's see what we've got in there. Yeah, pretty simplistic. Lot of wasted space, of course. Could they have designed it better? I don't know. It's probably the best they could do for removable batteries and they wanted

**Dave Jones:** removable batteries cuz you can't actually buy an optional for a pretty penny, I'm sure, a like a charging dock. So, you can have multiple batteries and stuff like this. And there are specific customers that'll just like drool over that. Being able to

**Dave Jones:** like, you know, it's like having like those walkie-talkies and you have like the rechargeable battery packs and stuff like that. For those who need that sort of stuff for field use, it's just fantastic. And having hot swappable batteries like this this would

**Dave Jones:** have been a big requirement from their customers like, you know, a lot of their key customers to do that. So, anyway, there's the board down there. Doesn't that look groovy? Oh, that's a linear tech jobby, I think. That's That's nice. Like just a

**Dave Jones:** jewel board. Oh, yeah, just lifts out. Sweet. Pull the battery out like that. And these boards I'm just going to lift out like that. Ah, isn't that fantastic? There you go. Here's a quick look. That is a linear

**Dave Jones:** tech jobbie. I won't go into details. Oh, it's a mod wire. It's a mod wire. Will that be in the production version? But as I said, as a qualification build, good old-fashioned budge there. Good work. It There you go. Like that's that's a nice

**Dave Jones:** implementation. I like the right-angled board like that. Oh, that's great. Oh, they got double-sided load. Geez. Why you couldn't fit it all on the backside there? Come on. The PCB layout engineer should have went, "Ah, I can fit all that on one side. No worries."

**Dave Jones:** But anyway, that is a very nice design. I I really like that. Like, you know, and then these pieces just slot in there like that. I like the the mechanical engineers like really had a good time with this one. Oh, and by the way, for

**Dave Jones:** those who don't want the super funky stand, I swear if this was had an Apple logo on it and cost a thousand bucks, it's It's one of the highlights of this product is the stand. So, hats off to

**Dave Jones:** whoever designed that. Anyway, if you don't want the stand, if you want the good old-fashioned, you know, like tilting bail kind of thing on it, they do actually have one. Now, mine is actually 3D printed. This is how new it

**Dave Jones:** was when I got it. They hadn't even done the molding yet. So, yeah, that just goes into the existing screws on the back fell out. Goes the existing screws on the back and yeah, you get a tilting bail, but that won't be 3D printed in

**Dave Jones:** the production. Trust me. I'll mention this in the review video, but I really love these captive screws in here. It's just absolutely brilliant. And you can actually have it like gently sloping backwards like this by only putting in

**Dave Jones:** these two. If you put in the two bottom ones, then it's completely vertical. Or as I said, you can do the tilting bail. Or you can even put it like that and you can actually have it designed sit flat

**Dave Jones:** on a surface either a or slightly angled. It's very nice. And the sticky rubber stuff on the bottom is really good. Apparently, it's the same magic material like you use on your um shoe phone inside your car or something like

**Dave Jones:** that to like stick it. And when it's there, like it's really hard to make that budge. Like it's real like I'm really pushing laying in all my body weight on that and I can't shift it. So anyway, I hope you enjoyed that

**Dave Jones:** teardown. If you did, please give it a big thumbs up and as always discuss down below. As I said, high-res photos of these over on my EV blog flicker account link down below and I've done there's two extra videos on my second channel as

**Dave Jones:** well. One is a 40-minute talk with Andy Ted who dropped off this scope for me hand carried it from the US. So we got to chat with him before he had to hop on a plane. So that's interesting and also

**Dave Jones:** my initial unboxing and first reaction of this thing cuz they did deliberately didn't tell me. They just said, "I've got a new scope. We're bringing it over." And you can see my reaction when I open it. So that's on my EV blog two

**Dave Jones:** channel. Catch you next time.
