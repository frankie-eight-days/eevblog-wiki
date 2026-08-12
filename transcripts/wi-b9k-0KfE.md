---
video_id: wi-b9k-0KfE
title: EEVblog #388 - Fake Apple USB Charger Teardown
url: https://www.youtube.com/watch?v=wi-b9k-0KfE
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 29, "3": 45, "4": 56, "5": 70, "6": 82, "7": 92, "8": 116, "9": 128, "10": 139, "11": 157, "12": 174, "13": 195, "14": 219, "15": 233, "16": 250, "17": 271, "18": 284, "19": 301, "20": 314, "21": 327, "22": 353, "23": 369, "24": 380, "25": 393, "26": 406, "27": 423, "28": 433, "29": 450, "30": 462, "31": 482, "32": 490, "33": 501, "34": 527, "35": 544, "36": 562, "37": 580, "38": 600, "39": 620, "40": 637, "41": 649, "42": 676, "43": 687, "44": 699, "45": 715, "46": 744, "47": 757, "48": 777, "49": 788, "50": 800, "51": 814, "52": 833, "53": 849, "54": 862, "55": 876, "56": 895, "57": 915, "58": 934, "59": 962, "60": 975, "61": 990}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. Yes, I'm finally getting around to tearing down these Apple or supposedly um Apple USB chargers. Universal uh mains input, you know, 110 to uh 240 volts at 5 watts output.

**Dave Jones:** So, they're quite remarkable devices for their size. And um I forgive me, I forget who actually uh sent these in to me. So, thank you very much. They sent them in to the mailbag segment some time back.

**Dave Jones:** And we have two types here. We have the one on the uh right here, which is a Check it out. Power Adapt-Ear, made in China. So, it's the model number A 1265.

**Dave Jones:** And the one on the uh left here is supposedly the genuine one designed by Apple in California. And you'll notice the differences. This one is UL listed Underwriters Laboratory.

**Dave Jones:** This one doesn't have any uh UL marking at all, though it says it's a listed power supply. And uh this one, of course, has a serial number, but I doubt that's even different between units.

**Dave Jones:** They're probably all the same. Just to make it look like it's, you know, uh sort of you know, legitimate. But um I cannot guarantee that this one is a genuine one by Apple.

**Dave Jones:** I was not assured that it is a genuine Apple, so we could be in for a surprise. But as I said before, this one I expect this one here to be a steaming pile of dog turd.

**Dave Jones:** I expect this one to be downright dangerous and badly designed inside, built for the absolute lowest cost. And if this one is a genuine Apple one, and we'll find out, it should be much better quality, design, and construction, and much safer if it is genuinely UL tested.

**Dave Jones:** Only one way to find out. Don't turn them on. Take them apart. And first cab off the rank here, we have the imitation adapter and uh I've already levered that off a bit.

**Dave Jones:** It didn't take much at all. So, let's take it out and uh have a look inside this thing. Looks like it just slides out as one complete assembly. Yes, it does.

**Dave Jones:** It looks like it's a two-board solution and uh uh There ain't much in that at all. We'll look at this in a bit more detail, I'm sure, but that is absolutely atrocious.

**Dave Jones:** I don't even see a full wave rectifier on the input there and uh nothing on the other uh on the secondary side. Single optocoupler there. Opto I think this one is a steaming pile of dog turd.

**Dave Jones:** We'll go into that bit more detail, but let's crack open this genuine Apple one and I cannot seem to lever this one open at all. And that tells you right there that uh this one is already better designed and constructed than the other one, which practically fell apart in my hands almost.

**Dave Jones:** Um so, I jeez, I might even have to get the Dremel out for this one. Crack this sucker open here. Aha, similar two-board construction there, but uh yeah, I don't think I was going to get that probably heat sealed.

**Dave Jones:** I wasn't going to get that open in a hurry, but uh hopefully, it should just yeah, just pulls out. Ah. Nah, little Is it a little bit different? Is it better?

**Dave Jones:** Let's have a look. Ah, not much. Nope. Afraid not. I think we've been had, folks. Yeah, this doesn't look not look like a genuine Apple one to me. So, there you have it, folks.

**Dave Jones:** We have the obvious one hung low cheapy on the right here and the not so obvious one hung low cheapy on the left. At least the cloners on the left here decided to clone the whole thing and actually put, you know, designed by Apple and you know, actually on there.

**Dave Jones:** Made it look like the real deal. The one on the right here is, you know, they didn't even bother. It was clear, even though it was the same model number, it was fairly clear that it wasn't a genuine Apple device.

