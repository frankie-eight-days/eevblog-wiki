---
video_id: XyqzVNNZEBQ
title: EEVblog #1154 - Surprising 4K Dumpster TV Fault
url: https://www.youtube.com/watch?v=XyqzVNNZEBQ
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 31, "3": 48, "4": 57, "5": 67, "6": 83, "7": 99, "8": 115, "9": 133, "10": 148, "11": 160, "12": 173, "13": 184, "14": 195, "15": 205, "16": 227, "17": 237, "18": 247, "19": 259, "20": 282, "21": 299, "22": 312, "23": 324, "24": 346, "25": 360, "26": 375, "27": 390, "28": 396, "29": 406, "30": 418, "31": 431, "32": 442, "33": 453, "34": 465, "35": 478, "36": 490, "37": 509, "38": 531, "39": 544, "40": 555, "41": 569, "42": 584, "43": 596, "44": 606, "45": 615, "46": 627, "47": 652, "48": 665, "49": 672, "50": 703, "51": 715, "52": 733, "53": 744, "54": 755, "55": 765, "56": 779, "57": 796, "58": 817, "59": 826, "60": 833, "61": 848, "62": 861, "63": 871, "64": 888, "65": 913, "66": 926, "67": 938, "68": 949, "69": 963, "70": 976, "71": 991, "72": 1004, "73": 1019, "74": 1039, "75": 1054, "76": 1064, "77": 1078, "78": 1094, "79": 1102, "80": 1112, "81": 1134, "82": 1143, "83": 1157, "84": 1170, "85": 1179, "86": 1189, "87": 1199, "88": 1212, "89": 1223, "90": 1238, "91": 1251, "92": 1260, "93": 1283, "94": 1295, "95": 1304, "96": 1314, "97": 1327, "98": 1341, "99": 1354, "100": 1366, "101": 1393, "102": 1405, "103": 1417, "104": 1424, "105": 1435, "106": 1454, "107": 1467, "108": 1481, "109": 1492, "110": 1503, "111": 1517, "112": 1544, "113": 1558, "114": 1575, "115": 1593, "116": 1607, "117": 1618, "118": 1627, "119": 1640, "120": 1651, "121": 1666, "122": 1675, "123": 1690, "124": 1704, "125": 1713, "126": 1726, "127": 1736, "128": 1748, "129": 1756, "130": 1764}
---

**Dave Jones:** Hi, another update on this 65-in LG 4K TV. Turns out it's a 3D TV. One of these newfangled 3D pieces of rubbish. I should just put it back in the dumpster, shouldn't I?

**Dave Jones:** Anyway, update video on this. People wanted me to do various stuff with it. Didn't have time before. So, let's plug in the etherneties and check this out. We've got some We search for EVBlog on Bing and you end up with some weird-looking yank.

**Dave Jones:** Dude, who's supposed to be me? I don't get it. Fail. Anyway, yes, the web interface works. Everything's hunky-dory. And yes, I actually got a remote control for it. So, I'm not sure if it's the original one for this, but it seems to work just fine.

**Dave Jones:** So, as you can see, the screen is just fine. I can get into these app thingies here. We've got Netflix, Stan, all that sort of stuff. Yeah, you see?

**Dave Jones:** Look, we can get inside Netflix. No problems whatsoever, right? But, watch this. Let's watch The Simpsons Movie. Well, let's watch the trailer for it and see what happens. Look at that.

**Dave Jones:** It normally auto plays the trailers and stuff like that, but we get that weird mild animated violence, nudity, and drug use. Fantastic. But, yeah, as soon as it plays something, it will go to pink.

**Dave Jones:** So, once it's actually displaying in video content, this is not coming from the HDMI. So, clearly, I was wrong about it or my initial assumption that it was like because I was feeding HDMI and that was causing the problem.

**Dave Jones:** But, no, it's not that. So, it's definitely not the HDMI input decoder, whatever you want to, you know, that part, that section of the board. There's obviously something where it renders video that actually causes the problem.

