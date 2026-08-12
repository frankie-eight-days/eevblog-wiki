---
video_id: F-VnbzXjH9I
title: EEVblog #398 - Lecroy 9384C Oscilloscope Repair
url: https://www.youtube.com/watch?v=F-VnbzXjH9I
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 22, "3": 31, "4": 43, "5": 63, "6": 77, "7": 84, "8": 96, "9": 113, "10": 122, "11": 134, "12": 147, "13": 160, "14": 172, "15": 191, "16": 206, "17": 217, "18": 228, "19": 246, "20": 254, "21": 270, "22": 281, "23": 293, "24": 311, "25": 323, "26": 335, "27": 351, "28": 372, "29": 385, "30": 411, "31": 434, "32": 447, "33": 456, "34": 470, "35": 480, "36": 488, "37": 497, "38": 513, "39": 524, "40": 536, "41": 546, "42": 567, "43": 584, "44": 608, "45": 619, "46": 642, "47": 663, "48": 680, "49": 694, "50": 718, "51": 737, "52": 748, "53": 759, "54": 777, "55": 787, "56": 805, "57": 828, "58": 844, "59": 855, "60": 871, "61": 897, "62": 910, "63": 927, "64": 946, "65": 967, "66": 978, "67": 1003, "68": 1016, "69": 1027, "70": 1040, "71": 1050, "72": 1060, "73": 1078, "74": 1099, "75": 1117, "76": 1137, "77": 1150, "78": 1164, "79": 1183, "80": 1196, "81": 1206, "82": 1223, "83": 1237, "84": 1251, "85": 1261, "86": 1276, "87": 1284, "88": 1311, "89": 1323, "90": 1344, "91": 1360, "92": 1380, "93": 1399, "94": 1416, "95": 1437, "96": 1450, "97": 1465, "98": 1476, "99": 1485, "100": 1493, "101": 1511, "102": 1522, "103": 1535, "104": 1551, "105": 1561, "106": 1574, "107": 1590, "108": 1602, "109": 1612, "110": 1636, "111": 1644, "112": 1659, "113": 1673, "114": 1683, "115": 1699, "116": 1718, "117": 1734, "118": 1748, "119": 1763, "120": 1776, "121": 1798, "122": 1807, "123": 1824, "124": 1846, "125": 1866, "126": 1884, "127": 1898, "128": 1913, "129": 1927, "130": 1950, "131": 1961, "132": 1972, "133": 1987, "134": 1997, "135": 2016, "136": 2029, "137": 2044, "138": 2062, "139": 2074, "140": 2085, "141": 2103, "142": 2120, "143": 2151, "144": 2162, "145": 2184, "146": 2197, "147": 2205, "148": 2225, "149": 2238, "150": 2254, "151": 2265, "152": 2278, "153": 2289, "154": 2302, "155": 2320, "156": 2338, "157": 2344, "158": 2358, "159": 2379, "160": 2402, "161": 2424, "162": 2434, "163": 2450, "164": 2465, "165": 2487, "166": 2498, "167": 2515, "168": 2534, "169": 2547, "170": 2558, "171": 2574}
---

**Dave Jones:** Hi, quite a while ago I did a teardown of this Lecroy 9384C 1 GHz oscilloscope 4 gig sample per second. And if you haven't seen it, I'll link it in down below.

**Dave Jones:** Check it out first if you haven't done that. And as you would have seen in that video, this thing had a few issues. And it had a fault and I haven't really had time to look into this thing at all.

**Dave Jones:** I just checked the power supply rails and they were all fine at the time. And well, just the other day I decided to uh crack it open again and have another look.

**Dave Jones:** So, this is going to be an attempted repair video. And I say attempted because I have no idea if I'm going to be able to fix this thing, find the problem, or whatever.

**Dave Jones:** So, if you get to the end of this video and I haven't fixed it, tough luck. All right? So, um this is like a real-time uh a real-time repair cuz I just powered this thing up and once again I measured the voltage rails again, had the same fault as before, and the voltage rails were all uh fine.

**Dave Jones:** And let's have a look at it down here and it was all fine. So, I cracked it open and then I started to run it again. I was about to uh turn on the uh camera and um you know, uh start troubleshooting the thing.

**Dave Jones:** And then I found it just uh you know, it just failed. It switched off. I heard a bit of a bit of a sizzling sound or something like that.

**Dave Jones:** Maybe it was my imagine I don't imagination, I don't know. It didn't sound that great anyway. And let's have a look at what I found. If we get our Here we go.

**Dave Jones:** Get our multimeter here. And look at this. Let's have a look. And here's the uh power Here's the power can Here's the power supply here. It normally like sits on top all this metal work as you saw in the teardown all normally sits over the top of this.

