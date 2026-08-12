---
video_id: KQF4UzLPpr0
title: EEVblog 1563 - New $389 12bit Rigol DHO800 Scope TEARDOWN
url: https://www.youtube.com/watch?v=KQF4UzLPpr0
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 41, "3": 52, "4": 69, "5": 80, "6": 92, "7": 108, "8": 114, "9": 127, "10": 138, "11": 149, "12": 160, "13": 172, "14": 185, "15": 196, "16": 213, "17": 221, "18": 230, "19": 243, "20": 252, "21": 260, "22": 270, "23": 284, "24": 293, "25": 310, "26": 324, "27": 343, "28": 350, "29": 367, "30": 380, "31": 389, "32": 400, "33": 409, "34": 419, "35": 433, "36": 444, "37": 456, "38": 468, "39": 485, "40": 494, "41": 509, "42": 518, "43": 534, "44": 544, "45": 555, "46": 566, "47": 579, "48": 592, "49": 609, "50": 619, "51": 639, "52": 649, "53": 660, "54": 675, "55": 692, "56": 703, "57": 720, "58": 730, "59": 741, "60": 756, "61": 768, "62": 786, "63": 802, "64": 822, "65": 835, "66": 857, "67": 873, "68": 887, "69": 906, "70": 923, "71": 935, "72": 947, "73": 963, "74": 972, "75": 990, "76": 1003, "77": 1015, "78": 1024, "79": 1037, "80": 1049, "81": 1064, "82": 1079, "83": 1089, "84": 1098, "85": 1109, "86": 1129, "87": 1143, "88": 1166, "89": 1176, "90": 1188, "91": 1200, "92": 1210, "93": 1224, "94": 1236, "95": 1250, "96": 1262, "97": 1272, "98": 1287, "99": 1298, "100": 1309, "101": 1323, "102": 1341, "103": 1352, "104": 1368, "105": 1382, "106": 1393, "107": 1405, "108": 1412, "109": 1422, "110": 1438, "111": 1458, "112": 1473, "113": 1489, "114": 1497, "115": 1516, "116": 1526, "117": 1538, "118": 1555, "119": 1571, "120": 1582, "121": 1594, "122": 1613, "123": 1623, "124": 1634, "125": 1645, "126": 1654, "127": 1667, "128": 1682, "129": 1690, "130": 1702, "131": 1717, "132": 1730, "133": 1743, "134": 1753, "135": 1765, "136": 1778}
---

**Dave Jones:** Hi, it's teardown time. We've got the new Rigol DHO814 DHO800 series 389 Yankee bucks for the four channel. We'll forget that the two channel actually exists. And this is the new one just released, which is the low-cost version of both the HDO, which is now called the DHO.

**Dave Jones:** I don't know. Whatever. The DHO1000 series and the 4000 series, which came out at almost the same time and I've done teardowns on both of those. So, basically the 4000 is the high-end high-performance high-bandwidth cost unit in the new center architecture, I think it is.

**Dave Jones:** And the 1000 series over here, this is just a lower cost version. As we saw in the teardown, it's basically the same except it's lacking an extra analog to digital converter.

**Dave Jones:** So, if you've got all four channels on, it, you know, drops it by a quarter of the two gigasample per second sample rate. But, it's basically a cheaper, but basically the hardware is pretty much the same apart from the lack of the smart probe interface over here, which you get on the 4000.

**Dave Jones:** But, anyway, that starts at 999 Yankee bucks for the four channel version. But, this cute little thing, look at it. Look at it. Look at it. It's gorgeous. It's got the VESA mount.

**Dave Jones:** It's got USB-C power. It's got HDMI output. I've just been experimenting with that today. And it seems to render at a higher resolution than the built-in 7-in touchscreen, which is 1024 by 600.

**Dave Jones:** So, it seems to output at the native resolution of your monitor, but I don't think at this stage actually get increased bits, but it does look really good. LAN and USB, they're all standard.

**Dave Jones:** It's got a fan in it, which is kind of a little bit whiny, high-pitched as you'd expect. Anyway, we're going to take a look at that. It's got the VESA mount, of course, absolutely fantastic.

