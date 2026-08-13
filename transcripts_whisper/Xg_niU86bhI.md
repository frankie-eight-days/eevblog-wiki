---
video_id: Xg_niU86bhI
title: Wens 540 Handheld Oscilloscope Multimeter Teardown
url: https://www.youtube.com/watch?v=Xg_niU86bhI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 65, "4": 85, "5": 101, "6": 117, "7": 137, "8": 161, "9": 185, "10": 201, "11": 225, "12": 241, "13": 265, "14": 285, "15": 301, "16": 317, "17": 341, "18": 365, "19": 389, "20": 409, "21": 429, "22": 449, "23": 473, "24": 497, "25": 521, "26": 541, "27": 557, "28": 577, "29": 597, "30": 613, "31": 633, "32": 649, "33": 669, "34": 689, "35": 713, "36": 729, "37": 745, "38": 769, "39": 789, "40": 805, "41": 821}
---

**Dave Jones:** Hi, just a quick second channel video. What I've got here, this is just going to be a single take video, is the Wens 540 debug meter. It's a... well, I'll go to the datasheet. Yes, it is all crusty and whatnot. I can only assume

**Dave Jones:** don't ask me how I come upon this, it's a crusty, like a repair unit or something. It's just scrapped, basically. But I thought, hey, we'd just do a teardown of this thing. And what is it? Well, let's have a quick look. It's actually a

**Dave Jones:** multi-function oscilloscope. Oscilloscope meter, not oscilloscope. They've dropped the O because, well, you know, that's too good for China. Anyway, high performance debug meter. I've done a video of this at the trade show last time. Charles from Triotest actually had this. It was like brand new, released at the time.

**Dave Jones:** Anyway, oscilloscope, a logic analyzer, a protocol analyzer, digital pattern generator, all sorts of, you know, it's a really interesting bit of kit. You can see the custom probes and everything coming over there for the logic analyzer. And it's, you know, graphical multimeter and everything

**Dave Jones:** else. You know, it's like Nomaly Cat 3 600 volts, you know, it's got all your regular multimeter functions, but a big graphical display, and does all logic analyzer type stuff too. So I thought we'd have a squiz at this. Let me go back.

**Dave Jones:** Sorry, I've only got a single capture window here. And let's have a quick look at it. So it's all on one main board here. And if you see the light flicker here, by the way, that is actually my overhead light which is causing the glare issues there.

**Dave Jones:** And it's intermittent. It's actually flickering at the moment. So let's actually start at the input here. I haven't actually looked at this yet. So I thought we'd do it live. And we've got our requisite, the input jacks, you know, they're the split type down the side.

**Dave Jones:** You know, they're A. But yeah, nothing to write home about. We've got our... oh, what is that? What is that? Is that just a cap? Or is that no, that could be a spark? Is that like a spark cap or something? I'm not sure.

**Dave Jones:** That's across the input. Directly across the input like that. SP 101. That's interesting. I'm going to assume that that's a just a spark gap directly across the input. Anyway, we have ourselves a PTC there. Yeah, there it is. It's labeled PTC. Got ourselves an isolation gap under this

**Dave Jones:** resistor here. Is that the current sense resistor for here? I'm not sure. There's an... anyway, two fuses. Whether or not they had HRC in there, I don't know. I don't particularly care. And because, like, you wouldn't use this as an industrial meter or whatever.

**Dave Jones:** It's just not going to happen. No, there are two current sense resistors over here. They look neat. Where's the tap coming out of those? Ah, can't actually see the tap coming off the bottom of there anyway. That's not a four terminal jobby. So yeah, that's interesting.

**Dave Jones:** Hmm. Anyway, no four terminal current sense. Anyway, lots of relays on this puppy. So there's like five relays on this thing. Jeez, like the only other major meter that has relays is like the Gossen one, I think. And it's I don't even think it has that many.

**Dave Jones:** Oh, a couple of little trimmer caps there. And HY 3131 chipset. There you go. Exactly the same chipset that's used in the new HY 3131 GW multimeter, as well as the Keysight U1282A and others. It's quite a nice little chipset. And I like how they've actually laid out the board and

**Dave Jones:** put them in the section. So they've got the multimeter chipset all in its own section. But obviously they actually provisioned for a metal can on here. Because they've got the, just the pads there to solder down a metal can. Not like the through-hole ones, but just like, oh, there goes my lights.

**Dave Jones:** Surface mount metal shielding can. But obviously it hasn't been removed, because otherwise we'd know about it. Although that one, what's that there? Anyway, I don't know. It's all been hacked around here, so yeah, it's obvious. I don't know if that's a production thing

**Dave Jones:** or whether or not it's been some sort of repair thing. Don't know. Anyway, they haven't labelled the sections. And multimeter chipset. What else is there? Oh, this is, of course, the oscilloscope front end, because it's an oscilloscope. Duh. I was just wondering for a minute

**Dave Jones:** what that was. Yes, so there are our compensation caps. Is it a dual channel? One, and that's why you've got your relays in here to do your, you know, switching. And ADG604, 8066. You can go look up these, playing along at home. Your driver, diff amp drivers

**Dave Jones:** for your ADC. And analog devices, AD9283-50, so that would be, I assume that's like an 8-bit ADC, 50 meg samples per second, usually the dash 50 would denote that. IO expander, HC595, got to have one of those babies in there. Classic, and what's that?

**Dave Jones:** LMP7704. Please excuse the crudity of this teardown, it's all done live, single take, CMP401, they're comparators, I believe. Oh, and by the... no, I'll get on to that. So anyway, on the bottom it's just got miscellaneous stuff. Is there some diode protection in there

