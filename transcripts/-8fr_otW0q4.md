---
video_id: -8fr_otW0q4
title: EEVblog #892 - Siglent SSA3021X Spectrum Analyser Teardown
url: https://www.youtube.com/watch?v=-8fr_otW0q4
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We're going to take a look at the brand spanking new just on the market Siglent SSA 3021X. And click here if you haven't seen the comparison of this against the Rigol 815. So, I've done a video on that.

**Dave Jones:** Let's crack it open. Now, for those playing along at home, this is the new hardware, the latest one that has been redesigned cuz they had a few issues late last year. They had to redesign this thing. So, this is the latest one

**Dave Jones:** May 2016 build. Got a couple of screws on the top here and on the bottom just like the Rigol unit screwed in exactly the same way. We can make short work of this security sticker with an antistatic bag here.

**Dave Jones:** I've done a separate video on that. Click here to check it out. And yes, they have a bit of thread locker on the screws. As is common, there's a couple of little clips there that you have to get off. And once we do that, well,

**Dave Jones:** let's crack it open. And tada. We're in like Flynn. There's our shielding. And yes, it's the exact same sheet steel construction as we've seen in other Siglent gear, which is prone to rusting along the cut edges, the famous Siglent rust.

**Dave Jones:** And we've got pop rivets here. Yeah, it's you know, it's not a full aluminum chassis. So, yeah, that's not great, but you got to remember that the main competitor, the Rigol 815, is no different. It's exactly the same sheet

**Dave Jones:** metal outer construction. We're going to have the aluminum block inside it for the RF shielding. Is it my imagination or is there a little teensy weensy bit of trademark Siglent rust there? It's really hard to see, but yeah, there's

**Dave Jones:** not much, but these edges, if they're not treated properly, yeah, they're prone to it. You can see they do have proper RFI shielding tabs down there for the ethernet and the USB. No worries. All right, let's pop this

**Dave Jones:** off. We're going to have one main board, I'm sure. As is quite common. That'll be my guess with There's our shielding blocks. We've got at least two shielding blocks. Excuse me while I disconnect the power cable. There we go. I'll swing it around for

**Dave Jones:** you. There we go. No. We've got a separate Well, no. One main board here, separate RF board, and then another section down here. There we go. We're in like Flynn. And if we have a look at the mains input down in there,

**Dave Jones:** bit hard to see, but they've got that properly heat shrunk and crimped and shake-proof washer onto the chassis. No worries whatsoever. And the power supply looks neat and tidy. Does have Siglent brand. Whether or not Siglent actually designed and engineered and built the

**Dave Jones:** thing, I don't know. They could have chopped it out as as is very common in the industry. Lelon brand cap. Groan. You know, it's the main DC input filtering cap. Gets less stress. We'll have to have a look at the output ones

**Dave Jones:** there. Nice strapping over there. Looks nice and tidy. They've selastic down the output caps, but it just looks decent design and build quality. No worries, I think. Just be able to see Rubicon caps down there. So, yeah, they're decent.

**Dave Jones:** Now, this is actually significantly different to the Rigol one which had, as I mentioned, a single board construction like this. This has got three separate boards here. And well, I don't blame them at all. We've got our main

**Dave Jones:** processor board down here, Spartan 6 FPGA. We'll have a look at the chips on here in more detail. Got an application processor and, you know, pretty Joe Blog's stuff. And then, this has what probably is the oscillator for the

**Dave Jones:** thing, I would say, would be over here and they're driving that. But then, we've got our input is over here like this and then it flows through all the various stages that a spectrum analyzer needs. And of course, this separate

**Dave Jones:** block down here is going to be the tracking generator. They've done that as a physically separate board, and they've just got the you know, 0.1 in IDC header cables going over here. That's no problem cuz these aren't carrying anything significant.

**Dave Jones:** They're carrying some power and just some you know, control signals and things like that. So, you know, you don't have to worry about that. Inside these blocks here, you'd have some power supply decoupling, local regulation, and things like that. Some inductors to

**Dave Jones:** filter out crap and all that sort of stuff coming back in and out of these two blocks here. But yeah, that's just fine and dandy. Power supply section down here, no worries. Better than the Rigol 815. If you have a look at that

**Dave Jones:** teardown video, you notice they had like a free-standing heatsink and it was all a bit how you doing. This one's a bit more polished. So, yeah, it looks good. And I think we can get right into this block

**Dave Jones:** here taking out the screws without taking out the board here. There's a couple of longer ones which go into support support posts on the bottom. There's another aluminum block on the bottom. But uh let's lift it up. We've got our gold

**Dave Jones:** flash around the edges. Ta-da! We're in like Flynn. And yep, as I suspected, here is our oscillators. It looks like we've got two of them. And these are super duper Well, one of them's going to be super duper special cuz this one's

**Dave Jones:** pretty schmick oscillator, much better than the Rigol 815 that we saw in the comparison video. It looks like they have a dual footprint there. So, let's take a look at this. All right. Now we can have a look around the main board here with our

**Dave Jones:** Takano microscope. We can zoom in to our heart's content. Let's start over with the boring stuff. Nothing exciting around here at all unless switch-mode power supplies float your boat. There's a switching controller there, dead giveaway with all the

