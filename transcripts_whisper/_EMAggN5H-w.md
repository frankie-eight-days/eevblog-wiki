---
video_id: _EMAggN5H-w
title: EEVblog #659 - Medical Plugpack Teardown
url: https://www.youtube.com/watch?v=_EMAggN5H-w
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 37, "3": 53, "4": 73, "5": 89, "6": 106, "7": 126, "8": 142, "9": 154, "10": 170, "11": 186, "12": 202, "13": 218, "14": 230, "15": 251, "16": 263, "17": 287, "18": 303, "19": 319, "20": 336, "21": 352, "22": 372, "23": 388, "24": 409, "25": 429, "26": 445, "27": 462, "28": 478, "29": 498, "30": 518, "31": 534, "32": 551, "33": 567, "34": 587, "35": 607, "36": 623, "37": 639, "38": 656, "39": 676, "40": 696, "41": 713, "42": 725, "43": 741, "44": 757, "45": 773, "46": 785, "47": 801, "48": 818, "49": 834, "50": 850, "51": 874, "52": 895, "53": 915, "54": 931, "55": 947, "56": 963, "57": 983, "58": 1008, "59": 1028, "60": 1048, "61": 1065, "62": 1085, "63": 1105, "64": 1121, "65": 1134, "66": 1154, "67": 1170, "68": 1194, "69": 1215, "70": 1231, "71": 1247, "72": 1263, "73": 1283, "74": 1300, "75": 1320, "76": 1332, "77": 1348, "78": 1364, "79": 1389, "80": 1409, "81": 1429, "82": 1449, "83": 1465, "84": 1478, "85": 1494, "86": 1514, "87": 1530, "88": 1543, "89": 1563, "90": 1583, "91": 1595, "92": 1611, "93": 1627, "94": 1639, "95": 1652, "96": 1672, "97": 1692, "98": 1704, "99": 1724, "100": 1745, "101": 1761}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Now, as part of the recent teardown for this St. Jude medical pacemaker monitoring system, it came with one of these medical grade power supplies, and everyone wanted me to tear this down, tear down this plug pack, this wall wart, and see what's inside a proper

**Dave Jones:** made in Germany. There we go, beauty, hi to all my German viewers. Made in Germany, medical grade, which would come under certain type standards. Basically, it's going to have increased clearance and, you know, much better build quality than your one hung low one from China.

**Dave Jones:** So, everyone wanted to take a look at it, so let's go. And these medical devices, as I explained in the previous teardown, everything is medical grade isolation in here, from the clearance on the ground planes to the type approval used on the transformer.

**Dave Jones:** There we go, I actually tore out that medical grade transformer, you know, the high value resistors, all that sort of jazz, and a medical grade optocoupler as well for transferring the data, and of course, to power the whole thing at the top, you need this medical grade plug pack for the isolation

**Dave Jones:** part of it. So, that's going to be the big difference. You'll see, should see a big difference in build and both clearage and creepage distances. Yes, they are different things, clearance and creepage, as I'll explain, no doubt, when we open it up. But yeah, that's

**Dave Jones:** going to be the difference between this made in Germany medical grade plug pack. It's just a 5 volt, you know, 5 watt plug pack. And a one hung low brand, you know, just off the shelf consumer plug pack. So, here we go. And for reference, here's all the

**Dave Jones:** stuff on the back, and it's from a company called Fryro, if I'm pronouncing that correctly. Yes, it is made in Germany, and anyway, Fryro specialize in like a, you know, medical grade plug packs, just like this, power supplies and things like that. So it's probably one of the most reputable ones you can get, and you know,

**Dave Jones:** it's going to be a pretty good example of a good medical grade power supply. In this case, it doesn't have it on here, but this is going to be designed to meet the ISC medical equipment requirements, which is 60601-1, and so it's going to meet those requirements.

**Dave Jones:** I don't know even if you can download that, you usually got to pay for these IEC standards. But anyway, this particular one, I think I found some data on it, and this particular one has an MTBF, a mean time between fire of 200,000 hours.

**Dave Jones:** I'm not sure if that's part of the standard or whether or not it's just a, you know, an internal thing from Fryro. And of course you can see all the type approvals on it, and yeah, these things aren't just, you know, slapped on by the

**Dave Jones:** manufacturer. These would have been, you know, fully tested and fully complied, absolutely no doubt. And I do like these plug packs with the, argh, see if I can get it off. Usually they're not that, argh, a bit easier to get off. But anyway, this isn't

