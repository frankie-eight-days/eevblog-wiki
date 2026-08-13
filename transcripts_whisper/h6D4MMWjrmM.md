---
video_id: h6D4MMWjrmM
title: EEVblog #682 - Ness D16X Alarm Panel Repair
url: https://www.youtube.com/watch?v=h6D4MMWjrmM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 41, "3": 61, "4": 81, "5": 105, "6": 121, "7": 137, "8": 157, "9": 173, "10": 193, "11": 205, "12": 225, "13": 237, "14": 261, "15": 281, "16": 297, "17": 317, "18": 333, "19": 349, "20": 365, "21": 381, "22": 398, "23": 418, "24": 434, "25": 454, "26": 470, "27": 491, "28": 511, "29": 527, "30": 543, "31": 555, "32": 575, "33": 596, "34": 616, "35": 632, "36": 648, "37": 668, "38": 685, "39": 697, "40": 717, "41": 737, "42": 753, "43": 774, "44": 790, "45": 806, "46": 826, "47": 843, "48": 860, "49": 876, "50": 888, "51": 908, "52": 928, "53": 940, "54": 952, "55": 973, "56": 989, "57": 1009, "58": 1025, "59": 1041, "60": 1058, "61": 1074, "62": 1094, "63": 1110, "64": 1127, "65": 1139, "66": 1163, "67": 1183, "68": 1200, "69": 1220, "70": 1232, "71": 1252, "72": 1268, "73": 1285, "74": 1301, "75": 1317, "76": 1329, "77": 1346, "78": 1362, "79": 1386, "80": 1406, "81": 1423, "82": 1439, "83": 1463, "84": 1479, "85": 1491, "86": 1511, "87": 1528, "88": 1544, "89": 1560, "90": 1580, "91": 1592, "92": 1609, "93": 1625, "94": 1637, "95": 1657, "96": 1673, "97": 1689, "98": 1706, "99": 1722, "100": 1746, "101": 1758, "102": 1774, "103": 1794, "104": 1811, "105": 1831, "106": 1847, "107": 1863, "108": 1880, "109": 1904, "110": 1924, "111": 1936, "112": 1948, "113": 1965, "114": 1981, "115": 1997, "116": 2017, "117": 2029, "118": 2042, "119": 2062, "120": 2070}
---

**Dave Jones:** Hi, this is an Australian-designed NESS D16X security alarm control panel board. And NESS are an Australian company of, and they make some of the world's best alarm panels. They're probably one of the biggest, if not the biggest, alarm panel manufacturer in Australia. Bosch would probably be the only other one of comparable

**Dave Jones:** size, I think. Anyway, these are designed and manufactured. I.e. pick and place everything just down the road here in Seven Hills here in Sydney. So maybe I should actually get a factory tour one day of the NESS facility there. How they design and manufacture these things.

**Dave Jones:** Anyway, it's quite a good panel, still a current model, and this one has actually failed. So I thought I'd take a look at it and have a see what the problem is. Well, if you're watching this, you can probably, even, hey, even if you're not watching in HD, you might be

**Dave Jones:** able to spot the problem already. Hmm. Yeah, take a look down there. Look at that. There's your problem. And yep, look at that. It's had the arse blown out of it. The magic smoke has escaped. And this is the plug pack AC input here.

**Dave Jones:** There's a 17 volt AC plug back here, which is Mayans earth. I'll describe that in a minute. But it looks like that puppy in there has, yeah, kind of, sort of, failed. You can tell that's the ignition point. Look at all of, look at the white charring around the outside

**Dave Jones:** of that, and it's, you know, flamed up. Basically, it's completely failed. And the reason all of the soot, and I haven't tried to clean this off yet, all of the soot and everything else, like, you might think that this bridge rectifier here has failed,

**Dave Jones:** but it may not have. It's certainly this part here, and it's flamed up and it's gone all the way up here. The reason for that is because it was sitting in a, in the control panel box vertically like this. So the flames would have

**Dave Jones:** risen up there and have just completely chipped and have just completely charred everything. Look at that. Wah! Now just a quick note on these alarm panels. Normally, like when you power something from a plug pack, it is completely isolated. But this uses a special plug pack that has three wires coming out,

**Dave Jones:** and one of them is Mayans earth. So it bypasses, it goes, you know, it doesn't go through the transformer of course, it goes directly from the earth pin on the socket, and that earth wire comes out and plugs in here. And if you have a look, the earth wire

