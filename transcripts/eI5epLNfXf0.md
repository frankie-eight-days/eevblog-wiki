---
video_id: eI5epLNfXf0
title: EEVblog 1736 - TOP 5 Jellybean MOSFET's
url: https://www.youtube.com/watch?v=eI5epLNfXf0
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 32, "3": 52, "4": 67, "5": 81, "6": 93, "7": 105, "8": 119, "9": 135, "10": 147, "11": 159, "12": 173, "13": 184, "14": 197, "15": 209, "16": 224, "17": 235, "18": 246, "19": 262, "20": 283, "21": 296, "22": 310, "23": 326, "24": 342, "25": 357, "26": 374, "27": 389, "28": 403, "29": 417, "30": 431, "31": 446, "32": 460, "33": 473, "34": 488, "35": 503, "36": 515, "37": 530, "38": 544, "39": 558, "40": 575, "41": 589, "42": 600, "43": 614, "44": 625, "45": 634, "46": 648, "47": 662, "48": 676, "49": 689, "50": 705, "51": 717, "52": 733, "53": 747, "54": 762, "55": 775, "56": 788, "57": 808, "58": 826, "59": 842, "60": 857, "61": 871, "62": 885, "63": 901, "64": 915, "65": 932, "66": 944, "67": 956, "68": 976, "69": 993, "70": 1007, "71": 1023, "72": 1037, "73": 1051, "74": 1064, "75": 1075, "76": 1087, "77": 1102, "78": 1116, "79": 1129, "80": 1144, "81": 1157, "82": 1174, "83": 1189, "84": 1204, "85": 1218, "86": 1233, "87": 1246, "88": 1261, "89": 1275, "90": 1287, "91": 1303, "92": 1316, "93": 1329, "94": 1345, "95": 1358, "96": 1374, "97": 1386, "98": 1400, "99": 1413, "100": 1429, "101": 1444, "102": 1462, "103": 1478, "104": 1492, "105": 1512, "106": 1528, "107": 1541, "108": 1559, "109": 1576, "110": 1594, "111": 1608, "112": 1619, "113": 1631, "114": 1644, "115": 1660, "116": 1675, "117": 1690, "118": 1702, "119": 1713, "120": 1726, "121": 1744, "122": 1762, "123": 1776, "124": 1791, "125": 1806, "126": 1822, "127": 1835, "128": 1854, "129": 1867, "130": 1883, "131": 1902, "132": 1920, "133": 1935, "134": 1947, "135": 1960, "136": 1978, "137": 1993, "138": 2008, "139": 2022, "140": 2037, "141": 2050, "142": 2067, "143": 2082, "144": 2098, "145": 2112, "146": 2125, "147": 2140, "148": 2156, "149": 2168, "150": 2181, "151": 2192, "152": 2205, "153": 2218, "154": 2232, "155": 2246, "156": 2257, "157": 2270, "158": 2284, "159": 2297, "160": 2309, "161": 2322, "162": 2338, "163": 2350, "164": 2363}
---

**Dave Jones:** Hi, it's time for another installment in the jelly bean component series. I'll link in the playlist down below if you haven't seen them before, where I've done jelly bean op-amps and voltage references and I've done bipolar transistors before and a lot of people

**Dave Jones:** since then have been asking for the same video on MOSFETs. So, here we go. So, MOSFETs or metal oxide silicon field effect transistor, that's the name, MOSFET or moosefets as I often call them, they are pretty much ubiquitous these days. They're more

**Dave Jones:** popular than BJTs for lots of reasons. They are better lower RDS on, which is the on resistance of the transistor, so that's better. It's called RDS on in a MOSFET versus VCE sat typically in a BJT. And that lower on resistance means

**Dave Jones:** lower voltage drop and more power handling more current handling capability and more power handling capability in a specific package, for example. So, if you've got like a little sub 23 package and it's got a lower RDS on, you're going to get a lot more bang

**Dave Jones:** for buck in your current and your power dissipation in a given package size in a MOSFET typically. And in a MOSFET, they're voltage driven as versus essentially current driven in a BJT. So, there's no constant base current like

**Dave Jones:** you get in a BJT transistor. You've just got a gate voltage. You switch on the gate voltage and the transistor switches on. As a switch, in probably the majority of applications, you're going to be using MOSFETs for switching

**Dave Jones:** purposes. You know, you switch on a relay load, you switch on an LED load or you're pulse width modulating some LEDs or something like that or using it as a switching element in a DC to DC converter, something like that. This is

**Dave Jones:** what MOSFETs are really good at. They're better than BJTs. It's why they're more popular. When you're talking about switching frequencies for like high frequency DC to DC converters which can go into the megahertz region, They're faster and more betterer than BJTs for

**Dave Jones:** that. So, MOSFETs universally popular these days. Of course, that doesn't mean nobody uses BJTs anymore. BJTs still have advantages in like linear applications. They're more robust. You know, there's no gate to blow, for example, via ESD or something like that.

