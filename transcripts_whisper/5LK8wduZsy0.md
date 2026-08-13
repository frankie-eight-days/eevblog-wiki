---
video_id: 5LK8wduZsy0
title: EEVblog #1005 - Keithley 2302 Battery Simulator Teardown
url: https://www.youtube.com/watch?v=5LK8wduZsy0
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 38, "3": 54, "4": 72, "5": 90, "6": 106, "7": 122, "8": 141, "9": 154, "10": 169, "11": 188, "12": 205, "13": 223, "14": 237, "15": 250, "16": 267, "17": 283, "18": 299, "19": 314, "20": 333, "21": 348, "22": 363, "23": 380, "24": 394, "25": 407, "26": 423, "27": 442, "28": 456, "29": 472, "30": 485, "31": 500, "32": 518, "33": 532, "34": 549, "35": 564, "36": 580, "37": 599, "38": 614, "39": 634, "40": 652, "41": 671, "42": 685, "43": 702, "44": 721, "45": 740, "46": 756, "47": 774, "48": 789, "49": 804, "50": 818, "51": 836, "52": 850, "53": 865, "54": 884, "55": 898, "56": 916, "57": 932, "58": 946, "59": 966, "60": 980, "61": 996, "62": 1014, "63": 1030, "64": 1048, "65": 1066, "66": 1080, "67": 1096, "68": 1118, "69": 1132, "70": 1148, "71": 1162, "72": 1178, "73": 1194, "74": 1210, "75": 1224, "76": 1242, "77": 1260, "78": 1278, "79": 1296, "80": 1310, "81": 1324, "82": 1342, "83": 1358, "84": 1378, "85": 1396, "86": 1412, "87": 1432, "88": 1450, "89": 1472, "90": 1492, "91": 1504, "92": 1522}
---

**Dave Jones:** Hi, I've got a real interesting bit of kit for you today that you don't normally see. It's a bit of special purpose test equipment from Keithley. We love Keithley gear here on the EEVblog. And I scored this puppy, and check it out, it's a fairly recent calibration,

**Dave Jones:** and it was sold as it just powers up. So, I have yet to test the thing. But it's the Keithley 2302 Battery Simulator. And what this thing does is that it basically, as the name implies, simulates a battery, any type of battery that you want, for use in product design.

**Dave Jones:** Because what it does is actually simulates the ESR, the equivalent series resistance, the ionic resistance. I've done many videos on this. I'll link in all my battery video playlists, which is quite extensive, down below, and at the end of the video in the outro as well.

**Dave Jones:** And it can simulate that equivalent series resistance output of the battery. So this is really important in product design, especially for products that require high pulse currents and things like that. Things like, you know, mobile phones that will draw big gulps of current when they're transmitting,

**Dave Jones:** and stuff like that. The ESR of the battery makes a huge difference. And the chemistry of the battery, there are some products that simply will not work if you power them from a low ESR, essentially a zero output resistance power supply. Because it's not simulating the battery, the energy can't get dumped back into the battery,

**Dave Jones:** and stuff like that. This is designed to simulate this. And it's a real expensive, special purpose bit of kit. I think it retails for about $5,000 or something like that, US dollars. It's still a current model. There are different models in the series that have, this is only the single channel one,

**Dave Jones:** I think there's like dual channel and other particular models available. But not only can it simulate that ESR, it can measure it as well. So it can actually measure the power consumption of your product under test, the current and the voltage. And it can also measure pulse current as well.

**Dave Jones:** So all the stuff people try to cobble together with, say, a microcurrent and an oscilloscope, and then you integrate it on the oscilloscope and do stuff like that, this can do it all built in. So really specialized bit of kit. And it really is quite a big beast like this, but it doesn't weigh much at all.

**Dave Jones:** There's hardly anything in it. So I expect it, like there's no big iron core transformer, so I expect like a switch mode supply or something like that. And if you have a look on the back, we've got your standard Phoenix contact connectors here