**Dave Jones:** particular to these medical ones. A lot of plug packs these days which are supplied with consumer products have, now have these plug-in replaceable plugs. So instead of giving you, you know, five plug packs with every product, or different leads and things like that, it's much cheaper, or different leads anyway, with different plugs,

**Dave Jones:** they just give you these little adapters that include all five in the package. And you can see the pads on the PCB down in there. There we go. So they just make direct contact down in there. So there's probably just one single PCB inside this entire thing.

**Dave Jones:** So let's crack it open and have a look. Unfortunately this looks like it's ultrasonically welded, so I may have to get the dremel out for this. Usually you can try and crack them open from the outside by banging on them, and stuff like that.

**Dave Jones:** But yeah, this one doesn't seem to budge at all. So, yep, dremel time. First of all, I'm going to start out on the case here. And look at the huge amount of overlap on this case, how it slides all the way on like that.

**Dave Jones:** Wow, that's a lot of overlap. I'm not sure, I don't think that's part of the requirements probably just their particular type. But geez, you know, if that thing explodes inside, it's probably not going to, you know, come apart in a hurry or explode out.

**Dave Jones:** Very nice. And look at the bottom side. The first thing that strikes you is the clear delineation between primary side over here, secondary side. Massive isolation slot down in there. Not only just the isolation slot, but the physical creepage distance there. And these big, long

**Dave Jones:** optocoupler packages like this for extra voltage isolation. The reason why they're that long is because they're probably 4kV rateable. I have to look at the parts on that. So don't quote me, but I believe that the specs for these things is 4kV clearance between primary and secondary.

**Dave Jones:** I could be wrong there. But anyway, it's, you know, it's much higher than usual. And just look at that delineation. Absolutely enormous. So they've got their slot cut out in here, they've got the slot all the way in here, and the traces are all

**Dave Jones:** the way back. They haven't just run them over, auto-routed them willy-nilly over here. And stuff like that. So really absolutely incredible. And if we take a look at the top side there, yes, of course, it's not FR4 board, it's a class board. It's a, you know, a phenolic

**Dave Jones:** base type board. But nothing wrong with that. Very common low cost. Once again, they still have to, you know, shave cost on these things. But look at that transformer. That looks beautifully wrapped. That looks, you know, looks like it's worth every cent. They've got a little heat sink.

**Dave Jones:** That's actually a heat sink down in there. You can see the package mount. It's a surface mount package actually mounted onto that. It's not bolted, it's actually soldered or welded onto there. But they've used that right angle bracket. They've got a thicker one over here

**Dave Jones:** for the secondary side heat sink. We'll take a closer look at that, but yeah, look at that. That's just beautiful. So I mentioned before the terms clearance and creepage. And yes, they are different, and they do get confused a lot. Here's what they mean.

**Dave Jones:** Clearance is the physical air distance between two points. So, you know, if I've got this point here and this point here, then it's the difference in free air between those two items. That is the clearance. But creepage is not the air gap. Creepage is

**Dave Jones:** the physical distance along the surface from that point. So from this surface all the way across, the shortest path on the surface across over to there, for example. Or, yeah, from there over to there. That would be the creepage distance. So in terms of like a board contamination and stuff

**Dave Jones:** like that, there's two different terms there and two different requirements. Clearance and creepy. So just keep that in mind. So that's what you're getting with the slot there. You're getting the clearance is the same. So if you had a pin there and a pin there,

**Dave Jones:** the clearance is exactly the same. So any high voltage across those two points can just arc over like that. Arc over air at a certain voltage. But then your creepage might be different because your board might be contaminated, could have dust on it, could have residue left over from the soldering

**Dave Jones:** process, manufacturing, people's fingerprints, whatever it happens to be, or a bug or, I don't know, you know, dirt and grime and all sorts of stuff driven by fans in equipment, things like that, that builds up on the board. So if you've got a physical slot on there, then

**Dave Jones:** that increases your creepage distance like that so you don't have to worry about surface contamination. Your clearance remains the same, but then your clearance becomes the minimum specification for your board instead of the creepage becoming the minimum specification for the board. And often it's the

**Dave Jones:** clearance you control and is going to be fixed in your design and manufacturing process between two points, but the creepage distance, while it's the same, you can actually get contamination. So that's why your creepage distance can actually dominate your effect. So that's why they put those slots in there.

