---
video_id: uq1DMWtjL2U
title: EEVBlog 1436 - The TOP 5 Jellybean OPAMP's
url: https://www.youtube.com/watch?v=uq1DMWtjL2U
source: youtube-asr
---

**Dave Jones:** Hi, today we're going to take a look at a whole bunch of different jelly bean components as they're called or industry standard components that you're pretty much expected to know right off the top of your head because you'll use these

**Dave Jones:** parts over and over and over again in your career and in the teardown videos you've seen me do, you'll no doubt have seen these these parts countless times. And when I'm doing a teardown, I don't even have to say anything more than the

**Dave Jones:** part number because you should instantly know what these chips are. They're called jelly bean components. So it's very important for any design engineer to have intimate knowledge of these a whole bunch of these jelly bean components so that you can just go, oh

**Dave Jones:** yeah, I need this chip for this particular task here. Oh yeah, just throw in the jelly bean part because right off the top of your head, you know the specs, you know it's going to do the job, it's going to be good

**Dave Jones:** enough, and that's why these parts are everywhere. And as you'll see in well, our first one here, it's been around for like 45 years and this is where most of these jelly bean parts have. Now, my definition for a jelly bean part is A,

**Dave Jones:** it's been around for a long time, B, it's available for many different manufacturers, C, it's like cheap, it's dirt cheap, and four, it's available because available from many different manufacturers, it's so ubiquitous. It's it's just like typically there's millions of these

**Dave Jones:** things in stock even during like times we have like this with the component shortages and things like that, you can almost certainly still get these jelly bean components from someone because if your the manufacturer you've specified in the bill of materials doesn't have it

**Dave Jones:** for some reason, well, you can pretty much throw in any equivalent part with the same part number and you know it's going to do the job because it's a jelly bean component. The first one we're going to take a look

**Dave Jones:** at here is the LM358. It's a dual bipolar op amp. So if you need just a basic run-of-the-mill op amp to just do basic stuff, then the LM358 is a great choice. It's a dual op-amp, and they specifically call it an

**Dave Jones:** industry standard op-amp because it pretty much is. So, it's two op-amp independent op-amps in the one package. There's pretty much no reason to use a single like op-amp jelly bean component. If you're going to like put and choose

**Dave Jones:** an op jelly bean op-amp, you might as well choose the LM358 because it's a dual one. Even if you don't use the second op-amp, hey, it's adds flexibility to the design later. You've got that second op-amp in you might be

**Dave Jones:** able to budge it in to your circuit or something like that. At least you have it available. It's designed in. So, yeah, dual op-amp handy. And as you can see, it's available from many different manufacturers here. Like I've only got

**Dave Jones:** three of them, but there's dozens and dozens including like no-name ones from China or whatever. So, as you can see, the date up here, look, June 1976. This is 45 years old, and it's still sold in the millions or billions. I don't know

**Dave Jones:** how many of these are sold every year, but it is the go-to op-amp, the LM358, also known as the LM2904. And 2904 is just like a higher temperature grade version, sort of like a more commercial industrial temperature range than the LM358. And it's available

**Dave Jones:** in different versions, the B version and the A version and stuff like that. And there are some slight spec differences between them, but if you're designing in a jelly bean component into your circuit, generally aren't pushing the specs. You don't really care whether or

**Dave Jones:** not you get the A version or the B version or anything like that. If you're worried about that sort of thing, then you're not really in the jelly bean category, so to speak. So, yeah, I'm I'm just going to run with that description

**Dave Jones:** anyway. Sometimes you might want to do that, but as a general rule, no. If you're after tighter specs, you'll go for a more non-jelly bean component. Some features of the LM358, it works anywhere from 3 to 36 volts. Brilliant.

**Dave Jones:** So, huge wide-ranging operation that includes both unipolar and bipolar supply. So, single supply or a split supply. It's relatively low power, 300 microamps per amplifier. That's not too shabby. It's got a unity gain bandwidth of 1.2 megahertz. Once again, that's not

