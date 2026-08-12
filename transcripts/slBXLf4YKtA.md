---
video_id: slBXLf4YKtA
title: EEVblog #985 - Siglent SDS1202X-E Oscilloscope Teardown
url: https://www.youtube.com/watch?v=slBXLf4YKtA
source: youtube-asr
timestamps: {"0": 1, "1": 14, "2": 33, "3": 44, "4": 56, "5": 72, "6": 90, "7": 103, "8": 120, "9": 135, "10": 152, "11": 170, "12": 184, "13": 198, "14": 216, "15": 231, "16": 245, "17": 258, "18": 272, "19": 287, "20": 302, "21": 316, "22": 330, "23": 346, "24": 359, "25": 374, "26": 386, "27": 400, "28": 413, "29": 428, "30": 447, "31": 465, "32": 480, "33": 494, "34": 509, "35": 523, "36": 538, "37": 553, "38": 568, "39": 583, "40": 598, "41": 611, "42": 627, "43": 641, "44": 660, "45": 670, "46": 686, "47": 699, "48": 712, "49": 728, "50": 740, "51": 755, "52": 769, "53": 784, "54": 798, "55": 811, "56": 826, "57": 843, "58": 856, "59": 874, "60": 895, "61": 913, "62": 928, "63": 947, "64": 965, "65": 989, "66": 1004, "67": 1019, "68": 1033, "69": 1044, "70": 1066, "71": 1082, "72": 1094, "73": 1113, "74": 1129, "75": 1152, "76": 1166, "77": 1182, "78": 1194, "79": 1207, "80": 1223, "81": 1238, "82": 1252, "83": 1267, "84": 1284, "85": 1300, "86": 1314, "87": 1330, "88": 1349, "89": 1369, "90": 1383, "91": 1398, "92": 1417, "93": 1430, "94": 1442}
---

**Dave Jones:** Hi, just a little preamble to this video. I actually shot this video a couple of weeks back and I was just about to release it as a world exclusive when Siglent said, "Hey, well, put it stop, please, cuz we're going to change

**Dave Jones:** the marketing on this scope." Now, you'll hear me mention during this video that it's a 100 MHz model scope and that it is $359. It's actually going to be $379 and it's going to be 200 MHz only. So, I

**Dave Jones:** I am getting a new version of the scope, but this is the original one they sent me. I don't believe there's any difference at all between the 100 MHz one I'm tearing down here and the 200 MHz one that they're sending me. I

**Dave Jones:** believe this still has a 200 MHz front end and it was just being software limited as these companies do for marketing reasons, but Siglent have decided to go against that and this is going to be an then an entry-level 200

**Dave Jones:** MHz scope for $379 with the free serial decoding and the one meg points FFT and everything we'll see inside this video. So, I just wanted to clarify if you see that further on or hear that further on in the video, it's

**Dave Jones:** changed. Anyway, on with the show. Hi, another world exclusive here. We've got the new Siglent ultra-low entry-level scope. It's the SDS1000X series and you may have said, "Dave, I've seen that before. You've had that on the blog a couple of years back."

**Dave Jones:** Yeah, I have, but this is the new {dash} E model, not to be confused with the other {dash} models they've got available. This one is not actually released yet. It's being released in Aprilish sometime and the thing about

**Dave Jones:** this is that it's 359 US dollars supposedly is going to be the retail price on this puppy. Now, it the way it differs from the existing 1000X series, which they're still going to have is that the 1000 X

**Dave Jones:** series has options for a wave gen and a logic analyzer as well mixed signal scope. This is not that. There's no option for a wave gen, there's no option for mixed signal scope. Don't even think about it. This is just your bare bones

**Dave Jones:** entry level two channel 100 megahertz bandwidth scope for 359 bucks 1 gig sample per second. But this is actually a completely different design to the existing 1000 X series inside which we'll take a look at. It's super fast,

**Dave Jones:** super responsive 1 meg points FFT and one of the big selling features of this and a lot of people have complained about this over the years is that why companies charge for serial decoding. Well, this one has it built in for free. Beauty.

**Dave Jones:** As you can see the front panel layout is practically identical to the existing 1000 X series except it has an an extra button here for the wave gen which this one doesn't have but it's got the nice auto roll mode with the roll

**Dave Jones:** button in that. I've been using this in a debugging repair video I'm using at the moment and I actually quite like that feature. It's working quite well and it's got you know the USB to save your waveforms everything else. Everything you

