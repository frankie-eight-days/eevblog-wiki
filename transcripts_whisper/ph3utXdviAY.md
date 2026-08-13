---
video_id: ph3utXdviAY
title: EEVblog #603 - Gas Sensor Teardown - Dräger Multiwarn II
url: https://www.youtube.com/watch?v=ph3utXdviAY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 37, "3": 55, "4": 81, "5": 101, "6": 124, "7": 138, "8": 152, "9": 172, "10": 190, "11": 212, "12": 235, "13": 255, "14": 282, "15": 304, "16": 317, "17": 335, "18": 352, "19": 372, "20": 385, "21": 404, "22": 423, "23": 443, "24": 459, "25": 475, "26": 496, "27": 514, "28": 530, "29": 546, "30": 562, "31": 577, "32": 591, "33": 608, "34": 622, "35": 637, "36": 659, "37": 675, "38": 695, "39": 718, "40": 741, "41": 757, "42": 776, "43": 792, "44": 812, "45": 828, "46": 844, "47": 859, "48": 880, "49": 895, "50": 917, "51": 934, "52": 954, "53": 970, "54": 991, "55": 1010, "56": 1030, "57": 1050, "58": 1063, "59": 1081, "60": 1099, "61": 1116, "62": 1136, "63": 1149, "64": 1168, "65": 1191, "66": 1210, "67": 1228, "68": 1244, "69": 1260, "70": 1274, "71": 1290, "72": 1307, "73": 1328, "74": 1345, "75": 1362, "76": 1380, "77": 1398, "78": 1416, "79": 1431, "80": 1450, "81": 1465, "82": 1484, "83": 1501, "84": 1517, "85": 1533, "86": 1552, "87": 1571, "88": 1595, "89": 1622, "90": 1641, "91": 1659, "92": 1682, "93": 1702, "94": 1727, "95": 1745, "96": 1764, "97": 1785, "98": 1805, "99": 1824, "100": 1845, "101": 1865, "102": 1880, "103": 1902, "104": 1923, "105": 1944, "106": 1960, "107": 1977, "108": 1996, "109": 2016, "110": 2033, "111": 2050, "112": 2068, "113": 2091, "114": 2110, "115": 2131, "116": 2155, "117": 2173, "118": 2190, "119": 2210, "120": 2228, "121": 2251, "122": 2271, "123": 2290, "124": 2310, "125": 2329, "126": 2345, "127": 2361, "128": 2377}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. This is an old mailbag item that we got. It's a drag-up multi-warn, and it was sent in by Andreas, and he's from Germany. So thank you very much, Andreas. Sorry it took so long to get around to it.

**Dave Jones:** What it is, is a warning system that's designed to detect different types of gases. You might be able to see different sensors in there. And this particular unit can actually accept different plug-in modules for this, up to, I think there's 35 different sensors for 35 different types of gas,

**Dave Jones:** or something like that, with dozens of different plug-ins that you can plug into here. And it's a gas detection system. There's an alarm on the top, and it flashes a light and sounds a big siren, loud siren, you know, screaming. If it detects, you know, a combustible gas or something like that, or a lack of oxygen,

**Dave Jones:** even, for example, and they're used by emergency services, for example. Fire brigades might have these, they're used in the mining industry, any sort of underground, sort of, you know, confined spaces type thing, to warn you, you just carry it around with you. It's battery-powered, carry it around with you, and it detects all these nasty gases

**Dave Jones:** which could kill you, or could explode, or something like that. So, you really have to be careful. So, this could be relatively interesting inside, although I think all of the interesting stuff is really inside the actual sensors themselves and how they work. So, yeah, I don't think we're going to get too much into that side of things.

**Dave Jones:** But, anyway, it is an intrinsically safe product. There's the intrinsically safe, the EX symbol there. And what that means is this is designed and certified to go in underground situations like mines, where there are these explosive gases, and things like that. And, well, it's not designed to ignite those, so it doesn't matter how this thing is used,

**Dave Jones:** whether you turn it off and on, or it goes off, you know, the siren goes off, or you plug the battery in, or something like that, or it fails internally. It's designed to be intrinsically safe, so it doesn't ignite any of those gases.

**Dave Jones:** And there's a lot of certification which goes into intrinsically safe products like this. So, yeah, let's check it out. It's got a dot matrix LCD, this one is faulty. I believe Andreas said it was faulty, it was too expensive to repair, so they just scrapped it.

