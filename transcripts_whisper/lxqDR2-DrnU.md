---
video_id: lxqDR2-DrnU
title: EEVblog #444 - Car Lane Guidance Camera Teardown
url: https://www.youtube.com/watch?v=lxqDR2-DrnU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 37, "3": 57, "4": 73, "5": 89, "6": 105, "7": 121, "8": 146, "9": 170, "10": 182, "11": 206, "12": 227, "13": 247, "14": 267, "15": 287, "16": 308, "17": 328, "18": 344, "19": 360, "20": 384, "21": 405, "22": 425, "23": 445, "24": 465, "25": 486, "26": 502, "27": 518, "28": 534, "29": 554, "30": 567, "31": 587, "32": 607, "33": 627, "34": 647, "35": 668, "36": 684, "37": 700, "38": 716, "39": 736, "40": 752, "41": 769, "42": 789, "43": 805, "44": 825, "45": 841, "46": 861, "47": 882, "48": 902, "49": 926, "50": 943, "51": 963, "52": 987, "53": 1004, "54": 1024, "55": 1040, "56": 1056, "57": 1080, "58": 1100, "59": 1125, "60": 1141, "61": 1169, "62": 1186, "63": 1206, "64": 1226, "65": 1238, "66": 1259, "67": 1271, "68": 1291, "69": 1307, "70": 1327, "71": 1348, "72": 1364, "73": 1384, "74": 1409, "75": 1433, "76": 1457, "77": 1473, "78": 1489, "79": 1510, "80": 1526, "81": 1542, "82": 1562}
---

**Dave Jones:** And here we have the lane guidance camera. Doesn't this look funky? Oh man, that's got spaceship written, like shuttlecraft, written all over it. Does a shuttlecraft make that noise? I don't think so. Putt, putt, putt, putt, putt, putt, putt. No, it's like silent, because it's in space.

**Dave Jones:** Pigs in space! And I don't know anything about lane guidance cameras, because I don't know anything about it. I don't know anything about it. Lane guidance cameras, because I don't have a car fancy enough to have such a thing. But there we go, there's the connector interface, a couple of screws on the back.

**Dave Jones:** Should be really simple to open. And there's our camera. So I'm not sure how much processing hardware is going to be inside this thing. I mean, it's a die-cast alloy case. So, hmm, another Teardown Tuesday item? Or should we open this now? Alright, what the hell, let's do a full teardown

**Dave Jones:** of this thing right here and now, shall we? Let's not wait for Teardown Tuesday. This will probably be it for the mailbag, by the way. Depends on how much is in here. I expect quite a lot of real-time processing power for this lane

**Dave Jones:** guidance, lane vision camera. I think they do a lot more than that, just for you know, they do a hell of a lot more. They, you know, object detection and all sorts of whiz-bang stuff. I don't know what Hyundai car it's from, or what features it's got, but I believe that they, you know, they generally

**Dave Jones:** have the capability to do those sorts of things. So here we have a weird-ass automotive connector used in the Hyundai cars. I've taken the two screws off the end. I had to actually prise that out. Had to get my knife in there and prise it out, but it does just

**Dave Jones:** pop off. And ta-da! We're in. We have we immediately see two surface-mount electrolytic caps, which is a bit of a surprise. I'll talk about that. And it looks like we have some more screws in there. A vertical riser board for the camera, which of course you can see down in there.

**Dave Jones:** And it really is a beautiful case. And it looks like it sort of looks and feels, because of the lightness of it, it looks like one of these magnesium, lightweight magnesium alloy type cases. It's really lightweight, it doesn't weigh much at all. Get in there and we'll whip these two screws out.

**Dave Jones:** Yep, screwdriver just makes it. Thankfully. So, and expect to see, as I said, some serious horsepower processing in here. And probably a dedicated chip for it. I don't think we'd find like an FPGA or anything like that. There's bound to be a CAN controller as well,

**Dave Jones:** because this will be a CAN bus interface as well. I'm not sure what sort of, you know, output signals they get from this thing, whether or not it's capable of outputting the video from the camera that goes to a potentially a screen in the car, I don't know.

**Dave Jones:** No idea, but let's... yep. Yep. We're out. Ta-da! And there we go. Oh, look at that! Mobile Eye STME IQ 2. And, yep, looks like we have another processor on the bottom there. Free scale, is it? Woohoo! Let's have a look. Yeah, so there you go.

**Dave Jones:** It's a company called Mobile Eye, or that's the brand STME. It's, you know, ST micro, obviously. Do it, but I guess that's their technology Mobile Eye. Maybe they've teamed up with someone. I'm going to have to Google it. I don't know. We've got some

