---
video_id: 8GLL6P662Fo
title: EEVblog 1667 - Reverse Engineering the Brymen BM2257 Multimeter LowZ Mode
url: https://www.youtube.com/watch?v=8GLL6P662Fo
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 26, "2": 50, "3": 66, "4": 85, "5": 103, "6": 134, "7": 146, "8": 170, "9": 196, "10": 213, "11": 230, "12": 245, "13": 264, "14": 281, "15": 309, "16": 332, "17": 353, "18": 365, "19": 379, "20": 401, "21": 420, "22": 436, "23": 453, "24": 471, "25": 484, "26": 502, "27": 517, "28": 535, "29": 551, "30": 569, "31": 587, "32": 601, "33": 616, "34": 625, "35": 640, "36": 654, "37": 673, "38": 689, "39": 707, "40": 723, "41": 737, "42": 754, "43": 770, "44": 788, "45": 804, "46": 821, "47": 834, "48": 853, "49": 869, "50": 892, "51": 908, "52": 925, "53": 945, "54": 964, "55": 977, "56": 992, "57": 1012, "58": 1030, "59": 1051, "60": 1067, "61": 1085, "62": 1098, "63": 1118, "64": 1134, "65": 1150, "66": 1164, "67": 1180, "68": 1192, "69": 1214, "70": 1230, "71": 1246, "72": 1260, "73": 1275, "74": 1287}
---

**Dave Jones:** Hi, it's reverse engineering time again. Today we're going to take a look at the EEVblog brand spanking new EEVblog BM2257 multimeter, available on EEVblog.store, selling like hotcakes, by the way. And it's basically pretty much an upgrade to the VM, the venerable BM235, which you can still get and it's still cheaper, you pay a bit more for this, but it has a few extra features, orange backlight instead of white, thank you very much.

**Dave Jones:** But we're going to take a look at the low Z or low impedance mode today, which is a very useful tool for eliminating ghost voltages in, say, when you're measuring mains and things like that. But it can be useful for other things like measuring batteries, for example, where it actually presents a load of a couple of K ohms on there to better measure your battery under load.

**Dave Jones:** And you can see the reading actually drop there. That's the electrochemistry inside the battery. If you load it down, it's, you can see that's dropping pretty quick at 1.21 volts, so you know that battery is, and that's with a couple of K loads, so you know that battery's pretty darn dead.

**Dave Jones:** And you'll even see that at the high end of a battery, for example, this one's fully charged, you'll notice that's dropping a bit there, because that's like right at the tippy top of the, like, voltage there, so when you put a little bit of a load on there, it tends to drop, and you'll notice that'll eventually stop, yeah, it'll stop dropping.

**Dave Jones:** There you go. But the old BM235 didn't actually do this, well, it did, but it didn't have the resolution like the new one has. So measure that same battery there, and you'll notice that it just doesn't have the resolution, because it's on a fixed 600 volt range there, it doesn't auto-range.

**Dave Jones:** So the new 2257 will actually auto-range down to the 6 volt range, and you get 1 millivolt resolution on there. Beauty. And even better on little coin cells, for example, because, like, 2.5 K load would be very typical. Of, say, a peak load, like, you know, a milliamp or 2, on, like, a small coin cell like this, and if you just measure it on regular volts here, you'll notice that's, oh, 3.3 volts, okay, you turned over to low Z like this, and, wow, look at that, yeah, the ESR of that cell, not too great, is it?

**Dave Jones:** But there was another problem with the design of the BM235, and if I plug it in to an ohmeter over here, yes, that's what they're called when your multimeter is in ohms range, it's an ohmeter, dammit. You'll notice that it's 10 meg input impedance.

**Dave Jones:** Where's this low impedance mode? Well, if you actually read the manual for the BM235, if you're RTFM, then you'll find that the low impedance mode doesn't kick in until, like, 6 or 7 volts or something like that, and there's a reason why. But if you do the same thing on the 2257, you'll notice that it is 2.3 K.