**Dave Jones:** It's got a NICAD battery pack in the back here, which we can take off. Hey, there we go. And D25 connector inside, that's really rather interesting. So this is the NICAD battery pack, presumably got some circuitry in here, charging circuitry and other such stuff like that.

**Dave Jones:** But, there you go, that just plugs in, and we can, got some screws on the back. Let's open this puppy up and see. So the first thing we'll do is just take off this module, it is designed to come out, so you can plug, they're designed to be user replaceable, so like, for example,

**Dave Jones:** if the fire brigade was on, you know, headed to a fire, you know, in a chemical factory or something like that, they may decide, oh, you know, they know ahead of time what factory it is and what sensors to put in here. They could just replace this module in here, and it looks like we've got a rubber surround,

**Dave Jones:** so they could replace that on route. There's a little port there, obviously that's for outside air. I'm presuming that this has maybe, well, it's got five ports, I'm not sure, you know, that's a free air port there. But also, there was a port on the side here, so I'm not sure if that's like the fresh air sensor or something like that,

**Dave Jones:** permanently built into the thing, because this is designed to be calibrated in fresh air. So you can turn it on apparently, and then run the calibration when you're out, you know, in the clean fresh air. And then that just recalibrates the thing for the current ambient environment that you're actually in.

**Dave Jones:** Generally fresh air, but it looks like, that doesn't come out, it looks like, so much for user replaceable, it looks like we have to, yeah, it's user, oh, OK, it's a bit compliant. Look at that, so it is user replaceable, but, well, so much for the, so much for the fireman changing the thing in the back of the truck on route to a fire.

**Dave Jones:** Ah, well, so, will that pop out? There we go. So, aha, there we go, and these are designed to be plug and play modules. So, i.e., they've got little identifiers in them, so that the firmware inside knows which one you've plugged in, so you don't have to reconfigure it or anything like that in software.

**Dave Jones:** You just plug it in, it's got an automatic ID system, it knows what it is, and it recalibrates itself. Now here we go, there must be some sort of pump system in here, because this looks like, as we said, came through that filter,

**Dave Jones:** there's that extra intake over there, and possibly that's linked to the outside here, so that may be, that's probably the pump. Um, so where they're actually pumping that around, and for what purpose, I'm not entirely sure, but, ah, like, how do you get these things out?

**Dave Jones:** They're supposed to be user replaceable, I guess you have to get a pair of pliers on there and pull them out. Hmm, actually that whole assembly in there, as we saw before, is sort of its own rubber shock mount, and I guess it's got to do that to reduce the noise and possibly vibration from the pump.

**Dave Jones:** I'm not sure if the pump continuously operates when you switch this on. I wouldn't think so, otherwise your battery life would be, ah, you know, wouldn't be great with this thing. So, not sure what the deal is there. Anyway, you know, maybe it just, um, does the pump, you know, once every 10 seconds or something like that,

**Dave Jones:** I'm not entirely sure how it, ah, actually operates, and then just, you know, takes a sample every 5 or 10 seconds or something perhaps. Now until we actually get down there and look at the labels, I don't know which ones are installed in here,

**Dave Jones:** what different types of, ah, gases these are designed for, but we can see different types of top elements here. This one has got, it's weird, it's got some sort of, I don't know, ah, you know, rough metallic surface on it, almost like it's little globules of solder or something like that.

**Dave Jones:** I'm sure it's not, obviously, but, ah, that's what me as an electronics engineer, that's what it looks like, almost. Um, anyway, we've got that particular surface, so it's acting as some sort of filter on top. These things are going to be filtered. And this one has some sort of membrane filter, I'm not sure what that material would actually be.

**Dave Jones:** This one looks basically the same, but it's obviously designed, it's a different sensor, designed for a different gas, they've got different colours on them, so presumably they're different models. And this one here is a complete, ah, moulded plastic case, except for it looks like a tiny little vent hole in the top, that's all we've got there.

**Dave Jones:** Why so small? These sensors, these actually can be blocked by, ah, you know, water or gross humidity or something like that in the air, at least some of them, so you just have to be careful not to, you know, certainly wouldn't want to immerse this thing, that's for sure.

