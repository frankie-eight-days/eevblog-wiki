---
video_id: WdYBL-_8-oo
title: EEVblog 1753 - Designing a 2000V Isolated Oscilloscope (Cleverscope)
url: https://www.youtube.com/watch?v=WdYBL-_8-oo
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 20, "3": 32, "4": 44, "5": 56, "6": 64, "7": 75, "8": 90, "9": 99, "10": 108, "11": 115, "12": 124, "13": 140, "14": 148, "15": 158, "16": 167, "17": 173, "18": 186, "19": 196, "20": 203, "21": 216, "22": 226, "23": 235, "24": 243, "25": 262, "26": 270, "27": 279, "28": 295, "29": 310, "30": 317, "31": 334, "32": 342, "33": 351, "34": 364, "35": 384, "36": 396, "37": 407, "38": 419, "39": 427, "40": 437, "41": 446, "42": 460, "43": 472, "44": 481, "45": 487, "46": 498, "47": 508, "48": 518, "49": 528, "50": 536, "51": 546, "52": 555, "53": 564, "54": 571, "55": 583, "56": 593, "57": 603, "58": 613, "59": 622, "60": 631, "61": 639, "62": 650, "63": 662, "64": 670, "65": 681, "66": 695, "67": 704, "68": 717, "69": 728, "70": 735, "71": 748, "72": 758, "73": 767, "74": 776, "75": 786, "76": 797, "77": 810, "78": 821, "79": 831, "80": 839, "81": 850, "82": 857, "83": 868, "84": 880, "85": 889, "86": 903, "87": 917, "88": 927, "89": 943, "90": 952, "91": 964, "92": 981, "93": 989, "94": 1000, "95": 1013, "96": 1020, "97": 1030, "98": 1041, "99": 1048, "100": 1058, "101": 1074, "102": 1088, "103": 1096, "104": 1104, "105": 1110, "106": 1122, "107": 1132, "108": 1146, "109": 1158, "110": 1170, "111": 1183, "112": 1194, "113": 1202, "114": 1211, "115": 1219, "116": 1230, "117": 1236, "118": 1246, "119": 1254, "120": 1261, "121": 1270, "122": 1283, "123": 1294, "124": 1306, "125": 1312, "126": 1326, "127": 1335, "128": 1345, "129": 1357, "130": 1369, "131": 1377, "132": 1386, "133": 1395, "134": 1407, "135": 1418, "136": 1429, "137": 1440, "138": 1447, "139": 1454, "140": 1466, "141": 1472, "142": 1486, "143": 1496, "144": 1506, "145": 1521, "146": 1531, "147": 1538, "148": 1549, "149": 1558, "150": 1572, "151": 1580, "152": 1588}
---

**Dave Jones:** Hi, I'm here at the Cleverscope stand. And you might remember but from Cleverscope, the designer of the Cleverscope. And we What, 8 years ago you told me? >> I talked to you, Dave.

**Dave Jones:** >> About the original design of the Cleverscope, but you've got a new one. >> Well, it's not that new, but it's you know, but it's new in 8 years.

**Dave Jones:** >> And we're going to look we've got it open here. And Bart's the designer, he's going to tell us all about this. Um tell us the ins and outs of designing a four-channel totally isolated high high voltage isolator.

**Dave Jones:** What's what's the basic specs? >> data there. >> 2 kV per channel? >> Yep. >> Yep. What what bandwidth we talking about? >> MHz bandwidth. >> 200 meg bandwidth, which is hard at that sort of yeah.

**Dave Jones:** >> Yeah, it's 200 MHz bandwidth, 500 MHz sampling rate. 14 bits. I don't know if any of that's useful to you. >> Absolutely. >> Okay. The ADC is right underneath where my finger is.

**Dave Jones:** >> Yep. >> It's not open, sorry. >> That's all right. >> It's a bit hard to see. The can is just closed. >> Sure. >> Um and then a little bit of circuitry to give us two ranges, 0.8 and 8 volts.

