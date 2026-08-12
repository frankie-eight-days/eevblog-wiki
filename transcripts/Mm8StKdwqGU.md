---
video_id: Mm8StKdwqGU
title: EEVblog #1294 - LLC Resonant Mode Converter Design
url: https://www.youtube.com/watch?v=Mm8StKdwqGU
source: youtube-asr
---

**Dave Jones:** Now this is actually starting to look an awful lot like a resonant mode controller. It just makes sense. Well, it's a basic generic resonant mode topology, but I think we're going to see that line up here. We've got ourselves our four

**Dave Jones:** diodes down here. We've got ourselves four MOSFETs under here, down on their own heat sink down there. There are four 60R360s. So yeah, I'm pretty sure this is a resonant mode power supply and that makes sense. Now I won't go into a full

**Dave Jones:** tutorial on resonant mode power supplies well cuz that'd be an hour video in its own right. And it can be quite a complicated subject if you're, you know, go into the deep dive into the maths of it. So what we had up here is our four

**Dave Jones:** MOSFETs. I'm going to show you the data sheet for those in a minute cuz that's the tail. And under here we have our four diodes as well. And we've got some transformers here and a big ass inductor like this.

**Dave Jones:** So that with the four MOSFETs and the four diodes, that is a classic configuration for what's called a full bridge resonant converter. So I'll show you the topology in a minute, but the data sheet for these will pretty much

**Dave Jones:** prove it. And those MOSFETs that we saw under there, surprise surprise, look at this. 600 V CoolMOS CFD7 for those playing along at home. SJ MOSFET. Infineon's answer to resonant high power topologies. Bingo, we got it. The Infineon's latest high voltage super

**Dave Jones:** junction MOSFET technology with integrated fast body diode complementing the CoolMOS 7 is the ideal choice for resonant topologies in high power switch mode power supply applications such as server, telecom, EV charging stations, and all that sort of stuff. And you can

**Dave Jones:** go into the technical details about why this is the best in the business and stuff like that. Anyway, yeah, they compare it to all their competitors. Blah, blah, blah, blah, blah. But, anyway, yeah, that's the jobby that's used in here. So, yeah, this is a

**Dave Jones:** resonant mode controller and it makes complete sense because they're trying to put an 800 W power supply into a two rack unit case here. So, the efficiency is very important. You can't piss away any power in your heat sinks cuz then thermally

**Dave Jones:** you've just got to get all that out in the air flow and everything else. It's just It's horrible. So, you want to make this thing as efficient as possible. And that's what resonant mode converters do. They are higher quiescent current

**Dave Jones:** supplies, but when they're actually switching at full power, they are actually more efficient. And I'll explain why. I found this application note from Infineon. I'll link it in down below. Resonant LLC converter operation and design. And it has a good uh generic

**Dave Jones:** application um circuit here. And I believe this is pretty much what we're saying here. This is why it's a full bridge. Now, you can actually get a half bridge a resonant converter as well and they're very common, which of course

**Dave Jones:** will only have if you're aware of your full bridge, you know, your H bridge. Uh You can get a half bridge would only have the two MOSFETs and would only have the two output diodes. But, in this case, we do have physically four MOSFETs

**Dave Jones:** and four uh diodes on those heat sinks. is what's going on here. Now, how a resonant mode controller works is that it's basically a switch in series with an LC tank circuit, a capacitor and inductor tank circuit here. And that

**Dave Jones:** forms That's where the name comes from. Hence, a resonance. It's resonant mode. So, it actually switches on the resonant point of the L and the C here. And then you've got a transformer, which then couples that and that's where they're

**Dave Jones:** getting their isolation from, of course, uh for each uh channel. And then the output is just a regular full wave uh bridge like this. But, um it's the switching in here at the resonant point of the LC tank circuit that reduces the

**Dave Jones:** switching losses in the converter, and hence the heat dissipated uh during switching. And there you go, you can go into the uh mass of it for that and it gets more complicated than that uh too. That's the equivalent resonant circuit.

**Dave Jones:** Uh and the quality factor and blah blah blah, all that sort of stuff. And then you can get into the regions and things like that, and we won't go into that cuz it gets quite complex. So, the thing

