---
video_id: MiXMKgxx_Oc
title: EEVblog #478 - Keithley 2015 THD Multimeter Teardown
url: https://www.youtube.com/watch?v=MiXMKgxx_Oc
source: youtube-asr
---

**Dave Jones:** Hi, welcome to teardown Tuesday. Yes, it's another multimeter, but it's not a new one. It's an old one. Well, it's a new model. You can still get it. It's the Keithley 2015 THD multimeter. Six and a half digits.

**Dave Jones:** Classic old green vacuum fluorescent display there. Probably looks a bit washed out on the screen here. I think that could be the just the color balance or something on the camera here. At least on my screen. Anyway, I scored

**Dave Jones:** this puppy on eBay for around 400 bucks. Absolute bargain. As I said, still a current model. Very precise. I forget the exact specs off the top of my head, but check it out compared to my EDC reference standard

**Dave Jones:** here. And it is bang on, of course. And I can just dial that sucker up. Look at that. Goes up. It's of course six and a half digits. This one only that gives six decimal places. This one here only

**Dave Jones:** gives my calibrator only gives five decimal places, but yeah, I can just turn that one up. No problems at all. So it's bang on, but I thought we'd take a look at this. It is it was designed in in first sold around

**Dave Jones:** 1998 or thereabouts. So, you know, it's around about a 15-year-old model. Thought we'd crack it open. Have a look. Now the interesting thing, this isn't just a multimeter. It's a rather unusual beast. This THD here of course stands

**Dave Jones:** for you guessed it total harmonic distortion. And it's able to do complete THD automated system measurements when you hook it up to a PC. I haven't actually tried that yet. Of course to actually see it. And that means it does

**Dave Jones:** have a low noise function generator or audio frequency range function generator built in. And as we'll see on the back it's not on the front, but the back has the BNC output connectors for the low distortion function generator. So, it is

**Dave Jones:** quite unusual. So, it could be a bit interesting inside. Let's check it out. Everyone loves a good precision multimeter here on the EEVblog. All the aficionados, they're getting a bit moist right about now. The thing with this instrument though, if you can

**Dave Jones:** pick it up for this sort of price, it really is a bargain. But, it's not doesn't have a massive range of functionality. Take for example the current measurement here. It's DC. It's only got milliamps and amps ranges, basically, and you can auto

**Dave Jones:** range that. So, it's got There it is, 3 amps. It only goes up to 3 amps maximum. Okay, it's got 1 amp, 100 milliamps, 10 milliamps, but that's it. Doesn't have microamps at all. Real bummer, but oh well, you can't have everything. Does

**Dave Jones:** support, of course, four-wire ohms measurement with the four terminals there. Probably shouldn't be feeding voltage into that during the ohms range, but yeah, it's you know, it's designed specifically for this automated system measurement kind of market. You can

**Dave Jones:** select the number Let's go back here. We can select the number of digits, of course, very fast updating, super quick. And we can set our update rate as well. Slow That was on medium, so now it's saying slow. We've got fast. Look at

**Dave Jones:** that. I mean, that's ridiculously quick. I'm not sure of the exact specs of the update rate, but it is very quick indeed. It's got filtering, and it's got Yeah, we can filter 10 readings, and actually we'll be able to see that.

**Dave Jones:** Enter. Moving average. What types of filter Oh. There we go. We've got repeat moving average. So, let's turn the moving average on. All right, I've dialed 100 moving averages in there, and if we tweak that up, boom, we can see that I I

**Dave Jones:** jumped to 2 volts, and it takes a while to get there because of that moving average. And of course it's got the source built in. I haven't actually tried any of this yet, but uh sign out I'm not even sure um channel 2 you can

**Dave Jones:** set the amplitude, set the impedance, set the frequency. I believe the frequency is under like audio measurement uh type range. It might I don't know go up to 50 or 100k or something like that, but uh it does have

**Dave Jones:** and then measurement capability THD per units you can uh oh you can set upper harmonics, frequency, all that sort of jazz and it's controlled via GPIB or RS-232 you can get uh step and scan and all sorts of that system multimeter uh

**Dave Jones:** capability as well. So, really is quite a versatile instrument, but uh I'm quite interested in the automated uh you know frequency uh THD part of it and getting uh frequency responses for um audio uh frequency range system. So, could be

