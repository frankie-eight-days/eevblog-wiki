---
video_id: i3XjdT4mIbQ
title: EEVblog #584 - What Effect Does Your Multimeter Input Impedance Have?
url: https://www.youtube.com/watch?v=i3XjdT4mIbQ
source: youtube-asr
timestamps: {"0": 1, "1": 10, "2": 22, "3": 37, "4": 53, "5": 75, "6": 91, "7": 106, "8": 131, "9": 139, "10": 151, "11": 172, "12": 187, "13": 199, "14": 215, "15": 230, "16": 239, "17": 255, "18": 263, "19": 273, "20": 285, "21": 292, "22": 306, "23": 316, "24": 338, "25": 356, "26": 368, "27": 380, "28": 399, "29": 415, "30": 433, "31": 448, "32": 462, "33": 476, "34": 489, "35": 497, "36": 515, "37": 527, "38": 538, "39": 551, "40": 563, "41": 577, "42": 590, "43": 603, "44": 620, "45": 635, "46": 657, "47": 676, "48": 692, "49": 707, "50": 729, "51": 744, "52": 755, "53": 764, "54": 780, "55": 791, "56": 802, "57": 811, "58": 826, "59": 845, "60": 871, "61": 885, "62": 896, "63": 907}
---

**Dave Jones:** Hi, I thought I'd show you a little trap for young players here about how the input resistance of your multimeter can really have an effect and really matter in some specific circumstances.

**Dave Jones:** Now, what I've got here is my little microcurrent test jig for my micro current. Just plugs on the top here like this and I can plug a known current into here and it's just got a window comparator as we'll see.

**Dave Jones:** Pass fail results. It's got some trim pots to allow me to trim the exact specification pass fail specification that I need. So, let's take a look at it, take some actual measurements, and see what we get.

**Dave Jones:** So, what I've got here for the circuit is a precision voltage reference here LTC 6665 precise 1.25 V like 0.025% accurate really quite nice. And then I've just got a resistive divider down here like this.

**Dave Jones:** And what this is doing is just generating two precision reference voltages ref plus and ref minus here. So, that's all I'm doing and it's basically I'm going to try and set them today to plus 0.025% or 1 V 0.025% above 1 V which is 1.00025 V and 0.025% below 1 V.

**Dave Jones:** There you go. So, we're trying to set some really precise values here. And to do that of course we're going to use our 6 and 1/2 digit you know really top of line Agilent multimeter to measure our voltage across our two pots.

**Dave Jones:** And you'll notice very low impedance in here. I mean we're only talking 10 ohms here and we're talking a 2K pot across that 10 ohm resistor. Why you put a higher value pot across a lower value resistor like this?

**Dave Jones:** Basically stability because I we're generating a very basically this center tap here is going to be 1 V. I've chosen the divider resistor to actually give that from our 1.25 volt reference, and then we're using the low value 10 ohms in here to give us a precise value above that, and then we're using a higher value pot, in this case 2K, across that.

**Dave Jones:** The reason why you wouldn't wouldn't put a very low value pot in there is cuz cuz the wiper resistance is really going to have an effect on the stability of that.

**Dave Jones:** So, it's much better design practice to put a higher value pot across a lower value resistance in this case. Anyway, that's just a little aside. We're going to generate and measure two precise voltages here, and then we're going to test it and see if it all works.

**Dave Jones:** So, there these two pots here which we're going to adjust the two trim pots on there, and we'll measure the wiper voltage on there. Now, this the wiper voltage for these two the two precision references voltages go into our standard window comparator here or window detector.

**Dave Jones:** Reference voltage plus reference voltage minus, and basically the LED comes on if the input value coming from the banana plug down here, the input banana plug we've got ground and banana plug input, which we can feed a precise DC voltage in to check it.

**Dave Jones:** If that's within side the margin of these two values, i.e. it's within spec, then the in spec LED here will light up. That's the plan. Let's give it a go.

**Dave Jones:** So, here we go. I've actually adjusted that trim pot. I'm measuring the wiper voltage on the positive side here, and I've set it for 1.00025. And you'll notice that uh I'll just show you the how I can actually tweak that.

**Dave Jones:** Here we go. See? We can actually tweak that pretty well. So, we'll get that right up to .25. Near enough. There we go. Fantastic. And likewise with the other pot down here, .99975.

**Dave Jones:** And you'll notice that we can pretty much fine adjust that sucker as well. This isn't a proper screwdriver for doing this. You need one of those proper captive adjustment screwdrivers.

**Dave Jones:** And you can see that's pretty stable too, by the way. Yes, there will be some temperature coefficient and stuff like that. Little bit of drift with temperature, but you know, really nothing serious here unless we're talking huge temperature swings.