**Dave Jones:** with a regular switch mode uh topology that you're used to with your regular switching uh transistor is that uh it's switching it basically like digitally, like high low high low high low like that. And the switching losses can be

**Dave Jones:** quite high, particularly the higher frequency you go, cuz you want to make it more efficient, so you go to a higher frequency, but at the higher frequency you get greater switching losses with that sort of thing. Whereas with a

**Dave Jones:** resonant mode uh converter like this, it actually changes the wave shape the switching wave shape so that there's effectively less losses. I'll I'll try and Dave cat it. Oh, and you can see the various uh switching wave forms. So, if

**Dave Jones:** you want to go through step by step how it works, this uh application note is uh pretty good. And it just goes through and it explains each cycle, etc. etc. And it shows some of the wave forms, too. But, uh let me try and explain

**Dave Jones:** something here. Please excuse the crudity of this model. I certainly didn't have time to build at the scale or to paint it. Now, this one on the left here is uh let's say the switching I'm simplifying this. Let's say this is the switching wave

**Dave Jones:** form for your typical uh converter, which is switching hard like this, okay? Now, this area in here and under here, these are you can consider those the power dissipation, the losses in your switching elements, which is heat that

**Dave Jones:** you have to get rid of, right? So, that's the efficiency of your converter. But, a resonant mode controller is going to change instead of like a hard switching like I've exaggerated the slew on that, by the way. Anyway, the

**Dave Jones:** resonant mode controller actually changes the wave shape, so it's like this. And I it's your switching losses are going to be smaller, but basically, what that does is it reduces the amount of switching losses in here, so it's

**Dave Jones:** smaller. And you can get a dramatic difference in the switching losses in your converter from a just a regular switch mode topology, whichever one you want to choose, which is hard switching versus a resonant mode switching, which is using

**Dave Jones:** the LNC to change the wave shape there, and you just get basically area under the curve you losses is less. But, as I said, it's not some magic bullet, that's why not everyone uses switch mode converters because the losses will

**Dave Jones:** actually in low power state like in effect quiescent power dissipation is going to be potentially higher for resonant mode stuff. So, you know, but for large output power supplies like this in a small amount of space where you want to

**Dave Jones:** make them as efficient as possible, resonant mode is a decent choice. And by the way, in this particular case, if you are actually using only half of the sinusoid the resonant LC sinusoid like this, then it's what's called a quasi

**Dave Jones:** resonant converter, and you might have heard that. And the other thing with resonant mode controllers, if you haven't already gathered, is that they're more expensive and more difficult to actually design and tweak and get right. So, hence they're only

**Dave Jones:** used in like really top shelf power supplies like this one, and you know, like you can just have a look at like all of the all of the analysis required, the equivalent resonant circuit, and this is just a

**Dave Jones:** first harmonic analysis, I believe, of it. But that's, you know, pretty much all you need to do, but you can go further down the rabbit hole, as I said. But yeah, actually getting just the tank circuit right and

**Dave Jones:** the the ratio, the turns ratio of the transformer and the various inductors and various modes and things like that. And the parasitics of the transformer, and and in some cases the transformer over here is is going to not be as like

**Dave Jones:** as well determined as specific inductors over in the LC tank part and things like this and matching all this and getting it all right and figuring out all this sort of stuff. Look, I mean, this is just right.

**Dave Jones:** Right, yeah, we're we're getting really serious in modes of operation and getting all right. So, it's pretty much vastly more difficult to actually design and engineer one of these than it is for your more traditional PWM you know, boost bucky sepic type

**Dave Jones:** converter that you're used to doing. So, yeah, you really only see these on like really pretty much top shelf power supplies. They've even got a flowchart design step here. What are the Qmax values? Find FX minimum is Kmax

**Dave Jones:** required required gain. All this sort of stuff and like choose your resonant component values. It's just It's it's seriously like selecting the M value for example. So, you've got to understand the formula up here and figure out what your M value is doing.