**Dave Jones:** So, BJTs still have their place, but you know, you're going to need some jelly bean MOSFETs. So, here we go. There's several criteria that define a jelly bean component. The first one is that it's been around for a long time. It's

**Dave Jones:** old. The first one we're going to look at here dates from like the late '70s, early '80s. So, it's been around for a long time. Everyone knows it. It's really established. The second thing is that it's available from multiple

**Dave Jones:** manufacturers. You know, you don't just want a single source component. That's not a jelly bean part, even if it's available from two or three manufacturers, not really jelly bean. Has to be available from dozens of manufacturers, both Western and like

**Dave Jones:** Asian sources as well that you've never heard of. The third criteria is that needs to be insanely cheap, especially, you know, like a buying a reel of 3,000 of them, you don't want to be paying a dollar each. You want to be paying a

**Dave Jones:** cent each or 0.1 cents each. So, they've got to be really low cost. They've got to be available in stock as well from all of the regular component catalog component suppliers that you're used to. And because they're available from all

**Dave Jones:** the different manufacturers and the stocks are in the millions of these things, then that's what makes them easy choice as jelly bean component. If you just need a MOSFET to just throw in your circuit, you don't really care about the

**Dave Jones:** specs that much, then you throw in a jelly bean component. Then, when you go to manufacture your party novelty gadget, you can be guaranteed that then your purchasing people can then go and purchase like any one of a dozen

**Dave Jones:** different brands, and it really doesn't matter. It's guaranteed to work. And from the design aspect, when you're choosing a jelly bean component, you don't go like you don't download the data sheet and go "Oh, look I can push

**Dave Jones:** the spec right on the edge of this limit over here." No, no, no. You're not in jelly bean territory anymore. Jelly bean territory, when you design it into your product, you go and look I'm smack bang in the middle of the specs so it doesn't

**Dave Jones:** matter which manufacturer I choose, it's practically guaranteed to work. So if you're pushing the spec limits, you're not using a jelly bean component. The first jelly bean MOSFET is the absolute classic 2N7002 here. It's also it started out as the uh

**Dave Jones:** 2N7000 in a TO-92 package back in the late '70s, early '80s from Siliconix back then who are now Vishay, hence why I've got the Vishay data sheet open. But I'm going to say it's the 7002 cuz the 7002 variety is the SOT-23. So

**Dave Jones:** you're more likely to use the SOT-23 variant these days for your pick and place machines and your newfangled surface mount stuff. Not many people use the BJT variety anymore. There are like some variants like a quad dip package

**Dave Jones:** and stuff like that, but we're not going to worry about in that. It's a 2N7002. This is you'll find this everywhere and it's an N-channel jobby of course. Our MOSFETs are available in N-channel and P-channel. Most of the time you're going

**Dave Jones:** to use N-channel because you're going to be using as a low side switch, you know, driving a relay or an LED string or something like that or switching element in a DC-to-DC converter. They're usually going to be using N-channel and that's

**Dave Jones:** equivalent to NPN in bipolar transistors as opposed to PNP. So the 2N7002, what do you get? So we're not talking anything spectacular spec or current-wise here, but it's if you just need a simple MOSFET to switch on a

**Dave Jones:** couple of basic LEDs at you know if tens of milliamps or even 100 milliamps, something like that, then this jobbie is for you, or a relay, for example, then no problems whatsoever. It's basically a 60 V rated part, plenty for almost

**Dave Jones:** every, you know, generic application. It's RDS on is not that great. It's spec like it's advertised as having 2.5 ohms here, which is pretty high for an RDS on of a MOSFET. We're going to see much better later, but hey, it's good enough

**Dave Jones:** for a straight. It's good enough for almost every, you know, simple application up to say a couple of hundred milliamps, something like that. It's got low input capacitance, 22 puff. It's got low voltage threshold, which we'll take a look at. So, it can operate

**Dave Jones:** from low logic level stuff. And this was like game-changing back in like the 1980s, for example. Oh, you can drive the MOSFET directly with your 5 V or even three newfangled 3.3 V logic. Beauty. So, if you just need to drive

**Dave Jones:** something, doesn't matter what it is that your microcontroller, for example, can't drive, cuz you usually only get, you know, like 5, 10 milliamps, or something out of it, like a microcontroller IO, for example. Need to drive anything harder than that, then

**Dave Jones:** this is your friend. 7 nanosecond switching speed here. So, when you're driving MOSFETs at low voltages, what you need to look at is the gate threshold voltage here, VGS. So, at a drain current ID here of 1 mA, it's only

**Dave Jones:** going to specify that on this particular data sheet. Typically like 2.1 V, so you can operate this directly from 3.3 V logic. That'll turn the gate on. So, if your output of your microcontroller 3.3 V, it'll turn that gate on, and then

**Dave Jones:** switch your MOSFET on. The other main thing you're going to be concerned with for jelly bean performance is the on is the RDS on, the on resistance when you switch that gate on, and when how many ohms do you get across the drain and

**Dave Jones:** source terminals. That's why it's RDS, the drain and source are the two terminals. So, as I said, it's not very spectacular at and this is going to change with VGS, your gate voltage. So, at 10 volts here, you know, you're looking at like,

