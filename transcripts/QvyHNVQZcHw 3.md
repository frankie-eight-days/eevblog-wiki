---
video_id: QvyHNVQZcHw
title: EEVblog #133 - Dodgy Digikey Components
url: https://www.youtube.com/watch?v=QvyHNVQZcHw
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 31, "3": 49, "4": 65, "5": 76, "6": 93, "7": 107, "8": 123, "9": 140, "10": 162, "11": 174, "12": 188, "13": 210, "14": 226, "15": 241, "16": 261, "17": 277, "18": 297, "19": 309, "20": 325, "21": 339, "22": 362, "23": 378, "24": 394, "25": 412, "26": 435, "27": 448, "28": 459, "29": 472, "30": 487, "31": 503, "32": 522, "33": 544, "34": 559, "35": 574, "36": 588, "37": 603, "38": 619, "39": 636, "40": 648, "41": 665, "42": 679, "43": 696, "44": 709, "45": 725, "46": 743, "47": 757, "48": 771, "49": 782, "50": 794, "51": 812, "52": 830, "53": 843, "54": 856, "55": 871, "56": 885, "57": 898, "58": 914, "59": 931, "60": 946, "61": 969, "62": 990, "63": 1005, "64": 1018, "65": 1033, "66": 1046}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, I've had a bit of a problem with my micro current project and I'm a bit

**Dave Jones:** pissed off, quite frankly. What's happened is I kitted up for a new batch of these and I tested them and shipped away a bunch of them and then I found, oops, there's a slight problem with them. And the thing with the micro

**Dave Jones:** current project is that it's a little precision current adapter and it basically relies upon the precise nature of the .1% resistors in here to give the accuracy that this unit actually has and you know, those resistors are usually

**Dave Jones:** very, very reliable. You either get the right part and it's spot on, within spec .1% or it's not or it's, you know, the wrong part or something else. So, I don't fully test every parameter of this thing before I send it out. I just do a

**Dave Jones:** couple of I just do a spot check on each current range to make sure it's working. I check the first build to make sure it's okay and then, you know, I just do some spot checks and ship them out.

**Dave Jones:** Well, after I shipped out a batch of them, the second lot I started to test it and it looked a bit looked a bit funny. The readings on the on the micro amp range were slightly off and I thought I'd investigate. Now,

**Dave Jones:** here's what typically happens, okay? I've got the micro current adapter here. I've got the output hooked up to a to a precision meter here, the Metrahit extra. I switch it on and I've got my Keithley current source here which I

**Dave Jones:** generate a constant current into the input. Now, this is on the nano amp range and I set it to 99.9 nano amps on my current source here and as you can see it's 99.7. It's pretty darn good because it's not

**Dave Jones:** this isn't this isn't like point one percent or lower accurate but that shows me that I've got the right value resistor installed and everything's hunky-dory with that and I switch the current range up to the milliamp range. Here we go. So it's 99.9

**Dave Jones:** milliamps and check it out. There we go. 99.89 pretty darn close to 99.9 not a problem but let's switch it down to the micro amp range and switch it over and here we go. It's a 101.2 millivolts so it's saying it's 101.2

**Dave Jones:** milliamps. Now what we need to do okay that seems to be a bit out way out of spec but what we need to do is whack a current meter in series and actually see what current's going into here to

**Dave Jones:** confirm that. Okay, so what we've got now is we've got a second Metrahit meter the Metrahit energy nice precise meter I love it haven't done a review of that yet but it's met now measuring the input current to my micro amp range and the

**Dave Jones:** other Metrahit extra meter is still measuring the output voltage or what the micro current is measuring. Okay, so I'm actually feeding in 99.76 microamps into the input and the micro current is telling me it's actually measuring 101.21 microamps. So

**Dave Jones:** you might think that that's you know it's pretty darn close but if you punch that into your calculator that's like a 1.4 1.5 percent error. It's hopeless. I we expect around point one point two percent or better accuracy so it's you

**Dave Jones:** know it's almost an order of magnitude worse really so something is wrong with the microamp range on this meter. Now, we know, if you look at the circuit, we know that it's not the two gain setting resistors or the three gain setting

**Dave Jones:** resistors because the other ranges which share those resistors, the nanoamp and the milliamp ranges, are spot on. So, there's nothing wrong with those resistors. So, it must be the 10 ohm current shunt resistor used on the microamp range. Something suss with it.

**Dave Jones:** And I found that it was like this right across the board with most of the units I measure. They were above They were over spec. This one's saying it's 103.28 microamps with 99.7 microamps input. It's crazy. So, let's investigate a

**Dave Jones:** really bad case board. This one's about 3.5% out. Now, based on these two readings here, if you punch in the numbers, we instead of that 10 ohm resistor being 10 ohms, we calculate we should get about 10.35 ohms. So, let's actually measure this

**Dave Jones:** resistor and see if we get around about 10.35. We're We're just ignoring the other resistors in the circuit. We're assuming they're spot on. So, there's going to going to be a bit of play there, but let's actually measure it and

