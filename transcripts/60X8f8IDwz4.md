---
video_id: 60X8f8IDwz4
title: EEVblog #405 - Lecroy 9384C Oscilloscope Repair - Part 3
url: https://www.youtube.com/watch?v=60X8f8IDwz4
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 25, "3": 33, "4": 44, "5": 57, "6": 70, "7": 87, "8": 106, "9": 129, "10": 149, "11": 157, "12": 175, "13": 204, "14": 217, "15": 233, "16": 244, "17": 261, "18": 273, "19": 297, "20": 308, "21": 319, "22": 328, "23": 346, "24": 361, "25": 379, "26": 394, "27": 406, "28": 421, "29": 439, "30": 463, "31": 478, "32": 492, "33": 514, "34": 542, "35": 563, "36": 573, "37": 588, "38": 603, "39": 618, "40": 631, "41": 655, "42": 664, "43": 695, "44": 721, "45": 732, "46": 741, "47": 755, "48": 782, "49": 793, "50": 819, "51": 831, "52": 846, "53": 859, "54": 877, "55": 885, "56": 898, "57": 907, "58": 925, "59": 934, "60": 944, "61": 955}
---

**Dave Jones:** Hi. Yes, it's the LeCroy 9384C oscilloscope repair again because people just could not let this one go. Um if you haven't seen the previous videos, please do. Otherwise, this uh won't make much sense to you.

**Dave Jones:** I'll link them in down below. Now, people wanted me to power this thing up even though it still has that short on the 3.3 V rail and see if it works.

**Dave Jones:** Well, okay, fair enough. Here we go. I'm about to power the thing up. I've got my um uh power supply around the back here for the 3.3 V rail.

**Dave Jones:** My leads aren't long enough, so um yeah, sorry about that. You can't see it, but it's set to 3.3 V and it'll be drawing about 10 or 11 amps.

**Dave Jones:** And there it is down in there. I've got that connected down into the 3.3 V rail with the alligator clip there, and I'm going to power the rest from the main power supply.

**Dave Jones:** So, let's power this sucker up and see what happens to it. Here we go. I'm going to try and do it try and power up the rails at the same time.

**Dave Jones:** Let's give it a go and there we go. And yes, it's drawing 12.6 amps. Yes, I've got the memory um installed again. I've got the uh processor board installed again, and I'm getting nothing.

**Dave Jones:** Zip. I think it should have uh should have powered up by now. Nope. No, I think it's uh I think it's dead, folks. There you go. I might wind the wick up on the supply a little bit cuz I know there is a couple hundred millivolts drop in those leads.

**Dave Jones:** So, um there's it shh Sorry. Nothing. Zip. Nada. What? Thanks for playing. Well, as it turns out, I just tried to measure the other rails and the 5-V rails up, the minus 5-V rail up is up, but I don't see the minus 2-V rail.

**Dave Jones:** I don't see the plus minus I think 15-V rails. This is one sick puppy indeed. So, it may become more of a bloody power supply repair instead of an oscilloscope repair, but man.

**Dave Jones:** Fail. I'd expect it even if the plus minus 12 V didn't go, I'd expect to see at least the processor powered up. Now, I've opened up this power supply.

**Dave Jones:** Don't get excited. I'm not going to do a bloody repair on the power supply today. I've got very limited time. And it the plus I've measured it again without any load and the plus minus 15-V rails have come back, but there is still the 2-V rail, which is missing.

**Dave Jones:** So, plus 5, minus 5, and plus minus 15 are all working just fine, but that 2-V rail has died. Now, I would have expected um you know, the thing to power up with that, but when I at you know, at least the main processor and stuff like that to power up and at least give me something on the display, but those but that plus minus 15-V those

**Dave Jones:** plus minus 15-V rails die when I hook it to the board under load. So, maybe it's taking out something else as well and well, this is just one very sick puppy.

**Dave Jones:** Now, as for the power supply itself, I cannot see blowing at all. No blowing caps, no blowing power resistors, you know, no charred power resistors or anything like that.

**Dave Jones:** Um, you know, you give it the smell test. Nothing really smells um out of place in the thing. Um, no, you know, big charred power diodes or anything like that.

**Dave Jones:** And it, you know, it um it looks just fine and dandy. So, as far as the visuals go, it's uh, you know, no problem at all. So, this thing would have to be um taken apart, dissected, things tested and measured.

