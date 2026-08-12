---
video_id: XyqzVNNZEBQ
title: EEVblog #1154 - Surprising 4K Dumpster TV Fault
url: https://www.youtube.com/watch?v=XyqzVNNZEBQ
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 34, "3": 51, "4": 65, "5": 83, "6": 99, "7": 118, "8": 140, "9": 155, "10": 170, "11": 184, "12": 199, "13": 214, "14": 229, "15": 243, "16": 257, "17": 275, "18": 293, "19": 308, "20": 320, "21": 337, "22": 352, "23": 366, "24": 383, "25": 396, "26": 409, "27": 424, "28": 437, "29": 453, "30": 467, "31": 481, "32": 501, "33": 515, "34": 528, "35": 544, "36": 557, "37": 577, "38": 592, "39": 605, "40": 615, "41": 627, "42": 645, "43": 658, "44": 674, "45": 696, "46": 715, "47": 737, "48": 752, "49": 765, "50": 783, "51": 801, "52": 820, "53": 831, "54": 848, "55": 864, "56": 874, "57": 890, "58": 906, "59": 917, "60": 930, "61": 946, "62": 963, "63": 980, "64": 993, "65": 1011, "66": 1028, "67": 1041, "68": 1059, "69": 1078, "70": 1097, "71": 1110, "72": 1126, "73": 1143, "74": 1157, "75": 1171, "76": 1183, "77": 1193, "78": 1205, "79": 1221, "80": 1235, "81": 1251, "82": 1264, "83": 1283, "84": 1297, "85": 1312, "86": 1329, "87": 1345, "88": 1359, "89": 1374, "90": 1393, "91": 1405, "92": 1418, "93": 1431, "94": 1449, "95": 1467, "96": 1482, "97": 1499, "98": 1515, "99": 1527, "100": 1544, "101": 1560, "102": 1581, "103": 1596, "104": 1609, "105": 1624, "106": 1635, "107": 1647, "108": 1659, "109": 1675, "110": 1693, "111": 1708, "112": 1720, "113": 1732, "114": 1744, "115": 1756, "116": 1766}
---

**Dave Jones:** Hi, another update on this 65-in LG 4K TV. Turns out it's a 3D TV. One of these newfangled 3D pieces of rubbish. I should just put it back in the dumpster, shouldn't I? Anyway, update video on this. People wanted me to do various stuff

**Dave Jones:** with it. Didn't have time before. So, let's plug in the etherneties and check this out. We've got some We search for EVBlog on Bing and you end up with some weird-looking yank. Dude, who's supposed to be me? I don't

**Dave Jones:** get it. Fail. Anyway, yes, the web interface works. Everything's hunky-dory. And yes, I actually got a remote control for it. So, I'm not sure if it's the original one for this, but it seems to work just fine. So, as you can see, the screen is

**Dave Jones:** just fine. I can get into these app thingies here. We've got Netflix, Stan, all that sort of stuff. Yeah, you see? Look, we can get inside Netflix. No problems whatsoever, right? But, watch this. Let's watch The Simpsons Movie.

**Dave Jones:** Well, let's watch the trailer for it and see what happens. Look at that. It normally auto plays the trailers and stuff like that, but we get that weird mild animated violence, nudity, and drug use. Fantastic. But, yeah, as soon as it plays

**Dave Jones:** something, it will go to pink. So, once it's actually displaying in video content, this is not coming from the HDMI. So, clearly, I was wrong about it or my initial assumption that it was like because I was feeding HDMI and that was causing

**Dave Jones:** the problem. But, no, it's not that. So, it's definitely not the HDMI input decoder, whatever you want to, you know, that part, that section of the board. There's obviously something where it renders video that actually causes the problem. Apart from that, the TV is

**Dave Jones:** absolutely actual screen is absolutely perfect. And this is a bit freaky, but let's watch the video of this TV. Let's go. Once again, it displays all the app stuff absolutely perfectly. So, there's obviously nothing to There it goes. The video ads and

**Dave Jones:** bloody ads. Got to earn my money, don't I? Unbelievable. I just I don't see ads on any of my YouTube videos because I've got YouTube Premium. So, anyway, I recommend YouTube Premium. But look, there you go. So, there you have it.

**Dave Jones:** Obviously, when it's displaying any form of video content, it buggers up. So, nothing to do with the HDMI input. It does it from any like any sort of streaming source because it's going to have like H.264, H.265 like hardware

