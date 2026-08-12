---
video_id: HyIYb2gAN6g
title: EEVblog 1694 - Scarlet Rae Teardown + Design Discussion with Xentronics
url: https://www.youtube.com/watch?v=HyIYb2gAN6g
source: youtube-asr
---

**Dave Jones:** Hey, and I'm here with Scott Williams from Sentronics. He's been on the Amp Hour and in the previous episode, so I'll link those in if you haven't seen it. Um he's from Melbourne, guys, so we won't hold that against him.

**Dave Jones:** And he's going to show us this rather interesting product for all my female viewers out there might be interested in this. Tell us about this and we'll Yes, we will do a teardown. Yeah, absolutely. This is This is the

**Dave Jones:** Scarlet Ray, so this product, the female founder came to us. She suffers from endometriosis, so effectively horrible cramping, pains, uh a lot of issues with, I guess, uh period pains and menstrual pains. Now, in terms of how do you solve that,

**Dave Jones:** right? That's a problem you have. How do you solve that? The typical go-to solutions for a lot of females is hot water bottles, disposable heat strap, uh heat strips, uh a few other solutions like that. Uh none of those for her and

**Dave Jones:** her personal experience they were suitable. Not fit for purpose. On the market, there's a few modern uh devices that are effectively portable heat packs. Some of them are, you know, you might have to have it plugged into the wall, so you're tethered to the

**Dave Jones:** wall. Some of them are big and bulky and they they heat up, but they have a big strap that wraps around you. Some of them are kind of overkill. They have a massaging mechanism in them as well or a

**Dave Jones:** TENS machine. They're all basically, again, kind of over-engineered or just not good not not right quality. don't want a jack of all trades, master of none. Exactly right. Exactly right. So, her vision for the product was a solution

**Dave Jones:** that just solved one problem and that was heat. That was all we want is heat. So, this just heats up? That's exactly right. So, it's effectively a portable heater, so we turn it on, press and hold this button.

**Dave Jones:** Oh, LED comes through the silicon cover there. Nice. This actually has haptics. I can't show you, but when I'm pushing the button, it's actually vibrating like your phone does. right. Oh, so you don't have to see You don't have to Yeah, and if you just

**Dave Jones:** press it, you know what what mode it's in. It vibrates different modes to Right. So, you can see the lights, there's three heat modes. They're super simple, right? You can't You can't go wrong with these. User interface, easy.

**Dave Jones:** Exactly. So the max heat setting is up to 50°. So there's various IEC safety standards that the product meets, and 50° is the maximum any heater product you. Exactly right. Can can intentionally be heated And it's just like your home hot water,

**Dave Jones:** you've got to install the the valve that automatically Exactly right. Even Temper temper valve. Even products that aren't intentional heaters, that's also their maximum temperature on the outside. So her vision was a product that was slim, sleek, portable, hot,

**Dave Jones:** easy to use, and this is where we came to. This is the end result. So this was two years of hard work. You can see all of the regulatory markings and safety safety standards that we've taken it through. It It's sold in

**Dave Jones:** the Europe, UK, Australia, and New Zealand. So quite a successful So it's only for those markets. Only for those markets, right? The US, quite interestingly, needs to be UL rated. Now anyone who knows about UL Yes. Anyone who knows about UL certification

**Dave Jones:** knows that even this was a complex project, UL makes it a whole lot more complicated. Yes. All right. So that's a separate step again. Exactly right. But look, this this this project's been fantastic to be a part of. They've They've sold, I think, a

**Dave Jones:** thousand in the first month of launch. If you check out the reviews on their website, you'll see about 70 five-star reviews, no other reviews. It's It's changing people's lives. They love the product. Everything she hoped for is now coming true, which

**Dave Jones:** is fantastic. So this is a silicon So you guys designed and built the entire So what So what we did is we did the electronics inside. A company here, you can see Trik. Trik, they're a design firm based in

**Dave Jones:** based in Melbourne. They also did the design for Oh yes, we saw that last time. Yes, they did the industrial design for this one. So we worked again with them on this project. Yeah, cuz you still don't you don't

**Dave Jones:** still have an industrial designer in house. You were talking about that last time maybe but Uh no, no. Last time we talked I said again we'll stick clear of that. More systems engineering and broader engineering I think. Um so again doing

