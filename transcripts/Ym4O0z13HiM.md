---
video_id: Ym4O0z13HiM
title: EEVblog #361 - LED Ceiling Panel Lighting 101
url: https://www.youtube.com/watch?v=Ym4O0z13HiM
source: youtube-asr
---

**Dave Jones:** Okay. And I'm here with everyone knows Doug Ford of Doug Ford analog design and he's got some cool light panels for us cuz he's into everything lighting. Including everything analog plus LED lighting and stuff. And you're the acoustic and audio guru.

**Dave Jones:** Something a bit like that. Awesome. So yeah look we've got some panels. These are four they're 1200 mm by 300 mm. Nominal power 60 watts input nominal output about 3000 lumens. So nominal efficacy around about 50 lumen per watt.

**Dave Jones:** 50 lumen per watt. And unfortunately that's around about what you can expect from these diffused flat panel emitters. Yep. The LEDs inside them are probably 120 lumen per watt. But by the time you go through the side process and diffusion

**Dave Jones:** relatively low efficacy but very good quality of light with low glare. Excellent. That's exactly what I want. The idea is put these on the wall in front of me to light up my face in front of the video cuz the corner of the lab

**Dave Jones:** is actually quite dark. So that's the idea. So these are LED strip of Yeah strips of LEDs. LEDs down the side. Yeah. Right. So they'll be a flat PCB down the side of that. Yes. And we've got four inputs.

**Dave Jones:** They've basically segregated the the power to these into four groups. Probably because they have four 600 mm PCBs. Okay. And there's none on the top and the bottom. It's just on the side. Yeah and we can find that out quite

**Dave Jones:** readily by powering up one of the four groups. Let's do it. We haven't powered this thing up yet. So Yeah we have here a a 3 amp power supply. Yep. We have a controller which is actually an RF

**Dave Jones:** controller for dimming. And it comes with a little wanky remote control. Ta-da! So, you can dim them from a distance. So, we'll put batteries in that later and find out how well it dims. Okay, let's run up. Let's do it. Hey, here we go. We're up.

**Dave Jones:** Okay. Now, depending on how well the video camera shows this may not I've got auto contrast auto exposure. Yeah. So, yep, we can see that. Let's see what's split in the middle there. Yes. Now, you can tell that it despite the fact

**Dave Jones:** that we've only got one half of it illuminated, it's uh diffusion is really very good. is very good. It's pretty you know, well, we could get the light meter out and see what the difference is here as it and as it drops going across, I

**Dave Jones:** guess. So, we could almost get the function of the Yes. plastic. If they've got it right, we'll be going from 100% to 50% to 25% over the span there. And it's linear? It should actually it should it should

**Dave Jones:** be linear per unit length, which actually makes it logarithmic when you plot it. Right, got it. So, we're up. And Okay, that's the second half. Yep. Now, let's run. Let's see if we can pick this half to illuminate. Let's see if we

**Dave Jones:** can get it right. Nope. Okay, uh let's try that one. Hey! There we go. And that is really very even. I like that. That's impressive. get the next two up And that's not hard on the eyes at all.

**Dave Jones:** No. When you have a large emitting surface like that Yep. 3,000 lm coming out of a large surface like that represents really quite low glare. When you have 3,000 lm coming out of a tiny little point source such as

**Dave Jones:** you can from some of the higher powered LEDs these days, it's a horrible amount of glare. There we go. I've ramped it up a bit. This Yeah, it's not easy to capture such a bright source on a camera with

**Dave Jones:** background at the same time. You do look beautiful. You look wonderful. Oh. Your hair's been messy though. It's got that you know, wind crazy proof. Wind swept and interesting. Wind swept and interesting. All right. So, that looks That looks really quite

**Dave Jones:** nice. Do they flicker down at the low end, do they? That's what I've seen on the tests I did. Yep. But, we'll re-verify it. Excellent. Any flicker will simply be due to the PWM frequency getting too low and

**Dave Jones:** starting to get into the visual range of 60 hertz, 50 hertz, 40 hertz. Yep. And it might show up on camera depending on the frequency as well. We might not see it, but it might show up. Yeah. Exactly.

