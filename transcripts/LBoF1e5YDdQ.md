---
video_id: LBoF1e5YDdQ
title: EEVblog #1164 - Xbox Engineering Baptism Of Fire
url: https://www.youtube.com/watch?v=LBoF1e5YDdQ
source: youtube-asr
---

**Dave Jones:** Hi, with the recent Weller video, I thought this one would be quite appropriate to have a look at and it's a retro one. Take your mind back to 2005 when the original Xbox console reigned supreme. Hands up if you still got one

**Dave Jones:** and you're still using it. Anyway, there was a problem with the Xbox console. Unfortunately, about one in every 10,000, give or take, would release the magic smoke. So, it was a big deal at the time. Millions of boxes involved,

**Dave Jones:** apparently only like 30 of them caught fire or smoked or melted down, it did whatever. Microsoft actually seemed to do quite well at identifying these problems and owning up to them and fixing them, but in this particular case, they didn't recall the actual

**Dave Jones:** boxes and they didn't really specifically say what the issue was that was causing the problem with these things. All they did was saying, "Oh, we're going to for voluntary recall of the power cord for this thing." So, what

**Dave Jones:** they did is they shipped out millions of these things, these replacement power cords to Xbox owners. You could go onto the website and you could request a new power cord and I did this at the time and sure enough, they shipped me one of

**Dave Jones:** these power cords. So, the reason I'm doing this video is because I'm still cleaning up the old lab and I came across this original replacement Xbox power cord, in quote marks. It's actually an electronic fuse, by the looks of it. And I thought it'd be

**Dave Jones:** interesting to take a look at this issue and do a teardown, which was designed to cut the power when your power supply developed or whatever the problem was inside the unit actually developed a fault and rather than burn

**Dave Jones:** down, it's like a fuse that Weller add to most of their products. But let's not go there again. Now, here's the original power cord, again in quote marks, that Microsoft voluntarily replaced. There wasn't any like like official like government like

**Dave Jones:** safety recall order or anything like that, but they voluntarily replaced the power cords on 14.1 million Xboxes. And I don't know if that's if that's how many they shipped, but that was the potential impact of this thing. So,

**Dave Jones:** why did they replace a normal power cord like this with this electronic fuse that has a reset button and test mode? You you press test on it and it flashes a few times and then the electromechanical cutout, you can see

**Dave Jones:** that there's a green like mechanical indicator in there, which will then switch off. So, why would you replace a normal cord with an electronic fuse like this? Well, the only reason is that it wasn't a faulty power cord. Now,

**Dave Jones:** Microsoft were very cagey about their actual wording for this thing saying, "Oh, we're replacing the power cord." and things like that. I think they kind of sort of admitted that there was an issue with the console. But, anyway,

**Dave Jones:** they decided, I guess the console didn't have adequate or or any fuse in it. So, we'll do a teardown of an actual Xbox console shortly, so stick around for that to have a look. But, they decided that rather than recall the consoles, which

**Dave Jones:** could have been one way to fix this problem, that would have been expensive. I mean, if you recall 14.1 million Xbox consoles, like it's it's cheaper just to design and manufacture this and just ship it out to people and problem

**Dave Jones:** fixed. And, you know, yes, there's nothing inherently wrong with that. You've got to weigh up the cost of doing this. I mean, just imagine if the bomb cost and the shipping cost of this thing is $10 for example, well,

**Dave Jones:** that's 140 million bucks right there. But, it would have been much more expensive to actually and much more damaging to the brand, etc. And the Xbox reputation, all that sort of stuff, actually recall units. Cuz apparently, this all came about because only like 30

**Dave Jones:** or 40 units actually caught on fire or smoked or melted down, something like that. Microsoft actually came out and said that you had a 1 in 10,000 chance of it happening. But, the actual number of units that that the fault did

**Dave Jones:** actually appear in was actually much, much smaller than that. So, anyway, if anyone has any details on the, you know, the background for all this, like actually inside information or something like that, please do leave it in the

