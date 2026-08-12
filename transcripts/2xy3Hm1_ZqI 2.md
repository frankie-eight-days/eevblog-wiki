---
video_id: 2xy3Hm1_ZqI
title: EEVblog #1178 - Build a $10 DIY EMC Probe
url: https://www.youtube.com/watch?v=2xy3Hm1_ZqI
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 31, "3": 40, "4": 52, "5": 65, "6": 89, "7": 108, "8": 117, "9": 128, "10": 138, "11": 149, "12": 159, "13": 175, "14": 188, "15": 202, "16": 210, "17": 222, "18": 233, "19": 254, "20": 263, "21": 273, "22": 283, "23": 298, "24": 310, "25": 322, "26": 345, "27": 358, "28": 379, "29": 399, "30": 416, "31": 428, "32": 444, "33": 456, "34": 464, "35": 481, "36": 491, "37": 507, "38": 516, "39": 526, "40": 540, "41": 551, "42": 561, "43": 574, "44": 591, "45": 609, "46": 619, "47": 629, "48": 642, "49": 653, "50": 675, "51": 687, "52": 703, "53": 715, "54": 725, "55": 735, "56": 746, "57": 757, "58": 773, "59": 789, "60": 801, "61": 814, "62": 824, "63": 835, "64": 852, "65": 867, "66": 877, "67": 889, "68": 908, "69": 918, "70": 931, "71": 946, "72": 958, "73": 967, "74": 979, "75": 989, "76": 1005, "77": 1012, "78": 1024, "79": 1041, "80": 1055, "81": 1067, "82": 1078, "83": 1088, "84": 1108}
---

**Dave Jones:** Hi, so in my previous video about two layer versus four layer and we had a look at using some H field EMC probes to measure the radiation on PCBs and they're very handy bits of kit.

**Dave Jones:** And the one I've got is the Tech Box EMC probe and they're very nice little set of three H field or magnetic field probes and one electric field probe along with a 20 dB wideband amplifier for the thing just to amplify the signal.

**Dave Jones:** You can connect these directly to a scope without an amplifier, but it's like pretty low level stuff. So, external amplifier is nice. And this is a nice bit of kit.

**Dave Jones:** Of course, it comes with the full performance characteristic curves. Here's the coupling loss measurement and they're just great. But the problem is they're like over 300 US dollars on Amazon.

**Dave Jones:** So, I thought we'd have a go at making our own H field probe for 10 bucks. Let's go. I've got a piece of rigid coax and a little preamplifier here.

**Dave Jones:** This was basically $10 on eBay delivered. This is rigid coax. It's RG402. You can see it's actually got a 400% rigid outer shield on it. It's 50 ohm coax already pre-terminated with SMA connectors and you can buy just the coax on its own, but might as well buy them pre-terminated like this.

**Dave Jones:** And these are like $5 delivered. Oh, no, sorry, $3 delivered on eBay. And you can get these little preamplifier boards as well. They come in many companies actually make these and sell these on eBay, but you know, you can get them for as little as like $6 each and delivered on eBay.

**Dave Jones:** Like you can get ones like in cases and stuff. This one's just like you got to feed in your own external five, you know, I think it's 6 to 12 volts this one.

**Dave Jones:** But, yeah, this is a 30 dB uh gain one as opposed to 20 dB gain in the uh TechBox one, but we can just uh knocking a 10 dB attenuator to make them equivalent.

**Dave Jones:** But, 10 bucks, can we turn these into our own do-it-yourself H-field probe? Well, let's have a go. And there's just a closer look at the uh rigid coax for those who haven't uh seen it before.

**Dave Jones:** And it is uh quite stiff. It really is very difficult to uh bend these. course, you can bend and form them, which is uh very nice for like um snaking through a product.

**Dave Jones:** And like if you open any like uh you know, top-end spectrum analyzer or something like that, you'll often find these uh rigid coax's going everywhere. They're just uh They're just fantastic.

**Dave Jones:** So, we'll try this. You could, you know, you could do it with regular coax, but this rigid stuff is very nice because it just forms a um a nice rigid structure um for the uh probe, whereas coax is just going to like flap around in the breeze.

**Dave Jones:** Now, of course, you can actually make a H-field probe just out of a piece of uh copper wire on the end of a BNC connector. But, and and it kind of work, you know, and it actually does work.

