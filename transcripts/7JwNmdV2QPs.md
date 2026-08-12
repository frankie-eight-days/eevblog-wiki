---
video_id: 7JwNmdV2QPs
title: EEVblog #897 - Radiation Effects On Space Electronics
url: https://www.youtube.com/watch?v=7JwNmdV2QPs
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 22, "3": 33, "4": 50, "5": 61, "6": 71, "7": 82, "8": 92, "9": 106, "10": 119, "11": 133, "12": 143, "13": 158, "14": 165, "15": 174, "16": 188, "17": 200, "18": 217, "19": 227, "20": 239, "21": 250, "22": 261, "23": 271, "24": 287, "25": 297, "26": 305, "27": 320, "28": 335, "29": 347, "30": 364, "31": 374, "32": 383, "33": 394, "34": 402, "35": 424, "36": 443, "37": 453, "38": 476, "39": 489, "40": 513, "41": 527, "42": 540, "43": 553, "44": 567, "45": 576, "46": 586, "47": 600, "48": 608, "49": 620, "50": 629, "51": 640, "52": 658, "53": 670, "54": 683, "55": 690, "56": 697, "57": 708, "58": 721, "59": 733, "60": 749, "61": 761, "62": 770, "63": 788, "64": 800, "65": 814, "66": 822, "67": 832, "68": 843, "69": 854, "70": 863, "71": 873, "72": 882, "73": 896, "74": 912, "75": 923, "76": 934, "77": 943, "78": 958, "79": 970, "80": 983, "81": 990, "82": 1010, "83": 1019, "84": 1031, "85": 1042, "86": 1055, "87": 1067, "88": 1077, "89": 1093, "90": 1103, "91": 1119, "92": 1128, "93": 1138, "94": 1149, "95": 1163, "96": 1174, "97": 1184, "98": 1192, "99": 1201, "100": 1212, "101": 1225, "102": 1238, "103": 1247, "104": 1257, "105": 1271, "106": 1283, "107": 1296, "108": 1307, "109": 1322}
---

**Dave Jones:** We've got Carson again from the Google Lunar PT scientist. Yes. Yes. And we're going to talk about space electronics and what makes it hard. What makes it hard? Yeah, so my electronics in space.

**Dave Jones:** It's not just launching them in the vibration of the rocket and everything else. No, we're not talking about that. Yeah, so this is actually the easy part, I guess.

**Dave Jones:** Um Yeah, right. The easy part is launching it and landing it and all that. Yeah, so so when you're when you're talking about electronics in space, it's not like um the ship knows uh oh now I'm in space, I'm no I will break, you know.

**Dave Jones:** This is not the point. The thing is that um when you're going into space, you're um you're leaving the um the atmosphere which uh which is providing you with sufficient shielding from the radiation environment that uh that the sun and uh the radiation radiation are there?

**Dave Jones:** So, there are um so it depends on where you are. So, if you're uh for example, if you are a CubeSat fan, then you know that there is the lower Earth orbit which is about 300 to 800 km.

**Dave Jones:** And uh in that um you um you have the inner belt of the Van Allen belt. Yeah, so the inner belt is uh dominated by protons. So, they um you know, they they make all kind of uh crazy stuff.

**Dave Jones:** For example, so there if you're if you think about space, there are two things that you have to take care of. It's uh it's called the total dose and uh it's called the single event effects.

**Dave Jones:** Yep. This total dose is um is something that um you're Total dose of radiation we're talking of. Yeah, exactly. Yep. Um it's uh you can think of it as a as a gradual effect.

**Dave Jones:** So, you have your uh NPN junctions and um there are um ions coming in and they are manipulating the doping of the of the They're interacting with the doping of the silicon.

**Dave Jones:** Exactly. And And this leads, for example, to the effect that um that your transistors don't uh switch as fast anymore. Um that you're Okay, so it starts to dis- degrade the transistors performance.

**Dave Jones:** Yes, it does so it does so gradually. Right, how gradually we talking about? Uh well Can it be destroyed in days depending on the feature size? Well, yeah it depends on it depends on actually the the protection that you have.

**Dave Jones:** So if you have absolutely zero protection Right. Um So if you've got So if you've got your Arduino board just flapping around in the breeze in space Um that's interesting.

**Dave Jones:** I would have to check on how quickly that would be dead but Um the good thing about the total dose is that you can add shielding. Right. So what you're doing is usually you you add some aluminum or if you want to go fancy you you add some tantalum.

**Dave Jones:** How thick does it have to be? So this is the this is the question. How thick has it to be to survive your mission? And this depends on what your mission is.