**Dave Jones:** you know, a couple of ohms, 2.4 ohms. It can rise at lower voltages, for example. So, it it's not spectacular. It's not designed for high current, but you know, 100, couple hundred milliamps, no worries. And 1 MHz switching frequency,

**Dave Jones:** if you care about your input capacitance on a jelly bean part, you're probably not in jelly bean category. And because we're talking about a SOT-23 package here, it's tiny, so power dissipation is only like max, absolute max at room

**Dave Jones:** temperature, like 0.2 of a watt, not much. So, the important thing with all MOSFETs, and I'll go over it a bit in detail on this one, and I'll skip it for the future ones, but the ID, or the

**Dave Jones:** drain current on your Y axis here, versus your VDS, not VGS. This is the drain to source voltage. So, like I said, like you can operate this from a logic level, you can put 3.3 volts on the gate, for example, switch

**Dave Jones:** the transistor on, but then you can have a higher voltage across your drain and your source. So, you can, you know, be like a big LED string, for example, can be powered from say 12 volts, and your logic can easily drive that with 3.3

**Dave Jones:** volts or 5 volts on the gate can easily drive that higher VDS voltage drain to source. So, you get these characteristic for different values of VGS, the gate voltage. So, if you say they don't actually have one for 3.3, but let's say

**Dave Jones:** 3.5 volts here, okay? If you're driving it with your 3.3 or 3.5 volt logic, we're talking about, right? This is drain current, you know, over 100 milliamps there, maybe 150 milliamps. This will vary slightly, you know, bit between parts from different

**Dave Jones:** manufacturers, but you know, at that low VGS uh voltage, you can do 100 milliamps there pretty safe. And at uh 5 volts here, well, you know, you can do like over 400 milliamps, no problems. And the transfer characteristics is the other uh

**Dave Jones:** common graph that you're going to want to look at uh for MOSFETs. So, it does once again the ID drain current here on the Y axis, but it's the VGS or gate to source voltage here. And you can see as

**Dave Jones:** they and and the characteristic curves are at different temperatures. So, you'll take like room temperature here, but you know, if you're designing for the extremes in your design for extreme uh you know, temperature ranges, um it doesn't vary a huge amount. But yeah,

**Dave Jones:** basically there at a VGS of say 3.3 volts, you know, there it is, you can do that, you know, 100 odd milliamps there if you're you know, extrapolate that and drop it down, for example. Um and if you

**Dave Jones:** do it at 5 uh volts, you know, you're going to get like 400 milliamps out of it. So, it's okay, but it's nothing to write home to your mom about. Tell us the price, son. Okay, let's go to

**Dave Jones:** Digi-Key. I'm going to be using Digi-Key and LCSC. Uh so, Digi-Key for a Western supplier and uh LCSC as a catalog uh Asian uh supplier over here. First thing, we said has to be available from multiple manufacturers. Check it out.

**Dave Jones:** Look at this. Ones you've never heard of. Diodes Incorporated, you've probably heard of. There's Microchip Technology, ON Semi, you know, and the Shish Siliconics, of course. So, the parametric selection I've got in stock only because it's jelly bean, it's got

**Dave Jones:** to be in stock, and then we can sort by the lowest price first, like this. And look at this. We're looking at 1.3 cents, Yankee cents each. That's from Formosa Micro Semi, you might have never heard of them. Venkel, MDD, Diodes

**Dave Jones:** Incorporated, you've probably heard of. But look look look at the stocks here. 770,000, 300,000 in the marketplace, 10,000 in Digi-Key. You can get a reel of 10,000 of them. Uh you know, 4.7 cents, that's getting a bit pricey. But

**Dave Jones:** you You see even from Digi-Key, no shortage of stock. Let's go to LCSC. Let's go in stock and we sort by price here and look at this. Um Asian brand LLC. Never heard of them, but they've got 10 million in stock at

**Dave Jones:** the catalog supplier at LCSC. And if you get 6,000 of them, they're 0.3 cents each. That's how cheap these things are. And we can go and actually have a look at the data sheet for this company. I've never never heard of them.

**Dave Jones:** LRC. There you go. It's it's this 7002. There it is. Low-side switch, you know, level shifters, DC to DC converters, and it's the characteristic curves are going to be like basically the same as what we've seen. VGS 3.3 volts. Oh, this one

**Dave Jones:** can do up to 300 milliamps there. So, maybe you know, that's a little bit better than the Siliconix one, for example. But, if you're equivalent as I said, if you're designing in that or 300 I you know, I need 300 milliamps through

**Dave Jones:** this thing at VGS 3.5 volts, no. You've chosen the wrong part. You you lock yourself in to a lower subset of suppliers there. You shouldn't be doing that, but like 100 milliamps, yeah, they'll all do it. So, all these

**Dave Jones:** different manufacturers, take a look at them. You've never heard of most of these. I guarantee it. All right. [laughter] Look at this. Look at this. This is just nuts, right? And these are the ones that are in stock. In stock.

