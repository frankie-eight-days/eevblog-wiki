---
video_id: 9KcOQsVxtoU
title: EEVblog #976 - Keysight 1000 X-Series Oscilloscope Teardown
url: https://www.youtube.com/watch?v=9KcOQsVxtoU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 41, "3": 56, "4": 73, "5": 91, "6": 114, "7": 133, "8": 150, "9": 169, "10": 183, "11": 206, "12": 222, "13": 239, "14": 261, "15": 284, "16": 306, "17": 321, "18": 337, "19": 357, "20": 375, "21": 399, "22": 418, "23": 433, "24": 455, "25": 471, "26": 491, "27": 508, "28": 525, "29": 548, "30": 569, "31": 581, "32": 596, "33": 613, "34": 632, "35": 648, "36": 662, "37": 682, "38": 704, "39": 717, "40": 736, "41": 755, "42": 772, "43": 788, "44": 803, "45": 819, "46": 836, "47": 854, "48": 866, "49": 883, "50": 902, "51": 918, "52": 933, "53": 952, "54": 969, "55": 990, "56": 1006, "57": 1023, "58": 1041, "59": 1056, "60": 1072, "61": 1088, "62": 1105, "63": 1122, "64": 1142, "65": 1161, "66": 1183, "67": 1201, "68": 1216, "69": 1241, "70": 1251, "71": 1273, "72": 1291, "73": 1306, "74": 1324, "75": 1345, "76": 1363, "77": 1385, "78": 1405, "79": 1424, "80": 1442, "81": 1460, "82": 1478, "83": 1499, "84": 1517, "85": 1534, "86": 1553, "87": 1569, "88": 1590, "89": 1606, "90": 1619, "91": 1635, "92": 1652, "93": 1665, "94": 1679, "95": 1697}
---

**Dave Jones:** Hi. It's always exciting when Keysight release a brand new oscilloscope, because it doesn't happen that often, especially in the lower-end market. In fact, the last time it happened was just over six years ago, way back when I was working in the garage and I did the review in the garage

**Dave Jones:** of the original Keysight 2000X and 3000X oscilloscopes. And they made a huge impression in the market, you could say almost practically game-changing, with their built-in function gen and their high-speed MegaZoom 4 ASIC and everything else. It was absolutely fantastic. But six years later, they've released the brand spanking new 1000X series,

**Dave Jones:** which uses the exact same MegaZoom 4 chip that we saw six years ago. So they're still trying to eke out the return on investment on that MegaZoom 4 ASIC that they had to design. And, well, no doubt, it probably costs some cheapest chips now.

**Dave Jones:** But it's amazing that we can now get that MegaZoom 4 ASIC technology in a $450 scope, and that's what this one starts at. This is the top-of-the-line unit, the 1102G, with the built-in function gen, and I'll be doing a separate review video on this, so I won't go into it.

**Dave Jones:** Anyway, two gig samples per second, 100 megahertz, only two channels, but it's got the built-in function gen, and it's got the demo stuff, same as the 2000 and 3000X series. And for those who do want to see the size difference, it's pretty substantial.

**Dave Jones:** And it gets the industry benchmark in low-end scopes, the Rigol DS1054Z. They're practically identical in size. Now, as far as the look and feel of it goes, it's exactly the same as the 2000 and 3000X series. The knobs are identical, the indents, everything else, the indented feel of them is absolutely identical.

**Dave Jones:** And as is common with practically every low-end scope on the market, they emit the automatic x10 probe and the probe power interface. But, you know, you expect that. And it's got quality tilting feet like that, with the rubber at the back. It ain't going anywhere, it feels really nice and solid, well-built,

**Dave Jones:** even kind of like the new sort of styling look on the thing. Anyway, this ain't a review. On the back, you've got power and you've got USB, that's it. No LAN, thank you very much. And yes, it is made in China, not made in Keysight's Malaysian facility,

**Dave Jones:** so I'm not sure if it's a Keysight facility in China or whatever, but it is not a rebadged scope. I want to make that clear, it is not a Rigo, it's not anything else, it's 100% designed and manufactured by Keysight. But who actually manufactures the thing, on what line, I don't know.

**Dave Jones:** But it's somewhere in China. So you know what we say here on the EEVblog, don't turn it on, take it apart. And just like other similar scopes, two screws here, two under there, and this whole panel will lift off, but expect to see a lot of shielding,

