---
video_id: SrDfRCi1UV0
title: EEVblog #716 - Raspberry Pi 2 Xenon Flash Problem Explained
url: https://www.youtube.com/watch?v=SrDfRCi1UV0
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 35, "3": 50, "4": 67, "5": 81, "6": 98, "7": 115, "8": 134, "9": 150, "10": 166, "11": 179, "12": 193, "13": 206, "14": 227, "15": 245, "16": 261, "17": 277, "18": 292, "19": 304, "20": 319, "21": 330, "22": 345, "23": 359, "24": 373, "25": 388, "26": 403, "27": 422, "28": 436, "29": 453, "30": 468, "31": 482, "32": 497, "33": 514, "34": 530, "35": 545, "36": 558, "37": 573, "38": 590, "39": 605, "40": 621, "41": 632, "42": 648, "43": 663, "44": 675, "45": 689, "46": 705, "47": 717, "48": 732, "49": 746, "50": 760, "51": 774, "52": 786, "53": 799, "54": 815, "55": 828, "56": 841, "57": 854, "58": 869, "59": 885, "60": 899, "61": 909, "62": 924, "63": 938, "64": 955, "65": 966, "66": 980, "67": 995, "68": 1010, "69": 1023, "70": 1035, "71": 1049, "72": 1065, "73": 1079, "74": 1099, "75": 1115, "76": 1132, "77": 1148, "78": 1167, "79": 1182}
---

**Dave Jones:** Hi, this is the new Raspberry Pi 2, just released very recently and a user by the name of Peter Onion discovered something very interesting with this board. Let's take a photo of this lovely little board with a camera with a xenon photo flash

**Dave Jones:** on it. Here we go. Oops, look what happened. We have just reset, not only reset our board, but we've um actually locked it up. It is no longer working at all. To get it working again, we have to

**Dave Jones:** re-power the thing. What's going on? Well, it's actually pretty darn obvious. Now, when this thing was first reported, of course, it spread like wildfire on all the forums and blogs and everywhere else, including the EEVblog forum. Everyone's going,

**Dave Jones:** "Oh, what's going on? This mysterious effect." But, hey, anyone who's been in the electronics industry a long time would instantly have seen this like I did and just went, "Oh, yeah, that's the photoelectric effect. Something on there is photosensitive to the xenon flash."

**Dave Jones:** No worries, happens all the time. And when I say happens all the time, well, it's actually not that common, but it's been a very well-known effect for a long time that light, as I'll explain in a minute, can affect semiconductors. And

**Dave Jones:** normally, it's not an issue because semiconductors like the main Broadcom chipset here, for example, and the main ethernet chipset down in here and all the other little black blobs you can see on there, they're plastic encapsulated or ceramic encapsulated or whatever. And

**Dave Jones:** of course, the photons of light can't get through to affect any of the semiconductors inside there. So, it obviously wasn't that. And people, you know, just did trial and error, looked around, and they finally found the culprit. Right down here. And bingo, there's is

**Dave Jones:** culprit there, that tiny little chip there, U16. You can see it in comparison to an 0402 capacitor there. It's absolutely tiny. And anyone who with any electronics packaging experience knows that is a chip scale package, which I'll talk about in a minute. And aha, of

**Dave Jones:** course, that sucker is going to be photosensitive because it's effectively a bare die flipped on its front side. So, what we've got here is what's called a wafer level chip scale package, CSP. And what it is is basically a bare

**Dave Jones:** semiconductor die with the balls directly on the bottom. And you can see the balls under there like this. And this is different to the balls on a regular BGA device, for example. They are plastic encapsulated or ceramic encapsulated chips. This is not. This is

**Dave Jones:** merely a bare die on there like that with just little metal balls on the bottom and flipped over. So, essentially the wafer of this uh chip here is actually exposed on the bottom. If we actually flip that over, you'd be able

**Dave Jones:** to see the circuitry on the back. And this is how the light is able to get in. It's able to sneak in under those balls in there and actually affect the semiconductor junctions in there, the PN junctions, and hence cause the thing to

**Dave Jones:** latch up, do something silly, give an impulse in the wrong part of the circuit, whatever is actually functionality-wise is causing this switch-mode power supply chip to lock up. So, what's happening here is basic quantum physics. You should have learned

**Dave Jones:** this in physics 101. You're no doubt familiar with the Planck relationship relationship. Energy equals Planck's constant times the frequency. Now, Albert Einstein in 1905 wrote a paper that explained some results of this and how that previously of course we thought that light was a

**Dave Jones:** wave, but he proposed is light was actually a packet of bunch of photons. So, when the photons hit a metallic material like this, it actually emits electrons like that because based on the Planck formula. So, that that's knowing now as the

