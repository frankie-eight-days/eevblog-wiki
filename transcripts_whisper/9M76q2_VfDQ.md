---
video_id: 9M76q2_VfDQ
title: EEVblog #1253 - LED Flicker 2: Electric Boogaloo
url: https://www.youtube.com/watch?v=9M76q2_VfDQ
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 25, "2": 54, "3": 83, "4": 106, "5": 123, "6": 142, "7": 159, "8": 180, "9": 200, "10": 220, "11": 238, "12": 256, "13": 269, "14": 291, "15": 314, "16": 335, "17": 354, "18": 378, "19": 394, "20": 412, "21": 430, "22": 450, "23": 466, "24": 493, "25": 511, "26": 531, "27": 547, "28": 558, "29": 577, "30": 596, "31": 612, "32": 633, "33": 650, "34": 667, "35": 680, "36": 696, "37": 716, "38": 730, "39": 752, "40": 769, "41": 782, "42": 805, "43": 816, "44": 833, "45": 852, "46": 868, "47": 886, "48": 893, "49": 906, "50": 923, "51": 939, "52": 959, "53": 969, "54": 983, "55": 1000, "56": 1018, "57": 1035, "58": 1051, "59": 1064, "60": 1076, "61": 1090, "62": 1100, "63": 1122, "64": 1130, "65": 1148, "66": 1166, "67": 1185, "68": 1195, "69": 1213, "70": 1232, "71": 1243, "72": 1259}
---

**Dave Jones:** Hi, quite a few people asked for a follow-up to my LED flippering video, linked in down below at the end if you haven't seen it, and you should, where I tore down one of these dodgy, cheap-ass, bottom-of-the-barrel, constant current panel drivers here, and how it was causing bad flickering on my LED panel lights, and basically it was like 100% ripple on the output.

**Dave Jones:** And then I compared it with a ripple-free or flicker-free one. Granted, this one is twice the power, 48 watts versus 24 watts, but still, the cause was, of course, the lack of any output constant current regulation here. Constant current regulation is done from the primary side, and not only is there a lack of output filtering here compared to over here, but there's also a lack of input filtering, which might cause an issue as well.

**Dave Jones:** So, anyway, let's do a follow-up and see, quite a few people wanted to know how we could improve something like this, or how we could hack it to fix it. Now, I wouldn't recommend hacking these to fix it, because there's a lot of design considerations, thermal considerations with your diodes, for example, thermal considerations with your transformer and other things that you really don't want to mess with, because these things are cheap.

**Dave Jones:** I just recommend tossing... I just recommend tossing something like this in the bin, and just getting a non-flicker-free or a ripple-free version of it. But anyway, let's just do some experiments with this and see what's what. Now, quite a few people commented that the input filter cap in quote marks was only 4.7 microfarads, and it was only a 50-volt jobby.

**Dave Jones:** Well, if it was a 50-volt job, and it was directly across full-wave bridge rectified mains, it would be toast. It would explode straight. But it's not actually across the mains. It's not doing the filtering. It's, well, it's filtering, but only for the controller chip.

**Dave Jones:** So here's the capacity here. Here's the full-wave bridge rectified diode after it goes through the common mode choke here. You can see that it goes through these two series resistors here. So there's nothing in the chip data sheet that says that has, like, an internal Zener to, like, clamp the voltage or anything like that across there.

**Dave Jones:** So it's actually getting... It's power from the feedback coil here, which goes through this diode and then to the chip. So it's using that after it boots up to regulate the voltage across there, which will be the chip maximum is 40 volts in the data sheet.

**Dave Jones:** So it's something under 40 volts. So a 50-volt rated cap is fine. So that capacitor there has absolutely nothing to do with the input filtering. The only input capacitors we have are these two here. And they're... They're basically being used as a... As part of the common mode choke.

