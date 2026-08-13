---
video_id: -q21AfxS1LY
title: EEVblog #270 - µCurrent Test Jig
url: https://www.youtube.com/watch?v=-q21AfxS1LY
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 32, "3": 52, "4": 68, "5": 85, "6": 101, "7": 117, "8": 133, "9": 145, "10": 161, "11": 186, "12": 202, "13": 218, "14": 234, "15": 251, "16": 267, "17": 279, "18": 295, "19": 311, "20": 327, "21": 339, "22": 376, "23": 396, "24": 420, "25": 440, "26": 457}
---

**Dave Jones:** Hi, I'm here testing microcurrents. You've seen this before in one of my raw videos. I showed the process of testing these microcurrents, and yes, I made another couple of big batches of them. And I always said that I'd probably do a proper test jig one day if the volumes got high enough,

**Dave Jones:** and well, I've already done 150 of them, or 100 of them, and I didn't even bother to, you know, do a jig for that sort of volume. It's, ah, just got to the point where, ah, what the hell, I'll just sit down for a couple of hours and test these things.

**Dave Jones:** But it's getting rather annoying, having to connect and disconnect the things, getting sore fingers, I get little shards of metal and fiberglass and all sorts of things over my fingers, and it's just really rather annoying. So I thought I'd just build a simple jig, because

**Dave Jones:** I've gotten down to a point where most of my time is actually spent connecting up the microcurrent like this, and I've got to do that. I do it in batches of 50. Why? Well, it's a nice round number, and 50 seems to fit nicely

**Dave Jones:** in this little area where I can just have them loose and then I can test them. And I go through three times, because it's got three different ranges on this thing. It's not really um, I don't want to wear out my test gear, so I'm not going to go

**Dave Jones:** and change the knobs for each unit three times, that's ridiculous. So what I do is I put it on one range, I set one range on my current, constant current generator, and I go through and measure all 50 on that range, and then I switch the current range, I go through

**Dave Jones:** measure all 50 again, and I do it again. So you can't really optimize the time it takes for things like inserting the battery and tightening up the connectors and doing a visual inspection and stuff like that. But I can I think optimize the time that requires

**Dave Jones:** to, like it only takes a couple of seconds to do this, but you do this a thousand times, it gets a little bit annoying. So I thought I'd just make up a little test jig to where I can just come along with the board, press it on, and take the readings.

**Dave Jones:** So how much time can I save? Well, it's probably not going to be a huge amount because, you know, the difference between inserting and removing some connectors and just pushing it down on a jig is probably not going to be a huge amount.

**Dave Jones:** But it saves, it's just nicer, it saves a lot of wear and tear on the fingers and hassle. So I don't expect a huge amount, but let's try and measure it. So I've already inserted my battery, I've tightened the connectors, I've given it a visual inspection, so let's go.

**Dave Jones:** Here we go. It's on the correct range, plug it in, and that is within spec. Happy with that. Disconnect, and bingo. That's it. Put it over there, stop. 15 odd seconds or so, you know. So I think we can maybe, you know, slash that

**Dave Jones:** down to 5, maybe. That actually might be significant, especially if you're making hundreds or if you're making thousands of things. So let's try and build up a jig. Now with a good lot of products that have to be tested, they will just have input and output connectors

**Dave Jones:** like this. So there's no test pads or anything on the bottom, I don't have to access the circuit. In this case it's just here and here, so really, I want a jig that automatically takes some banana plugs like this and inserts them into here.

**Dave Jones:** So I want them to line up here and here and just push it down in a jig like that that makes contact on either the bottom here or the top. I'm not too fussy on that, so it doesn't, it makes sense on the bottom

**Dave Jones:** because I can use some banana plugs like this and they can make contact, you know, make reasonably good contact with those bottom ones. But these top ones, they got, you know, they don't have the hole in them. So it probably makes sense to actually have my jig come in from the top.

**Dave Jones:** So I actually plug my, if my jig is sitting on the bench like this, let's say this is my jig and it's got the connectors sticking out of it, like this, I would probably take my board, stick it upside down, and plug it in like that so that these can make contact

**Dave Jones:** with the banana plugs. And I just hold it in place, I don't have to push it all the way on. It's good enough just to hold it there for a couple of seconds while you take the measurement and put it off. Bang, bang, bang.

**Dave Jones:** And of course the first thing you might think of is get a box like this and put in some banana plugs or some pogo pins or other test probes or something like that. But why? It's very common to use the existing board of your product, because it's already got the

**Dave Jones:** holes aligned for you, everything's there. So what we'll do is we'll just use an existing reject board for our test jig. This one's got a big silkscreen blotch on it, check that out. So, you know, can't sell that one. So what we'll do is we'll use that and we'll use the

**Dave Jones:** actual product case itself, and we'll just get some banana plugs and we'll solder them in there like that at the correct height, and bang! It'll just go on there. And you'll notice that these two connectors are of course different heights here, so I'm going to have to, my jig has to have

**Dave Jones:** these banana plugs at each end at different heights. So all I've got to do is measure the height difference there and ensure that I solder them. You know, the ones at one end actually stick out further than ones at the other end. So there we have it.

**Dave Jones:** I've soldered some 4mm banana sockets on there, and wired them straight through to the post like that. So here's my completed jig. It didn't take very long at all. All it does is duplicates the connectors and just allows me to press fit a board on top.

**Dave Jones:** So, I think we're going to save some time here. Let's try it out. I've got my board, battery's inserted, and I've tightened up the connectors, done my visual check, everything's fine, let's go! It's on the correct range, plug it on, hold it in place, bingo!

**Dave Jones:** It's within spec. Done. Ah, 10 seconds. So we shaved 5 off, but we could probably do that in 5. Let's try it again. What the heck. Let's go. Here we go. Ready? Bang, bang, bang, fine, boom, stop. Yeah, 5.7 seconds. You know, jeez, I should have done that

**Dave Jones:** 500 units ago. Crazy. But there you go, there's a simple, just not automated, but a nice little test jig that allows you to test products like this when you're manufacturing them in the hundreds or even the thousands. Really, to automate it even more than this,

**Dave Jones:** I, you know, it's really hard to do. So pretty much, gotten down to the point where it's completely optimized now. Testing the microcurrents. Beautiful. So there you go. So there you go. Got to finish testing these 50 units, and if you liked the video,

**Dave Jones:** give it a thumbs up. Helps a lot. Catch you next time.
