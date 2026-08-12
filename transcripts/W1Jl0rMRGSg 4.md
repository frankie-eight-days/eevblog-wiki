---
video_id: W1Jl0rMRGSg
title: EEVblog 1503 - Rigol HDO4000 12bit Oscilloscope TEARDOWN
url: https://www.youtube.com/watch?v=W1Jl0rMRGSg
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 29, "3": 42, "4": 60, "5": 69, "6": 79, "7": 87, "8": 99, "9": 111, "10": 121, "11": 130, "12": 139, "13": 152, "14": 174, "15": 185, "16": 196, "17": 209, "18": 223, "19": 233, "20": 246, "21": 264, "22": 276, "23": 290, "24": 308, "25": 316, "26": 333, "27": 351, "28": 361, "29": 372, "30": 382, "31": 394, "32": 403, "33": 415, "34": 433, "35": 443, "36": 457, "37": 469, "38": 479, "39": 495, "40": 503, "41": 523, "42": 534, "43": 547, "44": 565, "45": 576, "46": 601, "47": 610, "48": 628, "49": 638, "50": 653, "51": 662, "52": 675, "53": 689, "54": 700, "55": 714, "56": 726, "57": 735, "58": 754, "59": 763, "60": 771, "61": 794, "62": 806, "63": 816, "64": 830, "65": 841, "66": 854, "67": 866, "68": 874, "69": 889, "70": 901, "71": 910, "72": 929, "73": 945, "74": 961, "75": 970, "76": 980, "77": 992, "78": 1004, "79": 1015, "80": 1028, "81": 1041, "82": 1051, "83": 1065, "84": 1074, "85": 1084, "86": 1096, "87": 1107, "88": 1116, "89": 1125, "90": 1140, "91": 1151, "92": 1167, "93": 1176, "94": 1193, "95": 1208, "96": 1219, "97": 1232, "98": 1244, "99": 1264, "100": 1277, "101": 1288, "102": 1297, "103": 1317, "104": 1330, "105": 1340, "106": 1356, "107": 1368, "108": 1379, "109": 1390, "110": 1404, "111": 1419, "112": 1432, "113": 1444, "114": 1464, "115": 1476, "116": 1493, "117": 1506, "118": 1518, "119": 1529, "120": 1540, "121": 1555, "122": 1565, "123": 1576, "124": 1587, "125": 1602, "126": 1614, "127": 1624, "128": 1638, "129": 1653, "130": 1666, "131": 1687, "132": 1699, "133": 1712, "134": 1722, "135": 1733, "136": 1751, "137": 1761, "138": 1773, "139": 1783}
---

**Dave Jones:** Hi, it's time to tear down this new Rigol HDO 4000 series scope. I'll leave my first impressions and noise measurements video linked in up here. If you haven't seen it, it's got a new Rigol ASIC in it and I believe it also has a new Rigol front end and of course it is a 12-bit jobby.

**Dave Jones:** So this same I think the same front end chipset in this is going to be used in the new HDO 1000 series which is on the way. Anyway, let's take it apart, shall we?

**Dave Jones:** Not a fan of the feet, really? Oh, you betcha. Beauty. Oh, look at that. Jeez, that was a bit horrific. Got medieval. And it uses kind of like the de facto standard four screw arrangement here just to hold on the back case.

**Dave Jones:** And by the way, on my first impressions one I totally missed the fact that this has a battery pack slider on there. Hence all this wanky shape in here is designed and like clips up in here designed to have a battery pack slide in there, but I I don't know if that option is available yet, but it's there.

**Dave Jones:** It's obvious so obviously there'll be a back piece to be in there. Anyway, this will lift off and we've got the metal work. Oh, and that's oh yeah, there you go.

**Dave Jones:** So that's actually screwed into the back of the metal work there. Got a couple of RFI tabs there and you can see it's probably going to be one big single board construction.

**Dave Jones:** Oh, no, actually. I don't know. Anyway, we'll find out. Is it one big single board? Oh, look at this, dual fan jobby, dual exhaust on this bad boy. No wonder it's loud.

**Dave Jones:** Jeez. So anyway, air flow wise, it's all coming in this side. I like how it goes down onto the board as well. You can see the heat sink in here is angled in the right direction.

