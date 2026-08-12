---
video_id: WdYBL-_8-oo
title: EEVblog 1753 - Designing a 2000V Isolated Oscilloscope (Cleverscope)
url: https://www.youtube.com/watch?v=WdYBL-_8-oo
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 27, "3": 40, "4": 55, "5": 67, "6": 78, "7": 94, "8": 104, "9": 115, "10": 126, "11": 141, "12": 152, "13": 165, "14": 175, "15": 186, "16": 199, "17": 215, "18": 228, "19": 241, "20": 257, "21": 267, "22": 280, "23": 292, "24": 310, "25": 319, "26": 334, "27": 345, "28": 354, "29": 367, "30": 383, "31": 395, "32": 407, "33": 418, "34": 431, "35": 442, "36": 454, "37": 466, "38": 478, "39": 487, "40": 501, "41": 515, "42": 528, "43": 539, "44": 551, "45": 562, "46": 571, "47": 583, "48": 595, "49": 606, "50": 620, "51": 631, "52": 644, "53": 656, "54": 668, "55": 679, "56": 690, "57": 702, "58": 719, "59": 730, "60": 743, "61": 755, "62": 768, "63": 778, "64": 791, "65": 806, "66": 820, "67": 831, "68": 842, "69": 854, "70": 866, "71": 878, "72": 893, "73": 909, "74": 921, "75": 933, "76": 945, "77": 959, "78": 973, "79": 985, "80": 998, "81": 1013, "82": 1025, "83": 1037, "84": 1047, "85": 1059, "86": 1074, "87": 1085, "88": 1096, "89": 1105, "90": 1117, "91": 1129, "92": 1141, "93": 1158, "94": 1170, "95": 1183, "96": 1196, "97": 1206, "98": 1218, "99": 1228, "100": 1236, "101": 1248, "102": 1256, "103": 1268, "104": 1280, "105": 1293, "106": 1309, "107": 1324, "108": 1338, "109": 1350, "110": 1365, "111": 1377, "112": 1388, "113": 1398, "114": 1416, "115": 1429, "116": 1443, "117": 1454, "118": 1467, "119": 1480, "120": 1491, "121": 1506, "122": 1521, "123": 1532, "124": 1543, "125": 1552, "126": 1562, "127": 1576, "128": 1586}
---

**Dave Jones:** Hi, I'm here at the Cleverscope stand. And you might remember but from Cleverscope, the designer of the Cleverscope. And we What, 8 years ago you told me? >> I talked to you, Dave. >> About the original design of the Cleverscope, but you've got a new

**Dave Jones:** one. >> Well, it's not that new, but it's you know, but it's new in 8 years. >> And we're going to look we've got it open here. And Bart's the designer, he's going to tell us all about this. Um tell

**Dave Jones:** us the ins and outs of designing a four-channel totally isolated high high voltage isolator. What's what's the basic specs? >> data there. >> 2 kV per channel? >> Yep. >> Yep. What what bandwidth we talking about? >> MHz bandwidth.

**Dave Jones:** >> 200 meg bandwidth, which is hard at that sort of yeah. >> Yeah, it's 200 MHz bandwidth, 500 MHz sampling rate. 14 bits. I don't know if any of that's useful to you. >> Absolutely. >> Okay. The ADC is right underneath where

**Dave Jones:** my finger is. >> Yep. >> It's not open, sorry. >> That's all right. >> It's a bit hard to see. The can is just closed. >> Sure. >> Um and then a little bit of circuitry to give us two ranges, 0.8 and 8 volts. Not

**Dave Jones:** many ranges. We use probes to get the range we want. >> Yep. >> So, this is a 100 100 times probe and off the shelf. >> 100 X, yep. >> 100 X times 8 800 volts. There you go.

**Dave Jones:** >> Nice. >> So, then it connects using a what's called a QSFP fiber cable, an optical cable. These are These are used in data centers yep all over the world. >> Easy to get. >> And they're cheap and they're relatively

**Dave Jones:** cheap. And all the design work's take all the high speed >> All the difficult things taken out of them for us. We just have to plug the bloody things in. Sorry. >> That's all right. We can we can say

**Dave Jones:** bloody here on the EEVblog. Bloody designers. Anyway. >> It cost us so much. The greasy old one the old one cost us a lot of grease. >> Yeah, cuz you you designed that yourself back in the day back in the day.