**Dave Jones:** The only way I can think to get these out, ah, apart from pulling them is, give my, hey, there we go, give it a good whack, and we're out. Look at that, we've got ourselves, these, these two have popped out, ah-ha, you can see the connectors down in there, show you those in a minute, there we go,

**Dave Jones:** and this one down here, which is in its own plastic cavity, I'm not sure why, there we go, ta-da! We're in like Flynn, look at that. Ah-ha, so it turns out this one with the plastic surround here is different, it's got a pin header, it's got a standard 0.1 inch pin header,

**Dave Jones:** it's got a, ah, polarity, ah, hole plugged up there, so that's what this module plugs in for, I still don't know what it does, there's nothing, ah, EX sensor, so let's intrinsically say sensor C, I don't know, I'll have to, ah, take a close look at that,

**Dave Jones:** and decode that to see what, ah, that is, but anyway, it looks like there's, maybe that one is for like semi-permanent, ah, installation, it's only plastic, but, ah, perhaps that's different, anyway, the other three physically use a smaller, ah, smaller pin pitch connectors there,

**Dave Jones:** and they're male instead of, ah, female, so, entirely different, and that's what these sensors plug into, and they're plug and play, so obviously they've got some sort of ID system on there, whether, Lübeck, there you go, I've been to Lübeck, fantastic little town in Germany,

**Dave Jones:** I loved it, I went to an organ recital in Lübeck, Lübeck, there you go, at one of the churches there, um, that was something, ah, yeah, so, these are rather interesting, whether or not they do it with just like a resistor value or something like that,

**Dave Jones:** you could, and the firmware just reads the resistor value, but that'd be the easiest way to, easiest way to do it, otherwise you could have like a, a little Maxim, you know, laser engraved ID, ah, chip or something like that, ah, perhaps, or some sort of, you know,

**Dave Jones:** um, you know, something, I squared C, because you only got a couple of pins available there, but, anyway, ah, so that's the raw sensor, whether or not these have any, ah, amplifiers in them at the bottom, I guess we'll find out by taking them apart,

**Dave Jones:** or whether or not they, ah, are, you know, analog output, just direct analog output, so we'd only supply like a power, we'd get analog output, and then we'd have the ID, the pin ID, ah, system, whether or not that's the case, ah, or whether or not they do actually contain an amplifier,

**Dave Jones:** and the board in here is expecting, you know, a, ah, correlated like, you know, a one volt analog output or something like that, ah, because this thing does actually, you know, it measures value, so it's got to have ADC, it's got to be an analog output,

**Dave Jones:** ah, sensor, and it does data logging as well, I think I forgot to, ah, mention, you can actually, ah, log data for like 50 hours or, ah, something like that, so, yeah, it's, I don't know, might have to crack these open, but let's get the rest of the box open first, I think.

**Dave Jones:** Now it will be interesting to see inside if the PCB is, ah, conformally coded or not, um, you don't have to for intrinsically safe, ah, devices, although it may be, probably not, it'd be my guess, but, ah, certainly would not surprise me if we found a conformally coded board,

**Dave Jones:** I don't expect anything fancy, I expect a, you know, an 8 or a 16 bit micro or something like that driving the, ah, LCD, and, ah, with a ADC either built into the micro, if it's not, ah, that demanding a requirement, that's a long screw,

**Dave Jones:** or, um, or whether or not, ah, it uses an external, you know, precision ADC, something like that, could very well do, but we'll find out, but we'll find out, but I don't expect much else, I expect a microcontroller, on, on the electronic side of things, a microcontroller, maybe some signal conditioning,

**Dave Jones:** that one, that one's feeling quite, quite weird, almost as if it's slipping, so, I don't know, yeah, it's not just gonna, oh yeah, hey, there we go, we're in. Ta-da, look at that, that's pretty easy. I think it's gonna, there's a board on the front, for the PC, ah, for the LCD,

**Dave Jones:** as you'd expect, so, the rest of this, hopefully, just pulls out. There we go, it was just held in with a, a pin header, on the back side of the board there, there's our, oh yeah, it is conformally coded, yeah, there you go,

**Dave Jones:** you can see the gloss of the conformal code, so yeah, it just had the, ah, pin header, down in here, oh, the female, and, down there on the, ah, LCD, we've got our male pin headers, down there, which then plug into the board, neat.