**Dave Jones:** So you can calculate all this and that will obviously determine oh I need an inch worth because I'm going into deep space for 10 months. So I need Exactly.

**Dave Jones:** So but the thing is that an inch for example doesn't doesn't do much more than than half an inch. You got it. So it's it's the you know first tens of a millimeter that helps you a lot.

**Dave Jones:** Yep. And you know a millimeter is quite good. The mini sheen returns. Yeah and 1 cm is if you want to go really fancy you know. So Um And so it depends on what your what your mission duration is like.

**Dave Jones:** So it's also So if you want to make a um a five-year orbit in Leo then you can expect about 20 kilorad which is the unit for measuring the deposited dose in the silicon.

**Dave Jones:** And um then you can then you need to figure out what what shielding you need to add to to get to that point. Well well you wouldn't want to design on the limit of that.

**Dave Jones:** You want to be Yeah, well yeah. order magnitude under. Is there a rule of thumb for That's That's a good question. Yeah, you you What your margin depends on what your margin policy is.

**Dave Jones:** You know, if you The thing is that if you want to Um you can you can be very safe and very very expensive. Yep. Or you can be cheap and do lots of stuff.

**Dave Jones:** So, you can be Voyager 1 and 2. Cost is no object. Apollo 11 cost is no object. You know, let's just do it right and reliable. Yeah, exactly. Or you can go, "Ah, no worries.

**Dave Jones:** She'll be right." Yeah, so yeah, but the thing is that for example, this is a very valid policy that we are for example adopting that um uh you say we want to do as many missions as possible.

**Dave Jones:** And uh so for example, CubeSats uh I think that the price is about um $10,000 per one unit. unit, yep. Yeah, and so um you can say, "Okay, well, no matter I will fly 10 and there is a chance that after 3 years half of them are dead."

**Dave Jones:** Yep. And this could be a very valid, you know, They could be perfectly happy. Because if you if you if you try to add the shielding, um your mass increases and your size increases and Yeah, no longer a CubeSat.

**Dave Jones:** Exactly. And so this is this is a the philosophy that you um that you have to you know, think about what your what your aim for the mission is.

**Dave Jones:** And the total dose is actually the the part where it's where it's quite easy because you just you just add um your um uh your shielding depending on how much total dose your device can stand.

**Dave Jones:** So, now is this something you get in the data sheet? Uh well, not in the regular data sheet. No, but you can ask them for aerospace grade. Yeah, for you know, for space grade for example, they they if you want to something is the the space grade, they have to do some radiation testing and tell you the total dose.

**Dave Jones:** Yep. There are but there are also many um you know, many people around the world that do some testing. So, it's for example, it's quite easy to get um to get a mini um cobalt 60 Yeah, right.

**Dave Jones:** uh thing and put it on it and then you Yep. you get a very vague idea of um Right. of how how well it goes and uh what you can also do is a proper radiation source and do some total dose testing for the mission duration that you're aiming at and the and add the shielding to provide the length um You got it.

**Dave Jones:** How do they radiation harden the chip? You buy the normal version and you buy a radiation hardened version. What's the difference? The paperwork. So the the paperwork, is that it?

**Dave Jones:** No, it's not. You know, it's It's a bit of a bit of a it for It's a bit of a simplification, but the thing is that But there's nothing physically different.

**Dave Jones:** Yeah, it depends. Sometimes it is, sometimes it's not. Right. Sometimes Well, obviously they've tested them and they've sorted out that maybe this one is a good one. Well, they can't test it cuz it's fatal dose.

**Dave Jones:** Yeah, yeah, yeah. So what you what you do is you take you take one wafer. wafer bombard half of them and then Yeah, well, half would be very generous.

**Dave Jones:** Okay, you bombard a few of them. Yeah, you take like like a significant sample size like five to seven for example and you then you do some radiation testing with it and then you have a very rough idea of what the status of the other ones is and then you know, if you if you're talking about proper proper space grade stuff, then you also do hermetic sealing packaging,

**Dave Jones:** you know, with with all the fancy stuff. You add some shielding and do all the fancy bits and then you know, you have a chip that will will definitely work in a radiation environment up to the total dose that you're um supplying it, but also it depends on the on the process that that something is manufactured in.

**Dave Jones:** So some I was going to say feature size makes a huge difference. If you're working if you're on a leading edge FPGA at 20 nanometers or something. This is This is where it gets very interesting.