**Dave Jones:** there is connected to this ground side, the sensor ground side, all the way over here. So that's everything in this alarm panel system. On the input side is Mayans earth referenced right there. But you can see that the, then the isolated plug pack comes in here, goes around to

**Dave Jones:** these two pins here, which is this MOV, these two MOVs here going down to Mayans earth. So each one of those AC inputs has a MOV down to Mayans earth. We'll take a look at the part number on that. And, well, the rest of the circuitry, I can't see what's going on there.

**Dave Jones:** But obviously this is just, you know, simple full wave bridge rectifier going into your Mayans cap here. This cap could be gone as well, depending on, you know, if this all charred around here, you know. I don't know, there's a bit of charring on that cap

**Dave Jones:** there, but it's likely still survived. But I don't know, would you trust it long term? Eh, I'm not sure. Because once you get heat generated over there, obviously these caps are only rated. Actually, what one is that? That's a... what brand is that?

**Dave Jones:** It's a MaxCap. I can't say I've ever heard of a MaxCap. Anyway, it's 30 volt, 2700 mic. And has that got a temperature rating on it? I don't think so. Anyway, when these electrolytic capacitors heat up, of course, as I've mentioned many times before, the electrolyte

**Dave Jones:** inside, which is a liquid, it can actually dry out and the caps eventually fail. So yeah, having flames near these good, near electrolytic caps, of course, any hot component, including this heatsink. Not the best design, really, when you've got, you know, this there's a TO-220 device tucked away in there, you can see.

**Dave Jones:** So not the best having that right next to that heatsink, but when it's mounted in a panel, as I said, vertically like that, all of the heat is going to rise up. So it's, you know, if you mount it in upside down and all the heat rose up across that cap, that would be

**Dave Jones:** really bad design. So this thing has an interesting clip-on heatsink here, so I'm going to go ahead and see if I can get that clip off. And I need a bigger flathead screwdriver, but that clip should just pull off and then that heatsink should just pull straight out, because they

**Dave Jones:** kind of slot in the board like that, so it's rather interesting. It's just a clip-on device, really, whether or not there's any, even any heatsink compound. I can't see a seal pad or anything down in there, so let me get that off. There we go, that just popped off, so

**Dave Jones:** this heatsink should just, yeah, lift out like that and yep, look, they haven't even got any heatsink compound behind that. Not that great, I would have at least smeared something on there, you know, but I don't know, it's got to do the job.

**Dave Jones:** How much this is dissipating, I don't know. There you go, that's a 7805, so obviously the main regulator for all the control stuff on this board. I might give you a brief overview of the board actually, just to see what's on here. Now this is actually what's called

**Dave Jones:** a 16-zone alarm panel, which means it has 16 inputs. The main board is actually only an 8-zone one, here we go, from Z1 through to Z8 up here. So it's got 8 input zones plus an expansion board here which turns it into the D16X

**Dave Jones:** model, which allows it to have an extra 8 zone inputs here. And it's got a keypad input of course, which can, which is a multi-drop configuration, probably like RS485 or something like that, and that multi-drops through to multiple keypads you can just whack in parallel.

**Dave Jones:** And of course, just like any alarm panel system, they're all pretty identical. We've got a siren output, we've got the strobe, we've got a reset switch, and a tamper input, a dedicated tamper input as well. This goes to the case, usually there's a micro-switch on the case that this

**Dave Jones:** thing is in, and if so, somebody tries to open the case and disable the alarm that way, then, well, the alarm instantly goes off. And it's got a dedicated phone line interface for the dialer, so when the alarm goes off it can dial like a

**Dave Jones:** back-to-base type security monitoring thing. And so we've got a relay here which can switch that off and on, and you'll notice completely isolated here, that would be meeting telecom requirements, the telecommunications standard. We've got a nice big spark gap down here for protection, and yeah, there's not a huge

**Dave Jones:** amount in there. We've got a couple of optocouplers here for sending the data to from the phone line there. And this 16-channel expander board here, we can get a good look at the input circuitry here. You'll notice that these MOVs have been left out, Y1

**Dave Jones:** through to Y8 up there, so they've left those suckers out. But aha, what do we have in here? You might recognize this from a recent video I've done. What is that? It's a PCB spark gap. Click here if you haven't seen my video on PCB spark gaps, actually how to

