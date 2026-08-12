---
video_id: imdtXcnywb8
title: EEVblog #247 - Anti Static Bag Myth Revisted
url: https://www.youtube.com/watch?v=imdtXcnywb8
source: youtube-asr
---

**Dave Jones:** Hi. Why am I wearing the lab coat? Well, it's myth busting time. Going to revisit an old myth I did back right in episode number three. It's the pink antistatic bag myth. Now, as the myth goes, these pink antistatic bags and also these

**Dave Jones:** antistatic tubes, antistatic, okay, in quote marks, they're supposed to protect your ICs. And well, that it really is a myth. And I said that back in episode three. These do not protect your devices at all. I can just

**Dave Jones:** zap my chips straight through this bag and straight through that antistatic tube. What you need is one of these metal shielding bags. Now, what I did in episode three is I just talked about it. I didn't actually demonstrate it. So, I

**Dave Jones:** thought I'd do just that for this episode. It's really interesting. And what prompted me to do this is Element 14/Farnell. If you've been following my tweets, they actually This is how they sent me my chips. No proper static shielding bag at

**Dave Jones:** all. They just sent it in the antistatic tube and the antistatic pink ESD bag. Not good enough. Not by a long shot. Somebody wasn't thinking, didn't have their heads screwed on. But, if that happened to a company and you ordered

**Dave Jones:** them, they would you would Farnell Element 14 would fail an ESD audit, the company would be blacklisted, and all hell would break loose. So, you've got to take ESD seriously if you're a component distributor. And not only just

**Dave Jones:** shipping the stuff, because that's important, but handling in your factory as well. Now, granted, they they did actually call me up and admitted that yes, they're aware of it, they screwed up, it came from their Singapore factory or something, and they're investigating

**Dave Jones:** it. Whatever. So, anyway, I thought it'd be a real interesting thing to actually do a real test. Can we see the difference between a proper static shielding bag and one of these ESD bags? Let's go. The only good thing that this

**Dave Jones:** that this antistatic tube is going to do is that when you handle it and move it around, the surface itself, the plastic surface, is not going to build up a static charge because it is actually treated with an antistatic uh an

**Dave Jones:** antistatic material that actually stops the charge building up on the surface of the plastic. And this pink antistatic bag that the Element 14 parts actually came in is no different to this plastic. It's just like a In this case, it's probably just like a

**Dave Jones:** polyester type bag, and it is coated with an antistatic material, hence giving it that pink sort of effect. But they don't necessarily always have to be pink like that. They can actually be clear like these tubes. Now, these

**Dave Jones:** antistatic bags are also known as static dissipative. So, if you see it's the same thing. Static dissipative is effectively the same thing as antistatic. So, what you need to protect your devices is one of these static shielding bags. Typically, they'll have

**Dave Jones:** like a metal film inside of them, and they're they're kind not quite as see-through as the other bags, but once you put your chips inside one of these static shielding bags or a conductive bag, you can also get a black bag which

**Dave Jones:** is actually conductive that'll do exactly the same thing. And once your devices are in there, you can throw them around, do whatever you want, zap try and zap them, and you won't be able to actually kill the devices inside. But

**Dave Jones:** these bags and these tubes do absolutely nothing. I can walk up to this. If I'm charged, I can go zap and kill that device right through that bag and that tube. So, why bother having these bags and these tubes at all if they're no

**Dave Jones:** good for protection? Well, the idea is that they do not build up a charge. So, when you're using them on your ESD mat like this or you're in what's called your ESD safe area where everything's grounded, you've got your wrist strap on

**Dave Jones:** and everything, everything on these benches on a in an antistatic area should be static dissipative. It should be antistatic. So, I shuffle this around the surface like this and it's not going to build up a charge. I can get two bags

**Dave Jones:** like this and I can actually rub them together like this, two bags, and they will not actually build up a charge because that's how you build up a charge using the triboelectric effect. You get two different materials and you rub them

**Dave Jones:** like that. You're familiar with that, you know, walking across the carpet or rubbing your jumper with something with a you know, comb, things like that. You can generate static charge between two surfaces. So, how are we going to test

**Dave Jones:** this? Well, what I've got here is a surface DC voltmeter and this will actually give me a direct read out in thousands of volts, I kilovolts, at on any surface that is behind this metal sensor plate on the back. So, we

**Dave Jones:** can actually measure the charge on a surface and also see if any charge gets through these pink ESD bags or the static shielding bag. And to generate a spark, I've what I've done is I've got one of these little

**Dave Jones:** piezoelectric spark generators. There it goes. Like that and we can generate ouch, got myself there. We can generate a spark and I actually got this out of one of these butane barbecue lighters, one of the trigger base things. You pull