**Dave Jones:** too shabby, a meg, and it is unity gain stable. So, it's stable, it's not going to oscillate with a gain of one. And also another important thing, the common mode input range includes ground. So, that enables direct as it says here,

**Dave Jones:** direct sensing near ground. If you go over to say the Rome data sheet, it actually says calls it a ground sense operational amplifier. And that's huge advantage in terms of like if you want to do like a low side current shunt

**Dave Jones:** measurement or something like like a non-critical current shunt measurement, just you know, to a modicum accuracy, then it's a pretty good decent job for that. It's got a low input offset voltage, low, 3 millivolts. Once again, this is a jelly bean component, jelly

**Dave Jones:** bean specs. But this is just a guaranteed figure. The the typical figure is like 300 microvolts. It's an order of magnitude better than that. But just be aware that that offset voltage and the EMI filters here, if you go down

**Dave Jones:** here, you can see that that is specific to the B version here, 3 millivolts like that. If you go for the regular A version, which is what's available from other manufacturers in the I'm not sure if TI are the only ones that do a B

**Dave Jones:** version, just be aware of that. But the A one, you know, once again, it's around 1 millivolt typical, something like that. So, you know, good enough, but you can it's nice to know that you can get like a tighter version available from TI

**Dave Jones:** in the B version. But if you're designing this in, you have to be aware that that you may be limiting yourself to one manufacturer. So, if you design it in, once again, a typical 1 millivolt, something like that. The ST1 over here,

**Dave Jones:** 1 millivolt. So, you know, but that's good enough for a ton of applications. That's why it's a jelly bean part. And I won't bore you with all the other specifications and things like that. It just suffice it to say that this is a,

**Dave Jones:** you know, just a nice general purpose op-amp for non-critical applications. That's why you're going to use it. And as you can see here, it's a bipolar amplifier design. None of that CMOS rubbish. We'll look at that in a minute.

**Dave Jones:** And so, it's not going to give you rail-to-rail performance. I'll show you one that does in a minute. And the great thing about jelly bean components is they're typically available in many different packages. Look at this, eight different packages from TI here. Um,

**Dave Jones:** like PDIPs, like your regular, you know, DIP hobby ones, your SOs, your SOT23s, your TSOPs, your SOICs, your ceramic packages, your LCCC packages, and stuff like that. And you can see those over on the data sheet here. ST ones are

**Dave Jones:** available in four different DFN packages. But of course, you have to be careful if you specified in, say, the ST DFN package here, you might not be able to get that from TI, for example, or from uh, someone like Rohm, for example.

**Dave Jones:** Oh, no DFN there. So, just be careful. But in general, if you're choosing a jelly bean component, you're typically going to use a jelly bean footprint as well. So, you can see some differences in here in the spec,

**Dave Jones:** like this Rohm one is like 4 1/2 mV maximum and stuff like that. The input bias current, by the way, 20 nA. Pretty good for uh, bipolar stuff. The other great thing about jelly bean components is the pinouts are going to

**Dave Jones:** be identical across all the chips. In fact, this is the industry standard pinout for a dual op-amp. So, there you have it. The LM358 is my pick for the jelly bean, uh, just bipolar op-amp. It happens to be a dual one. I don't really

**Dave Jones:** have a jelly bean single op-amp, you know, a 741 or whatever. Nah. Just like LM358 comes in the same package anyway. You might as well get a dual jobbie. The LM358 still going strong after 45 years and that's why it's my pick for the

**Dave Jones:** jelly bean op amp. Next up is a jelly bean FET op amp and well, this one's hard to beat as well cuz it's September 1978 here and it's a classic TL07 series. The TL071 is a single, 072 is the dual, 074

**Dave Jones:** is the quad. So, really, you know, pretty easy to remember. Once again, available for many different manufacturers and it's kind of a little bit better and a little bit worse than the LM 358. Um you know, it's got a reasonably

**Dave Jones:** high slew rate. The offset voltage is 1 mV here. Offset drift 2 microvolts per degree C. It does have higher power consumption though, even though it's a an actual FET input op amp. And as you can see up here, it's actually

