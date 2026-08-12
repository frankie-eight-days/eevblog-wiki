---
video_id: pH-FySpUk84
title: EEVblog 1431 - Keysight EDU33212A Function Generator Teardown
url: https://www.youtube.com/watch?v=pH-FySpUk84
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 34, "3": 47, "4": 60, "5": 74, "6": 90, "7": 106, "8": 121, "9": 137, "10": 149, "11": 166, "12": 182, "13": 193, "14": 205, "15": 219, "16": 237, "17": 250, "18": 265, "19": 281, "20": 299, "21": 314, "22": 335, "23": 351, "24": 369, "25": 382, "26": 396, "27": 411, "28": 426, "29": 439, "30": 456, "31": 470, "32": 489, "33": 504, "34": 520, "35": 535, "36": 547, "37": 558, "38": 573, "39": 596, "40": 613, "41": 627, "42": 644, "43": 657, "44": 674, "45": 687, "46": 702, "47": 723, "48": 737, "49": 753, "50": 770, "51": 788, "52": 805, "53": 817, "54": 833, "55": 849, "56": 862, "57": 882, "58": 896, "59": 913, "60": 929, "61": 943, "62": 957, "63": 966, "64": 979, "65": 988, "66": 1003}
---

**Dave Jones:** Hi, quite a few people have asked me for the teardown of the Keysight EDU33212A waveform generator, 20 megahertz dual channel jobbie. So, let's tear it down. This will be in 4K resolution for those playing along at home. This is part of

**Dave Jones:** their new educational value series scopes which we've looked at. And apparently, yeah, cuz I did a giveaway of quite a lot of this gear. And apparently, they've been like they've due to a chip again, the component shortages, they're still having problem

**Dave Jones:** delivering those. So, yeah, there must be something in the well, they're having problems across the board as are a lot of manufacturers. And yeah, they're having problems. So, sorry to the winners of those who haven't actually received them

**Dave Jones:** yet, but they're still on the list. So, yep, once they get the parts, they'll be able to make them. Anyway, let's crack it open. It is the same form factor as the oscilloscope and the multimeter as we looked at. So, they reuse all the

**Dave Jones:** plastics. Everything else is practically identical in them. The metal works inside will be all the same. So, anyway, a sneaky little interlude, if I may, just to plug at my Odyssey channel over here cuz I'm up to 53,000

**Dave Jones:** followers over here. I think it'd be really cool if I got 100,000 followers on the YouTube alternative Odyssey. That would be absolutely awesome. Anyway, if you're like sick and tired of the ads on YouTube, go watch it all on Odyssey. And

**Dave Jones:** you can all my videos are there like minutes after they appear on the YouTubes. And they're in full full resolution as well. It's great. Then the Odyssey community, lots of engagement in the comments and stuff like that. Absolutely fantastic. I love

**Dave Jones:** Odyssey. And I occasionally post exclusive videos on Odyssey as well. You won't find on my YouTube channel or any other platform I use. This is a photo my photo spectrometer that I've got did of that. So go check it out. And I've

**Dave Jones:** got my EVBlog two channel on there and my EV Discover as well. And it's a really great platform. I'm probably doing like a third of my daily video views on Odyssey now instead of YouTube. So and a lot of electronics creators, a

**Dave Jones:** lot of your favorite electronics creators are on Odyssey as well. Check it out. And you can feel on the front panel here how they've still got the two little slots there for the oscilloscope probe compensation on there. So they

**Dave Jones:** certainly reused the front panel there. But of course you can't reuse the like the buttons here. This has to be entirely different. And in the EDU series here, you can actually feel the two extra BNCs there. So yeah, the the

**Dave Jones:** fourth channel plus the sig gen. Yeah, I do believe that's exactly the same metal work, exactly the same mains interface, exactly the same like metal threaded inserts here, which did have the gunk on the screws. Excellent. And probably got

