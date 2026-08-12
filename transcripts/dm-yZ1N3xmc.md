---
video_id: dm-yZ1N3xmc
title: EEVblog #409 - EDMI - Smart Meter Teardown
url: https://www.youtube.com/watch?v=dm-yZ1N3xmc
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 26, "3": 37, "4": 51, "5": 63, "6": 77, "7": 95, "8": 105, "9": 132, "10": 162, "11": 193, "12": 220, "13": 234, "14": 245, "15": 261, "16": 275, "17": 297, "18": 307, "19": 323, "20": 331, "21": 347, "22": 358, "23": 372, "24": 391, "25": 410, "26": 433, "27": 448, "28": 459, "29": 469, "30": 483, "31": 494, "32": 508, "33": 516, "34": 531, "35": 543, "36": 553, "37": 563, "38": 574, "39": 589, "40": 601, "41": 613, "42": 630, "43": 647, "44": 663, "45": 672, "46": 689, "47": 709, "48": 721, "49": 730, "50": 743, "51": 754, "52": 764, "53": 780, "54": 788, "55": 806, "56": 821, "57": 832, "58": 848, "59": 861, "60": 872, "61": 886, "62": 901, "63": 917, "64": 930, "65": 944, "66": 955, "67": 969, "68": 982, "69": 1005, "70": 1019, "71": 1034, "72": 1048, "73": 1059, "74": 1072, "75": 1085, "76": 1100, "77": 1120, "78": 1139, "79": 1162, "80": 1177, "81": 1193, "82": 1211, "83": 1222, "84": 1237, "85": 1250, "86": 1263, "87": 1278, "88": 1290, "89": 1302, "90": 1311, "91": 1323, "92": 1340, "93": 1369, "94": 1379, "95": 1393, "96": 1407, "97": 1418, "98": 1435, "99": 1441, "100": 1472, "101": 1486, "102": 1503, "103": 1516, "104": 1535, "105": 1549, "106": 1564, "107": 1581, "108": 1594, "109": 1607, "110": 1617, "111": 1630, "112": 1644, "113": 1657, "114": 1689, "115": 1705, "116": 1722, "117": 1736, "118": 1748, "119": 1765, "120": 1782, "121": 1795, "122": 1804, "123": 1817, "124": 1831, "125": 1847, "126": 1863, "127": 1875, "128": 1886, "129": 1895, "130": 1914, "131": 1924, "132": 1937, "133": 1956, "134": 1969, "135": 1983, "136": 1998, "137": 2019, "138": 2032, "139": 2048, "140": 2064, "141": 2085, "142": 2095, "143": 2106, "144": 2121, "145": 2141, "146": 2149, "147": 2162, "148": 2175, "149": 2194, "150": 2203, "151": 2219, "152": 2234}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Today's item is actually viewer submitted. It comes from Lewis Able from Abletronics in the UK. Thank you very much, Lewis. He sent me this little puppy.

**Dave Jones:** It's an EDMI Atlas Mark 10A three phase power meter. You know, one of these smart meters that they put on your house these days and it's got GPRS in it, you know, 3G thing.

**Dave Jones:** It comes with a SIM card, talks back to base, it monitors all your power consumption and you know, they don't have to send somebody around to read your meter anymore.

**Dave Jones:** They can do it all with one of these smart meters. Now, EDMI are actually an Australian company, they started out being an Australian company. It's manufactured in Singapore, so I'm not sure what the deal is if they're fully Australian anymore, but anyway, I'll claim it.

**Dave Jones:** So, this is an Australian-made smart meter. It's a 240 V one. It's brand spanking new, still has the unused SIM card in the packet, so pretty advanced functionality in this puppy.

**Dave Jones:** Now, this one's actually a 240 V model designed for the Australian or UK market. It's three phase as I said, not just single phase and it's got a whole bunch of features and I'll link in the data sheet down below and you can see what advanced capability this does.

**Dave Jones:** It does THD and all sorts of weird and wonderful power measurements. Fantastic. So, thought it'd be interesting to crack it open, take a look inside. So, you know, as I say here on the EEVblog, don't turn it on, take it apart.