**Dave Jones:** You have to mount on uh standoffs to get some airflow cooling in there perhaps. And it's got this integral handle. I guess uh you know, if you're going to mount it on a VESA mount, you probably don't want a handle flapping around in the breeze anyway.

**Dave Jones:** This is cute. Starts at 389 bucks for the four channel. We're going to get the two channel uh exist. So, let's do a teardown in 4K resolution. Thank you very much.

**Dave Jones:** High-res photos are as always available on evblog.com. And I have done a uh unboxing and first impressions of this video on this that's exclusively available over on my evblog.com website.

**Dave Jones:** So, check that out if you want to watch that video. I've also done a size comparison video on my evblog two channel. But anyway, let's go. Looks like we've got uh four screws here, two up there, and Bob's your uncle.

**Dave Jones:** The back should just lift off. Now, because this is USB-C powered, it does come with a uh Lite-On fully uh certified power brick. Not going to take that apart cuz that looks like it's ultrasonically welded, but it's got full certifications.

**Dave Jones:** It's a Lite-On. They're at least a reputable name. And because it's USB-C powered, it is uh technically isolated. I did actually measure 1 meg uh from the earth to the shield here.

**Dave Jones:** So, it's not directly uh connected. It's got a bleeder in there. And that's why they provide you with this handy-dandy little low impedance earth lead which goes onto the chassis in there.

**Dave Jones:** So, anyway, let's crack it open. So, we're talking a reduction from 999 US dollars uh for the 1000 series to 389 for this one. Both four channels. So, I expect that they've got uh some significant price reductions.

**Dave Jones:** I don't know if this will have the same Arctic 7 uh processor that we saw in the 1000 and the uh 4000. And whether or not it has the same 800 MHz bandwidth uh front end.

**Dave Jones:** So, we'll we'll find out. Oh, oh, almost forgot to void the warranty. Hang on. You can bet your ass I want to void that warranty. Oh, there we go.

**Dave Jones:** Oh, that's satisfying. All right, there's no nut on there, so this should just lift off. Come on, you can do it. Uh, that was caught there, wasn't it? Don't know.

**Dave Jones:** Anyway, uh, we're in. Check it out. Yeah, there's nothing else on the uh, bottom there. We do have our metal threaded inserts for the plastic here, but this thing only weighs 1.3 kilos.

**Dave Jones:** So, you don't really need an extra like metal base plate in there or anything like that. So, they they should be adequate for the uh, these amount. Yeah, it's not heavy at all.

**Dave Jones:** So, yeah, look, um, there's not much complexity in that uh, mold there, that's for sure. All right, off the bat, look at this. It's called the small sparrow. Oh, how cute.

**Dave Jones:** Right, cuz didn't the one have it I forget which specific bird they had silk screened onto the existing one, but it's the small sparrow. There you go. 230525 version 1.01 for those playing along at home.

**Dave Jones:** Do have some unpopulated memory. Now, you got to remember, this thing is also available as the DHO900 series. And the difference is is that the 900 series is higher bandwidth.

**Dave Jones:** This one only goes to 100 MHz, the 900 series goes to 100 250 MHz, I believe it is, and it has a logic analyzer option, which is really interesting cuz neither the 1000 nor the 4000 have a logic analyzer option.

**Dave Jones:** And a lot of people complained about that, but the little ultra baby DHO900 does. Anyway, um, yeah, lots of uh, power supply action happening over here. We've got Is that an SD card That's an SD card glued into there.

**Dave Jones:** Wow, look at that. They've Yeah, is that They've actually glued in that SD card. That's interesting. I might have to get that out and have a read. Um, can we just update it cuz this does run the Android operating system is it Is the operating system just on the SD card?

**Dave Jones:** Is that Is that a thing? I I don't know. Is that a way to reduce cost? I don't know. Anyway, we have some headers here and check it out.

**Dave Jones:** That is your logic analyzer option. The The footprint is there. It's unpopulated. There's a couple of more chips unpopulated down there, so I'm not sure what's doing there. Anyway, um they've got another connector over here which is unpopulated.

**Dave Jones:** That could be a production test. Oh, uh there's an extra BNC over here. That's interesting which goes up to another unpopulated chip up here. So, I does the DHO900 have an additional uh external trigger?

**Dave Jones:** No, like a reference out or something? I don't know, but this one's got an aux out. Oh, have a look at that whiny little uh fan in a minute.