**Dave Jones:** because this thing ain't light. So they promote this and have a slogan, scrap the toys, get a real oscilloscope. So we expect to see real oscilloscope quality in here. Any rust on the chassis? Nope. Now you can't hear it on here, but the fan is kind of annoyingly just on the loud side.

**Dave Jones:** Like it's not howling, but it's noticeable in a quiet lab. Yeah, I don't like it, I think it's a bit of a fail. And we've got a real clunking mains power switch. Another soft power rubbish. And yes, confirmed, it does actually draw zero power.

**Dave Jones:** And the folded metalwork looks typical for a scope like this. Yes, we've got our proper RF fingers here, no worries. There physically is nothing on the board down in there for the Ethernet interface, so don't get excited there. And external BNC is just not there.

**Dave Jones:** But hey, they put them in the metalwork, so who knows. Alright, let's get straight into it. Quite a few screws around the outside here. And let's pop it open. Ta-da! We're in like Flynn! Oh, look at that! Two-board construction. Look at this, I haven't seen this in a Keysight scope before,

**Dave Jones:** but we've seen it in other low-cost ones, notably the Instek, I think it was. A separate board for the MegaZoom 4 ASIC and the ADC, and the main ST arm processor and another Xilinx FPGA. So all the logic. So this is interesting, why they've done this.

**Dave Jones:** Is it for an upgradeability thing? I don't think so. But possibly they split it out maybe to two design groups, perhaps? And then they thought, oh, we can tweak the processor and everything later, keep your design decisions further down the development, your final decision on what you're going to include, what you're not going to include,

**Dave Jones:** further down the process rather than have to re-spin the top motherboard. But of course it's going to cost you more to put it on the separate board like that with the connectors, in theory anyway. It's going to cost you more, but hey, that'd be nice and easy

**Dave Jones:** just to test your processor and FPGA and ADC board on its own like that. You just plug it straight into a test jig and Bob's your uncle. So yeah, I like that. We've got a metal shielded can down here. It looks like we've got a screw on the top, so it looks like we can take that off.

**Dave Jones:** Hopefully it doesn't... oh yeah, it might be soldered down anyway. If it is, we'll rip it off, no doubt. Power all around here. We've got external trigger over here. And this would be the function gen and your waveform and that extra waveform output that they've got there.

**Dave Jones:** Battery backup, of course. And not much doing at all, as you'd expect in a $450 scope. You'd expect a cheapest chip's front end, 100 MHz bandwidth. Yes, even the 50 MHz model is going to have the full 100 MHz bandwidth. They're just software limiting that.

**Dave Jones:** And, of course, the MegaZoom 4 ASIC, which would be this puppy here, I believe, because this one's going to be your ADC. And yes, one ADC handling two channels. Wait a minute, I can see some Siglent-style rust. Ha, ha, ha, ha, ha. Yeah, it wasn't there at first glance, but yep, bonus rust with every low-end oscilloscope.

**Dave Jones:** Nothing particularly novel on the thermal airflow point of view. There's our fan down in there. It's blowing into this, so it's sucking air into the unit. Practically, like, directly over the processor here, and then that will just go disperse out, go over the heatsink fins here,

**Dave Jones:** and go out the back holes here, vent holes here. So nothing special, there's no vent holes on the side, so it's pretty much going to come down and go, and out. Meh, whatever, it'll get the job done. But I'm certainly not a fan of the fans.

**Dave Jones:** Sengen Henglixin Electronic Code Limited. Okay, underwriters listed. Anyway, there's no compliant mount on that, so rigidly coupled down to the chassis, so the vibration is going to possibly be amplified a little bit by the chassis. That's not helping. You probably don't expect that in a $450 bottom-of-the-range scope, though.

**Dave Jones:** As for the mains wiring, no worries. It's all heat-shrunk, of course. Nice touch, they've put the rubber grommet around there so it can't, you know, cut through the wires accidentally. Nice earth point. Everything doing right, no worries. And wow, check out the power supply.

**Dave Jones:** That is one of the neatest power supplies I've seen in a long time. Look at everything. God, someone's gone to town with a Celastic gun. Look at this, Celastic absolutely everything. Nice touch, they've got Loctite on the screws there. Beautiful. No worries whatsoever.