**Dave Jones:** So, if you design the 2N7002 into your product, um you've got a pretty safe bet that you're going to be able to get this thing. And at 0.3 cents each, it's an absolute no-brainer. And that's why that is the

**Dave Jones:** first jelly bean MOSFET. And we're not forgetting you P-channel fanboys, cuz you might have a P-channel applications. For the jelly bean equivalent to the 2N7002 is the BSS84. It's been around since like the late '80s or something like that. SMD parts SOT-23. And it's

**Dave Jones:** basically the sort of wimpy equivalent to uh the N-channel uh 2N7002. So, we're talking 50 V or -50 V because it's a P-channel, and we're talking, you know, in wimp a wimpy RDS(on) of like 10 ohms here at VGS uh 5 V or -5 V. Um and, you

**Dave Jones:** know, 130 mA like. So, yeah, it's but it is the traditional equivalent. So, if you're going to stock the 2N7002, you're going to be stocking the BSS uh 84 as well. And it's a bit pricier cuz it's not as popular, so we're talking uh

**Dave Jones:** 5.9 cents here. Once again, it's in stock, you know, in the hundreds of thousands at Digi-Key. And over at LCSC here, yeah, yeah, we're talking like, once again, um 0.39 cents or thereabouts in 50,000 uh quantity. Um so, it's a

**Dave Jones:** little bit pricier, not as much stock, like, you know, we saw like millions, 10 million stock before because the N-channels are more popular than the P-channel. So, not as popular the BSS 84, there's typically going to be better

**Dave Jones:** options as we'll uh see next. But, that is the traditional P-channel equivalent. So, worth calling out. And the characteristic curves for those playing along at home, it it does okay. It's a basic equivalent, as I said. So, yeah,

**Dave Jones:** but I have a better option for you next. Our next jelly bean part is the Alpha & Omega AO3400. In this particular case, the 3400A, I think they have officially discontinued the 3400, but available from every manufacturer. And but uh Alpha & Omega,

**Dave Jones:** hence the part number AO, they were the ones who introduced this in the late 2000s, I think it was, or thereabouts. So, this is not an old part at all. It's relatively new, but it's gained jelly bean status so quickly because it was

**Dave Jones:** just so good and so plentiful. Everyone copied it, and now it's available from all and sundry. So, whilst the 2N7002 is absolute classic jelly bean, this is kind of like the one you want today. This is like the jelly bean part.

**Dave Jones:** If you only have to stock one today, you're going to be stocking this one because it's it it is the most versatile. It's like order of magnitude better, as we'll see, than the 2N7002 for not much more increase in cost. A

**Dave Jones:** little bit more expensive, just a smidge, but check it out. So, it's not as high a voltage. Like like we're talking 30 volts here, okay? So, but still 30 volts covers like probably most of the stuff that you're going to work

**Dave Jones:** with. But, look at the ID. Look at the drain current. 5.7 amps. This is a SOT-23 package. 5.7 amps in a SOT-23. You've just like this is order of magnitude better stuff than the 2N7002. So, this is the one you want for like

**Dave Jones:** throwing in like the 2N7002 is not really suitable for like DC-to-DC uh converters. For example, with a couple of home a couple of ohms on resistance, you're just dissipating pissing away too much power in your switching transistor. But, this jobby, absolutely fantastic to

**Dave Jones:** have like, you know, 5 amps capability is just absolutely brilliant. So, and RDS on, we were talking about ohms before at at at at a VGS of 10 volts. Now, we're talking not ohms, we're talking tens of milliohms. Like 26

**Dave Jones:** milliohms stuff. And then they even specify so proud of it. They even down at 2.5 volts drive, we're we're still talking 48 milliohms on resistance. So, you multiply your drain current by your on resistance and you know, V squared on

**Dave Jones:** R, and that's how much power you're dissipating in this thing. But, little SOT-23 package can do this much current. It's incredible. So, drain source voltage, as I said, 30 volts maximum. Gate source voltage, it'll do plus minus 12 volts, so you can drive it, uh, you

**Dave Jones:** know, from fairly high, uh, voltages, but that continuous drain current, look at it, like for it, like 5 amps is is is pushing it for this thing, like this is absolute maximum, uh, rating. So, you wouldn't, you know, use it for that,

**Dave Jones:** but, um, let's go down. So, these are absolute maximum ratings. You don't want to exceed these, but it's just it's incredible. And you can say like the absolute power dissipation is like a watt here in a little SOT-23. Ooh, it's

**Dave Jones:** going to get a bit warm-sky if you try and dissipate a watt in it, but, um, yeah, this is just this is incredible. And if you care about like a leakage, for example, between your drain and source, you know, it's at like a maximum

**Dave Jones:** of 1 microamp here, you know, it's not much. But, look at this RDS on. This is just like killer, right? So, these are these are your, uh, not like down at 2.5 volts, it can do an and an, uh, current

**Dave Jones:** of, uh, 3 amps. So, you know, it'll easily do like, uh, 3 amps, uh, for example. Uh, you know, you're talking 24 milliohms typical, 48 milliohms maximum. Milliohms. So, get your confuser out here and, uh, your I squared R loss,