**Dave Jones:** for your output, two pins for the positive, two pins for the negative. So that simulates the battery, and then of course your sense line. You've got to hook up so it compensates for all of your cable loss. Because the last thing you want to do is simulate the series resistance of the battery,

**Dave Jones:** and you introduce bloody series resistance into the cable. That's just ridiculous. And it's got a separate DVM built in. I think it's like, I think it's probably just like a fixed 30 volt DC range, which is more than good enough. You know, it might be like a 5.5 digit meter or 6.5 digit or something like that DVM built in.

**Dave Jones:** It's got some relay outputs, so this is designed for, you know, production test automation, stuff like that. Your obligatory IEEE 4008 GPIB, and a remote display thing, so that you can stick this in a rack and have the display somewhere which is more user-operator accessible.

**Dave Jones:** USA! USA! So you know what we say here on the EEVblog, don't turn it on, take it apart. Yee-haw! Alright, so let's slide this puppy open. I love this. And you might be thinking, well, why can't you just use a battery in your product design?

**Dave Jones:** Why do you have to pay $5,000 to get one of these to simulate a battery? Well, you can, but yeah, it's just a lot of dicking around to use a real battery. And you can't just, you know, have like an almost dead battery.

**Dave Jones:** You can't just dial it up and say, look, show me what happens to my product when the battery's almost dead and things like that. This allows you to control it, get a plot, you know, get all sorts of characteristic performance curves and stuff like that

**Dave Jones:** as your battery dies, the performance of the thing. So yeah, an essential bit of kit, really, if you're serious about your product design. And we're in like Flynn. I like that. Oh, jeez, look at our huge board on the top. That's all your power MOSFETs under there.

**Dave Jones:** And they've got their little condoms on for our protection. So they look like just heat shrink. You might think, why would you put heat shrink in there when you should be putting thermal paste? These would be thermally conductive little tube things, so they just whack them in there.

**Dave Jones:** And they're not quite as good as a thermal grease, but they're pretty close. All right, let's take a look. One of the first things you'll notice is that up here we've got the different model options, the 2302, which we've got here, and looks like it shares the same board with the 2306 model.

**Dave Jones:** And clearly we have room for a second channel here. This top board is obviously the measurement channel, and we have room for the extra Phoenix contact connector there, plus basically a duplicate of the measurement circuitry here. It looks like it's a bit less circuitry there,

**Dave Jones:** so they've maybe got some more stuff tacked on here, but yeah. Oh no, no, it looks like they have it down here. You can see the traces snaking down like this, down to this unpopulated area down here. So hey, that's a bit... that's a bit of a pain in the butt from the...

**Dave Jones:** like, it's probably the PCB designer, went, oh, you've only given me this room, I need this amount of layout here for all this, and you want me to duplicate the channel. I don't have enough room, you haven't made the case wide enough, so I'm going to have to split this down here and have the extra circuitry down here.

**Dave Jones:** Bummer. But that might make a bit of sense, given that the extra MOSFETs for the other channel are down here. They're not populated, of course, and then this is the circuitry for the MOSFET that controls all the ESR, of course. That's how you would get a controllable battery ESR,

**Dave Jones:** is by using the on-resistance of the... controlled on-resistance of the MOSFETs to simulate the ESR. But yeah, why you wouldn't, from a first layout PCB point of view, like, whack this in the middle, like the heat sink in the middle, have the power transistors either side,

**Dave Jones:** and then have all the other circuitry going down like this, and then this tucked over here, we've got an unpopulated one over here, but, like, yeah, I don't know. Like, did they suddenly design, like, at the last minute, oh, we need a two-channel version,

**Dave Jones:** oh, let's just squeeze it in. I don't know. As a layout person, I wouldn't have put that there. I would have put it right in the middle. Symmetry. I like symmetry. So yeah, it looks like we've got some power supply stuff happening around here.

**Dave Jones:** We'll have a quick look. Looks like we've got some digital stuff happening in here, maybe. We've got a big-ass oscillator, or maybe that's the ADC, or something like that. Maybe that's the DVM front end. We'll take a closer look. Obviously there's another unpopulated power supply one here