**Dave Jones:** Yeah, there's not much to it. For those playing along at home, both of those are 150 nanofarads. So two of those in parallel, well, yeah, 300 nanofarads. Not much. So a lot of people said, how about we just whack a big, of course, high-voltage rated filter cap on the input?

**Dave Jones:** Because, yeah, sure enough, for the load that we've got, then this amount of input filtering is going to do bugger all. So all your ripple is going to happen on your high side here. Well, okay, well, let's experiment with that. First thing we'll do is actually measure this bridge, the output of the bridge rectifier here, and see what our ripple is.

**Dave Jones:** And because we're measuring the ungrounded primary side of this instead of the isolated transformer secondary, you'll blow up your oscilloscope if you try and probe this side. So you need a proper high-voltage. So you need a proper high-voltage. High-voltage probe, available in the EEVBlog store, of course.

**Dave Jones:** Anyway, so we'll use this baby, and we can safely probe anything on the primary side here. So we'll probe directly across the output of the common mode filter there. I've got this set to my divide by 100 range. Of course, you set your scope to divide by 100 as well for your probe.

**Dave Jones:** And there we go. And we can see that we have a maximum peak there of 340. And we can see that we have a maximum peak there of 340. And we can see that we have a maximum peak there of 340. And bingo, look at that.

**Dave Jones:** We've got ourselves a full-wave rectified jobby. Of course, it's 100 hertz. It's full-wave rectified. So there you go. This is at the full 20-watt output load or whatever it is. So, yep, that 300 nanofarads, it ain't doing much, is it? But the good thing about having a small amount of input capacitance is that you're going to have a good power factor.

**Dave Jones:** And this thing, well, this chip, anyway, is designed or advertised as having good power factor. And that would be probably a requirement to get that New South Wales government contract. You couldn't have a poor power factor converter, most likely. I'm just guessing. I haven't looked into the requirements, legislation, and all that sort of crap.

**Dave Jones:** Just over 24 watts there. There you go, 245 volts here in the lab. It is near to as high side as you can get. Anyway, we've got 140 milliamps, so let's go PF power factor, 0.95. That's not too shabby at all. Any bureaucrat's going to be happy with that.

**Dave Jones:** So that low power factor is going to be a combination of the low input capacitance here, plus power factor features of the chip there, which switches things at the zero point and stuff like that. So if we put our output toroidal so we can measure the current,

**Dave Jones:** we've got our current waveform there, at 200 milliamps per division. In fact, I've got that AC coupled, so we'll change that to DC. And you can see that there you go, there's the ground point. So it's 100% ripple, pretty horrible. So let's try a few experiments, add some input and output caps in various combinations,

**Dave Jones:** and see if we can improve that without killing our power factor. Okay, let's try some extra output caps. Not a huge increase, but we had a 330 mic, 50 volt before. We'll add a 470 mic, 50 volt before, salvaged from another bit of gear, of course.

**Dave Jones:** Hope I got the polarity right. If not, well, could go, whoop, there we go, look at that. We have improved it a bit. It's not going 100% to zero now, you see. It's improved it, not by a huge amount, but you know. And that really hasn't changed our power factor at all.

**Dave Jones:** And as I mentioned, thermals on things like your diode here are going to be a potential issue. So I've removed the output filter cap. I've had it running for a bit. Let's get the thermal camera on there. What do you know, the hotspot is that diode, and we're talking.

**Dave Jones:** Yep, 74, and rising. Maybe I haven't left it on there long enough, but it's, yeah, it's getting up there. Let's call it 74. Let's go overboard, 2200 mic, 63 volts, thank you very much. And bingo, there is our current waveform, sorry I've taken off the voltage probes.

**Dave Jones:** But you can see, it's much further away from ground now. So yeah, it's not, what is it, 50% ripple now instead of 100%. And by the way, we're still drawing 24 watts there. And let's have a look at our diode, our little diodee there.