**Dave Jones:** The feature size does not make a huge difference. make a huge difference. No. So but for example, what it what it's So but if you if you're talking about doping before which comes in the process technology not just features yes but the thing is that if you want to for example build it a smaller process then you need to have a tighter control of all parameters and so you know this can

**Dave Jones:** this can actually for example if you look at some of the single event effects which we come to in a second then you see that and then a smaller process does not lead to higher single event upset rate which means bit flip essentially.

**Dave Jones:** Interesting. Coming back to the total dose. Yeah. So this is this is for example influenced by how thick your layers are. Also if you are talking about you know finfet technology you know it's the transistors are made entirely different than and if you have a bipolar process if you have a bulk if you have bulk CMOS if you have silicon on insulator this all comes into play into what your total

**Dave Jones:** dose is and sometimes sometimes it's really just that one batch is bad whereas another one could be We've got the total dose which can slowly kill your chip. Oh well Which you can shield against which is good Which you can shield against.

**Dave Jones:** In in which ways? There's So you can you can add foil Aluminum is there any other materials that work better? Tantalum is one of the preferred ones so you use Titanium Tantalum Tit Wait is it tantalum?

**Dave Jones:** No wait. Uh It's a German accent. Uh I would have to look it up what's called. Okay. Uh All right but there is a material that is better is a better So it's a usually it's used in a composition with aluminum.

**Dave Jones:** So you have a little layer of the other the other one so this can help you up to a certain thickness you get because you get diminishing returns Diminishing returns on the thickness yeah okay.

**Dave Jones:** So you can do some shielding with that. Now just one more thing on the total dose the data sheet says it'll survive up to this dose. What does that mean?

**Dave Jones:** It'll still function to all the specs up to that dose? Yeah, this could be another way. not guaranteed. Yeah. But you don't know what specs will fail, do you?

**Dave Jones:** Exactly. You just it it's just don't go there. Yeah. just cross your fingers and This is for example one of the why some of these space grade stuff is is lower weighted in frequency for example than than the regular commercial part.

**Dave Jones:** All right, single uh single event. Single event Yeah, so there's a whole group of what's called single event effects. And where do they Where is Where is the source for the total dose radiation?

**Dave Jones:** Is this What What sort of space radiation is it? Where's it coming from? So there's those are the the low energy electrons mostly and So they're the cosmic rays?

**Dave Jones:** Uh no, the cosmic rays are coming from outside the solar system. Oh, so we're talking about solar the sun. Yeah. Radiation from the sun. Okay. Right. Essentially, yeah. Got it.

**Dave Jones:** And um Is that for both the for for the dose and for the single event? So radiation? Yeah. So the um the So it depends on what you're talking about.

**Dave Jones:** There you are. So So you have the the sun which provides you with plenty of protons and some ions. Yep. Um and then it gets trapped in the Van Allen belt and then you get some some electrons which are trapped there and the protons.

**Dave Jones:** of Yeah. particles flowing around and if you're flying in that or through it, then you're Then you have to deal with it. You have to deal with it. And there's also an interesting spot on Earth which is called the South Atlantic Anomaly.

**Dave Jones:** Which if you fly through there is a collection of what was it? Protons, I guess. Um Interesting. Yeah. So it's a in the in the northeast of South America.

**Dave Jones:** Very interesting. There you go. So you don't want to live there. Yeah. No. No. So all right. Yeah, so we we don't we don't attempt to fly through that.

**Dave Jones:** Okay. Excellent. Anyway. Right. So the single So the single event effects are uh is a group of um of effects that you can have with uh with high energy particles.

**Dave Jones:** So Cosmic you know we're talking about cosmic rays. When people think of space radiation, they probably think of cosmic rays. Oh, and my phone just stopped working. Must be a cosmic ray, bit flip, you know.

**Dave Jones:** Yeah, yeah, yeah. But but the actually the sun produces some high energy particles as well. Okay, all right. Got it. There's there's a good source as well. So you have to use low energy particles which are for total dose and the high energy particles It's the energy difference which differentiates the two types.

**Dave Jones:** Got it. And the single event effects are um you have the uh single event latch-up which is um that uh something like that. Yeah. Yeah. Uh SCR latch-up will typically destroy your chip.

**Dave Jones:** Uh it depends on how quickly you're able to to uh to switch it off for example. switch it off. Okay. Yeah, so you have the um you have the latch-up if you so which can destroy your the transistor for example if you're not switching it off uh quickly enough and you not you need to switch it off and remove the energy as well.

