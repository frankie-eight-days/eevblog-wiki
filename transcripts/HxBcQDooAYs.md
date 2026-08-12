---
video_id: HxBcQDooAYs
title: EEVblog #1101 - Siglent SVA1015X VNA Teardown
url: https://www.youtube.com/watch?v=HxBcQDooAYs
source: youtube-asr
---

**Dave Jones:** Hi, check it out. We've got a brand spanking new instrument for you, the Siglent SVA1015X. Thank you very much, Siglent, for getting this to me. Um, it has just hit the market, I think, like today or yesterday or something like that, or a

**Dave Jones:** couple of days ago by the time you see this video. Yes, it's a brand new spectrum analyzer, but not only that, check it out. It's a spectrum and vector network analyzer. Yes, it's a VNA, and VNAs are usually expensive uh, bits of

**Dave Jones:** kit designed for vector network analysis, and I won't go into all the details of VNAs and everything else. We'll just have a quick skim over this, but they're, um, basically, this, I believe, is the first really, uh, low-cost vector network analyzer in your

**Dave Jones:** traditional, um, you know, spectrum analyzer form factor like this. And the retail price for this is, uh, $1,395 USD for 9 kHz to 1.5 gig, uh, spectrum analyzer, but although it says spectrum and vector network analyzer, and the

**Dave Jones:** model number is SVA for vector analyzer, that's actually optional. The vector network analyzer, hang on, just let me facepalm. Oh. So, although Siglent have released this cool new spectrum and vector network analyzer, the network analyzer is optional extra. It's another 609

**Dave Jones:** smackers. So, that puts it around about the two grand figure. Could come under, maybe under, uh, two grand with the, uh, vector network analyzer, uh, street price perhaps. I haven't, uh, seen those yet. So, I don't know what their

**Dave Jones:** thinking is there. I mean, you know, they could have killed the market. Every ham radio operator on the planet would buy one of these if it, uh, for $1,395 it had the vector network analyzer built in. Anyway, it is very cool, so we'll

**Dave Jones:** check it out. Now, um, Siglent were actually going to release the SSA1015X, which was just the spectrum analyzer version of this without the vector network analyzer hardware built into it. I guess they just depopulate the chips. We'll take a look at this. It's

**Dave Jones:** primarily going to be a teardown video, so we'll check it out. But, at the last minute, they actually decided against that and they're only releasing the SV model, which is which has the vector network analyzer hardware built in. So,

**Dave Jones:** it's just a software upgrade. You pay your license, boom, you get your VNA plus other modulation stuff, demodulation stuff, and other cool stuff we'll take a quick look at. But, anyway, it is only 1.5 gig, whereas the SSA3000

**Dave Jones:** model we looked at previously, which this one is not replacing, the 3000 model actually the tracking gen was optional extra. But, on this one, the tracking generator is included. But, the new but the street prices these days of

**Dave Jones:** the 3000 model, the SSA3000, is that it includes the tracking gen as well for basically the same price as this. So, you can basically choose between a spectrum analyzer only, but the SSA3000 goes to 2.1 gig as standard with

**Dave Jones:** optional 3.2 gig, I think it is. Whereas this new lower end model, and it is lower end even though it's a vector network analyzer, is only limited to 1.5 gig. There is, as far as I'm aware, no higher bandwidth

**Dave Jones:** option for this. So, you know, great for covering all the, you know, anything like hams and stuff want to do and things like that. And EMI pre-compliance and all that sort of stuff, it should be plenty for that.

**Dave Jones:** But, if you want the higher frequency, this baby isn't going to do it for you. So, compared to the SSA 3000, the phase noise of this thing practically identical. But, the noise floor isn't as good on this one. This is minus 156 DBM where it

**Dave Jones:** compared to 161 DBM for the 3000 model. So, it's got better hardware in the 3000. So, as we'll see in the teardown, we expect significant differences in the hardware. Well, it's you know, at least significant enough to affect the

**Dave Jones:** performance of this thing. Speaking of which, I'll link in my teardown below for the previous version of this, the 3000. And I I'm going to pat myself on the back here. I think that's an absolutely brilliant teardown cuz I took a

**Dave Jones:** different approach to that one in that I took high-res photos and then I did all the voiceover and editing and zoomed in and I drew block diagrams around that sort of stuff. I may not go to the same

**Dave Jones:** and that was a lot of work. So, I may not go to the same amount of effort for this one. So, definitely check out the previous video if you want to know how a spectrum analyzer works at a block

**Dave Jones:** diagram PCB level cuz the previous video covers that really well. Oh, and the amplitude accuracy of this one isn't quite as good as the 3000 model. This is plus minus 1.2 dB compared to plus minus 0.7. So, yeah, its performance isn't as

**Dave Jones:** good, but hey, if you can get a cheap vector or a cheapish vector network analyzer in your traditional spectrum analyzer form factor, this could be a winner. This is a good move by Siglent. So, as the basic spectrum analyzer, it's

**Dave Jones:** basically an identical look and feel to the 3000 model. It's all the buttons are like a practically menus I believe are all going to be identical. I haven't fully checked it out menu for menu, but it's going to be pretty darn close to

**Dave Jones:** identical. But, a lot of extra functionality in this one. We can do modulation analysis in here. The I believe this one is actually fully optioned up. So, we can do you know frequency shift keying and stuff like that. So, we can demodulate signals and

**Dave Jones:** it's got distance to fault stuff because we have this vector network analyzer capability sort of building this extra hardware building that allows us to do like distance to fault. Fantastic. And of course, what everyone's going to be excited about is the vector network

**Dave Jones:** analyzer capability. And if we go in here and take a look, log magnitude, we can do phase, we can do group delay, terrific stuff. And we can do Smith charts, five different types of Smith charts. I won't go into them, but absolutely

**Dave Jones:** fantastic. I mean, you know, like like the hams are all getting all moist just watching this. Thinking about having one of these puppies. So, not only is Smith charts, but you polar plots as well, absolutely fantastic. Linear and log mag, what else we got

