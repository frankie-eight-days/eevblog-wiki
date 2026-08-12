---
video_id: U6qZPx4uD0g
title: EEVblog #555 - 555 Timer Kit
url: https://www.youtube.com/watch?v=U6qZPx4uD0g
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 32, "3": 45, "4": 71, "5": 84, "6": 96, "7": 110, "8": 120, "9": 132, "10": 143, "11": 155, "12": 167, "13": 177, "14": 186, "15": 205, "16": 216, "17": 230, "18": 251, "19": 264, "20": 278, "21": 294, "22": 310, "23": 335, "24": 363, "25": 390, "26": 410, "27": 430, "28": 459, "29": 472, "30": 492, "31": 510, "32": 534, "33": 547, "34": 558, "35": 571, "36": 584, "37": 605, "38": 618, "39": 650, "40": 656, "41": 666, "42": 674, "43": 685, "44": 695, "45": 702, "46": 718, "47": 728, "48": 739, "49": 749, "50": 762, "51": 773, "52": 784, "53": 797, "54": 810, "55": 825, "56": 839, "57": 855, "58": 868, "59": 891, "60": 907, "61": 919, "62": 937, "63": 954, "64": 968, "65": 981, "66": 998, "67": 1024, "68": 1046, "69": 1060, "70": 1076, "71": 1087, "72": 1109, "73": 1125, "74": 1137, "75": 1151, "76": 1168, "77": 1187, "78": 1200, "79": 1215, "80": 1226, "81": 1240, "82": 1254, "83": 1274, "84": 1301, "85": 1319, "86": 1335, "87": 1345, "88": 1355, "89": 1368, "90": 1378, "91": 1391, "92": 1403, "93": 1415, "94": 1424, "95": 1440, "96": 1454, "97": 1472, "98": 1508, "99": 1525, "100": 1540, "101": 1553, "102": 1571, "103": 1602, "104": 1616, "105": 1630, "106": 1650, "107": 1662, "108": 1680, "109": 1700, "110": 1712, "111": 1736, "112": 1747, "113": 1766, "114": 1781, "115": 1796, "116": 1805, "117": 1835, "118": 1849, "119": 1865, "120": 1890, "121": 1900, "122": 1910, "123": 1920, "124": 1932, "125": 1947, "126": 1957, "127": 1964, "128": 1975, "129": 1993, "130": 2004, "131": 2018, "132": 2032, "133": 2047, "134": 2061, "135": 2073, "136": 2091, "137": 2101, "138": 2112, "139": 2126, "140": 2146, "141": 2156, "142": 2170, "143": 2179, "144": 2191, "145": 2205, "146": 2219, "147": 2231, "148": 2241, "149": 2257, "150": 2271, "151": 2284, "152": 2300, "153": 2322, "154": 2335, "155": 2349, "156": 2358, "157": 2371, "158": 2401, "159": 2411, "160": 2425, "161": 2438, "162": 2450, "163": 2466, "164": 2478, "165": 2489, "166": 2505, "167": 2519, "168": 2534, "169": 2552, "170": 2564, "171": 2582, "172": 2596, "173": 2622, "174": 2642, "175": 2660, "176": 2673, "177": 2686, "178": 2697, "179": 2713, "180": 2726, "181": 2740, "182": 2757, "183": 2772, "184": 2787, "185": 2799, "186": 2810, "187": 2821, "188": 2840, "189": 2852, "190": 2866, "191": 2895, "192": 2904, "193": 2923, "194": 2937, "195": 2949, "196": 2965, "197": 2977, "198": 2993, "199": 3004, "200": 3017, "201": 3038, "202": 3051, "203": 3082, "204": 3097, "205": 3111, "206": 3126, "207": 3138, "208": 3166, "209": 3181, "210": 3189, "211": 3202, "212": 3213, "213": 3231, "214": 3249, "215": 3268, "216": 3278, "217": 3289, "218": 3317, "219": 3331, "220": 3360, "221": 3369, "222": 3388, "223": 3402, "224": 3413, "225": 3427, "226": 3440, "227": 3456, "228": 3473, "229": 3496, "230": 3510, "231": 3523, "232": 3532, "233": 3546, "234": 3563, "235": 3578, "236": 3599, "237": 3609, "238": 3621, "239": 3631, "240": 3646, "241": 3665, "242": 3676, "243": 3699, "244": 3710, "245": 3721, "246": 3732}
---

**Dave Jones:** Hi, welcome to the 555th EV blog episode. At least the official 555th video anyway. I've done like over 600 or something like that, but the official count of the videos seems to matter to some people.

**Dave Jones:** So, if yes, of course we're going to look at the classic triple five timer chip in the 555th episode. Why? Because it's arguably the most famous chip of all time and 555 just has that significance in electronics.

**Dave Jones:** Everyone's familiar with it. It's one of the first chips you play with when you're a hobbyist, when you're a youngster or it used to be. Now it's a bloody Arduino or something like that, but it's still around and you know, until fairly recently they still sold a billion of these things a year.

**Dave Jones:** I'm not sure what the current figure is, but that was like an early 2000s figure, but this chip has been around for so long. It's been used in thousands of different applications thanks to the various building blocks of flexible nature of the building blocks, which we'll take a look at, which Hans Camenzind you know, famously designed this chip and there's lots of info out there on how he designed it and stuff like that.

**Dave Jones:** It really is just a beautiful, beautiful design. So, 555 triple five as we call it here in Australia. Let's not get started on the name, shall we? Holds a very you know, sentimental place in electronics.

**Dave Jones:** So, let's look at a discrete triple five timer circuit today using discrete transistors. I've got one of these Evil Mad Scientist Labs discrete triple five timer kits. They call it the three five kits.

**Dave Jones:** Anyway, it's worth playing around with and we'll go through the basic building the basic block diagram of the triple five timer and maybe some of the internal circuitry as well.

**Dave Jones:** Should be fun. Let's go. And here's the kit from Evil Mad Scientist Lab, the three fives. All right, no, it's the triple 5. Let's not go through that again.

**Dave Jones:** We've debated that endlessly on the amp hour. Anyway, discrete triple 5 timer kit. Recreate one of the most classic, popular, and all round useful chips of all time. A faithful and functional transistor scale replica.

**Dave Jones:** Awesome. It's actually a bit smaller than what I imagined it would be. Maybe I'm I got fooled by the the triple 5 timer stool. Anyway, this is really quite neat.

**Dave Jones:** They've got these really looks like they're machined. They're not molded. They didn't I don't think they had the volume to go for machine, but looks like yeah, they've been stuck on there.

**Dave Jones:** Look at right angles like that. So, they've been machined out and then like as a flat piece and then an angle cut on there and then they've just been glued in place.

