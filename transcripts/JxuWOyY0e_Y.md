---
video_id: JxuWOyY0e_Y
title: EEVblog 1761 - Micsig MHO14 Tablet Oscilloscope TEARDOWN
url: https://www.youtube.com/watch?v=JxuWOyY0e_Y
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 33, "3": 46, "4": 61, "5": 73, "6": 90, "7": 107, "8": 123, "9": 133, "10": 145, "11": 152, "12": 168, "13": 178, "14": 188, "15": 199, "16": 208, "17": 225, "18": 238, "19": 251, "20": 262, "21": 281, "22": 294, "23": 306, "24": 322, "25": 330, "26": 347, "27": 365, "28": 375, "29": 385, "30": 400, "31": 415, "32": 421, "33": 438, "34": 449, "35": 463, "36": 472, "37": 491, "38": 509, "39": 521, "40": 539, "41": 556, "42": 569, "43": 588, "44": 606, "45": 621, "46": 636, "47": 653, "48": 664, "49": 679, "50": 692, "51": 703, "52": 719, "53": 734, "54": 744, "55": 753, "56": 764, "57": 780, "58": 794, "59": 817, "60": 830, "61": 846, "62": 857, "63": 874, "64": 893, "65": 907, "66": 916, "67": 927, "68": 940, "69": 957, "70": 973, "71": 983, "72": 999, "73": 1017, "74": 1027, "75": 1043, "76": 1053, "77": 1067, "78": 1080, "79": 1092, "80": 1108, "81": 1128, "82": 1144, "83": 1160, "84": 1170, "85": 1184, "86": 1199, "87": 1223, "88": 1236, "89": 1256, "90": 1273, "91": 1288, "92": 1301, "93": 1327, "94": 1340, "95": 1354, "96": 1369, "97": 1380, "98": 1390, "99": 1398, "100": 1412, "101": 1425, "102": 1437, "103": 1449, "104": 1461, "105": 1471, "106": 1490, "107": 1501, "108": 1515, "109": 1531, "110": 1551, "111": 1562, "112": 1570, "113": 1583, "114": 1596, "115": 1603, "116": 1616, "117": 1628, "118": 1641, "119": 1654, "120": 1664, "121": 1674, "122": 1686, "123": 1693, "124": 1704, "125": 1714, "126": 1722, "127": 1733, "128": 1746, "129": 1763, "130": 1770}
---

**Dave Jones:** Hi, it's a silly scope tear down time. I've had this one for a while, so sorry, but thank you very much to Mixi for sending this one in. It's the MHO 1 series portable oscilloscope.

**Dave Jones:** Yes, internal rechargeable battery, four channels, 200 MHz, and it's got a building multimeter, although it's available without the building multimeter. It's the MHO 1 series. In this particular case, the MHO 14 cuz it's four channels, and if you add an N on the end of the part number, it doesn't come with the multimeter, which is a 60,000 count job.

**Dave Jones:** Now, this is actually not new. It's been discussed on the EV blog forum since December 2024. So, like it's more than a year and a half, but they've just released in March, I think, this new variant of it.

**Dave Jones:** They haven't changed the part number at all, but apparently they had some issues with the design of the multimeter. I think it was originally 20,000 count, now it's 60,000 count multimeter, and there were some other issues with it as well.

**Dave Jones:** So, this is the latest build of it. So, we'll do a teardown of this thing. Have to do a review of a separate video, but anyway, anyway, it's a very nice rugged feeling bit of kit.

**Dave Jones:** I love the carry strap on here. Feels really rugged and really does feel like very nice and like it could probably take some knocks. We've got a 1280 by 800 touchscreen on it, four channels, and I like the grouping of the controls here.

**Dave Jones:** Anyway, that's for a future video. It's a very nice bit of kit. Under here, we have rubber baby buggy bumper protection for Yes, that is the fuse for our multimeter, and it's a 10 amp like automotive fuse in there.

**Dave Jones:** So, none of that HRC high rupture capacity rubbish. So, yeah, right off the bat, Uh, your multimeter's not going to meet any uh particular safety standard with um just an automotive uh fuse like that.

