---
video_id: 2CCWnJ35obQ
title: EEVblog #271 - Zoom H1 Recorder Teardown
url: https://www.youtube.com/watch?v=2CCWnJ35obQ
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 32, "3": 46, "4": 63, "5": 77, "6": 94, "7": 108, "8": 120, "9": 136, "10": 151, "11": 164, "12": 179, "13": 191, "14": 208, "15": 221, "16": 236, "17": 253, "18": 269, "19": 283, "20": 303, "21": 323, "22": 339, "23": 357, "24": 370, "25": 386, "26": 401, "27": 419, "28": 433, "29": 445, "30": 463, "31": 479, "32": 493, "33": 509, "34": 524, "35": 535, "36": 548, "37": 570, "38": 582, "39": 597, "40": 612, "41": 628, "42": 643, "43": 658, "44": 674, "45": 688, "46": 704, "47": 716, "48": 732, "49": 749, "50": 765, "51": 782, "52": 797, "53": 813, "54": 829, "55": 850, "56": 870, "57": 885, "58": 899, "59": 915, "60": 927, "61": 942, "62": 956, "63": 971, "64": 990, "65": 1006, "66": 1024, "67": 1042, "68": 1059, "69": 1074, "70": 1091, "71": 1105, "72": 1119, "73": 1136, "74": 1156, "75": 1176, "76": 1190, "77": 1204, "78": 1219, "79": 1235, "80": 1254, "81": 1269, "82": 1286, "83": 1303, "84": 1318, "85": 1338, "86": 1359, "87": 1373, "88": 1386, "89": 1402, "90": 1415, "91": 1428, "92": 1439, "93": 1454, "94": 1466, "95": 1478}
---

**Dave Jones:** Hi. Welcome to Teardown Tuesday. Where's the thing I'm going to tear down? Well, sitting on top of my video camera and I'm using it right now to record the audio for this video. It's the Zoom H1 handy recorder and

**Dave Jones:** here it is. Oh, I might be peeking a little bit. Check, check, check. Definitely going to peek there. It's a little handy wave MP3 stereo recorder and it's got an external mic out and you can use it to uh record stuff for your video.

**Dave Jones:** Let's check it out. And here it is. It's a very nice little compact bit of kit and I love it. It retails for like under a 100 bucks and it's a stereo MP3 or wave recorder. It's got a

**Dave Jones:** selectable MP3 wave switch on the back there. Let's have a look at this. It's got a auto volume level on and off. It's got a low cut filter which is great for actually cutting out low frequency noise and possibly some hand hold noise if

**Dave Jones:** you're using it as a handheld mic. It's powered from a single double A cell in here. It's got a standard thread on top for mounting on top of your camera or on a little mini tripod and it's got a nice

**Dave Jones:** LCD on it which has a proper VU level meter. It's got a basic start stop record function and it's got a power switch. It's got USB interface so it can be used as a USB mic and it's got some basic

**Dave Jones:** commands, input level so you can have auto or manual level level set and it actually has an external microphone input as well. So if you want to use a better quality handheld mic or something like you can stick this thing in your

**Dave Jones:** pocket and you can use like a external handheld mic then well, you can certainly do that. Use it as a portable recorder or a line in as well. So, you can use it to record stuff from like a

**Dave Jones:** tape deck or a something like that. It's got a uh clip um level indicator here. So, if your uh input clips, then it'll show you that. And it's got um these stereo microphones down in here. And uh they're

**Dave Jones:** in this crisscross uh fashion because that makes them equidistant. Wank word of the day, equidistant from the source, regardless of where the audio source is, if it's right out here, or if it's out here, or if it's in front like this,

**Dave Jones:** these are the same distance, so there's no phase difference between um if you had a traditional uh stereo microphone, they would have two separate uh mics like might be out here. And if your source is over here, there's

**Dave Jones:** different uh lengths to get to each microphone. So, if I put them in this cross configuration like this, they um just work. And apparently, it reduces the uh any uh phase any um issues due to uh phase, and it's supposed to increase

**Dave Jones:** the stereo imaging and all that sort of audio wank word stuff. But, there you go, it's a very nice little handy recorder. Oh, and it's got a volume and a speaker on the bottom, as well. And it's got a

**Dave Jones:** micro SD card in there to record your uh stuff directly on. It's very nice little recorder. I love it. So, let's open up this thing and uh see what's inside. Now, I expect a uh micro processor. I don't know what uh type it'll probably

