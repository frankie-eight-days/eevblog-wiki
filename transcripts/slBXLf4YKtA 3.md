---
video_id: slBXLf4YKtA
title: EEVblog #985 - Siglent SDS1202X-E Oscilloscope Teardown
url: https://www.youtube.com/watch?v=slBXLf4YKtA
source: youtube-asr
timestamps: {"0": 1, "1": 27, "2": 36, "3": 60, "4": 72, "5": 86, "6": 96, "7": 111, "8": 126, "9": 144, "10": 164, "11": 184, "12": 197, "13": 206, "14": 220, "15": 238, "16": 249, "17": 260, "18": 269, "19": 282, "20": 295, "21": 304, "22": 314, "23": 326, "24": 333, "25": 346, "26": 356, "27": 372, "28": 391, "29": 400, "30": 413, "31": 426, "32": 439, "33": 459, "34": 474, "35": 485, "36": 496, "37": 510, "38": 523, "39": 540, "40": 561, "41": 574, "42": 583, "43": 593, "44": 605, "45": 614, "46": 635, "47": 646, "48": 662, "49": 676, "50": 688, "51": 701, "52": 714, "53": 728, "54": 739, "55": 753, "56": 769, "57": 788, "58": 802, "59": 811, "60": 829, "61": 852, "62": 860, "63": 877, "64": 891, "65": 909, "66": 927, "67": 943, "68": 953, "69": 975, "70": 991, "71": 1004, "72": 1014, "73": 1028, "74": 1037, "75": 1051, "76": 1071, "77": 1084, "78": 1101, "79": 1129, "80": 1152, "81": 1169, "82": 1179, "83": 1191, "84": 1201, "85": 1212, "86": 1230, "87": 1243, "88": 1254, "89": 1270, "90": 1284, "91": 1296, "92": 1317, "93": 1329, "94": 1341, "95": 1362, "96": 1380, "97": 1394, "98": 1406, "99": 1419, "100": 1433}
---

**Dave Jones:** Hi, just a little preamble to this video. I actually shot this video a couple of weeks back and I was just about to release it as a world exclusive when Siglent said, "Hey, well, put it stop, please, cuz we're going to change the marketing on this scope." Now, you'll hear me mention during this video that it's a 100 MHz model scope and that it is $359.

**Dave Jones:** It's actually going to be $379 and it's going to be 200 MHz only. So, I I am getting a new version of the scope, but this is the original one they sent me.

**Dave Jones:** I don't believe there's any difference at all between the 100 MHz one I'm tearing down here and the 200 MHz one that they're sending me. I believe this still has a 200 MHz front end and it was just being software limited as these companies do for marketing reasons, but Siglent have decided to go against that and this is going to be an then an entry-level 200 MHz scope for $379

**Dave Jones:** with the free serial decoding and the one meg points FFT and everything we'll see inside this video. So, I just wanted to clarify if you see that further on or hear that further on in the video, it's changed.

**Dave Jones:** Anyway, on with the show. Hi, another world exclusive here. We've got the new Siglent ultra-low entry-level scope. It's the SDS1000X series and you may have said, "Dave, I've seen that before.

**Dave Jones:** You've had that on the blog a couple of years back." Yeah, I have, but this is the new {dash} E model, not to be confused with the other {dash} models they've got available.

**Dave Jones:** This one is not actually released yet. It's being released in Aprilish sometime and the thing about this is that it's 359 US dollars supposedly is going to be the retail price on this puppy.

**Dave Jones:** Now, it the way it differs from the existing 1000X series, which they're still going to have is that the 1000 X series has options for a wave gen and a logic analyzer as well mixed signal scope.

**Dave Jones:** This is not that. There's no option for a wave gen, there's no option for mixed signal scope. Don't even think about it. This is just your bare bones entry level two channel 100 megahertz bandwidth scope for 359 bucks 1 gig sample per second.

**Dave Jones:** But this is actually a completely different design to the existing 1000 X series inside which we'll take a look at. It's super fast, super responsive 1 meg points FFT and one of the big selling features of this and a lot of people have complained about this over the years is that why companies charge for serial decoding.

**Dave Jones:** Well, this one has it built in for free. Beauty. As you can see the front panel layout is practically identical to the existing 1000 X series except it has an an extra button here for the wave gen which this one doesn't have but it's got the nice auto roll mode with the roll button in that.

