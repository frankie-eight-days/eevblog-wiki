---
video_id: SrDfRCi1UV0
title: EEVblog #716 - Raspberry Pi 2 Xenon Flash Problem Explained
url: https://www.youtube.com/watch?v=SrDfRCi1UV0
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 31, "3": 48, "4": 62, "5": 79, "6": 95, "7": 112, "8": 131, "9": 147, "10": 158, "11": 170, "12": 179, "13": 203, "14": 213, "15": 234, "16": 250, "17": 261, "18": 275, "19": 289, "20": 300, "21": 311, "22": 326, "23": 345, "24": 357, "25": 369, "26": 386, "27": 397, "28": 413, "29": 424, "30": 436, "31": 456, "32": 468, "33": 476, "34": 493, "35": 509, "36": 522, "37": 532, "38": 551, "39": 573, "40": 588, "41": 605, "42": 619, "43": 627, "44": 648, "45": 660, "46": 669, "47": 682, "48": 695, "49": 705, "50": 717, "51": 739, "52": 750, "53": 764, "54": 776, "55": 791, "56": 805, "57": 821, "58": 838, "59": 849, "60": 864, "61": 880, "62": 894, "63": 909, "64": 926, "65": 940, "66": 957, "67": 964, "68": 976, "69": 1001, "70": 1012, "71": 1026, "72": 1037, "73": 1049, "74": 1062, "75": 1072, "76": 1085, "77": 1099, "78": 1113, "79": 1128, "80": 1146, "81": 1164, "82": 1173, "83": 1192}
---

**Dave Jones:** Hi, this is the new Raspberry Pi 2, just released very recently and a user by the name of Peter Onion discovered something very interesting with this board. Let's take a photo of this lovely little board with a camera with a xenon photo flash on it.

**Dave Jones:** Here we go. Oops, look what happened. We have just reset, not only reset our board, but we've um actually locked it up. It is no longer working at all.

**Dave Jones:** To get it working again, we have to re-power the thing. What's going on? Well, it's actually pretty darn obvious. Now, when this thing was first reported, of course, it spread like wildfire on all the forums and blogs and everywhere else, including the EEVblog forum.

**Dave Jones:** Everyone's going, "Oh, what's going on? This mysterious effect." But, hey, anyone who's been in the electronics industry a long time would instantly have seen this like I did and just went, "Oh, yeah, that's the photoelectric effect.

**Dave Jones:** Something on there is photosensitive to the xenon flash." No worries, happens all the time. And when I say happens all the time, well, it's actually not that common, but it's been a very well-known effect for a long time that light, as I'll explain in a minute, can affect semiconductors.

**Dave Jones:** And normally, it's not an issue because semiconductors like the main Broadcom chipset here, for example, and the main ethernet chipset down in here and all the other little black blobs you can see on there, they're plastic encapsulated or ceramic encapsulated or whatever.

**Dave Jones:** And of course, the photons of light can't get through to affect any of the semiconductors inside there. So, it obviously wasn't that. And people, you know, just did trial and error, looked around, and they finally found the culprit.

**Dave Jones:** Right down here. And bingo, there's is culprit there, that tiny little chip there, U16. You can see it in comparison to an 0402 capacitor there. It's absolutely tiny. And anyone who with any electronics packaging experience knows that is a chip scale package, which I'll talk about in a minute.

**Dave Jones:** And aha, of course, that sucker is going to be photosensitive because it's effectively a bare die flipped on its front side. So, what we've got here is what's called a wafer level chip scale package, CSP.

**Dave Jones:** And what it is is basically a bare semiconductor die with the balls directly on the bottom. And you can see the balls under there like this. And this is different to the balls on a regular BGA device, for example.

**Dave Jones:** They are plastic encapsulated or ceramic encapsulated chips. This is not. This is merely a bare die on there like that with just little metal balls on the bottom and flipped over.

**Dave Jones:** So, essentially the wafer of this uh chip here is actually exposed on the bottom. If we actually flip that over, you'd be able to see the circuitry on the back.

**Dave Jones:** And this is how the light is able to get in. It's able to sneak in under those balls in there and actually affect the semiconductor junctions in there, the PN junctions, and hence cause the thing to latch up, do something silly, give an impulse in the wrong part of the circuit, whatever is actually functionality-wise is causing this switch-mode power supply chip to lock up.

**Dave Jones:** So, what's happening here is basic quantum physics. You should have learned this in physics 101. You're no doubt familiar with the Planck relationship relationship. Energy equals Planck's constant times the frequency.

**Dave Jones:** Now, Albert Einstein in 1905 wrote a paper that explained some results of this and how that previously of course we thought that light was a wave, but he proposed is light was actually a packet of bunch of photons.