**Dave Jones:** But, I thought we'd uh splurge the extra uh three bucks and get this uh nice rigid coax, which I gives us the nice uh shielding. So, it uh shields out some of the um E-field as well as because we're really after a H-field uh probe here.

**Dave Jones:** And if we have a look at uh this H-field uh probe from TechBox, it's all it's going to be People think that there's many loops of wire in here.

**Dave Jones:** That's not so. What this is is this is just going to be a uh just a PCB, likely a very nice uh you know, controlled impedance like uh Rogers uh dielectric or or something like that.

**Dave Jones:** But, it's basically got the SMA on the end. There might be uh some ferrites in here, but I I doubt it. I think it's just uh PCB uh straight through.

**Dave Jones:** So, anyway, it's just a PCB with a 50 ohm uh transmission line embedded in there, and then it So, the ground on either side, and it's going to continue around here like this, probably with uh via stitching on either side, and all the way around, and then they're going to short the other end to the uh ground over here.

**Dave Jones:** So, it's actually a shorted uh loop, and they're going to have a little break in the uh shield there. And like I said, you can do the same thing with just a BNC.

**Dave Jones:** You literally take the output of the BNC, make a loop out of it some either a round one or a uh square one, and then just short it back to ground, and that's your EMC probe.

**Dave Jones:** And they're doing exactly the same thing here, and that's what we're going to do with our rigid coax as well. Now, some designs actually have the uh break over here, but then it's a non-symmetrical design.

**Dave Jones:** So, I'm sure this one's actually going to have the break in the middle. It just gives you a symmetrical shielding across the uh loop like this. Now, the difference between a round one and a square one is a bit uh academic, really.

**Dave Jones:** But if you wanted to get down to individual uh traces, then a square one with the end that's flat can often be better cuz you can actually uh put it right next to a straight trace like that.

**Dave Jones:** And then if you have a square one, it's going to couple better into the probe uh potentially. But we're just going to duplicate this uh round one today so that we can sort of maybe get an AB comparison.

**Dave Jones:** So, we just cut our uh rigid coax in half, which means that we actually get two of these babies. And as you can see, it just looks like uh any other coax with the uh die a solid dielectric in the middle um with a solid core conductor inside, and then the rigid outer uh 100% uh shielded outer uh well, it's not braid, but it's a a solid

**Dave Jones:** outer core, which makes it stiff and rigid, hence the name. Now, because we're going to form this into a loop and then solder it on or terminate it on one end, and then we need to put the slit in the in the middle of it like this.

**Dave Jones:** Just before you do that, it's probably best just to practice how to get in there and cut out the shield. We'll just give that a go. Probably best just to get in there a knife, and you're going to have to get in there and somehow like just split it along one edge, and then bingo, you should just be able to peel that off.

**Dave Jones:** Now, as I said, a common way to do this is to simply just bend this back on itself like that and just strip a tiny leave a like a just a small amount exposed over to here, and literally just solder the the center of that back over to the shield over here to form the shorter turn.

**Dave Jones:** You can do that, but as I said, then it's going to be non-symmetrical. So, what we want to do is actually not have any exposed here. We actually just want to cut it, then solder the inner conductor on there, and also the outer conductor as well, and then put our split across there.

**Dave Jones:** Now, I'm going to actually try and match the diameter here, as I said, but the diameter actually isn't really critical. I just want to be able to do a reasonable AB comparison between these.

**Dave Jones:** You can make it as small or as big as you want. The hence why the set actually comes with these different size heads, because the larger the loop, the greater the sensitivity, the greater the pickup, but unfortunately, the less resolution you're going to have to be able to spot problems.

**Dave Jones:** So, generally, you'll go over your board with like a larger one first to try and find any potential issues, and then you might get a smaller one like this, which you actually does There's probably a tiny little hole in the thing.

**Dave Jones:** It works exactly the same, just smaller diameter. You can go over, and then you know, get a bit finer resolution to try and pinpoint the exact location of any radiated emission.

**Dave Jones:** And as I said, what we want to do is short out both the inner conductor and the outer shield to the shield over here. So, maybe leave a bit out and then bend it over at 90° and then solder the whole lot.

**Dave Jones:** And while heating this up, I found that it actually tended to expand outwards. I guess due to, you know, thermal expansion. It just wanted to go back straight. So, probably best just to hold the loop together while you do it.

**Dave Jones:** So, there's our end result there, which kind of sort of matches the diameter of our Tech Box one. And just for good measure, you might want to throw a couple of clamp ferrites around there and maybe either heat shrink those on just to keep it tidy or something like that.