**Dave Jones:** I've been using this in a debugging repair video I'm using at the moment and I actually quite like that feature. It's working quite well and it's got you know the USB to save your waveforms everything else.

**Dave Jones:** Everything you typically expect in a bare bones two channel scope. And the inputs are a standard 1 meg 8 in puff 400 volts peak so reasonably high voltage inputs.

**Dave Jones:** On the back yes LAN is standard for the 359 dollar scope and we've got pass fail and trigger out and USB devices well. Your basic functionality very nice for the price.

**Dave Jones:** Anyway, you know what we say here on the EVBlog don't turn it on, take it apart. Interestingly this one says nominal power 25 watts max. Most scopes of this sort of you know, little four uh small two four channel uh scopes are normally, you know, like say normally 50 watts.

**Dave Jones:** So, that's going to be interesting because there's some new circuitry inside here that's different to the original series. Can't remember what the original series was, but uh yeah, this one could be lower power.

**Dave Jones:** Now, I've done a video on how to remove these uh calibration seals without uh damaging them. So, clip up click up here somewhere if you want to see that, but uh screw that for today.

**Dave Jones:** Yippee! As usual, we've got the two screws in the feet there, but uh curiously, we've got the screws vertically on the top this time and not in through the like that.

**Dave Jones:** And by the way, if you want to see the previous uh teardown of the original 1000X series, click up here somewhere. This stupid new YouTube card thing cuz they turned off annotations.

**Dave Jones:** YouTube have like you can't They've just completely abandoned annotations now, so I can't like annotate videos and uh don't get me started. They reckon cards replace it. [ __ ] they do.

**Dave Jones:** Unbelie- I can't leave a regular text comment in a card, but I can link to videos. So, teardown for this up there somewhere. Hmm. Anyway, let's open it up.

**Dave Jones:** Whoa. Here we go. Let's see what our built down to price scope is like. I can't I still can't remember. I should go watch my video for the uh other one, but that's uh interesting.

**Dave Jones:** Usually, uh we have a two uh you know, the power supply separate then comes off. This one, um it looks like the top it's just slightly different to how they normally are.

**Dave Jones:** Anyway, let's crack it open. Lift this up. There was only two screws on here. All Phillips, by the way. Different to the regular torques you find. And bingo, we're in like Flynn.

**Dave Jones:** Uh no separate shielding on the uh power supply. They've completely separated that. Single board construction down the bottom. We'll have a look at that, but uh that's, you know, interesting.

**Dave Jones:** This is supposed to have a 500 uh microvolt front end, uh but of course it's all shielded, so, you know, no worries. They're probably uh you know, not hugely concerned.

**Dave Jones:** There's nothing inherently wrong with that. It looks like quite neat and tidy, actually. I do like the look of the uh power supply. They've uh put a little cable tie on there with the earth uh strap and the um main ribbon power supply uh ribbon cable here, so that's interesting.

**Dave Jones:** I'll have to cut that to move it out of the way to get the uh photos. And look, they've put Loctite on the connector. Nice touch. They've done that over here with the fan, and they've route gone to the effort to route the wire under there, under the uh main uh screw there, so it's not flapping around in the breeze.

**Dave Jones:** Nice attention to detail. I like it. And in terms of uh airflow here, we've got the air blowing out uh this side here, and it's sucking the air from over this side.

**Dave Jones:** There are vents here, but they aren't in the uh top or bottom. So, that's blowing over the power supply and over the uh heatsink fins as well. They're even correctly oriented like that to get the maximum airflow over them.

**Dave Jones:** Nice. Power supply is certainly neat and tidy. It's got all the business. Nice uh fully encased uh fuse there. We've got uh isolation slots absolutely everywhere. Look at the primary and secondary here with the optocouplers.

**Dave Jones:** Very nice. There's our main switching uh transformer. We've got uh requisite MOV protection and uh common mode uh choke on the input. The earth lead is your standard uh standard fare.

**Dave Jones:** That seems uh tight enough. So, that's a neat-looking power supply. They've celastico'd the caps down. Uh Lelon caps. Yeah. Yeah, not exactly Panasonics. And you might not be able to see it, but they have gone for uh Lelons pretty much everywhere else as well.

**Dave Jones:** They look like the uh gold series ones. They're probably uh low ESR Uh uh jobs. So, yeah, at least they stuck with the one manufacturer, but you know, this is a bottom of the range scraping the barrel $350 retail uh scope.

**Dave Jones:** So, that's a pass. At least it's neat and tidy. Yeah, unfortunately, to get the main board out, it looks like I've got to do well, four self-tapping screws uh into the top metalwork here.

