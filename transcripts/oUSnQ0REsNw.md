---
video_id: oUSnQ0REsNw
title: EEVblog #447 - Samsung Plasma Followup
url: https://www.youtube.com/watch?v=oUSnQ0REsNw
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 25, "3": 47, "4": 65, "5": 81, "6": 94, "7": 106, "8": 125, "9": 136, "10": 145, "11": 159, "12": 171, "13": 190, "14": 202, "15": 220, "16": 231, "17": 252, "18": 263, "19": 281, "20": 293, "21": 310, "22": 322, "23": 333, "24": 344, "25": 366, "26": 381, "27": 394, "28": 407, "29": 419, "30": 433, "31": 442, "32": 455, "33": 465, "34": 483, "35": 494, "36": 504, "37": 522, "38": 535, "39": 548, "40": 566, "41": 580, "42": 590, "43": 605, "44": 621, "45": 641, "46": 652, "47": 667, "48": 682, "49": 699, "50": 709, "51": 736, "52": 759, "53": 782, "54": 800, "55": 818, "56": 827, "57": 838, "58": 849, "59": 861, "60": 873, "61": 883, "62": 897, "63": 905}
---

**Dave Jones:** Hi, this is just going to be a quick follow-up on this Samsung plasma TV because I wanted to test a few more things. Didn't have enough time last time, so we'll check this sucker out, shall we?

**Dave Jones:** See if we can at least get an external signal working. So, let's give it a go. Now, the problem last time was that none of the analogy type inputs worked at all.

**Dave Jones:** The component video didn't work, the S-video didn't work, the VGA didn't work, and but I didn't try the HDMI. So, I'm going to try the HDMI and now and also a lot of people suggested it might be something incredibly simple that was just due to the blue screen mode that I had turned on.

**Dave Jones:** So, we'll disable that and we'll give it a go. Now, I've got the thing plugged in now. Now, this one this board is completely safe to touch because it is isolated from the mains supply and you'll notice that they have a high voltage warning sticker up here.

**Dave Jones:** That is for the rest of all of the circuitry which we saw last time under there. That's all the high voltage stuff. You do not want to go poking around in that, but all this all, you know, low voltage 3 1/2 V 5 V stuff all mains isolated, so it's completely safe.

**Dave Jones:** So, that's why they have the warning sticker on this part and then a separate removable panel on here. It just allows servicing and repair on just the completely safe side of the thing.

**Dave Jones:** That's just a little safety aside there. Now, I've got this thing turned on and it is actually powered up and if I do the old back of the finger test, I mean that chip there is getting quite warm.

**Dave Jones:** Let's zoom in on that. Let's see how back of the finger test. This one is yo, hot, hot, burny, burny, burny. Um, that's the one the main Samsung BGA part there.

**Dave Jones:** That's just the memory there. That's another some sort of video processor. A little bit warm. That's the HDMI panel link. That's doing nothing. It's a little bit warm. This one's here.

**Dave Jones:** Not a problem. So, we're just searching for any parts that are particularly hot. Now, this one um a few people commented that it looked like it may have been out.

**Dave Jones:** Um, so we'll take a a closer look at that under the times 10 macro lens, but it's it's warm. So, it's powered up, but you know, it's certainly not It's getting warmer warmer warmer.

**Dave Jones:** So, I don't know if that's normal for that device. I have to check the data sheet. And oh, that one's That one's pretty hot. Geez. We'll have to check out what that one is.

**Dave Jones:** And the others not really a problem. So, let's take a close-up look at that one. As I noted in the previous video, it seems to be the decoder for all of the analog inputs down here, the component, the S-video, the RGB, and all that sort of stuff because all of these AC coupling caps down here.

**Dave Jones:** And you can just see all the traces flow from there into there. And possibly this chipset down here as well. But that one we're interested in. So, let's take a look at the data sheet for that one.

**Dave Jones:** I couldn't get the precise Philips data sheet, but I did get a second source one here from Trident Semiconductor. And no surprises. It's a 10-bit video decoder with comb filter and component video for studio quality ADC 16 analog inputs.

**Dave Jones:** And And I can link this in to the notes down in there. But it's you know, it's got all sorts of It's got the composite video input. It's got the um RGB inputs.

**Dave Jones:** It's got the component uh inputs and everything you'd expect. All that all those inputs which aren't working. So, it's you know, a fair guess that that chip that there's something wrong with that chip in there because we know that all the video processing around here all works cuz it's driving the panel just fine.