**Dave Jones:** quite interesting. I'm going to have to probably do another video hooking that up to the PC. This will just be a teardown. Does thermocouples, does diode, continuity. I don't even know what speed of the continuity tester is. Now, let's give that continuity tester a

**Dave Jones:** go. You can actually set the level of the the the value there. So, that's pretty darn quick. Actually pretty impressed with that continuity tester. Now, I've got to say this is one of the dickiest tilty dials I've ever

**Dave Jones:** encountered. It's a real dog. Man, whoever designed that should be shot. Now, I don't see any uh build date or anything like that on here. There's a serial number. I'm not sure if you can correlate that on the uh Keithley

**Dave Jones:** website, but there it is made in the US of A. And here it is a source output. It's also got an an inverse um source output and it like a pulse some sort of pulse output as well. A rear terminal uh multimeter input.

**Dave Jones:** There's a switch on the front, as you probably saw, uh to enable you to switch between front and rear panels, as is very common on these bench multimeters. A trigger link interface, some sort of custom thing. RS-232, um almost

**Dave Jones:** certainly not uh isolated, would be my guess. And IEEE-488/GPIB. And if you have a look at the uh voltage selection and fuse here, you can see it's got uh might be able to see in there 240. There it is. And it's

**Dave Jones:** actually got uh pins on here. There's a couple of pins there and a couple of pins there. And depending on um oh, sorry, you can just How do you Yeah, you pull that out and you rotate that into position to uh

**Dave Jones:** select your um voltage. And then there there's the There's the labels on the back of it. And then you just rotate that around and these pins um go into the socket there and select your voltage. Quite novel. I

**Dave Jones:** like it. And it looks like we've just got standard fare here. The two screws at the back. This panel um this back uh feet thing will come off and uh hopefully the top Well, the whole thing should uh slide off. So, that's

**Dave Jones:** the plan. And this is 15-year-old technology. Keithley, I'd expect lots of uh through-hole stuff. It'll be interesting to see what uh reference it uses as well. I'm sure the all the uh There we go. Shouldn't screwed that out

**Dave Jones:** too far. Sure the multimeter aficionados are just waiting to see what the reference sensor in this puppy is. And uh yeah, we should probably have to get a couple of No, uh yeah, there we go. Couple of little Phillips on the bottom there.

**Dave Jones:** And uh oops. Sorry about that. Poor camera ship. Is that the word? I need a camera operator. Full-time camera operator, that's what I need. I'm the on-screen talent. Yeah, right. All right. That now should hopefully slide out somehow. Yep, there we go.

**Dave Jones:** Ta-da! Let's have a look inside this puppy. All right. Hey, two two transformers in there. That's a bit surprising. I didn't really expect that. And Whoa! There we go. I see a Motorola processor there. Let's have a quick first

**Dave Jones:** look at this thing. And we have a Motorola 68306 FC16 processor there. Obviously got our system ROMs here. We'll have a look at it in a bit more detail. Aha, linear technology is that the reference? We'll take a good look at that. We have a

**Dave Jones:** shield here, which uh, you know, um, looks like it's covering some relays. We'll have a look under there, so that's probably some of the uh, ADC integration um, circuitry or something like that. We'll have a look, but uh, it's rather interesting. There's

**Dave Jones:** a second board down the bottom, which is clearly the uh, um, you can see it. Well, we'll see it down there. It's connected directly to the output terminals. So, that second board down the bottom uh, looks to be

**Dave Jones:** the function gen board, and the top one, I believe that's the reference there. So, the top one uh, is probably the ADC part of it. So, let's take a closer look. All right, let's start with our input circuitry

**Dave Jones:** down around here. You can see the big switch coming from the front panel there on the left big lever coming in that's a multi-way switch to switch the four wires coming in from this side front panel and the four wires coming in from

**Dave Jones:** the rear that's a very common way to do it you do it on the board there just the wires coming straight in we have got our input circuitry around here there's a big ass varistor if there ever was one biggest

**Dave Jones:** discharge tube big input uh protection resistor by the looks of it two big they're two big trans well they're labeled Q so they're probably transistors haven't looked at the numbers on those and we've got our high voltage resistor here it looks like it

