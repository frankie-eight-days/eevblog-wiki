---
video_id: EY0acWrCYjw
title: EEVblog #391 - Rigol DSA815 Spectrum Analyser Teardown
url: https://www.youtube.com/watch?v=EY0acWrCYjw
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 38, "3": 51, "4": 66, "5": 85, "6": 96, "7": 111, "8": 135, "9": 147, "10": 166, "11": 189, "12": 204, "13": 217, "14": 236, "15": 248, "16": 269, "17": 295, "18": 315, "19": 330, "20": 353, "21": 373, "22": 397, "23": 414, "24": 430, "25": 451, "26": 476, "27": 488, "28": 503, "29": 520, "30": 535, "31": 547, "32": 568, "33": 600, "34": 616, "35": 633, "36": 656, "37": 666, "38": 680, "39": 692, "40": 705, "41": 716, "42": 725, "43": 757, "44": 765, "45": 777, "46": 794, "47": 809, "48": 823, "49": 844, "50": 862, "51": 878, "52": 895, "53": 907, "54": 921, "55": 937, "56": 950, "57": 961, "58": 973, "59": 1000, "60": 1016, "61": 1029, "62": 1039, "63": 1054, "64": 1071, "65": 1080, "66": 1093, "67": 1111, "68": 1122, "69": 1136, "70": 1148, "71": 1175, "72": 1188, "73": 1206, "74": 1229, "75": 1245, "76": 1257, "77": 1272, "78": 1283, "79": 1300, "80": 1313, "81": 1328, "82": 1341, "83": 1361, "84": 1373, "85": 1390, "86": 1398, "87": 1415, "88": 1430, "89": 1442, "90": 1458, "91": 1467, "92": 1478, "93": 1489, "94": 1508, "95": 1518, "96": 1531, "97": 1565, "98": 1582, "99": 1595, "100": 1610, "101": 1628, "102": 1639, "103": 1654, "104": 1669, "105": 1683, "106": 1697, "107": 1710, "108": 1726, "109": 1735, "110": 1749, "111": 1774, "112": 1781, "113": 1792, "114": 1804, "115": 1822, "116": 1847, "117": 1862, "118": 1882, "119": 1903, "120": 1923, "121": 1940, "122": 1967, "123": 1989, "124": 2004, "125": 2016, "126": 2030, "127": 2044, "128": 2059, "129": 2078, "130": 2101, "131": 2119, "132": 2135, "133": 2143, "134": 2156, "135": 2169, "136": 2183, "137": 2199, "138": 2208, "139": 2220}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday with another spectrum analyzer, the Rigol DSA815-TG with the optional tracking generator. Thought we'd crack it open, take a look inside because spectrum analyzers are usually a bit more interesting than other bits of test gear like your run-of-the-mill scope or your multimeter or whatever.

**Dave Jones:** Bit more engineering poured in these things. So, you know what we say here on the EEVblog, don't turn it on, take it apart. And here it is, you've seen it before in previous videos and it's a real nice solid design, real solid bit of kit this one.

**Dave Jones:** I really like it. It weighs like 4.2 kilos. There's a lot of heft in this thing which uh indicates a lot of uh shielding, maybe some uh diecast uh stuff, of course, for the RF uh front end, perhaps.

**Dave Jones:** Um but it should be uh as easy to crack open as uh other Rigol gear is. Couple of screws here, couple of screws up the top. It'll uh the back will pop off, then we'll have uh big shielding at the uh on the top half, the shielded power supply as well.

**Dave Jones:** That'll all pop open. We should be able to access the main board but could be uh fairly involved in terms of uh getting the RF stuff apart and things like that but um I don't expect this to be a particularly uh you know, like a high-end electronics as far as the RF goes.

**Dave Jones:** No fancy black magic stuff in terms of, you know, uh PCB uh etched PCB filters and traps and things like that because this only goes up to 1.5 gig.

**Dave Jones:** It's not as far as um RF um spectrum analyzers are concerned, this thing is, you know, is pretty much a baby. It's basically working at DC as far as the RF engineers are concerned and we have a sticker on top.

**Dave Jones:** Demo equipment. Hey, we can fix that with a deft slice of the knife. There we go, No problems. And of course we have the obligatory warranty void sticker. And if other bits of Rygel gear are anything to go by, especially their new stuff, this should be pretty well designed and built.