**Dave Jones:** As I said, it's not like it's loud, but it's not annoyingly loud. Um it's not too horrific. Anyway, ooh, there we go. We're in. There's our front end there.

**Dave Jones:** One of the uh seal pads came off there. And oh yeah, there's our little small sparrow. Oh, isn't it cute? Small sparrow. Look. So, I guess yeah, it's a sparrow.

**Dave Jones:** Like unless anyone wants to uh contend that that's not a sparrow. Oh, we've got ourselves the rock chip here, but I like that they've got just one gigantic heat sink uh to cover everything.

**Dave Jones:** Aha, that looks different. That's not our Artix-7. So, we'll take a good look at that. That's how they got the cost down. So, maybe uh you know, performance update rate and stuff like that of this one is not going to be as grunty as the 1000 or 4000 series.

**Dave Jones:** But that's where I expected them to cut cost on the FPGA there cuz that was the Artix-7. It was a really expensive FPGA. So, they've obviously uh cut uh some corners there.

**Dave Jones:** There is some RAM missing as I said. Got the 1 ADC here which covers everything. We'll see if it's the same jobby. And we'll see if the uh Rigol um custom chip is the same on the front end, but they've only got the one relay there.

**Dave Jones:** So, it does look uh quite different. But it's crazy that like that whole thing is a 100 megahertz front end anyway. So, on the back of the heat sink here, we just got the larger seal pads going on to the die cast block.

**Dave Jones:** Very nice. The four front ends, that's the analog to digital converter, and then our main FPGA here, and then our Rockchip processor running the Android OS over here. There's one thing many people want to see, of course, and that's the USB-C interface.

**Dave Jones:** Yes, it is soldered directly down on the board. It's not on its own little daughter board. So, you know, if you wiggle, wiggle, wiggle, yeah, that, it could break off.

**Dave Jones:** So, that's one of the weak points of the design of this thing, but you know, for the cost reduction, I guess it's acceptable. But yeah, if you start ripping your pads off your USB-C interface there, you you know, you're you're going to be in a bit of a spot of bother anyway.

**Dave Jones:** So, there's no alternative way to power this. And they should have supplied a right-angle USB-C, so it could come out here like this, because this thing can actually sit very nicely flat.

**Dave Jones:** It's purposely designed to sit like nicely flat like that. So, yeah, please supply a right-angle USB-C. Come on. And maybe some sort of like cable clamping solution built into the back molding.

**Dave Jones:** That would have been nice, too. You know, you could put it in and you could like cable tie it in or something, so it takes the strain off the USB-C connector, especially if you're moving this thing around on like a VESA mount arm or something like that.

**Dave Jones:** You don't want the cable just to get snagged or whatever, and oops. So, I've taken all the screws off there, and it's doesn't seem to like want to pop out.

**Dave Jones:** Okay, so that's the front panel power button. That seems to go to the main board. Is everything connected to the main board? The other side doesn't want to come out.

**Dave Jones:** So, I'm thinking maybe I have to undo the chassis first, and I don't know. Is there a screw from the other side as well? All right, so I've gotten all of the screws out, including the chassis ones and there you go.

**Dave Jones:** Chassis starting to come out. The button is certainly on the front, although I don't think the I think there's a separate board in there is there for the Oh, no, that there we go.

**Dave Jones:** Got it. Got it. So yeah, there we go. There's board to board interconnect there for your display interface. So that's a obviously display interface capacitive touch there. I'll take I won't bother taking you through those photos available on evblog.com, but there you go.

**Dave Jones:** That's a nice solution. Duh, obviously. Yeah, we had to get that out first to get the nuts off and then the PCB will lift out. No worries, but anyway, look, we do have the chassis cutout.

**Dave Jones:** Of course you're going to reuse the chassis between the 800 and the 900 series. So it's all populated. So whether or not as I said in the previous video available on evblog.com, you somebody on the forum has apparently hacked this 800 series to a 900 series, but I don't know if it enables the logic analyzer.

**Dave Jones:** Apparently this just goes off. We'll see if there's any missing chips, but apparently I think it might just go off to the I think which is a Xilinx Zynq FPGA.

**Dave Jones:** Anyway, power button's on the main board and just some attention to detail with the RFI conductive sponge going between the chassis and the metal back in of the LCD as well.

