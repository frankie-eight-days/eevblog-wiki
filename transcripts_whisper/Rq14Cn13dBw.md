---
video_id: Rq14Cn13dBw
title: EEVblog #1204 - Samsung Galaxy Fold Failure - Analysis
url: https://www.youtube.com/watch?v=Rq14Cn13dBw
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 17, "2": 37, "3": 55, "4": 77, "5": 97, "6": 108, "7": 126, "8": 145, "9": 150, "10": 171, "11": 184, "12": 201, "13": 228, "14": 243, "15": 261, "16": 281, "17": 298, "18": 310, "19": 327, "20": 346, "21": 360, "22": 373, "23": 391, "24": 406, "25": 414, "26": 431, "27": 444, "28": 458, "29": 474, "30": 491, "31": 499, "32": 515, "33": 533, "34": 551, "35": 570, "36": 588, "37": 607, "38": 620, "39": 641, "40": 653, "41": 671, "42": 682, "43": 701, "44": 710, "45": 730, "46": 747, "47": 760, "48": 779, "49": 796, "50": 808, "51": 820, "52": 836, "53": 850, "54": 867, "55": 880, "56": 897, "57": 916, "58": 929, "59": 940, "60": 953, "61": 970, "62": 987, "63": 1000, "64": 1015, "65": 1030, "66": 1046, "67": 1064, "68": 1076, "69": 1094, "70": 1113, "71": 1130, "72": 1149, "73": 1158, "74": 1179, "75": 1198, "76": 1214, "77": 1223, "78": 1239, "79": 1256}
---

**Dave Jones:** Hi, one of my viewers wanted me to talk about the new Samsung Galaxy Fold, which is this newfangled $2,000 smartphone that folds open like this. You have it closed, it's like a regular large-ish, thick-ish smartphone, and you fold it open and it becomes a tablet.

**Dave Jones:** Very cool technology. Hats off to all the design engineers at Samsung who've made this thing work. But, unfortunately, it has been failing spectacularly in the hands of reviewers. They've just, like a week ago or something, and all these reviewers, all the screens started to fail on it.

**Dave Jones:** And it's just launched in the stores, but they have now announced that, no, they're going to delay it while they investigate this thing. So, it's been a huge marketing and technical fail right off the bat. Incredibly embarrassing. Now, normally I wouldn't talk about these newfangled smartphone machines.

**Dave Jones:** And gadgety things. I didn't know anything about this. I really don't care about newfangled smartphone and gadget releases and stuff like that. As impressive as this technology is, it looks absolutely fantastic. But there's two reasons I wanted to talk about this. One is because it's an interesting, from an engineering point of view, how and why something like this failed.

**Dave Jones:** And two is actually from a YouTube reviewer's point of view. Because I'm technically a YouTube reviewer. I do reviews. One thing, granted I do it on, if you haven't watched me before, I do, like, engineering test equipment, oscilloscopes, multimeters, and other sorts of test gear, and a few other little gadgets, occasionally, reviews.

**Dave Jones:** So, I wanted to talk about that first before we get to the engineering stuff. Now, because somebody asked me to take a look at this, I thought, oh, I know nothing about this Galaxy Fold thing, I'll have a look at a few things.

**Dave Jones:** And this particular video popped up from a YouTube reviewer, an incredibly popular one, 8.5 million subs. Wow, I've never really watched any of his stuff, I don't know. The first thing I heard of him was he was in the YouTube rewind video when Will Smith said, like, his name, and jumped over, whatever.

**Dave Jones:** You know, if I controlled rewind, I would want Fortnite and Marques Brownlee. Right, uh, Marques Brownlee. Hi, Marques, if you're watching this, good day. Done a review and unboxing video, but he's also done a more recent one, and I'll link it in down below, how, how, explain how these things are failing.

**Dave Jones:** So, I started to look at the screen protector, and I was like, why, and things like that, and something caught my attention. Listen to this. Screen protector. So I start peeling it up, and within a couple seconds, you start to realize, like, it's a little, it's more well-glued than a normal screen protector.

**Dave Jones:** He's trying to peel up the screen, screen protector. And then, by the time I get to an area the size of, like, a dime in, like, five seconds, the whole screen just goes black. And then, like, this little area, there's, like, a stripe, and then the top left corner starts flickering.