**Dave Jones:** That just might take the edge off anything picked up by the shield. And of course, don't forget to measure that it is actually the inner conductor is actually shorted out over here.

**Dave Jones:** Just measure that there's a direct short on there. Now, we can just get in there and cut start cutting the shield. Little gap, not huge. Just be careful you don't go too far and cut that inner conductor.

**Dave Jones:** That could ruin your day. So, there you go. Got two little cuts around there like to that now. Slightly off symmetry. She'll be right. And well, now we'll just cut that outer braid out of there.

**Dave Jones:** There you go. Look at that. Bobby dazzler. Right, so let's test this sucker. I'm going to get the Tech Box probe here as a reference. The Gigatron board that we did in the previous video.

**Dave Jones:** There we go. There's our response there and I've frozen that. Let's actually plug in our new do-it-yourself probe. See if we get the same response. Now, I'm going to use the exact same Tech Box amplifier here.

**Dave Jones:** Going to plug it straight in and yep, it seems to be working as a H-field probe. Look at that. No worries. Let's put it over the crystal again. Get the same amplitude as before.

**Dave Jones:** Bingo. Look at that. Bobby Dezler. Let me get an average on that. Check it out. That is insanely close. That's just nuts. Get real time there. Near identical. You can't really ask for much difference.

**Dave Jones:** There's small discrepancies in the diameter of this thing and the the positioning and stuff like that. Our $10 do-it-yourself probe basically exactly the same performance as that tech I'm not going to claim it's exactly the same performance, but you know, it's pretty close over this sort of bandwidth.

**Dave Jones:** And our address mode decoder chip over here, let's have a look. Let's get the Tech Box probe. Believe that's pretty close to the same height. Get tongue at the right angle.

**Dave Jones:** It's near on identical. You can see like the same peaks up here. Like say up at the high end here. You can see it's getting exactly the same peaks, everything else.

**Dave Jones:** The performance is you know, it it's this is near to identical as you can get, really. Okay, let's try it over a much wider frequency range now up to 1 gig and see what's what.

**Dave Jones:** We'll get the crystal once again. Yellow one's the Tech Box. And this one is our do-it-yourself jobby. More than good enough for any practical application of a H-field probe.

**Dave Jones:** And you have to remember that these probes don't have a really a direct correlation to the far-field radiated emissions that you're going to get in the test house. They're designed for like troubleshooting, finding any potential spikes before you get and spend all the expense on a full far-field compliance measurement.

**Dave Jones:** But hey, we're using the Tech Box receiver. Let's try our $5 jobby from eBay and see what happens. This is a 30 dB one, so it's got an extra 10 dB of gain, so that might be an issue, but it works a treat.

**Dave Jones:** 6 volt power source drawing uh milliamps. I believe this particular board can go from 6 to 12 volt. Actually, this is interesting. It is significantly higher amplitude with the lower gain 20 dB one here.

**Dave Jones:** So, so that's a bit uh surprising. Although, the gain of these things does change with uh frequency. But, yeah, I wouldn't have expected that much difference. That's pretty dramatic.

**Dave Jones:** What's going on there? I think you can buy this just on its own for like uh 200 bucks or something. But, basically, um yeah. Well, let's let's do a teardown, shall we?

**Dave Jones:** Well, that looks pretty schmick, doesn't it? But, you know, is it worth the money? Well, you tell me, cuz this one is a couple hundred bucks if you buy it on its own.

**Dave Jones:** This one is five bucks delivered from eBay. They use a different part, but the topology is absolutely same. 50 ohms uh controlled impedance line, AC coupled input and output, and then just feeding in uh the supply.

**Dave Jones:** In this case, just uh 5 volts being fed in, and that's it via via an inductor, of course, and uh Bob's your uncle. But, yeah, they're basically uh same thing.

**Dave Jones:** It just comes down to which chip is used. SK171343. So, I'm going to have to decode that jobby, give it a look. But, there's no reason why you can't roll your own if you wanted exactly the same as this.

**Dave Jones:** But, uh yeah, there there's not much in it. And this cheap ass one here, well, I don't know what that jobby is. But, either way you look at it, when you use the exact same amplifier, the performance is identical.

**Dave Jones:** Beauty. But, we're not done yet, because this probe is all exposed. We've got the big ground shield around here. And the last thing you want when you're probing around a board is to short out any pins.