**Dave Jones:** memory surrounding that, some miscellaneous probably some power supply stuff, not much else. And the camera of course is on a little riser board there. Can I just whip that out? That is... yeah, yeah, that's just going to pull out. There we go. Not a problem whatsoever.

**Dave Jones:** Isn't that neat? I don't, you know, I'm sure they've done their, you know, shock and vibration performance tests on these things. Very extensive, they would be. On all this automotive stuff, Rev-C, gone through a couple of revs, multi-layer board there. It'd be top quality gold plated on that,

**Dave Jones:** you can bet your bottom dollar. No idea what resolution camera. Now one thing I potentially didn't expect to see in here, as I mentioned, these surface mount electrolytic caps here. They might be a polymer type one which have a much longer life, but the reason I didn't expect them is because, as I said, that life

**Dave Jones:** expectancy thing, you know, automotive it's operating at a high temperature and of course the life of electrolytic capacitors goes down drastically with temperature. In fact it's pretty much mostly dependent on their operating temperature. So it's a really big deal. So in a car, in a

**Dave Jones:** hot environment, already from the body, let alone plus the ambient temperature as well, they'd be, you know, 105 degree C rated caps at least. And we'll have to look at the, we'll have to try and Google the type. They're a VCA, I assume that's the model number, so

**Dave Jones:** or the, you know, the model type. Probably a top quality brand, they won't be a one hung low one, they'll be a Panasonic or something like that, no doubt. And well, that was too easy folks, I Googled VZA capacitor and bang, I popped up

**Dave Jones:** with a Panasonic data sheet. They are the ZA series, type V, we'll go into what type V is, but yeah, no surprises that they're Panasonic. Panasonic are, you know, one of the top, if not the top capacitor manufacturer in the world, always have been.

**Dave Jones:** So, and they are a conductive polymer hybrid aluminium electrolytic capacitor. So they're going to have a much higher life than your regular ones. In fact, the endurance, here we go, 10,000 hours at 105 degree C. Low ESR, high ripple current, not a problem, they go up to 80 volts, and they're equivalent to conductive

**Dave Jones:** polymer type aluminium electrolytic. And there is a little characteristics change by temperature and frequency. Ooh, quite stable, I like it. But yeah, they're much better than, as they can bind like a polymer construction, which means the electrolyte doesn't wear out as quickly, they still

**Dave Jones:** have it, but it doesn't wear out as quickly at high temperatures as you would in a regular aluminium electrolytic capacitor. We've got more stuff in the endurance down here. The capacitor shall be subjected to application of a DC voltage with full rated ripple current at 105 degree C for 10,000 hours after stabilising

**Dave Jones:** room temperature. The capacitor shall not exceed the following limits, thou shall not exceed. So yeah, after 10,000 hours at 105 degree C at rated voltage and rated ripple current, they're still doing pretty darn good after the endurance. We're still talking what size we've got

**Dave Jones:** here, maybe a C size, we're still talking, you know, 2 ohms ESR at 100 kilohertz. So pretty darn good, I like it. And if we have a look at the marking information here, yeah, it's the first letter is the voltage mark, so V is 35 volts, so that's 35 volt rated cap.

**Dave Jones:** ZA series, Panasonic. They've done well, they've chosen exactly the right type, and 10,000 hours shouldn't be an issue. Because with 10,000 hours you do some simple calcs, even if you're driving the thing solid and it's at you know, cars at temperature and this thing's at temperature, but it's probably got

**Dave Jones:** you know, airflow going through this thing anyway, it's probably not that hot because it's right out, you know, in the front bumper or something like that. So it's probably not operating anywhere near sort of engine compartment temperature, because it is a lane guidance thing.

**Dave Jones:** So it needs to poke out the front of the car, so it's not only able to get the cooling, unless you're going backwards I guess, then it'd be getting probably, you know, at least some sort of cooling effect in the front bumper part of the car, or

**Dave Jones:** something like that, I assumed. I don't know how they mount these things in the Hyundai cars at all, or where they're actually located, but you know, it has to be somewhere like that. So really you know, 10,000 hours, but even if it was operating at

**Dave Jones:** a full 105 degrees Celsius, we'd still be talking, you know, 3 and a half years or something like that at 8 hours a day, solid temperature like that. But even then, it's still, you know, it doesn't just suddenly die at 10,000 hours. These things, you know, still meet these specs at

