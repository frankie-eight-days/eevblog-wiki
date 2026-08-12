---
video_id: wi-b9k-0KfE
title: EEVblog #388 - Fake Apple USB Charger Teardown
url: https://www.youtube.com/watch?v=wi-b9k-0KfE
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes, I'm finally getting around to tearing down these Apple or supposedly um Apple USB chargers. Universal uh mains input, you know, 110 to uh 240 volts at 5 watts output. So, they're quite remarkable devices for their size. And

**Dave Jones:** um I forgive me, I forget who actually uh sent these in to me. So, thank you very much. They sent them in to the mailbag segment some time back. And we have two types here. We have the one on

**Dave Jones:** the uh right here, which is a Check it out. Power Adapt-Ear, made in China. So, it's the model number A 1265. And the one on the uh left here is supposedly the genuine one designed by Apple in California. And you'll

**Dave Jones:** notice the differences. This one is UL listed Underwriters Laboratory. This one doesn't have any uh UL marking at all, though it says it's a listed power supply. And uh this one, of course, has a serial number, but I doubt that's even different between

**Dave Jones:** units. They're probably all the same. Just to make it look like it's, you know, uh sort of you know, legitimate. But um I cannot guarantee that this one is a genuine one by Apple. I was not assured that it is a genuine Apple, so we could

**Dave Jones:** be in for a surprise. But as I said before, this one I expect this one here to be a steaming pile of dog turd. I expect this one to be downright dangerous and badly designed inside, built for the absolute lowest cost. And

**Dave Jones:** if this one is a genuine Apple one, and we'll find out, it should be much better quality, design, and construction, and much safer if it is genuinely UL tested. Only one way to find out. Don't turn them on. Take them apart. And first cab

**Dave Jones:** off the rank here, we have the imitation adapter and uh I've already levered that off a bit. It didn't take much at all. So, let's take it out and uh have a look inside this thing. Looks like it just

**Dave Jones:** slides out as one complete assembly. Yes, it does. It looks like it's a two-board solution and uh uh There ain't much in that at all. We'll look at this in a bit more detail, I'm sure, but that is absolutely

**Dave Jones:** atrocious. I don't even see a full wave rectifier on the input there and uh nothing on the other uh on the secondary side. Single optocoupler there. Opto I think this one is a steaming pile of dog turd. We'll go into that bit more

**Dave Jones:** detail, but let's crack open this genuine Apple one and I cannot seem to lever this one open at all. And that tells you right there that uh this one is already better designed and constructed than the other one, which

**Dave Jones:** practically fell apart in my hands almost. Um so, I jeez, I might even have to get the Dremel out for this one.

**Dave Jones:** Crack this sucker open here. Aha, similar two-board construction there, but uh yeah, I don't think I was going to get that probably heat sealed. I wasn't going to get that open in a hurry, but uh hopefully, it should just yeah, just

**Dave Jones:** pulls out. Ah. Nah, little Is it a little bit different? Is it better? Let's have a look. Ah, not much. Nope. Afraid not. I think we've been had, folks. Yeah, this doesn't look not look like a genuine Apple one to me.

**Dave Jones:** So, there you have it, folks. We have the obvious one hung low cheapy on the right here and the not so obvious one hung low cheapy on the left. At least the cloners on the left here decided to

**Dave Jones:** clone the whole thing and actually put, you know, designed by Apple and you know, actually on there. Made it look like the real deal. The one on the right here is, you know, they didn't even bother. It was clear, even though it was

**Dave Jones:** the same model number, it was fairly clear that it wasn't a genuine Apple device. But, we have been had. This one looks practically identical to the one hung low cheapy. Now, I've actually looked online and I've seen a teardown of a genuine Apple

**Dave Jones:** charger, the same one as this, and it's nothing like this. It's much more complicated, much better designed than this thing. This is about as bare-bones a design as you can possibly get. And we'll reverse engineer this and have a look at the

**Dave Jones:** circuit as well. But, man, everything's wrong with this thing. I don't know where to start. Now, the major differences seem to be just a slight slightly different layout on this primary side board down here. I mean, we've got the,

