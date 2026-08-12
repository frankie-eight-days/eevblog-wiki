---
video_id: 2AcpRCNhbsw
title: EEVblog #1327 - 3 Ways to FAIL at PCB Manufacture
url: https://www.youtube.com/watch?v=2AcpRCNhbsw
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 28, "3": 44, "4": 58, "5": 75, "6": 87, "7": 99, "8": 113, "9": 126, "10": 139, "11": 155, "12": 170, "13": 189, "14": 205, "15": 230, "16": 245, "17": 261, "18": 277, "19": 297, "20": 308, "21": 323, "22": 337, "23": 352, "24": 364, "25": 377, "26": 388, "27": 402, "28": 412, "29": 424, "30": 435, "31": 452, "32": 469, "33": 480, "34": 494, "35": 510, "36": 525, "37": 542, "38": 562, "39": 575, "40": 593, "41": 606, "42": 620, "43": 633, "44": 650, "45": 664, "46": 676, "47": 693, "48": 709, "49": 724, "50": 738, "51": 750, "52": 765, "53": 779, "54": 793, "55": 805, "56": 823, "57": 838, "58": 853, "59": 867, "60": 881, "61": 892, "62": 905, "63": 918, "64": 934, "65": 949, "66": 964, "67": 977, "68": 994, "69": 1011, "70": 1029, "71": 1049, "72": 1065, "73": 1082, "74": 1099, "75": 1117, "76": 1130, "77": 1151, "78": 1169, "79": 1183, "80": 1197, "81": 1214, "82": 1226, "83": 1241, "84": 1263, "85": 1277, "86": 1291, "87": 1304, "88": 1318, "89": 1334, "90": 1349, "91": 1361, "92": 1375, "93": 1388, "94": 1403, "95": 1413, "96": 1431, "97": 1448, "98": 1459, "99": 1472, "100": 1487, "101": 1501, "102": 1513, "103": 1525, "104": 1537, "105": 1549, "106": 1566, "107": 1581, "108": 1590, "109": 1622}
---

**Dave Jones:** Hi, let's talk about PCB manufacturing and how you can easily come a cropper and there's a real trap for young players in terms of the manufacturing tolerances and manufacturing specifications for PCBs and possibly to do with Gerber generation as well. And

**Dave Jones:** this comes about from a discussion we had on the Amp Hour hasn't been released yet but by the time this video comes out probably will be released as an Amp Hour episode. So let's take a look some PCB

**Dave Jones:** design stuff. And yes, due to popular request I have green t-shirt floating Dave head. Let me know down below if you like this. I think it's a bit weird. I think I've gone a bit far. Said I should write a script to like

**Dave Jones:** randomly like like make my head just float around like in a Lisa just pattern. That'd be nice, wouldn't it? So let's talk about when you get your PCB manufactured. Let's go over to JLCPCB here only because that's the one that was discussed in the Amp

**Dave Jones:** Hour and somebody came a cropper on this. I won't mention who but anyway, it's it's a real easy trap and you're almost going to certainly cop this if you like and push the envelope in terms of clearances and and PCB specifications.

**Dave Jones:** You're doing really fine pitch BGA stuff. You need to route stuff out very finely then. Anyway, you can really come a cropper. I'm sure I've covered in previous videos. One of the first rules of when you start laying out a PCB, you

**Dave Jones:** know, you've done your schematic and then you import all your part footprints and your net list and you're ready to start routing. You set up all of your clearances. You set up your trace widths and you know, other sorts of you know,

**Dave Jones:** trace to via things and your via hole sizes and yeah, you know, you set up all this stuff first before you start routing and you base that information all the track and space and clearance and design rule DRC checking stuff on

**Dave Jones:** the capability of the PCB you're getting manufactured. Especially if you're going after one of these cheap $5 prototyping services and you need to do something really fine, like fine traces and and clearances and things like that, uh this

**Dave Jones:** is where you can come a cropper. So, normally you'd go down here and you go minimum trace width and spacing. Every PCB manufacturer will have their capabilities uh page. So, you go over to here, minimum uh trace track width and

**Dave Jones:** spacing. This is the main one you want here. And the PCB in question was a four-layer PCB. So, they actually have a better specification here uh four layers. They actually have 3.5 mil or 3.5 thou, which is equivalent