**Dave Jones:** I got it off and uh it's got multiple rails. It's got uh 3.3 V there. There's a yellow one, the orange one down in there is uh 5 V.

**Dave Jones:** There's four of those or three of those. There's ground. There's uh plus minus 15 V. There's plus minus 2 V and um a couple of other uh voltages there as well.

**Dave Jones:** And I think there's some sort of uh sense line as well coming back. But after I heard this um sizzle and it stopped working, um I measured the rails again and the 3.3 V rail is dead.

**Dave Jones:** So, I've got it on ohms and if we have a look here, let's probe our 3.3 V rail. Look at that, 0.17 ohms. Let's zero out our test leads cuz this is a very low.

**Dave Jones:** We're getting about 61 milliohms there. So, let's zero that out. There we go and that is repeatable. There we go. Nicely repeatable down to plus minus 1 milliohm. I like it.

**Dave Jones:** And let's probe that again. That's our 3.3 V rail, rail, folks. Just over 0.1. Let's call it 0.11 ohms. And obviously, it shouldn't be that. And let's swap the polarity around just in case it's some sort of semiconductor junction or something like that.

**Dave Jones:** No, it is spot-on. It's 0.11 ohms. So, something on this thing has shorted out. And I didn't measure the resistance uh before this uh happened, of course, but um that is definitely not right.

**Dave Jones:** Something is completely shorted and we're getting nothing on that 3.3 V rail now. So, the power supply is shutting down. So, woohoo! Excellent. This is what you're hoping for with a repair.

**Dave Jones:** You're hoping that, you know, a power supply like this will fail. At least you've got something to troubleshoot. So, um well, we're going to have to try and find the short on this thing.

**Dave Jones:** Um it could you know, uh in theory, it could be like a you know, a power plane in the middle of the board or something, but it's more likely to be a uh cap or a component, but I have no idea how many caps or how many caps and how many chips are in parallel on that 3.3 V rail on here.

**Dave Jones:** I'm assuming like maybe all of the memory up here and uh you know, a lot of the um ASICs and stuff like that and a whole bunch, probably all the uh processor board.

**Dave Jones:** So, let's start. We've actually got some things which we're going to unplug. So, let's We've got the processor board here. So, let's uh whack this out and measure that again.

**Dave Jones:** Because you always start with the stuff that you can No, 0.11 ohms. You always start with the stuff that you can physically remove. And if you've got a couple of modules like this, there's the memory module there.

**Dave Jones:** I don't know. Um can't see any signs of visual, you know, um the first thing you look for is uh is going to be uh visual stuff, but we're not into the visual inspection yet.

**Dave Jones:** We're just removing these modules. See if we can localize that short. So, I hope I've got time to fix this today. I've only got an hour or so before I've got to head back babysitting little Sagan.

**Dave Jones:** So, it's not that one. There's nothing nothing visual on that board that I can see at all. Let's measure it again and I don't like our chances. No, bummer.

**Dave Jones:** It's somewhere on this main board. Murphy, every time Murphy will get you. So, looks like we're going to pop out this main board, which is a mongrel. Got to undo all the uh screws on here, lift it all out.

**Dave Jones:** So, let's give that a go. You've seen the bottom if you've seen the teardown. I won't bother uh taking off all this uh metal work yet because um yeah, we can you know start with the power connector up here and work our way around the board.

**Dave Jones:** Now, I have no idea if this fire is related to the original fault. So, this is short on the 3.3 volt rail is in any way related to the problems I was getting with the scope all those waveform corruptions and all that sort of stuff.

**Dave Jones:** It certainly could be because if you saw the previous video, you notice that the way it was kind of sort of working. It was sampling a sine wave, but the memory was being all corrupted and stuff like that or it appeared to be.

**Dave Jones:** So, that could certainly be something to do with the digital 3.3 volt rail. So, I'm hoping that whatever was causing the problem on the 3.3 volt rail before it could have been excess ripple or you know some other issue like that was loading down the rail and it was still working, but then it eventually failed and went kaput and the magic smoke escaped and now it's completely failed.

**Dave Jones:** So, I hope they're related, but Murphy might intervene again and ensure that they're not related and this 3.3 volt is a new fault. So, even if I find this 3.3 volt issue and I fix it as no guarantee that it's going to fix the original fault, but fingers crossed.

**Dave Jones:** Now, when you're tracking down this sort of short on a board, you want the greatest resolution possible on your multimeter. Now, this is a case where accuracy does not matter.

**Dave Jones:** You just want resolution, cuz we don't care if it's a 5% accurate, 10% accurate or 0.005% accurate. We don't give a toss. All we care about is the resolution.

