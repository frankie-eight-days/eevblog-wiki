---
video_id: IpI-cGU6-FY
title: EEVblog #1104 - Omicron Labs Bode 100 Teardown
url: https://www.youtube.com/watch?v=IpI-cGU6-FY
source: youtube-asr
timestamps: {"0": 0, "1": 35, "2": 78, "3": 90, "4": 111, "5": 144, "6": 166, "7": 201, "8": 218, "9": 248, "10": 271, "11": 299, "12": 320, "13": 347, "14": 385, "15": 412, "16": 434, "17": 455, "18": 478, "19": 502, "20": 519, "21": 537, "22": 571, "23": 586, "24": 603, "25": 639, "26": 660, "27": 701, "28": 718, "29": 748, "30": 784, "31": 808, "32": 833, "33": 869, "34": 901, "35": 932, "36": 965, "37": 1002, "38": 1031, "39": 1056}
---

**Dave Jones:** Hi, in a previous video, which I'll link in down below and at the end, we took a look at this Omicron Lab Bode 100 frequency response analyzer / vector network analyzer. Whatever you want to call it. It's brilliant. But, let's do a teardown of this puppy to see what's inside and also this wideband injection transformer as well. We're talking about $5,500 worth of kit and a What is it? A $500 wideband injection transformer worth every cent. So, these things are not cheap. They are professional bits of kit

**Dave Jones:** for power supply analysis, component analysis, basically anywhere from almost DC up to 50 MHz. So, this is supposed to have a 24-bit superheterodyne receiver in it and all sorts of awesome stuff. I want to do this first. So, we've got the Hz to 10 MHz wideband injection transformer. It's just a one-to-one transformer, 600 V CAT II isolation, just BNC input, just the earth terminal, which is it'd just be the outer case here, and just banana plugs and balanced output on this side, isolated. So, let's take a look. Now, these things are

**Dave Jones:** you know, there's not many of these on the market, these wideband injection transformers, cuz they need a really wide bandwidth. I mean, to go to 1 MHz to 10 MHz, and this thing's almost ruler flat over that 1 Hz to 10 MHz range.

**Dave Jones:** It's absolutely amazing performance. And as far as I'm aware, there's no off-the-shelf transformer that does this. So, this is no doubt going to have some custom-made transformer in it. In this case, probably wound by nude virgins in Austria, no doubt. So, let's check it out. Hopefully, they haven't potted this thing.

**Dave Jones:** So, that's my fear is that they're trying to protect their secrets cuz as far as I'm aware, like you can't really buy an off-the-shelf wideband injection transformer for less than 500 bucks. So, you know, you're paying paying 500 bucks for a transformer, which sounds like a lot, but try and get this sort of performance yourself, and you'd spend a month of Sundays around experimenting trying to get it just right with your tongue at the right angle.

**Dave Jones:** And let's have a look. HERE WE GO. OH, HELLO. Thank you, Omicron Labs, for not potting this baby. Look at that. It looks very simplistic, doesn't it? They've got a core in there, and they've just got uh in this case, here we go.

**Dave Jones:** We've just got the uh twisted pair. I don't know what's inside that. Is that some sort of they've they've celastic that under there. Not sure if we're going to be able to see in there. Is that some sort of uh magnetic voodoo just to take the edge off something, or is that some sort of uh protection, perhaps? I'm not entirely sure. Hmm. Anyway, we've got a uh no doubt uh choice uh ferrite ring in there with just uh twi- in this case uh twisted pair here and here. Yeah, they

**Dave Jones:** actually look, they mix, you know, they mix up the output and the input and wind them like that. I don't know. If any I don't know my winding transformer terminology names. If If you know what that particular uh technique is called, then uh please leave it in the comments.

**Dave Jones:** But, there you go. That is a 500 buck wideband injection transformer. But, as I said, it is hand-wound by nude virgins, and it is tweaked and characterized and performance characterized uh to get that flat response. And as far as I'm aware, there's no off-the-shelf transformer which will meet, um, this sort of spec. And I don't think that's actually, uh, Litz wire or anything special like that. I think that's just, uh, solid core.

**Dave Jones:** Correct me if I'm wrong, but that's probably just, uh, you know, a single strand, uh, solid core wire. And sorry to break it to you, but, uh, that's not some weird ass, uh, magnetic voodoo in there. It is a fuse and they've just soldered, uh, the wire directly onto the end cap. Um, that's pretty how you do it. What, they couldn't do an inline, uh, holder?

**Dave Jones:** Anyway, that looks like it's a, uh, ceramic fuse and these things which I thought were some magnetic voodoo uh, just cable ties. Anyway, it is, uh, constructed with care and, uh, I like how it's on the, uh, rubber in the bottom and that just, uh, squishes wedges between that. So, it's not going to flap around in the breeze in there. So, there you go. If you don't think that's worth, uh, 500 bucks, then, uh, I guarantee you could, uh, corner the market with a low-cost wideband

