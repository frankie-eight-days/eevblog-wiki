---
video_id: TSwohZSjSdg
title: EEVblog #1329 - Magnetic Field Shielding DEMONSTRATED
url: https://www.youtube.com/watch?v=TSwohZSjSdg
source: youtube-asr
timestamps: {"0": 0, "1": 24, "2": 38, "3": 52, "4": 63, "5": 75, "6": 88, "7": 108, "8": 123, "9": 142, "10": 164, "11": 177, "12": 187, "13": 210, "14": 229, "15": 247, "16": 262, "17": 281, "18": 298, "19": 319, "20": 345, "21": 356, "22": 371, "23": 383, "24": 397, "25": 410, "26": 424, "27": 431, "28": 444, "29": 460, "30": 476, "31": 500, "32": 513, "33": 529, "34": 541, "35": 554, "36": 574, "37": 582, "38": 599, "39": 615, "40": 627, "41": 639, "42": 656, "43": 664, "44": 675}
---

**Dave Jones:** Hi, just a quick and interesting follow-up video here to my one where I measured the noise of the micro current with the OPA189 op amp using my HP dynamic signal analyzer using the power spectral density to get the microvolts per root hertz noise from zero to 100 kilohertz here and I thought I'd just show you an interesting aspect to do with shielding.

**Dave Jones:** Now, I've got the micro current inside here. It's got the OPA189 op amp. We're measuring the noise from zero to oh well, 256 hertz up to 1 kilohertz here because it's only got 400 points so you can't go to exactly zero at the start.

**Dave Jones:** Anyway, look, we're getting some interesting little spikes in there. I've got 100 averages on and I've got the cursor right there and you'll notice that it's actually around about 25 kilohertz there for this spike.

**Dave Jones:** What is this spike here? Aha, is that the switching frequency because the OPA189 is a chopper amplifier? No, well, as I explained in the previous video, that's way off.

**Dave Jones:** It's up in like the 200 to 300 kilohertz region up here which is beyond the measurement capability of this dynamic signal analyzer. It's only this is only designed for DC to 100 kilohertz.

**Dave Jones:** So, what is this 25 kilohertz spike here? And look, there's two other spikes here and if I go over, got to use the fast mode cuz it's otherwise it's going through 400 points.

**Dave Jones:** Aha, 50 kilohertz and what's this one over here? Well, you guessed it, 75 kilohertz. So, 25, 50, and 75 kilohertz. Aha, these might be some you know, sub modulation frequency of the of the switching frequency of the op amp.

**Dave Jones:** But no, that's not it. Watch what happens if we let's actually start that measurement again, but let's actually remove the lid. Ta-da! Look, they're going up-doodly-da. Look at that.

**Dave Jones:** A significant difference. So, it's not fundamentally the switching frequency of the chopper amplifier, the auto zero amplifier here. So, what is this? Aha, for those playing along at home, you might have guessed old school CRT, cathode ray ray oscilloscope.

**Dave Jones:** These are electromagnetic devices. They have big thumpin' coils in them which generate large magnetic fields, and a common switching frequency happens to be 25 kHz. So, that's actually what we're measuring here is the switching frequency of the CRT oscilloscope here.

**Dave Jones:** So, I don't mean switching, it's the horizontal scan rate of the CRT here. And by taking off the top lid on here, we're easily seeing that spikes, and I won't actually physically take it out and all that, and we could get higher, it doesn't matter.

**Dave Jones:** But, you know, if we put the lid on, let's start that again. There we go. If we put the lid on, it's going down, but it's not going to go down to zero.

**Dave Jones:** And this has to do with an excellent video I've done, if I may so may say myself. I don't have the original, but this is just a This is just a tribute to number 1273, linked in down below at the end, if you haven't seen it, where I explain near field versus far field EM C, and how there are both, H field, which is a magnetic field, and

**Dave Jones:** the E field, which is the electric field, and this is distance from the source in terms of wavelength of the frequency. And when you're what's called near field, when your device is physically near to your source like this, the electric fields and the magnetic fields actually differ.

**Dave Jones:** They actually separate like this. It's only when you get uh basically a wavelength pi on two distance away, do they start to combine to form the EM field or the electromagnetic radiation that you're more familiar with.

**Dave Jones:** The electric and magnetic fields combine in the far field, i.e. further away you go, to give you an electromagnetic field and that's what you used to with, you know, like RF shielding and all that sort of stuff is you're talking typically far field shielding.

**Dave Jones:** But when you're very close like this to a magnetic source, in this case, we're going to get the electric as, you know, from various things around, as well as the magnetic uh field coming from the CRT, which is, you know, behind there.

**Dave Jones:** It's like a, you know, a foot away or something. I don't know how deep this CRT is, but it's pretty darn close and we're able to pick up the magnetic field even through the shielded box and even when I have the input grounded like this, so it's gone to mains earth ground.