**Dave Jones:** So, uh rather than troubleshoot that right now, first thing I'm going to do is buy essentially bypass uh that chip by not using the analog inputs but using the digital um HDMI input.

**Dave Jones:** That'll go through the separate um uh HDMI uh processor here and uh presumably uh you know, directly into the processor up there. So, let's plug in HDMI. See if it works.

**Dave Jones:** All right, here we go. Plugged it into my notebook down here before HDMI and uh as before got that blue screen. We'll switch that off in a minute, but uh let's change our source.

**Dave Jones:** Down here, you ready? Ta-da! There you go. It works a treat. As expected, HDMI works fine. Now, we'll still check check that uh blue screen thing to make sure that's not an issue, but there we go.

**Dave Jones:** We bypassed that uh video um analog video decoder chip and went uh straight through the HDMI and that is perfect. I mean, there's no um dead pixels. There's nothing.

**Dave Jones:** It doesn't quite go right to the edge uh down there, but that that is beautiful. That works just fine. I love it. Let's uh play a video on on here.

**Dave Jones:** See if the audio and everything works. It's quieter down here. It's got Ta-da! There you go. Working a treat and the audio's as you can hear is coming through the TV.

**Dave Jones:** No problems. Beautiful. We have a winner, folks. Check it out. Okay, I've turned off the blue screen mode and note the PC input does not work and yes, I've set it to the lowest resolution possible, 800 by 600.

**Dave Jones:** If it can't do that, seriously, it does not work. So, the VGA input is definitely cactus. But, folks, woohoo, check this out. I am getting something on the composite video input now.

**Dave Jones:** I've got one of these VGA to composite converter box boxes which is generating the color bars there, but it's it's flickering. Check that out. So, I don't know whether or not that's normal.

**Dave Jones:** I haven't used this box before, but um it Yeah, I don't know whether or not that's the TV or the box outputting something, but I can't seem to make it um you know, stable or anything like that.

**Dave Jones:** So, I don't know if that's a fault with the TV or the generator box. No, blue screen mode's on. So, there you go. I'm So, it wasn't that. So, I'm not sure why it suddenly decided to work.

**Dave Jones:** This is the same box I was using yesterday to uh test this thing. So, I don't know what the deal is there, but composite is working. So, that means that chipset is actually processing something at the very least.

**Dave Jones:** I mean, it can't do that. A lot of complexity involved in doing that. It's not like I don't think part of the chip's going to fail with the VGA input.

**Dave Jones:** So, not entirely sure what the issue is. And what do you know, it does actually work a treat. So, that was that box generating a non-compatible composite signal in some way.

**Dave Jones:** I've got it now hooked up to a old DVD player with the composite output and uh it's working a treat. So, I don't know why that wasn't working the other day.

**Dave Jones:** This thing has suddenly decided to work. Did I actually press on the chip or do something uh weird like that? It is one of those um BGA chips, so you know, I presumably um I can only uh think that I did actually make the chip come good.

**Dave Jones:** Maybe it does have a uh dry joint on one of the balls underneath the BGA or something like that. Maybe we can try some freezer spray. So, what I'm going to do now is freeze this uh BGA chip to see if it does anything.

**Dave Jones:** Don't have any freezer spray here in the lab, but the next best thing, air duster. You've seen this before. Just turn it upside down, instant uh cold freezer spray.

**Dave Jones:** Let's go. Let's see if I can get in here and here we go. I'm going to hit that BGA chip. Let's see what happens. No. The chip's going all frosty.

**Dave Jones:** I've got Frosty the Snowman on that BGA chip, and it's holding in just fine. Not a problem. And if you want to have a look, it's still cold. Here we go.

**Dave Jones:** Oh, no, it was it was cold for a second there, but uh this is what it looks like when you freeze it. You get all the frost on the chip like that, and uh there you go.

**Dave Jones:** It's nice and cold, and it's still working. And just to show you that uh blue screen mode, you can see there's no signal. It's turned off, disconnected. It's got the blue screen uh there, and you switch it on, and it just automatically should Hello.

**Dave Jones:** There we go. Automatically uh switch. There you go. Look, we've got some Check check that out. That is not a clean signal anymore. So, what's going on there? It was before.

**Dave Jones:** You saw it before. It was absolutely perfect. Now, we've got this color There's some sort of color tearing across there. I'm not sure what the correct term for that is, but you can see it.