**Dave Jones:** And I will start out by taking a look just at the spec sheet here, see what we've got. I don't know, it's all sorts of compliance standards. If you're into that sort of thing, check those out.

**Dave Jones:** But, it's 220 to 240 V input, although it does operate from 180 to 290 V input. Burden voltage less than 10 W per phase. Frequency range it operates from 45 hertz to 60 hertz and then the current range is got looks like one channel is that one channel 6 amps 5 channels 20 amps I don't know current limit is 20 times the maximum current range for 0.5

**Dave Jones:** seconds for those surges then our burden power in this case less than 0.5 VA or 0.5 watts per phase and it does four quadrant energy measurement imports and exports uh real and reactive power it does absolute and three phase and per quadrant and all that sort of jazz and it does frequency phase angle power factor total harmonic distortion unbalanced stuff and you can do waveform downloads it's got five

**Dave Jones:** cycle resolution on sagging and stuff like that so it can record that time date and phase worst case excursions programmable trigger levels man it's got everything it's got IO as well it's got a various relay drive outputs and stuff like that really quite neat designed to operate over minus 25 to plus 60 degrees range it's 2.1 meg of non-volatile memory so it can record for 3600 days 10 years

**Dave Jones:** with 30 minute intervals across two channels it can do up to 32 channels interval programmable two independent surveys whatever they are instantaneous readings policy inputs ability to store all of that sort of stuff and it really is a very powerful little beast of course it's got a built-in real time clock as well it's got you know the rate adjustable rate output and stuff like that it's got a

**Dave Jones:** big LCD on it we might power it up after we do the tear down to see how it actually operates and it's going to have security as well because these are security and tamper detection and allowance because these things are smart meters, right?

**Dave Jones:** They don't want um the consumer to be hacking into these things and uh and doing that sort of thing, you know, and uh getting cheaper power bills or no power bills.

**Dave Jones:** So, it apparently has detection for bypassing current and reverse uh current provision for sealing with conventional wire or plastic uh seals and uh advanced tamper detection and login. Well, not quite sure what that is whether or not, you know, you uh can hack the components inside.

**Dave Jones:** I don't know. Maybe we'll find out. And then it's got various communication options. Uh it's got uh RS-232, RS-485 multi-drop, and it's got GPRS compatible, and compatible with ZigBee and MV90, whatever.

**Dave Jones:** Don't know what MV90 is. And it's got some software available for the PC which allows you to um set all this stuff up. And I'd be very surprised if you couldn't uh remotely program this thing as well and uh change all its loads and uh extract the data and run tests and things like that over the um GSM connection as well.

**Dave Jones:** And it actually came with the uh GSM card as well, the SIM card to put in it. So, wooh, it's got a lot of stuff. All right, let's take a look at it.

**Dave Jones:** It's quite a big unit here and unfortunately Lewis has uh had a peek inside. I don't blame him. He couldn't resist. So, the uh calibration um uh not the, you know, the uh warranty void and all that sort of stuff sticker has been busted.

**Dave Jones:** So, it's uh one big unit as well. All the interconnects are on the bottom here, which we'll take a look at. But apart from that, it's just designed for mounting in a box there.

**Dave Jones:** And uh the user interface, main LCD here, a couple of LEDs which uh pulses. It uh says that it does um 10 pulses per kilowatt hour there. So, you'd get 10 pulses on that for every kilowatt hour of power consumption.

**Dave Jones:** I'm assuming and that's probably programmable as well. Then we've got a couple of LEDs here and we've got a couple of push buttons, connect and select, and that's all there is to it.

**Dave Jones:** And if we take this bottom off here, we just unscrew this and whoop. There we go. And there's a couple of terminal blocks in there. They're they're not the mains power input.

**Dave Jones:** We'll take a look at those in a second, but um we've got a separate modem down in here. So, it's not actually built in. We'll have to do a separate tear down of that, but that is a it is a GSM modem, Intelsat Sam, Intelsat Proprietary Limited.

