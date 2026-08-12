---
video_id: pH-FySpUk84
title: EEVblog 1431 - Keysight EDU33212A Function Generator Teardown
url: https://www.youtube.com/watch?v=pH-FySpUk84
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 34, "3": 47, "4": 58, "5": 74, "6": 87, "7": 103, "8": 118, "9": 134, "10": 148, "11": 162, "12": 178, "13": 191, "14": 203, "15": 213, "16": 229, "17": 242, "18": 254, "19": 268, "20": 279, "21": 292, "22": 310, "23": 322, "24": 338, "25": 354, "26": 367, "27": 380, "28": 396, "29": 409, "30": 419, "31": 430, "32": 439, "33": 455, "34": 464, "35": 478, "36": 489, "37": 507, "38": 520, "39": 542, "40": 551, "41": 558, "42": 576, "43": 596, "44": 616, "45": 629, "46": 644, "47": 652, "48": 667, "49": 683, "50": 696, "51": 708, "52": 723, "53": 737, "54": 757, "55": 770, "56": 783, "57": 794, "58": 811, "59": 821, "60": 836, "61": 855, "62": 875, "63": 890, "64": 901, "65": 913, "66": 925, "67": 941, "68": 953, "69": 961, "70": 970, "71": 984, "72": 997, "73": 1005}
---

**Dave Jones:** Hi, quite a few people have asked me for the teardown of the Keysight EDU33212A waveform generator, 20 megahertz dual channel jobbie. So, let's tear it down. This will be in 4K resolution for those playing along at home.

**Dave Jones:** This is part of their new educational value series scopes which we've looked at. And apparently, yeah, cuz I did a giveaway of quite a lot of this gear. And apparently, they've been like they've due to a chip again, the component shortages, they're still having problem delivering those.

**Dave Jones:** So, yeah, there must be something in the well, they're having problems across the board as are a lot of manufacturers. And yeah, they're having problems. So, sorry to the winners of those who haven't actually received them yet, but they're still on the list.

**Dave Jones:** So, yep, once they get the parts, they'll be able to make them. Anyway, let's crack it open. It is the same form factor as the oscilloscope and the multimeter as we looked at.

**Dave Jones:** So, they reuse all the plastics. Everything else is practically identical in them. The metal works inside will be all the same. So, anyway, a sneaky little interlude, if I may, just to plug at my Odyssey channel over here cuz I'm up to 53,000 followers over here.

**Dave Jones:** I think it'd be really cool if I got 100,000 followers on the YouTube alternative Odyssey. That would be absolutely awesome. Anyway, if you're like sick and tired of the ads on YouTube, go watch it all on Odyssey.

**Dave Jones:** And you can all my videos are there like minutes after they appear on the YouTubes. And they're in full full resolution as well. It's great. Then the Odyssey community, lots of engagement in the comments and stuff like that.

**Dave Jones:** Absolutely fantastic. I love Odyssey. And I occasionally post exclusive videos on Odyssey as well. You won't find on my YouTube channel or any other platform I use. This is a photo my photo spectrometer that I've got did of that.

**Dave Jones:** So go check it out. And I've got my EVBlog two channel on there and my EV Discover as well. And it's a really great platform. I'm probably doing like a third of my daily video views on Odyssey now instead of YouTube.

**Dave Jones:** So and a lot of electronics creators, a lot of your favorite electronics creators are on Odyssey as well. Check it out. And you can feel on the front panel here how they've still got the two little slots there for the oscilloscope probe compensation on there.

**Dave Jones:** So they certainly reused the front panel there. But of course you can't reuse the like the buttons here. This has to be entirely different. And in the EDU series here, you can actually feel the two extra BNCs there.

**Dave Jones:** So yeah, the the fourth channel plus the sig gen. Yeah, I do believe that's exactly the same metal work, exactly the same mains interface, exactly the same like metal threaded inserts here, which did have the gunk on the screws.