**Dave Jones:** She's about the same, so there you go, there's no more stress on that diodee. Transformer is not. I, trust me, it's really not hugely hotter. So huge amount of increased output capacitance there, practically an order of magnitude increase. And pretty much overkill, like, you know, that is, you wouldn't make it that big on

**Dave Jones:** a 24 watt panel like this. And it's still got, that's still like 50 odd percent, that's terrible Muriel. And no surprises for guessing, that hasn't changed our power factor. So we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more, a little bit more, and we're going to put in a little bit more.

**Dave Jones:** fixing the output capacitance like this, because we've got no secondary side conversion over here. Nothing. It's all done via the primary side, and we've got bugger all input capacitance. So let's add some input capacitance over here and see what's what. Once again, we're going an order

**Dave Jones:** of magnitude. You've got to love orders of magnitude in engineering. Nippon Chemicon for the win. Once again, salvaged from an old board, and you should always have like scrap boards lying around so that you can salvage parts like this, because not everyone's going to keep like a component bin

**Dave Jones:** full of various size and rating caps like this, especially on the mains input side, unless you're working on that sort of stuff daily. But okay, I found a hole to put that into. Unfortunately, the pitch wasn't correct, and there's not enough clearance around there.

**Dave Jones:** Let's put a jumper over. Definitely got that correct. That's a negative on the board. Bridge rectifier, and I've confirmed that with the voltmeter as well. That's going to the negative of the cap. Don't want to screw the pooch on that one. Anyway, let's power that up and give her a

**Dave Jones:** ball. Oh, and by the way, I've disconnected the output cap again. So we're in the original configuration, just adding 33 mic input capacitance. And ta-da! Look at that. That fixed it like a winner, winner, chicken dinner. No worries whatsoever. And our output ripple is pretty decent.

**Dave Jones:** And look at our input voltage. Look at that. There's not, you know, there's a bit of ripple on that, but no worries. You know how it was going almost down to ground before, because there was only 330 nanofarads there. So the input capacitance is

**Dave Jones:** the, well, it fixes the problem. And our output ripple is really quite nice, even with the original, uh, was it 330 microfarad output cap. So we're still drawing our 24 watts. But our power factor, uh, wah, wah, wah, wah. Thanks for playing. It's dropped down to 0.58.

**Dave Jones:** That is a horrible, horrible power factor. So really from the utility, you're drawing almost double the amount of, uh, current through the network copper, even if you're not being charged for it. I've done a whole video on that, linked in at the end and down below, if I remember to do it.

**Dave Jones:** Um, that's really bad. And the, if the government knew about that, uh, well, probably wouldn't approve. So you might not be able to sell that, uh, with a power factor of 0.58 or, you know, under 0.6. That's pretty terrible compared to what 0.95 or whatever we

**Dave Jones:** had before. So yeah, that fixes our flicker problem essentially. And I turned off my studio lights. And as you can see, can't get any, pick up any real flicker on this anymore. Whereas if I look at the lights up there, they're the existing ones.

**Dave Jones:** I'll switch my main lights on. There you go. This one ain't, cause we're getting, you know, not much ripple on that. It is still, if you had decent measurement, uh, gear, you know, you could measure the, uh, flicker on that, uh, probably, but you know, it's, it's basically fixed.

**Dave Jones:** It's low ripple. Once again, the output, uh, bridge rectifier there, 75, the, uh, the main switch in chippy down in there, even though it's on the backside of the board, bridge rectifier there, neither, we're talking about the center spot there. It's neither here nor there.

**Dave Jones:** And our tranny under the bottom, it's doing all right. So really, uh, the only effect of, uh, increasing the input filter cap is not only, uh, you make it physically, uh, larger, of course, more expensive increases your bomb costs, but it kills your power factor and that could

**Dave Jones:** kill your lucrative government contract. And if you think that the, uh, flicker free version, uh, solves the problem by input capacitance, nope, it doesn't. There you go. It's a little piddly. You can barely see it, but 4.7 microfarad, 400. Volt there. It's solving it because it actually does proper secondary side current regulation