**Dave Jones:** the same power supply. I would say, you know, if you're going to reuse as much as possible, you would also try and reuse the power supplies even if it's like overrated between models and stuff like that. Cuz you know, generally you

**Dave Jones:** would design it around if you've only got like five and 12 volts output or something, then you'd do a plus minus 12 or whatever, then you would design your product around an existing power supply. So that remains to be seen. Let's get

**Dave Jones:** the metal work off. All right, so let's lift that off and tada! We're in like Flynn. Yeah, it's probably going to be an identical power supply. I will take the cage off that. Somebody had fun with a silastic gun.

**Dave Jones:** Look at that. Oh, beauty. Oh, all right, because I can I've taken apart the EDU series oscilloscope and here they are precariously a balanced. Don't try this at home, kids. I'm a professional. Um but yeah, as you can see, like it's

**Dave Jones:** identical metal work, everything else. It's and the board's designed to fit in place like that. So, there you go. For those playing along at home, that looks identical to the original 1000 that we've taken apart before, done tear down

**Dave Jones:** of, and also hacked. And here is the new function gen up here. So, yeah, all these chassis is the same, all the metal work cutouts, they're all the same. Everything's the same. Let me show you the power supply. And as predicted, the

**Dave Jones:** power supplies are absolutely identical. If I get that cable out of the way, check it out. Except that the oscilloscope has a couple of black caps in here instead of green. So, that's interesting. I don't know why they mix

**Dave Jones:** those up. I've got no idea. But yeah, no surprises for finding identical power supplies, right? Completely swappable. They've even got the same part number, have they? I believe they would. Yeah, just different manufacturer codes on them. Now, spot the difference.

**Dave Jones:** Spot the difference between these. Leave it in the comments down below. There is something actually dramatically different between these two power supply assemblies. Can you spot it? Can you spot it? Leave it in the comments now down below. I

**Dave Jones:** guess I will spoil it for you after this. Can you spot it? The fans are mounted back to front. Look at this. This is the function gen here. And this is the oscilloscope. They're exactly the same brand and model fan,

**Dave Jones:** but one's sucking in, one's blowing out. Which is the right one? I don't know. Are they installing them just randomly on the like is it an actual assembly error? Or did they decide that no, we're going to, you know, suck the air in on

**Dave Jones:** one of them and blow it out on the other? I don't know. Uh Keysight, Daniel. Müller, Müller. Müller. And the brand of cap is literally okay cap. These caps are okay. Same branding on the output filter caps as well. They're

**Dave Jones:** okay, too. Anyway, it's a very neat and tidy power supply assembly. And yes, the output voltages and the output cables are exactly the same. I'm sure that I could completely interchange these and it wouldn't make a difference. I could

**Dave Jones:** like mix up these back shells and I wouldn't even know when I put this back together. But yeah, it's got no shortage of output filtering. A TO220 is flapping around in the breeze here, but you know, um someone had fun with the

**Dave Jones:** silastic gun. Um but you know, yeah. It actually looks like a decent layout. Keysight almost certainly didn't uh design this as most companies don't. They just farm out their power supplies. But yeah, no, it looks nice. We've got a

**Dave Jones:** nice spade lug going down to the chassis down here. No wackers. Everything's all heat shrunk. We've got input fuse in here. We've got a PTC there, do we? X and Y class caps or your common mode chokes, all the requisite stuff. No

**Dave Jones:** worries. I mean, it's only like, you know, a 30 W power supply or something. All right, let's take a look at this board, shall we? I'm actually capturing my 4K screen this kind of time instead of my regular 1080 screen. So, let's

**Dave Jones:** have a squeeze. You can see that we've got the Cyclone 10 FPGA in here. And no surprises for finding that. Part number for those playing along at home, there's many varieties of the Cyclone 10 series. You can pay, well, I'm not going to say

**Dave Jones:** peanuts, but you can pay like orders of magnitude difference in price depending on the amount of silicon and feature set in there. So, I don't know what that one is and not really that fussed. Bit weird to see the old Intel inside symbol on