**Dave Jones:** Hopefully, you can see that. Yeah, you can definitely see that on the screen. There's that color tearing on the display across here and down here as well. So, I'm not as as it is something wrong with this thing, but it seems intermittent.

**Dave Jones:** So, at least we got the thing uh going. I'm not entirely sure why. Maybe I'll hit it with some more uh freezer spray and uh see what happens. No.

**Dave Jones:** Let's try in the general vicinity. Like the electrolytic caps and uh stuff like that. No. No, it's still got some tearing on there. So, there you go. That is very interesting.

**Dave Jones:** If you've got any good ideas about what's possibly going on there, then uh uh uh no. See, it was good there for a second and then it and then it's doing it again.

**Dave Jones:** So, if you've got any idea what's going on there, I mean, chipping Clearly, the uh decoder chipset is working just fine cuz you wouldn't get that um unless, you know, as I said, you can't get like a partial fire on that chip or anything like that.

**Dave Jones:** That's, you know, that's really not um feasible at all. So, ooh, your guess is as good as mine. So, this is one sick puppy here. Let's plug the HDMI back in and uh it does it auto detect?

**Dave Jones:** No, it doesn't auto detect, but I can uh switch the source there. And there we go. Nothing wrong with the HDMI, so um yeah, I don't know. Something's intermittent on this sucker and uh but the HDMI works fine, which makes this a very still a very usable set.

**Dave Jones:** I mean, you use it I mean, ideally, you want to be using the HDMI input uh for the best uh quality anyway, so it's a winner as far as that works.

**Dave Jones:** The audio and video, absolutely first class for this what 8-year-old uh plasma display, 2005 uh model and um uh which according to uh uh people complaining on the web, this particular model has very high failure rate uh and was uh very expensive uh to repair after the warranty period, which presumably was like a 12 months for your standard warranty unless you got one of those extended warranty things.

**Dave Jones:** And no, the component video is not working either. I'm generating my component signal. It's actually detecting that there's a component input there and it's uh enabling that particular channel when you cycle through the source here, but um I've got a component uh device which is generating component out and uh zip.

**Dave Jones:** Now, there are a few people who suggested that uh this uh Philips SAA711 9 uh video decoder chip looked a bit uh burnt or something like that. It had some physical uh damage and I've got to admit, I can actually see sort of the shape of the die um underneath it, but it doesn't get that uh hot and of course, it's uh working as we uh saw.

**Dave Jones:** It's at least doing something. So, there's certainly no uh physical damage to the chip and it yeah, it does look a bit sort of, you know, thermally stressed, I guess you could say, but I think that's just a uh natural part of the uh this particular package anyway.

**Dave Jones:** So, I mean, clearly, there's uh nothing uh physically wrong with it because it does actually work. Now, Trevor from the uh Television Mag forum, he commented that I should probably do a service factory reset mode in the service menu on this thing, but I don't have the service cable that plugs in the back of it.

**Dave Jones:** Couldn't be bothered making one up, don't know how it works. And from what I'm reading, you can enter the service mode via the remote control. So, I don't have a remote for it.

**Dave Jones:** So, we'll probably go out and get a remote now because it does seem to work. It seems to be useful, at least it's certainly in the HDMI mode, not a problem.

**Dave Jones:** So, if you got any ideas what's actually going on with this sucker, I'm sure it's something to do with that chipset, that main decoder chipset, but the freezer spray didn't seem to do anything.

**Dave Jones:** Bit surprised by that. I expected something to happen there, I guess. There was a good chance of that, but I don't know. I need a remote to enter do the factory reset.

**Dave Jones:** Maybe that'll help. Maybe there's nothing physically hardware wrong with it. Maybe it just needs a factory reset, you know, the I squared C codes going to that decoder chip or something to reset it.

**Dave Jones:** Who knows? Anyway, I think it's an absolute winner. Beauty. I'm going to not sure what I'm going to do with it cuz I don't have a stand, so I can't just take it home and whack it in the lounge room and replace my other one.

**Dave Jones:** So, it's either I try and get a stand for it or mount it on a wall somewhere. Could even mount on the wall here in the lab, perhaps. Well, that bloody thing weighs 50 kilos, so mounting it on one of these cheap rock walls, I don't know.

**Dave Jones:** And I've had a few people comment, do I always have bare feet around the lab? Do I always work in bare feet? Yeah, pretty much. It's much more comfortable.

**Dave Jones:** But occasionally, I do wear Australian safety boots. Pair of thongs. Beauty.