**Dave Jones:** So, that's rather interesting and uh Here you go. We've got some really nice instructions. Look at that. Kit assembly instructions. Beautiful. But, of course, we don't need that, do we?

**Dave Jones:** No. Let's get straight into it. We've got ourselves a the bag of screws and stuff. Big thumb screws to screw into there and there's our board. 555 timer. Brilliant.

**Dave Jones:** Triple 5. And I hate that how they've the PCB manufacturers just smacked on their manufacturing code there. That just really pisses me off. Designed by Eric. I'm not even going to try and pronounce that, but good on you, Eric.

**Dave Jones:** Awesome. Evil mad scientist triple 5 timer kit. Fantastic. All the parts all through. Don't need the instructions because they've got the values marked on the silk screen, which is very nice.

**Dave Jones:** So, we'll jump straight into that and assemble it. Beauty. Check this out though. They've included a card of Tada! Resistors. Look at that. Isn't that brilliant? All individually marked.

**Dave Jones:** Fantastic. And check out the lovely matte black solder mask on there. It's beautiful. I got sick of black solder mask when I was at Altium cuz Altium usually did all their boards in Altium black and it had to be a certain type of black and it was gloss black and it's a pain in the ass.

**Dave Jones:** I hate gloss black. But I do like the look of the matte black, the contrast with the white silk screen on top overlay is just very nice indeed. Although the only problem with black is that you know it is quite hard to see the traces underneath.

**Dave Jones:** You can kind of sort of see them under there like that, you know, and it's a bit more visible on the bottom there, but you know, black isn't the best solder mask of any type if you're looking to see the tracks underneath.

**Dave Jones:** And considering that this is a fully routed board like this, you may as well have gone in there with the route path and just rounded out the little notch on there to signify pin one down here, but I love how they do have the pins numbered like that and you know, the big screwing thumb screws.

**Dave Jones:** It's just a beautiful kit. Really is. Well, I think the best feature of this is that the how they've divided the board into the functional blocks. We've got the threshold comparator, the trigger comparator, we've got the flip flop and we've got the output.

**Dave Jones:** Beautiful. And here we go. I'm using my inverted Manfrotto tripod here. I actually tried using that new Manfrotto flex with the super clamp up on the shelf there, but as I rocked the table, the camera would just you know, sort of you know, move back and rock back and forth and it wasn't that good at all.

**Dave Jones:** So I've had to revert to my inverted tripod arrangement. Anyway, this should be really easy to do. In fact, this will be just a single pass soldering thing where you just start all the components first and then just you know flip it over and do all the soldering all at once really cuz there's you know there's not a huge mixture of components just resistors and transistors very easy so let's give it a

**Dave Jones:** whirl shall we and we've got them all individually marked far too easy and we'll put this in I mean we do have npn and pnp transistors so we have to be careful 2n 3904s and 2n 3906s here but let's get we've got a whole bunch and we've got individual resistors here all marked and then we've got 2 4 6 7 of these where are they 4k7s so there's a

**Dave Jones:** whole bunch of 4k7s in there so let's get those in and I do enjoy building kits it is quite therapeutic I don't get enough time to do it one of the things you've got to be careful of when you actually rip these things out of this these leader tape holders here I've mentioned this before you can't actually get gum on the end these ones aren't bad at all but

**Dave Jones:** just be aware of that even with through hole stuff if they've got gum on the ends and they're a tight fit in the holes when you actually push those in then you know that can be a real issue it can get in the hole I mean you know it's it's not a it's not a huge deal but just be aware of it you can end up with a crappy solder joint on

**Dave Jones:** the top side not that it hugely matters just a little note for young players there so let's whack in all the 4k7s I'm just bending these by hand of course I don't really give two hoots about the exact bend radius and you know I'm pretty good like you know generally if you get this like a 400 mil spacing I think it is generally just bend them like that you

**Dave Jones:** know you're going to be pretty close and they're just going to fall into place nicely. Of course, I have to orient the uh uh the bands around all the right way, otherwise the electrons will fall out.

**Dave Jones:** Can't have that. And uh 4K7 was another 4K7, there's another 4K7. And uh And the 555 timer, of course, is famously supposedly using four 5K resistors in there in the uh divider string.

**Dave Jones:** And uh this one's obviously not. And there's the uh uh 4K uh 4K7s instead being an E12 uh preferred value. Not a uh not a big deal, but that uh sort of uh doesn't lead to the authenticity that the original triple five timer does.

**Dave Jones:** If you're a stickler for uh your history on this thing, it normally contains the internal 5K resistors, but of course, 5K is not a preferred value. Of course, you can get 499K, or you could put two 10Ks in parallel um to give you a total resistance of 5K, but uh it's not quite the same thing, of course, the chip.

**Dave Jones:** It's It's only a nominal value, of course, inside the chip. There we go. Now, all our 4K7s are done. Far too easy. 820 ohms. Where's our 820 ohms? People are probably screaming at me.

**Dave Jones:** I can't see it. I got to look all over here. There it is. Every resistor's a winner. And this is just a lovely lovely kit. I highly recommend it.

**Dave Jones:** It's about uh 35 bucks, I think, which is uh quite good value. Cuz, you know, there's not much in it, but uh you know, all the nice uh legs and everything um makes it well worthwhile.

**Dave Jones:** Um unfortunately, there's no like uh test points on the thing. But uh test points, of course, you can just hook them onto the leaded resistors, but just not as nice as nice big uh test points on the thing.

**Dave Jones:** Uh where are we? 1K. We've got 1K somewhere. There we go. And uh this is just a lovely 10K. This is boring commentary. I mean, people asked for me to build kits and stuff, and they go, "Oh, why don't you do video of you building kits?" Well, you know, look, it's boring.

**Dave Jones:** What What am I supposed to say? Well, it's not boring for me. I find it therapeutic, but for people watching, I don't see what uh value people would uh get out of watching me assemble kits.

**Dave Jones:** But, hey, this is the 555th video. It's the 555 video. So, you're going to have to endure me building the 555 timer kit. Of course, you do all your flat components first, like your resistors, so that you can actually flip them over.

**Dave Jones:** When you do solder them, they're all down at the one level. There's nothing worse than having a board that sort of, you know, rocks around, and you're trying to solder it.

**Dave Jones:** So, you solder up sort of each level. So, on a typical board, you do all the resistors first, for example, through-hole boards, then you do, say, all of the ICs, cuz they're nice and flat and stuff like that.

**Dave Jones:** So, you kind of like do all those. And, of course, I put a little bend on the pins like that. That's fairly common, just to hold them in place.

