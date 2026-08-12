---
video_id: v3cnEr1sriQ
title: EEVblog #327 - Makerbot Replicator Troubleshooting
url: https://www.youtube.com/watch?v=v3cnEr1sriQ
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 26, "3": 44, "4": 61, "5": 76, "6": 88, "7": 102, "8": 114, "9": 133, "10": 152, "11": 171, "12": 188, "13": 202, "14": 221, "15": 236, "16": 251, "17": 266, "18": 282, "19": 303, "20": 326, "21": 343, "22": 357, "23": 372, "24": 389, "25": 413, "26": 430, "27": 444, "28": 460, "29": 483, "30": 498, "31": 511, "32": 528, "33": 543, "34": 552, "35": 566, "36": 581, "37": 593, "38": 606, "39": 617, "40": 633, "41": 648, "42": 662, "43": 678, "44": 695, "45": 709, "46": 719, "47": 734, "48": 751, "49": 764, "50": 782, "51": 797, "52": 816, "53": 829, "54": 848, "55": 867, "56": 885, "57": 900, "58": 917, "59": 930, "60": 945, "61": 961, "62": 975, "63": 990, "64": 1014, "65": 1025}
---

**Dave Jones:** Hi. If you've been following my tweets and on the forum, then you may have known that I had a few issues with my new MakerBot Replicator here. And um in the unboxing, I uh complained that I couldn't find the SD card where I

**Dave Jones:** finally did find it loose, hidden down under the flap in the bottom of the box just as I was about to throw it out. So, I thought, beauty, you know, I'll stick it in here. Don't know which way it goes

**Dave Jones:** up. And I'll print something from it. So, I printed what's um on here. It's got a spiral box example down here. So, I printed this one and this is what I ended up with. You can see it's it's printed the raft

**Dave Jones:** on the bottom properly and then it started to print the spiral box and then it went absolutely berserk. I wasn't here when it actually um did this. And uh you may recall that I did note that um it was you know violently shaking the

**Dave Jones:** machine while it was doing it. So maybe when they've uh rendered this spiral box example, I don't know, they've set it to like maximum speed or something like that. And the box was really shaking and vibrating and and I do have the rubber

**Dave Jones:** feet on it by the way. A few people uh complained, "Oh, I broke it because I didn't have the rubber feet on it." Anyway, what happened was I, you know, it failed to print this. Okay. Right. You get a failure. But then after that,

**Dave Jones:** it seemed to have permanently killed the Makeabot. Everything in the Y-axis was dead. So, I thought I'd uh troubleshoot this, see if I can fix it. Now, first of all, I'll try and get a shot of what the

**Dave Jones:** actual issue is. You'll notice the raft over here at this end up here. here. When it comes back, you'll see it, but it's supposed to be like a circle like at this end over here, but it's not. You

**Dave Jones:** can see that it's actually skipped like it's gone back like that. It's supposed to have a flat top and a flat bottom just like just like this here, right? It's supposed to look like that because it printed uh that good raft. This is I'm

**Dave Jones:** printed exactly uh the same thing. So, it's uh printed that good raft there, but it doesn't look like that. Now, you see it's all skewed in this Y direction back and forth here. It's it's uh completely bugged. And this is because

**Dave Jones:** it's going very slowly here. This is actually um doing quite well. Usually, it fails like like totally. And uh it's like halfway out in the Y axis. And here I've got it printing my microcurren uh case. And you'll be able

**Dave Jones:** to see in a second. Oh, see it's already skipped that line there. You see that square on the right hand side? That's not supposed to be there. It's already skipped a couple of centimeters in the Y direction. You can see those circles are

**Dave Jones:** supposed to be on top of each other. and they're not. And though and that cross in the middle there is not supposed to be there. And uh it's completely skipped. And you may be able to see some skipping

**Dave Jones:** on this axis perhaps. You've got to watch carefully. And it's only in the Y direction of course, but you might might be able to catch it perhaps. I don't know. It's hard. Anyway, it's definitely skipping in that Y direction.

**Dave Jones:** Total fail. Look at that. It's quite artistic though. I'll give it that. So, let's now have a look at this Y axis here. And of course, due to that rod going all the way under the back there. Of course, it's uh there's there's two

**Dave Jones:** sides to this thing. So, as I move it, here we go. As I move it manually back and forth like that, not only is there the belt on that side, but there's also the belt on this side as well,

**Dave Jones:** duplicating that, but of course the motor for the Y-axis is down in that corner and that vertical belt and that rod drives the other side over here. So, uh, my first thought of course was that, oh, okay, the belts, you know, slipped

**Dave Jones:** or something like that. But if I get in here, that is it's got the belt tensioner spring on there and that feels like absolutely ideal tensioning. There's no issue there at all. There's no seems to be no issue with the