**Dave Jones:** So, this top metalwork lifts off because there's no nuts on the front, of course, for the BNC. They're on the middle on the uh inside. But to get to the last nut, I got to take the power supply off.

**Dave Jones:** Er. And I think they got a bit of uh elephant hide on the bottom there. Elephant hide elephant hide um on the bottom. Um they're just insulating that backside of the board for those playing along at home.

**Dave Jones:** Look at that. Nice touch. Uh high-voltage isolation slots between each pin of the bridge rectifier. Neat. Okay, so all this is supposed to Uh pop out. No, no, got to undo the ribbon cables first.

**Dave Jones:** Oh, that sells a nice big juicy ferrite right across the uh main LCD ribbon cable there. Could that be a last-minute uh you know, EMI oopsie perhaps? Tell you what, I really like the fact that you can just uh swing out the power supply like this and get in there for the board.

**Dave Jones:** Of course, no uh touchy. Don't accidentally scrape the uh bottom of the board down here. But yeah, nice access for hacking. Speaking of which, check this out. Look, easy access right on the edge of the board and labeled the uh not only the JTAG interface, but for all the world like a UART.

**Dave Jones:** Look at that. Just like beautifully laid out. And there's even an extra pin header over there. I don't know what that is, but yeah, like purpose-designed, readily accessible for hacking.

**Dave Jones:** Go for your life. And I forgot to mention, there's no sign of any of the trademark Siglent rust on the on the chassis, on the edges of the chassis.

**Dave Jones:** So, yeah, they've upped their game. And here we go. Let's have a squeeze inside. Got this under the Teledyne microscope. It's all on one board, as you can see.

**Dave Jones:** Now, this is very interesting because the heart of this is the Xilinx Zynq processor. They've completely changed architecture on this thing. That's what's under the heat sink. Sorry, that's uh glued down.

**Dave Jones:** I won't be taking this off. Um it's the only one in the country, so I don't want to ruin it. So, I don't know exactly which Xilinx Zynq model it actually is.

**Dave Jones:** Anyway, it's the Zynq processor. That's all you need to know. Which we've seen before in the GW Instek 1000B series. And that's what gave it its incredible bang for buck performance in terms of FFT processing, the 1 meg point FFT, which is what this Siglent one has as well.

**Dave Jones:** And of course, the thing about the Zynq processor is that it contains not only a Xilinx FPGA in there, a reasonably capable one, but also a an I think it's a dual core processor in there.

**Dave Jones:** So, you know, tightly knit coupling between the FPGA and the internal arm processor and hooked up to a DDR3 memory, I believe it uses. I haven't actually looked up those numbers, but you can if you're playing along at home.

**Dave Jones:** They should be DDR3. You can see all the length matching there, all the classic length matching stuff. They got the little wiggle wiggle wiggle wiggle, yeah, to make them all identical length cuz you got to length match those puppies.

**Dave Jones:** Otherwise, you get timing problems at such speed like this. Now, the previous 1000X series from Siglent, we've seen the teardown. I'll link it in down below. It's actually got a it ran on the Blackfin DSP platform.

**Dave Jones:** So, they've completely changed the platform that this thing runs from. Although, I'm sure, you know, a lot of the code is compatible and everything else. They probably uh or it was able to port that over uh relatively um easily.

**Dave Jones:** But, uh yeah, it's they've got it all on one board. And the interesting thing is is that it is on the main board. Whereas, we saw it on a daughter board, just the processor part, on a daughter board inside the GW Instek.

**Dave Jones:** And that was to uh lower the cost because you need to fan out this BGA. You need a big multi-pin um a multi-layer board, you know? There's all the bypass caps and everything else.

**Dave Jones:** They've um fanned out almost every via on the thing by the looks of it. And to get that out, you need like an eight-layer board or something uh like minimum to get that out.

**Dave Jones:** And we've also seen that uh motherboard approach in the or the daughter board approach in the uh new K- Keysight 1000 X-Series as well. Once again, to get the cost down, keep all that multi-layer complexity on a smaller board.

**Dave Jones:** But, hey, for this ultra-low end one, it's different. So, I'm very surprised to see it integrated into the main PCB. But, the PCB itself is relatively small. So, maybe that's why they can get away with it and they can fit multiple ones in the one uh panel, of course.