**Dave Jones:** So what we've got here is a two board construction, right angle, ah, D25, as you'd expect, so, double-sided load on that, so, there's quite a bit of, ah, stuff going on on that board, but that's a processor, as I said, 8-16 bit, ah, micro,

**Dave Jones:** maybe some latches or something like that, very old school sort of design, um, so I'm not sure of the vintage of this one, but, ah, might be able to get a chip, ah, date code or something like that. So we've got ourselves a battery, for the battery backup, of course, for the, ah, real-time clock,

**Dave Jones:** that could be the real-time clock chip there, if it is quite old school, yeah, there's a 32 kil, that'd be the 32 kilohertz watch crystal next to it, because of course, being a data logger, you've got to, ah, ah, date and time, stamp everything, and then, ah, probably some analog stuff happening on the bottom, perhaps,

**Dave Jones:** but there is a secondary board here, I'm not sure if that's just, it's well shielded, look at that, they've really gone to town to put the, ah, that metal foil all over that, that's, yeah, that's really going to town, so I'm not sure if that's part of the intrinsic,

**Dave Jones:** ah, safety of it, or whether or not, ah, it has to do with, um, yeah, just, um, you know, in, in keeping out, ah, interference, for the sensor board, so, yeah, we've got some circuitry down on there, can see some resistor networks and stuff like that,

**Dave Jones:** so we're probably, oh yeah, yeah, yeah, I think it's going to be chocker too, so there's lots of analog stuff happening on here, but I think this is going to be a lot of old school, I'd probably expect a lot of 7-4 series logic, like, I'd probably expect these to be, you know,

**Dave Jones:** latches, or 7-4 series latches, or something like that, perhaps. And there's the top side of the board there, ah, this connector here is the pump output, so it goes directly up into the pump mechanism in there, there we go, there's the, ah, there's the reservoir for it, and the pump just drives that, boom, boom,

**Dave Jones:** on a, ah, offset shaft there, and boom, it just drives it in and out, something like that, and, ah, generates a bit of pressure, whether or not it's noisy, you wouldn't think it'd be, you know, hugely noisy or something like that, so, yeah, um, this, as I said, most likely,

**Dave Jones:** that oxygen sensor, if I can, ah, Google that part number. Aha, no, no, no, no, no, no, that's not an oxygen sensor, that's going to be a pressure sensor, of course, making sure that the pressure inside the system is still good. Here is going to be your oxygen sensor, I'm presuming, once again, it's an oxygen sensor,

**Dave Jones:** and they've got that sensor going directly down to the analogue board down there, there we go, two pin header, that's a bit, that's a bit dodgy in how you do it, look at that, don't like that. Gee, they could have done that a bit better, at least have a locking connector or something like that,

**Dave Jones:** not impressed there, and, ah, the, ah, pressure sensor, of course, I could, yeah, you can look up that number, there it is, PA6GF25, I have no doubt that's a pressure sensor, should have known that, I used to work on pressure sensors a lot back in the day,

**Dave Jones:** that also goes down to the analogue board down there, nothing special, so, that's what we've got in the whole system, so, I guess, ambient oxygen sensor plus the plug-in units, I still don't know what that one down there is with the separate connector,

**Dave Jones:** it's obviously got nothing to do with this pump system. Actually, no, I stand corrected again, I've gotten this out, and it gets more interesting as we get into this thing. There's a vertical board here, there's some sort of sensor board, there's another sensor embedded in this part here,

**Dave Jones:** this is really interesting, this is why it needs a pump, it needs to flow the air across there, I still think it is the oxygen sensor, but it's really interesting, look, they've got a mirrored, a real, like a polished mirror or something in there, almost looks like a gold-type finish or something like that,

**Dave Jones:** which is, you can see it's sort of welded on the back there, so they're obviously, so this, I don't think it's a sensor, this is like the, like a, probably, an infrared, aha! I reckon this is going to be an infrared LED, bounces through there, off the back,

**Dave Jones:** and we've got ourselves a photo sensor here, which can detect the oxygen level. Aha! That's what it's got to be. Just like those cheap-ass eBay pulse oxymeters you can buy, that clip on the end of your finger, they just clip on there and they put, they shine infrared light through your finger,

**Dave Jones:** and based on that, you can work, based on, you know, absorption and stuff like that, you can work out the level of oxygen in your blood. I reckon a similar sort of thing is probably happening here, we've got ourselves an infrared LED transmitting,

