---
video_id: dkdLWronrlk
title: EEVblog #1089 - XTAL Oscillator Teardown
url: https://www.youtube.com/watch?v=dkdLWronrlk
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 32, "3": 45, "4": 60, "5": 72, "6": 88, "7": 104, "8": 117, "9": 135, "10": 150, "11": 171, "12": 184, "13": 196, "14": 207, "15": 222, "16": 236, "17": 249, "18": 264, "19": 282, "20": 297, "21": 313, "22": 330, "23": 346, "24": 359, "25": 376, "26": 389, "27": 400, "28": 417, "29": 432, "30": 449, "31": 460, "32": 474, "33": 487, "34": 501, "35": 515, "36": 533, "37": 548, "38": 563, "39": 577, "40": 591, "41": 606, "42": 623, "43": 639, "44": 656, "45": 670, "46": 682, "47": 700, "48": 716, "49": 729, "50": 742, "51": 754, "52": 771, "53": 786, "54": 804, "55": 822, "56": 840, "57": 854, "58": 867, "59": 882, "60": 897, "61": 911, "62": 927, "63": 941, "64": 955, "65": 969, "66": 985, "67": 1002, "68": 1014}
---

**Dave Jones:** Hi, it's time for a quick 2-minute teardown. We're going to teardown a crystal oscillator. No, this is not a crystal oscillator. This is a crystal in the classic HC49U package you should be familiar with. You see that it's just like a soldered

**Dave Jones:** shut at the end and it pulls out and there's photos of these everywhere. In fact, if you look on Wikipedia for crystal oscillator, you'll see a photo that I actually added way back in 2006 inside one of these classic HC49U

**Dave Jones:** packages. But, this is not a crystal oscillator. It's just a crystal. It needs external circuitry to actually work. So, I thought we'd do a quick 2-minute teardown cuz I don't think I've ever seen inside one of these. This is a

**Dave Jones:** crystal oscillator in the standard 14-pin, 4-pin DIP package. I know that sounds confusing, but anyway, those little bumps on the bottom, by the way, are to keep it off the PCB to stop the metal case here from actually shorting

**Dave Jones:** out any pads or vias, you know, exposed vias or anything else on the board. Just allows some standoff there. Anyway, this is a complete oscillator. It basically contains, well, it will contain a crystal of some description. They do

**Dave Jones:** come in many different types and physical form factors and things like that, but this will also have, in this case, it's a HC MOS oscillator circuit in there. You've got there's a power pin, a ground pin, and a not connected or a like a tristate

**Dave Jones:** enable pin and an output pin on it. And it outputs a square wave. It has a proper oscillator and an output buffer. Because this actually comes from the previous video where I actually had this CMOS oscillator on here and I did

**Dave Jones:** actually consider at the time, well, does this have a bypass capacitor built in? As it turns out, it worked just fine. So, let's have a look inside. See what's in there. Is it a same a similar form factor as this with a little

**Dave Jones:** oscillator circuit in it? I don't know. Let's find out. Wow, check it out. It is actually quite uh similar to the uh circular quartz disc that you get inside the uh standard HC49U packages or a uh lot of them. And

**Dave Jones:** then there we just got a standard uh eight-pin DIP um oscillator/driver, whatever that is. I don't know. It's their own brand. They've rolled their own or they've re-bashed it or whatever. There's the quartz disc mounted in three places,

**Dave Jones:** which is interesting. Wow, okay. The ones inside the HC49U package only have the uh two mounts on them. This one has a third mount over here. Wonder why. That's not FR-4 uh fiberglass. That's actually a uh ceramic hybrid based on there. Although it's not

**Dave Jones:** really a hybrid because this is just a ceramic PCB hybrid would be like that. Actually, um embed the resistors on there and stuff like that. But uh they haven't done that. That's a zero-ohm jumper. There you go. That's not even a

