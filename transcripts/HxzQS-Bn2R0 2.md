---
video_id: HxzQS-Bn2R0
title: EEVblog #1309 - Siglent SDS2000X Plus Scope Teardown+Hack
url: https://www.youtube.com/watch?v=HxzQS-Bn2R0
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 39, "3": 49, "4": 71, "5": 86, "6": 98, "7": 119, "8": 139, "9": 149, "10": 167, "11": 180, "12": 189, "13": 199, "14": 216, "15": 229, "16": 242, "17": 258, "18": 269, "19": 283, "20": 295, "21": 306, "22": 322, "23": 335, "24": 343, "25": 359, "26": 378, "27": 401, "28": 413, "29": 425, "30": 445, "31": 455, "32": 464, "33": 476, "34": 493, "35": 513, "36": 528, "37": 540, "38": 562, "39": 573, "40": 586, "41": 597, "42": 608, "43": 622, "44": 639, "45": 652, "46": 664, "47": 685, "48": 697, "49": 718, "50": 728, "51": 740, "52": 753, "53": 761, "54": 774, "55": 789, "56": 800, "57": 815, "58": 824, "59": 835, "60": 848, "61": 863, "62": 875, "63": 890, "64": 908, "65": 926, "66": 938, "67": 951, "68": 971, "69": 982, "70": 994, "71": 1006, "72": 1017, "73": 1027, "74": 1044, "75": 1059, "76": 1074, "77": 1090, "78": 1106, "79": 1123, "80": 1136, "81": 1152, "82": 1168, "83": 1186, "84": 1200, "85": 1225, "86": 1243, "87": 1272, "88": 1284, "89": 1294, "90": 1305, "91": 1317, "92": 1328, "93": 1339, "94": 1353, "95": 1368, "96": 1395, "97": 1405, "98": 1416, "99": 1428, "100": 1440, "101": 1463, "102": 1477, "103": 1502, "104": 1518, "105": 1531, "106": 1539, "107": 1554, "108": 1570, "109": 1593, "110": 1613, "111": 1625, "112": 1633, "113": 1646, "114": 1661, "115": 1674, "116": 1687, "117": 1700, "118": 1715, "119": 1725, "120": 1737, "121": 1752, "122": 1770, "123": 1782, "124": 1791, "125": 1806, "126": 1814, "127": 1827, "128": 1838, "129": 1850, "130": 1873, "131": 1885, "132": 1900, "133": 1914, "134": 1928, "135": 1943, "136": 1958, "137": 1968, "138": 1984, "139": 2006, "140": 2023, "141": 2039, "142": 2051, "143": 2065, "144": 2084, "145": 2113, "146": 2135, "147": 2147, "148": 2170, "149": 2180, "150": 2191, "151": 2209, "152": 2233, "153": 2248, "154": 2261, "155": 2276, "156": 2293, "157": 2319, "158": 2329, "159": 2346, "160": 2374, "161": 2385, "162": 2398, "163": 2410, "164": 2429, "165": 2439, "166": 2451, "167": 2471, "168": 2496, "169": 2524, "170": 2537, "171": 2556, "172": 2568, "173": 2581, "174": 2592, "175": 2609, "176": 2622, "177": 2641, "178": 2656, "179": 2666, "180": 2681, "181": 2697, "182": 2708, "183": 2721}
---

**Dave Jones:** Hi, it's test equipment teardown time again and I have had this one for a while, so sorry I haven't gotten around to it. Quite a few people have said that they want to see a teardown of this brand small, almost brand spanking new now, Siglent SDS 2000X plus series.

**Dave Jones:** It's the plus series, not to be confused with the previous SDS 2000X series, which we've done a teardown of several years ago, which I'll link in down below at the end if you haven't seen it, and not to be confused with the SDS 2000X-E series, which is the smaller, cheaper two-channel jobby of the 2000 series.

**Dave Jones:** So, I don't know. Why do they confuse it all like this? Anyway, so they currently got three scopes in the 2000 series. This is the new big daddy, the 2000X plus.

**Dave Jones:** This one in particular is the SDS 2354X. So, this is the 350 MHz model, two gig samples per second, four channels, of course, although they do have a version in this series which goes up to 500 MHz and that's one of the differentiators from the just the regular 2000X series.

**Dave Jones:** And other differences from the 2000X series, this one's actually got slightly less waveform update speed, 120,000 waveform updates per second versus 140 for the regular X series. So, I'm not sure what the deal is there.

**Dave Jones:** It's probably to do with the extra memory they've got in this thing. This is a 200 meg points memory as opposed to I think it's 120 or something in the previous one and this one's got 500 microvolts per division.

**Dave Jones:** It's got a 50 MHz function generator output instead of a 25 MHz function generator output and it's got a much larger screen, 1024 by 600 10.1 inch capacitive touchscreen as opposed to to 8-inch screen in the regular X series we've torn down before.

**Dave Jones:** And yes, it is a mixed signal scope. Looks like identical probes and everything else. Couple of USB ports on the front. All the bells and whistles. And yes, of course, with the bigger screen to keep the form factor you know, relatively decent, they've had to go away from the four independent vertical channels to have the one combined vertical channel now.