**Dave Jones:** comments or over on the UV blog forum. Anyway, let's tear down this thing. Nominal 610 milliamps. Not sure how accurate that is, but it's made in China. It's got the C tick mark. It's all happening. Anyway, catalog number

**Dave Jones:** Q01. So, let's tear it down. So, obviously, it's designed to trip at 610 milliamps or thereabouts. Thankfully, it's got some screws. Let's get into it. Now, unfortunately, you can see the pain in the ass screw down there. It's one of

**Dave Jones:** those pentalobe type things with the security pin in the middle. And it's actually a large one. So, I've only got like the smaller ones for like the newfangled iPhone whatnots. And Well, I drilled out the screws and check

**Dave Jones:** this out. It is phenomenally complicated for an electronic fuse, which is basically all it is. Unbelievable. Look at all the control circuitry on here. I'm just absolutely stunned. We've got two eight-pin jobbies on here. They're probably little micros. Might

**Dave Jones:** have a closer look at those in a minute. So, that's your test switch. That's your reset switch, and you can see that that physically pushes that green indicator that mechanical green indicator. Why you'd go to all that effort for this mechanical green

**Dave Jones:** indicator and have all this molded plastic stuff? It's absolutely remarkable. Got a massive mold there by the looks of it. You can just picture the design meeting for this and the poor scared little engineers in there and and

**Dave Jones:** they're going, "Don't screw this up, otherwise Bill Bill himself's going to come here and personally kick your ass." This is like hilarious. Um yeah, they've just gone to so much effort and even like all these dedicated plastic mounts to mount the board on and

**Dave Jones:** everything else. It's just insane. I mean, you know, they could have just put a fuse in a lead if they really wanted to. Look at this, taking off that plastic cover. Look, they're breaking both the active and the neutral

**Dave Jones:** there. Like unbelievable. The amount of complexity they've gone into doing all that. Little solenoid in there. And it looks like they got a low voltage transformer here for powering various stuff. They would have got that right, I'm sure, with all the requisite

**Dave Jones:** approvals. They would have been very careful with everything in this thing cuz they didn't want to screw it up. Anyway, let's have a look at how they're actually doing the current tripping here. Now, it looks like they've got two current

**Dave Jones:** transformers here. This one here, some windings down there inside that potting down in there, and they come out these brown wires down to this chip down here. We'll have a look at that in a minute. And then they've got this other one. You

**Dave Jones:** can see the windings more clearly in that one. That one's not actually potted in place. That one looks like it has much finer and much higher number of turns in there, and that's just like a regular PCB mount current transformer

**Dave Jones:** there. Got a diode bridge rectifier, we'll look at that for the transformer in a minute, but look at how the mains current goes here. Why do they need two if they're just doing simple current sensing? Now, this first current

**Dave Jones:** transformer here has both the primary, the brown wire, and the black wire running through it. That does not make sense for measuring the current of the product under test because the if the current's flowing this way through the active brown wire

**Dave Jones:** and then back at this way through the black neutral wire, then they cancel each other out and you can't measure anything. So, but this is a classic configuration for a earth leakage circuit breaker or a current balance transformer. So, if there's any

**Dave Jones:** imbalance between current between the primary and the secondary here, then it will generate a magnetic field which can be sensed on the coil and then it trips at a certain current. So, that's how an earth leakage circuit breaker works.

**Dave Jones:** Now, we've got this extra winding which we'll have a look at in a minute, but obviously they're doing some earth leakage circuit breaker functionality. So, rather than just the 610, obviously they wouldn't be doing 610 milliamps in terms of earth

**Dave Jones:** leakage current there. That's way like above like the standard is like 20 milliamps or 30 milliamps. So, obviously that's the primary current that they're tripping the electronic fuse at 610 milliamps. So, they don't mention anything about earth leakage breaker

**Dave Jones:** inside here, but they're obviously taking no chances. So, this thing has dual functionality. Now, if you have a look at the second transformer, it now makes sense. The black wire, the neutral, avoids going through that and they've only got the active passing

