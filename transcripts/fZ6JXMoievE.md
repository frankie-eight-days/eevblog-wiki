---
video_id: fZ6JXMoievE
title: EEVblog 1550 - Keysight E36731A Battery Emulator Teardown
url: https://www.youtube.com/watch?v=fZ6JXMoievE
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 30, "3": 45, "4": 57, "5": 68, "6": 82, "7": 95, "8": 109, "9": 123, "10": 134, "11": 147, "12": 162, "13": 176, "14": 188, "15": 201, "16": 218, "17": 230, "18": 242, "19": 257, "20": 273, "21": 289, "22": 303, "23": 318, "24": 333, "25": 348, "26": 360, "27": 373, "28": 385, "29": 399, "30": 415, "31": 430, "32": 442, "33": 455, "34": 471, "35": 486, "36": 500, "37": 513, "38": 527, "39": 540, "40": 552, "41": 562, "42": 577, "43": 593, "44": 607, "45": 620, "46": 635, "47": 651, "48": 664, "49": 676, "50": 690, "51": 704, "52": 718, "53": 733, "54": 751, "55": 766, "56": 779, "57": 793, "58": 807, "59": 821, "60": 833, "61": 849, "62": 863, "63": 879, "64": 898, "65": 913, "66": 929, "67": 946, "68": 964, "69": 979, "70": 994, "71": 1011, "72": 1023, "73": 1037, "74": 1054, "75": 1070, "76": 1082, "77": 1094, "78": 1108, "79": 1127, "80": 1142, "81": 1155, "82": 1169, "83": 1184, "84": 1196, "85": 1208, "86": 1219, "87": 1236, "88": 1249, "89": 1262, "90": 1274, "91": 1285, "92": 1300, "93": 1313, "94": 1325, "95": 1339, "96": 1351, "97": 1366, "98": 1376, "99": 1392, "100": 1408, "101": 1427, "102": 1443, "103": 1459, "104": 1474, "105": 1489, "106": 1506, "107": 1517, "108": 1534, "109": 1548, "110": 1559, "111": 1572, "112": 1586, "113": 1598, "114": 1609, "115": 1622, "116": 1634, "117": 1647, "118": 1661, "119": 1677, "120": 1688, "121": 1702, "122": 1713}
---

**Dave Jones:** Hi, it's teardown time, and check out what turned up on the doorstep. Thank you very much, Keysight, for sending in their latest bit of kit. This is going to be really interesting. This is the Keysight E36731A. I don't know what these numbers that

**Dave Jones:** they keep coming up with. Anyway, how does anyone remember any of them? So, this is a threefer. This is three bits of kit in one. It's a DC power supply, electronic load, and battery emulator all in one bit of kit. Unbelievable. Uh

**Dave Jones:** uh price starts at about 4,700 Yankee bucks. So, this is not cheap. But, if you need the capability of emulating batteries and doing anything with any battery-related product, this is just an amazing bit of new kit. Now, you've seen

**Dave Jones:** me do a teardown, which I'll link in up here and down below if you haven't seen it, of my uh Keithley. I do actually have an old uh battery emulator. It's an older design, but, you know, it it still does the

**Dave Jones:** business. So, this not only has an equivalent to that battery emulator in it, but also an electronic load. I've got multiple electronic loads here in the lab. May as well not have them anymore, cuz it's all in the one bit of

**Dave Jones:** kit. And not only is it a DC power supply, but it's actually a precision DC power supply capable of going down to uh 1 microamp or better current resolution. And you've actually seen that demonstrated in my uh previous mailbag

**Dave Jones:** video. But, we're going to tear this bit of kit down today and see what's inside it. It is a big beast. It's not particularly heavy. I I thought it didn't have a fan, but after I power it up, it does actually have a fan. And

**Dave Jones:** there is a bit of fan noise, which is kind of annoying for like a bit of kit that's designed to like operate for like dozens of hours, you know, hundreds of hours or whatever, actually logging uh batteries and stuff like that. So,

