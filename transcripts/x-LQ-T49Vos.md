---
video_id: x-LQ-T49Vos
title: EEVblog #433 - Mailbag
url: https://www.youtube.com/watch?v=x-LQ-T49Vos
source: youtube-asr
---

**Dave Jones:** Next up, we have something from Lelay Chi. Thank you very much, Lei. He's from Malaysia, Paneang in Malaysia. Don't forget to look at the Malaysian stamps again. Okay, not a problem. Lovely birds, fruit, and flowers. Beautiful. All right, this one is a uh rather

**Dave Jones:** largeish box. Oh, I thought there was a uh gap along there. No, there we go. along the front here. So, this could be anything. I have no idea. Oh, HP. HP. Serial. See, serial port. No, it's not. Sure. It's a SATA power cab. No, sure it

**Dave Jones:** will be something else entirely. Hi, Dave. Thank you very much for an interesting EV blog. As I mentioned earlier in the forum, I'm going to send you a handheld pulse generator for your review. The reason I built this handheld

**Dave Jones:** pulse generators allow me to perform do-it-yourself passive probe. Yep. Um, another reason allowing me to verify the bandwidth and step response of my probing system. Of course, we've done some videos on that and a few people have sent some stuff in. Uh, when I hook

**Dave Jones:** up the pulse generator blah, yep, the rise and fall time.35 on uh that's for a Gaussian uh response bandwidth. Um, it generates 1.4 ncond rise time. Four time is a bit slower at 1.9. With this, you can verify up to 250 MHz. So yeah, it's

**Dave Jones:** not particularly quick. It's not like the Jim Williams uh pulse generator that is in the order of, you know, 300 picosconds or something like that. But thank you very much, Lei. Happy mailbag day. Woohoo. Let's have a look. And we

**Dave Jones:** have a most excellent uh 50 ohm 2 watt uh dummy load uh DC to one gig. Fantastic. And he's also included uh two signal conditioning kits from Pulse uh Research Labs. I hope you can use them. So, excellent. There looks like

**Dave Jones:** this just comes off here. Is there anything in them? No. Okay. They're just a uh they're just a blank uh board which then you can um you know do your own roll your own uh filters and stuff like

**Dave Jones:** that. So, that's they're very handy. That's really nicely uh engineered. I rather like that. Wonder how much they cost. And there you go. So, here's these signal conditioning kits and uh up to terminations up to 5 gig. Oh, beautiful.

**Dave Jones:** Yeah, these it feels like it's that sort of quality. Ah, that's for the SMA ones or 3 gig for the BNC uh version which we've got depending on PCB uh depending on the substrate they're using, I guess. And on the back here is a neat little uh

**Dave Jones:** uh sample applications. DC blocking, of course, you can just put the AC coupling cap in there. Um AC block, which just has a choke in the middle. Uh, series termination, shunt termination configuration, precise shunt termination, uh, feed through decoupling

**Dave Jones:** cap, diode detector, attenuator, low pass filter, highp pass filter. Beautiful. And here it is. Don't turn it on. Take it apart. No worries. We will take it apart. Overshoot 3.5 7 uh 3.574%. Pre-shoot 1.1 to1%. Getting pretty precise there. Cycle jitter less than

**Dave Jones:** 600 picosconds. Uh, peak to peek. Ah, look at this, man. It's got everything on there. It's the L7101 pulse generator. Fantastic. There's a uh nice BNC. We got some test points on there. Not sure what the dip switches.

**Dave Jones:** It's a Right. It's a It's actually a pulse generator as you can set it with the DIP switches. 1 kHz, 10 MHz, Logic Zero, or one. Excellent. I like that. Battery included. Please connect before use. There you go. Uses a standard uh 9V

**Dave Jones:** uh takes about 70 milliamps. That's actually that's a lot from a uh 9V battery, but uh patent pending. Really handade handmade in Malaysia. That's a nice case. I really uh quite like that. That is neat. So there's our battery.

**Dave Jones:** Yeah, that's really nice. Big thick screws on there. Let's take this sucker apart. Tada. There we go. Look at that. Neatly designed. It's even fused. Beautiful. And we have a little bit of uh budginess happening here on the

**Dave Jones:** board. Eh, few little last minute changes, but uh yeah, that's actually uh quite neat. That is uh well designed into that case. I really like that. And if I have a look at lay's schematic here, as you can see, there's uh not

**Dave Jones:** much to it at all. We've just got some uh output filtering down here. We got a 74 HC uh 4851. We're going to send an HC 390. Uh two 390s there. And uh not much else to it as far as the power supply

**Dave Jones:** section goes. Got a soft power on switch here. And uh looks like there's a low battery detect circuit and a um virtual ground with an opamp there just generating the virtual ground in the middle getting the uh positive and

**Dave Jones:** negative rails. And he's using an OPA 875 uh MX there to drive the output directly from that. So it just looks like it just chooses between uh the uh reference and ground and that's it. And I haven't uh decoded this one at all in