**Dave Jones:** Apart from that, the TV is absolutely actual screen is absolutely perfect. And this is a bit freaky, but let's watch the video of this TV. Let's go. Once again, it displays all the app stuff absolutely perfectly.

**Dave Jones:** So, there's obviously nothing to There it goes. The video ads and bloody ads. Got to earn my money, don't I? Unbelievable. I just I don't see ads on any of my YouTube videos because I've got YouTube Premium.

**Dave Jones:** So, anyway, I recommend YouTube Premium. But look, there you go. So, there you have it. Obviously, when it's displaying any form of video content, it buggers up. So, nothing to do with the HDMI input.

**Dave Jones:** It does it from any like any sort of streaming source because it's going to have like H.264, H.265 like hardware decoders probably in the main chipset or something like that.

**Dave Jones:** But anyway, I was able to acquire the service manual for this thing. So, let's take a look. And there's an interesting thing on the back as well, which we'll have a look at.

**Dave Jones:** Now, it does actually have a component in and that sort of jazz, but I don't readily have the like TRS jack to component video. I probably have one somewhere, but the lab is a mess.

**Dave Jones:** If you want to see the lab, there you go. That's the current state of the lab. I'm like standing where the benches used to be. So, yeah, it's kind of hard to cobble stuff.

**Dave Jones:** Anyway, the one of the interesting things is that we've got a RS-232C serial interface for like our servicing and remote operation. And as it turns out, the actual manual, not the service manual, but the consumer manual has all the commands for the RS-232 interface that allows you to remote operate it.

**Dave Jones:** Like you can change channels and switch the power off and on and do what not. So, it's fascinating that they are actually got that sort of stuff in a consumer manual.

**Dave Jones:** Wow, very impressed. One thing I am going to do is check for updates. It's been might be out of date. Just want make sure I get the latest one.

**Dave Jones:** Check for updates. Checking. Here we go. And if we actually go in here and do a picture test, I don't know what type of picture it's supposed to be.

**Dave Jones:** But if we do that, well, failed. So, obviously, this is like internally generating that video signal. So, obviously, some sort of video decoder is failing, but all the on-screen display stuff and anything that runs via app and goes through that sort of path instead of a video decoder um is a problem.

**Dave Jones:** There we go. Let's call them. Oh, that's the Aussie number. So, here we go. We actually have the service manual for this thing. Internal use only. Fantastic. This is the exact model that we have, and I'm actually very very impressed with this.

**Dave Jones:** There's actually a lot of stuff in here. Dates from 2014. Oh, I see. Look. Ah, check leakage hot circuit test. Nice. All right. So, we got specs and all that sort of jazz.

**Dave Jones:** So, let's go down here and have a look at what we've got. Now, one of the first things which I didn't know about um see all these like service menus and and stuff like that.

**Dave Jones:** Here we go. These are actually accessed via a remote control, a dedicated service remote control, which I guess you can buy if you're in the service business. If you have this, the block diagrams which we'll get into, if you had the a IR transmitter whatever you and you had the codes for it, you could of course send those codes out yourself.

**Dave Jones:** I don't know. Everyone says, "Oh, use your phone." My phone doesn't have an IR transmitter. Then, uh yeah, and you can do like calibration and um all sorts of, you know, test the ADC's and DAC's and all sorts of uh stuff.

**Dave Jones:** So, it's absolutely fantastic. Now, what we've got here, the full schematics for this thing, which is absolutely fantastic. All the juicy detail is there. They've got kind of like a troubleshooting uh process, but it's not It's not really the greatest thing.

**Dave Jones:** It It mostly just says if this, board swap. Here's Here's the checklist. Like uh repair power board and parts normal replace inverter or module. But, other ones just say check and replace main board.

**Dave Jones:** And it's pretty much all you can do is it narrows it down to either it's a panel fault, it's a power supply fault, or it's a main board fault.

