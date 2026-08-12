---
video_id: 6TYtdpbFWuA
title: EEVblog 1677 - Why Do Fuses Do This? (EXPERIMENT)
url: https://www.youtube.com/watch?v=6TYtdpbFWuA
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 26, "3": 35, "4": 53, "5": 66, "6": 81, "7": 99, "8": 109, "9": 135, "10": 148, "11": 164, "12": 177, "13": 187, "14": 202, "15": 213, "16": 227, "17": 236, "18": 252, "19": 264, "20": 278, "21": 291, "22": 303, "23": 317, "24": 329, "25": 346, "26": 356, "27": 366, "28": 376, "29": 386, "30": 398, "31": 411, "32": 425, "33": 442, "34": 452, "35": 469, "36": 483, "37": 496, "38": 511, "39": 520, "40": 532, "41": 551, "42": 563, "43": 581, "44": 596, "45": 616, "46": 629, "47": 640, "48": 652, "49": 663, "50": 678, "51": 693, "52": 703, "53": 712, "54": 720, "55": 729, "56": 738, "57": 747, "58": 758, "59": 767, "60": 779, "61": 787, "62": 803, "63": 812}
---

**Dave Jones:** Hi, I'm still working on the video part two of the unpredictability of fuses. I'll link in part one if you haven't seen it down below. It's very very interesting.

**Dave Jones:** Set up a little thing here. I've just modified the meter so that I can test the new 630 milliamp fuses that are in the BM225 multimeter as opposed to the old 400 milliamp fuses I did in the previous video.

**Dave Jones:** Anyway, I did some testing and I was getting rather confusing results that didn't quite match the data sheet. And then I realized that I had an old data sheet.

**Dave Jones:** So I asked them for a new data sheet and there's actually significant differences in the data sheet. They don't actually have the 630 milliamp one here. So I specifically asked them for the 630 milliamp data sheet and I got that, but what they sent me is the latest data sheet which is exactly the same fuse.

**Dave Jones:** Nothing's changed. It's the HV620 series, but take a look at these graphs. These are changed. Yes, they have actually added an extra decade here down below, but if you chop that off which is basically what they've done here and they've added an extra decade here.

**Dave Jones:** So they've just sort of like zoomed in a little bit, but you can see that these characteristics have actually changed. These characteristic curves. Take for example the 500 and 600 milliamp fuse characteristic curves.

**Dave Jones:** You'll see that they actually cross over down here. The characteristics actually cross over, but over here 500 milliamps, they haven't crossed over. And likewise for the 2 amp and 1.6 here, you can see that they don't cross over until right down here.

**Dave Jones:** But 2 amps and 1.6 they cross over right up here. So these are different characteristic curves for exactly the same model fuse. Just you know, like four years apart.

**Dave Jones:** I think this is 2020. This is 2024. No surprise really because manufacturers of fuses are constantly tweaking their metallurgy constantly tweaking their secret source cuz every fuse manufacturer has their own secret source of materials that go into manufacturing the fuse wire and and not just the materials, but also how they anneal them or whatever they do at the you know, mechanical level to physically manufacture the wires.

**Dave Jones:** So they all have their own secret source and they're always just constantly refining their characteristic curves whether it's slopes like this, whether it slopes like that. By the way, if you have it more the more vertical it gets the more unpredictability you get.

**Dave Jones:** You want to sort of make them like that. So I don't know, maybe they've changed you know, anyway, they have tweaked their processes and they can use a ton of different materials to do these things like tin, lead, copper, silver, nickel, zinc, chromium, aluminum, magnesium.

**Dave Jones:** All these types of different materials. They can blend these together to produce different types of fuses and how they react. So and not to mention the physical as I said, the physical manufacturing of them.

**Dave Jones:** So sometime in this last four years they've actually changed the materials in here. So this got me to thinking something that I read about like donkey's years ago, way back.

**Dave Jones:** I think it was in Electronics Australia. I'm not sure. If anyone knows, leave it in the comments down below. I read about how you can actually change the characteristics of fuses by thermally shocking like permanently change the characteristics by thermally shocking them.

**Dave Jones:** And I thought I'd actually test that here considering I've got the setup all ready to go. So that's what we're going to do in this video. We're going to thermally shock some of these fuses and see if we can get it to permanently change their characteristics.

**Dave Jones:** See if we can measure any difference. It's going to be interesting. Let's go. So this is the characteristic for the 630 milliamp fuse we've got. I'm going to pick a time that's like you know, if we can get it to like break in 10 seconds or something like that cuz I don't want this video to go on forever.