**Dave Jones:** 10,000 hours. So it's still going to continue to operate well beyond that, because you would have designed that in. There's our little camera board, we should be able to take the screws off there, and they get to the bottom of the camera, but it won't be that interesting.

**Dave Jones:** Of course, a couple of fiducials on the board there for component location. Rev-C board, and let's have a look at the front of the module. Once again, it looks like it uses that same magnesium alloy. So yeah, let's see what's under that. They've got like a

**Dave Jones:** plastic, no, that's rubber. There you go, they've got a rubber mounting base on that. Let's whip that off. And ta-da! Folks, is our sensor chip. That'd be a little BGA package, and that would, I presumably maybe have some processing on the integrated in that.

**Dave Jones:** And there you go, you can see the BGA balls under there. Stuck right down. And by the way, they did add some Loctite onto those screws, so of course they're serious about vibration in this thing. And just what is that gunk stuck to my ESD

**Dave Jones:** mat? I don't know, torn down too many things. And this, folks, is where all the magic happens, this ST-Mobile i, STM-EIQ2. And we're going to have to go for Google on this one, folks. Could be interesting reading, although I suspect we won't be able to get the full

**Dave Jones:** data sheet on this just, you know, basic top-level marketing wank for it really. You know, it'll tell you what processor it uses and all the features and all that sort of stuff, but yeah, really detailed data sheets, probably NDA, non-disclosure agreement. And on the back of that BGA device, of course they've got some serious decoupling

**Dave Jones:** happening there. Hey, that's a lot of caps. And the other processor on the bottom here is a Freescale SPC5604. And well, I think we're going to have to go to the videotape for that one, folks. And it looks like we have a 10-layer board

**Dave Jones:** here, folks, because PCB designers of course like to put on these layer markers here on each particular layer. So there's number 10 there, you can see number 9 on the layer underneath, and then if you were able to see through the board, you go

**Dave Jones:** 8, 7, 6, 5, 4, 3, 2, 1, right on the bottom! Yes! There we go. Number 1, number 2, so they've got the numbers all the way through there. 10-layer board, why do you need a 10-layer board? Well, you've got to route out

**Dave Jones:** this huge BGA package here, of course. I have no idea how many pins this sucker is, but there's all the bypass capacitor for the core, but yeah, look, they've got vias all the way in there, which is very, yeah, right to the outer edge of the chip, so it looks like

**Dave Jones:** they've at least got all pins going around there on the back of the BGA, like on the bottom of the BGA, at least going around there. They've probably got some centre stuff as well perhaps, so I'm not sure what, how many pins total.

**Dave Jones:** But to route out stuff like that, you know, it forces you into like a, you know, at least a 6 or 8 layer board. I would have guessed, you know, it'd be 8 maybe, but yeah, they've just gone for 10 because, well, they're, you know,

**Dave Jones:** putting a ground layer between everything, so. Belt and braces. And of course I haven't skimped on the connector, genuine AMP. That ain't much better than AMP, and AMP will certainly charge you for the privilege. That's why cars are so expensive. And we've got something that was, they couldn't be bothered to populate down

**Dave Jones:** there, not sure what. Let's have a look at that. By the way, it is a Rev-D board, so they've had a few sucks of the proverbial SAV there. And it looks like we've just got a couple of switching regulators around the place and stuff like that.

**Dave Jones:** Nothing too fancy, that's probably a low dropout linear reg for one of the cores. I'm not sure if it's got multiple voltage requirements or whatever on these chips, but no, I think this was a single 3.3 volt, wasn't it? There's the oscillator module, 10 megahertz, there we go.

**Dave Jones:** And yeah, there's not much else on here really, just miscellaneous support stuff. You see, like you do a basic Google search on that and you come up with ZIP. I mean, you know, you could spend a bit more time at it, you could

**Dave Jones:** decode these things, but I don't think they're worth it. Another switching converter on top, dead giveaway, there's your inductor, there's your high value caps. Nothing special at all. Got ourselves some Micron memory there. And we've got ST. Of course, ST, we've got another design

**Dave Jones:** win. Well, no surprises whatsoever. There we go, we've got some flash I believe. Yeah, that's actually a 64 megabit 3 volt flash memory. So you know, even though it's ST branded on there, it's actually associated with Micron and Neumonics as well, so I don't know.

**Dave Jones:** One big incestuous industry. Not sure what that device there is. Either I Google it and I came and the first thing was a phase controller SCR, I don't think so. But interestingly, on the bottom of it, we have, look at this, that's a

