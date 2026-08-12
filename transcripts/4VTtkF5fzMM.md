---
video_id: 4VTtkF5fzMM
title: EEVblog #1247 - DDR Memory PCB Propagation Delay & Layout
url: https://www.youtube.com/watch?v=4VTtkF5fzMM
source: youtube-asr
timestamps: {"0": 0, "1": 10, "2": 30, "3": 45, "4": 65, "5": 88, "6": 101, "7": 119, "8": 132, "9": 148, "10": 162, "11": 176, "12": 201, "13": 212, "14": 224, "15": 243, "16": 263, "17": 293, "18": 311, "19": 330, "20": 349, "21": 358, "22": 373, "23": 391, "24": 413, "25": 427, "26": 444, "27": 464, "28": 476, "29": 490, "30": 503, "31": 518, "32": 530, "33": 543, "34": 555, "35": 564, "36": 579, "37": 590, "38": 609, "39": 620, "40": 633, "41": 644, "42": 658, "43": 682, "44": 692, "45": 715, "46": 727, "47": 742, "48": 752, "49": 767, "50": 785, "51": 800, "52": 810, "53": 829, "54": 844, "55": 861, "56": 869, "57": 879, "58": 893, "59": 903, "60": 919, "61": 930, "62": 942, "63": 955, "64": 968, "65": 975, "66": 985, "67": 1003, "68": 1013, "69": 1030, "70": 1042, "71": 1057, "72": 1075, "73": 1085, "74": 1096, "75": 1114, "76": 1132, "77": 1156, "78": 1177, "79": 1190, "80": 1200, "81": 1219, "82": 1228, "83": 1238, "84": 1253, "85": 1262, "86": 1278, "87": 1291, "88": 1300, "89": 1311, "90": 1323, "91": 1339, "92": 1349, "93": 1362, "94": 1377, "95": 1388, "96": 1401, "97": 1409, "98": 1424, "99": 1441, "100": 1456, "101": 1468, "102": 1480, "103": 1492, "104": 1508, "105": 1528, "106": 1540, "107": 1550, "108": 1568, "109": 1577, "110": 1603, "111": 1609, "112": 1621, "113": 1640, "114": 1656, "115": 1675, "116": 1684, "117": 1706, "118": 1719, "119": 1730, "120": 1741, "121": 1752, "122": 1762, "123": 1778, "124": 1788, "125": 1801, "126": 1813, "127": 1831, "128": 1842, "129": 1862, "130": 1873, "131": 1885, "132": 1900, "133": 1911, "134": 1922, "135": 1936, "136": 1946, "137": 1958, "138": 1978, "139": 1999, "140": 2009, "141": 2017, "142": 2030, "143": 2040, "144": 2055, "145": 2064, "146": 2076, "147": 2086, "148": 2106, "149": 2115, "150": 2127, "151": 2144, "152": 2155, "153": 2166, "154": 2176, "155": 2187, "156": 2196, "157": 2222, "158": 2237, "159": 2247, "160": 2256, "161": 2267, "162": 2276, "163": 2297, "164": 2305, "165": 2320, "166": 2331, "167": 2341}
---

**Dave Jones:** Hi, this video was inspired from a tweet that I got and it was from someone by the awesome name of Johnny Cage. I love us. Ferris tweets now. Fantastic.

**Dave Jones:** Absolute that's a winning name. I love it. Johnny Cage. Not this cash rubbish. It's Cage. Anyway, and there's Ben. Hi Ben. He's in on the action, too. And basically the question started out being I'm seeing a lot of 4 8-bit digital computer project using TTL logic.

**Dave Jones:** Um from limited FPGA experience, I know that meeting timing is critical for a functioning design. Yet on these simple projects, nobody seems to talk about this and talks about signal propagation delay through the wires is much faster than through digital logic.

**Dave Jones:** Can a design like this be routed that these constraint without the constraints being violated? What frequency is this relevant? And he talks about that what could be problematic like routing a clock signal too far away from registers and other things where they have to go through other gates and take other paths on the PCB and it it gets complicated.

**Dave Jones:** At what point does it become an issue and he'd like someone to clarify this. And Ben asked, "What's the question?" I guess the question is for simple slow 4 8-bit computers, for example, the Gigatron, is propagation delay for digital signals an issue in the design layout of the board and at what clock frequency roughly would this become a big issue?

**Dave Jones:** Well, this opens a rather big can of worms. It's in some respects fairly easy to clarify. In other respects, well, no, we have to chase a red herring down a rabbit hole yet again.