**Dave Jones:** Oh, that that that heat sink extends all the way down into there. When we get that off you'll see it. But anyway, the air comes in here and they've got the fins in the right direction for the air flow and also the power supply inside there.

**Dave Jones:** So the power supply is in the upper half here and then that all comes out the other side. But yeah, as I said in the in first impressions, it is rather annoyingly loud and whiny.

**Dave Jones:** And as is common, we have to get the nuts off here. There's no washer, no star washer under there before we can lift off the entire thing. There we go.

**Dave Jones:** Although, yep, yep, I have to disconnect a few things. I'll get back to you. And we're in. There you go. AND WOW, LOOK AT THE heat sink on the front end here.

**Dave Jones:** And also, would this be the ADCs as well? So, um yeah, the new front end, the 12-bit front end ASIC is chewing some power here. That is like the heftiest heat sink in this thing.

**Dave Jones:** Um and usually when you got four channels like this, there'll be four ASICs here for the front end, and then probably two ADCs in here, and then the acquisition um ASIC, and then the whatever processor they're using to run the Android operating system on this thing.

**Dave Jones:** Anyway, that is very impressive and nice big single-board construction. And I am liking the look of the mains assembly down in here. The earth point there is very nice.

**Dave Jones:** Look at that. And they've got all crimps as well. It's neat and tidy, though. Should be easy enough to upgrade the fans in there for quieter ones. So, yeah, check out the just multi-stranded.

**Dave Jones:** That is just one big crimp terminal in there. They've got the multi-strands coming out here cuz I guess they wanted to like reuse the connector over here. And obviously, this is the battery contact board, and we can actually get that out there.

**Dave Jones:** You can see they've got a nice little plastic interface there with metal threaded inserts. So, that's really nice. So, there There you go. That is just It's basically just some MOSFET switch in there for your battery.

**Dave Jones:** So, it chooses either the battery interface um or it just comes from the power supply. And that's it. Took me a few seconds to figure out what that board down there was, but it actually tells us our AC triggering board.

**Dave Jones:** So, they've got an optocoupler there, and so it just takes the mains output and the mains input here, um and just gives us an optocoupler output, which then goes over this cable goes over to the main board.

**Dave Jones:** So, yeah, that's just for our line triggering. So, they've gone to a lot of trouble there. And we'll go through the board in some detail, but this is the LCD connection, so we can take that off and then we can see it, but I'm going to just going to now remove all the heat sinks so that we can take some high-res photos and go into it.

**Dave Jones:** If you don't know, I always have high-res photos available on my EVBlog Flickr account linked over on evblog.com. Well, I found an Artec 7 under there, and this one over here looks interesting, but we'll take a look at that.

**Dave Jones:** Now, let's see what's under the front end. Oh. Oh, okay. There you go. Oh, isn't that nice diecast case? Oh, isn't that beautiful? They've used sil pads there, and let's have a look.

**Dave Jones:** There's our four front ends. Geez, there's not much in it. Remember, this is an 800 meg bandwidth software upgradeable front end. So, this is 800 meg. So, this is all their custom I do believe they've rolled their own custom front end, but I'll take some high-res photos and we'll go in there and check it out.

**Dave Jones:** There's not much. They've got two relays. What brand are they? Not sure from this point. And up here, we've just got Yeah, they heat sinked all three of those chips.

**Dave Jones:** Well, I'll tell you what, I'm pretty impressed. Everything in here is metal threaded inserts for all of the like holding down the main metal chassis here, and you normally get self-tappers for that kind of stuff, but anyway, that just easily popped out.

**Dave Jones:** Then we can see the front panel board here for the SmartProbe interface things, so that'll be going off on its own ribbon cable, I would be assuming. Then we have our optical encoders, cuz one of their marketing claims is that uh these are not uh wiper type uh ones that wear out.

**Dave Jones:** These are optical or photo uh encoders, you know, they've got a LED and a phototransistor in there that, you know, detects the motion in either direction. So, there's no contacts to wear out inside these things.

**Dave Jones:** I'm not seeing a brand on it though, but um yeah, this is one of their uh one of their brags, and it has been a a sticking point um for several scope brands um over the years.

**Dave Jones:** And did Rigol actually cop some flak over the years for it? I'm not sure um but anyway, yeah, I think a few of the scope manufacturers have on the EEVblog forum and other places um for, you know, their their pots wear out.