**Dave Jones:** But that's the price you pay for having the big screen scope. So, this new X plus series starts at 999 Yankee bucks, goes up to about three grand or so.

**Dave Jones:** So, yeah, it does actually look quite big and imposing with its 10.1 in screen here. And on the back, you know, you've got the usual culprits. Quite large fan, so hopefully that's you know, it's relatively a low noise given the larger aperture because it can move more volume of air for a slower speed.

**Dave Jones:** We've got a pass fail output. We've got external trigger. We've got you know, your LAN and ethernet. And your USB. And just in case you thought you'd be getting a monochrome one these days, it's a digital color oscilloscope.

**Dave Jones:** Beauty. So, it's got a couple of pop out feet here which tilt it. It's not too bad. So, it's not going to fall over if you GO AH, STOP STOP you mongrel.

**Dave Jones:** And we've got vents on the side I like that. It's kind of you know, it's it's nice slim form factor. One event for the power supply and another matching vent on the other side.

**Dave Jones:** So, you know, it's a pretty decent looking scope. Although I really I still don't like Siglent's knobs on these things. They're just like silvery plasticky things. And the color schemes it's just a bit I don't know, amateur hour.

**Dave Jones:** There's no spit and polish in it. Wish they'd hire a proper industrial designer just to make it look a bit more professional, but you know, it's pretty decent. Anyway, four channel jobs, we do have the times 10 detection ring around there.

**Dave Jones:** So, auto probe detection. Unfortunately, no external uh supply for you know, active FET probes or any other external current probes. But, it does have a 50 ohm input 5 volts RMS max.

**Dave Jones:** So, yeah, that's decent, but you'd expect that on this class of scope. So, if you just compared it to like a similar size Rohde & Schwarz RTB 2000 here, you can like see the sort of like just the spit and polish in that one.

**Dave Jones:** It's just like a nicer industrial design, gold-plated BNCs, just a nicer color scheme, and this one's just like dull and bland. But, not that that matter. I mean, you know, ultimately it doesn't matter.

**Dave Jones:** It's just But, hopefully you can really see the Well, you can't see the matte screen on this one as opposed to the reflective one on the RTB 2004. It's just Yeah, it's not that great.

**Dave Jones:** Siglent has a nice matte screen, good for video. So, you know what we say here on the EVBlog, don't turn it on, take it apart. Oh, that's so satisfying.

**Dave Jones:** All right, let's lift the lid. Are we going to be metal canned? Yep, of course we are. The cable tied down that there, nice attention to detail. The earth connection looks really good.

**Dave Jones:** I like that. And uh nice heat shrink. Oh, that's not a heat shrink actually. That's one of those material uh fabric ones and uh bundle that's just coming out of the power there and neat fan for those playing along at home.

**Dave Jones:** It's an Adder. Whatever. And no, I can't see any trademark Siglent rust either. It's rather disappointing. Kind of miss the old rust. All right, let's take all this off.

**Dave Jones:** And that will work. There's our screw our um There's our washers, and it should just come off. It should be no wiring. Oh, we're in like Flynn. Look at that.

**Dave Jones:** Can we get those cans off? I think we can. Beauty. Uh bloody heat sinks. All right, so let's actually go to the video tape here because it's just going to be easier because I'm going to compare it with the original 2000X board.

**Dave Jones:** So, on the bottom here, I've got the 2000X PCB and on the top I've got the new 2000X Plus. So, we can directly uh compare the differences here. Sorry, I didn't have a photo of the uh cans off here, but we'll look at the uh analog front end separately later cuz that has uh changed.

**Dave Jones:** So, uh if we have a look at the old 2000X board, we've got our two ADCs down here. Sorry, I couldn't get any of the heat sinks off. They're uh they used uh thermal uh adhesive glue on there and unless I want to get the heat gun out and loosen those puppies up and try and get them off, nah, I'm not that keen and the details ultimately aren't that important.

**Dave Jones:** The new uh board could have like improved FPGAs or something like that. So, whether or not they've done that, yeah, kind of really doesn't matter. We're just looking at the basic um architecture here.

**Dave Jones:** So, anyway, two ADCs, I'm going to be assume that they're the same ADCs because we do have uh the same two gig sample uh per second and obviously one ADC shared between uh two channels.

**Dave Jones:** Same thing happening down here and then uh the ADCs go into um these two FPGAs here. And physically, I think roughly they're the same size, but as I said, they could certainly be upgraded uh FPGAs to handle more horsepower, but same waveform updates per second uh well, actually slightly less, but it's got deeper memory.

**Dave Jones:** So, the memory that they've uh the sample memory that they've got here and here, it's actually going to be more on this one. Um it's going to have a lot more sample memory than it had uh previously.

**Dave Jones:** So, you're going to pay extra for that. That's why sort of like the base model uh unit of this thing is like I think it's $150 more or something like that.

**Dave Jones:** So, it's going to have upgraded hardware bomb cost for that. So, it wouldn't surprise me if they do have slightly upgraded FPGAs because it's been like almost 4 years I think since they released the 2000X down here.