**Dave Jones:** We'll try that. Cuz I'm shooting this at 25 frames per second. Well, I get Well, that's 50. Let's see if we can get some beat frequencies happening. Interesting. So, there we Let's switch them off and have a close look at the

**Dave Jones:** back of them. Yep. Uh which actually won't reveal all that much. No. Okay. But, we might also pull out the chalkboard and sketch up the principle of operation of panels like these. Is there a brand? Uh yes, these come from QL LED.

**Dave Jones:** QL LED in Shenzhen. in Shenzhen. Yep. And there's the four There's the four cables running out. Just a standard DC 2.5 mm 5 5.5 mm Yep, DC barrel. Also comes with fastening hardware that goes in there so that you can link them

**Dave Jones:** all to the roof. no, we can't see the I thought we could see the board. Okay, no, they're the side attachment points. That's right. Right. Okay. Got it. And how much do these things cost? Uh well, uh they're at a price which will allow me

**Dave Jones:** to sell them locally for just below $200. Awesome. At at this size anyway. Right. Have you Have you Have you tried any other one hung low ones from Not in flat panel emitters. I've got an unfortunate amount of experience now

**Dave Jones:** with LED fluoro tube replacements. Mhm. Which we're going to look at as well. We've got a whole bunch of stuff here, folks. We've got LED fluoro replacement tubes, and we've got these massive long ones. Which are locally manufactured.

**Dave Jones:** Locally manufactured by Me. Doug Ford and Long Design. Peter's over here, too. Hey. Okay. Chalkboard time. Chalkboard time. Chalk? So antiquated. We've We've We We have evolved somewhat. I haven't. I'm a Luddite. Fair call. All right, Dougie. We're going to

**Dave Jones:** explain some of these lights, are we? Yeah. So, for those of you who aren't familiar with how flat panel light LED lights work, you start off with a PCB loaded with bucket loads of little LEDs. Typically 50/50 package or 35/35 or thereabouts.

**Dave Jones:** Okay. You then have a large slab of thick acrylic. It might be 10 mm 8 mm thick or thereabouts. Just standard acrylic? Standard diffused acrylic? Uh no, actually clear acrylic. The clearer it is, the better. Because what you're relying on is light Hang on.

**Dave Jones:** Chuck us a another color. Got plenty of colors. Light from the LED entering here as long as that angle is less than the critical angle, it'll undergo total internal reflection and total internal reflection, and it'll actually act rather like a a

**Dave Jones:** fiber optic. Does that mean you need a narrow angle LED lens LED? I will come to that because that is one of the areas of loss. If your angle of entry is too steep, you get external reflection. Yep.

**Dave Jones:** So the light doesn't enter in the first place. If the angle is shallow enough to enter, it might still simply reflect straight out there without traveling. You'll also undergo some degree of diffusion in here, which is why some of this light will

**Dave Jones:** tend to reflect a bit like that simply due to surface irregularities. So you will get some emission here. You'll be reinforcing all of that with on the back side of it a layer of white reflective paper. Is silver mirror better?

**Dave Jones:** Um yes, but you want to avoid specular reflections. You actually want diffuse reflections, which is why you use white rather than silvered. Right. Even though that's greater loss. Uh no, because you can get you can get white surfaces which have got about

**Dave Jones:** 99.5, 99.9% reflectivity. Ooh. It's just that when you do get a ray bouncing off them, instead of it reflecting, it will diffuse. Got it. And does that have to be totally flush with the surface? No, there can be an air space. That side

**Dave Jones:** of it's not too critical. The other thing that you want on this face here is either a diffusion layer or sometimes that diffusion layer is actually etched into that surface of the Perspex. So that's the key a a thin diffusion

**Dave Jones:** layer instead of diffused plastic. Yes. Aha. So you want highly conductive uh highly optically transparent acrylic so that you can get your light over to near the center Mhm. without too much loss. But, you still want it to