**Dave Jones:** design these and how they work. So check out how NESA have done it. This is obviously their preferred method. They've got tiny little points there and on the point of the track. So it's not just the square of the track, they've actually on their layout they've added just little spikes, little

**Dave Jones:** spurs on the end of the snaking track like that. So it snakes around like that, and that gives it multiple points. You know, one, two, three, four, five, six different chances to actually spark over before it gets in. And if you've seen my previous

**Dave Jones:** video, which you should do, you'll notice that these can actually wear out if you've got more than one input spark. So this would be protecting just for, you know, gross overloads and ESD discharge as well. But they've decided, well, we're going to save a couple of cents

**Dave Jones:** and we're not going to install the MOVs there. I don't know why, they went to the effort to design both in. Why wouldn't you populate them? Seems a bit silly. And there's nothing really much else happening here. We've got an input MUX chip,

**Dave Jones:** they're the three lines coming in here. Obviously they're, you know, with three inputs like that you can choose eight different inputs. And the input decoupling and for, and the resistors for the comparator circuits that go into, so this is just an analog multiplexer, it would be.

**Dave Jones:** And then the main alarm comparator would be down on the main board. Because the way these alarm inputs work is they're basically a window comparator. So we've got some resistors in here, you'll notice 2K22 there. And why are these resistors attached? Because these are the termination resistors for the inputs.

**Dave Jones:** And if you, so what that does is allows the alarm input, if you actually short the wires together, then you short out the 2K2. If, you know, somebody breaks in your house and tries to disable a sensor getting under it and shorting out the wires, then it's going to set off the alarm.

**Dave Jones:** So it has to have a 2K2 on the line, and likewise if you break the line, if you just snip it, the alarm goes off as well. So it goes off either way. So the line has to be terminated in that 2.2K resistor value to match the final window detector

**Dave Jones:** circuit down here. So just what failed in here? Well, I've got no idea, it's a tiny little like 0805 package, that looks like a resistor there, that's maybe a cap on that side. Don't know, oh, there we go, hello. Whatever it was, it's just a charred mess.

**Dave Jones:** Was it a surface mount fuse perhaps? I don't like the chances of there being any traces left there, that's for sure. I mean, this diode bridge, as I said, you can see the AC symbol on that. That one's probably still good, because I can't see any blowholes

**Dave Jones:** in it or anything like that. So why this input device? Obviously on the input side of the diode bridge here, my best guess, as I said, a surface mount fuse there. Why it blew, I don't know. I'll tidy it, and what I'm going to do is

**Dave Jones:** get in there with some PCB cleaner, try and clean it up and see if we can see anything, maybe trace it out. And because we've got an Australian made board, well, we have to use some Australian made cleaning products from TempChemTools also in Sydney here out at St Mary's.

**Dave Jones:** Fantastic! And they got these from the TempChemTools website. And they got these from the trade show. So the electronics trade show here in Sydney, they came up and gave me some free stuff. Thank you very much. ChemTools. We've got regular isopropanol alcohol of course,

**Dave Jones:** regular circuit board cleaner, and then 3 grades of flux remover. General purpose for WUSAs, heavy duty for better applications, and then ultra. Now flux remove is not exactly what we want here, although it would kind of do the job though. It's, yeah, it's more for obviously your flux residues,

**Dave Jones:** waxes and oils and things like that, hydrocarbon deposits. And likewise for the circuit board cleaner, probably the first round you would do cleaning something like this, just your stock standard isopropanol alcohol. Why? Well, you can get it everywhere, and every lab should have some.

**Dave Jones:** And it's just, it's probably, you know, the least damaging of all the ones, so it's always one you should try first. And any good lab, you should also have one of these conductive brushes as well. Yes, they are actually conductive bristles and, well, there it is, it says conductive brush.

**Dave Jones:** But more to the point, they're actually quite stiff like that, so you can really get in there and scrape it off. Because this needs a fair bit of elbow grease as well as the isopropanol or other cleaning compound, so you really need to get in there and physically...

**Dave Jones:** So let's get in there and give it a good little spray like that, and rub-a-dub-dub. And as you can see, yeah, that's doing a, not a bad job at all. It went all the way up the board up there, but really we want to get

**Dave Jones:** right around those components in there. You can see, oh, don't want to bend that moth too much. Got to be careful, but hey, we're getting some exposed copper down in there, that's for sure. That is one charred mess, look at that. But it's