**Dave Jones:** You use them so many times, and but these are optical. So, there's the interface, and interestingly, they do have a large cutout in here. That would be for the mixed uh signal connector, which is not there.

**Dave Jones:** It's not even populated on the board, so don't get your hopes up. Um no, this is not a mixed-signal scope. Doesn't have an arbitrary waveform gen, but interestingly, they do have uh cutouts there for two extra BNCs.

**Dave Jones:** That would be um you know, your arb gen output and whatnot. So, um interestingly, what I thought was um that might have been the LCD connector is not. You can see it actually goes to the front panel board here.

**Dave Jones:** So, they've got a ribbon, and this cable actually going through uh presumably for all of the uh contacts here. Um that could be individual power going over to power uh the active probes, and that power hypothesis makes sense cuz it goes over to here like this.

**Dave Jones:** And there's um like some switch mode uh chips in there. So, yeah, looks like that's active uh probe power. And the back of the interface board there, check that out.

**Dave Jones:** They've got uh polyswitch protection on all of the um like there's like four for each one. That is a lot. Uh I guess they expect a lot of goose, you know, idiot engineers short out active probes all the time.

**Dave Jones:** It's interesting how they've have to the effort to um like emboss these out from the other side. I guess that's to get a little bit more height for the connectors underneath.

**Dave Jones:** Let's go through the main PCB here and I am capturing this in 4K, so you will be able to see all the detail, but as I said, high-res photos are available on evblog.com if you want to have a squeeze.

**Dave Jones:** Now, this is the main PCB here and if we compare it with the Rigol 5000, which was quite a few years ago, but that was their new Phoenix chipset, I think it was at the time and they and they had like an eagle on there.

**Dave Jones:** This one has like a I don't know, it's some sort of flying bird, almost looks like a toucan or something. But this is supposed to be the Centaur chipset.

**Dave Jones:** So, anyway, this is the original Rigol 5000. It was very simplistic here and I don't believe I ever took these off cuz these were adhesive glue. So, yeah, we couldn't actually see what was under these, even the front end.

**Dave Jones:** I did take the cans off. Anyway, I was able to get the heat sinks off these cuz these weren't adhesive. So, we've got a Xilinx Artix 7 here. So, it's the main bad boy.

**Dave Jones:** So, all their new Ultra Vision 3 stuff is inside the Artix 7 and that's the main memory there. There is no extra memory on the bottom. I might show you the bottom of the board, but there's basically nothing of note on there at all.

**Dave Jones:** So, yeah, the that Artix 7 is not cheap. And if I'm right, Digikey puts that at about 205 US dollars 40 of quantity. So, we'll have a look at the main processor over here in a minute, but anyway, we have our bird here.

**Dave Jones:** Somebody had fun on the PCB, but this is really what we care about is the front end down here. So, actually take a closer up look at this. Now, as you can see, they're all identical.

**Dave Jones:** Um all of these is I don't think there's a single difference uh between them and they require substantial heat sinking. So, this is a new Rigol developed custom front end, but I believe this is the new center chip set upside down, so all the electrons are going to fall out, but that's the RT8847 or 4471, uh something like that.

**Dave Jones:** So, um yeah, a few hairy scary's on there. Um so, we've got two of those. So, one of those, obviously, uh shares the two channels and I believe that's the case.

**Dave Jones:** You you know, turn on channel one and channel two and it halves the sample rate because you've got your single ADC here like this. But, if you turn on channel one and channel um three like that or channel four, for example, you'll get the full sample rate on two channels.

**Dave Jones:** Most uh scopes work like that. And this in here, which is also uh heat sunk, this is actually you can tell by the uh component arrangement down here that this is the PLL.

**Dave Jones:** This is the clock generator PLL uh for this thing and that is a uh TI jobby. It's an LMK0482 ultra low noise clock jitter cleaner and clock jitter cleaner um with dual loop PLLs.

**Dave Jones:** So, it's got roomba function. Um and yeah, it's just there you go, uh femtosecond for you uh you know, clock aficionados. You can go for your life in that.

**Dave Jones:** Anyway, this does have a external 10 meg oscillator in. I don't know if it's this one down here, it's one of these. Um anyway, yeah, all this miscellaneous circuitry around here, this is for like internal uh it's got 10 MHz reference out, 10 MHz external reference in as well.