**Dave Jones:** Not many ranges. We use probes to get the range we want. >> Yep. >> So, this is a 100 100 times probe and off the shelf. >> 100 X, yep.

**Dave Jones:** >> 100 X times 8 800 volts. There you go. >> Nice. >> So, then it connects using a what's called a QSFP fiber cable, an optical cable. These are These are used in data centers yep all over the world.

**Dave Jones:** >> Easy to get. >> And they're cheap and they're relatively cheap. And all the design work's take all the high speed >> All the difficult things taken out of them for us.

**Dave Jones:** We just have to plug the bloody things in. Sorry. >> That's all right. We can we can say bloody here on the EEVblog. Bloody designers. Anyway. >> It cost us so much.

**Dave Jones:** The greasy old one the old one cost us a lot of grease. >> Yeah, cuz you you designed that yourself back in the day back in the day. >> did.

**Dave Jones:** So, we won't we've gone past that. Now, because we have a plug cap >> we thought, "Well, why don't we put a a switch under there?" And then we can switch between the one inside.

**Dave Jones:** So, this is the inside of the scope. There's a 12-layer board. >> 12-layer >> 12 Lots of 50-ohm um >> Yep. >> uh controlled impedance because we're trying to send 5 gigabits per second signals down these fibers.

**Dave Jones:** >> Of course. >> And we also have a whole lot of DDR3 RAM, which is ancient now, but you know, it's still running a data after mix. >> That's a big FPGA.

**Dave Jones:** >> And what uh >> It's an Altera one. It's a colon area five. >> Okay, RS series, yeah. >> It's got about 980 pins coming out of it. >> Yep.

**Dave Jones:** >> And they connect to everything. And at the back here we have a isolated signal generator. And we use the same power supply system. >> Okay. >> as we do here.

**Dave Jones:** >> Did you roll that yourself? >> Yes, we did. >> Yep. >> There's actually about a year of work, and we talked about this last time. >> talk about this last time.

**Dave Jones:** Yes, a year of development. >> across the board. >> Two path? >> Two path. >> Very nice. >> Very low common mode current, which is what we need cuz we don't want to inject any common mode current into the circuit we're measuring.

**Dave Jones:** >> Got you. >> Okay. So, we use the same for the signal generator. And the reason that we have the signal generator isolated is so we can do gain phase on power supplies.

**Dave Jones:** While they're alive and running. >> Yep. Okay, is that the main application market for this scope? People doing doing it for power supply design? Or is it motor drive?

**Dave Jones:** What's What's your >> It's It's anything in power electronics. >> Got it. >> Okay, uh five If we carry this on, we might get into SSTs, which we'll end on.

**Dave Jones:** >> Okay. >> Okay, which are solid state transformers, in case you didn't know. So, then of course we have USB 3, and we're missing the SFP cover there for Ethernet.

**Dave Jones:** >> Mhm. >> So, that just plugs in. It's another pluggable connector. It's great. >> Excellent. >> Um yeah, so anyway, we >> So, hang on. So, you've got your 14-bit ADC in here.

**Dave Jones:** Do you have to do any and and maybe some offset stuff as well? Did you have to do anything else to get the data to the transceiver? Is there a little knob?

**Dave Jones:** >> No, no, no. The wonderful thing about the AD the ADC we use, it's called a GSD 204 ADC. It's 6 out GSD GSD 204 um 5 gigas 5 giga bits per second data two two lanes and it can go straight into the fiber.

**Dave Jones:** >> It just goes straight in. That's brilliant. >> And the other end it goes into the FPGA and we have a decoder for it. >> Fantastic. >> So simple.

**Dave Jones:** >> Yeah. Um, any heat sinking in there? Any sort of power dissipation? Oh, well, yeah, yeah, on top, but like internally to cool it. >> So, inside we have a big thermal pad which covers the whole board.

**Dave Jones:** So, we suck the heat out of the board, which is again 12 layers and it has quite a lot of copper in it. So, we spread the heat from all these quite the ADC on it's on it's 1 and 1/2 watts and we have a clock generator which makes our 500 megahertz clock reference.