**Dave Jones:** over here. Quite a significant topological differences between these, this one and this cheap ass jobby. And if you want to know what the power factor of, uh, this particular one is, it's even better than the other one. 0.974. Thank you very much. Now, of course we could try and

**Dave Jones:** correct this power factor correction problem by, uh, but passive means, uh, using some inductors, uh, for example, but it's kind of like polishing a turd pretty much because we don't know, uh, the, what impact this, these mods have had to the efficiency of something like this.

**Dave Jones:** We saw that potentially the, uh, main switching debate IC is potentially getting hotter. There's internal losses in the switching transistor and stuff. Don't know what's going on there. You'd have to have to characterize the whole thing. And it's just, no, you are polishing a turd and you could do it as a,

**Dave Jones:** uh, academic exercise, of course, but as a practical solution, no, it's just easier to go out and buy a proper flicker free version. Now I actually found this, uh, TI part, which is a TPS 92, 3, 1, 4 for those playing along at home.

**Dave Jones:** And it does look to be a near identical part to the on bright one. In fact, the look at the typical application schematic, it's practically identical and it's got all the same stuff, offline primary side sensing controller. But this one says, uh, with a PFC or power factor correction.

**Dave Jones:** Now with inherent in it, when they have to use the word inherent PFC, it means it's, it kind of does PFC like our existing design here. It actually had a good power factor correction because it does inherently do that, but at the expense, but

**Dave Jones:** because it's a single stage converter, it's essentially going to have that trade-off limitation between your output ripple current and your power factor correction. So, you know, it's, it's not that great. So if, but this part, the good thing about this is that look, there's a few extra things in here.

**Dave Jones:** See, it's got some additional clamping across the primary side, uh, transformer tap here. It's got a, uh, Zener diode clamped, but it's essentially the same. We've got our auxiliary winding here and just a single, uh, half wave rectifier output. And it does exactly the same thing.

**Dave Jones:** It's got all the same stuff. It's got quasi resonance switching and you know, all the same stuff. So it's got all the same stuff. So it's got all the same stuff. So it's got all the same stuff. So it's got all the same stuff.

**Dave Jones:** So it's got all the same sort of stuff that the, uh, on bright one says. And if we have a look and it does actually have a complete schematic down here, uh, well, you know, a complete application example, uh, schematic, we've got some additional,

**Dave Jones:** uh, filtering in here, but apart from that, that looks pretty much the same. Here's the compensation capacitor down here. And that value there does the, or attempts to do the power factor correction. So maybe we could tweak something like that on our on bright, uh,

**Dave Jones:** blind perhaps, but, uh, we don't have the relevant data sheet doesn't have the relevant information on that. And it's given us a typical output, uh, capacitance figures as well. Once again, uh, input capacitance is only 47 nanofarads. And the good, the other good thing is that it

**Dave Jones:** lets us calculate the output capacitance and ripple. So it gives you the example here of, uh, for 30% ripple current, which is a heck of a lot, right? And you still need 400, 480, you know, 470 microfarads, uh, on the output. And that still gives you 30% ripple current.

**Dave Jones:** So yeah, you get your nice power factor correction, but your ripple, it sucks. So really, if you want to do this properly, you need a two stage converter instead of a single stage converter. And you might get something, this is maybe a bit overkill.

**Dave Jones:** You can get low cost ones in this, but this is a, the LM 3450, for example, is a lead driver with active power factor correction. None of this inherent power factor correction. So you can get a lot of power factor correction, rummage, and, and you can do a phase dimming.

**Dave Jones:** So you can do like phase control, uh, dimming of the thing as well. And, uh, you can implement it as a single stage or a two stage design here. And here's the, basically, this is what we're doing here. Here's our secondary lead driver.

**Dave Jones:** And that is essentially what I said of having the constant current regulation on the secondary side. You're doing it as a second stage. And this does active power correction. So you can do some active power factor correction. You'll notice here's the main switching FET down here,