**Dave Jones:** resistor. That's it. Oh, no. No. There we go. No, there's one cap. There's a cap. There is a bypass cap, is it? There's one under there. It's going to pin eight of the chip here, which also goes along

**Dave Jones:** that trace up to the power pin here. And it looks like the other side of it likely goes under the chip and connects to there. I can just buzz that out to confirm, but I'm sure it does. So, this

**Dave Jones:** thing does have a bypass cap. So, there you go. But that um ultimately didn't interfere with my uh test for in the previous video um for the bypass capacitors. But there was one in there. Cuz this is the exact model that I used

**Dave Jones:** in there. Um I had multiple ones of this. As a bonus, let's do one of these smaller eight-pin DIP ones. Hmm. At a guess, I'd say all the circuitry here is going to be packed underneath the uh quartz disc there. So, it's just going

**Dave Jones:** to be like stacked up. Yep, I was right. It was pretty obvious and oops, yeah, they're very close to the top of the can on there. So, when I got my Dremel in there, it just shattered cuz these

**Dave Jones:** things shatter really easily. But, it just suspends it over the top there. But, check this out. It's totally different to the other one. Look at those mounting posts on there. They're actually springs on both sides there and there is no third mounting point like we

**Dave Jones:** saw on the previous one. So, that's really interesting. In fact, you could probably come a gutser there if you weren't careful because if the if the crystal forms some sort of resonant mode vibration mode with the spring, you could be in trouble. But, that's

**Dave Jones:** that's quite fascinating how they've actually added the springs in there because uh quartz crystal oscillators and I've done that quite a bit of research into this in at a former job are very susceptible to shock and vibration. In fact,

**Dave Jones:** I've done some research actually shocking crystal oscillators. I built a jig to actually drop them and shock them and get the response. We put accelerators accelerometers on them and to measure the response and you would actually reset the drift characteristic

**Dave Jones:** of the oscillator when you actually shocked it. So, like like it's very small amounts. It's very marginal. But, if you design in high stability oscillators, which we were for underwater seismic stuff, the stability is what mattered over time. And if they got shocked, then

**Dave Jones:** it would actually reset that drift characteristic and you'd have to start your drift compensation stuff all over again. It just ruined everything. So, that's I just find that fascinating that they've got those springs on there. Are they they're trying to eliminate sharp

**Dave Jones:** shocks, which of course are directly coupled through the pins on the board straight into the ceramic PCB and then straight up the shaft onto the quartz plates. And they're trying to avoid that. Neat. So, exactly the same as a

**Dave Jones:** HC49 crystal, again with a bypass cap between ground the ground pin and what looks like I'll buzz it out, but I'm sure it is the power pin up there. So, these crystal oscillators I I wouldn't take it as an absolute rule, but two out

**Dave Jones:** of two have bypass caps in them. And but they don't mention this on the data sheet that I've seen anyway. So, what effect does this bypass capacitor have on here on our previous experiment that we did where I

**Dave Jones:** placed bypass capacitors on the board and showed the effectiveness of them. I'll link that in at the end if you haven't seen it. Well, it does have some effect. It doesn't negate the previous video in any way. It's just that the

**Dave Jones:** effect would have been more dramatic last time if we didn't have that bypass capacitor inside this thing. But you've got to remember though that that bypass capacitor is inside this thing which has those little traces running. We've got

**Dave Jones:** the leads on here. We've got the inductance of these lead lengths. We've got the inductance of the traces all going through there. And of course our reference plane here that we're actually measuring everything relative from is outside the package. So, having the

**Dave Jones:** bypass capacitor inside the package, it's not as it's not the same as having it actually directly connected to the ground plane, the reference that we're actually measuring from, which is what we actually care about. In this case, it's going to have an inductor

**Dave Jones:** basically almost practically no DC resistance there, but it's going to have inductance of the leads and the traces and everything else on that path. No matter how small they are, they're still going to have a dramatic effect at the