**Dave Jones:** But, we have been had. This one looks practically identical to the one hung low cheapy. Now, I've actually looked online and I've seen a teardown of a genuine Apple charger, the same one as this, and it's nothing like this.

**Dave Jones:** It's much more complicated, much better designed than this thing. This is about as bare-bones a design as you can possibly get. And we'll reverse engineer this and have a look at the circuit as well.

**Dave Jones:** But, man, everything's wrong with this thing. I don't know where to start. Now, the major differences seem to be just a slight slightly different layout on this primary side board down here.

**Dave Jones:** I mean, we've got the, virtually identical transformer here. I'm pretty sure it's almost identical circuitry between the two, but the obvious fake one has two TO-92 packages, whereas the other one only has a single TO-92, but it's got on the bottom here, if you turn it over, it's got a sock 23 package on there, whereas this one doesn't.

**Dave Jones:** And the the Apple branded one has a couple of my I think two or three more passive parts than the uh one hung low cheapy on this side. So, geesh.

**Dave Jones:** Uh where do we start here? Well, there is no X or Y class uh rated filter cap in this thing at all. Then, we don't even have a full wave bridge rectifier.

**Dave Jones:** We've just got a piss ant halfway rectifier there with a 1N probably a 1N4001. We've got a crap Chong X brand cap. I wouldn't trust that thing as far as I could throw it.

**Dave Jones:** 105° C, blow it out your ass. And the Apple branded one has the same Chong X, I think it is, uh 105° C 400 V rated electrolytic in there.

**Dave Jones:** Wouldn't trust that thing any further than I could shove it up the designer's ass. Next up, check out the creepage distance we've got on this thing. Okay? Here's, let's say, the negative input side going directly to the electrolytic cap there.

**Dave Jones:** And here's the positive input here going through the diode, jumps over to here. Single um single diode rectification, not bridge rectifier. And to the other side of the cap here.

**Dave Jones:** And there, look. Look at the creepage distance in there. What is that? It's nothing. It's absolutely nothing. You're kidding me. And not only do they have it there as well, but it also goes around on the other side here.

**Dave Jones:** You've got to be killing me kidding me. That's like barely a millimeter. And then up here, they do the same thing around this surface mount resistor. You've got to be kidding me.

**Dave Jones:** The creepage distance is just awful. Right there, straight off the bat, we're not going to pass any safety standard or a type approval standard on the planet. Now, let's have a look at the creepage distance between primary and secondary of the transformer, which is effectively these two pins here on this ribbon cable.

**Dave Jones:** There's the gap down in there. It's a bit better than over here, but jeez. And then it comes through this ribbon cable over to this secondary board here, and check out that.

**Dave Jones:** There's nothing in there. You've got to be kidding me. And of course, there's no talking of isolation slots on this thing either. Forget it. I mean, here's the optocoupler.

**Dave Jones:** Okay, they've got a reasonable distance between the primary and the secondary side of the optocoupler here, but look, it's instantly ruined by that gap there. Unbelievable. And I don't think I'm even going to bother to unwind that switching transformer there, cuz it's going to be an absolute shocker inside in terms of clearance as well.

**Dave Jones:** And one thing you won't find on this design is any fuse protection at all. No fusible resistors, no thermistors, no resettable fuses, nothing. And also, you won't find any inductive filtering either.

**Dave Jones:** There are no Well, apart from the transformer a switching transformer itself, there are no inductors on this thing at all. And there's no insulation tape or anything in terms of uh clearance when you, you know, whack these two boards together.

**Dave Jones:** So, I'm not going to go into the complexities of you know, all of that, but yeah, there's just no insulation tape whatsoever. Probably no thought put into that. Well, there's no thought put into this whole thing at all, except how cheap can we produce this steaming pile of dog turd?

**Dave Jones:** And the exposed metal USB shield here, check this out, right? Here is the tab for the USB shield. This is the primary side. These two pins with these traces going around here is the primary side of the transformer.

**Dave Jones:** Are you kidding me? Look at the creepage in there. Look at the creepage distance. Man, this thing is a bloody death trap. Now, interestingly, the Apple branded one does actually seem to have had, look, some thought put in to where the creepage paths are.

**Dave Jones:** They've marked them in here with the silk screen. It's around here like this, around here. They've got one in there, and that also extends down to the shield on on the secondary side of the board, cuz here's the two primary connections down in here.