**Dave Jones:** Obviously, all of the active circuitry is going to be surface-mount on the back, but the input is fused, no worries. It's got common-mode choke. It looks like it's got MOV protection on the input. And it's just a beautiful layout. Look at it. Everything's nicely spaced and separated.

**Dave Jones:** Big thumbs-up to that. And there's the model number for those playing along at home. Oh, I guess you could say that they've skimped a little bit with the direct wiring straight to the PCB on the output there. Didn't bother with the connector. Saved a couple of cents.

**Dave Jones:** But who the hell is AsiaX? What? AsiaX caps. 105 degrees C rate, a little bit close to the heatsink there, but meh. And the others are OK cap. Oh, please. Oh, this is not instilling confidence in me. I mean, you know, they can't even keep the same manufacturer.

**Dave Jones:** Give me a break. And on the blue output caps there, they're Aishi brand, or however you pronounce it. Yeah, they're one of the biggest manufacturers in China, but yeah, not exactly highly ranked. And the other green ones there are Zunda. Oh, my. Mix and match.

**Dave Jones:** What did they get at the Shenzhen market this week? There's the bottom side for those playing along at home. That looks neat and tidy. Once again, like, I like the design and layout of this thing. It's just let down by some cheap-ass caps, perhaps.

**Dave Jones:** But anyway, yeah, we've got our spark gaps down there, and you know, it's all doing. In fact, that seems to have a conformal coating on the bottom of it. Interesting. And if we lift off the processor board here, you can see that there's bugger all underneath it.

**Dave Jones:** We've got four high-speed board-to-board interconnects there. Par for the course of course. The horse is a course of course, of course. Anyway, yeah, so they could have put all this logic on one board and potentially saved themselves a little bit of cost here.

**Dave Jones:** But no, they've gone for that second board. So there's obviously some sort of strategic design decision to put that on the second board. I'd love to hear the design team's reason for that, if they're watching. Leave a comment down below. Now one of the things people will want to check on is what is the clock like,

**Dave Jones:** what's the PLL like, all that sort of stuff, because that determines your time-base accuracy and jitter and all that sort of jazz. You know, not that you should be that concerned about it in a low-end scope, but we've seen, hey, we've seen Rigol goof that before in their 2000 series, for example.

**Dave Jones:** Well, unfortunately, you won't find that on here. Here's the main oscillator. I might get the macro lens out and have a look at that. But there basically is no PLL inside this thing. You've got this puppy here, if you're wondering. That's a TPS 6150 or something.

**Dave Jones:** That's the LCD bias circuitry. So there is no PLL on here. It's basically built in to the MegaZoom 4 ASIC there. So all the magic is done inside there. So you won't find your traditional PLL on here to get your high clock rate.

**Dave Jones:** And we've got ourselves a 4 megabit flash memory there, so that must be for the Spartan FPGA, I'd be assuming. Speaking of which, it's the XC3S500E. FTG256DGQ169 for those playing along at home. And the processor is the same Spear 600 ARM processor we've seen in the previous versions.

**Dave Jones:** Of course, it would be. It's going to be running the same OS and software and everything else. Of course, they're going to leverage that. They're not going to re-spin that. They ain't stupid. And there, thank you very much for providing that key site,

**Dave Jones:** is the JTAG bus. So those of you who want to hack away, go for it. And there's the other JTAG as well. Thank you very much. And DB, that'd be debug. So that looks like it's tied into the MegaZoom 4 ASIC. So I'm not, you know, I'm not sure what's going on there.

**Dave Jones:** I think some people have reverse engineered it or have hacked around on the 2000 and 3000X series, but I haven't been following that thread. Sorry. Interestingly, there's temp and tempB here, so they'd be monitoring the die temperature, I would be presuming. So the scope should know if it's getting too hot under the collar

**Dave Jones:** and probably pop up with a warning, Will Robinson, shut down. There's nothing else exciting on the back. There's a TL074 up there. There's a massive bypass happening underneath the ADC, I believe, and I would be guessing that that one there is your ADC

**Dave Jones:** and that one's the MegaZoom 4 ASIC. I won't bother trying to heat these things up and get the heat sinks off. I mean, these are custom Keysight parts, so really, you know, it's not going to tell us anything, except that it's a MegaZoom 4 ASIC.