**Dave Jones:** Some people like the uh flip, you know, stands, the soldering stands, where you can actually just rotate, you know, easily rotate these things, hold them in clamps like this.

**Dave Jones:** And uh well, yeah, I don't have one of those. I just like um the feel of doing it by hand. I don't like our clamps when I'm doing boards.

**Dave Jones:** Not a huge fan of them. I can I can appreciate it for people who do it all day, every day. So, they're common in the production environment, for example.

**Dave Jones:** The good thing about these resistors, you probably don't have to bend the legs because they're a nice sort of snug fit in those holes. So, really, you know, I I don't have to bend those, but sometimes if you got a board with loose uh holes in there Oh, like that one there.

**Dave Jones:** See, that one Hey, there we go. No, I spoke too soon. It did fall out. There we go. But it doesn't matter. As I said, once you flipped it over, they're all going to sit down nice and flat like that.

**Dave Jones:** So, that's the advantage of that. Last one, 100 ohms. 100 ohms. There we go. They've given us the exact number of resistors. This is a beautiful kit. All labeled.

**Dave Jones:** Values labeled on the silk screen, so you don't have to reference the um uh schematic or anything like that. You can just build it up. Now, for the transistors.

**Dave Jones:** Now, our transistors are labeled 3904, um NPN 3906, PNP. Just your uh bog standard um signal transistor. Now, these ones you don't want to uh pull out or anything like that.

**Dave Jones:** They're really annoying. So, these ones you'd go along with your side cutters and just chop them off. So, there we go. We'll do our 3904s first. And if we try and stick it in like that, it comes down and Oh, no.

**Dave Jones:** No, there we go. It fits in. That's not bad at all. That gives it a nice snug fit. And you'll find that the pins on the other side push together a little bit.

**Dave Jones:** These are a nice fit. Especially for hand soldering, um because you just push them in and they sort of hold in place. So, very, very nice. Here we go.

**Dave Jones:** 3904s. Do do do. And they've got the emitter base collector marked on there, but of course, but um Oh, oh, I've got them backwards. Oh, I'm an idiot. Look at that.

**Dave Jones:** I've got two in backwards. I'm a total idiot. Look at this. There we go. 3904, there we go. Based on I wasn't even watching. I was too busy uh uh checking to see if the damn thing worked, but I caught myself.

**Dave Jones:** You know, that's the main thing. Mistakes happen. happens, folks. Can't avoid it. Murphy will get you every time. I'll probably put one of these in backwards and people will be screaming at me as I'm soldering the thing that I've got it all wrong.

**Dave Jones:** And so I assume that the pinout is correct because if they've goofed up there the flat on the silk screen, then well, the kit is hopeless. But I'm sure they haven't.

**Dave Jones:** So Nothing worse than having getting your silk screen wrong and then putting it in backwards and well, and there is something wrong worse than that is getting your getting your footprint wrong, getting your pinouts wrong.

**Dave Jones:** Very common. And happens all the time. Especially with transistors, which can be a real pain in the ass. Always double-check your transistor footprints, folks. Golden rule. Hopefully I haven't put a 3904 into a 3906 position.

**Dave Jones:** I don't think so. I just love the look of this kit. It's brilliant. How can you not like it? The matte black solder mask really really does the business on this board.

**Dave Jones:** Don't always like it, but as I said, it's infinitely better than the glossy one. If I'm going to get black, always get matte black. Glossy one is awful. And man, it just irked me every time at Altium.

**Dave Jones:** when I was working at out him bloody gloss black solder mask everywhere unbelievable. All right, yeah, the matte black bloody uh sorry uh gloss black solder mask got so sick of it.

**Dave Jones:** And uh and you couldn't see the traces that was a pain in the ass, you know, you got these really fine traces all over your board and you're building and testing prototypes and sometimes you'd have to hack them and uh uh it was just it was awful but hey it was the company standard.

**Dave Jones:** And it had to be the right type of gloss black, too. Uh man those were the days. That was a long time ago now. That was uh 2 and 1/2 years ago at least.

**Dave Jones:** And uh time flies when you're doing a video blog. Let me tell you. I'm got I've got to get one of these wrong. I've got to goof it up on camera.

**Dave Jones:** Murphy's going to get me cuz I'm not concentrating, you know, I'm just I'm just cruising here. I could almost do this blindfolded. Stevie Wonder style. So I hope you're enjoying this folks those who asked me to assemble kits.

**Dave Jones:** I'm assembling a kit. With pointless commentary over the top. I don't know don't know why anyway I've um what I've been doing at the moment I've actually been slowing down the videos um trying to get to the triple five video cuz I didn't want to like cuz I had all these other videos like the um Maker Faire for example.

**Dave Jones:** I've got like another couple of videos for the Maker another three or maybe even four videos for the Maker Faire of interviews and stuff and I didn't want to release them cuz uh that would have um screwed things up or at least if I adhere to my numbering system, I'll probably give it the same number but then call it, you know, video A B C or whatever part one, part two, part three.

**Dave Jones:** I'll give it the same EEVblog number. Um possibly. Yeah, it's always a toss-up whether or not to you know, off-topic kind of videos whether or not to actually give them an EEVblog number but I mostly do these days.

**Dave Jones:** Ta-da! We're all done. That is fully assembled, folks. Now, that that's still bugging me. That bloody PCB manufacturer putting their process mark on there. If you go to companies like uh PCB cart, uh for example, they now they never used to give you the option.

**Dave Jones:** They used to put this on and I used to complain by default and I used to complain all the time to them about the boards I got and they finally listened and now they've got an option on their shopping cart where you can say don't put any of that crap on my board.

**Dave Jones:** Thank you very much. And which is excellent but other manufacturers um uh other PCB supplies don't seem to do that. So, it's a bit of pot luck and when you're using a board as a front panel like this and it's important, you know, I've had front panels come back and then there's all this gar manufacturer garbage just spewed all over the front of your front panel.

**Dave Jones:** It's disgusting. So, oh I actually I probably should Yeah. Oops, that's silly. I should have soldered my resistors. Um that was dumb. Yeah, I goofed it, folks. I should have soldered those resistors because I was mentioning before how you flip it over and it holds them all down.

**Dave Jones:** Well, they're not. Oh, that was dumb. See what happens when you're too busy talking and you're not you know, do as I say, not as I do. So, yeah, that's pretty embarrassing but we're ready to solder.

**Dave Jones:** All right, here we go. Let's solder this sucker. I'm using 60/40 uh tin lead solder. There it is. Standard 60/40 stuff. Ancient multicore uh stuff. Not 0.46 mm really fine.