**Dave Jones:** obvious what's going on here. Now, as I said, the two AC inputs come up through this lead here and this lead here of these MOVs, which then go down to main ZIR, so they're intact. So it hasn't taken any energy hit in regard, or at least

**Dave Jones:** not enough to blow these things, like at least not enough energy from relative to main ZIR on the input there. So you can see that trace, you can still see the copper, it's burnt all the solar resist off. It goes into here and goes

**Dave Jones:** around into, straight in to the one side of the bridge rectifier there, and the other one, likewise, goes around here. And it might be a bit hard to see, it looks better under my mantis. Yeah, no, there it is. There we go. Scrape a bit more

**Dave Jones:** of that crap off, and the trace goes straight around. So both of the AC inputs on the terminal here, so both of these two terminal inputs here, do go straight to the bridge rectifier here. So what was in the middle there that blew up?

**Dave Jones:** Oh, by the way, these are just caps going here, down to ground. So no big deal there, we've just got some smaller suppression caps there. So what have we got that was in the middle here? Well, the only thing is, there's no vias on the other side, it must have been

**Dave Jones:** between, across these two inputs here. So it must have been another surface mount MOV or similar device between, you know, TVS or something, between the two inputs like this. So we've got a voltage overload on these two inputs which blew the absolute arse

**Dave Jones:** out of this thing. So I was wrong in my guess that it's a fuse that would have been in series with the bridge rectifier. It's not, this copper is still in, see it? There we go, didn't scrape enough off with that brush, even the brush

**Dave Jones:** wasn't good enough, to go all the way over. So there was nothing in series with that bridge rectifier, so it's got to be across there. But do you know what the upside of this is? Well, it's clearly done its job. It has exploded, it's...

**Dave Jones:** well, we haven't checked the diode bridge yet, but it's pretty much intact. And then of course on the output side of the diode bridge, the 7805 looks intact too. There's no blowholes in the front side of that at all. So in fact, the board does actually power up just fine

**Dave Jones:** from the battery input down here. I've already tried that and it talks to the keypads and lights up and does everything. So, oh by the way, look, we've got some little, they're being used as series protection devices for the battery. Hmm, it's pretty much

**Dave Jones:** bodged on there though, don't really like it at all. But yeah, crude but effective. And if you're curious to know what processor is used in this thing, well check it out, it's a bit obscure. It's a Fairchild MB39F 538. Absolutely ancient, but these NES security products have been around

**Dave Jones:** for many decades, so wouldn't surprise me if it's still running original assembly code from like the early 90s or the late 80s or something like that. And the only other chip of note is hidden under the expander board there, it's a Haltech HT9170, and that's a DTMF

**Dave Jones:** receiver. They need that for the modem of course. So what they're doing with these bulbs here is they've actually got two of those in series with the battery terminal here. Just for a bit of protection, jeez. And you can see down in here

**Dave Jones:** our dual diodes. This one here of course comes from our 7805 output there. These are our current steering diodes, so we can either power from the 7805 when you've got your mains input, or you can power from the battery here through your two series bulbs and through

**Dave Jones:** this diode. So this is your common point on this side. And they've got the requisite protection on the secondary side of that too as well. We've got a couple of poly switches, large and small types down in there. They're resettable fuses is essentially what they are.

**Dave Jones:** And it's important to have a resettable fuse on the board of course, because all of the 12 volt outputs over here, for example, that power all of your sensors and everything else, these have to be protected by resettable fuses. Because when you're installing these things or what, you know, screwing them in or whatever, wires can

**Dave Jones:** short out, you accidentally hook them around the wrong way or whatever, and well, you don't want to blow the onboard fuse and blow your board. So a resettable poly switch will actually protect you there, and it'll just shut down. And then when you remove the power, it'll come back up, no problems at all.

**Dave Jones:** And we can see what kind of moths we've got here down to mains earth on the input. That's an EPCOS symbol there, 05K35. So let's look that one up. And yep, confirmed it is a moth. And they've of course got many different types,

**Dave Jones:** but here we go, they didn't have the S on the packaging there. So sometimes it's a bit tricky to Google search these things. You've got to sort of, you know, know what you're doing and make a few guesses and things like that. But I found this, so it's clearly an