**Dave Jones:** through it. So, obviously this current transformer is measuring the product consumption current from the active goes out to your Xbox and then if current comes back and then avoids that. So, we're measuring the current taken by the Xbox. So, that one is doing your

**Dave Jones:** current sensing and the circuitry on the back it looks like and that's going to bugger off to your control board here as a track on top. I don't know if you can see that, but there's a track that goes

**Dave Jones:** from the pin of that current transformer over to that board. So, there you go. It's got dual functionality. Wow, didn't expect that. So, what's going on with this white wire here that's all wrapped around and buggers off down here? Well,

**Dave Jones:** obviously this is the test functionality. So, that because it's going through the primary current measurement transformer here, they're obviously going to put a load on this thing and then test out both the product current, the electronic fuse trip current, and also the

**Dave Jones:** earth leakage circuit breaker as well cuz you can see there's a couple of turns wrapped around there like that and then it buggers off down to here and down to this relay down here, which is a nice Omron jobby.

**Dave Jones:** Spared no expense. Really spectacular. Spared no expense. And then it goes through these three 1206 resistors. That's to get the voltage requirement. So, three of those in series and here are the two contacts on the coil and then the contacts just

**Dave Jones:** go off to to the neutral pin down the bottom and of course the top side of that is connected to the active after this transformer here. So, they're obviously just putting those three resistors directly across active and neutral with that relay and that's

**Dave Jones:** designed to test both the earth leakage circuit breaker via these couple of loops here, which give you more current by the way. So, it like magnifies the current going through there and also by putting a small amount of increased current into the

**Dave Jones:** main current measurement transformer, but how small? Well, we're only talking these are three 18K resistors in series. So, we're only talking like four odd milliamps or something. So, obviously they're not testing at the full load cuz if you want to test at the full load,

**Dave Jones:** you'd need a massive power resistor, especially like for the 610 milliamps. A massive power resistor or a varistor or something like that. Now, I know there's a lot of stuff on there, but you know, surely you would have as a

**Dave Jones:** first pass, you would have tried to integrate that onto the main board down there. Maybe, you know, I know they've got to keep the size down, but jeez, you'd think they could have some I mean, it's double-sided populated

**Dave Jones:** anyway, although it's only through-hole on the top, I guess, but still it's almost maybe like, you know, two separate design teams, you know, one worked on this this test controller, the other one worked on the rest of it or something

**Dave Jones:** and then they had to integrate them together, but it's it's just seriously com- complex. Unbelievable. Son of a medium microchip. What does that mean? I I Is that like an in joke? There's our lead and the microchip fanboys go wild.

**Dave Jones:** That's a 12F675. They had some sort of marker pen on top of that, obviously, to show that it's been programmed and then elsewhere, we just have a LM358 op amp. So, little eight-pin micro jobby just controlling that test functionality. Oh, that's SO8.

**Dave Jones:** That makes sense. It's not SOP, but maybe that's what they refer to it internally as, I'm sure. Now, if I was designing this and wanted it to be reliable, I wouldn't be doing the detection of that 610 milliamps in

**Dave Jones:** software in the micro. I wouldn't be relying on that micro to then, like the ADC, measure it, continually measure it, and then trip it. Not only is it Well, it's going to be slower. Still going to be fast enough, of course, for the

**Dave Jones:** application, but then you add an extra layer of unreliability in there as as reliable as these are, every extra process you add in there. So, I'm wondering, is there any like analog functionality and all of this other the micro and everything else

**Dave Jones:** is just doing the test functionality, perhaps. So, the active stuff might be done analog-wise. Cuz we certainly do have lots of discrete transistors on here and stuff. And of course, we've got the op-amps and things like that. So, it

**Dave Jones:** could certainly the thresholds could certainly be done in hardware, but then what do you do for different regions? You're going to need different test currents. So, if you did it analog-wise, you would have to change some of the

**Dave Jones:** values of the resistors. And you can see the microcontroller has the test pads up here. So, obviously, this is programmed in circuit, and it wouldn't surprise me if that had different programming for different regions for the different required test currents. All right, let's