**Dave Jones:** So, they've made significant improvements since then. So, yeah, wouldn't surprise me to find a new FPGA under the hood there. Um yes, even if I take off these latches that hold it down here, it's still thermal adhesive uh glue, which is really annoying.

**Dave Jones:** Anyway, so all that's pretty much the same uh front end wise. So, this is where the physical layout actually starts to differ. On the old design, we had our display processor FPGA under here, and you can tell there's the ribbon cable there going off uh to the LCD.

**Dave Jones:** The new one actually uses like old school um cable up there. So, yeah, that's interesting. Haven't actually taken the board physically off yet, but uh yeah, that's um they went from a ribbon cable back to old school cuz they've entirely changed the display on this thing.

**Dave Jones:** So, it's a 10.1 in, it's higher resolution, they've got more mapping. So, it wouldn't surprise me if this FPGA is greatly enhanced over this one here. So, yeah, they've physically moved it from here over to here.

**Dave Jones:** So, this has to get from here all the way over to there. So, yeah, that's a significant uh difference. Anyway, um so, I assume that this is an upgraded uh FPGA to the one used over here because it's higher resolution and uh everything else.

**Dave Jones:** So, now on the old one, here is our uh applications processor. That was a uh Analog Devices. Well, we can go right in there. That's an Analog Devices ADFP.

**Dave Jones:** It's one of those uh Blackfin uh jobbies, and we don't actually have that up here. Well, it's we can't see it anyway. So, they could have uh changed that completely uh to something else.

**Dave Jones:** They could be running a a even a Xilinx uh Zynq or something under there uh perhaps. I just don't know. Anyway, they've got a Lattice uh semiconductor. Um is that a CPLD or an FPGA?

**Dave Jones:** Um it's interesting that almost certainly these ones under here won't be Lattice. So, I think they might have actually mixed them. Anyway, the same Lattice uh was used down here.

**Dave Jones:** Of course, what that's for is here's our logic analyzer input connected down in here, and here's our uh latches and uh level, you know, there's going to be like a trigger level conversion and um you know, comparators and uh trigger stuff and things like that.

**Dave Jones:** So, all of that there is our logic analyzer part. And if we go up here, it's basically uh the same thing except there's another jobby in here right next to it, which is um I can only assume that that's the applications processor, and they've moved it down there.

**Dave Jones:** But anyway, is it Is it actually the same part, the 0640? The 0640. Yeah, it's exactly the same. So, I don't think the uh specs have increased. I think it's still 500 meg samples uh per second.

**Dave Jones:** Oh, it is a CPLD. There you go, it tells you. It's not an FPGA. So, anyway, that's like they probably haven't changed anything in there unless they've like tweaked it, made a few improvements, or something like that.

**Dave Jones:** So, this one here is still the applications uh processor, I would be guessing because this is still got to be uh the uh display process FPGA unless they've like changed the architecture and it's combined, as I said, like a Xilinx Zynq, which has a combined FPGA and uh applications processor in it, like an ARM processor in it, then yeah.

**Dave Jones:** Yeah, hard to tell unless you actually get the uh heatsink off and the the off, which I'm not keen to do at the moment. But, they've basically got uh the same number of uh you know, same major components here.

**Dave Jones:** Um sample FPGA and ADC, uh display, and FPGA, sample, and uh ADC, and display, FPGA, applications processor, applications processor, and uh logic analyzer, logic analyzer. So, you know, apart from that, it's pretty much the same.

**Dave Jones:** Then, we've got our function generator stuff down here. Now, that actually has changed cuz it's now 50 meg samples uh per second. And you can go in there and look at individual part numbers.

**Dave Jones:** Uh high-res photos over on uh LinkedIn on my Flickr uh account and over on eevblog.com. What was that, a burr brown? Ooh. Anyway, um yeah. So, that's changed down here.

**Dave Jones:** We've got five We've got five relays, NEC jobbies. Five relays here. They switched from NEC, have they? No NECs anymore. Still made in Japan. All the best stuff's made in Japan.

**Dave Jones:** Anyway, 50 meg uh arbitrary waveform generator. Then, we've got just got all the uh power supply for all the different rails that all these pesky FPGAs require, things like that.

**Dave Jones:** So, that's yeah, that's similar on both of them. That's going to be our PLL in there for our logic analyzer. I think it's going to be Surely, it's identical down here.

**Dave Jones:** Uh no, no, different jobby down there, I think. That looks different. Anyway, there's our Ethernets. There's an interesting little uh semiconductor E-squared PROM. Look at that. They're storing something in there.

**Dave Jones:** Hmm, I wonder what. Good thing about this, JTAG headers. There's one in there. They're already populated. Just whack on your JTAG on there and Hack Oh, no, that one's not.

**Dave Jones:** Sorry, that's uh I-squared C, SCL, SDA, and digital VDD enable. Oh, that's interesting. Ah, that that controls What? Is that just Is that just for setting up That's a power supply.

**Dave Jones:** Um so, I don't know why they've got that in there next to the Like, you know, its layout implies that it has something to do with the power supply.

**Dave Jones:** I'll check the data sheet for that. You can see more headers up here. That's another JTAG job. Ah, there That's They don't have it, but that is probably the boot um serial interface.