**Dave Jones:** As I've mentioned in previous videos, I do recommend your basic solder should be 0.5 mm or less than that. So, that's excellent. So, let's get in here. I don't use that lead-free stuff.

**Dave Jones:** It's just It's just not worth the hassle, really. And one of the issues here is going to be As I said, I should have uh uh done all the resistors first and cut their legs off and then done the transistors, but uh oops.

**Dave Jones:** Too busy yapping away. Not paying attention. And um But, that's not a problem. So, I'll just do all the resistor legs and cut them off. Now, one of the issues here, I'm trying to It's not easy.

**Dave Jones:** Usually, I'd be flipping this board around all the uh place while I'm actually uh soldering, but because I'm trying to keep it in a central location on the camera here, um it does make it a bit more difficult.

**Dave Jones:** So, this isn't my usual soldering style, I'm afraid. It's uh I get that in my soldering videos, the comments and things like that. People are going, "Why did you do this?

**Dave Jones:** Why did you do that?" And it's the you know, it's not my usual not quite my usual style. So, please forgive me. I just don't want to you know, move the board around everywhere.

**Dave Jones:** I want to give some uh nice visual quality to the video. That's the idea, anyway. If my hand isn't in the way, I don't know. I'm not looking at the uh screen at the moment.

**Dave Jones:** So, one of the issues I've got to blow the solder fumes away, because if I use my solder um my pace uh fume extractor, then um oops. Then, I'm uh uh going to It's going to be too noisy cuz that thing is like a freaking jet engine.

**Dave Jones:** It's It's just absolutely awful. I'm going to have to actually get some low-noise uh fans, you know, the silent uh fans, you know, some 12-V ones or something like that, some big ones, and just, you know, stick some batteries on the bottom, maybe with a you know, a couple of double A's and maybe boost the voltage up or something to power the fan, and um then uh I could just have it next to the

**Dave Jones:** work and just blow the fumes away cuz often that's all that's required. I'm choking on them. Um just to blow the fumes away, really, rather than uh Although, I could have one on the other side, so I could have I was possibly thinking maybe I'd have one that There we go.

**Dave Jones:** I think I got them all. One that um sits on this side here and blows across like that, and, you know, have another one which sits on the other side, which actually sucks through, and um just have some uh carbon filter on that one.

**Dave Jones:** So, sort of like I can position them uh anywhere. That would be uh you know, kind of good. I could have a, you know, a fan sitting here like this, fan sitting here, and it's going to blow across and suck.

**Dave Jones:** And if they're relatively um you know, those uh silent type ones, and I run them at a sort of a low-noise speed cuz you don't need a huge air flow to uh bring that across.

**Dave Jones:** Then, you know, that's not a problem. The fume extractors aren't that great because, you know, they've got to run really fast and loud in order to suck the fumes uh through cuz they don't have a hood on top.

**Dave Jones:** The best uh fume extractors I've used are, of course, the ones on a big snakey arm that, you know, come down and you can move them over your work, and the fumes just go straight up and get sucked in.

**Dave Jones:** But, when you've got a solder sucker that's on the side here trying to suck the fumes in. Uh it just, you know, it doesn't work really well. So, anyway, time to uh trim these leads off and uh let's have a look.

**Dave Jones:** Yes, this is going to be a long rambling video. As I said in a previously, what you do with your uh side cutters is getting there, but don't cut it flat like that.

**Dave Jones:** Actually, give it a bit of a tilt like that and tilting it up just gives it enough uh angle that you're not cutting into the solder joint, because you don't want to cut the solder joint.

**Dave Jones:** You want to cut the lead, not the joint. Uh sorry, I've got to move this one around. There's no there's no choice on this. Um it makes it really difficult.

**Dave Jones:** So, uh yeah, this is terribly exciting video, folks. I hope you're enjoying it. But anyway, some people wanted to see it and uh me assembling a kit. And well, this is what it's like.

**Dave Jones:** It's not exciting at all. And I just get to waffle on and on and on. In fact, I've had to um I've been sitting idle on this for a couple of days now.

**Dave Jones:** Oh, no, I missed one. There we go, I did miss one. Silly me. That always happens. Murphy'll ensure that you uh always miss a part. Don't always hold onto the leads, by the way, cuz uh these things can fly right up into your eye.

**Dave Jones:** Not good. So, there we go. Let me finish that off. And uh There we go. All right. Now, I can go around. And of course, because I did bend the leads on that, but um just check that, you know, none of them are sticking out really ugly or anything like that, you know, the uh visual aspect's kind of important, and I think I Yeah, I did double-check those

**Dave Jones:** uh transistors, and I had them in all the right way, so I can start again. Anyway, I was saying that I had to This soldering is actually uh three or four days after the previous scene, which was me actually assembling them in there, because I didn't uh have the time.

**Dave Jones:** I've had lots of uh family stuff on recently, and uh I haven't done anything for uh you know, 4 days or something like that, so I've only just gotten back into it.

**Dave Jones:** And at the moment, I'm busy um and I'm also busy working on my um new microcurrent, trying to get that sucker up and running, uh which is a lot of work.

**Dave Jones:** By the way, it's um as I've discussed many times on the blog and the Amp Hour and other places, it's uh you know, actually designing the circuit is uh is not the and laying out the board, for example, is not not a huge part of it.

**Dave Jones:** It's uh the bill of materials, finding components, in this case, really precise components and um certain types of switches. I'm going to move this around. Certain types of uh switch that I need, and uh getting stock of this sucker has not been easy, so I've had to uh actually commit myself to uh you know, several thousand volume of uh some parts, um just to get them so that I'm not caught short, cuz

**Dave Jones:** the last thing I want to do is run a crowdfunded campaign, for example, and find that I've, you know, got uh I'm oversubscribed, and then I can't deliver for 3 months because there's a, you know, um, a huge lead time.

**Dave Jones:** Some of these parts are like, you know, 12 weeks factory lead time. So, you know, so if I didn't buy stock now, I would have been, uh, I would have been screwed.

**Dave Jones:** So, you sort of I sort of had to buy up in some cases, I think, all of the world's stock these switches and, uh, and these resistors in order to, uh, in order to secure the, uh, success of my new micro current.

**Dave Jones:** Well, and, you know, I just be might like that, you know, no one wants to buy the thing and I'll be stuck with, you know, a reel of a thousand parts at $4 each, you know?

**Dave Jones:** And, um, yes, one reel of parts, you know, cost well over $4,000. This is crazy. And, uh, which sounds like a lot, but in the scheme of, uh, you know, um, if you actually make a thousand units, you know, it's, uh, and sell a thousand units, it's not much at all.