**Dave Jones:** So even, and this is basically only outputting, like, you know, like a volt or something. Something like that in, well, we can measure it. Oh, no, it's only 0.2 volts in this range, right? So it's only outputting 0.2 volts. But even at 0.2 volts, the low impedance inside this thing is kicking on and giving you 2.2 K ohms instead of 10 meg that you get on the BM235 here.

**Dave Jones:** Why is it so? Why is it so? Why is it so? If we have a look at our DaveCad reverse engineering drawing here of the BM235, it's a bit simplistic. It's a little bit. It's a little bit more here, but basically what it does is that your positive input, positive terminal here, you've got two different paths.

**Dave Jones:** One is through a 1K resistor and a PTC, which is about 1K or 1.5K or thereabouts, and another path through, again, another 1K. These are high voltage input resistors, by the way, and another PTC, and both of those are clamped down to the common terminal with MOVs.

**Dave Jones:** It's a bit more complicated. There's, like, multiple ones in that series here, but let's not worry about that. They're clamped down there. And this is the range switch here. And in voltage mode, of course, it uses this path here through a 10 meg input impedance through to the IC.

**Dave Jones:** But on the 235, the low impedance mode is effectively using this path here, which is the same one that's also used for the ohms range, which then has a diode Zener clamper here. And I've done an entire video on how this dual transistor clamp actually works.

**Dave Jones:** It's very popular. It multimeters going right. Back to the old school fluke days. And it's basically two transistors acts as a Zener diode and a diode in series. And this is different polarities. They just flip around like that. And you can watch this in video 1157.

**Dave Jones:** So I won't cover that. But basically what it is is it's effectively, you know, around about a 7-volt Zener clamp. So that's why the low impedance path here of 1K through the PTC here, which is about 1.5K, so that 2.5K only starts to conduct and become 2.5K at voltages above 7 volts where this Zener clamp starts to clamp down through to the common terminal.

**Dave Jones:** Otherwise, you just get the high impedance going into the IC, which is around about, you know, another 10 meg just like up here. But the new design, BM2257, doesn't do that. It has that 2.3K, that low impedance, that low Z path. So it's basically doing something different to the BM235.

**Dave Jones:** So this video is all about just basically not fully reverse engineering the schematic for this because Ryman famously won't even give dealers like me the schematic for this thing. They're very protective of their schematic for some reason. But yeah, let's reverse engineer the front end and figure out what's going on here and how it differs from the BM235.

**Dave Jones:** But before we do that, there is one other interesting thing. One other interesting quirk I'll show you is that, like, at 1 volt, right, it absolutely works fine, okay? But if we go up to 10 volts, for example, you'll see that it'll actually range up.

**Dave Jones:** It's now in the 60 volt range and it'll ramp up to the 600 volt range and it'll do this automatically. But under 1 volt, it doesn't go actually all the way to 0. Let's go to 0.9. Ah, look at that. It starts sort of, like, flickering a little bit.

**Dave Jones:** Not sure if you're actually seeing that. So let's actually dial that down, 0.96, 0.95. So, at about 0.93 volts, it doesn't actually detect that anymore. So, that's interesting. Just keep that in mind. And the BM235 will actually go a bit lower. I'm down at 0.6 volts there, I'm at 0.5.

**Dave Jones:** And, well, at about 0.4 volts, it does about the same thing. Once again, doesn't go down to that least significant digit there. And they will actually automatically detect AC and DC as well. You notice DC there. And DC there. But if I swap over to an AC source down here,

**Dave Jones:** then you'll see that it's automatically detected 1 volt AC and 1 volt AC over here. Cool. All right, so let's try and reverse engineer this. Not completely, of course. Just the input front end and just for the voltage ohms and other stuff. And, of course, the low Z stuff.

**Dave Jones:** So, not including the current ranges and stuff like that. And here's the internal shot of the new 2257 here. Two ball construction. Same as the old one. BMI 235. And if you desolder the top board here, I've taken high-res photos, always available on the EVBlog Flickr account, by the way,

**Dave Jones:** top and bottom like this. So, I can just swap between the top and bottom and we can reverse engineer this circuit. So, I've done a whole video on various techniques for reverse engineering PCBs and stuff like that. So, I'll link that one in if you haven't seen it.