**Dave Jones:** just run this. I'll push the test switch. Test it. Use my poker here. Woo! Talking about belt and braces engineering, a ZNR series MOV in here, big-ass transorb. And if if that's not enough, coupled thermally to a thermal fuse, 105° C

**Dave Jones:** thermal fuse. At what point in like the engineering cycle do you go, "Well, you know, yeah, we've They've a MOV in there, but we want to have a thermal fuse in series with that just in case the MOV heats up and gets too hot. What

**Dave Jones:** like my kingdom to be a fly on the wall at the safety review meeting for this thing. Because well, you know, look, hundreds of millions of dollars are on the line for this thing. You've got to remember that. And, you know, the brand

**Dave Jones:** the Xbox brand that's worth billions and billions of dollars is all on the line. And if they don't get it right, you know, So, the pressure on the engineers to over-engineer the out of this would have been, yeah, pretty intense. And

**Dave Jones:** that's what they've done. I mean, this is just massively over-engineered. So, there's a fuse in series with the MOV and they've like run a wire over a jumper link directly over here. I It's not an after thought, really, but

**Dave Jones:** you know, why they couldn't have snaked the traces on there clearance-wise, they could have just slotted that out, I guess, but anyway, um yeah, directly across the mains input before any of the uh switching happens in here. So,

**Dave Jones:** obviously our test button that uh goes in the back here pushes up these armatures that latches in place and then they activate this uh solenoid to actually um switch it, you know, to deactivate or or trip the thing,

**Dave Jones:** basically. So, that solenoid is connected under here. You'll notice that's going over there. It's going over to looks like there's a little solid state relay jobby. No, that's actually just a bridge rectifier down in there. Here's the neutral over here going into the

**Dave Jones:** solenoid here. Then the solenoid goes into the uh AC side of the bridge rectifier and then the bridge rectifier comes out here. It's your DC out. So, they've got a little transistor in there. And so, they're What? CRO3AM.

**Dave Jones:** No, it turns out that's a thyristor. So, they're using that to switch the solenoid. That's rather interesting, isn't it? And they've just got a varistor in series with that to protect it. But yeah, um thyristor control of the solenoid. Huh.

**Dave Jones:** And what do you know? That's a dedicated uh earth leakage breaker chip. But you'll notice that the coil goes through the bridge rectifier between active and neutral there, and the thyristor is on the other side of that bridge

**Dave Jones:** rectifier there. So, it's got It's not actually switching the coil like directly across that. That's not how it works. If you look at the uh typical application circuit for our earth leakage circuit breaker chip here, we've got our bridge rectifier, okay? Here's

**Dave Jones:** our contacts over here. Here's our solenoid to drive it. So, there's our thyristor there as part of this latch circuit here, and that solenoid, of course, drives the contacts. But that's that's not what we see here. Look, this

**Dave Jones:** is neutral. Goes through the bridge rectifier, through the coil to active. It's just permanently enabled. That solenoid is permanently enabled across that mains. How else does it get driven? It's bizarre. So, I've traced this out here, and this middle pin is

**Dave Jones:** the anode of the thyristor. We're talking about this point up here. Instead of it going to the solenoid, which makes perfect sense, it doesn't. Goes through these four resistors here in series going over to pin eight of the

**Dave Jones:** chip, the power pin. So, those four resistors are obviously the 50k there. So, of Of we're getting our, you know, our 240 volts AC rectified across this full wave bridge rectifier here. So, we're getting our 240 volts on there.

**Dave Jones:** That's why we need those four resistors in series, high voltage, doing a direct mains powering of this chip here. And it's got a built-in regulator. It's designed to do this. So, no problems whatsoever. But, where's the solenoid? Where's Wally?

**Dave Jones:** It's directly across active and neutral permanently. I swear. I must be going nuts. And I have confirmed that that is correct. The gate goes over to pin seven here as part of the latch circuit. I've confirmed that. And the other the cathode, of course,

**Dave Jones:** goes down to ground. So, it's exactly the same. But, instead of that coil there, this just connects directly to that. There is no coil. It shorts out the output of the bridge rectifier. So, instead of having our solenoid here,