**Dave Jones:** not great. But, anyway, it's got digital ports, it's got the LANs, it's got the USB, it has the optional GPIB. It's got uh external sense, and this is uh external uh binding posts on the input. Speaking of which, look at this. This is

**Dave Jones:** just a Bobby dazzler. Oh, thing of beauty is a joy forever. You'll notice inside there, it's got a I don't know if you can see it, but it's got a big ball that sort of like forces the wire in

**Dave Jones:** there. It's really fantastic. It is a 200 uh watt jobbie, so the battery emulator can do uh 200 watts, 240 watts for the electronic uh load, and the power supply is similar, I believe. Now, of course, you can do all this

**Dave Jones:** functionality with three separate bits of kit, but it's like you got to cobble things together, and if you don't have a proper proper battery emulator, then well, it's a real mess. Um because you got to have that equivalent series resistance in

**Dave Jones:** your power supply, it's got to be taken into account, and etc. etc. So, what a battery emulator does is it basically uh simulates the ESR of a battery because the the equivalent series resistance cuz that basically changes um with as as the

**Dave Jones:** battery uh depletes itself, and also uh changes with age as well. So, there's if you're designing a battery-powered product, there's a couple of ways Well, there's only two ways you can do it. One is to actually use the actual battery,

**Dave Jones:** and then actually discharge it over whatever the product life. If you've got a product lasts for hundreds of hours on a battery, then you got to test for hundreds of hours. Or, you can use a battery emulator like this to uh

**Dave Jones:** actually as the name says, emulate um the discharge characteristic not not just the discharge characteristic, but the ESR characteristic of uh that battery, and you can do this like uh if you're testing over temperature, you can test aging, you can test, you know, charge

**Dave Jones:** cycles, and all sorts of stuff like that. So, if you're designing a battery-powered product, bit of kit like this can be very handy. As I said, the power supply is um very few power supplies on on market. I do

**Dave Jones:** have one here in the lab, but they're quite rare, that can actually measure very low currents. This one can go down at least 1 microamp, but I saw in their data sheet that if you get the data out of it, you

**Dave Jones:** might be able to go down to 0.1 microamp resolution as well. So, you know, not only for So, not only can it do like a couple hundred watts batteries, but it seems like it can do the smaller ones as well. All right,

**Dave Jones:** let's take this off. I am shooting this in 4K. So, oi, there we go. We've been mooned. We've got the bottom of the top board there. We've got the mains power supply under here. There's the fan that I couldn't see. So, anyway, this is you

**Dave Jones:** might think because it's basically a power supply and an electronic load, you might think that this thing is actually a four-quadrant power supply. But according to the data sheets, it's actually only a two-quadrant power supply. So, it looks like uh so, the

**Dave Jones:** power supply section of this can't actually do the load sinking. So, it looks like they do actually literally have three instruments, and that's what might be, you know, maybe three different boards here. They're probably going to have like one power supply

**Dave Jones:** board. They're going to have an electronic load board, which can be like totally separate. And also, uh the basically the battery emulation, all it does is it puts a series resistance on the output of the power supply. So, the

**Dave Jones:** power supply in this thing will have another lot of circuitry, maybe this board, don't know yet, with an equivalent with a basically an adjustable resistor, which is a MOSFET or a bank of MOSFETs, that can adjust the equivalent series

**Dave Jones:** resistance or emulate the equivalent series resistance of your battery. So, it looks like there's no panel on the bottom. It's just one big folded case like that. It's got a Kensington lock on it, too. Um so, yeah, it looks like we can't just get access

**Dave Jones:** the bottom of those PCBs, so everything's got to come out from the top side, unfortunately. It's going to take a while. Okay, this top board here, it doesn't look like it has anything to do with the battery emulation. You can

**Dave Jones:** see a board-to-board interconnect going over to the main processor board, which is on the front panel here. Then you can see all these traces running over here, right over. That is the IO part of the board, and then you've got your LAN

**Dave Jones:** interface there. So, that just goes back. There's a couple of pairs there, and that there is just your right USB. So, yeah, they've just got LAN and USB traces just running all the way back. The LAN and USB chips, they'll just be