**Dave Jones:** for the front end? Perhaps. Something like that. Is there some diode... no, no, they would be the diff amps for the oh no, current, no, I was going to say there, that's probably your amp. There you go, that's probably your amp for your

**Dave Jones:** current sense, I'd say, for your current ranges. Anyway, got an extra relay on the bottom, jeez. Got ourselves a buzzer there. And that'd be a buzzer. The difference between a buzzer and a transducer is that a buzzer has the oscillator building, you just apply the voltage and bzzz.

**Dave Jones:** Sorry, that's a poor buzzer sound, isn't it? Whereas a piezo transducer you've got to actually drive it with a signal. Because it's just a piezoelectric element, and it doesn't do anything on its own if you just apply DC, it's just a capacitor. So, ATML320, is that a

**Dave Jones:** that's an E2P, that looks like an I2C thing, you can tell by the two resistors there, going up to pin 8, which is almost certainly the power, it is, because there's a bypass cap across there. So that is some E2P calibration stuff. So there you go, nothing else special up here, just got a DC to DC converter.

**Dave Jones:** So that's all the bottom. What's the main processor over here? Oh, the PICFAN boys go wild, PIC32MX795F for those playing along at home. And an Actel ProASIC 3, that's interesting, because maybe the PIC32 can't do all the stuff on its own for the oscilloscope, and you know,

**Dave Jones:** serial decoding and all that. So the Actel ProASIC 3 FPGA is obviously doing some stuff down in there, doing the business. What is that? I have no idea what that is. That's interesting. Bueller? Bueller? Oh, that's gotta be just based on what it is there, that's a DC to DC controller

**Dave Jones:** chip. So anyway, one of the interesting parts about this is it does have USB, it's probably the only multimeter on the market that has USB. And a lot of people ask, it was a very common question on the 121GW multimeter design, why we didn't include USB?

**Dave Jones:** The answer is safety regulations. You cannot just whack in a USB, especially when it's on the same ground as everything else, because your case has to be sealed from your ground terminal down here. It's all, you know, there can't be any exposed metal.

**Dave Jones:** You might have been able to have one like behind the battery cover or something like that, but this is why virtually every multimeter on the market does not have USB. They have like infrared, or they have, you know, new ones like the 121GW will come in with blue, you know, wireless Bluetooth type

**Dave Jones:** stuff. But before that, they've all had like serial infrared interfaces. They wouldn't even have a proper serial RS-232 connection. Why? Because of the electrical continuity between the connector and the input jack. It creates a safety hazard. So I'm not sure how, well, actually, duh, I do know

**Dave Jones:** how they got this one passed, because it's got an analog device's ATEM 4160. They're very nice chips, very expensive to them. I'd like to know what they get those for in volume. I've looked at those in volume quite a few years back now, and I can't remember the price, but

**Dave Jones:** jeez, they were a pretty penny, even in like 1000 or 10,000 volume. And that's a complete USB opto-isolator. I mean, look, it's like they've actually done it properly, they've routed out the tracks right around that, absolutely brilliant. You know, there's a little bit of creepage distance in there, but the solder

**Dave Jones:** mass handles that no problems. And yeah, they've just like completely isolated that. So with the chip, of course, and you can see the chip under there, and that's how they can get, if you didn't have that, you would not be able to have your

**Dave Jones:** USB and external metal connector on a you know, on a certified multimeter. It's just not going to happen. So there you go, and that's why you can get them on oscilloscopes, because the oscilloscopes you use have grounded input connections, which is the mains, which is connected directly to mains.

**Dave Jones:** They have to be, for safety reasons. So there you go, what's that crystal there run at? 100. It's at 100. Wow, that's speedy, isn't it? Wow. Wonder if they've got, if they're doubling that or doing something else in psi, but you know, usually you have like an external 20 megahertz crystal and then you

**Dave Jones:** PLL it up inside the FPGA, but yeah, that's, they've got 100 megahertz straight off the bat. Wow. And the PIC, PIC32F, because people are going to want to know. 8! Ah, it's just a standard 8 meg jobby, but the PIC32 series actually has a PLL built in, and it can multiply that.

**Dave Jones:** I can't, like, 4, 6 times or something, 4 times at least. Something like that, so it might be operating at, say, 48 megahertz. Or something like that. So there you go. That is inside the Wens 540, and there's nothing else interesting in there, you know.

**Dave Jones:** It's just got the graphical LCD and whatnot. And this one's really crusty and the bottom of it is just, the bottom of the case like that is just, it's got some sort of, oh, is that a custom? Is that a custom battery pack?

**Dave Jones:** Yeah, that's a custom battery pack. So we'll probably find like a lithium ion charger. No, that was the I2C job, wasn't it? ATML H3, 22 gigabytes. Is that 2 gigabit? Sorry? Wow, that's a heck of a... Anyway, bat 1, where's that going off to?

**Dave Jones:** Let's have a look on the other side. Nothing doing. But you might find, if you look hard enough, you might find a, because I presume that was a lithium ion pack. Maybe it's got the charger built into it, perhaps. On the board, like a board, or in part of the pack or something like that.

**Dave Jones:** Not sure, because I'm not seeing anything. Ah, could be that. Could be that thing there. That's probably a lithium ion charger, I'd say. By the way, if you're asking, no I do not, that zoom up in the top corner, yes it is a hex thing,

**Dave Jones:** and yes it is bloody annoying on my Tigano microscope, and I did figure out a way to turn it off once. There you go for those playing along at home. That's probably some sort of lithium ion charger, is it? I don't know. And yeah, I think there's a combination

**Dave Jones:** on my little controller here to turn that off, but I can't remember. I don't know. Might be RTFM. But there you go! That's a look inside the Wens 540 single take teardown. Catch you next time.