**Dave Jones:** So, everything should stay pretty stable when we disconnect this. Now, let's feed in an external voltage into here and see if we can get within that pass file window.

**Dave Jones:** It should work. All right. So, what I'm doing now is I've got my Kron Hite EDC precision voltage standard here and I've dialed up 1 V precisely on it.

**Dave Jones:** Sorry, I haven't actually let it warm up at all. I've just switched it on anyway. I've got it measuring I've got our Agilent meter here measuring the output as well.

**Dave Jones:** So, that's what we'll actually go by. We won't go by the exact dials on here yet cuz it needs to stabilize, but we're going by the Agilent meter which we set it to before.

**Dave Jones:** So, we're using the same instrument and it should be within spec. We should And look, there it is. Our green LED has come on with point Well, let's let's tweak that up, shall we?

**Dave Jones:** There you go. That's pretty close. There we go. We got our 1 V and our in spec LED is on. So, everything's working fine. Now, let's test this top voltage reference.

**Dave Jones:** So, this LED should switch off at 1.000 25 V. Does it? 25 No. Look, it's still on. 38 What's going on? The LED is still on. Look, it doesn't turn off until basically Look.

**Dave Jones:** 47 48 Something like that. So, look, it's almost doubled. What's going on? We set that voltage on that pot to precisely 1.00025 V. So, let's test the low side now and see what we get.

**Dave Jones:** Remember we set it to 0.99975. So, the LED should stay on for anything above that value. It should go off for below it. So, let's go to 0.8. No, look.

**Dave Jones:** It's switched off. The LED has switched off at 0.99986. That's higher than our reference value there of 0.99975. So, what's going on? What value does it actually switch off at?

**Dave Jones:** 0.9926. Look at that. Crazy. On off. Look. That's just unbelievable. There is something wrong with the either our comparator circuit or our trimming of those resistors cuz nothing has drifted in the meantime.

**Dave Jones:** Trust me, the temperature hasn't changed. So, that's quite strange. We're feeding in our precision 1 V on the well, our our adjustable voltage from our reference standard on the banana plug here, the input the center input to the window detector here.

**Dave Jones:** We've precisely set our reference values here plus minus of 0.025%. But, when we input the value here, it doesn't seem to match. The LED doesn't match those values. And you might be thinking, "Aha, the offset voltage of the op amp.

**Dave Jones:** You've got to have really precise op amps here." Well, I'm using an OPA2376 and it's got a nominal a typical offset value of only 5 microvolts. And 5 microvolts in 1 V is 0.0005% at that 1 V.

**Dave Jones:** So, really, you know, um it's not causing an issue before. We're we're not causing an issue at all cuz we're looking at 0.025%. This is 0.0005%. So, the error of that op amp is not contributing.

**Dave Jones:** So, it must be something else. And no, the input impedance of these op-amps isn't going to matter cuz these are really precise fit input op-amps. We're only talking like picoamps into uh the input values here.

**Dave Jones:** So, the loading on there doesn't matter. Although, it even if it was much higher, it wouldn't matter anyway because we were measuring the precise value on there, which would have compensated for any input bias current loading on that trim pot.

**Dave Jones:** And if you want to try and figure it out for yourself, it's on the screen there. So, stop the video, try and figure out what's going on, and we'll find out in a second.

**Dave Jones:** And I hope you figured it out, and you should because it's the title of the video. This um Agilent uh 34461A has a um high impedance input mode, but currently it is set by default to the standard 10 meg input impedance there.

**Dave Jones:** Aha, but hey, 10 meg, should that matter? I mean, take a look at this circuit, right? We've We've only got 2K on here. What is 10 meg going to do on that 2K?

**Dave Jones:** You might think it's many orders of magnitude above. It shouldn't have an effect at all. It Most multimeters have a typical uh digital multimeters have a typical input impedance of 10 megohms.

**Dave Jones:** And really on 2K, that shouldn't do much at all. And if you actually do the math and figure out what 10 meg uh you know, can how it can affect the 2K, it depends whether the wiper pot value is and all that sort of jazz, right?

**Dave Jones:** But we're only talking about 0.02%. Well, you know, on a precision circuit like this, that can really matter. But aha, we the 10 meg resistor is not across that pot there.

**Dave Jones:** It's from this reference point, the wiper of the pot, down to ground like this. And look, we've got an extra 10K in there. So, that 10 meg is really going to upset this entire voltage divider thing here.

**Dave Jones:** You can't do it. When you're down at this sort of precision level, that 10 meg really matters, even though it's a you know, a couple of orders of magnitude more than the impedance of the circuit you're trying to measure.