**Dave Jones:** It's all part of the manufacturing cost, but when you're got it up front, that cost up front and you, uh, don't have any sales to, at the moment, to pay for that, then, uh, you know, can be a real pain in the ass.

**Dave Jones:** So, sorry, I haven't been checking the camera. Has that been on camera? This is incredibly boring. I should just, uh, shoot video of me instead of the board, maybe.

**Dave Jones:** Yapping away. Got to try and keep good posture, too. Do pride myself on my posture. I do try and keep excellent posture, but, uh, you can find yourself lapsing here and there, which isn't good.

**Dave Jones:** Anyway, so that's what I've been working on for a while, and that's why I haven't really been coming out with the videos, and it's annoying me. And of course this one has to be the 555th video.

**Dave Jones:** So, it's not like I can release cuz I got other videos I can release, but I can't release them under the numbering scheme. Um otherwise, I'd get to 555, and well, it wouldn't be the triple 5 timer video building this thing, so that's no good.

**Dave Jones:** Don't want that. So, I've had to slow down a bit, and that's given me time to work on my micro current. I've been thinking about it for ages. I changed direction a couple of times, but I went back to what worked in the end, and it's just a more precise version.

**Dave Jones:** There we go. There it is. Oh, that's the entire board. Completed. Holy crap. There we go. I should actually trim off those uh leads, of course. Those transistor leads are rather annoying.

**Dave Jones:** Once you've got to trim those off, but anyway, once again, same thing like that, and then give it a tilt like that, so you're cutting into the leads and not the solder joint.

**Dave Jones:** That's a a uh real beginner trap that one, cutting into the solder joints. Although sometimes you have to, you know, you've got to grind them down sometimes. I've, you know, um ground boards down completely flat because you had to get it in some, you know, tight enclosure or something like that, or some physical reason why you've had to make all the leads flatten, and it had to be through hole

**Dave Jones:** instead of surface mount, for example, and yeah, I've done that uh done that more than once. That's for sure. And uh you know, it it works. There's nothing wrong with cutting into your solder joint.

**Dave Jones:** I mean, ultimately it works, but you can, you know, get the stress fractures in there and stuff like that. So, you know, it's just not best practice to cut into the solder joint, but in practice, even though it's not best practice, it does, you know, it it does actually work.

**Dave Jones:** Um But it just can't be counted on, that's all. And uh when you get a long-term a um you know, fracture like a a fracture in your solder joint that only shows up, you know, like it's an intermittent long-term problem or something like that, then that can really ruin your day, you know, it goes into a product, goes out in the field, and it only uh starts failing when it, you know, the

**Dave Jones:** joint heats up to a certain temperature in a certain environment or something like that, and you know, you trace it back to uh a solder joint. Now, that's just crazy.

**Dave Jones:** But it happens, and yeah, I've been caught with that before. But look at that. Ta-da! 555 timer board fully assembled. That was really easy. I don't know, I wasn't timing that, but it doesn't take long at all.

**Dave Jones:** Um it would have been uh quicker if I didn't uh have the camera going and wasn't taking my time and just went all over the place. Sorry, that's just blurry.

**Dave Jones:** That's just going too quick cuz I can uh solder really quickly if I am so desired. So, here you go. Going to screw in the yeah, terminals on that and make it look like a real 555 timer.

**Dave Jones:** I just noticed here the tips on that how to solder. Got really nice little uh diagrams here. I rather uh like that. But they say um but step um two, of course, you know, uh or step two, place the solder against the joint that you wish to connect.

**Dave Jones:** So, and put the solder on fir- uh touch the solder to the joint first and then touch the iron to the solder joint for about 1 second. That's no, that's back-to-front.

**Dave Jones:** You need to put the iron onto the joint first and then the solder. Although you may have noticed, you know, do as I say, do as I say not as I do.

**Dave Jones:** You may have noticed that I sort of, you know, might have put them on at the same time when I was doing that, but yeah, you're supposed to heat up the joint first then apply the solder.

**Dave Jones:** That's how it works. That is the industry way to do it. And these funky looking IC legs just screw in there with these little cap head screws. Rather annoying that it's not Phillips, you've got to go find your uh um hex driver for that, but still that looks really neat.

**Dave Jones:** You know, the black matches the black solder mask and I love cap head screws. They're just really neat. So that's just beautiful. And there's all the pin tails. Keep those, folks.

**Dave Jones:** They can come in real handy. Trust me, always have a component drawer full of offcut pin tails. They're just great. Ta-da! There's the finished article. Isn't that cute? I love it.

**Dave Jones:** That's just great concept, brilliant, and the thumb screw terminals on here even got red and black for the power and the five or six other pins. Sorry for all the control signals.

**Dave Jones:** The only issue with this that immediately comes to mind as well. Okay, I've got to hook this damn thing up now and I like the thumb screw terminals, but if I have to get, you know, a resistor from over here to over here, it's not going to reach.

**Dave Jones:** I'm going to like it's not just like a breadboard where everything's nice and tight and all the components, external components, are designed to, you know, fit around the regular sized IC on your breadboard and it doesn't do that.

**Dave Jones:** So you've got to use like clip leads and wire and things. Goodness, but jeez, it's fun and you get to play around with the individual segments and probe stuff inside your 555.

**Dave Jones:** Brilliant. And once again, very detailed instructions on this thing. So, you know, if you're really after a beginner's kit, this one, you know, is really quite good in terms of, you know, soldering through-hole stuff and just, you know, getting a nice little practical circuit to play around with.

**Dave Jones:** And they've given you a suggested test circuit. What I even like more is that they point to Colin Mitchell's Talking Electronics site for more stuff. Definitely check out Colin Mitchell's Talking Electronics site.

**Dave Jones:** And I've done some interviews with Colin Mitchell, one of my heroes who taught me electronics way back in the old days. So, there you go. And let's wire up this 555 LED blinker.

**Dave Jones:** Well, see if it blinks. I've probably goofed something up. Probably won't work. Bloody Murphy. Well, of course, astute viewers will know that my first mistake is to think that pin four was ground.

**Dave Jones:** It's not on a 555 timer. Pin four is reset. The 555 timer goes against the regular, you know, opposing side pinout on there. Oh, I just, man, I was not thinking this was a 555 for some reason.

**Dave Jones:** I don't know. Geez, I've known the 555 timer pinout for, you know, 30 years or more, but, you know, still screwed it up because I'm too busy yapping away.

**Dave Jones:** I'm just not paying attention. And of course, I don't follow instructions. There we go. Now, we're ready to go. So, here we have it all wired up. And yes, it's a bit messy to actually use it in this configuration.

**Dave Jones:** Yes, you can get resistors directly from point to point like that. So, the classic astable configuration like this, you do need, you know, a couple of wires coming around here.