**Dave Jones:** But, I'm not actually seeing the oscillator there, though. So, I don't know what's doing there. And are these two LEDs? Are these two I don't know, I haven't powered it up without the back on it, but uh they look like there's there's two LEDs there.

**Dave Jones:** I mean, we can zoom in on that. That That That looks pretty leddy, doesn't it? So, this here is the Rigol 5000 front end like this. And as you can see, there's the BNC input.

**Dave Jones:** Then we've got our AC coupling switching relay here. We've just got one IC here, where whatever that is, I don't know. Could even be a discrete off-the-shelf chipset. And then all of your divider stuff around here.

**Dave Jones:** And then a just a differential pair output buggering off there. But the new one is actually substantially different. Let's have a look at the front end. Now, I've actually taken the bottom.

**Dave Jones:** So, this is the bottom side of the Well, the front. The bottom side of the actual PCB as such, but it's the BNC It's the business side of it.

**Dave Jones:** And this is the top here. But this 5000 series Rigol front end here, this is like a lower-end scope. You get it like sub at $1000 now. So, it's more fair to compare this one with the upcoming HDO 1000, which I'm getting in another week or two.

**Dave Jones:** And we'll take a look at that. So, I expect a simplistic front end like this. So, it's fair to compare it with the Rigol 7000 series, which I've done a teardown of that as well.

**Dave Jones:** And here we go. It's not rotated, unfortunately. Can I rotate? So, this is the 7000. You can see that we've got two relays here, which we didn't have on the 5000.

**Dave Jones:** And we've got the AC coupling relay here. That's the little Cosmo solar state jobby there. And it looks like I think I don't know if I saw this in the previous one, but it looks like this actually has a separate 50 ohm path like this and a separate 1 megaohm path.

**Dave Jones:** I might have missed that in the previous teardown, but have a look. But if we compare that with the new HDO 4000, here it is. It's relatively similar. We've got our two relays here.

**Dave Jones:** You'll note that they are exactly the same and it's interesting to note that a Chinese oscilloscope actually uses Japanese Fujitsu relays cuz some of the best relays are made in Japan.

**Dave Jones:** All the best stuffs are made in the Japan. They're actually a Fujitsu jobby. There you go. Ultra miniature relay. They're not shielded or anything like that, but they do actually specify you know, high frequency characteristic here.

**Dave Jones:** So, yeah, superior contact spring for high frequency characteristic. So, it complies with various standards, but they're not shielded relays. They're not like high frequency coaxial relays or anything fancy like that.

**Dave Jones:** So, this is a Remember, this is an 800 MHz front end. When I was a boy, 800 MHz front ends they didn't look like this. Yeah, it's just absolutely incredible.

**Dave Jones:** Anyway, we've got the new Rigol AC key. This is the RT1642 IQ. So, I There's no info on that at all. If somebody can get info on that, I doubt Rigol are going to give us anything.

**Dave Jones:** I don't know. I should ask maybe. Maybe they will. You know, they might give us a block diagram. They wouldn't give us more than the block diagram or anything.

**Dave Jones:** But, this is Rigol's secret weapon here and this is of course, this is not a 12-bit front end, but it would have the dynamic range and low noise capability cuz this is a low noise 12-bit well, 12 bits is the converter which is further up.

**Dave Jones:** It's not in the front end, but the front end has to have the low noise dynamic range for the to enable the 12-bit functionality. But, anyway, the So, so the relays are the same.

**Dave Jones:** So, it seems like this does have a separate 50 ohm path and a separate 1 megaohm path as people are speculating on the EVblog forum. You can see tiny little biddly traces there.

**Dave Jones:** They're really thin. Thin as. Anyway, if it goes through the relay like this if you AC or DC coupling, it doesn't matter. It goes through the relay and then it comes through like this and this is your AC path like that going into your divide-y amplifier differential driver front end chip.

**Dave Jones:** But the 50 ohm path actually is here. And I have actually measured this. This point here is actually physically connected through to If we draw this, the relay has three Please forgive my mouse, but it has three contacts like this.

**Dave Jones:** And this is the center pin, and then it flips between there or down here. Yeah, so that point is actually it it's not actually connected over to here. It's actually physically connected through to just the just the actual input pin here like this.