**Dave Jones:** see what we get. Now, because we're talking about a 0.1% resistor and it's a low value of 10 ohms, 0.1% represents 10 milliamps or 0. 01 ohms. So, the test When you short out the test leads on your multimeter like this,

**Dave Jones:** we'll use the Metrahit Energy for this, okay? Then you're talking You've got to zero out the residual resistance in these test leads when you're doing something like this. So, it's 0.29 ohms. 0.29 ohms, let's zero that out. Okay,

**Dave Jones:** it's pretty close to zero and we're after 10. 35 or thereabouts. Let's have a look. 10.3334. There you go. Bingo. The resistor's about 3.3% out of tolerance. Unbelievable. Now, of course, we can't just leave it at that. Let's try another meter just in

**Dave Jones:** case, you know, something might be happening with the meter. I've got the Fluke 87 here. Let's zero out the test leads, shall we? .15. There we go. And let's probe this resistor here. You've got to really have sharp when you're

**Dave Jones:** talking um this lower resistance. You've got to have really sharp probes. So, the ones that come with um say the uh the the Metrahit Energy, they aren't very sharp at all. They're, you know, really thick ones. So, you've got to actually

**Dave Jones:** get really sharp probes to get in there to um get through the oxide coating on the solder joint and all that sort of stuff. So, you really need to make a good connection, but there it is. 10.35 34 ohms. It's exactly what we got with

**Dave Jones:** the other one. Confirmed. Hey, but I'm still not convinced. So, let's get the Agilent meter and give that a go, shall we? Null that out. And there it is. 10.34 ohms. Gotcha. Now, thankfully, I just so happened to

**Dave Jones:** have some resistors left over from the build. And there's the part number, okay? You can clearly see it's the correct part number. I can go through that on Digikey, but um I've got some left over over resistors because, who

**Dave Jones:** knows? They may have been damaged during soldering or something like that. They could have drifted. Who knows? But these are brand spanking new from the packet. I've got one here on the bench and let's check it out. It's really hard to probe

**Dave Jones:** a little 0805 resistor, so bear with me. When it's not on the board, it can be a little difficult.

**Dave Jones:** 10.23 ohms. There you go, you saw it, eh? I tried a few others and similar thing. So, it's nothing to do with the soldering at all. The ones out of the packet that are supposed to be 0.1%. It's hard to see there. It you you think

**Dave Jones:** it says 1%, but there's actually a decimal point in front of that. 0.1% uh you know, a couple of percent. It's crazy. Just as a sanity check, I've got one of my original units from my very first batch here, and let's measure that

**Dave Jones:** and see what we get. Let's measure the 10 ohm resistor. And what do we get? There it is, 9.9 10.00, exactly what you expect, within 0.1%. Not a problem. So, there's something seriously wrong with this new batch of

**Dave Jones:** resistors. And here's my original unit hooked up measuring, as you can see, input current 99.74 microamps, and the measurement out of the micro current is 99.76. Pretty darn close, well within uh 0.1% spec. So, these new units are ruined.

**Dave Jones:** Okay, I know what you're thinking. I've only done a what's called a two-terminal measurement with a regular multimeter. What about a four-terminal measurement? I'm glad you asked. Now, if you don't know what a four-terminal measurement is, let me explain or a four-wire

**Dave Jones:** measurement. It's a special resistance measurement. You got to have a special meter that supports four-wire. I happen to have my Hewlett-Packard 3478A bench multimeter here that supports regular two-wire and what's called four-wire measurement. And this is how it works.

**Dave Jones:** If you have a regular you try to measure a resistance like this. What it does is it has a current generator just like it has in a normal multimeter, but instead of reading back of the value right in

**Dave Jones:** here, what it does is it actually has a second set of wires and a second set of inputs that is a voltmeter. So, you're measuring the current and the voltage, but you're measuring the voltage right at the point

**Dave Jones:** of the resistor. So, you're not measuring the extra voltage drop along the resistance of the wires of of the wire that's actually carrying the current. So, what you do is you probe it directly on the resistor itself and you

**Dave Jones:** get a very very accurate measurement effectively nulling or zeroing out any effect due to the test leads whatsoever. Now, this is shows it is two separate leads like this, but often well, usually they're they're actually um they're actually the same set of test leads, but

**Dave Jones:** they'll have instead of just one wire, they'll have two wires running in them and they'll be connected right at the tip of the actual probe and that goes into the multimeter like that, but you've got to have those special

**Dave Jones:** four-wire resistance probes. Now, I don't have one of those, so I decided to make my own. And it's real easy. It's It's pretty trivial. Now, because it's pretty hard to hold four probes at the same time, you've pretty much got to solder it. So, what I

**Dave Jones:** got is is one of my microcurrent boards and I soldered just the 10 ohm resistor on there, as you can see. There it is there, the the 10 ohm resistor and I've got two wires coming in, which is comes

**Dave Jones:** from the from the current generator basically and then what's called the sense wires are connected directly onto the resistor like that. They're not soldered directly on like they should be be the microcurrent layout the board layout already has the wires actually