**Dave Jones:** Nice. And there's the metal work for you metal work aficionados. Metal threaded insert studs in there. So that's very nice. Look at that. But basically, yeah, there's that piece and then there's the two then there's the PCB and then there's the two other pieces and Bob's your uncle.

**Dave Jones:** Oh, and the heat sink of course and and Bob's your uncle. Geez, they're really gotten this production stuff down pat, haven't they? The plastic injection molding experts will have to weigh in on this, but to me this seems like a relatively um plastic molding.

**Dave Jones:** I mean, you've got two major plastic molded pieces and that's it for this entire design plus the one little formed uh metal there for that and like Bob's your uncle.

**Dave Jones:** So, you can really see how they're uh cutting the production cost on this. It's It's really nice. There's no you know, minimal of extra stuff required. They've even integrated the uh the little mounting clips there on that uh on that one-piece mold, but yet two plastic molds for this whole thing.

**Dave Jones:** But, this mold must be different between the 800 and the 900 because there is no cutout in there. And we'll take a look at the PCB a minute. I think that's really curious.

**Dave Jones:** Hmm. And there's the backside there and there's not much on the front end. Just has a few uh passives there and an extra chip that could be a 595 or something.

**Dave Jones:** And there's that for the uh that location seems to be for the uh auxiliary outputs uh here, but um yeah, all the USB uh stuff and HDMI and all that, that's all on the top side there and that's looks like it's all handled by the Rockchip.

**Dave Jones:** I do believe it's all internal to the Rockchip. I think that is the same one from memory, but yeah, I see something really interesting down here. Anyway, uh let's go over to the video tape and we'll have a closer look.

**Dave Jones:** All right, let's compare with the HDO 1000 and as I've shown in the previous video, the HDO 1000 is basically identical to the HDO 4000. So, here's our new board and obviously, the big change here is the Zynq uh processor as you find in practically every modern scope has the Xilinx Zynq in there.

**Dave Jones:** Um and this one has the Artix-7, of course. So, once I have not used this in anger yet, so I don't know about like the uh you know, the grunt speed, the pro waveform update rate, and all the rest of it, okay?

**Dave Jones:** But, that's all being run inside the Artix-7. The new architecture's all uh done inside there. And then the HDO 1000 had a single analog to digital converter as opposed to dual ones on the HDO 4000 and the new HDO 800 is upside down all the electrons are going to fall out.

**Dave Jones:** RT88471. Let's see. That looks like 88471. I've got higher higher res photos are always available on my Flickr account by the way which is on my EV also LinkedIn on EVblog.com.

**Dave Jones:** So it's exactly the same analog to digital converter as used in the other ones but you only get the one. So you turn on all four channels and they all feed in and you can actually see here the trace of the differential pair output here trace length matched here so that they're all equal timing going into the analog to digital converter there.

**Dave Jones:** So this one is 1.25 gig sample per second so you can divide that by four if you turn on all four channels there. And once again because there's only one it makes no difference you can't do that trick of like using channel one and using channel three as you can on some other scopes that have two analog to digital converters.

**Dave Jones:** This is one sharing all four channels and that's how they reduce the cost there and there. That's the main and the Rockchip AK3399 is it? I believe that is the same.

**Dave Jones:** Yeah, there it is Rockchip 3399 it's just rotated um layout uh reasons but exactly the same processor that's running the Android operating system but we did not find an SD card anywhere on the HDO 1000 or the 4000 or DHO renamed it.

**Dave Jones:** So yeah, I'm going to look at the contents of that card in a minute. So we've got some memory missing here. There's nothing on the bottom side. I'd say that could be not only does the Uh, the 900 model have more sample memory don't quite I think it does.

**Dave Jones:** Um, but also doesn't have the uh, logic analyzer. So, I figure if you're going to put the if you're going to try and hack this to include the logic analyzer, um, you might have find you have to install those chips.

**Dave Jones:** Now, interestingly, look, they've populated the termination resistors here. Why would you do you know, if you're reducing your bill of material I know they don't cost anything, but you know, it's all production time.

**Dave Jones:** It's all you know, like you've got to change your production reels faster and stuff like that. The more like they're just absolutely wasted, right? But they populate them, which you can see if we look at the bottom side of the board, they've also done down here for the logic analyzer.