**Dave Jones:** And well, yeah, I, you know, I don't know if I'm going to bother. Yeah, yeah, have a winge. Um, I just I don't think I want to spend any more time on this thing.

**Dave Jones:** Really, it's just you know, I I can't see it being a good investment. That's all. So, I I don't know. I Yeah, give me your thoughts. Let me know, but jeez, yeah, I just don't think I want to spend the time troubleshooting this bloody power supply as an much as an interesting video it might make, perhaps.

**Dave Jones:** I don't know. Anyway, it's not going to happen today. Sorry, folks. And for those who asked, this busted relay has absolutely nothing to do with the short at all.

**Dave Jones:** I believe this happened during the initial uh teardown cuz it was a bastard. Several screws got um threaded and caught and all sorts of things and I was levering the board out.

**Dave Jones:** So, I'm not sure if that uh happened um during my teardown or not. I don't actually remember it happening, but I can only presume that it did happen during that.

**Dave Jones:** It's got nothing to do with it. It's just a little break in the case of a relay. It's nothing. And just to satisfy those who are harping on about removing this second ASIC here, fine, I'll remove the second ASIC and see if the short goes away.

**Dave Jones:** It's not, but I'll do it anyway. Now, this is a pain in the ass. This is stuck on to this chip good and proper with uh thermal adhesive, and you're not going to get that off in a hurry um short of some nasty chemicals or something like that, which I don't um have.

**Dave Jones:** And really um the proper way to get rid of to suck off one of these chips is to use a hot air gun and a proper QFP attachment to your hot air gun after you've got the heat sink off because this is a massive thermal mass here.

**Dave Jones:** So, I you know, you could probably heat it up um with like a you know, something horrible and nasty like a blowtorch and lift it off with pliers maybe, but uh it's going to be really really horrible.

**Dave Jones:** So, unless you absolutely absolutely desperately needed this chip to be intact when you took it off, um which we don't, we just want to get the thing off and see if it makes a difference.

**Dave Jones:** Well, the easiest way to do it is to just cut all the pins around there. And there's several ways to do it. You could try and get in there with a scalpel, but the leverage you know, the the angles in there aren't very good with the other heat sinks in the way and stuff like that.

**Dave Jones:** So, um I think I will just Dremel the pins off and see if that works. Let's give it a go. Well, I was going to try the Dremel, but the sanding discs I've got are unfortunately um just slightly too big to get in there.

**Dave Jones:** What a absolute bummer really. Um that's not very nice at all. So, I think we're going to have to And really the heat sink is too high. So, even if I had a smaller disc to get in there, um really the uh spindle is going to end up uh you know, I'm I'm going to I don't think I'm going to be able to get the angle in

**Dave Jones:** there. So, what I I am going to get in there with the scalpel blade and push it across like that and maybe that's not bad. The problem with this is that you're putting a bit of shear force on those pins.

**Dave Jones:** So, you could actually damage a pad, which isn't that great. So, but we don't necessarily care a huge amount about that. We just really want to get the get the sucker off.

**Dave Jones:** There we go. I think I managed to get all the way along one side. I should be able to do the other side and uh the other three sides and pop this sucker off.

**Dave Jones:** And look at that. We've got it levered up like that. No problems at all. And here she comes. Ta-da! There we go. And there are those pins left over on there.

**Dave Jones:** You can see. It looks like we didn't do any damage to any of the pads. I was uh relatively careful. I was using the correct uh tongue angle there, but there are a hell of a lot of leftover pins on there, which we need to go over with the uh soldering iron and just uh wipe those pins off the pads and we'll be left with the pads, cuz

**Dave Jones:** obviously, you know, they could be uh shorting out uh all sorts of things. So, we want to get rid of those. And check this out. There's a fiducial mark on the board there.

**Dave Jones:** You can see it. And usually these are outside the uh chip as a reference, but they've put this one under the chip like that. So, the vision system on the pick and place machine comes and finds the center of that chip.

**Dave Jones:** It looks like it's directly in the center of like that. I'm assuming that it is exactly the center and they've put it under the chip instead of the more familiar place, sort of, you know, two marks outside the chip like that.

**Dave Jones:** Unusual. And here we go. We're going to wipe off our pins. Now, you have to be really careful here. You've got to set your iron to a very low temperature like under 300 so that you don't apply excessive heat to the pad.