**Dave Jones:** decoders probably in the main chipset or something like that. But anyway, I was able to acquire the service manual for this thing. So, let's take a look. And there's an interesting thing on the back as well, which we'll have a look at.

**Dave Jones:** Now, it does actually have a component in and that sort of jazz, but I don't readily have the like TRS jack to component video. I probably have one somewhere, but the lab is a mess. If you want to see the lab, there you go.

**Dave Jones:** That's the current state of the lab. I'm like standing where the benches used to be. So, yeah, it's kind of hard to cobble stuff. Anyway, the one of the interesting things is that we've got a RS-232C serial interface for like our servicing

**Dave Jones:** and remote operation. And as it turns out, the actual manual, not the service manual, but the consumer manual has all the commands for the RS-232 interface that allows you to remote operate it. Like you can change channels and switch

**Dave Jones:** the power off and on and do what not. So, it's fascinating that they are actually got that sort of stuff in a consumer manual. Wow, very impressed. One thing I am going to do is check for updates. It's

**Dave Jones:** been might be out of date. Just want make sure I get the latest one. Check for updates. Checking. Here we go. And if we actually go in here and do a picture test, I don't know what type of

**Dave Jones:** picture it's supposed to be. But if we do that, well, failed. So, obviously, this is like internally generating that video signal. So, obviously, some sort of video decoder is failing, but all the on-screen display stuff and anything that runs via

**Dave Jones:** app and goes through that sort of path instead of a video decoder um is a problem. There we go. Let's call them. Oh, that's the Aussie number. So, here we go. We actually have the service manual for this thing. Internal

**Dave Jones:** use only. Fantastic. This is the exact model that we have, and I'm actually very very impressed with this. There's actually a lot of stuff in here. Dates from 2014. Oh, I see. Look. Ah, check leakage hot circuit test.

**Dave Jones:** Nice. All right. So, we got specs and all that sort of jazz. So, let's go down here and have a look at what we've got. Now, one of the first things which I didn't know about um see all these like

**Dave Jones:** service menus and and stuff like that. Here we go. These are actually accessed via a remote control, a dedicated service remote control, which I guess you can buy if you're in the service business. If you have this, the block

**Dave Jones:** diagrams which we'll get into, if you had the a IR transmitter whatever you and you had the codes for it, you could of course send those codes out yourself. I don't know. Everyone says, "Oh, use your phone." My phone doesn't have an IR

**Dave Jones:** transmitter. Then, uh yeah, and you can do like calibration and um all sorts of, you know, test the ADC's and DAC's and all sorts of uh stuff. So, it's absolutely fantastic. Now, what we've got here, the full schematics for this

**Dave Jones:** thing, which is absolutely fantastic. All the juicy detail is there. They've got kind of like a troubleshooting uh process, but it's not It's not really the greatest thing. It It mostly just says if this, board swap. Here's Here's the checklist. Like uh

**Dave Jones:** repair power board and parts normal replace inverter or module. But, other ones just say check and replace main board. And it's pretty much all you can do is it narrows it down to either it's a panel fault, it's a power supply

**Dave Jones:** fault, or it's a main board fault. And that's, you know, pretty much it. So, they've got some flowcharts, which aren't the best, but hey, at least we've got them. Uh 20-point white balance ADC calibration. There's the remote. What is

**Dave Jones:** it? Ad- adjust adjust remote or something like that. So, it's basically a service remote control. Neat, huh? I didn't know that. Here you go. Uh CNT is broken. It tells you, you know, uh abnormal power section and stuff like that. So, if you're

**Dave Jones:** generating this uh test signal, which is kind of a weird test signal dot and a cross and a faded thing. It's kind of kind of weird weird to have that as a test signal. Anyway, it tells you, you know, ab-

**Dave Jones:** abnormal display, abnormal power section, you know, like stuff like that. So, anyway, it doesn't have anything specific to the fault we had. So, what we're going to look at here is we know the symptoms now. So, we're going to

**Dave Jones:** have a look at our block diagram. The block diagram is very handy cuz that's This is where we're going to be able to narrow the stuff down. And there's basically uh sort of like, you know, two major chip sets here. What Confusingly,

**Dave Jones:** they're both called H13. So, I don't know, is that the main board is called H13? I don't get it. Anyway, one is the LG1154D and the LG1154AN. I presume they're different chips. I don't have it open at the moment. So,

**Dave Jones:** this is interesting. We know it's not a like a HDMI receiver problem because even the internal generated test pattern generates the video fault. Basically, anytime you play video, that causes the problem. So, um but all the on-screen display stuff is fine. So,

