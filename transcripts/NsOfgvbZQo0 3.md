---
video_id: NsOfgvbZQo0
title: EEVblog #354 - CityRail PA Amp Teardown
url: https://www.youtube.com/watch?v=NsOfgvbZQo0
source: youtube-asr
timestamps: {"0": 1, "1": 24, "2": 48, "3": 77, "4": 103, "5": 121, "6": 136, "7": 154, "8": 168, "9": 197, "10": 220, "11": 257, "12": 270, "13": 298, "14": 311, "15": 338, "16": 362, "17": 383, "18": 403, "19": 423, "20": 439, "21": 461, "22": 478, "23": 494, "24": 514, "25": 540, "26": 565, "27": 580, "28": 594, "29": 613, "30": 634, "31": 657, "32": 673, "33": 700, "34": 716, "35": 734, "36": 754, "37": 773, "38": 790, "39": 802, "40": 833, "41": 861, "42": 874, "43": 905, "44": 925, "45": 952, "46": 969, "47": 992, "48": 1012, "49": 1028, "50": 1057, "51": 1077, "52": 1105, "53": 1131, "54": 1167, "55": 1188, "56": 1205, "57": 1225, "58": 1240, "59": 1267, "60": 1286, "61": 1304, "62": 1327, "63": 1369, "64": 1395, "65": 1429, "66": 1448, "67": 1477, "68": 1495, "69": 1521, "70": 1540, "71": 1560, "72": 1585, "73": 1598, "74": 1636, "75": 1655, "76": 1673, "77": 1696, "78": 1712, "79": 1730, "80": 1744, "81": 1768, "82": 1802, "83": 1820, "84": 1847, "85": 1877, "86": 1897, "87": 1915, "88": 1932, "89": 1957, "90": 1987, "91": 2015, "92": 2040, "93": 2053, "94": 2080, "95": 2102, "96": 2129, "97": 2149, "98": 2176, "99": 2191, "100": 2210, "101": 2223, "102": 2235, "103": 2252, "104": 2277, "105": 2295, "106": 2311, "107": 2334, "108": 2370, "109": 2395, "110": 2424, "111": 2449, "112": 2467, "113": 2491, "114": 2507, "115": 2537, "116": 2550, "117": 2571, "118": 2590, "119": 2609, "120": 2622, "121": 2629, "122": 2648, "123": 2667, "124": 2687, "125": 2705, "126": 2726, "127": 2743, "128": 2759, "129": 2779, "130": 2795, "131": 2822, "132": 2848, "133": 2859, "134": 2893, "135": 2909, "136": 2932, "137": 2946, "138": 2963, "139": 2981, "140": 2996, "141": 3035, "142": 3051, "143": 3083, "144": 3100, "145": 3121, "146": 3138, "147": 3158, "148": 3184, "149": 3208, "150": 3230, "151": 3244, "152": 3261, "153": 3275, "154": 3292, "155": 3312, "156": 3328, "157": 3362, "158": 3381, "159": 3409, "160": 3434, "161": 3453, "162": 3481, "163": 3508, "164": 3521, "165": 3540, "166": 3553, "167": 3577, "168": 3596, "169": 3614, "170": 3634, "171": 3651, "172": 3673, "173": 3696, "174": 3714, "175": 3742, "176": 3759, "177": 3787, "178": 3803, "179": 3821, "180": 3842, "181": 3862, "182": 3884, "183": 3901, "184": 3928, "185": 3951, "186": 3977, "187": 3991, "188": 4010, "189": 4033, "190": 4060, "191": 4079, "192": 4109, "193": 4129, "194": 4157, "195": 4182, "196": 4191, "197": 4213}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Got something interesting for you today. It's a PA amplifier from a train. Not a toy train, like a real train here in Sydney. People in Sydney may notice the Sydney Rail or State Rail or whatever it's bloody well called these days. Um simple, these are used in our trains.

**Dave Jones:** You've heard them before. If you've been on Sydney trains, you know, "Next stop, Central." Or "All stations to Wollongong." So, that's you know, that muffled sound, it comes from one of these amplifiers. Should be interesting. What's a high-power stuff? It's got to drive, you know, a whole bunch of speakers on the train, so we'll look into the design aspects of it as well.

**Dave Jones:** And we'll get some really good design insight from this. Ha, think we're going to like this one. So, you know what we say here on the EVblog, don't turn it on, take it apart. Now, normally, um it would come with a cover and we'd take it apart, but the cover's already off this thing. Now, normally, if you're really lucky, you'll find a schematic inside one of your products, but I found something a hell of a lot better in here. We've got the original designer.

**Dave Jones:** Ta-da! It's Doug. Doug Ford. Hey, Doug. You You designed this beast. I designed this beasty back in 1992. So, these are now 20 years old and still rattling around in Sydney trains. Literally. I believe so and to the best of my understanding, there are between 1,200 and 1,500 of these being manufactured.

**Dave Jones:** In fact, the most recent batch that was manufactured was an additional 50 units about 2 or 3 years ago. They're still made? They're still made, they're still in use and still pretty damn reliable. And you can tell us about the design of this beastie cuz you designed it from scratch.

**Dave Jones:** Yep, except we ran out of scratch and had to use metal work instead. Three rack units? Three rack unit high? Yep, 19-in standard rack mount. Mhm. You can probably tell by the front panel over here that it's got two distinct amplifier sections in there.

**Dave Jones:** One for public address and one for crew intercom and emergency. And what we might do is backtrack a little bit to the specifications of why we had to design such a complicated beastie for something that's just a power amplifier.

**Dave Jones:** Fire? It just yeah. Well, it's a little bit more than just a power amplifier. It's got a few extra frills in there and a few criteria that had to be met in the design. Excellent. So, let's go back in time, way back.

**Dave Jones:** Okay, first of all, let's kick off with how trains operate in Sydney, Australia. Different countries have different standards. We have heavy rail, by the way. We are one of the few People don't know, Sydney is one of the few cities in the world that actually runs heavy rail directly into the city instead of a What do you call it? One of those metro services, you know, the quicker, the smaller, lighter trains. We have heavy rail. Anyway, I'm sure you can look that up on Wikipedia. It's a lovely drawing,

**Dave Jones:** Doug. Oh, yes, indeed. Terribly accurate. And dreadfully accurate. Okay, our train system runs from 1,500-V DC overhead lines. Mhm. Our silver trains are generally configured so that we get a motor car with pantograph. So, these are the silver the traditional silver trains, which went from what vintage are they?

**Dave Jones:** Uh, I don't know. Late '70s? Yes, '70s onwards. Late '70s onwards? Are the Tangaras Are all the same? All the new Millennium train? These amplifiers don't go into the Tangaras or the Millennium Right. trains or any of those. Uh They called them the lemons because they they trains were lemons because they when they went in the tunnels it tunnels had a significant gradient on the track, I believe, and then they draw draw drew too much current and they couldn't get up the They weren't spec'd right. So, anyway,

**Dave Jones:** that was a bit of a fire on part of City Rail or whatever they call themselves. Anyway, these are the silver trains. All right. And we have Everyone in Sydney is familiar with those. Uh what what are called pantecs that pick up the 1,500 V DC.