**Dave Jones:** here? SWR ratio, brilliant. And yes, it is only a two-port VNA, of course. It's none of that four-port rubbish that you'll pay, you know, 20, 30,000 dollars for or something like that. But you know, two ports more than

**Dave Jones:** good enough to do all sorts of, you know, antenna calibrations and all sorts of stuff in your RF field that there's probably a dozen applications that I wouldn't even know about cuz that's just not my field. Anyway, it does have

**Dave Jones:** resolution bandwidth that can go all the way with LBJ down to 1 1 hertz. Trust me, you can get down there. And it's got optional EMI filtering as well. Once again, there's a whole bunch of options for this thing including

**Dave Jones:** RF field probes and stuff like that uh you've seen in many of my uh previous uh videos and all the you know a ton of options. So, you know, it really it is it's probably going to be an

**Dave Jones:** impressively priced bit of kit for uh EMI pre-compliance and all of uh your low-end vector network analyzer stuff. Terrific. Anyway, it's identical to the 3000 we've seen before. It's got a headphone port, USB. We've got the uh tracking generator which comes standard,

**Dave Jones:** which is fantastic. RF input up to uh plus 30 uh dBm max or 50 V uh DC maximum, which is pretty generous. Uh reverse voltage maximum 50 V uh DC on the tracking gen source. And if we have

**Dave Jones:** a look at the back, um standard uh Ethernet LAN with uh remote uh web viewing and web browsing stuff like that. Um external 10 meg reference and we can get our 10 meg out. Um it's going to have a reasonable clock. As I looked

**Dave Jones:** in the previous video, uh the 3000 model actually had a better clock than the Rigol uh unit. External trigger in and you Kensington lock and that's all she wrote. Beauty. Feels like a solid bit of kit. And it does take a while to boot, too. I

**Dave Jones:** don't know, 20, 30 seconds or something. Not going to write home to my mom about it. Anyway, I forgot to mention, yes, it is all touchy-feely touch scope. Um it is Come on. There we go. Whoop, we can

**Dave Jones:** pop up this one little annoying bug here. I don't like you can pop up this menu, but I can't get rid of it. How the hell do I get rid of it? Anyway, like direct buttons like screenshot and

**Dave Jones:** things like that. Really is quite cool, but you don't have to use the touch functionality if you don't want to. You can do it all with the uh good old buttons. Speaking of which, the screen is very bright. I do actually have my uh

**Dave Jones:** studio lights on here. So, if I turn those off, it's actually, you know, it really is quite uh nice. The view angle on it going a bit low. Um going past the horizontal, actually. Sorry about that. If you go to low angle like that, of

**Dave Jones:** course you lose some of your graticule and stuff like that. So, if you've got it mounted high up on a bench, it's probably not the best thing. You really have to be looking pretty much either straight on or sort of down at an angle.

**Dave Jones:** It's designed for bench use. Like there's like standing or sitting on a bench and looking sort of down onto it like that. Anyway, it is a nice big screen 10.1 in 1024 by 600. Anyway, let's do a teardown of this thing and

**Dave Jones:** it's obviously going to be significantly different to the SSA 3000. Even though it looks like an identical unit, it's got the basic tracking generator, the same tracking generator, and the same RF input, which is going to be near

**Dave Jones:** identical apart from the bandwidth differences, but topology-wise and everything else. In fact, a lot of the chips, I'm going to assume that they're going to be very similar. So, only a bandwidth difference, but because it's a vector network analyzer, it's got to

**Dave Jones:** actually and it's two-port vector network analyzer, it's got to actually tap off the magnitude and phase of the source output. It's got to be able to measure that and the magnitude and phase of the RF inputs. So, it's got to have

**Dave Jones:** like a directional couplers built in to actually tap those signals off to get your phase and amplitude measurements, which allow all your vector network analyzing magic to happen. So, expect significant differences from a traditional spectrum analyzer. Let's whip that open, shall we? Oh,

**Dave Jones:** that's satisfying. All right, four screws there, two on the top. Pretty traditional stuff. Should lift off. The flippy feet are okay and I do like the rubber baby buggy bumpers on the bottom. Come on. It's got to be a clip

**Dave Jones:** somewhere. Hang on. There we go. And of course, can't see a damn thing. Got to get all the shielding off. Aw, there's no more trademark sealant rust. Nothing. Anyway, got ourselves a header there. All right. Just a few screws around the outside.

**Dave Jones:** See if we can lift this puppy off. Looks like the power supply is going to come out. We're in. We're in like Flynn. And of course, we expect our machine down in medium complete block for the analyzer section. Looks like we've got a

**Dave Jones:** tracking gen down there and stuff. We'll have one of the the directional couplers down in there. So, that's looking pretty sweet. And we've got ourselves separate little processor board here. Don't actually remember what the previous teardown was. Going to have to go watch

**Dave Jones:** my own video. And we'll take a look inside the power supply, but we've got a little piss ant fan there. I couldn't like there was a little bit of noise there, nothing really offensive. Air flow directly over this which comes

**Dave Jones:** through the vent holes in the power supply and also over the network analyzer itself or spectrum analyzer. Little heatsink on the power supply, but the main power supply down in here, well, somebody had fun, didn't they, with the selastic gun down in there.

**Dave Jones:** Wow, check it out. Um Lelon brand crap Lelon brand main DC filter cap, but secondary caps, I do believe they're Rubycon. Geez, that's all right. Not too shabby whatsoever. Nice. Anyway, does look nice, well designed and laid out. So, yeah, no

**Dave Jones:** worries. They've got nice folded metal work down in there, so no sharp burs to cut the wires there. Speaking of which, these are really quite sharp. I think I scratched myself on some of these. You've You to be careful taking this

**Dave Jones:** apart. Um, yeah, there's no rust, but uh they've added extra bonus sharpness on there. That's a fairly decent power supply for a low-end uh thing, you know? Uh could have done a little bit better, but not much. Uh the earth terminal down

**Dave Jones:** there, no worries whatsoever. Okay, if we have a look at the main board, very significant uh differences from the uh SSA 3000 model from a couple of years back. They've now put all the process and which used to be a Spartan 6 FPGA