**Dave Jones:** on that front panel board in there. Well, that's interesting. There's a little peg there with a hole. It's like this whole board slides forward, but then there's the board-to-board interconnect. Yeah, I'm pretty sure this front panel has to come off first,

**Dave Jones:** otherwise it doesn't make much sense to do what we just saw. And this metal work here, take that screw off. Looks like this metal work goes right under there. So, yeah, I think front panel, then this top board slides out and up, and then

**Dave Jones:** this metal work comes out with the mains power supply, and then we can get down into the guts of it. Pesky screws under a strip. Give it a tug. Uh-huh, I see it moving. There you go. She moved. So,

**Dave Jones:** going to pull that Yep, there we go. Ah, we're off. And we can Look at that. We can access the innards, and this top board is going to slide out of there and lift off. Ah, what a Bobby Dazzler.

**Dave Jones:** So, I got to make sure I reconnect those. Oh, there we go. Oh, look at that. Little planar jobby. Wow, nice. There you have it. There's an excellent example of a planar transformer. Basically uses little PCBs in there with

**Dave Jones:** windings, so hence you've got the multiple layers in there like that. So, it's basically just a multi-layer uh PCB in there and they use planar transformers to get, you know, more accurate and controlled uh transformers. You can just control the process better

**Dave Jones:** than you can with like a physical mechanical, you know, winding with uh wires and whatnot. So, yeah, I'm dead steady. Anyway, we've just got a DC-to-DC converter here. Obviously, two MOSFETs here. Bob's your uncle, but I like that's not particularly high power.

**Dave Jones:** I don't know. They just need a DC-to-DC converter uh for something. We've got a fuse over here and I Yeah, it's just an off-board uh DC-to-DC converter. So, what is it for? Well, looks like it goes up to here and luckily, those are

**Dave Jones:** labeled. It's upside down, so all the electrons are going to fall out, but uh They just says P3 power supply and uh P4 e-load. So, the electronic uh loads. This is the power supply for the electronic load, I guess. And there's

**Dave Jones:** the controller on the uh top side there. Anyway, high-res photos available on evblog.com. And looks like uh it's These are inductors. Um so, we've got some uh common mode chokes here by looks of it going off to this and we don't know

**Dave Jones:** where that ribbon cable went off to. Well, that's a mystery at the moment. So, we'll find out. And as you'd imagine, the digital IO there has a fair bit of uh protection and drive going on to it. So, yeah, that's to be expected,

**Dave Jones:** but uh apart from that, yeah, Ethernet USB interface. Uh the USB just goes uh straight over there. There you go. A couple of inductors and Bob's your uncle. Off she goes. Woohoo! So, we've got two main boards here. One's going to

**Dave Jones:** be a power supply. I don't know which one's what, but one's going to be power supply and uh one's going to be the uh electronic load and also uh to do the battery uh emulation as well, which as I

**Dave Jones:** said, is basically just a series MOSFET or a bank of series MOSFETs that simulates the uh ESR output of uh your battery. That's basically all there is. The rest is in the uh smarts in the software. And believe me, you pay extra

**Dave Jones:** for the software. Because of course you do. And look at the interconnections here. Look at the these large gigantic solid brass and then tapped in here connectors that go to the front panel. And you you've seen how impressive they are. And obviously

**Dave Jones:** they've got a four-wire Kelvin connection here. So that's buggering off. And then over here you've got these big bus bars screwed into here, shake-proof washers, everything else. Big thick ass bus bars going over to here. So these are

**Dave Jones:** effectively in parallel with here. Cuz I think this is the electronic load over here. just using this. Basically the electronic load is just basically going to be in parallel with the output here. So they can turn it off on as required.

**Dave Jones:** Cuz when you have a battery emulator, you don't need that electronic load. But this is a third part of the capability that's built into this thing. You wouldn't get in your normal battery emulator product. So you know, they've really tried to do an

**Dave Jones:** all-in-one product here. It's fantastic. And is this down here part of the battery emulator ESR? Cuz you don't want you don't need to go too high in your battery ESR. There's going to be a point where is that adequate heat sinking for