**Dave Jones:** Uh and in each motor car set we've got big inverter motor drivers which and also circuitry which drives big 120 V battery banks. Now, for every motor car set there's also a trailer car. Then we'll get usually another trailer car and then another motor car set with its pantec and drive and battery set, etc. etc.

**Dave Jones:** And then that can be twice as long or three times as long. Yes. Are there two car sets, four car sets, six car sets, eight car sets, but they're always in pairs of a motor car and a trailer car.

**Dave Jones:** Got it. Okay, they're all cross-linked by rather large connectors which circulate things such as uh commands from the driver Let's say the train's going that way. So, we've got the driver in there. It's going to transmit motor speed controls from that motor inverter down to this one down here etc. etc.

**Dave Jones:** Uh there are public address signals that are circulated amongst the train. There are intercom signals so that a driver here can talk to a a guard who might be resident in the guard's compartment down here. There's quite a lot of signals. I think that there's some 20 or more wires within these rather large connectors.

**Dave Jones:** Are they used for existing other stuff? You don't have to piggyback signals on them or anything like that? Yes. Okay. There are now Right. I've opened a can of worms, have I? Oh, yes, indeed, because long ago they ran out of conductors in the wires, particularly now that they also have to transmit things like door open and close Right.

**Dave Jones:** commands. Yep. There's also now a lot of data signaling from destination signs up the front and down the back Got it. etc. etc. There's quite a lot of data superimposition and indeed even back in '92, that's where this amplifier came in.

**Dave Jones:** Now we'll erase that and kind of zoom in a little bit to what this amplifier has to do. Now we'll zoom into a plan view of a driver's car set with a driver's compartment up here and next car down here and the next car down here and the next car down here with a say a guard's compartment here.

**Dave Jones:** Mhm. Okay. Driver wants to talk to guard. Well, we need an amplifier here so that the driver can address the speaker down in the guard's compartment. Is it just speakers? Is there no Are there headphones? Are there Speakers only.

**Dave Jones:** Speakers only. Yep, ceiling speakers. Got it. We also So, we have a microphone here running into a power amplifier driving his speaker. Mhm. He wants to reply. Guess what? He needs a microphone driving into a power amplifier Mhm.

**Dave Jones:** back up the same lines to his. How many lines are we talking about here? A pair to do that. Single pair? Single pair. Yep. Yeah, the thing is it's entirely possible that if they get into a bit of an argument, they're both going to be pushing their talk buttons at the same time.

**Dave Jones:** So, it's not full duplex with a single pair. Oh, no. They're both going to be talking into each other, and basically the amplifiers have to be designed to not only feed Dean shorts, but also feed into the outputs of other amplifiers without self-destructing.

**Dave Jones:** That's part of the criteria. Uh another part of the criteria is Okay, these amplifiers are run from the 120-V battery banks previously mentioned. The voltage on those battery banks can vary from Oh, well, on a bad day when they're near stony flat, they might be down at 70 V.

**Dave Jones:** Mhm. If they're fully charged to the point of overcharge, they might be up at 150 V. That's a pretty big voltage range. of battery technology are we talking about? Lead acid. Lead acid. Thought so. Big lead acid. But just to add insult to injury, there's rather a lot of different electromechanical bits of machinery run from these 120-V batteries. They're not only used for the PA system, they're used for a plethora of other things.

**Dave Jones:** They're connected to inverters so that they can run the air conditioning systems. So, there'd be lots of dips and brownouts and all sorts of crap on there. there's brownouts. Uh they actually just describe the spikes that they see on these lines, which extend from, yeah, minor overvoltages of maybe 200 V for hundreds of milliseconds, down to 4 kV for some microseconds.

**Dave Jones:** Ouch. And State Rail actually have a list of spikes that they have observed. So, that And you have to design the amplifiers to accommodate. Do they have spike simulators to test that? Since So, when you're designing gear like this, do you test it to their standard?

**Dave Jones:** They didn't. We had to create Oh, you had to create the generators to do that. Yeah. There you go. Mhm. Which actually is disturbingly easy. Mhm. How do you do it? Pass a current through an inductor and open circuit the inductor.

**Dave Jones:** Capacitor couple the resultant spike energy onto your main rail and Bob's your uncle. It's disturbingly easy to simulate. Okay. this is a half duplex push-to-talk system if I've got the terminology correct. Yes. Right. Now, on the this is for the intercom system. We haven't addressed the PA system yet.

**Dave Jones:** The intercom system can use relatively low power amplifiers and in this case we are limiting the power here to 30 35 watts. Mhm. The lines connecting all of this run at nominal 100-V levels. Yeah. So, it's a fairly high voltage level, very few transmission losses.

**Dave Jones:** Mhm. But, one of the systems that was proposed is the use of a passenger help points. That's right. Such that in each in each passenger location, you would have a help point where you could push the button and talk to crew.

**Dave Jones:** So, that effectively overrides the crew intercom system. Yeah, now how does it do that? Does it give priority over the crew talking to each other at moments? Aha, there you go. Now, how does it do this? When a passenger pushes their emergency button, Mhm.

**Dave Jones:** as well as connecting their little local amplifier onto that intercom line and squirting audio, which will be heard by both of these speakers, it also injects a 25-kHz tone. Aha. That 25-kHz tone is detected by these power amplifiers, these pieces here, when they detect a 25k tone, they lock out other activity.

**Dave Jones:** Got it. So, that only the the passenger in in dire straits is heard. Excellent. Now, similarly, how do they reply to just him and not to that one and that one and that one and that one and that one?

**Dave Jones:** Cuz you don't panic the rest of the train. Exactly. Mhm. Okay. These, when the crew want to reply just to that help point, Mhm. they press the passenger emergency intercom button, and they're putting audio back down that line, plus a 50 kHz tone.

**Dave Jones:** Ah. The 50 kHz tone is detected by only the one who's had its button recently pushed. Right. Thus, two-way communication between Recently pushed, has it got a timeout on that? Yes. Right. Got it. Absolutely. Uh the logic of all of this was fairly carefully thought through.

**Dave Jones:** Right. Uh and not only that, they can't hold their button down for any more than 30 seconds. It times out. Mhm. Similarly, they can't hold their button down for more than 30 seconds. It times out. So, if you get someone who likes to have a good gab on your and then it's just You're out of here. Kill switch.

**Dave Jones:** They're flicked off the queue. Okay. Uh now, public address. Okay, all through here, we've got loud speakers spread right throughout the carriages. Now, these are double-deck carriages, so you've got uh yeah, maybe 10 or 20 or 30 speakers down the bottom.

**Dave Jones:** These are the ones you can't hear. Yeah, they're the ones that you can't hear, and there's there's a reason for that, which I'll actually come to. We will go into. Oh, yeah. Oh, yes, indeed. Everyone wants to know why they're crap, so we'll find out, folks. Stick around.

