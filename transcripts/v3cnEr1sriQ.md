---
video_id: v3cnEr1sriQ
title: EEVblog #327 - Makerbot Replicator Troubleshooting
url: https://www.youtube.com/watch?v=v3cnEr1sriQ
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 31, "3": 48, "4": 61, "5": 76, "6": 84, "7": 98, "8": 112, "9": 125, "10": 137, "11": 154, "12": 171, "13": 186, "14": 194, "15": 215, "16": 228, "17": 239, "18": 257, "19": 277, "20": 292, "21": 307, "22": 322, "23": 336, "24": 364, "25": 382, "26": 396, "27": 424, "28": 439, "29": 450, "30": 462, "31": 481, "32": 493, "33": 515, "34": 530, "35": 545, "36": 554, "37": 566, "38": 579, "39": 586, "40": 599, "41": 608, "42": 620, "43": 633, "44": 642, "45": 664, "46": 692, "47": 711, "48": 724, "49": 736, "50": 749, "51": 764, "52": 777, "53": 789, "54": 801, "55": 824, "56": 836, "57": 858, "58": 879, "59": 892, "60": 904, "61": 917, "62": 927, "63": 942, "64": 961, "65": 972, "66": 985, "67": 995, "68": 1018, "69": 1032}
---

**Dave Jones:** Hi. If you've been following my tweets and on the forum, then you may have known that I had a few issues with my new MakerBot Replicator here. And um in the unboxing, I uh complained that I couldn't find the SD card where I finally did find it loose, hidden down under the flap in the bottom of the box just as I was about to throw it out.

**Dave Jones:** So, I thought, beauty, you know, I'll stick it in here. Don't know which way it goes up. And I'll print something from it. So, I printed what's um on here.

**Dave Jones:** It's got a spiral box example down here. So, I printed this one and this is what I ended up with. You can see it's it's printed the raft on the bottom properly and then it started to print the spiral box and then it went absolutely berserk.

**Dave Jones:** I wasn't here when it actually um did this. And uh you may recall that I did note that um it was you know violently shaking the machine while it was doing it.

**Dave Jones:** So maybe when they've uh rendered this spiral box example, I don't know, they've set it to like maximum speed or something like that. And the box was really shaking and vibrating and and I do have the rubber feet on it by the way.

**Dave Jones:** A few people uh complained, "Oh, I broke it because I didn't have the rubber feet on it." Anyway, what happened was I, you know, it failed to print this.

**Dave Jones:** Okay. Right. You get a failure. But then after that, it seemed to have permanently killed the Makeabot. Everything in the Y-axis was dead. So, I thought I'd uh troubleshoot this, see if I can fix it.

**Dave Jones:** Now, first of all, I'll try and get a shot of what the actual issue is. You'll notice the raft over here at this end up here. here. When it comes back, you'll see it, but it's supposed to be like a circle like at this end over here, but it's not.

**Dave Jones:** You can see that it's actually skipped like it's gone back like that. It's supposed to have a flat top and a flat bottom just like just like this here, right?

**Dave Jones:** It's supposed to look like that because it printed uh that good raft. This is I'm printed exactly uh the same thing. So, it's uh printed that good raft there, but it doesn't look like that.

**Dave Jones:** Now, you see it's all skewed in this Y direction back and forth here. It's it's uh completely bugged. And this is because it's going very slowly here. This is actually um doing quite well.

**Dave Jones:** Usually, it fails like like totally. And uh it's like halfway out in the Y axis. And here I've got it printing my microcurren uh case. And you'll be able to see in a second.

**Dave Jones:** Oh, see it's already skipped that line there. You see that square on the right hand side? That's not supposed to be there. It's already skipped a couple of centimeters in the Y direction.

**Dave Jones:** You can see those circles are supposed to be on top of each other. and they're not. And though and that cross in the middle there is not supposed to be there.

**Dave Jones:** And uh it's completely skipped. And you may be able to see some skipping on this axis perhaps. You've got to watch carefully. And it's only in the Y direction of course, but you might might be able to catch it perhaps.

**Dave Jones:** I don't know. It's hard. Anyway, it's definitely skipping in that Y direction. Total fail. Look at that. It's quite artistic though. I'll give it that. So, let's now have a look at this Y axis here.

**Dave Jones:** And of course, due to that rod going all the way under the back there. Of course, it's uh there's there's two sides to this thing. So, as I move it, here we go.

**Dave Jones:** As I move it manually back and forth like that, not only is there the belt on that side, but there's also the belt on this side as well, duplicating that, but of course the motor for the Y-axis is down in that corner and that vertical belt and that rod drives the other side over here.

**Dave Jones:** So, uh, my first thought of course was that, oh, okay, the belts, you know, slipped or something like that. But if I get in here, that is it's got the belt tensioner spring on there and that feels like absolutely ideal tensioning.