**Dave Jones:** So, let's take the Fluke 87 in regular 3 and a half digit mode, okay? We put it on ohms, we short it out, we've only got a lousy 100 milliohms resolution there.

**Dave Jones:** It's absolutely hopeless, right? And you saw that our short on this board was 0.11 ohms. So, how can we trace this fault down to a lower and lower resistance with that?

**Dave Jones:** You can't. You at least need an order of magnitude better, at the very least. So, we put it in four and a half digit mode and we get an extra digit of resolution in there.

**Dave Jones:** So, the Fluke 87 in four and a half digit mode like this, yeah, we're going to see that last digit, but ah, you know, it's not as good as it could be.

**Dave Jones:** Ideally, you want a like a five and a half digit meter, for example, or uh something like this Agilent 1272A, which has a 50 ohm mode instead of the usual 500 or 200 ohm mode.

**Dave Jones:** So, short it out and bingo, we've got 1 milliohm resolution. So, that's brilliant. So, that's what I'm going to do. And of course, we can you saw before, we've got 1 milliohm resolution.

**Dave Jones:** Fantastic. This is what you need for tracing down a uh short on a board like this. Or you could use like a bench multimeter or so, you know, if you've got like a five and a half digit bench multimeter or something like that, that'll do the job as well.

**Dave Jones:** So, we know it's not either of our other boards, it must be on this main board. So, here it is again, and there are three pins. These top three pins here are all the 3.3 volt pins.

**Dave Jones:** So, if I get in there and get the third third pin down. There it is. Now, around about 0.11 ohms, and then the next pin up also 0.11 ohms, and the next one up is actually is open.

**Dave Jones:** That That's my finger there. It's my fingers on the probe doing that. So, that top one is open. So, it looks like that top pin, which is very surprising because usually that they're they're all uh shorted together on the board there and they're just using the three pins to get extra current handling uh capability through that.

**Dave Jones:** I mean, the 3.3 V one isn't the highest current um supply on this board. I think it's the 5 V cuz it's got four wires on it. So, usually they short them all together to a an internal plane or a internal track, but let's flip this thing over and uh have a look down here at what we've got on these pins.

**Dave Jones:** Now, it's uh often handy to know how many layers this board is. And uh uh often, well, a a well-designed board will a multi-layer board will have these layer designators here.

**Dave Jones:** And they're actually physically uh copper and they've placed them on the different layers like this. And this one here, you can see number one is placed on well, layer number one, the top layer, and then layer number two is under that, and then three, four, five, and there's actually six there if you flip the thing over because it's physically on the bottom layer there.

**Dave Jones:** So, there it is. It's upside down there, but you can see 1 2 3 4 5 6. So, we've got six layer board here. And as I said, in theory, the short could be on the internal uh layers on the planes, but uh usually that doesn't happen um as a post-manufacturing uh fault.

**Dave Jones:** Usually, it happens at the PCB manufacturing stage. Now, these are the three pins we're concerned about here. They're uh shorted to ground somehow, and um I can't see those um pins coming out on this top layer anyway to any sort of big beefy uh power track at all.

**Dave Jones:** So, clearly, um they're not connected on the top layer here. So, we need to flip this thing over and have a look at the bottom layer. And here's the bottom layer.

**Dave Jones:** And here are the three pins again. And once again, bummer, they're not connected through to this plane down here at all. But um this is you know this is more of a manufacturing uh type inspection really because you wouldn't expect um you know a working unit to suddenly fail and then to find a short on your PCB.

**Dave Jones:** It's got to be almost certainly within side one of the components in parallel. But in this case um you know it's going to be next to impossible to follow this rail because it like physically follow it to components because it just goes off to an internal uh power plane somewhere which probably snakes across the board.

**Dave Jones:** They might have a whole plane in there dedicated to the 3.3 V rail and another one dedicated to the 5 V rail for example. And then the other power rails or it could be a split internal power plane or something like that.

**Dave Jones:** So um uh you know that's why you need these multi-layer boards cuz this power has to go everywhere. Now, I don't really have the exact uh schematic for this thing.

**Dave Jones:** I've got a schematic for the M model uh unit which isn't exactly the same and it's very difficult to read. So um really you know I pretty much we you know we're going to do this without the manual because um and finding the uh designated components anyway of all the components on the 3.3 V rail.

**Dave Jones:** What we're just going to do now is just um probe around well, first we'll do a visual inspection of course, first step to see if there's any obviously uh blown components.