**Dave Jones:** virtually identical transformer here. I'm pretty sure it's almost identical circuitry between the two, but the obvious fake one has two TO-92 packages, whereas the other one only has a single TO-92, but it's got on the bottom here, if you

**Dave Jones:** turn it over, it's got a sock 23 package on there, whereas this one doesn't. And the the Apple branded one has a couple of my I think two or three more passive parts than the uh one hung low cheapy on this

**Dave Jones:** side. So, geesh. Uh where do we start here? Well, there is no X or Y class uh rated filter cap in this thing at all. Then, we don't even have a full wave bridge rectifier. We've just got a piss ant halfway rectifier

**Dave Jones:** there with a 1N probably a 1N4001. We've got a crap Chong X brand cap. I wouldn't trust that thing as far as I could throw it. 105° C, blow it out your ass. And the Apple branded one has the same

**Dave Jones:** Chong X, I think it is, uh 105° C 400 V rated electrolytic in there. Wouldn't trust that thing any further than I could shove it up the designer's ass. Next up, check out the creepage distance we've got on this thing. Okay? Here's,

**Dave Jones:** let's say, the negative input side going directly to the electrolytic cap there. And here's the positive input here going through the diode, jumps over to here. Single um single diode rectification, not bridge rectifier. And to the other side of the cap here. And there, look.

**Dave Jones:** Look at the creepage distance in there. What is that? It's nothing. It's absolutely nothing. You're kidding me. And not only do they have it there as well, but it also goes around on the other side here. You've got to be

**Dave Jones:** killing me kidding me. That's like barely a millimeter. And then up here, they do the same thing around this surface mount resistor. You've got to be kidding me. The creepage distance is just awful. Right there, straight off the bat, we're

**Dave Jones:** not going to pass any safety standard or a type approval standard on the planet. Now, let's have a look at the creepage distance between primary and secondary of the transformer, which is effectively these two pins here on this ribbon

**Dave Jones:** cable. There's the gap down in there. It's a bit better than over here, but jeez. And then it comes through this ribbon cable over to this secondary board here, and check out that. There's nothing in there. You've got to be kidding me. And of

**Dave Jones:** course, there's no talking of isolation slots on this thing either. Forget it. I mean, here's the optocoupler. Okay, they've got a reasonable distance between the primary and the secondary side of the optocoupler here, but look, it's instantly ruined by that gap there.

**Dave Jones:** Unbelievable. And I don't think I'm even going to bother to unwind that switching transformer there, cuz it's going to be an absolute shocker inside in terms of clearance as well. And one thing you won't find on this design is any fuse

**Dave Jones:** protection at all. No fusible resistors, no thermistors, no resettable fuses, nothing. And also, you won't find any inductive filtering either. There are no Well, apart from the transformer a switching transformer itself, there are no inductors on this thing at all. And

**Dave Jones:** there's no insulation tape or anything in terms of uh clearance when you, you know, whack these two boards together. So, I'm not going to go into the complexities of you know, all of that, but yeah, there's just no insulation

**Dave Jones:** tape whatsoever. Probably no thought put into that. Well, there's no thought put into this whole thing at all, except how cheap can we produce this steaming pile of dog turd? And the exposed metal USB shield here, check this out, right? Here

**Dave Jones:** is the tab for the USB shield. This is the primary side. These two pins with these traces going around here is the primary side of the transformer. Are you kidding me? Look at the creepage in there. Look at

**Dave Jones:** the creepage distance. Man, this thing is a bloody death trap. Now, interestingly, the Apple branded one does actually seem to have had, look, some thought put in to where the creepage paths are. They've marked them in here with the silk

**Dave Jones:** screen. It's around here like this, around here. They've got one in there, and that also extends down to the shield on on the secondary side of the board, cuz here's the two primary connections down in here. We're primary side primary side

**Dave Jones:** connections, which go down to the optocoupler, which go over here, and that in there, once again, the silk screen marks the creepage path in there or the creepage paths that matter. By the way, a couple of people have

**Dave Jones:** actually asked me to clarify creepage and clearance, because I use both terms. Creepage is actually across the board like that. So, creepage is the correct term to use going from pin to pin like that, because it like you can