**Dave Jones:** well it looks like it's a four No could be a no a six terminal device but it looks it's interesting I'm going to get a close up of this cuz it's like almost like three different ones sandwiched like glued together there's

**Dave Jones:** one on the top here one in the middle and a smaller one on this bottom side so let me have a look at that but there we have some sort of optocoupler action there happening we've got a isolation slot we've got high voltage

**Dave Jones:** isolation slots around here we've got bigger power SMD resistors here a lot of those would be in series to give you high voltage once again and we've got a relay switching there's some more high voltage isolation slots there over this

**Dave Jones:** side between the crystal separating that that looks like a diode bridge and what's that puppy let's have a look you can see those precision film resistors down there on their ceramic base it looks like they're all glued together and presumably to just

**Dave Jones:** thermally bond them all together there's actually three of them and they're a Caddock TF series let's go to the data sheet there we go TF ultra precision film resistors low temperature coefficient 5 ppm per degree C. Yeah, pretty damn low from 1 K to 125

**Dave Jones:** meg point 01 percent tolerance. Not too shabby at all. Maybe they're even uh selected or they could even get a better grade. I don't know. You'd have to go into the uh uh because you can often um custom order these resistors. So, yeah,

**Dave Jones:** there they are. They're just single like that. So, maybe there are there's a reason to thermally bond them together. They're obviously you know, not individual range resistors. If they were I you know, I don't see the uh uh the

**Dave Jones:** reason for that. Anyway, very precise resistors. Probably cost quite a bit. So, yeah, they haven't skipped there at all. And here's the block diagram for the analog input circuitry. This is in the service manual for this thing and I

**Dave Jones:** will link it in down below. So, if you want to check out the uh service manual, unfortunately, it doesn't have a schematics uh but it's uh chock full of uh all sorts of goodness if you actually own one in terms of you know,

**Dave Jones:** calibration and uh stuff like that. It's got a a scanner option. Uh of course, this one doesn't isn't fitted with a scanner option. In fact, I don't see anywhere to put a scanner option um physically in the thing in terms of you

**Dave Jones:** know, a cutout on the back panel or whatever. So, anyway, fairly basic multimeter, you know, analog input circuitry. It's got a mux with gain this ADC U165 there. Haven't found the ADC yet. Doesn't mention the reference on there at all. So, I'm going to have to

**Dave Jones:** search around. And there is the ADC U165 and it's got um looks like a custom device. It could be off the shelf and just start rebranded um of course, but it's got 2000-8080Z AO2. So, might have to uh look that one

**Dave Jones:** up, but 2000 may not be a coincidence because look, this board is shared between the Keithley 2000 and the 2015 model which we have here. And I just looked at the parts list for that and it lists it as a programmed ROM. So, there

**Dave Jones:** you go. It could very well be a custom ADC that uh you know, Keithley developed a long time ago and uh just like Fluke, you know, developed their custom ADCs a long time ago and they're still using them. And there's our reference there

**Dave Jones:** and yeah, it has a linear technology uh part number on it. Oh, there's a little Is it wobbly? Nothing worse than a wobbly voltage reference. It's like it's just got a uh cap on that, but uh I checked the um uh parts

**Dave Jones:** list for this. It's actually an LM399. Yes, manufactured uh second source by Linear Technology. Now, if you have a look at the uh circuit overall, you can see the isolation slots in here dividing the digital section and these

**Dave Jones:** optocouplers looks like some of the digital uh processor section over here is coupled through to the uh uh you know, the output side of the trigger uh circuitry down here. That's the trigger connected down there. So, it looks like um the RS-232, which is here

**Dave Jones:** of course, here's the RS-232 drivers, that will be uh isolated from your ADC input. So, you can uh safely hook it up, I believe, safely hook it up to your PC and uh do the business there. And if And there

**Dave Jones:** we go, there's more isolation slots around there. That's, you know, probably why they're using a couple of transformers uh in here actually. They're powering uh various things. This one pops over here and looks like it powers the digital

**Dave Jones:** circuitry. There, we've got another one coming in there powering something. Probably it looks like the display section up the top has its own little power supply, perhaps. Um so, that's rather interesting. And the probably the second transformer is