**Dave Jones:** But it's something a lot of people have asked me about over the years and that is what point do I have to start doing these serpentine traces in a design, for example, to match the length of the traces going to memory and and stuff like that.

**Dave Jones:** Like, why and at what point and at what frequency do you do this? Well, I I kind of replied this in my tweet here. It only becomes an issue really at sort of like DDR level speeds.

**Dave Jones:** Like, you know, when you start talking 100 MHz, couple hundred MHz of clock rates and stuff like that. But, not necessarily, but in generally for high-speed design like this cuz most people are not going to design their own, you know, TTL computer like this.

**Dave Jones:** But, uh FPGA stuff, for example, has timing requirements and there are specific timing analysis tools that you can use inside FPGAs, but that's a whole 'nother can do a year's worth of a series of videos on uh just that issue.

**Dave Jones:** But, it basically on DDR or double data rate memory, which if you don't know, uh DDR stands for double data rate, and that's when uh data is actually clocked on both the positive and the negative edge.

**Dave Jones:** So, twice per clock cycle. And the first thing I mentioned in my tweet is the traditional rule of thumb, which you must know when you're designing electronics, laying out boards, and stuff like that, is the signal propagation through a trace on a PCB is approximately 1 ns of propagation delay for every 15 cm or 6 in for you Yanks of uh PCB trace.

**Dave Jones:** So, you've got a a trace which goes from here over to here, and it's 15 cm long, it takes 1 ns for that signal to travel across your board like that.

**Dave Jones:** So, if you've got your CPU over here and your memory over here, like 15 cm away, for example, then it's a 1 ns propagation propagation delay from your CPU to your chip.

**Dave Jones:** But, more importantly, and the difference with serpentine traces and trace length matching, which is what this video is really going to be about and why you sometimes have to at what point you really think about having to do this sort of thing is that um often you can't route all your traces across.

**Dave Jones:** Ideally, you should you should prioritize when you're routing out PCBs, you should prioritize high-speed memory buses and things like that. But let's just say for the extreme example I put in Twitter here is that if you had one of your signals for example, one of your data pins take an extra 15 cm path to all your other data pins.

**Dave Jones:** So that's a real extreme example of a really bad constrained PCB layout, but even then that'd only be a 1 ns difference. So if you look at a 100 MHz DDR memory, which clocks on both cycles, so you've got 10 ns for one cycle, but because it clocks on both the positive and negative edge, it's half that or every 5 ns, you've got a 1 ns delay in there for your 5 ns

**Dave Jones:** uh you know, clocking intervals for your data. So that really it starts to become a very significant issue uh at that point. But that's for 100 MHz, but that's for extreme case of 15 cm difference between your best-case signal and your worst-case signal.

**Dave Jones:** But it gets crazy complicated with a design like the Gigatron, which is a TTL computer like this because well, okay, there's memory here and there's memory over here, but all these registers and everything else in the actual processor, it's all over the shop.

**Dave Jones:** And really, when you're laying out something like this, you wouldn't put any thought into really the layout of this and optimizing it for speed. You may, if you're going after the absolute best possible speed you could for something like this, but generally you wouldn't bother.

**Dave Jones:** You'd just end up with what you end up with. So, when you finish your design, your layout, you build it up, and it works. The thing with these sort of computers is you just want them to work, right?

**Dave Jones:** You don't care whether it works at, you know, 9 MHz or 10 MHz, for example. Not really that important. It's going to work at several megs, for example. I think the Gigatron, I think I've tested it up to about 8 MHz, and it works.

**Dave Jones:** Works over that. Uh you have to change the chips from 74 HC on here. I believe uh the designers of the Gigatron have used 74F series chips or fast TTL chips, um which reduces the propagation delay through the actual chip itself uh compared to the HC chips.

**Dave Jones:** And I think they've gotten up to, don't quote me, it's like, you know, 15 megs or something like that. But really, like, nobody cares. In theory, it is possible to actually simulate this and work out, you know, the worst possible propagation delay and at what point it would fail in your architecture of your processor and stuff like that, but uh god, you wouldn't bother.

**Dave Jones:** Really, that's just no. No. No. No. But it really becomes a big deal on a complex design like uh something like this. This is a 12-layer open-source hardware. I'll link it in down below.

**Dave Jones:** It's um some Argentinian thing. Fantastic. Anyway, it's a Xilinx Kintex a 7 FPGA with two ARM Cortex A9 processors in it. It's got 1 gig of DDR3 memory. And if you have a look at here, it's a 12-layer board.