**Dave Jones:** But I don't I've had a quick glance over it and I don't think there is. Um so next we're going to actually uh trace this thing down and try and hunt down that value as it gets lower and lower towards um the you know the point where it's ultimately shorted.

**Dave Jones:** So um with a 1 mΩ resolution meter, we should be able to do that fairly well because any sort of uh short fault on a product or any sort of product like this, uh 1 mΩ resolution is, you know, is uh generally going to be enough to find um to narrow down that resistance reading and eventually track down the fault.

**Dave Jones:** Now, I've taken off the metal shield on the bottom here and I, you know, I'm looking around and I can't see any components that are visually uh gone. Of course, the thing you're going to look for most often is the uh is the cap.

**Dave Jones:** So, you're going to look for these tantalums here, make sure they haven't blown. I don't know if they're across the 3.3 V rail yet. Odds are at least one of them in each of those uh channels is, I would be guessing.

**Dave Jones:** And well, I can't see anything obvious there and uh likewise, on the top of the board, we really have to um scan this thing over and uh see if we can find any shorts at all.

**Dave Jones:** There's a couple of tantalums down there. We've got a couple of big electrolytics here and there's one over there. There's a couple of electrolytics there, but there's a whole bunch of little tantalums on top on the analog rails, but and no, I had a good look over this board and I checked for both the um tantalums, the electrolytics and other caps, and I can't see any that have

**Dave Jones:** visually uh failed, i.e. melted, have a big uh burn hole in them or anything like that. So, the next thing you're going to look for is the ICs themselves because ICs do actually fail and go short internally.

**Dave Jones:** It's not that uncommon. And generally, you would look for like a like a burn mark in the center of the chip or it's, you know, it's indented or warped or something like that Because that that's where like if the dying side is heated up and it's you know you've got SCR latch up or something like that.

**Dave Jones:** I've done a video on SCR latch up which can cause fires like this permanent fires within the chip then or some other failure mode of course then you'd expect to see a visual deformity in the chip if it got bad enough but not always.

**Dave Jones:** Murphy will ensure that the failure will be inside the chip with no visual uh you know no visual outside clue at all that anything's gone wrong. So you're looking for little ripples or cracks in the tops of the chips or little indentations or bubbles or something like that or a big gaping damn hole in the thing perhaps.

**Dave Jones:** But I've had a good fairly good look over this thing and I can't see anything. What a bummer. So we're going to have to start tracing this thing down with the multimeter.

**Dave Jones:** So let's start tackling this thing. Here is our 3.3 volt rail up here. Remember it was that second pin down there. By the way the other thing you're going to need is very sharp probe tips very high quality sharp probe tips to pierce the oxidization on the solder joints and get right into those solder joints so you get the lowest resistance reading possible cuz you don't want variation when you're

**Dave Jones:** chasing a delta variation in a contact resistance like this. By delta I mean a difference with starting out with 0.11 ohms here and we're going to measure the differential as we go across the board.

**Dave Jones:** So we're looking for the difference. So repeatability is a key thing. So if these contacts are all dodgy and all you're not putting enough force on there you don't want to get dodgy readings.

**Dave Jones:** And we're talking very low resistance values. But as you can see this thing is quite repeatable as we saw like you shorted out like that and it's 0.06. So ultimately we're assuming that we find our short, it's going to be around 0.06.

**Dave Jones:** If we get down right to that, then we can, you know, zero out the probes, maybe, and even track it do some fine tracking right at the final point.

**Dave Jones:** But, you know, it should get down So, we should trace it from 0.11 down to .06, and we can at least localize the area where the fault is going to be.

**Dave Jones:** So, contact resistance, absolutely key, nice firm pressure on there. So, let's take a look. We've got our 0. Uh sorry, and this is our 3.3 V rail. So, let's uh go between the ground pin again.

**Dave Jones:** There it is. Hey, there we go. 0.16. Oh, look. It's it's going all over the place. Look. Look at that. Oh, I hope it doesn't disappear on us. I've had that happen once or twice where I've been tracing the thing down, and it suddenly vanishes, and that's when you're really having a bad Murphy day, let me tell you.

**Dave Jones:** So, uh it's gone up to .17 now. So, you know, maybe you'd give them This is where you'd probably give the board a little bit of a flex to see if it's a see if it's some sort of flexion issue, like a physical issue within the components.

**Dave Jones:** So, I'm flexing the other side here. No. No, it's not. I don't see any drastic change there on the board. So, 1.57 ohms. Okay, well, let's just skip on over here to these caps.

**Dave Jones:** I reckon one of these has got to be the 3.3 V rail. I'd be a bit surprised if it wasn't. No, there we go. 136 ohms and climbing. That's another rail we can, you know, we're obviously charging up the rail capacitance there.