**Dave Jones:** frequencies we're talking about. So, that bypass capacitor has a nice effect on this chip, of course. It really helps a lot, but outside the circuit, well, it's going to help, too, but relative to the reference plane, it's just a

**Dave Jones:** different thing. So, anyway, what I've done is I managed to I couldn't get in there off the soldering iron, but I managed to get in there with a little flat-headed screwdriver and just prize out the capacitor, just crack it cuz

**Dave Jones:** they're ceramic capacitors and they crack really easily. I was able to do that without damaging the quartz resonator there. So, it still works, but we have no bypass capacitor on there. So, let's take another look. Now, I won't go over the whole setup again. You

**Dave Jones:** have to watch the previous video to get an idea for that. So, I still got bang on 1 MHz here, so we didn't physically damage the resonator there, but look at the ripple that we're getting now. Rather than just at the edge there, it's

**Dave Jones:** got all this other crap in here as well at multiple points in inside that one 1 MHz fundamental. So, that's rather interesting, isn't it? And look at channel two. We're now 2 V per division on here. This is crazy. So, it's like

**Dave Jones:** the 5 V rail is just going up by 2 and 1/2, down by 2 and 1/2. That's just ridiculous. That's with absolutely no bypass capacitor. That rail is horrid. But, of course, that is driving our 50 ohm load which we had there before and

**Dave Jones:** yes, I am using the proper probing that we did last time. So, if we disconnect our 50 ohm load, we should see that improve dramatically. So, there you go. That's with no load and you can see there's now no large transitions. It's

**Dave Jones:** still very bad on the 5 V rail, the blue channel here at 2 V per division, but no large transitions that we saw before. And if I put one of the resistors back, you'll see it drops in amplitude and you

**Dave Jones:** get that large transition going there like that. So, that's actually sinking high frequency current into the load with no bypass capacitor. It doesn't have any bypass capacitor to store that little gulp of energy that it needs. So, I

**Dave Jones:** really should have set up this video better last time, but let's have a look what happens now if I whack that 330 microfarad back on here. Still got no high frequency bypass, but if we do the bulk decoupling, still does quite a

**Dave Jones:** reasonable job. Look at that, but that high frequency stuff at 100 mV per division is still there. And look at the large stuff on the positive transition here. There we go. On the positive transition, you can really see it.

**Dave Jones:** That's absolutely enormous. So, because it's got no high frequency bypass capacitors. But, let's see if we can see this change as I slide it. I'll start near there and I'll slide it backwards. So, here we go. There we go. Look at that. And I'll

**Dave Jones:** slide Look at the level. Look at the level. Keep looking. Keep looking. And you can see it going higher and higher level as I move that bypass capacitor. So, I've got it right down here and I put it up there and it makes quite

**Dave Jones:** a dramatic difference in terms of that's 100 mV per division in that high frequency ripple. Even though we're not you really using a real optimized cap for that. So, let's try our 0.1 microfarad ceramic, shall we? But, at

**Dave Jones:** this point any capacitance is going to make a difference. So, even the big bulk cap up there is going to do a reasonable job. We'll find that this ceramic here is There we go. That's near it and we

**Dave Jones:** move it away. Oops. Move it away and it gets bigger and bigger yet again. So, let's use that 0.47 microfarad film cap on there. There we go. And now let's try and replace that with this 0.1 ceramic. You probably won't see much difference

**Dave Jones:** cuz they're both going to be There we go. Pretty much both equally effective there. Okay, let's do the combo now. 0.1 and the 0.4 7. Come on. There you go. Sweet as. Oops, stay there, you mongrel. It does

**Dave Jones:** have a bypass capacitor in there, but that doesn't mean that you shouldn't use a bypass capacitor on that device because you've got the inductance of the leads and everything else. So, it's not as effective relative to the reference

**Dave Jones:** plane. And when you're trying when you've got a driver over here and you're trying to drive another chip over here, and this chip all the chip cares about there is the what's actually received relative to this reference plane and the