**Dave Jones:** So it cuz they're really uh well, they've always been quite reasonable in their construction, Rygel, but as of late they uh their new series of gears seems to be designed and engineered very, very well indeed.

**Dave Jones:** So I don't expect to see any shoddiness inside this thing. I expect uh really decent build quality. And uh nice clean PCB, probably washed nicely. All that sort of jazz.

**Dave Jones:** All right, this puppy should just lift straight off. Maybe if I've actually got all the damn screws out. Maybe not. There we go. Tada! And yeah, the obligatory metal shielded back on this thing.

**Dave Jones:** Power supply under here and that'll also be shielded from the rest of the circuitry. And we've got a couple of headers down here. They're polarized with the missing pin there.

**Dave Jones:** So they're some sort of programming or and or test interface, something like that. Got the nice shielding down here in the ethernet connector and the USB. You can see the shielded lugs there.

**Dave Jones:** Really nice EMI shielding on that. And of course we've also got a little mount and shield for the mains connector there. Neat. And it looks like this whole thing is going to lift off rather than just uh this up here.

**Dave Jones:** So, get our screwdriver under there. We can lever that whole thing off, and that power supply is going to come off in one section and the obligatory big power cable going over.

**Dave Jones:** Ooh, looks nice in there. Looks nice. You'll see it in a second. Hold on to your hat. And here we have it, folks. Whoa, look at this. Beautiful. We've got the huge die-cast box we've got here for all the RF circuitry and all of this juicy stuff we've got under here.

**Dave Jones:** As you'd expect, we've got a Spartan-6 FPGA, and we'll go into details. We've got an Actel ProASIC 3 by the looks of it, some flash memory, and a Blackfin DSP processor down there, some power supplies up here, and interestingly, some a small little angled heat sink there with TO- 220 package with some packages with some seal pads under there for uh isolation.

**Dave Jones:** And this, ta-da! Check it out. They're a little bit proud of it. Designed in China. Not designed in China, so mm yeah, right. Good one. Chinglish. And we're actually looking at a version 1.05.

**Dave Jones:** Looks like the 30th of the 12th, 2011. And here we've got a fairly pedestrian, I guess you could call it a Spartan-6 FPGA. It's the XC6SLX25, and it's only like a 24 uh thousand gate device.

**Dave Jones:** So, it's not particularly high-density at all, but it does have built-in almost 1 meg of RAM. So, they're using this for the display processor. Clearly, they've Here's the external memory as well, and you can tell it's essentially the display processor because well, it's hooked into you guessed it, the display connector down there.

**Dave Jones:** And you can see all the uh uh termination resistors on the bus there to drive the uh long cable off to the LCD. And once again, the bastards, look, they've put this uh magic tape or laser etch or whatever it is on this chip here like they've done in other ones.

**Dave Jones:** And uh this is uh it looks like the um ADC because if you have a look here, there's this controlled impedance trace here running up through that via there which probably comes out of the RF section here, runs over to here, down through a few choice inductors there.

**Dave Jones:** And through a looks like there's a little I don't know, is that some sort of little common mode transformer or something? I'm not sure, but that's probably um the ADC I would be assuming with maybe some uh local voltage regulation here perhaps.

**Dave Jones:** And of course, that flows parallel output bus um flowing into the FPGA there straight into the display FPGA processor. I mean, that FPGA is probably doing other stuff as well as the display processor.

**Dave Jones:** And they've gone to town on the uh silk screen here. They've identified um all of these various um differential pair lines in here. I mean, we've got uh D in, clock, we've got done, we've got TX in, uh TXP, sync negative, sync positive, RXP, init, program, various lines there.

**Dave Jones:** Um once again, directly coupled into that main Spartan-6 FPGA. So, that's obviously the uh capture and processing as well as the display engine. And of course, that's got its own JTAG connector down in there, which they use to program this thing and or debug, or do in-system tests or something like that.

**Dave Jones:** And there's that chip up close, and yep, it does appear to be laser etched off. You can almost see the lines going across the thing, and it is definitely like stepped down into it.

**Dave Jones:** So, they've done something to really etch out the top of that chip. Bastards. Pretty darn effective, though. And down closer towards the main processor, which is a Blackfin, I'll show you in a minute, we've got another FPGA.

**Dave Jones:** It's an Actel ProASIC 3, and it's rather interesting why they use, you know, multiple vendor FPGAs in this thing. They obviously had a specific requirement based on cost or whatever, but they love to chop and change for various things here.