**Dave Jones:** Now if this was me and I was doing real belt and braces design, like gilding the lily, then I would have actually routed out another slot underneath those optocouplers. But in this case, no, you can see that they haven't. The board, so the

**Dave Jones:** creepage distance is going to be across the board under those packages. So you know, in theory you could get moisture under those packages and then, you know, degrade your isolation there, but you know, they're obviously still doing, you know, still got a massive isolation

**Dave Jones:** there between the pins on either side of those optocouplers there, and I'm sure it more than meets the specification. I'm, you know, there's a difference between meeting the specification and meeting it comfortably and really gilding the lily. Now one thing you may have

**Dave Jones:** noticed here is your typical primary secondary suppression capacitor, which, you know, is normally a, you know, an X-class capacitor to go between your primary and secondary there. They haven't fitted that at all. And of course they've put a slot under that to, you know, eliminate your

**Dave Jones:** creepage distance between there and there. So how they're actually keeping their EMC compliance in check there without the suppression cap between primary and secondary, I don't know. And yeah, it might be interesting to go into the details on something like that. But yeah, anyway, obviously

**Dave Jones:** they deem isolation to be, I guess, more important than EMC in this particular case. Or maybe they've tested it and they just didn't need it. But yeah, it was certainly designed to be in there, but they decided not to fit it. And the optocoupler, no surprise for finding

**Dave Jones:** a Vache part in there. They're the best in the business, of course. TCLT 1005. Let's go to the data sheet. And here it is, the TCLT 100 series. And here we go. Here it is, creepage distance. Look at this, 8mm, greater than 8mm, hence the wide package there.

**Dave Jones:** Specifically look at all the type approvals of course, and applications switch mode power supplies. And look at this, it's got more agency approvals so you can poke a multimeter probe out. Unbelievable. And there's an agency table somewhere in the data sheet as well.

**Dave Jones:** And if we have a look down here, what are we talking about in terms of isolation? Look, isolation coupler, isolation test voltage. Ah, sorry about the selection thing, it's really annoying. The ISO, look, 5000 volts RMS. Beauty. That's what you want. So, you know,

**Dave Jones:** absolutely enormous creepage distance on this thing and in terms of the optocoupler itself, well, 5000 volts RMS. You know, that's just absolutely enormous. And that's why they've chosen this thing because of its isolation characteristics and its type approvals as well. And look, you know,

**Dave Jones:** they really go to town on this optocoupler. As you'll see in the cheap one, then, you know, they just use some crap, you know, one hung low brand optocoupler and it's just, you know, absolutely useless. So yeah, if you want to do it right, you've got to use a proper

**Dave Jones:** branded part like this with all the agency approvals and everything else. Otherwise, you know, when you submit, if you design your plug pack and go and submit it for all those approvals, unless you want to fake it, you know, you're a crap manufacturer and you fake those sort of things, but nobody's going to buy it.

**Dave Jones:** No reputable company's going to buy your product, especially medical stuff. They're not going to take the risk. So when you go and submit it for approval to the agencies, they're going to look at, they'll look at this data sheet. What optocoupler have you used?

**Dave Jones:** Show us the, you know, manufacturing information on your isolation transformer, everything else. So all that stuff, and once they see I use this, you know, tick, tick, tick, it's already got all these agency approvals. Yep. Awesome. And the controller there is a TH20594,

**Dave Jones:** and I wasn't able to get any immediate data on that. That's a switch mode controller for the primary side there, and well, it's, you know, one of these Chinese jobs, I don't know what brand or whatever, and data sheet seems to be a bit hard

**Dave Jones:** to come by. But if I can find it, I'll link it in down below. I'm surprised that they didn't use a name brand one there, actually. Now if we have a look at the input here, it goes around to a series protection resistor here, and straight over to the

**Dave Jones:** diode bridge over there, and then the diode bridge is, whoop, there we go. There's our inline fuse, if you're wondering where the fuse was. No fuse, if you're wondering where the fuse was. No, that's not a capacitor. That's an 800 milliamp fuse, once again, with all the requisite type approvals on it.

**Dave Jones:** So yes, they haven't just bunged in anything there. They've used a top brand, I don't, offhand, I don't know who the manufacturer it is, but yeah, VDU, Underwriters, you know, the whole work. So they haven't just, like, whacked in an M205 on its ass,