**Dave Jones:** bouncing off the back, and then, you know, maybe, you know, that, why that, they've obviously gone to a lot of trouble there. It's not just a mirror, it's a specific type of mirror. So, specific type of material, so whether or not that's doing some filtering or something,

**Dave Jones:** or some such thing, I don't know. I'm certainly no expert on that side of things, but here's our second board, down the bottom here, we can pull that off, there we go, they've got a little flex membrane going there, so it's all really quite a bit of a mess going together here,

**Dave Jones:** so that's only an interface board really, nothing fancy there at all, but they've gone to a lot of effort to sort of integrate that in to that whole pump system. It just seems very convoluted, like they could have easily done something a lot more attractive

**Dave Jones:** and sensible than that, I would have thought. And that plastic ring on that connector there, it's just that. It's a plastic ring. So, yeah, to stop, presumably to stop the wrong modules being forced into the wrong hole, so why they've gone to that effort, there's obviously one module which, you know,

**Dave Jones:** they really don't want as part of this modular system, it's designed to be plugged into a separate connector. What that one is, I don't know, you'd have to read the user manual. I haven't read the user manual. That'd be too much trouble, wouldn't it?

**Dave Jones:** And it would ruin all the fun of trying to figure out all this yourself. Actually, this is getting rather confusing the more I think about it. I'm, the first thing I'm thinking now is that, well, why do you need the pump? The pump isn't needed just for an infrared oximeter, for example,

**Dave Jones:** that could easily work without the pump, so that doesn't make sense that they would need a pump for that. So, I, yeah, I don't know, oh! Eh, eh, I get it. I just got it. I just got it. Okay, yep, duh. Um, where does the pump go?

**Dave Jones:** Look, at this bottom here, here's the inlet, okay? This is actually, I think this is the inlet up here, and that's what plugged into, Aha! There you go. That was our port on the top, so there you go, that's designed to plug an external probe into it,

**Dave Jones:** and then, of course, when you've got an external probe, you need the internal pump to suck it into the chamber in here to actually analyse it. And, I'm also thinking that this is, may not just be an oxygen sensor, it might be doing other stuff as well.

**Dave Jones:** I, you know, I think I'd better go to the manual for this one. And, yeah, sure enough, it all becomes quite clear when you read the manual. Should do that first, RTFM. Um, yeah, the internal pump is an optional thing, which, look, he's a happy dude there,

**Dave Jones:** he's checking a remote, the hose coming out there, and checking a sample port on this pipe here. He's probably got some stuff running through it, he's checking whatever, you know, for the presence of gases or something within that pipe, that it's a suitable level.

**Dave Jones:** And there you go, you can draw 45 metres, that's pretty good. So, there you go, so that answers the question about the noise and stuff like that, who cares, you know, how quiet it is, it's not continuously operating, it's only when you choose the internal pump.

**Dave Jones:** And they also differentiate between this, which, yes, confirmed it is an infrared sensor, that was pretty easy, I was pretty sure I wasn't going to be wrong there, but this, what they call a CATEX sensor, which is the one that plugs into here, which is this module here,

**Dave Jones:** you can choose to switch between these two, and they might be the same sensor for the same gas, for example, or not the same sensor, but the same, detecting the same gas, you can choose between two different types. This one, which uses whatever method,

**Dave Jones:** and the infrared one. And there's a page which explains that. Ta-da! Here it is, IREX, so the infrared one versus the CAT. So the infrared operates in environments with low or no oxygen. Aha! And the infrared one is immune to poisoning and inhibiting compounds

**Dave Jones:** that affect this poor sucker here. So there you go, so you can have both of those in there, and you can choose, well, there you go, different responses, different compounds versus catalytic sensor, which is this one here. So there you go, you can choose during operation

**Dave Jones:** which one you want, even though they're detecting the same gas, useful for different environments. Terrific! Thought of everything. So why don't you just use the infrared for everything? Well, I don't know, I'm sure one of these catalytic sensors is going to be better performing in some situations.

**Dave Jones:** And as it turns out, I believe this one is actually a methane sensor, but you can get different types, you can get ones that do hydrogen, and what's called nonane. Never heard of it. Anyway, for you chemistry buffs out there, it's C9H20. Go figure.