**Dave Jones:** Anyway, we've got a 64 megabit expansion flash memory. We've got a fast SRAM here, and up here, we've got a Cypress USB microcontroller. And no surprises, of course, for finding a Blackfin DSP processor in here.

**Dave Jones:** It's same as what they use in the Rigol series scopes. Of course, you know, they've already got the development system, a lot of code, reuse it with the Blackfin processor.

**Dave Jones:** And next to it, here, we have a Micron, sorry, a Micrel Ethernet controller. It's a KSZ8051. So, this thing actually has Ethernet built in, but they've decided to use an external Ethernet controller here.

**Dave Jones:** And this section here, just above the processor, they've got a Linear Technology LTC7328LX two-phase synchronous regulator and you can see above it just there, you can see the um two external MOSFETs as well, the two external N-channel MOSFETs used for the synchronous rectification and uh it's probably um wouldn't be a stretch to uh guess that they've uh got the um uh switching frequency of this thing locked

**Dave Jones:** to the uh sampling frequency so that it doesn't interfere with the acquisition part of the RF front end. No surprises for finding a whole bunch of uh low drop out linear regulators here, you know, triple 17s, um you know, sort of like the industry standard.

**Dave Jones:** We've got 5-V rails, they've got all sorts of little test points here, 15 V you go right over to here, we're talking 32 V up here and they've got various other uh rails and they're all hooked into nice little test points all down here.

**Dave Jones:** Very well labeled board, very well laid out. Now, there's one thing I'm not seeing around this part of the circuitry here. I mean, here's the 10-MHz reference out, external 10-MHz reference in and um you know, apart from a 32-kHz uh watch crystal up there for the time date, I don't um see any obvious crystal oscillator module on this thing.

**Dave Jones:** I would expect it I would expect it to be a reasonable quality one, but uh I assume it must be on the bottom side of the board cuz unless I'm blind, I can't see it on the top here.

**Dave Jones:** And if you're wondering what the TO-220 devices are, well, sorry, nothing exciting, just a bunch of LM317s and 337s. So, that's a very neatly presented and neatly laid out and well-engineered uh main PCB there.

**Dave Jones:** I mean, it's going to extend uh under here. It's quite possibly the full width of this whole weight unit right under the diecast uh shield here where the RF front end is.

**Dave Jones:** Um but yeah, it's you know, it's super clean. There's no flux residue on here at all. Well laid out, well silk screened. It's got all the JTAG interfaces and various things if you want to hack and play around with it.

**Dave Jones:** We've got our LCD connector down here. This will be our keyboard up here I'm assuming. And well, looks like we're going to have to take this thing apart. Look at all the screws on there.

**Dave Jones:** So, I'm not sure how this thing lifts out. I mean, there's a couple of screws on here for the main board, but I think if I just take those out, it's not just going to lift out.

**Dave Jones:** I'm And but then I'm not sure if I take out these ones first. Maybe there's a couple of them that hold it in down lower. I don't know. But you can bet your bottom dollar there's some porn under there.

**Dave Jones:** And here we go. That was an awful lot of screws and there did seem to be two lengths here, which was rather annoying. So, I only got to record a couple of them.

**Dave Jones:** But anyway, here we go. Let's lift the skirt. I expect to see some RF gasketing perhaps on the bottom of this. Oh, one big board. Oh, I know there's no RF gasketing.

**Dave Jones:** Look, it's just directly like uh you know, directly um just the machine aluminum backing on that. Go figure. So, yeah, anyway, this is a bottom of the range spectrum analyzer.

**Dave Jones:** So, I guess you don't expect to get all that goodness, but look at that. Once again, as with every RF spectrum analyzer, you'll get all this couple of filters and stuff on the board.

**Dave Jones:** I was wrong. I was wrong. We'll take a look at these. I didn't expect to see um well, much if anything in the way of PCB filters there. Because this thing's only a 1.5 gig scope, but there you go.

**Dave Jones:** It's like it's very modularized. Um I don't see any labels on the individual modules at this stage, but uh uh you know, if you know your um RS spectrum analyzer uh you know, the workings of it, the topology, the top-level block diagrams, you could figure out what each section does.

**Dave Jones:** And I just popped out the main board, and that was really easy. I mean, it's There's nothing in There's nothing holding it in there is at all once you do off all those top screws, and there's the matching shield for the bottom set of that, and of course the uh end connectors just pull straight out of there, and the board down here is completely integrated.