**Dave Jones:** The amplifier section used for public address, Mhm. particularly because it might be addressing the speakers in eight carriages, sometimes up to 16 carriages. Mhm. Much higher power. 150 watts. Right. Separate set of lines reticulated right through. Again, 100 volt stuff. That uh each of the each of these little 4-in speakers is I think tapped for about a half a watt or 1 watt load onto that line.

**Dave Jones:** So uh if let's say they're tapped at half a watt, it means that you can put 300 speakers onto that 150 watt amplifier. Right. And the amplifier will treat that with perfect aplomb. Yeah. Uh once you get to maybe 400 uh sorry, once you get to maybe 200 watts worth of load on the amplifier, it's V I limiting, I'll come to that, will start kicking in.

**Dave Jones:** Uh but you can talk to an awful lot of speakers. Awesome. Half a watt into a little 4-in speaker still represents a fair amount of sound pressure level in the carriage, particularly when you've got a number of such speakers.

**Dave Jones:** Multiple spread throughout, it'd be enough. Yeah. Okay, what kinds of problems do we have with PA systems even on nominally working trains? Mhm. There's two that I'm distinctly aware of. The first is that between some of the uh middle-aged and extremely old trains, there were some compatibility problems in the links that couple the carriages together.

**Dave Jones:** One of those areas of incompatibility was perfectly capable of connecting 120 volts DC straight onto the PA loudspeaker lines. Ouch. Ouch, indeed. want to burn your coils out. Well, what had burned out was the all of the uh the coupling transformers at the individual speakers.

**Dave Jones:** Until they started fitting those speakers with coupling capacitors. So that what you wind up having is a little coupling cap. Okay, this is your 100-V rail. Running into a step-down transformer. Transformer which drives speaker. Into the speaker. And you would pick the correct tapping on the transformer to give you nominally half a watt into that speaker from 100 V there.

**Dave Jones:** Mhm. Okay, so that was number one problem. Incidentally, in the earliest amplifiers we were not made aware of this particular problem, as a result of which uh you'll see in a minute there's a couple of toroidal transformers under here.

**Dave Jones:** Mhm. The larger of the transformers would get 120 V straight up it. It was sufficiently large that it would actually take quite some time to die, maybe tens of seconds. Right. During that period of tens of seconds before it ruptured, there would be a lot of smoke emitted.

**Dave Jones:** Uh it was after that first batch of amplifiers went into production that we were made aware of this, so we started on those first ones fitting extra coupling capacitors on the output of the transformer, so that DC wouldn't affect the transformers. Later versions, such as this one, had coupling capacitors incorporated on the PCB.

**Dave Jones:** Got it. And note, incidentally, that they're electrolytics. They are? They are electrolytics, but they're connected back-to-back. Right. Yes. So it doesn't matter which way round you put your DC on it during a fault condition, it'll still hack it.

**Dave Jones:** Okay, we're having a look at the back panel of this amplifier. Uh they're all uh XLR style connectors. Power. The output connector actually needs six connections. I'll come back to that shortly. We're missing a three-pin connector there for muting, which actually never got used. It was simply a provision that was put in for later. Uh this particular unit that I've got my hands on here at the moment is actually a production sample, Right.

**Dave Jones:** which is uh because let's face it, all of the working ones are rattling around in trains or sitting in depots waiting for something to break down. Okay, we've got an input here which allows uh uh program input, such as maybe radio or pre-recorded messages, into the intercom.

**Dave Jones:** We have two inputs here which allow similar uh program input, pre-recorded, whatever, music, annunciations to be fed into the PA system. We also have a guard's microphone connection and a driver's microphone connection. Mhm. Okay, uh I should at this stage maybe go back to the whiteboard and discuss the overall topology of the amplifier.

**Dave Jones:** Possibly. I'm interested in this uh heat sink. It's a rather unusual riveted arrangement with a What, a stabilizing bar on the back? Well, Did Did they vibrate loose or what? Uh well, at at the stage that these amplifiers were designed, the company who I was working for, Jans Jans Electronics, uh were very good at sheet metal and had excellent sheet metal uh facilities.

**Dave Jones:** Uh and it was viewed at the time to be expedient to design the heat sinks from sheet rather than extrusion or any other form. So, we designed them out of uh stacked U sections Mhm. with this bar across the back so that it would made it more difficult to bend an individual fin out of shape. Now, also bear in mind these had to undergo almost military specification testing up to and including I think it was 24 hours on a shaker table.

**Dave Jones:** Mhm. And 3 weeks Swept through what range? What's the range of vibration on a train? Cuz I know there are standard specifications for vibration for road, air, rail travel and in international vibration equipment standards. You're pressing my memory here, but I think it was of the order 5 or 10 hertz through to about 500 hertz.

**Dave Jones:** Yep. That sounds right. And if you give me long enough, I'll remember what the actual amplitude levels were because they varied with frequency, too. Yep. And uh So, that would be a swept sine test from through that range just continuous sweeping once a in 10 seconds or something.

**Dave Jones:** Yes. Yep. And there was a an additional pretest where they actually went through searching for resonances Mhm. that were visible to the naked naked eye. Yep. Was it only tested in one axis? The mounted The axis it was mounted on, was it tested in all three axis?

**Dave Jones:** Seriously, I can't remember. It was 20 years ago. Yeah, it was 20 years ago, literally.

**Dave Jones:** Okay. We're in. What we've got down there is the two toroidal output transformers. The power amplifiers, since they run for a nominal 120 volt DC supply rail, we designed them simply to be a push-pull class AB amplifier run directly from 120 volts, which gives us RMS output voltage before clip of about 35 volts.

**Dave Jones:** So, these transformers are 35 V and 100 V step-up transformers in 30-odd W size and 150 W size. And that's the one that the smoke comes out of in large quantities when you put 120 V DC into the 100 V AC side.

**Dave Jones:** Oops. Lots and lots of very, very solid 1.2 mm punched steel. All good, solid stuff. And we can have a look at this. Okay, pretty simple wiring looms. Bucket loads of TO3 output transistors, also used for voltage regulation and such as well.

**Dave Jones:** are they? Okay, these are MJ15024 and 15025s in PNP pairs rated 250 V 16 amps. That's a lot of cancer compound on there. Uh well, actually this is just, just post the cancer compound era. So, these are actually zinc oxide There you go.

**Dave Jones:** rather than beryllium oxide. Yep. Uh I was rather disturbed at the stage that the zinc oxide thermal compounds came out to have a look at the MSDS sheets and discover that the LD50, in other words, the dose required to kill 50% of typical human beings was in excess of 50 kg of that stuff. Now, we had 2 kg tubs of this, and I just had this nasty mental image of sitting down to a meal of 25 tubs of silicone silicone thermal grease.

**Dave Jones:** I I think I think I'd die of repugnance before I actually died of thermal grease poisoning. Yeah. So, yeah, this is the non-toxic stuff. Yeah. Uh I don't think I've ever actually come across any true beryllium stuff. However, I have as a teenager being up to my elbows in polychlorinated biphenyls out of power factor correction capacitors. Maybe that goes some way to explaining some aspects of my behavior.