**Dave Jones:** And that's, you know, pretty much it. So, they've got some flowcharts, which aren't the best, but hey, at least we've got them. Uh 20-point white balance ADC calibration. There's the remote.

**Dave Jones:** What is it? Ad- adjust adjust remote or something like that. So, it's basically a service remote control. Neat, huh? I didn't know that. Here you go. Uh CNT is broken.

**Dave Jones:** It tells you, you know, uh abnormal power section and stuff like that. So, if you're generating this uh test signal, which is kind of a weird test signal dot and a cross and a faded thing.

**Dave Jones:** It's kind of kind of weird weird to have that as a test signal. Anyway, it tells you, you know, ab- abnormal display, abnormal power section, you know, like stuff like that.

**Dave Jones:** So, anyway, it doesn't have anything specific to the fault we had. So, what we're going to look at here is we know the symptoms now. So, we're going to have a look at our block diagram.

**Dave Jones:** The block diagram is very handy cuz that's This is where we're going to be able to narrow the stuff down. And there's basically uh sort of like, you know, two major chip sets here.

**Dave Jones:** What Confusingly, they're both called H13. So, I don't know, is that the main board is called H13? I don't get it. Anyway, one is the LG1154D and the LG1154AN.

**Dave Jones:** I presume they're different chips. I don't have it open at the moment. So, this is interesting. We know it's not a like a HDMI receiver problem because even the internal generated test pattern generates the video fault.

**Dave Jones:** Basically, anytime you play video, that causes the problem. So, um but all the on-screen display stuff is fine. So, it's got nothing to do with H13 over here. This is a AV component video, SCART, tuner, all that sort of jazz, okay?

**Dave Jones:** So, it's clearly not any of that. We can rule out all that. Now, uh with the 1154D over here, this is like the main processor. It's got everything. It's got the Ethernet in, so when we do the YouTube video, for example, or the Netflix, and we're coming in via the Ethernet LAN, it's going directly into this uh chip here, and it's doing Well, have a look down here.

**Dave Jones:** We'll come back to this in a second. H13D, here it is. Ethernet comes straight in. It's doing everything internal. As interest to us here is this video encoder, 1080p 30 frames per second.

**Dave Jones:** It's got a dual uh um dual core um processor in there, and it's got all the sound DSP, and it's got uh the secure stuff. It's got a 1 meg cache, and then it's got down here.

**Dave Jones:** I don't Actually, I don't know where the 3D They've got 2D graphics up here. I love this GPU, Rogue One. Nice. I assume that's Han Solo. Um that's That's terrific.

**Dave Jones:** The here's on-screen display generation, for example. Um oh, H3D, is that like the 3D engine? It probably doesn't doesn't seem to do much to do like 3D, to add 3D capability or whatever.

**Dave Jones:** It's got JPEG encoders, all that sort of stuff. So, you know, one possibility is that the video encoder inside this main chip is actually, you know, there's something wrong with it.

**Dave Jones:** But, the problem with that is that, you know, a lot of these faults will be uh hardware-related in terms of like a large BGA chips like this. They heat up over long term, heat up, cool down.

**Dave Jones:** Every time you power them up, they cycle, you can get cracked solder joints, dry joints, all that sort of stuff. That's why uh often everyone just says, "Oh, just reflow the BGA." You know, um all that sort of thing.

**Dave Jones:** Or, if it's extreme, you reball it. But, jeez, you'd have to be pretty desperate to do that. Anyway, yeah, like reflow the chip and stuff like that. The problem with this is that this is all internal on the silicon.

**Dave Jones:** So, if it was this, like it kind of doesn't make sense from that physical failure uh point of view, which is probably the most likely scenario. So, unless the silicon's died, like maybe the video encoder section in in in there has died as part of it, but it doesn't like that seems the that doesn't seem very likely, quite frankly.

**Dave Jones:** So, it could be like decoupling for this chip or something is a bit marginal. Well, then why isn't anything else affected? Why is it just the video encoding? So, yeah, I don't think it's that.