**Dave Jones:** So, it's a fail and leave it in the comments down below. Oh, oh, I think we just turned it on. Oops. Uh, there you go. Sorry, it's on. Uh, that ruined the don't turn it on, take it apart thing.

**Dave Jones:** Um, anyway, let us know in the comments down below what you uh think about having a multimeter in an oscilloscope like this. I'm I'm not sold on it. I, you know, uh horses for courses, right?

**Dave Jones:** Uh jack of all trades, masters of none, but yeah, you can actually buy it without the multimeter. If you totally don't want it, you can save a few bucks.

**Dave Jones:** Um, this is a sub even with the 200 MHz model. It's also available as a 100 MHz version, 1 gig sample uh per second, 12-bit, of course. Uh, these days everyone's uh running 12-bit ADCs, and we're talking um sub $1,000 street price.

**Dave Jones:** So, you know, very affordable for what you get. But, as I said, um it's quite rugged. It's uh about 3.1 uh cm thick here. Weighs a decent amount. Let me weigh it.

**Dave Jones:** That was 1.73 kilos, and uh yeah, you can like get different apps for it. I think you can like download electronic tools and oscilloscopes. Anyway, not a review. We care about um what it's like inside.

**Dave Jones:** So, let's go. It does have a fan on the back. Uh, that was just on, and when it's on, it's a bit annoying, but it's just switched off, and the oscilloscope is actually on at the moment.

**Dave Jones:** So, when that switch is on, I don't know. Anyway, uh when I first got this thing, I could not get the damn thing to boot because there's a power lock here.

**Dave Jones:** Um, this is an interlock. It's actually quite smart because when they ship the thing, you don't want it to um accidentally like switch on during handling and shipment. So, this is actually a power override, and I thought it was just a manual like a like a momentary push button.

**Dave Jones:** It's not. It's a physical latching switch like that. A latching tactile switch, which you have to push in to enable this thing to actually uh switch on. So, um yeah, that just confused me.

**Dave Jones:** Anyway, external uh DC power here, but it can charge from the included uh USB-C as well. It's got all the requisite uh LANs, um LXI, I believe, and also HDMI output.

**Dave Jones:** So, unfortunately, it doesn't have a removable battery. Previous MixSig scopes have, I believe, but uh this one doesn't. So, and yeah, anyway, it's neither here nor there as long as you can get in easy.

**Dave Jones:** There's a bunch of uh Phillips screws here. No wuckers. Yes, we do want to void the warranty. No wuckers. Let's get in there. And it is voided. Awesome. So, right off the bat, this is nice.

**Dave Jones:** These are metal uh threaded inserts, which go into the uh metal chassis inside here. So, you can see the shielding through the back. And that's why it uh it weighs a bit.

**Dave Jones:** No sneaky screws. Nope. All right. Is it spudger time? How do we how do we get this sucker apart? Aha, it looks like the rubber baby buggy bumper has to come off.

**Dave Jones:** And yeah. All right. Well, that's some extra drop protection, anyway. Uh Oh, yeah. Yep. Yep. There we go. It's actually a full full-on holster. Neat. But the handle is stuck in there.

**Dave Jones:** So, no worries, but that is that is pretty neat. Makes it feel really good. Trust me. Um feels like a solid BIT OF KIT. OH, OKAY. YEAH, there you go.

**Dave Jones:** Metal pins in there for the strap. That's very nice. I like that. I was wondering how that would uh attach in there. Yeah, that's uh very thoughtful design. So, let's open it.

**Dave Jones:** And we're in like Flynn. Just have to disconnect the uh the battery. Well, this is interesting. Here's the They've got the heat sink back here with uh integrated um heat sink protrusions, which then go onto the main uh chips down here, which we'll take a look at.

**Dave Jones:** So, they've engineered the thickness of those to uh just go straight onto the chips. Very nice. Um why they've used heat sink compound on seal pads, I don't know.