**Dave Jones:** Now I've figured out why we've got different sensors here. These are, well, in this case, this one's an oxygen sensor, there we go, O2, and this one's a hydrogen sensor, H2. So these are just regular sensors, but this one is a catalytic sensor, as I said,

**Dave Jones:** and this one is designed to, that's why it's got a different, physically different connector on it, it needs power for an internal heating element in there, designed to detect combined combustible gases. And this is the EX Sensor C. And here's how it works.

**Dave Jones:** And ta-da! We don't even have to open it. This is what is going to be inside this sensor here, and it looks like it's fully potted anyway, I don't think I'm really going to be able to get in there properly. Thankfully, Draeger have provided an exploded internal diagram.

**Dave Jones:** Fantastic. What we've got inside here is basically a catalytic bead sensor, and it's based on the polyester principle, where, yes, it's like a resistance, but the resistance value changes with the gas in there. So what we've got is we've got ourselves a heating element here,

**Dave Jones:** and a sensing element, and basically you heat it up to a couple of hundred degrees, I'm not sure exactly what temperature it gets to, but heat it up very hot, and what it does is it actually burns the gas inside. That's why you need the flame arrestor here,

**Dave Jones:** because you don't want it to, you know, actually catch a light inside there, and, you know, it flames to shoot out with these combustible gases. So that's what they're doing, which is funny in an intrinsically safe sensor, an intrinsically safe device, to actually burn the combustible gas you're actually trying to detect.

**Dave Jones:** Hilarious. Anyway, what they're going to do is burn the gas in there, and if, of course, the more combustible the gas in there, the hotter it actually gets, which changes the resistance of the detector element, which is a platinum coil. And that's pretty much all there is to it.

**Dave Jones:** It's rather neat. I like it. And it gets even neater than that. The reason that they show two coils here, one's not actually the heater element, they're not actually showing the heater in there, but one, they've called it a compensator element. And what that is basically doing is

**Dave Jones:** that one is not reactant to the temperature change. So this allows them, this is built into a Wheatstone bridge circuit, and that allows them to compensate for ambient temperature, because they've got the one that changes with the gas, the burning gas pressure in there,

**Dave Jones:** and one that doesn't. So that allows them to compensate for that ambient temperature changes. Brilliant. So yes, the gas inside here can actually explode, because, hey, we're trying to detect combustible gases. They're going to combust, right? So to stop it, yeah, they've got this flame arrestor here

**Dave Jones:** and a sinter disk inside the thing, which basically controls the reaction. It stops it blasting out the end here, but it also stops the reaction internally. So when it does, if it does explode, it sort of self-extinguishes itself. And that's why you can use these sensors

**Dave Jones:** in an intrinsically safe product designed in a combustible environment. Yes, they do combust it, but, hey, do it safe. And I might see if I can dig open one of these puppies and... Ta-da! Hello. What have we got in there? Aww. Well, let's see if we can't hack into that with a pair of side cutters.

**Dave Jones:** Brilliant. I've got my hacky pair of side cutters, not my good ones. And what? That was a waste of time. Don't know what's going on there. Anyway, potted inside there by the... That's interesting. No, hang on. Ooh. Ooh. What is that? That's interesting.

**Dave Jones:** I've never... never encountered that before. Not sure what material that is. No idea. Anyone got a clue? Anyway, there is a wire hanging off there. So, whoop, I just broke it. Little stuff in there. Oh no, look at that. There you go, that's weird.

**Dave Jones:** There's a couple of wires. You can see them going. That's soaked in some sort of... well, I won't call it electrolyte material, but some sort of soaked in something. And there's obviously some sort of sensor down in there. Not sure what, right, down in there.

**Dave Jones:** Yeah, that wire was going through to the top of there. So anyone, anyway, if anyone has any idea how this hydrogen sensor works, I don't know. And unfortunately, the PCB down in there is potted as well. Aww. Alright, over to the PCB, and I'll try and scrape off this conformal coating.

**Dave Jones:** Looks like this one's coming off relatively easy. Ah, I see an M in there. I see the big M. I see the golden arches. And no, it's not Makars. Not bloody Mickey D for you, Yanks. It's Makars here. So, no surprises for finding a Motorola