**Dave Jones:** Yeah. Now, okay. This is real good old-fashioned earth technology. Uh we've got op amps down here which are NE5532s. Now, in '92, these op amps would have been out probably maybe up to a decade. I can't remember when the 5532s first came out, but they Look, oddly enough, they're still pretty much considered to be the duck's guts with regard to audio op amps. There are only a few op amps that are considered superior to them.

**Dave Jones:** So, for an old and venerable chip, they're doing all right. We've got some a couple of CMOS switches over here for routing signals to different places. What's missing here and here are, God help us, a couple of gate array logic chips.

**Dave Jones:** Oh, you didn't. You didn't design in a GAL. We designed in a couple of GALs for the logic functions. Why on earth did you do that? This is '92, remember? Okay, we didn't want to use micros because particularly back then uh micros unless you knew that they were going to be regularly rebooted, there was always the risk that they get just sent off into a loop or misbehave in some fashion.

**Dave Jones:** Yep. Unrecoverably. Exactly. Now, the alternative would have been to use quite a smearing of 4000 series CMOS chips. Which with the benefit of hindsight would have been a vastly superior solution because the logic combinations we've got down here really aren't that difficult.

**Dave Jones:** No, I wouldn't think so cuz you can't do much in a GAL. Ultimately, you save might save five or a 10 chips or something. We were probably saving five or 10 4,000 series CMOS chips. Those GALs proved to be the bane of our lives in later variants because the primarily the input pins started off having very, very weak pull-ups.

**Dave Jones:** Mhm. About I think it was one between one and five microamps. Then they went to, you know, the B and C versions which had maybe 10 or 20 microamps, 20 to 50 microamps. The most recent ones that we got had more than 200 microamp pull-up.

**Dave Jones:** Ouch. And this completely stuffed some of the uh some of the analog cheating that we were doing around the GAL. Ah. Cuz you can fly to the moon on a couple hundred microamps. So this is simply the change in uh manufacturing technology Mhm.

**Dave Jones:** over the over the last 20 years has made huge differences to the strength of the input pin internal pull-ups. Got it. Now, they've also become faster, but let's face it. This is dumb switching of mic signals. We can't tell the difference between 50 nanosecond or 20 nanosecond performance.

**Dave Jones:** Tell it like it is, Doc. Okay. What else we got on here? Okay. This is probably where we might want to have a look at first of all a system architecture drawing. Let's do the topology. And then uh we'll go to a circuit diagram. We have circuit diagrams.

**Dave Jones:** We have circuit diagrams. Beautiful. 30-W amplifier going through a transformer. Okay. In whe- whenever the amplifier is unpowered, what we want is for the let's call that the circulating uh intercom line throughout the train. We want that to be switched to I'll just draw a a relay here. In the off state, we want it to be switched here to the local speaker.

**Dave Jones:** Okay. Doug's had a 20-year brain fart, folks. Okay. So, we have here a local speaker in the crew compartment. We We actually need two relays here. I'll just draw them in place and then figure out what they do later.

**Dave Jones:** Doesn't have to be accurate. We can have stick figures. Yeah. This will be sticky. This will be very very sticky. In the off state, we want that local Sorry, that circulating intercom line to go nowhere. Mhm. We want that speaker to be dead.

**Dave Jones:** When it's powered on, we want that to switch down and allow that speaker to be connected to the intercom line. So, that if if there's somebody occupying it occupying the the crew compartment, so that relay's energized, any audio coming through on the intercom line gets heard.

**Dave Jones:** And then of course, if we hit a push-to-talk switch on a microphone, we engage that one. So, we send the amplifier output onto the intercom line. Yeah, got it. So far, so good. What have we got over here? We've got a guard's microphone.

**Dave Jones:** We've got a driver's microphone. He has three switches associated with him. Okay, guard and driver.

**Dave Jones:** He also has three switches associated with him. Because the guard sits in a different place to the driver. Yep. Even when the driver's at the front, he's in the driver's seat. When the guard's down the back, he's in a little guard's compartment.

**Dave Jones:** Mhm. The driver's compartment and the guard's compartment might be next to each other. Yep. They've still got their own microphones in their own places. Got it. Okay, so he could address PA, intercom, or passenger emergency intercom. The driver, too, can address PA, intercom, or passenger emergency intercom.

**Dave Jones:** Okay, these are just uh switch signals from a box. Now, this is the other aspect about poor-quality announcements. The microphones for the guard and the driver are dynamic microphone capsules embedded behind perforated steel mesh. Right. Okay, so picture we've got these little microphone uh capsules with diaphragm there mounted behind stainless steel with a bunch of holes there.

**Dave Jones:** Okay, when you're uh talking into that, there's a fair amount of low-pass filtering applied to the speech by those holes. Oh, okay. Due to the diameter of the Yeah. Based on the diameter and the pattern and the Yeah. Now, why are we doing that?

**Dave Jones:** To try and make them Well, not vandal-proof, there's no such thing, but vandal-resistant. Mhm. Uh we have been told anecdotally, and I'm still not certain if this is true or not, and I don't want to offend too many train drivers and guards. We've been told that some crew are They've got time on their hands, they're bored, they're irritable, and if they can break something on the train, then they don't have to use that something on the train.

**Dave Jones:** Uh-huh. So, they've actually almost got a vested interest in trying to make things not work. Mhm. So, and also there's the possibility that if members of the public get into these compartments, they can wreak damage. So, we made these as bulletproof as we could, but at the expense of frequency response. So, the frequency response of the mic capsules might once have been kind of vaguely flat, but now look more like that.

**Dave Jones:** At what sort of frequency were we talking about Uh couple of hundred hertz. Couple of hundred hertz. Couple of hundred hertz roll off? So, but the human speech goes up to 3 kilohertz nominal. Yeah. Yeah. And indeed, the response the basic response the basic response of the power amplifiers here are 100 hertz to 15 kilohertz.

**Dave Jones:** Mhm. So, the power amps are quite wide band. Mhm. And indeed, the various other inputs that I showed you here for program material, they are unshaped. They're allowed to be flat up to 15 kilohertz, and they're capable of pretty high quality reproduction.

**Dave Jones:** So, in theory, they could play music on the train, no problems at all. They could. And you'd hear that, but then you'd get Next stop, Central or stations to woop woop. Just so. So, this is why the internal preamps down here Mhm.

**Dave Jones:** have shaped response with a frequency response like that to correct for the deficits here. So, in principle, as long as the person speaking is within about or maybe 200 mm of their panel, Mhm. you should be perfectly capable of getting quite good enunciation, quite good clarity over the PA speakers.

**Dave Jones:** Now, back in '92 through to about '96, I understand that State Rail was actually getting their guards and their drivers and putting them through a form of elocution lessons. Seriously. They apparently had little booths set up where they would uh record the person speaking, play it back to them for correction and amendment. And I believe at that time uh speech quality and comprehension were really very good.

**Dave Jones:** And it has slipped and slipped and slipped since then. It's not much wonder that uh because there's not a lot of attention paid to this side of things at the moment that you know, the the the crew don't necessarily know that they have to speak into the the grill panel instead of speaking off to one side. Uh they're not got their head half hanging out the door while they're trying to make the announcement.