**Dave Jones:** plus plus a TI applications uh processor, they've consolidated which was on the main board around here. Um, they've now consolidated that onto a single plug-in daughter board. And we've uh discussed this, there's many advantages uh to this. You could have

**Dave Jones:** like a standard processor uh platform across your product ranges, so they might be uh doing something like that. Um, and also it uh it keeps the hot all the high layer count uh stuff all on this much smaller board, so it's a

**Dave Jones:** little bit uh cheaper and easier to test and things like that. Really nothing doing at all apart from a uh Altera MAX II uh CPLD in there, so you know, nothing hugely uh grunty or special. And of course, the

**Dave Jones:** rest of it is just inside these blocks here, which looks uh for all the world like the same sort of configuration we saw in the SSA uh 3000 series, but of course, it's going to be significantly different cuz it needs those directional

**Dave Jones:** couplers uh couplers or however they're uh you know, tapping off the uh phase and magnitude for the ports and everything else to do that. So, you know, but apart from the spectrum analyzer, I mean, here's your RF input

**Dave Jones:** is uh going to be over here. So, this is your tracking gen, um but uh like the cabling's all looks, you know, fairly identical to the SSA 3000. So, that's interesting, but as I said, a lot of the

**Dave Jones:** RF uh cha- uh spectrum analyzer chain in here is going to be near identical. It'll be identical from a block diagram uh point of view, you know, the ADCs and other um stuff are probably all going to be the same and stuff like that cuz it's

**Dave Jones:** all digital IF and all that uh sort of jazz. Um but, you know, this the performance isn't quite as good and the bandwidth isn't as high as the SSA3000. So, I expect, you know, RF uh component differences in there.

**Dave Jones:** You can't leave your poor little watch crystal flapping around in the breeze like that. That's what the pads are for. Solder it down. Goodness sake. Well, hello, Mr. Ewart. There we go. We're going to have our transmit, receive, and

**Dave Jones:** our ground in there. Five-pin header, that's some sort of uh probably programming interface cuz these two look like uh different ones. But anyway, uh we can get in there and uh tap off the uh the boot loader and uh

**Dave Jones:** jazz like that. Hmm. Uh we can just get the boot loader there. No worries whatsoever. We're just going to have our uh serial interface adapter. Uh ground is pin uh one here and pin three is the 115k board uh

**Dave Jones:** serial output. We can tap that, use a terminal uh program, and dump it. Beauty. So, it turns out that we've got the processor. Looks like it's a uh Xilinx um Zynq uh processor, ARM Cortex-A9, and uh it's I'll post in the code down

**Dave Jones:** below on the EEVblog uh forum, and you can have a look for yourself. But yeah, it's all there. It's running a version of some flavor of Linux. All right, let's have a look at the tracking generator here. As you uh saw, it's

**Dave Jones:** actually got uh two connectors here as opposed to the uh 3000 model, which only has the one. Of course, one of them um it presumably is going to be the uh required VNA uh measurement uh aspect to that. It's

**Dave Jones:** interesting that they put it on a separate board. You can tell by the uh mouse bites in here that it was actually part of the panel the main PCB panel. So, it was all assembled at the same time

**Dave Jones:** by the same pick and place machine all the components on here, but then it was actually snapped off and used as a separate module. Now, there's no reason to do this electrically really because like you know, we've got

**Dave Jones:** the cable coming over here. Okay, if you want to have one point of ground, but actually snapping out the board doesn't really again you anything electrically. You could have just left the mouse bites connected and have your routed edge on

**Dave Jones:** there and Bob's your uncle. But, they've decided to take this out as break this out these tabs here and do it as a separate module presumably because this is probably tested on a separate test rig and it's just easier for them to do that than it

**Dave Jones:** is if it was a still part of this one main PCB panel here. And we've obviously got a JTAG header here for the Max II PLD there. It's probably just doing some you know, glue logic housekeeping something like that.

**Dave Jones:** I don't think it's powerful enough to do any real processing otherwise they would have used an FPGA instead of a you know, just an old Altera Max II PLD. Anyway, and I like how they've numbered the screws here. Number one actually takes

**Dave Jones:** them out from the chassis then takes apart these. So, let's it should just fall apart. Let's just take a look. Beautiful gold plating. Look at that. I've got our distributed element filter of course. Nice little bow tie arrangement there. Okay, to make heads

**Dave Jones:** or tails of this we're going to have to compare it to the previous model to see what they've added. But of course it's got all your classic block based approach. Look at this and the signals pass between the individual

**Dave Jones:** blocks like that and they're all shielded. They've got the solder mask removed or gold plated and you'll find that's matched under there. They machine out the little slots so the signals go, you can see that, signals just go

**Dave Jones:** between the individual blocks and that's how you shield one section from the other. Common as mud, you'll find this technique used on virtually, well, really any product right in the spectrum analyzer or not, that has any sort of,

**Dave Jones:** you know, gigahertz range like RF stuff. Even down, you know, on the sub gigahertz range you'd still do something like this and the bottom, let's take a look. Yep, not much at all. Oh, there's some extra chippies on there,

**Dave Jones:** double-sided load. They had to fit it in there but the rest of it's just all bypassing and stuff. Okay, as for the rest of it, take out all the number one screws and all the rest of the screws on

**Dave Jones:** the board and it should, in theory, lift out like that. Once you get those cables off up there, beautiful. Look at that. There you go, there's not much on the bottom as you'd expect, just some miscellaneous housekeeping stuff, some

**Dave Jones:** bypassing. What we want is all under here. So, that is really nice construction. I like that, how it all just comes apart in a block and we've got our, looks like our LCD driver board down there, is it? No, nothing special. This

**Dave Jones:** ribbon coming over here is for the rest of our front panel keypad and what's that 3M stuff down in there? Anyway, we're not too concerned with the rest of this. It's meh. All right, let's get ready for the rest of