**Dave Jones:** It's Australian as well. Beauty, I like it and and there's where you whack your SIM card down in there and it comes with an antenna as well. There we go, just an external antenna so you can put that away from the box inside your distribution cabinet or something like that.

**Dave Jones:** Just a RJ45 on there, connecting it and there's our antenna output. And that is a separate item. That's kind of makes sense. They can change that for different countries and things like that so they can sell the main unit anywhere in the world and then have different standards for GSM and phone interconnection depending on where you are.

**Dave Jones:** And inside the case they've thoughtfully provided a little pinout here for the interconnects and there's a looks like there's a relay output there, some uh uh probably optocoupled um outputs there.

**Dave Jones:** There's our RJ45 and then we've got our mains input down here. And as I said, this is a three-phase model so they've called the phases A, B, and C.

**Dave Jones:** So, we've got phase 1A here going in there and coming out. So, it measures the current on that phase, and of course it can measure the voltage relative to the neutral over here as well.

**Dave Jones:** So, second phase B and third phase C in and out. And check out the size of these big beefy mains input terminals here, absolutely massive. And I'm not sure where you screw those in.

**Dave Jones:** I think you've got to take the uh this whole cover off to actually get in there. And there we go, that cover just pops off there, and there's your huge big screw terminals down in there.

**Dave Jones:** Woah, monsters. And we've got a little jumper here which selects between the internal battery which is currently connected and an external battery pack as well. So, you just move the jumper across there.

**Dave Jones:** I'm not sure why you would want a uh external battery pack. Now, this cover should just pop straight off here because the tamper seal is on the side here.

**Dave Jones:** It should just pop off. Now, under here I'd expect a because it it is sealed on the side there with that thing, I'd expect there to be a a tamper switch under this thing to sense that the cover's removed at a minimum.

**Dave Jones:** Woah. And pop. Pop goes the weasel. And there we go. Ta-da! There's inside the unit. I love how it's just bare. I mean, this is a a transparent case anyway.

**Dave Jones:** You can sort of translucent case. You can sort of see through. Aha! There's our micro switch. Ta-da! Love it. So, that's our tamper micro switch. So, it already knows there's our internal battery.

**Dave Jones:** So, it already knows that we've uh presumably if it's actually monitoring, I don't know. You might have to sort of, you know, set it up first and then it's all ready to go.

**Dave Jones:** So, this is a factory one, hasn't been used apparently straight out of the box. So, not sure if it's configured yet, but there's your micro switch which disables when you take that front cover off.

**Dave Jones:** Couple of mobs down here by the looks of it. We'll have a look at the board in more detail and the LCD there. There's our main processor under there and the LCD is just standing off the board like that.

**Dave Jones:** You don't see that too often. That's rather quite neat and of course there's a second boards underneath cuz there's no big power stuff on this top board here. This is just the data logging and processing board, I'm assuming.

**Dave Jones:** We've got some light pipes there. There's our two little light pipes going up from the LED down on the bottom there and they just go up through the front panel there.

**Dave Jones:** There you go. And there's two other LEDs down here that they went through the big clear window on the bottom there. So, um those things don't need a light pipe and got our two contact switches over here.

**Dave Jones:** Looks like they're just a Yeah, they're just a Oh, there we go. They actually fell out. There's the little rubber I rather like that. Check it out. They've got that sitting in there like that and when you push it, oh, that's a that's a really nice switch.

**Dave Jones:** Look at that. That's beautiful. I like And down near our outputs down here, you can see that we've got four outputs, four moves. Those moves are obviously protecting the outputs there and there's our relay which went to that one, I believe it was.

**Dave Jones:** So, one of those relay contacts there would go to there and there's our optocouplers there. Those three optocouplers would be controlling these three channels here. We've got more optocouplers over here.

**Dave Jones:** So, all of this circuitry around in here is We've got four optocouplers there coupling that over from the digital section, the control section all up the top here down into this output which drives the RJ45 which goes to the G GSM module down there.

**Dave Jones:** So, that's all optocoupled isolated, as you'd expect. Safety first on this sort of stuff. Another optocoupler in there, and uh that's it. Bob's your uncle. The main processor, there'll be a a flash memory device under there as well.