**Dave Jones:** Yep. Uh interestingly, on some of the diesel car sets which uh which run interstate and out of the country, the announcements are made with a handset or handheld microphone and results apparently are much clearer because of the fact that they're using a close mic technique.

**Dave Jones:** I think that the crews on those runs are considered to be you know, a cut above and you therefore don't have to vandal proof it quite as much. Right. What's the what's the truth of that? I don't know.

**Dave Jones:** Seriously don't know. The mic preamps have frequency response shaping. Uh we've got all of these various switches so that the mic the output of the mic preamp can be gated through to the intercom amplifier or to the the PA amplifier to be sent out to the global PA line.

**Dave Jones:** Uh So, that switch will kind of run that one. That's the electronic switch there. That one will run that one. And if they are using that one, it not only gates that through, but it also gets the local uh 25 kHz oscillator and gates it through to And they And that's just summed onto the signal and Summed onto the signal.

**Dave Jones:** That's it. Okay, you have to do that a few times. Uh Yeah. But you said the bandwidth of this was only 15 kHz. Yeah. Uh it's for for speech. For speech. Yeah. Right. Uh the actual bandwidth of the power amplifier itself is intrinsically much higher. We do the limiting back in the pre-ampy side of things. Uh yeah, uh we're actually pushing, sorry, 50 kHz out here.

**Dave Jones:** And uh we figured in the system we get these ones to talk at 50 kHz because we've got enough power here and enough grunt to do those relatively high frequencies well, right? The passenger help points talking back, we're getting them to do that at only 25 kHz Mhm.

**Dave Jones:** because they're lower power, they're feebler, we're not asking too much of them. Right. Now, incidentally, at the moment, I seriously do not know whether that particular tone signaling system is being used for the help points or whether they've gone to use the uh how do you put it? The digital data path that's apparently a part of the most recent Lincoln signs, the display signs and stuff like that.

**Dave Jones:** That's an unknown to me. Right. Yeah. Let's face it, my knowledge is, okay, this is These are designed 20 years ago. My knowledge is probably 12 years old. So, the hardware's still there, but whether or not they're using it and I don't know.

**Dave Jones:** And part of what the Gatorade logic chips were doing was deciding who had priority. Okay, lowest priority of course was these program inputs. Uh next priority was uh things like the PA mics. Next priority was intercom and highest priority was the passenger emergency gear.

**Dave Jones:** Come on, you need the Gatorade for that? That's gilding the lily. Look, it was thought to be a good idea at the time and it probably was because it shrunk uh you know, maybe eight or 10 chip solution and a whole bunch of passives.

**Dave Jones:** For the that kind of thing I would have used uh probably diode resistor logic for a lot of this. Yeah? Uh it shrunk maybe a yeah, a six or eight or 10 chip solution down to two chips. Yeah.

**Dave Jones:** So, that was thought to be a a good thing at the time. Yeah, minimize the amount of hardware. And you came to regret it. Oh, yes. Yes, indeed. Uh there's a lot of other decisions that were made here that have proven over the period of time to be absolutely spot-on.

**Dave Jones:** Uh Tell us about them. Well, things like uh we've got probably three times as many output transistors as are actually needed. Mhm. They're just in parallel? Uh yeah. Yep. This is where we probably want to go to the circuit diagram, but for example, 150 W amplifier has three pairs of these beasties.

**Dave Jones:** Uh now, ordinarily out of three pairs of those, you would probably get a three or 400 W RMS rock and roll amplifier. Yep. Okay. Which you've designed many of. Oh, yeah. James did a lot more than uh train carriage amplifiers.

**Dave Jones:** Yeah, this was an oddball project for James, which is why uh I think around about '96 or thereabouts they decided not to support these anymore. How many amps did you design at Jands? Uh All of them? Uh During during the period you were there?

**Dave Jones:** Uh All of All of the All of them during the period that I was there. There's two that I did not design, uh, which are the First of all, the J300 and the J600, which were pretty much the first power amplifiers that Jands, uh, manufactured and they manufactured a lot of those.

**Dave Jones:** They were almost a copy of the Phase Linear 700. Okay. The next ones along were the J1000 and the J700. They're an amplifier which almost sent Jands broke. Why so? They had some, uh, fundamental design problems. Some of them electronic, but most of them simple mechanical stuff related to cooling and connection. The designer at the time, uh, didn't seem to be able to get a good grip on how to fix the problems.

**Dave Jones:** Incidentally, field failure rates were of the order 10%. Ooh, that's It's huge. Yeah. And seriously, it just about sent Jands broke. You know, they just in the middle of doing nothing, they just go bam boom. And apparently they sounded pretty much like that. I I I I heard one do it at a gig and it just sounded like bam boom.

**Dave Jones:** That was it. Uh So, lots and lots of lots of output devices later, uh the designer at the time, like I said, didn't seem to have a good handle on how to rectify it. Mhm. Uh, I came up with a whole bunch of incremental improvements, each one of which did its bit to get them back online. So, at the end of the day we had a set of solutions, you know, an an amplifier would come in, we'd apply the set of solutions, go out and have

**Dave Jones:** reasonable confidence it would survive. Got it. Uh at that time, I just got my degree, 1983. Uh the designer left or was pushed, I don't know which. Uh Jan said, "Hey Doug, do you want the job?" I said, "Yeah, pick me, pick me." And that's when I started designing power amplifiers. And the Jan's S920 was my first one.

**Dave Jones:** Mhm. Weighed a ton. I mean, it took It was a 450 W per channel amplifier and grossly over designed when it came to the heat sinking, the transformers. They weighed a ton. Well, actually, I think that they weighed something like 22 kg.

**Dave Jones:** The roadies loved you, I bet. Oh, yeah. Yeah, yeah, yeah. Once they got their compo for their backs, they did. But, the thing is, they were reliable. They just didn't break. Yep. As far as I know, these still 920s uh Power amplifiers in rock and roll go through a sequence or they did when I was there.

**Dave Jones:** The newest amplifiers were bought by the cream of the crop touring outfits Mhm. for hire and sometimes by cream of the crop bands who happen to have their own PA systems. Now, these days most bands just won't own a PA system.

**Dave Jones:** Mhm. They don't want them. They just want to hire them. So, they start off blowing to these prestige touring companies. After maybe 3 years in service, three touring seasons, the touring companies don't want to bother about, you know, the the seams that are starting to folded seams that are starting to just rip a little bit, the little bits of corrosion that are starting to creep in on of the connectors, the components that are just starting to rattle a little. I don't want to have to tighten up the mounting

**Dave Jones:** screws on the transistors. So, they sell them to the next tier down. And by the best crop. Okay, so these amplifiers go to the next tier down who are hiring out to all of the little pub bands, etc.

**Dave Jones:** Once they've done a few seasons there and they're really starting to get They they kicked around, look. Then they go to maybe a quiet retirement in a practice studio somewhere where the local punk bands are just beating the living snot out of them, but they're not actually moving them around much.

