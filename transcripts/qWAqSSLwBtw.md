---
video_id: qWAqSSLwBtw
title: EEVblog #1031 - $25 DPS3003 PSU Module Characterisation
url: https://www.youtube.com/watch?v=qWAqSSLwBtw
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video where I showed off this very cool DPS3003 power supply module. It's a complete lab power supply in a tiny little module like this. It's all fully self-contained and I'll link in that video down below if you hadn't seen it

**Dave Jones:** and it's a real cheap and easy way. It's like a sub $25 delivered for this module and you can turn it into a bench power supply. Just voltage in and voltage out. Fantastic. And here's the specs for the

**Dave Jones:** things just as a recap. 6 to 40 volts input. It is a buck only. So you have to have an input voltage range at least the dropout voltage greater than the output voltage range you want. The maximum voltage range you want is 0 to 32. So

**Dave Jones:** for example, if you only needed like a 12 volt 0 to 12 volt lab power supply, then you could get away with say like a 13, 14, say 15 volt input. Something like that. So output current 0 to 3 amps. 96 watts

**Dave Jones:** which I'm dubious about based on the you know, the efficiency of the heatsink in this thing. But that's one part of this video. I want to characterize this now cuz so many people said that they want me to characterize this and see how

**Dave Jones:** efficient it is over various ranges. So that's what we're going to do. Anyway, very nice 10 millivolt resolution, 1 milliamp current set resolution and adequate 0.5% you know, plus one or two digits voltage and current accuracy. So what do we need to characterize this?

**Dave Jones:** Well, you can do it with your multimeters. This is where I've always said having four multimeters is very handy in your lab because you can characterize not just modules like this. You can characterize your own design DC to DC converters. You can measure you

**Dave Jones:** have two multimeters for the input measuring the voltage and the current IE the power going in to your converter and then a 2 m measuring the voltage and current on the output, i.e., the output power when you've got input power divided by output

**Dave Jones:** power, you can get your efficiency. Uh so, you can plot efficiency curves over various voltages and whatnot. So, very handy to have four supplies, but we're not going to use multimeters today. We're going to use the Rigol DP832

**Dave Jones:** power supply. This is like 0.05% class instrument, so it'll allow us to know the input voltage we're feeding in and the input uh current as well. Near enough. I'm not going to bother worrying about like the drop across

**Dave Jones:** the leads here. It's like it's going to be near enough. Um this thing does have an external sense, so maybe I probably should take some wires around the back. I don't know. Anyway, and we've also got the Rigol DL3021

**Dave Jones:** uh DC electronic load. And electronic load, I've done videos on do-it-yourself electronic loads. You can build these really cheap. You don't have to spend, you know, 500 bucks for a commercial one like this. But once again, very accurate, 0.05% class,

**Dave Jones:** measuring the output voltage and the output current as well. And this one I do have the sense output. So, I am feeding that directly back to these terminals. I'm not going to worry about the once again the drop across these

**Dave Jones:** output cables here. It's you know, it's going to be near enough cuz we're not going up to particularly high currents. Anyway, I've enabled the external sense there. And if you want to know uh what the dropout voltage is with no

**Dave Jones:** load. Anyway, I'm feeding 32 V in and I'm getting a maximum of 31 V out of this thing. So, that's not bad. 1 V dropout with no current load. By the way, in the previous video, I completely overlooked the fact that you could set

**Dave Jones:** the voltage and the current just by pressing these keys. I thought, well, I just went into set and you know, it was a little bit dicky to go in there and select your digit and all that sort of

**Dave Jones:** stuff. It was a little bit tedious, but you don't actually have to do that. You can if you want to set your voltage, simply press V there and bingo, you've got your control. And it it does seem to

**Dave Jones:** have maybe like it goes in 10 mV increments there. It does maybe seem to have a little bit of velocity control. So I can turn that relatively fast, not as fast as I'd ideally like, but it's still quite usable. So very easy to set