**Dave Jones:** for the second channel. There's a display PCB down the front there, nothing really doing. That's the, you know, processor that controls it all. There's a separate display PCB in there for the vacuum fluorescent display. But, you know, apart from that. Anyway, all the top stuff is the measurement acquisition

**Dave Jones:** and load simulation board. The bottom board will be the power supply. Here's our power coming in from the bottom board. And also, a fair bit of digital. So there might be some processing. Yeah, all your processing's going to be happening down on the bottom board.

**Dave Jones:** Because, there goes your display down on the bottom board, not the top one. You'll notice this little crimp lug in there, that's actually a thermocouple. They've got two wires going off there to a little thermocouple amplifier over there. They're measuring the temperature of the heat sink.

**Dave Jones:** Very nice. But anyway, we're going to have four MOSFETs there. So that would be four MOSFETs there. They might be paralleling up the pairs or whatever. I don't know. We'd have to have a look. And we'd have to take it off to have a look at what parts they are.

**Dave Jones:** But yeah, just big beefy, you know, low voltage in channel MOSFETs. And that board just popped out beautifully. There's basically no active stuff on the bottom. It's all just passive decoupling and other, you know, some resistors and whatnot. And we're down into the power supply.

**Dave Jones:** And this has got a few interesting aspects to it. And it confused me at first glance. I didn't know what was happening. Now, look, a nice plastic cover here. So that just... Oh, whoa. I broke it. I broke it. Look, anyway, that just comes off.

**Dave Jones:** We've got our main processor down in there. We can have a look at it, but you know, whoop-dee-doo. We've got our mains coming in here. We've got a top-quality mains input filter here. Spared no expense at all. Really spectacular. Spared no expense. Spared no expense.

**Dave Jones:** Spared no, no, no, no expense. Oh, look at the beautiful earth down here with the shake-proof washer right down to the chassis and crimped properly. Oh, it's just, you know, crotch-moistening stuff. Speaking of which, oh, look at the rod in there. That goes all the way back.

**Dave Jones:** You know, I'm a big rod fanboy. But this is interesting. Down here, I mean, look, this is the digital section, right? Down here, look how close that is to the mains input switch here. It's just, like, I'm sure they've left their adequate clearance and everything else.

**Dave Jones:** It just looks so close. It's like, what are you doing? Now, if we follow the money here, obviously, look, this comes in, goes through our mains switch. Then where does it go? This is the output of our power supply. Like, where does it go?

**Dave Jones:** Here's our mains supply. Obviously, look, we've got our big mains choke up here. So let's flip it around, shall we? And have a look what's going on here. Here's our input mains choke that they've got there, the RFI choke. They've got some input protection happening there, so that's all good.

**Dave Jones:** But once again, look at this. Curiously, like, plus 5 volts D, which would be digital, plus 5 volts digital. They've got a common mode choke here. So it looks like 6.5 volts in, 5 volts out. They've just got a linear reg happening there.

**Dave Jones:** But look how close that is to the other mains circuitry. Once again, they've probably added adequate clearance, according to the, you know, the creepyjar standard and everything else. But it's just amazingly close. And it's obviously not coming through here. I thought at first it might be some, you know, capacity divider or something,

**Dave Jones:** powering that, but no, it's all just part of powering the digital stuff over on this side of the heatsink here. So obviously what they're doing is routing the mains from the power switch, probably under the back of the board, the backside of the board,

**Dave Jones:** and popping up into here. Because you can see some dark traces on the bottom, through the bottom of the board there, but that's... It's like layout! I mean, somebody just wasn't thinking about the layout and just hasn't adequately separated it. Like, from a technical point of view, it's fine, I think,

**Dave Jones:** but it's just rather puzzling why they did it like that. Strange. Anyway, that power supply is no doubt going to be absolutely first class. I might be able to take it out and take the cage off and have a squeeze, but not hugely interested.

**Dave Jones:** It looks like it's a fixed plus 12 volt DC output here, so they're just using the dual wires there for extra current handling capacity. So it looks like 12 volts is powering everything, and then of course that goes up to here, which is our main power supply generating the different rails.