**Dave Jones:** typically expect in a bare bones two channel scope. And the inputs are a standard 1 meg 8 in puff 400 volts peak so reasonably high voltage inputs. On the back yes LAN is standard for the 359 dollar scope and we've got pass fail and

**Dave Jones:** trigger out and USB devices well. Your basic functionality very nice for the price. Anyway, you know what we say here on the EVBlog don't turn it on, take it apart. Interestingly this one says nominal power 25 watts max. Most scopes

**Dave Jones:** of this sort of you know, little four uh small two four channel uh scopes are normally, you know, like say normally 50 watts. So, that's going to be interesting because there's some new circuitry inside here that's different to the original series. Can't remember

**Dave Jones:** what the original series was, but uh yeah, this one could be lower power. Now, I've done a video on how to remove these uh calibration seals without uh damaging them. So, clip up click up here somewhere if you want to see that, but

**Dave Jones:** uh screw that for today. Yippee! As usual, we've got the two screws in the feet there, but uh curiously, we've got the screws vertically on the top this time and not in through the like that. And by the

**Dave Jones:** way, if you want to see the previous uh teardown of the original 1000X series, click up here somewhere. This stupid new YouTube card thing cuz they turned off annotations. YouTube have like you can't They've just completely abandoned annotations now, so

**Dave Jones:** I can't like annotate videos and uh don't get me started. They reckon cards replace it. [ __ ] they do. Unbelie- I can't leave a regular text comment in a card, but I can link to videos. So, teardown for this up there

**Dave Jones:** somewhere. Hmm. Anyway, let's open it up. Whoa. Here we go. Let's see what our built down to price scope is like. I can't I still can't remember. I should go watch my video for the uh other one, but that's uh interesting. Usually, uh

**Dave Jones:** we have a two uh you know, the power supply separate then comes off. This one, um it looks like the top it's just slightly different to how they normally are. Anyway, let's crack it open. Lift this up. There was only two screws on

**Dave Jones:** here. All Phillips, by the way. Different to the regular torques you find. And bingo, we're in like Flynn. Uh no separate shielding on the uh power supply. They've completely separated that. Single board construction down the bottom. We'll have a look at that, but

**Dave Jones:** uh that's, you know, interesting. This is supposed to have a 500 uh microvolt front end, uh but of course it's all shielded, so, you know, no worries. They're probably uh you know, not hugely concerned. There's nothing inherently wrong with that. It looks like quite

**Dave Jones:** neat and tidy, actually. I do like the look of the uh power supply. They've uh put a little cable tie on there with the earth uh strap and the um main ribbon power supply uh ribbon cable here, so that's interesting. I'll have

**Dave Jones:** to cut that to move it out of the way to get the uh photos. And look, they've put Loctite on the connector. Nice touch. They've done that over here with the fan, and they've route gone to the effort to route the wire under there,

**Dave Jones:** under the uh main uh screw there, so it's not flapping around in the breeze. Nice attention to detail. I like it. And in terms of uh airflow here, we've got the air blowing out uh this side here, and it's sucking the air from over this

**Dave Jones:** side. There are vents here, but they aren't in the uh top or bottom. So, that's blowing over the power supply and over the uh heatsink fins as well. They're even correctly oriented like that to get the maximum airflow over

**Dave Jones:** them. Nice. Power supply is certainly neat and tidy. It's got all the business. Nice uh fully encased uh fuse there. We've got uh isolation slots absolutely everywhere. Look at the primary and secondary here with the optocouplers. Very nice. There's our

**Dave Jones:** main switching uh transformer. We've got uh requisite MOV protection and uh common mode uh choke on the input. The earth lead is your standard uh standard fare. That seems uh tight enough. So, that's a neat-looking power supply. They've celastico'd the caps down. Uh

**Dave Jones:** Lelon caps. Yeah. Yeah, not exactly Panasonics. And you might not be able to see it, but they have gone for uh Lelons pretty much everywhere else as well. They look like the uh gold series ones. They're probably uh low ESR Uh uh jobs.

**Dave Jones:** So, yeah, at least they stuck with the one manufacturer, but you know, this is a bottom of the range scraping the barrel $350 retail uh scope. So, that's a pass. At least it's neat and tidy. Yeah, unfortunately, to get the main board