**Dave Jones:** I didn't want them going over the top like that because we're going to be probing stuff on here. I've got a 3.3 V 3.3 mic cap 450 V. I think it'll do it.

**Dave Jones:** Anyway, that's what I got out of my junk bin. I got a jumbo LED as well. Considering that this is a jumbo 555 and here it is, classic astable configuration for the 555 timer.

**Dave Jones:** It does warn you though, it's not a direct replacement if VCC is greater than 6.5 do not connect reset directly through cuz normally the reset pin four would be connected directly to pin eight up here, but it says you got to put a 100k in series.

**Dave Jones:** So, that's a limitation. So, it's not a direct functional equivalent. Although they recommend they say that it should be in most uses and configurations, but that is one small trap there.

**Dave Jones:** So, we've got a 100k pulled up there and we should blink our LED at I don't know a hertz or two, something like that. Haven't done the calculation, but flip the switch and I've got it powered from 9 V.

**Dave Jones:** Let's have a look. It's on. Hey, it's blinking. It's blink. We have a blinker. There we go. Works a treat. We obviously don't need anything on the control voltage really cuz it you know, it doesn't matter a rat's ass.

**Dave Jones:** That's just basically some internal bypassing and stuff. So, really we're looking pretty. Look at that. It works. Bobby dazzler. Oh, and by the way, this isn't a plastic. It's a hard cell PVC foam.

**Dave Jones:** So, you can actually get in there and dent that if you really want to, but that's really neat stuff. You can make some cool stuff out of that. It's lightweight and rigid, but easy to cut and mold.

**Dave Jones:** The model making industry use it extensively, you know, the props industry and model making type stuff use this hard cell PVC foam pretty extensively. Now, here is where we're going to get a bit messy, but stick with me and apologies at the start.

**Dave Jones:** I haven't thought this through. So, I'm a kind of winging this, but we're going to have a look at the 555 circuit diagram here. Now, this is one of the more disappointing things with Well, the most disappointing thing with the kit is that it's designed to, you know, allow you to play with and a transistor-based replica of a 555 timer.

**Dave Jones:** And it neatly divides them into the threshold comparator, the trigger comparator, the flip-flop, and the output, and the reset, and all that sort of stuff. But, what it doesn't do is give you a circuit description of how any of this works.

**Dave Jones:** And I think that's greatly lacking for people who want to It almost defeats the purpose of the kit, really, cuz who wants to play around with the outside? You want to get in there with your scope and look at waveforms and do things like that.

**Dave Jones:** So, it really, you know, would pay for them to have some sort of, you know, a deep description or, you know, at least some sort of description of how the arrangement works in here.

**Dave Jones:** Anyway, I'm going to have a crack at it and do a few notes, if I may. Now, the first thing I notice is that this these three resistors here aren't part of this trigger comparator.

**Dave Jones:** So, I'm going to draw a dashed line down there like that because these a And they should be, by the way, 5 K because well, 555 555. Now, of course, Hands on Cams in, I think, has actually said that no, that has nothing That's not why it was named that because it actually had, you know, the five nominal 5 K resistors in there.

**Dave Jones:** The number was just a, you know, next in their sequence or something like that. I don't know. It's got nothing to do with it. But, by coincidence, it does have 555 in there.

**Dave Jones:** And that's just a resistor divider in there to generate the threshold voltages. And of course, the control voltage pin is directly connected to one of those taps here. Now, what I've got is basically the same diagram that's on my 555 timer shirt.

**Dave Jones:** This is the typical internal block diagram of the 555 timer, and we'll see how these modules relate to these items in here, like the threshold comparator. There's the comparator, of course, uh connected to the threshold pin.

**Dave Jones:** We've got our trigger comparator, sometimes called the upper and the lower comparators. This is the that goes to the trigger pin in there. Um and there's the 555 5K resistors in there.

**Dave Jones:** They set the threshold values for those trigger comparators. Then, we've got ourselves a flip-flop here, which we'll take a little look at. And then, we've got our output driver here, and then our discharge um pin over here, and the reset is tied into the flip-flop.

**Dave Jones:** So, we're going to come back to this um periodically, but let's uh start out with, say, the threshold comparator over here and see what we've got. Now, in the threshold comparator, it looks a bit complicated.

**Dave Jones:** They've got all these transistors connected in weird and wonderful ways like this, but it breaks down fairly simply. And let me briefly explain. What we've got here basically are two inputs to our comparator.

**Dave Jones:** One here, which is the threshold pin, the other comes from the voltage tap on our 555 um resistor ladder there. So, these are the two inputs to our comparator, just like you'd get a regular uh comparator, you know, LM311.

**Dave Jones:** You've got your positive and your negative input there. And this is a um typical arrangement. What it is is basically a differential pair amplifier. And uh but it's working as a comparator cuz there's no external feedback to make it work as an amplifier.

**Dave Jones:** And usually, these are pretty crude amplifiers, but they do work uh reasonably well as comparators, but not on their own. You've got to have some current sources, which we've got up here, that just make them a bit less sucky as comparators.

**Dave Jones:** So, uh what we've got here actually is these two transistors here and here, there's nothing unusual about these arrangements at all. That's just a Darlington pair. So, you know, if you're familiar you should be familiar with the Darlington transistor pair, there it is.

**Dave Jones:** So, they've just got extra uh gain in there so that the um input current on the pins is very small for a particular gain. So, they're just increasing the gain with a pair of Darlingtons.

**Dave Jones:** No issue at all. No magic going on there whatsoever. Once again, there's nothing tricky going on up the top here um at all really. It's a standard building block component called a current mirror and that's what this uh these arrangements of these two transistors um does here.

**Dave Jones:** Now, what we've actually got here, okay, is this You see how the the uh base is connected to the collector here on this one and this one. Well, basically what that is acting as is a diode.

**Dave Jones:** So, essentially what this thing is here is just a diode connected like that. And this arrangement I won't go into how current mirrors work, but basically that's a you know, I could do it like a Fundamentals Friday video on that, but basically the current flowing in there and down there like that is going to be equal.

**Dave Jones:** So, that's all there is to it. And likewise on this side over here, they've got exactly the same thing. This arrangement is going to be a diode like that and by current mirror action we'll call it the current flowing down here is equal to the current flowing down here.

**Dave Jones:** And that's all you got. So, they've got two constant current generators. Sometimes they'll have the constant current source down in the bottom resistor down here. They'll replace that with the constant current, but what they've got it is the constant current up the top, and I won't go into the pros and cons of various arrangements, but that's what they've decided to do in this arrangement.

**Dave Jones:** So, constant current feeding this so it acts as a, you know, a decent comparator, and then the output in this case is tapped off here, and this is one of our outputs.