**Dave Jones:** >> did. So, we won't we've gone past that. Now, because we have a plug cap >> we thought, "Well, why don't we put a a switch under there?" And then we can switch between the one inside. So, this

**Dave Jones:** is the inside of the scope. There's a 12-layer board. >> 12-layer >> 12 Lots of 50-ohm um >> Yep. >> uh controlled impedance because we're trying to send 5 gigabits per second signals down these fibers. >> Of course.

**Dave Jones:** >> And we also have a whole lot of DDR3 RAM, which is ancient now, but you know, it's still running a data after mix. >> That's a big FPGA. >> And what uh >> It's an Altera one. It's a colon area

**Dave Jones:** five. >> Okay, RS series, yeah. >> It's got about 980 pins coming out of it. >> Yep. >> And they connect to everything. And at the back here we have a isolated signal generator. And we use the same

**Dave Jones:** power supply system. >> Okay. >> as we do here. >> Did you roll that yourself? >> Yes, we did. >> Yep. >> There's actually about a year of work, and we talked about this last time. >> talk about this last time. Yes, a year

**Dave Jones:** of development. >> across the board. >> Two path? >> Two path. >> Very nice. >> Very low common mode current, which is what we need cuz we don't want to inject any common mode current into the circuit we're measuring.

**Dave Jones:** >> Got you. >> Okay. So, we use the same for the signal generator. And the reason that we have the signal generator isolated is so we can do gain phase on power supplies. While they're alive and running. >> Yep. Okay, is that the main application

**Dave Jones:** market for this scope? People doing doing it for power supply design? Or is it motor drive? What's What's your >> It's It's anything in power electronics. >> Got it. >> Okay, uh five If we carry this on, we might get into SSTs, which we'll end

**Dave Jones:** on. >> Okay. >> Okay, which are solid state transformers, in case you didn't know. So, then of course we have USB 3, and we're missing the SFP cover there for Ethernet. >> Mhm. >> So, that just plugs in. It's another

**Dave Jones:** pluggable connector. It's great. >> Excellent. >> Um yeah, so anyway, we >> So, hang on. So, you've got your 14-bit ADC in here. Do you have to do any and and maybe some offset stuff as well? Did you have to do anything else to get the

**Dave Jones:** data to the transceiver? Is there a little knob? >> No, no, no. The wonderful thing about the AD the ADC we use, it's called a GSD 204 ADC. It's 6 out GSD GSD 204 um 5 gigas 5 giga

**Dave Jones:** bits per second data two two lanes and it can go straight into the fiber. >> It just goes straight in. That's brilliant. >> And the other end it goes into the FPGA and we have a decoder for it.

**Dave Jones:** >> Fantastic. >> So simple. >> Yeah. Um, any heat sinking in there? Any sort of power dissipation? Oh, well, yeah, yeah, on top, but like internally to cool it. >> So, inside we have a big thermal pad which covers the whole board. So, we

**Dave Jones:** suck the heat out of the board, which is again 12 layers and it has quite a lot of copper in it. So, we spread the heat from all these quite the ADC on it's on it's 1 and 1/2 watts and we have a clock

**Dave Jones:** generator which makes our 500 megahertz clock reference. It's another watt and there's some uh analog devices 1 gigahertz op amps. They're also pretty power hungry. >> I noticed um thermal-wise there's no fans in this thing. So, it's all

**Dave Jones:** passive. Oh, there is. Where does it go? >> There's too much heat. >> Oh, okay. Oh, yeah, that's on the top. I was going to say, yeah. >> Fan was on the top. >> Right, okay. Okay, so you're drawing in

**Dave Jones:** the air here and bringing it out here. >> Exactly. So, it goes straight past the digitizers, these these ones here. And it also it pulls the air up from the FPGA and we run it at constant temperature actually of 40° C.

**Dave Jones:** >> Okay, and you don't need a heat sink on the um exterior jobby there? >> No, because the board itself is pretty good. >> Oh, okay. >> Lots of copper in it. >> Okay. >> And because the air is being dragged out

**Dave Jones:** of it all the time, >> Yeah, it doesn't get too hot. >> We measure that it has a temperature sensor inside it. >> Yeah, got it. >> So we can make sure it's not too hot. >> Yep, fantastic.

**Dave Jones:** >> So yeah, 40 The reason we run it at 40 is and we control the fan speed to keep it at 40, so all those analog electronics stay nice and steady, don't drift around. >> Yep. >> So that's one of our things.