**Dave Jones:** And of course if you swap your leads around like that, you'll no doubt get something different. There you go. So, yeah, don't follow that. That's a uh that's a red herring.

**Dave Jones:** So, let's have a look at this cap here. Ah, bingo. There you go. 0.162. So, technically, that's higher than what we had. So, there you go. Another rail. So, that cap there, um we've at least got one of those those caps, as I said, on that uh on that rail there.

**Dave Jones:** So, we'll find that one of these caps it's slightly laid out different here, but like this one over here will be possibly, yeah, 0.16. They're all slightly different layouts, these boards.

**Dave Jones:** 52 ohms. Yeah, um so, all right. Let's probably start probing some caps on the top and see I mean, we're getting a reference point at this connector down here.

**Dave Jones:** So, let's measure so sort of something right on the opposite side of the board, shall we, and see if that makes a difference. So, if our power connector's over here, let's try and get something like right over in this trigger section over here, perhaps.

**Dave Jones:** So, maybe not. I mean, it's it's not a definite, but I don't know. You'd assume that they'd maybe not in the trigger section. Maybe that's not No, it doesn't look like that might be the case.

**Dave Jones:** But, what about these little puppies down here, maybe? Although, these look like local regulators. So, we might be uh 2.7 ohms. Now, I've had a quick little probe around these ASICs.

**Dave Jones:** You can see these four large um ASIC ADC hybrid uh modules here in the circuitry on the back. They've got no uh bulk uh decoupling on there, just lots of small uh caps.

**Dave Jones:** And I've probed quite a few of those, and I can't seem to find any 3.3 volt rail on there, so that hybrid um doesn't seem to use any 3.3-V which is not terribly surprising, but these are the uh A6 or whatever they are under the uh heat sinks.

**Dave Jones:** I don't uh haven't got the heat sink off to uh look at the number on there. Um they that we looked at before, we can actually certainly trace those.

**Dave Jones:** So, let's um start doing that. I mean, once again, a reference point over here. .152 ohms. .15 1. I'm giving the board a bit of a flex there with my arm at the same time, which you probably can't see, but .152 Let's go across to the cap here.

**Dave Jones:** .154. You see how it's higher? I mean, we're talking what you know, 2 m higher there, but that is enough to tell us that it's closer towards here than it is here, that extra resistance.

**Dave Jones:** Now, if we go over to here, we should see slightly higher. So, I'm assuming. So, if this one is .157, let's say, and if we go, you know, if we know this point over here is lower, this one's higher, then something over here should be higher again or over here should be higher again.

**Dave Jones:** So, let's find the cap in there. I've got this on manual ranging now, by the way. Um just so it doesn't have to auto. Oh, hang on. .24. Probably not probing that thing right.

**Dave Jones:** There we go. No, look at that. It's lower again. That's quite interesting. Point it's lower. .148. Very, very interesting. It's higher over here, so this is now our lowest point.

**Dave Jones:** This is interesting. Let's go over here. .154 And I just expect this one over here to be higher. Oh, look. It's It's It's lower. Again, has it changed? Yeah, look.

**Dave Jones:** I'm putting Actually, that could be the solder joint. Well, the others I was putting a lot of pressure on that. .16 But you saw it go down before just a second ago to like close to .1 again.

**Dave Jones:** Put a bit of flexion on the board with my arm. No. Man, this is I was hoping this would be a good demonstration of troubleshooting this thing, but it seems to be all over like tracing down a classic short on a rail, but seems to be all over the shop.

**Dave Jones:** Ah, this is annoying. Just did that again off camera, and it once again it went down to .11 ohms. I swear. It did, and now it's back up. As soon as I press record, it's the white coat syndrome.

**Dave Jones:** As soon as the people in the white coats come around, the fault disappears. That's what that's a classic industry term. So, I'm going to actually mark these uh these ones with uh red so I can come back to them.

**Dave Jones:** That's the only one in that channel. So, I don't get uh don't have to dick around again. The ceramics in there as well are also um across the 3.3 V rail.

**Dave Jones:** So, there's a whole bunch of caps in there, but it's you know, if one if if it is one of the caps, it is most likely to be one of the uh talums, uh you would think.

**Dave Jones:** It doesn't necessarily have to be in this section. I still haven't fanned out over the board or anything like that. I'm just trying to get a reference point at the moment.

**Dave Jones:** I find it hard cuz this one here keeps jumping around, but it could certainly be. That could be a telltale sign that it is actually that um cap. And well, I don't want to be a bit premature and go sucking it off and um doing that yet, or maybe that could be a smart a smart move.