**Dave Jones:** designated as a low noise FET input operational amplifier, but in terms of noise, it's actually on par. Here you go, input voltage noise there. We're talking about, you know, 9 microvolts peak to peak. That's a typical. Whereas the

**Dave Jones:** LM358 is actually only a typical 3 microvolts peak to peak. It does have lower noise density though than the 358, which is about 40 nanovolts per root hertz and the 071 is about 18 nanovolts per root hertz at

**Dave Jones:** 1 kilohertz there. So, you know, lower noise density, but in terms of input noise and stuff like that, but it does have a low total harmonic distortion. .03%. This is why it's very common. You'll find these in lots sort of audio

**Dave Jones:** designs and things like that. And it does have a bigger voltage range as well. It'll go from 4.5 to 40 volts. So, plus minus 20 volts supply, pretty impressive. So, you might be wondering why it's actually got a higher power

**Dave Jones:** consumption than the LM358 even though it's a a FET thing is because well, it's a FET on the input here, but as you can see, it's basically a bipolar design that just has a FET input front end like

**Dave Jones:** this. This is why it's still relatively high power consumption. But of course a big advantage that FET input op amps give you is you're talking pico amps now. You're talking typical plus minus one maximum plus minus 120, so it varies a a

**Dave Jones:** fair bit, but this is like three orders of magnitude. It's a thousand times less than the nano amps or tens of nano amps you'll get in a bipolar input design. So this is why you want to go for the end and the input offset current

**Dave Jones:** as well like you down in like like femto amps, right? 500 femto amps. Pretty low stuff. So that's the advantage of the FET design compared to the bipolar design, but apart from that like I prefer the 35 I don't like the 072s

**Dave Jones:** are nice FET input ones, but they're not my preferred jelly bean op amp just for general applications because the LM358 and next one we'll see as well is also the four channel version of the 358 is lower power consumption and it can do

**Dave Jones:** ground sensing as well. The input common mode range includes ground as I said great for current sensing single supply application something like that, whereas the uh TL07 series is not really designed for that. It won't sense to ground. It's

**Dave Jones:** output will go to the positive rail, but it's not a true rail to rail output device. And well, yeah, you'd want to have specific reasons for going to the TL074, but this is it's been around once again for like 40 plus years. It is a

**Dave Jones:** lot of people's go-to op amp especially if you need FET input. So what if you like the LM358, but you kind want that fit input niceness as well, as well as the ground sensing and single supply applications. Well, I've got the chip

**Dave Jones:** for you. The good thing about this one is that you don't have to remember the part number, it's the same. It's the 358 again, but it's the LMV. V stands for voltage because it's a lower voltage version of the part, but it is a CMOS

**Dave Jones:** version. It's not bipolar and it's rail-to-rail output operational amplifier as well, as the LM358 is not there. But apart from that, very similar specs, you know, offset typical offset voltage. It's got rail-to-rail output, as I said, 1 MHz

**Dave Jones:** gain bandwidth product, which is good enough for a lot of applications, relatively low noise. But the kicker is that because it's a CMOS version, the input bias current is only 10 pA. So, three orders of magnitude lower. We're

**Dave Jones:** looking at nano tens of nano amps before, now we're looking at tens of pico amps. So, if you're, you know, like a very high input impedance stuff, things like that, that's where you want to go. It's got lower current as well,

**Dave Jones:** 70 micro amps per channel, pretty good. Once again, unity gain stable, and some versions have the RFI and EMI filter as well. But good thing is it goes down lower voltage even. It goes down to 2.5 V guaranteed. It actually

**Dave Jones:** operates a little bit below that, which is good for like single lithium cell applications. Something like that, you might want to use this. I use one, and in fact, I use the LMV321 in my micro current, and I've done a

**Dave Jones:** video on that where, you can have a trap with using different brands of this sort of thing. Yeah, so I've actually done a video on that where I used a jelly bean part, but there were differences between manufacturers. So, I recommend going and

**Dave Jones:** have a look at that one cuz that's a real fascinating trap for young players in like using jelly bean parts like this. I thought they were all the same, but it turns out there was a slight difference in capacitive loading and