**Dave Jones:** It's exactly the same as what's in the 2000 and 3000X series from six years ago. The ADC could have changed. It could be a lower spec part or whatever, but yeah, we're not going to know the details. That's going to be a Keysight custom part.

**Dave Jones:** But the MegaZoom 4 ASIC, exactly the same. They're leveraging that because they spun that once, spent the millions of dollars developing that, and they're amortizing. They've been amortizing the cost for like six years now, so it's probably cheap as chips for them on some old silicon process.

**Dave Jones:** So yeah, it has the full capability in there. It's got the one million waveforms updates per second. It's got the four mega sample memory. They could easily enable this stuff. It's got the hardware decoding, the real 64K point FFT, all real-time in hardware,

**Dave Jones:** protocol decoded all in hardware, everything else. But they chose not to enable it because that'd eat into their 2000 and 3000, or at least 2000 series sales. And also you can tell that one's the ADC because when you're laying out a system like this,

**Dave Jones:** it's going to be the closest to the front end. So the signals are going to be coming out here. They're going to be differential pairs, of course, coming out. It's going to be a differential analog signal. It's going to go straight into this connector here,

**Dave Jones:** which pops up on the bottom there, and then it goes, I think there might even be some termination down there, goes straight into the ADC here. And of course your Megazoom 4 ASIC is going to be coupled into your processor over here. So you can almost bet your life that's the Megazoom 4

**Dave Jones:** and that's the ADC just by the system arrangement there. And for those wondering if they're going to release a mixed signal version, well, I haven't heard anything and I wouldn't expect them to. They've been working on this for years. If they had that option, you would have seen cutouts in the front

**Dave Jones:** or things spaced to put that in there, but we don't have any of that. I mean, they've deliberately spaced these things out. There's really, maybe tucked away in there, perhaps you could have like an 8-channel jobby or something, but then the probes wouldn't be compatible.

**Dave Jones:** And no, it's just, I don't think it's going to happen. Don't hold your breath. And it's not really worth spending much time on the signal, the R, SIGGEN, R stuff. These are just amps and things like that to do offset and output buffering and stuff like that,

**Dave Jones:** and the demo signal generator down here. Now, this is the BNC. Now, they sell this as a non-generator model. I don't actually have the non-G version. The base price unit does not have the signal generator, and I am led to believe that it physically does not have it populated.

**Dave Jones:** So I assume maybe it doesn't have the rest of the stuff populated either. I'm not entirely sure, but we'll have to wait until somebody does a teardown of a non-G version. But I can almost guarantee the non-G version will be the exact same layout.

**Dave Jones:** So in theory, these are all, I believe, these are all off-the-shelf parts, so you could potentially, if you are really, really keen, potentially get the non-G version without the parts fitted and fit them yourself and the BNC. I believe the front panel doesn't have the cutout for it, though,

**Dave Jones:** doesn't physically have the cutout, but the layout in the PCB would be there. That's what I believe anyway, but don't quote me on that. But yeah, no, if this thing is going to get hacked and people, you know, want to get a real feature-rich,

**Dave Jones:** the top-end model for the low-end price, they're going to be buying the function generator version with everything installed. Otherwise, it's just too much hassle, even if you could do it. Poor puppy's unpopulated. What's going on there? And there's all that LCD bias driver stuff I was telling you about.

**Dave Jones:** Power supply, nothing to write home about. These are wet electrolyte ones. You can tell because they've got the vents in the top. They're not the solid SMD caps, so, you know, but they're fine. Par for the course. You've got all our LDOs. This thing has no shortage of power rails.

**Dave Jones:** 1.8 volts, 3.3, 1.2, 1 volt, of course. They're all for the FPGA and other digital cores and things like that, and what else? I think we've got, like, 2 volts over here, I saw somewhere. I don't know, there's a whole bunch of stuff.

**Dave Jones:** And the trigger circuitry's like, meh. Always nice to see an NEC relay, though. I can list, there's three on here. There's one thing I don't see on here, and this is an LCD cable. This one over here, this tiny one, that's the keyboard cable.

**Dave Jones:** So it's going off to the front panel. So there must be a PCB mount, or the cable is on the bottom and it connects. Anyway, I'm going to whip this board off. I'll do the cans last, but let's get this off and see what's behind.