**Dave Jones:** early focus groups and user studies to work out the shape they should go for, doing different prototype colors and sizes, even the silicon. This has a specific finish of silicon to get that smooth feel. It's not actually just

**Dave Jones:** normal silicon. Does it have to be a specific type of silicon for non-allergic kind of Oh, it's right. Food grade. Food grade silicon. Okay. So again you obviously see various other things that are subtle like the user manual. So we helped design and develop

**Dave Jones:** the content of that as a part of the safety standards. And look, it's been a great success so far. Great, can we do a teardown? Yeah, so I mean obviously it's it's on the market. Anyone Cuz these things are actually sealed in

**Dave Jones:** two parts glued. Exactly. So and I can feel that getting warm, trust me. This is feel a vision. So if you if you have your hand up to the screen, you'll be able to feel the heat coming out of that. So here we here we go.

**Dave Jones:** So this is what looks like on the on the inside of the unit. So exactly as you would expect, you rip it open and there's uh a flex heater. And now this this was very novel to design, right? And with the flex heater

**Dave Jones:** if you have a really thin trace, it gets warmer with less current but it also has higher resistance. It does. Yes. This is a consumer product. You can't design in complex power electronics drivers and things. We had to come up

**Dave Jones:** with something simple, neat, something that would spread the heat evenly. Even the glue between the flex and the silicon, nothing sticks to silicon. That's a little known fact. That's why it's made of silicon is it's easy to clean. So good luck trying to find

**Dave Jones:** something that can glue this to a silicon. That was a challenge in and of itself. Got it. Did you have to thermally model this or you just did a trial and error kind of trial and error? There I'm sure

**Dave Jones:** you could have done this. Probably specialized software, right? What are they What does that guy say? My favorite simulation tool is solder. Is solder Yes, right. My favorite programming language is so. Programming language Programming language is solder. Yep.

**Dave Jones:** Uh so you can see the battery underneath this cage here. So that's a standard requirement for the IEC standard. So it's actually protected mechanically. Right. So you can't put a raw like a battery just directly against the skin.

**Dave Jones:** No, exactly. Not so much the skin, more just the Right. It's like More against the back parts of the product. Right. Uh and then obviously the button, the LEDs, various other parts for the control, the battery charging, everything you would expect in an

**Dave Jones:** electronic product. There's the main board down in What processor did you use? So we actually used an NRF52. Okay. And that's actually future-proofed for blue It's future-proofed it for that. Right. So not at the moment, but you could future-proof it. Okay, got it.

**Dave Jones:** thing with the NRF52s, which is great, little known fact, they're so cheap now that you can kind of just use an NRF instead of an STM or instead of an NXP or instead of a microchip. It's still like a dollar, two

**Dave Jones:** dollars, even if you don't use the Bluetooth. Doesn't mean you should standardize on it. They obviously have their own trade-offs and limitations, but if you're even remotely thinking about connectivity, same with an ESP32 and Wi-Fi, right? If you're even

**Dave Jones:** remotely thinking about it, it's worth just going with that. Got it. And what's the retail price of this? So the retail price is 129 Australian dollars. Way cheaper than I thought it would be. I mean, look, it's like I said, it's got

**Dave Jones:** 5 hours of battery life, right? It's a premium product, USB-C recharging. It's designed to be something modern in a person's life and a modern woman's life and a companion. Same as your phone, right? And the value it brings, I think it's it

**Dave Jones:** sells itself. I totally Now, you were saying that you did not do this as a rigid flex hybrid, which is which is Well, we've got an example over here, right? This is your new That is a rigid-flex hybrid

**Dave Jones:** where the flex is like done as an inner layer. It's actually embedded or it's done as a top layer or a bottom layer, right? Yeah, yeah. So, it's actually embedded in there like that. Um that's rigid-flex. And you said the reason you

**Dave Jones:** didn't go with that is cuz it's like a dollar more expensive. Yeah, right. So, so even having two separate a flex and a rigid, uh in a lot of cases, it's still more affordable than doing a rigid-flex design. Rigid-flex just steps it up such

**Dave Jones:** a higher degree. What that means is if you're designing to do a rigid-flex in your design, you need to make sure you have a really strong justification for it. See, that's actually separate. Yes. So, that's just glued on the bottom like