**Dave Jones:** diffuse so that you're not seeing the immediate glare from emitted from around here. Yep. And that's pretty much it. So, your losses are uh this entry angle. Mhm. Now, incidentally, I understand that uh 3M have and probably others have a film

**Dave Jones:** which you can place here to say, is there some magic gunk you can There is some magic gunk. Haven't tried it. Haven't tested it. Don't totally know its properties, but is reputed to uh basically get more of the light from

**Dave Jones:** the LED utilized within the acrylic. Aha. Uh the other magic gunk is the high reflectivity film here. There's a few manufacturers of that around the place and more every day. And there are a number of plastics manufacturers. Uh I think the Bayer one

**Dave Jones:** of them who are getting into this material with the right characteristics on the front face for good diffusion. Got it. But, bottom line is it's lossy. It's lossy as hell. Uh even with the best will in the world,

**Dave Jones:** the uh transparency of the acrylic is finite. But, that's what you If you want a thin diffused light panel, this is pretty much the only way to do it. Uh I mean, ultimately, would it be better to have your LED here and shine out if

**Dave Jones:** thickness wasn't an issue? Indeed. The other way of doing it, which does yield you higher efficacy but higher manufacturer cost, is a dedicated big flat PCB plastered all over with LEDs. Yep. And somewhere over here in front of it,

**Dave Jones:** a diffusion layer. Mhm. So that all the light emitted by these Yep. tends to give you a fairly good homogeneous light output. But I am imagining that wouldn't be as diffused as this solution because you would still probably see the point sources still,

**Dave Jones:** maybe as hot spots. can. If you get the diffusion layer too close to the LEDs, you start seeing the individual LED hot spots. Or you can it with some magic gunk, perhaps. Uh there are magic gunks. Uh one type of magic gunk I've seen is a

**Dave Jones:** a set of films. Mhm. Typically, you would also see these used on the LCD screens of laptops. Oh, got it. Yep. Which laptops tend to use just either a single CCFL tube Mhm. or sometimes arrays of LEDs and they

**Dave Jones:** need a high degree of diffusion. They do. Cuz yeah, you get consumers complaining about hot spots and cuz that used to be the case on the old notebooks. You get the hot spots in the edges where the Yeah.

**Dave Jones:** And color shifts, etc. etc. It's an expensive solution though Okay. The the cheap expensive solution Mhm. is to use a simple diffuser, space it relatively far away from the LEDs Yep. and just plaster this with many, many LEDs as closely packed as you can.

**Dave Jones:** Mhm. Uh you do what tend to wind up with first of all panels which aren't as robust as this. This is solid. This is solid. If you squeeze it, you can't feel any flex. There's no give. You can actually drive

**Dave Jones:** nails through that and nobody cares and it still keeps on working. If you want to, we can try that. No, thanks. I have seriously seen nails and nails driven through these and they just keep on working. Of course.

**Dave Jones:** Can't do that with this. It's going to flex. There's unless you have pillars in there to space that away, they're not as robust. And I in theory you could make this panel flexible as well. In theory if you use flex PCB and

**Dave Jones:** Ah, you would have to have a gel type acrylic. Ah, which would which you can do with a semi polymerized PMMA. Oh, okay. But I wouldn't like to try it myself. Right. Ah, that's an experiment for others to

**Dave Jones:** perform. Excellent. And we talked about the graph of the response of the light response across here. What's that going to Well, look like? Ideally, what you'd want is if you're getting 100% here, Yep. at some point you're going to get 50%.

**Dave Jones:** Mhm. Okay. Now, that's 50%. Where it is we we don't know. And if that whatever length that is in the same length, you're going to go from 50% to 25%. Yep. In the same length, you're going to go

**Dave Jones:** from 25 to 12%. So, in effect it's a uh inverse square law Yep. uh relationship. Ideally, if you've got a second Mhm. batch of those over there, which we do in these panels. you want to plan that half attenuation

**Dave Jones:** distance, Yep. so that the next one that you put over here just about there and they approximately cross in the center. Yep. And that will give you an approximately even light across there. So, me seeing a hot spot in the middle