**Dave Jones:** In fact, that is the reset output coming out of our comparator into here. So, we can go over here and label that input uh on our flip-flop there. So, that's all there is to it.

**Dave Jones:** So, that is not too dissimilar to just a regular comparator chip that you would buy off the shelf. Now, over here in the trigger comparator, it's essentially uh the same function.

**Dave Jones:** It's just a comparator because, look, it's it's really no different except we've got our external input going to the negative input, but they've decided to configure this transistor arrangement differently using PNP transistors down here instead of NPN.

**Dave Jones:** And actually, this is a more typical uh comparator arrangement you'll find in uh commercial comparator chips which you can just uh buy off the shelf, but it essentially works just the same.

**Dave Jones:** We've got a constant current going down here by virtue of this transistor over here. Once again, we've got our current current mirror arrangement. This is actually, once again, we've got ourselves a diode in there.

**Dave Jones:** So, the current um flowing down here is going to be a constant current setting the bias for this comparator down here. Very simple. And once again, we've got another Darlington arrangement there as well, but with uh PNPs instead of NPN.

**Dave Jones:** And then we've got our output being tapped off here, and so that becomes our set input to our And there's the output of the comparator. That's the set input going into our flip-flop block over here.

**Dave Jones:** So there you go. We've got our two comparators there with the R and S inputs to the flip-flops. Too easy. This one here is not actually one of part of this functional block arrangement.

**Dave Jones:** They're just got like a jewel current sourcing arrangement here. That's actually I think that's probably clever. Hans has probably done a trick or two in there to save the odd transistor, I think.

**Dave Jones:** That could be neat. That could You could go into more detailed analysis of why that is done. But as you can see, it's pretty much following this arrangement we've got here.

**Dave Jones:** So as I said, this one helps provide constant current to both of these points down here. So we've got Basically, let's have a look at our flip-flop arrangement now.

**Dave Jones:** Now, technically, it's probably not correct cuz it's not really a clocked flip-flop as such. The more correct term would be an RS latch. And that it should have four two inputs two output Sorry, three inputs and two outputs.

**Dave Jones:** Reset pin. We've already got our R and S here. And of course our reset arrangement comes from over here into there. So there it is. So that's our Well, RS.

**Dave Jones:** So we'll call that RST. Reset there going into our flip-flop. And these here are our So that's our Q output, and that's our not Q output from our flip-flop block.

**Dave Jones:** So how does this RS flip-flop block work? Well, it's rather interesting. Now, a normal RS, you know, textbook RS latch like this made up of two NOR gates like this cross-coupled NOR gate and of course you might have a a third input here for your reset you know, external reset pin, but that is not what we find here because we have a look at a typical old school data

**Dave Jones:** sheet for a NOR gate. I mean, look at how many transistors we've got. We've basically got an inverter and some NAND gates and inverts the output and that's you know, basically how it does it.

**Dave Jones:** Now, you in fact often you'll see this configuration in a 555 timer you know, block diagram instead of just showing it like this. They might actually show these cross-coupled RS flip-flops, but look at how many transistors we've got to implement and that's just for one NOR gate.

**Dave Jones:** So, we'd have to have two of those in all of this up here and we don't have that. We've just got some constant constant current source up here. That's pretty much it.

**Dave Jones:** So, these transistors down here we don't have enough to implement this classic arrangement. Well, we don't have to cuz what they've done is what Hans has done is implemented the classic two transistor arrangement like this.

**Dave Jones:** RS it does exactly the same job and you'll notice it may not look like the same as this, but it actually is. Follow with me here. Let's assume that this is the Well, we know this is the set input here, okay?

**Dave Jones:** So, this is the base of the set transistor here. This is our set transistor and that then feeds back via a resistor here back to the base of the reset transistor.

**Dave Jones:** There's our reset input. So, this is our set transistor down here. This is our reset transistor and you'll notice it is cross-coupled back. Here it is, cross-coupled back there to there, but there's no resistor in there.

**Dave Jones:** Where is that resistor? Well, we don't need it because we've got that constant current source coming from over here. So, we don't need that series resistor. So, we're not going to blow our transistor.

**Dave Jones:** It already is limited by the internal constant current arrangement of this chip. And it's very common for the chips like this to have constant current generators everywhere. Like a typical comparator might have three or four constant current generators in it all over the place.

**Dave Jones:** And things like that. So, that's the way they've got away with directly connecting the transistor in there like that. And by the way, this um array this particular uh circuit is taken directly from the original Signetics triple five time data sheet, which is fantastic, which I'll link in down below.

**Dave Jones:** They've got some excellent drawings in there as in hand-sketched uh little cartoony drawings. Fantastic. But anyway, that was a little aside. We've got this classic arrangement using these two transistors here.

**Dave Jones:** Very minimalist uh design. Fantastic. They don't even need that resistor in there. And it's um and you'll once again notice this arrangement here is our diode. So, we've got a effectively a diode like that, and that's what allows us to feed this external reset into basically the uh same arrangement as the into the uh reset flip-flop, which then is buffered from the output of here.

**Dave Jones:** So, we've taken We're basically taken the output from our reset There it is. We're taking our output from here, like this, from our reset uh uh transistor. Sorry, not reset flip-flop, reset transistor.

**Dave Jones:** And that is then driving that through this constant current generator here, and that is driving our complementary outputs of Q and not Q. That's all there is to it.

**Dave Jones:** It's a very clever implementation of a basic RS latch. I really like it. And then from our Q and not Q, we can see how these drive the output buffer and the discharge transistor down here.

**Dave Jones:** Here's the output buffer block and you can see that it is driven by the Q output there. And basically that's a totem pole arrangement. Once again, we have ourselves a diode in there like that.

**Dave Jones:** And so that is just a buffer to drive this totem standard totem pole output like that. Too easy. So these are all just you know standard building blocks. So when you know your circuit building blocks like your totem pole output, like your diode from the transistor, you got your Darlington pairs, you've got your current mirrors, and you know, it all sort of starts to make sense and come together this

**Dave Jones:** convoluted circuit diagram. Once again, here is the uh um not Q output coming via a resistor there. There it is. Straight into the open collector output discharge transistor. Too easy.

**Dave Jones:** So there you go. I hope you found that brief walk through somewhat interesting. And of course you could play with this to your heart's content. And that's the beauty of this kit.

**Dave Jones:** You can get in there. You can see what the current mirror mirrors are doing. You can see how the RS latch is working. See how the totem pole output works, the comparators, everything like that at the transistor level.