**Dave Jones:** probably powering the board underneath. So, everything's isolated from everything else. Curiously, though, the transformer there very, very close to our input sockets. Check that out. Our input wiring is just, you know, flapping in the breeze there. I love

**Dave Jones:** these little uh uh clips. You know, they gone to a bit of trouble. Obviously, they don't need to shield these. Um So, you got to think that uh Keithley know what they're doing there having the input uh wiring so

**Dave Jones:** close to the mains transformer like that. And of course, they would. I mean, this thing's probably got um excellent uh supply line rejection anyway in the ADC front end. So, there we go. There's a voltage reference, lots of uh analog

**Dave Jones:** devices, uh precision op-amps all around there, as you'd expect, lots of miscellaneous stuff. These in here are actually uh resistor networks. Dead giveaway are there. So, and lots of, you know, uh basic stuff. There's some 74HCT stuff happening around there. Much lot more uh

**Dave Jones:** precision op-amps, and there's probably some multiplexers in there, and you know, all sorts of jelly bean type stuff. Um curiously, check out this one. 70K um with 1% marked on it. They got 70K000. It looks like one of those um precision

**Dave Jones:** film resistors, you know, you pay like uh 20 bucks for, but it is marked 1.0%. Don't know what's going on there at all. And uh yeah, there's more stuff happening. We'll have to check out under the shield under there, but there I can just move

**Dave Jones:** it out. There is, tada, no surprises at all. Analog devices 637 true RMS converter. But um yeah, that's basically the uh uh front end. Pretty standard looking uh front end, quite well designed for a multimeter. It's got all the requisite

**Dave Jones:** uh protection. Not sure This one's not actually uh CAT rated, actually. It's designed all pre-those CAT uh ratings, so I don't know what it would be uh rated to rated to uh today, but uh I'm I'm sure it is. I'm sure the latest

**Dave Jones:** one is uh branded. I just haven't read the manual on that. And the ADC, you can see that's uh really separated from everything else. They've got quite a lot of uh ground plane surrounding that sucker. And of course, the ADC is quite

**Dave Jones:** important. But by the nature of it being separated from everything else, it no surrounding components, you're going uh-huh, where's the bypass stuff? Well, it's got to be on the bottom of the board. So, this is obviously a uh

**Dave Jones:** dual-sided uh dual uh side populated board. So, I'll see if I can get it out. Um, could be a bit of a pain. ferrite in there. There it is. Uh. It's not just a uh pretty piece of plastic to hold the

**Dave Jones:** wiring in place. And as far as getting this board out goes, there were two screws on here holding this back panel in place. There was a screw here holding this uh linear regulator down to a little side um flange there using it as a heat sink.

**Dave Jones:** And there was another screw up here doing a similar thing. So, I've taken out both of those screws, and there's little sliders um on the side of the case here. So, I'm assuming that the board will just No, uh of course, uh duh, of course,

**Dave Jones:** I've got to uh undo these connectors here on the back. But if I do that, and maybe I don't know about the AC input there, but it looks like the whole board is designed to slide out once you

**Dave Jones:** disconnect all the cables, but maybe I should actually read the service manual. Nah. Of course, we have all our fixed wiring. Do they just Ah! There you go. They're just uh so- sockets that just uh pull off the input.

**Dave Jones:** Very nice. There it is. Check it out. We can just pull those off. I really really like that. I better actually uh remember where they go. Hmm. Aha, I think I figured it out. These little sliding notches over here are

**Dave Jones:** designed to slide, so the board has to actually slide that way. It has to slide into the case instead of pull out. So, I've got to disconnect all the connectors down here. The board slides in and then should lift up. Excellent.

**Dave Jones:** So, that's why we have the big cutout in here cuz the board's designed to Once it moves in a little bit, it can then lift up and clear all of these connectors. And uh Yeah. That's pretty good. I rather like

**Dave Jones:** it. So, I've disconnected all that. That should slide forward. Tada! And of course, all these wires are hand-soldered. Uh we've got our connecting rod there. Maybe we should Oh, how do you take the connecting rod off? It doesn't look like you can.