**Dave Jones:** Um yep, you can see the mouse bites. There you go. You can see the uh mouse bites there and there on the board, which shows it's all panelized. So, you can probably fit uh you know, they've size optimized this probably to fit four of these like on one uh PCB panel or something like that.

**Dave Jones:** So, that's how they can get the uh cost down. Otherwise, the bare board alone, if it's eight or 10 layers, just because you need this part to be uh high-density uh cuz most of the you know, the rest of it can be four layers, no problems whatsoever.

**Dave Jones:** And you'll get away with that uh fine and dandy. But, all this stuff is, you know, probably eight layer just to fan out the pain in the butt BGA package zinc processor.

**Dave Jones:** But, that's the price you pay, but it's interesting that they haven't gone for the daughter board approach. So, I'd say because this board is pretty darn small in the scheme of, you know, complete motherboard complete oscilloscope motherboard type boards, you know, they've done well.

**Dave Jones:** So, they you know, that would have been a real cost optimization exercise anyway. That looks like a LED, is it? What? HL? HL? I don't think I've ever seen a HL designator before, but that looks like I mean it's got a it's got a series resistor in there, so uh Okay, or is it some sort of ambient light sensor?

**Dave Jones:** I don't think so. It's probably just a LED like a heartbeat LED or something like that. Anyway, what is all this array of big array of transistors around here for?

**Dave Jones:** What? It's got two test points associated with it. Seems to be hooked into the zinc processor up there, but what like why? Um what are they doing? I I don't know.

**Dave Jones:** That is very curious. Um Anyway, JTAG interface, no worries. Whack our point one inch header on there. So, what have we got there? Just a 7404. Got ourselves a crystal there.

**Dave Jones:** BOCPC. Thanks for telling us all the information on that one. Not. Um it's just a 244. Some jelly bean logic. And the ADF 4360. If we go on over the data sheet, that's our PLL, basically our VCO.

**Dave Jones:** Our voltage controlled oscillator, that's what generates the main clock there. So, yeah, it's the jelly bean one. I think we've seen that before. And but it's all about of course the uh loop components that you actually put inside this thing.

**Dave Jones:** And I'm sure if you scroll down far enough you'd find examples of various loop components which some companies shall remain nameless Rigol have screwed up the the loop on the with all the building registers and everything else.

**Dave Jones:** Anyway, there's the loop filters for those who want to analyze that to see if they goofed up. Go for it. And moving on from that, what do we got here?

**Dave Jones:** We're entering our trigger section of the board. ADCMP I think that's just a a comparator and 74HC4053 got to have some 4000 series CMOS in there. No wackers. Cells the classic 595 again 74HC4051.

**Dave Jones:** It's all happening all jelly bean stuff. Anyway, this is the trigger section. Some local regulation across there. Analog VCC has got its own separate 5 volts and nice little test points all labeled and that's the interface.

**Dave Jones:** But people want to see the ADC. We almost missed it. There it is. It's a had 1511. Let's check it out. And here it is. It's a 1 gig sample AD converter.

**Dave Jones:** So no, we're not going to be able to overclock this thing anytime soon. And we've probably seen this in other parts as well. Typical applications digital oscilloscopes. Thank you very much.

**Dave Jones:** So yeah, it's purpose designed for this sort of thing. And of course it's got the four channel interface in there. And of course the 1 gig samples per second will have of course cuz it's not 1 gig sample per second per ADC.

**Dave Jones:** It's 1 gig sample per second total. So when you turn on that second one it's just going to have and well, I'll link it in down below for those who want to check it out.

**Dave Jones:** Oh, all right, calm down. I know you want to see the analog front end. Well, here it is, two identical analog front ends. I'm sure they are. I'm not going to look, but yeah, pretty sure they're absolutely identical here.

**Dave Jones:** Now, this actually differs from the analog section used. In fact, I'll try and put them possibly side by side here in the shot. Different to the one used inside the other 1000X series.

**Dave Jones:** So, this is the 1000XE series. And looks like they've got a slightly different front end. There's two relays in this one. There was three in the I'm going to call it the older one cuz this one is brand spanking new.

**Dave Jones:** And we've got some trimmers there, which I don't believe that we had. Two trimmer caps up there that we didn't have on the other one. So, yeah, two relays, but apart from that, the top section actually all this section in here looks pretty close to identical.

**Dave Jones:** So, the previous one had a 200 MHz bandwidth. This one is available in a 200 MHz model. So, I'm sure absolutely sure that the base model unit um if you bought the 100 MHz version, it's going to have the 100 the 200 MHz analog front end and they just software limited But, if we have a close look at that identical section that we had before, we've got