**Dave Jones:** Planck-Einstein formula, Planck-Einstein relationship. And not only does it work with just basic metal surfaces like this, you've got energy in these photons, they hit, and they release and emit electrons. Well, it it's not just like a sheet of

**Dave Jones:** metal just sitting there. It's also going to happen with a semiconductor PN junctions, i.e., your transistors and your diodes and everything else that modern electronics and everything on this Raspberry Pi board is made with. It's all going to

**Dave Jones:** somehow emit some amount of electrons if any sort of photo if any amount of photon hits it based on that relationship. And it's based on the frequency, which I'll talk about in a minute. And you can uh demonstrate this

**Dave Jones:** in a vacuum tube, for example, if you've got the cathode down here and the anode up here, photons come in, then electrons leave the plate, and you can actually get a current flow around there. And the same thing happens in your PN junction

**Dave Jones:** here. If you expose it to light as what we're doing up here with this switch mode converter, then electrons can actually flow around the circuit. And that can completely screw up the chip depending on how much photon energy is

**Dave Jones:** actually coming in here and at what part of the circuit and how the circuit works and all that sort of stuff, but it can certainly and in this case we've demonstrated it does affect it. Now, here's something that's often not well

**Dave Jones:** known. Albert Einstein actually won his Nobel Prize in Physics for the photoelectric effect, exactly what's happening here. He did not win it for the more famous theory of relativity because that was still sort of a bit debated by the time it came

**Dave Jones:** around. So, he actually won it for this photoelectric effect, which of course was the start of both him and Planck. This was effectively the start of quantum fit the theory of quantum physics as we know it today. Now, it's

**Dave Jones:** actually not just a weird side effect of affecting chips that are exposed like this chip scale package we've got here. This is principle is fundamental to all the sensors that we have these days. The camera that you're using, the camera I'm

**Dave Jones:** shooting this with now is not possible if it wasn't for the photoelectric effect. Photons actually strike the semiconductor sensor inside the camera and generate a current and that can be measured and turned in to the image that you're seeing now. The infrared receiver

**Dave Jones:** you got on your TV, the remote control, all that sort of stuff. Solar cells, for example, they work based on the photoelectric effect and a whole bunch of other stuff. So, it really is a fundamental physical phenomenon, fundamental

**Dave Jones:** principle of physics and electronics 101. So, that's why something like this, that semiconductor junctions are affected by light is is nothing new to electronics people. It's a very well-known phenomenon. And we can actually demonstrate exactly what's happening here. I've got a standard 5 mm

**Dave Jones:** LED here. I think it's a yellow one. Doesn't matter about the color. And I've got it hooked up to my triplet analog multimeter here in current mode. So, it's 60 microamps full scale deflection here. And then I'll get my camera. This

**Dave Jones:** flash, here we go. Let's hook it up. Let's flash this and see that? See the needle jump there? That is the photoelectric effect in action. It's converting the photons from this xenon arc flash here into the PN junction of

**Dave Jones:** this LED and it actually generates a current. Not a huge amount, but you can see that it actually does have an effect. And in a modern, uh, IC like we have on this Raspberry, uh, Pi, it might have a lots of high impedance, uh, nodes

**Dave Jones:** on the inside. Well, that amount of current can be a real big deal, and that's what's causing that chip to latch up. And here's a metal can transistor, which you no doubt used to. It's a 2N2222A, and I've cut the top off that, and you

**Dave Jones:** can probably see the die inside there with the two bonding wires jumping over to it. That tiny little blob in there, that is the little, uh, transistor die, and the wires go over to there. I've hooked it up to a breadboard. Now, we've

**Dave Jones:** exposed this thing to light, let's see what happens. Okay, here we go. See that? Jumped up. It's doing exactly the same thing on that, uh, PN junction inside the transistor. And of course, all your modern ICs in here, they're all just

**Dave Jones:** physical PN junctions and transistors, exactly what's inside there. Oh, that's That's nice and sharp cutting that thing open. Ooh, and no wonder this thing is locking up. When you expose the PN junction in there to all this photon energy coming

**Dave Jones:** from that, uh, xenon flash, it's really going to ruin your day. Now, I mentioned before it's all determined upon the actual frequency here, not necessarily the amplitude. That's why, uh, some people on the forums who've been investigating this, they've been shining

**Dave Jones:** like, I think, like 1,800 lm onto the chip, and you can't make it do it, because it's not necessarily about the amplitude, it's the frequency. And here is a typical xenon arc spectrum in nanometers, the wavelength. And the