**Dave Jones:** So, very carefully, very gingerly, lift this out. And then the connecting rod comes out of the front panel, and ah It's rather tricky. Bit of a hotchpotch. There we go. We've got the connecting rod out. There we go.

**Dave Jones:** Tada! Let me check underneath. We've got some plastic flapping in the breeze there. But uh it's not not too bad once you know. Look at that. There we go. Ta-da. We flipped it out of the way. Not a problem. And there is our complete

**Dave Jones:** board. And as suspected, yes, double-sided load, of course. All of the passives on the bottom, pretty much. There's no sort of real Don't see any active stuff on the bottom at all. Just all There's our ADC up there. You remember

**Dave Jones:** our ADC was in that complete section over there. There's the a couple of, you know, it's only got a handful of bypass caps down in there. We've got a cells a nice little plastic isolation shield there. Obviously, so you know, it

**Dave Jones:** doesn't come in contact with anything else. And uh some ground plane action. And not much else. Oh, no. See a couple of guard traces. Let's have a look. And here it is. Here's an excellent example of some guard traces. Those ones there with the

**Dave Jones:** exposed tinned traces there. Now, don't confuse these with that shield any any form of ground shield or anything like that. That's not their purpose. Their purpose is not to shield interference from these adjacent traces here. It's designed to prevent

**Dave Jones:** leakage from these traces and the ones outside the guard zone. So, to prevent leakage from these outside traces into these pins in here, which are going to be quite critical. And how you can get that? Well, you can get the

**Dave Jones:** contamination of your PCB flux residues. You can get dust and dirt and grime and fingerprints and all sorts of crap. If you've got a very sensitive input node like some of these system Well, a lot of multimeters on the lower ranges will

**Dave Jones:** have like effectively you know, many gigaohms input impedance effectively open. That's why you see all the digits on the millivolts range just you know, it just charges up because these things um, aren't just 10 megaohms. They're very high impedance nodes. So, that's

**Dave Jones:** why you would typically want guard traces in here like this. So, it just prevents, um, any like surface leakage going across. And really, if you want to do it properly, you put And if you've got a multi-layer board, you put you put them

**Dave Jones:** on internal layers and uh stuff like that as well, just in case there's any, um, sort of leakage on the internal layers. So, these are really sensitive points in your circuit and you really want to prevent any leakage into those

**Dave Jones:** from somewhere else. Now, this guard trace isn't necessarily ground. It is going to be the reference point of of the sensitive part of the circuit that you're trying to prevent leakage into. So, may or might may not be ground

**Dave Jones:** depending on the system configuration, but And that's why the solder mask has been removed and they've got the bare tin, uh, plating on there is to actually get, when you have surface contamination on here, to actually get leakage, to

**Dave Jones:** actually get leakage into that reference point. And that's okay. That prevents it just prevents outside leakage. So, any leakage at all is going to be confined to the reference point, which is not a problem. You don't want it leaking into

**Dave Jones:** the other points in your circuit. So, the reference node is fine and that's why they leave that trace exposed like that. So, you'll typically find that in, uh, these sorts of, uh, multimeters. Some people implement this incorrectly and all that sort of stuff. Well, we

**Dave Jones:** won't go into the details, but, yeah, that's a really good example of a sensitive, um, input circuit that requires guard tracing. There's another example of how you're just going to put a guard trace around one particular pin because you

**Dave Jones:** want to prevent any leakage into that particular pin. And what is that guard trace protecting? Surprise, surprise, look at it. We have ourselves a P-channel JFET, J177. And you can see the guard trace running on top there as well, protecting this

**Dave Jones:** high-impedance JFET. No surprise whatsoever. And there's another critical device, Analog Devices AD706, a dual picoamp input amplifier. And you can see the guard trace going, protecting that pin up there and running right around there. These guys know what we're doing.

**Dave Jones:** And there's the other one, you see it sneaking around the JFET there, and all around there. Mm, attention to detail. Love it. So, the reason for all those guard traces? Surface leakage. That's what it's all about. Contamination. So,

**Dave Jones:** these so nothing leaks into these critical pins. And there's all our true RMS converter circuitry around there. That was all the stuff that was under the shield on top. And it wasn't fully shielded, of course. And you can see the