**Dave Jones:** Obviously, they've got a second one here for the two-channel model, and they're absolutely identical. You can be able to see the differences, but it basically generates minus 15 volts and plus 15 volts B. This one's labelled A, and this one's labelled B, so minus 15, plus 15, plus 25,

**Dave Jones:** and minus 5 over here. Down here, it's just beautiful. We've got a HRC fuse down here, Sprague capacitors, Nichicon capacitors on the output over here. Ah, thing of beauty. I don't know how much that puppy would have cost, but it's worth it. Spared no expense in this thing.

**Dave Jones:** It doesn't matter. When you're building a $5,000 instrument, you don't worry about cost. It just, it essentially doesn't matter. The instrument, you know, the instrument bomb cost is what it costs. Oops, I forgot it also generates plus 5 as well. So plus minus 5, plus minus 15, and 25.

**Dave Jones:** So why have they actually rolled their own here instead of typically putting that into the mains power supply over here? Well, they'd be doing that for probably, ah, that they can control the efficiency better in this thing. They can control the pulse current capability,

**Dave Jones:** and they just want it, this is the one that you have to engineer very, very nicely, because you want, you know, incredibly low output resistance, and it needs to be engineered really a lot nice, right? This is a precision battery simulator, so you don't just want it, you know,

**Dave Jones:** left up to some third-party supplier who's designing your mains power supply over here to do that. Nah, bugger that. Now, look at this, this seems to be a bodged afterthought. Look, we've got, now this is interesting, check out this wire in here, it's all neat,

**Dave Jones:** they've cable tied it, they've heat shrunk it, everything else, but it seems to be an afterthought, because look, they've soldered in the wires down to like a surface, is that a resistor down there? Yeah, R112 is it, or is that that one? I don't know, but yeah, like they've,

**Dave Jones:** they've bodged in that, and they've taken that over to the mains power supply. Why? I have no clue why. That is puzzling. Of course, they didn't muck around on the heat sinking on these two MOSFETs here, did they? Look, it's just going the full length there, nice.

**Dave Jones:** And of course the thermals are very good on this, as you'd expect, the air is sucked in through the vent holes on the front here, so it comes from like, you know, the clean air in the lab, you know, because this thing would probably be rack-mounted, for example,

**Dave Jones:** so it's sucking the air in the front, and then it also goes over the top of the board like this, and then over through the thin heat sink, which has got the channel out, and the fin's going in that direction, nice, and then it blows it out the back.

**Dave Jones:** So, yeah, thermally, it's very nice. And the Motorola fanboys go wild! And the National Instruments ones too, you've got to have the National Instruments chipset for the GPIB. Genuine. That's fake rubbish. Ooh, Denzyl Lambda, thank you very much, certainly spared no expense on the third-party

**Dave Jones:** provider of the power supply. Look at that, oh, it's just beautiful. Look at, I love the angled heat sink on the back. Yeah, they've got the odd cap stuck between the heat sink, but they know what they're doing, this is Lambda for goodness sake.

**Dave Jones:** Anyway, that's beautiful. That's, you know, I wonder how much that would have cost them to, you know, they weren't penny-pinching when they got them to design that mains power supply. Gorgeous. And Nichicon main DC filter cap, of course, and the output ones. Nippon Chemicon, thank you very much!

**Dave Jones:** Best you can get. Alright, let's go and have a look at the more detailed circuitry here. Let's just zoom straight into this section over here, this little isolated section with the big crystal oscillator. See what's what. Alright, this looks for all the world like a

**Dave Jones:** Keithley custom multi-slope integrator, like you see in the Keithley high-end DVMs, except this one's probably not going to be as good, it just doesn't have the same huge requirement, but you can see the PLCC package up there, it's some custom part number for Keithley,

**Dave Jones:** so it's probably like a custom embedded PLC, PLD type array, which is implementing their multi-slope integrator circuitry, and you can see the voltage reference down in the bottom right corner as well, multiple packages there, but this one just uses a buried Zener reference, just the