**Dave Jones:** So I've measured that. But the 50 ohm looks like this flips it on. It goes through here. I have measured that resistor there. Even though it doesn't say it on the top, that is a 50 ohm resistor.

**Dave Jones:** And then it goes through here. Once again, contact over to here. And this is your 50 ohm path. Here's another 50 ohm resistor here. And it goes up into there.

**Dave Jones:** So separate 50 ohm and 1 megaohm paths. Interesting. And once again, we've got all of our divider stuff like this. But this is Rigol's new secret weapon, which is their low noise front end.

**Dave Jones:** And as you saw in my previous video, this is not a 100 microvolt per division front end. It's only a 1 millivolt per division front end. Uh 100 200 500 microvolts are software magnified.

**Dave Jones:** But you can do that because you got the 12-bit converter. And anyway, people over on the EV blog forum I'll put the link down below. They have actually measured uh the noise and compared it with the Siglent and a Lecroy I think something like that.

**Dave Jones:** And yeah, the Rigol does a pretty decent job. The front end is pretty decently low noise especially for the cost. So yeah, it's it's really good. But this is an entire front end.

**Dave Jones:** I mean, you know, there's nothing doing over here. There's a whole bunch of bypassing and stuff. Looks like we have a filter there because you can tell it's got the extra extra contacts in the middle extra contacts in the middle there.

**Dave Jones:** You can see those. But apart from that like there's nothing else doing here. Sorry, I do have to my head's in the way. So let me move my head floating Dave head.

**Dave Jones:** There we go. But what I didn't show you down here this this image is flipped just to make it the same way around but this is a 4053 the classic 4053 jelly bean 4000 series CMOS analog switch is still used in everything.

**Dave Jones:** This is a 272. There was another one if you spotted up closely up on the main board. There's probably a whole bunch of these. The 272 is just a here it is.

**Dave Jones:** It's just a precision dual op-amp. It's nothing you know super special. So this would be doing the bias function which this has which is actually different to the offset.

**Dave Jones:** This actually I I got that wrong in the previous video. I just assumed that the bias in the front end settings was the offset but it's not. The actual physical offset where you move the waveform up and down.

**Dave Jones:** That's different to the DC bias. You can actually add a DC bias to the front end and I think I suspect that's what that's doing there. Yeah, but there's nothing else here doing at all.

**Dave Jones:** So it's that's an 800 meg front end. There's not much cost in that. I don't know what this A6 cost them. What sort of process they did that on?

**Dave Jones:** I don't know. If you know what sort of you know process they would have used for that thing. Obviously it's pretty high power because like it needs a pretty decent heat sink as you saw.

**Dave Jones:** Now as for getting the signal out you can see that there's actually two there's a different way there's actually two differential pairs coming out of here. So these two here and these two here.

**Dave Jones:** So there's two differential pairs coming out. So I don't know what the deal is and I can't see those on the bottom of the board. So I think they're actually going through that this is what this via stitching here's for, I suspect.

**Dave Jones:** Um so yeah, that's obviously I don't know. It's buggering off to the ADC. What is clearly right goals uh 4 gig sample per second ADC. So this is their center chipset here um that they, you know, claim.

**Dave Jones:** And the, you know, the UltraVision 3 technology whatever, that's just being run in the Arctic 7 FPGA. So this is the bottom of the board here. As you can see, like there's not much doing.

**Dave Jones:** You can see all the matched length traces. We've got the wiggle wiggle wiggle years in here. Check those out. So what's going on here is when you see both pairs like that take a snake, it means that they're matching the entire length of this pair with all the other pairs.

**Dave Jones:** They're length matching. But when you see a wiggle wiggle wiggle year in just one of the traces like that and down here as well, what they're doing there is matching one the one side of the differential pair with the other side of the differential pair.

**Dave Jones:** They're just matching between the two. So there's two different types of length matching and you can mix and match those two. They want to ensure that the, obviously this is coming out of the ADC.

**Dave Jones:** They want to ensure the data coming from the ADC is exactly the same matched timing going from both channels over to the FPGA here. Yeah, there's really nothing else on there.

**Dave Jones:** It's not very exciting, is it? So we want to look at the processor now. Here it is. It's a Rockchip RK3399. Hadn't heard of this before. Turns out it's actually um quite old.