**Dave Jones:** that it's installed directly in series with the AC side of the bridge rectifier there. That's it. There doesn't seem to be any other way to activate that solenoid. I'm going nuts. I think I'll go start a Jim's Mowing

**Dave Jones:** franchise. Okay, so the only way this thing can work, look what happens. The solenoid, okay, is normally off like this because, like, you've got 240 volts on here. So, comes through here. There's no way that it can go anywhere else,

**Dave Jones:** right? Because it's just it's just going through and powering the circuit here. So, if the thyristor shorts out this point here and this point here, bingo, we've got a short across there. Bingo, you suddenly have a path for the current

**Dave Jones:** to flow through that diode, through here, through there, and back like that, activating the solenoid and disconnecting the circuit. So, it's like they're doing it completely opposite to what the um application circuit for this chip says. But, that certainly explains why

**Dave Jones:** they've got that varistor in there. Aha, cuz it like it you know, you don't want the full mains across that. You want a varistor in series to then go high resistance as it heats up, but you only need the solenoid to activate for you

**Dave Jones:** know, a split second and then bingo, cuts off the power. So, you could say actually that's rather clever variation on this classic application circuit, which no doubt the designers would have seen. They would have had the data sheet

**Dave Jones:** just like I've got for this chip, which has this application note on the very first page and they looks like they're doing it almost identically, except for the fact that they haven't bothered to put the solenoid here. They've actually

**Dave Jones:** put it in series with the bridge rectifier and then once it trips, shorts out the bridge rectifier, cuts its own power off. Cuz once you spread rectifier sorry, shorts out across here of course, then then there's no more power on the

**Dave Jones:** rail up here and the switch chips switches off the thyristors off, everything's off. So, it just goes bam, but why they decide to do that over the standard implementation with the solenoid coil here? I don't know. I'll let you guys fight it out in the

**Dave Jones:** comments. Go for it. As for the solenoid activation, let's push this lever all the way with the lever right down to the bottom. Push that in like that and that that holds it in place until the solenoid releases and the whole

**Dave Jones:** thing flips up. And what is this transformer doing? Well, it's just a little low power transformer just to power the electronics. It's connected directly across the mains there. Just goes over to the other side here and then that

**Dave Jones:** just powers the uh board. So, this is the AC mains input here. Goes into the AC side of the full wave bridge rectifier there. The other side of that bugger's off to one pin of the module, and the other ones over here

**Dave Jones:** go through here over to here. So, this can find its way back certainly find its way back into um the main earth leakage circuit breaker tree. So, obviously, you know, you've got to have two paths. One's got to come from

**Dave Jones:** the uh test board uh logic control has to be able to trip it. So, it's obviously has that extra path through there to do that. So, let's just have a quick look inside the Xbox, shall we? Got to get all this cage stuff out

**Dave Jones:** before we can access the mains down here cuz there's going to be something to do with the mains input. And take out the hard drive, we're into the power supply, a totally separate board, of course, as you'd expect. Very nice construction

**Dave Jones:** inside the Xbox, by the way. Very well designed. Nice uh use of the envelope. Avid thermal alloy. Oh, for all you avid fanboys, there you go. Um they've got those in the right direction for the fan here. If you had them in the other

**Dave Jones:** direction, they wouldn't work. You wouldn't get the air flow across them. It's made by Foxlink Technologies. Made in China. It uh looks pretty good. Single-sided uh board, of course, as you'd uh expect in all of these uh ones,

**Dave Jones:** but uh that looks uh nicely laid out, nicely designed. It's got a Teapo main cap there. Geez, haven't seen Teapo for What happened to Teapo? Still around? Probably. Anyway, common mode choke there. There's your full wave bridge rectifier. There's your

**Dave Jones:** uh suppression cap. No worries whatsoever. On the backside here, we've got our mains input directly across here. The clearance is uh just fine. Everything's hunky-dory there. No problems whatsoever. They've got decent amount of clearance between there. I I