**Dave Jones:** The whole idea of seal pads, which is a trademark, but a thermal pad, is that you don't have to add heat sink compound. You just need the thermal pad.

**Dave Jones:** So, uh I don't know. Anyway, it looks like they have the heat sink there, and there's our fan in there, which then will push the I probably should try and get that out, but that's going to push the air across almost certainly the heat sink fins on here.

**Dave Jones:** Um and it looks quite good. The mounts for the uh feet look very good. They've got like metal pins going through there. They're plastic feet, but uh metal pins going into uh yeah, yeah, probably going into plastic under there.

**Dave Jones:** But anyway, might have take all that off. So, the battery is integrated under here somewhere, which is a bit of a bummer. Would have liked to have seen a replaceable battery.

**Dave Jones:** That would have been much nicer, but uh you get what you get, and you don't get upset. Got one gigantic board here. As always, this video's in 4K, my teardowns, and I'll also put high res teardown photos on eevblog.com as well.

**Dave Jones:** Well, it looks like we can get those metal cans off uh pretty easy. Wow, look at the gigantic screws in there. What's What's doing? Um but I I'm very impressed.

**Dave Jones:** Anyway, this is Mixig's uh they claim sixth generation oscilloscope, so like portable oscilloscope. So, yeah, they've been at this a long time. They're you know, one of the best makers of uh portable scopes on the market.

**Dave Jones:** They know what they're doing. And from a design point of view, it's excellent. Of course, here is our multimeter. We'll look at that more up close. It's got these are It's all optical isolated here.

**Dave Jones:** That looks like the DC-to-DC converter for it. And look, it's all shielded. They've got routed slots under the isolators. Everything's beautiful. I Yeah, thoroughly impressed. And there's some pogo pins up there for that connects over to our battery board over there.

**Dave Jones:** Tell you what, this retaining clip here for the shields for the front end, it's a rather impressive implementation with these slot cutouts and a spring here. So, that's That's really neat.

**Dave Jones:** Wow. So, what you do is you push down on that and then slide it across and it should pop out of that slot. Uh, yeah. There you go. It's a bit hard to do it when the camera's in the way.

**Dave Jones:** And a really nice design touch here is this insulating plastic sheet on top of the metal. That's designed to overlay the multimeter section. And the multimeter section with the banana plugs has little rubber plugs on the insulating rubber plugs on the back of it.

**Dave Jones:** So, there's actually dual insulation with the rubber plug and the plastic sheet here to the metal at the back. Um, that's really great. I like that. And you can see this is a chunky just die-cast metal case on this thing.

**Dave Jones:** It's very impressive. And all the screws, of course, as I said, metal threaded inserts directly into the die-cast. No wonder this thing weighs like 1.7 kilos, which isn't particularly heavy, but it's why it feels robust and solid.

**Dave Jones:** I'm very impressed. There's inside the back end of it. Once again, they've got metal threaded inserts into the plastic back in here. That's very nice. Oh, there's the Oh, yep, yep, the fins are the right direction so that the airflow goes through here like this and doesn't block it.

**Dave Jones:** That'll be a trap for young players. So, that's really nice and they've put little springs on there, too. Little springs. To put pressure down onto the chips. Oh, so they didn't have to engineer that to be a perfect fit.

**Dave Jones:** They engineered it so it puts a bit of downward pressure on with the seal pads. That is beautiful. Somebody was thinking about that. Hats off to the design engineer for engineering the springs in there to bring that down.

**Dave Jones:** That's great. Hats off. For you fan aficionados, as I said, the air comes in here and gets blown out the back like that. And the battery, the manufacturer is Newozi.

**Dave Jones:** 20,000 milliamp hour, 7.3 volts, 74 watt hour jobby. So, you know, pretty relatively easy to replace that, I guess, if you can get like a similar size and shape kind of thing with just the interface like this and that looks like it's just a temp sensor, probably.

**Dave Jones:** I've actually shot this bit of the video at the end and a spoiler alert, I was actually confused over why on the PCB there's an audio amplifier and it's near the pogo pins which connect to here.