**Dave Jones:** It's another watt and there's some uh analog devices 1 gigahertz op amps. They're also pretty power hungry. >> I noticed um thermal-wise there's no fans in this thing. So, it's all passive.

**Dave Jones:** Oh, there is. Where does it go? >> There's too much heat. >> Oh, okay. Oh, yeah, that's on the top. I was going to say, yeah. >> Fan was on the top.

**Dave Jones:** >> Right, okay. Okay, so you're drawing in the air here and bringing it out here. >> Exactly. So, it goes straight past the digitizers, these these ones here. And it also it pulls the air up from the FPGA and we run it at constant temperature actually of 40° C.

**Dave Jones:** >> Okay, and you don't need a heat sink on the um exterior jobby there? >> No, because the board itself is pretty good. >> Oh, okay. >> Lots of copper in it.

**Dave Jones:** >> Okay. >> And because the air is being dragged out of it all the time, >> Yeah, it doesn't get too hot. >> We measure that it has a temperature sensor inside it.

**Dave Jones:** >> Yeah, got it. >> So we can make sure it's not too hot. >> Yep, fantastic. >> So yeah, 40 The reason we run it at 40 is and we control the fan speed to keep it at 40, so all those analog electronics stay nice and steady, don't drift around.

**Dave Jones:** >> Yep. >> So that's one of our things. >> Okay. >> No drift. Well, not much. >> Well, it's yeah, nothing consequential. >> Nothing consequential. >> I was going to say that we have this switch in here, so we can switch between the top QSFB connector and the bottom QSFB connector.

**Dave Jones:** >> Oh. >> Now this >> Oh, what is the bottom What's What's the bottom one doing? Oh, YOU CAN HAVE OUTPUT. OH. >> SO the advantage of having the bottom one is that we can switch to an external digitizer.

**Dave Jones:** Now we can't run both at the same time cuz the FPJ's not up to it. >> Got it. >> But we can switch between the two. >> Very >> So that's very handy because if the customer comes to us and says, "I've got a big safety cage.

**Dave Jones:** I've I want to measure something inside the safety cage, and I don't want to get fried. How do I do it?" >> Got it. >> Well, >> You've got a 10 10 kV Is that a real 10 kV demo there?

**Dave Jones:** >> No. >> it No, I was going to say are you with >> You know, we don't really want to kill the customer. >> kill the the the potential customers.

**Dave Jones:** >> Not really. >> Nice, but I I I I love it lit up there blue 10 kV sig. >> Yeah, well, that's how they look. They look exactly like This is a 3D printed one.

**Dave Jones:** >> Oh, okay. >> Right. Nice. Basically because it's kind of hard to get 10 kV sigs with the nice blue lettering behind them. >> Yes, exactly. Yeah, they don't exactly make those, do they?

**Dave Jones:** >> No, they don't. No, but the advantage here is is a fiber connection, and because it's digital, it can go 30 m. >> Got it. >> So say you want to Say you're at Airbus, and you want to measure from one side of a wing to the other side of the wing and look at correlation between things.

**Dave Jones:** You can do it. >> Excellent. Is that power over fiber as well? >> No, it's not. No, it's not. >> Okay. >> No. We do have a module that does power over fiber.

**Dave Jones:** Um >> Oh, so you can just plug a module in series? So it doesn't >> no, what we do is we we've got So if we go back to the back of those, you can see there's a battery box here.

**Dave Jones:** >> Oh. >> And so you can open the battery box. >> Right. >> And >> and slide in a unit and a power supply. >> I got it. Okay.

**Dave Jones:** Right. >> So That's a developmental thing. Not actually available. >> Right. And so right, so that is you can there's nothing off the shelf that allows you to do that really.

**Dave Jones:** >> Uh there is. There is, but most of the Evergo the these are mostly Evergo things. And the off-shelf can handle 2 W and we want 4. >> Oh.