**Dave Jones:** can't fault that at all. Looks look like a 240 switch mode supply. So, I got got no issues with that, but let's look at the protection. There's our protection, 2.5 amps. It It'd be different for the 110. Looks like they

**Dave Jones:** got a MOV in there. Don't know They got a resistor across that to bleed any residual when you pull the cord out. So, that's nice. Everything's hunky-dory. There has been speculation that there was bad soldering joints on these, and that's what would heat up and

**Dave Jones:** start, you know, it catch the fire and everything else. But, of course, those joints look fine. And of course, you'd expect them to be fine. My just the one random unit that I opened that dates from 2002, by the way. Then, uh if the random

**Dave Jones:** sample was out, then you'd expect a much higher failure rate than the expected one in 10,000 Microsoft claim, or even, you know, what is it? .002% actual field failure rate. So, of course, you know, the odds of us

**Dave Jones:** actually seeing anything in here was zip. Yeah, the only real issue there is the strain relief is just these two little plastic clips like that. Um there is no other way to hold that except for the two solder joints and these little

**Dave Jones:** plastic clips. So, every time some kid comes along and goes wham, look at that. You can see the plastic in there wiggle like that. The rest of that strain and stress is going to be taken on those solder

**Dave Jones:** joints. Well, there's your problem. But, there could be two issues here. You know, they do mention maybe some sort of component failure, but the component could include the PCB, the soldering, the assembly, whatnot. A 2.5 amp fuse on

**Dave Jones:** 240 volts, that's 600 watts. Yeah, I think that was just a badly spec'd fuse, which would have been like it's okay for like gross overloads and gross shorts and stuff like that. Needs to be over 2.5 amps for a significant amount of

**Dave Jones:** time for it to blow. It just doesn't magically blow it instantly at 2.5 amps. That's not how fuses work. They're a you know, a There's a thermal delay mechanism plus some tolerance added in there. So So with hindsight in that

**Dave Jones:** there might have been some sort of a solder joint failure in here that was drawing power causing these to heat up and even in the odd case catch fire, that 2.5 amps wasn't spec'd well enough to do that. But of course, as I said,

**Dave Jones:** recalling all of these all the Xbox units to replace that fuse, meh, nah. It was much cheaper to simply supply an external one. So Microsoft just went, "Ah, bugger it. Look, after extensive testing, I'm sure they would have

**Dave Jones:** determined that 610 milliamps was the optimal trip point for the you know, the 230 240 volt market unit. They determined will protect these Xboxes and stop them melting down if that particular fault, whatever it is, which they probably keep in very close to

**Dave Jones:** their chest, happen." Like it's been like 13 years at least now. Has the Has the truth come out? I don't know if it has, please leave it in the comments. Well, not only do we need a fuse in

**Dave Jones:** there, let's make it electronic. And hey, while we're at it, let's let's add some earth leakage circuit breaker as well. Just built and braces approach. Anyway, they came up with this no doubt very expensive and massively over-engineered response

**Dave Jones:** to this particular fault, which is very fascinating. It you know, might be a classic example of you know, there's a lot on the line. As I said, billions of dollars on the line and the engineers have to get it right. So they decided,

**Dave Jones:** "Well, built and braces, we're we're taking no chances. We're going to over-engineer the crap out of this." And they did and when I thought I'll do a quick tear out of this. Sorry, it's been like half an hour or something now. Dry

**Dave Jones:** joint, cracked joint on a on the ACN which is pretty important. Uh the buzzing noise we're hearing was uh probably the arcing of that to the actual board.

**Dave Jones:** That was fascinating. It's so if you like the video, please give it a big thumbs up and as always you can discuss down below if anyone actually worked on this for Microsoft at the time and now you can uh talk about it, then please

**Dave Jones:** let us know. But I hope you enjoyed that fascinating look at some retro safety engineering to avoid a product recall. It still cost them hundreds of millions of dollars though. Cost them a couple of hundred million bucks and that's not counting

**Dave Jones:** reputation, everything else. happens. Catch you next time.