**Dave Jones:** That could really ruin your day. So, let's solve that problem. This commercial probe has like a uh rubber baby buggy bumper uh protected like vinyl rubbery coating over the PCB here.

**Dave Jones:** So, what we're going to do is rubber coat this as well with plasti dip. This is for like, you know, automotive you know, plasticize your rims on your car or whatever.

**Dave Jones:** I don't know. And that should provide a nice insulative layer. There it is. It insulates electrical shock, vibration, heat, deadens sound, all sorts of stuff. Haven't used this before.

**Dave Jones:** I'll give it a burl. Just stick that on. And well, I only had time to give it two coats and it's a little bit how you doing, but it is like rubbery coated like insulated.

**Dave Jones:** I think it needs probably another good two coats at at least. It didn't really like sticking to that plastic over there. So, but of course you could use heat shrink or maybe a like if you there's some other dip solution or something you can dip it in.

**Dave Jones:** I don't know how they actually do this coating on here. If anyone knows, please let us know. All right. I know everyone's not going to be happy unless I actually show you what's inside this thing.

**Dave Jones:** So, let's see if my guess is correct that it is actually just a symmetrical split shield with a single controlled loop terminated on one side just like we did here.

**Dave Jones:** And surprise, surprise. Not really. There it is. There's the split in your shield like that both top and bottom. And yeah, they put a few vias around there. Not a huge amount, but just enough to stitch it together and you can probably just see inside there.

**Dave Jones:** In fact, it's going to it's close to this side than it is that side because they're actually doing this on a four layer board. You can see the vias around there like that.

**Dave Jones:** And yeah, it's just a single 50 ohm controlled impedance trace in there. But as I said, you know, this will be a controlled impedance dielectric, no doubt. But that's that's all that's inside this is just a shorted loop.

**Dave Jones:** And it'll be shorted on one side. Hang on. And yep, there you go. You can see the extra vias over there. So it comes in and goes around the center of there all the way around with LBJ and terminates on that other side there.

**Dave Jones:** Exactly like the one we just built. But we did it with coax instead of PCB. And I might do a follow-up video. Um actually, you know, laying out a board and actually doing one of these, getting a PCB manufactured.

**Dave Jones:** But the performance is near on identical between these. Just less the rubber's left a bit of bit of residue on the board there. Woohoo! Hold on to your hat.

**Dave Jones:** Hang on. This preamp does actually perform. I increased I was operating at 6 volts before. It said 6 to 12 volt range. But of course it's going to be voltage dependent.

**Dave Jones:** And taking it up to 12 volts and look at the response. This was the one before with the yellow one's the tech box. And it looks like we could be that 10 dB higher.

**Dave Jones:** The wave shape's exactly the same. So let me whack in a 10 dB attenuator in there and I think we're going to be on the money. So I whacked a 10 dB attenuator on there and look at that.

**Dave Jones:** We're on the like it I have to get the exact right height, hold your tongue at the right angle. But that's near on identical if I move it away and move it in.

**Dave Jones:** There you go. That preamp works just fine. There's nothing wrong with it. So don't believe those eBay ads that said 6 to 12 volts. Yeah, right. So there you have it.

**Dave Jones:** Three bucks for the coax, about $6 for the board, like under $10 delivered. And I don't know, you got to throw in some heat shrink or whatever. And I As as as I can measure, it's basically the same performance as this $300 um tech box set here.

**Dave Jones:** Of course, I consider this a part one of this uh video cuz we need to like measure the full performance. Have to manufacture another one, get like the coupling uh response and all, you know, that sort of jazz.

**Dave Jones:** And um and I've got some other amplifiers um coming as well. I just ordered a couple of them. This one just happened to turn up first. You can buy ones with like a shielded enclosures and uh stuff like that, but it it works fine.

**Dave Jones:** 10 bucks. Practically identical performance. So, I hope you like that and it's encouraged you to go and build your own H field probes because they are a really nice bit of kit.

**Dave Jones:** Even if you're not going to send something out for uh pre-compliance, just a like a sweep over your board. We're going to have to do a separate video on the different usages of them and probably do another one making an E field probe.

**Dave Jones:** They're even uh simpler than the H field uh probes, but yeah. But 10 bucks, that's absolutely fantastic. So, if you found that useful, please give it a big thumbs up and as always, you can discuss down below on in the YouTube comments or EEVblog forum.

**Dave Jones:** Catch you next time.