**Dave Jones:** is probably imaginary. It must be by theory, it must be down. Not necessarily. Not necessarily because if it so happens that on this stuff the 50% mark is there Mhm. and there then you'll actually get an overall brightness profile like

**Dave Jones:** that across it. Ah. Of course. It won't be like that. Like yep. So, it won't be peaky. Right. It's just going to be a vaguely brighter in the middle. Mhm. Or if it's the opposite, it's going to be

**Dave Jones:** vaguely duller in the middle. Yep. It's not going to be extreme. Uh except for edge effects where you might get a a huge increase in brightness. Of course, yeah. Over at the edges due to edge effects around here.

**Dave Jones:** We don't seem with these panels, we don't seem to be getting a huge amount of that. No. Seems good. For a one hung low brand Oh, yes. panel. Yeah. They've done their homework. Yep. The efficacy is around about what you'd

**Dave Jones:** expect of such a thing. I have seen flat panels quoted at up to 70 lm/w but that would probably be for a horrible actinic dead 6,500 K color temperature with so much blue it burns your retinas out. And these are well, what? 4,000?

**Dave Jones:** Uh yeah, these ones are 4,000 K. So, they match my strip fluores I put in here recently. What uh what most people are finding is that 4,000 K is pretty much the ideal color temperature for uh office lighting, task lighting, paperwork, uh

**Dave Jones:** electronics work, that kind of thing. Uh for domestic lighting, anywhere between 2,700 K and 3,500 K with most most people seeming to have a vague preference for around 3,000 K. Okay. Interesting. And where where do the 6 and 1/2 thousand, you know, those huge

**Dave Jones:** daylight ones, so those six and six and 1/2, 7,000 even, something? Yes, yes, yes. You use those where you just don't care about the quality of light, you just want quantity of light. Yep. Uh got it. Street lighting tends to be a

**Dave Jones:** little bit that way. Right. Uh car park lighting, uh particularly subterranean car parks and uh outside your local clubs, the car park out there. So, you get the greatest efficacy at Yes. at around 6 and 1/2 K? Yeah, and the reason for that, okay, um

**Dave Jones:** where's the rubber? Rubber? Or an eraser even. Sorry, we can't do the chalkboard. Sorry. Okay. Let's do a plot of wavelength versus intensity. Yep. LEDs are on a blue LED, Mhm. which has got a spectrum a bit like

**Dave Jones:** that. Yep. And you chuck that into a phosphor. Mhm. The phosphor gives you your lower wavelengths. Now, depending on the shape on the balance of blue light versus phosphor emitted light, and of course of the characteristics of the phosphor, the

**Dave Jones:** phosphor will emit light down here in the visible region or region or uh if they've got a good phosphor, it might be a little bit down further towards the red. Right. Whenever you have a look at the uh characteristics of LEDs,

**Dave Jones:** you'll always see that characteristic like that. And it's the balance between the blue spike and what happens down here that gives you your color temperature. Color. Now, a cool LED will give you well actually pretty much what I've

**Dave Jones:** drawn there. Big blue spike and maybe right that. A warmy will give you A warmy being about 3,000. Yeah. will give you relatively low blue in comparison with your lower spectrums. Yep. Now there's also a characteristic of LEDs called the R9

**Dave Jones:** coefficient. A lot of the phosphors don't have much of the true deep red output. The R9 parameter tells you how much true deep red you get because a lot of the phosphors only really give you from your ready orange

**Dave Jones:** through to your aquas. Got it. Incidentally, that point there the the saddle back is usually just at aqua. Right. And for some reason well actually we we know why most LEDs are a little bit deficient in aqua. But your eye tends just not to notice it

**Dave Jones:** Mhm. because it's picked up on other side by the blue of the LED itself and the phosphor emissions immediately that side. Got it. And you're doing work on underwater LEDs too. Are there any tricks to underwater LEDs? Uh

**Dave Jones:** apart from the mechanical construction of doing underwater uh luminaires or underwater water electronics of any kind Mhm. I think that the basic thing to recognize about LEDs or light underwater is that the blues are attenuated much more quickly