**Dave Jones:** >> Okay. >> No drift. Well, not much. >> Well, it's yeah, nothing consequential. >> Nothing consequential. >> I was going to say that we have this switch in here, so we can switch between the top QSFB connector and the bottom QSFB

**Dave Jones:** connector. >> Oh. >> Now this >> Oh, what is the bottom What's What's the bottom one doing? Oh, YOU CAN HAVE OUTPUT. OH. >> SO the advantage of having the bottom one is that we can switch to an external

**Dave Jones:** digitizer. Now we can't run both at the same time cuz the FPJ's not up to it. >> Got it. >> But we can switch between the two. >> Very >> So that's very handy because if the customer comes to us and says, "I've got

**Dave Jones:** a big safety cage. I've I want to measure something inside the safety cage, and I don't want to get fried. How do I do it?" >> Got it. >> Well, >> You've got a 10 10 kV Is that a real 10

**Dave Jones:** kV demo there? >> No. >> it No, I was going to say are you with >> You know, we don't really want to kill the customer. >> kill the the the potential customers. >> Not really. >> Nice, but I I I I love it

**Dave Jones:** lit up there blue 10 kV sig. >> Yeah, well, that's how they look. They look exactly like This is a 3D printed one. >> Oh, okay. >> Right. Nice. Basically because it's kind of hard to get 10 kV sigs with the nice

**Dave Jones:** blue lettering behind them. >> Yes, exactly. Yeah, they don't exactly make those, do they? >> No, they don't. No, but the advantage here is is a fiber connection, and because it's digital, it can go 30 m. >> Got it.

**Dave Jones:** >> So say you want to Say you're at Airbus, and you want to measure from one side of a wing to the other side of the wing and look at correlation between things. You can do it. >> Excellent. Is that power over fiber as

**Dave Jones:** well? >> No, it's not. No, it's not. >> Okay. >> No. We do have a module that does power over fiber. Um >> Oh, so you can just plug a module in series? So it doesn't >> no, what we do is we we've got So if we

**Dave Jones:** go back to the back of those, you can see there's a battery box here. >> Oh. >> And so you can open the battery box. >> Right. >> And >> and slide in a unit and a power supply.

**Dave Jones:** >> I got it. Okay. Right. >> So That's a developmental thing. Not actually available. >> Right. And so right, so that is you can there's nothing off the shelf that allows you to do that really. >> Uh there is. There is, but most of the

**Dave Jones:** Evergo the these are mostly Evergo things. And the off-shelf can handle 2 W and we want 4. >> Oh. >> Okay, but they've got a new receiver which is 10 W. We can use that. >> Yep. >> So the efficiency is the big problem. Um

**Dave Jones:** the total round trip efficiency is about a quarter, 25%. So if you want 4 W, you really have to stick 16 W in to make it work. And uh that's a lot of heat you've got to get rid of.

**Dave Jones:** >> Exactly. >> Batteries are so much simpler. And they float freely. You can have 30 kV there and it doesn't matter. >> It doesn't matter a rat's. Yeah. That's great. >> So the utility of of having the extra

**Dave Jones:** socket is that we can handle putting these things far away. Inside here is exactly one of those. >> Oh, okay. Got you. >> There's no difference. So it was a simple thing for us. >> Yeah. >> Take one of these.

**Dave Jones:** >> Yep. >> Add a battery. >> Exactly. And in your case it have an external case for it. And uh yep. >> And away it goes. >> Excellent. >> Yeah, it has a little fan inside it, too. >> Oh, okay. Right. Just a

**Dave Jones:** >> Cuz you've got to get rid of the 4 W and things. >> Okay. Yeah. Got it. And you can't exactly have like a metal case when you're >> It's a metal case. >> Oh, OH, THAT'S A DIECAST.

**Dave Jones:** >> OH, NO, NO. SORRY. NO, NO. That's plastic. And that has to be because as you say, you don't want to fry people. >> Exactly. Yep. >> I wasn't understanding completely there. Yeah, so a metal box inside a plastic

**Dave Jones:** case. >> the plastic case. >> Yeah, quite right. And it uses exactly the same connection method, just a BNC at the front end. >> Got it. >> Except there's a there's a bit of a difference there. >> Hang on, you've done you've done your

**Dave Jones:** own custom sort of like >> you know, we we we everything we do is is using everything we do is 3D printed. These are 3D printed. >> I thought they were, but they do kind of get that Yep.