**Dave Jones:** Uh, that's definitely not good. I'm like, I really just broke it? Like, I feel like such an idiot, and I, I kind of regret that I didn't get to keep that footage because it's on camera, literally, as I'm peeling it, the screen goes black.

**Dave Jones:** Listen to that again. Like, I feel like such an idiot, and I, I kind of regret that I didn't get to keep that footage because it's... I kind of regret that I didn't get to keep that footage, is the quote. And the YouTube reviewer in me goes, what the?

**Dave Jones:** Like, you didn't get to keep it? Who stole your footage? The footage fairy? Uh, like, yeah. Okay. He obviously, he's a professional reviewer. He shot this footage. It's his. He owns the copyright on it. He can show it. There's only two reasons that I can think of, from a YouTube reviewer's point of view, why you, why he's not going to show this footage.

**Dave Jones:** A, he was either under some sort of contractual obligation. B, he was either under some sort of contractual obligation to Samsung to let them either review or vet footage beforehand, or something like that, or maybe they requested to him that he not show this footage.

**Dave Jones:** Or B, he voluntarily decided, I'm not going to show this footage because it may look bad for Samsung, and I don't want to ruin our good relationship. That gets me all these, you know, review units ahead of time and stuff like that. And being an 8.5 million...

**Dave Jones:** And being an 8.5 million sub, I believe this is what he does. He does, he reviews gadgets and things, um, and stuff like that. Yeah, he doesn't want to damage his relationship with Samsung. Either one of those is, is not good. I, from a YouTube, uh, reviewer's point of view, I reckon both of those things are a bad option.

**Dave Jones:** I reckon he should show the footage. That's just ridiculous. Anyway, let, I can't think of another reason why he would not show the footage. It's got to be one of those two reasons. Anyway, let us know what you think down below. But anyway, I'm sure Marcus, uh, has his reasons.

**Dave Jones:** Anyway, from a YouTube reviewer's point of view, I just heard that, and that sounded interesting. So, enough of that. Let's get on to the more technical stuff. So, naturally, this, uh, OLED display screen that Samsung has spent years developing, we'll get into that.

**Dave Jones:** It's actually more than a few years, uh, with a folding OLED screen, right? It's the first one. Folding screens aren't particularly new, or bendable screens aren't particularly new. But I believe this is, like, the first. One in a, like, a real important mass, high-end, high-volume consumer product like this.

**Dave Jones:** This is a $2,000 flagship smartphone slash smart tablet. I'm sure someone will come up with a wanky word for it. But this is as serious a product as you'll get in our business from one of the top-tier manufacturers, Samsung. And it's failing in the hands of reviewers.

**Dave Jones:** Like, this isn't like the Samsung battery thing, like, from a couple of years back. Where it was out for quite some time before, like, the first, uh, Samsung phone, Galaxy phone, caught on fire. And then, you know, I'll write it off as a one-off.

**Dave Jones:** These things happen, right? A lot of energy density in modern batteries and stuff like that. And they have to pass stringent, uh, testing, like the nail test, where they put a nail through it and short out all the layers inside the battery. It's gotta pass that without catching on fire.

**Dave Jones:** Yet, somehow, these Samsung batteries, uh, caught on fire. And that was a real big deal. They had to recall all these phones and fix the problem. And they mass-tested it. And it was all better, and everything's good again. That sort of stuff happens when you have, uh, like, really, like, small tolerances in manufacturing.

**Dave Jones:** Small manufacturing variability. And when you sell things in large enough volume, that manufacturing bell curve, you're gonna get these outliers. And it took some time, and shipping, I don't know how many hundreds of thousands or millions of these units, before that sort of problem was discovered.

**Dave Jones:** But in this case... On my timeline, like, all next to each other in a row within minutes. Are other reviewers with the Galaxy Fold saying, "Hey, my screen broke too." "Oh yeah, my screen broke too. Mine too." All these reviewers. Boom, boom, boom, boom, boom.

**Dave Jones:** All next to each other. So I'm reading this all thinking, "Oh, I didn't realize that I wasn't the only one." But now we have all the information about the couple Galaxy Folds that had problems. So, of the four Galaxy Folds that broke in the last two days, uh, these are the reasons why they broke.

**Dave Jones:** So, the first one, Dieter's. He never messed with the film on the display, but it did start to develop this bulge for some unknown reason. Like, something got under the film somehow, and that bulge eventually, a day later, killed the screen, giving it these stuck pixels.