**Dave Jones:** you know, from some, you know, one hung low vendor in the, you know, the Shenzhen market. They've, you know, they've really gone to town to choose the fuse properly, and that's probably part of all the type approval as well. And that common mode choke on the input there, look at that, they've really

**Dave Jones:** gone to town there. Bit messy on the winding there, but hey, you know, look at the shroud on it. Beautiful. Now at first glance, these main electrolytic caps here, JH brand CD263, they look like, you know, one hung low Chinese ones, 105 degree C rated.

**Dave Jones:** I've never heard of them before, but I believe they are from actually a German company called Zhenghai, which, yeah, sounds Chinese, but hey, it's Zhenghai Europe, they're a German, maybe made in Germany. And interestingly, the other brand in here is a Rubicon. There we go, no problems with

**Dave Jones:** a Rubicon whatsoever. Once again, that's the YXA series, I think, 105 degree C rated. No problems with Rubicon, but it's interesting that they combine the two manufacturers there. And they're, that's 400 volts, so they're all 400 volt caps. So the JH ones are there and

**Dave Jones:** over here as well, exactly the same. Unfortunately on the second side, they haven't exactly gone with the best. They've gone for Samsung there, which, you know, isn't exactly known for the best quality, but eh, you know, they're okay. So they've cut a little bit of cost there, not sure why.

**Dave Jones:** Oh, and by the way, the other electrolytic cap in here is JH brand as well. You can see a nicely heat-shrunk vertical inductor there. Nice attention to detail, they haven't just left the wires hanging out willy-nilly. Now the heatsink for the diode here is interesting, because it's not

**Dave Jones:** screwed in, it's pot-riveted in. Yes, they do have a heatsink compound behind that, and then it's designed to press fit into the board. So eh, rather unusual, but I'm sure quite effective. Now it looks like we have some sort of PCB-based spark gap there.

**Dave Jones:** I haven't seen that design before, it's rather unusual. But they've removed the solder mask and they've done deliberately sharp points on it, so it's got to be some sort of spark gap. I'll tell you what I'm not that keen on though, is the creepage distance in here, and the clearance.

**Dave Jones:** This is a 400 volt rated cap, as you saw soldered on the other side here. And they've got the trace, and this resistor's very close to it, and well, I don't know, I gotta presume that they've done their homework there, but yeah, jeez, I don't know.

**Dave Jones:** And that spark gap up there by the way, there's the other high voltage cap across there, that's the other 400 volt JH brand one. So once again, not a huge amount of, you know, creepage distance between those two tracers in there. So yeah, but they've probably done their homework, I don't know, offhand, I'd have to give them the

**Dave Jones:** benefit of the doubt and, you know, otherwise you need the schematic to run through and compare everything. Now I've gone and sucked the transformer out of this thing so that we can unwind that and see what it's like. But anyway, I, it brought up

**Dave Jones:** what's happening on this side, on the secondary side of the circuit. I don't really care much for the primary side, but this secondary side here is rather interesting. And I've done a little bit of reverse engineering, not complete, and here it is. Here's a Davecad drawing of it, and it's rather

**Dave Jones:** unusual. Look at the output rectifier diode, it's actually between the two coils on here. There's two coils between, one between the outer pins like that and one between the inner pins like that on this secondary side. And they've actually got the rectifier diode between

**Dave Jones:** the two like that. It's really quite weird. And then they've got another signal diode down here, and this is one of the optocouplers here. This is this first optocoupler, and that's directly across the transformer output. Now, there's some more circuitry around here which I haven't bothered, because I'm lazy, to actually decode

**Dave Jones:** that, and you can do that yourself if you're really keen. But yeah, it's, once again, it's across the transformer output, and it's going to a second optocoupler there, which is then coupled back to the primary side. So we're going to have those two optocouplers and a rather unusual diode in between

**Dave Jones:** the two coils there. Hmm. Oops, I actually forgot the big-ass filter cap there. Of course, you've got to have that, because it's just basically a single wave rectified with the filter cap across there. And, of course, the optocoupler feedback to ensure the 5 volt

**Dave Jones:** regulation on the output, and they've got some extra filter in here with that vertical heat-shrunk output inductor which we saw there. And of course, a good majority of our power dissipation is inside that rectifier diode, and of course that's why it's on a heatsink there.