**Dave Jones:** It's got the It's got big-ass processor on here. Here's your DDR memory. Here's your expansion. And look look at all of these serpentining traces. They do this to match the trace lengths, so there's no uh skew or difference between one data pin and another data pin or a clock pin and a or another clock pin or something like that.

**Dave Jones:** They even them out not only to memory but also to this expansion like header up here as well. So, you know, it and not only between signals but also between individual pairs.

**Dave Jones:** We'll get into that as well. But as I said in my tweet, DDR3 well, DDR level memory is sort of once you start getting into the hundreds of megahertz, this is where it really starts to matter.

**Dave Jones:** So, anyway, I thought we'd just do a little dive into some data sheets and stuff like that and just find out exactly why do you have to do this and at what speed does it matter?

**Dave Jones:** Well, let's go into it. But unfortunately, there's some one thing I'm going to leave out of this video and I have to. That will be signal integrity because you'll notice that the these these traces down here, these are thick traces.

**Dave Jones:** They are thicker than your other signal lines going signal lines going around here like this. This means that they're obviously doing like a controlled impedance trace cuz there's a big ground plane underneath here.

**Dave Jones:** So, you can see see that there. So, signal integrity is another thing entirely even on this which I've done a video on like a removing bypass capacitors months in on a board like this.

**Dave Jones:** Does it have an effect? Well, on on something like this DDR level memory on your computers that you're familiar with? Um yeah, it's a big deal. Signal termination, signal integrity, stuff like that.

**Dave Jones:** You'll see termination resistors. There's different techniques for termination and stuff like Oh yeah, have they got termination resistors at the end here? Um I don't I haven't looked into this design.

**Dave Jones:** But anyway, that also factors into the equation of not just propagation delay of signals but signal integrity as well cuz then you can get reflections and I that. Like, blah.

**Dave Jones:** Truly, if you want to analyze this sort of stuff properly, you're going to take signal integrity into account as well. But today, we're only going to look at signal propagation delay times.

**Dave Jones:** And set up and hold times and all that sort of jazz. Let's get into it. So, this propagation delay rule-of-thumb which I've been talking about, it comes about because a propagation delay on a signal on a bit of copper on a PCB is different than it is through a wire or free air because of the dielectric constant of the PCB material.

**Dave Jones:** What are the fiberglass that it's actually made up with? And you've maybe heard dielectric constant before. A typical FR4 PCB might be four or four and a half dielectric constant.

**Dave Jones:** And there's formulas, I'll link in this down below. This is from uh just Sierra Circuits. And there's formulas where you can calculate this sort of stuff. And you can even go deeper down into the material science of it and things like that.

**Dave Jones:** But basically, er is the dielectric material of constant of the material. But it basically comes down to here it is uh 6 in per nanosecond for a typical thing.

**Dave Jones:** That's what it is. But it varies between PCBs cuz the materials vary. Like, standard FR4 can vary quite significantly in in its dielectric uh constant. And there's better materials.

**Dave Jones:** For example, Rogers Corporation make very expensive, very schmick PCB materials for RF applications and other controlled impedance applications. If you're doing a a really high-end DDR4 memory board or something like that where the data rates are phenomenal, you know, high-speed FPGA and all sorts of, you know, memory interconnects and architecture and stuff like that.

**Dave Jones:** Well, you might be using a more controlled impedance PCB cuz something like this, look, you can choose your dielectric constant from 3 to 10. Knock yourself out. Look at this.

**Dave Jones:** This one down here, it's PTFE ceramic dielectric constant 3 plus minus .04. Thank you very much. Real expensive exotic materials you can really do your controlled impedance traces, but you know, for most designers, just a regular FR4 and just knowing roughly what the dielectric constant is and using a rule of thumb, good enough.

**Dave Jones:** And if we're going to a PCB calculator like this Saturn one, which I highly recommend is the best out there, then we can have a look for a typical trace on top of your PCB like this, typical propagation delay.

**Dave Jones:** They have it for picoseconds in centimeters and you'll enter your ER up here, your dielectric constant. Uh you know, like a typical 4.5 for example, and you solve and it's basically 57.6 picoseconds per centimeter propagation delay.

**Dave Jones:** And if you change that to four and it's changing from 57 to 54, even if you go down to extreme three or something like that, you know, it's not varying by a huge amount.

**Dave Jones:** So, if your designs are that critical on your propagation delay to actually work, then either you're working on some bleeding edge system at daylight speeds or you're just you're doing it wrong.

