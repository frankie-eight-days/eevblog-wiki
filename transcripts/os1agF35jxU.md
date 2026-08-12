---
video_id: os1agF35jxU
title: EEVblog #148 - Agilent 3000 X Series Infiniivision Oscilloscope Teardown
url: https://www.youtube.com/watch?v=os1agF35jxU
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 33, "3": 47, "4": 140, "5": 153, "6": 166, "7": 179, "8": 199, "9": 219, "10": 235, "11": 254, "12": 269, "13": 286, "14": 302, "15": 316, "16": 332, "17": 345, "18": 358, "19": 377, "20": 392, "21": 406, "22": 422, "23": 436, "24": 453, "25": 472, "26": 531, "27": 547, "28": 564, "29": 582, "30": 604, "31": 618, "32": 633, "33": 647, "34": 667, "35": 684, "36": 698, "37": 717, "38": 730, "39": 745, "40": 756, "41": 773, "42": 792, "43": 811, "44": 825, "45": 837, "46": 851, "47": 868, "48": 879, "49": 893, "50": 933, "51": 950, "52": 966, "53": 983, "54": 1000, "55": 1015, "56": 1034, "57": 1051, "58": 1069, "59": 1083, "60": 1101, "61": 1115, "62": 1132, "63": 1151, "64": 1166, "65": 1180, "66": 1197, "67": 1211, "68": 1315, "69": 1328, "70": 1347, "71": 1361, "72": 1378, "73": 1394, "74": 1409, "75": 1424, "76": 1438, "77": 1455, "78": 1471, "79": 1485, "80": 1502, "81": 1515, "82": 1529, "83": 1548, "84": 1562, "85": 1581, "86": 1596, "87": 1608, "88": 1625, "89": 1640, "90": 1658, "91": 1669, "92": 1685, "93": 1701, "94": 1717}
---

**Dave Jones:** Hi, welcome to the AEVlog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi. No, it's not deja vu. This isn't the Agilent 2000 series. I've already reviewed that one. This is the new

**Dave Jones:** Agilent 3000 series and I thought we'd tear down this one as well to see how different it is to the 2000. Does it have just the same board? Is it just a firmware difference? Well, there's only one WAY TO FIND OUT. CRACK IT OPEN. And

**Dave Jones:** here it is, the new Agilent 3000 series, 500 megahertz, fully optioned up. Whoa! Let's crack it open. It's about 12 grand worth.

**Dave Jones:** That new product smell. And you crack it open, and here it is. It is clearly different to the 2000 series scope, which is right here. Check it out. And you can clearly notice the large differences between them. The tooth the

**Dave Jones:** 2000 series on the bottom, 3000 series on the top. As you can see, the 2000 series is a physically smaller board, and it's got this cutout, which goes around like this. And you'll notice that the chassis is made exactly identical

**Dave Jones:** between these, cuz there's the two screws up here that for the 3000 series that are still there on the 2000, exactly the same chassis, which they've reused, but they've done a cutout on the board. Why they've actually cut that

**Dave Jones:** out, I don't really know. Why you wouldn't just take it across there and go down, I'm not really sure, because well, you just have to route that out, and you don't really gain anything at the PCB penalization stage. So, I'm

**Dave Jones:** rather rather confused with the 2000 series. I didn't really notice that before, but it really stands out when you look at the 3000 series board. And the input cans down here, the the analog input sections are physically bigger, as you'd expect, because they do

**Dave Jones:** have the the active probe input pins on them, so they physically have to have more connections on those. Um, and of course, the big change is that we've now got four ASICs here, two of the new waveform the new MegaZoom 4 ASIC, which is where

**Dave Jones:** all the magic happens, and two of these unknown devices over here. Whereas, we've only got one set on the 2000 series board here. So, it's really is a a substantial difference. You're basically getting uh double the amount of grunt, really,

**Dave Jones:** which is not surprising considering that the 3000 series model does 1 million 1 million waveforms per second. Unbelievable. And the 2000 series does 50,000 waveforms per second, which given that it's probably the identical ASIC, is probably crippled a bit. I

**Dave Jones:** think they might be able to up the 50,000 waveforms per second, but that's just a that's just a guess. And the processor is exactly the same on the new 3000. It looks like an identical part with an identical spec. It's the um

