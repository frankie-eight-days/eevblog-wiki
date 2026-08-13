---
video_id: Cn3DVQGmF9A
title: Dyson Battery Failure
url: https://www.youtube.com/watch?v=Cn3DVQGmF9A
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 44, "3": 60, "4": 80, "5": 102, "6": 119, "7": 136, "8": 153, "9": 178, "10": 198, "11": 228, "12": 242, "13": 262, "14": 281, "15": 296, "16": 315, "17": 331, "18": 352, "19": 368, "20": 384, "21": 400, "22": 416, "23": 435, "24": 450, "25": 467, "26": 484, "27": 503, "28": 520, "29": 540, "30": 564, "31": 580, "32": 602, "33": 619, "34": 635, "35": 651, "36": 666, "37": 681}
---

**Dave Jones:** Hi, you might remember 13 years ago I did a video on delusional Dyson marketing where this Dyson dustbuster-y thing, vacuum thing, um, the marketing on the box for this thing was that it saves the environment. Zero carbon emissions because it didn't have any carbon brushes inside the motor in this thing that produce carbon dust.

**Dave Jones:** Anyway, absolutely ridiculous, but turns out this thing has failed. Wah, wah, wah, wah. Mrs. EEVblog just ordered me to take a look at it. So, um, it does have a really cool dropout battery. So I have no idea if the actual units, like the motors died or whatever, or whether or not it's the battery or the charger or whatnot,

**Dave Jones:** but it does have a button on here and it just drops out. Look at that. And that's all in one. So we've got the charger built into the stem of the battery. I rather like that. So let's have a squiz here. We've got our two contacts on the top, which go to the motor,

**Dave Jones:** and we've got three contacts on the side here, unlabeled, so maybe a temp sensor or some other thing? Um, and yeah, there we go. We've got one of those weird-ass DC jacks on the thing coming from the charger. Specs are 22.2 volts. Ooh, that's high voltage.

**Dave Jones:** Um, that's quite unusual. 77 watt-hours, 3500 milliamp-hour lithium-ion jobby. So, ah, let's measure it. So 22.2 volts divided by 6 cells inside, that would give a nominal 3.7 volts per battery. So I assume it's a 6-cell construction. Well, you could probably count them, couldn't you?

**Dave Jones:** Um, are they 18650s? So yeah, that looks like an 18650 to me. And 1, 2, 3, yeah, 4, 5, 6. Yeah, that looks like 6 cells in there. So no wuckers. And by the way, this one's brilliant marketing. If you want marketing, check this out.

**Dave Jones:** It's going to catch on fire. It's trust fire. Trust that it's going to catch on fire. Don't think they thought that one through. So what do we get? Oh, yeah, 18.11 volts. That's just a smidge over 3 volts per cell. Um, that's no good.

**Dave Jones:** So we could have ourselves a dead battery pack here. But we could try and revive the thing, I guess. So let's plug in the charger. And there it is. What have we got here? Ah-ha, 24.35 volts. 24.35 divided by 6 on the confuser here,

**Dave Jones:** that's 4.06 volts per cell. So that sounds reasonable to charge that sucker up. I don't know why there's an additional one there. Oh, oh, there's an inner... Oh, it's a tri... What? It's a special doodaddy tri-ring thing? Are you serious? What? Yeah, yeah, there is a ring inside there,

**Dave Jones:** as well as the outer ring and the tip. Just the tip, ma'am. What kind of proprietary bullshit is that? Unbelievable. Anyway, let's stick it up the clacker and see if it charges. The green LED on the plug pack is on, but I know it doesn't charge because we've had it left on

**Dave Jones:** and it doesn't do anything. So, 19.2. There you go. And is that rising? It's rising. So, maybe... See, what do these other ones do? I'll leave that as a common. 11 millivolts. 8 millivolts. 11 millivolts, there's nothing on there. No, it looks like there's nothing relative on there at all.

**Dave Jones:** So, no, no, nothing on those, so I don't know what they do. So I'm not sure if there's, like, some charging circuitry in here or not, because we're not going to get this apart, it's all heat-sealed. Well, we could, but, you know, it's going to damage it.

**Dave Jones:** So yeah, we expect a constant current charge thing, but anyway, yeah, what the extra 13 volts? Volts, is that to power... what? No, I don't... why? What do we get on the inside? Oh, 26, did I get that backwards? Oh yeah, there you go.

**Dave Jones:** The inner ring is 16.7 and then 24.35. Yeah, so we're a bit higher. So, it looks like we're a bit higher on both. So it looks like this is an unregulated plug pack. And, yeah, so they must have the charging circuitry inside there for the lithium-ion,

**Dave Jones:** because you want your constant current curve and then your constant voltage curve to kick in. So my guess would be that the battery is dead-ski. Because these seem fine. I mean, they're not going to be out of regulation on both. Like, they're not going to...

**Dave Jones:** if they were, you know, fully regulated, then they're not just going to suddenly, you know, both go high like that. So, yeah, I would say that those are just nominal voltages on the plug pack, and this is unregulated. It's a bloody tri-axial thing.

**Dave Jones:** I don't have one of those. Like, I've got this style of jack. I've got, like, you know, 50 different adaptory things. I don't have a tri-axial one. So if I did, I'd be able to, like, charge this up externally. So I don't know if it needs the 13 volts there or whatnot.