**Dave Jones:** inductors around here and everything else. So, and then some big sort of power traces going to the inductors. That's probably a multi-channel job. Uh, what is it? 3.3 ox? Yeah, 3.3 all around there. Not much doing around here.

**Dave Jones:** Micrel, good to see Micrel. I'm a bit of a Micrel uh, fanboy myself. And uh, yeah, not a huge amount else happening. Everyone, come on Dave, show us This is the um, LCD connector going off. You can tell by the uh, twisted pairs. The

**Dave Jones:** reason they need twisted pairs is because they're high-speed serial interface. And we've got ourselves a Spartan-6 XC6SLX45. Um, a Spartan-6 was also used inside the uh, Rigol 811 uh, 5 as well. I can't reme- recall offhand if it was the exact

**Dave Jones:** same one. Unpopulated memory uh, footprint here. They didn't need it. Anyway, the Spartan-6 FPGA, you know, reasonably pedestrian uh, FPGA. Sort of middle-of-the-range uh, type stuff. It'll be doing all the FFT uh, processing and things like that. That's

**Dave Jones:** what uh, FPGAs are really, really good at. And can't see that number very well. It's all about the light, by the way. Seeing part numbers, it's all about the lights and the angle. Anyway, we've got a TI part. And if I shield the light

**Dave Jones:** from this side with my hand, there it is, the AM3352. That's an ARM Cortex uh, A8 processor. You know, the typical thing that'll run Linux and uh, everything else. No worries. It's got whiz-bang 3D graphics in it and all that

**Dave Jones:** sort of stuff. Anyway, I'm not fussed over those. And then we've got our uh, looks like we have some Samsung uh, DDR memory here, by the looks of it. And there's our flash program memory. We've got ourselves very nice. We've got

**Dave Jones:** ourselves a JTAG uh, header up here. So, bingo, you can uh, whack that straight in. Probably does uh, both devices, I would say. They might be daisy-chaining those together, cuz I can't see one for the Is there one down Is there one down here

**Dave Jones:** somewhere for the uh processor. I don't think so. This would be a test connector or something would be my guess. They'd be using that for some sort of uh production system testing, but uh it's interesting to note what device is missing up here? U14.

**Dave Jones:** Um that's fascinating. It's got no external crystal, just a HC49 uh crystal there, and yeah, it's got a thermal pad on the bottom. Um so, it's doing something reasonably serious. I'm not sure what. Why did they leave that unpopulated?

**Dave Jones:** Where's Wally? Think what everyone wants to see though is this marvelous oscillator they've got inside this thing. Oh, it's not marvelous. It's not like a you know, a uh oven controlled oscillator or rubidium or anything fancy pantsy, but you know, it's a decent

**Dave Jones:** spec. Now, who that is um there's our 10 That's our main 10 MHz reference. So, uh yeah, by all means try and decode that part number and get that. Who actually makes that? I don't know. Let me Google it. Well, that

**Dave Jones:** doesn't uh show up anything unless I do uh some more exhaustive searching, I'm afraid. Not much I can do there. Sorry about the glare, but that's the only way we can get the part number on these puppies. These are Micrel 5209s. So,

**Dave Jones:** I've used those before. They're uh low noise low dropout regulators. Not bad little things. So, nothing else much doing. Discrete or two. No wackers, but what is U16 over here? And that one right there. Bit of magic happening. Bit hard to make out, but

**Dave Jones:** that's an Analog Devices ADF4001. And here's the data sheet for the ADF4001 from Analog Devices. 200 meg clock generator PLL. But uh look at this. It's a PLL that requires um for clock sources that require very low noise stable reference signals. It's

**Dave Jones:** ultra low phase noise. And that's uh you know, what we're getting in this thing. I mean, it's not an industry-leading uh spectrum analyzer by any stretch of the imagination, but it's uh certainly better than the uh Rigol. And as always,

**Dave Jones:** I'll link in the data sheets down below for those who want to uh take a quick look at it. But uh yeah, it's a pretty decent uh PLL. I like it. And pin six here, you can see coming through the

**Dave Jones:** firewall here all the way over to this 40 MHz oscillator over here. So, this is the pin six is the RF input to that. So, there that is coming directly from the crystal over here. And of course, the 10

**Dave Jones:** MHz reference will be going um into the main uh clock input for this thing. And I really like the way that they've done this tracking generator module here. You'll notice that all these numbers, 11111, these are the uh long screws which uh as

**Dave Jones:** I said for the previous board go right down into mounts on the bottom here. And two and two is obviously mating up with the uh end connector on the front. And once I've taken out all these ones, actually, sorry.

**Dave Jones:** There we go. Taken out Oh, what's that one? No, that one's got no number. So, I've taken out all that. Entire module pops out like that. Isn't that beautiful? Nice bit of engineering. Love it. And you'll notice the PCB as well.

**Dave Jones:** Look, gold plating on the edging. Castellation is like a half moon on the um you know, if you do like a drill on the uh side of the thing. But uh yeah, that's a separate uh manufacturing process. You can get uh most PCB