**Dave Jones:** your power dissipation in this thing at say 3 amps here at, uh, 24 milliohms, you're only, uh, talking like 0.2 watts. So, you know, well within the package capability that we saw of 1 watt. So, for a SOT-23 package, this is like, you

**Dave Jones:** know, pretty much the duck's guts. Fantastic. And I forgot to mention, uh, as with all of, uh, these, uh, MOSFETs, due to the construction of them, you're going to get your back diode across your drain and source here. This is just, uh,

**Dave Jones:** inherent in the physical, uh, silicon construction of this. I'm sure I've done that in a video somewhere, but you basically get that, uh, back diode for free. But, it's input capacitance, uh, 630 puff. You saw we were in the like the 20 puff, uh, region

**Dave Jones:** before, uh, for the 2N7002, but you're typically going to get that. You're going to get a greater, uh, gate capacitance in there the gruntier your MOSFET is. That's just a general rule. And once again, this is because of the

**Dave Jones:** physical construction of the MOSFET, a higher current MOSFETs like this one need a bigger like physical surface area in there. The bigger the physical surface area you have on the actual transistor substrate itself, the greater the capacitance. So, it it they

**Dave Jones:** just go hand in hand. You you know, it's just a side effect of that. But, for jellybean applications doesn't matter. Just as a little aside, this gate capacitance is not called that here, it's called the input capacitance, which is CISS, which strictly speaking

**Dave Jones:** is not the gate to source capacitance. It actually includes the gate to the drain and source shorted together. But, it's basically the total capacitance that your driver is going to see. So, you know, it's effectively the gate capacitance, really. And they're pretty

**Dave Jones:** darn fast. Look at these turn on times here, you know, down in the nanoseconds. You can see the characteristic curves here, for example, like even specifies it down at VGS at 2 V here. You know, look, it's it's just bragging. I mean,

**Dave Jones:** granted, these voltage drops here, VDS, is getting quite high, you know, you often don't want to drop a couple of volts on your drain source there. But, you know, look, 10 amps, 20 amps, this is just like insane sort of stuff. But,

**Dave Jones:** we can look at the RDS on in milliohms here. So, you know, look, around what, you know, 18 milliohms or something like that at VGS 10 V and VGS 4 V. Not a huge difference between that. But, look at

**Dave Jones:** the currents you can do. This is just like what? But, you typically want to would wouldn't want to do these types of, you know, 10s, 20 amp sort of stuff in a SO-23 package. So, yeah, don't be going there. And the thing with MOSFETs

**Dave Jones:** is there's plenty of different graphs, for example, like here we go. Here's RDS on again, versus your VGS voltage like this. And you can see, that's why they say, like, you know, 2 volts, once you get down to it like 2 volts gate source

**Dave Jones:** drive on this thing, it's, you know, hasn't got much more to give there, captain. And if you pull up other manufacturer data sheets like NextGen, who you've probably never heard of, you know, similar look, 5.8 amps here, you

**Dave Jones:** know, 27 milliohms RDS on. Now, when you start talking about high current products like this, you know, look, it says ID here, right? 5.7 amps there. Okay? That's the continuous drain current. And sure enough, in the absolute spec ratings here, continuous

**Dave Jones:** drain current, okay, you know, 5.7 amps. If you continuously putting continuous current through there, you don't want to exceed that. But, aha, it you can actually get a lot more than that in pulse current. Let's have a look here.

**Dave Jones:** This is why the on state drain current here, it can actually technically do 30 amps, but you know, you don't want to be pushing 30 amps through a sub 23 package, but you might be able to in, like, for a

**Dave Jones:** brief period of time. But then you'll get what's called a safe operating area. So, this is characteristic curve, and this is your ID in amps, your drain current in amps here. And as you can see, this is logarithmic access, so axes, so it's a

**Dave Jones:** bit harder, but there's basically 1 amp here, 10 amps up here. So, you know, it can go up to that 30 amps maximum there that it said up above. But then you've got time here, 10 microseconds, 100 microseconds, 1 millisecond, and they're

**Dave Jones:** your different characteristic curves. So, if you're doing it for 10 seconds here, for example, that curve, that 10 second curve there, is a little bit higher than this like DC curve here. Okay? But at DC, at your drain

**Dave Jones:** source voltage of like, you know, 0.2 volts or something like that, you're going to be doing 1 amp, 2 amps, 3 amps. You're going to be doing that for, you know, 4 5 amps or whatever that we saw as the maximum

**Dave Jones:** continuous rating there. And then above that, um, yeah, for 10 milliseconds, 1 millisecond, you know, 100 microseconds. If you're doing really fast uh switching, you can do it. But if you are getting, you know, really into the tens of amps

**Dave Jones:** range, this jelly bean's probably not for you, but it can do it for short periods. Pretty cool for a SOT-23 package, let me tell you. We won't even get into the normalized transient thermal resistance. Oh jeez, you can go