**Dave Jones:** There's no issue there at all. There's no seems to be no issue with the retention uh the belt retention clips down in here either. They they actually look like nothing's gone wrong there at all.

**Dave Jones:** And uh if I inspect these cogs and things up in here. You I you know I don't notice any issues at all with um any of the belts or anything like that.

**Dave Jones:** So really it's uh it's quite a bit quite puzzling what's actually going on here. And uh but it seems you know I push it back and forth here and the motor turns.

**Dave Jones:** no problems whatsoever. So, you know, I really um when I first looked at this thing, I was at a loss to uh figure out what was going on here.

**Dave Jones:** And you know, being an electronics engineer, naturally, my mind gravitated towards um you know, something happened to the motor controller and now it's not getting enough torque. due to the you know the violent uh nature that it was uh printing you know it was really shaking the machine and maybe causing you know some serious uh back EMF issues on the motor or something like that could have something could have gone

**Dave Jones:** wrong with the controller perhaps and uh I thought that you know that's the level that I would have to go down to but uh it's not I did actually find the issue and if you were keen uh eyed, you may have already spotted the problem.

**Dave Jones:** Now, what's happened here is I was cleaning out a few, you know, just little odds and ends from in here, and I uh noticed something down in one of the corners here.

**Dave Jones:** And you might recognize this little sucker. Well, hello there, Mr. Grubcrew. Now, ordinarily, you wouldn't expect to find a grub screw sitting on the base of a Makeabot. You thought, "Ah, you know, come straight from the factory, should work, and it was working until this thing was rather violently uh shaken by that test print on the SD card." So, I bummed around a bit more.

**Dave Jones:** What did I find? A second grub screw. So, I went and looked at all of these cogs, and you can see there's two grub screws in there for each one, and uh they all looked to be in place.

**Dave Jones:** And there's actually eight of these total on the two large rods which run the length of the MakerBot on the top of the unit here. And they're all in place.

**Dave Jones:** There were there's none missing whatsoever. So, I was wondering where these things had come from. And as it turns out, here's the motor. The cog attached to the motor.

**Dave Jones:** Tada! Two missing grub screws. They have clearly shaken themselves loose out of the motor. What? Gotcha. So, there it was. The culprit was down in the Y-axis motor there.

**Dave Jones:** And with hindsight, it's pretty darn uh easy and uh obvious that uh you know that was the case. And if you methodically troubleshooted this thing, u you probably would have found it.

**Dave Jones:** But I had a you know a 10-minute cursory glance around this thing and I didn't notice any grub screws missing. So, I was about to go on a jump off the rails and go on a campaign of, you know, ripping this thing apart and uh troubleshooting it, jumping on the forums trying to, you know, figure out if anyone else has had the same problems, whether or not there's motor

**Dave Jones:** current issues, cuz I had those in my previous Makerbot Fingeratic. I had uh those issues where you know it's it was a little bit uh touchy and uh the I had the wrong uh current drives as you probably saw in a previous video.

**Dave Jones:** And so naturally my mind was all you know jumping towards those sort of conclusions. But it was only by uh sheer chance that I happened to find uh you know a grub screw down in the bottom.

**Dave Jones:** And I eventually found the second one. If it uh you know fell down one of the uh one of the things in the corner there if I tilted the machine it would have rolled in there and I would have never found the thing.

**Dave Jones:** And they're they're only tiny. They're absolutely tiny. So they would have just been gathered up in the uh you know in the dust and crap on my bench and could have been tossed out.

**Dave Jones:** And really, it was uh I really didn't notice um that it was missing the grub screws in there at all. But there you go. It pays to have like a methodical uh procedure to thoroughly check out this thing.

**Dave Jones:** And it would have been easier if I built it cuz then I would have known and remembered that oh yeah, there were grub screws in there and yeah, you had to do them up tight, etc., etc.

**Dave Jones:** But because this thing I didn't build it unlike the Thingomatic. Um it you know I just expected it to work and not fail. So I don't know what the these things weren't done up tight enough.

**Dave Jones:** I'm not sure. Maybe they should put some Loctite in them perhaps. But the good news is the MakerBot does come with a whole bunch of Allen keys. So I found one that fitted.

**Dave Jones:** And uh really I should like print a little uh tool holder to hang on the side of this thing or something, you know, containing all the Allen keys and stuff to fix and maintain this thing to keep it in operational order.

**Dave Jones:** And if I check the other grub screws on the uh cogs on these uh dry shafts on the Y axis here, I can I can tighten those up a little bit.

**Dave Jones:** They certainly weren't fully tight. Not sure how tight you're supposed to do them up. But I could certainly some of them I could certainly do another half turn on them or thereabouts.