**Dave Jones:** manufacturers to actually do that. You just need to specify that uh separately. I'll have the edges gold plated. Thank you very much. But obviously, they panelized it. There's going to be a break in uh that there. So, maybe they

**Dave Jones:** uh do it Oh, no, that's just around the connectors there. Uh but anyway, that's just nice. Like a separate block like that makes it real easy to design, real easy to change the design if you had to. Like if they had to re-spin this, you

**Dave Jones:** know, they had an issue with it, they only have to re-spin this. They don't have to re-spin the the main RF board up here, the whole, you know, the whole shebang. They can just do the tracking generator. It's just much nicer from an

**Dave Jones:** engineering point of view, modular base like that. Whereas the Rigol one, as I've seen in the Rigol teardown, completely different. It's all on one board, everything. That makes it much more difficult to re-spin, potentially lower cost. But this one it's going to

**Dave Jones:** be higher cost, uh potentially, little bit, you know, it's not a huge amount in it, but potentially higher cost. But yeah, it's just nicer design. Time for the reveal. Tada! What do we got on the top? There we go. Ooh, yeah, baby. Some RF magic.

**Dave Jones:** And on the bottom side more No, not as much RF magic happening there. In fact, it's just Mhm, boring. Some passives. All the magic happens on the top. And this sort of stuff looks like RF voodoo, RF magic,

**Dave Jones:** but it's not. I've mentioned these in the videos before. These are just distributed element filters. They're basically LC and R filters. That's basically all they are. Because these elements at RF, high frequencies, uh look like that trace there, for example,

**Dave Jones:** is an inductor. This big square here is a capacitor cuz there's going to be a ground plane on the layer under this uh controlled dielectric board, by the way. This would be a, you know, some maybe a Rogers brand or something, uh controlled

**Dave Jones:** uh dielectric constant. So, it's just has more controlled uh frequency characteristics over controlling impedance characteristics over the uh wide frequency range. So, this will be a capacitor directly down to ground. We'll have another inductor, another capacitor, another inductor, another

**Dave Jones:** capacitor, another inductor, another inductor in series with the capacitor going down to ground, an inductor. a much smaller inductor, much smaller than this one here in value, and then a larger capacitance going down to the ground, inductor, inductor, capacitor,

**Dave Jones:** inductor, but and so on. It's going to be a distributed element low-pass filter. There's no magic in there, and a similar sort of thing is happening here as well. We've got another uh distributed element low-pass filter. Once again, we've got the uh Micrel

**Dave Jones:** They're using these everywhere, these 5209s um for low noise uh local voltage regulation, and uh then we've got a few other op 74 Is that a 74HC04? There you go. You've got to have some uh 7400 series uh TTL in there. Magic. And

**Dave Jones:** you've got to have a classic TL072 op amp as well. But, of course, it's not doing anything uh you know, high performance. It's just doing an offset thing or uh you know, something like that. So, it's no big deal. It's not

**Dave Jones:** working at uh frequencies. Just maybe doing some uh DC type stuff. And we've got a HMC307. This is from uh Hittite, uh now owned by Analog Devices. It um looks like it's an obsolete part, but that's actually a

**Dave Jones:** uh digital attenuator. And when you go into the Siglent uh tracking generator software, and you can set the um attenuation value of the uh tracking generator anywhere from 1 dB uh in this particular case, the chip goes from one

**Dave Jones:** one dB steps up to uh 31 dB attenuation. So, that's how it's doing it. Very simple. Now, of course, there's no clock on this board because the tracking generator is does exactly what it says. It tracks. So, it's uh designed

**Dave Jones:** to take whatever the current uh sweep frequency is as the uh spectrum analyzer is, you know, sweeping across from whatever uh your start frequency to you stop frequency, then this uh just designed to track that. It generates the same frequency as what it's

**Dave Jones:** tracking. So, that's why it doesn't need its own oscillator. That's why the frequency Well, does it come in here or does it pop out there? Not entirely sure. Anyway, which one's what? Which is in, which is out? Doesn't matter. And of course, no

**Dave Jones:** surprises for finding another Hittite part here, which is the uh PLL. This is exactly what you expect in here. Um goes up to 3 gig. A reasonably capable part there. So, that would That's generating the the main tracking clock. You might

**Dave Jones:** be wondering about these. Also got H in front of it. Look, 860 835. We looked at over here. We've got an 860. We've got a H 976 here. These don't look like, of course, anything high frequency sort of

**Dave Jones:** going into them or anything like that. And you know, lots of bypass caps around them, the zero ohm resistors, not much else. Um what are they? They're actually linear voltage regulators. They are from Hittite, of course, but they're, you

**Dave Jones:** know, specifically high power supply rejection ratio. Uh The PSRR, um of course, low drop out voltage regulators. So, there you go. They use the specific Hittite ones, which are would have been recommended possibly in the data sheet for this, um

**Dave Jones:** even though I haven't had a look for that, you know, that's probably where they came from. They're specifically designed to match the other Hittite chip sets. And that's not uncommon for manufacturers of specific stuff like that. 74HC 244. And that's about all she