**Dave Jones:** I mean, you know, it could certainly be one of these um chips which has failed. Who knows? Um cuz we can't visually inspect that cuz these heat sinks are glued well and surely onto this thing.

**Dave Jones:** I don't think the 3.3 V is going into one of these uh ADC hybrids. So, um that doesn't look to be a problem, but there's no bypass caps on the top really.

**Dave Jones:** So, it all seems to be all the action appears to be on the bottom. Um I you know, there's no reason I target this area first other than the fact that it had its I know it's digital um because here's all the analog uh part of the board.

**Dave Jones:** Analog, analog, it gets a bit you know, it's still analog up to it hits the ADC hybrids here, and then it goes digital. And of course, uh 3.3 V rail is going to be used for digital.

**Dave Jones:** It's not going to be used for your ADCs and uh front end uh typically. So, um you know, something around here, and then you're going to get 3.3 V uh rails over on your uh memory modules over here as well.

**Dave Jones:** But as you can see, they've got no bulk uh capacitance. They've got no bulk capacitance down on there cuz all the bulk capacitance is localized on on the uh on the memory expansion board down in there.

**Dave Jones:** So, they've just got a couple of ceramics, and it could certainly be a ceramic uh for example, failing. Um I wouldn't completely rule it out, but uh you've got to go with the odds when you're troubleshooting stuff like this.

**Dave Jones:** And yeah, I don't know. I'm going to play around with that and give it a few extra little uh wiggles and pokes and see if I can get it to uh uh do something consistent.

**Dave Jones:** Now, I've probed a lot of the circuitry around here and as you can see there's not much in the way of bulk capacitors on here, just a few little tantalums around this shield here and all of this seems to be running from the 5-V rail because if we go down, you can actually you know, measure the 5-V rail on the pins of these chips.

**Dave Jones:** For example, oh sorry, you can't see the multimeter there, but it's showing a short which indicates shorted to the 5-V Well, you know, as it should be. It's It's connected to the 5-V rail.

**Dave Jones:** So, all this sort of stuff seems to be 5-V operated with a 3.3-V rail being used on possibly the memory modules here, I would suspect and at least one of the pins on these ASICs under here.

**Dave Jones:** So, I'm going to I can actually prove that the memory modules. Let's plug that in. And I'm guessing this would be 3.3-V logic as well. And yep, it is.

**Dave Jones:** There's our 0.17 ohms. So, you can see it's higher than what we've been getting cuz it has to go through the contact resistance of the connectors and stuff like that.

**Dave Jones:** And you can see why the 1 million ohm is important here. If we were trying to do this with anything less like a 10 million ohm resolution meter like the Fluke 87, we'd be really pushing the proverbial brown stuff up a hill with a pointy stick or a pointy probe.

**Dave Jones:** So, I'm having a bit of a hard time tracing this thing down. It seems a bit non-consistent. So, there seems to be some sort of possibly physical manifestation of the short which is not uncommon to you know, vary with time and pressure and you know, flex and all sorts of stuff like that on the board.

**Dave Jones:** So, really it you know, it's almost gotten to the point where Well, I know that there's four tantalum caps here and you know, I would always start out suspecting caps and I can't find any electrolytics on the board that are doing that.

**Dave Jones:** So, I think probably even at this early stage in the tracing process, I think I might just go bugger it. I'll get the iron out and just suck off those four tantalums and uh well, see if we get lucky.

**Dave Jones:** I I don't think we will, but it's worth a shot. Only takes a minute. And of course, I was a bit off there. There's actually two caps on the 3.3 V rail on each of those channels except this one over here.

**Dave Jones:** And of course, getting these caps off is pretty trivial. You get your two irons. Of course, I've shown this before with your wedge tips on them and get in there and bang and it's straight out.

**Dave Jones:** Piece of cake. And of course, what are our odds of that being the issue? I reckon Buckley's and Murphy's. Buckley's and Murphy's. Yep, 0.150 bugger. But maybe there's one good part about sucking out those caps.

**Dave Jones:** Let's put that back on our manual range. Is that we now have some really nice pads we can get down there with a lot of force and look I'm wiggling those probes and look 0.156.

**Dave Jones:** So, you can tell 158 so you can 159 is climbing. So, by wiggling those probes around you can tell that that contact resistance is pretty good. So, we're getting 0.158 on that channel.

**Dave Jones:** 0.156. So, it's gone lower. Let's check the cap next to it. 0.151 Ooh, right next to it really. 0.152 Oh, okay. They're actually connected via vias. Like on long looks like on long traces right down there.

**Dave Jones:** They're not a particularly uh low impedance path down there. 0.152 So, we're getting lower and all the way over here Aha, 0.158. Look at that. So, is that consistent with this one?