**Dave Jones:** I've got a data sheet of 2018 here um and it's an arm processor. It's running the Android operating system. I think I showed that in the previous video. So yeah, it's got Cortex A72 quad core Cortex A53 with separate neon coprocessor.

**Dave Jones:** Uh yeah, it's got H264 265 decoders, 10 bit jobbies. Um 1080p, 30 frames per second, JPEG encoder decoder, um, pre image processors and stuff like that, embedded 3D GPU.

**Dave Jones:** Well, we don't need that. But yeah, there you go. For those playing along at home, um, it's got cryptography extensions and stuff. But yeah, I don't know. It's just they presumably chose it.

**Dave Jones:** I don't know. Because it's cheap or they have experience with the ecosystem or whatever. Um, you could choose any arm based processor here. But this one's, you know, it's it's at least 4 years old.

**Dave Jones:** It's not something new. And mysteriously, there are two buttons up here. I wonder what they do. They're not marked. Huh. And they're populated. So, what? That's interesting. But as I mentioned before, this is the power supply up here by the looks of it or at least part of that, um, for the connector that goes off to the active probes on the, uh, front end.

**Dave Jones:** That's like mostly, um, power there. They had all those wires going over. Don't know why. Um, just separate uh, fused ones. I don't know. And I don't know if this had, uh, HDMI output direct.

**Dave Jones:** Did it Did it? Yes, display interface, one HDMI port. There you go. So, I'm not sure what that one's doing. Let's look it up. Yeah, I'm not finding any ready info on that.

**Dave Jones:** So, like you can see that some of the pairs go direct from the Rockchip over the HDMI driver on there. But others, um, come from the 4C. So, I don't know what's doing there.

**Dave Jones:** Anyway, um, here's our touch, uh, sensor for the, uh, touch screen. And this is our, um, LCD ribbon cable. You can see those going on physically over onto the LCD over there.

**Dave Jones:** And basically, that's coming directly from the Rockchip over here. Now, I don't know how much memory is associated with that. You can decode the, uh, Micron part number over there as you can do for the, uh, FPGA, um, as well for the Micron memory.

**Dave Jones:** We've got a, uh, real-time battery, uh, backup. Yeah, so apart from like your auxiliary ins and outs here, there's nothing doing. There is a third unpopulated USB over here, so I don't know.

**Dave Jones:** But yeah, obviously like this board doesn't even have the options for the of what you saw with the connector cutouts on the front panel. There's no option for mixed signal waveform gen or anything like that.

**Dave Jones:** So, nothing doing there um at all, really. And one of these inputs over here was external trigger. Was that external trigger at the top? Anyway, we have a very nice populated JTAG over there for us.

**Dave Jones:** That's excellent. If you want to hack this thing, is there any like serial? Oh yeah, there you go. That could be a UART interface. Geez, the the real mouse operation's really laggy on my 4K when I'm capturing my 4K screen.

**Dave Jones:** Doesn't do this on the 1080. But anyway, this is the power input. It's just I think it's just 12 volts in for the whole thing, really. And and then you've got, you know, look, there's obviously like there's 0.9 volts here, is it?

**Dave Jones:** Yeah, there's 0.9 volts here. There's, you know, separate voltage for the CPU. There's 3.3 volts there. There's another CPU jobby over here. VDD center here. I assume that's the supply for the high-speed split transmission line termination.

**Dave Jones:** So, that'll be what that's for. There's another analog VGC management analog VCC. There's 1 volt over here. There's 2.5 volts over here. There's 1.8 volts here. There's another 1.8 volt generator here.

**Dave Jones:** There's like like it's crazy. In fact, what we don't see here inside the front end, we don't actually see a low noise supply. So, this looks switching like. What's going on here?

**Dave Jones:** Not seeing any major inductories. So, of course you wouldn't have a switching supply powering your ultra low noise front end here. Um you're just not going to do that, but I'm uh maybe five five five 5.2?

**Dave Jones:** Would they be uh low noise? They they might be powering the front end. Perhaps, but I would have expected to see one for each, and I didn't see it on the bottom.

**Dave Jones:** There is a three-pin jobby there, but I don't think that's doing it. So, yeah, they must be supplying them outside. So, that's that's surprising. Didn't expect that. There you go.