**Dave Jones:** Maybe that one down there. It's looking a bit suspicious. So, that'll be our 2 mega flash memory, perhaps. Um and we can't get that LCD out cuz that's actually soldered directly into the board.

**Dave Jones:** You may not be able to see that, but I can see it, and that is a TI MSP430 processor down in there. There's a 32 kHz crystal down there.

**Dave Jones:** There's probably another crystal somewhere else as well, or that could be the main one. Plus, there's got to be another real-time clock crystal somewhere as well. So, yeah. Um I don't know.

**Dave Jones:** That's probably it for the main processor board. I mean, it's not, you know, there's not a huge amount doing there. We've got our uh cables connecting down to our main power board down here.

**Dave Jones:** That's where a lot of the interesting stuff is going to be. And of course, we have the classic LM324. It's actually an LMV uh 324. Whole bunch of uh passives around that.

**Dave Jones:** It's probably just doing some uh buffering and things like that. Now, our battery's a Varta uh CA um half double A size, made in Germany. Aha, brilliant. Now, on the uh power board, well, there's probably three boards down there.

**Dave Jones:** There's probably a big power one down there. It's probably in that uh second one down in there. Oh, no. That could be an upside down. I see some uh through-hole components on there.

**Dave Jones:** So, maybe there is just one big power board under there, but I wouldn't rule out a uh third board underneath there as well. And um on that power board, of course, we're going to see a uh big uh beefy current shunt for each um a very precise current shunt for each of the um three uh phases.

**Dave Jones:** We're going to see you know some pretty high spec ADC type stuff. You know, like I don't expect this thing to be terribly accurate down at the watt or sub watt range.

**Dave Jones:** Of course, it's designed to measure you know the main current of your house and monitor the main current. So, if this thing is 2400 watts your standard mains outlet, but it can actually go much higher than that.

**Dave Jones:** Well, you know, if you want to say point one watt resolution, that's 24,000. You know, if one bit is 124,000, you know, you're going to need at least a 15 say you know round it up to you know a 16 bit converter there for each channel.

**Dave Jones:** If you wanted you know in the order of sub one watt resolution on this thing. May not have that. May just you know may just be happy with a 12 bit converter or something like that.

**Dave Jones:** But this would be a pretty you know high spec device. They've spared no expense. I'm sure these things are probably quite expensive. So, let's see if we can Oh, there we go.

**Dave Jones:** Hey, look at that. Look at that. The board just pulls back. It's hinged under here like it's hinged at the back here with the connectors and it's just held in place so it doesn't move with that that plastic retaining clip there.

**Dave Jones:** So, you slide it back and ta-da lift it up, forward and out. Oh, no, that's something's Oh, there we go. Got to take this. I'm not sure what that cable's doing there.

**Dave Jones:** I might find out. There we go. Ta-da. Aw, we've been mooned. Look at that. Now, on this main board of course, you can see the classic isolated grounds. This is the optocouplers would be bridging these two grounds.

**Dave Jones:** Here's our output ground here based on our output connectors down here. And then this is all our logic ground up the top. And then they would have the of course, have the optocouplers separating those two grounds.

**Dave Jones:** Classic, and yeah, they've got a lot of margin on there, that's for sure. Now, it looks like this board is directly connected by these screw terminals down into there.

**Dave Jones:** Now, you note that this extra terminals here, which they said do not connect, they do actually looks like they go through there, and then they do connect down into here.

**Dave Jones:** So, are they like a earth connection or something, but it definitely said, if you have a look down in here, uh do not connect. No connections to terminals 2, 5, 9, and 13.

**Dave Jones:** 2, 5, 9, and 13. So, do not connect them, but they are actually connected to something down on the board. So, yeah, we're going to have to uh screw this thing.

**Dave Jones:** We've got direct connection Yeah, direct connection down onto the board, which is what you want, of course. You want big beefy connections down into there. And uh surprise only had one screw, actually.

**Dave Jones:** I would have thought maybe they'd have a have a couple in there, perhaps. So, interesting to see what form the current shunts take, um because I don't think they're mounted on the I'm not sure if they're mounted on the board.