**Dave Jones:** Excellent. And probably got the same power supply. I would say, you know, if you're going to reuse as much as possible, you would also try and reuse the power supplies even if it's like overrated between models and stuff like that.

**Dave Jones:** Cuz you know, generally you would design it around if you've only got like five and 12 volts output or something, then you'd do a plus minus 12 or whatever, then you would design your product around an existing power supply.

**Dave Jones:** So that remains to be seen. Let's get the metal work off. All right, so let's lift that off and tada! We're in like Flynn. Yeah, it's probably going to be an identical power supply.

**Dave Jones:** I will take the cage off that. Somebody had fun with a silastic gun. Look at that. Oh, beauty. Oh, all right, because I can I've taken apart the EDU series oscilloscope and here they are precariously a balanced.

**Dave Jones:** Don't try this at home, kids. I'm a professional. Um but yeah, as you can see, like it's identical metal work, everything else. It's and the board's designed to fit in place like that.

**Dave Jones:** So, there you go. For those playing along at home, that looks identical to the original 1000 that we've taken apart before, done tear down of, and also hacked. And here is the new function gen up here.

**Dave Jones:** So, yeah, all these chassis is the same, all the metal work cutouts, they're all the same. Everything's the same. Let me show you the power supply. And as predicted, the power supplies are absolutely identical.

**Dave Jones:** If I get that cable out of the way, check it out. Except that the oscilloscope has a couple of black caps in here instead of green. So, that's interesting.

**Dave Jones:** I don't know why they mix those up. I've got no idea. But yeah, no surprises for finding identical power supplies, right? Completely swappable. They've even got the same part number, have they?

**Dave Jones:** I believe they would. Yeah, just different manufacturer codes on them. Now, spot the difference. Spot the difference between these. Leave it in the comments down below. There is something actually dramatically different between these two power supply assemblies.

**Dave Jones:** Can you spot it? Can you spot it? Leave it in the comments now down below. I guess I will spoil it for you after this. Can you spot it?

**Dave Jones:** The fans are mounted back to front. Look at this. This is the function gen here. And this is the oscilloscope. They're exactly the same brand and model fan, but one's sucking in, one's blowing out.

**Dave Jones:** Which is the right one? I don't know. Are they installing them just randomly on the like is it an actual assembly error? Or did they decide that no, we're going to, you know, suck the air in on one of them and blow it out on the other?

**Dave Jones:** I don't know. Uh Keysight, Daniel. Müller, Müller. Müller. And the brand of cap is literally okay cap. These caps are okay. Same branding on the output filter caps as well.

**Dave Jones:** They're okay, too. Anyway, it's a very neat and tidy power supply assembly. And yes, the output voltages and the output cables are exactly the same. I'm sure that I could completely interchange these and it wouldn't make a difference.

**Dave Jones:** I could like mix up these back shells and I wouldn't even know when I put this back together. But yeah, it's got no shortage of output filtering. A TO220 is flapping around in the breeze here, but you know, um someone had fun with the silastic gun.

**Dave Jones:** Um but you know, yeah. It actually looks like a decent layout. Keysight almost certainly didn't uh design this as most companies don't. They just farm out their power supplies.

**Dave Jones:** But yeah, no, it looks nice. We've got a nice spade lug going down to the chassis down here. No wackers. Everything's all heat shrunk. We've got input fuse in here.

**Dave Jones:** We've got a PTC there, do we? X and Y class caps or your common mode chokes, all the requisite stuff. No worries. I mean, it's only like, you know, a 30 W power supply or something.

**Dave Jones:** All right, let's take a look at this board, shall we? I'm actually capturing my 4K screen this kind of time instead of my regular 1080 screen. So, let's have a squeeze.

**Dave Jones:** You can see that we've got the Cyclone 10 FPGA in here. And no surprises for finding that. Part number for those playing along at home, there's many varieties of the Cyclone 10 series.

**Dave Jones:** You can pay, well, I'm not going to say peanuts, but you can pay like orders of magnitude difference in price depending on the amount of silicon and feature set in there.