**Dave Jones:** So, I suspect if we reflowed that chip, that I don't think that's going to help us much. What I think's possibly more likely is have a look up here.

**Dave Jones:** This just shows HDMI coming in over here like this. Uh and here's our panel output, 120 hertz uh LVDS combo. EPI, I don't know, V uh X1, I don't know what any of those are offhand, but of course LVDS is the low voltage differential signaling, which is it goes off to they've got to have a panel driver there.

**Dave Jones:** And if we sure enough follow the money down here, look at this. Aha. They got two LVDS paths. OSD, on screen display, which works fine, and FHD, full HD.

**Dave Jones:** I presume they've got separate on like over a screen overlay paths and separate video paths. So, aha, it could be that the video path is something wrong with that.

**Dave Jones:** So, reflowing that chip could help. Who knows? It could be the pins for that, for example. So, obviously the on screen display, everything's working and the apps and things like that.

**Dave Jones:** So, you're doing web browsing and stuff like that. It's obviously not rendering that through the video engine. So, it's it's probably going via the on screen display path because all the apps work fine.

**Dave Jones:** You browse the web, you do everything else, you go into your Netflix, it all looks good until it plays that video. I think my money at the moment's got to be on this LVDS full HD part here.

**Dave Jones:** And then V1X um, there's an eight lane thing here and a two lane for the OSD. So, it could could very well it may not be that path there.

**Dave Jones:** It could very well be these lanes here. These by lanes it does physically means differential pairs, um, high speed data lanes, paths, basically traces, uh, going over. So, you know, so we've got potentially three suspect components here.

**Dave Jones:** We've got the this path here, which could be solder joints this end perhaps. Let's assume it's a physical fault. Um, solder joints this end, this end, uh, it's so this chip and also this, um, Ursa 9 chip over here, whatever that is.

**Dave Jones:** And then they've got this one path going off to the panel. So, there's obviously nothing wrong with that one path going off to the panel and then going onto the T-con board.

**Dave Jones:** A lot of people said, "I checked the ribbon cables and stuff like that." No, this is happening on the board. Um, this is definitely not anything to do further down the pipe.

**Dave Jones:** I think it's most likely something to do with this sort of interface here. And this is interesting in that the HDMI input over here uh, comes through the HDMI switch.

**Dave Jones:** There's nothing wrong with that. That was my original thought cuz I was just testing with the HDMI. So, that was a a reasonable first assumption was that the HDMI input switch decoder, whatever uh, it is, um, that would be an issue.

**Dave Jones:** A lot of people said, "Oh, are they ESD and stuff like that on the inputs?" No, it's got nothing to do with that cuz that's what we've seen. We've proven that even internally generated video signals.

**Dave Jones:** So, you know, it goes through a splitter here and interestingly it bypasses the main chip here. So, if you uh, feeding the HDMI input signal here, it can actually just split right out jitter cleaner and it goes straight to U14 down here and shoots it straight out.

**Dave Jones:** So, the processor doesn't main processor up here, H13, doesn't do any of that. Um, it just does all your on-screen display stuff and other things that would, you know, it it has internal video generation because that would be for Netflix and YouTube and stuff like that where it decodes it from Ethernet, uh, for example, or decoding it from a USB port or or a hard drive or or whatever

**Dave Jones:** it is. So, oh, by the way, for those who want to know about the RS232 serial interface, unfortunately, it doesn't actually give me any useful information. Somebody said, I'll control C when you're booting up to try and avoid like to try and break into it.

**Dave Jones:** I can't get that. So, I've got it hooked up here. Turn the TV on. Okay. TV's on and we get nothing. But, if we power it off, there we go.

**Dave Jones:** And we got something when we powered it off. Emergency remount RO. Sometimes we get some more data than that, but basically that's it. We just get a message when it um shuts down.