**Dave Jones:** the trigger and the flame comes out because the spark at the end of this piezoelectric igniter generates the butane coming from here. And you can get them out of cigarette lighters and all sorts of things. So, um it's not exactly the best. I'd rather

**Dave Jones:** use a proper ESD gun. You can actually buy proper guns which actually generate what's called a human body model charge. Like it's a known designated charge in into your device. But we don't know that. I think this will be a decent

**Dave Jones:** substitute. Let's try it out. You need about 10 kilovolts or so, rough rule of thumb per centimeter, per 10 millimeters to jump across there like that. But it depends on the atmospheric conditions and all sorts of stuff. Okay,

**Dave Jones:** so let's do some practical demonstrations if we can. I've got my surface DC voltmeter here. And as I said, it measures directly in kilovolts. So, what you're reading is 1.00 kilovolts. So, that is 8 volts at the moment that it's displaying. And that's

**Dave Jones:** relative to 1 inch below the surface of that plate there. So, if I reset it, as you can see, I've got it grounded to my antistatic mat underneath. So, I'll zoom out here and we can put various things under here and we can actually

**Dave Jones:** see the effect of the charge on those surfaces. Now, I'm just standing here. I've got my lab coat on, not that that matters. But I'm not haven't got my wrist strap on at all. And there you go, 30

**Dave Jones:** 30 odd volts. That's what my That's what my body's actually at. You know, your regular bubble wrap that you're no doubt familiar with. And let's put it under here and see what this is generating. Many hundreds, 500 odd volts in this case, negative 500

**Dave Jones:** volts. Now, let's take some Mylar wrapping which is from my MakerBot. And let's put that under there and have a look at that. Oh, look at that. 2,000 volts, 3,000 volts. Huge. Generating massive voltages on the surface, 4,000 volts. Generating

**Dave Jones:** massive voltages as I peel that off and the triboelectric effect is working on that Mylar wrapping. This is horrible stuff. Let's take our pink funnel bag and put that under there. Look, it's generating nothing and that's exactly what you'd expect. That's what these

**Dave Jones:** antistatic bags are designed to do. They're not designed to build up a charge at all, no matter how you handle them. Here's another pink one. I'm rubbing them together like this and we can't generate anything at all. These These are doing exactly

**Dave Jones:** what they're supposed to do. They're antistatic. How about a drawer of resistors? One of these non-antistatic drawers in non-antistatic bags and of course they're not really going to kill the resistors in there, but if you put that under there it generates these hundreds

**Dave Jones:** of volts. So, probably the last thing you want to do is throw your chips directly in one of these non-antistatic drawers. In fact, the good quality component drawers, they will be made of a conductive plastic. So, what happens

**Dave Jones:** when we get our little spark generator here and we do some stuff under it? There we go, 11 kilovolts. 14 kilovolts and that's actually charge building up on the surface of the plate in there. So, that will actually stay

**Dave Jones:** there now and build up and this one only goes to 20 kilovolts maximum. There you go. It's overloaded. So, what happens when we stick our static generator inside one of these pink the funnel pink ESD bag? Well, let's

**Dave Jones:** give it a go. Bang, overloaded. There you go. We just zapped straight through this pink ESD bag. Not a problem at all. Not surprising. So, let's now try one of these static shielding bags. Let's put it inside here and see if we can

**Dave Jones:** generate the same charge. Now, I've got to be careful not to touch the bottom plate here cuz I can actually, if I do that with the bag, just the bag on its own can actually induce voltage. You're not actually supposed to touch that

**Dave Jones:** plate. So, we'll reset that. Okay, I'll try and it's inside the bag. I'll try and get it as close as possible to the sensor. And there you go. It's not generating That's only a couple of millimeters away from the sensor plate and it's

**Dave Jones:** generating no charge at all cuz nothing is escaping that bag and it's doesn't matter whether it's from inside out or from outside in. You put your devices in here, they're fully protected. And if you're wondering about that antistatic tube, well, it's

**Dave Jones:** not going to do anything either. Let's It's going to work exactly like the pink ESD bag. Bang. There we go. 4 and 1/2 5,000 volts, not a problem. Now, here's an interesting one. I've got the Digilent chip kit MAX3240

**Dave Jones:** in here and let's take a look at it. What does it come with in the packaging? There's this foam on the bottom of it. Doesn't look like ESD foam to me. It's not the pink stuff. It's not conductive. Looks like regular

**Dave Jones:** foam. Let's try it out, shall we? Remove this. Look at that. Couple hundred volts right there. Look, that's nasty. I can generate in the order of Look, kilovolts. It was going up to kilovolts there. That's rather nasty stuff when you don't