**Dave Jones:** have an M because it's got MP3 uh encoding uh capability. Maybe there's a separate uh MP3 encoder chip or something like that, or maybe it's built into the main micro, and there'll be an analog-to-digital uh converter as well.

**Dave Jones:** That'll be a 24-bit type cuz this thing's capable of um it's got a 24-bit analog-to-digital converter up to 96 kHz uh sample rate. So, you know, it's pretty high-end stuff. I expect there to be some uh shielding in there because

**Dave Jones:** we're talking about, you know, a 24-bit converter. So, there won't be a terribly a terrible amount more than that ADC and a micro and maybe an MP3 encoder and some miscellaneous circuitry, some level stuff. So, there'll be some analog input

**Dave Jones:** circuitry, but that's probably about it. The micro probably controls the SD writes directly to the SD card and well, I don't know. We'll find out. Let's open it. Looks like we've got two screws there and let's see if there's a another

**Dave Jones:** screw inside the battery compartment. Doesn't look like it. So, take out these two screws for starters and maybe it just lifts off like that.

**Dave Jones:** Using my spudger here to There we go. It's got a clip in there and a clip in there and it's probably got another one up the back here, but it looks like it separates like that. So, yep. Bingo. It looks like there's another

**Dave Jones:** clip up the back. And ta-da! There it is. Now, that's rather interesting. The first thing I notice, of course, is this uh copper shielding here on top of this board. It's soldered at a couple of points down in there and

**Dave Jones:** that's rather interesting. I guess they decided it's almost as if maybe it's a uh maybe it's an afterthought. I'd have to have a look at the PCB pattern down in there, but anyway, we've got our flat flex cable going over

**Dave Jones:** to the switch. Uh switches on the back of the unit here. So, it looks a fairly uh They've really uh jammed a fair bit of uh electronics physically in here. These are these uh tall uh surface mount electrolytic capacitors

**Dave Jones:** fit in this space up along here. And uh this board here is clearly the uh DC to DC converter because you need that because it's only a single cell. It's only 1.5 V. I don't know what voltage it

**Dave Jones:** actually uh operates down to, maybe 1.1 minimum or if it'll be nicely designed it might be 1 V or 0.9 V minimum. But um uh you obviously need a uh boost step-up DC to DC converter for that. And uh I looked at that chip under

**Dave Jones:** the uh microscope and it doesn't uh it's not readily identifiable. It uses some uh weird code mark, but uh there you go. It's a basic boost converter. You can see the uh gold test points there, there, there, and there. They're for the

**Dave Jones:** production uh test jig. They would have a bed of nails uh tester that they would test each individual board on. Now, this is rather curious. They've got the USB uh mini B connector there connected uh soldered onto the DC to DC converter board up the

**Dave Jones:** top here. And uh really that's very that's quite strange because you'd have to get the uh data connections off this board. So, presumably it's got a either there's a ribbon cable under the bottom that connects down to the bottom board,

**Dave Jones:** presumably where the processor is, or it's got through the DC to DC converter and somewhere else. Or there could be a processor over here perhaps. I haven't lifted that flap up there, but it's got to get those data connections all the

**Dave Jones:** way through that DC to DC converter. That's just a rather unusual placement for the USB connector. And check out the uh footprints there for those little surface mount resistors or capacitors there. They've got no solder mask removed. So, they've decided that they

**Dave Jones:** don't uh want want to mount those components and they've actually haven't they've actually closed off the solder mask for those. So, there's no solder on those pads at all. That's not fairly common. Usually on unpopulated footprints like that, you would just

**Dave Jones:** leave the solder mask open and you'd see the reflow solder on those pads, but not in this case. Now, let's take a look at this side of the top board the or the blue board as we'll call it here and

**Dave Jones:** there's this plastic is that looks like a plastic protecting there's another copper shield under all of that and that's not very surprising because these are your input and output connectors here. So, this is all your audio stuff your analog to digital

**Dave Jones:** converter and your DAC and stuff will be all under there and possibly well the actual processor is probably down on the bottom green board down in here and I'd say this is all of your ADC and amplifier stuff cuz it's got to drive

**Dave Jones:** the speaker which is all the way over here by the way and uh so, let's take a look. Let's lift up that lift up the skirt and see if we can find anything under there. We may actually have to