**Dave Jones:** Of course, you can just like kludge it all and kind of sort of make it work, but that kind of defeats the point. So, here you've got to know the ratio of the total primary inductance to the resonant

**Dave Jones:** inductance. So, you you've effectively got your resonance inductance here and then your primary inductance here transformer. You've got to match all that and all the parasitics involved in that, and it gets complicated. Any resonant mode smidge mode design experts, let us know

**Dave Jones:** in the comments down below if this is your day job designing that resonant mode controllers because yeah, a lot of effort went into doing this. Let's just put it that way. So, here it is. Like, this is for different values of M, for

**Dave Jones:** example, like M3, M6, for example, and how this like it flattens out the peaks here. So, lower M values are going to give you higher boost gain, narrow frequency range, more flexible regulation. But, if you want higher efficiency, you've got to go for the

**Dave Jones:** higher M values. But, then you got to get higher magnetizing inductance, and it's just yeah. No. So, yeah, like knock yourself out on resonant mode power supply design voltage gain verification. Look at this. As I said, I'll link this down below. And then you

**Dave Jones:** finally, once you've done all that engineering, you calculate resonant mode values, and then bridge and rectifier selection, for example. This is why they use MOSFETs in here. There's basically two you really can't do this with bipolar transistors cuz their drive requirements

**Dave Jones:** are too much. So, really you need a very specific, in this case, highly optimized MOSFET. One that's carefully tailored for this kind of specific resonant mode operation. And this is what they design these specific MOSFETs for. And if you

**Dave Jones:** want to know the difference between a full bridge and a half bridge one, how and why, here you go. The Although a half bridge requires half the primary turns for the same voltage gain and magnetic flux swing, thus half

**Dave Jones:** the primary winding resistance, the primary copper losses are, of course, double compared to the full bridge because the squared RMS and that pesky I squared R thing. The squared RMS current in the half bridge is four times. So, it

**Dave Jones:** might be cheaper and simpler to design a half bridge resonant uh, converter. And, as I said, uh, they're relatively common, um, but yeah, for the best performance in, like, a top-shelf product like this, you're going to want to implement the

**Dave Jones:** full-bridge, uh, converter, definitely. And here's where they talk about the output rectification as well. As I said, you can actually do a full, uh, bridge rectifier for a common transformer like this, but then again, you've got to have

**Dave Jones:** like a center-tapped transformer if you want to do that. Whereas, this one is, uh, not center-tapped. So, you probably larger transformer, maybe there's some, you know, design extra design losses and things like that. So, you might be better off for the full-bridge. So,

**Dave Jones:** there you go. There's a summary of the full-wave, uh, output rectifier compared to the full-bridge. And this has got, like, essentially nothing to do with the, resonant converter side. That's over on the, uh, primary side. This is just the

**Dave Jones:** secondary, uh, side. So, diode voltage rating's got to be times two, number of diodes, but you can save cost on your number of diodes, the conduction losses are divided by two, the number of, uh, secondary windings, but you've got to go

**Dave Jones:** up by two, as I said, uh, the resistance per winding goes up by two, and the IMS current, uh, is a square times square root of a half, and transformer secondary copper losses times two. Blah, blah, blah, blah, blah. So, you know,

**Dave Jones:** there's a big trade-off there. And by the way, you'll see, uh, these resonant mode, uh, controllers often like a half, uh, bridge type actually implemented in something like a, you know, a backlight for, uh, TV backlight, uh, power supplies and and

**Dave Jones:** things like that. Um, they're just trying to basically, uh, get the losses down. And, you know, these do a pretty good job at it. So, they actually give you a design example here. Once again, I'll link this down

**Dave Jones:** below, and you can actually go through the steps of actually designing, uh, a resonant mode, uh, converter step by step, calculating the resonant mode component values and all this sort of stuff. Look, we need like one mic, uh,

**Dave Jones:** for For for the capacitance, we need 11, uh, microhenries, uh, for the inductance, and all that sort of jazz. Experimental waveforms and efficiency, and he's actually measured waveforms and stuff like that. And you can see typical waveforms here, and you can check out