**Dave Jones:** So, not only have they got this as the fan coming through here, but also they've actually got a speaker. They've actually got a speaker in this thing. A dual 2 and 1/2 watt speaker.

**Dave Jones:** Um, why? I don't know, but presumably, I don't know. You can play Doom on this thing and have like the full soundtrack. So, let me take some high-res photos and we'll go over to Dave head.

**Dave Jones:** More detailed look at the PCB. Let's go in 4K capture resolution of course. So yeah, as I said, one big giant board construction. It's all got the front end on here.

**Dave Jones:** It's got the multimeter. Everything's integrated on here. It's probably got some double-sided loaded. Almost certainly does bypass caps for various things. But it's neither here nor there. Don't really have to get the board out to see that.

**Dave Jones:** And of course the beautiful diecast alloy case here. Absolutely fantastic. And surprise, surprise, not a Xilinx Zynq main FPGA up here which is does all the capture engine. It's a next C7Z020.

**Dave Jones:** You can go look that up if you're playing along at home. This is obviously the sample memory. There could be more on the other side there, but I'm not going to be bothered decoding the part numbers there.

**Dave Jones:** You can do that yourself if you really wanted to. I don't know. Might even be able to read the barcode. Anyway, so that's sample memory. That's going to have bypassing on the bottom of it.

**Dave Jones:** So as I said, yeah, there's going to be like bypassing. This is a double-sided load cuz there's going to be a whole bunch of bypassing here. We've got bypassing out here, but you're typically going to get also bypassing on the bottom of your FPGA here.

**Dave Jones:** And once again, no surprises. The Rockchip, the RK3568. We've seen that in other oscilloscope teardowns. It seems to be like the go-to one for quite a few manufacturers. And this is interesting up here.

**Dave Jones:** I didn't know Rockchip did a DC-to-DC converter cuz that's obvious. Don't even have to look up the number because you can just tell by the surrounding circuitry with the inductors here like this and you know, some big fatty traces running out here.

**Dave Jones:** This is obviously a multi-channel DC-to-DC or multi-phase DC-to-DC converter here. Specifically to presumably power of Zynq uh, processor and or the, uh, Rockchip over here. Cuz these high-end devices, they all need very low power rails, you know, 1.2 volts, 0.8 volts, you know, crazy stuff like that.

**Dave Jones:** Yeah, so I'd say that one's probably for the Xilinx zinc over here. They probably chosen it because, well, they've used it over here, um, as well. Here's another one which, uh, that would be presumably for the, uh, Rockchip up here.

**Dave Jones:** So, it's a companion uh, DC-to-DC converter. Curious to look that up now. Here it is. Woah, confidential. Didn't sign the NDA. Oh, no. How did I get it? >> [laughter] >> And let's have a look there.

**Dave Jones:** A complex power management integrated circuit PMIC for those playing along at home. Uh, five configurable synchronous step-down converters, yeah. Nine LDO reg- regulators, two switches, and a battery fuel gauge, as well.

**Dave Jones:** Nice. So, they could use that for the, um, onboard battery, as well. It's got an RTC, as well. Uh, that's that's crazy. It also includes an audio codec. Real great What?

**Dave Jones:** Seriously? So, it's obviously designed for like a different type of product to an oscilloscope, or you know, just a generic to go with the Rockchip, well, the Rockchip chip where where the, um, arm processor chip would probably be used in a whole bunch of, you know, multi-media products and cheap tablets and stuff like that.

**Dave Jones:** So, maybe that's what this, um, is. You know, it's got a 1.3 W, uh, class D power amplifier. It's got, you know, supports microphone input. It's got I2S. So, it's got all the audio stuff that you'd expect to find on a tablet.

**Dave Jones:** So, yeah, so I think the primary application for this is, uh, like a multi-media tablet device or something like that. And they've just used it here. Well, why not?

**Dave Jones:** Used it here because it's you use it for the processor. It's, you know, you can use any DC-to-DC converter, but that's interesting. Wow. There you go. We've got a couple of them.