**Dave Jones:** use proper ESD material. Now, granted, a a fully populated board like this is pretty robust. So, the odds of killing it are very small, but still that is not proper ESD protection at all. Crazy. Look at that, 4 kilovolts.

**Dave Jones:** And let's try that same thing if you got proper conductive foam. Not a problem whatsoever. Generates nothing. And there you go. Yes, it is actually conductive. About 5K. And again with one of these little embed platforms, it comes on.

**Dave Jones:** Ta-da, pink antistatic foam. And let's play around with this to our heart's content. Rub the pins, do whatever, play around. Not a problem whatsoever. You get this horrible non-antistatic foam stuff. Look at that. Thousands of volts. So, although these

**Dave Jones:** static shielding bags will protect any device you put inside, it's only if all of the objects, including the tubes, all the foam material inside is antistatic as well or static dissipative. If you put one of these, this horrible-looking

**Dave Jones:** thing inside that can generate thousands of volts, if you stick that inside there with your devices, you're screwed. All right, so enough of that. How about we actually try and kill a chip? Well, I've got a 4000 series CMOS device here

**Dave Jones:** and an MC 14569, and I've got it just flashing an LED to show that it actually works. So, what we'll do is we'll start a baseline. I switch it off. We've got a working chip. Let's take it out. I'll just

**Dave Jones:** get rid of that for a second, and let's try and kill it, shall we? This is pretty nasty stuff for a 4000 series CMOS device. So, this is a real baseline test. This is directly on the chip itself.

**Dave Jones:** And let's put it back. Just as a reference to see if we can actually kill one of these things. And yep, there you go. Bingo. Dead. So, we were able to kill it. So, we've got a baseline. Let's see if we can do that

**Dave Jones:** through various antistatic uh protection devices. So, let's actually give this a go. I'm going to switch off the power there, take the chip out. Going to put it in a antistatic tube. And let's see if we can kill it.

**Dave Jones:** Generate away. Woo, it's going over the top surface there. Ooh, that's interesting. Check this out. Whoa, look on the scope here. Two higher voltages is being applied to the waveform generator B and C. Oops. Anyway, let's take it back down and

**Dave Jones:** let's uh take that out. Hope I didn't kill my uh function gen. But it at least knows. And what? There you go. Well, I don't know. We might have killed our function gen. Let me uh No, there we go. The waveform gen's on.

**Dave Jones:** No, we couldn't kill it. Going to have to try harder. So, what we've got is our working circuit. Switch it off. Take out the chip and I'll put it inside one of these pink ESD bags. Now, because we're dealing with

**Dave Jones:** a surface in addition to the air here, it it's these bags do actually provide a modicum tiny amount of protection just because they're not direct contact and so I'll fold it over like that and that'll give us a better path

**Dave Jones:** to try and get our spark to jump through the bag, which is what we want, not over the surface. Like if I put it like that, you'll probably see it jump over the surface like that. There we go.

**Dave Jones:** We don't want that. We want to go through. We want to ah, I saw it jump through the bag then. Didn't jump over, it jumped well and truly through that bag. Which of course is the whole point. Oh, it's supposed to be able to

**Dave Jones:** do this. But it's going to be harder to destroy this device than it was just when we were doing direct contact or very close to it in free air. There we go. Haha. We killed it. We got it to die through one of these pink ESD

**Dave Jones:** bags. It was more difficult than it was just in free air. That's because it does actually provide some barrier. If we had a proper ESD gun, we would find it it would probably go straight through this really easily, but it took a little bit

**Dave Jones:** of work there to actually get it to finally kill the device, but we did. So there you go. I'm going to call that myth busted. These pink ESD bags and the one the funnel one came in, they do not

**Dave Jones:** provide protection for your devices. They provide a little tiny amount just for the fact that they're um actually you know, an extra distance away and they're not an air gap, but that's that's all. They're not designed for ESD

**Dave Jones:** protection at all. They just won't build up a charge on the surface. And I hope we've proven that today. Would have been better if we had an ESD gun. Um we couldn't kill one within a tube because the distances in there are greater and

**Dave Jones:** the wall is thicker. If we had a proper ESD gun, I have little doubt that we would have eventually been able to kill a device directly through one of these ESD tubes as well. And I won't bore you

**Dave Jones:** with the details, but no, I could not kill anything inside one of these static shielding bags. And no surprise, that's what they're designed to handle. They've been tested to do that. So, once you put your devices in there, they're fully

**Dave Jones:** protected. Myth busted. Catch you next time.