**Dave Jones:** the RF porn. This should, yep, it's going to lift off. Lot more distributed element filters. Yeah, there we go. That's that's not a huge amount. Looks like we've got some directional couplers down in here as was seen on the uh

**Dave Jones:** previous design but you can see the signal flow from the RF input here through the various sections like this around there. It's tapped off with that distributed element filter, which there you go. There, that's where it's I suspect that's where it's going back. Um

**Dave Jones:** this one going over to there. So, we're tapping off that, which we probably didn't have in the uh previous version, I suspect. Then you can just see flow through the various blocks. And I've gone through it in quite some detail um

**Dave Jones:** on previous ones. Like a 40-minute video or something like that just going through the architecture of a uh spectrum analyzer like this. But, of course, this has some VNA Well, it has a two-port VNA capability as well. Um so,

**Dave Jones:** I'll probably just go through the differences here. Um as always, high-res teardown photos over on uh eevblog.com if you want to see it for yourself. And yes, well, let's have a look at the bottom. And yeah. Just some housekeeping stuff. Some

**Dave Jones:** bypassing. Nothing hugely special. All right. So, let's take a look at the main spectrum analyzer board. I've got the original SSA 3021 um X, the uh 2.1 gig / 3 GHz uh spectrum analyzer, the original model from a couple of years

**Dave Jones:** ago, on the left, and the new one, the SVA 2015 VNA, on the right. And I'll try and uh keep the left-right thing going for the rest of this uh video. And if you want a very detailed, in-depth look

**Dave Jones:** at how a spectrum analyzer uh works on a block-by-block basis, as in, you know, signal comes in here and then it, you know, signal goes down here like this, and then it goes through the mixer, and then like it There's you know, a local

**Dave Jones:** oscillator and all that sort of stuff, and then it goes through a mixer and a saw filter, and blah blah blah blah blah, and then the intermediate frequency comes out and goes in the ADC, all that sort of stuff. I've done it in

**Dave Jones:** the previous video. It goes for like half an hour or something. I walk you through each section. I won't do that here. Um for this VNA, what I'm going to do is um just have a look at the

**Dave Jones:** differences. So, I've got a photo of the main board here. Now, the VNA, uh the SVA2015, I had to actually flip the board. So, if you the writing's back to front on the chips, you know why because they

**Dave Jones:** actually put the physical components on the other side, effectively, the other side of the board. You can see that with the um with the connector up here. It's actually physically on the other side. So, I just had to flip it so they match.

**Dave Jones:** And you can see it's reasonably similar, but there are some differences. Like, presumably because it is lower frequency, it's 1.5 gig uh maximum over here, whereas this design is designed for uh 2.1 and 3 gig. They've got a I

**Dave Jones:** believe they've got a 3 GHz model. So, um they're obviously looking for that lower frequency range and also uh to lower the cost as well cuz the uh this VNA is a lower cost product in terms of spectrum analyzer compared to

**Dave Jones:** the previous model. So, let's have a look, okay? Here's our RF input here. It goes through a 50 ohm attenuator here. This is all the same. Now, this is interesting. The original one had a proper 20 dB attenuator. If

**Dave Jones:** you have a look in there, it's actually a uh ceramic little ceramic job like this. And uh that was a switchable attenuator. Like, you you know, you go into the menu option and you switch that and it enables that. But, the new one

**Dave Jones:** doesn't seem to have that and it's not on the bottom, either. So, I'm not sure if they even have uh like, you know, I can't get the detail on these chips. I'm not going to go into there, but uh it

**Dave Jones:** looks like that's just like a driver or whatnot. Um so, I think what they're doing is they're actually doing the uh attenuation inside this what was a digital attenuator before over here, they actually use a different chip. Now

**Dave Jones:** they've got a Peregrine uh semiconductor, and here's the data sheet for that. Uh Peregrine semiconductor um attenuator here, and that actually, I think that's where they're doing all of the attenuation in there. So, maybe this chip is like, you know, lower cost,

**Dave Jones:** they've refined it's a couple of years later, and uh maybe if they made the 3000 model again, they might change back to this Peregrine semiconductor part. I don't know all the performances are as good or whatever as the original 3000

**Dave Jones:** model, but anyway, uh apart from that, um you know, it's it's basically the same front end as you'd expect, and then we've got a preamp here, we've got a preamp over here. I don't know, I'm not going to

**Dave Jones:** bother looking at the part numbers, but it looks very similar arrangement with those two eight-pin uh chips there and there, and this little job here, which is probably, I don't know, is that just like a power supply, a local uh

**Dave Jones:** regulator, or something like that? Uh that's unsurprising. And then, I've probably got all this detail in the original um teardown of this uh 3000 model. I go into like detailed data sheets on each one of the chips. Anyway,

**Dave Jones:** then it flows down into the low-pass filter, which you can see here, they've got it as a distributed element filter, whereas over here, they've decided, "Well, we don't need this distributed element filter rubbish. Um we can just do this with our um with our caps and

**Dave Jones:** our um in inductors." Whereas, that's basically what they're doing over here. These circuit elements, right? These are inductors in here, and these elements over here uh capacitors, and that's exactly what basically is happening over on this one over here. We've got inductors and

**Dave Jones:** capacitors and that forms our um um low-pass uh filter. Then it goes into the mixer. I looks like the mixer might be It looks like it is a different part. But basically uh the topology's all going to be the same. The crazy thing

**Dave Jones:** about this is if you have a look on the right, they have actually changed the chip from the HMC 400488 to the HMC 213. But the HMC 213 is just as obsolete apparently as the original one used in the original. Why would you

**Dave Jones:** use an obsolete part in a new product? Now, the mixer is fed from this uh bowtie low-pass filter here and they've got the same bowtie low-pass filter over here. It's physically larger by the looks of it. I mean, the

**Dave Jones:** sizes of those boards are very similar, but the So, the characteristics are going to be different. Uh this one's going to be probably physically bigger because it's lower frequency, but it's basically doing um exactly the same thing. They've the side to use a

**Dave Jones:** distributed element filter there. And then uh this original design goes directly into the coupler like this, whereas this one has got some extra stuff in there. So, maybe it's got like an extra um a driver or something like that. I

