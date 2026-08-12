---
video_id: VwdnGbI5ls8
title: EEVblog #1036 - PSU Fire PCB Repair
url: https://www.youtube.com/watch?v=VwdnGbI5ls8
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 41, "3": 67, "4": 81, "5": 93, "6": 105, "7": 113, "8": 129, "9": 144, "10": 164, "11": 176, "12": 190, "13": 201, "14": 208, "15": 219, "16": 228, "17": 237, "18": 250, "19": 259, "20": 280, "21": 288, "22": 311, "23": 324, "24": 339, "25": 352, "26": 368, "27": 382, "28": 396, "29": 422, "30": 438, "31": 458, "32": 474, "33": 494, "34": 506, "35": 518, "36": 534, "37": 542, "38": 557, "39": 566, "40": 578, "41": 592, "42": 603, "43": 613, "44": 625, "45": 642, "46": 655, "47": 664, "48": 675, "49": 687, "50": 703, "51": 712, "52": 724, "53": 730, "54": 745, "55": 755, "56": 769, "57": 787, "58": 803, "59": 813, "60": 828, "61": 837, "62": 846, "63": 858, "64": 878, "65": 894, "66": 906, "67": 924, "68": 936, "69": 959, "70": 980, "71": 999, "72": 1022, "73": 1032, "74": 1047, "75": 1057, "76": 1071, "77": 1089, "78": 1098, "79": 1114, "80": 1126}
---

**Dave Jones:** Hi, just quick follow-up video to my previous one where we saw this uh RDT DPS 5020 module uh have the magic smoke escape from it. And I'll link that one in here at the end of the video and also down below um if you haven't checked that out.

**Dave Jones:** So, I thought we'd do a quick follow-up actually getting this thing up and running again cuz I didn't have time last time. Let's get to it. Now, as you saw in the uh previous video, the problem was that uh there was a multi-layer ceramic uh capacitor 100 nanopharad uh one connected directly across the uh pins on this uh well the two uh screw terminals on the uh back

**Dave Jones:** side of the board here. And uh Glenn, who uh is the designer at RD Tech, um said yes, this was the problem. are actually screwing the terminals on the top of the board actually cause mechanical stress and cracking inside the multi-layer ceramic uh capacitor when you turn those screws too tightly cuz that force of those even though they're rigidly soldered to the PCB is just enough that a tiny bit of you know

**Dave Jones:** like torsional type force is applied to the uh capacitor which is directly of course rigidly soldered between the two pins and then it you can get possibly a little micro crack inside and that lead to the failure mode of these things which is typically a short circuit.

**Dave Jones:** And of course, all the energy which was delivered into that capacitor via this grunty little power supply caused it to catch a light and burn all the board. Oops.

**Dave Jones:** So, yes, the followup to that is that Glenn has admitted that's a problem and has stopped selling these until he can uh fix or actually redesigning the board to uh have less stress on there.

**Dave Jones:** So, if you do have one of these, um, he says just remove the capacitor. It's not hugely needed. It's just some like little extra filtering on the output. So, that was a huge oopsie.

**Dave Jones:** So, as I mentioned in the previous video, um, just be careful of mechanical torsion force on multi-layer ceramic capacitors and also thermal as well. Having the capacitor directly across and soldered to these two pins that have to be hand soldered, not a good idea at all.

**Dave Jones:** uh thermal stress can also lead to similar sort of problems uh uh causing a short failure. Now when I repowered it in the uh previous video, you saw that it hiccuped and turned off and that was a combination of two things.

**Dave Jones:** Uh one is that I was using an external uh current limited power supply which was going into uh limiting and then causing the thing to hiccup. And the reason that it was uh overloading with no output um on it was that the uh the board that's being carbonized in here actually h formed a low impedance.

**Dave Jones:** So it's actually conducting across the output and that was what was drawing the quiescent current and uh causing the thing to trip. Now I did actually measure this before I uh powered it up in the video.

**Dave Jones:** You didn't see that and it was the in the order of you know tens of k or something like that but it's now 47 ohms for example and this will most likely change with uh uh the applied voltage as well.

**Dave Jones:** So um yeah it's like it's physically changed but anyway um you can't if we swap the leads around. There we go. It's the same either way. So we do have a low impedance directly across there.

**Dave Jones:** So, what we have to do is get in there with a Dremel and or a knife and just h gouge out all of that carbonized uh uh fiberglass in there.