**Dave Jones:** wrote. There's nothing really exciting on the other side of the board here. Geez, this um Tagarno microscope handles I mean, that board is angled at, you know, 30° or something like that. Handles that really really nicely. So, you can see that whole board

**Dave Jones:** there. That's That's just brilliant. The optics on this are great. I love it. But, yeah, that's all she wrote. Uh the via stitching is just absolutely everywhere. Look, they've got a channel in here, which is the um main output here. So, that's uh

**Dave Jones:** that's coming from that's we've got ourselves a driver over here. I don't know, you know, you'd have to decipher that uh that part there, but uh yep. It's via stitching everywhere. And as we talked about, the uh gold plating on the edge here before, it

**Dave Jones:** doesn't matter. It's not like it's going to leak out. They've got that inside as well on the different layers. So, you know, it's just fine. Oh, here we go. We actually have some silk screen to tell us what which connector is what. That's

**Dave Jones:** the tracking generator local oscillator, and that's the tracking generator reference input. There you go. And as is standard practice with uh all these RF shielding enclosures, the very You see them all in spectrum analyzers and RF sig gens and everything, they've got the

**Dave Jones:** machined aluminum uh things with each individual building block. They, you know, each block uh circuit block, they actually uh machine out a little part. like there's no leakage, and you see the gold uh plate that makes contact with it. There's no

**Dave Jones:** leakage between uh modules and channels and things like that. Fantastic. These things aren't particularly cheap, but you know, like they don't make these in millions, so they're not going to cast these. That's why you can see all the

**Dave Jones:** machining marks in there. They've just milled that out. And I suspect the main uh spectrum analyzer module here is going to come out as well. It's fantastic. I love this. I don't have to dick around with taking out the steel

**Dave Jones:** chassis, and then, you know, around with the nuts on the you know, on the connectors and things like that as you have to do with lots of scopes. This is just beautiful. It's designed for ease of module uh replacement, ease of

**Dave Jones:** assembly and disassembly and servicing. Fantastic. But of course, you might think, "Ease of servicing, you got all these screws on here." You know, like you have to to get tight seal on all of these. Like a lot of your high-end stuff

**Dave Jones:** will actually use an RF gasket underneath there. And if you take out all the screws on the real bleeding edge high-performance ones, then and you disturb the gasket underneath the pressure of the gasket that's separating all the sections and

**Dave Jones:** everything else, then you might have to get the thing recalibration checked. So, yeah, just to make sure, you know, because the real bleeding edge RF stuff, it really matters. This is only like a 3.2 gig one, so it's you know, it's like

**Dave Jones:** baby stuff in terms of RF. It's real RF graybeards will probably go, "Ah, it's practically DC." So, I've undone all the number ones here, and we should in theory, oh, no. Oh, there's one more left here. Oh, oops. Sorry, one more

**Dave Jones:** left. There we go. Oh. Okay, they should have labeled that number one as well. There we go. I think it's it's just going to pop out as a complete module. Ah, complete with There we go. The end connector got caught.

**Dave Jones:** But because it's got the you know, it's got the extra thread sticking out there. But look, it's just one complete block. Beautiful. And once you as I said, this is great for production testing and handling and assembly and things like

**Dave Jones:** that. And you know, you don't have to like if you had one like in the Rigol for example, your assembly yield, like it you know, the bigger your board is, the you know, the greater risk you take with

**Dave Jones:** your PCB yield and just, you know, one part in here, for example, that didn't reflow solder properly, uh the whole thing uh can fail. Whereas, this they can test the assembly separately and things like that. So, there's lots of uh production

**Dave Jones:** advantages and uh design R&D advantages to doing it uh separate module like that. But, that's just that's winner winner chicken dinner all over. I don't have to take out the chassis, dick around with any of that stuff. Beauty.

**Dave Jones:** All right, here comes the big reveal. Last screw here. And unless I've forgotten one. Probably laughing at me if I have. Ta-da! Ah. Ah. We've been mooned. That's the back of it. And all the RF goodness. Once again,

**Dave Jones:** we'll see lots of distributed element filters. Once again, ta-da! Yep. There we go. Ah, beautiful. Look at that. So, let's take a detailed look at the main board here. And uh we're only going to be concerned with the top side here

**Dave Jones:** because if you have a look at the bottom side here, there's just nothing of interest there. It's just all uh passives, bypassing, and some regulation, maybe, things like that. So, nothing special at all. Now, it might look daunting at first with all these

**Dave Jones:** distributed element filters and everything else. But, as we've seen before, you can see that's pretty much a modular block approach. And I've done a handy little overlay here that will uh attempt to, hopefully, explain all the different functional blocks and the

**Dave Jones:** signal flow on the board. So, let's get to it. Now, of course, I can't guarantee this is 100% accurate. I've likely made uh mistakes on here. And if I have, I'll endeavor to uh correct them with overlays. So, let's start by taking a

**Dave Jones:** look at the RF input in the top left corner. This section here, of course, contains the 50-ohm input impedance. But, that uh little sot23-6 package, you'll see uh four of these here. These are actually uh single pole double throw