**Dave Jones:** It's really very nice. And look what we have here. We have another Xilinx Spartan down there, but we'll take a look at each uh section in a little bit more detail.

**Dave Jones:** I mean, jeez, we could spend hours analyzing this thing. I mean, really. Prah. And it's very typical of most products with these uh large hand-soldered uh BNC connectors, you see some flux residue around there on the board.

**Dave Jones:** Nothing major, though. And let's see if we can follow this thing, shall we? Now, I'm not going to go into a full system breakdown of a spectrum analyzer and absolutely nail each each module on the head.

**Dave Jones:** I'll leave that to the viewers. I'll be posting uh high-res photos on the uh site, by the way, so if you want to uh check out the board in some more detail, there should be some um high-res photos there for you to play with.

**Dave Jones:** Now, here's our input, of course. Here's our uh in connector down here. Straight in. Now, when you probing around these things, just be very careful about ESD cuz there is some sensitive stuff on here which you really don't want to kill at all.

**Dave Jones:** So, anyway, we've got our input there directly AC coupled straight in, hence the minimum, you know, bandwidth of this thing is 9 kHz because, well, there's a series cap on the input.

**Dave Jones:** You can't measure down to DC on these things. These are not dynamic signal analyzers. They are RF spectrum analyzers. Straight in. We've obviously got some sort of buffer or something like that.

**Dave Jones:** Not sure what the other two chips are. Might have a look in more detail. And of course, all of this is controlled impedance stuff, as you know, and as I've talked about before.

**Dave Jones:** And also, check out all the heavily stitched vias all the way around each individual module is each circuit each system module is heavily via stitched basically to lower the ground inductance to ensure that the ground in inductance in all places around the module is well, it's basically DC at RF.

**Dave Jones:** Inductance is absolutely everything. So, what have we got? We've got our input here. It doesn't look like there's any There might be some attenuation happening in there. I'm not sure, but anyway, we're jumping through the wall here because there's a die-cast shield here.

**Dave Jones:** So, this one some of them go under like like this one here is jumping under. You can see the controlled impedance trace in there. Goes through a via, then actually jumps under through a middle layer and back up through to the top side there.

**Dave Jones:** This one doesn't bother doing that. It goes straight across. I guess they wanted the minimum amount of loss there cuz when you include a via like that, vias have inductance.

**Dave Jones:** So, you know, if you want the utmost in signal integrity, you try and keep everything on the top layer here. Now, if there's any components on the bottom side of the board of any note with each module, I'll tell you.

**Dave Jones:** Now, here's a chip once again, bastards have laser um etched the number off there. Now, that possibly looks like some sort of input filter, maybe some attenuation, but those resistor values are all the same there by the looks of it.

**Dave Jones:** Then we've got some sort of amp, and then we I'm not sure what's going on there. We're going into another That's possibly No, that might be part That might be the mixer perhaps.

**Dave Jones:** Let me uh check the bottom side. And let's back up a little back to the input here. Check it out. TL072s. Hardly um RF amps or anything like that.

**Dave Jones:** So, they're just doing some very basic stuff with those TL072s. Nothing RF there at all. And then we go over into this network here. And yeah, they are all the same value resistors.

**Dave Jones:** Yep, they are. And then we jump in in. There's a low voltage um local There's a low dropout linear regulator on the other side of that. Just some local voltage regulation.

**Dave Jones:** Then we've got looks like a multi-stage LC filter there. And going into another device, not sure what that one's doing there. And once again, they've lasered the number off that one.

**Dave Jones:** Bastards. So, we're going into some sort of small network over to here, but over at this point is coming in from this filter here. So, let's check that out.

**Dave Jones:** Now, this funny looking pattern etched onto the board here, this is just a uh a multi um element stub filter. Each one of those, like that big pad on the end of that is actually acting as a capacitor, and then the trace going to it is actually acting as an inductor, depending on what size and shape you make them based on the controlled impedance uh value and uh the

**Dave Jones:** you know, the distance to the ground plane underneath, and all that regular um uh high-speed signal integrity stuff. So, you know, it might look like magic, but it's just um a basic um LC stub filter pretty much.

**Dave Jones:** And that's coming from this circuitry over here. I'm not sure what that's doing at all, but if you flip the board over, that circuitry which is under there, actually, which is under around about there, comes from pretty much the um FPGA on the bottom there.