**Dave Jones:** don't know what's going on there. But anyway, it's the same topology. The general topology is the same. It goes into a coupler like this. But here's where I there's a huge difference. Here's the VCO, the uh voltage-controlled oscillator, the PLL.

**Dave Jones:** This is the first local oscillator. It's basically uh the same. I haven't looked into detailed in the uh parts in there like, you know, they've got some regulators down in here to um uh you know, local regulation. There's

**Dave Jones:** local regulation all over these boards. So, you'll find like little chips here, probably here, here as well. Um these are all like uh local regulation cuz there's not just the one 3.3 V rail or whatever it is powering this whole thing

**Dave Jones:** to because these uh sections are so critical, you need to isolate power, particularly say for a preamp, for example, that needs its own local regulation. Um you know, and this mixer might need its own regulation. These are critical

**Dave Jones:** RF parts. It's why they go to all the effort to separate all the sections like this and then shield them with the big aluminum block and all that sort of stuff. So, not only do you have to shield them separate eliminate crosstalk

**Dave Jones:** between them, you also want to eliminate crosstalk by way of the power supply. So, you have local regulators and stuff like that. Anyway, we've got our VCO, our PLL, our first local oscillator. Basically, the same thing happening here, okay? But

**Dave Jones:** look what's going on here. This has got a frequency doubler in here. I don't think we've got that. And we've got some single pole double throw switches in here, which we don't have over here. In this case, look, it's going directly

**Dave Jones:** into the coupler. Whereas if that was happening over here, it would have bypassed all of this stuff here. All this stuff is additional on the 3000 model because it's higher frequency and it has to get the different frequency

**Dave Jones:** ranges. So, this is the interdigital band pass filter here. There's three separate sections and there's switches up here to divide the signal into those and then combine them over here, some more switches, and then it finally goes into

**Dave Jones:** the coupler. Whereas the VNA over here just goes directly from the local oscillator straight in to the coupler and doesn't have all of this stuff. So, that's a significant cost saving. Obviously, like there's no cost involved in say these interdigital these

**Dave Jones:** distributed element filters, the band pass filter here, there's nothing in that. Um no component cost. It's just uh board space. But all these extra chips you got to buy, you know, this frequency doubler, these uh switches, these are

**Dave Jones:** proper RF switches aren't cheap and stuff like that. So it avoids all that because it doesn't have the frequency range and possibly the performance of the original 3000 model. So that's probably the major difference in this entire design. Uh

**Dave Jones:** now, let's go back to the mixer here. So we've got our whoop, we've got our mixer over here like this, and we've got our mixer here, okay? So and then that goes into an amp here. It looks like it's a

**Dave Jones:** different amp amplifier chip. Look, they've got a little um QFN package down in there. It's a Hittite one. I probably showed the data sheet in the uh previous video, but this one over here has just got a little six-pin uh SOT23 package.

**Dave Jones:** Anyway, that's probably like an amplifier. And then um it's actually got these. Looks like it's got them uh back to front. Here it's got a bowtie low-pass filter as a distributed element filter. The low-pass filter is once again just done with uh discrete

**Dave Jones:** capacitors and inductors in there. Um for performance reasons, I don't know. They maybe uh chose that. Of course, because the distributed element filter is actually lower cost. You got to pay for these capacitors and inductors, but you know, they're trivial cost in the

**Dave Jones:** scheme of things. Um so maybe it was just a performance thing that they uh went away um they went away from the distributed element filter. Anyway, they've got the bandpass filter here and the bowtie filter back to front. Not that it makes really

**Dave Jones:** any difference, I guess. Anyway, they've decided to swap those two around. Um but once again, we've still got a distributed element filter bandpass filter. And you can see it's physically bigger on this lower frequency model than it is on the higher frequency um

**Dave Jones:** 3000 model over here. So, you know, you see some physical differences, but it's still doing the same thing. You can see the topology between them is exactly the same. It's a band pass filter implemented as a distributed element

**Dave Jones:** filter. Anyway, that goes into a mixer over here and it goes into a mixer over here. Exactly the same thing. Some physical location uh differences here. Anyway, that mixer uh is being fed from the second local oscillator here, which then goes into a

**Dave Jones:** low pass filter, a band pass filter, and goes into the mixer. Over here, it's the second local oscillator, a low pass filter. In this case, I don't think there's any band pass filter there. Um so, they've just got a low pass filter

**Dave Jones:** once again instead of a distributed element filter. Um they've got that as a discrete component filter here. But anyway, second local oscillator into the mixer exactly the same thing. And then out of the mixer goes into a uh saw filter. That's these

**Dave Jones:** two parts down in here. There we go. They're the saw filters and I believe I included the data sheet on the previous one. Uh I won't go through it again. But where are we? Yep, saw filter. They look very similar

**Dave Jones:** to me. So, there you go. Saw filter and then into the mixer. What is that? A Got to have a mirror to read it. Anyway, um it looks very similar to the mixer over here, but no, I think it's

**Dave Jones:** not it it's a different one. You'd expect a different uh performance mixer in there. Anyway, and it looks like there's a couple of differences in here. The output of the mixer um um to a switch, another switch over here. They

**Dave Jones:** have the same switch part over here. Um but basically then that goes straight to the output here. Okay, that's the intermediate frequency output on the previous design, uh which then went via the coax. But the new VNA is a bit

**Dave Jones:** different. They didn't have uh in the 3000 they had that as a separate physical block, a separate aluminum block that had the cable going over and they had the ADC um in there and the filter. But uh this, so

**Dave Jones:** all this stuff is now implemented in the main block here. So the 12-bit um analog to digital converter, which I believe is the same one, I'll have to verify, same one they had in the 3000, but it was

**Dave Jones:** mounted on the separate board. But it's now built into here. They just went, "Ah, bugger it, we don't want to have a separate physical block, we can just put it on this main board. Thank you very much." And then another difference is