**Dave Jones:** You're You're being too critical on your design constraints. You're not being loosey-goosey enough. Yeah, you could come a gutser um and really you shouldn't on something like this. You should be operating with reasonably good design margins where using a rule of thumb is more than enough.

**Dave Jones:** And you'll notice, of course, this doesn't change with frequency. There's 500 MHz, let's drop down to 100. Oh, that doesn't change any, does it? No, it doesn't because it makes absolutely the frequency doesn't matter.

**Dave Jones:** It's the just the propagation delay the signal. And of course, that can change with how your signal's routed on your PCB. As I said, this one is on the top layer with your ground plane underneath like this.

**Dave Jones:** Well, that's microstrip, of course, and I've I've actually tweaked my dielectric constant to give a spot-on almost spot-on 50 ohms 50 ohms I'm thinking impedance up here. No, 50 picoseconds per centimeter here.

**Dave Jones:** So, let's actually change that to microstrip embedded. Oh, we've gone up to 55 because it's embedded inside your dielectric material. That's the green part there. And stripline like that, 59.

**Dave Jones:** So, look, it's you know, it's gone up fairly significantly. That's 20% difference right there in your propagation delay just because you've put your signal in there. So, if you've got your 12-layer board like this one here, good luck trying to You can get simulators for this sort of stuff.

**Dave Jones:** You know, you can do it field solvers and like real expensive uh software to do it. But, look Look at all these Look at all these serpentine squiggly traces in here.

**Dave Jones:** So, yeah, trying to figure out like exact propagation delays of all this sort of stuff. That's why you should be designing with like a rule of thumb with margins kind of thing.

**Dave Jones:** Like it's it's just yeah, to try to analyze this. You might have to, as I said, bleeding-edge stuff. Yeah, maybe. Okay, knock yourself out. But, um generally, yeah, you shouldn't have to.

**Dave Jones:** But, be aware. That matters. Even the weave of the PCB dielectric material, you'll notice like if you have a look at the construction of it, it's weaved like this.

**Dave Jones:** You know, it's a woven pattern. And if you run your signal actually on top of one of the weaves and the or then like in the direction that it's going, you get a different dielectric constant than if you do if it's passing over the ones running in the other direction like that.

**Dave Jones:** That can matter as well. That can change your propagation delay right there and your signal integrity and everything else. So, let's take a look at a a discrete design like this Gigatron.

**Dave Jones:** It uses the absolute classic 62256 SRAM, which has been around from day dot 32K SRAM chip and it's available in fast access times from uh 45 up to 85 nanoseconds.

**Dave Jones:** So, let's take the fastest 45 nanoseconds. Right off the bat there, you've got the fastest design you can possibly get uh for your computer using this um and nothing else considered is about 22.2 MHz.

**Dave Jones:** Um that's as fast as you can access the memory on this thing. You can't cycle it any quicker than that. So, right off the bat, you know your rule of thumb that 15 cm per 1 nanosecond.

**Dave Jones:** So, right off the bat, if you Please excuse the crudity of model. Didn't have time to build it scale or to paint it. Um let's say this is your 62256 chip here.

**Dave Jones:** This is the physical layout of board. Let's say this is your processor chip over here. I know the address lines don't match up. You don't actually have to match up the address lines, by the way.

**Dave Jones:** Little routing trick there. You can actually Depends on the design. You can actually It doesn't matter where in this memory you actually store something. Depends on the design. But, you can actually swap data and address lines because it's just a random array of It's just an array of It's just a memory array in there.

**Dave Jones:** Do you care that it stores it in this part of the thing? No? No. You know, you've got some routing constraints like this. Uh this is what I was talking about before about prioritizing your layout.

**Dave Jones:** If you knew that memory speed was important, you wouldn't whack memory on the other side of a processor over here, memory over here, for example, and then one corner in there you've got to cross the board and you've got to go all higgledy-piggledy with your traces and everything else.

**Dave Jones:** You wouldn't do it. Anyway, but look, this trace here is just by natural layout is going to be half the length, less than half the length of the one on the outside here.

**Dave Jones:** That could be 30 cm. Let's say it's extreme like that, right? That's only 2 ns out of our 45 ns. Whoop-dee-doo. It's not just the layout of the board is not going to affect a design like this.

**Dave Jones:** Not a chance. That's why computer designers in the '80s really didn't have to take this into account in general sense. They They might have for various like like niche parts of the design, but overall in the basic scheme of things, no, you just didn't care.

**Dave Jones:** But of course, this is where you get up to your setup and hold times and you can get into our way. Yeah, there's our Yeah, there's our read timing waveforms.