**Dave Jones:** So, looks like we've got our FPGA feeding this around here, which then jumps over to there, as we've looked at before, goes through this um stub filter in here through this controlled impedance trace, and then it drops down to the bottom, and it actually I believe it actually connects over to there, cuz I can't see anywhere else it would connect to.

**Dave Jones:** So, it's jumping over there into there, which then mixes. So, that might be the mixer, perhaps, and this might be something to do with the local oscillator, although it doesn't seem to be enough parts around there to do that.

**Dave Jones:** Um but anyway, it's going through another network up here, through another LC filter up here, and into another magic-looking device over here, but this is nothing uh fancy at all.

**Dave Jones:** It's fairly uh common. It's just a bandpass filter. And once again, depending on the size and shape of the various traces on here based on the thickness and type of material of the dielectric, etc., etc.

**Dave Jones:** This is just a multi-element band pass filter. But, as I said at the start, why they've done that on only a 1.5 gig um bandwidth uh spectrum analyzer, I don't know.

**Dave Jones:** Cuz you can see once again, there's a just a regular component multi-stage LC filter there going into another band pass filter here, which why they didn't do that with uh regular parts at this sort of um bandwidth, I don't know.

**Dave Jones:** Um you'd have to talk to the system designer about that one, I'm afraid. So, this multi-element resonant stub filter here is really, you know, it looks kind of weird, but there you have a capacitor going to ground essentially.

**Dave Jones:** Then you have another inductor here in series, then you have another capacitor going to ground, then you have another inductor here. And you can look at there's an inductor there, there's a capacitor to ground and tiny little bit amount of inductance capacitor to ground.

**Dave Jones:** And basically, it's just a multi-element LC filter. Now, I think I might actually have a bit of a bet that this section down here is the local oscillator next to the input there.

**Dave Jones:** And if I flip the board over, there's the base of it. Once again, got another lasered chip there, the bastards. Um So, I think that's possibly the local oscillator there once again going up into this, which then possibly goes and mixes up near the top somewhere.

**Dave Jones:** Because if you know your uh spectrum analyzer topology, that's basically what you've got. You've got an input and you'll have some sort of input attenuator, then you'll have some uh filtering.

**Dave Jones:** And then basically, it goes into a mixer somewhere. So, a mixer has to be up there somewhere. Uh and then there's a local oscillator driving the mixer. So, possibly local oscillator here up there driving the mixer, which is somewhere up there.

**Dave Jones:** I don't know. I can You can spend hours analyzing each one of these blocks and drawing the complete system diagram. Uh and you'll also notice some routed slots in there like that.

**Dave Jones:** And uh they have really went, "Well, we really don't want any coupling between those sections. So, let's route out some slots." The way to do it. And once we come out of that band pass filter there, we go into another couple of blocks.

**Dave Jones:** There's some more filtering there, I'm assuming. We've got ourselves an RF relay there, by the looks of it. And going over to some more filtering. I mean, there's plenty of filtering everywhere on this thing.

**Dave Jones:** Everywhere you look, there's a whole bunch of LC filter. Hey, hello. Check out that uh top uh inductor there. Oopsie, it's on an angle. What? So, you know, like there.

**Dave Jones:** Look, there's another section of LC filtering. All right, I've got a basic block diagram of how a typical spectrum analyzer works here. Now, it's very simplistic. If you want to go into more details, there's plenty of info out there.

**Dave Jones:** Just Google it, you'll find how spectrum analyzers work in great detail. And this is going to be quite similar. So, let's check it out. We've got our input here.

**Dave Jones:** Goes into our input attenuator. So, our input on the BNC um the uh end connector down here. Uh input attenuator is going to be around here somewhere. There's going to be some uh you know, amplification and stuff like buffering and stuff like that.

**Dave Jones:** Our um input uh filter is going to be, you know, around here somewhere. Then we've got a uh local oscillator, which I thought was down around here somewhere. And then it goes into a mixer.

**Dave Jones:** And that mixes the two signals together. And then that goes into a um uh the resolution bandwidth filter. And I've know that that is actually adjustable. So I'm not sure at you know at what part bandwidth filter up there has anything to do with it.

**Dave Jones:** I don't know. It's in there somewhere and it basically then pops out and goes into your a traditional analog uh spectrum analyzer is going to have these additional stages as well.