**Dave Jones:** it? Off the top of my head I couldn't tell you. And yeah, this makes total sense once you look at it. This is obviously the electronic load over here. It's going to have the largest heat sinking cuz it's it's a purely a linear

**Dave Jones:** thing for the electronic load. And as I said, it's just basically connected in parallel with the main functionality of this product. A lot of people won't use the electronic load capability in this product. They'll just use the battery

**Dave Jones:** emulator. And we've got the power supply which is a separate. So that's the switching power supply. That'll be a high quality main switching power supply. And that could be a tracking switching regulator, too. We don't know. And then and because this is a precision

**Dave Jones:** product, you're going to have a linear tracking regulator on the output here. So, that's why it only needs a small you know, relatively small heat sink here because it's tracking. It's doing you know, it's doing most of the

**Dave Jones:** efficiency in the switching and then for your extra low noise output, you just have a tracking pre-regulator. And I've done that in my power supply design series. So, that's why there's not a huge amount of heat sinking on the what

**Dave Jones:** is a power supply which is like I think it's a couple hundred watts, isn't it? And interestingly, this is actually two levels of power supply. The output here is actually on a PCB which is at a lower level than this one up here. And I think

**Dave Jones:** that lower level supply goes all the way to the back end over here. We can see that the remote output the rear terminal power output is is here with the sense terminals as well. And that's on a lower

**Dave Jones:** PCB than this one up here. So, they're obviously using these giant bolts here as board-to-board interconnects. And I've done a video on designing your own electronic load. It's been very popular. Tons of people have actually built their own and they do sell their own. And so,

**Dave Jones:** we won't go into detail on the electronic load here. So, basically these are going to be our current sense resistors here. And then our MOSFETs which are on here. Looks like we've got three main ones like that. And there's

**Dave Jones:** also I think another three duplicate on the other side I can see as well. And another little something or other down there as well. But yeah, basically an electronic load is nothing more than it can be nothing more than an op-amp or

**Dave Jones:** you can do it under digital control as well. A resistor and a bunch of MOSFETs and big heat sink and Bob's your uncle. Of course, all the magic's in the loop stability and stuff like that making sure it doesn't oscillate and whatnot.

**Dave Jones:** But yeah, apart from that, don't know what that little relays down there doing, maybe some range switching perhaps, don't know. Ah, you can actually see down in there couple of spare footprints. So, another couple of MOSFETs can actually go in there. So,

**Dave Jones:** that might be up for a higher power or different voltage models. I think it does come in different voltage and power models. Not sure what one I've got. No, they're not four wire sense. Look at that. They're thermistors. They've got a

**Dave Jones:** thermistor measuring the temperature rise on the output connectors. Wow, isn't that jazzy? There's your four wire Kelvin connection. There it is there. That pair is actually buggering off over there, going over the relays over here, and then it looks like it's going off

**Dave Jones:** somewhere else. Could be some circuitry on the bottom. Don't know, but yeah, so these two big brass solid brass blocks, they're just bolted in and connected to the giant pad that's under there like that. You can see that there's a giant

**Dave Jones:** screw in there like that. So, yeah, they're measuring the temperature of each connector. Wow, that's attention to detail. Now, here's something interesting. Look at this. There's a large footprint for a capacitor C27. Like, you know, a huge jobby like that,

**Dave Jones:** but they've actually put a little daughter board in there with two, four, six, like seven or eight, missing one, ceramic caps. Look at that. So, they've obviously changed their mind there. That is very interesting, is it not? Hmm, so

**Dave Jones:** I wonder why they did that. Maybe they have to make changes depend on different models or something perhaps. That could be maybe the reason behind that. Yeah, don't know. And there's a relay behind that. Um, so it looks like maybe is that

**Dave Jones:** relay like switching in that capacitor bank? Perhaps. It's like cuz that's not the like a relay for the output. It's obviously not rated for that amount of power. So, I can only think that that's switching that capacitor load there perhaps.