**Dave Jones:** going directly onto the resistor. But you normally solder these sense resistors directly onto the contacts of the resistor. And let's see what we get. Now hopefully you can see that. It's not that great in the light. But what I've

**Dave Jones:** got it is on is I've got it on two-wire measurement. And as you can see it's 10.227 ohms basically. But let's switch it to four-wire measurement because I've got the uh two current uh ones here what's called the input and then you've got the

**Dave Jones:** uh sense wires here. So let's switch to four-wire measurement and that effectively takes out any effect due to the uh test leads. And as you can see it's 10.08 ohms. So it's actually 0.8% out. That's no good at all. It's

**Dave Jones:** supposed to be 0.1% or better. So we're expecting 10.01 or better on this display. And we're not getting it. So clearly um it shows that there's something wrong with these resistors. This was just a random one picked out of

**Dave Jones:** the brand new batch. Now if you actually want to do your own four-terminal resistance measurement at home and you don't have a meter which supports four-terminal resistance measurement that's fine. You can actually do it with two multimeters. One

**Dave Jones:** to measure voltage and one to measure current. And you use Ohm's law. Simple. And here's an example of using two multimeters. I've got my four-terminal board again. I've got uh my constant current generator. If you don't have a

**Dave Jones:** constant current generator that's okay. You can just use a voltage source. Generally with a series protection resistor um because you don't want to blow a low value like this. You don't want to put 10 volts across 10 ohms,

**Dave Jones:** okay? So um you need a series dropper. So we're measuring the current. We're putting through 9.963 milliamps. There it is. And we're getting we're measuring across directly across the resistor, directly probing it, 100.43 millivolts. And if you whack that into

**Dave Jones:** the calculator, you get 10.08 uh ohms, which is exactly what we got with our Hewlett-Packard uh here. We got uh 10.081, actually. So, near enough. Okay? And that's how you can do a simple four-terminal resistance measurement with two multimeters.

**Dave Jones:** And one of the main benefits of this is that you can measure actually really very low values of resistance. You know, down to milliohms or thereabouts, which a regular multimeter just can't measure on its ohms range, no matter how good it

**Dave Jones:** is. Um you know, you can have a real super precision bench meter like this. If you try and measure the resistance, your probes are just going to swamp anything under generally about, you know, an ohm or 10 ohms or under, you

**Dave Jones:** really should be using a four-terminal resistance measurement to get accurate results. Okay, let's use our little Extech uh microscope here to take a look at the one from that we actually got from the batch. Now, it looks to me it looks

**Dave Jones:** pretty close to my original ones, but we'll have a look at that in a minute. And there's the identifying mark on it. There you go, 10R0, which indicates that it's a precision resistor.

**Dave Jones:** So, that looks pretty good. Now, let's uh do a comparison with the one on my original board. Now, as you can see, there it is. It's a bit harder to say because it's mounted on the board. I can't quite uh zoom in

**Dave Jones:** as well as I could on the other one, but it looks like it's an identical resistor. So, I think it's actually the correct uh type, but why it's um several percent out, I've got no idea. So, there you have it. What's going on

**Dave Jones:** with these resistors from Digi-Key? Now, these are actually from a company called Bourns, uh who manufacture some pretty good resistors. They're world-renowned. They manufacture great resistors. Now, so either Digi-Key are at fault here, they've shipped me the wrong part, or

**Dave Jones:** Bourns are at fault because they've sent them to Digi-Key incorrect. I don't know who's actually at fault here, but if you look at the part number, the part number is Here it is. Let's look at the Digi-Key website. It's the BYC

**Dave Jones:** RT0805 BY- 10A0ELF. And the Digi-Key website says that's 0.1% 0805. And if you look at the data sheet here from Bourns, you can see that the the B in the after the 0805 there, the B stands for 0.1%.

**Dave Jones:** And the Bourns this uh particular CRT series of resistors is available um up to of anywhere from 1% tolerance down to 0.01% tolerance. So, but clearly I've had some that are greater than 1% out. So, it's almost as if they aren't actually this

**Dave Jones:** CRT series. They you know, they've actually screwed it up beyond just giving me the wrong particular type. They've uh the wrong the wrong tolerance. They've actually gone for I think it's a totally different type of resistor. Anyway, I'm not happy. Not

**Dave Jones:** happy with Digi-Key or Bourns, whoever damn well fault it is. I don't care. I've been screwed over. And yeah, it's my own fault. I should have tested them a bit more thoroughly before I uh sent a couple of units out, but jeez, you trust

**Dave Jones:** these things to be you know, when you buy 0.1% you expect 0.1%. Now, if they if I got the wrong part, odds on I would have got the wrong value or something like that, and it would have been obvious. But in this case, no. I

**Dave Jones:** got the wrong tolerance. And that can be a real pain in the ass when you're aligning that tolerance in your design because sometimes, unless you do exhaustive testing, you might not notice it. It's a real pain in the ass. Not

**Dave Jones:** happy at all. Digi-Key, what's going on?