**Dave Jones:** retention uh the belt retention clips down in here either. They they actually look like nothing's gone wrong there at all. And uh if I inspect these cogs and things up in here. You I you know I don't notice any issues at all

**Dave Jones:** with um any of the belts or anything like that. So really it's uh it's quite a bit quite puzzling what's actually going on here. And uh but it seems you know I push it back and forth here and the motor turns. no

**Dave Jones:** problems whatsoever. So, you know, I really um when I first looked at this thing, I was at a loss to uh figure out what was going on here. And you know, being an electronics engineer, naturally, my mind gravitated towards um

**Dave Jones:** you know, something happened to the motor controller and now it's not getting enough torque. due to the you know the violent uh nature that it was uh printing you know it was really shaking the machine and maybe causing

**Dave Jones:** you know some serious uh back EMF issues on the motor or something like that could have something could have gone wrong with the controller perhaps and uh I thought that you know that's the level that I would have to go down to but uh

**Dave Jones:** it's not I did actually find the issue and if you were keen uh eyed, you may have already spotted the problem. Now, what's happened here is I was cleaning out a few, you know, just little odds and ends from in here,

**Dave Jones:** and I uh noticed something down in one of the corners here. And you might recognize this little sucker. Well, hello there, Mr. Grubcrew. Now, ordinarily, you wouldn't expect to find a grub screw sitting on the base of a Makeabot. You thought, "Ah, you know,

**Dave Jones:** come straight from the factory, should work, and it was working until this thing was rather violently uh shaken by that test print on the SD card." So, I bummed around a bit more. What did I find? A second grub screw.

**Dave Jones:** So, I went and looked at all of these cogs, and you can see there's two grub screws in there for each one, and uh they all looked to be in place. And there's actually eight of these total on

**Dave Jones:** the two large rods which run the length of the MakerBot on the top of the unit here. And they're all in place. There were there's none missing whatsoever. So, I was wondering where these things had come from. And as it turns out,

**Dave Jones:** here's the motor. The cog attached to the motor. Tada! Two missing grub screws. They have clearly shaken themselves loose out of the motor. What? Gotcha. So, there it was. The culprit was down in the Y-axis motor there. And with hindsight, it's

**Dave Jones:** pretty darn uh easy and uh obvious that uh you know that was the case. And if you methodically troubleshooted this thing, u you probably would have found it. But I had a you know a 10-minute cursory glance around this thing and I

**Dave Jones:** didn't notice any grub screws missing. So, I was about to go on a jump off the rails and go on a campaign of, you know, ripping this thing apart and uh troubleshooting it, jumping on the forums trying to, you know, figure out

**Dave Jones:** if anyone else has had the same problems, whether or not there's motor current issues, cuz I had those in my previous Makerbot Fingeratic. I had uh those issues where you know it's it was a little bit uh touchy and uh the I had

**Dave Jones:** the wrong uh current drives as you probably saw in a previous video. And so naturally my mind was all you know jumping towards those sort of conclusions. But it was only by uh sheer chance that I happened to find uh you

**Dave Jones:** know a grub screw down in the bottom. And I eventually found the second one. If it uh you know fell down one of the uh one of the things in the corner there if I tilted the machine it would have

**Dave Jones:** rolled in there and I would have never found the thing. And they're they're only tiny. They're absolutely tiny. So they would have just been gathered up in the uh you know in the dust and crap on my bench and could have been tossed out.

**Dave Jones:** And really, it was uh I really didn't notice um that it was missing the grub screws in there at all. But there you go. It pays to have like a methodical uh procedure to thoroughly check out this thing. And it would have been easier if

**Dave Jones:** I built it cuz then I would have known and remembered that oh yeah, there were grub screws in there and yeah, you had to do them up tight, etc., etc. But because this thing I didn't build it unlike the Thingomatic. Um it you know I

**Dave Jones:** just expected it to work and not fail. So I don't know what the these things weren't done up tight enough. I'm not sure. Maybe they should put some Loctite in them perhaps. But the good news is the MakerBot does come with a whole

**Dave Jones:** bunch of Allen keys. So I found one that fitted. And uh really I should like print a little uh tool holder to hang on the side of this thing or something, you know, containing all the Allen keys and

**Dave Jones:** stuff to fix and maintain this thing to keep it in operational order. And if I check the other grub screws on the uh cogs on these uh dry shafts on the Y axis here, I can I can tighten those up

**Dave Jones:** a little bit. They certainly weren't fully tight. Not sure how tight you're supposed to do them up. But I could certainly some of them I could certainly do another half turn on them or thereabouts. Um fingertight. So really in my opinion that's not good