**Dave Jones:** Interesting, huh? Maybe for different feedback optimizations, different loop stability optimizations perhaps based on range. I don't know. There you have it. I was on the money for that board going all the way through like that. And uh right through to the rear

**Dave Jones:** terminals over there. And check out all that via stitching down there. Enormous. But uh yeah, uh basically just one big connecting board to connect the front uh to the rear connections. Nice. There's the 4K resolution glimmer. There's the 4K resolution glimmer shot

**Dave Jones:** of the main PCB. This is what's doing all the business. And there's the backside of it there. And uh let's go through this in a bit of detail. And here's the power supply. No surprises for finding Mean Well uh designed and

**Dave Jones:** manufactured this. So, there's our output over there. We've got our uh screw clamps. Very nice. Um that looks very schmick, of course, um as you would expect in this. So, yeah, no wuckers there. This is the input uh side over

**Dave Jones:** here. Mains input uh side. And the output side. They're all uh Nichicon, are they? Anyway, there you go. It's got uh thermal cutout and uh all sorts of goodness with that. Anyway, uh fan for those aficionados, it's a

**Dave Jones:** fan. It's an X fan. An X fan. Uh okay, whatever. All right, let's take a quick look at the main board. This is where all the magic happens. Now, I've got the uh top side of the board here and the bottom

**Dave Jones:** side which I have uh flipped over. So, that's why all the uh numbers are backwards so that, you know, things line up like these mounting holes here all line up, okay? So, it's a physical map. Uh so, it's like you're looking through

**Dave Jones:** uh the PCB. Now, I was actually a little confused at first because I assumed that that PCB sits on the top like this. I assumed that it was somehow connected in here, but it's it's not. There's actually no connection from that board

**Dave Jones:** to the front panel terminals here. As we saw, these big screw terminals, these are the this is the actual output. So, the output is actually closest to the rear output panel and this board here is just I I've actually checked these are

**Dave Jones:** just direct physical connections via the internal planes directly to this. So, the output of the board is actually at the rear end here and then it's got to travel all the way over here to get to the front. Anyway, we've got another

**Dave Jones:** couple of those capacitor budge boards there, which is rather interesting. It shows that that's a you know, a thing across the design. So, we've got three of those, which is really interesting. So, this is our output here. Sorry, I'm

**Dave Jones:** moving my head around, but the input actually is here like this, which comes from the the sweet main switching power supply. So, we've got our input here. We've got a 20 amp surface mount fuse there. We've got a big filter cap. These

**Dave Jones:** are all top name quality. They're either Nichicon or Chemicon or Nippon Chemicon capacitors. So, no worries whatsoever. What we've got is four FETs here and these are actually these jobbies. These are TI 100 V N-channel NextFET power MOSFETs, very nice. So, obviously

**Dave Jones:** that's the push-pull drive for each leg of this switching transformer here. So, yeah, so this is a big switch mode power supply here. So, this would be a tracking switch mode so that you don't have to dissipate as much power down in

**Dave Jones:** your heat sink down here. So, yeah, very nice and then we've got another inductor. Doesn't that look schmick? Coilcraft jobbie. Oh, very nice. And these are uh, these heat sinks, uh, ones here. They're just, uh, diodes, so, uh,

**Dave Jones:** full wave, uh, bridge rectification there. Um, some filtering, some common mode choke, and output filter cap, some extra filtering here. Don't know what these two resistors here are doing. Can we see the top side? No, can't see anything there, so I'm not sure what

**Dave Jones:** they're doing. Anyway, so that is the main, uh, output here. So, this is basically the output here, common ground, uh, of course. And then we've got some more big ass filtering here. And that's basically our output. And that output, uh, then goes into the main

**Dave Jones:** heat sink, which is down here. And this is the, basically, the series pass element that's doing, uh, not only the, uh, regulation, cuz you don't want your output being directly from the switch mode, uh, supply like this. It's going

**Dave Jones:** to be noisy. In fact, I don't know what the noise spec of this, uh, thing is. And I just checked, uh, ripple and noise peak to peak, 7 mV up up to 20 MHz, though, uh, ripple and noise RMS, uh, to