**Dave Jones:** So, do wonder if they're using the battery management in what one of these. You wouldn't need both, of course, for the battery. So, I've turned that upside down, so the electrons don't fall out, and there you go.

**Dave Jones:** So, you can read those memory chips over there more betterer, and that is the processor memory cuz they're running the application. So, all the, you know, the actual Linux application in here, and like the oscilloscope application, and all the other stuff it's running, that's all in there.

**Dave Jones:** And running in this external memory, whereas the memory over here is for your sample memory. And there's our flash over there, so that runs the operating system, and our ADC is an AAD2400.

**Dave Jones:** Yes, I have checked. It is actually that is an extra zero there. So, I can't really find that. Have we seen that in another scope? I can't remember. Done too many teardowns.

**Dave Jones:** But, they're obviously sharing that between both channels there. So, that's obviously serving all four channels there. So, it's over a four-channel multiplexed input. I don't see any other multi They're not No, no.

**Dave Jones:** They're just doing some offset there. 595 spotted. Classic 74 HC 595 serial shift register there. Just a like a IO expander just to get some IO. I've done that in my Jelly Bean component series.

**Dave Jones:** And And that's obviously the PLL. Don't even have to look that up. You can You can just tell by the surrounding. You know, it's got some inductors and capacitors all around it, and a oscillator here.

**Dave Jones:** And it's near the main sampling FPGA up here. So, you know, that's the phase-locked loop generating the higher um sampling frequency the sampling clock for the well for the ADC and also the um acquisition uh FPGA.

**Dave Jones:** And all of the analog uh front ends, they're all the same. I didn't even have to take the cans off uh two and three here. If one and four are the same, then yeah.

**Dave Jones:** Um anyway, so the sample rate of this thing uh with the one ADC is um going to get uh divided by four if you turn on all four channels, but I haven't used it to verify that, but that's almost certainly what's happening here.

**Dave Jones:** Um not much else doing anywhere else. We've got all power supply stuff happening around here. There's our HDMI output. Uh the Rockchip uh supports that, so there's no external uh HDMI um chipset there.

**Dave Jones:** Oh, there No, no, there shouldn't be. I think it's a direct output. And it looks like we have ourselves the Ethernet uh driver up here. And um yeah, it's not hugely interesting.

**Dave Jones:** Otherwise, there's not much else. Oh, I can't quite that in the photo that I've got here. No. I'll have a closer look at that. Anyway, um um STM uh 32 processor over here doing its own thing.

**Dave Jones:** So, what's that being used for that? There's the programming interface for it. Why would you have an STM 32 sitting there? Oh, I can only think that that must be for the uh multimeter section over here.

**Dave Jones:** That That'd be my guess. Hmm. This is completely weird. Check this out. This is an NSi, never heard of them, 4205. Look what it is. I I double-checked this.

**Dave Jones:** It is a Oh, go away. It is an NS4205. It's a 3 W um a class D dual channel audio amplifier. What? Leave it in the comments down below.

**Dave Jones:** What? Front end time for you front end aficionados. Let's have a squeeze. No surprises whatsoever. It looks like your basic, you know, couple hundred meg modern uh front end.

**Dave Jones:** Here's our input, there's our AC coupling cap, there's our Cosmo uh solid state uh relay there which just shorts out the capacitor in uh DC mode. And it looks like we've got another path here through an attenuator system here.

**Dave Jones:** It gets a little bit fuzzy. And this doesn't have a uh 50 ohm input. Um, so nothing doing there. Um, this is interesting. Um, check it out. That's an That's an interesting um, package there.

**Dave Jones:** It's Normally, we've got just an a wide SO8 uh type package here. But no, they put the alternate footprint there, which is quite common, especially if you You know, if you're designing your board and you're not sure um if you can absolutely get that part and it's available in different packages and you've got the room and you know, and layout's not an issue and stuff like that, it pays to

**Dave Jones:** actually um put in both footprints just in case you can't you have supply problems, supply chain problems getting a particular package. You can put in an alternate package. And that's sure enough, that's what they've done there.

