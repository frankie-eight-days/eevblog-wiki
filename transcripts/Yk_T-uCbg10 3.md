---
video_id: Yk_T-uCbg10
title: Returned BM036 Clamp Meter Investigation
url: https://www.youtube.com/watch?v=Yk_T-uCbg10
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 28, "3": 42, "4": 58, "5": 77, "6": 97, "7": 118, "8": 134, "9": 149, "10": 164, "11": 178, "12": 189, "13": 202, "14": 216, "15": 229, "16": 245, "17": 261, "18": 275, "19": 296, "20": 316, "21": 338, "22": 353, "23": 369, "24": 384, "25": 402, "26": 417, "27": 437, "28": 453, "29": 471, "30": 490, "31": 509, "32": 534, "33": 553, "34": 569, "35": 586, "36": 603, "37": 623, "38": 642, "39": 671, "40": 686, "41": 701, "42": 714, "43": 724, "44": 737}
---

**Dave Jones:** Hi, just a quick look at a returned BM036 clamp meter here. I think this is the first one that I've had returned. I've sold quite a lot of these. It's a quite popular unit. Um, and uh what's the

**Dave Jones:** fault report is uh start a reading 7 to 8 amps DC current and cannot be zeroed. Cannot be zeroed. That's weird cuz that's a software function. Um, every day so it shouldn't matter in theory what the offset is. Uh,

**Dave Jones:** it should be able to zero it. Every day it seems to be reading higher and higher. That's interesting. So when something changes over time like that, maybe you suspect, you know, some sort of capacitor changing or something perhaps.

**Dave Jones:** Um, it now reads 14 amps. The AC clamp measurement works perfectly fine. So AC works fine. It's just a DC thing. Okay. Um, it still reads 14 amps. All right. Well, let's turn it on, shall we? So we've got volts AC. That's going to

**Dave Jones:** be That's going to be hunky-dory. Volts DC. Yeah, so AC Um, yeah, it he says AC works fine. So let's uh put that on DC and overload. Hello. Overload.

**Dave Jones:** Overload amps. Let's put it on the other position. AC is fine. And DC and there you go, 85 amps. Wow. What was it reading before? 7 to 8 amps. Now it's 85 amps. Or overload on the other uh range. That is

**Dave Jones:** That is nuts. Wow. Okay. Um and ohms. I like I assume, like does that functionality still work? Um, it it should and 10k bang on. Um, so yeah, so the resistance works. I assume that the uh volts uh works as well, and the electric field

**Dave Jones:** detection. Yeah, that works. All right, so that's interesting, is it not? Um like Why? Oh, I didn't try and uh zero that. Um so, yeah, we'll put on DC, and 86.

**Dave Jones:** Wow, beep beep. It can't zero that. Are you serious? Wow, cuz that's just a software feature. Like, it doesn't matter what that reading is, it should be able to zero that. So, um maybe it's yeah, it's just it's

**Dave Jones:** just too large, and the software knows it's too large, so the software knows something's wrong. Maybe it's software's being smart, or whatever. So, Now, of course, clamp meters will actually have an offset on the DC uh range, especially on the lower range

**Dave Jones:** here. This one's uh the lower range with 10 milliamps resolution here, and that's why it shows you up here, it's like the it's a positional uh thing. You're going to get more accuracy. It shows, you know, that's what these arrows show. It

**Dave Jones:** shows that if you're doing like the low current measurement, the wire needs to be it's more accurate if it's in that location here. You know, if you just have it in the middle of the clamp here, it'll still work, but it won't be as

**Dave Jones:** accurate as it will be if you actually put it um up there in that positional uh space. So, that's on the lower uh current reading. But, anyway, um cuz it's susceptible to the Earth's magnetic field. So, um that's just that's not

**Dave Jones:** particular to this meter, all meters um have it. So, if you have one that has even a lower range than this, like the Uni-T one, it's all over the shop, right? Um so, yeah, it's nuts. Uh so, anyway, let's uh let's open this up, and

**Dave Jones:** let's have a squeeze. I assume it's not a battery uh related issue, cuz we're not getting low battery. So, uh by the way, this company bought uh three of these. So, two of them um I I think they bought three. So,

**Dave Jones:** two of them have worked uh fine, and anyway I don't I don't expect anything on the front board because it works works hunky-dory. It's going to be something to do jeez the overexposure on the camera there is really really

**Dave Jones:** something, isn't it? Um so I got multiple pots in there. Anyway ribbon cable looks good. The four trim pots I have no information on what those trim pots do I do not even though I'm a dealer for these I do not have Brymen do not

**Dave Jones:** release schematics at all. So I don't have schematics. I don't have calibration procedures or anything for this. So I don't know. I'm just you know shooting around in the dark really. I'm just seeing like if there's anything obvious

**Dave Jones:** at all inside this. I'm I'm I'm doubting it's probably some I don't know. Maybe a component fire or something. Uh not exactly sure but anyway it's really interesting giving an offset like that. So maybe the sensor's gone skee. I don't

**Dave Jones:** know. Anything obvious under here? We're going to have to get the whole board out I think. It's uh just looking for any visual indications. That resistor there doesn't look Oh yeah. Yeah there's solder on that that resistor just