**Dave Jones:** injection transformer. If you could sell one for 100 bucks, everyone would want one. And, uh, for, you know, power supply, uh, injection testing and stuff like that. And if you can do it and get similar performance to this, go for it. Now, for this bad boy, the Bode 100. Let's go. Again, made in Austria. Hi to all my Austrian viewers.

**Dave Jones:** Brilliant. There's the back panel. That's very nice. Um, that's just the, uh, ground earthing, uh, thing for the entire, well, it's not earthing because it's, uh, not mains earth because it's a uses a floating, uh, plug pack supply input, but it does, uh, ground the entire case. So, just two screws on here. It's in a beautiful case. I love this. Oh, you ready for it? Oh, metal cans. They're not soldered, so we We lift the lid on those babies.

**Dave Jones:** I ju- Geez, that's a bit naked, isn't it? All the magic's happening in the cans. Ah, we're in like Flynn. Our Terra Cyclone 4. So, yeah. All the magic's in the tin. But, oh jeez. That's not your regular FR4 uh class PCB. That's some, you know, uh controlled uh dielectric uh Rogers special. There we go. That might be able to give us some input into the type of PCB, perhaps. Uh H4M blah blah. That's quite a nice uh DC-to-DC converter section. Uh all Rubicon caps down in

**Dave Jones:** here. You know, I won't go into detail, but uh that's what you expect on the input. Um so, what is it? We've got a 19-V uh sorry, 9-to-24-V uh DC. So, it's a wide-range uh input uh nominal 10 W. So, anyway, like I don't think it'd use 10 W uh driving this thing. Then, we've got some more uh local regulation right next to the metal can. We've got a uh 10-pin header there.

**Dave Jones:** So, that's probably some sort of uh programming type thing. We've got duplicate uh circuitry up here for the next can, but we don't have that for the top can because uh you expect these two cans to be identical cuz they're both the uh receivers. They're They should be identical uh receiver channels. You know I'm a reed relay fanboy.

**Dave Jones:** What have we got down in there? Is that a meter? Sweet. So, that's obviously uh design- You can see the traces going in. I think that's obviously uh designed to um join the two channels together uh that internal uh the switching. So, obviously, it's at a non-critical point where they can go outside the can.

**Dave Jones:** Mm, we've got some sort of filtery doodad going on in here. Look, some sort of multi-stage uh filter. We've got jumpers. Don't know what that is. Another little header, some sort of test. I doubt it's a programming header, maybe just a yeah, do some production testing, something like that. Oh, what's that? It's an Analog Devices baby. And that's an AD9851.

**Dave Jones:** There's our DDS generator for our 50 MHz waveform output. So, that's got a 10-bit DAC in it, no worries. So, that'll do the business for generating your test waveform, no problems. And next to it, no, that's not an Analog Devices even though it's got AD245. I think that's just a like a 74AC series 245 TTL chip.

**Dave Jones:** And after that, we move through this filter we do that section into an AD8007. That's a high-speed amp, basically. So, like 600 meg or something like that. So, yeah, that'll do the business. And there's our little crystal in there.

**Dave Jones:** Ah. It's teeny tot, but apparently this has a 2 ppm class reference oscillator in it. So, that would be pretty schmick. Who'd have wanted to be for the money? And the processor section, well, Altera Cyclone IV with some memory attached.

**Dave Jones:** It's not the least bit special, so I'm not going to go into details there, but looks like, you know, we might have a JTAG header up the top here somewhere. Um, yeah, I don't know. There's a FTDI USB driver. Meh. So, that's just basically sampling, you know, buffer and then just dumping it out to the USB port because there's no real processing done on this thing. It's just basically our control and data buffering and sampling, stuff like that. And here's what we've come here to see. This is our source.

**Dave Jones:** So, this will also contain Well, no, does it it shunts it through to to measure the reflective power. Anyway, let's have a look. Come on. Come on.

**Dave Jones:** We're in like Flynn. Bunch of reed relays and not much else. We've got yet another 809851 upside down so all the electrons are going to fall out. Why have we got a second DDS generator? One inside, one outside.

**Dave Jones:** Mhm. Could that be because I'm just speculating here that they're that they're basically running them synchronized so that one, you know, this one in here is the generator, right? And the actual generator itself for the source output and the other one might be so that the device under test doesn't affect the source and so that they can do the reflection measurement using this one as the phase reference perhaps.

**Dave Jones:** That's That's my first guess. Next to that we've got an ultra precision 80 8676. Special. Don't know what the top job up there is. That doesn't That's just a Probably that looks like a voltage reference. So down here we've got some filtery doohickey going on.