**Dave Jones:** So, why it actually changed from when I originally measured it before I powered it up uh to now where it's like 47 ohms or whatnot, it could be different if I power it up again.

**Dave Jones:** Um I I don't know. There's some sort of, you know, uh some sort of chemistry thing happening in there with the with the carbon based uh you know, burnt fiberglass or whatever.

**Dave Jones:** I won't pretend to uh try and explain it. All I know is that we have to get rid of that, grind it out, and hopefully this thing will repower up.

**Dave Jones:** Now, unfortunately, it's not as simple as just like grinding out a uh track, like cutting a slot into that because if you have a look at the top, there's actually uh two fuses down in there and also like the trace going over to there.

**Dave Jones:** Like I could do it, but I'd rather try and keep those intact. Um and those fuses, they're two 20 amp fuses, by the way. And yes, they are intact.

**Dave Jones:** Uh they didn't blow at all. And after gouging out a decent part of that, let's measure it again. And bingo. You can see it's changed. So you can see that the more material that we're going to remove from there, well, the more resistance that we're well low resistance um short that we're actually taking out.

**Dave Jones:** So if you physically remove all of it, um we should remove the output short. Unfortunately, we're going to have to gouge out a few things. All right, let's take a look at this.

**Dave Jones:** I've gouged out uh some of it in here, but as you can see, it goes all the way practically all the way through the board. Um, and if we flip it over onto the top side here, and you can see down in there that under this uh 20 amp fuse, yeah, the burn has gone all the way through the board.

**Dave Jones:** Uh the top 20 amp fuse there is fine, but yeah, that's just a complete fail. So, we can't just uh scrape out gouge out uh like half the depth of the board.

**Dave Jones:** We really have to route out the whole blink and lot between here, which is a real shame. I could probably maybe get the grinding wheel in there. And if you have a look, you can see that there's these two two 20 amp fuses aren't in series.

**Dave Jones:** Um, one's actually coming from some VAS down in there over to here over to the positive pin. And the other one's also coming from the positive pin from the output of the inductor.

**Dave Jones:** And if you flip it over here, you can actually see what's happening there. So, this one goes straight in down those VAS through uh that 20 amp fuse and then into the positive uh jack here.

**Dave Jones:** And then the other one is of course on the uh top side coming from the exact same uh pins of the inductor. So they're effectively two separate 20 amp fuses going from the output of the inductor in parallel to the output pin.

**Dave Jones:** So why they've put two 20 amps in parallel in there? Um my guess would be that maybe 20 amp is the most that they could get in an SMD size and they didn't want all the current going through one because this is a 20 amp output rated power supply.

**Dave Jones:** So, they didn't want to use a 20 amp rated uh fuse in there in SMD size. So, they went put two in and yeah, it's overrated. Um, so I wouldn't have I would have put maybe two 15 amps in parallel or something like that in that particular case cuz it's going to be much harder to actually blow uh both of those um at 20 amps um as opposed to

**Dave Jones:** like you know 21 15 amps in parallel or something like that. Um, but yeah, I'm not sure if that's the best choice. But of course, you can't use a single uh 20 amp one for a 20 amp rated supply because eventually in theory, a 20 amp fuse will blow.

**Dave Jones:** Of course, they they don't just magically blow at 20 amps. There is a characteristic uh curve for all uh fuses like this. And it's all to do with uh temperature rise inside the fuse, melting the internal uh wire and how long that takes the fusing time and all that sort of jazz which I won't go into.

**Dave Jones:** But anyway, there's two 20 amp fuses there. So either I can get down the side and dremel it maybe um like right down here or I just grind out the whole blinking lot but then I have to wire the fuses in separately and that's a real pain in the butt.

**Dave Jones:** So, don't know if I like doing that. Maybe the grinding wheel is the best option. And there we go. That uh seems to have worked a a treat where like the you probably can't see it very well, but the internal charring on that board basically uh stops there.

**Dave Jones:** So, we scored away most of that. I'm going to have to repair that track is still intact. The copper's still there. Um, but yeah, I'll just wick away that solder on there.

**Dave Jones:** Of course, we have to repair these sense lines here. There's one on the top. And let's have a look. Well, one on the top here and one on the bottom on the other side.

**Dave Jones:** But we've basically still got that fuse intact, all the vas, everything coming through. Um, and that I think should work a treat. Let's go measure it. Anyway, that saved around with having to uh remanually rewire those fuses.