**Dave Jones:** >> And they're made out of nylon, PA12 nylon from HP, because it has it meets the creepage and clearance that we need. >> Got it. >> Okay. And there's this company in in China called JLCPCB. >> Yes, I know them, yep. Yes, everyone's

**Dave Jones:** heard of them. >> They're a one-stop shop for us. >> They are, they are, yes. >> We can send them a solid model and they'll make it. >> Fantastic. >> fantastic. And of course, they'll make the the end nuts as well.

**Dave Jones:** >> Got it. Yeah, it doesn't it doesn't really pay to sort of have those high-end 3D printers in house, really, when it's so easy to job it out to >> Exactly. And we just wouldn't get the utility. And and as the technology changes, they

**Dave Jones:** are willing to invest in new stuff. In fact, they've got a new material coming along, which is going to be even better. But no one really looks at them and says, "Ah, 3D printed." >> Yeah, exactly. No, it's great.

**Dave Jones:** >> Yeah. >> And tell us about the software, cuz software is almost well, it's not more important than hardware, but it's pretty darn important. >> Well, you know, we've written all the software ourselves. >> Yep. >> And perhaps someday we might open source

**Dave Jones:** it so that people can add stuff to it. >> Nice. >> I think it might be an idea. >> Do you have an API interface? >> We do. We have an API, and you can talk to it with anything, like Python or C or

**Dave Jones:** >> Or your latest AI, if you want. >> Or the latest AI. >> latest Claude or whatever bloody thing. >> No, yeah. >> Yeah, yeah, we should do that. >> Yep. >> Um and uh >> Well, what we can market that anyway,

**Dave Jones:** and just let the customers go, "Yeah, you can talk with with with your cloud agent or whatever." >> It's It's a good idea. I hadn't actually thought of that. Thank you very much. >> That's all right. >> It's very kind. Um so, we're actually

**Dave Jones:** displaying three things here. So, this one here is displaying this thing which is our new super duper probe because it does 10 kV. >> Oh, jeez. >> And it's aimed at the solid state transformer market. >> Oh, yes.

**Dave Jones:** >> and seen some solid state solid state trans- transformer makers. So, they're trying to take 33 kV in and sticking out 800 V into a AI data center. >> Oh, I was going to say that is AI data

**Dave Jones:** center. I had that. >> That's what it is. >> Yeah. >> Between 1 and 10 MW. Kind of a big thing. >> Yeah. >> It's to replace the big heavy metal traditional transformers, which have some issues. Supply is one of them.

**Dave Jones:** >> Yes. >> Second issue is that they have a power factor variation, >> Mhm. >> which affects the power supply system. They don't like it. Whereas, a solid state transformer can be unity power factor, which is quite useful. Or

**Dave Jones:** invariable, in fact, if the utility wants them to do that. >> Oh, you can you can power factor correct for your for the energy utility. >> Exactly. >> Oh. >> Well, you know, you're drawing 10 MW. >> Yeah, exactly. You want to you want to

**Dave Jones:** give a little back, you know? >> you give a little back. And as well as that, they're much smaller. >> Yeah. >> So, we think this is a market that's expanding. >> All right. >> Um and and so, we thought we'd better

**Dave Jones:** make a 10 kV digitizer because who does that? >> Exactly. Well, is there any any of the big >> Not that I know of it, no. >> No. >> No. So, you know, we're doing our usual thing, making something that's new. And

**Dave Jones:** eventually, they might catch up. So, um now, we were talking about the software, and we'll then go and look at some hardware again. So, this here is measuring this pseudo 10 kV digitizer. >> Yes. Trust us, folks. It's 10 kV.

**Dave Jones:** >> Anyway, uh what we've got there is a little switch and it's switching and about 10 amps. So, it's not huge, but it's there. And it's about 300 nanoseconds. It's only a little transistor, so it's a bit slow. There's

**Dave Jones:** the gate drive for it. >> Mhm. >> And you can see the usual Miller plateau that you're used to done. There's a couple little gremlins which we know about. We won't talk about it. There's a the power supply that runs it.

**Dave Jones:** >> Mhm. >> And we were interested in seeing how much it was being hit as this current turns on and you can see it here. >> Yep. >> It's being hit by about 300 millivolts. And here's VGS, which is from

**Dave Jones:** 19 volts, which is what it's running to about 0 volts. Now, I have to point out that this is on the 1 kilovolt range. >> Yes. >> Okay. So, it gives you an idea of the dynamic range of the system.