**Dave Jones:** with stability with capacitive loading where you can come a gaza. Hmm. And once again, it's available in a bunch of uh packages as well. Uh absolutely terrific and lots of application like countless applications for this. But uh one of the

**Dave Jones:** downsides is is uh maximum voltage is only 5.5 V. So, you know, great for like any sort of like battery-powered sort of like low-power uh supply something like that, you might want to look at the LMV version instead of just the regular LM

**Dave Jones:** version. But apart from that, it's pretty much an identical um op amp. And the good thing is it is available in a single version. You can get like a little SOIC-23 jobbie and stuff like that, all the regular um 358. So, the

**Dave Jones:** single one is three 321 or the 358 for the dual as we're used to. So, as you can see, it's a just a CMOS FET version of the LM358 and you get some advantages with that. Uh like you can go once

**Dave Jones:** again, you can go rail-to-rail output voltage. There's basically no drop in these output uh driver transistors here like you'll get with uh bipolar op amp. So, really good for battery power supplies and you where you have to go

**Dave Jones:** right to the rail. Winner. Now, of course, just like any op amp, you can actually use this with a split supply, but you are limited to that 5.5 V maximum. So, you can go plus minus 2.5 V or a little bit above that. Uh no

**Dave Jones:** problems whatsoever, but you can't go plus minus 5 V for example. It's not going to do it. You'll have to go back to the LM358 for that or choose another option. And once again, available in a whole bunch of different packages like

**Dave Jones:** this and uh single and dual. So, and in the we'll have a look at the sec a quad version as well. So, yeah, the LMV358, that's my recommendation for a CMOS jelly bean dual op amp or single. So, I

**Dave Jones:** hear you asking, "Dave, I really do need a jelly bean quad op amp. Okay, it's the LM324, absolute classic. In fact, it's probably more well known than the 358. The 324 is basically, think of it as a quad version of the LM358.

**Dave Jones:** And if you go to some manufacturers here, they will actually tell you. Where is it? Look, Rome, ground sense operating. Look, LM358, LM324. It's on the same data sheet because they're essentially the same part. It's just basically a quad version. Really nice.

**Dave Jones:** Same specs, 3 volts to 32 volts. Once again, that can work dual supply, plus minus 1 and 1/2 volts up. It's got 800 microamps typical there. Common mode includes range as well, so you can get your ground sensing and stuff like that.

**Dave Jones:** The offset voltage is pretty much the same as before. Input offset current, once again, you're in the nanoamps or tens of nanoamps range. You're not down in picoamps because this is a bipolar op amp, just like the LM358. But apart from

**Dave Jones:** that, it's pretty much identical. Go and check the specs for yourself, and you should know all these specs. You should learn them off by heart. And it's, you know, there's little subtle differences here and there, but basically, quad version

**Dave Jones:** of the LM358. That's why the LM324 gets my vote for the jelly bean quad op amp. And as we saw before, the LMV358 also includes the LMV324. You can get a quad version in the CMOS, exactly the same. See how

**Dave Jones:** easy this is? If you know the 358 and the 324, then you know they just add the V for the CMOS version. And these, like, four of these cover a whole ton of different applications. It's It's unbelievable. This is why they're still

**Dave Jones:** used 45 years later. And the LM324 is basically the industry standard quad op amp pinout here with the annoyingly the rails in this position, positive on this side over here, and negative over here. Always hated it, but that's the industry standard. It

**Dave Jones:** probably started with the LM324. And just for completeness, yes, you can actually get a single version of the LM324 and the LM32 58. It's called the LM321 here. Hasn't been around quite as long. I mean, this data sheet here, February

**Dave Jones:** 2001. I don't know if it was available before that actually, but um once again, it's exactly the same as the LM358 324 in a single package. But as I said, I virtually don't design in a single op amp. Like I have designed in the LMV

**Dave Jones:** 321 in like a tiny little uh, you know, SOT23 or something like that. You're looking at saving space and pin count. Yeah, you might do that, but I typically wouldn't. If I'm going for like an SLA or something like that or a DIP 8 um old