**Dave Jones:** Um, genuine Panasonic Japanese relays. So, it's interesting that, you know, even these um cheaper Chinese front ends will still use, you know, Japanese genuine Panasonic relays. It's fascinating. And then, once again, speak of the devil, go up here and you won't find any Asian source program will gain amplifier.

**Dave Jones:** They use in um National Semiconductor LMH6518. You've seen this in every um scope. And if we go over to the videotape over here, it's, you know, it's the standard front end for almost every scope on the market, you know, like like 900 MHz bandwidths here.

**Dave Jones:** So, any like, you know, 500 meg and under scope is probably going to use the Texas Instruments LMH, which is national, comes from the old national days. And it's just the programmable gain amplifier.

**Dave Jones:** So, that's where you get your bandwidth limiting, for example, and you get your different gains. You get the different attenuator/um gains on your scope up front end, and then just a differential output driver buggering off to your ADC there.

**Dave Jones:** It's fascinating that these Chinese companies still use these western front ends, and you know they're not adverse to using the local Chinese ones, cuz you'll get those for the ADC and other things, and you get the Rockchip one for the main application processor and things like that, but not you'll still find the TI/National LMH65180 here, or and you'll find the Panasonic relays.

**Dave Jones:** It's just weird, huh? But yeah, there's nothing else doing around there, so it's your basic 200 MHz front end, low cost, super simple, Bob's your uncle. And here's the multimeter front end.

**Dave Jones:** They've done a really good job isolating this. You remember I said like they had the rubber they put the rubber boots on here, plus the extra plastic sheet on there, so you got dual isolation between the input connectors and the metal case.

**Dave Jones:** Absolutely fantastic. Um and then you let yourself down by using this automotive grade blade fuse in here. There's no not HRC or anything. And they've done really good, right?

**Dave Jones:** They've got the isolation slots here like this, and you'll notice that they've actually got another a plastic protective sheet, which obviously like we can see it under here through this slot as well.

**Dave Jones:** It obviously like goes all the way over here to protect it once again. So, that would be protecting it from the metal back end of the LCD. Would be behind there, wouldn't it?

**Dave Jones:** So, yeah, that's interesting. I think I might have mentioned before that this was a DC to DC converter. I didn't have my brain engaged. So, that was a brain fart.

**Dave Jones:** No, this is obviously the input voltage divider. Not sure if it's a hybrid or it's just a potted bunch of individual resistors in here. But, so what they're going to have in here is just a whole bunch of resistors coming up the top and then they're just going to have more of those here.

**Dave Jones:** So, yeah, [clears throat] that that could be like just individual selected resistors and then potted. Not sure if it's I'd have to bend it right out and I don't want to do that to get a part number.

**Dave Jones:** But, anyway, that's our positive input there. So, it goes straight into there and then you have another path over here through the relay. But, you'll notice that they don't reuse the Panasonic relay in here.

**Dave Jones:** They use a H that's a Hongfa, isn't it? I think relay. Anyway, the chipset HY3131 common as mud used in the 121G multimeter, a whole bunch of Keysight meters, a whole bunch of meters.

**Dave Jones:** So, yeah, that's a 60,000 count chipset. Very nice chipset. So, I really like the actual design of this apart from the bloody fuse up here. But, this is weird.

**Dave Jones:** Look at this and I have verified this, okay? Here is the Yeah, I think this is the amp input and this is the milliamp. And look, there's a trace shorting them out.

**Dave Jones:** And I've verified this. I've measured it. I've I've I've removed the fuse out here and there's still a dead short between these two terminals. They're identical terminals. Why do you have milliamp and amp terminals when you only need one and you could have just called it amp/milliamp?

**Dave Jones:** They've put the other terminal in there. It's entirely redundant. So, what they've done is they're using the 10 amp fuse for both the 10 amp range and the milliamp range as well.

**Dave Jones:** And then, look, and then you've got I can't get the part numbers on can't see them in this thing anyway. But, these are MOSFETs. These are MOSFETs. You can see that there's the gate pin there and these three pins are tied together here and all four pins are tied together over here.