**Dave Jones:** switches. So, they can actually switch in the 50 ohm load and various other stuff. So, we'll go to a higher res photo for this and then zoom in on the RF section here, and we can see that the

**Dave Jones:** input is AC coupled there through C10, and then that goes into U1, which is a 955C as all the other ones here, these SOT23-6 parts there, some form of single-pole double-throw switch, which I can't find the data sheet for. If I can,

**Dave Jones:** I'll link it in down below. But, you can see that one side of the switch there, I believe pin one there, switches in C9 and R1, which is the 50 ohm load there. So, it's not a permanent 50 ohm

**Dave Jones:** load input. And you'll notice that there's actually four diodes unpopulated there, so there's a distinct lack of input protection here. So, unless there's something inside that little wimpy U1 switch there, there's, you know, not much here at all.

**Dave Jones:** There's basically nothing on the other side. There is a tiny little diode D7 there, but jeez, it's wimpy. And if we scroll down here, we've got a couple more of these switches here. And there's some diodes, four diodes there, so I'm

**Dave Jones:** not exactly sure what's doing there, but that looks like some power supply clamping protection there. At least they start to have something now. And a bit further down here, you can see that VR1 there has got 20 written on it. I'm

**Dave Jones:** going to assume that's a 20 dB attenuator there, and you can see that's basically switching in C16 that that straight controlled impedance line there. So, it's basically either going straight to it's selecting either straight through or a 20 dB

**Dave Jones:** attenuator here. Next up, we go down into a HMC, once again, Hittite there, everywhere. They've got the entire solution for this thing, the HMC 307, and this is the digital attenuator. So, when you go into the spectrum analyzer and you set the input

**Dave Jones:** attenuation, you can set it in 1 dB steps um up to 31 dB over and above the 20 dB input attenuator, and that's exactly what this chip does. So, the software is limited by the capabilities of this chip, but

**Dave Jones:** yeah, nice device. DC to 4 gig, DC to daylight. And I really like the way the designers have laid out this chip. Look at this. There's the input pin, and then there's the two ground pins right there. So, you

**Dave Jones:** can see all that via stitching to separate the input and the output, so there's no coupling there. And then the pin below that is the output. So, from a layout point of view, it allows you to lay it out with a minimum amount of

**Dave Jones:** coupling. Nice. But we're not done with our input section yet. If we scroll down a little bit more, we'll see the signal flow down into our next section, which is of course the preamp. This thing has, I believe it's a 10 dB preamp gain on

**Dave Jones:** it. Once again, selectable, so expect to see the digital switches there, and that's exactly what we get. So, I can either bypass the preamp or switch in the preamp. But of course, in this case, you'll notice that the switches are

**Dave Jones:** bigger. They're a different package, and we can't actually get the data sheet. Surprise, surprise, it's another Hittite part, a single pole double throw. It's a non-reflective switch up DC to not quite daylight this time, 3.5 gig. It's a

**Dave Jones:** non-reflective switch. You can see the internal diagram there. It's actually got internal 50 ohm termination resistors in there, but basically it's just a switch. It allows us to So, they use a combination of two of them. You can switch in your preamp or switch it

**Dave Jones:** out. Easy. Now, that's all bread and butter stuff, but look at all these other blocks in here, and this is the complex operation of a spectrum analyzer. Not all spectrum analyzers operate the same, but they use very similar techniques. So, what we're going

**Dave Jones:** to do is take a look at a basic block diagram here. So, we've looked at basically just one block here, the RF input attenuator in near the signal input there and that includes the switching and the preamp and everything

**Dave Jones:** else. Now we expect to see a low-pass filter in here and that's what we'll see in a second and then that goes into a mixer which then uses a local oscillator mixes the two signals together generates a higher frequency called the

**Dave Jones:** intermediate frequency and then we expect to see a gain stage there. There's that gray amplifier block there. Attenuator we won't see this in this one but it doesn't matter. Um that IF then goes into an IF filter. We'll definitely see

**Dave Jones:** that and then goes into a log amp and envelope detector, video filter, and display but that's not quite how this one works. We need to look at another block diagram for that. And as it says here most spectrum

**Dave Jones:** analyzers use two or four mixing steps to reach the final intermediate frequency that we can then in this case or do all digital processing and actually display that cuz this is an all digital IF system instead of a

**Dave Jones:** traditional analog spectrum analyzer. Anyway, so there's going to be going to see several steps here. By the way, these diagrams come from the Keysight application note AN 150. I'll link it in down below. Highly recommend it's one of

**Dave Jones:** the best reads on how spectrum analyzers work and everything else. So we expect to see in well in this case what we're going to see is two local oscillators. The first one goes in the first mixer and then the second one that goes into

**Dave Jones:** the second mixer here. If we take a look at the first mixer on the left-hand side there, that's the green circle with the X there. We need this because we need to generate a higher frequency than our frequency range of interest. In this

**Dave Jones:** case our spectrum analyzer can go up to 3.2 gig. So we have to generate an intermediate frequency higher than that because if we don't do that then there will be dead bands within the measurement window that just won't work.