**Dave Jones:** Got it. Okay, so they're being canned, but they're not being physically punished. Mhm. And after a while there, maybe they'll go into somebody's home recording system and just mold there for a decade or so. Uh and that's that's what happens to old amplifiers. So, amplifiers.

**Dave Jones:** Yeah. Mind you, they eventually get binned? I'm sure they must, but They wind up in someone's basement somewhere driving Seriously, I don't know what happens to a lot of this pro gear at end of life. Mhm. Uh some of it I think just gets too old.

**Dave Jones:** Uh mixing consoles especially. Mixing consoles are nasty. They're full of pots and knobs. of pots that have to be There's full-time pot jockey's, isn't there? They go around and replace the the pot. Is that the correct term? Pot jockey or something? Uh close enough. Solder jockey.

**Dave Jones:** Yeah. Uh Uh no, a pot jockey is somebody who sells you green stuff at the pub. Yeah.

**Dave Jones:** Mixing consoles and lighting control consoles can be an absolute mongrel because quite often it costs more to replace all of the pots that have gotten scratchy than it does to buy a new console. That's it. So, I think there's a lot of mixing consoles that die premature deaths.

**Dave Jones:** Mhm. Yeah, before things like power amplifiers do. So, we've got three relays here. Were was vibration an issue in Absolutely it was. He Oh, yes. So, I picked it, did I? Yeah, because Okay, see how they well and truly tied down. Okay, that was of vital importance.

**Dave Jones:** But, there's a socket. They're in sockets there. Yes. Are sockets more trouble than they're worth in a high vibration environment for a relay? It's proven not to be so. Interesting. Yeah. Now, one of the things we were very uh conscious of, I think, is the fact that Okay, the relays are a weak link.

**Dave Jones:** They're an electromechanical component. They're one of the components more liable to failure than others. Mhm. In fact, the relays have proven to be ridiculously reliable. Wow. Uh I think are they? Uh I think we were using Omron. Omrons?

**Dave Jones:** Yep. Uh but we're actually we're using two different brands, I think, Omron and Finder. Okay. Actually, if you give me 2 seconds, I'll tell you what Yeah, they're Omrons. Yep, they're definitely Omrons, but uh um what we found Well, we didn't want to solder the relays directly onto the PCB Mhm.

**Dave Jones:** because if they were to be less reliable Reliable. then it made replacement an absolute bastard. By socketing them, we might be making a rod for our own back and reducing the inherent reliability simply by socketing them, but that was a better risk.

**Dave Jones:** It was a better trade-off than that. Yep. Exactly. And particularly given that we weren't entirely sure about the relative reliability of relay on PCB versus socketed relay, we opted to go socketed. Just go for the socket. Yep. Right.

**Dave Jones:** And yeah, they've been to be very reliable. Would would these things get hot where dried out caps an issue? Uh no, well yes and no. It's one of the things we made allowance for. We knew what the highest operating ambient temperature was going to be and I think it was uh 55 C Mhm.

**Dave Jones:** ambient. We knew the degree of maximum self-heating within the chassis, which incidentally is why it's got these huge number of vent holes on the lead and the Right side. Um so I think that the internal temperature would Was there ventilation there as the train moved?

**Dave Jones:** No. No. Right, it's in a sealed compartment. Uh not quite sealed, but there was no active blow-through, so we were relying on just natural convection for both uh heat sink cooling and also chassis cooling. Got it. So just from memory the uh we knew that the maximum operating temperature for the caps was going to be something like 65 or 70.

**Dave Jones:** Mhm. Uh we used 105° capacitors. With the electrolytic capacitors, I got it from the horse's mouth, one of the head honchos at Nippon Chemi-Con, Mhm. that the uh the Arrhenius coefficient, well the coefficient to use in the Arrhenius equation for capacitor lifespan, was double or half the lifespan per 10° increase or decrement.

**Dave Jones:** That's always been the rule of It's been used for a long time, but I've actually had it confirmed by one of the head honchos from Nippon Chemi-Con and that was kind of cool to have. So increase it by 10°, and you can kiss half your life goodbye.

**Dave Jones:** Yep. So in the case of a 105° cap, go down from 105 to 95, 85, 75, and that's two, four, eight times the lifespan of a 5,000 hour cap, 40,000 hours. Bang. Now in actual fact, we knew that uh because of cyclical operation and never going to sit there for incidentally the lifespan had to be 50,000 hours. We knew that they were never going to sit there at 70° or whatever for 50,000 hours.

**Dave Jones:** Yep. It was inherent that with cyclic of seasons, etc. etc. and especially the fact that they were not going to be used at 100% duty cycle for speech. Yep. They were never going to sit there baking at that temperature.

**Dave Jones:** So, they infinite almost the life and shelf life of the product. Yeah. And look over 20 years, how many electrolytics have I replaced? Mhm. None. There you go. Uh mind you, this is we've used Nippon Chemi-Con caps and I guess the two brands of cap that I tend to prefer Mhm.

**Dave Jones:** rightly or wrongly, uh Nippon Chemi-Con or United Chemi-Con so they do. Uh and Panasonic. Yes. I've had very good results from both of those. Both are the ducks guts. There's a few capacitors that I would not touch with a barge pole.

**Dave Jones:** I just did a video on that. Oh, okay. The caps on. All over the place wherever we've got capacitors electrodes is going to be Nippon Chemi-Con. Uh for yep. for a lot of the smaller stuff, these ones and also all of these little red fellows here, they're Wima.

**Dave Jones:** Yep. Uh and again in in that class of capacitor, uh Wima are considered to be pretty good. Not necessarily ducks guts but pretty damn good. Uh when it comes to little ceramic stuff, uh we didn't care. No. It's like uh whatever.

**Dave Jones:** Whatever the Chinese factory can Yeah. churn out. As long as they were COG or NPO dielectric and as long as the voltage rating was hugely in excess of what was required, That was all that was required? Mhm. Yeah.

**Dave Jones:** And these are high voltage? Uh these ones are actually mains rated. Yes. So, they're self-healing self-healing dielectric? They are. Yep. Uh we've actually had to replace a couple of those, but the main reason for failure is because in the environment that these are used, just occasionally, or more than occasionally, we will get a leak of carriage wash fluid. Now, this carriage wash fluid, we still don't know whether it's intensely acid or intensely alkaline, but it is intense. And it just Anything that it touches, it just stuffs

**Dave Jones:** completely. And it's all the it's all the worse if you actually have voltage on whatever this stuff drips onto. Ouch. And here's one we prepared earlier. Earlier. Let's have a look. Let's put that one to one side. Okay.

**Dave Jones:** Let's have a look at that. That is toasty, folks. That Look at that. We are talking roasty toasty, indeed. Now, we've had a drip of or a leak of wash fluid down here, and we've obviously had uh resultant arcs across the top of the circuit board that have etched through the circuit board while self-perpetuating as arcs. And it's just completely chewed that section of the PCB away.

**Dave Jones:** Ouch. Over on the far side of the PCB here, you can see the results on around the legs of these RAM chips here of just small amounts of surface wash fluid. Now, all of this stuff is low voltage.