**Dave Jones:** Zener diode reference, but they could have put a more high-spec unit in there, so they're just hedging their bets there. Alright, let's jump straight in and take a look at these power MOSFETs here, and here we go! We're in like Flynn, look at this, IRFP

**Dave Jones:** 9140s, a genuine international rectifier, none of this, these wouldn't be fake rubbish you can buy on eBay, no sorry Bob. These are P-channel MOSFETs, guess what, the other two are going to be on the other side, they're going to be probably N-channel MOSFETs,

**Dave Jones:** so these are 100 volt jobbies, 23 amps, 0.117 ohms, not the lowest RDS on, but they don't have to be, because this unit is capable of going from basically 0 ohms ESR, right up to 1 ohm actually, in 10 milliohm steps I believe it is, based on the

**Dave Jones:** specs. So, how can you use a 0.117 ohm one, even if you parallel these two, which they're probably doing, to get that 0 ohm output impedance? Well, it depends on where it is in the feedback loop for that, just like a regular power supply PSU

**Dave Jones:** can have 0, effectively 0 output impedance because it's where it is in the feedback loop, it's just compensating for that, so this'll be in there, there'll be some sort of step response that allows them to progressively increase the on resistance of this thing.

**Dave Jones:** Just basically based on the voltage drop across it. And, of course, the other matching MOSFETs, yep, they're N-channel, of course. These are Vishay ones, IRFP 240s, and once again not particularly low on resistance, you know, not the lowest in the industry, but they're nice

**Dave Jones:** big, beefy power transistors so you can't blow them up, and once again, I believe they'd be operating these in parallel to get extra power handling capability. Well there you have it, they're not in parallel, if you take a look at the bottom side of the

**Dave Jones:** board, you can actually see the arrangement, or at least you can see the bottom side arrangement there, they're clearly in series, both the P-channel ones are in series, source connects to drain, or drain connects to source on one of the P-channel pair, and same

**Dave Jones:** for the N-channel pair as well. Hmm, curious this is. And then you can see that they're directly connected into those CADIC TO220 package power resistors there. And let's go in to near the inputs over here, and we'll find that along with the MOSFETs of course, we've got to have the current

**Dave Jones:** sensing resistors for this thing, very very important, so expect to find some pretty schmick ones down here, let's have a look. Well it doesn't get any more schmicker than this, spared no expense, alright, look at this, it's a Isabellenhut I can't pronounce that,

**Dave Jones:** it's German, these are German four terminal resistors, like a 10 watt job, so they've got the sense terminals built in and the low PPM, everything else, and manufactured by Nude Virgins. And right behind that beautiful one we've got some CADICs, look at that, four CADIC ones, they make good

**Dave Jones:** current sense resistors as well, 0.2 ohms each, my guess is that they're gonna with that oddball value, they're gonna have two of those in parallel, so they're only 1% jobbies, but it doesn't matter about the accuracy as I explained many times before, it's all about

**Dave Jones:** how many PPM they are. And there's one little current sense resistor left that's that brown looking Dale one, their Dale makes some great resistors as well, so no expense spared. This 100 ohm jobby, being 100 ohms that'd be for the 5 milliamp current range, whereas the other ones would be for

**Dave Jones:** your 5 amp range, and we've also got some input protection, you've got to have that, so reverse protection with the big diode, leaded axial diode there, and also this API 5 amp bridge rectifier as well. And we've got a couple of power trannies hidden

**Dave Jones:** away there, they're IRFZ44 for those playing along at home, a low RDS on job, they're probably switching in the 5 milliamp range or something like that, but yeah, there's a couple of extra MOSFETs here and there. And of course the rest of the supporting circuitry, we're just gonna

**Dave Jones:** have a lot of schmick op amps, like that DIP package there, it's prominent, why have they used DIP? Well it's an LT122300 current feedback amplifier only available in DIP package for the win, none of that surface mount rubbish. And here's something that I

**Dave Jones:** didn't expect to see, look at this other DIP package, it's a Mikra, or now owned by Microchip, the Mik 5021, this is a high-side current sense MOSFET driver, so specifically designed for current sense applications like this, but it's you know, I wouldn't have expected