**Dave Jones:** >> That's ridiculous. >> That looks pretty good for a 1 kilovolt range. >> Exactly. >> two ranges, 1 kilovolt and 10 kilovolts. >> Oh. Wow. >> So, you can still use it as a general purpose tool to go and measure things,

**Dave Jones:** even on 1 kilovolt. >> Is there any mixed signal capability with this? >> of mixed signal capability. >> Because I see I see digital pattern generators and digital trigger and >> You can you can go off and and look at

**Dave Jones:** digital inputs if you like. >> Yeah. >> And and maybe that introduces me to a new thing. We can do mixed signal triggering. And let me just expand this. So, we have two triggers. So, this trigger and this trigger and you can

**Dave Jones:** combine them in a number of ways. Including digital triggers and you can make patterns. >> That's programmable. >> It's all programmable. >> They're all programmable. So, you can >> sit here and say >> Sequence. They're actual programmable sequences.

**Dave Jones:** >> Exactly. >> Oh. >> You can capture sequences. >> Yeah. >> We will turn this into an area trigger cuz that seems to be the latest and greatest. You can already do area triggering with it, but you You have to do the hard

**Dave Jones:** yards to figure out where to put the the triggers. So, we will do that, but it's already pretty useful. Um so, you can count things and you can look at differences. >> Yeah. >> We could really go into it, but it would

**Dave Jones:** take too long. So, uh there's lots of triggering and yes, you can make patterns here and say I want a one there and I want a zero there and I want to actually trigger on that one going high. You know, and then

**Dave Jones:** >> And where does that come out in the hardware? You got a module in the back? >> Uh You you you bring up a new point for me. >> Excellent. What do we got? >> Sorry. >> There's too much happening.

**Dave Jones:** >> Too much happening. I need to get something here. So, we have these two pods. Do you see the two pods? >> They are USB-C? >> They are USB-C connector. >> Yeah. Oh, okay. Right. >> Okay, and on the standard USB-C wires,

**Dave Jones:** we have five differential pairs. >> Yep. >> And the five differential pairs can do 400 megabits per second. And we have power as well. >> Yes. >> In fact, you could power your phone from it if you wanted to.

**Dave Jones:** >> Yeah, fantastic. >> Um but anyway, those five differential pairs are bidirectional. We can we can go either way. We can have a input pod or we can have an output pod. Or we can have a temperature probe, a

**Dave Jones:** voltage reading pod, a current reading pod. We're really getting into pods. >> Yes. >> Over here, I'm just going to so show you an output pod. >> Oh. >> Here's an output pod. And you can see it's got four outputs and one input.

**Dave Jones:** >> And you can have like manufactured different combinations of those that have different numbers of I/O. >> Yeah. Yeah, yeah, that's right. But this is our our first output pod. It's got four outs and one in. And you can use it

**Dave Jones:** you can program it. A thing called pulse builder. >> Yep. >> And you can make up pulses. >> Sweet. >> So, you don't need an arbitrary waveform generator. You just go and I'm not going to play with it cuz it's doing things.

**Dave Jones:** >> Sure. >> Um you can just say, "Okay, I want a 2 marker second pulse." This is for my double pulse test. And then I want a 100 nanosecond pulse. Okay. And I want these gaps and I want to run at 5 times a

**Dave Jones:** second. >> Yep. >> So, there you go. You just do it. It's so simple. And >> Brilliant. >> Yeah, and you can have up to eight outputs. >> Yep. >> And >> And what is this head here? >> Uh this is a new product.

**Dave Jones:** >> Yes. >> It's called the CS1202. >> Oh. >> It's It's a transient transient >> It tries a Oh, capture a whole transient specifically for transient for semiconductor manufacturers for transient >> for anyone who wants to measure a

**Dave Jones:** >> Oh oh, right. Okay. >> If you think about If you think about the standard a half bridge, there's one there. >> Yep. >> You want to often measure VDS. >> You do on the high side and that's why

**Dave Jones:** you need a isolated >> Correct. >> And often a fiber isolated >> want to measure current. >> Yep. >> And you want to measure the the VGS. >> Yep. >> And you probably want to measure the own voltage as well.

**Dave Jones:** >> Of course. >> Okay. So, that's four signals. And you might notice there are four signals going into that. >> Yes. >> And they are VDS, IS. >> Yep. >> We are going to have a gate drive coming