**Dave Jones:** supposedly to 0.09 mm for your four- and six-layer boards. It's not as good for your one- and two-layers. They're a bit more loosey-goosey on those. That's, you know, 5 thou uh clearance, but 3.5 thou clearance sounds like, oh, you know,

**Dave Jones:** that's that's heaps. I can do anything with that. Well, then let's have a look at that, shall we? But, the first thing to note is 0.09 mm here. Does that actually equal 3.5 mil? Let's get our confuser and check. So,

**Dave Jones:** 0.09 mm divided by 25.4 mm cuz they actually one point I can't forget the date, but they find it spot on as 25.4 mm is There it is. Oh, it's back to front. Sorry. The Yeah, the camera's back to front. Oh, no, I'll

**Dave Jones:** just read it. 3.5433 0708 7 thou. But, they've rounded it to 3.5 thou here. So, they've Whereas, it's actually 3.54 thou. So, you might say, well, what's the big deal with that? It's close enough. Round it off. Well, aha, here's

**Dave Jones:** where you can come a cropper. Because you're only paying five bucks for your board or whatever, you're sharing a panel with like a hundred other designs, they don't want to dick around and spend time and treat you special just for your

**Dave Jones:** 100th of that one board, right? So, they have these limits for a reason and if you have a look at everything else, everything else seems to be like in millimeters. We've got clearances. Here we go. Clearances Everything's in millimeters,

**Dave Jones:** but they gave you the value in thou. So, if you like laying out your PCBs as I do with all your traces and spaces as thou, and there's nothing wrong with that, then you can come a cropper. If you go in and

**Dave Jones:** to your PCB software and set your limit as 3.5 mil or 3.5 thou, you're actually going to be under that 0.09 millimeters. So, they're going to all their software, their Gerber checking software will automatically reject your boards. They won't just automatically

**Dave Jones:** manufacture. They'll come back to you as the example on the amp hour, they come back to you and say, "Hey, sorry, you don't meet our specification." But, then you go to them and say, "Oh, but look, it's on your website, 3.5 mil." Well,

**Dave Jones:** 3.5 mil is actually different to 0.09 millimeters. And it looks like the manufacturing engineers at the PCB company, they sort of looks like they're using millimeters metric for everything. So, even though they've, you know, just tried to be nice and giving you this in

**Dave Jones:** 3.5 mil, just be aware, there is going to be a rounding error here and you can fail your their automatic checking and then you might have to go in and redo your entire board because they're not going to be flexible enough for five

**Dave Jones:** bucks, they're not going to be flexible. They're going to say, "Sorry, your board's rejected. Please meet 0.09 millimeters." Doesn't matter what it says on the website. So, first rule is beware of companies that mix their units like this. So, if we're in our PCB

**Dave Jones:** software and we're in like you can change between inches and millimeters here. I'm using KiCad by the way. If you go into inches mode and then you set up your board, you know, you're about to lay it out and your track width here

**Dave Jones:** you've set it to precisely 3.5 mil. So, aha, I'm I've obviously met their specification. No worries, she'll be right. And then you go in there, but if you switch to millimeters and you lay out your whole board, you can spend a

**Dave Jones:** whole week laying out your board, go to get it manufactured, and then what? They say, "Sorry, we're not going to touch that with a barge pole because it's slightly under and they do care. All it is is a go no-go thing. Does it meet

**Dave Jones:** their 0.09 millimeters?" Well, if you switch to millimeters mode, oh, we're 0.0889 millimeters now. What what what what? Hang on.

**Dave Jones:** So, and there's no point arguing with them either. They're not going to argue with you. As I said, for their five bucks board or whatever. If you're paying for the whole panel, like if you're paying hundreds of dollars

**Dave Jones:** tooling charge and you're getting the whole panel, right, they'll they'll bend over backwards to accommodate you. If you're getting these cheap boards like that and you're one of a hundred different designs on a panel, they're not going to care. You're under the 0.09

**Dave Jones:** millimeters and you've come a cropper and they're not going to make your board. So, you might have to go in there and then change all your traces and then you might find all the clearance. Look in here. Let's say you widen that to