**Dave Jones:** but they're attenuated primarily by scattering Got Let's go for the Let's rub it again. More theory folks. This is all off the cuff. We have no idea what we're doing here. I've got no bloody idea what I'm talking

**Dave Jones:** about most of the time. If we're looking down on a swimming pool and we've got a light over here. Yep. If it's if that light is emitting red light, most of that red light is going to travel really well through the pool,

**Dave Jones:** Mhm. but you don't get to see it. Why? Because it's traveling through the water, it lights up the wall over here perfectly nicely, but Uh-huh. that doesn't give you a lot to see. The blue, on the other hand,

**Dave Jones:** fascinating. Ah, do tell. It attenuates relatively quickly. It might only go, I don't know, maybe 10 m would be the 50% point. Right. But all of that blue is scattering. It's not just being attenuated, it's scattering and the pool iridesces blue

**Dave Jones:** and it's a beautiful sight to behold. Why do they Why does it Why does blue scatter? That's probably got something to do with the size of water molecules Molecules and or chlorine or something. Maybe, you know, maybe it's different

**Dave Jones:** between salt water or something. uh No. No? Nope. No. Okay. That's something it doesn't matter whether it's fresh water or salt water, although I have seen learned studies which show the the transmission of light through waters of different seas and they do

**Dave Jones:** have different properties, Mhm. but the differences aren't gross. Right. So, maybe the physicists out there can jump on to the forum and tell us all about it. Why? Bottom line is blue light in a swimming pool looks beautiful because the whole

**Dave Jones:** pool appears to glow blue. True. Red light Yeah. Whereas red light in a pool transmits just fine, but doesn't look any good. Mhm. In order to make the the redness of the pool equal to the blueness of the pool, you've got to

**Dave Jones:** really pile on the red light. You've got to have a lot a lot a lot of red light. And of course, you do run the risk like blues and greens in a pool look inviting. Mhm. I don't think that anybody wants to dive

**Dave Jones:** into a yellow pool or a red pool. Uh it's Yeah, it's We won't go there. We won't go there. let's let's not go there. Oh boy. Okay. And what happens to these panels when they age? Oh, you haven't got the you haven't got

**Dave Jones:** good data on that yet? Uh we've only got 4 years of data and Only? What do you mean these 100 W low panels last 4 years? Oh no, no. I'm talking about the underwater underwater lights, right. Yeah. So

**Dave Jones:** I've been in the business for yeah, 4 years doing the underwater lights for a local company, Aqua Quip. And yeah, we've got 4 years of data. Uh failure is uh incredibly rare. It's delightful. Uh the only real forms of failure

**Dave Jones:** they've had uh if the luminaire leaks. Yep. And they had a couple that did that. Uh Do you seal them with a re-enterable potting compound? No. No, you just don't bother. You just rely on the O-ring seals and

**Dave Jones:** Uh you're done with it? Yeah, in fact these are now they basically glue seal. Oh, okay. Because there's there's no need to service them. Yep. They either work or they're dead. Yep. One of the other reasons for them being

**Dave Jones:** dead is installers who forget that these are supposed to be low voltage light from 12 V AC. We have definitely had a few that have had 240 V put into them. The smoke has come out of the components.

**Dave Jones:** smoke, yep. Ah oh boy. uh mind you on on the upside, we actually do have designed these such that the first thing that the power hits is basically fuse protection, series fuse protection and parallel voltage clamping. Right. So, when that does happen,

**Dave Jones:** uh there's basically a weak link that blows. You know, in a They're They're They're fused. So, the potential for destruction, uh explosive destruction within it, is small. Got it. And it means that nobody's going to get electric- electrocuted diving into a

**Dave Jones:** pool that some wally has wired up. Uh-huh. Just as an aside, uh Queenslanders recently passed laws stating that you have to be a qualified sparky to do work on certain aspects of swimming pool lighting. Even if they're 12 volts?

**Dave Jones:** Even if they're 12 volts. Anything that requires An- anything that doesn't simply plug together Yep. a logical sequence that is impossible to up. Anything that requires a screwdriver or joining of wires Mhm. needs a qualified sparky. Doesn't matter