**Dave Jones:** and look that one up in your own. So Digikey here, as you can see, we've got like 169,000 stock. We're talking like, you know, 10 cents each, something like that. Little bit, oh no, no, 6 75,000 quantity. Um, 6.8 cents. So it's a bit

**Dave Jones:** pricier, but uh you'll get it cheaper if you go to LCS. See, um look, 129,000 stock here. We're talking like 0.8 cents, 0.8 cents there. Yeah, it's double the price of the 2N7002, but oh, for 10 times the capability, uh it's a

**Dave Jones:** no-brainer stock the AO uh 3400. And once again, available from all these manufacturers. Look at them all. It's just, yeah, yeah, the silly buggers. And for you P-channel fanboys, uh it's the AO 3401 or 3401A. So we can take a quick squeeze at that,

**Dave Jones:** but it's basically the uh P-channel equivalent to uh the 3400. So that's nice and easy to remember. 3400, 3401. Um, once again, you know, we're talking 30 volts. We're talking, you know, slightly less uh continuous DC current at 4 amps, you

**Dave Jones:** know, a bit more on resistance and stuff like that, but um that's not uncommon in the uh that's fairly typical for uh P-channel versus uh N-channel, but apart from that, everything's like pretty similar. It's similar sort of uh

**Dave Jones:** ballpark. That's why they're complementary. Huh, complementary transistor, get it? I'm here all week. 27 amps or negative 27 amps here. Like so, it's it's a little bit less, a little bit less, but still fantastic parts. The AO3400 and the 3401.

**Dave Jones:** Digikey selection and stock isn't great here. They've only got like three different manufacturers, for example, but they all have stock. But once again, at LCSC here, look at all the manufacturers. Just crazy. Half a million stock, 900,000, 1.7 million.

**Dave Jones:** Just crazy, right? And we're talking Oh, have I haven't even sorted that yet. $0.9 each for 50,000 quantity. >> [laughter] >> Crazy. We can go and have a look at that manufacturer's data sheet, for example. Never heard of them. Wang Wang

**Dave Jones:** Electronics Co. or whatever. But they're all going to be equivalent. Fantastic. If you only had to stock Well, two N-channel and P-channel parts, it'd be the AO3400 and 3401. Definitely. If you need something even gruntier than the 3400 we looked at,

**Dave Jones:** well, we need to now look at the AO4400 series. So, it's the AO4400XX series. There's there's ton of them. So, if we just type in AO44 into Digikey here, like we get a whole bunch of these Alpha and Omega ones. But there is one

**Dave Jones:** king, basically jelly bean, of the 4400 series, and that's the AO4410. Unfortunately, if we type that into Digikey, we only get the one hit, and it's not even from Alpha and Omega. I don't know why. Western suppliers for this thing is

**Dave Jones:** a bit limited. So, in So, it's UMW here. Okay, we can we we can pull up their data sheet. Never heard of UMW. But as you can see, it's available in the SO-8 package. So, the SO-8 package is going

**Dave Jones:** to be bigger and better. It's going to have more surface area in there. It's it's to dissipate more power, it's going to have low lower RDS on, greater dissipating power handling capability, so it's going to be even gruntier. So,

**Dave Jones:** we're moving up a package from the SO23 to the SO8. But, even though it's only got one hit here on Digikey, if we go over to LCSC, if we have a look at the manufacturers that are in stock, there

**Dave Jones:** is, you know, 1 2 4 6 8, like, you know, more than half a dozen different manufacturers, and they've got no shortage of stock. And if we source by price, you know, we're talking as little as 3.7 cents, for example. So, let's

**Dave Jones:** pull up some data sheets for this SO8 package part. And typically, when you go to like higher power, more exotic devices, even the jelly bean, they become less jelly bean, because they're more, you know, specific requirements. But still, half a dozen manufacturers,

**Dave Jones:** and if you do like a ton of tear downs, you'll find this everywhere, the AO4410, or maybe the AO4414, which is a a similar device, but the 4410's a bit more jelly bean than the 4414. Slightly slight differences, but let's

**Dave Jones:** go with the 4410, shall we? Editing permission is currently restricted. For some reason, that manufacturer password protected their data sheet, so I couldn't like annotate the damn thing. So, anyway, >> [laughter] >> let's choose another one. So, yeah, SO8

**Dave Jones:** package here, there's no thermal pad on the bottom, so you can't get dis can't get stuff out. But look, we've got four pins for our drain now, instead of one, and we've got three pins for our source, instead of one. So, and in

**Dave Jones:** countless tear downs I've done, you've no doubt it's a dead giveaway that it's a MOSFET on the board, even if you can't identify the number, if all these four pins are shorted together, these three pins are shorted together, and then

**Dave Jones:** you've got just the one little pin piddly pin left over for the gate, you know it's a MOSFET. So, we're talking 30 volts, 15 amps here, so three times same voltage, but basically three times the current we could get in that piddly