**Dave Jones:** input switching relays and other stuff still around the analog front end all around here. There's our input protection stuff and just running and the shield sort of goes over part of this part here. Optocoupler down in there. And here's that DC power input

**Dave Jones:** here, yeah, going off to the front panel here. And that's You can see the physical separation in there between the analog stuff. We've got ourselves an isolation slot there, and that goes up there to the main processor and powers

**Dave Jones:** all that. And there's our mains input down there, all separate. They've got their rod coming from the front panel. There it is. Beautiful. Comes all the way from the front of the chassis. I'm a big sucker for that. Really nice um

**Dave Jones:** earthing on the chassis there, going directly over to the filter over here, which actually is a proper common mode input filter. And there's all the different um the there's all the different wiring from that voltage selection um thing

**Dave Jones:** which I showed you right at the start. That actually goes all onto the board. That's rather neat. They've got that going all the way over there and then that selects the, uh, uh, various, um, taps on the mains transform which goes

**Dave Jones:** in over here. Very neat. Got some more protection in there. Check those out. They're massive for the mains protection and, uh, that is done really, really well. Time now to take a look at the bottom board, the signal gen.

**Dave Jones:** And here we have it and look at this beast. We have ourselves an Analog Devices SHARC DSP. That's a huge quad flat pack there. It's the ADSP-21061 SHARC DSP processor. Would have been really bleeding edge, um, you know, 15

**Dave Jones:** years ago. This would have been really hot stuff and we've got, uh, three other Xilinx devices up there. So, it looks like, um, I'll have to get the block diagram of this it is in the, uh, manual, but it looks like, uh,

**Dave Jones:** this is our, our generator here and then this is all of our output, uh, attenuation and filtering and stuff like that which then, of course, goes into the, uh, sockets right down there on the bottom. So, uh, we'll have to look at

**Dave Jones:** what the other stuff is doing. Thanks to the manual, we do have the block diagram for the various sections. This is the digital, uh, distortion circuitry and we also have the block diagrams for the analog distortion circuitry we'll check

**Dave Jones:** out and the sign gen circuitry around here, but basically there's that big bad ass, uh, um, Analog Devices SHARC DSP up there with its ROM and its JTAG interface and its main oscillator. I think it's 33 MHz or thereabouts. And, um, the FPGA little

**Dave Jones:** Xilinx down in there. We'll have a look at that type and, of course, it's got to have an external EEPROM to boot that upon, uh, power up and then you've got opto-isolation. That just goes across. It looks like, just, you know, serial,

**Dave Jones:** um, interface going across some optical isolators because your output circuitry, you want that to be totally iso electrically isolated from the rest of your generation circuitry. So, they're doing that really, really well. So, we'll take a look at these other block

**Dave Jones:** diagrams as well. So, here's the distortion analog circuitry. That There's the block that we just looked at, the digital circuitry there, but we've basically got our ADC here. We've got a filter. There's our analog stuff. We've got our ADC clock oscillator,

**Dave Jones:** another FPGA controlling the whole ADC system with an E2 prom as well. So, not a huge amount happening there. Then we've got our sine wave generator circuitry. And as I uh mentioned before, it's got its own control FPGA as well.

**Dave Jones:** Generate the sine generator is U301. We might have a look at that puppy, but then we've got the attenuation filter. And the output the second output that's the main source output, of course, and the second output there is either an inverse phase. You

**Dave Jones:** can see minus one there. It either inverts it or it can do it as a pulse output, which is the same frequency as your output uh generator. So, looking at the generator sine generator part of this thing, there's our

**Dave Jones:** generation FPGA there. And surprise, surprise, we've got an Analog Devices AD9850 125 MHz DDS generator. These puppies are everywhere. We saw one of these in the last teardown as well. They're all over the shop. Then our DDS goes into an amp

**Dave Jones:** 03, another Analog Devices part. That one is a unity gain differential amp. And then, as I said, it goes all into the filter stuff and the attenuation stuff, which is all around here. Relay switching. And then you've got your outputs over here

**Dave Jones:** with some common mode chokes as well. And all three FPGAs in this are the same. They are as I like, ancient, obsolete, by the way. Um XC5202s a lousy 3,000 gates each and the silicon process technology 0.5 micron. Wow,