**Dave Jones:** your voltage and current like that. So the user interface is really quite good and it permanently displays your set voltage and current up the top which I absolutely love. All power supplies should display set voltage and set current if possible

**Dave Jones:** and also the input voltage as well just so that you're aware if the input voltage is drooping or anything like that. Anyway, let's get on to the characterization. Now there's two ways to get an efficiency characteristic curve of a power supply like this. One is to

**Dave Jones:** fully automate it and these two instruments probably ideal for this task as they're both ethernet LXI enabled. So if I hook them up to network the PC you could write a script that outputted your necessary voltage from here. Of course you can read you'd be

**Dave Jones:** able to read back your input current as well so you'd be able to read your input power going into your module and of course you can control the electronic load, set it up for any constant current load you like and then sweep it over

**Dave Jones:** there and you can run various sweeping runs and get all the data points at at basically 1 mA resolution or whatever the resolution of this thing is. But unfortunately, even though you can fully automate these instruments here, this

**Dave Jones:** one down here is not. So you're going to have to actually set, you know, turn the knob. Several of from the same company who manufacture this, they do offer uh wire, you know, Wi-Fi enabled ones, Bluetooth enabled ones, and all serial

**Dave Jones:** enabled ones. So, you can actually get digital uh control of these things. So, you can actually for virtually hardly any more cost, just like five bucks or something extra, I don't know, five, 10 bucks extra, you can get the uh wireless

**Dave Jones:** or serial enabled version of these modules. I believe in the bigger one, I don't think it comes not sure if it comes in the smaller one. So, yes, while I could uh semi-automate this thing by like I could sweep the load, for

**Dave Jones:** example, for a particular output uh current, and then I could get a characteristic curve uh of the load for each particular output voltage and get a whole set of characteristic curves and the efficiency at each point for each particular output

**Dave Jones:** voltage and each over the uh sweep from 0 to 3 amp output current and all that sort of stuff. But, hey, I'll just get a couple of uh ones, you know, at at like low output voltage, like 5 and then 12 V, and then 24 V

**Dave Jones:** maybe, you know, those three characteristic curves might be okay for a 0 to 3 amp uh current sweep in I don't know, you know, 100 mA increments or something like that. Good enough. Uh when you're taking these measurements

**Dave Jones:** manually, writing them down on paper, you know, it it takes time. So, I'll just I'll just uh get uh you know, fairly crude plot. It's going to be good enough. It's not like the characteristic plots are going to like, you know, curve

**Dave Jones:** up like this and then suddenly go boom and then up, you know, like they they're going to have a characteristic shape, you know, something like that. Typically, there's going to be a peak efficiency. Um so, you know, I expect

**Dave Jones:** this the efficiency of this thing uh based on just some, you know, temporary feeling the heat sink on the back and stuff, it's going to be like greater than 90% um at its peak. So, it'll be interesting to see

**Dave Jones:** uh how efficient this is over the full uh range for a couple of uh input voltages and a a of voltages. So, I just wanted to show you what the noise looks like here when you go from no load,

**Dave Jones:** which we've got at the moment, basically 20 mV peak-to-peak there, and we actually switch on the full 3 amps at a 24 V output. There you go, it jumps up to like 110 mV or thereabouts. So, you know, it ain't pretty. So, if you're

**Dave Jones:** building a supply out of these things, you probably want to do some at least a modicum of output filtering would be nice. Bugger it, I decided to go to town. I had just took apart my leads there, and now

**Dave Jones:** I've got the sense and the load leads going directly into the Phoenix contact connectors, and I've got much thicker gauge wire, really overkill, going to the input there, so we don't have to worry about the drop across there. The

**Dave Jones:** power shown here should be the input power, and absolutely, cuz we're doing the sensing, the output power shown here should be absolutely spot-on. So, yeah, no worries. It was a bit how you doing before. Interestingly, the quiescent current here with no load