**Dave Jones:** uh 9 the Speer 600 uh processor, but the uh FPGA the Xilinx FPGA has changed. It is now a Spartan 3 uh 1200 as opposed to the Spartan 3 500 used the smaller Spartan 3 500 used in the 2000 series

**Dave Jones:** model. And of course, as you'd expect, they've got the extra uh channels here populated on the logic analyzer, whereas on the 2000 series model down here, they weren't populated. Um so, yeah, maybe uh with the 2000 series model, they planned

**Dave Jones:** to have 16 channels, so they designed it in and then they decided maybe at a late stage, "Well, we don't really we'd rather have the 16 channels on the 3000 series scopes." So, they just left it in there and depopulated the parts. And as

**Dave Jones:** you'd expect, there's minor differences between uh boards in terms of layout cuz the the physical layout is completely changed. They obviously started from scratch, really. I mean, there is uh you know, a real total difference in terms of uh ground planes, component

**Dave Jones:** locations, because as you can see, the uh processor and um FPGA are up the top here on the 3000. Down the bottom, they're um sort of in the center of the board on the 2000 series model. Uh of

**Dave Jones:** course, you know, things have to be the same like the power connectors and the physical interface products, but as you can see what they're physically move the battery on the 3000. It's in a different location. They've put these caps up here. It's

**Dave Jones:** just you know, there are a fair few differences between these two boards. So, they've just started from scratch. But apart from the two extra ASICs here, really there's there doesn't appear to be any real you know, system level changes to

**Dave Jones:** this thing. A slightly bigger FPGA, but that's it. So, really they've just gone for the extra ASICs to get the extra throughput required for the much faster waveform updating on the 3000 series model compared to the 2000, but they would save significant

**Dave Jones:** cost by not including these extra I'm not sure how much the ASICs are cost, but they're going to be reasonably significant, but still there's not a huge amount of difference and the analog front end will most likely be

**Dave Jones:** well, it should be better because you wouldn't pay for a 500 MHz front end and then put it in 2000 series. I'd be very surprised if that's the same 500 MHz front end because well, you know, maybe if they got it down cheap

**Dave Jones:** enough if they designed it cheap enough, they might be able to share technology between the 3000 and the 2000 on the front ends, but you know, really bandwidth is generally quite expensive to get. So, analog bandwidth that is.

**Dave Jones:** So, really I think they probably got a high performance higher performance front end there as well. But apart from that, not much at all. The only identical part of the layout I can see is the logic analyzer section down around here.

**Dave Jones:** That's the 3000 series model and if I pan down to the 2000 series model, you'll see that it's an identical layout physically as far as the chip location goes, but the silkscreen designators here, the actual component designator numbers have actually changed. So,

**Dave Jones:** they've refactored that entire design when they re-laid out the board. That's a common practice to actually refactor it and give them all new component designators. But, really, that's the only section the PCB designers seem to have copied.

**Dave Jones:** And here's the rear side of the board. And, as you can see, not much different to the 2000 series board. But, uh it is quite uh telling. As with the 2000, you can actually uh see the traces and kind of

**Dave Jones:** work out the system architecture that they've got going here. Now, for starters, the four ASICs they've got here, they've interestingly they've labeled them master and slave. So, this is the master channel. There's two master uh devices here, and there's

**Dave Jones:** two slave devices over here. Very, very interesting. Now, as you can see, this uh this is the MegaZoom ASIC, I believe, up here. And, if you follow all of the uh all of the uh control impedance differential pair

**Dave Jones:** serpentine traces down to the bottom here, you'll find that it goes into all four channels. So, that main mega zoom for ASIC or the master actually connects into the four analog channels. Now, the slave mega zoom ASIC on the other hand

**Dave Jones:** really doesn't have any of that. Well, not that we can see actually through here cuz this is probably like an eight or maybe a 10 Yeah, it's probably like a 10 layer board. It'd be at eight at an absolute

**Dave Jones:** minimum. So, the traces could be inside going down to the four channels, but clearly you can't see anything. There's a little bit going over to the main master ASIC over here, but apart from that, there's not much visible.

**Dave Jones:** Um There's not much in the way of visible traces at all. And you'll notice the difference between the decoupling between the mega zoom ASIC up here and this Well, what I call like a secondary ASIC down the bottom