**Dave Jones:** It's going to have an IF filter adjustable IF filter then it's going to have a logarithmic amplifier. It's going to have an envelope detector then it's going to have a low pass video filter and then goes into the ADC.

**Dave Jones:** But the DSA 815 has basically doing all that in digital. So it's basically got a high So the ADC is connected directly to there like that and it samples at high frequency and it's able to do all this traditional stuff in as you know computational stuff ever inside the Spartan FPGA or inside the DSP processor itself.

**Dave Jones:** But all that is done digitally that you used to do analog in a spectrum analyzer. But you can see I mean you know we've only got five basic blocks here for this all this RS spectrum part and you can see all you know there's like you know more than a dozen different blocks on there.

**Dave Jones:** So think like this mixer you can get multiple mixers and things like that. So you know there might be more than one mixer in there and all sorts of additional filtering and control and all sorts of stuff.

**Dave Jones:** But anyway that's just a very quick breakdown. I mean if somebody wanted to go through you could map out all the individual modules and how they fit in with your traditional RF spectrum analyzer front end like that.

**Dave Jones:** And by the way, this ADC here doesn't have to be a particularly high-speed one. It's going to be a high-precision one, but, you know, the output of your resolution bandwidth filter and your mixer here is going to be, you know, in the order of tens of megahertz.

**Dave Jones:** So, it's, you know, it's not like the ADC is for bandwidth of several gigahertz or something like that. It doesn't because the local oscillator mixes that down to a lower frequency.

**Dave Jones:** And that's why they call this part of it down conversion because it down converts it in frequency so that you can actually use a lower bandwidth ADC to do all of this extra stuff in digital.

**Dave Jones:** So, as we saw before, this is almost certainly our ADC down here coupled in to our main Spartan-6 FPGA because here's the output of it here. As we saw before, it's actually jumpered to an inner layer there as I mentioned before.

**Dave Jones:** So, it ducks under, so to speak, the ground shield around there with the die cut shield and everything else. Jumps to a lower layer there. So, this is the final output of our final filter here just before the ADC.

**Dave Jones:** And there's another TL072 down there. They just love using those on here cuz, you know, they're only working at, you know, sub-1 megahertz. They're not working particularly fast at all.

**Dave Jones:** Maybe they're um you know, buffering some sort of low-frequency signal or something like that. But, clearly we have a couple of RF amps in there. Those are a typical RF amplifier package.

**Dave Jones:** I have no idea of the part number, but, you know, they're they're basically, you know, supply, ground, input, output. But, that's a very typical package for, you know, a low-noise amplifier buffer or something like that.

**Dave Jones:** We've got another package there which doesn't seem to be lasered off like the other ones. It's sort of It's almost like it's got some epoxy or something on top of that.

**Dave Jones:** I'm not sure what's going on there. And there's our tracking generator output there. There's the big N connector. We've got a multi-stage LC filter there. As you can see, there's no uh PCB magic filtering happening there.

**Dave Jones:** And we've got yet another lasered off chip there. They really don't want you to know what ones they're using in there. They're They're almost certainly uh commercial chips. It's not like these are custom ASICs or something, but they're just stopping people reverse engineering this and it's probably not hard if you spent, you know, a few hours at it to uh find out what the device is based on the uh block diagram of A, what

**Dave Jones:** it should be, and B, you know, the uh package type and the number of pins. You can um you know, narrow it down in uh not much time at all.

**Dave Jones:** So, I'm not sure what that one's doing there. Some Obviously, uh looks like some sort of selectable filter. We've got And on the back side of the board, yet another laser marked chip.

**Dave Jones:** And there's our um Spartan FPGA. So, I'm not entirely sure uh what that's doing in the um RF uh section. Aha, I found our local oscillator. There it is.

**Dave Jones:** It's an Analog Devices ADF4106. And uh that's a 6 gig uh bandwidth um uh frequency synthesizer which they're using it as a local oscillator here. So, let's have a look here to see if we can follow it.

**Dave Jones:** Here's our local oscillator, that Analog Devices part. Let's flip this board around. And it's on the back of here. This section here. So, it looks like that's doing some sort of output uh buffering and there's some probably some filtering in there and it's outputting through the there's two there's like a transmission line going out there.

**Dave Jones:** So, let's take a look at where that pops through on the other side. No, it's obviously going to an inner layer. So, it looks like uh where are we?