**Dave Jones:** like four mils, something like that. Oh, look, see? We've violated our clearance rule in here for the spacing between the pad and the trace here. Aha, we've got different specs for that. So, if you've gone in there and gone, "Oh, okay, I've changed

**Dave Jones:** all my traces to four mils. Yeah, no worries." Let's run the design rule checker and you run your DRC and you go "Track too close to pad because that's their minimum specification for the like distance between the track and the pad

**Dave Jones:** like that and you've just you're just a smidgen over only needs to be a smidgen over. Remember this is software doing this, right? Humans aren't going to override this unless you're paying them money and then they'll rub their chin

**Dave Jones:** and go, "Oh yeah, yeah, she'll be right. No worries." You know, but no, they're just going to automatically reject your board because it's you know, 0.01 mm over the you know, the tolerances that they specify. Let's go back to the

**Dave Jones:** website here and trace width and spacing is not the only thing you need to look at. You would think that okay, the minimum spacing is three you know, 0.09 mm. So you set that and you're good to go. Uh-uh, look at this, right? These

**Dave Jones:** are their minimum They've also got minimum clearances for all different types of geometries and they can be out by large values, too. Let's have a look at this. So let's have a look at the difference the minimum spacing between a

**Dave Jones:** track and a pad, which is actually what we've got here. We've got a a pad and a track on our BGA chip. 0.2 mm. So much for your 0.09 mm. What? You can only do in Look, they they could reject your

**Dave Jones:** board because it's only you know, if you're closer than 0.2 mm. Wow. So let's go into our board setup here. Let's go into our nets. 0.15 mm clearance. Well, what did we say? It's 0.2, right? That's what we need between a pad

**Dave Jones:** and another trace, right? So you might have to you would have to net classes, you would have to set up different net classes cuz we have different specifications or you might run your DRC twice, for example, and then have

**Dave Jones:** differences between trace to trace specification, which is 0.09 mm, and a trace to pad, which is 0.2 mm. So, if you go in there, I've got a 0.1 mm grid here, right? So, 0.1 0.2 mm. That's the absolute minimum that they will accept

**Dave Jones:** for pad to trace. If you've got a BGA chip here, right? You can't route out these traces like this. This just assume that this trace is actually connected up there. I can't do this because I don't have a

**Dave Jones:** schematic. There's no netlist. And it looks like in KiCad, you can't manually input a netlist and like a generate a new net on the PCB to join this track to this track manually, anyway. It doesn't matter. So, just assume that that's that

**Dave Jones:** you wanted to route these traces out here between the pads like this. You couldn't do it on that JLCPCB four-layer board. They could actually completely reject your board if you wanted to do that. You'd have to put a via in there

**Dave Jones:** and drop them out. So, yeah, just be careful. Like rule number two is look at all the different specifications. It's not just the the trace width specification minimum trace width to spacing. You've also got all these other things. And then they've got like you

**Dave Jones:** know, the the pad to the track and things like that. Via to track and all sorts of other different specifications. And they can be really tricky to actually program into your software. I don't know how you do that in KiCad, actually, cuz I'm not

**Dave Jones:** a huge user of KiCad, but they could reject your board just based on that. And imagine if you went to all the time and effort to lay out that board and find out you couldn't get your $5 prototype. Wah, wah, wah, wah. Not all

**Dave Jones:** manufacturers are going to be you know, like have these sorts of differences. Some of them will all they'll care about is trace width and spacing. And technically, there's no manufacturing etching process reason why there should be a difference in the

**Dave Jones:** specification between the a track a copper track and a copper pad and two traces like this just two traces separated apart. In fact, that technically the requirements more stringent for the two traces parallel like this cuz you could have two traces

**Dave Jones:** running right across your board like that and they're only like, you know, 3.5 thou 0.09 mm actually between them and you just got to etch out that little tiny slither of copper where as a track to a pad is like technically it's only

**Dave Jones:** that one little bit there. So, what's going on here is it must be to do with drill tolerances because a pad a typically this shows a hole. So, it's there's going to be drill tolerances drill wander and drill tolerance they

**Dave Jones:** can, you know, little skid off a little bit and you can potentially get breakouts in your pad. That's why you need minimum annular rings on your vias and your pads and stuff like that and really if that wanders across and if