**Dave Jones:** There's a bunch of self-tappers in there, and bingo, we're out. And there's our LCD. We can see that that does actually connect down to the bottom of the board down there, so that's always a bit of a pain in the butt. I won't bother showing you the keyboard front panel.

**Dave Jones:** It's like, meh, whatever. And of course they're taking RFI seriously. We've got our metal fingers there and there, going down to the pads there and there. Nice. Low inductance for the win. Well they're pretty darn proud of their mate in China. Well now this is interesting.

**Dave Jones:** Look at this unused BNC cutout here. Were they thinking a 4-channel version maybe? And bingo, they've also got it up here in the chassis. So are they hedging their bets down the road, with the chassis at least, that they could do a 4-channel version?

**Dave Jones:** Because this is one of the key things that does not make it competitive with the Rigol 1000Z series and why it's so popular is because it's a 4-channel scope. But they've gone, they've done that for a reason. So, and of course you don't have the external trigger when you have the 4-channel.

**Dave Jones:** So, you know, there's no reason why they couldn't re-spin that board and have 4-channels in there with no external trigger. Hmm. Maybe, also, that's why they've done the processor board, so they can whack another ADC on there. Perhaps, or change that, or multiplex it, or do whatever they need to do to get 4-channels.

**Dave Jones:** But do not get excited and do not hold your breath and hold out for a 4-channel version of this scope. Because I don't think you'll see one anytime soon, if at all. They're just hedging their bets early on in the design process and probably just went, nah, we'll stick with 2-channels.

**Dave Jones:** Because that's all tech have got. And here's the LCD, which is manufactured by Oneunglo Anonymous. The interesting thing about this is, if you read the data sheet for this thing, it tells you that there's a little asterisk, and you read the fine print down below,

**Dave Jones:** it says that this display can have up to 5 dead or stuck pixels and not be deemed a failure. Are you kidding me? What is this? The bloody 1990s? Ridiculous. So they've obviously used some cheap-ass, you know, bottom-of-the-range, consumer-grade display in this, because they don't have, as far as I'm aware, don't have that same clause in the 2000 and 3000X series.

**Dave Jones:** No one would tolerate dead frickin' pixels, but apparently it is, so we'll just read the fine print. We're not going to give you your money back. One of the BNC front panel nuts had two washers. Someone was feeling extra generous that day on the production line.

**Dave Jones:** Good on ya. Well, that was a waste of effort. Oh, there's nothing on the bottom. Couple of crystals, 25 and 30 meg there, and why they couldn't put those on the top? Don't know. Anyway, yeah, a couple of 74HC, a couple of standard 78L05 regulators,

**Dave Jones:** and that's about all she wrote. A little bit more on the analog front end. On the bottom here, it looks like we've got, like, some sort of differential filtering thing or something like that. And the 125 megahertz crystal on the top side of the board, I can't find any info on that.

**Dave Jones:** So if anyone has any clue, let us know. Hey, 25 meg and 30 meg, that'd be for the processor and the FPGA, probably. And those parts on the bottom of the analog section there? No, I thought it was some sort of differential pair thing.

**Dave Jones:** It looks like it's just some sort of star ground with some, like, decoupling or something going back to it. Meh. And the analog front end shields just come off with a screw. Oh, beautiful, thank you very much. It's even labeled, not. Beautiful, they didn't solder them in.

**Dave Jones:** Thank you, thank you, thank you. Oh, it's just gotta be hacked now. First cab off the rank here, LMH6574, and this is actually a video multiplexer, so there you go. Couple of trannies down there, are they? An analog devices part, haven't got the number for that.

**Dave Jones:** Got ourselves a trimmer cap which has the hole, there's only one trimmer cap on this thing, which has a hole in the can to adjust. What else? Got a relay, that's our photomos relay down there, is it? Looks pretty standard for 100 megahertz.

**Dave Jones:** Front end, 74HCT595, the digital expanding choice of champions there. And I believe that is a Hittite HMC626 there. So it's a 1 gig bandwidth variable gain amp, exactly what you'd need here. Well, you don't need 1 gig, but you need a variable gain amp in there.

**Dave Jones:** So this one actually doesn't have like a bandwidth limiter in it, a software bandwidth limiter. So they must be limiting that somewhere else. Curiously, there's an unpopulated footprint there, so I'm not sure what's going on there. And they've got that jumper link, a 0 ohm jumper link, bypassing that.