**Dave Jones:** S05K35. So it's a 30, as the 35, no doubt it tells you it's a 35 volt RMS rated there, 45 volts DC, and they're just the energy you know, absorption figures for them. But yeah, so anything over 35 volts RMS from either of those two inputs to mains earth will actually

**Dave Jones:** be clamped by this moth. But as I said, that is not the fault mechanism here, the fault mechanism was not relative to mains earth, it was across the isolated output of that 17 volt AC plug pack. It got too high and blew the arse out of whatever device, MOV or TVS or some other device

**Dave Jones:** that was in there actually protecting across the rail itself. So in case you didn't quite get what I was trying to explain there, here's a little diagram for it. We've got our 17 volt AC plug pack in here, oh I forgot it's got the mains earth connection coming out of the plug pack as well.

**Dave Jones:** And then this is the one that blew, okay? This is so it's across the AC input here. So if the voltage across here gets greater than that 35 volts RMS that we saw there, then these ones would blow, okay? If either of these terminals are relative

**Dave Jones:** to this mains earth blue, but these things haven't blown. And of course they're not always designed to blow. If the energy is low enough and fast enough it can absorb it internally and you wouldn't see any external sign of damage and it'd work just fine again.

**Dave Jones:** So but this one just blew the crap out of it, so we must have got much higher rating across here. I don't know, it was some sort of SMD device, pads aren't even left, there's just nothing there at all. So I have no idea what it was, and that just protects, so that's

**Dave Jones:** a differential voltage across there. So you can have you know, a huge differential voltage across here, you can put 240 volts on there or 1000 volts or whatever, and these MOVs won't blow because it's not relative to the mains earth over there. So just

**Dave Jones:** the reason that they have two different types of protection there is for two different fault mechanisms. And I don't think we've actually broken our traces there, so let me measure between there and the input to that diode bridge. No, that trace is still intact.

**Dave Jones:** Because as I said, it just vaporized the trace between the two, there we go. So our input is still, our AC input is still connected directly through to our diode bridge, our MOVs are still relatively intact. Well let's measure those, make sure they're not shorted.

**Dave Jones:** No, there we go, 5.9 meg, that's what you'd expect. Inspect the things to be a very high impedance, is that one okay? Yep, that's a very high impedance as well. You may measure a difference if you put it around the other way perhaps.

**Dave Jones:** Yeah, there we go. A little bit different, but yeah, that's what you expect, very high value. So those MOVs going down relative to mains earth have not shorted, not blown at all. So that's still, that input apart from our vaporized component, is just fine.

**Dave Jones:** Okay, so let's check our diode bridge to see if it's still intact. And what we want to do, let's measure each one of these diodes. So we'll put the negative lead here, you'll see the cathode of these two diodes on the positive output.

**Dave Jones:** So here's our positive output here. So, oh, I'll try and keep this in shot. Positive output terminal there, and measure between both of those inputs, and we should get a diode drop. Half a volt. Ta-da! There we go! These two diodes here, still intact.

**Dave Jones:** And likewise, we can do the same thing if we put our positive lead on our negative terminal down here, and then measure between both of these inputs. Ha ha! And bingo! Nothing wrong with that diode bridge, it has survived just fine. But we do have one

**Dave Jones:** more test left before we attempt to power this thing up, because as I said, that input side diode bridge is just fine. Well, what happens on the output of this thing? So let's measure across the positive and negative output, and there we go, it's

**Dave Jones:** yeah, it's open, so it's not shorted. We're basically looking for shorted. Okay, so let's now power this thing up and see what happens. The good thing about having a diode bridge is you don't have to worry about the polarity, which way around you actually get the thing, so that's just fine.

**Dave Jones:** Anyway, 17 volts AC, I don't know, I've just got it set to 20 volts. Current limit, 0.25 amps, 5 watts or thereabouts. You know, the board shouldn't be drawing 5 watts, so that's sort of an acceptable margin. So let's power it up, and there is a

**Dave Jones:** status LED on this board which should flash if it's working. So here we go. Point set, yeah, it's drawing 0.8. Sounds right, relay clicked in for the DTMF, and flashing LED. Bingo. Works a treat. And in case you're wondering about the heatsink, you don't need it just for a little power-on test like this, and I wouldn't

**Dave Jones:** expect it to actually get that hot, so I'm touching that, it's been on for like a minute now, and it's not getting that warm at all. You know, it's only heating up by maybe 5 degrees or something like that. Not much at all, so that heatsink was