**Dave Jones:** enough for a consumer level machine like this. If you got to keep, you know, maintaining and massaging the thing with Allen keys, maybe putting your own Loctite on it or something like that, it, you know, it it's just not going to

**Dave Jones:** cut the mustard for them to be successful. And for this thing to be a robust consumer bit of kit, they need to do here is re-engineer these shafts just so that they're not uh smooth on the ends like uh actually get them machined

**Dave Jones:** or something uh so that the uh you know like so they have teeth on them so that they can slide into a a cog and they don't need those little uh grub screws on it to grip onto to a completely

**Dave Jones:** smooth round shaft like that because these things, you know, if these things will go for hundreds and thousands of hours of operation, these grub screws are going to come loose and just, you know, supplying an Allen key with it and

**Dave Jones:** maybe, you know, putting it, I don't know. I haven't read the manual. I haven't said anywhere. I haven't read anywhere about maintaining this thing. Maybe there is a page for it uh somewhere, but they don't include like a

**Dave Jones:** maintenance uh guide with it or anything, you know, a a preventative maintenance type guide uh in the box. So really, it really doesn't cut it. They need to re-engineer that solution. So it, you know, it just works and

**Dave Jones:** continues to work over the operational life of the unit. And the interesting part about this failure here is that really it failed on the only point in the system which can fail in that mode, the most vulnerable point. And what do

**Dave Jones:** you know? It failed at the most vulnerable point because on those grub screws on a round shaft, the Y-axis is particularly vulnerable because it has two here, two over in this corner, two in this corner here, and two over here.

**Dave Jones:** So there's eight, you know, there's five failure points in the y-axis system there to fail. There's only one failure point in the x-axis system. So, you know, statistically speaking, you'd expect that to fail less often. You know, it's obvious that it failed at

**Dave Jones:** that point, but it shouldn't have to. The damn thing was engineered properly. And we're all fixed up now. And we're printing the microcurrent case here. And with no raft, of course. And it's working. A treat. No more slippage in

**Dave Jones:** the Y direction. I think we got a winner. Check out the fine detail on the walls of this box. Absolutely brilliant. I love it. Well, my print's finished. And look down here. 84% complete.

**Dave Jones:** Sorry. So, what on earth is going on there? It's not like it has to wait another 16% of the time for it to cool down. It looks like it's not even uh uh switching off the heaters there. So,

**Dave Jones:** what's going on? My printer's finished. It's all done. All done and dusted. 84%. Jeez. Get your algorithm right. So, now I'm going to hit home axis and Oh, holy Oh, what's going on? Hang on. Quit this process. It just moves the platform

**Dave Jones:** up. What the hell? I I think it's going to continue to go back to home and probably destroy my print. I'm assuming I I'm pretty sure I've seen it do that before. So, yes, I want to quit this process. This is crazy.

**Dave Jones:** Yes, finished. Okay, let me move this down manually and uh scrape it off first and then print the home and then do the home button. Huh. All right, I've taken my print off and uh let's do that home

**Dave Jones:** thing again. And I I had to cancel the print, by the way, because it still had 16% left even though it was finished. And uh so maybe there's a bug there where if your home axis uh uh before

**Dave Jones:** it's actually finished and after you uh cancel it. So let's see what I'll do. Home axis. Here we go. So it's going up and imagine that print was still on there. Okay. Bang. Bang. It probably would have went right

**Dave Jones:** through my print there. And um who knows what damage it would have maybe it didn't wouldn't have done damage but it would have hit my print and maybe moved it off axis or it could have damaged the print if it was delicate. That's just

**Dave Jones:** that's crazy. They need to work on these little things like that that just ruined the experience. But anyway, here is the final print. And that's my first one that's really worked well with no raft on the bottom. You can

**Dave Jones:** see how relatively smooth that is. Actually really quite smooth. You can still see all of the little uh you know, you can see the printed bottom on it, but that is that feels really smooth because it was on the um capped bed

**Dave Jones:** there. And that's that is really worked a treat. And this is a beautiful beautiful print. Just look at all those. Well, I've looked at these before. You know, I've showed you these before, but the thin walls, brilliant. And uh let's

**Dave Jones:** have a look at the uh the microcurrent printed on the surface there. It's still a little bit little bit, you know, dodgy over here, but jeez, that's that's pretty good. I mean, you know, it's not up to a commercial case, uh injection

**Dave Jones:** molded case. I mean, it's nowhere near it, but just got the little daggies here. So, I just ripped those off. But uh that is an absolutely beautiful print. Ah, I love it. So, my Makeaker replicator is certainly back in business.

**Dave Jones:** Beauty. And uh so I that was just a little troubleshooting video there and getting it uh back up. If you want to discuss it, jump on over to the EE blog forum. And if you like the video, please

**Dave Jones:** give it a big thumbs up. Catch you next time. [Music]