**Dave Jones:** So, yeah, might probe that later and have a look to see if we can't get the boot information. Did we do that on the previous one? Not sure. Anyway, it looks like another JTAG over here.

**Dave Jones:** So, they got no shortage of headers to access to hack this thing. Nice. And sure enough, just went and looked at the data sheet for the TPS65400 here. It's It's on its side, so half the electrons are going to fall out.

**Dave Jones:** And yes, it does have a SMBus / I2C interface to control it. It's a multi-channel Yeah, power management controller. And it looks like yeah, they they do actually set that up.

**Dave Jones:** There's a reason they wouldn't populate that unless they actually you know, program this thing, factory programmed it to do what they want. So, now that 83849 there that's a national semiconductor a PHY.

**Dave Jones:** Why it's physically here and here's your Ethernet over here. I don't don't get it. Seems like poor placement. Hmm. That solder is a bit how you doing there? Um Is that a couple of solder balls in there?

**Dave Jones:** Not sure. Is that like All the vias are tented. So, I It's not a pad. I don't know. Anyway, they look like USB jobbies. Curious to know why they left that cap off there.

**Dave Jones:** Looks like they got three caps in parallel and they just left one off. Maybe they're really expensive. So, yeah, generally the layout of this like seems a bit bit over the place.

**Dave Jones:** I mean, you know, this has to get over to here like this. These USB ones have to get over to the USB over here. Where else is there the other USBs they're down the bottom of the board here on the front panel.

**Dave Jones:** Seems all over the place, but anyway, but now I'm thinking that these USB drivers here that's going into this, which I assumed was the display processor. Why the USBs would connect to that?

**Dave Jones:** I don't know. So, as I said, it that could be a combined. I think they've changed the architecture a bit perhaps. So, that then leaves, well, what is this one?

**Dave Jones:** If this is a combined applications and display like a Xilinx Zynq or something like that perhaps. Um, then what is this puppy doing? Hmm. Okay, let's have a look at the analog front end significant differences here.

**Dave Jones:** I've got the old 2000X on the bottom, although I still believe it's a current model. I don't know what the deal is. I kind of Oh, I did I think they're physically like the same size case except one has the bigger screen.

**Dave Jones:** Maybe they want to keep both cuz some people prefer having the four separate channels on like physical knobs on there and the smaller screen and maybe like 150 bucks less or something, but I don't know.

**Dave Jones:** I don't know why you just wouldn't consolidate with a new design. Anyway, um, the first uh, difference is that the old design has uh, four relays once again NEC jobbies.

**Dave Jones:** They've changed to I don't know what's uh, FT is that like like Fujitsu or something? Anyway, made Made All of this stuff's is made in Japan. And uh, the old one has a trimmer compensation caps, whereas the new one Where's Where's Wally?

**Dave Jones:** I'm not seeing it. Not seeing it. Oh, by the way, no, I missed they have a a Cosmo electronic relay down here and they don't have an equivalent one up here unless that No, I don't know.

**Dave Jones:** I don't think that is. No, it's not. So, yeah, it's significant differences there. The newer one has a much beefier looking It's 24.9 ohms. So, is there another one on the flip side of the board?

**Dave Jones:** I can only assume there is. Anyway, the new design This is a 500 MHz front end. You buy it as you can't buy the 3 500 MHz model. You buy the 350 MHz model and then you get the software upgrade, which changes it to 500 MHz.

**Dave Jones:** So, presumably there's like a varactor or something in here somewhere, which simply changes the software-defined bandwidth in this thing. Whereas the old one, this was 300 MHz maximum. So, you couldn't go any higher than that.

**Dave Jones:** So, new one, yeah, 500 MHz layout, 350. So, yeah, it looks it looks significantly more refined. Look at this divider network they've got down here. So, we've got the old store watt, the HC595, one of my favorite TTL chips.

**Dave Jones:** Of course, that's just a serial-to-parallel expander so it can drive all the control pins going into the various chips and probably one of those lines like controls the filter element or something like that.

**Dave Jones:** So, anyway, here's our output driver. You can tell by by the symmetry here. Look at the nice symmetry. That's a differential output driver. Isn't that beautiful? It's a 6518.

**Dave Jones:** And the old one is a analog devices 6370. So, that looks like is that our differential output driver there? So, that would be an analog front end. Look at all the sort of like the residue on there and stuff.

**Dave Jones:** Anyway, all right. So, this is what they had previously the 808370 low frequency to 750 MHz digitally controlled VGA. That's not video graphics adapter. That's gain amplifier. And this is what you find in you know, it's got the adjustable gain preamp.

**Dave Jones:** It's got the adjustable output amp. And I think it even that probably has the ability like the inbuilt filters as well. So, that then that's how they software the gain on these things, I believe.

**Dave Jones:** Anyway, they've changed that over to the LMH6518, which is a faster and 900 MHz digitally controlled programmable gain amplifier. And I wonder if they have and look And of course, specifically oscilloscope programmable gain amplifiers differential ADC drivers because that's exactly what we're doing.

**Dave Jones:** So, yeah, they know their target market. And bingo bandwidth limiting circuitry. So, that would not surprise me if they're just you have to just have a little twiddle. It's good to have a little twiddle of the pins here and you might be able to change the bandwidth limit on this thing.