**Dave Jones:** something or other. Ta-da! Motorola MC68L11. Well, basically it's a 68HC11, as you might be more familiar with. The L stands for the low-voltage version, which goes down to, wait for it, folks, 3 volts. Aww. But back then, that was absolutely stunning. So, yeah, there you go.

**Dave Jones:** Obviously for battery operation, they're using a low-voltage version. Now, this is probably all the firmware in here, which is in that puppy over there, is probably all in assembly language. It could be in C. It could have been originally written in C, but more likely assembly language,

**Dave Jones:** because to get a product like this certified as intrinsically safe, every line of code in this thing must be verified. You pay someone like 100 bucks per line of code to actually go in and verify that it's all OK and it's not going to explode or something like that.

**Dave Jones:** So, yeah, more than likely written directly in assembler. And those other chips, yep, I was right, latches, there we go, 74HC574s. Is that a date code I can see there of the 27th week 01? Possibly. The number on that one's not easy to make out,

**Dave Jones:** so get some of the magic spit and put that on there. Might come up a bit better. Let me get the right angle on that. And you probably can't read that, but I can, it's just an NEC memory, so, yeah, that's just coupled to the processor on the other side.

**Dave Jones:** And just some random ones next to it, 74HC320. So, as I said, all these are probably going to be just, you know, pretty generic 74 series logic, nothing much happening at all. Now, this array of components down here is quite interesting. What I think, there's no analog stuff happening here,

**Dave Jones:** this is another analog latch, so all of this stuff is digital. So what this is, because of its proximity down to the external connector down here, for intrinsic safety, what they've done is they've got resistor limiting and diode clamping here. So that's why they've got so many in that symmetrical arrangement

**Dave Jones:** near the connector there. So all of the I.O. going to this connector for intrinsic safety reasons is all going to be resistor current limited and diode clamped. And you're going to see the same thing over here with this D25 connector as well, and probably this external connector here.

**Dave Jones:** They're all going to have the same arrangement. And if we rip apart what we'll call the analog board here, interesting, they've got some marks on there. They've done that before it was conformally coded, you can see the coding over that. So I'm not sure why they're marking those,

**Dave Jones:** because they just look like resistor arrays to me. Nothing fancy-pancy going on there at all. They've got some board, some like elephant hide under there, hot-snotted in place, that's interesting. That'd be for intrinsic safety reasons, there's no other reason why they'd have that cardboard in there,

**Dave Jones:** that's for sure. And there we go, there's the bottom side of presumably our analog board. Fine, pin-pitch part there. Ooh, fancy-pancy stuff. Probably just some more 74HC interface stuff here on top would be my guess. And yeah, that is a four-layer board too.

**Dave Jones:** Well that's interesting. And a Philips PCF8577 I2C interface, of course Philips invented that. LCD driver, so there you go, that's driving the big dot matrix LCD on the front. Which is strange, because they have a proper LCD module down there with the LCD drivers, so, huh?

**Dave Jones:** And it seems that I don't have to scrape the conformal coding off this to see the numbers in there. If I get it at the right angle under my Mantis microscope, I can see clean through the conformal coding, straight through the numbers, and nothing is revealing.

**Dave Jones:** We've got three op-amps down here, just 27L2s, nothing happening, just, you know, dual op-amps. These are all 74 series logic all around here, and well, nothing and all up here, so nothing else on the top side there. And on the other side here,

**Dave Jones:** we've got a couple of quad op-amps going on, once again, 27L4s there instead of the dual version, and some MUXs, some 4000 series, you know, 4051 type MUXs going on around here, but that's it. So that literally is just an analog interface board,

**Dave Jones:** really, going over via, presumably, this header cable here, over to the main board, and of course there is no ADC on this board, or not as a separate chip. So it is built into the microcontroller, of course. This is an E-series 68HC, or even though it's the L version,

**Dave Jones:** 68HC11 E-series, so it's got an 8-channel, 8-bit ADC built in. So, yeah, fairly crude measurements, nothing fancy, but that's doing all your data logging, all your memory over there is holding all your data logging stuff, and well, yeah, there's not much else to it, really.

**Dave Jones:** Fairly old-school stuff, couple of op-amps, and ADC built into a microcontroller, pretty much as expected. But of course the most interesting stuff is to be found in these sensors and things like that. Yeah, sorry, I can't get that apart, and the other one just didn't come apart,