**Dave Jones:** it's got nothing to do with H13 over here. This is a AV component video, SCART, tuner, all that sort of jazz, okay? So, it's clearly not any of that. We can rule out all that. Now, uh with the

**Dave Jones:** 1154D over here, this is like the main processor. It's got everything. It's got the Ethernet in, so when we do the YouTube video, for example, or the Netflix, and we're coming in via the Ethernet LAN, it's going directly into

**Dave Jones:** this uh chip here, and it's doing Well, have a look down here. We'll come back to this in a second. H13D, here it is. Ethernet comes straight in. It's doing everything internal. As interest to us here is this video encoder, 1080p 30

**Dave Jones:** frames per second. It's got a dual uh um dual core um processor in there, and it's got all the sound DSP, and it's got uh the secure stuff. It's got a 1 meg cache, and then it's got down here. I

**Dave Jones:** don't Actually, I don't know where the 3D They've got 2D graphics up here. I love this GPU, Rogue One. Nice. I assume that's Han Solo. Um that's That's terrific. The here's on-screen display generation, for example. Um oh, H3D, is

**Dave Jones:** that like the 3D engine? It probably doesn't doesn't seem to do much to do like 3D, to add 3D capability or whatever. It's got JPEG encoders, all that sort of stuff. So, you know, one possibility is that the video encoder

**Dave Jones:** inside this main chip is actually, you know, there's something wrong with it. But, the problem with that is that, you know, a lot of these faults will be uh hardware-related in terms of like a large BGA chips like this. They heat up

**Dave Jones:** over long term, heat up, cool down. Every time you power them up, they cycle, you can get cracked solder joints, dry joints, all that sort of stuff. That's why uh often everyone just says, "Oh, just reflow the BGA." You

**Dave Jones:** know, um all that sort of thing. Or, if it's extreme, you reball it. But, jeez, you'd have to be pretty desperate to do that. Anyway, yeah, like reflow the chip and stuff like that. The problem with this is that this is all internal on the

**Dave Jones:** silicon. So, if it was this, like it kind of doesn't make sense from that physical failure uh point of view, which is probably the most likely scenario. So, unless the silicon's died, like maybe the video encoder section in in in

**Dave Jones:** there has died as part of it, but it doesn't like that seems the that doesn't seem very likely, quite frankly. So, it could be like decoupling for this chip or something is a bit marginal. Well, then why isn't anything

**Dave Jones:** else affected? Why is it just the video encoding? So, yeah, I don't think it's that. So, I suspect if we reflowed that chip, that I don't think that's going to help us much. What I think's possibly more likely is have a look up here. This

**Dave Jones:** just shows HDMI coming in over here like this. Uh and here's our panel output, 120 hertz uh LVDS combo. EPI, I don't know, V uh X1, I don't know what any of those are offhand, but of course LVDS is the low voltage

**Dave Jones:** differential signaling, which is it goes off to they've got to have a panel driver there. And if we sure enough follow the money down here, look at this. Aha. They got two LVDS paths. OSD, on screen display, which works

**Dave Jones:** fine, and FHD, full HD. I presume they've got separate on like over a screen overlay paths and separate video paths. So, aha, it could be that the video path is something wrong with that. So, reflowing that chip could help. Who knows? It

**Dave Jones:** could be the pins for that, for example. So, obviously the on screen display, everything's working and the apps and things like that. So, you're doing web browsing and stuff like that. It's obviously not rendering that through the video engine. So, it's it's

**Dave Jones:** probably going via the on screen display path because all the apps work fine. You browse the web, you do everything else, you go into your Netflix, it all looks good until it plays that video. I think my money at the moment's got to be on

**Dave Jones:** this LVDS full HD part here. And then V1X um, there's an eight lane thing here and a two lane for the OSD. So, it could could very well it may not be that path there. It could very well be these lanes

**Dave Jones:** here. These by lanes it does physically means differential pairs, um, high speed data lanes, paths, basically traces, uh, going over. So, you know, so we've got potentially three suspect components here. We've got the this path here, which could be

**Dave Jones:** solder joints this end perhaps. Let's assume it's a physical fault. Um, solder joints this end, this end, uh, it's so this chip and also this, um, Ursa 9 chip over here, whatever that is. And then they've got this one path going

**Dave Jones:** off to the panel. So, there's obviously nothing wrong with that one path going off to the panel and then going onto the T-con board. A lot of people said, "I checked the ribbon cables and stuff like that." No, this is happening on the