**Dave Jones:** whether it's the 12-V side or the 240-V side. Got it. It has to be blindingly obvious to cretins how it goes together, or else you have to be a qualified sparky. Ah, that's Queensland for you. Yeah. Well, one day crazy, the next.

**Dave Jones:** Yeah, I was about to say, look, maybe they've got a high proportion of uh cretins. I don't know what the reasons for the laws are. Hi to all my Queensland viewers. Yeah. Yeah. I do not respond to emails.

**Dave Jones:** It wasn't me, it was somebody else. And what happens to these lights when they age? Does the Do they just reduce in intensity and the spectrum stays the same? Yes. The third uh form of failure that we've discovered

**Dave Jones:** Mhm. is chemical contamination of the LEDs. Oh, okay. We kicked off using Cree XRE LEDs, which are actually more subject, I think, to chemical contamination than most of the current crop of LEDs. Why is that? Physical? Yes, it's it's their physical manner of

**Dave Jones:** construction. Got it. And we don't know if and we we actually sent these LEDs back to Cree for examination. They weren't able to tell us what it was. And they didn't put them through their labs. All they could do is

**Dave Jones:** shrug their shoulders and say, "Well, yeah, it's chemical contamination." But here's the interesting thing. We suspect that it might be ingress of some form of chlorine vapor. Oh. And uh the LEDs are susceptible to things like chlorine vapor, uh various volatile

**Dave Jones:** organic compounds, solvents. this on the underwater LEDs, not the regular shop ones. Correct. Uh mind you, we've also seen them in the regular shop ones where they've been operated next to stockpiles of pool chlorine. Oh, there you go.

**Dave Jones:** And what happens is the dies on the LEDs go dark. Yeah. Not only low emissivity, but the actual die looks discolored and ugly. So, you can physically see the wear on them. Yeah. The contamination. Yes. And And the the output drops to

**Dave Jones:** a tenth, a fiftieth of what it used to be. Wow. You can resuscitate them. Do tell. You operate them at very high temperatures, like 85 to 100 C on the die, for about a fortnight, three weeks, a month.

**Dave Jones:** They go good again. Do you have to do it on the die? Do you have to light them up, or you can just put them in a thermal oven and bake them? You could probably bake them, but we did

**Dave Jones:** it the easy way. We used the self-heating. Yeah. Got it. Yeah, they're they're they're they're not fit for resale or anything, but the fact that you can revive them from chemical contamination is absolutely fascinating. is fascinating. So, how did you know the

**Dave Jones:** die temperature? You measured the back temperature, and then you know the thermal conductivity of the We we know what the thermal conductivities are. We know the input power to the LED. So Let's let's go Down to the drawing board.

**Dave Jones:** Okay, down to the white board again. Here we go. If you've got a LED sitting on a heat sink you know what the thermal resistance is from the LED die to its solder junction point. cuz that's in the data sheet.

**Dave Jones:** You can measure what the thermal resistance is from the junction point to the heat sink fins because you can get a thermal couple on that. You can get a thermal couple on that. Measure the difference in temperature. You know how

**Dave Jones:** much power you're putting in. The math is easy. So bottom line is if you put enough power into this to get the heat sink up to say 85 degrees C and you know that you've got say well I'll pluck some numbers numbers out of

**Dave Jones:** the air. 10 degrees per watt there and maybe another 5 degrees per watt there. Total of 15. If you put a watt into that and it's enough to get the heat sink up to 85 then you're you're looking at 100 on the

**Dave Jones:** chip. Simple. I've done a video on that. LED lighting. Geez that was a couple of years ago now. They're still going. My the LEDs on my deck. Yeah, we're not talking about high level calculus and integration Yeah. It's yeah. It's a series series

**Dave Jones:** resistance Ohm's law Ohm's law type thing. Power is current and the thermal resistance is the resistance and the temperature is the voltage. There's the electrical parallel there. No pun intended. Too easy. And that's all we need to know about