**Dave Jones:** That would have been a pain. So, that should do it. All right, so let's try it again. You saw that we were getting 47 ohms and then up to 70 or whatever.

**Dave Jones:** So, I expect to see uh uh like some sort of uh capacitive output charging or something. Hello. There we go. Started out low, of course, and it's uh Yep, it's gone up.

**Dave Jones:** That's what I expect. Put it around the other way. And there we go. Started out low because there's some output capacitance somewhere that's charged. And Bob's your uncle. Look at that.

**Dave Jones:** All right. That's where I'm not sure what it's supposed to be, but hey, I deem that to be um as normal as it possibly could be. So, let's put it back together and power it up.

**Dave Jones:** Oh, and by the way, for those who uh spotted it and pointed out, thank you very much. Um the short across the pins on the microcontroller in there, that was a just a solder dag that got in there from part of my soldering or whatnot fell off.

**Dave Jones:** Not sure how, but that did not cause the issue at all. It's gone now. And because that's only on the uh keyboard uh display side of thing. Had nothing to do with the rest of the circuitry.

**Dave Jones:** All right. So, if we actually uh power this thing on and got it powered from a 40 volt source with a 5 amp current limit this time. Uh, so it's capable of 200 watts.

**Dave Jones:** And you can see that it's drawing 2 watts quiescent current. And you'll see that everything is just hunky dory. Now, let's switch that got set to 4.9 volts. Whatever.

**Dave Jones:** Let's switch the output on. Um, it's not drawing. It's not measuring anything at the moment. Let's There you go. Bingo. 4.97. It's reading precisely what it's uh set to and there's no current draw on the output because this thing, you've got to assume that it's still working because it the fuses were intact.

**Dave Jones:** It's got all sorts of protections built in. So, no worries whatsoever. It just flamed that capacitor on the output and the magic uh smoke escaped. So, it should still be a fully working power supply.

**Dave Jones:** And it looks like it is. So, let's uh switch on the load now and see what we get. All right. So, let's set it to a uh 10 watt constant current load.

**Dave Jones:** I've set it to 10 volts precisely on the output. Um, in fact, let's h switch that on now. There we go. No worries at all. It matches and uh 2 amp current limit.

**Dave Jones:** So, that's 20 watts. No worries whatsoever. So, let's switch the output on and see. Bingo. 9.8 watts is And it's a little bit out, but it's I think it's like half a percent or something is the spec on this thing.

**Dave Jones:** So, no worries. whatsoever. 10 watts, fine and dandy. One thing I don't like, and you can probably hear, is the fan in this thing. I don't have the top on it, but it is just worring at constant speed, even with no load.

**Dave Jones:** It's just really annoying. And it's loud enough to be quite annoying. But, you know, you could retrofit any uh fan you wanted to. Okay, now we're drawing 100 watts.

**Dave Jones:** There we go. And everything's hunky dory. Don't worry about the voltage loss on here. I haven't set up remote sensing. So, we're just getting some loss across the uh cables here.

**Dave Jones:** Even though they are a decent size, when you're talking 10 amps, yeah, you're going to get some drop. Let's just have a look at the uh output noise here.

**Dave Jones:** Like 10 volts, there's no load on there whatsoever. And uh that's actually quite substantial. I mean, that output cap shouldn't make it like the the 0 missing 0.1 uh mic on there shouldn't make a huge difference.

**Dave Jones:** If you're wondering where these uh spikes are coming from, you can see those there. If I capture it, look at those. Um they like are still there even if I switch the output off.

**Dave Jones:** I've got no load at the moment. So that's a that's the low no low no load noise. And if I switch the output off as in like soft button on the uh front of it, we still get that high frequency stuff.

**Dave Jones:** So that is coming from somewhere in the system and that's actually coming from my environment here. So uh yeah, I've actually switched off the input the power supply. You can probably hear there's no fan noise now and it's completely uh switched off.

**Dave Jones:** So yeah, we're just picking up crap because I've just got the leads flapping around in the breeze here. Me ignore the man behind the curtain. And if you're wondering if that no load ripple is caused by the lack of the capacitor on the output, the answer is no.

**Dave Jones:** I can whack in a uh 22 mic uh 200 volt cap here. Let me make sure I got around the right way and I can put that directly on.

**Dave Jones:** Again, we got no load and bingo. It makes no difference whatsoever. So that uh measly I think it's a 0.1 microfarad cap across the output. It's just for uh you know EMC like you know CE compliance.