**Dave Jones:** Brilliant. If you're doing serious design, and maybe if you want me to do a video on how to read these kinds of timing diagrams and things like that, please please let me know cuz that's an interesting thing.

**Dave Jones:** How do you What is all the What are these things mean? What is it What is all this? I don't get it. You know, anyway, propagation delay like for example, the address or the data might have to be on the pins a certain amount of time before the clock pulse comes along and that's called your setup time.

**Dave Jones:** Your data or your address your input data to your chip has to be set up before that clock edge comes along. But in this particular case, aha, of course, there's nothing in the read cycle for the setup, but if we go into write, address setup time, there you go.

**Dave Jones:** It's actually 0 ns. So there is no address requirement. So your data has to doesn't have to be there. So you've got Well, let's say that your clock rate was 20 MHz for example, you've got a whole 50 ns to get all of your address signals over there before you clock in uh that address cuz there's zero setup time required.

**Dave Jones:** But, depending on how your computer works, your processor, your processor architecture, or your FPGA, whatever it is that you're reading the data, okay, you can you request your data, for example, it comes out of the chip, but it might be latched into the processor on one of the half cycles, for example, opposite clock edge to what you used to get it out of the chip.

**Dave Jones:** So, you might only have your 25 nanoseconds to get your data across. And then there might be setup time on that particular uh data and things like that. So, yeah, you might have to go into that sort of detail.

**Dave Jones:** And when you're talking about a TTL computer like this, where the processor is actually made up of all these chips, each individual chip, the register in your chip will have its own propagation delay time.

**Dave Jones:** And as I said, trying to analyze something like that is just nuts. That's why you wouldn't bother. You'd go mentally insane. You'd have to call the white van and take you away because you just you build it up and you see if it works and then you adjust your clock up and oh, look, it works up to 10 MHz.

**Dave Jones:** Beauty, but it doesn't work at 11. Nah, whatever. Like if you went in if you're a sane enough, you could go in and look at Let's go down, have a look at the propagation delays.

**Dave Jones:** Here they are. You just scroll down until you see the nanoseconds-es. 12 nanoseconds, that's typical, but that's going to vary with voltage, with temperature, with all sorts of stuff.

**Dave Jones:** So, there you go. I like you know, right there, you combine that with all the other dozens and dozens and dozens of chips on here. But, as I said, you could use a faster logic 74F, for example, it's going to have a faster propagation delay time than this.

**Dave Jones:** So, yeah, you might be able to eke out a more speed more speed from your design by doing that. But, generally, yeah, you're going to be constrained in these TTL type designs drastically.

**Dave Jones:** All right, let's take a quick look at DDR memory. As I said, on this uh processor board that which uses DDR4 memory. Now, this won't be a DDR3 tutorial cuz no, that's a 1-hour video in its own right.

**Dave Jones:** Um this we'll just have a quick look at the data sheet here. So, here's our termination resistors over here, 40.2 ohms. They go to a specific midpoint termination voltage, and I won't go into the reasons why.

**Dave Jones:** It's a complex issue if you really want to get into termination of DDR memory and all that sort of jazz. Anyway, you don't pull them high, you don't pull them low.

**Dave Jones:** It's It's a to a voltage series voltage source. Anyway, um yeah, this is the memory chip that we're using, DDR3. So, let's Here we go. It's a Micron jobbie, and it's you know, it's it's pretty new tech.

**Dave Jones:** Let's Let's take a look at this thing. These are our cycle times down here. Look at this, 938 picoseconds. We're talking puffs here, none of this nanosecond rubbish, right?

**Dave Jones:** For the DDR3 2133. Not sure what value we have on this design, but we're down into the 1-nanosecond class timing here, right? Then this is just cycle, let alone uh propagation delay and skew between signals.

**Dave Jones:** You'll hear me start talking more about skew rather than uh propagation delay at this point. Because what we start talking about now is a difference between one signal and another.

**Dave Jones:** So, the skew between the signals. You want everything to be clocked all at the same time. You want all If you send out an address from your processor to your memory chip, you want them all all the pins to arrive there at the same time.

**Dave Jones:** That's why you want a length match. And when you're down in cycle times like 1 nanosecond, it's really going to matter. And these data sheets have 200-plus pages for a reason.

**Dave Jones:** I can't possibly go into all the details of driving and memory. I think just the state diagram is enough to scare you all away. Well, as always with these videos, I didn't actually plan before I went ahead with this.