**Dave Jones:** There we go, it's an MBR 1660. And for those playing along at home, there's the markings on the ferrite core, if you know what they mean. And by the way, the primary side has three windings on it, one between there and there, another between the two inner ones, and another one between

**Dave Jones:** there and there as well. So let's unwrap this sucker and see what's inside. You can see that, interestingly, on the outside, it looks like they've got a winding on the outside of the ferrite. Just a couple of turns there, nothing huge, so you've got to wonder, do you unwrap this sucker first?

**Dave Jones:** You can see that winding around there is not enamel-coated. There you go, that's interesting, it looked enamel-coated under the wrap there, but no, it's certainly not. So, that is very curious. And no, that's not actually a winding, because both strands, of course, go back to the one point down here, and if it was a

**Dave Jones:** winding, it would be enamel-coated wire, of course, so it doesn't, you know, short out at that point. So they've just, from that point there, they've just wrapped a couple of turns around there as yeah, I don't know. Hmm. So I'm not 100% sure of the, why they've actually gone to the effort to

**Dave Jones:** do that. If anyone's got any definitive answers, please let us know. So I'm taking that winding off, and we've got a, what looks like an E-core transformer here. Why is it called an E-core? Well, you can see the split there and there, and there's almost certainly

**Dave Jones:** one going through the centre as well, so it's actually, if you take just that one half, and imagine that, we'll probably see it when we take it apart, is shaped like a letter E, hence the name E-core. And E-cores like this are extremely popular, because they're really easy to wind and they're cheap,

**Dave Jones:** so, you know. But they don't, they do form a closed magnetic system, but they don't offer any inherent shielding. You can start to see inside this, look at this big spongy stuff. I originally thought that that was right under, separating the primary and the secondary, but it's not.

**Dave Jones:** You can see it's sort of like, just like an end stop there. So, like it's just a, you know, a, like a spacer on the end of that there. And you can see, there's the primary winding under there, and you can see that some of the primary winding is also on top

**Dave Jones:** actually wrapped over, if I can take more of that mylar tape off, but you can clearly see it, it's wrapped over the top of that secondary winding. So that's got to be the feedback loop there wrapped over the secondary. So the primary side is tucked

**Dave Jones:** right on the bottom there, secondary is outside that, with this huge insulation on these wires. So there we go, that's how we're getting, you know, it's not just an enamel coating with a mylar wrap, they're you know, really gone to town on the insulation on the secondary

**Dave Jones:** windings there. And then clearly the feedback coil wrapped, you know, it's not a huge number of turns, only a small number of turns, but that's wrapped over the top of the secondary. And that sense winding is not just wrapped on top of that

**Dave Jones:** by the way, it's sort of sandwiched in between, I've peeled off a little bit there, broken that off, but it's sandwiched in between two mylar wraps like that, so they've really gone to town on the insulation there. As you'd expect, because that's the big requirement for these

**Dave Jones:** medical transformers and medical power supplies, is the isolation. That's everything. And I don't really need to go much further than this, because we can see pretty much everything. There's the primary winding in there, and then look at, you know, I'll get my knife here,

**Dave Jones:** look at that layer of insulation there. It's not just, it kind of looks like mylar tape from the top, but it's not. It's some other you know, hugely thick compared to mylar tape wrapping on there, and it's almost it's almost spongy-like. It's, yeah, it's rather unusual

**Dave Jones:** but that's where they're getting all their isolation, right there between primary and secondary, and yep. Yeah, they haven't skimped. Come to think of it, this spongy stuff on the top is probably to, you know, ensure that the secondary winding here doesn't sort of, you know, stray across to the

**Dave Jones:** right over to the side here and get close to like a gap. So it's almost like it's a creepage distance between the primary, the primary down in here, it has to get around the edge under that tape, the creepage all the way, and then through this thick insulation on the secondary winding

**Dave Jones:** right through. So I think that's what it's doing, is increasing the creepage distance there. Ah, beautiful. That rubber stuff is really quite quite thick. I'm very impressed with that, and it looks like they've probably got another Mylar wrap under that as well. Jeez, talk about gilding the lily.

**Dave Jones:** And just as a very quick comparison, let's take a quick look inside another one which is not a medical grade one, but you know, hey, it's UL listed, it's got all the requisite, you know, TUV approvals, all that sort of stuff. Once again, 5 volts,