**Dave Jones:** Here's the logic analyzer, which is not an option on the 800. It doesn't physically have the cutout on the front, but the footprints are the layout's the same. They've included the series resistors here.

**Dave Jones:** They've populated those, right? They don't those don't come for free. Why would you not just simply remove those from your bill of materials? I don't get it. So, it's almost as if like conspiracy theory, they want you to hack this thing and but you'd have to dremel out the front cut like a hole in the front case, but yeah, no worries.

**Dave Jones:** Um, you can see that uh, yeah, there's no um, extra memory like on the bottom side here. Here's that memory. Look, like look, look. They've populated. They've populated all of the bypass caps.

**Dave Jones:** Count them. Count them, right? I know they you know, 0.1 0.1 something 0.1 I don't think they they all add up. Look, for the unpopulated chips, those extra memory chips.

**Dave Jones:** So, all we have to do is get a photo of the um, 9000. Someone will do a teardown. We'll be able to find out what chips they are. You presumably can buy them and you can looks you know, they're BGA.

**Dave Jones:** You know, you've got to be careful, but you might be able to like reflow those on there and maybe everything's good to go for your to convert this into a a logic analyzer.

**Dave Jones:** Now, these ones down here, once again, all this stuff is populated down here and these two chips are not. But, they don't they seem like power supply related. So, I'm not sure what's going on there.

**Dave Jones:** So, that's interesting. It'll be interesting once we get a photo of the DHO900. But, yeah, all the memory's installed for the processor, so that's not a problem. Anyway, I know you all want to see the front end.

**Dave Jones:** And uh sorry, stupid Drawboard PDF is the software I'm using here. Doesn't let me scroll in the vertical direction like that. Um yeah, right. Here's the Here's the I think this is the 4000, this is the 1000, and this is the 800.

**Dave Jones:** But, it's basically missing the extra relay here cuz it doesn't have 50 ohm termination. So, they've saved some cost there. But, look, the chipset's the same. It's the RT1642IQ.

**Dave Jones:** It's exactly the same chipset. In fact, there's only a couple of weeks difference in the manufacturer there. Look at that. Um So, yeah, this is Rigol's a custom front end chip.

**Dave Jones:** And it looks Yeah, the layout's a bit different with the parts around here, but that's neither here nor there. This chip is capable of 800 MHz. So, in theory, um this front end is capable of 800 MHz.

**Dave Jones:** So, there's absolutely no doubt in my mind unless it's like software limited software bandwidth limited, of course, internally it's got the bandwidth software bandwidth limit filters built in. They just send a serial command to it and it's the Yeah, it's got a programmable gain amplifier in here and they end programmable filters as well.

**Dave Jones:** So, they can actually you can set that. I don't think you would have to hardware hack any filter you know, any external components. So, I think you just you know, you upgrade it to the DHO900, and I think I think you're going to get that 250 meg bandwidth.

**Dave Jones:** But, I think it's capable of more. You know, unless there's like layout another tweaking reasons, I'm I'm not seeing it. It's the same relay, it's the same Cosmo. Relay down here that shorts out the AC coupling and stuff, so yeah, I think it's capable of 800 meg.

**Dave Jones:** It's just a software limitation. But it makes sense once you spend all the NRE, the non-recurring engineering cost designing the custom ASIC for this, you you just use it in absolutely everything.

**Dave Jones:** You use it in your 300 Well, it's minimum $329 retail scope for the two-channel right up to your multi-thousand dollar, you know, 4000 series. Just the same chip and it's capable of 800 meg.

**Dave Jones:** No worries. And on the bottom of the front end here, yeah, we've just got a 4053 mux there, but yeah, there's basically nothing doing there at all. There's no extra.

**Dave Jones:** But yeah, that that logic analyzer there, it just goes straight into the zinc FPGA. Just got a series resistor here and Bob's your uncle, right? So there's no extra like level uh stuff.

**Dave Jones:** It's just going straight in. But the FPGA, they might have a selectable, you know, a threshold front end, you know, 3.3, 1.8, something like that. So I don't know what the DHO900 is capable of in in that regard, but it's just yeah, basically digital straight in.