**Dave Jones:** They could be like just free standing underneath, or or like actually, you know, lumped right at the back of these connectors, and then they just and then these are just like the wiring coming up from them or something, the sense lines, perhaps.

**Dave Jones:** Um I'm not entirely sure. We'll find out. This is terribly exciting stuff watching me unscrew. Somebody in the recently commented, "Oh, why don't I use an electric screwdriver?" Ah, come on.

**Dave Jones:** That's uh that's cheating. I only use an electric screwdriver for you know, one of those RF die cast cans or something that have 50 screws on the things. Otherwise, you're cheating.

**Dave Jones:** And you can't get me to just banter on about random crap, either. So, there we go. Um that looks like it is going to leave her out of the Okay.

**Dave Jones:** No, okay. They're they're stuck under there like that. So, it looks like you've got to fold probably fold these up. Hmm, this could be tricky. Let me work on it, folks.

**Dave Jones:** Well, that's pretty obvious. You have to unscrew these in here, and they just pop out like so. So, now we should be able to pop this board out. And pop out, presumably.

**Dave Jones:** I mean, there was nothing nothing on the bottom of the case at all. So, um yeah, I think it just needs some delicate persuasion. Aha! This whole terminal block section pulls out, by the looks of it.

**Dave Jones:** There we go. Up. There we go. That all pulls out. The board pops out. It's all rather It's all rather complicated. Not that trivial. Oh, there Oh, look at that.

**Dave Jones:** Oh, look at that. Beautiful. Aha! Oh, that's pornographic. Look at that. And isn't this beautiful? We have three current transformers. There's no traditional current shunt resistor as such. They're using these current transformers.

**Dave Jones:** And after a tiny little bit of investigation and thought, it's obvious why. And here's the reason. And the thing that's driving this is the IEC standard 62053-21 and various other dash standards.

**Dave Jones:** They basically say that these current meters, these smart meters, power meters on your house can't take any more than 2 W per phase. And you know, yeah, you've got you know, a million houses hooked up.

**Dave Jones:** I guess all that sort of stuff adds up. So, they're determining that maximum power value that these energy meters can consume per phase, a measly 2 W. So, let's look what happens if you've got one of these We're only going to look at one phase here, okay?

**Dave Jones:** So, let's have a look if you've got a traditional current shunt resistor. What does that mean? Okay, our current shunt resistor RS, we're going to have a current flowing through it.

**Dave Jones:** And this particular model has a 100 amp capability. So, let's take 100 amps. And as you know, um P equals I squared R. So, you rearrange that. Our resistance there, so we're calculating Sorry, that's RS.

**Dave Jones:** And we've got RS here is going to be equal to the power, our maximum power in this case, 2 W, divided by IS squared. So, that's 100 amps maximum capability.

**Dave Jones:** Or if you design this meter to be 50 amps, you can redo the calculation. But let's use 100, okay? It's going to be in the order. So, 2 W on 100 amps squared is going to give us a value of that resistor of 200 microohms.

**Dave Jones:** Absolutely tiny. So, you know, what does that mean? Well, at the not only is that an incredibly low value of resistance, okay? It's going to be, you know, very difficult to implement that.

**Dave Jones:** Not impossible, but you can certainly implement that. But what it means is that it then at low values of current, instead of say 100 amps, if your house is only drawing say 1 amp on that phase, what does that mean?

**Dave Jones:** What's the voltage drop across that shunt resistor? Well, 1 amp, do the math. It's going to be 200 microvolts, basically. And we're talking very small voltages there at very small currents.

**Dave Jones:** And that becomes a pain in the ass to measure. So, you know, let alone get me out trying to measure, you know, 100 milliamps or 50 milliamps or something like that.

**Dave Jones:** So, what they've done is they've used these current transformers instead of your traditional current shunt resistor. I like it. And they've got three big beefy ones here per phase.

**Dave Jones:** The output of these current transformers, they're going to convert those into voltage, and they can measure the current as well based on a burden resistor down in there. And also, if you use traditional current shunt resistors, well, you're going to be dissipating, you know, up to a couple of watts inside this thing.