**Dave Jones:** here. And you can see this secondary ASIC has a real bunch of you know, really heavy duty really serious ceramic bypass capacitors on it as opposed to the mega zoom ASIC which has a bunch of 100 ends just distributed around like that. There

**Dave Jones:** really is a remarkable difference between those two. And all of the logic analyzer circuitry down here goes into the master mega zoom ASIC over here. So, it doesn't look like any of it goes into the secondary ASIC over here, which probably just maybe

**Dave Jones:** processes the extra two channels. I don't know or maybe it helps helps divide up the you know, half a million waveforms per second each or something like that. I've really got no idea about that master slave arrangement. I'd have to sit down and

**Dave Jones:** have a good think about it. And as before, the master MegaZoom ASIC goes down here over to the display connectors directly to the display. The MegaZoom ASIC drives the display directly. The processor up here really doesn't have much to do at all. Only if

**Dave Jones:** it wants to do some math functions or some other auxiliary functions that are actually done in here and they're passed to the MegaZoom ASIC, which then goes in and drives the display. That's why you can get that massive display update

**Dave Jones:** refresh rate. And as with the 2000 series board, I I'm not sure if you get this on camera, but you can see some wash residue from when they've washed the board. There's some There's some residue left over there. And that's not

**Dave Jones:** that great, but it's really not that much of a big deal. But um I expected them to take a little bit more care than that. I expected the boards to be a bit cleaner. But really, not a big deal.

**Dave Jones:** It's very common. There's one interesting design choice I noticed on this board. When you look all over it, there's something that you can't see in terms of the capacitors. Now, take a good look around there, memorize it, and

**Dave Jones:** take it and see if there's any difference on the back in terms of the capacitors used. Now, if you're if you've got a keen eye, you'll notice there's one tantalum there. One tantalum on the entire design. Now, um

**Dave Jones:** usually a a lot of companies will have like a blanket rule to avoid tantalums because they're expensive, the material in them is quite rare, ceramic technology is really putting big pressure on tantalums these days and, uh, some of the older, um,

**Dave Jones:** style ones or the cheaper ones actually, um, have a lot of problems, uh, in terms of, well, blowing up. Um, but I won't go into the details of it, but overall, I guess the team who designed this, or

**Dave Jones:** maybe it was designed in sections, I don't know, but somebody decided they wanted one little tantalum there. So, that's an extra bill of materials um, item. Why they couldn't have used one of these large ceramics or something like

**Dave Jones:** that, it's probably due to the regulator chosen. They might have to use a particular that tantalum to get the ESR to make the thing stable. I don't know, but, um, I thought that was just rather interesting that they've avoided

**Dave Jones:** tantalums on the entire design except for one. Unbelievable. Actually, looking at the value, it is, uh, 470 micro Farad. So, that is pretty big. So, really, you can't get that with the ceramic, uh, options they're going to have on the board there. So, you

**Dave Jones:** know, they've got one other electron on the top side, but, yeah, maybe they were forced into using the tantalum. Who knows? Now, I'm on the top of the board here and this is the master ASIC and this is

**Dave Jones:** the slave and you can see the traces actually connecting the two. There's bound to be a lot more internally, that's for sure, but really, that's all we can see, uh, on the top side. There's not really any other

**Dave Jones:** connectivity here on the board at all. Okay, we've taken apart the, uh, front panel display and there's the front panel PCB, very similar to the 2000 except that the board actually extends down to here and the the points that there's actually uh pads

**Dave Jones:** along each input connector like that on the front for the if you have a look, bingo, there it is. They actually go in there for the active probes, those smart probe interfaces. So, they're actually just like a digital

**Dave Jones:** um IO interface. There's some power on there as well, I believe for powering external FET probes, but you just get that that extra interface on the 3000 series scope and really not much difference at all, but there's one interesting thing you'll

**Dave Jones:** note is the shielding on this on on the design of these new scopes is excellent. And here's what they do. They actually put these pads on here which are the ground basically. They just expose them and then they actually mate up when you

**Dave Jones:** push them together, they mate up with these spring contacts down here so that you get excellent ground shielding between the board and the actual chassis. So, these are these are all over the scope. They do this in a lot of places and it shows great