**Dave Jones:** Yes. Um so not just switch it off but really put it to ground uh so to speak. And um Which is why filtering on your power supply can be bad because it's got a lot of energy in the bypassing and it can keep dumping energy.

**Dave Jones:** And if you're all switched off my power supply, no you haven't. All your bypassing is still supplying a big gulp of energy that can destroy your transistor. Yeah. Exactly.

**Dave Jones:** Yeah. And uh so that is um that is one source and uh the the interesting thing about the single event latch-up is that if your um if your process for example allows for a lower voltage, you're less expectable to um so single event latch-up.

**Dave Jones:** You're less susceptible. Yes. I would have thought lower voltage would be worse. No, it's not. No, it's not. Interesting. And so some of the newer processes are uh less expectable to single event latch-ups than the previous ones.

**Dave Jones:** And also at 1.1 volts or 0.8 volts core voltage or is stupid. And uh silicon on insulators are for example also um uh very immune to that. So this is a very very rough thing.

**Dave Jones:** Right, so it can cause latch up. What's the next problem? Bit flipping. Yeah, bit flipping is also it's called bit flipping is called single event upset. There are soft and hard single event upsets.

**Dave Jones:** So the soft one is um uh you have a you have a memory cell and um instead of a one you're reading a a zero or the other way around.

**Dave Jones:** And if you write over it and it's uh it's re-backed to normal and the hard single event upset is um you cannot write to it for you know, it's it's get stuck for a time.

**Dave Jones:** Sometimes it anneals. Okay. But uh yeah, so you have to but dealing with the soft single event upsets this is where where stuff gets really interesting because this is what everyone is afraid of in it.

**Dave Jones:** Everyone's afraid. You've got this big die which is your DDR3 memory or whatever it is and it's got it's a massive die, big square area because it's a random event.

**Dave Jones:** Bigger the square area of the die, the more chance you have of getting hit, right? And because it's big memory array, something's going to get hit. How do you deal with it?

**Dave Jones:** Yeah, so this is where where you start to choose some of the processes for example that have ECC uh error correction or EDAC which is that you read and correct it.

**Dave Jones:** You can But what if the error correcting circuitry gets hit? You're screwed. Yeah. Yeah, well space is hard. But the thing is that it's a small area compared to the memories for example.

**Dave Jones:** Yeah, but Murphy will get you every time. Yeah. The thing is that about single event upset is that you can you know, you can um deal with it and by by having error corrections or by having TMR which means that double redundant triple modular redundancy.

**Dave Jones:** For example, if you have a in a in a processor you have a register you have then three registers and then you do majority voting. Exactly. And and take this one and um this is how you have to do it.

**Dave Jones:** any of that in here? Um, so we this is why for example we are using the SmartFusion2 which you have cuz the processor is actually having uh EDAC for the the memory interface.

**Dave Jones:** Oh, it does. It's got to build in. Okay, so there's features there that And and in the in the FPGA area has has some ECC going on. Okay. Um, uh so this is your parity.

**Dave Jones:** Hm. Some some error correction. Okay. Uh the the thing is that uh with PSH I can do some testing about the radiation effects of the IP cores that we're developing and so we can take care of that.

**Dave Jones:** The thing is that um you have a big area and uh with with for example many registers and you have to know which bit is actually important. You know, not all bits are created equal.

**Dave Jones:** No, that's right. Some are more important than others. Yeah, some of them are junk and so you don't care about if they are flipped. Exactly. And so you have to you have to know which which of the bits are for example in the control path which are in the data path.

**Dave Jones:** You know, in the in the data you know it doesn't matter if there is a instead of a 127 you're encoding a 128 in the in a in an image.

**Dave Jones:** You know, no one notice. Yep. But uh in the control path you know it makes a difference between turning left and turning right. Yep. So you need to um you need to make a decision on which parts you want to um TMR to make them uh uh redundant against the single event upsets and which parts uh you can just ignore for example.

**Dave Jones:** Dosage and single event. Is there anything else? Yeah, so you have to from a single event you also have the single event transient which is when you are um having a spike uh in the uh in the path for example.

**Dave Jones:** This there's not much you can do with it. No, right. It's so you can have to deal with it on the on the TMR level for example. And and you've got some software the European Space Agency Oh yeah, so has written some software.

**Dave Jones:** Oh yeah, so yeah, so this Do this sort of stuff. Yeah, so that if you want to um there is uh software called SPENVIS which is uh the uh space environment blah blah blah.

**Dave Jones:** Can anyone download this? This is a website really just you can just go there you can register All right. you you enter your your orbit and um then you can take a look and see what you get out of it.