**Dave Jones:** But these are just nominal curves. They're not guarantees. You don't know what the actual physical spread on these is. So I'll just experiment a bit. Pick a nice value.

**Dave Jones:** Okay, 1.5 amps. Here we go. Boom. And oh, 1.8 seconds. Okay. Oops. And we can also measure the resistance of the fuse here. I'm not doing a four wire compensation or anything, but that's going to be good enough for Australia.

**Dave Jones:** That just it gives us a ballpark to see if thermally shocking these fuses changes their resistance at all because it's all a relative measurement anyway. All right, let's try 1.45 amps.

**Dave Jones:** Boom. Oh. Oh, that one blew straight away. Bugger. Well, that's the unpredictability of fuses for you. Let's try 1.45 amps again, shall we? There you go. That one's lasting a bit better.

**Dave Jones:** Yeah, that other one was just an outlier. So 1.15 volts. Well, that was 21 seconds. So yeah, I reckon that's all right. Somewhere in there. That we've probably got the two extreme ends of the curve there.

**Dave Jones:** So what I've got here is three random fuses out of my batch here. All these 630 milliamp jobbies. And I put a red mark on them just so I don't get them mixed up and we'll go whack these in the freezer.

**Dave Jones:** Oh, all right. I've gone for four wire resistance measurement here. So I've got the extra sense wires connected directly across here like this. If you want to see the board, it's just the 121GW multimeter and I've just bridged the fuse over there.

**Dave Jones:** So the fuse is basically between the amps and milliamps jack there. There's nothing else in circuit. That residual resistance there is just the power supply and the timer which are in parallel here.

**Dave Jones:** So let's measure five fuses. .49 .5 .49 .495 So they're all fairly consistent, aren't they? But this is just the cold DC resistance of course. The fuse wire the fuse wire heats up.

**Dave Jones:** What our ballpark is. Now, let's go get the ones out of the freezer and see what they're like. So I've had the fuses sitting in my little lab freezer here.

**Dave Jones:** You can see them down there. Yes, I've got a couple of ice blocks there and let's measure the temperature this. Should be about -15 or something like that. Yep.

**Dave Jones:** Yep, you can just see the outline in there. So they've gotten to the temperature of the freezer. -15 -17, whatever. Anyway, we've thermally shocked shocked those little suckers. Let's test them.

**Dave Jones:** Don't know if you can see that, but they're a little bit frosty. But yeah, like they don't have to stay cold like that, but yeah, they're still at Anyway, you can see that the minimum 8° there.

**Dave Jones:** So they've they've come back pretty quick. So it doesn't matter whether we test them frozen or not. We're testing whether or not we've physically permanently changed the alloy in there.

**Dave Jones:** Bloody lights. All right, let's just get a control fuse in there. .487. You know, they're all around about that figure there. There's another 1.476. Now let's get one of the frozen ones here and let's actually put that in there.

**Dave Jones:** And look, not not .384 ohms. Wow. Wow, that's crazy. And I'm thermally like warming those up. Those aren't really cold anymore. So it's not just the my permanent marker's rubbing off.

**Dave Jones:** It's not like just a regular thermal response of these things. It's like seriously um .385. Same. What the heck? Last one here. See if that's exactly the same and .387.

**Dave Jones:** They're all exactly the same. What the heck? And as I said, we're not just talking about the regular thermal response here. The actual rating of the fuse is a nominal one at you know, regular ambient of 20° C.

**Dave Jones:** So it will actually scale based on that, but these are back at room temperature now, but they seem to have permanently lowered their resistance. And if they lower their resistance I assume that's going to change the like the melting point of this thing.

**Dave Jones:** There's something that's happened to the metallurgy in here by freezing it that's permanently changed that. So that should I think anyway, we'll test it now, translate into a actual breakage current.

**Dave Jones:** Let's try it. Okay, frozen fuse. Well, no longer frozen, but went through a thermal cycle. Let's whack it in there and let's time it at the same 1.45 amps constant current that we had before.

**Dave Jones:** So let's do that. Where Where at a volt? Was it What was it? 1.3 volts before? That's what you'd expect with a lower a lower effective resistance of the fuse.

**Dave Jones:** And it's Is Is that going up? Is that heating up? It's not. Now, based I've been doing fuse testing for the last day or two um mucking around with them trying to get various results.