**Dave Jones:** little piss-ant SOT23 package. RDS on, look at this. 6.5 mΩ here at 10 V VGS. Even at 4.5, we're talking 12 mΩ. Now we're talking. Pulse drain current maximum, we're talking 42 amps here. Continuous drain current, 8.2 amps. RDS

**Dave Jones:** on in the like typical region, we're talking like 7.5 and 11 here at 4.5 V at 8 amps and then 10 amps continuous current. So, if you want a gruntier MOSFET, the SOT23 package is not really going to cut the mustard. You need this

**Dave Jones:** SOT8 package here. And we're talking maximum power dissipation of 1.5 W in the package. And this is rather interesting. You'll see at VGS at 3 V here. Yeah, we get this characteristic curve and we can, you know, our current we can

**Dave Jones:** get to 10 amps here with a drain to source with a significant drain to source voltage. But then, you know, so it's not really for ultra low voltage gate drive here. But a VGS of 4.5 V driving IT FOR TTL, WHOA, goes off the

**Dave Jones:** charts. And you can see that over here on the characteristic curve for RDS on versus VGS here. Whoa. Oh, it's a bit how you doing? There you go. Yeah, you can see it like, you know, so it's not for really low VGS voltages.

**Dave Jones:** But, you know, for 5 V drive and stuff like that, killer. And for you P-channel fan boys, the 4407 is the equivalent to the 4410 there. Once again, tons of manufacturers, tons of stock, super cheap pricing. I haven't

**Dave Jones:** even sorted that, have I? No, you know, 5 cents a pop, something like that. Again, manufacturers, there's more manufacturers of the P-channel. And when you start talking higher power like this, you typically might find them in pairs. For example, for like you know,

**Dave Jones:** motor drive, PWM drive, or say, you know, some some driving um, high and low as well. That totem pole, uh, arrangement. Um, so, yeah, um, no surprise that the P-channel is like really quite available and really quite cheap. So, yeah, stock both of those.

**Dave Jones:** And if you've seen the teardowns, you'll find, yeah, as per the, uh, notes here, like battery protection, battery switching, switching a lithium ion battery, do a teardown of any product, you'll find something like this in there switching the lithium ion, uh,

**Dave Jones:** battery or something like that. Um, so, yeah, you know, 15 amps, 6.5 milliamps, 12 milliamps, like really good stuff in a SOT-23, um, SOT-8 package. Beauty. Now, we start getting a bit more obscure. The next jelly bean one, not

**Dave Jones:** quite jelly bean, but if you're into low voltage products, which a lot of people might be, then the best jelly bean low voltage threshold, uh, MOSFET would have to be the, um, IR, International Rectifier, IRLML, it's a handful, uh, 25 O2. And, um, this

**Dave Jones:** is, once again, a SOT-23 jobbie. It's pretty good. It's 20 volts here. It's, uh, 45 milliamps here. Um, but, it's VGS voltages can go really low. Now, the AO34100 was pretty good at this as well, but this goes lower. VGS here, gate

**Dave Jones:** threshold voltage, we're talking a minimum of .6 volts here, maximum of 1.2. So, you know, this can, if you really want low voltage drive, because there's lots of low voltage power rails, um, out there at the moment for FPGAs

**Dave Jones:** and, uh, micro, you know, other like high performance micros and stuff like that, they typically need, like really low, uh, rail voltages. And if you need to switch those or do whatever, then, um, this thing can do the business.

**Dave Jones:** Like, check it out here, they'll actually specify this at, uh, 2. a characteristic curve at 2.25 volts, uh, and they give you the, uh, current. So, it's got, you know, a lot of them can some can go down to like low voltages,

**Dave Jones:** but your RDS on goes through the roof. But, this one can still maintain it down at like 2.25 V. Look at this, we can get like 10 amps here with what? It's logarithmic. 0.1, 0.2, like 0.5 V there. Oh, you can see the fact that

**Dave Jones:** they've like specified this at like 0.25 V increments. Like, that's just crazy, right? You You know when they're doing that with the characteristic curves, that you know they're serious about the low voltage specifications of this thing. And you can get it from a couple

**Dave Jones:** of manufacturers on Digikey here, but of course more on LCSC. If you go over here and have a look, heaps of stock, pretty cheap. Look at this, you know, like 13 cents here. Um it's peanuts. So, this is like more of

**Dave Jones:** like a really edge case design, but you might find your requirement for this in like really low voltage battery design, really low power design where you you know, you've got sniff of an oily rag to drive the gate with, but you still want

**Dave Jones:** a decent RDS on for your you know, whatever loads you're trying to drive, then you know, this thing's pretty much the king. And for you P-channel fanboys, it'll be the IRLML6401.

**Dave Jones:** So, you know, we can take a look at that, but it's basically going to be the P-channel equivalent of this, and it's pretty schmick. There's your VGS drive down there at 2 V, no worries. So, yeah, really sniff of an oily rag, low

**Dave Jones:** voltage, low power sort of you know, gate drive stuff. Yeah, this is what you want. And for our final jelly bean part, yes, we're going even higher power here. You probably can't beat the International Rectifier IRLZ44 here. Absolute classic. Look at this,