**Dave Jones:** the efficiencies here. You know, 97 and 1/2% it's pretty schmick. And it doesn't drop a huge amount with, uh, input uh, voltage variation. I mean, even like worst case here, we're still looking at 94%. Not too shabby. Oh, look at that.

**Dave Jones:** They've even got a reference design there. And the schematics and the bill of materials and everything. Great application note. Thumbs up. By the way, I forgot to mention that these are also called a resonant LLC, uh, converters. The reason that they're called LLC is

**Dave Jones:** because it's pretty obvious. Let's have a look down here. There's a capacitor, that's the C, and there's essentially two inductors here because that is, like, the transformer primary has to be, by definition, part it's an inductor, too. So, it's part of the, uh, LLC tank

**Dave Jones:** circuit. You have to take that into consideration in your calculations and stuff like that. So, they flip it even though the C is first physically in the circuit, it's LLC. Anyway, so if you see that term, they're talking about

**Dave Jones:** resonant mode converters. And basically, all it's doing is, uh, taking your DC input here, and it's converting that into a square wave, which then gets pulse shaped by this LC tank circuit. So, instead of having nice, hard, fast,

**Dave Jones:** uh, switching currents, you have nice, more gentle currents. Or, hence, hard switching versus smooth switching, effectively. So, LC circuits are just known as like smooth switches, really. And another advantage of resonant mode, uh, converters compared to your typical, uh, pulse

**Dave Jones:** width modulation ones, which as you know, can change the pulse width and actually freak change frequency, as well. I'm sure I've done, uh, videos on like, uh, different modes of operation. You know, they'll go into some pulse skipping mode and then they'll go

**Dave Jones:** they'll switch down frequencies or up frequencies depending upon the output current and things like that. They'll dynamically change. And they're actually when you've got like really broadly changing switching frequencies like that, it's really hard to filter out those sort of frequencies. So in terms

**Dave Jones:** of your EMI or electromagnetic interference and your compliance for that sort of stuff, resonant modes are actually much better. It's It's in the name. It resonates at one frequency. So you've pretty much got a really narrow range of frequencies

**Dave Jones:** that you have to filter out here. And it's it's just much easier to filter out to put in an EMC filter for your resonant mode LLC controller. And that especially comes into play at large output currents and large output

**Dave Jones:** powers cuz when you're switching huge amounts of current, if you're doing that over a huge variable frequency range, you know, you can really come a gutser come EMC testing time. So yeah, resonant mode has definite advantages there. So

**Dave Jones:** you can actually see these capacitors under here like this and they've got the same ones up under here. You just can't see it at this angle. So they would be our series capacitance in our topology. And maybe the inductor is actually this

**Dave Jones:** baby, but the part number of these two is identical. So we need an inductor plus a transformer. So maybe they're reusing one side. I'm not sure. Now you you might think that this one here, that's the resonant mode

**Dave Jones:** inductor, but I don't think so cuz it's not these little fiddly surface mount jobbies here. So yeah, and its location is further like is looks like it's on the isolate you know, it's on this isolated side of the converter. So that that really

**Dave Jones:** doesn't make sense. So that's probably just part of an output filter I'd say, but yeah, I'd say yeah, it's coming in here. This is our full wave bridge. These are our caps.

**Dave Jones:** Stick with me. And we've got an inductor, we've got a the now isolation transformer, we've got our four output rectifier diodes down here, and then there's as I said, there's another MOSFET under here, so I'm not quite sure what they're doing

**Dave Jones:** there. And then we've just got some output filter in. So, yeah, I think that's how it works. Sure the power supply aficionados will all be commenting down below about what's going on here, but anyway, it looks to be some

**Dave Jones:** variation of a resonant mode controller. Exactly how they're doing it, I don't know. We'd have to reverse engineer it, and that would require ripping the whole guts out. So, I hope you found that brief overview of LLC or resonant mode

**Dave Jones:** converters useful. If you did, please give it a big thumbs up. As always, you can discuss in the YouTube comments down below or over on the EV blog forum, or even in my library comment videos, even though the comment system's still not

**Dave Jones:** that terrific on library, but anyway, I'm getting right up there on subs. Fantastic. Anyway, catch you next time.