**Dave Jones:** I just pressed record and then and see what happens. And I started going through the data sheet and I'm just like my eyes are rolling. How do I increase the signal-to-noise ratio here and pull out the important stuff?

**Dave Jones:** So I went, "Oh no, I look bugger it. Micron have probably got an app note that that that will make it a bit easier a little bit easier for us anyway.

**Dave Jones:** And sure enough they do. I'll link it in down below. Point-to-point simulation process. And this talks about your timing budget, which is a big thing that you'll hear in these types of designs when you're like you wouldn't always do this.

**Dave Jones:** If you're laying out this board here, right? Like you wouldn't I would not go in and do a timing budget for for something like this. I I just really wouldn't like waste my time doing Sometimes it's not a waste of time, but I really wouldn't bother.

**Dave Jones:** All I would know is that right, let's just match the lengths of the traces and that's it. And and just be done with it, right? You don't have to worry about stuff like like how how close do I need to match?

**Dave Jones:** Just match them to within not like half a bee's dick, you know, 5 mm or something like that. Set some constraint in there. Match all of the lines to the DDR together.

**Dave Jones:** And then and then you don't have to worry about doing the sorts of stuff which we're about to take a look at here, looking at analyzing error budgets. There's a clock source, there's a transmitter which might be your processor {slash} FPGA.

**Dave Jones:** For example, there's data and strobe lines and there's receiver and these all have skew or propagation delay. Just think of skew and propagation delay is the same they're effectively the same thing.

**Dave Jones:** They you've got the transmitter skew here. You've got the PCB skew, which is the thing we're interested in, and the receiver skew as well. Like the internal setup and hold propagation delay times inside the chip and the transmitter as well when it's sending data back.

**Dave Jones:** So then they talk about the signal integrity process. As I said, we won't talk about signal integrity, but it does impact these things. So anyway, in this particular case, they've got a 266 MHz period, which is a 3.75 ns half period because it's it's DDR, double data rate.

**Dave Jones:** So we've got a setup budget of 1.8 nano 1.875 ns cuz we're working 1,800 ps. We're now down in the picosecond region here, right? This is This is real engineering.

**Dave Jones:** And then we've got our hold budget of 1875. And then they've they've pulled out the transmitter skew. Well, they tell you where they get it from, the vendor data sheet here.

**Dave Jones:** And then they then they tell you that what budget do we have left over? We have 585 ps for our PCB skew. So that's the longest period that we can afford the biggest mismatch we can afford to have between the traces on our PCB.

**Dave Jones:** And it it'll might tell you which traces we go down into, but basically setup and hold times are exactly the same. So right off the bat, we get our confuser here.

**Dave Jones:** And so 150 mm, none of that inches rubbish. 150 mm uh times 0.585 cuz it's a nano per nanosecond. So we're talking uh 87 mm, 87 mm difference that we can have, maximum difference, between Let's just say all of our traces for our chip.

**Dave Jones:** We don't know exactly which ones yet, but you know, let's just keep it simple. So there you go. Up to 85 That that 87. That sounds like a lot.

**Dave Jones:** And we won't mention voltage margin and stuff like that. Let's just Let's just not go there. This is an interesting diagram. It shows the skew and how the the data's only valid within side here.

**Dave Jones:** If your skew, let's say your skew is this big here, then it would start impacting into the squeeze in that the eye narrows. It's called the eye, and it narrows and narrows and narrows until well, your operating valid window for your data is not full.

**Dave Jones:** And then your system just completely falls over. And the reason we don't go into signal integrity is because well, yeah. Just gets a bit complicated, don't it? But aha, the board skew budget, we have to actually break that down even further.

**Dave Jones:** It gets more complicated. The components that make up the board skew budget include ISI, Vref noise, path length mismatch, which is the main thing that we're talking about, crosstalk, input capacitance mismatch, termination resistor tolerance, the type of termination, where the termination resistors are.

**Dave Jones:** Nuts. So, we can look at the different components here, and they break them down, which is really good. First of all, we've got the ISI, which is intersymbol interference.

**Dave Jones:** What that basically means is a symbol is is what's inside the eye here, right? The the type of data that you've got in there, and due to reflections on your PCB, you might have one data interfering the previous data interfering with the new data because then you've got some overshoot, undershoot, some reflections coming back, and that can interfere.

**Dave Jones:** Sometimes, sometimes not. It doesn't always happen cuz your data's always changing. So, some symbols, some the combination of data may interfere with another combination of data if they're in the right order, depending on termination.