**Dave Jones:** And yeah, it's going to heat up, and that can cause potential issues as well. So, just something to consider. And the reason that they've gone for these funky current transformers here because, as you can see, you know, there's practically no power dissipation at all in this, um, you know, basically, it's only drawing the current it needs to drive the circuitry and all the measurement stuff, which isn't going to be much compared to

**Dave Jones:** a traditional current shunt resistor. So, look at these big bus bar, um, huge big links down in here. They're absolutely massive. So, these are the three phases here, and we've got our neutral.

**Dave Jones:** But of course, having no other connections on there doesn't make sense. So, figured it out. What it is is you remember these little links that we took off uh before in here.

**Dave Jones:** These are little voltage tap links and they actually um short out. If you have a look down in here, they actually short out the uh one of the phases here down to this terminal.

**Dave Jones:** So, you're not supposed to connect this terminal because these links are connected internally. Got these internal links which then connect it through to this trace which then goes off down in here.

**Dave Jones:** So, they're your voltage taps going down to all your uh circuitry over here. And plus, there's also another tap which come comes off the same pin over to a 3.3 meg resistor on each channel down in there.

**Dave Jones:** There's one on each channel. So, that looks like that's the other one looks like uh the all that stuff up there, it looks like a a protection um tap.

**Dave Jones:** That's just a you know, uh getting the protection devices off. This is probably uh powering the rest of the circuit as well. But, the actual measurement voltage measurement on each uh phase seems to be going through this 3.3 meg resistor into this little uh SOT-23 package there and off to um well, uh I guess the um um ADC uh stuff has to be on the main processor board because I don't see

**Dave Jones:** anything on this board down here that uh looks like it's an ADC. So, it's obviously tapped off. We've got a whole bunch of uh unpopulated circuitry around here. I'm not sure what that was supposed to do.

**Dave Jones:** And this link here which we uh saw before and we had to disconnect, which goes up to this main board here, it's obviously an isolated uh voltage tap. There's a little power supply there and that's going off to power this part of the isolated circuitry down in here on the RJ45 output.

**Dave Jones:** So, the rest of the circuitry around here, which uh taps off the three phases here, any one of the three phases by the looks of it, it is just a mains switch mode DC power supply.

**Dave Jones:** There's a switching transformer. There's There's the controller. It's a uh Power Integrations TNY268GN. So, that's a really efficient switch mode controller, like less than 50 mW no load consumption.

**Dave Jones:** So, you know, really one of those eco green ones. So, they really do want to get the power dissipation down on these things, of course, to meet those various standards that require these things to have low power.

**Dave Jones:** So, that powers the rest of the circuitry. It wouldn't need much at all. I mean, they've got big 400-V caps down in here, you know. It seems a little bit overkill, actually.

**Dave Jones:** We've got a got a common mode choke here. So, we've got some filtering over on this side, but it does seem um you know, a little bit overkill for the amount of power that I suspect this thing requires, but anyway, I'm sure it needs it for a reason.

**Dave Jones:** Once again, they've got lots of protection in here, lots of MOVs all over the place. Looks very well designed. I think they've spared no expense there. The The switching transformer there is really looks first class.

**Dave Jones:** So, I really quite like that. And of course, there's that separate winding coming off there I told you about before, which uh powers the output circuitry. That's isolated from this one here, which powers the main circuitry over there.

**Dave Jones:** Now, if you look at each channel here, there's a four components. There's a Zener diode. There it's marked ZD10, but it doesn't look like a uh Zener diode package.

**Dave Jones:** Anyway, I'm I'm presume it is, and um they've just got some There's a filter cap there, and they've got a shunt resistor there, a burden shunt resistor on the output of the current transformer.

**Dave Jones:** And there's not much else to it. There's So, you're going to have a bunch of the four of those per channel. There they are, duplicated. And then there's some extra circuitry in here tapped off this one here.

**Dave Jones:** So, I'm not sure what that one's doing, but it's going through an optocoupler there. And as I said, I don't know what that unpopulated stuff is. There's a whole row of resistors in there populated, but all that sort of stuff is unpopulated.