**Dave Jones:** It's 12 volts. Mhm. Over on the other highly damaged end of the PCB, we've got full 120 V levels. So, uh yeah, this wash fluid has been responsible for, I think, maybe 3/4 of the repairs that we've needed to do.

**Dave Jones:** I notice you've got some snot in there. Uh yeah. Why have we snotted those down? Vibration? Uh yeah. Uh basically, a lot of these components, such as the capacitors, we've joined to each other. Mhm. Uh it's a sort of self-support society.

**Dave Jones:** Yep. Uh it makes the it makes it that much harder for anyone to start developing a wobble or a shake and breaking through its own leads. Yep. Incidentally, you'll will notice around these resistors that we've got little holes, or actually, not so little holes, under all of the resistors.

**Dave Jones:** Are they ventilation? They are. Yeah, the resistors are slightly spaced above the PCB, or actually, they should be. They're not on this one. Oh, they're not on this one. This is a pre-production. Uh uh no, this one's actually a production unit. The the other one was the production sample. Uh these should, by rights, be spaced up a little. Um Are you a fan of doing the little loop in the lead to distress the when they expand due to temperature?

**Dave Jones:** Uh no, I'm a fan of doing the loop. an inductor, right? That's an inductor. Look, uh actually, an inductor. Look, uh again, a note for audio fools, anybody who's silly enough to worry about a couple of tens of nanohenries of stray inductance in their low-value emitter resistors is a bloody loony.

**Dave Jones:** Seriously, it makes no difference. It adds a small amount of degeneration. Does it affect the stability of your amplifier? Well, if it does, you've done a pretty good pretty crook job of designing a power amplifier. Exactly. Okay, what I am a fan of with regard to resistors is doing a bit of shaping on the legs.

**Dave Jones:** Okay. Simply so that when you drop the resistor in the holes, it self-spaces. It self-spaces, yep. Not so much for a stress reduction or any of that stuff. Mhm. But any of your large components such as these 5-W resistors Yep.

**Dave Jones:** and sometimes the 1-W ones. These fellows down here. Yep. Uh I like to see and in fact I have a pair of uh leg crimpers that put that shape in to space them. Got it. And it's yeah, it's a nicety.

**Dave Jones:** On the downside because your component is stood up off the circuit board, it does leave it prone to It can. rock and roll. That's why you Which is where where you Yeah, you whack your Silastic on to fix it.

**Dave Jones:** And here's the schematic. You've done well. Is it on one sheet, Doug? Uh yes, and bear in mind because this is drawn back in '92 this was drawn up in uh Protel schematic. Uh sorry, Protel schema DOS. Uh DOS-based.

**Dave Jones:** DOS. Yes. Okay, let's have a look first of all at just one power amplifier. And this is a power amplifier here. Yep. Yep. Okay, we've got an input long-tail pair differential pair with a small amount of resistor uh so sorry, small amount of emitter degeneration.

**Dave Jones:** Current through the long-tail pair is set by this resistor to ground. Ordinarily, we might have say a current source in there, but a current source is gilding the lily on something like this. The Because we only want to go to central.

**Dave Jones:** Shush. Okay, the the output of the uh sorry, the long-tail pair is differencing okay, the non-inverting input here of actual signal and the negative feedback here which is 330k into 6k2. All right, now for AC it's 330k into 6k2, for DC it's 330k into 6k2 plus 100k.

**Dave Jones:** This means that for 60 volts there, we're expecting maybe about 15 volts there and indeed the bias for here is from a 15 volt reference derived by a 47k resistor from the 120 volt rail and 6k2 down here.

**Dave Jones:** Okay, so another diff pair up here to give us our different signals. Uh this is our voltage amplifier stage here. So that's basically a mirror. Okay, we then have MJE 340 and 350 pre-drivers MJE 340 and 350 drivers MJ15024 and 025 output stage.

**Dave Jones:** Got it. Output from this point here goes to coupling capacitors and into the output transformers. We'll trace that through in a second. One of the most important points is the output limiting the short circuit protection. Output current here comes down through those two emitter resistors which in this case are 1 ohm.

**Dave Jones:** We use the voltage sensed across those resistors to well if the voltage across there is high enough it starts turning on these transistors Got it. which shorts drive away from the pre-drivers down to there or away from this drive down to there.

**Dave Jones:** How much distortion does something like that add if we're talking about like a hi-fi? Would Would you do that on a rock and roll amp? Absolutely. Yep. Absolutely. it's essential, of course. Yes. The whole point is you design all of the circuitry around these VI limiters so that it simply does not take any action during normal operation. So, if you've designed a power amplifier to run, say, a 4-ohm speakers, Mhm.

**Dave Jones:** you would typically not have those take a action until the impedance drops below, say, 2.7 ohms. Got it. Or maybe below 2.7 ohms plus 2.7 uh reactive. Mhm. Or 2.7 Sorry, 2.7 J reactive. Yeah. Uh so that normal reactive loads that you might encounter in speakers just Mhm.

**Dave Jones:** have no effect. But as soon as you start getting serious overloads, which are enough to really stretch your output devices. Oh, incidentally, of course, you have to size your output devices so that they will cope with normal loads.

**Dave Jones:** No. Duh. That's Who would have thunk it? Yeah, who would have thunk it? Yeah. Okay. So, once you You have an issue with fake transistors in the day? No, we didn't. They just didn't bother to fake these ones or you just were lucky enough not to get caught out?

**Dave Jones:** I think it was a little bit of both. I think that whoever was supplying our devices at the time were getting them from the horse's mouth. Yep. Uh which was uh Motorola, who then became On Semi. That's right.

**Dave Jones:** Uh for a while we were using some devices, I think EB203 and ED203 from a manufacturer called Hyrel. Oh. Uh China Sorry, Japanese, I believe. Mhm. They were the moral equivalents of these fellows here. Similar bandwidth, similar voltage, similar current, similar gain structure, yada yada yada. Uh all same poo.

**Dave Jones:** Got it? Um So, that's the you know That's the power amp section. Second Uh what else have we got? Another power amplifier, oddly enough. Uh incidentally, you will see here that uh this output rail comes down here through a big coupling capacitor, 470 mark, into our output transformer.

**Dave Jones:** Mhm. The output transformer Well, look, if you if you're that desperate, yes, you can trace through all of this relay line but who cares? Uh one of the items that you might be interested in having a look at, though, is that op amp there.

**Dave Jones:** I was going to ask about that one, yes. Okay, it's having a sniff of signal going into the VAS, the voltage amplifier stage. Now, while ever the power amplifier is acting within closed-loop conditions, Mhm. there's going to be very, very little signal there.

**Dave Jones:** Yeah. But, as soon as it falls out of closed-loop conditions, due to either clipping or short-circuit limiting, or uh well, actually, those are the two main conditions, clipping and short-circuit limiting. Uh there's going to be a lot of signal appears there.

**Dave Jones:** Amplifier, put it through a rather crude half-wave rectifier, uh feed it down into that LED there, and you've got a short-circuit indicator. Clip LED. Yep. Bingo. Too easy. Duplicated over here. Yep. Too crude, too easy, too simple. Yep.