**Dave Jones:** Possibly from 350 to 500 MHz. They have selectable bandwidth limiting circuitry common to both main and auxiliary 20. So, that's how they obviously doing the 20 MHz bandwidth limit even best scopes these days all have 20 MHz bandwidth limits because that's a common frequency used for back in the old days it was just a de facto standard that uh you use for power supply noise measurement bandwidths for

**Dave Jones:** example. That's why all scopes still have like a 20 MHz bandwidth limit. Anyway, so bingo, 20, 100, 200, and 350. That's why this scope has a 350 MHz bandwidth limit.

**Dave Jones:** It's because um like it's in the next one is 650. It's not like it has 500. It's basically they designed this front end for 500 MHz bandwidth minus 3 dB.

**Dave Jones:** Of course, it'll go beyond uh that. So, they obviously for the full 500 meg limit they disable the like they disable the bandwidth limiting completely. And uh yeah, but for the 350 MHz model.

**Dave Jones:** So, that's all it is. So, that's what you're paying your what 1,100 bucks for is for the fact that they just flip a little bit inside the register here and it just changes the bandwidths.

**Dave Jones:** So, obviously what you could do is you could play piggy in the middle here for example and you could twiddle these here, twiddle dee, twiddle dum, and you've got your bandwidth limiting circuitry disabled.

**Dave Jones:** Hmm. And that looks like it just uh directly drives the ADC um differentially of course. Uh you know, you don't have single-ended at this sort of frequency run across boards.

**Dave Jones:** Um the rest of it doesn't really matter. But anyway, um yeah, that's a 500 MHz front end old 300 MHz front end. So, uh significantly enhanced um for a base cost really of an extra 150 bucks.

**Dave Jones:** So, it'd be interesting to know if anyone's got a uh teardown of the lower models whether or not they actually have the same front end or whether or not you have to actually buy the 350 MHz model to actually be able to get that.

**Dave Jones:** You know, if this is in the $999 model, then that's potentially pretty good. You could hack it up to 500 meg, but I wouldn't count on that. So, yeah, please leave it in the comments down below if you know of links to anyone who's torn down a lesser the lower bandwidth model cuz this could specifically be different because they do not sell an option that lets you

**Dave Jones:** upgrade a software option that lets you upgrade from 100 MHz to 500 MHz, for example. They they don't offer that. And why wouldn't they if it was the same hardware?

**Dave Jones:** So, you know, it wouldn't surprise me at all if the hardware is significantly different to what you see here in the lower end models. Maybe they actually even reuse this down here, perhaps.

**Dave Jones:** All right. All right, let's boot this sucker and see if we can get some of the serial terminal information out of this. So, I've got it hooked up to a USB serial interface 115,000 board, you know, the usual 8N1.

**Dave Jones:** And let's see. So, I've got to turn on the soft power button. So, yeah, I've got it connected up. I haven't soldered it in that header. I've just got it sitting in there.

**Dave Jones:** So, you know, the contact's a bit how you doing, but she'll be right. So, let's go. Bingo. We're in like Flynn. Start menu VDMI config. Whoa. Whoa, we got a whole dump of information with the timestamp next to it.

**Dave Jones:** Wow. Down to the microsecond, the timestamp. Cuz we've got six decimal places. Initializing VNC. I got no idea what half this stuff is, you know, all the reverse engineer aficionados out there.

**Dave Jones:** Product type SDS2004X done value plus plus. Scope ID. That's interesting. That's all zeros. Not sure what the deal is there. And we've got a couple of flashy flashies. One, two, three, four.

**Dave Jones:** So, it looks like that one's probably the logic analyzer. Flashy flashy. That one's looks like it's the heartbeat for the processor. Oh, another one up there. Sorry. That looks like it's a heartbeat for the um well, that Sorry, that could be the processor up there.

**Dave Jones:** Anyway, another heartbeat and heartbeat for the um 80 like sampling um engine and a LED for the second sampling engine there. So, whole bunch of stuff. I will uh dump Oh.

**Dave Jones:** There's a lot of blank at the start of that. Um so, I'll dump this as a text file on the uh EV blog forum and people Yep, there it is.

**Dave Jones:** Xilinx Zynq. There it is. So, yep, they've switched over to the Xilinx Zynq. Uh ECC disabled, 256 mega RAM. Bad CRC. What? These didn't bother enabling it or it's actually wrong.

**Dave Jones:** Flatten device tree blob. Whatever that is, no idea. There you go, it's running Linux 3.19 um Linux kernel uncompressed. So, all you Linux fanboys out there can start hacking away.

**Dave Jones:** Booting Linux. There we go, that's a zero time booting Linux on physical CPU zero 3.19.0-01 blah blah blah. Um V7 processor, that's inside the Zynq, of course. Um the Zynq is a combined if you know the Zynq is a combined FPGA with an um seven uh core in it as well as hard silicon, not as part of the FPGA fabric.

**Dave Jones:** And that's what makes it so terrific for FPGAs like this. That's, you know, it's relative It's a fairly expensive chip, but like it does everything. It's got the processor that you can run Linux on and it's also got all the FPGA stuff where you can do all the fast parallel uh you know, display stuff that, uh, you need for an FPGA.