**Dave Jones:** certainly adequate in there, but you know, it's in a case with very little ventilation and stuff like that, but yeah, you know, it's adequate. So that thing actually works, and what I haven't tested at the moment is the plug pack that comes with this, it's actually a fused plug pack.

**Dave Jones:** So it was working originally, and then the board failed, so I think the fuse inside that plug pack is blown. So yeah, so we've blown an input protection device, and we've blown, it looks like we've blown a fuse in the plug pack, but apart from that, it works just fine.

**Dave Jones:** But as I said, as a matter of course, I'd be changing that main filter cap up there, I wouldn't trust that thing. But it probably only smoked very briefly, you know, maybe it's a bit paranoid to change that cap, but I you know, just would as a matter of course if you're doing a repair on this thing.

**Dave Jones:** And would you have to replace the MOV across the input there that blew? Well, you know, not necessarily, if you just, you know, it really, it's very rare that these things are going to get overloaded like that. So you know, really, I mean, you've still got the regulator here

**Dave Jones:** to protect your circuitry, so you know, you don't have to, but as a good repair as a matter of course you would. And of course if you're fixing this you wouldn't just leave that charred remains, you'd get in there and try to sort of dig it out, and then you don't just want to leave the bare copper on there.

**Dave Jones:** So what you can do with the bare copper is you can get some of this stuff, and this is UV curable solder mask. Solder mast? Got some chinglish happening there, but you can buy these really cheap on eBay, and they're exactly as the name says, it's green solder mask

**Dave Jones:** that comes in a liquid form, in a syringe like this, and you just squeeze it on sort of, you know, flatten it out and dab it down, and then you apply UV light to it from like a UV torch or a UV lamp or even, you know, you can put it out

**Dave Jones:** in the sun if you want, that'll work as well, it'll just take longer than a concentrated source. And then you have to put on really thin, you can't just sort of like clump it on in big clumps, because it actually won't cure on the inside, so it really has to be an extremely thin

**Dave Jones:** coating on top of there. And then it will cure hard, so it's very similar to regular solder mask like this. And yes, you can actually apply this stuff to your own home-etched boards like this one for example, and I might do a separate video on that, and in that

**Dave Jones:** case you just get the film, like you just drop it on there and you get the film and you put it over, and then you expose the, so that, the film, you push it down and you spread it all out with a credit card or something like that, and then

**Dave Jones:** you're left with a very thin coating, and then the UV that's left behind that hasn't been exposed by the individual pads on there, the pad shapes, you can actually define those printed on the overhead transparency, is still all liquid form, and you can use a solvent to just wash that away, and bingo, you'll be left with

**Dave Jones:** a proper solder mask coated board. And if you had a large section of flat board without any parts, that how, that's how you do it, you put a dab of the solder mask on there and with, well, not with a post-it note, but with a film, you would squish it down

**Dave Jones:** like that, and do that, and then rub it, and then you'd be left with a very thin coating of the film, but because we have to get inside an area like that, you might have to use something dodgy like a cotton bud. And then, well, I don't have my

**Dave Jones:** good UV light box here, it's at home, I'll just cure that with a little UV torch there. It's pretty pissant, it probably might be faster if I just take it out in the Australian sun here. And well, no, it turns out it isn't quite that easy, there's an

**Dave Jones:** intermittent issue here, I just tried to power it up again, and I was getting short circuit current on the power supply, so it was current limiting out. So if we have a look at the AC input here, again, look at that, 18 ohms.

**Dave Jones:** What the? Yeah, something is, something is fried, and it's not between mains earth either. Oh, 10k, yeah, no, oh sorry, got 10k between there and mains earth. Well it turns out there's nothing wrong with that diode bridge, and I removed it, and we're now getting

**Dave Jones:** 25 ohms, look at that. Something else is going on there, and I didn't see this before, but there's a trace going off from the diode bridge under that big cap. I'm going to desolder that and follow it. Well, as it turns out, there's

**Dave Jones:** nothing really doing there, that trace is just going off, and it's going through a series resistor down in there, I won't go into huge detail, but that's a 1 mega resistor down there, and I've measured that, and it's fine. So it's just detecting the mains AC input there,

**Dave Jones:** and using it for some purpose. And so the low impedance path is under here, and obviously there's carbonisation in there at the traces, and it's just going across there, and it's just, yeah. And it really needs to be dug out, and really get in there with a knife, and