**Dave Jones:** power plane here. When you start adding little leads and everything and inductors all in series and stuff like that, you start to complicate the equation. Doesn't look great, does it? But just put your little bypass cappy on there

**Dave Jones:** and she's sweet as. Look at that. Like a bought one. Now, if you're wondering what all this stuff in here actually is, obviously it's not just the one pulse and then just some ringing in there that then eventually settles out. There's

**Dave Jones:** obviously some very deliberate high higher frequency components in here. So, if we set up some cursors here like roughly from one peak to the next, that's sort of higher frequency stuff, we're looking at about, you know, 29.4 MHz or something like that. But there's

**Dave Jones:** something more interesting, which are these periodic higher peaks in here like this. So, this isn't like just your normal ringing. It wouldn't do that. Something is resonating or oscillating at that particular frequency. It's given it a kick each time. So, it's obviously

**Dave Jones:** oscillating something like that. So, if we uh move the cursor over there from one peak to the other, Aha! What have we got? 8 MHz. Aha! And you might have seen that in uh some previous footage here. I might have to

**Dave Jones:** replay that. I think even the previous video, that matter how uh well, eventually with bypassing was pretty good, but you could see this um like higher frequency like little spikes in there. So, let's actually go in and actually probe the crystal oscillator.

**Dave Jones:** It's the actual uh crystal resonator inside there and see what frequency we get. I think this um in fact, I'm pretty sure this is going to not use a 1 MHz res resonator. It's going to use an 8

**Dave Jones:** MHz resonator and they're actually uh dividing that by eight. And the chip in there might be have some uh pin straps uh to give you different frequency, different uh divider ratios, for example. So, that might be how um they

**Dave Jones:** might get the different uh frequencies out of the thing. Obviously, it can't get like uh the oddball ones with the same resonator. If you've got an 8 MHz resonator, you're not going to get, you know, 2.048 MHz uh for example. Probe one pin.

**Dave Jones:** Hopefully, we will not shut down the oscillator with the capacitance. Aha! What's the frequency down the bottom there? 8 MHz. There it is. So, there you go. It's obviously an 8 MHz resonator on here and divided by eight. And that's

**Dave Jones:** why you get that higher frequency uh stuff. Yeah, there's a ringing in there, but as you saw, I gave an extra kick every time the 8 MHz um oscillator uh did its business. So, you might have to uh remember that when you're, you

**Dave Jones:** know, doing EMC uh compliance and the rest of it, um you're going to have to factor in in this particular case, it's a uh divide by eight. So, the actual frequency is eight times higher and that sort of stuff can actually leak out of

**Dave Jones:** your pins into your ground planes and and actually radiate or couple out. So, you know, you're just got to be aware of that. It's not a 1 MHz oscillator. It's actually an 8 MHz divide by eight. I know that was slightly more than two

**Dave Jones:** minutes, but nah, I wanted to see inside these things. I'd never actually cut one apart before and it's pretty much exactly as I expected. So, nothing hugely groundbreaking there, but at least I know. And now you know. Hope you

**Dave Jones:** enjoyed that. If you did, please give it a big thumbs up. As always, subscribe at the end, play the videos at the end here, all that sort of jazz. Subscribe to EEevblog, too. And as always, you can subscribe on Patreon, as well. Thanks to

**Dave Jones:** all my patron subscribers who often, by the way, do get some, but not all videos early before I release them on the main channel. If you're wondering how some comments from a day ago, before it was released, well, that's how they do it.

**Dave Jones:** Catch you next time. And if you found that interesting, be sure to stick around for the links I've got to three videos at the end of this after the end screen here. One is the crystal oscillator drift, which I talked

**Dave Jones:** about in the circuitry to do that and how we did that back in the day. That's a real old video. And I've also got one on how to detect gravity using a frequency counter and it has to do with crystals. It's a

**Dave Jones:** fascinating thing. Check that one out, definitely. And I've also done a rubidium frequency standard teardown, as well. Check them all out.