**Dave Jones:** Then, number two, Steve Kovach. He also didn't mess with the film, but I look at the photos that he sent before he's sending the phone back to Samsung, and it doesn't look fully intact, so it might have taken some damage somehow, but either way, it clearly did not survive.

**Dave Jones:** And it looks like half the display is going completely... Look at this. Look at these problems. ...completely insane. Then, number three, Mark Gurman's. He actually tweeted, "The phone comes with this layer that he thought was a protective film. He peeled the entire thing off, so it must have survived that peeling, but that did pretty quickly cause the death of the screen, which slowly over the..."

**Dave Jones:** So, there you go. We've had, like, maybe half a dozen or so files from these reviewers, and there's more reports than Marquez's, uh, showing here. And a couple of them were due to, including Marquez's one, of peeling off this so-called, uh, protection film, which is

**Dave Jones:** not a protection film. It's designed like it's a proper layer on the screen, but it was, like, not glued on well enough that you would think it's there, and I don't blame them for doing that. I probably would have done a very similar thing.

**Dave Jones:** And since, uh, the reviewers found this problem, apparently the ones that they, the few that they have shipped, have now had this warning label on it that says, "Do not peel this off," and "Do not..." It's only a small print, so maybe they need to make it,

**Dave Jones:** you know, huge, or do something else to ensure that users don't do this. But anyway, they've decided, apparently, to, uh, stop shipping. Uh, the thing, it's on hold, it's delayed worldwide, uh, we don't know for how long. Pulling them from the shelves, and you won't be able to, you can't buy them, or you won't be able

**Dave Jones:** to buy them. So you have all these failures in the hands of reviewers. So as I said, unlike that battery thing that happened out in the field once millions of units have shipped, this is like, they sent out, what, a few hundred of these to reviewers, or something like that, and like, what, 10% of them are

**Dave Jones:** bailing, or 5 or 10%. This is insane, how they can spend so many years. In fact, they've been doing this for more than eight years. I'll show you this. Phys... physics, uh, dot org, from, uh, May 2011. "Foldable display shows no crease after a hundred thousand folding cycles." This is from

**Dave Jones:** Samsung Advanced Institute of Technology. They've been working on this, just the display, just this folding mechanism. For eight years, they've been working on this thing, and they, of course, have done, uh, these folding tests, and they do these automated tests like this, and this is very common in industry.

**Dave Jones:** I've designed and built and worked on jigs like this for various, uh, production testing of connectors and other things, like this hinge that moves, but it's one thing to, uh, test on this jig, but it's another thing entirely to actually have it in the

**Dave Jones:** hands of a user. I know somebody did a video of where they folded it a thousand times, and it was just fine. Yeah, they have actually tested this, and they spent eight years developing this, and even eight years ago, they folded it a hundred thousand times, and it was fine.

**Dave Jones:** So, what's the deal? Well, and A, these jigs never really replicate what a user is going to do and abuse this thing, because it doesn't... these jigs are purposely engineered, and you can actually see it. And I'm sure the mechanical engineers can go to town here, but, like, you can, like, there's

**Dave Jones:** different methods to actually fold something like this, which either, uh, puts less stress or more stress, or tries to even simulate, uh, you might have a bit of variability in your jig to try and simulate users, especially when you're testing connectors, which I've done before.

**Dave Jones:** If you have a jig that's perfectly aligned, and you made it perfectly each time, that doesn't really simulate it. You want to, sort of, it a bit loosey-goosey to, sort of, simulate how users actually try and, sort of, force it in, even at one degree difference, or something like that.

**Dave Jones:** Can make the difference between 5,000 cycles and 1,000 cycles, uh, for example. So, all the mechanical engineers, if you are one who, uh, has experience, um, in these folding, uh, type jigs, please let us know. But really, you can't beat the four-year-old test.

**Dave Jones:** Just giving it to a four-year-old or give it, like, I can't believe that Samsung, like, the engineers must have played, everyone must have played with this. The engineers, the management should have given it to the, uh, receptionist and said, "Here, have this for a week and see if you can

**Dave Jones:** break it." They should have given it to the cleaner or whatever. "Oh, whack this in your back pocket and fold it, open it a couple of hundred times and go around and do your job and see if, see if it fails. Let us know." And surely, it, they would have found these.