**Dave Jones:** visible spectrum, of course, around about 390 to, uh, 780 nanometers or thereabouts. That's the visible spectrum, so it's generating, you know, the bulk of the energy within that visible wavelength, but look at these massive spikes up here in the near

**Dave Jones:** infrared. So, it's possibly the near infrared stuff here that's really giving uh, a kick into the chip and whatever is causing that there. So, you know, it's not necessarily about just shining light into it. Has to be a specific frequency.

**Dave Jones:** No electrons will be emitted from this metal surface unless it hits a specific frequency. And that spectrum from the xenon arc lamp is why it's able to work in this particular case and that's why people have had no luck with their phone

**Dave Jones:** flashes like this. Look. See, no problem whatsoever cuz it's just regular ambient light. All of the energy is contained down here and I suspect what's happening is up in the near infrared or something like that. That's what we're getting the

**Dave Jones:** huge not only does it have the frequency but it has the energy up in that range as well. So, I suspect that's what's happening. And the actual chip used in here to switch my power supply converter, it's actually an on

**Dave Jones:** semiconductor NCP6343. Unfortunately, there's not a public data sheet for it but yeah, like even if you had the data sheet, you're probably only just guessing what aspect of the circuit is actually latching up and doing that sort of

**Dave Jones:** stuff. But you know, it's your regular switch mode buck power supply converter so it's a step down converter typical topology but it does have you know, a fair amount of circuitry in there to enable that. So, it could be any aspect

**Dave Jones:** of that. You'd have to go back to on semiconductor themselves and they'd have to do extensive experiments to figure out what's going on here. So, if anyone thinks they know, it's just a guess. So, you might think okay, what happens if we

**Dave Jones:** shoot say a laser onto here? Well, I've got the little you know, half a milliwatt laser pointer or whatever it is. Yeah, it's no well, less than 1 milliwatt. So, it's just your typical laser pointer here and well, I can't get

**Dave Jones:** that to do anything regardless of what angle I shoot it at or anything like that. I can't get a damn sausage. Look at that. So, that's rock solid, but it's certainly a possibility cuz we don't know the exact wavelength that's

**Dave Jones:** actually causing this thing. So, it will be a specific frequency, of course, amplitude, of course, plays a role, too. You can't just, you know, hit it with, you know, bugger all energy and just because it's the right frequency, it's

**Dave Jones:** going to upset it. No, it has to be a specific energy and a specific frequency in the spectrum in order to generate what's called photocurrent. And when you actually get a current flow through a PN junction or a circuit or solar cell or

**Dave Jones:** whatever it is, that's actually called a photon current cuz it's converting the photon into a current in your circuit. So, how can they fix the problem of this little chip? Well, it's very simple. There's two ways to do it. Either you

**Dave Jones:** use another chip that is not a chip scale package, i.e., an exposed die. So, you use like a BGA part or something like that. That'll be just fine, just like this BGA part is just fine. No light's going to sneak under there and

**Dave Jones:** get onto that Broadcom um arm processor die in there. It's just not going to happen because it is fully encapsulated. It's only on that tiny little beast down in there, the chip scale package. So, you can either change the package, which

**Dave Jones:** probably means that, you know, a totally different chip. You have to change the layout, the pinout, all that sort of thing, perhaps. Or as is very common with chip-on-board COB technology in the industry, which uses bare dies directly

**Dave Jones:** on the board, like generally facing up, they'll actually put them facing up and then little bond wires going over. They have a machine that actually just bonds the wires directly from the chip onto the pad. And that's how, you know,

**Dave Jones:** really low-cost, super low-cost greeting cards, for example, might work. All those sort of, you know, throw away products that cost, you know, a cent or something like that for the circuitry. That's how they get them. If using chip-on-board technology, and

**Dave Jones:** then they encapsulate it, rather than the bare die, to protect it all, and also to shield it from light as well. They gunk it with an epoxy, a big black epoxy. So, if you've ever seen a big black blob on a board, that's

**Dave Jones:** chip-on-board technology. And they could come along, it's probably their factory that assembles this, probably has that they just have a machine which comes over, you know, a human usually does it. They just bring it over and go gunk, you know, like a big

**Dave Jones:** syringe-type thing just comes over and just gunks it all in big black goo, like that, and it sets, and Bob's your uncle. All right, so let's see if we can probe and capture something here when we actually do this. So, I've got my scope

**Dave Jones:** probe connected across the 1.2 V output of U16, that's the switch-mode power supply under question here, and there we go, there's our nice 1.2 V 500 mV per division, everything's hunky-dory. Let's It's all working, and trust me, it's