**Dave Jones:** No worries, man. There's not even any protection, is there? Yeah, nah. It's just It's just nothing on top here. So there you go, you can get some of the pin outs there.

**Dave Jones:** But yeah, people are making their own do-it-yourself probes for the Rigol scopes, of course, and they seem to work just fine. So we've got our small sparrow there, but like there's not much else to really show you on here apart from this jumper link here.

**Dave Jones:** This is our flash and JTAG. I might actually solder in another like a header in there cuz that's a transmit and receive, so I might put that on the serial packet sniffer.

**Dave Jones:** But over here, right up the top here, they've once again got ground transmit and receive. I don't know if that's a duplicate one or a different one. And that one I can't see it.

**Dave Jones:** That might be a JTAG. The only other interesting thing up here is the arbitrary waveform generator, which is optional on the DHO 900 and it's going it looks like it there's a just a this is just be a buffer chip.

**Dave Jones:** This is just be a buffer driver. I mean, looks like this will be the input here, this pin, and this is the output. So, that's very common. You just have a 50 ohm buffer driver there.

**Dave Jones:** But where's the other circuitry for the arb? I mean, this is it over here. But like there's no DAC or anything. So, is that a where is it where is it coming from?

**Dave Jones:** Is there just an MPM 36 30 step down converter and they've a interestingly they've got an integrated inductor. If you're wondering where's the magnetics? Yeah, they're they're actually integrated in there.

**Dave Jones:** So, they're just some step down converters. So, so there's nothing else really doing on this board. The soft power over here, that's probably part of that there. I noticed that when I put it through a power meter and only limited to 5 volts, the LED would still light up and it would turn green.

**Dave Jones:** But then 5 volts was not enough to power this thing. It needed to negotiate over USB-C for the 15 volts. And but it's still the LED still came on and operated.

**Dave Jones:** On and off when I limited it to 5 volts. So, that was interesting. Yeah, but that's all she wrote there on the new HDO 800. They've really got that price down with the zinc processor, the 180C.

**Dave Jones:** They're just reusing the front end, eliminating the 50 ohms, you know, having optimized assembly procedures and stuff like that. But having the extra components on there for the all the bypass caps and everything for those chips.

**Dave Jones:** That's just That's hilarious. Like I I just could No. No. I couldn't I couldn't allow that. I could not allow that. As an engineer, I could not allow that in production.

**Dave Jones:** To put all this termination stuff on here and and just not have the chips populated. Oh god, no. The humanity. Anyway, um that's a look at the board there.

**Dave Jones:** There's not much else uh to tell you. So, I'll go have a sniff of these things and I'll see what we get in the SD card. All right, we have a serial terminal uh connected up here.

**Dave Jones:** So, I'm getting uh transmit, receive, ground, and uh power cuz I'm just using one of these uh isolated uh micro art um came in the mail bag while back.

**Dave Jones:** Um it's one of several that I've got. Uh usually 115,000 baud. So, eight-in-one standard. It's even 9,600 or, you know, 115k. Sometimes it's like 19.6 or something weird like that, but let's switch it on.

**Dave Jones:** Bop. Whoa. Why'd it vanish? There you are. There you are. I don't know why that vanished. We're in. So, I'll dump this on the EV blog uh forum. So, it's Yeah, it's the Rockchip uh setting up ports, HDMI, I squared C bus driver.

**Dave Jones:** Like I said, I think it actually detects the monitor you've got connected and selects the appropriate and scales the appropriate output resolution. Now, whether or not the 12-bit data is actually mapped into the screen, haven't confirmed that yet.

**Dave Jones:** Maybe not. But, it seems to scale the interface, which makes sense because this is only a 1,024 by 600 display. Then, it's got to map it to bigger displays and the this same firmware would be used on the other higher-end scopes, which have higher resolution screens.

**Dave Jones:** So, it makes sense that they would build the firmware to scale, at least the user interface, cuz the user interface looks great. I've got it I've had it on a 4K external monitor.

**Dave Jones:** Looks Looks really schmick. It doesn't look like 1024 by 600. So, can we get in? Rigol prompt. Help. Games. Nope. Joshua. Damn. Anyway, I got no idea what I'm doing here.