**Dave Jones:** school, then I'm pretty much going to put in the dual op amp instead of the LM321. But this is not really a recommendation cuz to me the LM321 is not really a jellybean op amp because if you just go over to Digi-Key here, okay,

**Dave Jones:** it's available from TI and On Semi, but look, zero stock. Zero stock. On on all of Digi-Key. Go to Mouser here. Okay, they've got 140,000 on order. Great, but on order on order on order. That's it. You can't get stock of this thing. So it

**Dave Jones:** doesn't meet the requirement for the jellybean. And it's more expensive than the 358. So what's the point? Look, the cheapest price on Digi-Key, 22 cents here. Okay, if you go to AliExpress or something, you might be able to, you

**Dave Jones:** know, you're going to be able to get it cheaper, but the 358 in stock. Look, 1.8 million in stock at 12 cents each. It's it's a complete no-brainer. This is why I would never really design in just the

**Dave Jones:** LM, just the generic LM321 over the LM358. You get that extra op amp for less price, more available, complete no-brainer. So I it's just I'm just including that for completeness. It's not really a jellybean part. All right, I'm not going to hear the end of it

**Dave Jones:** unless I mention the LM 741. For all the 741 fanboys out there, meh, it is one of your traditional jelly bean op-amps, but for me, it just There's very little reason to use the 741 these days. Just go for the LM358 or

**Dave Jones:** 321 even or, you know, 324. And the other thing is, well, yeah, you can sort of get some available in like old-school packages. And look at this old-school dip at 91 cents each. It's like Yeah, nah. There's a better option than this,

**Dave Jones:** and it's the basically the dual version of the 741, and it's the RC4558, also known as the MC4004558. And we can take a squiz at that. And here you go. This goes right back to March 1976 here. It's And it's the dual

**Dave Jones:** Basically, it tells you it's a dual version of the 741. So, really, there's no reason to use the 741 these days. I would just go for the dual version. And as you can see, like availability is better. And also, if we sort by price

**Dave Jones:** here, yeah, check it out. 183,000 available for like 10 cents. Why you'd use the 741? I've got no idea. So, yeah, sorry to all you 741 fanboys, but no, you'd use the 4558 is just going to be is just a better option all around. But

**Dave Jones:** once again, like this similar sort of specs, you know, it's fairly robust little beastie, you know, short circuit protection, all this sort of stuff. But it it's not It doesn't include ground sensing. It's not rail-to-rail. It's just Yeah, nah. So, it's nothing special, but

**Dave Jones:** it does have relatively low noise, which is why you'll often find the 4558 in lots of audio circuits, you know, preamps and things like that. It It's quite a common part out. Probably, you know, the common jelly bean audio

**Dave Jones:** op-amp, I guess. But you don't get any niceties like ground sensing or uh or anything like that. So, it's just like your old-school bipolar op-amp. Having said that, I will not survive the comment section unless I mention the

**Dave Jones:** NE5532. Uh you could say this is the de facto standard audio op-amp, I guess. I won't go into the reasons why, but you know, low noise, grunty little thing. It's good decent THD performance and everything else. So, you'll find this in a ton of

**Dave Jones:** uh audio designs. And once again, it's like 1979. It goes way, way back. And there's a whole bunch of audio files out there who will not touch an audio design unless it has double 532 uh chips in it. And you'll actually see

**Dave Jones:** these often advertised in the uh product design that it uses this chip. But it's not the best performance chip out there, but I guess it's the jelly bean of you know, decent performance audio op-amps. So, yeah, you will see

**Dave Jones:** this one out there a lot. So, it's well worth uh familiarizing yourself with it. Making yourself familiar with it. So, although the definition of jelly bean components kind of implies meh specs, I kind of feel obligated to include the jelly bean precision op-amp,

**Dave Jones:** which is the OP07. And this one is going back, of course, 1983. Fantastic. So, as the precision name implies here, it basically means it's got low offset voltage. It's it's precise, doesn't need any like external trimming or anything like that. So, you