**Dave Jones:** Um fingertight. So really in my opinion that's not good enough for a consumer level machine like this. If you got to keep, you know, maintaining and massaging the thing with Allen keys, maybe putting your own Loctite on it or something like that, it, you know, it it's just not going to cut the mustard for them to be successful.

**Dave Jones:** And for this thing to be a robust consumer bit of kit, they need to do here is re-engineer these shafts just so that they're not uh smooth on the ends like uh actually get them machined or something uh so that the uh you know like so they have teeth on them so that they can slide into a a cog and they don't need those little uh grub screws

**Dave Jones:** on it to grip onto to a completely smooth round shaft like that because these things, you know, if these things will go for hundreds and thousands of hours of operation, these grub screws are going to come loose and just, you know, supplying an Allen key with it and maybe, you know, putting it, I don't know.

**Dave Jones:** I haven't read the manual. I haven't said anywhere. I haven't read anywhere about maintaining this thing. Maybe there is a page for it uh somewhere, but they don't include like a maintenance uh guide with it or anything, you know, a a preventative maintenance type guide uh in the box.

**Dave Jones:** So really, it really doesn't cut it. They need to re-engineer that solution. So it, you know, it just works and continues to work over the operational life of the unit.

**Dave Jones:** And the interesting part about this failure here is that really it failed on the only point in the system which can fail in that mode, the most vulnerable point.

**Dave Jones:** And what do you know? It failed at the most vulnerable point because on those grub screws on a round shaft, the Y-axis is particularly vulnerable because it has two here, two over in this corner, two in this corner here, and two over here.

**Dave Jones:** So there's eight, you know, there's five failure points in the y-axis system there to fail. There's only one failure point in the x-axis system. So, you know, statistically speaking, you'd expect that to fail less often.

**Dave Jones:** You know, it's obvious that it failed at that point, but it shouldn't have to. The damn thing was engineered properly. And we're all fixed up now. And we're printing the microcurrent case here.

**Dave Jones:** And with no raft, of course. And it's working. A treat. No more slippage in the Y direction. I think we got a winner. Check out the fine detail on the walls of this box.

**Dave Jones:** Absolutely brilliant. I love it. Well, my print's finished. And look down here. 84% complete. Sorry. So, what on earth is going on there? It's not like it has to wait another 16% of the time for it to cool down.

**Dave Jones:** It looks like it's not even uh uh switching off the heaters there. So, what's going on? My printer's finished. It's all done. All done and dusted. 84%. Jeez. Get your algorithm right.

**Dave Jones:** So, now I'm going to hit home axis and Oh, holy Oh, what's going on? Hang on. Quit this process. It just moves the platform up. What the hell? I I think it's going to continue to go back to home and probably destroy my print.

**Dave Jones:** I'm assuming I I'm pretty sure I've seen it do that before. So, yes, I want to quit this process. This is crazy. Yes, finished. Okay, let me move this down manually and uh scrape it off first and then print the home and then do the home button.

**Dave Jones:** Huh. All right, I've taken my print off and uh let's do that home thing again. And I I had to cancel the print, by the way, because it still had 16% left even though it was finished.

**Dave Jones:** And uh so maybe there's a bug there where if your home axis uh uh before it's actually finished and after you uh cancel it. So let's see what I'll do.

**Dave Jones:** Home axis. Here we go. So it's going up and imagine that print was still on there. Okay. Bang. Bang. It probably would have went right through my print there.

**Dave Jones:** And um who knows what damage it would have maybe it didn't wouldn't have done damage but it would have hit my print and maybe moved it off axis or it could have damaged the print if it was delicate.

**Dave Jones:** That's just that's crazy. They need to work on these little things like that that just ruined the experience. But anyway, here is the final print. And that's my first one that's really worked well with no raft on the bottom.

**Dave Jones:** You can see how relatively smooth that is. Actually really quite smooth. You can still see all of the little uh you know, you can see the printed bottom on it, but that is that feels really smooth because it was on the um capped bed there.

**Dave Jones:** And that's that is really worked a treat. And this is a beautiful beautiful print. Just look at all those. Well, I've looked at these before. You know, I've showed you these before, but the thin walls, brilliant.

**Dave Jones:** And uh let's have a look at the uh the microcurrent printed on the surface there. It's still a little bit little bit, you know, dodgy over here, but jeez, that's that's pretty good.

**Dave Jones:** I mean, you know, it's not up to a commercial case, uh injection molded case. I mean, it's nowhere near it, but just got the little daggies here. So, I just ripped those off.

**Dave Jones:** But uh that is an absolutely beautiful print. Ah, I love it. So, my Makeaker replicator is certainly back in business. Beauty. And uh so I that was just a little troubleshooting video there and getting it uh back up.

**Dave Jones:** If you want to discuss it, jump on over to the EE blog forum. And if you like the video, please give it a big thumbs up. Catch you next time.

**Dave Jones:** [Music]