**Dave Jones:** So, that's one up in this corner. There's also this one over here. I did solder a header in there. All right, so I've got that hooked up. Unfortunately, the VCC's over here, so I have to bring that wire over.

**Dave Jones:** If you've got a non-isolated one, you don't need the VCC, of course. There we go. Hey! Xilinx first stage bootloader. Silicon version 3.1 boot mode is QSPI. Okay, so that's a Well, that's the flash.

**Dave Jones:** Xilinx first stage bootloader. Release 2020. Boom. Boom. Once again, this is all stuff that I will dump I will dump this as well over on the EVBlog forums. And back to the boot code here, we do actually get an accurate boot time, 47.4 seconds.

**Dave Jones:** Now, I was able to get this SD card out from the glue. It's a 32 gig Lexar jobby. I was not able to read it even with like a Linux reader program or whatever, but it just does not identify under win uh Windows or a Linux reader.

**Dave Jones:** Maybe it's something else. Maybe it doesn't actually contain anything. Maybe it's designed to use as just cheap ass memory or something, perhaps that's non-critical, but I I don't know.

**Dave Jones:** Anyway, I'm going to try and boot it um without having that. And unfortunately, I'm going to have to stick something in the front because I forgot to put the button back in before I screwed the board down.

**Dave Jones:** Doh! Well, sure enough, there's no Rigol boot message without the card. So, um it booted fine before with the card. So, yeah, I I'm presuming it contains the OS, I guess, or some needed stuff required for the boot uh process.

**Dave Jones:** So, yeah, it's on there. Um I don't know. I'm going to have to uh uh get the nerds on the forum to try and uh help me with that one cuz I can't read the card.

**Dave Jones:** Maybe I'll try a Linux machine. And the card's going back in, and it boots up straight away to the splash screen. Yeah, the boot is slow. It's about 45 46 seconds, something like that.

**Dave Jones:** Mm. So, there you have it. That's the new DHO 800, and I'll show you the power consumption there. So, it negotiates uh the 15 V output, 2.4 amp. So, uh just over 35 W there.

**Dave Jones:** Um that's with like it doesn't matter if you have all four channels and uh the math on, it's basically uh the same uh power consumption. So, 35 odd watts there.

**Dave Jones:** If you want to power it from a battery pack, which you could, of course, you could uh design your own custom mount, put it on a V on the VESA mount on the back, and have the cable running over, and you could actually power this uh from battery.

**Dave Jones:** But, offhand, I haven't seen that style arrangement for that fan before, but you might want to replace the fan with a more silent solution. But, I don't know if you're going to get much better because, yeah, it's right near all these, and I don't know what you can do there.

**Dave Jones:** So, anyway, it sucks air in uh from the back uh through the VESA mount, and then comes out through all the fins out here like this, and then out the vents out the side.

**Dave Jones:** So, it's a little bit noticeable if it's a quiet if the lab's uh completely quiet, I can hear it from halfway across the lab uh for example. So, it's a little bit whiny.

**Dave Jones:** It's certainly not the worst um I've heard though. Anyway, this is a hugely interesting develop in this oscilloscope scene. I mean, a 12-bit four-channel scope for 389 Yankee bucks.

**Dave Jones:** As I said, forget about the uh two-channel with the possibility of hacking uh this thing. Unfortunately, like if you go to too high a bandwidth, it doesn't have the sample rate in there with that one ADC and the 1.25 gig sample per second.

**Dave Jones:** Once you turn on the four channels, uh you know, you might be able to bandwidth hack it and then get extra bandwidth on what I say one channel for example, but you turn on more and that sample rate's just not quite going to cut the mustard.

**Dave Jones:** I'm looking forward to doing a full review of this thing and playing around with this a lot more because well, this might have changed the oscilloscope, the entry-level oscilloscope landscape.

**Dave Jones:** So, hats off to Rigol. I think they've done something really special and it's going to drive the industry here. I mean, it's you know, 8-bit might be dead. I don't know.

**Dave Jones:** At least at this entry-level price point anyway, but anyway, thoughts and comments down below and if you like that video, please give it a big thumbs up and as always discuss down below EVblog forum, high-res pictures over on EVblog.com.

**Dave Jones:** As also, there's I've already done the unboxing and first impressions video. That's over on exclusively on EVblog.com. Catch you next time.