**Dave Jones:** It's brilliant. And it's a shame that this kit doesn't come with a really detailed circuit explanation of how this works cuz it's a great learning tool I think for discrete transistor design.

**Dave Jones:** And yes, I've probably goofed something up in there. I haven't really thought about this in detail. There's probably a few nice little tricks in there that Hans put in to sort of optimize this and lower the transistor count and get the performance required and you know stuff like that.

**Dave Jones:** So not really going to go into deep analysis of this thing. By the way, the LTSpice circuit simulator the free one from Linear Tech comes with a transistor level 555 timer circuit.

**Dave Jones:** It's or it's not too dissimilar to this. It is you know functionally identical to this. It's a drawn a bit different of course uses the transistors in a different sort of arrangement but it allows you to play around with a 555 timer in a circuit simulator and that's one of the examples that come with it.

**Dave Jones:** So I highly recommend you download that have a play with it although I haven't played around with it myself so I don't know how it performs and simulates but I do know it's there.

**Dave Jones:** All right, let's take a look at some external scope waveforms or external to the chip and we're basically following our standard got our a stable circuit built as shown here.

**Dave Jones:** Now the yellow waveform is pin six which is the threshold comparator pin. The green waveform there is pin seven which is the discharge open collector discharge output and the blue waveform of course is our output voltage and you'll notice that well there's our output voltage and you see the blue waveform like that and that's that's what when it goes high of course it's switching on our LED because we've got

**Dave Jones:** it driving the LED via the anode there. Now if we have a look at our yellow waveform here the charging that's the main capacitor that's the one 3.3 micro farad capacitor charging up via the 200k resistors there.

**Dave Jones:** So 200k in series via 1 micro farad and that's the charging waveform, so you can use your formulas to calculate how long that's going to take to charge up, and then it is when it reaches the threshold voltage, if we have a look at our internal block diagram of a 555, the comparator, because of the 555 K resistors in there, it's 2/3 the threshold comparator is 2/3 of the

**Dave Jones:** supply voltage. In this case, the supply voltage is 9 V, so our threshold voltage is going to be 6 V. And is it? Here's ground. We're at 2 V per division, 2 4 6.

**Dave Jones:** It switches at exactly that 6 V threshold limit. And then, once that happens, our discharge pin kicks in, so our not Q output turns on the discharge transistor, which then discharges the current.

**Dave Jones:** Please excuse the crudity of all this. Then it discharges the charged 1 microfarad capacitor, which is currently at 6 V, and discharges it through the 100 K resistor down to ground like that.

**Dave Jones:** And that's exactly what we're seeing there. It's discharging back down. It's taking half the time that it took to charge up, because it's only going through a 100 K resistor instead of the 200 K.

**Dave Jones:** And of course, then our trigger comparator down in here is measuring that value at 1 because of the 55 K resistor divider in there. It's 1/3 of the supply voltage or 3 V.

**Dave Jones:** And bingo, look, it discharges from 6 V down to 3 V, and then the cycle starts again. And of course, I'm preaching to the converted. Most of you know about a standard 555 timer operation.

**Dave Jones:** So there it is. It's all confirmed and verified. Works a treat. Now, what we can do with our fourth channel, the pink channel here, which I'm uh touching it my finger, we can probe around the circuit here and uh have a look at some of the waveforms, shall we?

**Dave Jones:** Let's uh take a look at our um reset input of our RS of our flip-flop latch here. So, that's the collector of Q6, and luckily they have labeled emitter base collector on the overlay, and there it is.

**Dave Jones:** You can see that our output there because it's it's actually quite small. That's uh 500 mV per division. So, it's about 600 mV, one diode drop. So, that But, that is basically switching that uh constant current source off and on there, which goes then into um our flip-flop over here.

**Dave Jones:** And let's have a look at our set one. That should be much lower. We should be looking at diode drop switching there. So, look at base of Q15, which is There it is.

**Dave Jones:** Base of Q15, and there we go. We're not actually getting a pulse. Uh well, what are we getting? Just a pulse on that. Check that out. Up. No, there we go.

**Dave Jones:** My trigger point's a bit off, but yeah. You can see we're just getting that little um set pulse down in there. Just once again, that's only a single diode drop.

**Dave Jones:** There it is, 500 mV per division. Single diode drop just to switch that transistor back on and change states. Then we can have a look at things like this uh constant current output here, which will be uh switching, of course.

**Dave Jones:** That's our drive, the buffer drive going into our uh Q and not bar output. So, let's have a look at the uh collector of Q19A. There we go. Collector of Q19A, and there we go.

**Dave Jones:** It's switching. Now, if we have a look at our Q output here. Let's have a look at that. That is the collector of Q20. Yeah, where is it? Emitter, base, collector.

**Dave Jones:** No. Collector. There it is. And that is our Q output going into our final output buffer stage, nice and squared up. Huge voltage there, almost full swing. And our not Q output here is once again only small.

**Dave Jones:** We're only talking, you know, a diode drop sort of level there. There we go. And we can have a look at the things like, you know, the constant current output here for example of our Q9.

**Dave Jones:** So, let's take a look at the collector of Q9 there, and you'll see that that that was just a some contact bounce there, and you'll see that that is basically just a steady state voltage, that steady state current.

**Dave Jones:** And of course, we're only looking at the voltage here, but basically that's going to be a constant current source coming out of there to bias all of our trigger comparator circuitry down here.

**Dave Jones:** So, you can just probe around the circuit here to your heart's content and figure out exactly what's going on, and maybe compare it with the So, it's a really handy kit to figure out how this sort of stuff works.

**Dave Jones:** Of course, there's going to be, you know, process technology differences between a discrete transistor design like this and the actual manufactured 555 timer IC of course, but you know, functionality-wise, it's going to operate fairly similar.

**Dave Jones:** Now, if we actually probe the outputs of our set and reset transistors here inside our latch, so we'll probe the collectors there, you'll see that they'll be opposite polarities, both single diode junction.

**Dave Jones:** So, let's have a look at the set Q15, the collector of that and you'll notice how that is There you go. It's positive. Whoop. Positive going while the output is low and we should get the opposite on Q 16 down here, the collector of that one and we do.

**Dave Jones:** There we go. It is low when the output is low. So, there you go. I hope you found that interesting. If you're still with me after what's it been an hour or so, uh well well done sticking in there.

**Dave Jones:** But, uh yeah, I was going to do a few more things for this uh 555 timer video, but uh you know, things happen and uh they just don't get done.

**Dave Jones:** Maybe for 556, I don't know. But, anyway, um if you enjoyed it, please give it a big thumbs up and if you want to discuss it, jump on over to the EVblog forum.

**Dave Jones:** Catch you next time. Good on you, Hans. What a beauty.