**Dave Jones:** >> Okay, but they've got a new receiver which is 10 W. We can use that. >> Yep. >> So the efficiency is the big problem. Um the total round trip efficiency is about a quarter, 25%.

**Dave Jones:** So if you want 4 W, you really have to stick 16 W in to make it work. And uh that's a lot of heat you've got to get rid of.

**Dave Jones:** >> Exactly. >> Batteries are so much simpler. And they float freely. You can have 30 kV there and it doesn't matter. >> It doesn't matter a rat's. Yeah. That's great.

**Dave Jones:** >> So the utility of of having the extra socket is that we can handle putting these things far away. Inside here is exactly one of those. >> Oh, okay.

**Dave Jones:** Got you. >> There's no difference. So it was a simple thing for us. >> Yeah. >> Take one of these. >> Yep. >> Add a battery. >> Exactly. And in your case it have an external case for it.

**Dave Jones:** And uh yep. >> And away it goes. >> Excellent. >> Yeah, it has a little fan inside it, too. >> Oh, okay. Right. Just a >> Cuz you've got to get rid of the 4 W and things.

**Dave Jones:** >> Okay. Yeah. Got it. And you can't exactly have like a metal case when you're >> It's a metal case. >> Oh, OH, THAT'S A DIECAST. >> OH, NO, NO.

**Dave Jones:** SORRY. NO, NO. That's plastic. And that has to be because as you say, you don't want to fry people. >> Exactly. Yep. >> I wasn't understanding completely there. Yeah, so a metal box inside a plastic case.

**Dave Jones:** >> the plastic case. >> Yeah, quite right. And it uses exactly the same connection method, just a BNC at the front end. >> Got it. >> Except there's a there's a bit of a difference there.

**Dave Jones:** >> Hang on, you've done you've done your own custom sort of like >> you know, we we we everything we do is is using everything we do is 3D printed.

**Dave Jones:** These are 3D printed. >> I thought they were, but they do kind of get that Yep. >> And they're made out of nylon, PA12 nylon from HP, because it has it meets the creepage and clearance that we need.

**Dave Jones:** >> Got it. >> Okay. And there's this company in in China called JLCPCB. >> Yes, I know them, yep. Yes, everyone's heard of them. >> They're a one-stop shop for us.

**Dave Jones:** >> They are, they are, yes. >> We can send them a solid model and they'll make it. >> Fantastic. >> fantastic. And of course, they'll make the the end nuts as well.

**Dave Jones:** >> Got it. Yeah, it doesn't it doesn't really pay to sort of have those high-end 3D printers in house, really, when it's so easy to job it out to >> Exactly.

**Dave Jones:** And we just wouldn't get the utility. And and as the technology changes, they are willing to invest in new stuff. In fact, they've got a new material coming along, which is going to be even better.

**Dave Jones:** But no one really looks at them and says, "Ah, 3D printed." >> Yeah, exactly. No, it's great. >> Yeah. >> And tell us about the software, cuz software is almost well, it's not more important than hardware, but it's pretty darn important.

**Dave Jones:** >> Well, you know, we've written all the software ourselves. >> Yep. >> And perhaps someday we might open source it so that people can add stuff to it. >> Nice.

**Dave Jones:** >> I think it might be an idea. >> Do you have an API interface? >> We do. We have an API, and you can talk to it with anything, like Python or C or >> Or your latest AI, if you want.

**Dave Jones:** >> Or the latest AI. >> latest Claude or whatever bloody thing. >> No, yeah. >> Yeah, yeah, we should do that. >> Yep. >> Um and uh >> Well, what we can market that anyway, and just let the customers go, "Yeah, you can talk with with with your cloud agent or whatever."

**Dave Jones:** >> It's It's a good idea. I hadn't actually thought of that. Thank you very much. >> That's all right. >> It's very kind. Um so, we're actually displaying three things here.

**Dave Jones:** So, this one here is displaying this thing which is our new super duper probe because it does 10 kV. >> Oh, jeez. >> And it's aimed at the solid state transformer market.