**Dave Jones:** So, there's this board basically is just the power supply and the um uh current to voltage conversion. Uh that's pretty much it. So, the ADC must be up under there somewhere, and I suspect it's Well, it's either going to be the internal to the Texas Instruments 430 processor, or it's probably one of those puppies under there, cuz that's that LM 324 we saw previously.

**Dave Jones:** So, let's have a look at that one. And no, that's just another LMV324. Bummer. And the other 14-pin SO package over there is also an LMV324. So, they must be using the ADC in the MSP430 processor.

**Dave Jones:** And that's an MSP430FG4618. And that's actually a mixed signal one with the higher resolution, 12-bit ADC in it. So, that's what they're using. Just a microcontroller that's got the internal reference.

**Dave Jones:** I don't really see an external reference anywhere under there. They might Yeah, I don't think there is. They're probably using the internal reference there, but as I said, you know, these things don't have to be um you know, hugely accurate right down at the uh low end.

**Dave Jones:** So, you know, the internal reference in the 12-bit uh ADCs there, good enough. And let's take a look at the uh current transformer we got in here. It's a Vac brand, and they make current transformers specifically for electronic watt-hour meters.

**Dave Jones:** There it is down there, for electronic watt-hour meters. Brilliant. I like it. we've got here is the E4626X501. That's a 100 amps uh primary uh current capability. They're all at a current ratio of uh 2,500.

**Dave Jones:** So, it's um uh you divide the 100 amps there by 2,500. We're going to get 40 milliamps uh maximum on the output. And they have pretty much essentially a fixed uh phase error due to It tells you down here, due to the excellent soft magnetic properties of the Vac core.

**Dave Jones:** Um these are DC-tolerant uh current transformers, and they need to They lead to a negligibly small amplitude error, as well as to an extremely low and linear temperature dependence as well.

**Dave Jones:** And they've got all the curves in here for all the temperature dependence and stuff like that. And due to the low permeability of the core material, the phase error is typically 4 to 5°.

**Dave Jones:** And there it is, 4.73 they specify precisely. And of course, that you can calibrate that out. They're saying uh either do it in the software or uh do it in the uh LC RC uh low-pass filter.

**Dave Jones:** My guess is they're probably doing it in the software, cuz that's the easiest way to do it. Once this thing is already uh installed and assembled, they would uh individually calibrate um each one of them to uh uh to basically remove uh that error.

**Dave Jones:** And here's those uh components I showed you earlier on the um output there. There's the primary side. It's just a current transformer. We've got a burden resistor there, which gives us a voltage uh drop across here, and there's our low-pass filter, and off it goes to your ADC.

**Dave Jones:** And here's the uh characteristic uh curve graph, and it shows uh various things versus uh current here. We've got uh basically uh the graphs extend from, you know, a couple of hundred uh milliamps down there all the way up to a couple of hundred amps.

**Dave Jones:** So, this one's only rated to uh 100 amps, but it can obviously go a bit beyond that. And you can see that we have the amplitude uh error here, tiny little amplitude error in percentage down in there.

**Dave Jones:** And you can see that basically uh does not change with that temperature at all. But you can see the uh phase angle does obviously uh change with temperature here.

**Dave Jones:** So, that would be uh calibrated Well, they try and calibrate it out at a nominal temperature there, but you can see it's pretty good over the entire current range.

**Dave Jones:** I really like it. And of course, these things accurately measure the uh phase angle as well. So, they may even be taking uh the temperature into account. There might be a temperature sensor on the board, and uh they're, you know, they could they could compensate for this because, you know, it it you know, it's fairly linear with temperature there.

**Dave Jones:** I mean, you know, over an operational range look of, you know, 55 down to sort of, you know, minus 10 over that sort of 50° range, it's going to change by roughly uh the order of half a degree error there.

**Dave Jones:** So, you know, that that could be significant. I don't know. You'd have to go through the math and figure it out. Um do some ballpark calculations. But if it is, you could compensate for that in the firmware.