**Dave Jones:** So, when the photons hit a metallic material like this, it actually emits electrons like that because based on the Planck formula. So, that that's knowing now as the Planck-Einstein formula, Planck-Einstein relationship.

**Dave Jones:** And not only does it work with just basic metal surfaces like this, you've got energy in these photons, they hit, and they release and emit electrons. Well, it it's not just like a sheet of metal just sitting there.

**Dave Jones:** It's also going to happen with a semiconductor PN junctions, i.e., your transistors and your diodes and everything else that modern electronics and everything on this Raspberry Pi board is made with.

**Dave Jones:** It's all going to somehow emit some amount of electrons if any sort of photo if any amount of photon hits it based on that relationship. And it's based on the frequency, which I'll talk about in a minute.

**Dave Jones:** And you can uh demonstrate this in a vacuum tube, for example, if you've got the cathode down here and the anode up here, photons come in, then electrons leave the plate, and you can actually get a current flow around there.

**Dave Jones:** And the same thing happens in your PN junction here. If you expose it to light as what we're doing up here with this switch mode converter, then electrons can actually flow around the circuit.

**Dave Jones:** And that can completely screw up the chip depending on how much photon energy is actually coming in here and at what part of the circuit and how the circuit works and all that sort of stuff, but it can certainly and in this case we've demonstrated it does affect it.

**Dave Jones:** Now, here's something that's often not well known. Albert Einstein actually won his Nobel Prize in Physics for the photoelectric effect, exactly what's happening here. He did not win it for the more famous theory of relativity because that was still sort of a bit debated by the time it came around.

**Dave Jones:** So, he actually won it for this photoelectric effect, which of course was the start of both him and Planck. This was effectively the start of quantum fit the theory of quantum physics as we know it today.

**Dave Jones:** Now, it's actually not just a weird side effect of affecting chips that are exposed like this chip scale package we've got here. This is principle is fundamental to all the sensors that we have these days.

**Dave Jones:** The camera that you're using, the camera I'm shooting this with now is not possible if it wasn't for the photoelectric effect. Photons actually strike the semiconductor sensor inside the camera and generate a current and that can be measured and turned in to the image that you're seeing now.

**Dave Jones:** The infrared receiver you got on your TV, the remote control, all that sort of stuff. Solar cells, for example, they work based on the photoelectric effect and a whole bunch of other stuff.

**Dave Jones:** So, it really is a fundamental physical phenomenon, fundamental principle of physics and electronics 101. So, that's why something like this, that semiconductor junctions are affected by light is is nothing new to electronics people.

**Dave Jones:** It's a very well-known phenomenon. And we can actually demonstrate exactly what's happening here. I've got a standard 5 mm LED here. I think it's a yellow one. Doesn't matter about the color.

**Dave Jones:** And I've got it hooked up to my triplet analog multimeter here in current mode. So, it's 60 microamps full scale deflection here. And then I'll get my camera. This flash, here we go.

**Dave Jones:** Let's hook it up. Let's flash this and see that? See the needle jump there? That is the photoelectric effect in action. It's converting the photons from this xenon arc flash here into the PN junction of this LED and it actually generates a current.

**Dave Jones:** Not a huge amount, but you can see that it actually does have an effect. And in a modern, uh, IC like we have on this Raspberry, uh, Pi, it might have a lots of high impedance, uh, nodes on the inside.

**Dave Jones:** Well, that amount of current can be a real big deal, and that's what's causing that chip to latch up. And here's a metal can transistor, which you no doubt used to.

**Dave Jones:** It's a 2N2222A, and I've cut the top off that, and you can probably see the die inside there with the two bonding wires jumping over to it. That tiny little blob in there, that is the little, uh, transistor die, and the wires go over to there.

**Dave Jones:** I've hooked it up to a breadboard. Now, we've exposed this thing to light, let's see what happens. Okay, here we go. See that? Jumped up. It's doing exactly the same thing on that, uh, PN junction inside the transistor.

**Dave Jones:** And of course, all your modern ICs in here, they're all just physical PN junctions and transistors, exactly what's inside there. Oh, that's That's nice and sharp cutting that thing open.

**Dave Jones:** Ooh, and no wonder this thing is locking up. When you expose the PN junction in there to all this photon energy coming from that, uh, xenon flash, it's really going to ruin your day.

**Dave Jones:** Now, I mentioned before it's all determined upon the actual frequency here, not necessarily the amplitude. That's why, uh, some people on the forums who've been investigating this, they've been shining like, I think, like 1,800 lm onto the chip, and you can't make it do it, because it's not necessarily about the amplitude, it's the frequency.