**Dave Jones:** out, it looks like I've got to do well, four self-tapping screws uh into the top metalwork here. So, this top metalwork lifts off because there's no nuts on the front, of course, for the BNC. They're on the middle on the uh inside. But to

**Dave Jones:** get to the last nut, I got to take the power supply off. Er. And I think they got a bit of uh elephant hide on the bottom there. Elephant hide elephant hide um on the bottom. Um they're just insulating that

**Dave Jones:** backside of the board for those playing along at home. Look at that. Nice touch. Uh high-voltage isolation slots between each pin of the bridge rectifier. Neat. Okay, so all this is supposed to Uh pop out. No, no, got to undo the

**Dave Jones:** ribbon cables first. Oh, that sells a nice big juicy ferrite right across the uh main LCD ribbon cable there. Could that be a last-minute uh you know, EMI oopsie perhaps? Tell you what, I really like the fact that you can just uh swing

**Dave Jones:** out the power supply like this and get in there for the board. Of course, no uh touchy. Don't accidentally scrape the uh bottom of the board down here. But yeah, nice access for hacking. Speaking of which, check this out. Look, easy access

**Dave Jones:** right on the edge of the board and labeled the uh not only the JTAG interface, but for all the world like a UART. Look at that. Just like beautifully laid out. And there's even an extra pin header over there. I don't

**Dave Jones:** know what that is, but yeah, like purpose-designed, readily accessible for hacking. Go for your life. And I forgot to mention, there's no sign of any of the trademark Siglent rust on the on the chassis, on the edges of the

**Dave Jones:** chassis. So, yeah, they've upped their game. And here we go. Let's have a squeeze inside. Got this under the Teledyne microscope. It's all on one board, as you can see. Now, this is very interesting because the heart of this is

**Dave Jones:** the Xilinx Zynq processor. They've completely changed architecture on this thing. That's what's under the heat sink. Sorry, that's uh glued down. I won't be taking this off. Um it's the only one in the country, so I don't want to ruin it. So,

**Dave Jones:** I don't know exactly which Xilinx Zynq model it actually is. Anyway, it's the Zynq processor. That's all you need to know. Which we've seen before in the GW Instek 1000B series. And that's what gave it its incredible bang for buck

**Dave Jones:** performance in terms of FFT processing, the 1 meg point FFT, which is what this Siglent one has as well. And of course, the thing about the Zynq processor is that it contains not only a Xilinx FPGA in there, a reasonably

**Dave Jones:** capable one, but also a an I think it's a dual core processor in there. So, you know, tightly knit coupling between the FPGA and the internal arm processor and hooked up to a DDR3 memory, I believe it uses. I

**Dave Jones:** haven't actually looked up those numbers, but you can if you're playing along at home. They should be DDR3. You can see all the length matching there, all the classic length matching stuff. They got the little wiggle wiggle wiggle

**Dave Jones:** wiggle, yeah, to make them all identical length cuz you got to length match those puppies. Otherwise, you get timing problems at such speed like this. Now, the previous 1000X series from Siglent, we've seen the teardown. I'll link it in

**Dave Jones:** down below. It's actually got a it ran on the Blackfin DSP platform. So, they've completely changed the platform that this thing runs from. Although, I'm sure, you know, a lot of the code is compatible and everything else. They

**Dave Jones:** probably uh or it was able to port that over uh relatively um easily. But, uh yeah, it's they've got it all on one board. And the interesting thing is is that it is on the main board. Whereas, we saw it on a daughter board, just the

**Dave Jones:** processor part, on a daughter board inside the GW Instek. And that was to uh lower the cost because you need to fan out this BGA. You need a big multi-pin um a multi-layer board, you know? There's all the bypass

**Dave Jones:** caps and everything else. They've um fanned out almost every via on the thing by the looks of it. And to get that out, you need like an eight-layer board or something uh like minimum to get that out. And we've also seen that uh

**Dave Jones:** motherboard approach in the or the daughter board approach in the uh new K- Keysight 1000 X-Series as well. Once again, to get the cost down, keep all that multi-layer complexity on a smaller board. But, hey, for this ultra-low end

**Dave Jones:** one, it's different. So, I'm very surprised to see it integrated into the main PCB. But, the PCB itself is relatively small. So, maybe that's why they can get away with it and they can fit multiple ones in the one

**Dave Jones:** uh panel, of course. Um yep, you can see the mouse bites. There you go. You can see the uh mouse bites there and there on the board, which shows it's all panelized. So, you can probably fit uh you know, they've size optimized this