**Dave Jones:** attention to detail that they really cared about the EMC when they when they designed this scope. They really know what they're doing, but you'd expect that. It's Agilent. And I really love how this whole thing fits together. Look, they've bent the

**Dave Jones:** chassis like that and that actually protrudes through the front panel there and actually makes the ground test hook for the demo signals and the probe calibration signals directly connected to the chassis. Very strong, very nice design. And then the if you'll take a

**Dave Jones:** look look the board, the actual the actual probes are built on to the board. The test hooks are on there as well. So, when you assemble the whole thing, it actually protrudes through the front panel. So, these these test posts, when

**Dave Jones:** you assemble the whole thing, they poke through there along with that. It's just beautifully designed. It's a beautiful example of system design at its best. There is a whole bunch of concessions and tooling and throwing between R&D groups, the guys who

**Dave Jones:** designed the PCB, the guys who designed the schematic, and the guys who designed the housing. By guys, I mean guys and girls. Let's not be sexist here. And it's just There's a lot of effort which goes in into producing

**Dave Jones:** a high-end product like this at a complete overall system level. I love it. I just noticed something that is a brilliant attention to detail. I almost missed it. These two connectors here, you can see how these two boards don't

**Dave Jones:** line up, right? They Obviously, they couldn't push this connector down further because due to, you know, constraints that actually surround the connector and things like that. So, they they pushed it up to there for some reason. And you'll notice that they're

**Dave Jones:** offset in height. One This one here is higher than this one. So, instead of just bending the cable, what have the PCB layout guys have done? They've tilted that connector from the vertical off to the side of it, you know, 5° or

**Dave Jones:** something like that. Same here. They've tilted that slightly offset so that they line up. Great attention to detail. Thumbs up. Now, of course, they may or may not have thought of that right up front. That's why the PCB is at rev five, perhaps,

**Dave Jones:** because, well, they assembled it and went oops, they you know, the first prototype, oops, these don't line up. We should just rotate the rotate the connector a little bit and that's why this front panel display board, as simple as it is, is it rev two? Because

**Dave Jones:** maybe something as simple as that, they may have been caught out in the first prototype, who knows? They may may not have been that smart and thought that far ahead. That's kind of you know, stuff like that can really catch you out

**Dave Jones:** unless you do complete 3D system modelings and mock-ups of how PCB designs are going to work, which is one of the major advantages of today's PCB packages with all their 3D capability. You can import the model for the case,

**Dave Jones:** for the entire external case and put this PCB in here and see how it fits, put the other one, you can even put the connectors in there and things like that. Those sort of powerful tools allow you to get these sort of things right

**Dave Jones:** before you go and spin your first prototype. Now, thanks to Steve Leibson, we have an excellent block diagram of what goes inside and what happens inside the new Agilent MegaZoom 4 system-on-chip ASIC. It's phenomenal. Check out the capability built into this thing. Let's

**Dave Jones:** check it out in some more detail. Now, of course, you got your external AD converter here. That's not built into the MegaZoom ASIC. That's external. And that has four megasamples per second pumping data from the four channels into the

**Dave Jones:** acquisition memory manager. Now, the 16 digital channels from the logic analyzer also fed into the acquisition memory manager. Now, this block here clearly handles all of the segmented memory capability cuz there's that segmented feature that would be done in here as

**Dave Jones:** well surely with the help of some support circuitry as well. And it handles like breaking up the data like if you're measuring two channels, it will halve the sample rate and put it into memory and stuff like that. So, there's a

**Dave Jones:** there's a lot of magic that happens in that acquisition memory manager. A lot of really high-bandwidth stuff. And that's coupled directly to the built-in DRAM. Now, the ASIC has four megasamples of built-in DRAM on the 3000 series model. I'm not sure if it's

**Dave Jones:** a slightly lower spec ASIC for the 2000 series model which only has 100K, but uh the 3000 series certainly has 4 megabit of DRAM or 4 meg samples of DRAM uh built in, and that's phenomenal. And having it directly coupled on the die

**Dave Jones:** like that, that's how they can get the um the fast updating rate because it's going to be faster when it's on die, it's more tightly coupled uh straight into the acquisition memory manager, and that's how they can do it.

**Dave Jones:** Now, this goes into a display plotter over here, which we'll go into later, but there's a measurement buffer up here, which uh presumably that would take um just uh captures of the data and then uh would have its own analyzing