**Dave Jones:** We're primary side primary side connections, which go down to the optocoupler, which go over here, and that in there, once again, the silk screen marks the creepage path in there or the creepage paths that matter.

**Dave Jones:** By the way, a couple of people have actually asked me to clarify creepage and clearance, because I use both terms. Creepage is actually across the board like that. So, creepage is the correct term to use going from pin to pin like that, because it like you can say like it creeps across the surface of the board.

**Dave Jones:** So, that's creepage. When you're talking about, oh, you know, creepage inside that ribbon cable, for example, technically, it's not correct to say the clearance, because clearance is air-to-air clearance.

**Dave Jones:** So, if you've got if you fold this board over like that, then it is the correct term to say clearance between there and there because it is a physical air gap.

**Dave Jones:** And a clearance is the correct term if you have a high voltage slot routed into the PCB, for example. We don't have any example of that on this product, of course, cuz this is a steaming pile of dog turd.

**Dave Jones:** But, there you go. That is the difference between creepage and clearance. And of course, just because this Apple branded one actually has these silk screens on here and does seem to be a little bit better designed and has slightly larger creepage distances than the One Hung Lo branded one, it is still not good enough and is still not going to meet any safety approval or type standard on the planet.

**Dave Jones:** And on the primary side here, it doesn't appear that we have any uh snubbers at all. And you'll note the lack of any filter cap between primary and secondary of the switching transformer here.

**Dave Jones:** And of course, that would be a proper uh Y-class rated safety cap. But, not none of that. Bugger that. That costs money. Now, curiously, I measured out the uh two primary windings on the transformers here.

**Dave Jones:** And this is the Apple branded one. This is the cheap one. And the cheap one has a coil here, primary coil here, and a second primary coil on these two pins.

**Dave Jones:** But, the what looks like exactly the same physical uh transformer on the Apple branded one, this one is not between these two pins. It's actually this pin and that one down there is one coil.

**Dave Jones:** And those two pins there are another one. So, there's actually a big difference in the transformer there in terms of pinout. You'll notice that the Apple branded charger has a 1 kV ceramic here.

**Dave Jones:** Looks like 470 picofarads between the primary and secondary of the transformer. You can tell by the white silk screen there which indicates the primary and secondary barrier there. And of course, that is supposed to be a Y class rated safety cap to meet any sort of type approval.

**Dave Jones:** They just used a crappy 1 kV ceramic there. Not good enough. But hey, at least that's better than this one over here which doesn't have any cap at all between primary and secondary.

**Dave Jones:** Well, I've done a quick reverse engineering to this. Hopefully, I've got it right and here's the basic circuit for it. It's a Dave CAD drawing of course and this is the Apple branded charger which of course is a clone.

**Dave Jones:** And it speaks for itself. It's pretty bloody simplistic. There's no main controller I see at all. It's an absolute shocker. But this non-Apple branded one is even worse. It doesn't even contain a MOSFET.

**Dave Jones:** It's just a cheap ass 2 W class B output transistor and SS8050. You got to be kidding me. And the other transistor in there is a TV chroma KSE13001.

**Dave Jones:** It's like uh what can we get which transistors can we get this week at the local Shenzhen market? Just whack them in there. Got to be kidding me. So at least this Apple branded one is a little bit better than the other one in that it uses a proper MOSFET transistor in here a 1N60.

**Dave Jones:** It's a little bit better. At least it's got a suppression cap between primary and secondary. But once again, there is no fuses, no um inductive uh inputs and output filtering, nothing, no snubbers, no you know, no full wave bridge rectification.

**Dave Jones:** The clearances are absolutely horrible and the creepage distances are ah ah. So, what I'll do is I'll link in a blog post of somebody who's reverse engineered a genuine Apple charger and the circuitry is completely different and much better uh designed and well laid out, uses Y-class uh safety caps and you know, it's got uh fuses in it and snubbers and inductors and everything's done, you know, pretty right and they've done uh

**Dave Jones:** wonders to put it in there, but unfortunately, um the one we got was not a genuine Apple one. It It says, you know, it was certainly said it was Apple, but nah.

**Dave Jones:** Cheap-ass clone. So, I hope you enjoyed that teardown there. Sorry it wasn't a genuine Apple one. What a bummer. But anyway, if you want to discuss it, jump on over to the EEVblog forum cuz that's where everyone hangs out and don't forget to give it a big thumbs-up cuz that helps a lot.

**Dave Jones:** And of course, there is only one place for these steaming piles of dog turd. Catch you next time.