**Dave Jones:** out of it. >> Yep. >> VDS and VSET. >> Wow. >> All of them come out nice and time aligned and hit off to your board. Now, this is a little GAN half bridge that we've made so we can show this thing

**Dave Jones:** off. >> Hang on. Hang on. I've got to ask about Are these little ferrite beads in there? >> They are. One of the big issues we have, especially for current especially for current, we're using a 1 milliohm current sensor.

**Dave Jones:** >> Yep. >> So, that's 50 millivolts for 50 amps, right? >> Yes. >> And so, and we want a resolution of one part in a thousand, which is um 50 microvolts. >> Mhm. >> Mhm. And if this thing's going up and

**Dave Jones:** down a thousand volts, uh we need 146 dB COMMON MODE REJECTION. >> OH, THAT'S BRUTAL. THAT'S BRUTAL. >> It is. >> So. >> So, what we do is we have some double shielded coax inside here with really high rejection to external

**Dave Jones:** signals. There's a name for it and it's passes me by. >> Is that a foil shielded? >> It's it's yeah it's it's a mix it's a mix. It's a mix a mix of braid and foil and foil that's right.

**Dave Jones:** And it rejects on its own about 120 dB. >> Nice. >> Which is pretty good. We need a bit more than that. So we put ferrites on there. And they give us the extra 25 dB that we need.

**Dave Jones:** The ferrites also are quite good because they act as a choke and they stop common mode currents flowing back into the device. And that stops resonances which we don't want because you'll measure them. >> That is a twofer you get two for the

**Dave Jones:** price of one. >> You get two for the price of one. It's just so wonderful. >> always want a twofer when when you're actually designing stuff getting a twofer is fantastic. Getting it for free. It's a great plan.

**Dave Jones:** >> So now I would like you to come over here and look at the tiny black blob where my finger is. You might need to rotate around. See where my finger is there's a little black chip here labeled

**Dave Jones:** QL. >> Yep. >> Yep. >> I can see it. >> That's the bottom transistor. We have another one on the other side QH which is the top transistor. Take a guess at how much current that thing can handle.

**Dave Jones:** >> Ooh. Is there a heat sink on the bottom? Is there a thermal pad on the bottom? >> There is a thermal pad on the bottom. It's actually the chip is you're seeing the top of the chip here.

**Dave Jones:** >> I'm going I'm going to say >> Mhm. >> Is that not the normal plastic package is it? >> No it's not. >> a glass package or something? >> No that's the bottom of the chip. >> OH THAT THAT OH OH THAT'S THE BOTTOM OF

**Dave Jones:** THE DIE. It's a flip okay. >> It's a flip chip. >> It's a flip chip okay. >> And you can put another heat sink on top if you want to. >> Got it. Yeah what does it do like 5

**Dave Jones:** watts or something just as they >> You know let's talk about current. How much current current can it can it conduct you reckon? >> OH I DON'T KNOW. With those number of pins 40 amps. >> 400. >> 400? Get out of here.

**Dave Jones:** >> It's just amazing. Yeah, it's made by EPC. It can handle 400 amps. Get out of here. Unbelievable. >> Wow. >> So, what we do is we turn it on into this inductor, which you can see has only got two turns.

**Dave Jones:** >> Yes, that's not many, but but they're chunky. >> Very chunky. >> Yeah. >> Because uh we need to stick a lot of current into them. It's a 470 nano Henry inductor. Pretty small. And if you come over here,

**Dave Jones:** >> Nothing. >> uh when we look at IS down here, we're going from zero up to um 156 amps. >> Yep. Wow. >> Just like that in two microseconds. >> That's ridiculous. >> It is ridiculous. >> Come on, bud. This is just ridiculous.

**Dave Jones:** >> So So >> So yeah. >> So and this is on the high side, too. >> Yeah. So That's it. Okay. Yeah, I'm very impressed. >> And the defect is that we can go and measure all the stuff that's happening on that

**Dave Jones:** transistor, the IS, Vsat, and VGS, and VDS. And we can then go off and measure a whole lot of things. Now, let's zoom in on the on what's actually happening in the actual switching action. >> Yep. >> So, here we can see the overshoot that's

**Dave Jones:** due to the capacitance of the bus. The bus We don't want that to get too big, otherwise goodbye transistor. >> Yeah, yeah, sure. >> So So we have some questions, which is how much inductance is there? We can