**Dave Jones:** changes when you turn the output off and on, even though there's no load. So, it's you know, 0.5 W drops down to 0.39 with it with the output off. So, we should actually include the on figure in the efficiency

**Dave Jones:** calculations, I think. All right, so what I think we're going to see on the results for this thing is that it's going to be optimized because it's like designed it's got bugger all heat sinking on it, and it's designed for

**Dave Jones:** like 70 W capability power capability or whatever it is. It needs to be like really high efficiency, even like 90% is not going to cut it. So, I'm they're probably going to be shooting for like 95% or, you know, something of the mid-90s. But,

**Dave Jones:** you can't design the problem with universal supplies like this, you can't design them to be universally efficient over the entire input voltage range and output voltage range, and output current range, as well. It's just not possible. So, you've

**Dave Jones:** got to pick probably the worst-case position like this because where you can design your thermals around. The worst-case condition of like the maximum output voltage driving the maximum output current. I mean, that's 70 W. The power delivered worst-case.

**Dave Jones:** They're going to design around that. So, I expect to where it's it's maximum power delivery capability is where it will be most efficient at 90 to 95% efficient or something like that. And then, at lower output voltages for the

**Dave Jones:** same given input, I'd expect it to be lower efficiency. So, say you've got, you know, 30 V input, and then you like for 20 V out, you'll get an efficiency curve. And then, if you do 5 V out,

**Dave Jones:** it'll be lower efficiency again. So, that's the sort of results we expect. That's just, you know, how things are with DC-to-DC converters like this. They're always a compromise, and they always basically as buck converters like this basically have the same

**Dave Jones:** characteristic trade-offs. Right. So, I finished the sweep at 5 V. I got basically the input power and the output power from 0.1 amps up to 3 amps, basically. And I just noted, right? I was just going to do the sweep again for a 12 V output

**Dave Jones:** here. And you'll notice that the quiescent current, well, the quiescent current remains the same. If you switch the output off like that, it's not the exact same 0.390 W. So, that's that's the electronics in there, as I said.

**Dave Jones:** That's not going to change. But you switch it on with absolutely no load at all, and it's 0.6, whereas we're getting 0.5 before. So, that's all part of the efficiency of this thing. And after laboriously measuring and plotting or

**Dave Jones:** entering and plotting the data, this is what we get. Ta-da! We have our efficiency curve here for the DPS 3003 power supply for a 15-V input. And we have uh separate data for 30-V input and 40-V input as well. I didn't

**Dave Jones:** uh measure like a low input voltage cuz like what's the point? No one's going to have like a, you know, a 7-V input volt in a 0-5 V power supply, but yeah. Anyway, there's only so much you can measure. Um so, this is our

**Dave Jones:** efficiency from 30 to 50%. I just sort of expanded the scale. Uh when you plot things from zero, it kind of like just cramps all the data up in the top and you don't see as much uh detail. And

**Dave Jones:** this is quite interesting. Look at this. This is the Let's go in. This one here, the red one, is the 12-V output. So, 15 V in, 12 V out, and look at that efficiency. That was pretty much where I

**Dave Jones:** thought it must be. Actually up like 96% where I thought it kind of like had to be for uh right up to 3 A. So, I've got 0 to 3 A here. By the way, I didn't I measured uh 0.1 A down at the lower end

**Dave Jones:** cuz I knew there'd be that big uh taper down at the lower end and not much happening up at the lower at the higher end. So, I did 0.2. And I did 0.75 here, which is an oddball one. And if you have

**Dave Jones:** a look in here, the chart type, I think done a video on this somewhere, is actually a scatter chart. It must be to then get the linear axes down the bottom here. It's kind of weird. Um I think

**Dave Jones:** Excel does the same thing. I'm using LibreOffice here. Um so, yeah, otherwise it just linearly spaces the samples. Um so, you have to use a scatter plot. Anyway, doesn't matter. Small little uh tech tip there. So, anyway, that's a