**Dave Jones:** desolder the shield. Geez, I hope not. And of course, you can see the microphone connections there and there as well. So, this is really that's why it needs all the shielding and I can't seem to get that plastic off. It

**Dave Jones:** seems to be stuck down well and surely it adhesive stuck to the copper board there. So, looks like we are going to have to desolder that. I'm a There's the circuitry underneath. There's a couple of devices there. I'll

**Dave Jones:** put those under the microscope and see if I can get some numbers. And there's the main device there. It's a Texas Instruments AC 3101. So, we have to check out the data sheet for that. Well, no major surprises at

**Dave Jones:** all. It's an off-the-shelf stereo audio codec from Texas Instruments. It's It's a TLV 320AIC3101. Uh 01. They don't put uh the extra uh info on there. They just stamp the chip uh 3101. But, you search for it and it

**Dave Jones:** uh pops up. No problems at all. It's got an DAC and an ADC. The uh stereo audio uh DAC here is it got a 102 dB signal-to-noise ratio. Um uh sample rates up to 96 kHz. It's got some uh

**Dave Jones:** wanky effects as well, bass, treble, 3D stuff, and de-emphasis, and things like that. They're probably not used in this particular uh product. And the stereo uh ADC down here at 92 dB signal-to-noise ratio is supports sample rates up to 96

**Dave Jones:** kHz. Hence, the uh spec on this thing. It's a uh classed as a 24-bit analog-to-digital converter up to 96 kHz sample rate. Um it's got some DSP stuff as well and noise filtering available. I'm not sure if they actually use that. They may.

**Dave Jones:** It's software selectable. And it's actually got uh six audio inputs. It's got one stereo pair, single-ended. It's got one stereo pair, fully differential inputs. Um and it's got six audio output drivers. Wow, it can drive uh differential and single-ended

**Dave Jones:** headphones. It can drive stereo line outputs. Hence, this thing's capable of uh dual headphone and line out uh capability. Um and it's got a 500 mW um speaker driver as well. They're probably not uh driving it that hard in this thing. It's

**Dave Jones:** only a tiny speaker in there, but it's capable of doing that. It's low power. It only takes 14 mW um during uh playback. It's a 3.3 analog supply. Uh what else we got? It's got automatic gain control, which uh there's that

**Dave Jones:** switch on the unit, which um selects uh uh, automatic gain control on the input or manual. Um, it supports, um, it has microphone bias as well built in. You would need that for these, uh, electret, uh, microphone inserts. And,

**Dave Jones:** uh, it's got nice I squared C control bus for setting the data and uses the, uh, no surprise as most of these audio class, uh, codecs do. They use the, um, I squared S, uh, not to be confused with

**Dave Jones:** I squared C. I squared S, uh, audio interface, um, industry standard type thing and it's in a 5 mm by 5 mm 32-pin QFN. Let's take a look at the block diagram and it contains a lot of, uh, analog and

**Dave Jones:** digital stuff that would ordinarily require a, an awful lot of, uh, separate, uh, discrete circuitry. So, um, the inputs here, it's got, uh, a programmable gain amp from 0 to almost 60 dB in half dB steps. Wow, going into

**Dave Jones:** the ADC. It's got the auto gain control there. It's got, uh, line inputs. It's got the microphone amplifier here and a summer and there's the, uh, I 2 S, uh, audio, uh, interface and, uh, it's got some switches, the effects processor down

**Dave Jones:** here, volume controls and then another DAC. Oh, jeez, and then the output, all the output, uh, muxing for the, um, uh, headphone, uh, outputs and the, line outputs as well and the, of course, all the, uh, I squared C control, um, uh,

**Dave Jones:** data interface and, uh, the clock generation as well and then the microphone biases and the different voltage supplies it needs. It's a really heavily integrated device. And if you take a look at the typical circuit configuration here, you can see that,

**Dave Jones:** uh, the I 2 S interface connects to a DSP or an application processor. We could have, yeah, a DSP or a microcontroller, but because this has to do MP3 encoding unless there's a separate MP3 encoder chip on the other board which we haven't

**Dave Jones:** seen yet which is quite likely. Then it would need a fairly heavy DSP because it's not easy to do MP3 encoding on a low-end microcontroller but pretty basic stuff. It's got the microphone electric microphone input here with the