**Dave Jones:** So, like it's it's to do with the data that you're actually transferring, not just the fact that you've got your termination right. Anyway, into symbol interference. And And that's what it tells you.

**Dave Jones:** It can cause by the bus running faster than it can settle, basically. Um cuz you need time for it to settle before you send the next data so that your data doesn't interfere with from the previous data due to signal integrity issues.

**Dave Jones:** So, anyway, that is a component of that. And then you got crosstalk between your signals because your signals are right next to each other and they're they're talking and they're coupling.

**Dave Jones:** And if you're routing them, they're typically running parallel like that. And when you have traces running parallel like that with no ground shield in between them, you get capacitive coupling.

**Dave Jones:** If traces just cross like that, the crosstalk's very little because there's little mutual capacitance between them. But when you're running buses like this all the way up, then the crosstalk can be very serious.

**Dave Jones:** And we won't go into differential mode, common mode. We get into signal integrity. Come on. And coupled circuits is all just part of that. We won't talk about crosstalk effects, blah blah blah.

**Dave Jones:** VREF noise, that's a thing. As I said, the termination the volt is terminated to a mid-rail voltage reference. You can actually get specific voltage reference DDR termination chips that are actually designed to do this.

**Dave Jones:** And the noise of these reference voltages impacts your budget for your timing budget for the amount of skew that you can have on your PCB, the difference in your traces.

**Dave Jones:** So, for example, with a 0.5 V per second edge rate and a 50 mV VREF noise, it's it's 200 picoseconds of And there you go. It's extremely important aspect of DDR SDRAM design.

**Dave Jones:** When laying out the trace, it should be as wide as possible to reduce inductance on the line. So, really, here's where signal integrity does matter just on getting your voltage reference.

**Dave Jones:** And I've done DDR designs where I've decoupled and inductor isolated the V ref to buggery because it it it matters. And then they tell you about the space into adjacent signals from the V ref cuz you typically want to keep your V ref isolated from crosstalk from other signals as well.

**Dave Jones:** So, not only crosstalk between signals, but crosstalk between your signals and your voltage reference for your termination resistors. And this has a large impact on your total timing budget.

**Dave Jones:** And here we were just going to talk about like propagation delay of traces. No, it's more than that. Then you've got input capacitance variation. Look at your data sheet.

**Dave Jones:** We could go in and see what our input capacitance variation is. Should we do that? Oh, yeah, why not? Look at all this ODT sensitivity definition to do with the IO calibration.

**Dave Jones:** Oh. I found it. You search for capacitance and Bob's your uncle. Look at this. Input-output capacitance. Ta-da! But look at this, the variation 1.4 to 2.5. That can ruin someone's day.

**Dave Jones:** And someone could be you. And would you like single-ended or differential fries with that, sir? So, anyway, yeah, that could matter. Let's get down here. Here we go. Here's our timing budget, okay?

**Dave Jones:** So, this is You remember this was a transmitter skew, the receiver skew, and all of this stuff down here is the stuff that's made up is our budget for our total PCB skew, basically.

**Dave Jones:** But, if you have a look here, the path length mismatch, that's all we got. That's all we got. Calculation from spec when you subtract all the other stuff from the total, what was it?

**Dave Jones:** The 580 or whatever picoseconds that we had, when you take out crosstalk and and intersymbol interference and V ref noise, it it doesn't leave you much budget. 30 picoseconds.

**Dave Jones:** So, yeah. What's that? Get the confuser out again. So, average PCB at, you know, the our rule of thumb, 150 uh millimeters uh times point uh 05, 50 picoseconds, we're talking 7.5 mm.

**Dave Jones:** There you go. So, 7.5 mm just just off the bat there is kind of like the worst case we could get if we were using the laying out this board with this chip, and that would include the the, you know, the PCB weave uh problems, variation in the dielectric constant of the PCB material, stuff like that, right?

**Dave Jones:** We're not including any of that. So, right off the bat there, seven and a half. So, good design prudence would say you would at least halve that to be on the safe side.

**Dave Jones:** So, you know, as I said, like you'd be down in the millimeters before I kind of guessed, you know, did did say the lesson like 5 mm difference. There you go.

**Dave Jones:** That's why. Um because, right? So, you'd say, "Oh, like a couple of millimeters difference, for example." Because when when you're laying out this kind of PCB, you can do it.

**Dave Jones:** I've done it without the uh the tools to automatically uh drag and do the, you know, when you drag your if you differential pair or your single uh pair to match the lengths.