**Dave Jones:** this was only 0.09 mm away, then technically even though your pad would still be good. It might, you know, it could wander closer to the track and then if your tracks only three and a half thou might break it. You know,

**Dave Jones:** things like that. So, but technically copper to copper there's no difference. That's why some manufacturers will only give you this track and space and that applies to everything. But, JLC have decided you know, quite a few manufacturers do

**Dave Jones:** they have different tolerances for different things. Definitely something to watch out for and you'll see there's definitely a drill related aspect to this cuz it's got PTH which is plated through hole to track. This is just pad to track I copper to copper. This is

**Dave Jones:** actually from the hole. You'll see it's it's not from the top here. It's actually from the hole over to the track just in case the drill wanders. Wiggle wiggle wiggle yeah. And then you've got like totally contradictory stuff up here

**Dave Jones:** nothing to do with holes. 0.127 mm for pad-to-pad clearance. Pads without holes, different nets. What's the difference between that and the two traces down here, which are going to be different nets? Huh? But it's there. Technically, they can reject your board.

**Dave Jones:** You know, you think you got 0.09, but technically, if you got two different nets with two pads, 1.27 mm. Thank you very much. So, yes, let let's just look at the example here. This is a BGA. This is not a dense BGA. Um oh, fine pin

**Dave Jones:** pitch BGA. This is 0.8 mm pin pitch. This is like, you know, almost positively enormous by my, you know, compared to like this one over here. Let's go over to this one. This one is 0.4 mm. So, this is half the pin pitch

**Dave Jones:** of this one over here. Look, this is the keep out that you need around that pad in theory from JLCPCB. You couldn't even route You couldn't even drop a via down there on this 0.3. Now, whether or not

**Dave Jones:** JLC actually push that point, you know, actually enforce that 0.2 mm, uh you know, pad to or whether or not it's only through hole pads. Why that make a difference? I don't know. Um pad to trace cuz maybe they could uh you

**Dave Jones:** know, the drill could slip and it could come near the edge of the pad or something like that and you could get a possible breakout and then that could potentially break through your trace or not. Maybe that's a that's a thing, so

**Dave Jones:** they might not care. But hey, a via is going to be a drilled hole. Unless, you know, all this laser micro drilling and stuff like that, but we won't go into details. Like even at 0.1 mm, okay? Look

**Dave Jones:** at that. Oh, yeah, yeah, you'll just have a room for a via in there, maybe. But we won't go into the specifications for vias and the annulus ring and, you know, all that sort of stuff. So, anyway, I'm sure I've done

**Dave Jones:** that in previous videos. Right, so let's just say that your manufacturer had a 0.15 mm clearance, for example, right? And you're trying to route out this BGA here, and you set your trace to 3.5 mil here, 3.5 thou. You know, you've got a

**Dave Jones:** little bit You've got a little bit of room left in there. Don't push the limits of these specifications. Like, I would go like, you know, "Can we go 3.7?" Something like, "Yeah, we can easily go 3.7, and still we're not going to come a

**Dave Jones:** gutter on those clearances. So, don't push the limits. Just cuz the manufacturer says you can do 0.1 mm trace or 3 thou trace, don't do it unless you absolutely have to and you're absolutely careful about your metric and

**Dave Jones:** imperial units and the conversion to and from. Now, there's actually another way that you can come a gutter here, and that's actually when you generate Gerber files. It's not really going to be a problem in KiCad here, but it can be in

**Dave Jones:** other software. When you plot your Gerber's, most packages are going to give you the option They call it the coordinate format, but really it's it's resolution. It's how many digits of resolution you're going to export in into your Gerber files. Now, KiCad give

**Dave Jones:** you two only two options here, which is good, as we'll see in a minute. 4.5 or 4.5 or 4.6 unit millimeters. It's a I don't like the way they've named this, cuz as I said, it's resolution. What 4.5

**Dave Jones:** stands for is it's not not actually 4.5. It's four is the number of significant digits before the decimal point. So, in terms of millimeters, you can have 9999 mm, right? That can be your maximum maximum number it can put in the Gerber