**Dave Jones:** there. Yeah, so anyway, that is surrounded by some memory here and up here as well. We've got our controlled impedance wiggle wiggle wiggle yeah traces all in here and also going out to our DAC out here. Ah, bloody orphan view can't do multiple

**Dave Jones:** level undoes. That sucks. Anyway, for those who don't know, all of these wiggle traces here, these are of course matched length. So, when you're talking about the speeds going to DDR memory these days and in this case going to the

**Dave Jones:** DAC, then yeah, you've got to match the length of the lines. So, this trace that goes all the way on the outside here, that has to match that which goes further. So, that's your longest one and then your shortest one goes from well,

**Dave Jones:** you know, like into here like this. So, they've got to match the length there and overall those two lengths will be matched. So, your skew, your data skew and your clock skew and everything else, your timing is pretty matched

**Dave Jones:** with the distances even with the small distance was we're talking about between the chips there which isn't much but still it matters once you get up in speed. Yeah, so I'm not sure what speed the memory would be operating there.

**Dave Jones:** Your guess is as good as mine. I mean, this is only a 20 MHz uh bandwidth thing. So, the TX DAC here but of course you've got a 20 MHz clock cycle you've got to be spewing out more data than

**Dave Jones:** that. So, the data rate is high. That's why all that stuff in there has to be matched. And the AD9747 here, that's a dual 16-bit 250 megasample per second DAC. So, as I said, yep, it's pretty quick and then

**Dave Jones:** they've just got some drivers here of course. We can go in and have a better look at those numbers there. 51 661. I think these might be Intercil uh EL5166s. So, yeah, which is now Renesas. Um and they're 1.4 GHz bandwidth current

**Dave Jones:** feedback amplifiers. Yeah, that would make sense in that sort of application. And with this be some offsetting? I don't think that's local regulation. Not sure what the deal is there. Anyway, they're going into some relays and attenuator networks down there to get

**Dave Jones:** your uh various low output signal levels and whatnot. And then your extra stuff down here, these are your two output BNCs. You can see there's a bit of residue on the connectors there. They're hand soldered, so a little bit how you

**Dave Jones:** doing, but it's neither here nor there. Um and then of course there's your 50-ohm um output impedance there. And it looks like they have dual drivers there with 100 ohms in series each, and they parallel Looks like they're paralleling

**Dave Jones:** those up. So, you can see them joining at the output here, and they've just got some output filter in there. You can see a couple of little chokeys down in there. Um but yeah, that's interesting. They're They've paralleled those up, and

**Dave Jones:** you can see Look, the Here's the output of the uh the attenuator network, and then that's going and that's splitting into the two sides here. So, they're paralleling those up, presumably uh to get extra grunt um out of that. You

**Dave Jones:** wouldn't be getting extra Like they wouldn't be Of course, you can parallel um the amplifiers for reduced noise, but I I don't think this is a stellar performer in that regard. So, they're doing that for extra output grunt. And

**Dave Jones:** there's your PLL clock gen. Uh that's an LMX2582 for those playing along at home. Uh 10 MHz reference there. Does this accept? No, I don't think this accepts an external 10 MHz input. I'd have to check that. But yeah, that's the PLL clock

**Dave Jones:** driver for everything. But apart from that, not much else doing. And this is our calibration output here. We've got a 74HC4051 jobby for the win. Old school. Old school again, TL072. Love it. Don't know what that analog devices jobby there is.

**Dave Jones:** This here is a ground connection. Very nice if you're designing a product like this. It's a very appreciated to designing little ground loops like that. They don't cost much and you can put your oscilloscope probe in there and very handy for getting

**Dave Jones:** there and probing during debugging. And this here is our trigger gate burst. Well, that includes all the circuitry there. And then this is our sync output here, which is nothing. It's just got a like a transistor driver on the output