**Dave Jones:** So, I won't go over details, but you can see that we've got our varistas here, which are out there. We've got our MOVs and we've got two PTCs here. These are both unbranded, by the way. There's no markings on them. And this one's a bigger one, which is heat-shrunk here.

**Dave Jones:** Here's our two input resistors up here. So, they're big, large, high-voltage jobbies like that. And these two resistors down here are our 5-meg input resistors for our current sense jack circuit. So, we won't bother with that. And we've got our board-to-board interconnect. Four pins up here, JU1.

**Dave Jones:** And JU6 here just goes to... This little SOT 23, which I think is just a temperature measuring thing. So, they've put that on the main board. So, we won't bother with that. But as you can see, we can reverse engineer that nicely. It's got the nice isolation slots here.

**Dave Jones:** Everything's hunky-dory. We've got our Dave K reverse engineering schematic here. And you can see that there's our positive input jack. So, that's here. And then R33 and R32 here. These are these two resistors here. High-voltage jobbies. Oh, I forgot to put one. K on there.

**Dave Jones:** That's also one K. And then through our two PTCs. So, the small PTC here is this PTC here. And the bigger one here is the one in the heatring. So, basically, you've got two different input paths here. And these go off to the four-pin header up the top here.

**Dave Jones:** And then there's two separate protection paths here with the MOVs, these varistas. One is clamping PTC2 here. And the other is clamping via here and down to the COM terminal down. And these are CNR brand. I'll put up the data sheet here if you're interested.

**Dave Jones:** There is one which is a slightly different value. The 5-1 here means 560 volts. The 6-2-1 here, here, and here, that's 620 volt nominal rating. So, these will clamp any of your high-voltage inputs over and above your 1,000 volts or whatever your meter is capable of.

**Dave Jones:** So, very typical front end here. And very typical to have two separate paths. Typically, you'll have one path for your voltage and one for your voltage. And one path for your ohms and diode stuff. So, here's that four-pin connector. And here is basically on the main PCB here.

**Dave Jones:** So, I've reversed engineered this. And we'll get a photo up. And you can see that we've got our top and bottom of the PCB. The range switch has been removed here. So, we can see all the contacts. And you can see that there's actually multiple contacts on both sides of this thing.

**Dave Jones:** So, as you rotate the switch, the little contacts in there just make contact. And I've taken a photo of the bottom of the range switch here. And I've taken a photo of the bottom of the range switch here. And I've cropped that out.

**Dave Jones:** So, you can just have the contacts. And you can see that those contacts actually rotate around and just make contact. You know, they'll short out here. And here, for example, when the switch is in this vertical position. But we can do better than this.

**Dave Jones:** Behold, my finest work. What I've done using GIMP here is that I've taken this image and set it transparent. And I've scaled it to actually fit. And you can see it overlaying the contacts here. So, hopefully, you can see, like, this gold outline.

**Dave Jones:** Like that, that square. And these two pins over here are obviously, they will short out those two contacts when they're physically in that position there. And likewise, these two contacts, these two, these two. So, this is basically a six-way by however many positions, seven positions that we've actually got on the front here.

**Dave Jones:** So, multimeter range switches, they're relatively complicated. So, what I can do here is I can actually rotate this. So, minus 22.5 degrees is each angle on here. You just... Figure that out by how many positions and divide by 180 degrees or whatever. Right?

**Dave Jones:** So, we can actually rotate that switch like that. And then you can... Right? That's actually the off position. Vertically like that is the low impedance position, the low Z. And you can see... Sorry, the image is flipped. The low Z input is the one where it's straight like that.

**Dave Jones:** And minus 22.5 degrees is actually the off position. And then minus 50 degrees is actually the first. Which is the AC volts position on here. And then you can increase it again. And you can rotate this thing around. And then you can... You know, it's not easy.

**Dave Jones:** You get lost quite a few times chasing a red herring down a rabbit hole. But you can eventually figure out how all of these are doing. Anyway, I've done all that. I've spared you the hard work. But the odds of me having goofed something here are reasonably high.