**Dave Jones:** on the screen there, so let's hook it up and flush it. Bingo, captured. Look at that, we've got some sort of transients actually triggered when it's going back up. So, it's obviously dropped here, there's something happened right back over here.

**Dave Jones:** Let's have a look. You can see a tiny little impulse there. That's It's not going up by much, and that's So, if we zoom right into that, we've got the capture memory to do that. There's It's really nothing doing there, because

**Dave Jones:** we've got our big antenna earthly connected up to this. We're not actually probing it properly. You got to This is where you got to be careful, could be a trap for young players when you're trying to measure this sort of thing.

**Dave Jones:** When you've got this ground lead connected like that, you've got a nice and big turn there, which can pick up any electromagnetic pulse generated by that xenon arc flash in there, all the current flowing, can easily couple into

**Dave Jones:** that and uh you know cause that sort of spike. So, I don't think that's actually what's uh causing the thing what's genuinely there. I think that's actually being picked up by the probe, but you can see that your regulators obviously dropping

**Dave Jones:** out and then it's coming back into regulation like that. But, it So, it still works. So, the switch-mode power supply is recovering. That chip is recovering just fine. It's the Raspberry Pi processor or whatever else Well, there's only a processor in there really

**Dave Jones:** that has locked up and uh causing it to do it. So, it's not the switch-mode power supply controller itself. I think that's recovering just fine and dandy. Let's see if we can AC couple that. Okay, our Raspberry Pi is running. We're

**Dave Jones:** AC coupled this. We're now down at uh 20 mV per division. Let's flash it. Ta-da! You can see that big impulse in there. No, look at that. No, it's still fine. So, you can see it's just fine. There it is. Even though our screen is

**Dave Jones:** blank, our processor is locked up, everything else, that switch-mode is is just fine. So, it's not entirely the fault of the switch-mode controller chip that's causing that, but it's certainly uh something to do with the arm uh processor, the Broadcom processor that's

**Dave Jones:** not allowing it to gracefully restart after that uh uh the the big dip we saw in the power rail. So, just to make sure this is actually genuinely the output and not some sort of uh current induced in the scope probe uh itself, which I

**Dave Jones:** believe that high-frequency content there is. So, I've scaled this up. We're now on 200 mV per division. We can see the dip a lot better there. But, this is by just by the shape of it and the recovery like that, it looks like it is

**Dave Jones:** the switch-mode uh controller actually doing that, recovering and then ramping up and leveling back out there. But, hey, let's uh just prove that by putting some Blu Tack over the chip, i.e. uh masking out the light, doing the flash

**Dave Jones:** again, see if we can get any trigger. Okay, so I've restarted the thing. I put a big blob of Blu Tack over that. That should keep out the light from the sides and around the chip, and let's flash it.

**Dave Jones:** Trigger again. Oh, no, we still get it. Look at that. And no, I didn't get the light out enough. Geez, it's sensitive. Well, it seems like my Blu Tack's not up to snuff. I had to put a hell of a lot more

**Dave Jones:** on there before I could get it so it's not sensitive. So, now if we single shot trigger, of course, there we go. It's We did get that impulse there. That's interesting, actually. Check it out. So, we got that

**Dave Jones:** impulse as I suspected, that is due to the electromagnetic pickup by the coil. That's why it's all high-frequency stuff, but we do get a little little bip little blip like that, positive going up. Once again, that's at a much, much lower frequency, so that's

**Dave Jones:** that's rather interesting. So, there is still a bit of a hiccup in that supply. There's one thing I do want to check, and that's its reverse side dependency. No. So, we got that same thing happening there. So, yeah, I think

**Dave Jones:** that's Yeah, that's no problem whatsoever. Anyway, we've proved that the huge dip that we saw there was actually the uh a dropping out of the switch-mode regulator and then recovering and restarting. So, that's pretty well proven. And I saw that

**Dave Jones:** somebody actually referred to this as the Mogwai effect, and well, all you youngsters out there who've never seen Gremlins, you won't know what we're talking about, but it's kind of funny, but not really accurate because it's not sunlight that does this. It's a specific

**Dave Jones:** high-frequency uh xenon arc flash that does it. Ah, well. Eh, nice turn, though. Three. No, no. What happened? He hates bright light. And yes, that is awful Blu Tack I've got. Ugh, I don't know how long I've had that

**Dave Jones:** sitting around, but ah, man, I'll never get all that off. So, there you go. I hope you found that interesting. There's nothing unusual happening here at all. But, if you haven't seen or heard about the photoelectric uh effect, or even if you

**Dave Jones:** had, but you didn't know it applied to uh basic electronics and PN junctions and everything else in today's modern electronics, then, well, you've learned something new. Catch you next time.