**Dave Jones:** say like it creeps across the surface of the board. So, that's creepage. When you're talking about, oh, you know, creepage inside that ribbon cable, for example, technically, it's not correct to say the clearance, because clearance is air-to-air clearance. So, if you've

**Dave Jones:** got if you fold this board over like that, then it is the correct term to say clearance between there and there because it is a physical air gap. And a clearance is the correct term if you have a high voltage slot routed into the

**Dave Jones:** PCB, for example. We don't have any example of that on this product, of course, cuz this is a steaming pile of dog turd. But, there you go. That is the difference between creepage and clearance. And of course, just because this Apple branded one

**Dave Jones:** actually has these silk screens on here and does seem to be a little bit better designed and has slightly larger creepage distances than the One Hung Lo branded one, it is still not good enough and is still not

**Dave Jones:** going to meet any safety approval or type standard on the planet. And on the primary side here, it doesn't appear that we have any uh snubbers at all. And you'll note the lack of any filter cap between primary and secondary

**Dave Jones:** of the switching transformer here. And of course, that would be a proper uh Y-class rated safety cap. But, not none of that. Bugger that. That costs money. Now, curiously, I measured out the uh two primary windings on the transformers

**Dave Jones:** here. And this is the Apple branded one. This is the cheap one. And the cheap one has a coil here, primary coil here, and a second primary coil on these two pins. But, the what looks like exactly the

**Dave Jones:** same physical uh transformer on the Apple branded one, this one is not between these two pins. It's actually this pin and that one down there is one coil. And those two pins there are another one. So, there's actually a big

**Dave Jones:** difference in the transformer there in terms of pinout. You'll notice that the Apple branded charger has a 1 kV ceramic here. Looks like 470 picofarads between the primary and secondary of the transformer. You can tell by the white

**Dave Jones:** silk screen there which indicates the primary and secondary barrier there. And of course, that is supposed to be a Y class rated safety cap to meet any sort of type approval. They just used a crappy 1 kV ceramic there. Not good enough. But

**Dave Jones:** hey, at least that's better than this one over here which doesn't have any cap at all between primary and secondary. Well, I've done a quick reverse engineering to this. Hopefully, I've got it right and here's the basic circuit

**Dave Jones:** for it. It's a Dave CAD drawing of course and this is the Apple branded charger which of course is a clone. And it speaks for itself. It's pretty bloody simplistic. There's no main controller I see at all. It's an absolute shocker. But this

**Dave Jones:** non-Apple branded one is even worse. It doesn't even contain a MOSFET. It's just a cheap ass 2 W class B output transistor and SS8050. You got to be kidding me. And the other transistor in there is a TV chroma

**Dave Jones:** KSE13001. It's like uh what can we get which transistors can we get this week at the local Shenzhen market? Just whack them in there. Got to be kidding me. So at least this Apple branded one is a little bit better than

**Dave Jones:** the other one in that it uses a proper MOSFET transistor in here a 1N60. It's a little bit better. At least it's got a suppression cap between primary and secondary. But once again, there is no fuses, no um inductive uh inputs and output

**Dave Jones:** filtering, nothing, no snubbers, no you know, no full wave bridge rectification. The clearances are absolutely horrible and the creepage distances are ah ah. So, what I'll do is I'll link in a blog post of somebody who's reverse engineered a genuine Apple charger and

**Dave Jones:** the circuitry is completely different and much better uh designed and well laid out, uses Y-class uh safety caps and you know, it's got uh fuses in it and snubbers and inductors and everything's done, you know, pretty right and they've done uh

**Dave Jones:** wonders to put it in there, but unfortunately, um the one we got was not a genuine Apple one. It It says, you know, it was certainly said it was Apple, but nah. Cheap-ass clone. So, I hope you enjoyed that teardown

**Dave Jones:** there. Sorry it wasn't a genuine Apple one. What a bummer. But anyway, if you want to discuss it, jump on over to the EEVblog forum cuz that's where everyone hangs out and don't forget to give it a big thumbs-up cuz that helps a lot. And

**Dave Jones:** of course, there is only one place for these steaming piles of dog turd. Catch you next time.