**Dave Jones:** So, please correct it in the comments down below. But anyway, we got ourselves a schematic like this. So, just imagine that there's like a split between here and those contacts on the top half are like the two that are joining. So, I've got the different positions here.

**Dave Jones:** Low Z, off, volts AC, volts DC, ohms, millivolts. I've left out the current ranges just so we don't confuse anything. So, in the low Z position, okay, these two contacts will short out here. And likewise, these two contacts will short out here. And if we have any further ones, they'll short out.

**Dave Jones:** So, in the ohms range, we'll have these short out. These short out. These short out here and these short out down here. So, I've physically arranged them like that. Now, you remember the low impedance path, low Z path on the BM235, the older design went through a resistor and a PTC like this.

**Dave Jones:** And then it went through a Zener diode clamp like this down to ground. So, this wouldn't conduct until you'd get to like that threshold, that Zener threshold voltage of like 7 volts. And then you would start to see the load presented by this, you know,

**Dave Jones:** 2.5k, 2.75, or whatever it is here. But what happens in low impedance mode here, okay, this shorts to here like this. And this shorts to here. And you'll see that our positive input jack goes through R32, which is a 1k resistor, through that large PTC.

**Dave Jones:** Because it's physically larger, it's going to be able to dissipate more heat. So, that's the one you want to use in your low impedance mode. Because you're going to be, because this PTC, positive temperature coefficient, it means the resistance. So, you're going to be able to dissipate more heat.

**Dave Jones:** When the temperature increases. And, trust me, go and, if you stick this across 240 volt mains, go and use Ohm's law, 240 volts divided by 2.25k, and see what you come out with. You definitely want that to increase in value. Otherwise, your multimeter's going to get pretty hot pretty quickly, okay?

**Dave Jones:** But at low voltages, it's just going to remain that, you know, nominal 1.25k or whatever. Okay? So, it goes through here, like this, and then it goes into this contact, boom, straight down here, and then they shunt it directly to ground like that.

**Dave Jones:** And they bypass any Zener clamping diode. So, that's why the new BM2257 model has the low impedance mode all the time. Because they're shunting that right down to ground. No wuckers. Excellent. And then how are they reading off that voltage? Well, they're not reading it off this path, because this path has gone down to ground.

**Dave Jones:** So, this terminal here. So, this path, which goes into our, the BTC, the Bryman Technology Corporation chip. I know which processor it is, but I'm not allowed to tell you. Sorry about that. But, yeah. So, these are the two signal paths here and here,

**Dave Jones:** which go off to the processor and the ADC to measure the signal. So, it's not going up here through this one, like that. It's not going through there. So, it actually reads it through, like this, boom, up here, and then goes. Oh, it jumps around there.

**Dave Jones:** We'll explain that in a second. And then it goes through the 10-meg high-voltage resistor R34 here. And that is that beautiful jobby down there with the isolation slot. So, that's the big high-voltage ceramic 10-meg input resistor there. And you'll notice that this is our AC coupling capacitor over here.

**Dave Jones:** And we have that because in our volts AC position like this, you'll notice that it's tapping off AC like that. And going through the same. So, it's AC coupling the input signal on the volts AC mode. But in the low impedance mode and the volts DC and ohms and millivolts,

**Dave Jones:** it's all going through that 10-meg resistor, boom, like that. And if you want to see what happens in ohms range, for example, well, we can short that out, short that out, and short that out here. And we've got some extra stuff happening here.

**Dave Jones:** So, in ohms range, what you want to do is you want to drive the signal out as well as read back the signal. Like across the terminals. Because in resistance mode, you're basically driving a current through your resistor under test. And then you've got to measure the voltage.

**Dave Jones:** So, what they're doing is obviously still tapping off the voltage here. And that's coming from across the terminals. But they're also driving in this direction, like that. They're driving that, which goes through, boop, boop, boop, boop, boop, through the protection. And, of course, all the input clamping here.

**Dave Jones:** But there's also on the board. There's D20 and D21 here, which are two diodes. And I haven't mapped out. There they are there. So, I haven't mapped out what they're actually doing there. But it doesn't really matter. And you can see that in the off mode here, they're physically, like, breaking the inputs like that.