**Dave Jones:** probably to fit four of these like on one uh PCB panel or something like that. So, that's how they can get the uh cost down. Otherwise, the bare board alone, if it's eight or 10 layers, just because you need this part to be uh high-density

**Dave Jones:** uh cuz most of the you know, the rest of it can be four layers, no problems whatsoever. And you'll get away with that uh fine and dandy. But, all this stuff is, you know, probably eight layer just to fan out the pain in the butt

**Dave Jones:** BGA package zinc processor. But, that's the price you pay, but it's interesting that they haven't gone for the daughter board approach. So, I'd say because this board is pretty darn small in the scheme of, you know, complete motherboard complete oscilloscope

**Dave Jones:** motherboard type boards, you know, they've done well. So, they you know, that would have been a real cost optimization exercise anyway. That looks like a LED, is it? What? HL? HL? I don't think I've ever seen a HL

**Dave Jones:** designator before, but that looks like I mean it's got a it's got a series resistor in there, so uh Okay, or is it some sort of ambient light sensor? I don't think so. It's probably just a LED like a heartbeat LED

**Dave Jones:** or something like that. Anyway, what is all this array of big array of transistors around here for? What? It's got two test points associated with it. Seems to be hooked into the zinc processor up there, but what like why?

**Dave Jones:** Um what are they doing? I I don't know. That is very curious. Um Anyway, JTAG interface, no worries. Whack our point one inch header on there. So, what have we got there? Just a 7404. Got ourselves a crystal there. BOCPC.

**Dave Jones:** Thanks for telling us all the information on that one. Not. Um it's just a 244. Some jelly bean logic. And the ADF 4360. If we go on over the data sheet, that's our PLL, basically our VCO. Our voltage

**Dave Jones:** controlled oscillator, that's what generates the main clock there. So, yeah, it's the jelly bean one. I think we've seen that before. And but it's all about of course the uh loop components that you actually put inside this thing. And I'm sure if you

**Dave Jones:** scroll down far enough you'd find examples of various loop components which some companies shall remain nameless Rigol have screwed up the the loop on the with all the building registers and everything else. Anyway, there's the loop filters for those who

**Dave Jones:** want to analyze that to see if they goofed up. Go for it. And moving on from that, what do we got here? We're entering our trigger section of the board. ADCMP I think that's just a a comparator and 74HC4053

**Dave Jones:** got to have some 4000 series CMOS in there. No wackers. Cells the classic 595 again 74HC4051. It's all happening all jelly bean stuff. Anyway, this is the trigger section. Some local regulation across there. Analog VCC has got its own separate 5

**Dave Jones:** volts and nice little test points all labeled and that's the interface. But people want to see the ADC. We almost missed it. There it is. It's a had 1511. Let's check it out. And here it is. It's a 1 gig sample AD

**Dave Jones:** converter. So no, we're not going to be able to overclock this thing anytime soon. And we've probably seen this in other parts as well. Typical applications digital oscilloscopes. Thank you very much. So yeah, it's purpose designed for this sort of thing.

**Dave Jones:** And of course it's got the four channel interface in there. And of course the 1 gig samples per second will have of course cuz it's not 1 gig sample per second per ADC. It's 1 gig sample per second total. So when you turn on that

**Dave Jones:** second one it's just going to have and well, I'll link it in down below for those who want to check it out. Oh, all right, calm down. I know you want to see the analog front end. Well, here it is,

**Dave Jones:** two identical analog front ends. I'm sure they are. I'm not going to look, but yeah, pretty sure they're absolutely identical here. Now, this actually differs from the analog section used. In fact, I'll try and put them possibly side by side here in the shot.

**Dave Jones:** Different to the one used inside the other 1000X series. So, this is the 1000XE series. And looks like they've got a slightly different front end. There's two relays in this one. There was three in the I'm going to call it the older

**Dave Jones:** one cuz this one is brand spanking new. And we've got some trimmers there, which I don't believe that we had. Two trimmer caps up there that we didn't have on the other one. So, yeah, two relays, but apart from

**Dave Jones:** that, the top section actually all this section in here looks pretty close to identical. So, the previous one had a 200 MHz bandwidth. This one is available in a 200 MHz model. So, I'm sure absolutely sure that the base model