**Dave Jones:** Check that out. Then we've got our six What? Six op amps? What have we got? And these are AD 8170s. These are muxes so I can only presume that they're muxing in different filtering there. These ones up here are 8007s again. Oh, no, only two of those. Two 8007s and one That's just no PA 2277 low noise amp. So anyway, so they're the drivers. Looks like they're the drivers for the output. So then we've got our output protection resistors and six read relays again. They'd just be the

**Dave Jones:** same meter uh model, I'm sure. Yep. I wonder if they're shielded. Have to look up the exact part number on that. All right. Now let's take a look at the receiver. You can see my new camera microphone cable there. Ta-da! Aw!

**Dave Jones:** Anyway, we do have an internal shield. So there's nothing in here except three read read relays, couple of resistors, a few passives, and that's about it. And over here we have just a bunch of well, you know, eight-pin SOs, and that looks like the only thing special in here. That must be our 24-bit ADC. Is it? Or are they implementing that in the Altera Cyclone IV?

**Dave Jones:** Huh. And in case you're wondering, is there any magic on the bottom here? Well, no. It's just some passive, you know, maybe a couple of driver for the relay, stuff like that. But apart from that, no, there's nothing on the bottom. No man behind the curtain. Aw, come on. For five and a half grand, one of the nude virgins assembling this thing can surely clean the flux off. Okay, we've got our AD8007 again, our fast op amp. And this one up here, the AD AD65, that's just a another

**Dave Jones:** 140 meg fast FET op amp. What else? Our AD8170 there is a mux. Then we've got an ultra precision op amp again. Geez. Ooh, something different. Some DG419s. Whenever you see DG like that and the four series, you know it's some sort of like uh analog switch or maxi type thing.

**Dave Jones:** Probably an analog switch. Geez, well they like those, don't they? Um What's that? Another 8170 down there? Another 2277. We've seen it before. It's just an op amp and switch fest. Wow. And more over here. That's uh basically all there is to it. Geez, there would have been something interesting.

**Dave Jones:** Here we go. AD S 1271. There's your ADC. And sure enough, that is a 24-bit ADC, but it's only 105K samples per second. So, how do you get the 50 MHz bandwidth? Well, that's where the superheterodyne uh receiver comes in. They actually use an intermediate frequency to get the signal in the particular uh sampling passband for this analog-to-digital converter. So, I'm now thinking, well, look, there's nothing else in there, nothing else doing. Uh what are those two? SO-14s? They look like glue logic or something. So, I'm

**Dave Jones:** now thinking that this um external DDS here might actually be to generate the intermediate frequency so that they can uh down convert and then sample the uh signal in the 100 uh you know, the 100 kHz bandwidth of the ADC. Of course, there's 74HC595s, everyone's favorite. And it goes without saying that the other receiver channel is absolutely identical.

**Dave Jones:** There you go. With just a uh bridge read relay to us join them together. So, that's actually uh very simplistic. I was expecting a lot more in there, but obviously they can get the performance out of this thing by uh you know, superheterodyning the uh main well, at the at each point of the frequency test uh each point of the frequency sweep, they just mix that down to the um ADC in there, the uh sample range at 100 kHz sample range of the 24-bit ADC. That's

**Dave Jones:** how they get the performance and resolution, but of course it takes time to uh do that. And the other thing is I didn't notice any uh directional coupling happening here to actually uh get the uh reflection for the um S uh 11 test. So, for the VNA. So, obviously I think yeah, maybe they're just um using the second um DDS generator here to keep the synchronization and then just switching it back through. And once you you know, once you got the phase, you got that information that the source output here

**Dave Jones:** and like all the load on the source output isn't going to affect or you know, it doesn't matter that it affects uh that because they're genera- generating a second DDS, but then I think they need one for the um They also need it for the uh down conversion as well. So, I'm not sure. Um but yeah, they're obviously pulling this off with you know, a relatively, you know, just basically op-amp you know, high-speed op-amps and switches and uh and so you know, 100 kHz 24-bit ADCs in this thing.

**Dave Jones:** So, that's really quite remarkable. Hats off to Omicron. So, from that point of view, it's you know, it's worthy of the uh price tag you pay for this thing, but yeah, it's not overly complex. I you know, there's obviously not five and a half thousand dollars worth of uh you know, performance magic in here. But as I said before in the review video, you're paying for the you know, the R&D, the engineering, the software, and everything else that uh goes along with that in making this happen. So, there

**Dave Jones:** you go. That's a uh rather um simplistic teardown, how simpler than I was expecting, but anyway, they pull it off. 0 to 50 MHz VNA plus, you know, a frequency response analyzer. Really is quite nice. Anyway, if you like that, please give it a big thumbs up. As always, high-res teardown photos over on eevblog.com and that's it. Discuss.

**Dave Jones:** Catch you next time. Bonus teardown. What's this I think it's 600 bucks worth, isn't it? For this Yeah. That's all you get. But I don't know. Kind of okay, but yeah, definitely done by it. Definitely hand-soldered by nude virgins for that price.