**Dave Jones:** circuitry to actually do your on-screen measurements like your, you know, your RMS voltage and your average and all that sort of stuff would probably done in that measurement buffer. There's no other detail there, so let's assume that's what it's actually going to do.

**Dave Jones:** And down here they have hardware serial decoders built in. This is uh traditionally a feature which uh has been performed inside the CPU up here, which we'll also go into, but they've decided to build it onto uh the die

**Dave Jones:** itself. And as you can see they're they're simultaneous, so you can decode uh I squared C, you know, SPI, USB, um all that sort of stuff, all those serial protocols uh done in real time on the actual hardware itself, which is

**Dave Jones:** phenomenal. That's a another traditional one which is done on the CPU, but because you've got a built in, you've got speed advantages, and you can actually decode stuff in real time. Of course, they've got all the triggering uh capabilities built in there as well,

**Dave Jones:** as you'd expect, and they've got the waveform synthesis uh engine too, which is uh presumably like an arbitrary uh waveform capability. Now, I'm quite disappointed that it doesn't actually have to the user an arbitrary capability because it would have been phenomenal to

**Dave Jones:** be able to capture data, put it in memory, and then store it and or modify it and then output it as an arbitrary waveform directly from the waveform synthesis engine. So, it's a bit of a shame that it doesn't have it, but I

**Dave Jones:** suspect there may be arbitrary type capability in there. And with the test waveforms, they're probably I don't think they're stored on chip here. They're they're probably stored as part of the CPU up here and the CPU down dumps the data

**Dave Jones:** for the test signals into the waveform synthesis engine. Now, as you can see, they've got masking capability as well built in. Another traditional function that the CPU actually takes care of. So, in your traditional scope, you would have your AD converter

**Dave Jones:** here and you might have a big FPGA or a custom ASIC like this doing various stuff, but then it would usually funnel the data or there'd be like a dual port memory and funnel it into external memory and then the CPU would access the

**Dave Jones:** memory and then update the display and then your CPU becomes the bottleneck. And that's the real problem. So, that's what they get around with with this new custom ASIC because everything's done on here through the display plotter directly coupled onto the LCD display,

**Dave Jones:** the CPU is really relegated to just like a secondary function. Steve's put in here like math, measurement, and search capability and things like that, but of course it runs Windows CE and it handles Ethernet capability, USB, and file stuff

**Dave Jones:** and all that sort of thing, but really it doesn't talk to the LCD direct. If it wants to do something, it goes through here and there's a GUI controller as well which handles, you know, all of your graphical interface type stuff,

**Dave Jones:** maybe your cursors and all that sort of thing are handled directly via the ASIC. So, your CPU has just become a supplementary item in these modern scopes. It's phenomenal. And then it will output some data directly into other capabilities. This

**Dave Jones:** acceleration for measurement, search, and things like that, that may be the separate FPGA on the board. I'm not quite sure of how because you saw in the teardown that the that there's an FPGA next to the CPU. So, possibly that's

**Dave Jones:** what that FPGA does, but that's only a guess. But as you can see, it's phenomenal and it's entirely different to your traditional scope design where the centerpiece is a CPU. But that becomes a real bottleneck and you can avoid that with a custom

**Dave Jones:** ASIC like Agilent have done here in the new Mega Zoom 4. It's great. I love it. And that's how they can It probably took them years to develop this ASIC, but once you do, once all the hard work's

**Dave Jones:** done, then you can bring this capability down into your low-end scopes. You can amortize the cost down into the low end. And it just you know, allows all this phenomenal update rate capability in low-end scopes. Whereas traditionally if I had

**Dave Jones:** to pay 10, 20,000 dollars to get a million waveform updates per second, which is what this ASIC is capable of, 1 million waveforms per second directly onto the LCD display. There's no way you would ever do that with your traditional

**Dave Jones:** CPU approach. Now, that's on the 3000 series model. I'm not sure if the 2000 series model uses exactly the same ASIC or whether or not it's a scaled down version which has less sample DRAM and less waveform update capabilities per

**Dave Jones:** second. I'm not sure. But it certainly allows you to bring that capability down to the affordable level. It's great. Agilent, huge thumbs up to Agilent for designing this new mega zoom ASIC. I love it.