**Dave Jones:** If it, if, like, half a dozen fail in the hands of reviewers in the first day or two, why this didn't show up before is, uh, yeah. The thing is, this must have shown up before. I can't believe they've released it and all of a sudden, oh, they said, "It could

**Dave Jones:** be a bad batch." Granted, there could have been something wrong with this first batch. All the previous ones might have passed all the, all the tests, not only the, uh, the formal mechanical jig test like this, but it could have, uh, passed all the, uh, like, user tests within the company or, you know,

**Dave Jones:** things like that. And then they might have just had a bad batch. That's possible, but after working on this for eight years and they had it nailed, they reckon they had it nailed 100,000 tests eight years ago. Okay. So, I'm not, I'm not buying that.

**Dave Jones:** I, I think, potentially, they probably knew about potential issues like this. So, yeah, and coming out with that warning, like, straight away within, like, days of these reports, yeah, something, something smells a bit fishy. So, if I actually have a look at a typical

**Dave Jones:** configuration for a foldable OLED display like this, they're actually quite complicated. This is from 3M and I, I'll have to link it down below. There's, like, touch sensors, there's cover windows, there's polarizers, there's, like, transfer barriers, like, cathode emission layer, the anode, that's the actual, uh, display down there and

**Dave Jones:** things like that, right? Very complicated thing to get this to fold, uh, reliably, hence, you know, the eight years of research before they actually released a product here. But they're talking about things like, uh, you know, shear, uh, forces and things like that.

**Dave Jones:** So, when you're, uh, this is, uh, to do, would have to do with the peeling off. If you're trying to peel off and there's a lot of force and you're trying to overcome that glue and stuff like that, you're, you're peeling off those top layers in there.

**Dave Jones:** Could, there's the shearing stress or whatever. I'll let the mechanical engineers explain better and I'm sure they will in the comments and over on the EUVblog forum down below, but you're going to get shear stress on there. It's not just about the folding.

**Dave Jones:** And did they test for that sort of stuff? Obviously not, because Marquez, like, and others have just peeled it off and boom, it failed. So, others have reported peeling off and there weren't any problems, but then a couple of days later, it failed.

**Dave Jones:** And then they're talking about, uh, uh, actually, interestingly, the jigs, the dynamic bend test, uh, jigs and things like that. And there's different ways to actually implement these. I won't pretend to know the mechanical, uh, physics behind here. We always, at my companies, we always have

**Dave Jones:** mechanical engineers to sort of advise on, uh, this sort of, you know, stuff. Whereas I'd come up with the more random, like, oh yeah, you want to just plug it in randomly? I can, I can do a jig that wobbles. No worries. Uh, and hinge design is important.

**Dave Jones:** And whereas a single hinge or a mandrel bending and all that sort of stuff, max strain versus fixed distance, whether or not it keeps like a certain separation in there. And, and there's many sorts of things involved in these sorts of, uh, bend tests.

**Dave Jones:** So I'm, I'm sure it passed that with flying colors, but I can't believe that they didn't have any other issues with inside Samsung. Uh, I, I think they knew it could potentially be a problem and whether or not the engineers spoke up and, hey, I think we've got an issue.

**Dave Jones:** And they went, no, we've been working on this for eight years. We have to push this out now. And like, yeah, we're going to take the Marcus by storm. We have to be first. Maybe they got rumor that somebody else was going to beat them to the folding, uh, smartphone-y phablet thing.

**Dave Jones:** I don't know. But anyway, it's really interesting and you wouldn't expect something like this to be super rugged. And I watched one, uh, reviewer skip through and I heard him mention that the first thing I thought about this is that this is not rugged.

**Dave Jones:** You've got to treat it. It's delicate. And they're saying they've actually held it in their hands and go, yeah, this doesn't really like paraphrasing, you know, instill a lot of confidence in me in terms of the robustness. It felt quite delicate and like, you've got to treat it gently and stuff like that.

**Dave Jones:** And well, that's always going to happen with this sort of like Samsung are leading the way here. So, hey, they should have done this. They should have released it, but for it to fail, this is incredible, like in the hands of reviewers and so

**Dave Jones:** many of, if it was one, it was just a simple manufacturing defect. Two, Samsung would be worried. But more than that, it's, there's obviously some sort of systemic problem and to have them actually, uh, pull this from the shoals. A lot of people are asking, well,