**Dave Jones:** in this type of application, it's voltage is 12 to 30 volts operation, it doesn't seem to fit, and look at this physical location it's way away from the current sense resistors and the MOSFETs over there, so I need to be curious to trace that one out and get a schematic for this.

**Dave Jones:** I can only imagine that they're using that maybe for a gross current overload, you know, maximum overcurrent protection thing for the MOSFETs, or something like that perhaps. And another part I didn't really expect to see, a video op-amp here, Analog Devices AD 818, you can see

**Dave Jones:** three of those in there with the prominent white silk screen there so yeah, maybe it was just the designers, you know, jelly bean go-to op-amp for some reason. And hello old friend, down in the bottom left-hand corner there, the Analog Devices AD 620 instrumentation amp

**Dave Jones:** I've used that one a lot, and it's a nice little instrumentation amp, it's well, low cost in quote marks but yeah, for a precision instrumentation amp it is. No surprises for finding an in-amp in here. And of course, as always in a design

**Dave Jones:** like this, you're going to find a smattering of ultra-precision operational amplifiers we've got the OP177s they're scattered in various locations across this, so yeah, no surprises you're going to have a bunch of those, and you're going to have a bunch of, yeah, there's LM393s

**Dave Jones:** and there's other, you know, jelly bean type stuff. So I won't look too much further. And I'll just leave you with a choice smattering of high-res photos here for the other power supply section, and as always, the high-res photos are down on EEVblog.com, linked down below

**Dave Jones:** if you want to check them out yourself, and because I actually use a macro camera, as I'm tearing something down I use a macro lens camera, take some photos and I always upload them on EEVblog.com. Anyway, fun. Look at all this. It's wonderful.

**Dave Jones:** You can smell it. Smell the quality. Oh, yeah. So let's just power this puppy up. It's like a jet engine taking off. Jeez, that fan has not got any temperature control on it. The vacuum fluorescent display is a bit low. There you go.

**Dave Jones:** This puppy's a little bit old, but you can see that we've got our voltage and our current there displayed, and then we can choose display type, actual voltage and current. So there you go, and we've got our DVM input separately, and there's the pulse current

**Dave Jones:** I was telling you about, if you want to measure the pulse current of your product, and you can do long integration. You can set the integration time over that it actually calculates the current, and stuff like that. So it's very simple. We can set the GPIB address,

**Dave Jones:** we can set our current range, so let's go in there and 5 amps, auto, 5 milliamps, so we can really get right down if you're doing low power products, and we'll definitely have to do a video on this showing you actually measuring the

**Dave Jones:** current, and maybe compare it to an integrated oscilloscope value perhaps. Anyway, so it's only got the two ranges, 5 milliamps and 5 amps, so it'd be a real bugger if your product drew 10 milliamps for example, pulse current, and then you had to go to the 5 amp range and lose

**Dave Jones:** all that resolution. Unfortunately, there's just nothing you can do about it. It's really, you know, you really need a current meter like this with many, many different ranges. So number of power line cycles that it takes into account, average readings, save and recall setup, pair on setup,

**Dave Jones:** calibrate, voltage protect, current limit mode, so you can protect your product under test, revision number, VFD brightness, oh yeah, thank you very much, full, oh. We're already on full, damn it. Anyway, unfortunately we won't see anything if we operate this, because it'll just show random voltages

**Dave Jones:** because we haven't connected anything, the sense line isn't hooked up so it's just high impedance loading, etc, etc. But hopefully we can play around with this in a future video, we're going to have some fun. So anyway, there you go, hope you found that

**Dave Jones:** interesting, that's a teardown of the Keighley 2302 battery simulator. Definitely not something that you get to see every day. Anyway, high res teardown photos down below on eevblog.com, LinkedIn, and also check out somewhere over here at the end of the video will be all my battery playlist

**Dave Jones:** videos, I've got a whole ton of them. And if you like the video, please give it a big thumbs up. Catch you next time.