**Dave Jones:** So, is this second stage an absolute duplicate of the first? Looks almost identical. Almost identical. The main difference is, whereas this one had one pair of output transistors. there we go. We've got a couple. This one's got Well, actually, we've got this time This one had little pre-drivers, little drivers, big outputs.

**Dave Jones:** Here, we've got little pre-drivers, big drivers, and big outputs. Got it. And part of the reason for that is where we were actually configured the big drivers to contribute a fair bit to directly to the output. And you've got a a couple of four of one in four double O sevens on the output.

**Dave Jones:** Yeah. The reason for those is if the VI limiting kicks in while the amplifier is driving a heavily inductive load, well, let's face it, inductors hate to have the current to them interrupted. You try and interrupt the current to an inductor, and the voltage is going to fly to one way or another. So, we catch that to either the positive rail or to ground.

**Dave Jones:** The diodes don't have to be particularly huge because the amount of energy involved isn't particularly high. No, that's right. So, even they Let's face it, we've got some 50 amps worth of output device here. We've got one amp worth of diode there.

**Dave Jones:** And it suffices. Yeah, fine and dandy. Yeah. Right. Uh another little bit of circuitry over here. We've got an LM35 temperature sensor, which is a fundamental part of the heat sink. We're sniffing its temperature. When it gets to 80°, in other words, if ventilation's really sadly blocked off for some reason, if the heat sink gets to 80°, we mute the PA system.

**Dave Jones:** Got it. But we let the intercom system keep on going until it hits some 85°, and at that stage, we decide okay, enough is enough, let's kill the whole shooting match. Got it. So, we've got a progressive shutdown.

**Dave Jones:** Down. Yeah. That's rather clever. Uh well, this is the if you like the the pre-ampy signal steeringy bit. Yeah. These are where all of the various switches, you know, the guard's intercom switch, driver's intercom switch. These are the switch contacts.

**Dave Jones:** They're duty great big industrial push buttons. Nothing fine or dainty about these. So, we wanted to have quite high uh voltage switching levels on these. So, we pull those switch contacts high to plus 120 V with 47 K resistors and we switch those to ground with the actual switches.

**Dave Jones:** Yeah. Uh we then use the transistors within ULN2003s Series. uh to detect what the level there is, whether it's high, low, or indifferent, and to act as drivers. These are Darlington pair drivers. That's right. We're simply using them as uh transistors.

**Dave Jones:** Logic input buffers, really. Yeah, logic trans- logic level translators, maybe. Yeah. 120 V to 5 V logic translators. Look, call them what you will. Okay. Overkill again, though. Okay, gross overkill, but it means that we can have kilovolt transients on those lines and it doesn't matter. Nothing dies. Yeah.

**Dave Jones:** Okay, we've even got a bit of switch debouncing in there. Yeah, not a whole lot, but enough. Terrific. Now comes the ugly bit where we get all of those 5 V logic levels and we feed them into the gate array logic chips, called our little Yeah, okay, dismal fail.

**Dave Jones:** Uh Disappointing you, Doug. Oh, shush. Uh including analog man. Yeah. Uh mind you, between you and me and the gatepost, I was dragged into this side of things kicking and screaming. And in fact, it was I think Peter Godwin at Jands who did the logic, uh, uh, what do you call it? The logic equations required for these and programmed them in.

**Dave Jones:** Got it. Yeah. Um, okay, including we've got a an oscillator over here which we tune up to 50 kHz. Oh, LM567. Yep. Uh, now you can use these LM567s as either, uh, oscillators Mhm. or down here as a tone decoder.

**Dave Jones:** A sniffer. They are 567 is the classic tone decoder IC. Mhm. That's what it's famous for. We also use them as a precision oscillator. There you go. Um, getting these amplifiers back, you know, 18 and 20 years after manufacture, we discover, for example, that the 50 kHz oscillators have maybe drifted 250 Hz, 200 Hz, 300 Hz over that period of time.

**Dave Jones:** Is that a drama? No. Because the tone decoder can capture it has a wider capture bandwidth than that. Yeah. But, uh, that's a incredibly small range and generally not due to chip drift, but of course due to capacitor and resistor drift.

**Dave Jones:** Yep. Okay. Now, that's all the boring bit. Now, let's come over here to what happens at each of our various inputs. The inputs are balanced Mhm. configuration so that they reject common mode noise and only respond to differential input which is exactly what you want.

**Dave Jones:** Okay, we've got bridge rectifiers here so that extreme transients present there just get clamped to the supply rails through the bridge rectifier. Balanced amplifier. Now, in these early versions, God help us, We're using JFETs for audio switching. And guys JFETs or anything anymore, do they?

**Dave Jones:** Uh yes. Yes. Name a niche. Uh one of the best possible niches is, of course, the uh input buffer amplifiers to condenser microphones. Yeah. Uh condenser microphone preamplifiers where you want staggeringly low leakage currents and staggeringly high input impedances and staggeringly low parasitic capacitances.

**Dave Jones:** Got it. And that's what I did for cross-the-road microphones. Mhm. Either that 'nother story. Yeah. Either that or I used JFETs with pilot light, also known as like triodes. Tubes. Yeah, tubes. Tubes. No, tubes. Tubes with a c h.

**Dave Jones:** Yes, c h w o b s, tubes. Oh boy. So, okay. We're audio switching there with JFETs and spitting them out into the two mixing amps to go out of the two power amplifiers. Uh well That's it. Uh and the only the only particularly interesting thing here is where we're getting the uh uh the intercom line doing a whole stack of high pass and low pass filtering and buffering and then sending it into this detector 425 kilohertz.

**Dave Jones:** That's our That's our tone decoder. Yep. His output then goes back into the Gator Eye Logic chip, so Right. That's your lot. That's it. That's it. That is the Sydney Rail What is it? What's it called? It's a PA It's a PA crew intercom amplifier.

**Dave Jones:** PA crew intercom amplifier for Sydney Rail. Everyone hates Sydney Rail. Yeah. And not only that, but apparently there've been court cases brought recently to State Rail because of the paucity of PA announcements. Uh there's Poor cases. Some people didn't Some Some lawyer missed his stop and decided to sue them.

**Dave Jones:** No, some uh blind fellow Oh. sight impaired uh has He's been catching the train for decades and he's got the ear of because quite often they just don't bother announcing They just skip them and Yeah. And being blind, he's got no real way of looking out the window to see where he's at.

**Dave Jones:** Fair call. Yeah. And look, good on him. Oh, look, I want to see these things used more.

**Dave Jones:** Next up, Stan Laurel. Come on, Doug. You must cop it all the time. the doors, please. The announcements are so bad. Enunciation, please, guys. Enunciation. Ah. Thanks, Dougie. Yeah. Speak like I say you should, not the way I speak.

**Dave Jones:** That's it. That was an interesting teardown. Okay. Well, maybe you'll somebody will bring in something else vaguely industrial in nature for you to have a look at one day. Sweet. Put the word out. Catch you later. Bye-bye.