**Dave Jones:** that the VNA seems to have its reference oscillator under here. Once again, these look like some regulators, dead giveaway in that there's just a cap on the outputs uh there. So they're uh powering all this stuff and locally, of course, um and

**Dave Jones:** that's our 10 MHz reference oscillator, whereas that was external on the main board um on the 3000 model. So that's, you know, substantial difference there. So as you can see, like from a functional uh block diagram point of

**Dave Jones:** view, it's, you know, it's very similar, but a different performance level to the original 3000 model. And that's exactly what you expect because it's the same topology spectrum analyzer, you know, it's all digital IF, so it's, you know,

**Dave Jones:** got to get the intermediate frequency output and then it digitizes all that, which is, you know, different to uh previous, you know, really older generation uh spectrum analyzer, like analog spectrum analyzer designs for example and they're doing exactly the same

**Dave Jones:** thing. But at this point we don't readily see any huge differences for the VNA. The only thing we see is like we've got this circuitry up here like this which doesn't look like much doing. There's an unpopulated little RF connector there but you'll

**Dave Jones:** notice that the new VNA model has you know significantly different components on there. They you know like quite similar anyway. I'll have to show the bottom of that but we have an additional RF connector here that we didn't have previously.

**Dave Jones:** Okay, so what we need to look at now is the tracking gen and we've got the SSA 3000 on top and the new VNA 1015X on the bottom here and you can see that they're very similar. Once again,

**Dave Jones:** everything's mounted on the other side of the board so I've had to flip it so you can see here that the connectors are physically on the other well here on the other side of the board like this compared to the two models. So that's

**Dave Jones:** why on the SVA one you might find that the well you will find that the text is mirror image cuz I had to flip it. Anyway, you can see that the topology is very similar. Okay, here's our tracking

**Dave Jones:** generator output here and you can see that comes from pretty much identical circuitry around here. We can go like the individual chips might be a bit different but of course we've got a different frequency range tracking gen. So you know you'd kind of expect that

**Dave Jones:** and here is the input coming from that coupler that we saw on the main board and once again you know like this stuff around here looks to be similar to what's here. I don't know what's doing here. These look like Macrel voltage

**Dave Jones:** regulators I think. Anyway, anyway, so comes in here, does the same thing. We've got a bow bow tie low pass filter like this, goes up that chip there looks identical. We've got this going across here, here, and once again, we've replaced our

**Dave Jones:** distributed element filter with a discrete component filter. But apart from that, yeah, that is our tracking gen. It's all exactly the same. And all this stuff over here, what have we got? We've got a well, can't see that because it's mirror

**Dave Jones:** image. Got there H835 and H835. If you want to look at that mirror image. So exactly the same stuff going on here on the new one, pretty much. But the only difference is down here. Look at this. Aha, we have that extra RF

**Dave Jones:** connector going over that we saw on the main board that we didn't have before. And you'll notice that whereas this is its own isolated block up here, it now breaks that isolated block and the signal comes down here.

**Dave Jones:** This is actually a digital switch down here. We can pull up the data sheet for that one. So these two parts down here are HMC284 non-reflective switches DC to 3.5 gig for those playing along at home. So, you

**Dave Jones:** know, overkill for what we need here. So what it looks like they're doing is taking the tracking gen output and actually feeding that back through these switches into there like that, which then goes via coax over back to the main board, which then I

**Dave Jones:** think what's happening is they're using There's no dedicated circuitry to measure the reflective power cuz that's basically what you have to do in a vector network analyzer to get your S11 parameters um for your uh for your VNA is to

**Dave Jones:** measure the reflected power coming back from your tracking generator output, cuz that's exactly what we have to do. So, what they're doing is actually using the existing spectrum analyzer measurement hardware uh to actually then measure the reflected power. So, they must be sort

**Dave Jones:** of like multiplexing between doing the spectrum analyzer sweep and then doing a reflected power sweep. It seems like that's how they're doing it anyway. And if so, that's a very way and that's a very clever way to do it with very

**Dave Jones:** little additional hardware. I mean, look, you know, just this additional hardware here, which is basically bugger all, plus a little bit extra on the main board to feed it back into the spectrum analyzer input, and Bob's your uncle.

**Dave Jones:** So, if we go back over here and have a look at where this one goes, back over to our main board, you can see it actually comes in here like this. So, it's associated with this circuitry here. It looks like

**Dave Jones:** there's just regulators and other stuff on the back. So, I'm not exactly sure what's doing here, but there may be a path for this to come through. Is this an additional Is this a switch that then switches this path back into here so

**Dave Jones:** that it can measure that reflected power over the bandwidth and use the existing use the all the existing spectrum analyzer hardware that they've got in here to measure that. Um you know, to measure the phase and the amplitude of

**Dave Jones:** that. So, I think that's I think that's possibly what they're doing, cuz there's basically you know, like there's no actual measurement hardware going on in here. So, I think they're just switching it through that reflected power. Neat, huh?

**Dave Jones:** In fact, that's, you know, without deeper analysis, that seems to be what's going on here. And it makes sense because they're doing traditionally what is a very expensive functionality in a VNA. There's a reason that they're very expensive and doing sort of like low-end

**Dave Jones:** VNA functionality and blending it with a traditional spectrum analyzer. That's basically all there is to it by looks of it. So, how much cost are they adding just for that plus this over here, you know, just just a

**Dave Jones:** couple of switches and an extra coax going back to do the VNA and do some software smarts and multiplex between them? That looks like what they're doing. Brilliant. Well done, Siglent. All right, let's just take a quick look

**Dave Jones:** at some operational capabilities of this thing. This is, as I said, not a review cuz it would take me a month of Sundays to look at every aspect and every feature of this product. It's just absolutely ridiculous as is just any

**Dave Jones:** normal spectrum analyzer, let alone one with VNA and other capabilities. It's just nuts. Anyway, let's just have a look at some typical noise floor here. I've got an unterminated input resolution bandwidth of 10 kHz, just a smidge above -115

**Dave Jones:** dBm there and rising up as is fairly typical. I think that's a little smidgeon better than the 3000 series. But, I don't have the 3000 series scope here to actually compare it with. You'll have to watch my previous video. But