**Dave Jones:** So, I don't know what that one is and not really that fussed. Bit weird to see the old Intel inside symbol on there. Yeah, so anyway, that is surrounded by some memory here and up here as well.

**Dave Jones:** We've got our controlled impedance wiggle wiggle wiggle yeah traces all in here and also going out to our DAC out here. Ah, bloody orphan view can't do multiple level undoes.

**Dave Jones:** That sucks. Anyway, for those who don't know, all of these wiggle traces here, these are of course matched length. So, when you're talking about the speeds going to DDR memory these days and in this case going to the DAC, then yeah, you've got to match the length of the lines.

**Dave Jones:** So, this trace that goes all the way on the outside here, that has to match that which goes further. So, that's your longest one and then your shortest one goes from well, you know, like into here like this.

**Dave Jones:** So, they've got to match the length there and overall those two lengths will be matched. So, your skew, your data skew and your clock skew and everything else, your timing is pretty matched with the distances even with the small distance was we're talking about between the chips there which isn't much but still it matters once you get up in speed.

**Dave Jones:** Yeah, so I'm not sure what speed the memory would be operating there. Your guess is as good as mine. I mean, this is only a 20 MHz uh bandwidth thing.

**Dave Jones:** So, the TX DAC here but of course you've got a 20 MHz clock cycle you've got to be spewing out more data than that. So, the data rate is high.

**Dave Jones:** That's why all that stuff in there has to be matched. And the AD9747 here, that's a dual 16-bit 250 megasample per second DAC. So, as I said, yep, it's pretty quick and then they've just got some drivers here of course.

**Dave Jones:** We can go in and have a better look at those numbers there. 51 661. I think these might be Intercil uh EL5166s. So, yeah, which is now Renesas. Um and they're 1.4 GHz bandwidth current feedback amplifiers.

**Dave Jones:** Yeah, that would make sense in that sort of application. And with this be some offsetting? I don't think that's local regulation. Not sure what the deal is there. Anyway, they're going into some relays and attenuator networks down there to get your uh various low output signal levels and whatnot.

**Dave Jones:** And then your extra stuff down here, these are your two output BNCs. You can see there's a bit of residue on the connectors there. They're hand soldered, so a little bit how you doing, but it's neither here nor there.

**Dave Jones:** Um and then of course there's your 50-ohm um output impedance there. And it looks like they have dual drivers there with 100 ohms in series each, and they parallel Looks like they're paralleling those up.

**Dave Jones:** So, you can see them joining at the output here, and they've just got some output filter in there. You can see a couple of little chokeys down in there.

**Dave Jones:** Um but yeah, that's interesting. They're They've paralleled those up, and you can see Look, the Here's the output of the uh the attenuator network, and then that's going and that's splitting into the two sides here.

**Dave Jones:** So, they're paralleling those up, presumably uh to get extra grunt um out of that. You wouldn't be getting extra Like they wouldn't be Of course, you can parallel um the amplifiers for reduced noise, but I I don't think this is a stellar performer in that regard.

**Dave Jones:** So, they're doing that for extra output grunt. And there's your PLL clock gen. Uh that's an LMX2582 for those playing along at home. Uh 10 MHz reference there. Does this accept?

**Dave Jones:** No, I don't think this accepts an external 10 MHz input. I'd have to check that. But yeah, that's the PLL clock driver for everything. But apart from that, not much else doing.

**Dave Jones:** And this is our calibration output here. We've got a 74HC4051 jobby for the win. Old school. Old school again, TL072. Love it. Don't know what that analog devices jobby there is.

**Dave Jones:** This here is a ground connection. Very nice if you're designing a product like this. It's a very appreciated to designing little ground loops like that. They don't cost much and you can put your oscilloscope probe in there and very handy for getting there and probing during debugging.

**Dave Jones:** And this here is our trigger gate burst. Well, that includes all the circuitry there. And then this is our sync output here, which is nothing. It's just got a like a transistor driver on the output and that's it cuz all it does is trigger output pin.