**Dave Jones:** So, it's of no help. So, we can actually try and find maybe an internal uh debug thing cuz that is a very common. But, yeah, we could potentially maybe get some additional debug stuff out of it.

**Dave Jones:** So, let's go to this uh Ursa 9 chip, which was like the main output uh driver. And we can have a look here. Looks like it's got its own SPI flash.

**Dave Jones:** It's got chip configuration stuff. Slave boot from SPI flash. There's lots of like configuration jumpers and stuff like that. Here we go. Debugging. It's I squared C. Yeah, I'm not that keen to get out the scope and do I squared C decoding and stuff like that.

**Dave Jones:** That, you know, no, thanks. I don't see a big value in doing that. But, the LGE 7411 the Ursa 9. Once again, there's more like option jumpers is there.

**Dave Jones:** The schematic's probably not going to tell us a huge amount. Look at all the power pins. That is a metric buttload of They're just the VSS. They're just the ground pins.

**Dave Jones:** Wow. If you lost a couple, lost a few dozen, it's still not going to be a problem. Anyway, this has its own core power supply. So, once again, I don't think it's that because obviously it then it wouldn't if the power supplies were to fail for this chip, you wouldn't be able to get the OSD data coming through, for example.

**Dave Jones:** So, if I went in and measured those local regulators, I'm I almost guarantee that they're fine. It just wouldn't make sense for it uh to be uh a power supply issue on that chip.

**Dave Jones:** So, I've got a ground. Where's all the power? Oh, over here. Didn't see that. There you go. There There's all the There There's all the power rails. Sweet. Ooh, look.

**Dave Jones:** Secret. Secret squirrel. Um only for training and service purposes. It's lucky I'm doing training and servicing. All right. So, I've got the board out. I thought I'd have a at least have a go a reflowing a chip.

**Dave Jones:** Now, I know it's not the highest odds, but this Ursa 9 chip up here, it's this puppy right here, and it's already had the heat sinking pad actually removed from it.

**Dave Jones:** Stuck to the back of the uh the metal plate on the thing. So, I don't know. Maybe that's kind of a you know, a suspect in its own right.

**Dave Jones:** Perhaps maybe it's you know, it's gotten too hot or something like that and the adhesive on the back of that's come off. I don't know, but anyway, this is the of course goes out to the LCD panels here.

**Dave Jones:** So, it's not going to be anything on this side of it, but but certainly something coming in that on-screen display bus coming in. Perhaps anyway, it's readily available. The other ones, I'm not quite sure where they are, but these seem um ridiculously difficult to get off.

**Dave Jones:** There's a main chip under here as well and another one up there. Really just for pure access sake, I'm just going to have a go at just reflowing this.

**Dave Jones:** I'm not going to reflow the whole board. There you go. It's just a couple of bypass caps there. So, nothing really doing there at all. So, what I'm going to do is actually use my uh preheater here.

**Dave Jones:** It's a pooy poo hoo pooy um preheater. J8280 for those playing along at home. I got this like for like 10 bucks on eBay. It cost more for postage than it did for the actual thing.

**Dave Jones:** I got it like an auction. Nobody bid on it. So, it's a preheater. So, what we're going to do is just heat uh the bottom of this board. There's multiple layers of uh ground planes in here.

**Dave Jones:** I don't know how many layer board this is, but basically the idea is just to raise the bottom temperature of that so that we when we hit it with our hot air gun on top, it's not as big a thermal shock.

**Dave Jones:** And there's pros and cons and I some people don't like using preheaters, other people swear by them, etc. etc. I just thought I'd give it a go. Maybe just, you know, bump it up by 100°.

**Dave Jones:** Just help it along. So, all the stuff I'm going to do here, please do not take this as uh my recommendation or uh best practice or anything like that for reflowing or reworking BGAs.

**Dave Jones:** I do not do this for a living. I don't really have any major feel for it uh because I don't do it every day or even every month um stuff like this.