**Dave Jones:** board. Um, this is definitely not anything to do further down the pipe. I think it's most likely something to do with this sort of interface here. And this is interesting in that the HDMI input over here uh, comes through the HDMI switch.

**Dave Jones:** There's nothing wrong with that. That was my original thought cuz I was just testing with the HDMI. So, that was a a reasonable first assumption was that the HDMI input switch decoder, whatever uh, it is, um, that would be an issue. A lot

**Dave Jones:** of people said, "Oh, are they ESD and stuff like that on the inputs?" No, it's got nothing to do with that cuz that's what we've seen. We've proven that even internally generated video signals. So, you know, it goes through a splitter

**Dave Jones:** here and interestingly it bypasses the main chip here. So, if you uh, feeding the HDMI input signal here, it can actually just split right out jitter cleaner and it goes straight to U14 down here and shoots it straight out. So, the

**Dave Jones:** processor doesn't main processor up here, H13, doesn't do any of that. Um, it just does all your on-screen display stuff and other things that would, you know, it it has internal video generation because that would be for Netflix and YouTube and stuff like that

**Dave Jones:** where it decodes it from Ethernet, uh, for example, or decoding it from a USB port or or a hard drive or or whatever it is. So, oh, by the way, for those who want to know about the RS232 serial

**Dave Jones:** interface, unfortunately, it doesn't actually give me any useful information. Somebody said, I'll control C when you're booting up to try and avoid like to try and break into it. I can't get that. So, I've got it hooked up here.

**Dave Jones:** Turn the TV on. Okay. TV's on and we get nothing. But, if we power it off, there we go. And we got something when we powered it off. Emergency remount RO. Sometimes we get some more data than that, but basically that's it. We just

**Dave Jones:** get a message when it um shuts down. So, it's of no help. So, we can actually try and find maybe an internal uh debug thing cuz that is a very common. But, yeah, we could potentially maybe get some additional debug

**Dave Jones:** stuff out of it. So, let's go to this uh Ursa 9 chip, which was like the main output uh driver. And we can have a look here. Looks like it's got its own SPI flash. It's got chip configuration stuff. Slave

**Dave Jones:** boot from SPI flash. There's lots of like configuration jumpers and stuff like that. Here we go. Debugging. It's I squared C. Yeah, I'm not that keen to get out the scope and do I squared C decoding and stuff like that. That, you

**Dave Jones:** know, no, thanks. I don't see a big value in doing that. But, the LGE 7411 the Ursa 9. Once again, there's more like option jumpers is there. The schematic's probably not going to tell us a huge amount. Look at all the power

**Dave Jones:** pins. That is a metric buttload of They're just the VSS. They're just the ground pins. Wow. If you lost a couple, lost a few dozen, it's still not going to be a problem. Anyway, this has its own core power

**Dave Jones:** supply. So, once again, I don't think it's that because obviously it then it wouldn't if the power supplies were to fail for this chip, you wouldn't be able to get the OSD data coming through, for example. So, if I went in and measured

**Dave Jones:** those local regulators, I'm I almost guarantee that they're fine. It just wouldn't make sense for it uh to be uh a power supply issue on that chip. So, I've got a ground. Where's all the power? Oh, over here. Didn't see that. There

**Dave Jones:** you go. There There's all the There There's all the power rails. Sweet. Ooh, look. Secret. Secret squirrel. Um only for training and service purposes. It's lucky I'm doing training and servicing. All right. So, I've got the board out. I thought I'd have a at least

**Dave Jones:** have a go a reflowing a chip. Now, I know it's not the highest odds, but this Ursa 9 chip up here, it's this puppy right here, and it's already had the heat sinking pad actually removed from it. Stuck to the back of the uh the

**Dave Jones:** metal plate on the thing. So, I don't know. Maybe that's kind of a you know, a suspect in its own right. Perhaps maybe it's you know, it's gotten too hot or something like that and the adhesive on the back of that's come off. I don't

**Dave Jones:** know, but anyway, this is the of course goes out to the LCD panels here. So, it's not going to be anything on this side of it, but but certainly something coming in that on-screen display bus coming in. Perhaps anyway, it's readily

**Dave Jones:** available. The other ones, I'm not quite sure where they are, but these seem um ridiculously difficult to get off. There's a main chip under here as well and another one up there. Really just for pure access sake, I'm just going to