**Dave Jones:** anyway, this is a much better result than say the Rigol one. There's just no competition, really. And this is with the preamp turned on. Now, if we change our resolution bandwidth up here, we can there there it is at a megahertz,

**Dave Jones:** for example. So, as typical, uh the update rate is much faster at that. Um and we can turn the uh preamp off and on here. Here we go. That's on and off. It's not nearly as good with that uh

**Dave Jones:** preamp off, is it? Meh, that's how it works. I expect the spectrum analyzer functionality to be basically equivalent performance, almost the same as the 3000 series. So, I've already gone through that. I won't bother. Uh what we're interested in is

**Dave Jones:** uh some of the more um some of the different modes here. So, let's go into uh distance default here, and let's give it a whirl, shall we? And ta-da! There it is. I've just got a coax flapping around in the breeze here, just

**Dave Jones:** unterminated at the end, and sure enough, um there it is, about 0.81 m. And then we can, you know, plug in a uh a terminator on the end of that, it'll drop. Hang on. Expected it to drop, but yeah, there we

**Dave Jones:** go. But, yeah, we're still, you know, 0.86 m there. Near enough. We haven't calibrated this thing uh yet. So, to calibrate it, we would actually need the calibration kit, and you'll see this in um not only just in this mode, but other

**Dave Jones:** modes as well. So, you basically need that calibration kit in order If you're doing, you know, proper quantitative measurements and all this sort of stuff, it basically you do open short uh compensate open short load compensation on the thing. Um so, yeah, we don't have

**Dave Jones:** that cal kit, which is Like, they should just include it. Like, this is a It's on the front here, spectrum and network vector analyzer. It's a VNA. Yet, the VNA is optional extra, and even when you buy the VNA, you don't even get the

**Dave Jones:** bloody calibration kit with it. Like, how much is that worth? Like, bugger all. And yet, I think the street price is like for the cow kit, I don't know, a couple hundred bucks or something. But, they should throw it in. This thing

**Dave Jones:** would be a killer if it had the VNA capability built in for the base price of like under 1,400 bucks in the cow kit. Unbelievable. doll PEM CAC And if you're curious to see the basic tracking gen performance, that's 1 DBM

**Dave Jones:** per division there. It It's fairly typical. I'm not sure if that's any better or worse than the 3,000. Okay, so let's go into our vector network analyzer, VNA. That's what we're here for. And I've got it on the output

**Dave Jones:** unterminated. It can only do S11 and S21 cuz it's a two-port analyzer and they're the basic measurements. You've got reflected power and your transmitted power basically. So, if we look at S11 or the reflected power in here, where are we? We're 1 dB per division

**Dave Jones:** there. Let's whack on our empty coax, shall we? And we should see Yeah, bit higgledy-piggledy over the line there. Let's plug in our This is over the full span, 1.5 gig. Let's plug in a terminator on the end of

**Dave Jones:** that and just have a look. Where are we? We want our scale per division. Let's go to 20 dB per division. There we go. Sweet. And that's our basic log magnitude. But, of course, we can do Smith charts or anything else. Let's

**Dave Jones:** have a look at Basically, log phase Smith chart. Oh, ain't it beautiful? It's pretty. It's full of stars. That's actually very cool. Check that out because you can They would you to those lobes that will get in over the

**Dave Jones:** entire band there. And basically, I won't go into Smith charts. There's actually no markers on this thing at all. There's no identifiers. It's just a blank screen. So, that's you know, not terrific. Would have been nice to have

**Dave Jones:** some identifiers on there. Um but these basically represent uh pure resistances, these circles. So, this one might be 50 ohms for example. And then if you d- and then these lines going out here represent your complex impedances going in your different phase

**Dave Jones:** angle like that. So, you know, because we're fairly close to an ideal resistive load there, it's kind of in the middle like that. But we should see something funky if we actually disconnect this. Ready?

**Dave Jones:** Woohoo! Go! Brilliant. It's going to get funkier though if we put it back. Aw, I could like to play with this all day. The interesting aspect of this, look, if I just loosen this BNC, we're actually changing the character I just touched it

**Dave Jones:** there. We're actually changing the characteristic of the termination. If I just like twist it and loosen it like that, just a little bit, check that out. Significantly different. Just by mucking around with the load like that. Look at that. I just loosened it off a

**Dave Jones:** bit. Wow. See the difference? That's terrific. But of course, that's um over the full span of uh yeah, oh there it is, 10 meg to 1.5 gig. So, let's actually change that. Let's go into um sorry, our span here. Let's go into

**Dave Jones:** Let's say Let's do I don't know, 100 megahertz span for example. It should sign- show significantly less artifacts like that. There you go, cuz we're not over the full range anymore. And if we drop that down to 10 MHz,

**Dave Jones:** it'll probably go to a point. Will it? Will it? Yeah, pretty close. And of course, we can do all the different formats here, but let's not worry about that. As cool as it is, um let's actually go back. How do we go

**Dave Jones:** back? There we go. And we can uh change the scale, of course, of our actual chart here, our Smith chart. Oh, there we go. We're going to go under. We're going backwards. There we go. Small up. Down to um half. There you go.

**Dave Jones:** And up, we should start seeing above that, we should start seeing multiples. Yeah. There we go. Oh, it's so pretty. Anyway, all the RF aficionados are getting very excited. Now, I was going to show you this demo with my telescopic

**Dave Jones:** uh rod antenna, but unfortunately, um I can't find it. It's in the lab here somewhere. So, we'll make do with this state-of-the-art antenna here, which is our yellow wire. Um and don't fiddle with it, because that'll change the characteristics of your

**Dave Jones:** antenna. So, we're basically measuring the reflected uh power from the antenna here. So, I was going to use my telescopic rod to show you that when I move it in and out, it changes, but we can do the same thing by I won't touch

**Dave Jones:** anything else. We'll just do a snip of our antenna. There we go. That's going to significantly change Oh, I'm getting out of there. Significantly change our antenna. And snip it again. OH, SNIPPITY-DOODAH.