**Dave Jones:** I've done it without the automated tools to do that. But when you have a PCB tool, and I believe KiCad, although I haven't actually used it, believe KiCad actually does have route, here it is, tune track length, tune uh differential pair length, and things like that.

**Dave Jones:** I haven't used it. Anyway, we can somehow tune that, and we can set the parameters and things like that. I haven't used this in KiCad. Um so, please forgive me.

**Dave Jones:** But anyway, when you've got an automated tool to do it, you may as well set fairly precise constraints. You know, there's no reason why it can't be we a millimeter or two, something like that.

**Dave Jones:** So, you wouldn't go, "Oh, I've got 7.5 mm to play with cuz I calculated my timing budget. I'm a hero." And I spent a whole week working on my timing budget.

**Dave Jones:** And no, just just lay out your board so that you've got no skew between the signals. They're matched to within a millimeter or two. So, anyway, that is why you see all of these little zigzaggy serpentine traces like this on boards is because they're trying to match the lengths.

**Dave Jones:** In this case, which is what's this signal? There There you go. Yeah, this is DDR. So, this is actually a differential pair. Okay, so this is a the positive and negative.

**Dave Jones:** You can see it. The DQS3 negative and positive. So, they're actually So, this is why you're keeping the pairs going like that. And this one is a good example.

**Dave Jones:** Just happens to be a good example because look, not only do you have to match the length of this pair here to data pair four and five and six and seven, you match those lengths between the pairs, you also match the difference.

**Dave Jones:** This is why it's got an extra little kink in here. Look at this little kink going out here like this. And the other one doesn't have it because you're matching the difference between uh D3 positive and negative.

**Dave Jones:** So, you match the length there. And your tool your automated tool can actually do this. And and you can do it manually. I've done lots of boards where I've had to manually add in the squiggles.

**Dave Jones:** And it's a lot more work. So, why these tools are valuable in a PCB when you're laying out DDR memory is you know, it can save you a lot of time.

**Dave Jones:** Can do the push and shove. And it does You just set it up, you know, I want this maximum difference between your pairs like this. So, it'll add in these little kinks.

**Dave Jones:** There's another little kink out here as well. You can see that. And and then it'll also match those between the pairs as well when you when you manually laying them out.

**Dave Jones:** Or if you're auto routing, but don't auto route. Manually route. Anyway, that's why you have these two different types of serpentine traces like this, both within a differential pair and between differential pairs or between single-ended traces like D0 and to D7 and A0 to A7 or whatever it is on your memory.

**Dave Jones:** So, that's it. There you go. So, yeah, this video's long enough. Sorry, but that's basically what it comes down to is timing budgets. And timing budgets are critical, but as I said, you don't have to go in and do a timing budget.

**Dave Jones:** You're laying out a board with your DDR memory or whatever. You know it's critical because I've told you so. Everyone's told you so. Micron's told you so. Every Tom, Dick, and Harry's told you so.

**Dave Jones:** And you can go in and analyze it yourself, but you don't have to. If I was laying out this board, as I said, I would just set those constraints to a millimeter or something like that.

**Dave Jones:** Something reasonable. Don't set it to like 0.01 mm, half a bee's dick, cuz the software's just going to go can't do it. Sorry. Yeah, it's Don't gild the lily there.

**Dave Jones:** But that's all you have to do. Just do that. Know it's critical. Put it in and then you've got other signal integrity things to worry about. In fact, it might tell you that Yeah, it does.

**Dave Jones:** There you go. They talk about split return paths here. So, if you've got your never split your ground planes. If you add a little cut out in your ground plane like that, not a physical cut out, a routed out part of your board, but if you if some reason didn't flood fill your ground under there, and it's going to take a longer path, you've just ruined your day right there again.

**Dave Jones:** You've ruined your timing budget. You've ruined your signal integrity. You've ruined everything. And well, yeah, they're going to sack your ass because you didn't know how to lay out boards.

**Dave Jones:** So, there you go. I hope you liked that video. Can't as I said, can do video whole video series of just on signal integrity, just on doing analyzing DDR timing budgets and and things like that.

**Dave Jones:** Anyway, I hope you learned something from the video. And if you did, please give it a big thumbs up. And if you want to see more videos of, you know, more specific stuff like this thing, please let me know.

**Dave Jones:** And occasionally I see a tweet like that and it just goes, "Oh, yeah, I'll I'll do a video on that. I'll just press record and have a rant for half an hour." Anyway, I hope you liked it.

**Dave Jones:** As always, discuss down below in the comments or over on the EEVblog forum. Catch you next time.