**Dave Jones:** So, this box is completely shielded, right? It but it's a diecast alloy box and uh both copper and aluminum and diecast alloys like this aren't particularly good at shielding down at, you know, DC to low frequencies in terms of what's called the near field.

**Dave Jones:** They can shield electric electric fields, but they can't shield magnetic fields. The magnetic fields well, they're not perfectly goes through, but they they attenuate a little bit, but they will they can penetrate completely shielded boxes like this and, you know, typically as a rule of thumb, you might say copper is, you know, pretty much only good for kind of like, you know, the kilohertz range and above.

**Dave Jones:** Anything sort of like below that is going to uh like anything, you know, really low frequency stuff below say, you know, roughly a kilohertz or so is not going to be shielded by copper.

**Dave Jones:** So, you can have a completely, you know, completely welded copper or aluminum box that's completely shielded, but magnetic fields will still get through. So, let's actually do a little experiment here.

**Dave Jones:** I've got because this is 25 kilohertz, this is actually quite, you know, relatively high frequency, copper should actually work. So, what I've got here is I've got a large copper clad.

**Dave Jones:** It's the old school This is a positive photo resistor coating. That's why it looks green. Hasn't been exposed, but you know, big 1 oz copper sheet like this, we should at 25 kilohertz, we should see this actually go away.

**Dave Jones:** So, it will start that again. Actually, let's take the lid off. And then we'll Sorry, you won't be able to see it, but well, I'll put that in there like that.

**Dave Jones:** Let's start. And let's wait a bit. And we'll be able to see that this copper sheet's probably going to do the business. Whereas the aluminum the die cast box, let's let's have a look.

**Dave Jones:** Ready? Take it away. It might It's still averaging. Well, it's still there. You can still see it. And when I took it away, it was quite low, but it was still there.

**Dave Jones:** So, having that one big copper sheet there was actually better than than the die cast box here. And if we use both, we'll probably find that it goes away.

**Dave Jones:** We can pretty much make make that go away completely. I know this is not the best example. If this was down like, you know, 100 hertz or something magnetic field, this copper sheet pretty much wouldn't do it it attenuate a little bit of it, pretty much wouldn't do jack all.

**Dave Jones:** So, yeah, let's There we go. Yep. Yep. It's basically completely gone and you'll see it start moving up again there. And let's actually try to do this same thing with a an aluminum sheet like this.

**Dave Jones:** Just add some more. Although aluminum's not perfect, but we'll pretty much see that go away, I suspect. Yeah, pretty much pretty much goneski. But you'll notice that although the copper clad worked reasonably well, if I just put some copper perf board like that, wow, that's not That's not doing too terrific, is it?

**Dave Jones:** It's uh you know, once again, it's it's the copper, but it's not a continuous sheet and it's not a large uh sheet. So, the magnetic fields uh getting through that no problems whatsoever.

**Dave Jones:** And if we put the aluminum lid through like that, no, that's not going to do the business. You really need to really need to mostly shield that. So, it can drop down, but it's not going to be perfect.

**Dave Jones:** And you'll notice that that sheet is not on its own without the lid is not going to do much. It has has attenuated it a little bit. See? It goes back up.

**Dave Jones:** But you need the combination. You need to really play whack-a-mole here. Don't know if you can No, you can't see that. But I can see the I can just see the waveforms through there.

**Dave Jones:** There we go. And she's goneski and she's back. So, to really get down to the lower uh shielding lower frequency stuff like, you know, down in hundreds of hertz, you know, the sub-kilohertz range right down to DC, you need you need to start getting um what's called a high permeability uh steel.

**Dave Jones:** So, you need like a mu metal, that's called. There's, you know, specific like brands and types of mu metal. They have a high permeability, so they don't saturate as much.

**Dave Jones:** And, you know, pretty much like a steel will do the job, but a low-carbon steel would do better than a high-carbon steel, for example, because the saturation point is higher, so it can, you know, absorb more of that magnetic field before it saturates.

**Dave Jones:** And then, well, it can't, you know, do the job anymore. And shield that. So, if we put a steel sheet between these, let's try that. I don't know what type of I just got this from one of my instruments.

**Dave Jones:** So, let's give it a whirl. And we should find that steel should work pretty damn well, especially at 25 kHz with no shielding on the top of the box there.

**Dave Jones:** And tada, completely gone. And she goes back up. Look at that. Beautiful. That's the high permeability of steel. It's doing the business on the H field. So, there you go.

**Dave Jones:** I just thought that is a interesting little example of how we can pick that up. And of course, if we move this away, if we move it away, we'll probably find that it's not going to pick it up any not going to pick it up as well anymore.

**Dave Jones:** There you go. It's only when we get closer, closer, closer. Unfortunately, you got to sort of like restart the averaging cuz it's it's too noisy if I don't have the averaging on.

**Dave Jones:** But, yeah, we can get closer, and there you go. Just really goes to town there. So, there you go. Hope you found that interesting, useful. If you did, please give it a big thumbs up.

**Dave Jones:** Catch you next time. Mhm.