**Dave Jones:** what is that? We've got two large precision resistors there by the looks of it, and what looks like some sort of maybe common mode choke or something like that. Here we go, this freescale microcontroller, the SPC5604 is actually the MPC5604. So I don't know why it has SPC on there, but

**Dave Jones:** this is all I can find, and I'm pretty sure it is actually the one. So here you go. What is it? It's a Corvia processor. A Corvia? Like it's not an arm or anything, it's a Corvia. Microcontroller is a gateway system designed to move data

**Dave Jones:** from different sources via ethernet to receiving systems and vice versa. Woohoo! The supported data sources are video data, audio data, radar data, other serial comms including FlexCAN, LinFlex, and DSPI. Here we go, features and specifications. It's got a 64 megahertz Corvia E200 Zen-off, Zen-OH core.

**Dave Jones:** Jeez, can you get any more obscure than this thing? I'm sure it's well known in the automotive world, but jeez. I don't know, I thought the whole world was going arm. Apparently not. 512K program flash, 4 times 16K data flash. Ooh, it's got four segment data flash

**Dave Jones:** segments in it. 96K of SRAM, that's quite a bit. One motion APEG video encoder with image sensor interface supporting up to 1.2 megapixels. I wonder if that's used or not? I would have assumed that the main processor, which we'll take a look at, the main

**Dave Jones:** VisionEye thing that we saw before would have been doing everything. MobileEye. Sorry, that would have been doing the whole shebang here, and this would have just been the interface. But anyway, it does have a video encoder interface. It's got ethernet and well, I don't think they're using ethernet here, but they're using CAN bus, of course.

**Dave Jones:** Some sort of, well, FlexCAN. And what else have we got? What runs off a single 3.3 volt supply? 64-pin LQFP package, that's what we saw. So let's go to the data sheet. And here's the data sheet, folks. We've got it. Look at this, SafeAssure by Freescale.

**Dave Jones:** That's I'm assuming, we'll have to check that out, I'll have to Google that one. I'm assuming that it's some sort of standards compliance system that if it meets that, you know, it's designated safe silicon and all this sort of stuff, designed for reliable applications.

**Dave Jones:** Eh, something like that. We'll check it out. Up to 64 megahertz, single-issue 32-bit CPU. That's the type of core, the E200Z0H. Compliant with power architecture embedded, variable length encoding. Blah blah blah, failsafe operation, programmable watchdog, non-mask, fault collection unit as well, so it collects fault codes

**Dave Jones:** or something. Presumably a Nexus L2 interface. It's got DMA, it's got general purpose e-timers, 16-bit resolution, LINFLEX, four DSPI channels, automatic chip select. Oh man, tons of stuff. This is definitely not your regular microcontroller, that's for sure. One safety port based on FlexCAN 32 message objects.

**Dave Jones:** FlexRay modules, oh, it's got ADCs built in, of course. Two of them, 10 bits, with 15 input channels. So, you know, doing the regular microcontroller thing and just banging in, you know, a dozen plus input channels on their ADC there. Programmable cross-triggering unit, it's got URs, clock generation, it's got an internal

**Dave Jones:** RC oscillator, I think I saw an external oscillator module on the board there. No, but yeah, apart from, oh, ballast resistor, on-chip single-slot with an external ballast resistor, and there you go. If you want to go read the details of this rather obscure processor,

**Dave Jones:** go for your life. There's the E200Z0 core. Woohoo! Nexus 2, must be doing something magic. And yep, here we go, the Freescale SafeAssure functional safety program. As industry standards such as IEC 61508 and ISO 26262 require more sophisticated functional safety concepts, real-time control of safety-critical applications increases

**Dave Jones:** in complexity. The Freescale SafeAssure functionality safety program is designed to help you simplify the process of achieving system compliance with functional safety standards in the automotive and industrial markets. And that, folks, is why they've chosen this, because these things have to pass safety and compliance standards.

**Dave Jones:** And if you use one of these chips, which has been through this SafeAssure program or whatever, then your paperwork and stuff is probably much less and your chances of passing these standards much higher. So if you're a design engineer working on these sort of things, well, you're not going to go use your little

**Dave Jones:** microchip part that you've been using at some other company. No, because you'd end up probably failing the safety and standards compliance. So you're going to use a chip, or you're probably forced into using by company standards a chip that, you know, has all this safety and support automotive functional standards and compliance stuff.

**Dave Jones:** I don't know. If you want to read more about it, I don't know whether or not it's like silicon or whether it includes the compilers and the tool sets and other stuff. No idea. Go read it, if that floats your boat. And here, folks, is where all the goodness happens.