**Dave Jones:** So we have to actually mix that with a higher mix our input frequency with a higher frequency to generate an intermediate frequency above our maximum 3.2 gig input range. And if we go back to our original block diagram here, what we expect after our

**Dave Jones:** input stuff is a low-pass filter and then a mixer with a local oscillator feeding into that mixer. Do we get that? Well, let's take a look. Yes, of course we do. You can see the preamp there on the left that we looked at before. It

**Dave Jones:** then feeds into a down into that low-pass filter, which is again a distributed element filter there with the various L's and C's. And then that goes into a mixer IC there, which then accepts the signal from above it there

**Dave Jones:** from that nice-looking bowtie distributed element low-pass filter, and that will come from the local oscillator as we'll see. But, it's a bit more complex. It's not like the local oscillator feeds straight in. We're doing some tricks with our local

**Dave Jones:** oscillator in this particular case. But, anyway, the output from the mixer then goes into that amplifier gain stage as we saw on the block diagram. And if we take a look at a high-res photo of the mixer and that amplifier IF

**Dave Jones:** amplifier stage, once again, we've got two Hittite parts yet again. The HMC488 mixer there on the left and the HMC716 amplifier. Let's take a look at the data sheets. And this mixer can go from 4 to 7 gig, which is exactly what we want.

**Dave Jones:** It's above our operational frequency range of our amplifier. And if we have a look at the specs here, then our intermediate frequency range DC to 2.5 gig. And then our IF amplifier chip, the HMC716, it's exactly what you expect. It's a In

**Dave Jones:** this case, it's an 18 dB gain amplifier, but it's got the bandwidth of 3.1 to 3.9 gig. So, it's designed to operate within that range, which which basically our 3.2 gig maximum operational frequency range. And that's where our IF frequency is going to sit

**Dave Jones:** somewhere above 3.2 gig. The exact value, uh we don't actually know unless we do more investigation or some measurements. But before we follow that intermediate frequency out, we want to see our local oscillator cuz as I said before, it wasn't as simple as just a

**Dave Jones:** local oscillator feeding into the mixer as it shows on the uh block diagrams for spectrum analyzers. So, if we zoom in here, we can find our uh first local oscillator or our main uh voltage-controlled oscillator. And this one uses a Z-Communications uh

**Dave Jones:** part there for the VCO, the voltage-controlled oscillator, and which is the big metal can there, and another Hittite uh PLL there to form our local oscillator. Now, this is made by a company called Z-Communications, and they make a ton of different variants of

**Dave Jones:** these with different ranges and things like that. And this one is going to cover the frequency range that we need. If you have a look at the uh tuning voltage here, it goes from 1,800 to 4,200 MHz or uh 1.8 to 4.2 gig. And

**Dave Jones:** pretty much exactly the range we need here. And this is our sweep generator we saw in the block diagram on the bottom left there, the red sweep generator feeds into the local oscillator and then feeds into the mixer. But as I said,

**Dave Jones:** there's a few more steps after our local oscillator before we get to the mixer in this particular analyzer. But as part of that local oscillator, we've got a Hittite HMC703 uh fractional synthesizer which forms part of the ultimate uh PLL local

**Dave Jones:** oscillator loop. And we can see that here. If we take a look at the uh demo board you can actually get for this chip, it shows that there's a VCO integrated as part of the system here. In this case, a Hittite HMC508, but in

**Dave Jones:** the case of the uh Siglent spectrum analyzer here, we're using a VCO from uh Z-Communications. And if you believe the sales blurb here, check it out. This platform has the best phase noise and spurious performance in the industry.

**Dave Jones:** Yes, thank you very much. But once again, you know, decent choices being made here to enable a pretty decent performance at a low price point. Well done, Siglent. But even with all that magic, the output of the first main

**Dave Jones:** local oscillator here is not high enough in frequency. So, it goes into a frequency doubler there and uh this is designed for a two two to four gig input, so doubles that anywhere from uh four up to eight gig. But once again,

**Dave Jones:** the exact bandwidth uh frequency range we're talking about here, we don't exactly know unless we did further investigations or measurement. And the frequency doubler being used again, a Hittite HMC189 here, two to four gig input as I said,

**Dave Jones:** so four to eight gig output. Eh, it's designed for exactly this job. And this particular part isn't obsolete. Unlike uh if you were very keen, you would have noticed uh plastered over the data sheets for a couple of chips before, we would have

**Dave Jones:** seen that they're actually obsolete. So, yeah, why they're still using them, I don't know. Maybe there's nothing better at the price point. But we're not done yet. No siree Bob. The output of the frequency doubler here for our local

**Dave Jones:** oscillator uh goes into uh two single pole double throw switches, which then can select one of three band pass filters. In this case uh the this particular uh physical arrangement, the distributed element uh filter is called an interdigital uh band pass filter. And

**Dave Jones:** so, three different frequencies. You can actually see that they're different uh geometries there, which actually selects the bandwidth and the response. And then there's three uh single pole double throw switches on the other side. So, the software can select one of three

**Dave Jones:** band pass filters on our local oscillator. And these switches are different to what we've seen before. These are uh VSW A2-63, blah blah blah blah blah. And these are uh high isolation absorptive uh single pole double throw switches