**Dave Jones:** microphone bias supply AC coupled pretty standard stuff. Line inputs here also AC coupled another line input here and well it's got a whole bunch of line inputs and then the headphone driver down here an external audio power amp so it's recommending

**Dave Jones:** if you know a separate external amp if you want to drive a decent type of speaker load instead of headphones and lots of decoupling over here for the built-in supplies. So there's a whole bunch of stuff analog VDD is rated from 2.7 to 3.6 and it also

**Dave Jones:** needs for the IO as well go can go down to 1.1 volts to 3.3. So that's rather neat and that's all there is to it and you'll basically find that all this stuff will be mirrored on the PCB. It's just got a

**Dave Jones:** whole bunch of coupling caps and decoupling caps and a couple of pull-up resistors and that's about all and that's what we see on the board. Now this is rather interesting. I highly recommend you read the data sheet if you

**Dave Jones:** want to know how the AGC setting works. I haven't read the manual for this thing maybe it explains fairly well but this is you know coming from the horse's mouth directly from the chip manufacturers data sheet because AGC's automatic gain controls can be

**Dave Jones:** rather tricky and if you use them you know you've got to know exactly how they work under what conditions otherwise you could end up with things that are clipped or too low and audio that's all over the shop. So, you want

**Dave Jones:** to know about the decay time and that's actually selectable. So, who knows what decay time that they're actually using that what they've set that in software hard-coded that into the firmware of this thing. So, if you go down here, it

**Dave Jones:** can show you your input signals and your output signals and how it adjust that in real-time. So, if I'm recording like a lecture or something like that, I'll set the level up manually. I'll place the thing, set it up so that I know that

**Dave Jones:** it's going to give me a consistent audio level and I don't have to rely on any tricky business happening in the AGC. And there's a digital audio processing for playback and there's all sorts of stuff in this data sheet. So, I

**Dave Jones:** highly recommend you check it out if you're interested in how this sort of stuff works and the digital interpolation filter and the delta-sigma audio decks. It's all in here. It's great stuff. Excellent bedtime reading. And the other part is a JRC 2100A04.

**Dave Jones:** Not familiar? Well, you'll have to check it out. Maybe it's some sort of uh you know, dual op amp or dual microphone amplifier or something like that. And I was right on the money on the other device, the JRC 2100 is actually an NJM

**Dave Jones:** or New Japan Radio 2100 dual operational amplifier. No funny business going on there at all. It's just a low operating voltage plus minus 1 V to plus minus 3.5 V single supply operation dual op amp. No more to

**Dave Jones:** say there. And if we have a look at the dual board construction here, I was able to lift out the microphone insert over here and you can see the board-to-board interconnect they've got down here. And there we go. We can see the bottom

**Dave Jones:** board. We can see the side switches directly right angle side tactile switches directly soldered onto there. Some test pads that would be for programming the microcontroller. That'd be the JTAG interface. I haven't even looked at the silk screen there, but that's obvious

**Dave Jones:** what that is. A couple of more side tactile switches up here. There's the flat flex cable directly soldered onto the board. A whole bunch of resistors neatly laid out in lines. I like that when you're laying out a board. It's

**Dave Jones:** rather neat. And let's go in and see if we can find out what sort of a processor that thing is. And you can see the uh other bunch of electrolytic caps for the for the coupling input and output coupling here. These

**Dave Jones:** large ones would be for the output coupling for the headphones. And another And some of those would be used for the input coupling as well. One rather interesting thing to note is you'll notice that the shield of the USB connector has this

**Dave Jones:** black wire running all the way up to presumably one of the grounds up here, one of the analog grounds right up there, which might be connected through to the shield on the top. I'm not sure, but obviously that's like a maybe an

**Dave Jones:** afterthought perhaps. Or maybe that was the easiest and best way they could get that all the way back to that on the double-sided board. Who knows? But they've obviously had to do that to get the noise down in some way, shape,

**Dave Jones:** or form. And you'll also notice the extra circuitry in here for the DC-to-DC boost converter. Now, if I take out these little plastic clips either side here for the plus minus buttons, then the board seems to seems to lift

**Dave Jones:** out somehow, perhaps, very gingerly. I don't know. This could be tricky. I might have to uh get some pliers there and pull it out vertically, perhaps. And there we go. I got it. Aha! There we go. Now we've got some serious