**Dave Jones:** file. Then, the dot five, that means five decimal places. So, with reference to 1 mm. So, effectively, this uh choosing this 4.5 option gives you a resolution of {point} double O double O five millimeters, which is more than enough.

**Dave Jones:** You're not going to You're not going to get have to worry about rounding errors between uh you know, Imperial and metric and stuff like that doing that. And 4.6, that'll be {point} double O double O O six millimeters

**Dave Jones:** resolution. Got it? But, other packages like Altium here, uh cuz you know, Altium's It's been around a long time, probably before you were born. And if we go to our fabrication outputs here, and we generate our Gerber files, okay? They give us the option in

**Dave Jones:** inches or millimeters here. And if we go to millimeters, and they don't use 4 .2, they use 4:2. So, that means you have four significant digits and uh two only two decimal places for millimeters. So, if you chose

**Dave Jones:** this 4:2 option here, it would generate go Oh, yeah, it actually tells you here has 0.01 mm resolution. 4:3 has one micron because it's 0.001. Got it? But, it varies with inches. You saw that KiCad it as far as I'm aware,

**Dave Jones:** it only has the option to output Gerbers in in metric. Uh whereas Altium can do it in millimeters. And uh you can have the same thing with reference to 1 inch here. So, if you choose 2:3 like this,

**Dave Jones:** it has a 1 mil resolution, 1,000 resolution. If your trace is 10.5 mil, for example, right? 10.5 thou, when you actually render that, it's going to render that as uh either 10 or 11 thou. It's not going to give you your 10.5

**Dave Jones:** thou. You're limited in your output resolution. Okay, so what I've done is just place some traces here and I've set them at different widths. I set it at 10.1, 10.2, 10.5, 4, 5, and 10.6. Now, let's generate the Gerber for this thing

**Dave Jones:** and let's choose that 2 3, i.e. 1 mil resolution. It warns you here. 2 4 and 2 5 only need to be chosen if objects on the grid are finer than 1 mil or 1 thou and we've got that. If you

**Dave Jones:** don't understand what this format is, you can kind of come a gutser. Let's generate our top layer and bingo, we've got our CAM file down here. Oh, this this Camtastic Gerber viewer Gerber viewer is awful. I'm going to something

**Dave Jones:** else. So, let's use the Gerber viewer in KiCad, shall we? Unfortunately, I can't get right on there, but you can see it's exactly the same. It hasn't increased the resolution there. Unfortunately, I believe this is like the lowest grid. I

**Dave Jones:** don't believe you can set a custom or finer or non-snap grid in KiCad. Please leave it in the comments down below. In the Gerber viewer, you can do it, a custom grid in the PCB, but Gerber viewer seems to be different. So, it's

**Dave Jones:** somewhat annoying. So, you know, please bear with me, but like, you know, fair enough, good enough for Australia. There you go. That's 11 thou. Okay, it's jumped up to 11 thou. You can see how just the resolution is not there. Let's

**Dave Jones:** just generate that again, but using 2 5. So, that'll give us a .01 thou resolution, right? Plenty, absolutely plenty. So, let's do that. Bingo, we've generated that. Open PCB 2. Now, hopefully, we've got different size traces here. Oh, it's like 10. Let's

**Dave Jones:** call that 10.1. Anyway, you can see how that is over 10.2 there. That's just the resolution on here. You can see that just the Gerber viewer resolution is not there. Let's go to the second last one, which is

**Dave Jones:** supposed to be uh 10.5. And yep, yep, there we go. 10.5 mil, near enough, because the Gerber viewer is not perfect. But if you had a perfect Gerber viewer that let you measure that exact Let let me know if you can

**Dave Jones:** actually get the information how to Can you just click on that object and get the width? I don't think there is any. Anyway, you can see how that resolution option in generating your Gerbers can make a difference in roundings. You

**Dave Jones:** thought you were safe with your 3.5 thou uh you know, minimum or whatever and they reject your board and you're like, "Oh god, I can't I'm going to have to re-route this thing or like large parts of it uh because you were trying to push

**Dave Jones:** the limits of your PCB designs." So, there you go. There's three ways you can come a cropper there, actually, with uh getting your PCBs manufactured like this. The first one is the difference between the rounding errors between imperial and metric and how your