**Dave Jones:** terms of the uh uh actual operation of this, but there seems to be shenanigans going on here with the um HC 390 flip-flops to generate the uh pulses required, hence the Rs and C's in there. So, let's give this thing a go. I've got

**Dave Jones:** it uh directly connected into a coupler. Of course, this is a 50 ohm capable uh scope. So, the input is set to uh 50 ohms input impedance. And uh we'll give that and give that a go. Press our

**Dave Jones:** button. Tada. And the rise time there pretty much bang on to what he said. 1.4 odd ns. There you go. And the fall time there. Yeah, around about 2 nconds. He said about 1.9, but yep, close enough. Now, the thing is it's um just a square

**Dave Jones:** wave. Um so I don't know what all those uh shenanigans were going on with the Rs and C's around the uh flip-flops, the HC 390s. Uh not sure what's going on there at all. I expected it to like generate a

**Dave Jones:** uh a shorter pulse or something like that with a different uh duty cycle, but no. Anyway, that's the 10 MHz option. Whed it's got auto switch off uh mode on the switch there. there. It only goes for about 20 seconds or so. So, that was

**Dave Jones:** the 10 MHz waveform. This is the 1 kohz uh waveform and same duty cycle, 50% duty cycle. And uh if we go in and have a look at the rise time, yeah, there it is. The same 1.4 odd nconds. And the

**Dave Jones:** fall time there, yeah, around 1.9 to 2 nonds. Same as the 10 MHz waveform. Now I'm using what uh Lei calls the uh logic high output level and the thing just switched off and it looks like it's uh I

**Dave Jones:** don't know designed to generate a single pulse or something like that. So I think his terminology might be a bit wrong but check out as it's decayed like this. Check out the weirdness which is happening as the uh as the power supply

**Dave Jones:** voltage discharges. Really quite neat. So if we trigger on the positive going edge here I'm going to push the button and uh see what we get. There we go. we just get a single edge which oh that does not look clean at all. That's very

**Dave Jones:** nasty. So I'm not sure what mode that thing's actually uh what that's actually designed to do. It's a bit weird. And there's that uh same decay you saw before over time. That same weirdness happening as the voltage drops and

**Dave Jones:** finally decays and then drops off right at the end there. Neat. It's fascinating the effects you can get with uh you know when power supplies do weird stuff and you wonder why your circuits do weird stuff when your power supply does weird

**Dave Jones:** stuff. Check that out. Try and model that on your bloody simulator and see what you get. Huh. So here we go. I've managed to capture this thing on the what Lei calls the logic low mode. And uh I you know look it it's attempting to

**Dave Jones:** generate pulses there. But look at that. I mean, you know, yeah, we might be getting a uh a falling edge there. Um sorry, I've haven't sampled that properly. It's all over the shop, of course, due to all those um RC's

**Dave Jones:** doing stuff. But there you go. Look, we're generating Look, it looks like we're generating a sharp positive edge there and then a Yeah. So, like a sharp an alternating sharp positive edge and then a sharp negative edge. Um, in that case, I guess

**Dave Jones:** it's kind of rather clever. But, uh, yeah, I just don't sort of understand the benefit of that at all. I've sampled that a bit better. And, well, the falling edge there is, you know, is is hopeless. I mean, we're talking, you

**Dave Jones:** know, 3.8 microsconds. So, I'm not sure what's actually what's going on there at all. The uh the uh rising edge there is reasonably quick, but yeah, I don't see what mode that is at all. Lei, please explain. But on the regular signal

**Dave Jones:** generation mode, that really does give a nice response. You can see there's very little overshoot. There's very little pre-shoot there at all. Very little overshoot. I mean, this is only only a 500 MHz bandwidth um scope, but you

**Dave Jones:** know, that's that's pretty good. I like it. Next up, we have something from France from Thomas Salandi. I'm sure it's not Salandi Thomas. Well, it could be. I don't know. Um, I don't know what the uh if that's normal to put your last

**Dave Jones:** name first on something like this, but uh this is a rather interesting box. I like this. Um, there you go. There's a French stamp. Not really. It's not even a stamp. No, it's just printed on there. Hopeless loser. All right. One

**Dave Jones:** old mobile phone. Woohoo. There we go. Must be a bloody big mobile phone. Of course, the uh Motorola one we uh tore down ages ago. There you go. Thomas Salandi. Thanks, Thomas. He's a geek and a photographer or a geek

**Dave Jones:** photographer and safeta.org, however you pronounce that. I'm sure I've got it wrong. Anyway, and he's from Paris. Dave, I can't thank you enough for everything you taught me in your videos and of the fun I had listening to

**Dave Jones:** the Amp hour with Chris. Hi, Chris. This was uh my very first mobile phone. It was pretty old when I got it. Required full-siz SIM card and made me feel very important every time I pulled the antenna. Hope you enjoyed taking it