**Dave Jones:** Okay, you see how that's higher. These two are higher at than this one here. So, that indicates like that it's this area in here perhaps or you know, at equidistant um the short is equidistant between those.

**Dave Jones:** So, let's do that repeatedly. 0.15160 Jump up to channel uh three, we'll call it. 15 two Sorry, 154 that was, wasn't it? And this one seems to be lower at 0.148.

**Dave Jones:** So, there you go. That one is and this one should be slightly higher again. 0.1 Oh, no. 52 uh bloody hell. It's all over the shop. This is really embarrassing.

**Dave Jones:** Let's go to the main connector up here. And Oh, jeez. There's not much in it, but that is sort of sticking out a little bit. Now, I found and marked a red here.

**Dave Jones:** I found seven other ceramic caps which are on the 3.3 V rail. And well, really, we could keep sucking these off until the cows come home or uh we can go to plan B, which is actually um some people's plan A for uh shorts like this is uh hook it up to a high current uh power supply and see if we can blow the ass out of it.

**Dave Jones:** So, what we're going to do here, I've got my big uh 40 amp power supply set it to 3.3 volts. It's showing 3.2 volts on there. It's a smidge under.

**Dave Jones:** And it's capable of very high current. I got some very thick well, quite thick leads on it. And I'm just going to apply this over the 3.3 volt rail.

**Dave Jones:** Be sure you if you're going to do this, make sure you get the right polarity, of course. Otherwise, you're going to blow your board up. So, now the idea of this is that a couple of things could happen.

**Dave Jones:** One, you're going to heat up and blow that short out so that then you will get that visual hopefully, you know, with a smoke or you'll warp, deform, catch on fire, whatever.

**Dave Jones:** You'll get that visual indication of the exact component that's actually failed. Or you could actually blow it and then blow it open. And your short's gone. Well, that's not so bad because you you may blow it without any visual indications.

**Dave Jones:** And if you do that, then well, your board get your board powered back up again, but that chip or that cap or that part of the circuit that was failed has, you know, is not going to work.

**Dave Jones:** So, then you're, you know, back to square one almost start troubleshooting except you're not tracing a short anymore. You're tracing a, you know, a failed component. So, you know, one of all nothing can happen, of course.

**Dave Jones:** It's, you know, it could just heat up and you may not be able to find it. You may have to go over with your finger, try to find stuff that's hot or maybe a thermal imaging camera if you're really fancy fancy equipped like that or an infrared thermometer or something.

**Dave Jones:** You might be able to find the hot spot. But I'm just going to touch these terminals down in there. And I'm I can't I'll try and do this and we'll see what the current peak's up to.

**Dave Jones:** So, let's give it a go. So, hopefully, here we go. I don't uh get this wrong. So, I've got my black going to the negative. Make sure, you don't want to blow the board up.

**Dave Jones:** 1 2 3 4 5 6. So, that's our ground point and then our second pin, here we go. 11 amps. Woohoo! Something is going to be smoking. That's a lot.

**Dave Jones:** That's a lot of amps. So, I don't know. Can't smell anything yet. This is why you need a heavy duty power supply. So, now it's it's 11 amps and what now?

**Dave Jones:** I can just whip that off, turn it off and maybe All right. Nothing. Uh That's a bit of a bummer. Not entirely conclusive except for the fact that it's a solid, whatever it is, it's a very solid short.

**Dave Jones:** Now, I think the power supply in the in this scope is I think rated for about 6 amps on the 3.3 volt rail. So, it's rated for half that.

**Dave Jones:** So, um it's certainly not just a circuitry powered up, but anyway, let's uh see. Let's measure our resistance again and see if we haven't blown that thing out. No, we're still 0.16 ohms.

**Dave Jones:** There you go. Bummer. So, anyway, we do have a very solid short somewhere in this thing. So, I may have to leave it uh powered up a bit longer and I don't know.

**Dave Jones:** Maybe try and find a hot spot. Now, I've got some uh physical connectors in there now, so I can leave these uh permanently hooked up and I can start There we go.

**Dave Jones:** I can feel that warm. That chip down there's warming up. That one's warm. Yeah, they're all warming up. So, these chips are all powered up. I don't know. I guess I just leave it for a while and see which one I mean, you know, that is chewing a lot of power there.

**Dave Jones:** So, uh you know, it's chewing in the order of like you know, 35 watts or something. So, it's a fair amount. So, I might leave this and uh see if there's any visual indications.

**Dave Jones:** Well, I've checked the temperature on all all four of these heat sinks and uh they're all identical. So, it's not like there's one chip different and you'd go, "Aha, that one's getting twice as hot as the others, you know?" Um so, I don't know if that's their normal operating temperature.