**Dave Jones:** unit um if you bought the 100 MHz version, it's going to have the 100 the 200 MHz analog front end and they just software limited But, if we have a close look at that identical section that we had before, we've got

**Dave Jones:** our cosmo relay there, a 595 port and digital port expander, of course, and an 8370. Let's check that one out. So, to be verified later, but I'm pretty darn sure that everything is identical including the differential uh gain um amp and the uh

**Dave Jones:** variable gain amplifier in there. I'm pretty sure that they're all the same that we had in the previous model. So, I won't go through details. There's the top half for those of you who love to take screen captures, but I've got

**Dave Jones:** high-res head-on photos down below, but I don't know. I didn't get them under the Tagarno microscope, so there you go. Beautiful. Oh, look at that. Ah, it's better than a macro photo. It really is. But, it's limited to 1920 by 1280. Gosh

**Dave Jones:** darn it. And if you want to see the bottom of that, and of course you do. Of course you do. Um there is the bottom. For those playing along at home. And there's not much else. Got a nice big

**Dave Jones:** cutout in the ground plane there cuz they didn't want to uh up- upset the apple cart, but uh that looks all neat and tidy. That's a 200 meg front end. I'm not sure what else I can uh show you there. That's about all she

**Dave Jones:** wrote on the new Siglent 1000 XE main motherboard. They've really uh you know, they've It's not much in your modern uh scopes. Then again, if you look at an old to someone will say it, I'm sure. Look at the old uh Tektronix TDS 210,

**Dave Jones:** for example, which is like 25 years old now or something, and that had bugger all in it, but it also had bugger all uh performance as well. But, this thing is uh very remarkable, and it's all thanks to the uh Xilinx Zynq processor down in

**Dave Jones:** there, and nothing else. It just That's what handles all the grunt in this thing. 1 meg point FFT. I believe it's got hardware serial decoding. It's got a complete digital trigger system, uh which is effectively zero jitter, they

**Dave Jones:** call it, uh cuz it's digital, and you get just one Yeah. Anyway, um because you can extract it out instead of doing the triggering in analog. Anyway, uh probably pros and cons both ways there. And um it's all integrated

**Dave Jones:** inside the zinc um the FPGA part of the zinc in there. Whereas the core of course would be running all the the OS and the display and everything else. So yeah, oh we've got another HL there. There you go HL1 HL2 they've got

**Dave Jones:** to be LEDs. I don't know. I haven't powered this thing up with the uh uh back off it yet. It works flashy flashy. And you betcha that TX RX is a UART. Ta-da! I'll dump this on the EV

**Dave Jones:** blog forum for those playing along at home who want to check out this but once again it uses that U-Boot just like the 1000 X series that we're playing around with last week and uh ECC is disabled and

**Dave Jones:** then 256 megabits. Let's I don't know. Anyway, you can go in here. Let's see if there's anything interesting. Is there Linux? Currently this is not going to be a hacking video by any stretch. I we just want to have a quick booting

**Dave Jones:** kernel booting Linux on physical CPU Linux version 3.9.8.0 for those playing along at home GCC version there you go. Ah, it's all happening. It's all happening. So is there anything interesting? So that's all the Linux boot stuff USB blah blah blah

**Dave Jones:** blah blah Xilinx data Xilinx AXI DMA engine successful. That'll be for dumping all the high speed oh open SPI dev HC595 failed. What? What? That's to speak to a 595. Um but it got this one here did it? Hmm

**Dave Jones:** anyway that's the port expander I would be guessing for the that they use on the front ends but they they might not might have No we didn't see a 595 anywhere else on the uh thing did we? So I think we're

**Dave Jones:** going to assume that that's the that's the front end. But hmm, there doesn't seem to be anything hugely interesting. I don't know. I'm not going to look into this in detail. The dumps down below for those who want to check it out. Oh, no, more

**Dave Jones:** stuff down here. Uh Skippy. Um what else have we got? Driver manager, blah blah blah blah blah. Error module. Doesn't sound that great. Anyway, but this may not be a release version. So, yeah, don't take this as uh

**Dave Jones:** gospel. And bingo, we can actually talk to this. I tried help and uh help not found. Been asked whatever that is. I don't know. All the Linux people are probably screaming at me. Um and so I tried help games, of course, because the

**Dave Jones:** more complicated these things are, the more they have to help you out, apparently. So, uh help not found. Uh hang on, I know what to do.

**Dave Jones:** Damn it, they've taken out the password.