**Dave Jones:** work it out from this drop here. So, this is the bus and that loop This is the current ramping up. >> Yep. >> Um I'll just put just put that there. So, it's ramping up to 180 amps. >> Mhm.

**Dave Jones:** >> And while it does that, the bus loop inductance is acting as a retarder, if you like. It doesn't like that current flowing. And because it's a ramp, we get a pretty much a flat >> Mhm. >> where where in the in this voltage drop

**Dave Jones:** here. And that's V V equals L di by dt. You know that one? >> Yes, I know it. >> From that therefore you can calculate the bus loop inductance from the L. Which we do. >> Oh, okay. Fantastic.

**Dave Jones:** >> Okay, I just have to find the >> Oh, they've got they've got an infographic. >> I've got an infographic that's so much simpler just putting out a bit of paper. >> Yep. Yep. There you go. >> Okay, which we do. Here it is and

**Dave Jones:** there's a bus loop inductance 914 pico Henry. >> But it matters. Really matters. I know. >> That's why it >> 914 pico Henry. Let me explain that one nano Henry is 1 mm of wire. >> Yeah. Yes, exactly.

**Dave Jones:** Decent rule of thumb there, folks. >> Then it resonates. You can see that resonates there. >> And I guess I could I could go and measure the resonance. >> Yep. >> Essentially why just I'll do it just quickly.

**Dave Jones:** Just do a couple of little blobs there and you can see it's 181 MHz. >> Have you ever heard of F equals 1 over 2 pi root LC? >> Yes. That's kind of familiar. It's pretty basic. >> So we know the L.

**Dave Jones:** >> Yes. >> We just measured it over here by looking at the voltage drop there. >> Yes, we did. >> Okay, so now we can put plug that L in there. >> Mhm. >> Pull the C out and put the F in cuz we

**Dave Jones:** know what the F is. We've just measured it and we can measure the opens this the capacitance of the upper transistor that we're measuring. And there it is QH 908 pico Henry. 908 pico Henry. >> Can you do that calculation in the

**Dave Jones:** software? >> You can. >> You can? >> You can do it in maths. >> Oh, oh yeah. Yeah. Okay, right. You just a standard maths function. Oh, okay. >> So we can calculate it. And and um and we can go on and and we can measure

**Dave Jones:** other stuff like RDS on. Let's try this. So >> Oh, we've only got 2 minutes of card footage left. >> Oh my god, we're going to run out. >> Yep. >> So here we are measuring RDS on. So this

**Dave Jones:** little thing is there it is about 3 3.1 m. >> And it's varying a little bit as it heats up. >> Yeah. >> And it's going up to 3.2, which is 118 milliohms change. >> It's crazy. >> It's crazy.

**Dave Jones:** >> Yeah. That's And so, no other manufacturer Yeah. No other manufacturer has really got this capability. No other scope manufacturer really. >> No, they don't. >> No. No, it's pretty unique, but we were impressed last time and we're even more

**Dave Jones:** impressed now. The CleverScope, roughly how much? Four or five bucks? >> Got more expensive now, about $13,000. >> Yeah. Yeah, but >> It does more now. >> It does a hell of a lot more. >> And and uh

**Dave Jones:** >> Very impressive. >> We can we can waste another 2 minutes talking about frequency response analysis. I don't know if you want to see a BH curve. Here's a BH curve. >> Yeah. Yeah, I I saw that before. Yeah.

**Dave Jones:** >> that before. And the reason we have it is because so many people have asked us because they want to wind their own magnetics. >> Yes. >> So, they want to they want to make sure that their cores

**Dave Jones:** aren't going to saturate. So, it's really simple. You put it in there. You change the frequency down by 10% and you watch to see if it saturates. No, it doesn't. >> It's a good go. >> You keep it.

**Dave Jones:** >> Fantastic. This is great, Bob. Thank you very much. Very impressive. We'll link in CleverScope down >> Thank you very much for coming and visiting us. Sorry? >> Are they still made made in house? >> Well, not SMT, no.

**Dave Jones:** >> No, right. >> No, the SMT for that's done by a company called Triode in Auckland. >> Okay. >> And then we put it together. >> In case you didn't realize the accent, folks. >> Yeah, I'm a New Zealander from Auckland.

**Dave Jones:** >> Right. We'll go and have some fish and chips. >> Fish and chips. >> Thanks, Bob. >> Okay, thanks. >> See you, mate. >> Thanks very much.