**Dave Jones:** and that's it cuz all it does is trigger output pin. That's it. No workers. And got some other op-amps here, TLV274s. I don't know what they're doing. They don't seem associated with anything in particular, at least not on

**Dave Jones:** the top layer anyway. Meh, whatever. Just that some housekeeping op-amps. Then of course, you got all your regulation stuff up here. Good old old school 7905 for your negative 5 V regulator. 7915 up here. 7815 and 7805. So, we got plus minus 5 V

**Dave Jones:** rails and plus minus 15 V rails for the op-amps of course. Very nice. You want the headroom on the op-amps. So, yeah, that's interesting because that mean this is linear. So, the output of the power supply, that must be not plus

**Dave Jones:** minus 12 V as I mentioned before. It must be like at least there's got to have at least a 2-V dropout voltage on that. So, it's got to be like plus-minus 18-V or something like that would be my guess. You want to

**Dave Jones:** keep it down so the dissipation in those isn't much, but you know, yeah. There you go. Anyway, there's another switching rig there. That's probably for like a 3.3-V. Another Well, there's another linear rig. There is that another switching

**Dave Jones:** jobbie and the one that's left out. There you go. They've left out another one. I don't know. Miscellaneous circuitry, but yeah, like there's not much in it. There's a Cyclone 10 FPGA, some memory, a DAC, you know, output

**Dave Jones:** dividers, output drivers, and then just some calibration and sinky stuff and a clock gen and Bob's your uncle. Although, what is driving the screen? But, of course, you got to have something to run the operating system and there's our arm

**Dave Jones:** jobbie there. It's an STM 32H750. And it's got its own associated memory and everything else and that it has its own PLL as well happening there. So, yeah, that that fuse half-amp fuse is gone. It's gonski. And then behind my head here, there's

**Dave Jones:** some unpopulated circuitry. So, that would have been and including a relay and stuff for what external gate output or something like I don't know. External No, that might have been like No, because it's got a relay. It's going

**Dave Jones:** to say like an external 10-MHz input or something like that, but no, I don't think so. Another unpopulated device there with a power pad on the bottom. It's got a thermal pad on the bottom. Got another test connector here. Um not sure what it's

**Dave Jones:** doing there. This would be going off to the touch screen, wouldn't it? And anyway, so this would have like video driver and everything Uh, built in. That looks like another switch mode controller that's doing something. Analog VDD, is it? Okay. Um, the power

**Dave Jones:** and fan connectors, nothing much doing. There's your real time clock. That's your 32 kHz, uh, clock, uh, crystal there. And that'd be And that the BQ, uh, 32002 would be an RTC, uh, clock chip. And there's your battery

**Dave Jones:** backup, of course. Aha, there's your video connection. That's on the bottom side of the board there. You can see some, uh, matched length, uh, traces going on in there, um, as well. And then you've got all, uh, series resistor terminator.

**Dave Jones:** So, that's yeah, there's got to I'm not going to I get the board out to flip it on the other side. I don't think there's a huge lot, um, a huge amount there, but that would be the, uh, surface mount,

**Dave Jones:** um, LCD connector, uh, going off. So, this would be the front panel, um, over here. That'd be like the front panel and, uh, controls and stuff. So, there you go. I just took a bunch of, um, high res, uh, photos and didn't

**Dave Jones:** decide to do the full 4K screen capture because my, uh, I could have done this under my Tagarno microscope, of course, but that's only, uh, 1080p. So, yeah, if I want to be able to And I don't really

**Dave Jones:** need to zoom in on stuff. But there you go. That's, uh, that's it. It's all pretty basic stuff. So, there you go. That's a teardown of the new whatever part number. I can never remember these bloody part numbers.

**Dave Jones:** Why can't they give them something decent? Um, I don't know. Anyway, it's some part number, um, 28 function gen. If you liked it, give it a big thumbs up. As always, discuss down below. Catch you next time.