**Dave Jones:** And you can you can calculate for example a single event upset rate. Interesting. Yeah. And it'll give you recommendations for different materials for thicknesses? No, no you don't. No, you you have You're on your own.

**Dave Jones:** Okay, got it. So, what are you most concerned about passing through the Van Allen belt? Yeah, the Van Allen belt is the main thing on the ISS. the how big is the how long do you spend in the Van Allen belt?

**Dave Jones:** Not long. So, this is a good news. Yeah, right. Um, oh by the way, um, from from a total dose perspective, there's also some annealing effects. So, once you accumulated some you know, when you're passing through the Van Allen belt for example, you accumulated some dosage.

**Dave Jones:** And some of it will anneal depending on the temperature and the biasing you do. Interesting. and also total dose that gets deposited also depends on whether the the chip for example was was biased.

**Dave Jones:** So, if if you are running some application with a high frequency, it's more chance to accumulate more dosage than it is when it's switched off. Interesting. Pesky physics, pesky silicon physics and all that rubbish, quantum stuff.

**Dave Jones:** Yeah, yeah, so yeah, so you know the quintessence of it is that um you have to decide on on how much failure you are you are for example willing to accept.

**Dave Jones:** And one of the things that you need to know about SPENVIS for example is the most of the models that are dealing with the solar particles for example are made for solar flares.

**Dave Jones:** That doesn't So, it means that essentially on a on a good day, you could have no trouble at all. Exactly. Solar flare comes up, you're screwed. Because you don't want to design That won't be one of your risk factors, right?

**Dave Jones:** You go, well, we have a one in 50 chance of a solar flare. We're not going to add 20 kilos weight to But but it may for example it may be your requirement if you're flying a mission that lasts 20 years.

**Dave Jones:** Exactly. You have to Exactly. a solar flare are almost 100%. Yeah. That's right. Yeah, but if for example for our mission duration, um you know, we are not expecting any any solar flares.

**Dave Jones:** Um and this is some of the trade-offs we have decided early on that um uh we are designing as good as we can, but if we have a solar flare, we are and we know that.

**Dave Jones:** So, you wouldn't be much the rover through the Van Allen Allen belt, would you? Because I assume it's just powered down. Yeah. And it'd be it wouldn't be doing anything.

**Dave Jones:** So, you get get some dosage, but you're going to survive that, right? That that it's always a given. You can always guarantee that. Yeah, well, so yeah, if you're it depends on how often you pass through it, you know.

**Dave Jones:** So, it depends on this depends on your trajectory. Oh, yes, of course. Yes, because you don't People think you just shoot straight off Earth like that. You do you like straight up.

**Dave Jones:** No, you Yeah, so so for example one of the early trajectories we had was you know, circularizing about five times. Five orbits? Yeah, five orbits and um And then do a translunar injection.

**Dave Jones:** And yep, I know all the translunar injection. I'm a space buff. Yes, thank you very much. Is it a three-part system? Cuz you got the rover, Mhm. you've got the uh lander, Yeah.

**Dave Jones:** but you've got the ship that takes it there. Or is the lander that the lander is the ship? Right, so the lander is the spacecraft that takes it there.

**Dave Jones:** Is that all we need to know about surviving space? Well, yeah, if you So, if you want to survive space, you for example it's it's good way to start with CubeSat stuff and uh yep.

**Dave Jones:** Go on from that. So, radiation is much bigger problem than thermal. Yeah, the thing is that you know, with thermal it's quite easy. You know how much wattage a chip dissipates and you need to get rid of it.

**Dave Jones:** Yep. but what you really can't tell is how much dosage a chip is able to handle without you making radiation tests. But that's why you buy space grade and that's what you're paying for.

**Dave Jones:** Yes. Well, yeah, there is uh yeah. Maybe it's been tested and you've got some data. You know you know how bad it is. Yeah, exactly. It doesn't you know, space grade is so you can buy There's a difference between radiation hardened and radiation tolerant, by the way.

**Dave Jones:** Oh, yes, there is. And radiation tolerant is a is a is usually designed for you know, lower dosage um Right. and so for CubeSats stuff, for example. cheaper stuff.

**Dave Jones:** Yeah, and radiation hardened is really for deep space missions that are geostationary satellites which last for many many years. 20 years or something like that. Yeah, but usually so it's uh occasionally it's it's a bit of a rip-off because you you just get the same chip You say yeah, exactly.

**Dave Jones:** With a different test report. with a yeah, with a different test report, you know, as So That's brilliant.