**Dave Jones:** particular manufacturer actually enforces uh those. And don't expect miracles for your five-buck board delivered or whatever it costs. Um yeah, if you pony up the money, yeah, they'll bend over backwards, but otherwise, no. Don't get angry at them because, "Oh,

**Dave Jones:** you said on your website 3.5 thou and I set my thing to 3.5 thou and I spent a week laying out my board. You damn well better manufacture it for five bucks." Like, no. They're just going to tell you

**Dave Jones:** to bugger off. So, yeah, just be careful, especially when websites like do those conversions and they don't add up. You know, if they're going, "Uh it's 0.09 mm or 3.5 thou." Same thing. You go, "Well, no, it's not." You should

**Dave Jones:** question like really question them or simply don't push the limits unless you absolutely have to. And if you are pushing the real fine limits, probably you don't want to use the prototype uh services anyway, you know, you might uh

**Dave Jones:** pay, you know, pony up a bit more and uh get uh you know, like better tolerances and more controlled and more flexibility in that sort of thing. So, the second one can be those differences between trace width and minimum clearance. Just like you

**Dave Jones:** know, really be careful, take note of these, don't just go by oh, it's 3 1/2 thou, so it's it's it's 4 4, you know, uh good enough. I'll set all my traces to four and she'll be right. And you can

**Dave Jones:** come a cropper with much larger specifications for other objects, various uh clearances and things like that. And then you've got BGA clearances like this minimum BGA pad dimensions and stuff like that. These may conflict with these minimum clearances up here. Look

**Dave Jones:** at this, 0.2, once again, 0.25 mm for the same minimum pad dimensions and stuff like minimum distance between BGA, there you go, 1. 127. And this figure here, 0.127 mm, that's coincidentally the same as this pad-to-pad clearance up

**Dave Jones:** here. So, different nets, nothing to do with holes at all. So, one of the issues here could be related to actually the solder mask, which you wouldn't necessarily think of, and solder mask alignment, cuz you've got solder mask uh

**Dave Jones:** slivers. I won't go into it, but there's there're going to be a minimum thickness of solder mask you need, just like uh trace width on your copper layers, you're going to have the same minimum uh you know, amount of solder mask sliver

**Dave Jones:** between your pads like this. So, you're going to be limited to solder mask expansion around uh your pad on your BGA, and then not only that minimum, but then you also got the alignment as well. So, maybe this is partially uh related

**Dave Jones:** to the alignment of of what they're capable of in their solder mask uh alignment, cuz then you start getting like solder mask over the pads, overlaid onto the pads and stuff like that, and that's not terrific, but you know, what

**Dave Jones:** do you want for your five bucks? And what do you know, they do have a solder mask section. Here you go, 0.2 mm. Although, that seems to be that's not the solder mask slither, that seems to be pad to pad. So, there you go, solder

**Dave Jones:** mask bridge spacing between copper pad edges must be 0.2 mm. Or does that mean that they'll touch your gerbers? And like if you don't have the minimum solder mask expansion, they'll expand it for you or something like that, or

**Dave Jones:** you've got too much and they'll reduce it. Don't like that. Don't like any company touching my gerbers, but you may not have a choice when you're using one of these prototype service panels. When you're paying for the whole panel

**Dave Jones:** yourself, you can demand things, but not when you're designing not when you use these, you know, five bucks for your five boards on your prototype panel. No, you get what you get. As we teach our kids in preschool, you get what you get

**Dave Jones:** and you don't get upset. So, again, there's no actual process technology reason why there would be an electrical difference between a pad and a pad on a BGA. I mean, technically, if they can do 0.09 mm here, technically, they can do

**Dave Jones:** it here. So, it's to do with other factors. Yeah, it's interesting. You've got different all these different options. And then the third one, of course, is generating your gerber files, the resolution, which you may not have known about before, but now, hopefully,

**Dave Jones:** you do. So, anyway, I hope you found that video useful. If you did, please give it a big a thumbs up. Let me know about the floating Dave head. Severed I I don't think I'll do the severed Dave

**Dave Jones:** head. I'm not I'm not a fan of it. I don't I'm not liking the It's It's It's greatly disturbing. Really is. Anyway, catch you next time.

**Dave Jones:** Mhm.