**Dave Jones:** have a go at just reflowing this. I'm not going to reflow the whole board. There you go. It's just a couple of bypass caps there. So, nothing really doing there at all. So, what I'm going to do is actually use my uh preheater

**Dave Jones:** here. It's a pooy poo hoo pooy um preheater. J8280 for those playing along at home. I got this like for like 10 bucks on eBay. It cost more for postage than it did for the actual thing. I got it like an auction.

**Dave Jones:** Nobody bid on it. So, it's a preheater. So, what we're going to do is just heat uh the bottom of this board. There's multiple layers of uh ground planes in here. I don't know how many layer board this is, but basically the idea is just

**Dave Jones:** to raise the bottom temperature of that so that we when we hit it with our hot air gun on top, it's not as big a thermal shock. And there's pros and cons and I some people don't like using

**Dave Jones:** preheaters, other people swear by them, etc. etc. I just thought I'd give it a go. Maybe just, you know, bump it up by 100°. Just help it along. So, all the stuff I'm going to do here, please do

**Dave Jones:** not take this as uh my recommendation or uh best practice or anything like that for reflowing or reworking BGAs. I do not do this for a living. I don't really have any major feel for it uh because I don't do it

**Dave Jones:** every day or even every month um stuff like this. So, really I'm just kind of like just sucking it and seeing um if I can make any difference here. So, by all means leave comments down below about how you uh reflow BGAs and all that, but

**Dave Jones:** you know, please look, just you know, keep it nice, okay? Just got a small amount of uh preheat under there, 100° C. That's pretty warm. So, yeah, that'll maybe reduce the thermal shock, but I don't want to do too much other uh

**Dave Jones:** damage as well. You got to be careful with any uh as I've done in previous video. Whoop, yeah, I melted the connectors uh previous time I tried to do this in controlled in my reflow oven. Anyway, I've got my quick uh 861DW.

**Dave Jones:** I set it for uh rough, 400° uh nominal maximum air flow. So, we'll give it a go. I could have put some Kapton tape around here, but uh anyway, I'm just looking for any movement, maybe help reflow the pins self-center.

**Dave Jones:** Of course, there is an art and science to this, and as I said, I don't have a feel for it. This is just me trying to do something at least. Just to see if I can get this chip to

**Dave Jones:** reflow and make a difference. If the chip doesn't actually get to 450, there's a lot of loss in the air. It all has to do with uh air flow and how quickly it can uh tra- how efficiently it can transfer

**Dave Jones:** that heat and the uh drop from the element, etc., etc. There's a ton of stuff which goes into this, and I didn't see that chip. You know, I expected to see it sort of like just maybe slightly wobble a bit. And again, you've

**Dave Jones:** got to be looking carefully for it. So, hopefully those joints get hot enough to reflow and maybe it'll fix something. Well, unfortunately, uh that didn't work. I'll spare you the uh details, but the exact same problem. It's still We

**Dave Jones:** haven't harmed it. It's still uh hunky-dory. So, the um thermal pad for this one actually came off is the infamous U14, which connects everything else. You can actually see the traces actually going up here. These pairs, they jump down to the

**Dave Jones:** bottom and go up to there. So, you know, we've kind of sort of tried to reflow that, whether or not the balls actually reflowed, not 100% sure. Anyway, this little baby here is central to everything. It's coming from the other

**Dave Jones:** main uh chippity do dah up here, but this one interconnects the more. So, this one technically has the highest probability of having and interconnect IE a BGA ball that is suspect on one of those not the OSD line the the actual video

**Dave Jones:** line. I'll do the same preheat and reflow on that one and that's the bottom of the chip there. What's there once again there's a couple of bypass caps but there's really nothing else interestingly there's a flat flex cable

**Dave Jones:** connector there. So I'll only put part of the board on there like there's no point heating up the whole thing. It could fit like lengthwise but then you heat up and it's got those little rubber bumpers on the bottom. I don't

**Dave Jones:** want to melt those or take them off or anything. So just give it a little hand. That's all. All right. I've got some preheater action on there. Let's give this a go. Max 120 liters per minute air flow. Let's try and heat it up.

**Dave Jones:** Hopefully I don't melt this. I should cover those plastic connectors. Should put some tape on those. Famous last words right? Shoulda coulda. Trying to find the slightest little movement in that just to see that it's Should hopefully it'll the surface

**Dave Jones:** tension of the solder will keep the balls in line. Just want to see some resemblance of movement. It could be hard to see. Aha! Now this is really interesting. And if you remember the picture before the squares and it was like pink and it