**Dave Jones:** LEDs. That's LED 101. For the moment. Yep. Brilliant. Thanks Dougie. So with a little bit of luck Let's check out the RF remote on these panels. Sorry, but we're gaining here. That is fading down. Yeah. Now, apparently we didn't quite start

**Dave Jones:** with both of them at full ball. No. Can you see a little bit of residual flicker on the left one? I can see flicker on the camera here. Well, I'm The These These linear ones here Yeah. have no ripple.

**Dave Jones:** Mhm. So, they won't be responsible for any strobing. Yep. They're PWM control. Got it. Yep. We don't know what what PWM frequency they're running from. So, no None of the ones we installed up in the ceiling here are PWM at all.

**Dave Jones:** No. They're all constant current. Yes. Right. But, any of your fluores will have 100 Hz ripple. They will. There you go. And we are recording this at 25 frames per second. Okay. Now, let's see if Okay. That looks as though they're both

**Dave Jones:** up full now. All right. Now, it might also make a difference on where the actual controller boxes are. Yeah, it might. It might. All right. Okay. So, fading down. Fading down. And down and down and down. Down and down.

**Dave Jones:** You have you got a pretty good control range. The fact that you can get them down to Yeah, that's pretty impressive. Now, visually I've got this camera set to fixed exposure, by the way, so Come on. Okay. That's as low as they'll go.

**Dave Jones:** Yep. And coming up. And that looks like pretty much full ball. Mhm. Yeah, I'm seeing no strobing at full brightness here on the LCD screen of the camera, but when it was halfway, I was seeing significant strobing. When it's at 100% and 0% there will be

**Dave Jones:** no flicker content Mhm. because the P W M is either going to be full 100% or nil. But yeah, as soon as you start fading a bit, you should start getting some strobing there. Yeah, getting some strobing now.

**Dave Jones:** Yeah. Not sure if this will show up on camera, folks, but bucket loads of light. Oh, that's really sweet. I like it. Not bad for a one and only cheapy. Yeah. And these are 60 W Yes. rated 60 W output.

**Dave Jones:** Yes. Got it. All right, no, rated 60 W input. It's input, sorry. Yes, of course. 3,000 lm That's 3,000 lm output. Yeah. What's a regular office fluoro in lm? Uh call it 70 lm per W for plain vanilla

**Dave Jones:** Yeah. tubes. You might get 90 lm per W for a quad phosphor. Yeah, which is what I got. Yeah. And some of the new quad phosphor T5 tubes Mhm. which can only be run with electronic ballast. They're the very, very skinny

**Dave Jones:** ones. Oh, yeah. Uh they can get in excess of 100 lm per W but don't put your money on them. Right. And the other thing about fluoro tubes of any type, of course, is that their efficacy varies hugely with temperature.

**Dave Jones:** Mhm. Which is why you get the warm up effect that we noted before. Yep. And which is also why at low temperatures below 15°, 10° C quite often when they first spark up, they're half as bright as a dead

**Dave Jones:** glowworm. And they perform incredibly badly in sub-zero temperatures. There you go. LEDs rule. Yep. None of this compact fluoro rubbish, right? Well, compact fluoros are just a variant on the fluorescent theme. Yeah, yeah. They're Look, they served their purpose

**Dave Jones:** as a stopgap solution between incandescence and LEDs. Look, you'll see them around for half a dozen more years, but LEDs will take over. Definitely. Oh, I think within a decade, definitely. Exactly. And we're starting to see more and more

**Dave Jones:** solutions using LEDs that don't necessarily conform to your usual bayonet socket plug-it-in type lamps. They're still definitely a place socket plug-it-in lamps because there's billions of such lamp bases in the planet. But, new lighting can use different form

**Dave Jones:** factors like these ones, which aren't just a slot-in replacement. They're a new lamp unto themselves. These strips up here, they're a new lamp unto themselves. I can see these going into these uh flat panel ones going into where the all the

**Dave Jones:** McMansions. The you know, cuz they look pretty jazzy. Particularly if the if they're in 3000K color temperature. Right. Which is something it's the preferred color for domestic applications because it's fairly close to that that you would get from an incandescent lamp anyway.