**Dave Jones:** very, very efficient. And as always, down at low currents, it tapers off, but still a respectable, you know, 80 2%. And for 5 volts out with the same 15 volts in, it's still a very respectable 90% efficiency. Uh peaks at there. It's

**Dave Jones:** a little bit under, but you know, that's hunky-dory. But look at this, for 1.5 volts out for 15 volts in, it's not great. Look at peaks at around uh 68% here, and like right up at the higher currents, it's pretty miserable, even

**Dave Jones:** though it's delivering a lower amount of power, right? It's still the 3 amps, but it's only at 1.5 volts, right? So, 4 and 1/2 watts as opposed to up here, which is uh you know, 15 watts for the 5-volt output

**Dave Jones:** one, for example. That's because, like I said before, the the converters, you have to optimize them for a certain input voltage and like input power and output power range, and you just have to live with whatever efficiency you get

**Dave Jones:** outside of that. And that's usually not a problem in product design, because if you're designing a switch mode converter for your product, for example, then you know how much power your product's going to take, as long as it doesn't

**Dave Jones:** drastically change power modes from one to the other. Of course, you know how much it's going to take, so you optimize your DC-to-DC converter design efficiency for that particular current. You size your inductors, you size your, you know, your transistors and whatnot.

**Dave Jones:** And for that particular configuration. But on a universal power supply like this, there's just really not much avoiding this until you unless you go to great complexity and great expense. You know, spare no expense. Um you're going to just have to put up with

**Dave Jones:** a poor result like this. Now, here's the interesting bit. What we what we really care about is how much power does this thing dissipate? So, what I've had to do, right? I've deliberately kept this one a bit clean,

**Dave Jones:** but here's what I prepared earlier. Here's the exact same graph again, but I've included a second Y axis on the side here. This secondary Y axis, and this is the power loss, the power dissipation in the module. So, that is

**Dave Jones:** from 0 to 4 W, and that's what these dash lines here, the colors represents the exact same. So, red is 12 V out, red is 12 V out here. Um, and this is you'll find these in some data sheets as well. They'll do

**Dave Jones:** power dissipation loss. So, this is how much is dissipated, and here's the interesting bit. For the say the 12 V output, right? Which is delivering the most amount of power, 3 amps * 12 V, so 36 W output power, right? Which is quite

**Dave Jones:** a lot for such a little module, right? It's only dissipating at worst 2. uh, 2 W there. And of course, the heat sinking there, it's sized up. It might be maybe it's you know, 5 degrees C per watt or something like that. So, it

**Dave Jones:** might raise, you know, a 10 degrees, which is kind of what you feel if you stick your fingers on the back of those things. So, guesstimate, you know, ballpark, it's probably a 5 degrees C heat sink. Uh, 5 degrees C per watt heat sink,

**Dave Jones:** right? And it's not it's not too dissimilar for the 5 V output, the blue line there, which is what you'd expect because they're a similar sort of efficiency up here. They're both plus 90%, but look at the loss in the 5 V one. Now, the 5 V one is

**Dave Jones:** only delivering 1.5 V at 3 amps. So, it's only 4 and 1/2 W as opposed to 36 W, so it's delivering much less output power, but look at the power dissipation, this green line going up here. It is now

**Dave Jones:** even though it's delivering, right? Less than order of magnitude, it's that little module has to dissipate 3.8 W. So, there you go. There are the tradeoffs when your efficiency drops like that because it's not an optimized or can't be an optimized design almost

**Dave Jones:** by the nature of DC-to-DC converters trying to deliver a full range of output power, you just can't get it. So, it actually dissipates more power and has and heats up more delivering a lesser load. And that's exactly what you'd expect.

**Dave Jones:** There's nothing surprising here. This is basic DC-to-DC converter stuff. And by the way, that power loss includes the quiescent loss of 0.39 W. So, even though it's not necessarily being dissipated in the the output transistor, the output diode, the output inductor, and that