**Dave Jones:** 10 MHz is less than 600 microvolts, right? So, it's, you know, it's pretty darn clean, as you'd expect, cuz this thing's got a 14-bit analog, uh, to digital converter to get all the resolution you need. So, this series

**Dave Jones:** pass element here is not only working as the regulation, you know, the low noise regulation, linear regulation element, um, but it's also working as the equivalent series resistor element. How that particular arrangement is there, not 100% uh, sure, but I think they're

**Dave Jones:** getting, uh, dual use functionality out of that thing. And And you don't need a massive heat sink down here, cuz as I said, uh, having this, uh, regulator here, this is a tracking, um, switching regulator. So, it minimizes

**Dave Jones:** the voltage drop, uh, across here. I'm sure that's got to be a tracking jobbie. And all of our current sense resistors, you notice two big Dale jobbies here. These are 10 ohms a pop. These are both in parallel. Yes, they're only 1%, uh,

**Dave Jones:** because you calibrate it out later. These are actually, you know, very low tempco resistors. You pay a fortune for all of these current sense resistors. Like the one in my microcurrent, for example, that's like $2.50 US for one

**Dave Jones:** resistor, right? For the 10 m current shunt resistor I use in there. Anyway, this one's got two 10 ohms in parallel, so we've got 5 ohms there. That's for one range. Then we've got another two in parallel here. I don't know why they

**Dave Jones:** went with through-hole, maybe for power dissipation reasons, perhaps. That's got the range with the highest power dissipation in there. Anyway, um they So, they're uh 100 m each, so that's 50 m. So, we've got 5 ohms, 50 m,

**Dave Jones:** and then you've got these two big surface mount jobbies up here. These are actually uh from what I can measure, 1 m a pop. So, you're getting 500 If they are in parallel, haven't actually checked. Are they? I don't know. They've

**Dave Jones:** got some slots cut out here. Yeah, they seem to be in series, so I'm not sure what's going on there. Anyway, they could be like lower values. I don't They're They probably are in series. Anyway, they do have Look Look at this. You can

**Dave Jones:** see the taps coming off there, because these are our four-terminal Kelvin ones. These tabs here are the two tabs which you get your Kelvin connection off, and that goes into an instrumentation amp up here. So, there's two of those. So,

**Dave Jones:** we've got three ranges. One there, one to do with this. I'm not sure if this is a separate one. I'm not sure what's doing there. But anyway, it looks like like they have three different ranges separated by two orders of magnitude

**Dave Jones:** each. So, there's not like not 5 ohms and then there's not 0.5 ohms. It goes down to 50 m, so it jumps by two orders there, not one order. And you'll notice this tap in the middle here. Look at all these star

**Dave Jones:** power connections just going off like this. These are all going over to here, which I'm not sure what that goes with. That's just powering other stuff. So, I'm not sure what's what's doing there. But you'll notice some very low

**Dave Jones:** precision TL071, TL074 jobbies. They're not doing anything precise, so they're just doing like, you know, some sort of rough window uh comparison or something like that. Then you start getting your precision ones like your 8086 76 and there's a few of those on here. There we

**Dave Jones:** go. I'll go to one that's not flipped down here, so you can read them. 86 76 and that's an 8675. Why they using those two? They're both low spec op-amps a 339 quad comparator here and then there's your instrumentation

**Dave Jones:** amplifier. There's an OPA 189. I think I've done a video on that and that's reading the the two current sense resistors here. STM fan boys go wild. There you go. STM controlling all this. That's a a LVC04, so that's just inverter. And is

**Dave Jones:** this a DAC? I can't read that. Anyway, I won't be surprised if that's the 14-bit analog-to-digital converter. I'm going to go put a bit of spit on that. Yeah, that's an ADS 220 from TI. That's a 24-bit 2K sample four-channel low-power

**Dave Jones:** delta-sigma ADC with PGA, VREF, SPI and two DACs as well. So, yeah, that's where all the magic's happening. So, this is your basically it says they're only got 14-bit converter in this, but there's a 24-bit converter in there. And you can