**Dave Jones:** That's it. No workers. And got some other op-amps here, TLV274s. I don't know what they're doing. They don't seem associated with anything in particular, at least not on the top layer anyway.

**Dave Jones:** Meh, whatever. Just that some housekeeping op-amps. Then of course, you got all your regulation stuff up here. Good old old school 7905 for your negative 5 V regulator. 7915 up here.

**Dave Jones:** 7815 and 7805. So, we got plus minus 5 V rails and plus minus 15 V rails for the op-amps of course. Very nice. You want the headroom on the op-amps.

**Dave Jones:** So, yeah, that's interesting because that mean this is linear. So, the output of the power supply, that must be not plus minus 12 V as I mentioned before. It must be like at least there's got to have at least a 2-V dropout voltage on that.

**Dave Jones:** So, it's got to be like plus-minus 18-V or something like that would be my guess. You want to keep it down so the dissipation in those isn't much, but you know, yeah.

**Dave Jones:** There you go. Anyway, there's another switching rig there. That's probably for like a 3.3-V. Another Well, there's another linear rig. There is that another switching jobbie and the one that's left out.

**Dave Jones:** There you go. They've left out another one. I don't know. Miscellaneous circuitry, but yeah, like there's not much in it. There's a Cyclone 10 FPGA, some memory, a DAC, you know, output dividers, output drivers, and then just some calibration and sinky stuff and a clock gen and Bob's your uncle.

**Dave Jones:** Although, what is driving the screen? But, of course, you got to have something to run the operating system and there's our arm jobbie there. It's an STM 32H750. And it's got its own associated memory and everything else and that it has its own PLL as well happening there.

**Dave Jones:** So, yeah, that that fuse half-amp fuse is gone. It's gonski. And then behind my head here, there's some unpopulated circuitry. So, that would have been and including a relay and stuff for what external gate output or something like I don't know.

**Dave Jones:** External No, that might have been like No, because it's got a relay. It's going to say like an external 10-MHz input or something like that, but no, I don't think so.

**Dave Jones:** Another unpopulated device there with a power pad on the bottom. It's got a thermal pad on the bottom. Got another test connector here. Um not sure what it's doing there.

**Dave Jones:** This would be going off to the touch screen, wouldn't it? And anyway, so this would have like video driver and everything Uh, built in. That looks like another switch mode controller that's doing something.

**Dave Jones:** Analog VDD, is it? Okay. Um, the power and fan connectors, nothing much doing. There's your real time clock. That's your 32 kHz, uh, clock, uh, crystal there. And that'd be And that the BQ, uh, 32002 would be an RTC, uh, clock chip.

**Dave Jones:** And there's your battery backup, of course. Aha, there's your video connection. That's on the bottom side of the board there. You can see some, uh, matched length, uh, traces going on in there, um, as well.

**Dave Jones:** And then you've got all, uh, series resistor terminator. So, that's yeah, there's got to I'm not going to I get the board out to flip it on the other side.

**Dave Jones:** I don't think there's a huge lot, um, a huge amount there, but that would be the, uh, surface mount, um, LCD connector, uh, going off. So, this would be the front panel, um, over here.

**Dave Jones:** That'd be like the front panel and, uh, controls and stuff. So, there you go. I just took a bunch of, um, high res, uh, photos and didn't decide to do the full 4K screen capture because my, uh, I could have done this under my Tagarno microscope, of course, but that's only, uh, 1080p.

**Dave Jones:** So, yeah, if I want to be able to And I don't really need to zoom in on stuff. But there you go. That's, uh, that's it. It's all pretty basic stuff.

**Dave Jones:** So, there you go. That's a teardown of the new whatever part number. I can never remember these bloody part numbers. Why can't they give them something decent? Um, I don't know.

**Dave Jones:** Anyway, it's some part number, um, 28 function gen. If you liked it, give it a big thumbs up. As always, discuss down below. Catch you next time.