**Dave Jones:** with integrated CMOS drivers and all sorts of weird and wonderful stuff. And we don't care about the quiescent current really. And 500 to 6 500 meg to 6 gig bandwidth. Pretty decent. And we're almost there. I've mentioned this before. You can see the output of

**Dave Jones:** that one that's selectable band pass filter there. Then goes through just a little bit more stuff there and goes through another bowtie low pass filter. It's called a bowtie low pass filter because it looks like a bowtie. That's where it

**Dave Jones:** gets its name from. Another low pass filter just takes the edge off something or other. And then that finally goes into the mixer. So that block diagram we saw before and you see for all spectrum analyzers the local oscillator goes

**Dave Jones:** straight into the mixer. Well, as you've seen, it's a bit more complicated than that for various performance reasons. But if you're keen eye, you wouldn't notice something in between there. The output from the interdigital filter after the switching

**Dave Jones:** and probably some little buffering there or something then goes into this odd looking arrangement here on the board which is coupling the signal to go over if you follow the trace on the other side. It's coupling over to go up to the tracking generator

**Dave Jones:** local oscillator SMA connector. And that jumps on over to the tracking generator module we saw before. So finally out of our mixer and then through our IF gain stage which we've looked at, we expect to find an IF

**Dave Jones:** filter and well, you betcha. Look at the output of the amp in the 18 dB IF amplifier down here. Bingo, it goes into another band pass filter. Another interdigital type. Once again, different geometry in there to give you a

**Dave Jones:** different range and response of the thing. And then that's followed by another cute-looking bowtie low-pass filter as well. Once again, just to take the upper edge off something. And if you're curious about how these interdigital bandpass filters actually

**Dave Jones:** work, when you can clearly see that both like the input signal comes in and then it basically goes down to ground with a trace sticking up and then the other then the trace on the right-hand side and next to that goes up to ground at

**Dave Jones:** the top side and then the next one goes down to ground. So, how does this actually work? Well, it's because we're at high frequencies here. These work at, you know, several hundred megahertz up to, you know, several gigahertz or something

**Dave Jones:** like that. They're basically coupled resonators. They're also known as interdigitated coupled resonators. So, yeah, they resonate between the two and then it propagates along and resonates and that's why you might see different spacing in there is to give a different

**Dave Jones:** passband characteristic for this thing. Anyway, you have to get into real complex RF microstrip type theory to, you know, figure out exactly how this works and there's a ton of math into it and I'm sure you could Google it if you're

**Dave Jones:** really interested. But, yeah, even though it goes down to ground there, it gets through. But, we said here before that this particular spectrum analyzer arrangement uses two mixing techniques and so we need to find that second mixer and the

**Dave Jones:** second local oscillator as well. And if we pan across here, bingo, the output of our filter there goes into another mixer, the 488 488 exactly as we had before. But, just like on the block diagram here, you'll notice that the output of

**Dave Jones:** the second mixer is a much lower frequency. It's within way under way within the passband of our spectrum analyzer. In this block diagram, 322 megahertz, but in the case of uh this particular one here, it's actually at 810

**Dave Jones:** megahertz. And the reason we know that is because hey, look, we can look at the um filters on the output of the mixer, and we can see that there are SAW filters or surface acoustic wave filters, and we

**Dave Jones:** can have a look at the data sheet for this particular uh one. They're available in all different frequencies. This one happens to be an 810 megahertz SAW filter. So, we know that's the output uh frequency of the second mixer.

**Dave Jones:** But this isn't low enough uh frequency for now us to do digital IF sampling on. So, what we want to do is feed it into another third mixer, just like what's uh shown here, to actually down-convert it to a frequency that we a baseband

**Dave Jones:** frequency that we can actually sample with like a Joe Blog's uh you know, 16-bit analog-to-digital converter. And we can see that here, the output of the SAW filter goes into this little white block here, which is a Mini-Circuits.

**Dave Jones:** Yes, we finally get a Mini-Circuits win in the design here. It's not all Hittite. Mini-Circuits one of the biggest uh providers of uh these sorts of uh mixers. And so, this will go in, and we can take a look at the data sheet

**Dave Jones:** for this Mini-Circuits mixer as well. But there's nothing terribly exciting to see here. It's just a you know, basically 5 megahertz to 1 gig mixer designed for this sort of application, uh down-conversion uh to a baseband signal. But wait, we're not finished

**Dave Jones:** with the mixer. Every mixer's got to have a local oscillator input. Where's that coming from? Well, it it is coming from the second local oscillator, but we need a much lower frequency. So, you'll notice that the second local oscillator

**Dave Jones:** here uh as like feeding the second mixer across to the left there, it also goes up, and that same signal feeds a is divided by four, and then that gets fed into the third mixer, which does the down-conversion. So, we've got our final

**Dave Jones:** RF uh frequency bandwidth here, and this goes into curiously a single pole four throw switch, and that's what the IC is. So, I'm not exactly sure what it's selecting there. You know, there's some sort of different filtering options that it's doing there.

**Dave Jones:** I'm not exactly sure what. Anyway, that then goes over into another single pole four throw switch here, which has only half the stuff populated. So, that's quite unusual. Why did they leave that out? Now, as a user by the name of Go Zoo, if