**Dave Jones:** You know, the fast updating and everything else. So, yeah, I really don't know what I'm looking at. So, I'll dump it on the EEVblog forum. Go Go for your life.

**Dave Jones:** Um, but there's tons of stuff. And yeah, here's the, uh, this is like the boot time. This is a microsecond, uh, timer. So, it goes down to 1 microsecond here.

**Dave Jones:** It's how long it takes to execute each of those instructions or each of those do each of those tasks. And I'm sure, uh, it's trivial to like, you know, load like custom boot images and all sorts of other, uh, stuff.

**Dave Jones:** I'm sure people will figure that out. It's doing some calibration there. Looks like it's, uh, testing the acquisition engine, the first and second acquisition engine. Cuz remember there's two acquisition FPGAs in there.

**Dave Jones:** Product type SDS2004. No lease failing. No idea. Be interested to know what this scope ID is. It's got 000 all up there, but then it's got an ID here.

**Dave Jones:** Um, and then another scope ID here. Product, uh, ID. I mean, like, is it as simple as, um, changing like a product ID to make it go to the 500 meg version and then the code just takes care of it or something like that, perhaps?

**Dave Jones:** Um, wouldn't surprise me if it's that easy, but, you know, uh, Murphy. Arbitrary waveform generator is okay. That's calibration data. It's, uh, doing, uh, skew. Why isn't it only channel 3 skew?

**Dave Jones:** Why isn't it doing all the channels? And it's using Siglent dev, I guess. That's their development environment or something, is it? It's from October 6, 2007. It's pretty ancient.

**Dave Jones:** Wow. So, there you go. That's it. Um, that's all I'm sure there's lots of juicy stuff in there. As I said, I'll leave the, uh, text file on the EEVblog forum.

**Dave Jones:** Actually, no surprises for finding. It looks like Mr. Miyagi has Yeah, there's a hack for this thing. So, yeah, I won't show you what's in the links and things like that.

**Dave Jones:** You can go check it out for yourself, but yeah, there's stuff there. And in case you're interested, heat sinks with no fan. Ernie Bernie, I can't keep my hand on that.

**Dave Jones:** Yeah, so ADCs Yo, yep, Ernie Bernies. Yep, yep, I can't. Oh, wow, yeah, they all run very hot. I can't I cannot keep my hand on any of those.

**Dave Jones:** So, they're over like 55°. They're probably 60° or more. But of course, they wouldn't run that hot when you have the fan running continuously. It would cuz you'd get air flow over them and they're much more efficient.

**Dave Jones:** Heat sinks aren't very efficient without air flow. Forgot to press record. I just switched it off and you can see that here. All it did was just unmount the volume there.

**Dave Jones:** So, let me switch it back on and There we go. Just boots straight back up. Doo doo doo. Hear all the relays click. It's very satisfying to hear the relays click when it turns on.

**Dave Jones:** Can't read a UART. Maybe you can feed in data. It's Yep, there we go. Should be booted now. Should be working. And here's our power supply and check this out.

**Dave Jones:** Somebody had fun with the Silastic. Fantastic. Love the little heat sink down there, little itty bitty one. Nice isolation slot down in there. Looks like it has all the requisite stuff.

**Dave Jones:** Big ass common mode choke. There's the diode bridge. I see Yeah, look at all the isolation slots. Yeah, that's that's just really nice. Looks It's all about the vibe.

**Dave Jones:** Just the vibe of the thing. It's just the vibe of it. No, that's it. It's the vibe. I rest my case. And the vibe is good on this one.

**Dave Jones:** It's a SsangYong, you know, not the worst, certainly not the best, but anyway, what do we got? Looks like there's SsangYongs on the output as well. So Yeah, at least they've kept to the one manufacturer, you know, they haven't like looks like they haven't just gotten whatever they could at the Shenzhen market that week.

**Dave Jones:** So yeah, nice big isolation slot under the transformer there as well with and the optocoupler. So just small attention to detail even isolation slots around the nuts there. That's fantastic.

**Dave Jones:** Got to protect your nuts. Okay, something is very strange here. I've got of course the 350 MHz model and if I go into utility, so I thought I'd check if I had the 500 MHz bandwidth option.

**Dave Jones:** It says remaining times optional. So I'm not sure what the deal is there. Anyway, I believe that that 05 there would be the 500 MHz option and yes, I do have the ability to um hack this thing.

**Dave Jones:** So that's what I want to try. Anyway, what I tried to do is like feed in a like 5 350 MHz 500 MHz signal and I was getting like nothing.

**Dave Jones:** Like almost nothing at 500 MHz. So I've actually got it down. I'm actually generating a 100 MHz signal at the moment and I'm getting basically minus 3 dB, you know, .707 roughly for the 100 MHz.

**Dave Jones:** So it's almost as if this thing only has a 100 MHz bandwidth and no I and yes, I do have the full bandwidth option on and you know, 200 MHz and of course if we go to 20, it uh it it drops down.

**Dave Jones:** And I've got the full bandwidth on. It's almost as if this is only the 100 MHz model. Um it's it's just nuts. And if I go to 200 MHz, there it is.