**Dave Jones:** and they've got another switching FET here that is doing some active power factor correction. So this is the puppy you want if you want to do it properly. But of course, it's much higher cost than the simple single stage solution designs. Internal block diagram, but pretty comprehensive

**Dave Jones:** and complicated. We won't go into the details. This is not, uh, the place to do it, but you can actually implement it, as I said, as a, just a single, you know, this typical, uh, single stage design, typical flyback application like that. And we won't get into power factor correction

**Dave Jones:** because I've done that in another video. But suffice to say, this one uses active power factor correction. And here you go. They specifically tell you single stage design, low cost downlight. So you want the high end downlight, you go for the two stage design,

**Dave Jones:** which is more expensive. And here's the two stage lead driver. Look at this. It's even got soft start, fantastic. We've got, uh, EMI filter up here. Very nice. And then we've got all the active, uh, power factor correction and drive. We've got control feedback.

**Dave Jones:** And then we've got the second stage lead driver here. They're using, and of course they're pushing their own parts and I'm, uh, 3409, but you can use any constant current, uh, lead driver you like. And that just inherently gets rid of all the ripple and it solves the problem.

**Dave Jones:** And here's your opto coupler feedback here, but that's expensive. As, uh, it said in the on bright one, I think you need the opto coupler. You need an LM. V four, three, one typically. And then you need to buy the, uh, constant current lead driver.

**Dave Jones:** And well, there, there's some extra stuff for dimming if you're doing that, but all of that adds significant costs as well as the active, uh, power factor correction, uh, stuff adds very significant costs. You could easily triple your bomb cost or something like that by, uh, adding

**Dave Jones:** in these parts. And by the way, this schematic might look a bit weird. It might look like all this stuff is physically on the primary side, but it's not, you will notice V out here. It is connected to V out here, which is on the isolated side of the transformer.

**Dave Jones:** So they just didn't have a landscape format schematic. So that's just a good, well, a poor example of laying out a schematic. Well, you, you kind of, I, I would have like physically put some dashes down here to sort of like, you know, show that it's primary side, secondary side.

**Dave Jones:** I would have added that, those, uh, notes to the schematic there, but anyway, yeah, two stage output current regulation. So as for our on bright turd here, well, you know, it's, it's probably equivalent to that, uh, TI, uh, part. You're not going to get any better.

**Dave Jones:** Once again, there is that compensation capping there. So you could try and experiment with that. And they've got some detail on that. The duration of the turn on period T on is generated by comparing the internal fixed sort of way with the voltage on the, uh, comp pin during steady state operation voltage on

**Dave Jones:** the comp in V comp is slowly varying due to a large external capacitor connected to the comp in there for the turn on. Time T on is constant in a flyback topology, which is what we've got, uh, constant turn on time and quasi resonant operation provide higher power factor and low THD.

**Dave Jones:** Yeah. Okay. How do we calculate that? They don't tell you. No, there's just, there's, there's nothing in here. There's nothing in here to tell you how to calculate that compensation capacitor, unlike the TI document. So, you know, what are you supposed to do?

**Dave Jones:** Like, yeah, you can just suck it and see. I don't know. I'm not going to polish this turd. It's done. And just like get a proper flicker free one. Yeah. You can probably shoehorn this thing to work, but no, I don't recommend it.

**Dave Jones:** As I said, you'd probably have to do full characterization. Again, I wouldn't want to put these things up, you know, a dozen of these things up in my roof that are hacked and just, oh, it's, it measures okay in the bench when you put it up on the roof and the

**Dave Jones:** overheats and does what it, no, no thanks. No, no, just don't do it. So I hope you like this, uh, relatively. Lovely quick second video looking at this again. If you did, please give it a big thumbs up as always. You can discuss it down below in the comments or over on the EEV blog forum.

**Dave Jones:** Catch you next time. . . . . . .