**Dave Jones:** so, yeah, I don't know. But this infrared sensor, rather interesting, look, they've actually got, this is the infrared transmitter here, but they've obviously got another sensor in there, and another something, another sensor, happening down in there. This is a cheap-in TO-92 package device,

**Dave Jones:** just bent over at right angles like that, and shoved through a hole in there. Doesn't come out as a separate hole inside there, though. Well, actually, that, what I thought would be the infrared lead there, is not. It's got, like, 4 ohms. And also, given that looks like just a bent TO-92 package like that,

**Dave Jones:** potted in there too, by the way, they've got some potting compound down the bottom there, so can't really get it out intact. But I am suspecting that that is a temperature sensor against the top metal there. That would be my guess about what's going on there,

**Dave Jones:** because usually, plastic TO-92 packages like that aren't a top-entry sensor, even if it does have, like, a transparent, or, you know, a transparent encapsulant there. Usually they're on the side, they're actually a side emitter. So, yeah, my guess is, because they've got the top surface there

**Dave Jones:** attached to, you know, basically thermally coupled through to that metal, my guess, and being 2-pin, my guess, eh, temperature sensor. Although, this being an infrared sensor, it is quite perplexing, because this is obviously a 3-terminal device. Whatever is encapsulated in this side of the housing over here,

**Dave Jones:** and this certainly isn't a lead, that's for sure. So, unfortunately I've had no luck trying to get this sucker out. It just won't budge. I've taken off the retaining screw clip in there, and it just ain't budging. Curiously, that reflective backing piece there,

**Dave Jones:** which is, you know, some sort of gold mirror or something like that, has got an individual serial number, whether or not that's a serial number for the whole unit, or whether or not it's just the serial number for that back surface. It could be that important that they had to individually serial number

**Dave Jones:** and presumably test and characterize that before they actually welded that in place. Hmm. I just had a thought. Now I think I might know what's going on here. And by the way, check this out. You can see the angle on that mirror. I just noticed that, of course, because it has to,

**Dave Jones:** the angle is going to be important to focus it down into the detection chamber down in here. What we've got, what I think is happening here, is that we've got a heater element here, and that is what's heating up and generating the infrared source.

**Dave Jones:** We've got our, you know, our polished and perfectly aligned mirror that then reflects that down into the chamber down here. And what we've got is a reference temperature sensor down in here, a reference sensor, presumably, and then we've got the actual detector for the signal.

**Dave Jones:** So that's what they're doing. It's sort of like a differential between the reference sensor and the temperature sensor under test, and then that way you can take out any ambient temperature differences. Possibly. I don't know. That's my best guess. And if you're curious to see inside the battery pack,

**Dave Jones:** well, there we go. We've got a conformally coded charging PCB down in here, which then plugs at right angles into there. That's rather neat. I like that. And it looks like we've got ourselves a baseboard that's used as the connection, the external connection,

**Dave Jones:** to power through to the main board. So, yeah, really interesting arrangement, really. Looks like there's a charging port on the top here, but that looks like it's all gunked up. Looks like it's totally sealed, once again, for the intrinsic safety. So, yeah, that's really heavy and probably fully potted.

**Dave Jones:** So I don't think there's any chance of me getting that out any time soon. So there you go, that's the Drager, I'm probably pronouncing it incorrectly, I'm sure. Multi-Warn. It's the Multi-Warn 2, actually. And that was really rather interesting. A bit more involved than what I thought,

**Dave Jones:** and rather is fascinating. So if you've got any more details on how, say, the infrared sensor and stuff like that works, then please link it in, because that's fascinating. But there you go, a whole bunch of detectors, fascinating technology. And I'm sure there's a whole bunch of, you know,

**Dave Jones:** really good science behind all this stuff too. You could do a PhD thesis on just, you know, how various different types of infrared sensors, there are different types of these, different techniques for actually doing it. There's an open one which actually works in open air,

**Dave Jones:** which is, you know, much huger than this, you know, like in the scale of meters and things like that, for, you know, big plants and stuff like that, detection. But this is fascinating how that's just, you know, linked in like that, and then you can plug a probe on the top here,

**Dave Jones:** and you can sniff things, and fantastic. I like it. Fascinating technology. Anyway, I hope you enjoyed that, and if you want to discuss it, the EEVblog forum is the place to do it. The link is down below. Catch you next time. Transcription by ESO, translation by —