**Dave Jones:** apart. All this Thomas, thank you very much. Let's look at what Thomas's first. Oh my good. Oh, right. That's the Oh, it's the Microteac. There you go. It's the uh Oh, yes, folks. Oh, state-of-the-art. Has it got that old electronic smell? Hang on.

**Dave Jones:** Oh, yeah. Isn't that just a thing of beauty? Look at that. Ah, state-of-the-art technology. Ah, pull the antenna up. Ah, you're a big shot, you know, Wall Street broker or something like that with your mic Motorola Microte mobile phone. Were they

**Dave Jones:** I don't were they even called mobile phones back then? I wonder when that term actually started. I don't know. I have a vague recollection that they weren't actually called mobile phones and they were called portable phones or well cell phones in the US. Um something

**Dave Jones:** like that. So, not sure when that terminology came along, but there's the uh charging station for it. I wonder if it uses nickel metal hydride, probably. Uh, sorry. Um, yeah. Well, Nikiad or nickel metal hydride. So, let's whip that off. Let's have a look.

**Dave Jones:** Doesn't tell you. Bummer. Uh, yeah, I'm guessing that would be Nike or nickel metal uh hydride probably. And there it is. It's the Motorola 7200 Microte made in Germany. Well, as it turns out, this thing's actually fairly recent. It's

**Dave Jones:** 1994 vintage. So, well, it's almost uh 20 years old still, though. But it's uh not one of those analog ones from the '90s. This is a digital uh 900 MHz GSM model. So, it's actually far from the uh

**Dave Jones:** analog bricks that we had back in the day. And if we have a look at the uh weight of this thing, what does it weigh? Let's have a look.

**Dave Jones:** 250 grams, quarter of a kilo. Ah, it's not too bad. So, thank you very much, Thomas. That will be the recipient of a tear down Tuesday. Coming to a video blog near you. The uh charge is interesting, too. It just slot. Well,

**Dave Jones:** yeah, fail. It does slot in there like that. And it has another slot down in there. Uh presumably to charge a spare battery, or at least uh that's the plan, I suspect. There we go. Yeah, that's the idea. You whack the battery in there,

**Dave Jones:** and you can whack your phone in the front, or you can whack two batteries in there like that. It's actually rather neat and modular. You can char Looks like you can probably charge two batteries at a time. Um as well as

**Dave Jones:** having that third one ready to go on your phone. Wonder what the uh battery life on this sucker was. And just to even it out, we've got one from JP in Willoughby here in New South Wales, Australia, not Austria. Let's check it

**Dave Jones:** out. Paid a whopping $865 to post it. Thank you very much, JP. Wonder what it is. doesn't actually say cuz there's no, you know, no need for customs uh forms of course when you're sending stuff internally. So, let's flip it open. Mystery.

**Dave Jones:** Hey, it's a can of something. Look, check it out. All right, let's have a look. Yes, we've got some flux in here. Sorry, some uh solder. Yeah. Oh, look at this flux gel. There we go. Fluxine PCB cleaning solvent. Awesome. Complete with

**Dave Jones:** a little brush there and nozzle. And we've got some flux gel. Brilliant. From um AIM solder. And there's no Yes, there is. There's a letter. Hi Dave. I'm glad that you do like the probes. Ah, of course. George is the one who uh sent me

**Dave Jones:** those um sexy little probes. In regards to the soldering video, please try out these two products. Been using them for years and they work well. Yes. On the smartboard, apply the flux flux gel around the chip and blow hot air from

**Dave Jones:** your 18 hot air station until the flux gel starts to boil and solder melts down. That will trim the solder joints. Yeah, it' probably uh work a treat, I'm sure. After this, let it naturally cool down and clean with the electrolu.

**Dave Jones:** Now you should see a nice factory looking solder work. I'm also using this for hand soldering and it works great. Yes, I have no doubt. Thank you very much, George. Yeah, I don't have any of this um gel type uh flux. I've only got

**Dave Jones:** like the flux uh pen. I've used this uh sort of stuff at work before, but I've never actually had any at home. And I've actually used this before as well. This uh flux clean stuff from Electrolube. Um they make, you know, a ton of stuff. And

**Dave Jones:** uh here's the stuff I actually have in the lab here. It's a more general purpose electronic cleaning solvent. Once again from Electrolube in the familiar package with the big E, but this is just um isopropanol uh alcohol. What's the percentage? Uh yeah, you

**Dave Jones:** know, 99.7 pure um% pure isopropanol alcohol. So it's different to this fluxine stuff I believe, which is let's have a look. Does it tell you a rapidly drying blend of solvents for removing contaminants from print circuit boards and flux residues after soldering? Just

**Dave Jones:** spore area before using on plastics. Well, you know, a lot of your components um on your board are going to have plastic packaging. There you go. Uh it doesn't actually tell you what's in it. H nope, there's no information on that at

**Dave Jones:** all. It's just got a blend of solvents. Yeah. Well, anyway, um thank you very much, George. I will definitely use these two next time I do a soldering video.