**Dave Jones:** So, really I'm just kind of like just sucking it and seeing um if I can make any difference here. So, by all means leave comments down below about how you uh reflow BGAs and all that, but you know, please look, just you know, keep it nice, okay?

**Dave Jones:** Just got a small amount of uh preheat under there, 100° C. That's pretty warm. So, yeah, that'll maybe reduce the thermal shock, but I don't want to do too much other uh damage as well.

**Dave Jones:** You got to be careful with any uh as I've done in previous video. Whoop, yeah, I melted the connectors uh previous time I tried to do this in controlled in my reflow oven.

**Dave Jones:** Anyway, I've got my quick uh 861DW. I set it for uh rough, 400° uh nominal maximum air flow. So, we'll give it a go. I could have put some Kapton tape around here, but uh anyway, I'm just looking for any movement, maybe help reflow the pins self-center.

**Dave Jones:** Of course, there is an art and science to this, and as I said, I don't have a feel for it. This is just me trying to do something at least.

**Dave Jones:** Just to see if I can get this chip to reflow and make a difference. If the chip doesn't actually get to 450, there's a lot of loss in the air.

**Dave Jones:** It all has to do with uh air flow and how quickly it can uh tra- how efficiently it can transfer that heat and the uh drop from the element, etc., etc.

**Dave Jones:** There's a ton of stuff which goes into this, and I didn't see that chip. You know, I expected to see it sort of like just maybe slightly wobble a bit.

**Dave Jones:** And again, you've got to be looking carefully for it. So, hopefully those joints get hot enough to reflow and maybe it'll fix something. Well, unfortunately, uh that didn't work.

**Dave Jones:** I'll spare you the uh details, but the exact same problem. It's still We haven't harmed it. It's still uh hunky-dory. So, the um thermal pad for this one actually came off is the infamous U14, which connects everything else.

**Dave Jones:** You can actually see the traces actually going up here. These pairs, they jump down to the bottom and go up to there. So, you know, we've kind of sort of tried to reflow that, whether or not the balls actually reflowed, not 100% sure.

**Dave Jones:** Anyway, this little baby here is central to everything. It's coming from the other main uh chippity do dah up here, but this one interconnects the more. So, this one technically has the highest probability of having and interconnect IE a BGA ball that is suspect on one of those not the OSD line the the actual video line.

**Dave Jones:** I'll do the same preheat and reflow on that one and that's the bottom of the chip there. What's there once again there's a couple of bypass caps but there's really nothing else interestingly there's a flat flex cable connector there.

**Dave Jones:** So I'll only put part of the board on there like there's no point heating up the whole thing. It could fit like lengthwise but then you heat up and it's got those little rubber bumpers on the bottom.

**Dave Jones:** I don't want to melt those or take them off or anything. So just give it a little hand. That's all. All right. I've got some preheater action on there.

**Dave Jones:** Let's give this a go. Max 120 liters per minute air flow. Let's try and heat it up. Hopefully I don't melt this. I should cover those plastic connectors. Should put some tape on those.

**Dave Jones:** Famous last words right? Shoulda coulda. Trying to find the slightest little movement in that just to see that it's Should hopefully it'll the surface tension of the solder will keep the balls in line.

**Dave Jones:** Just want to see some resemblance of movement. It could be hard to see. Aha! Now this is really interesting. And if you remember the picture before the squares and it was like pink and it was shimmering all over the place.

**Dave Jones:** It is changed. It is now fixed. So something has changed and I didn't see any change like this when I reheated that output chip the one that was driving the panel.

**Dave Jones:** I didn't see that at all but heating this one up it's done something. And that's the same for Netflix as well. We're definitely onto something. So I might take that board out again.

**Dave Jones:** It's just hanging on by a loose thread and uh just be I don't just reheat it again. Maybe I wasn't uh vigorous enough. Just put some Kapton around there just to protect the connectors there.