**Dave Jones:** 200 meg and it's dropped to naff all. And fall. And if I go to 500 MHz, it's just uh it's dropped off a cliff. Because if I go over to my uh 500 meg Keysight over here, there you go.

**Dave Jones:** My 500 MHz um yeah, it's over 0.707. So, it's basically this thing has greater than 500 MHz bandwidth. But if I take the exact same signal, whack it into here, yes it is uh but they're both uh 50 ohm terminated, I get absolutely nothing unless I uh you know, I basically have to go down to 100 MHz to get my 3 dB bandwidth.

**Dave Jones:** So, I I think I've been diddled. And yes, I've tried the other uh channels by the way. Here's channel two and channel three. This is the 350 MHz. So, anyway, so what I'm going to do now is have a little bit of a fiddle and see if I can uh get higher bandwidth.

**Dave Jones:** Winner winner chicken dinner. Hang on, it didn't instantly uh give me the more bandwidth. So, I tried repowering and it's now actually vanished. Where has the bandwidth option gone?

**Dave Jones:** Uh I'm not sure if that's normal or not. So, yeah. I don't know what happened there. I've um installed a license for the 500 MHz version and this is I'm only getting like 100 MHz.

**Dave Jones:** Let me put it back to 100 MHz. Here it is. There you go. And uh yeah, 0.707. It's only 100 um you know, little bit more little bit more than 100 MHz bandwidth.

**Dave Jones:** Um and I still got the I've got full bandwidth limit on. Turn 20 meg on of course. 200 won't make any difference and uh having full on makes a little bit of smidgen of difference there, but still it's go up to 500 meg.

**Dave Jones:** And not flatline. Now apparently it's supposed to Now I checked on the forum and apparently it is supposed to actually remove that option once you enter it and sure enough we go into the info screen it's a changed it to the SDS 2504X plus and of course we have a 2354X cuz it's the 350 megahertz so 25 is 500 megahertz.

**Dave Jones:** So that's there but the waveform so I thought I'd have a go updating the firmware we'll see what happens now. No, that simply doesn't work. We've got 750 millivolts here and like 50 ohm input of course, you know, we can change it to one meg, but it's supposed to have 50 ohms supposed to be one uh RMS.

**Dave Jones:** I come a gutser. Wow, I'm dumb. I was just looking around and I noticed down here it had down in the time base 10 bits. So I thought I'd go in there and you know, have a look.

**Dave Jones:** Well, I'm feeding in our 100 megahertz signal. 750 millivolts let's go to 8 bits. Ha. 1 volt. Dull. The problem here is is that you saw it before it only had on 10 bits it's only got like oh no I'm sure it was showing 50 points before oh maybe I was over a time base here you go 40 points 20 points.

**Dave Jones:** There's not many points in there. So anyway, we're coming a gutser with our box car averaging filter there. So we have to turn it back to 8 bits. All right, let me go.

**Dave Jones:** Now let let's go 200 megahertz. Dull. I feel really dumb. There it 200 megahertz. Let's go up to 500 megahertz. Let's see if we actually get our 500 meg bandwidth.

**Dave Jones:** And 500 meg, there it is. It's actually higher than 500 meg, 800 and 50 odd millivolts. So, around about like, you know, 0.707 minus 3 dB, we're up at 590 meg.

**Dave Jones:** There you go. So, yep, I was able to successfully hack this thing and it's really quite easy. I'm not going to tell you how. It's over on the EV blog forum if you want to do it and you can get possibly get, although I already had the options, you know, the function generator, the MSO, the FlexRay and the can and all that, all your triggery goodness.

**Dave Jones:** And let's just check the Keysight over here. This is 500 megahertz. There it is. And let's turn on our high resolution mode, which is equivalent to the Siglent 10-bit mode, of course, with the boxcar averaging.

**Dave Jones:** And you don't get the same digitizer problem as you get on the Siglent. So, that warrants some more investigation. I won't do that now, but that's that's interesting. Hmm.

**Dave Jones:** Um the arbitrary waveform generator, great that it's built in instead of having like the external thing which they've provided for other scopes and it's 50 megahertz as opposed to 25, but you know, it it is fairly rudimentary.

**Dave Jones:** Unfortunately, the different wave types, yeah, okay. We've got, you know, sine, square, ramp, pulse, noise, DC. A relay clicks inside when you go to DC, by the way. It's got arb as well, which is great, but the sine, like how it's got no modulation capability at all.

**Dave Jones:** So, it just, you know, it really would have been nice if it had modulation capability. I don't think you can do that in your arb type. It's just I think it's just got the different Yeah, you got the math ones, the engine, windows, trig trig functions and all that sort of stuff and you can store the, you know, upload USB ones and, you know, things like that and probably via the LAN as

**Dave Jones:** well and stuff like that. But yeah, lack of modulation capability, pretty disappointing. I was going to use it to uh generate my standard waveform which like going to have to use the Keysight.

**Dave Jones:** One thing that's really silly on this is the universal select control here. It changes the intensity of your display, but there's nowhere on the display, unless I'm absolutely blind, that shows me the intensity level at all.