**Dave Jones:** >> Oh, yes. >> and seen some solid state solid state trans- transformer makers. So, they're trying to take 33 kV in and sticking out 800 V into a AI data center.

**Dave Jones:** >> Oh, I was going to say that is AI data center. I had that. >> That's what it is. >> Yeah. >> Between 1 and 10 MW. Kind of a big thing.

**Dave Jones:** >> Yeah. >> It's to replace the big heavy metal traditional transformers, which have some issues. Supply is one of them. >> Yes. >> Second issue is that they have a power factor variation, >> Mhm.

**Dave Jones:** >> which affects the power supply system. They don't like it. Whereas, a solid state transformer can be unity power factor, which is quite useful. Or invariable, in fact, if the utility wants them to do that.

**Dave Jones:** >> Oh, you can you can power factor correct for your for the energy utility. >> Exactly. >> Oh. >> Well, you know, you're drawing 10 MW. >> Yeah, exactly.

**Dave Jones:** You want to you want to give a little back, you know? >> you give a little back. And as well as that, they're much smaller. >> Yeah. >> So, we think this is a market that's expanding.

**Dave Jones:** >> All right. >> Um and and so, we thought we'd better make a 10 kV digitizer because who does that? >> Exactly. Well, is there any any of the big >> Not that I know of it, no.

**Dave Jones:** >> No. >> No. So, you know, we're doing our usual thing, making something that's new. And eventually, they might catch up. So, um now, we were talking about the software, and we'll then go and look at some hardware again.

**Dave Jones:** So, this here is measuring this pseudo 10 kV digitizer. >> Yes. Trust us, folks. It's 10 kV. >> Anyway, uh what we've got there is a little switch and it's switching and about 10 amps.

**Dave Jones:** So, it's not huge, but it's there. And it's about 300 nanoseconds. It's only a little transistor, so it's a bit slow. There's the gate drive for it. >> Mhm.

**Dave Jones:** >> And you can see the usual Miller plateau that you're used to done. There's a couple little gremlins which we know about. We won't talk about it. There's a the power supply that runs it.

**Dave Jones:** >> Mhm. >> And we were interested in seeing how much it was being hit as this current turns on and you can see it here. >> Yep. >> It's being hit by about 300 millivolts.

**Dave Jones:** And here's VGS, which is from 19 volts, which is what it's running to about 0 volts. Now, I have to point out that this is on the 1 kilovolt range.

**Dave Jones:** >> Yes. >> Okay. So, it gives you an idea of the dynamic range of the system. >> That's ridiculous. >> That looks pretty good for a 1 kilovolt range.

**Dave Jones:** >> Exactly. >> two ranges, 1 kilovolt and 10 kilovolts. >> Oh. Wow. >> So, you can still use it as a general purpose tool to go and measure things, even on 1 kilovolt.

**Dave Jones:** >> Is there any mixed signal capability with this? >> of mixed signal capability. >> Because I see I see digital pattern generators and digital trigger and >> You can you can go off and and look at digital inputs if you like.

**Dave Jones:** >> Yeah. >> And and maybe that introduces me to a new thing. We can do mixed signal triggering. And let me just expand this. So, we have two triggers.

**Dave Jones:** So, this trigger and this trigger and you can combine them in a number of ways. Including digital triggers and you can make patterns. >> That's programmable. >> It's all programmable.

**Dave Jones:** >> They're all programmable. So, you can >> sit here and say >> Sequence. They're actual programmable sequences. >> Exactly. >> Oh. >> You can capture sequences. >> Yeah. >> We will turn this into an area trigger cuz that seems to be the latest and greatest.

**Dave Jones:** You can already do area triggering with it, but you You have to do the hard yards to figure out where to put the the triggers. So, we will do that, but it's already pretty useful.

**Dave Jones:** Um so, you can count things and you can look at differences. >> Yeah. >> We could really go into it, but it would take too long. So, uh there's lots of triggering and yes, you can make patterns here and say I want a one there and I want a zero there and I want to actually trigger on that one going high.