**Dave Jones:** So and I believe this thing is uh uh you know CE uh compliance. So not having that cap on there actually technically changes the uh compliance of this thing.

**Dave Jones:** But uh yeah even a you know a 22 mic cap on the output doesn't fix that. But you might see it change if you put a load on. So we can actually do that.

**Dave Jones:** I've got a 100 watt load on the output. Let's put the cap on. 22 microfarads. Bingo. You can see it. That's off. That's on. So, you can see that uh change just a tad.

**Dave Jones:** So, there you have it. That's the uh repair of the DPS 50/20 power supply that completely smoked. And uh you know, thumbs up to RD Tech. They did actually admit it was a problem and they'd actually seen it before as well in one or two uh cases before, so they should have fixed it at the time, but they didn't.

**Dave Jones:** They sent me one. Um, and a classic mechanical uh and/or thermal could have had uh something that could have contributed as well. But and the most likely scenario is that when you screw in those screw terminals on the top, it just got some micro cracks inside the multi-layer ceramic capacitor.

**Dave Jones:** And in most of those circumstances, they will fail short. And then this thing is capable of I mean, we're only 100 watts at the moment, but even that like you dump 10 watts into that capacitor or something and it's going to start smoking and flames.

**Dave Jones:** the magic smoke escapes and you get the flames and it starts burning. But anyway, it's robust enough to handle all that. No worries whatsoever. So, sorry, but I'm not going to fully characterize this thing in the video and do a full review of it and everything like that.

**Dave Jones:** Um, Glenn, I believe it has actually stopped selling these um and until such time as they can change the PCB to do the layout uh properly and then they'll be reselling these with the uh corrected MLCC.

**Dave Jones:** But I hope that's an interesting lesson to not only RD tech but to everyone out there that these multi-layer ceramic capacitors are susceptible as I said in the previous video to not only mechanical uh stresses which is a big thing for them thermal stresses uh they're susceptible to just a failure in manufacturing you know you've got an infant mortality thing on these components so some will eventually

**Dave Jones:** fail and a good way to actually uh reduce or elim basically eliminate the problem is to put two of them in series. So if one happens to short due to whatever issue it is um then then the other one uh will uh still be a capacitor and yeah you will uh effectively double your capacitance but it's generally not a huge issue.

**Dave Jones:** At least it won't smoke and catch on fire. Especially for high power supplies like this that are capable of delivering not not just on the output of a supply but as you saw on my uh Nest uh alarm system which had the same smoking ceramic capacitor that caught a light and burnt the entire board.

**Dave Jones:** That was al on the input side. So just like the AC plug pack, the rectified AC plug pack, um if the capacitor was on there just to, you know, filter it a little bit on the input side of the regulator after the bridge rectifier and of course the plug pack can deliver watts and you know five or 10 watts and the capacitor shorted uh due to in this case it wasn't a

**Dave Jones:** mechanical fail. It was just like an infant mortality failure uh component manufacturing intolerance thing. It happens and it caught a light as well. So, not only just the output, but input side of things as well.

**Dave Jones:** So, just be careful of multi-layer ceramic capacitors. When you're laying out boards, take into account your location of the uh ceramic capacitors next to any stress components. In this particular case here, we got screw terminals on the PCB.

**Dave Jones:** So, when you put, you know, screw them up real tight, uh the torsional force on there can uh couple through to the PCB. Or if you've got mounting holes or something like that, you're putting screws into those.

**Dave Jones:** have uh multi-layer ceramic caps next to those can, you know, ruin your day. Uh if you get a generally they'll fail short. If you're lucky, they might fail open and well, the product might fail or you might get more noise or whatever.

**Dave Jones:** But when they fail short and you've got a supply across it that can deliver a certain amount of power that can make these things uh catch a light. So anyway, it's a real interesting real case of how component failure can in this case lead to something quite dangerous in a component catching on fire.

**Dave Jones:** Anyway, hope you enjoyed it. If you did, please give it a big thumbs up because that always helps a lot. And as always, discuss it down below. Catch you next time.

**Dave Jones:** Oh, by the way, if you're wondering why this video is maybe a little bit different, I actually I'm shooting this thing on my uh Sony Nex uh VG30, which I normally only use for my uh talking head mailbag, and I'm using the internal mic on that main air, which is a shotgun.

**Dave Jones:** So, it may not be audio may not be as uh well, it's probably going to be a little bit different to what you expected. Anyway, catch you next time.

**Dave Jones:** [Music]