**Dave Jones:** huge. We've actually got ourselves a second DDS generator down here and there's the main ADC analog devices 7722 16-bit 200k sample per second sigma delta converter and obviously this is the um um main ADC control FPGA. So, that's

**Dave Jones:** taking care of all of that and over here you can see the opto isolators with the isolation slots down in there separating all of the digital circuitry over here, the DSP and its control FPGA over this digital link which then

**Dave Jones:** drives the ADC and then that drives all of this generation stuff and completely isolated from all the digital section. And then we've got some of the feedback going up to our main um multimeter board as well. These are

**Dave Jones:** just wired directly onto the board here flying leads up to the top. Even the transformers are made in the USA by North Lake Engineering in Bristol in WI. Is that Wisconsin? And check out that slot system up there as well. They've

**Dave Jones:** just got a little retaining um looks like pin on the bottom of the case. You slide the board backwards and then it just pops out through there. Very nicely engineered. I like that a lot. So, that's a rather nice

**Dave Jones:** implementation of a you know, a THD generator and distortion measurement system. It's got you know, 16-bit ADC in there, FPGAs, DDSs to generate, DSP processing, the whole works to add this rather unusual THD capability to this system multimeter. I

**Dave Jones:** think it's the only multimeter on the market that's got building generator and THD. So, rather unusual little beast and uh certainly if you can pick one of these up, um you know, you might be able to get one fairly cheap cuz people don't

**Dave Jones:** really understand this model. They go, "THD? What? No, what? I don't What's that got to do with multimeters? I don't know. I'm not touching that thing." But, yeah, it's not bad at all if you can score it for a decent price. So, that is

**Dave Jones:** a look inside the Keithley 2015 THD. And if you know how it If you got photos of the 2000 model as well, which presumably this this top board is identical to the 2000, then by all means share it with us and we'll

**Dave Jones:** see how the internal construction differs to the 2015. So, it'd be interesting, but that that is quite an interesting bit of kit. It's rather unusual. It's above and beyond your usual bench multimeter teardown. So, it's very well-designed and manufactured

**Dave Jones:** instrument. I'm not sure what it cost brand new. I think it's like it, you know, $3,000 or something like that brand new. So, if you can pick one up, especially that it's a current model for 1/10 the price, man, what a bargain. And

**Dave Jones:** based on the date code of some of this stuff, I mean, you know, there it is, the 39th week '04. So, this one that I've got is less than 10 years old. So, not bad at all. It should give some

**Dave Jones:** really good service. One thing that I didn't find in here, of course, is a backup battery like you get in a lot of old multimeters to hold, you know, calibration data or something like that. No, none of that to worry about

**Dave Jones:** here. So, there you have it. Looks like an absolute mess and uh I'm sure it'll go back together and work a treat. And as always uh if you want to see some uh high-res photos of the teardown, um my

**Dave Jones:** Flickr account is always uh linked in there. So, go check it out. And if you want to discuss it, the EVblog forum is of course the place to do it. If you're not on the damn EVblog forum, why not? You should be. It's where

**Dave Jones:** everyone hangs out and chats. Oh, man, there's like 600 posts a day or something. It's crazy. If you want to ask questions, don't send me a personal email. Jump on over to the forum. Someone will answer you quick-smart.

**Dave Jones:** That's a beautiful thing I love about the EVblog community. You ask a question, somebody knows. Somebody's got the answer to it always. It's and oh, bang, you know? Somebody will just know the answer to your problem off the top

**Dave Jones:** of their head, no matter how obscure it is. It's really amazing. Never ceases to amaze me. Anyway, um I hope you like the teardown of this Keithley 2015. And um I'll probably um Yeah, I'm going to uh This is a keeper, of course. I'm going

**Dave Jones:** to uh use this here in the lab. And um very nice bench multimeter, a bit limited in some capabilities, but uh I'm certainly uh going to use it. And I'm going to try and use the uh THD feature

**Dave Jones:** of it as well. So, I might have to do a video on that uh once I get it hooked up to a PC, run the uh Keithley software, which I think you can download from the website, and do all that THD measurement

**Dave Jones:** goodness. Hope you liked it. Catch you next time.