**Dave Jones:** IT'S BRILLIANT. LOOK, I love it. And we're going to shorten our antenna again, antenna again, which of course changes the characteristics and changes what reflections we get back from the antenna. And we can visualize that in terms of complex impedances on our

**Dave Jones:** Smith chart. So, there you go. It's fun. Anyway, what uh uh You can play with this all day. It's great. Okay, let's try the demodulation capability modulation analysis of this thing. I've just got a 1 gig carrier here with an amplitude modulated 1 kHz

**Dave Jones:** sine wave on here. So, let's go into mode and modulation analysis. Let's have a play around. Um Hello. Where's my AM option? AM and FM. I do believe like I think these are like you buy them as different options, but why I

**Dave Jones:** wouldn't have AM and FM? What the What's going on? System. Oh, like where's all my stuff? There's all our system messages, by the way. That's when I did the PEBCAK. I'm overloading my ADC. Oops. Sorry. No, looks like it's not installed. AMA. Uh

**Dave Jones:** Bugger. Anyway, bugger that. Um I'm not going to muck around with the modulation analysis. Suffice it to say that if you fed in your What have we got? Um your amplitude shift keying in here, then you'd be able to see your waveform if

**Dave Jones:** you had your AM modulation. It should be able to decode um demodulate and show you that 1 kHz sine wave. That's the idea, anyway. Anyway, I think that'll do it for this video, which is a teardown and a quick little look at this thing.

**Dave Jones:** Um as I said, a review video would take a weekend of Sundays to do, so I'm not sure if I'm going to be able to do that at this stage, but others are talking about this on the EV blog forum. They

**Dave Jones:** have units in hand and they can, you know, do tests and things like that. I'm sure there'll be no end of discussion about this, but it is a very interesting bit of kit. It's basically the first low-cost VNA in this sort of form

**Dave Jones:** factor. You can get other ones that you know, plug into your USB port and they come with PC software and all that sort of jazz. And And I think like apart like the good brand ones are very sig

**Dave Jones:** like double the cost of this one for example or significantly more. I know there are potentially some cheaper options than this because this is basically going to be two grand by the time you include the VNA. Now, whether or not they're going to

**Dave Jones:** like do any bundling options, maybe not at the start, but as we're seeing with not only Siglent but the other manufacturers, once these have been on the market for a while, competition comes in or the sales aren't what

**Dave Jones:** they're expecting, they start bundling in the options. And if they bundled in the VNA for $1395 or whatever, wow. I think that'd be an absolute killer. Like it's not going to set the world on fire in terms of vector network

**Dave Jones:** analysis. I mean like you can't do like your different like you can't separate as far as I I'm aware anyway, you can't like separate the screen and display the different functions and things like that. So, that would have been nice. So,

**Dave Jones:** it's kind of you could call it like rudimentary vector network analyzer, but it What was that? What was that? Was that a bug? Is that a bug? Is it going to happen again? Sweeping across? Might have an acquisition bug there. I

**Dave Jones:** didn't touch anything. Bellying breed on it and just yelling at it. Um yeah. So, that's interesting. But uh yeah, I'd expect the firmware to be relatively mature cuz it's probably based on um the existing 3000 series, which has been

**Dave Jones:** out for several years now. So, I haven't been in keeping up with sort of like the firmware bug fixes and things like that. But, uh anyway, it should be reasonably uh mature at this stage. And if you're in the market for a vector network

**Dave Jones:** analyzer, jeez, check it out. But, uh yeah, it'd be interesting to compare something like this with like maybe a uh low-cost or a similar cost uh USB-based vector network analyzer. I know there's a couple of do-it-yourself projects. Uh

**Dave Jones:** There's been uh maybe a Kickstarter or two out there for a uh VNA, hasn't there? Um but, anyway, it's a very interesting bit of kit for those into uh RF stuff. Not only for, you know, antenna tuning, but uh you know,

**Dave Jones:** diplexers and filters and all sorts of uh you know, RFE type things that you want to uh measure and calibrate the performance of. And in this case, this can do your basic uh S11 and S21 parameters. So, um

**Dave Jones:** any bit of kit. Uh you could argue that it's probably a bit pricey for the uh 600 over 600 bucks for the VNA option, but I don't know. Um you'd have to compare it with the competition on the market, which I don't

**Dave Jones:** have at the moment. Anyway, Siglent could have a winner on their hands here. It pretty much comes down to uh price and market uh penetration and stuff like that. I wouldn't like to speculate what the market is for a for the low-cost

**Dave Jones:** VNAs and stuff like that. You pretty much got to be into the RF uh side of things to get value out of this. If you're just a your regular basic hobbyist or basic engineer working on stuff, then a VNA is not something

**Dave Jones:** that's ordinarily part of your kit. But, I guess to have the option later to actually just buy it if you need it, then just buy the software license, bam, away you go um with your existing bit of kit. If you're in the market for a new

**Dave Jones:** spectrum analyzer, then it might be worth a look, but it is limited to the 1.5 gig. It is there is no option to go higher. There's no as far as I'm aware the hardware internal is only designed for 1.5 gig. They have no intention of

**Dave Jones:** going higher. If you want higher frequency, that's what the 3000 version is for, but it doesn't have that vector network analyzer stuff. Whether or not they're going to come out with like a 3000 a SVA 3000 version, wouldn't surprise me at all in the

**Dave Jones:** future, but I don't know anything about that. Anyway, this one is a fun bit of kit. So, it's definitely worth checking out. As always, discuss down below EVblog forums the best place to discuss test gear and stuff like that without a

**Dave Jones:** doubt. And as always high res teardown photos down below, so you can have a play around with it. And no, I don't know anything about hacks for these things. So, yeah, I don't know. People might be able to do it in

**Dave Jones:** the future. Who knows? Anyway, hope you enjoyed this little look at the SVA 1015. If you liked it, please give it a big thumbs up. The video that is. May or may not like this. I don't know. Anyway,

**Dave Jones:** catch you next time.