**Dave Jones:** No problems at all. Just by measuring the ambient temperature. Now, here's an interesting uh performance graph. It shows the um uh the basically the behavior of uh different types of VAC core materials compared to regular 80% nickel iron uh cores.

**Dave Jones:** So, they've got, you know, they're Vitroperm and Vitrovac. Um you know, these are probably, you know, trademark terms for their own uh core material that they actually use. And they've got an amplitude error here.

**Dave Jones:** And you can see theirs is basically flat over the full current range there compared to a typical 80% nickel iron core like that. So, much more linear using their Vitrovac.

**Dave Jones:** And the same thing on the phase error as well, of course. Look at that. It's pretty much almost ruler flat pretty much for the um phase angle there compared to the typical 80% nickel iron stuff.

**Dave Jones:** So, really, you know, they've got some wizbang core technology that makes these um pretty linear current transformers. I like them. And they've gone to town here. They've even got typical characteristics of the amplitude error versus the primary current over the full current range from 1 milliamp all the way up to past 100 amps there.

**Dave Jones:** And you'll, you know, you'll note that it's only um you know, barely even uh plus minus .25% amplitude error. Well, as for the supposed wizbang uh tamper protection and all that, yeah, they've got the micro switch down here.

**Dave Jones:** But uh apart from that, you know, I don't know if they're um you know, got uh firmware and uh maybe even circuitry to try try and uh detect uh whether or not uh you know, somebody's Well, they've got to um try and detect the how somebody's bypassing the current.

**Dave Jones:** So, maybe they're able to do that in firmware somehow. But um yeah, I you know, I'm not sure um you know, you could probably get in there. And if you're really uh knowledgeable about these things, you could get in there and hack the uh uh shunt values in there or something like that.

**Dave Jones:** And I'm not sure if the firmware would be able to um know that sort of thing. But of course, um once you of course to get into it, you physically got to bypass the yard micro switch and then well, it alerts the the utility that you know, somebody's you know, broken into this thing and yeah, they'll probably wave the finger at you.

**Dave Jones:** So, you know, I I don't think they have to do too much in in part in you know, in regards to the tamper protection and stuff like that. It's built in.

**Dave Jones:** It'll be interesting to know how they actually buy you know, actually detect bypass current like in the main box itself rather than going through here. I'm not actually sure how they would do that.

**Dave Jones:** So, there you go. That's a look at the main guts of this thing and you know, there it's very well engineered and looks like they spared no expense for this thing as you'd as you'd probably expect.

**Dave Jones:** It really is quite nice and I've run out of time to power this thing up and have a play with it. And I kind of wanted to do that, but I might even leave that for another video if there's enough interest in that powering up and playing around with it, but I'm not sure if I could use it for anything useful really cuz you know, I'm not into doing the high

**Dave Jones:** current stuff and things like that, but it might come in handy for something, but I might try and power it up and see if I can have a fiddle around with it later.

**Dave Jones:** So, I hope you liked that little tear down. If anyone has a schematic or service manual of this thing, that would be great cuz that would reveal a bit more I'm sure of what they're doing here.

**Dave Jones:** So, if you have it, please let us know in the comments. And of course, we can't leave it without taking a look inside the GSM adapter here. So, there's our SIM card module.

**Dave Jones:** There's nothing terribly exciting in here at all. Let's uh flip it over and there's our wireless uh wireless CPU model Q24 plus. Woohoo! Whoop-dee-doo! And there we have a Sipex SP3238.

**Dave Jones:** Nothing terribly exciting there. It's just an RS232 transceiver. But all of the magic is done in that Wavecom wireless CPU module. So, I'm not going to take that out.

**Dave Jones:** That requires to unsolder the tabs on the whole thing and get it out and rip it apart and ah couldn't be bothered. So, there you have it. There's a teardown of the EDMI Australian supposedly Atlas Mark 10A three-phase energy meter.

**Dave Jones:** Hope you enjoyed it. And if you've got any further info and you want to discuss it, jump on over to the EEVblog forum. The link is below as well as to various data sheets in this teardown as well.

**Dave Jones:** And don't forget, if you haven't already done so, please subscribe to my YouTube channel. Catch you next time.