**Dave Jones:** that's the input that's the high voltage series input string that's got nothing to do with reading the current. Those so uh it all looks fine. It all looks okay there. Not seeing anything obvious. So uh rest of the board maybe. Of course

**Dave Jones:** the the front end board there's going to be nothing on the front end board. I like how the BM036 has ton of protection on here on its own dedicated board. No wackers. It's uh uh It's really quite the little beastie.

**Dave Jones:** I I forget what the rating is. Cat 4 300 volts cat uh 3 600 volts. So, it's not too shabby. So, that's our input uh marks down there. That's all sort of like the more multi-metery stuff. Then the current clamp,

**Dave Jones:** I would think. Um but basically, I do believe like it's just like multi-regular multimeter chipset. Yeah, the current clamp just converts it um into a voltage which the multimeter just reads and that's uh that's basically how your clamp meter is

**Dave Jones:** going to work. So, let's take the ribbon cable out of there. Oh, that's soldered in there. Ah, forgot about that. They use a connector over here, but they solder it on the other side. It's kind of annoying. Anyway, there's

**Dave Jones:** there's not much under there. There's a few passives and stuff. What do that? Here we go. We are in. There's our board. So, I'll flip that over. You know how I mentioned capacitors before? Well, there's an awful lot of tins on there, isn't there?

**Dave Jones:** Mhm. So, but once again, without schematic, I'm kind of uh just in the dark. These solder joints going over to there look pretty good. The bottom of that board though, I suspect you know, if you're going to have a problem, that's where it's going

**Dave Jones:** to be cuz the multimeter seems to work fine. So, I'm thinking that that's but to get that board out, I'm going to desolder those three pins over there. Cuz that's annoying. Like they used a header here and there's no header over

**Dave Jones:** here. They're just soldered in. That's really annoying. Yeah, my guess would be that it's that front-end board. Um Brymen chipset, of course. They won't tell you what chipset that is. Yeah. Yeah, nah. Cuz the multimeter works, so that's all the

**Dave Jones:** multimeter stuff. It's you know, it's got to be you think it it's almost certainly has to be on that board there. Get all three at the same time, maybe? Come on. Nah, that's really annoying. Why did they do that? So, that MCP uh 6002,

**Dave Jones:** I think that's a I on the end there. Um that's a uh that's one of the microchips op amp jobbies. And then got another little analog devices jobbie up there. I don't know what an AO9 is. Um yeah, there's nothing

**Dave Jones:** obvious there. There's no solder joint issues that I can see. So, uh it would have passed its factory test, and why it got worse over time I don't know. And as I said, I'm doubting any of the mol- like the multimeter functionality,

**Dave Jones:** cuz it seems to work otherwise. Just looking at the joints there. You know, like you could retouch them as a matter of course. Uh but otherwise, that looks fine and dandy. But the symptom is is that it slowly got

**Dave Jones:** worse. So, I don't cuz each one of these is of course factory uh calibrated, cuz they have to be like manually um each one has to be manually tweaked. Uh it could be a dodgy pot. Yeah. Wouldn't rule out a dodgy pot, like a

**Dave Jones:** dodgy contact one of these pots. They're only the single turn jobbies. But you know, there's like doesn't look like there's any contamination on there, but you never know. It's a little hairy scary sticking out there. What's he doing? It's probably worth

**Dave Jones:** actually putting it back together and just giving those a tiny little tweak either way. Just Just basically put it back to where it was. Um and just just, you know, work the contacts again and see if that's a problem. Just

**Dave Jones:** reheating all those pins. Well, after touching up some things and putting it back, now we're getting exactly the same as we did before. So, yeah. That's not good, is it? Um I guess I can put some current through there and see if we actually get

**Dave Jones:** an offset. Um that'll actually show that the uh sensor's working and and the amplifier and stuff and that's just some offset issue, maybe. Okay, I got 3 amps. It's currently 89. 0 and sure enough it goes up to 92. So,

**Dave Jones:** yeah. Um it does actually measure and it's bang-on. So, yeah, it looks like there's some sort of offset issue. Hmm. Give each one of those a little uh uh tweak back and forth and we'll see if that changes anything.

**Dave Jones:** Uh nope. Nope. Nope. Nope. Nope, it's an offset issue. Uh bugger. Um there you go. So, yeah, I'm probably not going to spend any more time on this now. I just wanted to um have a look to verify that and uh have a

**Dave Jones:** quick visual and um and see. So, it doesn't seem to be um it well, it seems to be like yeah, some sort of offset issue. So, without a calibration procedure and um, a schematic and other stuff like that, I guess I could ask

**Dave Jones:** Brymen for it. Um, yeah, I'm not going to go chasing that any further at this stage, but uh, there you go. Um, just wanted to show you that yeah, these things do fail. Um, you know, all meters have a

**Dave Jones:** uh, you know, a mortality uh, rate and as I said, I think the customer bought three of these and two of them perfectly fine. This is the first failure I've had. I've sold quite a lot of these now.

**Dave Jones:** Um, so, it's a very popular and robust little meter, but you know, there's going to be one out of every, you know, a couple of thousand meters that uh, comes a gutser for whatever bizarre reason, but yeah, I'd say there's some

**Dave Jones:** sort of offset issue there. So, if you notice something that I didn't see on screen here, uh, please leave it in the comments down below, but uh, uh, uh, anyway, that's it. Catch you next time.