**Dave Jones:** that. So, yeah. Yeah, so that is a cheaper solution, um but works just the same. Exactly. So, with rigid-flex, the reason you might want to use rigid-flex in for this application, it's actually get the sensors pointed in the right direction.

**Dave Jones:** Because these these uh sensors This is an acoustic I think we did this last year. This is an acoustic direction of audio. Yeah. Yeah, so these are little microphones, and then these just flip up like that. So, you just bend them up. So, yeah.

**Dave Jones:** Rigid-flex. And um the the the thing is uh alternatively, it can be related to like inside camera devices. Rigid-flexes are very common in your ears. Oh, I've done tear downs of the cameras. It's It's you literally have to use

**Dave Jones:** rigid-flex. It's not possible to have so many connections, so much shielding, controlled impedance, right? A normal flex FFC even, you can't have controlled impedance on this. You've just got tracks going over it. Some companies are now selling ones with EMI shielding. EMI

**Dave Jones:** shielding is different to controlled impedance again. So, uh yeah. So, again, you got case-by-case basis, but a lot of times, rigid-flex, it can't just be about the look and the convenience. It's got to be a real specific reason,

**Dave Jones:** otherwise the job the cost is too hard to justify. Got it. Uh yeah. Yeah, so that is that is very cool. And I noticed that um of course um cuz you don't want it to go over 50°C, so you've

**Dave Jones:** got a thermal cutout there. You can see that's glued down. Is that Is Is there a cutout slot in the board there? Right, yeah. Right, right. So, there's cutout slot in the board there for that little uh thermal um switch. And you can see

**Dave Jones:** that that's just in series. Exactly. This is There's so much that's been designed into this to just not compromise quality and not compromise my safety. That was That's a huge part of this. When we're working with a local

**Dave Jones:** brand here in Melbourne, we don't want to cut corners. We want to make sure even, you know, for example, the battery charger, it's not just some backdoor component we found. It's Texas Instruments. Like it's a premium component, right? In terms of power

**Dave Jones:** electronics, you can't go wrong. Exactly. All of the um, you know, if the battery's getting too hot, it'll charge at a slower rate according to the JDEC standards and stuff. It's It It's all comes out of the box, so no

**Dave Jones:** compromise there. And look, there's I think there's nearly 2,000 of these out in the field. It's been 3 months, and there's been no quality issues whatso whatsoever. Well, that is very cool. That's a very cool example of where somebody with an

**Dave Jones:** idea um like this can come to a design consultancy like like yourself and go, "Please um you know, it's not particularly cheap. There's a lot of money in the money and a lot of money in the development of this thing."

**Dave Jones:** So, Like this one, the question was how hot can we go? How hot should we go? The amount of time we spent just on that before starting to design anything at all. That was, you know, a quarter of

**Dave Jones:** the project. It's just working in the problem space, we call it. So, that was a 2-year project from start to first production. Yep, that doesn't surprise me at all. And you could say another year just the client uh ruminating the idea and and

**Dave Jones:** you know, exploring other ways of getting it done and working with China and all these other options, right? So, uh yeah, fantastic result for everyone in the end. That is great. That's yeah, fantastic example of a very simple product. Trust

**Dave Jones:** me, you don't do not want a jack of all trades masters of none product. You want a product that just solves one problem and solves it well. That's always way better than a Swiss Army knife solution. So, yeah, the ones

**Dave Jones:** that have vibration built in and and massaging all that. No, no. It's just you get bulky because of that, but then the problem then is we want something slim, right? And um tell us about why you've done these little um fingers embedded these

**Dave Jones:** little fingers into here. Yeah, so it's pretty pretty obvious, right? If you if you don't have these and this is sitting over here glued, people can pinch and squeeze and break either the electronics or or the heater itself, right? Um again, even the

**Dave Jones:** spacing of these and the thickness of it, that's something that you can't really um guess nor can you simulate. You just genuinely have to iterate and test. Got it. Um so, yeah, quite a quite an amazing uh amazing project to be a part of that

**Dave Jones:** one. That is really cool. Thank you very much, Scott. That is awesome. And check out Zentronics, uh link down below. Catch you next time.