**Dave Jones:** So, they're doing MOSFET switching and so it's the same thing here and you know, your gate's over here and they're they're using the There's the 10 milli ohm uh current shunt for the 10 amp range and then then there's then there's a 500 milli ohm or half ohm uh current shunt for the milliamp range.

**Dave Jones:** But, like what? Why go to the effort to put in two separate jacks when you don't need it and then put in MOSFET switching? Why not just have the amp jack coming straight into your um current shunt via your few via your 10 amp fuse, of course.

**Dave Jones:** Um I don't get it. Is it a layout thing? Like cuz the fuse is over here and like they've botched it in as some sort of afterthought? Or something?

**Dave Jones:** I don't know. I haven't seen the original but they redesigned this multimeter apparently. As I said, it used to be 20,000 count and now it's now it's 60,000 count.

**Dave Jones:** So, they probably changed the chipset in this thing and maybe they changed the design of the front end and I botched it in somehow. But, that is bizarre. I've never seen that before.

**Dave Jones:** They literally These aren't split jacks either. There's no input jack alert on this, right? I looked physically looked inside the socket. These aren't split jacks and these are just shorted out.

**Dave Jones:** You don't need the extra jack. I don't know what's going on there. Weird. Anyway, um you've got your digital optical isolation here and this looks like your power isolation.

**Dave Jones:** You can tell because it's buggering off there and that looks very powdery like, doesn't it? With the big traces and that and whatnot. Then you got your continuity buzzer as well.

**Dave Jones:** So, yeah, you know, stock standard HY3131. You can go look up the data sheet and the application and notes. It's just a basic implementation of that. But that is That is very weird.

**Dave Jones:** I I don't understand that at all. >> [laughter] >> Thoughts in the comments down below. So, there you go. That's the Micsig MH014 teardown. I I think that's excellent.

**Dave Jones:** It's very well designed, constructed. As I said, it's built like a brick dunny, this thing, with the diecast alloy case on the thing. It's really hefty and the nice implementation of the They they use the pins for the strap.

**Dave Jones:** They use metal pins in the in the carry strap. So, I don't think that'll ever break unless like the rubber deteriorates or something like that. And it's very nice.

**Dave Jones:** So, I'm looking forward to actually using this thing operationally and see what it's like. I hope it works as well as it's designed and built apart from what the heck What the heck?

**Dave Jones:** Come on. HRC fuse, please. But as I said, you can order this without the multimeter and I guarantee you they didn't relay out the board. They would just unpopulate all of that.

**Dave Jones:** They would just unpopulate like the holes would still be in the case and then the front panel decal will just go straight over it. I'm sure that would be the difference.

**Dave Jones:** But if anyone's got the non-multimeter version, you can verify that, but it's almost certainly the exact same board layout. And there's, you know, 10 bucks worth of parts here.

**Dave Jones:** So, you know, it's it's not much difference. This goes over to the battery, but your power's not coming through there. Your power's actually over here. This is where the battery actually connects into, right?

**Dave Jones:** So, it can go into all these DC to DC converters and everything else, right? Yeah, so what is this But as I said, that's a dual audio op amp.

**Dave Jones:** What What that doing? Does this thing have speakers in the back I'm not aware of? So, I hope you found that teardown useful. Hopefully, I'll do a follow-up uh review on this thing.

**Dave Jones:** Uh leave down below if you want me to test anything specific cuz it's really hard to test oscilloscopes like thoroughly. You've got to have like you know, you can test like a hundred different things and it's just crazy.

**Dave Jones:** So, if you want something uh specific checked out, um leave it in the comments down below. But, if you like that teardown video, please give it a big thumbs up and as always comment down below and there's an EVBlog forum link for every video and high-res uh teardown photos are always available on EVBlog.com.

**Dave Jones:** Thank you very much, Mixig, um for sending in this nice bit of um kit. I'm really looking forward to using it cuz I've really got an old uh portable scope.

**Dave Jones:** So, I think um yeah, this one is going to replace it. Catch you next time. >> [music]