**Dave Jones:** see like labels on the board here. PCB design has been a bit kind. Constant current start and things like post regulation here and constant current DAC for example and then constant voltage DAC and constant power DAC. So, it looks

**Dave Jones:** like they got three different DACs for the different modes, voltage monitoring here and there's a parallel relay here, voltage sense local or something. There's local again, voltage sense serial relay. So, not sure how the configurations working there, but

**Dave Jones:** there's current monitor and up here it looks like we have hardware over voltage protection trip, over current protection deck over voltage protection deck another current monitor over over current protection trip. So this is done in hardware not software

**Dave Jones:** but looks of it. Beauty. Well, you'd expect it for the price. Looks like there's another current monitor resistor here but so I'd love to see the schematic for this exactly how this is arranged. I'm not going to reverse

**Dave Jones:** engineer it at all but I think yeah, what they're doing is that's the ESR output that does the battery emulation they're using that as a regulation element and also the ESR capability in there. So yeah, they don't need a massive heat sink for that. As I

**Dave Jones:** said, yeah, they got a tracking switching converter over here. And that's the primary side drive there and not sure what that bit there is doing. You know the bunch of resistors in parallel there. Not sure what's going on but anyway,

**Dave Jones:** there you go. That's that's all the smarts on this thing. I won't take you through the electronic load cycle cuz it's in there's nothing on it. There's a bunch of MOSFETs and you know, a couple of op-amps and maybe if it's I don't

**Dave Jones:** know if it'll be controlled by the same micro up here but obviously this is handling all your local regulation. They're not using the main display processor to actually you know, do any of that. So it's it's got its own

**Dave Jones:** local regulation. You need that for speed and you know, consistency and and just separation of your design like cuz you don't want to be doing like this kind of like low level uh stuff for your supply in your main

**Dave Jones:** applications processor. That's not the job for it. It's the job of the local processor here to actually do that. So it's you know, it it's got to do all the you know, overcurrent overvoltage protection stuff which is all happening

**Dave Jones:** around here and then it's going to be controlling the regulation of your ESR and all your different modes your constant power mode and your constant current modes and everything else. So it's handling all that sort of jazz. So

**Dave Jones:** there you go. Um A diagram wise it's it's fairly simplistic, you know? It's All the magic's in the firmware and of course all the precision parts, all these, you know, really expensive parts on here and this is this is why

**Dave Jones:** these things cost a pretty penny. So, there you have it. That's a teardown of the new Keysight battery emulator. It's their lower cost series. As I said, they've got real higher end units and then like all like, you know, like

**Dave Jones:** dozens. I think they mentioned like 50 different add-ons or something for their other units. It's just nuts. Um yeah, but I think it uses the same it uses the same bench view battery emulation software. So, yeah, we've got the

**Dave Jones:** smaller E36371A. Why can't they have real part numbers? So, yeah, if you compare those two, two to three times the price. So, yeah, this is the new like runt of the litter here, but they've got these existing ones.

**Dave Jones:** This one's been around for a while. They've got another like a low noise source down here, like a photovoltaic array simulator and a big huge converter solution like it's just nuts. Like view all. Oh, we haven't seen them all yet.

**Dave Jones:** And then and there's internet of things battery life solution. So, you know, if you want to do more than this like the runt of the litter can do. I'm going to have fun playing around with this thing. It's It can do a ton of

**Dave Jones:** different stuff. You can get all these different modules and things like that to expand this solution here. It's just crazy. Anyway, hope you enjoyed that teardown, found it useful of the Keysight battery emulator the E whatever it is.

**Dave Jones:** Anyway, thanks Keysight for sending that in. Let me know in the comments down below what future videos you want me to do with this thing cuz it's incredibly powerful. So, I can do lots of battery not only battery simulation, but like

**Dave Jones:** battery discharge testing and all sorts of, you know, weird and wonderful things we can do with this. So, yeah, leave it in the comments. Catch you next time.