**Dave Jones:** You know, and then >> And where does that come out in the hardware? You got a module in the back? >> Uh You you you bring up a new point for me.

**Dave Jones:** >> Excellent. What do we got? >> Sorry. >> There's too much happening. >> Too much happening. I need to get something here. So, we have these two pods. Do you see the two pods?

**Dave Jones:** >> They are USB-C? >> They are USB-C connector. >> Yeah. Oh, okay. Right. >> Okay, and on the standard USB-C wires, we have five differential pairs. >> Yep. >> And the five differential pairs can do 400 megabits per second.

**Dave Jones:** And we have power as well. >> Yes. >> In fact, you could power your phone from it if you wanted to. >> Yeah, fantastic. >> Um but anyway, those five differential pairs are bidirectional.

**Dave Jones:** We can we can go either way. We can have a input pod or we can have an output pod. Or we can have a temperature probe, a voltage reading pod, a current reading pod.

**Dave Jones:** We're really getting into pods. >> Yes. >> Over here, I'm just going to so show you an output pod. >> Oh. >> Here's an output pod. And you can see it's got four outputs and one input.

**Dave Jones:** >> And you can have like manufactured different combinations of those that have different numbers of I/O. >> Yeah. Yeah, yeah, that's right. But this is our our first output pod.

**Dave Jones:** It's got four outs and one in. And you can use it you can program it. A thing called pulse builder. >> Yep. >> And you can make up pulses.

**Dave Jones:** >> Sweet. >> So, you don't need an arbitrary waveform generator. You just go and I'm not going to play with it cuz it's doing things. >> Sure. >> Um you can just say, "Okay, I want a 2 marker second pulse." This is for my double pulse test.

**Dave Jones:** And then I want a 100 nanosecond pulse. Okay. And I want these gaps and I want to run at 5 times a second. >> Yep. >> So, there you go.

**Dave Jones:** You just do it. It's so simple. And >> Brilliant. >> Yeah, and you can have up to eight outputs. >> Yep. >> And >> And what is this head here?

**Dave Jones:** >> Uh this is a new product. >> Yes. >> It's called the CS1202. >> Oh. >> It's It's a transient transient >> It tries a Oh, capture a whole transient specifically for transient for semiconductor manufacturers for transient >> for anyone who wants to measure a >> Oh oh, right.

**Dave Jones:** Okay. >> If you think about If you think about the standard a half bridge, there's one there. >> Yep. >> You want to often measure VDS. >> You do on the high side and that's why you need a isolated >> Correct.

**Dave Jones:** >> And often a fiber isolated >> want to measure current. >> Yep. >> And you want to measure the the VGS. >> Yep. >> And you probably want to measure the own voltage as well.

**Dave Jones:** >> Of course. >> Okay. So, that's four signals. And you might notice there are four signals going into that. >> Yes. >> And they are VDS, IS. >> Yep.

**Dave Jones:** >> We are going to have a gate drive coming out of it. >> Yep. >> VDS and VSET. >> Wow. >> All of them come out nice and time aligned and hit off to your board.

**Dave Jones:** Now, this is a little GAN half bridge that we've made so we can show this thing off. >> Hang on. Hang on. I've got to ask about Are these little ferrite beads in there?

**Dave Jones:** >> They are. One of the big issues we have, especially for current especially for current, we're using a 1 milliohm current sensor. >> Yep. >> So, that's 50 millivolts for 50 amps, right?

**Dave Jones:** >> Yes. >> And so, and we want a resolution of one part in a thousand, which is um 50 microvolts. >> Mhm. >> Mhm. And if this thing's going up and down a thousand volts, uh we need 146 dB COMMON MODE REJECTION.

**Dave Jones:** >> OH, THAT'S BRUTAL. THAT'S BRUTAL. >> It is. >> So. >> So, what we do is we have some double shielded coax inside here with really high rejection to external signals.