**Dave Jones:** our cosmo relay there, a 595 port and digital port expander, of course, and an 8370. Let's check that one out. So, to be verified later, but I'm pretty darn sure that everything is identical including the differential uh gain um amp and the uh variable gain amplifier in there.

**Dave Jones:** I'm pretty sure that they're all the same that we had in the previous model. So, I won't go through details. There's the top half for those of you who love to take screen captures, but I've got high-res head-on photos down below, but I don't know.

**Dave Jones:** I didn't get them under the Tagarno microscope, so there you go. Beautiful. Oh, look at that. Ah, it's better than a macro photo. It really is. But, it's limited to 1920 by 1280.

**Dave Jones:** Gosh darn it. And if you want to see the bottom of that, and of course you do. Of course you do. Um there is the bottom. For those playing along at home.

**Dave Jones:** And there's not much else. Got a nice big cutout in the ground plane there cuz they didn't want to uh up- upset the apple cart, but uh that looks all neat and tidy.

**Dave Jones:** That's a 200 meg front end. I'm not sure what else I can uh show you there. That's about all she wrote on the new Siglent 1000 XE main motherboard.

**Dave Jones:** They've really uh you know, they've It's not much in your modern uh scopes. Then again, if you look at an old to someone will say it, I'm sure. Look at the old uh Tektronix TDS 210, for example, which is like 25 years old now or something, and that had bugger all in it, but it also had bugger all uh performance as well.

**Dave Jones:** But, this thing is uh very remarkable, and it's all thanks to the uh Xilinx Zynq processor down in there, and nothing else. It just That's what handles all the grunt in this thing.

**Dave Jones:** 1 meg point FFT. I believe it's got hardware serial decoding. It's got a complete digital trigger system, uh which is effectively zero jitter, they call it, uh cuz it's digital, and you get just one Yeah.

**Dave Jones:** Anyway, um because you can extract it out instead of doing the triggering in analog. Anyway, uh probably pros and cons both ways there. And um it's all integrated inside the zinc um the FPGA part of the zinc in there.

**Dave Jones:** Whereas the core of course would be running all the the OS and the display and everything else. So yeah, oh we've got another HL there. There you go HL1 HL2 they've got to be LEDs.

**Dave Jones:** I don't know. I haven't powered this thing up with the uh uh back off it yet. It works flashy flashy. And you betcha that TX RX is a UART.

**Dave Jones:** Ta-da! I'll dump this on the EV blog forum for those playing along at home who want to check out this but once again it uses that U-Boot just like the 1000 X series that we're playing around with last week and uh ECC is disabled and then 256 megabits.

**Dave Jones:** Let's I don't know. Anyway, you can go in here. Let's see if there's anything interesting. Is there Linux? Currently this is not going to be a hacking video by any stretch.

**Dave Jones:** I we just want to have a quick booting kernel booting Linux on physical CPU Linux version 3.9.8.0 for those playing along at home GCC version there you go. Ah, it's all happening.

**Dave Jones:** It's all happening. So is there anything interesting? So that's all the Linux boot stuff USB blah blah blah blah blah Xilinx data Xilinx AXI DMA engine successful. That'll be for dumping all the high speed oh open SPI dev HC595 failed.

**Dave Jones:** What? What? That's to speak to a 595. Um but it got this one here did it? Hmm anyway that's the port expander I would be guessing for the that they use on the front ends but they they might not might have No we didn't see a 595 anywhere else on the uh thing did we?

**Dave Jones:** So I think we're going to assume that that's the that's the front end. But hmm, there doesn't seem to be anything hugely interesting. I don't know. I'm not going to look into this in detail.

**Dave Jones:** The dumps down below for those who want to check it out. Oh, no, more stuff down here. Uh Skippy. Um what else have we got? Driver manager, blah blah blah blah blah.

**Dave Jones:** Error module. Doesn't sound that great. Anyway, but this may not be a release version. So, yeah, don't take this as uh gospel. And bingo, we can actually talk to this.

**Dave Jones:** I tried help and uh help not found. Been asked whatever that is. I don't know. All the Linux people are probably screaming at me. Um and so I tried help games, of course, because the more complicated these things are, the more they have to help you out, apparently.

**Dave Jones:** So, uh help not found. Uh hang on, I know what to do. Damn it, they've taken out the password.