**Dave Jones:** They're in the order of 65 to 70° or something like that. I mean, this thing uh takes a lot of uh power anyway. I'm not sure if that's normal.

**Dave Jones:** I The other service manual I had said um as I said, the 3.3 V rail was uh 6 amps capable or something like that. So, but it seems to be drawing uh you know, in the order of 11 amps, 35 odd watts.

**Dave Jones:** And of course, nothing else is getting uh warm at all. These main um hybrid ADCs here, which ordinarily get uh very hot as well, aren't. And none of the circuitry over here.

**Dave Jones:** So, as I measured before and suspected, that uh none of this is operating on the 3.3 V rail. Rail. Um you know, none of the front end, nothing like that um seems to be operating.

**Dave Jones:** So, it's only uh uh these four devices here plus the expansion memory. Oh, and of course the um if I plug the CPU board in there as well, the uh CPU might be taking some 3.3 V as well, but I've had this thing going for about 5 odd minutes now and well, nothing smoking yet.

**Dave Jones:** Bummer. And of course if the uh power supply in the unit was only rated for 6 amps on the 3.3 V rail, then that would explain why it's uh shutting down and this one is powering it uh just fine cuz the 3.3 V rail actually wasn't, you know, working.

**Dave Jones:** It had actually shut down. All the rails had um all the other rails had uh stayed up and they were spot-on, but the 3.3 V rail was uh uh dead.

**Dave Jones:** So, um yeah, maybe that uh power supply was going into uh uh you know, some sort of current limit mode or something like that and uh it it just uh wasn't capable of supplying, whereas this beastie will go up to 40 amps.

**Dave Jones:** No uh problems at all, so it'll, you know, power practically any loads you give it, which is why it's still sitting on uh 3.3 V. So, So, given that all four of these chips here are getting to equal temperature, it shows that they're probably good and uh you know, there's nothing um you know, wrong or blown inside those chips uh at all.

**Dave Jones:** Potentially, you know, not 100% sure, but it's you know, a reasonable guess um that that is the case. So, I guess all that's left really, if I think that this is the only um part of the 3.3 V circuit is to possibly find every darn cap on there and uh rip the darn things out.

**Dave Jones:** Uh what a pain in the ass. Now, I'd like to uh load test the power supply just as a matter of of uh course. I was going was going to use my dummy load, but then I looked at the uh manual and the uh power supply, at least on the M model, I assume it's the same for this C model as well, that the 3.3 volt rail comes off

**Dave Jones:** the five the 14 amp capable 5 volt rail there. So, you know, you really have to sort of load down both of them to check that it's actually capable of doing that.

**Dave Jones:** And I've plugged it back in here and yes, the 3.3 volt rail is still dead. So, whereas all the other rails are just uh just fine, really. So, we're only getting, you know, there's like .03 volts on the uh 3.3 volt rail.

**Dave Jones:** And the 5 volt rail is just hanging in there just fine and dandy. Well, as a matter of course, I did suck off every bypass cap on all of these channels on the 3.3 volt rail and no, didn't find it, of course.

**Dave Jones:** We're still getting .0 16 ohms or thereabouts in Really, I mean, uh I Am I chasing a red herring here? I'm not 100% um sure that I'm not, but you know, it seems likely because that is an an incredibly low resistance for a power rail.

**Dave Jones:** And of course, uh you power it up and it's drawing uh double what the manual um says it, you know, should that the power supply is even capable of on that rail.

**Dave Jones:** So, jeez, what's left? I mean, I may have missed the odd uh bypass cap on here, but I'm pretty sure that the 3.3 is only around um these four chips here plus the memory interface um expansion connectors here.

**Dave Jones:** And I've tried I've measured uh lots places elsewhere on the board and I cannot find the 3.3 volt rail going anywhere else. So, uh man, all that's left are these chips, I suspect, unless there's something else going on.

**Dave Jones:** Ah, I don't know. Running out of time here. Well, unfortunately, that is it for the day. I got to head off, but I hope you enjoyed that little troubleshooting exercise anyway, even though we didn't get the happy ending we wanted.

**Dave Jones:** Sorry, not all these things work out. So, yeah, if you want to discuss it, jump on over to the EVblog forum if you got any good ideas, of course, please do let me know.

**Dave Jones:** And yeah, sorry. These things aren't always easy. They do actually take time. What did I spend on this, like an hour or something? And I've Well, I have, you know, eliminated quite a few things, but yeah, we're still stuck.

**Dave Jones:** Something is going on. I don't know. Anyway, that's real life. Catch you next time.