**Dave Jones:** So that's interesting. Once again, I don't have the 50 megahertz educational model to compare it to, but I'd be surprised if they're not identical. So the output of the variable gain amp then goes up to here, and this is a LMC6552, I believe it is.

**Dave Jones:** Once again, this is a 1 gig bandwidth differential driver, which is of course exactly what you want. You can see sort of the differential type layout there. And then the differential pair buggering off. Even got a nice handy little test point there, so they can characterize that at the production stage.

**Dave Jones:** But once again, that does not have any attenuation built in. So like, you know, digital attenuation or anything like that. I pretty much know for a fact I think they are software limited in this, because you can actually buy a software upgrade option from 70 megahertz to 100 megahertz.

**Dave Jones:** So obviously, they've got to be able to at least switch those two in software. So yeah, they've got to be switching in something in there, whether or not it's a varicap or whether or not it's, you know, just some LCRC filter or something like that.

**Dave Jones:** Crude filter being switched in. Not entirely sure. I'd have to reverse engineer this to really see. So there you have it. That's inside the new Keysight 1000X series oscilloscope. And it's very well designed and manufactured, as you'd expect. A little bit of a letdown with the quality of the caps in the power supply,

**Dave Jones:** but meh, it's par for the course these days. The fan is a little bit loud, meh, don't like that. But apart from that, they've actually engineered the board really well. And having that processor board on there is a really interesting design decision. And as I said, they probably thought about, with the front panel holes and everything,

**Dave Jones:** probably thought about a four-channel version early on in the design process, and then maybe change their mind further down the track. That's one of the key limitations of this thing, is that it is only a two-channel model. They don't have a four-channel option, so I wouldn't...

**Dave Jones:** Don't hold your breath for a four-channel version, and don't hold your breath for a mixed signal logic analyzer add-on either. And I wouldn't expect it. It's designed... Oh, it clearly targeted this to compete directly against the TechTBS 1000 series in the educational market.

**Dave Jones:** It's not really designed for the hobbyists. If it was, I'll talk about pricing in the review and stuff like that, which I haven't shot yet. Sorry, I goofed up, I didn't realize it was 28 days in February. Oh! Anyway, this is released today,

**Dave Jones:** and it's $450 for the base model one, without the function generator, goes up to $700 or $800 or something. For the full bells and whistles 100 MHz version that we've... 100 MHz with function gen that we've got here. But hey, as you'd expect, it's a very nicely designed amplitude scope,

**Dave Jones:** and it does work exactly like the 2000 and 3000x scopes, as you'll no doubt see in the review. So it is really quite, you know, a high-quality scope at a low-end price, pretty much exactly as they advertise. So I'm reasonably impressed with this.

**Dave Jones:** I'll have to do a reverse engineering of the analog front end, of course, and as always with these teardowns, I'll take some high-res photos, I'll put them over on EEVblog.com, so for those who want to do some reverse engineering or hacking on this thing,

**Dave Jones:** then go for your life. Anyway, the ultimate test of whether or not this is going to be successful in the market is whether or not it can be hacked, I think. Like in the market that, you know, like the hacker-hobbyist-maker kind of market

**Dave Jones:** to compete against the 1054Z, which is hackable, and other scopes which are hackable, this one has to be hackable. And if you can get the function gen version for that, then it's going to be an absolute bargain. It could be a killer scope, and of course, as time goes on,

**Dave Jones:** they can release extra functionality in this, because it's got the MegaZoom 4 ASIC in there, they can increase the sample rate to up to 4 gig if they wanted to, they can increase the sample memory up to 4 meg if they wanted to,

**Dave Jones:** they could implement the million waveforms per second if they wanted to, all that functionality is already built into this scope. And of course, the serial decoding is an optional extra, they can include that for free. So they have a lot of scope to move on the pricing,

**Dave Jones:** but clearly at this stage, they're targeting the tech TBS1000 series. So I hope you found that teardown interesting, and if you did, please give it a big thumbs up. And as always, EEVblog Forum is the place to discuss hacks and all sorts of test equipment reviews and teardowns and stuff like that.

**Dave Jones:** Always linked in down below. Catch you next time. Transcribed by https://otter.ai