**Dave Jones:** It looks like that pops up there like that. It's going into here. Yeah, so we have local oscillator on the back here coming up here probably a mixer after some of the input filtering up here and then our resolution bandwidth filter is the rest of that going out to our ADC over here.

**Dave Jones:** Aha, I finally found the main 10 MHz oscillator. There it is there and it's in the RF section here. So, it's it's generating both the system clock by the looks of it for all the digital section as well as of course all stuff for the RF section.

**Dave Jones:** So, then it just pops out here and we've got some additional circuitry over here and it eventually comes on over to clock all of the digital stuff as well because there is no local oscillator here no pun intended for the DSP processor and the rest of the digital stuff.

**Dave Jones:** And if you have a look at the backside of the local oscillator circuitry here, you can see some more PCB components going on. We've got diodes here and look it goes through this long controlled impedance trace over to the via stitching over here.

**Dave Jones:** Why do they do that? Because that is a controlled impedance component on either side of that. And in this block here just above the main oscillator down here, I found an Analog Devices AD5449 dual out dual current output DAC with some companion TL07 two devices there to convert the current output into voltage.

**Dave Jones:** So, that's been a relatively quick overview of the DSA815 main board. And it's relatively impressive. I really like it. They've It's well-engineered. And you know, it's only a 1.5 gig spectrum analyzer, but they they you know, they really seem to have gone to town here.

**Dave Jones:** And it's not just you know, some gimmick. That's why the performance of this thing isn't bad. And well, is you know, is pretty spectacular for the price actually. And they've done a lot of work integrating this thing into a single board.

**Dave Jones:** I really like it cuz there's nothing else in this product. Just this main board and the power supply. And there's the connectors bolted directly on there. Brilliant. I like it.

**Dave Jones:** Thumbs up. And there's a quick peek inside the power supply. It's you know, they're doing all the right things. They've got input protection. They've got input filtering. They're using Epcos brand capacitors, which aren't too bad at all.

**Dave Jones:** They've celastic'd a lot of it down. They've got output filtering. Yeah, it's all happening. They've got high voltage isolation slots there. We won't go into it in too much detail because really it's not that interesting.

**Dave Jones:** And we've done that in previous videos like this oscilloscope teardown. But yes, it is a good quality. Looks like a quite a reliable or should be quite a reliable power supply.

**Dave Jones:** Well-engineered. It is Rigol branded there, but yeah, they they may have subbed it out to somebody else. But yeah, its model number is LPS SMPS80 version 1.1. And of course the rest of the guts under there not particularly interested in that at all.

**Dave Jones:** It's just a display and the keyboard will have some local circuitry on there for the keyboard. Boring as the proverbial bat poo. So there you go. It's back together again and yeah, that was really interesting.

**Dave Jones:** I mean got our ADC here and pretty much I think that Spartan 6 FPGA there is probably doing like the all your traditional sweeping functions and whacking it all straight into memory doing some processing and stuff perhaps.

**Dave Jones:** Not sure how much of the heavy lifting the Blackfin DSP processor is doing down there. Probably not much like in the other Rigol's it's probably just doing some you know, just your you know, regular gooey interface type stuff and things like that.

**Dave Jones:** So maybe all the grunt work is done inside that Spartan 6. But as I said that's not a particularly large unit. So but it's at least handling the ADC input there.

**Dave Jones:** So it is doing that and quite possibly it looks like it's driving out here as well. Like it's generating like there's all these clocks and and control signals and stuff.

**Dave Jones:** So it's probably going out here and controlling the you know, the local oscillator and doing all sorts of jazz like that. So who knows. So there you go. The warranty has been voided.

**Dave Jones:** Gone-ski. And let's power this thing up and see if she still works. And it looks like we have a winner folks. Check it out. There we go. Little spikes from my RF remote here.

**Dave Jones:** Beauty. And uh yeah, that was an interesting look inside the Rigol DSA 815. Very well-engineered bit of kit, especially for the price. I mean, this is practically uh the lowest-price spectrum analyzer like this on the market by far.

**Dave Jones:** Um yeah, it's a great nicely designed engineered unit, but that's uh what we've come to expect from Rigol these days, and they certainly didn't disappoint. I think it's a winner.

**Dave Jones:** So, if you want to discuss it, I've almost certainly um skipped over stuff and missed stuff, and maybe got the odd thing uh back to front. But, the best place to discuss it is over at the EEVblog forum.

**Dave Jones:** Catch you next time.