**Dave Jones:** know, I kind of have like the old-school uh talking points like uh comparing it to like chopper amplifiers and stuff like that because back in the day, to get low offset voltage, you have to use a chopper amplifier. But when uh you know,

**Dave Jones:** the op-amp OP07 came along, it was sort of no, you didn't have to do that. It was kind of like it was just low offset voltage built in. And uh it's got, you know, a decent uh voltage range as well,

**Dave Jones:** plus minus 18 V here. Can work down to plus minus 3. And once again, this is available in different grades from different manufacturers and stuff like that. But if we look at like the Oppo 7, see here input offset voltage typically

**Dave Jones:** like in the order of you know sub 100 micro volts here like 60 odd micro volts something like that. So if you want to step up from like the LM358 or a 324 or something like that because of the

**Dave Jones:** offset voltage, then this is the one that you would design in would be the Oppo 7. And because it is a bipolar jobby, it's actually nano amps input current. It's not pico amp. So yeah, sorry for all you pico amp fanboys, but

**Dave Jones:** unfortunately one of the major downsides is that it's not ground sensing or rail-to-rail op-amp. So think of it as like a precision LM741 or double 4558 for example. You can also get dual versions of this and quad as

**Dave Jones:** well available in different part numbers. You can go look at those over your own accord. And one of the things is because it's like a 741, it does actually have offset pins so you can have offset capability. So

**Dave Jones:** you can get a trimmer in there and trim it to even better specs. But if you're after a precision op-amp these days, if you're designing in like you know fairly tight specs, then you know there's lots of other alternatives to the Oppo 7, but

**Dave Jones:** it is a generic part available for lots of different manufacturers at a reasonable cost. So it's certain and it's been around for like 30 40 years. So it's certainly gets the jelly bean tick of approval. So there you have it. That's my list of

**Dave Jones:** kind of like the top five, I guess, jelly bean op-amps. You know, the LM324, LM358, the TL070 series, the LMV series, and the old school 40058 for kind of like audio or general purpose bipolar stuff. And the Oppo 7 for the precision as a

**Dave Jones:** bonus. There's a kind of like top five jelly bean op-amps. So as always, leave it in the comments down below if you think I've missed something cuz I'm sure everyone will have their favorite. What is your favorite? What is

**Dave Jones:** your most used? What is your go-to jelly bean component? Please leave it in the comments. I want to know. And beginners out there, these chips you're kind of like expected to know these, not like every in-depth specification. Like you

**Dave Jones:** don't have to memorize absolutely everything in here, but you should know the basic order of magnitude of the offset voltages of these and like features like do they have ground current sensing output rail-to-rail capability and stuff like that. And you

**Dave Jones:** should be able to just recognize and use these parts right off the bat. You should have them in stock. You should have them in your CAD library so you can just drop them into your designs. And you should just be able to at a job

**Dave Jones:** interview or something, somebody ask you, oh, you know, give us a name us an op-amp, right? You'll be able to tell them, oh, yeah, I use the LM358 because it's a dual jobby and it's nice, it has ground sensing, and it's just, you know,

**Dave Jones:** across different manufacturers, it's cheap, really available, it's been available for like 40 years. It's, you know, Bobby Dazzler. So, anyway, I hope you enjoyed that. If you did, please give it a big thumbs up. And certainly let me

**Dave Jones:** know in the comments down below and by the thumbs up. If I get a lot of thumbs up and views on this, I'll do more cuz like I haven't even touched on, you know, comparators and all sorts of other

**Dave Jones:** analog devices, let alone digital ones. I'll do a like a little mini series of jelly bean components that you should know. So, anyway, I hope you found that useful. And as always, you can discuss either in the comments down below or

**Dave Jones:** over on the EEVblog forum where I have a thread for each and every one of these videos. In fact, I did want this video to like cover more things, but I started yapping on about op-amps, so it's just

**Dave Jones:** dedicated to op-amps. But anyway, and also check out my Odyssey channel. I've got more than 60,000 subscribers over on Odyssey as well if you're sick of the YouTube-y ads. Anyway, I you enjoyed it. Catch you next time.