**Dave Jones:** And here is a typical xenon arc spectrum in nanometers, the wavelength. And the visible spectrum, of course, around about 390 to, uh, 780 nanometers or thereabouts. That's the visible spectrum, so it's generating, you know, the bulk of the energy within that visible wavelength, but look at these massive spikes up here in the near infrared.

**Dave Jones:** So, it's possibly the near infrared stuff here that's really giving uh, a kick into the chip and whatever is causing that there. So, you know, it's not necessarily about just shining light into it.

**Dave Jones:** Has to be a specific frequency. No electrons will be emitted from this metal surface unless it hits a specific frequency. And that spectrum from the xenon arc lamp is why it's able to work in this particular case and that's why people have had no luck with their phone flashes like this.

**Dave Jones:** Look. See, no problem whatsoever cuz it's just regular ambient light. All of the energy is contained down here and I suspect what's happening is up in the near infrared or something like that.

**Dave Jones:** That's what we're getting the huge not only does it have the frequency but it has the energy up in that range as well. So, I suspect that's what's happening.

**Dave Jones:** And the actual chip used in here to switch my power supply converter, it's actually an on semiconductor NCP6343. Unfortunately, there's not a public data sheet for it but yeah, like even if you had the data sheet, you're probably only just guessing what aspect of the circuit is actually latching up and doing that sort of stuff.

**Dave Jones:** But you know, it's your regular switch mode buck power supply converter so it's a step down converter typical topology but it does have you know, a fair amount of circuitry in there to enable that.

**Dave Jones:** So, it could be any aspect of that. You'd have to go back to on semiconductor themselves and they'd have to do extensive experiments to figure out what's going on here.

**Dave Jones:** So, if anyone thinks they know, it's just a guess. So, you might think okay, what happens if we shoot say a laser onto here? Well, I've got the little you know, half a milliwatt laser pointer or whatever it is.

**Dave Jones:** Yeah, it's no well, less than 1 milliwatt. So, it's just your typical laser pointer here and well, I can't get that to do anything regardless of what angle I shoot it at or anything like that.

**Dave Jones:** I can't get a damn sausage. Look at that. So, that's rock solid, but it's certainly a possibility cuz we don't know the exact wavelength that's actually causing this thing.

**Dave Jones:** So, it will be a specific frequency, of course, amplitude, of course, plays a role, too. You can't just, you know, hit it with, you know, bugger all energy and just because it's the right frequency, it's going to upset it.

**Dave Jones:** No, it has to be a specific energy and a specific frequency in the spectrum in order to generate what's called photocurrent. And when you actually get a current flow through a PN junction or a circuit or solar cell or whatever it is, that's actually called a photon current cuz it's converting the photon into a current in your circuit.

**Dave Jones:** So, how can they fix the problem of this little chip? Well, it's very simple. There's two ways to do it. Either you use another chip that is not a chip scale package, i.e., an exposed die.

**Dave Jones:** So, you use like a BGA part or something like that. That'll be just fine, just like this BGA part is just fine. No light's going to sneak under there and get onto that Broadcom um arm processor die in there.

**Dave Jones:** It's just not going to happen because it is fully encapsulated. It's only on that tiny little beast down in there, the chip scale package. So, you can either change the package, which probably means that, you know, a totally different chip.

**Dave Jones:** You have to change the layout, the pinout, all that sort of thing, perhaps. Or as is very common with chip-on-board COB technology in the industry, which uses bare dies directly on the board, like generally facing up, they'll actually put them facing up and then little bond wires going over.

**Dave Jones:** They have a machine that actually just bonds the wires directly from the chip onto the pad. And that's how, you know, really low-cost, super low-cost greeting cards, for example, might work.

**Dave Jones:** All those sort of, you know, throw away products that cost, you know, a cent or something like that for the circuitry. That's how they get them. If using chip-on-board technology, and then they encapsulate it, rather than the bare die, to protect it all, and also to shield it from light as well.

**Dave Jones:** They gunk it with an epoxy, a big black epoxy. So, if you've ever seen a big black blob on a board, that's chip-on-board technology. And they could come along, it's probably their factory that assembles this, probably has that they just have a machine which comes over, you know, a human usually does it.

**Dave Jones:** They just bring it over and go gunk, you know, like a big syringe-type thing just comes over and just gunks it all in big black goo, like that, and it sets, and Bob's your uncle.

**Dave Jones:** All right, so let's see if we can probe and capture something here when we actually do this. So, I've got my scope probe connected across the 1.2 V output of U16, that's the switch-mode power supply under question here, and there we go, there's our nice 1.2 V 500 mV per division, everything's hunky-dory.

**Dave Jones:** Let's It's all working, and trust me, it's on the screen there, so let's hook it up and flush it. Bingo, captured. Look at that, we've got some sort of transients actually triggered when it's going back up.