**Dave Jones:** really dig this thing out. So I've desoldered the diode bridge, and the diode bridge is still fine I think, but you might replace it as a matter of course as well. And of course, you know, you might replace the ceramic caps and maybe the MOS,

**Dave Jones:** but I still think the MOS are still good on this thing. But, well, I've dug down in there a fair bit, and look, it is just, nah, it's gone. It is just completely charred all the way through. We just got lucky before, I thought it was just maybe a, you know, a bit of surface contamination, but no,

**Dave Jones:** that board is well and truly, ah, dig right down nut, that's just right through, right through that fibreglass. It's just gone. That needs to be like a drill, like a slot drilled out in there or something to isolate those two sides. Ugh, ugly.

**Dave Jones:** So, yeah, yeah, nah, it's not as easy. So I thought, it's still doable, I mean, if you wanted to get this up and running again, you certainly could, but I would get in there with a routing bit, a drill, and just drill a

**Dave Jones:** slot right down there so it isolates one side from the other, and ugh, yeah, it's just, ugh, it's horrid. That is awful. Yeah, those, and those traces are gone. And, yeah, we did get it up and running for a minute, it was fine,

**Dave Jones:** but, ah, look at that. Look at that, nah, nah, it is, it is toast, oh my goodness. And let's get in there and try and measure that charriness. And, oh, look at, ah, 150 ohms, yeah, you saw it, look, 200, no, 2 meg there, but, ah, it can go as low as, like, you know,

**Dave Jones:** tens of ohms as we saw before, hundreds of ohms, really nasty stuff. Look at that, 400 ohms, yeah, ah, blech. And what can happen to, when you get an overload on the input like that, and when it can blow the arse out of a protection device, but that's exactly what they're designed

**Dave Jones:** to do, they're designed to take the brunt of it so that it protects the rest of it, it protects, you know, you don't care if your diode bridge blows, or maybe your 7805, but by the time the energy gets to 7805 it can get through into your

**Dave Jones:** rest of your circuitry, it does provide some, ah, protection, of course, and you can just blow your regulator and not the rest of it, but, yeah. Um, certainly, if you want it to blow, you want it to blow right at the input there, but it can just get real messy

**Dave Jones:** like this one, and just cleaning it up is just, blech, ugly. So, yeah, I don't think I'm going to be, ah, finishing this one off today, but it's still fixable. As I said, route a big slot out there and really clean it, but you'd, you know, almost have to chop out, you know,

**Dave Jones:** a big chunk of the board down in there, because you don't want any of that, ah, carbonised fibreglass to short out between the inputs. That's a real nasty fail, that one, when it burns right through the fibreglass. Because, you know, FR4, that's, ah, what

**Dave Jones:** one of its ratings is, is flammability rating, fire rating. Um, you know, usually they, you know, they might, ah, char on the surface just for a mild, you know, poof. Just, ah, like, ah, just blowing the arse out of something, and, ah, you might get a little bit of charring on the, ah, top surface,

**Dave Jones:** but this one went really, really deep, so, yeah, nah, that's, that's ugly. It's still doable, but yeah, anyway, ah, yeah. I won't finish in today's video, sorry about that, but anyway, that was the problem with this thing. And, ah, as you can see,

**Dave Jones:** it can get real nasty, so just be careful there. Like, I thought I had that up and working again. Um, I probably wouldn't have trusted it, still would have, ah, done some more, you know, soak testing and, ah, other stuff on it, maybe

**Dave Jones:** replaced a few of the parts and things like that, but, yeah, that was, um, yeah, that came back to bite me. I powered it up again and sure enough, that short circuit current, so it went from, like, open, working just fine, as you saw, which is just like a dead short.

**Dave Jones:** So, there you go. Um, just something to watch out for. Charring on PCBs, real nasty. So anyway, I hope you enjoyed that, ah, you know, almost repaired video. It's, at least we found the problem. Um, yeah, it's just a matter of, ah, a lot of manual labour to, and a bit of, ah, tender loving care

**Dave Jones:** to fix this thing. So anyway, if you want to discuss it, jump on over to the EEVblog forum or you, leave a YouTube comment, as always. And if you like the video, please give it a big thumbs up on YouTube, that helps a lot.

**Dave Jones:** And as always, I'll link in data sheets and stuff down below as well. I hope you enjoyed it. Catch you next time.