**Dave Jones:** sort of stuff, the power devices that deliver your output load, it's still part of the module. So, the module's going to heat up. So, I think it's, you know, it's a good thing to actually include that in your total module power loss cuz that

**Dave Jones:** you could label that module power loss, for example. So, there you go. Interesting, huh? Now, we've done exactly the same thing again for a 30-V input this time instead of a 15-V input. So, double. It's not quite up to its

**Dave Jones:** maximum. Its maximum is 40. And as you can see here, efficiency, once again, we've got different output voltages. We've got 24 V this time. We've got 12, that's in the green, 12 V in the red, and the blue is 5 V. And once again, I

**Dave Jones:** didn't do 1.5 here, but if you did, it'd be, you know, horrible like down in the 60% probably just like last time. So, very similar, but we're getting a similar result. Like once again, that 95 odd percent right up there. Does it hit

**Dave Jones:** 96? You know, like it's pretty darn good. Exactly where you'd expect it to be for this type of, you know, small heat sink module that we've got here. It's fairly respectable at 5 V out, but unfortunately the power losses are

**Dave Jones:** bigger this time with the 30 V input. That's just the nature of the beast. Um, and they all track fairly well, even though the 5 V one output here is quite lower efficiency at under 80% here right up at the 3 A. They all track very well.

**Dave Jones:** So, we're getting about 4 1/2 W max dissipation at the full 3 A output current. But once again, that the heat sink on it is like it doesn't get hot. It doesn't get too hot to touch. It does a decent adequate job of doing

**Dave Jones:** this. And why not? Let's do 40 V input. Only two output voltages the maximum, which is 32 V. That's the red one there. Once again, we're talking, you know, that same 95%. Obviously, they've optimized it for that output power

**Dave Jones:** level. And once again, it drops, you know, it tapers down. It's pretty horrible at the low currents here for the 5 V out, but looking at the power dissipation here, there's obviously a couple of little oddball values in

**Dave Jones:** there. They're probably just typos. This should be, you know, fairly flat. There shouldn't be little spikes and things like that. The efficiency is pretty horrible right down here at low currents. But, you know, that's the problem with designing these

**Dave Jones:** wide range converters. As I said, but once again, you're at low output current, so the efficiency doesn't matter, so you're not dissipating much power. Once again, we're under 4 W there for those sort of for those two particular 5 V and 32 V

**Dave Jones:** output from a 40 V input. So, there you have it. That's some characterization of the DPS3003 power module. And it's a really neat little unit. Noisy as all buggery, but you know, add some filtering or something like that if you're uh

**Dave Jones:** concerned about that sort of thing, but it it basically does what it uh claims. Full full voltage and current with 96 W output uh capability, and it does it with basically in that tiny little passive heatsink. Cuz it really is, you

**Dave Jones:** know, quite efficient. Uh and if you want to really want to push it to its extreme limits, we haven't characterized every extreme limit here. Um then you might have to have a bit of uh forced airflow, but that's a winning little module for

**Dave Jones:** like what, under 20 25 bucks delivered or something like that? Absolutely crazy. Um yeah, maybe I'll do like a reverse engineering of that and uh see what's uh doing in there. We know it's the What is it? The XL 7005

**Dave Jones:** converter uh chip or something like that, but it's going to be using an external MOSFET and uh uh you know, external MOSFET cuz it's not built in to do that uh sort of jazz. But anyway, that is a really neat little

**Dave Jones:** module, neat designed, and it basically isn't lying in the specs. I rather like it. So, there you have it. I hope you enjoyed that. If you did, please give it a big thumbs up. And at the end of this

**Dave Jones:** video, I'll link in Yeah, it's somewhere up there, somewhere. Yep. All over the place. Um some uh other power supply videos uh measuring I've done one specifically on measuring the uh DC-to-DC converter efficiency and all sorts of stuff. Linked in. Watch them if

**Dave Jones:** you haven't seen them. I've got tons of power supply type videos. Anyway, hope you enjoyed it. Catch you next time.