**Dave Jones:** And I know that I've had some of them running at like overnight at like uh previously I was running these overnight at like 1.1 amps I think it was and it didn't break at all.

**Dave Jones:** And they from memory I think were around about a volt. So there you go. I I don't think that is going to break at all. It's just not near the breaking voltage which of course you know, V squared on R is going to heat up internally and then the metallurgy of the fuse inside breaks it.

**Dave Jones:** But 1 volt is not going to I'm pretty confident I can leave this for hours and that is not going to break. That is permanently changed. We'll try another one here.

**Dave Jones:** Let's whack that in and yeah, reset. But whoa. Whoa, that's .676. What the heck? That is super low. Wow, we're getting 1 volt on the other one. Seems to be some variability.

**Dave Jones:** This one is definitely never going to blow. And we'll get the third one. Let's whack that in. .68. Oh, what was wrong with that first one then? I I was the first one that I had.

**Dave Jones:** So, let's whack that back in and try it again. 9.9. Okay. So, there is a significant Yeah, that one's Okay. So, one out of three, but still that is like that's never going to blow at 1.45 amps.

**Dave Jones:** We're going to have to go higher. Going to put one of those lower reading ones back in and I'm going to adjust the current 1.65 amps. That would definitely instantly blow any of the traditional ones.

**Dave Jones:** So, let's give that a go. 9.8. No. No, that is never going to blow. That is never going to blow. We have permanently changed that. Wow. All right, I'm going for broke.

**Dave Jones:** 2 amps. Let's see if we can blow it at 2 amps. Oh, yeah, we might we might get it to blow at 2 amps. Come on. Come on. You can do it.

**Dave Jones:** You can do it. No. We We won't see the magic smoke escape, but yeah, this is a 630 milliamp fuse. The other ones have a snowball's chance in hell of surviving uh 2 amps.

**Dave Jones:** They'd last for like a millisecond before they blow. And this one is doing holding 2 amps. No problems whatsoever. Wow. Oh, she she just blew at 53 seconds there.

**Dave Jones:** 53 seconds at 2 amps. That's incredible. And just as one last experiment, I'll get a brand newie from the box unfrozen. So, no thermal shocking. 1. Now, let's wind it back to 1.6 cuz 2 is just going to blow so instantly.

**Dave Jones:** This one probably only will last a second or something. So, let's go. Yep. Oh, I didn't reset that properly. But yeah, you saw it there. It it just blew straight away.

**Dave Jones:** There you have it. That is amazing. Other brands, other models like all bets are off. Leave it in the comments down below if you want to experiment with this.

**Dave Jones:** But freezing fuses like that can permanently alter the current. You know, if you've got like a 1 amp fuse in stock, but you need like a 2 amp jobbie.

**Dave Jones:** Well, you might just be able to just freeze the thing and then it permanently changes the alloy in there somehow. Sorry, I'm not a metallurgist. I've got no idea.

**Dave Jones:** Any metal metallurgist in the comments, please leave it in the comments down below how you think this is happening. But unfortunately, we don't know the secret sauce that they're using in those few fuse wires.

**Dave Jones:** But there you go. So, that old thing I heard about about freezing fuses, thermally shocking them. I don't know if you can thermally shock them the other way. Heat them up.

**Dave Jones:** I don't know if you want to try that. Leave your results down in the comments down below. But freezing those fuses and shocking them can change the characteristic curve, even move it like this.

**Dave Jones:** I don't know if the slope still stays the same. Of course, you would have to extensively test this. It's a huge amount of time and effort and expense to actually get these curves.

**Dave Jones:** But whether or not it changes the slope like that or whether you know, it's but it's obviously at least shifted it up like that. Like and it seems permanently cuz these were back at room temperature.

**Dave Jones:** So, there you go. A fascinating effect. If you know, I don't know if there's a name for this kind of effect. If there is, I don't know. I I hereby name it the Jones effect for fuses.

**Dave Jones:** If there isn't an existing name, handy little tip. Next time you're in a dire need cuz I don't recommend this as like a proper technique. But if you're in a pinch next time, maybe you can chuck your fuses in the freezer and get a higher current rating out of them.

**Dave Jones:** Who knew? Unbelievable. Anyway, might do. Leave it in the comments down below if you want me to do more experiments on this. But that is a fascinating insight, is it not?

**Dave Jones:** Anyway, if you like that video, please give it a big thumbs up. As always, discuss down below. Catch you next time.