**Dave Jones:** stuff happening. Awesome. And bingo, there was too much uh happening to all be on that one tiny chip on the top. So, obviously, we've got some sort of processor here. We'll check it out. One of these is probably the MP3 encoder.

**Dave Jones:** We've got our SD card directly mounted on the board. Another device over here. Our tab mounted uh LCD custom LCD display over here. Our carbonized PCB button which connects to the rubber uh button for the front panel for the

**Dave Jones:** record switch. And a few miscellaneous things. And a real-time uh clock for the time and date. That's the 32 uh kHz crystal. And there's another uh surface mount connector up here which they decided not to populate. And there we

**Dave Jones:** go. The main processor is a DSP. It's the classic uh Texas Instruments TMS 320 series. And the first device we've got up there is an EN 39SL800. And that's an 8 megabit flash memory. And the other device we have there is a

**Dave Jones:** Cool Magic. Uh haven't heard of them before, but it's a CMS 3216LAH-75. And I believe that's actually an SRAM. So, there you go. We have a uh Texas Instruments TMS320DSP processor. We have external flash, and we have external SRAM. Now,

**Dave Jones:** interestingly, this is a TMS320C5504. And it already has uh 256K of built-in SRAM and 128K of ROM. That's It's a huge amount of ROM, but it is a lot of SRAM, but maybe they need a lot more. So, I

**Dave Jones:** given given the proximity of these two devices to the TMS320 up here, this does actually support external memory up to 4 meg. So, it's most likely that they are actually external flash and SRAM for the TMS320 processor. Now, the thing that's missing, of

**Dave Jones:** course, is the MP3 encoder capability, and that's either built in to the TMS320, and I'm sure it's probably uh capable of doing that, but there's this mysterious device over here which we couldn't identify, which is close to the

**Dave Jones:** connector going through to the top audio board. But, of course, one thing the TMS320 processor is not going to have is an LCD driving capability, especially to drive all the segments that are actually on this display. It's a large number of

**Dave Jones:** segments. So, clearly, also given the location of this micro here, it's it's pretty obvious that this is the LCD controller because it's close to the tab the tab connections on the left-hand side there. So, that's some sort of

**Dave Jones:** maybe custom or rebadged LCD controller. And that means that the MP3 encoding must be done in the TMS320 processor. Hence, probably all the extra external SRAM and ROM required. Now, for those curious about the copper shielding here, that's clearly all over this digital

**Dave Jones:** circuitry here cuz we've got parallel buses running between the external memories and the DSP. And maybe, you know, around here we've got the SD card. So, you know, there's the main crystal oscillator for it by looks of it. So,

**Dave Jones:** all of that sort of stuff is running, you know, it's going to be running at a reasonable frequency, and it's all going to be digital stuff. So, they've obviously just shielded on there. Now, whether or not that's an afterthought uh

**Dave Jones:** to meet our EMC or noise compliance or uh something else after they did testing, I'm not sure. And based on the looks of uh the pads designed into the PCB to solder this uh copper shielding down onto it, um it's at least uh

**Dave Jones:** thought out as part of the uh PCB PCB design. So, it's not just a you know, it's not just a hack add-on or anything like that after the fact, but maybe it could have been. Maybe they did their original uh testing and they found

**Dave Jones:** oops, you know, we probably need this uh copper shield all the way over here. So, they might have respawned the board to uh add in the uh pads there for the shield. Who knows? Or they could have been smart and designed it in to begin

**Dave Jones:** with. Your guess is as good as mine. So, there you go. I hope you enjoyed that. That's the Zoom H1 handy recorder. I rather like it. It's a nice neat bit of kit. It's uh actually uh fairly well

**Dave Jones:** designed and uh fairly compact. They've put a lot of uh thought into maximizing uh the amount of uh circuitry inside the 3D envelope in the case to uh keep this thing quite tiny. They couldn't have made it uh much smaller without a

**Dave Jones:** significant uh um more amount of effort. And it's like less than 100 bucks. So, uh if you're in the market for one of these things, I highly recommend you pick one up. They're very neat. So, if you like Teardown Tuesday, please give

**Dave Jones:** the video a big thumbs up cuz that really does help a lot. And uh if you want to discuss this thing, uh go and jump on over to the EEVblog forum and there should be uh some photos on my

**Dave Jones:** Flickr account as well for you to check out eventually. So, till next time. See you.