**Dave Jones:** So, it's obviously dropped here, there's something happened right back over here. Let's have a look. You can see a tiny little impulse there. That's It's not going up by much, and that's So, if we zoom right into that, we've got the capture memory to do that.

**Dave Jones:** There's It's really nothing doing there, because we've got our big antenna earthly connected up to this. We're not actually probing it properly. You got to This is where you got to be careful, could be a trap for young players when you're trying to measure this sort of thing.

**Dave Jones:** When you've got this ground lead connected like that, you've got a nice and big turn there, which can pick up any electromagnetic pulse generated by that xenon arc flash in there, all the current flowing, can easily couple into that and uh you know cause that sort of spike.

**Dave Jones:** So, I don't think that's actually what's uh causing the thing what's genuinely there. I think that's actually being picked up by the probe, but you can see that your regulators obviously dropping out and then it's coming back into regulation like that.

**Dave Jones:** But, it So, it still works. So, the switch-mode power supply is recovering. That chip is recovering just fine. It's the Raspberry Pi processor or whatever else Well, there's only a processor in there really that has locked up and uh causing it to do it.

**Dave Jones:** So, it's not the switch-mode power supply controller itself. I think that's recovering just fine and dandy. Let's see if we can AC couple that. Okay, our Raspberry Pi is running.

**Dave Jones:** We're AC coupled this. We're now down at uh 20 mV per division. Let's flash it. Ta-da! You can see that big impulse in there. No, look at that. No, it's still fine.

**Dave Jones:** So, you can see it's just fine. There it is. Even though our screen is blank, our processor is locked up, everything else, that switch-mode is is just fine. So, it's not entirely the fault of the switch-mode controller chip that's causing that, but it's certainly uh something to do with the arm uh processor, the Broadcom processor that's not allowing it to gracefully restart after that uh uh the the big dip we saw

**Dave Jones:** in the power rail. So, just to make sure this is actually genuinely the output and not some sort of uh current induced in the scope probe uh itself, which I believe that high-frequency content there is.

**Dave Jones:** So, I've scaled this up. We're now on 200 mV per division. We can see the dip a lot better there. But, this is by just by the shape of it and the recovery like that, it looks like it is the switch-mode uh controller actually doing that, recovering and then ramping up and leveling back out there.

**Dave Jones:** But, hey, let's uh just prove that by putting some Blu Tack over the chip, i.e. uh masking out the light, doing the flash again, see if we can get any trigger.

**Dave Jones:** Okay, so I've restarted the thing. I put a big blob of Blu Tack over that. That should keep out the light from the sides and around the chip, and let's flash it.

**Dave Jones:** Trigger again. Oh, no, we still get it. Look at that. And no, I didn't get the light out enough. Geez, it's sensitive. Well, it seems like my Blu Tack's not up to snuff.

**Dave Jones:** I had to put a hell of a lot more on there before I could get it so it's not sensitive. So, now if we single shot trigger, of course, there we go.

**Dave Jones:** It's We did get that impulse there. That's interesting, actually. Check it out. So, we got that impulse as I suspected, that is due to the electromagnetic pickup by the coil.

**Dave Jones:** That's why it's all high-frequency stuff, but we do get a little little bip little blip like that, positive going up. Once again, that's at a much, much lower frequency, so that's that's rather interesting.

**Dave Jones:** So, there is still a bit of a hiccup in that supply. There's one thing I do want to check, and that's its reverse side dependency. No. So, we got that same thing happening there.

**Dave Jones:** So, yeah, I think that's Yeah, that's no problem whatsoever. Anyway, we've proved that the huge dip that we saw there was actually the uh a dropping out of the switch-mode regulator and then recovering and restarting.

**Dave Jones:** So, that's pretty well proven. And I saw that somebody actually referred to this as the Mogwai effect, and well, all you youngsters out there who've never seen Gremlins, you won't know what we're talking about, but it's kind of funny, but not really accurate because it's not sunlight that does this.

**Dave Jones:** It's a specific high-frequency uh xenon arc flash that does it. Ah, well. Eh, nice turn, though. Three. No, no. What happened? He hates bright light. And yes, that is awful Blu Tack I've got.

**Dave Jones:** Ugh, I don't know how long I've had that sitting around, but ah, man, I'll never get all that off. So, there you go. I hope you found that interesting.

**Dave Jones:** There's nothing unusual happening here at all. But, if you haven't seen or heard about the photoelectric uh effect, or even if you had, but you didn't know it applied to uh basic electronics and PN junctions and everything else in today's modern electronics, then, well, you've learned something new.

**Dave Jones:** Catch you next time.