**Dave Jones:** There's a name for it and it's passes me by. >> Is that a foil shielded? >> It's it's yeah it's it's a mix it's a mix. It's a mix a mix of braid and foil and foil that's right.

**Dave Jones:** And it rejects on its own about 120 dB. >> Nice. >> Which is pretty good. We need a bit more than that. So we put ferrites on there. And they give us the extra 25 dB that we need.

**Dave Jones:** The ferrites also are quite good because they act as a choke and they stop common mode currents flowing back into the device. And that stops resonances which we don't want because you'll measure them.

**Dave Jones:** >> That is a twofer you get two for the price of one. >> You get two for the price of one. It's just so wonderful. >> always want a twofer when when you're actually designing stuff getting a twofer is fantastic.

**Dave Jones:** Getting it for free. It's a great plan. >> So now I would like you to come over here and look at the tiny black blob where my finger is.

**Dave Jones:** You might need to rotate around. See where my finger is there's a little black chip here labeled QL. >> Yep. >> Yep. >> I can see it. >> That's the bottom transistor.

**Dave Jones:** We have another one on the other side QH which is the top transistor. Take a guess at how much current that thing can handle. >> Ooh. Is there a heat sink on the bottom?

**Dave Jones:** Is there a thermal pad on the bottom? >> There is a thermal pad on the bottom. It's actually the chip is you're seeing the top of the chip here.

**Dave Jones:** >> I'm going I'm going to say >> Mhm. >> Is that not the normal plastic package is it? >> No it's not. >> a glass package or something? >> No that's the bottom of the chip.

**Dave Jones:** >> OH THAT THAT OH OH THAT'S THE BOTTOM OF THE DIE. It's a flip okay. >> It's a flip chip. >> It's a flip chip okay. >> And you can put another heat sink on top if you want to.

**Dave Jones:** >> Got it. Yeah what does it do like 5 watts or something just as they >> You know let's talk about current. How much current current can it can it conduct you reckon?

**Dave Jones:** >> OH I DON'T KNOW. With those number of pins 40 amps. >> 400. >> 400? Get out of here. >> It's just amazing. Yeah, it's made by EPC. It can handle 400 amps.

**Dave Jones:** Get out of here. Unbelievable. >> Wow. >> So, what we do is we turn it on into this inductor, which you can see has only got two turns. >> Yes, that's not many, but but they're chunky.

**Dave Jones:** >> Very chunky. >> Yeah. >> Because uh we need to stick a lot of current into them. It's a 470 nano Henry inductor. Pretty small. And if you come over here, >> Nothing.

**Dave Jones:** >> uh when we look at IS down here, we're going from zero up to um 156 amps. >> Yep. Wow. >> Just like that in two microseconds. >> That's ridiculous.

**Dave Jones:** >> It is ridiculous. >> Come on, bud. This is just ridiculous. >> So So >> So yeah. >> So and this is on the high side, too. >> Yeah.

**Dave Jones:** So That's it. Okay. Yeah, I'm very impressed. >> And the defect is that we can go and measure all the stuff that's happening on that transistor, the IS, Vsat, and VGS, and VDS.

**Dave Jones:** And we can then go off and measure a whole lot of things. Now, let's zoom in on the on what's actually happening in the actual switching action. >> Yep.

**Dave Jones:** >> So, here we can see the overshoot that's due to the capacitance of the bus. The bus We don't want that to get too big, otherwise goodbye transistor. >> Yeah, yeah, sure.

**Dave Jones:** >> So So we have some questions, which is how much inductance is there? We can work it out from this drop here. So, this is the bus and that loop This is the current ramping up.

**Dave Jones:** >> Yep. >> Um I'll just put just put that there. So, it's ramping up to 180 amps. >> Mhm. >> And while it does that, the bus loop inductance is acting as a retarder, if you like.

**Dave Jones:** It doesn't like that current flowing. And because it's a ramp, we get a pretty much a flat >> Mhm. >> where where in the in this voltage drop here.

**Dave Jones:** And that's V V equals L di by dt. You know that one? >> Yes, I know it. >> From that therefore you can calculate the bus loop inductance from the L.