**Dave Jones:** fifth generation Hexfet. Might have more on the Hexfet coming in coming weeks after I uh shoot this. Uh by the way, um I'm going to have the inventor of the Hexfet on the show. That'll be interesting. It's available in your

**Dave Jones:** classic TO220/TO262 here. So, whether you want to attach it physically uh to a heatsink with a TO220 package, that is not in this uh data sheet. You can get TO220 uh variants of uh the uh 44 here. Um TO262, but you

**Dave Jones:** know, D-squared. So, these are surface-mount uh jobbies, but uh you know, you can dissipate uh so I've done videos where you can dissipate uh via thermal vias and other things, surface-mount heatsinks, and then uh transfer blocks through the case and

**Dave Jones:** stuff like that. Or you can simply bolt the TO220 on your heatsink. So, when you have to dissipate a decent amount of power, this thing's not too shabby. So, the actual package itself with no heatsink in 3.8 W, but then, you know,

**Dave Jones:** like you're going to really go up there when you start uh heatsinking this sucker. So, it's not too shabby. Uh VGS here, um it can like minimum of a volt. It's pretty great. So, RDS on here, yeah, they specify it. Look at 4 V

**Dave Jones:** here, they specify that at 4 V at 21 A and 4 V drive with 21 A for example, like 35 mΩ. Now we're talking. And maximum continuous current load 46 A, but you can do 160 A pulsed drain current. So,

**Dave Jones:** if we go down and have a look at the uh characteristic curve down here, yeah, look at this. ID at 100 A here for, you know, 20 uh VDS 25 V, 20 μs pulse width. This is like good stuff. They've got the

**Dave Jones:** characteristic curve for 2.5 V, so even if you want to operate it at, you know, particularly low gate voltages, it's pretty terrific. So, I'm going down like 2.5 V down here like this, but then it jumps up pretty quick. Look at this,

**Dave Jones:** right? Yeah, okay, we can only do what uh the 4 A there or whatever. Um and but you jump up to 3-V gate voltage, for example, then you start talking in the 10s of amps here, and then you go to

**Dave Jones:** like That one there is 4-V. Look at that. So, as long as you you know, above 4-V, you start hitting that, you know, peak performance, uh, type stuff. Fantastic. Of course, you're not going to be getting these in the millions, uh,

**Dave Jones:** of units like we could on the other ones, but, you know, there's a few manufacturers here. Um, it's Infineon is the original, you know, International Rectifier/Infineon, um, is the OG here, but it's available from, uh, these other usual, um,

**Dave Jones:** suspects here. And, you know what, 50 cents a pop? But, you know, you can get stock. So, you know, once again, over at Digi-Key, um, if you go over to single MOSFETs over here, let's have a look. Only got a couple of, uh, manufacturers

**Dave Jones:** here, but, you know, you can get this sucker in stock, and, um, yeah. So, it's like about as jelly bean as you can get a power transistor. Shout out to the classic IRF, uh, 510, cuz I know there'll be a few fanboys out there,

**Dave Jones:** "Oh, you didn't include that on the list." Yeah, okay, here it is. Um, yeah, it's not as good as the, uh, 44, though. Um, it's just more better in every way, but this is like a bit Yeah, old-school

**Dave Jones:** jelly bean. And for you P-channel fanboys, the P-channel equivalent, uh, is probably the closest match is the IRF, uh, 904905 here. So, again, have a squeeze at the data sheet here just briefly, but, you know, you're going to get these in

**Dave Jones:** similar packages. You can get it in Did we see it there? We can get it in, uh, yeah, TO- 220, uh, packages here, no worries whatsoever. It's, you know, it's available, it's jelly bean-ish, and it's going to do It's similar HEXFET, uh,

**Dave Jones:** construction, but it's going to do your, uh, P-channel, you know, similar voltage, similar on resistance, similar currents. No worries. So, I hope you enjoyed that look at a jelly bean MOSFET. If you did, please give it a big

**Dave Jones:** a thumbs up, and as always, discuss down below. Yes, I'm sorry, there are millions of different MOSFETs out there. I can't possibly cover everyone's favorite MOSFET. Put it down below. I've used this and I can get them in the

**Dave Jones:** trillions quantity for, you know, 0.1 cents each and blah blah blah blah blah. But, I've covered the ones that I thought are pretty jelly, you know, I pretty much standard jelly bean. If you only have to stock the one MOSFET for generic use,

**Dave Jones:** yeah, it's going to be these Alpha and Omega jobbies both in the SO8, the higher power SO8 packages, and the lower power uh SOT23s here because they're just like even the SOT23 is it's rather incredible. And that's why it's copied

**Dave Jones:** by everyone. And that's why it's jelly bean. Anyway, as always, discuss down below and over on the EEVblog forum linked down below. And if you want to help support the channel, me making videos like this, buy some merch at

**Dave Jones:** EEVblog.store down below cuz, you know, YouTube doesn't really pay the bills anymore. Got to sell the merch. Get yourself a good meter. Catch you next time.

**Dave Jones:** >> [music]