**Dave Jones:** I'm pronouncing that correctly on the EV blog forum, postulated for this one, it it certainly looks like another band pass filter in there with inductors and the caps in there, and that would be one of going into presumably one of the

**Dave Jones:** channels of U85 on the left hand side there, the single pole four throw switch. And presumably, there would be a software option for this to have another additional band pass filter on the final IF before it goes into the

**Dave Jones:** sampler. So, maybe there's even a secret menu option for it if you could hack the firmware or whatever, or maybe, you know, they had an early version of firmware they decided they didn't want it. I don't know. Could still be there.

**Dave Jones:** Who knows? Could be interesting. But, yeah, I don't know. If you could find it, you might be able to hack in your own band pass filter in there for some additional functionality. And the good thing about an experimental hack like

**Dave Jones:** that is that you're not really, you know, damaging anything. You're populating existing footprints in there with an existing digital switch that's only affected if you enable a software option in the firmware to actually flick that switch and in, you know, put that

**Dave Jones:** filter in series with the final IF there. So, you know, you can play around if your heart's content without really risking damaging anything. So, that's it. We're finally through our complete block diagram here, but this envelope detector, we don't have that cuz as I said before,

**Dave Jones:** this spectrum analyzer uses what's called an all-digital IF filter. So, it does everything after the IF stage, intermediate frequency stage, it just samples that directly with a high-resolution high sample rate analog-to-digital converter and then does everything in software. As we see

**Dave Jones:** in this Keysight application note here, here is how the Keysight X-Series signal analyzers do an all-digital IF. They've got an ADC in there with a gain and the alias filter, everything else, but it goes into then a custom IC, which in this

**Dave Jones:** case would be that Spartan-6 FPGA we saw is doing a Hilbert transform and then it's doing some filtering and then it can do the video bandwidth in there and does logs and then powers and all sorts of and the detector, all sorts of stuff

**Dave Jones:** all within side that would be happening inside that Spartan-6 FPGA, no doubt. And then that goes into the and probably it'll be doing the FFT in there as well. And then that just goes out to the display applications processor, which we

**Dave Jones:** saw earlier. So, now we have to go full circle right back to the main PCB under that block where we found our main reference oscillator before. And what do we find? Surprise, surprise, an ADC driver designed specifically for IF baseband

**Dave Jones:** processing. In this case, it's the National Semiconductor, none of this Texas Instruments rubbish, LMH6517. It's designed exactly for this for a 16-bit ADC. And there's the block diagram down the bottom. So, no surprises to find what's down below

**Dave Jones:** this. I'll give you a one guess. And congratulations, you win a brass razoo. It's an analog-to-digital converter. It's the Analog Devices AD9235. Actually, 12-bit, surprise, surprise. Not this 16-bit rubbish, I guess. For Siglent, no, 12-bit will do the job just

**Dave Jones:** fine. And yeah, it's designed for ultrasound equipment. Low-cost digital oscilloscopes, there we go. Winner, winner, chicken dinner. And you'll notice that we've got the dash 40 part there, which it means 40 megasamples per second. This part's available from 20 up to 65 megasamples

**Dave Jones:** per second. So, at 40 megasamples per second, we know that our IF baseband frequency has to be somewhere below 20, cuz you know, all that Nyquist stuff. Really annoying. Yeah, so it's got to be at most half of that sample rate.

**Dave Jones:** So, there you go. That's a rather lengthy look inside the brand spanking new Siglent SSA3021 spectrum analyzer. I hope you enjoyed that. I sort of went to town a bit, actually, going through the various sections on here. I hope you found that

**Dave Jones:** rather interesting. And as always, if you want to discuss this, jump on over the EVblog forum. Links down below. That's where everyone's trying to going to try and discuss the pros and cons of this thing. But, hey, I could not fault

**Dave Jones:** this. There's no bodges in the thing. There's no crap quality parts in the thing. And they've designed and engineered the RF part of it really, really well. So, the design and engineering that went into the RF section, which is much more capable and

**Dave Jones:** more complicated than the Rigol one, they've really, I think they've gone to town on it. And Siglent should be pretty proud about this effort for their first-ever spectrum analyzer. So, well done, Siglent. Big thumbs up there. So, if you liked it, please give it a big

**Dave Jones:** thumbs up. And links down below, all that sort of jazz, as always. Catch you next time. Oh, sorry. I'm trying to rush to get this video out. It's been kicking my backside and I don't have time today to put it back together. I got to

**Dave Jones:** quickly finish this edit and get out of here. So, yeah, trust me, it'll work. She'll be right. No worries. Hi. Welcome to Teardown Tuesday with another spectrum analyzer, the Rigol DSA 815 TG with the optional tracking generator. Thought we'd crack it open, take a look

**Dave Jones:** inside because spectrum analyzers are usually a bit more interesting than other bits of test gear like your run-of-the-mill scope or your multimeter or whatever. Bit more engineering poured in these things. So, you know what we say here on the EEVblog, don't turn it

**Dave Jones:** on, take it apart.