**Dave Jones:** Mobileye. Yes, they are a company, but they've teamed up with ST, of course, who we saw branded on the chip there. And this is the STME IQ2. Well, it's just got IQ here, but this is the IQ2. And I believe they're working on the IQ3

**Dave Jones:** at the moment, or I don't know, it might already be out. I'm not sure. But anyway, this is specifically designed for the task. Look at this. Oh man, you can go read all about it. Utilizing CMOS 90 nanometer process, operating at 332 megahertz.

**Dave Jones:** Since their first generation processor for use in vision-based driver assistance systems, and is approximately six times more powerful than the predecessor, the IQ. The IQ2 follows the same concept, albeit more powerful. So they have the IQ dual CPU cores running in parallel with multiple

**Dave Jones:** additional dedicated and programmable cores. This allows even a greater range of multifunction benefits. Woohoo! Winner of the 2008 Best Automotive Design Award. There you go. It's quite old. Who knew? Unless you're in this sort of automotive market, you just wouldn't keep tabs on these sorts of things.

**Dave Jones:** So what's inside this little puppy? Well, it consists of two floating-point hyper-thread 32-bit RISC cores. They're MIPS 32, actually. There you go, they're not ARMs, they're MIPS 32, 32K cores. Five vision computing engines. Brilliant. I guess you need, what, five to do five different objects.

**Dave Jones:** I assume they dedicate a vision computing engine to each individual item that they're trying to track, either obstacles or whether they're trying to track the lanes. I mean, this is supposed to be a lane guidance camera, but maybe it actually does more than this, or at least the chip is capable of doing

**Dave Jones:** more anyway. Whether or not they've actually implemented, I don't know. So maybe they need one vision computing core per lane marker. You know, if you're driving along the road in the center of the lane, then well, you know, maybe they need a separate vision core for each

**Dave Jones:** white marker on the road or something. Three vector microcode processors. Oh, sounds important. Denali 64-bit mobile DDR controller, 128-bit internal Sonix interconnect, whatever that is. Dual 16-bit video input and 18-bit video output controllers. So there you go, we can get video out from this thing.

**Dave Jones:** 16-channel DMA, several peripherals, MIPS 32K. CPU managers, 5 VCEs, blah blah blah blah blah blah. Very impressive! Oh man, that's a lot of silicon. Wow. This sounds very impressive, folks. Look at these classifier engines, image scaling and preprocessing units, pattern classifier units, tracker engine, image warping and motion

**Dave Jones:** analysis units. Oh man, unbelievable! There you go, it supports up all... So there you go, the interconnect ports, it can support up to 428-bit OCP buses. Woohoo! Huge! Supports a wide range of image formats, monochrome, Bayer RGB, and input frame size up to 2x2 megapixels.

**Dave Jones:** Awesome. 4 data channels, blurring, subsampling, G-curve approximation per channel, programmable cropping frame size, up to 4 histograms per channel, and video output as well. It does output frame size 4096x2048. Very impressive. There you go, by using an audible warning upon an unintentional deviation from the driving lane, these lane departure warning systems

**Dave Jones:** create an intelligent rumble strip imitation that alerts the driver even when there are no physical strips on the shoulder of the road. So you know, if you're going off, they have those rumble strips, very common to have those on the road so that you get to do do do do do do do do, like that, as you

**Dave Jones:** sort of, you know, you get that rumble sound and vibration as you move off the lane. But they're designed to do this by visual camera, real-time visual camera ID, identifying the lane to make sure you don't drift off. Man. So there you have it.

**Dave Jones:** That's very impressive and no, I can't find a data sheet on Quick Glance, as I said, you probably need an NDA to get the full data sheet on this sucker. But by all means, all the links for these will be in the video description below, so

**Dave Jones:** click on them if you're interested in checking out all this stuff. Well there's not much more I can tell you about that one folks, really. But it's rather interesting, so thank you very much Joey for sending this in, and we'll no doubt do the airbag controller

**Dave Jones:** as well in another Teardown Tuesday. And it could be actually interesting to try and power this thing up. If anyone's got any data on the pinouts here and the functionality of the pins, please leave it in the comments or on the forums. So that was certainly worth a look.

**Dave Jones:** And if you do have any more info on exactly what model, you know, what functionality this model has in this particular Hyundai car, then also leave it in the comments as well. So that was well worth a look. So if you like the mailbag

**Dave Jones:** segment, please give it a big thumbs up, and if you want to discuss it, the best place to do it is the EEVblog forum. Catch you next time.