**Dave Jones:** how long is it going to be delayed? Well, look, they've been working on this for eight years. They thought they had it leaked. Many, at least management thought they had it leaked. Otherwise they would not have released this thing and sent it to reviewers and started to sell them.

**Dave Jones:** So it's a huge deal to sell a groundbreaking new product, world beating product like this. It's a massive deal. So they were so confident that they went ahead with it. But as it turns out, they come a gutser completely. How long is it going to take them

**Dave Jones:** to like, it's, nobody knows at this stage, I don't believe. It's unlikely that you'll get a comment on them when they're going to actually, uh, potentially release, re-release this thing and fix the problems. But look, working on it for eight years, it would

**Dave Jones:** take at least unless they knew about it. As I suspect, I think some people in Samsung know about this and they go, uh, yeah, the first thing they'll go to the engineers and what's causing this and the engineers will go, oh, well, it was in the report I wrote six months ago, right?

**Dave Jones:** Here it is. Here's the data. This is why it failed. And, uh, but even then to then, uh, fix the manufacturing issues, which they either knew about and didn't fix before, or something brand new could entirely be something brand new. And it could be, you know, they did their best practice and,

**Dave Jones:** and they thought they were good, but failed it and then happens. So it could be that, but yeah, anyway, let's, let's just assume that they know instantly what caused the problem. And they have to engineer a new production solution or some other solution.

**Dave Jones:** Maybe it could be a slight variation in the manufacturing of how the, you know, the screen layers and stuff, uh, you know, are gone together. Maybe there's some slight variation in that they can tweak in that, uh, process there that like fixes the problem.

**Dave Jones:** And by the way, the, those folds that we're seeing, those little bulges, they're obviously due to peeling of the different layers and stress. I can't believe it's the folding stress because they've tested this, you know, unless there's some drastic variation between the jig and humans actually doing this.

**Dave Jones:** And some little combination of some of the layers, some users are just getting it just right that it causes, uh, like delamination for one of a better term of these particular layers. And I think that's what we're seeing with some of these phones here.

**Dave Jones:** So yeah, I think that's what we're seeing, uh, here, the layers are like delaminating up and that's what causes the systemic fire, uh, either due to the sheer force of pulling that protector off or due to some other folding mechanism. Uh, it's, I think we've got layer

**Dave Jones:** so maybe they can tweak something there. Maybe they can't, if they have to re-engineer this whole thing from scratch, it's going to be months and months just to re-engineer this. Then it's going to be another month or two to thoroughly test it again, minimum, minimum.

**Dave Jones:** And then they, then they'll want a closed review cycle, probably. Uh, they'll get in, I don't know who they'll get in, even the existing reviewers. I, I would get in these existing reviewers, most definitely. I'd give it to them and say, here, do exactly what you did before and even more to it and try and break it.

**Dave Jones:** Again, so I, I can't see them getting this back on the market for four to six months, minimum. So yeah, I wouldn't, uh, hold your breath trying to get a new game, you know, Samsung Galaxy Fold anytime soon. I, there's just, unlike the battery problem, this thing is, wow, it's just out of the

**Dave Jones:** gate. This is just like having the Melbourne Cup, for example, which is a huge horse race here in Australia, if you didn't know. Anyway, it's world famous. Anyway, 20 horses lined up in the barriers. They're all already ready to go. They go out and a couple of them just fall on their arse straight out of the gate.

**Dave Jones:** And like three or four of them fall on their arse. That's exactly what happened here. And it's nuts. So that's, that's really embarrassing. So I feel bad for the engineers at Samsung, who've obviously worked on this for a long time. They've done an incredible job.

**Dave Jones:** This looks like an amazing product. It's probably not something I'd, I'd use on a daily basis, but I can understand why people are going, wow, about this. And it's $2,000 and you expect it to work and wow, you don't even know. Anyway, they've come a gutter.

**Dave Jones:** So yep, don't expect to see it anytime soon, is my prediction. So there you go. Let us know what you think down below. If you have experience in these foldable jigs and even foldable OLED displays, my audience is vast and wide. Let us know in

**Dave Jones:** the comments or over on the EEVblog forum. Anyway, if you like the video, as always, give it a big thumbs up and you can discuss down below on the EEVblog forum or in the comments. Catch you next time. Bye.