**Dave Jones:** That's it for the um teardown the Rigol HDO 4000. So, yeah, this is a it's a serious bit of kit. As I said, like the performance of the front end seems pretty good.

**Dave Jones:** Like it's not industry leading or anything, but for the price point, um it's pretty good. Now, for the HDO 1000 series upcoming, uh should be that should be on the uh on the plane in another week or two.

**Dave Jones:** Um so, we'll be able to tear on that, but as I said, I wouldn't expect uh the dual relay front end cuz this lower bandwidth. It's not 800 meg, but I suspect it might you because it is a 12-bit.

**Dave Jones:** Once again, it's 12-bit. So, it's going to be using the new Centauri chipset, and I suspect it will use the front end 800 MHz capable. Obviously, who knows? It might even go higher than that.

**Dave Jones:** We don't know. Um but yeah, I expect it to use the exact same chip, but as you uh saw in the Rigol 5000, I expect it to eliminate cuz it won't have 50 ohm, right?

**Dave Jones:** So, it won't it won't need the relays. It'll probably just eliminate both of those, and it'll just have the uh AC DC input ac dc, and um yeah, Bob's your uncle, but where is the power supply for each each of the front ends?

**Dave Jones:** I like ultra low noise. I would have expected like this bad these bad boys to have a a low noise um linear reg on each one of them. I don't know.

**Dave Jones:** Maybe it's built in. Anyway, it'll be interesting to compare this with the HDO 1000, a much cheaper one which starts at $699. This one starts at $2699, I think it is.

**Dave Jones:** Um, so it's significantly uh more expensive. Um, yeah, I don't know if they've like cheaped out on the uh processor over here. The Arctic 7, you know, you'll find that in any, you know, top-end oscilloscope these days, something like that.

**Dave Jones:** So, I don't think they've necessarily like they haven't really skimped there, I guess. Um, and they've developed their own custom um front end and new center chipset here. Or is center like both of these combined or something?

**Dave Jones:** That might be, you know, that might be the thing. But, yeah, it's like it's amazing how simple the front end 8 800 meg front end, come on. And it seems to be a pretty decent front end, low noise.

**Dave Jones:** 12-bit capable front end, 1 mV per division. Um, yeah, really quite amazing stuff. And this will have uh software bandwidth limiters in there as well, I suspect. Um, so yeah, there's probably like an I2C bus that comes into it or something that actually commands sends the commands uh to it cuz there's no separate uh PGA programmable gain amplifier.

**Dave Jones:** It's all in here. There's no separate differential uh driver. So, it's got a programmable gain amplifier, you know, with with the attenuator uh system and stuff. And it's got the differential uh driver output.

**Dave Jones:** Or it's probably got adjustable bandwidth limiters in there, 20 meg, 200 meg, 400 and 800 uh meg. Um, cuz I I think they'd be implementing those in the front end and not actually like digitally inside the FPGA.

**Dave Jones:** But, uh yeah, anyway, you can tell that from the um shape. I mean, uh everyone over on the EVBlog forums analyzing the uh shape of the noise curve and everything.

**Dave Jones:** Um, and you can actually tell a lot from the shape of the noise curve. It's rather interesting. Anyway, that's really cool. So, if you like that, please give it a big thumbs up and as always, you can discuss down below.

**Dave Jones:** I'll link the EV blog forum down below where people are discussing this bad boy and comparing the noise and analyzing doing performance analysis and all sorts of stuff. So, if you're interested in getting one of these and you're you know, curious to know how good like the 12-bit performance and front end is, there's people over there doing tests and comparisons and stuff.

**Dave Jones:** Really neat. And I'm impressed by the construction of this thing, too. It's you know, it's really good and and Rigol seem to have engineered this pretty well. So, I'm quite happy with it.

**Dave Jones:** And thanks to all the patrons who help pay for all the stuff that I do here. This is my full-time job and they help pay for it. So, that's always linked in down below and is very much appreciated as is the EVblog store.

**Dave Jones:** If you want to support, you can buy like a multimeter on the EVblog store. Clamp meter coming soon, by the way. So, I hope you enjoyed that and found it useful.

**Dave Jones:** Give it a big thumbs up, comment cuz that adds to the metrics and it you know, it really helps beat the algorithm. Catch you next time.