**Dave Jones:** Just enough temperature so that you can wipe these pins off. And the other thing is you don't want to wipe in this direction like that because then that puts increased pressure on the pads and you can lift the pads.

**Dave Jones:** So, you want to swipe it longways on the pad like that. So, let's give it a go. Here we go. And there we go. If we just swipe across, we can remove those pins fairly easily.

**Dave Jones:** Might have to do the odd second pass here and there and you can clean it up with our solder wick later if you wanted to solder in a new chip, but we don't want to do that.

**Dave Jones:** We just want to ensure that all the pins are gone and we can then measure the rail again. And there you go. Should be left with a whole row of very nicely tinned pads.

**Dave Jones:** Now, if you wanted to if you're soldering a new chip on those, you might of course go and solder wick some of the rest of it off, but that is a very nice result and that was a pretty horrible way to rip a chip off like that, but uh really, I think that's probably the best available option I um had to hand really considering that we didn't have to reuse the uh chip at all.

**Dave Jones:** So, yeah. Well, only one thing left to do. Let's measure that power rail. I bet you it's exactly the same. All right, here we go. Let's short our probes again.

**Dave Jones:** Compensate for that. What were we getting before? Uh 0.11 ohms on our 3.3 volt rail. There we go. It's pretty It's going to be pretty repeatable as we saw last time.

**Dave Jones:** I don't mind these probes. They're pretty good. And uh 1 2 3 4 5 6 and here is our 3.3 volt rail. Let's see what we get, folks. Ha!

**Dave Jones:** 0.14. There you go. So, it's that makes sense. It has um Yes, it has gone up from 0.11 to 0.14, but that's what you'd expect. We got 1/4 of the chips um actually um you know, if if the theory is correct, then or you know, something happened to the 3.3 volt rail and it took out all four A6 on that particular um 3.3 volt rail.

**Dave Jones:** So, there you go. You would expect it to go up a little bit like that because we've now taken out 1/4 of the shorted chips, but I reckon that all of them are shorted.

**Dave Jones:** That sort of confirms the original theory that well, the heat had nothing that tiny little what 3 or 4 degrees C difference between this chip and the others As I said, it it didn't add up at all because just the extra power dissipation in there, it didn't uh you know, it it just didn't make sense for it only to rise for a couple of degrees Celsius.

**Dave Jones:** All right, so let's see what that translates to into with uh current. We expect it um to be slightly less than what we're getting before, which was around uh 10 amps or something without power on the other rails.

**Dave Jones:** So, the other rails aren't powered at all. And uh of course, it's a non li- we've already determined it's a non-linear uh thing. So, um you know, we expect it maybe to drop to I don't know, 8 amps or something like that.

**Dave Jones:** Maybe nine or something like that cuz it is going to be shared across the um ASICs here, of course. And if we're And if our theory is right about the four four ASICs all being equally blown or reasonably equally blown, we should see a percentage decrease.

**Dave Jones:** So, let's have a look. Ta-da! There we go. 8.8 amps. It has actually dropped by you know, uh 1. 2 amps or thereabouts. I'm not exactly sure uh exactly what the value was last time, but it was around about 10 amps or so.

**Dave Jones:** So, there you go. It's dropped in proportion. And I'm sure if we desoldered the other chips one by one and measured the current, it would drop in proportion as well.

**Dave Jones:** So, there you have it. I don't think there's uh much option left but to just simply give up on this thing as I said last time. Looks like all four of these chips are shorted out on that rail.

**Dave Jones:** So, something happened to the power supply. We got a spike on there, something. It took out the rail. Um no, we're not going to be able to get these uh chips anywhere.

**Dave Jones:** No, I'm not going to solder them back in. I don't care. It's not Even if I could get the chips, uh man, it's not worth the effort. And fixing that power supply and getting it all going again for an ancient scope like this, eh no, there's no point.

**Dave Jones:** Um sorry folks. So, there you go. Complain all you like, but I think this one is dead and I hope I cleared up a few things that people wanted me to do on this thing.

**Dave Jones:** It definitely is a short inside the chips on the 3.3 V rail. Something happened to that rail, a spike or whatever, and it took out all four A6 on there.

**Dave Jones:** And I think if we suck off those A6 then yeah, we'd eventually get rid of the short. Whoop-de-do. What do we do then? Makes for a great, you know, paperweight.

**Dave Jones:** I don't know. Catch you next time.