**Dave Jones:** I mean, that's just silly. Why? Anyway, this won't be a full review video because well, that could be an hour in its own right. I've already looked at the new like interface Siglent which is identical to this in terms of like the drop-down menu display and the touchscreen interface and the zone triggering and all sorts of other stuff in the Siglent 5 SDS 5000 series review.

**Dave Jones:** That's a 1 gig scope, really high-end, but this one is going to work exactly the same. Obviously, it's the same underlying operating system user interface and all that sort of jazz.

**Dave Jones:** It's just that the hardware's physically a bit more capable on the higher-end one, but yeah, like it's really an incredibly powerful scope. You got to remember this is like a 900 and this starts at $999.

**Dave Jones:** Sure, it's for the 100 MHz version, but as you saw, I was able to easily upgrade this thing. I won't tell you exactly how. If you want to know, it's over on the EEVblog forum.

**Dave Jones:** The information's readily available. So, 995 bucks and you get a lot of a ton of incredibly powerful stuff and they have added bode plotting here as well for the thing and of course with the function gen going up to 50 meg that's like really handy.

**Dave Jones:** That's higher than like the 20-25 meg typically found on other scopes. That's really quite nice. How do I get out of the control loop bode response plot off? I guess.

**Dave Jones:** Yeah, off. It's also got power analysis there and you can do power quality switching loss slew rate. Might have to actually do a video on that one day. Get a good example to hook up.

**Dave Jones:** I believe Siglent actually have like a proper demo board for this that allows you to actually look at all the different types. So if you want me to actually look at that maybe ping Siglent and get them to send a board in and something and then we can do that like it's just nice if you already have like a nice hardware example that you can probe easily and

**Dave Jones:** you know do all that sort of stuff. And like all that sort of jazz but that is an optional extra of course and it's got of course well no mass testing it's got serial decoding as well and look this is not a review of course but it's got I2C SPI UART CAN LIN FlexRay CAN FD I2S got a built in hardware frequency counter but it's already showing it up there so I don't

**Dave Jones:** know why they actually have another counter over here. I'm not entirely sure but anyway it's pretty powerful the trigger of course they've got the zone triggering if I remember rightly I had some issues with that on the 5000 series so zone one on can we Yep, go like that and you can trigger within the zone must intersect like that and bingo it's going to trigger on little ramp pulses and things like that

**Dave Jones:** but I think there were issues with it on the 5000 maybe but that was like a year ago maybe they've solved those on the 5000 and that any things they solve on one is probably going to flow down to the other models that use the same OS.

**Dave Jones:** It's just an incredibly modern and powerful scope and probably one of the best bangs for buck you get under a thousand bucks although I've yet to do that. If you want actually give me a thumbs up in the video and also leave it in the comments down below if you want to see like a thousand dollar scope shoot out.

**Dave Jones:** I can do that like on paper like a spreadsheet shoot out. It's really hard to get physically all these you know five or six different scopes and then do a big video but you remember how I did the one gigahertz scope spreadsheet shoot out.

**Dave Jones:** If you'd like to see the same one for say like a thousand dollar price point. What's what's the best you know and most hackable best bang for buck under a thousand bucks or some you know arbitrary limit like that.

**Dave Jones:** Price is always a good arbitrary limit so anyway if you want to see that let us know but it's it's a well built unit incredibly powerful. I've used it a little bit off and on and it is a quite nice.

**Dave Jones:** It's fast and responsive and it's you know it really is quite nice scope but as I saw in the 5000 I think if I start using it more there'll probably be a few little quirks and and things like that but fixing is Siglent like the firmware I just uploaded was just like released like ten days ago or something.

**Dave Jones:** They're really fixing issues and solving things and up and grading firmware and adding new options like the baud plot test and things like that so good stuff from Siglent.

**Dave Jones:** It's fantastic to see incredible value and unfortunately well unfortunately in quote marks because it's still incredible value for money the nine hundred ninety nine dollar unit is only a physical two channel unit and I believe you physically only get the two channels in it.

**Dave Jones:** It's thirteen ninety nine. This is like just the retail price on their website. You might be able to get it better on the street price for the base model four channel unit, but even that jeez, pretty darn good value, let me tell you.

**Dave Jones:** And one of the cool things is that it's got the LAN interface. You can do just automatic DHCP connected to your network and then you got phone access. No worries, look at that.

**Dave Jones:** Obviously not the best thing on the phone, but there it is, it's connected. Got our skippy commands, our instrument control. So, there it is. We've got our screen. So, this would be much better on an iPad and can we actually There we go.

**Dave Jones:** We can zone trigger and you can see that that is actually live updating on there. That's really cool. Good stuff from Siglent. It's fantastic to see incredible value like and you can hack it, too.

**Dave Jones:** Wow, great bang for buck. Anyway, if you like the video, please give it a big thumbs up. As always, discuss down below and if you want me to test something specific on this thing, I can certainly do that.

**Dave Jones:** I'll take requests and I can just whack a quick five minute video over on my EVblog 2 channel. That's what the EVblog 2 channel's for. No spit and polish, just turn the camera on, yap away, test something and upload.

**Dave Jones:** Catch you next time.