**Dave Jones:** Which we do. >> Oh, okay. Fantastic. >> Okay, I just have to find the >> Oh, they've got they've got an infographic. >> I've got an infographic that's so much simpler just putting out a bit of paper.

**Dave Jones:** >> Yep. Yep. There you go. >> Okay, which we do. Here it is and there's a bus loop inductance 914 pico Henry. >> But it matters. Really matters. I know.

**Dave Jones:** >> That's why it >> 914 pico Henry. Let me explain that one nano Henry is 1 mm of wire. >> Yeah. Yes, exactly. Decent rule of thumb there, folks.

**Dave Jones:** >> Then it resonates. You can see that resonates there. >> And I guess I could I could go and measure the resonance. >> Yep. >> Essentially why just I'll do it just quickly.

**Dave Jones:** Just do a couple of little blobs there and you can see it's 181 MHz. >> Have you ever heard of F equals 1 over 2 pi root LC? >> Yes.

**Dave Jones:** That's kind of familiar. It's pretty basic. >> So we know the L. >> Yes. >> We just measured it over here by looking at the voltage drop there. >> Yes, we did.

**Dave Jones:** >> Okay, so now we can put plug that L in there. >> Mhm. >> Pull the C out and put the F in cuz we know what the F is.

**Dave Jones:** We've just measured it and we can measure the opens this the capacitance of the upper transistor that we're measuring. And there it is QH 908 pico Henry. 908 pico Henry.

**Dave Jones:** >> Can you do that calculation in the software? >> You can. >> You can? >> You can do it in maths. >> Oh, oh yeah. Yeah. Okay, right. You just a standard maths function.

**Dave Jones:** Oh, okay. >> So we can calculate it. And and um and we can go on and and we can measure other stuff like RDS on. Let's try this. So >> Oh, we've only got 2 minutes of card footage left.

**Dave Jones:** >> Oh my god, we're going to run out. >> Yep. >> So here we are measuring RDS on. So this little thing is there it is about 3 3.1 m.

**Dave Jones:** >> And it's varying a little bit as it heats up. >> Yeah. >> And it's going up to 3.2, which is 118 milliohms change. >> It's crazy. >> It's crazy.

**Dave Jones:** >> Yeah. That's And so, no other manufacturer Yeah. No other manufacturer has really got this capability. No other scope manufacturer really. >> No, they don't. >> No. No, it's pretty unique, but we were impressed last time and we're even more impressed now.

**Dave Jones:** The CleverScope, roughly how much? Four or five bucks? >> Got more expensive now, about $13,000. >> Yeah. Yeah, but >> It does more now. >> It does a hell of a lot more.

**Dave Jones:** >> And and uh >> Very impressive. >> We can we can waste another 2 minutes talking about frequency response analysis. I don't know if you want to see a BH curve.

**Dave Jones:** Here's a BH curve. >> Yeah. Yeah, I I saw that before. Yeah. >> that before. And the reason we have it is because so many people have asked us because they want to wind their own magnetics.

**Dave Jones:** >> Yes. >> So, they want to they want to make sure that their cores aren't going to saturate. So, it's really simple. You put it in there. You change the frequency down by 10% and you watch to see if it saturates.

**Dave Jones:** No, it doesn't. >> It's a good go. >> You keep it. >> Fantastic. This is great, Bob. Thank you very much. Very impressive. We'll link in CleverScope down >> Thank you very much for coming and visiting us.

**Dave Jones:** Sorry? >> Are they still made made in house? >> Well, not SMT, no. >> No, right. >> No, the SMT for that's done by a company called Triode in Auckland.

**Dave Jones:** >> Okay. >> And then we put it together. >> In case you didn't realize the accent, folks. >> Yeah, I'm a New Zealander from Auckland. >> Right. We'll go and have some fish and chips.

**Dave Jones:** >> Fish and chips. >> Thanks, Bob. >> Okay, thanks. >> See you, mate. >> Thanks very much.