**Dave Jones:** But, like, oh my god, seriously? Actually, it turns out that the different various adapters I've got, they're also tri-axial, so to speak, with the inner metal like that. And I've measured it, and that is actually isolated from the outer metal like that. So that is isolated.

**Dave Jones:** So it looks like they're all inherently tri-axial. Tri-axial? I've never really looked into the details of that. But, of course, I can't access that. But it's only co-axial out the clacker there, not tri-axial. So I can't actually get in and contact that. But I'll see if I've got one that matches.

**Dave Jones:** If I do have one, hey, one that fits. There you go. That might do the job. So I might try that. And if it doesn't need that 16 volts and only needs that 24 to charge the thing, then we could be right. It's worth a go.

**Dave Jones:** The battery's dead anyway, but if we can, like, rejuvenate it, that'd be cool. So let's just bump that up to 24 volts there. And let's just say, let's just half an amp, something like that. So let's give it a whirl. Got it around the right way.

**Dave Jones:** Yeah, I think so. Just do a sanity check there. There you go, 24 volts. All right, all right, let's go see if it can do anything. And we're in constant current mode. So we put in half an amp into there. You can see that.

**Dave Jones:** See that right there. I'm going to leave that for a bit and see if we can't rejuvenate this sucker, huh? Yeah, because those cells might have gone completely dead. There might be some protection circuitry in the cells or whatever. So yeah, maybe the plug pack doesn't have the grunt to get it going again.

**Dave Jones:** But it's a long shot, but it's worth it. I'll get back to you. Let's see what voltage we've got on there. 19.5. Okay, that's what we were getting before. No, we were getting 18 point something, weren't we? I can't remember exactly. But like, oh, it's rising.

**Dave Jones:** It's coming at a right angle. And it's going up. Run the numbers on that. So my guess here is that with the multiple voltages, the lower voltage, that 16 volts there, that just powers the internal circuitry inside the Dyson because it's going to have, I don't know,

**Dave Jones:** whiz-bang, you know, Dyson-y magic in there. And then the 24 volts just, like, goes straight from the motor to the battery, and that's it. And they couldn't be bothered putting a voltage regulator in there to do all they wanted. It's sort of proprietary, so you had to buy their, you know,

**Dave Jones:** whiz-bang tri-axial plug pack thing. I'll just leave it there for a while and just see if the batteries come back. It's been a couple of hours. I just, I wasn't monitoring much. I just came back, and I, look, 8 milliamps. Um, yeah? Okay.

**Dave Jones:** Did something go, did it go pop goes the weasel? 20.8 volts. There you go. Still not fantastic, is it? Oh, by the way, it just occurred to me that, um, given that there is the 16 volts in here, and we actually measured nothing on here,

**Dave Jones:** um, I don't know how that voltage gets through to the thing. It just seems odd that there's nothing there. So I've got the plug pack back in, and you can see that there's, like, there is nothing on here at all. So, like, where is, where is the 16 volts?

**Dave Jones:** So, like, yeah, I just don't get it. Like, it is on that circular thing. Where does it go? Does it, oh, is it for another product? Maybe, ah, maybe it's for a lower, right. I think I know what that is now. The plug pack could be compatible with two different voltage, uh, batteries.

**Dave Jones:** That's what it might be. That's what it might be, I think. Yeah, that makes sense. That makes sense. Okay, so we've got a 24 volt battery here, but there might be, like, a 16 volt version as well. So, yep, okay. I think that's what it might be.

**Dave Jones:** So, yeah. Anyway, 20.8 divided by 6 is only 3.5 volts. So, per cell. So, that ain't gonna work. No, wah, wah, wah, wah. No, I, I just don't think that this thing, I think the battery's gone, and, uh, this thing is just not gonna accept a charge properly.

**Dave Jones:** So, um, yeah, I think I'm just gonna have to get a new battery. I'm not gonna try and repack it. Like, as I said, this is probably, like, um, heat, heat sealed, I would suspect. I don't think there's any... No, that's probably, that's not a screw, I don't think.

**Dave Jones:** Be surprised if that's a screw under there. I think it's just the, uh, heat, uh, like the injection port for the plastic. Yeah, that looks like the plastic. Yeah, the battery is, uh, dead-ski. I mean, it is 13 years old. It's had a ton of use.

**Dave Jones:** Not every day, but yeah. I don't know how many hundreds or a thousand times we've used it or something over 13 years. So, yeah, I'll just get a new battery. Um, so it's a DC31. Uh, type A. Type A, not to be confused with type B, which is totally different.

**Dave Jones:** So, Dyson have a ton of different batteries. But I can pick up one of these. Um, they are still available, so it's still a thing. So, um, yeah, sorry, boring video. Um, yeah, it looks like this thing, this sucker, does not hold a charge at all.

**Dave Jones:** Um, and those batteries, just like 3.5 volts per cell. That's nut, nut. And you see the charge cut out there. So, um, yeah, there's just no point. No point. Ah, there you go. It's going again, but it'll just cut out again, I'm sure.

**Dave Jones:** And nut. Gone-ski. Anyway, that's it. Catch you next time.