**Dave Jones:** it's a bit higher current than the other one which is 2.5 amps, but let's take a quick look inside. And there you go, check out that. The first thing that strikes you is the CapZon cap. Oh, man, one hung low all the way.

**Dave Jones:** Bigger heat sink in, of course, because this is a higher current one, but still a 5 volt output supply. And it just looks pretty crusty, doesn't it? And so let me whip the board out and have a look on the underside. And here we go, check it out.

**Dave Jones:** You can see that the, here is the primary side over here. Yeah, they've got nice isolated slots there between the, here we go, between the diode bridge, between the individual wires. So you know, it's all nicely, you know, laid out and spaced. And here is the

**Dave Jones:** primary of the transformer, the secondary of the transformer. Huge gap in there. No problems. Got another isolation slot down in here. Here's our optocoupler across here. And there's our suppression cap across there, because this one does actually have a suppression cap. And there's

**Dave Jones:** the optocoupler tucked away down in there. Looks a bit dodgy, but I mean, I've seen worse than that. So that's a relatively, I guess you could call that a reasonable example of a cheap one. That optocoupler down in there doesn't instill a lot of confidence.

**Dave Jones:** L0452. Well, yeah, I couldn't even get data on that sucker at a quick check. But yeah, notice the Y class suppression cap between that primary and secondary there. There we go. There it is across there. And there's our optocoupler there. You know, it's okay.

**Dave Jones:** I mean, it's, you know, it's alright for just a regular consumer-grade supply. But this one simply wouldn't cut it as medical-grade isolation. Not a chance. And this transformer, well, it's not instilling a lot of confidence in me. That's for sure. So yeah, let's see if it won't

**Dave Jones:** fully tear it apart. But let's have a look. This is the secondary side over here. You can tell by the thicker wires, of course, the higher current. And the primary side over here, it looks like it's got a couple of windings. And we've got a similar thing

**Dave Jones:** happening here. We've got the outer sense wire wedged between two, well this isn't mylar, it's some other sort of tape, and just wedged between that on the outside of the secondary. So you'd have your sense winding here, then your secondary, then your primary in the core.

**Dave Jones:** And we've got the secondary winding coming here, and then there's another wrap of the secondary winding going in there. But what it's all about is the insulation in there between the primary, which you can see, which is the red colour enamel-coated wire, and the secondary

**Dave Jones:** which is in there. So they're probably just going to have more wraps of this yellow tape. And yeah, you can see it there. There we go. I won't bother taking it apart any further. You can see there's just a wrap or two of that yellow tape, plus the enamel

**Dave Jones:** on the two windings, of course. And as you see, there's nothing stopping it sort of like, you know, creeping over the, you know, right to the edge here. And, you know, how you wind that tape, it might be a bit thinner on the edge,

**Dave Jones:** or it might not be there at all. Depends on how you control your wrapping during production and stuff like that. So there's no creepage distance like we saw on the, you know, or with this sponge tape here, no creepage distance, large creepage distance like that around

**Dave Jones:** the edge of the tape and back over between primary and secondary. So yeah, no contest there in terms of primary-secondary isolation. And of course, the medical one had this really thick rubber insulation there between the primary and the secondary, let alone the sponge creepage

**Dave Jones:** thing. So none of that you find on this consumer one. Chalk and cheese, really. Yep. If I'm going to trust my life to something, it's going to be this one. And of course, you do with these medical things. That's the whole point. So it's not

**Dave Jones:** that these are, you know, inherently more reliable, although that might be part of the spec. It's all about the isolation between primary and secondary. And you can see it in spades inside the construction of the transformer, which is where it's all at, and the very nice, you know, quality brand

**Dave Jones:** rated and meet-the-standard Vishay optocouplers in the isolation slots. And that's what it's all about, and that's why this has been given medical type approval, and is, you know, approved for use with medical appliances. And, you know, a cheap thing like this just isn't going to cut the mustard.

**Dave Jones:** So if you enjoyed that, please give the video a big thumbs up, that'd be really appreciated. And please comment and subscribe and, you know, all that jazz that us video bloggers say at the end of any video. And as always, data sheets will be linked down below if you want to check out the data sheets

**Dave Jones:** for parts used in this thing, and also a link to the EEVblog forum discussion as well. But you're welcome to leave comments on the blog or on YouTube. I do read them all, or I attempt to anyway, and reply where possible. Catch you next time.