**Dave Jones:** And interestingly, I found, because in the low impedance path here, I noticed that, okay, we've got these contacts here like this. Okay? So, they're actually shorting out like that. So, this will be. So, like, the off position like that. And these ones and this contact around here with these little ones here,

**Dave Jones:** they're the, so that the processor knows which switch position you've actually selected there. But in the low impedance position, which, as I said, is the vertical position like that, you've still got these extra contacts here and here like this. What are they doing?

**Dave Jones:** You'll notice that it jumps around here and it bypasses that in off mode like that. And it actually traced it out. What that is, is the backlight. So, what they're doing is actually physically connecting the backlight when you switch the meter on. So, this is what this mod wire goes across here.

**Dave Jones:** The PCB designer really, yeah, it's almost as if they rushed this and they didn't have enough time to get that. But they've added this bodge wire. And this is actually for the backlight because this is the backlight terminal here. And this is your voltage.

**Dave Jones:** This is your battery terminal, basically. So, they're connecting the backlight through to the battery. And they've also got another jumper wire here, which is the big 10-amp jumper wire here for the 10-amp input, which goes over to our clamping diodes here, which are bigger and beefier, by the way, than the ones on the old BM-235.

**Dave Jones:** And then they've just got an extra diode because they couldn't fit it on the top there. But that's all part of the input current clamping circuit. But, yeah, they disabled the backlight for some reason. So, my guess there would be maybe it's somehow, if you have it on all the time,

**Dave Jones:** even when the meter's switched off and there's no voltage on the processor here, then you might find that you can reverse power the thing and you might get extra leakage through the processor when it's actually switched off. So, they're just physically disconnecting the backlight there.

**Dave Jones:** So, that's interesting. Didn't expect that. And I didn't finish my thing about the PCB design. Yeah, you'll notice that there's a bodge link across there because the PCB is so thin at that point that they actually had to put, they couldn't put it on the backlight.

**Dave Jones:** They had to put a trace on there. So, that's a PCB goof. So, yeah, I'm not sure if they, well, yeah, you probably can't fix that because that's a physical distance because you can't bring it around here like that because you've got physical, you know, space reasons.

**Dave Jones:** So, you can't do that for compliance reasons. So, it's got to go around that side. So, yeah, yeah, it's almost as if they did a rush job on the PCB and they didn't want to rip up and reroute things and try again and stuff like that.

**Dave Jones:** So, that's why we have... You know, big-ass jumper wire going over here and a jumper wire for the backlight going across here like that. And that little link on there. So, that's a bit disappointing, but, you know. So, there you have it. We've explained why the new BM2257 actually has the low impedance mode all the time

**Dave Jones:** because they're shunting that sucker directly down to ground as they do on lots of other meters that actually do that. So, I don't know why the original BM235, um, did it the way it did it through the clamping diodes and that they had that 7-volt minimum.

**Dave Jones:** I don't know. But they did learn the error of their ways and they fixed it in this, uh, new edition, which is great to see. And why it actually, um, cuts out at that 0.93 volts, um, there's no reason for it, really. So, I've got to assume it's part of the auto-detection

**Dave Jones:** because they're just reading the voltage off here like they do. You know, there's no reason it can't measure down to zero. So, I assume it's some sort of firmware, threshold thing that they've arbitrarily chosen to do there. Remember, this is auto-sensing AC and DC.

**Dave Jones:** So, they need to, like, set thresholds somewhere to auto-sense these and auto-detect them, something like that. So, in theory, you could read down to zero, but they've decided to, I don't know, they have that limits in there for that automatic detection, AC-DC detection reason.

**Dave Jones:** Anyway, I hope you found that reverse engineering useful. If you did, please give it a big thumbs up. And as always, discuss down below and over on the EEVBlog forum, of course. Each video gets... gets its own EEVBlog forum link. And you can buy the new 225 meter

**Dave Jones:** at EEVBlog.store. Catch you next time. ELECTRONIC MUSIC