**Dave Jones:** was shimmering all over the place. It is changed. It is now fixed. So something has changed and I didn't see any change like this when I reheated that output chip the one that was driving the panel. I didn't see that at all but heating

**Dave Jones:** this one up it's done something. And that's the same for Netflix as well. We're definitely onto something. So I might take that board out again. It's just hanging on by a loose thread and uh just be I don't just reheat it again.

**Dave Jones:** Maybe I wasn't uh vigorous enough. Just put some Kapton around there just to protect the connectors there. Hopefully, the higher temperature will get the heat through quicker, hopefully reflow the balls quicker without putting less and putting less stress on the

**Dave Jones:** on the chip, but obviously, we didn't do any damage last time. This is as high as the uh quick goes, by the way, 500° and uh 200 L per minute. I could like decrease the air flow. Um you know, but

**Dave Jones:** once again, I said I don't have a feel for this because unless you've extensively do this like every day, every week, you really get a feel for the particular type of gear that you're using, then well, you know, you're just having

**Dave Jones:** a stab like I am. All right, let's give it a burl. Yep, panel still works, so we didn't damage it. And picture test, nah, same. Bummer. Um and I found my um wider nozzle. And this nozzle's much nicer

**Dave Jones:** because your uh hand doesn't get all the reflected heat coming back. Yeah, it's moving. Whoa. Whoa. Whoa. Whoa. Whoa. Whoa. Please. Oh, yeah. Okay, I expect a high probability of it not even powering up now. Nah. Yeah, completely gone. Damn, that chip is

**Dave Jones:** goneski. Well, it's it's it's moved out of alignment. All right, when in doubt, add flux. Um could say probably should have used flux to begin with, but uh I've got this uh liquid flux here. I have not used it

**Dave Jones:** before, so please don't take this as a recommendation, but it's sort of like it's got a brush, and it's liquid. So, I want to try and get it at least to run down the balls there. So, I'll do all

**Dave Jones:** four corners, let gravity try and get in there, but there's so little gap between the balls in there, it's going to be hard. Oh, she's bubbling. She's bubbling. Nope. I do believe we've done our dash. We've got some lines in there, not sure if you

**Dave Jones:** can see that. Oh, now I got lines on this half over here. So, it seems to be like yeah, it's just changing all the time. Well, there you go. I think we've come a gutters on this poor little chip.

**Dave Jones:** I think it's had maybe a bit too much abuse and you know, the thing might have shifted on there. We're probably like, you know, shorted some balls out, something like that. So, that's going to be really hard to get going again unless

**Dave Jones:** we actually physically take the whole chip off, clean up the pads and and stuff like that. There's I don't know how many, you know, 5 600 more pins on this thing. Clean up the pads and maybe some balls have come off. So, you might

**Dave Jones:** have to reball it and that's not I don't want to go down that rabbit hole really. Certainly not in this video. And like it's nothing else around it. So, I think it is that lane interconnect. We of course reflowed this one up here. Wasn't

**Dave Jones:** that. Like they use different memory here to like D1 decodes video, one doesn't. It, you know, could have potentially have been that, but the fact that we actually got it to change substantially when we reflowed this chip shows that that thing was an issue. So,

**Dave Jones:** that's most likely our diagnosis was right that was a real bummer, but at least we had a go at reflowing this thing to see if it made a difference. And I hope you enjoyed that troubleshooting procedure. In the end, I

**Dave Jones:** believe we guessed the right chip. We sort of, you know, looked at the symptoms, narrowed it all down and said highest probability was that chip. Sure enough, when we reflowed that puppy the first time, it actually changed. So,

**Dave Jones:** there was some difference in there. What that issue, you know, was? it? it fix a couple of bad joints that we had on there? I don't know. And I've tried several times since to actually try and get this back into a

**Dave Jones:** working state, but unfortunately I can't. Might have another go or two cuz it's like I might as well, right? So, I'll might give it another go, but anyway, um I hope you enjoyed that troubleshooting procedure is valuable to

**Dave Jones:** go through and see that chip. So, ultimately may not it might be a board swap. I don't I'm not going to try and find another board like this and take the chip off like a dumped board and take the chip

**Dave Jones:** off and all that. So, no. A few more shots at this um see if I can do if I do, I'll put a I might just whack a video on the second channel um if I get this thing fixed. Um if not, I hope you

**Dave Jones:** enjoyed the troubleshooting procedure and if you did, give it a big thumbs up and as always discuss down below. Catch you next time.