**Dave Jones:** And I can show you the effect of that live by using another multimeter, putting it in parallel with this uh Agilent one. I've actually got it uh hooked up back to the uh pot again there.

**Dave Jones:** So, let's actually uh probe this in parallel. We'll measure the same voltage, of course, but let's see if it changes. Ta-da! Look at that. It's dropped just by putting another 10 meg in parallel.

**Dave Jones:** It's affecting our reading because the impedance of that circuit is now changed. So, our voltage divider ratio has changed. So, any good precision multimeter will have a high impedance mode.

**Dave Jones:** Sometimes on uh like handheld multimeters, it's only on the millivolt range, for example. You may not get it on the voltage range. This uh uh Agilent uh meter uh 6 and 1/2 digits doesn't do it on some of the higher voltage ranges, like the hundreds of volts, but I think up to the 10 V range, it allows you to have uh effectively infinite input impedance.

**Dave Jones:** And it says auto here, but input impedance, let's change it. And look, the value has changed by going from our 10 meg input impedance to effectively infinite. It says in the data sheet, I think it's like greater than 2 gig or something like that, but effectively, it's just the input uh effective input resistance of like uh the FET input amplifier.

**Dave Jones:** That's pretty much um all it is. So, it's now changed. So, you can see that the adjustments we did before were completely wrong because we forgot to use an a multimeter that had a high input impedance mode.

**Dave Jones:** 10 meg is high, yes, but for precision circuits like this, nope, it ain't. So, we'll adjust this again in our high impedance mode. 7 5 is it? Yep. There we go.

**Dave Jones:** That's pretty spot on. We'll do the same for the positive side. And there we go. We'll tweak that down to 2 5. That's pretty darn spot on. All right, I've hooked it back up feeding the output voltage from my uh generator here into the BNC inputs and also measuring that with the meter here.

**Dave Jones:** Um once again, because this is a low impedance source now from my uh generator, it doesn't matter. Look, uh it whether I'm using 10 meg or whether or not I switch over to high impedance, makes no difference whatsoever.

**Dave Jones:** Because we're a low impedance source as opposed to the high impedance source we had in our circuit with the pots down in there. Anyway, let's have a look to see point triple nine.

**Dave Jones:** We expect it to go out and we it's just under. So, that technically in theory the LED should be out, but look, I mean, there it is. It's just on the border.

**Dave Jones:** It's just flickering a bit, but there we go. That's pretty darn close to what we programmed in point triple nine 7 5. In fact, our the offset voltage, as I said, of our op-amp down here, the 5 microvolts, could be starting to come into play there cuz it might actually be higher than 5 microvolts.

**Dave Jones:** Uh could be, you know, slightly off or something like that. But anyway, that's pretty darn close. Let's try it for the uh positive side. There we go. Our LED is still on at point triple 0 2 4.

**Dave Jones:** We expect it to turn off at point triple 0 2 5. In theory, there's going to be some No, just over, but we go up one. Oh, it's just starting to flicker.

**Dave Jones:** There's a tiny bit of noise on there and bang, it's gone. So, there you have it. We're now spot-on. So, that can be a real trap for young players.

**Dave Jones:** Just keep it in mind next time you're well, measuring anything really. Is the 10 meg input resistance of my meter affecting my measurements? At first glance, you may not have thought so with the lousy, you know, very low impedances here, 2K, things like that.

**Dave Jones:** But, as you can see, when we're talking about precise settings like this, it really made a dramatic difference. So, that's a real practical example where you can come a gutser by not being aware of what effect the 10 typical 10 meg input impedance of your multimeter is going to have.

**Dave Jones:** So, any good lab should have a multimeter that has a high impedance voltage mode just for doing these sorts of precision measurements where that 10 meg can matter. If you had a very high impedance source circuit here, you know, 10s of K like we had here, 10K, hundreds of K even, you know, up in the megs, voltage divider for something incredibly low power or something like that, then woah,

**Dave Jones:** your 10 meg is not going to be good enough. And in some circumstances, really, really high impedance circuits, even the infinite effectively infinite input impedance of your meter can actually matter cuz it's not going to be infinite.

**Dave Jones:** There's going to be something there. There's going to be some charge on the gate of that input FET or something like that. But, anyway, that's for another time and that's for really, really niche applications.

**Dave Jones:** But, even for general ones, your 10 meg input impedance on there can really matter. Keep a watch out for it next time. Hope you enjoyed the video. And if you did, please give it a big thumbs up.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum. The links are down below. Catch you next time. Mhm.