**Dave Jones:** Hopefully, the higher temperature will get the heat through quicker, hopefully reflow the balls quicker without putting less and putting less stress on the on the chip, but obviously, we didn't do any damage last time.

**Dave Jones:** This is as high as the uh quick goes, by the way, 500° and uh 200 L per minute. I could like decrease the air flow. Um you know, but once again, I said I don't have a feel for this because unless you've extensively do this like every day, every week, you really get a feel for the particular type of gear that you're using, then well, you know, you're just having

**Dave Jones:** a stab like I am. All right, let's give it a burl. Yep, panel still works, so we didn't damage it. And picture test, nah, same. Bummer. Um and I found my um wider nozzle.

**Dave Jones:** And this nozzle's much nicer because your uh hand doesn't get all the reflected heat coming back. Yeah, it's moving. Whoa. Whoa. Whoa. Whoa. Whoa. Whoa. Please. Oh, yeah. Okay, I expect a high probability of it not even powering up now.

**Dave Jones:** Nah. Yeah, completely gone. Damn, that chip is goneski. Well, it's it's it's moved out of alignment. All right, when in doubt, add flux. Um could say probably should have used flux to begin with, but uh I've got this uh liquid flux here.

**Dave Jones:** I have not used it before, so please don't take this as a recommendation, but it's sort of like it's got a brush, and it's liquid. So, I want to try and get it at least to run down the balls there.

**Dave Jones:** So, I'll do all four corners, let gravity try and get in there, but there's so little gap between the balls in there, it's going to be hard. Oh, she's bubbling.

**Dave Jones:** She's bubbling. Nope. I do believe we've done our dash. We've got some lines in there, not sure if you can see that. Oh, now I got lines on this half over here.

**Dave Jones:** So, it seems to be like yeah, it's just changing all the time. Well, there you go. I think we've come a gutters on this poor little chip. I think it's had maybe a bit too much abuse and you know, the thing might have shifted on there.

**Dave Jones:** We're probably like, you know, shorted some balls out, something like that. So, that's going to be really hard to get going again unless we actually physically take the whole chip off, clean up the pads and and stuff like that.

**Dave Jones:** There's I don't know how many, you know, 5 600 more pins on this thing. Clean up the pads and maybe some balls have come off. So, you might have to reball it and that's not I don't want to go down that rabbit hole really.

**Dave Jones:** Certainly not in this video. And like it's nothing else around it. So, I think it is that lane interconnect. We of course reflowed this one up here. Wasn't that.

**Dave Jones:** Like they use different memory here to like D1 decodes video, one doesn't. It, you know, could have potentially have been that, but the fact that we actually got it to change substantially when we reflowed this chip shows that that thing was an issue.

**Dave Jones:** So, that's most likely our diagnosis was right that was a real bummer, but at least we had a go at reflowing this thing to see if it made a difference.

**Dave Jones:** And I hope you enjoyed that troubleshooting procedure. In the end, I believe we guessed the right chip. We sort of, you know, looked at the symptoms, narrowed it all down and said highest probability was that chip.

**Dave Jones:** Sure enough, when we reflowed that puppy the first time, it actually changed. So, there was some difference in there. What that issue, you know, was? it? it fix a couple of bad joints that we had on there?

**Dave Jones:** I don't know. And I've tried several times since to actually try and get this back into a working state, but unfortunately I can't. Might have another go or two cuz it's like I might as well, right?

**Dave Jones:** So, I'll might give it another go, but anyway, um I hope you enjoyed that troubleshooting procedure is valuable to go through and see that chip. So, ultimately may not it might be a board swap.

**Dave Jones:** I don't I'm not going to try and find another board like this and take the chip off like a dumped board and take the chip off and all that.

**Dave Jones:** So, no. A few more shots at this um see if I can do if I do, I'll put a I might just whack a video on the second channel um if I get this thing fixed.

**Dave Jones:** Um if not, I hope you enjoyed the troubleshooting procedure and if you did, give it a big thumbs up and as always discuss down below. Catch you next time.
