---
video_id: U6qZPx4uD0g
title: EEVblog #555 - 555 Timer Kit
url: https://www.youtube.com/watch?v=U6qZPx4uD0g
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 36, "3": 47, "4": 62, "5": 74, "6": 90, "7": 105, "8": 120, "9": 134, "10": 150, "11": 164, "12": 178, "13": 198, "14": 213, "15": 229, "16": 247, "17": 259, "18": 270, "19": 284, "20": 300, "21": 317, "22": 333, "23": 346, "24": 363, "25": 381, "26": 394, "27": 405, "28": 415, "29": 427, "30": 444, "31": 461, "32": 477, "33": 502, "34": 518, "35": 534, "36": 549, "37": 566, "38": 579, "39": 599, "40": 611, "41": 644, "42": 655, "43": 666, "44": 677, "45": 690, "46": 701, "47": 713, "48": 724, "49": 739, "50": 757, "51": 769, "52": 782, "53": 803, "54": 819, "55": 836, "56": 850, "57": 868, "58": 894, "59": 900, "60": 917, "61": 937, "62": 948, "63": 965, "64": 983, "65": 1004, "66": 1021, "67": 1034, "68": 1046, "69": 1063, "70": 1076, "71": 1085, "72": 1099, "73": 1114, "74": 1127, "75": 1141, "76": 1165, "77": 1182, "78": 1200, "79": 1215, "80": 1230, "81": 1249, "82": 1265, "83": 1282, "84": 1294, "85": 1312, "86": 1326, "87": 1341, "88": 1351, "89": 1366, "90": 1376, "91": 1387, "92": 1403, "93": 1417, "94": 1435, "95": 1451, "96": 1467, "97": 1488, "98": 1504, "99": 1517, "100": 1537, "101": 1556, "102": 1571, "103": 1588, "104": 1604, "105": 1621, "106": 1636, "107": 1656, "108": 1674, "109": 1687, "110": 1703, "111": 1727, "112": 1747, "113": 1764, "114": 1776, "115": 1792, "116": 1805, "117": 1823, "118": 1837, "119": 1852, "120": 1866, "121": 1882, "122": 1894, "123": 1909, "124": 1920, "125": 1935, "126": 1947, "127": 1959, "128": 1969, "129": 1983, "130": 1997, "131": 2011, "132": 2032, "133": 2046, "134": 2061, "135": 2077, "136": 2091, "137": 2106, "138": 2119, "139": 2139, "140": 2156, "141": 2170, "142": 2182, "143": 2198, "144": 2216, "145": 2229, "146": 2241, "147": 2256, "148": 2275, "149": 2289, "150": 2303, "151": 2316, "152": 2330, "153": 2343, "154": 2354, "155": 2368, "156": 2390, "157": 2405, "158": 2418, "159": 2434, "160": 2446, "161": 2460, "162": 2476, "163": 2491, "164": 2505, "165": 2519, "166": 2534, "167": 2552, "168": 2567, "169": 2582, "170": 2599, "171": 2615, "172": 2631, "173": 2648, "174": 2659, "175": 2673, "176": 2689, "177": 2703, "178": 2724, "179": 2738, "180": 2754, "181": 2772, "182": 2789, "183": 2803, "184": 2819, "185": 2838, "186": 2857, "187": 2875, "188": 2892, "189": 2906, "190": 2923, "191": 2939, "192": 2957, "193": 2975, "194": 2990, "195": 3004, "196": 3017, "197": 3033, "198": 3049, "199": 3070, "200": 3090, "201": 3108, "202": 3123, "203": 3142, "204": 3157, "205": 3175, "206": 3189, "207": 3202, "208": 3217, "209": 3231, "210": 3253, "211": 3268, "212": 3279, "213": 3299, "214": 3315, "215": 3331, "216": 3346, "217": 3362, "218": 3376, "219": 3398, "220": 3413, "221": 3430, "222": 3445, "223": 3461, "224": 3478, "225": 3498, "226": 3514, "227": 3529, "228": 3544, "229": 3563, "230": 3585, "231": 3605, "232": 3617, "233": 3631, "234": 3648, "235": 3667, "236": 3684, "237": 3702, "238": 3714, "239": 3729}
---

**Dave Jones:** Hi, welcome to the 555th EV blog episode. At least the official 555th video anyway. I've done like over 600 or something like that, but the official count of the videos seems to matter to some people. So, if yes, of

**Dave Jones:** course we're going to look at the classic triple five timer chip in the 555th episode. Why? Because it's arguably the most famous chip of all time and 555 just has that significance in electronics. Everyone's familiar with it. It's one of the first chips you play

**Dave Jones:** with when you're a hobbyist, when you're a youngster or it used to be. Now it's a bloody Arduino or something like that, but it's still around and you know, until fairly recently they still sold a billion of these things a year. I'm not

**Dave Jones:** sure what the current figure is, but that was like an early 2000s figure, but this chip has been around for so long. It's been used in thousands of different applications thanks to the various building blocks of flexible nature of

**Dave Jones:** the building blocks, which we'll take a look at, which Hans Camenzind you know, famously designed this chip and there's lots of info out there on how he designed it and stuff like that. It really is just a beautiful, beautiful

**Dave Jones:** design. So, 555 triple five as we call it here in Australia. Let's not get started on the name, shall we? Holds a very you know, sentimental place in electronics. So, let's look at a discrete triple five timer circuit today

**Dave Jones:** using discrete transistors. I've got one of these Evil Mad Scientist Labs discrete triple five timer kits. They call it the three five kits. Anyway, it's worth playing around with and we'll go through the basic building the basic block diagram

**Dave Jones:** of the triple five timer and maybe some of the internal circuitry as well. Should be fun. Let's go. And here's the kit from Evil Mad Scientist Lab, the three fives. All right, no, it's the triple 5. Let's not go through that

**Dave Jones:** again. We've debated that endlessly on the amp hour. Anyway, discrete triple 5 timer kit. Recreate one of the most classic, popular, and all round useful chips of all time. A faithful and functional transistor scale replica. Awesome. It's actually a bit smaller

**Dave Jones:** than what I imagined it would be. Maybe I'm I got fooled by the the triple 5 timer stool. Anyway, this is really quite neat. They've got these really looks like they're machined. They're not molded. They didn't I don't think they

**Dave Jones:** had the volume to go for machine, but looks like yeah, they've been stuck on there. Look at right angles like that. So, they've been machined out and then like as a flat piece and then an angle cut on there and

**Dave Jones:** then they've just been glued in place. So, that's rather interesting and uh Here you go. We've got some really nice instructions. Look at that. Kit assembly instructions. Beautiful. But, of course, we don't need that, do we? No. Let's get

**Dave Jones:** straight into it. We've got ourselves a the bag of screws and stuff. Big thumb screws to screw into there and there's our board. 555 timer. Brilliant. Triple 5. And I hate that how they've the PCB manufacturers just smacked on their

**Dave Jones:** manufacturing code there. That just really pisses me off. Designed by Eric. I'm not even going to try and pronounce that, but good on you, Eric. Awesome. Evil mad scientist triple 5 timer kit. Fantastic. All the parts all through.

**Dave Jones:** Don't need the instructions because they've got the values marked on the silk screen, which is very nice. So, we'll jump straight into that and assemble it. Beauty. Check this out though. They've included a card of Tada! Resistors. Look at that. Isn't

**Dave Jones:** that brilliant? All individually marked. Fantastic. And check out the lovely matte black solder mask on there. It's beautiful. I got sick of black solder mask when I was at Altium cuz Altium usually did all their boards in Altium black and it had

**Dave Jones:** to be a certain type of black and it was gloss black and it's a pain in the ass. I hate gloss black. But I do like the look of the matte black, the contrast with the white silk screen on top

**Dave Jones:** overlay is just very nice indeed. Although the only problem with black is that you know it is quite hard to see the traces underneath. You can kind of sort of see them under there like that, you know, and it's a bit more visible on

**Dave Jones:** the bottom there, but you know, black isn't the best solder mask of any type if you're looking to see the tracks underneath. And considering that this is a fully routed board like this, you may as well have gone in there with the

**Dave Jones:** route path and just rounded out the little notch on there to signify pin one down here, but I love how they do have the pins numbered like that and you know, the big screwing thumb screws. It's just a beautiful kit. Really is. Well, I

**Dave Jones:** think the best feature of this is that the how they've divided the board into the functional blocks. We've got the threshold comparator, the trigger comparator, we've got the flip flop and we've got the output. Beautiful. And here we go. I'm using my inverted

**Dave Jones:** Manfrotto tripod here. I actually tried using that new Manfrotto flex with the super clamp up on the shelf there, but as I rocked the table, the camera would just you know, sort of you know, move back and rock

**Dave Jones:** back and forth and it wasn't that good at all. So I've had to revert to my inverted tripod arrangement. Anyway, this should be really easy to do. In fact, this will be just a single pass soldering thing where you just start all

**Dave Jones:** the components first and then just you know flip it over and do all the soldering all at once really cuz there's you know there's not a huge mixture of components just resistors and transistors very easy so let's give it a

**Dave Jones:** whirl shall we and we've got them all individually marked far too easy and we'll put this in I mean we do have npn and pnp transistors so we have to be careful 2n 3904s and 2n 3906s here but let's get we've got a whole bunch

**Dave Jones:** and we've got individual resistors here all marked and then we've got 2 4 6 7 of these where are they 4k7s so there's a whole bunch of 4k7s in there so let's get those in and I do enjoy building

**Dave Jones:** kits it is quite therapeutic I don't get enough time to do it one of the things you've got to be careful of when you actually rip these things out of this these leader tape holders here I've mentioned this

**Dave Jones:** before you can't actually get gum on the end these ones aren't bad at all but just be aware of that even with through hole stuff if they've got gum on the ends and they're a tight fit in the

**Dave Jones:** holes when you actually push those in then you know that can be a real issue it can get in the hole I mean you know it's it's not a it's not a huge deal but just be aware of it you

**Dave Jones:** can end up with a crappy solder joint on the top side not that it hugely matters just a little note for young players there so let's whack in all the 4k7s I'm just bending these by hand of course I don't

**Dave Jones:** really give two hoots about the exact bend radius and you know I'm pretty good like you know generally if you get this like a 400 mil spacing I think it is generally just bend them like that you know you're going to be pretty close and

**Dave Jones:** they're just going to fall into place nicely. Of course, I have to orient the uh uh the bands around all the right way, otherwise the electrons will fall out. Can't have that. And uh 4K7 was another 4K7, there's another

**Dave Jones:** 4K7. And uh And the 555 timer, of course, is famously supposedly using four 5K resistors in there in the uh divider string. And uh this one's obviously not. And there's the uh uh 4K uh 4K7s instead being an E12 uh preferred value.

**Dave Jones:** Not a uh not a big deal, but that uh sort of uh doesn't lead to the authenticity that the original triple five timer does. If you're a stickler for uh your history on this thing, it normally contains the internal 5K

**Dave Jones:** resistors, but of course, 5K is not a preferred value. Of course, you can get 499K, or you could put two 10Ks in parallel um to give you a total resistance of 5K, but uh it's not quite the same thing, of

**Dave Jones:** course, the chip. It's It's only a nominal value, of course, inside the chip. There we go. Now, all our 4K7s are done. Far too easy. 820 ohms. Where's our 820 ohms? People are probably screaming at me. I can't see

**Dave Jones:** it. I got to look all over here. There it is. Every resistor's a winner. And this is just a lovely lovely kit. I highly recommend it. It's about uh 35 bucks, I think, which is uh quite good value.

**Dave Jones:** Cuz, you know, there's not much in it, but uh you know, all the nice uh legs and everything um makes it well worthwhile. Um unfortunately, there's no like uh test points on the thing. But uh test points, of course, you can just hook them onto

**Dave Jones:** the leaded resistors, but just not as nice as nice big uh test points on the thing. Uh where are we? 1K. We've got 1K somewhere. There we go. And uh this is just a lovely 10K. This is boring commentary. I mean,

**Dave Jones:** people asked for me to build kits and stuff, and they go, "Oh, why don't you do video of you building kits?" Well, you know, look, it's boring. What What am I supposed to say? Well, it's not boring for me. I find it therapeutic,

**Dave Jones:** but for people watching, I don't see what uh value people would uh get out of watching me assemble kits. But, hey, this is the 555th video. It's the 555 video. So, you're going to have to endure me building the 555 timer kit.

**Dave Jones:** Of course, you do all your flat components first, like your resistors, so that you can actually flip them over. When you do solder them, they're all down at the one level. There's nothing worse than having a board that sort of,

**Dave Jones:** you know, rocks around, and you're trying to solder it. So, you solder up sort of each level. So, on a typical board, you do all the resistors first, for example, through-hole boards, then you do, say, all of the ICs, cuz they're

**Dave Jones:** nice and flat and stuff like that. So, you kind of like do all those. And, of course, I put a little bend on the pins like that. That's fairly common, just to hold them in place. Some people like the

**Dave Jones:** uh flip, you know, stands, the soldering stands, where you can actually just rotate, you know, easily rotate these things, hold them in clamps like this. And uh well, yeah, I don't have one of those. I just like um

**Dave Jones:** the feel of doing it by hand. I don't like our clamps when I'm doing boards. Not a huge fan of them. I can I can appreciate it for people who do it all day, every day. So, they're common in

**Dave Jones:** the production environment, for example. The good thing about these resistors, you probably don't have to bend the legs because they're a nice sort of snug fit in those holes. So, really, you know, I I don't have to bend those, but

**Dave Jones:** sometimes if you got a board with loose uh holes in there Oh, like that one there. See, that one Hey, there we go. No, I spoke too soon. It did fall out. There we go. But it doesn't matter. As I said,

**Dave Jones:** once you flipped it over, they're all going to sit down nice and flat like that. So, that's the advantage of that. Last one, 100 ohms. 100 ohms. There we go. They've given us the exact number of resistors. This is a beautiful kit. All

**Dave Jones:** labeled. Values labeled on the silk screen, so you don't have to reference the um uh schematic or anything like that. You can just build it up. Now, for the transistors. Now, our transistors are labeled 3904, um NPN 3906, PNP. Just your uh bog

**Dave Jones:** standard um signal transistor. Now, these ones you don't want to uh pull out or anything like that. They're really annoying. So, these ones you'd go along with your side cutters and just chop them off. So, there we go. We'll do

**Dave Jones:** our 3904s first. And if we try and stick it in like that, it comes down and Oh, no. No, there we go. It fits in. That's not bad at all. That gives it a nice snug fit. And you'll find that the pins on the

**Dave Jones:** other side push together a little bit. These are a nice fit. Especially for hand soldering, um because you just push them in and they sort of hold in place. So, very, very nice. Here we go. 3904s. Do do do. And they've got the emitter

**Dave Jones:** base collector marked on there, but of course, but um Oh, oh, I've got them backwards. Oh, I'm an idiot. Look at that. I've got two in backwards. I'm a total idiot. Look at this. There we go. 3904, there we go. Based on

**Dave Jones:** I wasn't even watching. I was too busy uh uh checking to see if the damn thing worked, but I caught myself. You know, that's the main thing. Mistakes happen. happens, folks. Can't avoid it. Murphy will get you every time. I'll probably put one of

**Dave Jones:** these in backwards and people will be screaming at me as I'm soldering the thing that I've got it all wrong. And so I assume that the pinout is correct because if they've goofed up there the flat on the silk screen, then well, the

**Dave Jones:** kit is hopeless. But I'm sure they haven't. So Nothing worse than having getting your silk screen wrong and then putting it in backwards and well, and there is something wrong worse than that is getting your getting your footprint wrong, getting

**Dave Jones:** your pinouts wrong. Very common. And happens all the time. Especially with transistors, which can be a real pain in the ass. Always double-check your transistor footprints, folks. Golden rule. Hopefully I haven't put a 3904 into a 3906 position. I don't think so.

**Dave Jones:** I just love the look of this kit. It's brilliant. How can you not like it?

**Dave Jones:** The matte black solder mask really really does the business on this board. Don't always like it, but as I said, it's infinitely better than the glossy one. If I'm going to get black, always get matte black. Glossy one is awful.

**Dave Jones:** And man, it just irked me every time at Altium. when I was working at out him bloody gloss black solder mask everywhere unbelievable. All right, yeah, the matte black bloody uh sorry uh gloss black solder mask got so sick of it.

**Dave Jones:** And uh and you couldn't see the traces that was a pain in the ass, you know, you got these really fine traces all over your board and you're building and testing prototypes and sometimes you'd have to hack them and uh

**Dave Jones:** uh it was just it was awful but hey it was the company standard. And it had to be the right type of gloss black, too. Uh man those were the days. That was a long time ago now. That was uh

**Dave Jones:** 2 and 1/2 years ago at least. And uh time flies when you're doing a video blog. Let me tell you. I'm got I've got to get one of these wrong. I've got to goof it up on camera. Murphy's going to get me cuz I'm not

**Dave Jones:** concentrating, you know, I'm just I'm just cruising here. I could almost do this blindfolded. Stevie Wonder style. So I hope you're enjoying this folks those who asked me to assemble kits. I'm assembling a kit.

**Dave Jones:** With pointless commentary over the top. I don't know don't know why anyway I've um what I've been doing at the moment I've actually been slowing down the videos um trying to get to the triple five video cuz I didn't want to

**Dave Jones:** like cuz I had all these other videos like the um Maker Faire for example. I've got like another couple of videos for the Maker another three or maybe even four videos for the Maker Faire of interviews and stuff and I didn't want to release them

**Dave Jones:** cuz uh that would have um screwed things up or at least if I adhere to my numbering system, I'll probably give it the same number but then call it, you know, video A B C or whatever part one, part two, part three.

**Dave Jones:** I'll give it the same EEVblog number. Um possibly. Yeah, it's always a toss-up whether or not to you know, off-topic kind of videos whether or not to actually give them an EEVblog number but I mostly do these days. Ta-da! We're all done. That is

**Dave Jones:** fully assembled, folks. Now, that that's still bugging me. That bloody PCB manufacturer putting their process mark on there. If you go to companies like uh PCB cart, uh for example, they now they never used to give you the option.

**Dave Jones:** They used to put this on and I used to complain by default and I used to complain all the time to them about the boards I got and they finally listened and now they've got an option on their

**Dave Jones:** shopping cart where you can say don't put any of that crap on my board. Thank you very much. And which is excellent but other manufacturers um uh other PCB supplies don't seem to do that. So, it's a bit of pot luck and when you're using

**Dave Jones:** a board as a front panel like this and it's important, you know, I've had front panels come back and then there's all this gar manufacturer garbage just spewed all over the front of your front panel. It's disgusting. So, oh I actually I probably should

**Dave Jones:** Yeah. Oops, that's silly. I should have soldered my resistors. Um that was dumb. Yeah, I goofed it, folks. I should have soldered those resistors because I was mentioning before how you flip it over and it holds them all down. Well, they're not. Oh,

**Dave Jones:** that was dumb. See what happens when you're too busy talking and you're not you know, do as I say, not as I do. So, yeah, that's pretty embarrassing but we're ready to solder. All right, here we go. Let's solder this sucker. I'm

**Dave Jones:** using 60/40 uh tin lead solder. There it is. Standard 60/40 stuff. Ancient multicore uh stuff. Not 0.46 mm really fine. As I've mentioned in previous videos, I do recommend your basic solder should be 0.5 mm or less than that. So, that's excellent.

**Dave Jones:** So, let's get in here. I don't use that lead-free stuff. It's just It's just not worth the hassle, really. And one of the issues here is going to be As I said, I should have uh uh done all the resistors

**Dave Jones:** first and cut their legs off and then done the transistors, but uh oops. Too busy yapping away. Not paying attention. And um But, that's not a problem. So, I'll just do all the resistor legs and cut them off. Now, one of the issues here, I'm

**Dave Jones:** trying to It's not easy. Usually, I'd be flipping this board around all the uh place while I'm actually uh soldering, but because I'm trying to keep it in a central location on the camera here, um it does make it a bit

**Dave Jones:** more difficult. So, this isn't my usual soldering style, I'm afraid. It's uh I get that in my soldering videos, the comments and things like that. People are going, "Why did you do this? Why did you do that?" And it's the you know,

**Dave Jones:** it's not my usual not quite my usual style. So, please forgive me. I just don't want to you know, move the board around everywhere. I want to give some uh nice visual quality to the video. That's the idea, anyway. If my hand

**Dave Jones:** isn't in the way, I don't know. I'm not looking at the uh screen at the moment. So, one of the issues I've got to blow the solder fumes away, because if I use my solder um my pace uh fume extractor,

**Dave Jones:** then um oops. Then, I'm uh uh going to It's going to be too noisy cuz that thing is like a freaking jet engine. It's It's just absolutely awful. I'm going to have to actually get some low-noise uh fans, you know, the silent

**Dave Jones:** uh fans, you know, some 12-V ones or something like that, some big ones, and just, you know, stick some batteries on the bottom, maybe with a you know, a couple of double A's and maybe boost the voltage up or something

**Dave Jones:** to power the fan, and um then uh I could just have it next to the work and just blow the fumes away cuz often that's all that's required. I'm choking on them. Um just to blow the fumes away, really, rather than uh

**Dave Jones:** Although, I could have one on the other side, so I could have I was possibly thinking maybe I'd have one that There we go. I think I got them all. One that um sits on this side here and blows

**Dave Jones:** across like that, and, you know, have another one which sits on the other side, which actually sucks through, and um just have some uh carbon filter on that one. So, sort of like I can position them uh anywhere. That would be uh you know,

**Dave Jones:** kind of good. I could have a, you know, a fan sitting here like this, fan sitting here, and it's going to blow across and suck. And if they're relatively um you know, those uh silent type ones, and I run them at a sort of a

**Dave Jones:** low-noise speed cuz you don't need a huge air flow to uh bring that across. Then, you know, that's not a problem. The fume extractors aren't that great because, you know, they've got to run really fast and loud in order to suck the fumes uh

**Dave Jones:** through cuz they don't have a hood on top. The best uh fume extractors I've used are, of course, the ones on a big snakey arm that, you know, come down and you can move them over your work, and

**Dave Jones:** the fumes just go straight up and get sucked in. But, when you've got a solder sucker that's on the side here trying to suck the fumes in. Uh it just, you know, it doesn't work really well. So, anyway,

**Dave Jones:** time to uh trim these leads off and uh let's have a look. Yes, this is going to be a long rambling video. As I said in a previously, what you do with your uh side cutters is getting there, but don't cut it flat

**Dave Jones:** like that. Actually, give it a bit of a tilt like that and tilting it up just gives it enough uh angle that you're not cutting into the solder joint, because you don't want to cut the solder joint. You want to cut

**Dave Jones:** the lead, not the joint. Uh sorry, I've got to move this one around. There's no there's no choice on this. Um it makes it really difficult. So, uh yeah, this is terribly exciting video, folks. I hope you're enjoying it.

**Dave Jones:** But anyway, some people wanted to see it and uh me assembling a kit. And well, this is what it's like. It's not exciting at all. And I just get to waffle on and on and on. In fact, I've had to um

**Dave Jones:** I've been sitting idle on this for a couple of days now. Oh, no, I missed one. There we go, I did miss one. Silly me. That always happens. Murphy'll ensure that you uh always miss a part. Don't always hold onto the

**Dave Jones:** leads, by the way, cuz uh these things can fly right up into your eye. Not good. So, there we go. Let me finish that off. And uh There we go.

**Dave Jones:** All right. Now, I can go around. And of course, because I did bend the leads on that, but um just check that, you know, none of them are sticking out really ugly or anything like that, you know, the uh

**Dave Jones:** visual aspect's kind of important, and I think I Yeah, I did double-check those uh transistors, and I had them in all the right way, so I can start again. Anyway, I was saying that I had to This soldering is actually uh three or

**Dave Jones:** four days after the previous scene, which was me actually assembling them in there, because I didn't uh have the time. I've had lots of uh family stuff on recently, and uh I haven't done anything for uh you know, 4 days or something like

**Dave Jones:** that, so I've only just gotten back into it. And at the moment, I'm busy um and I'm also busy working on my um new microcurrent, trying to get that sucker up and running, uh which is a lot of work. By the way, it's

**Dave Jones:** um as I've discussed many times on the blog and the Amp Hour and other places, it's uh you know, actually designing the circuit is uh is not the and laying out the board, for example, is not not a huge

**Dave Jones:** part of it. It's uh the bill of materials, finding components, in this case, really precise components and um certain types of switches. I'm going to move this around. Certain types of uh switch that I need, and uh getting stock

**Dave Jones:** of this sucker has not been easy, so I've had to uh actually commit myself to uh you know, several thousand volume of uh some parts, um just to get them so that I'm not caught short, cuz the last thing I want to do

**Dave Jones:** is run a crowdfunded campaign, for example, and find that I've, you know, got uh I'm oversubscribed, and then I can't deliver for 3 months because there's a, you know, um, a huge lead time. Some of these parts are like, you know, 12 weeks

**Dave Jones:** factory lead time. So, you know, so if I didn't buy stock now, I would have been, uh, I would have been screwed. So, you sort of I sort of had to buy up in some cases, I think, all of the world's

**Dave Jones:** stock these switches and, uh, and these resistors in order to, uh, in order to secure the, uh, success of my new micro current. Well, and, you know, I just be might like that, you know, no one wants to buy the thing and I'll be

**Dave Jones:** stuck with, you know, a reel of a thousand parts at $4 each, you know? And, um, yes, one reel of parts, you know, cost well over $4,000. This is crazy. And, uh, which sounds like a lot, but in the

**Dave Jones:** scheme of, uh, you know, um, if you actually make a thousand units, you know, it's, uh, and sell a thousand units, it's not much at all. It's all part of the manufacturing cost, but when you're got it up front,

**Dave Jones:** that cost up front and you, uh, don't have any sales to, at the moment, to pay for that, then, uh, you know, can be a real pain in the ass. So, sorry, I haven't been checking the camera. Has that been on

**Dave Jones:** camera? This is incredibly boring. I should just, uh, shoot video of me instead of the board, maybe. Yapping away. Got to try and keep good posture, too. Do pride myself on my posture. I do try and keep excellent posture, but, uh,

**Dave Jones:** you can find yourself lapsing here and there, which isn't good. Anyway, so that's what I've been working on for a while, and that's why I haven't really been coming out with the videos, and it's annoying me. And of course this one has to be the

**Dave Jones:** 555th video. So, it's not like I can release cuz I got other videos I can release, but I can't release them under the numbering scheme. Um otherwise, I'd get to 555, and well, it wouldn't be the triple 5 timer video

**Dave Jones:** building this thing, so that's no good. Don't want that. So, I've had to slow down a bit, and that's given me time to work on my micro current. I've been thinking about it for ages. I changed direction a couple of

**Dave Jones:** times, but I went back to what worked in the end, and it's just a more precise version. There we go. There it is. Oh, that's the entire board. Completed. Holy crap. There we go. I should actually trim off those uh

**Dave Jones:** leads, of course. Those transistor leads are rather annoying. Once you've got to trim those off, but anyway, once again, same thing like that, and then give it a tilt like that, so you're cutting into the leads and not

**Dave Jones:** the solder joint. That's a a uh real beginner trap that one, cutting into the solder joints. Although sometimes you have to, you know, you've got to grind them down sometimes. I've, you know, um ground boards down completely flat

**Dave Jones:** because you had to get it in some, you know, tight enclosure or something like that, or some physical reason why you've had to make all the leads flatten, and it had to be through hole instead of surface mount, for example,

**Dave Jones:** and yeah, I've done that uh done that more than once. That's for sure. And uh you know, it it works. There's nothing wrong with cutting into your solder joint. I mean, ultimately it works, but you can, you know, get the stress

**Dave Jones:** fractures in there and stuff like that. So, you know, it's just not best practice to cut into the solder joint, but in practice, even though it's not best practice, it does, you know, it it does actually work. Um

**Dave Jones:** But it just can't be counted on, that's all. And uh when you get a long-term a um you know, fracture like a a fracture in your solder joint that only shows up, you know, like it's an intermittent long-term problem or something like

**Dave Jones:** that, then that can really ruin your day, you know, it goes into a product, goes out in the field, and it only uh starts failing when it, you know, the joint heats up to a certain temperature in a certain environment or something

**Dave Jones:** like that, and you know, you trace it back to uh a solder joint. Now, that's just crazy. But it happens, and yeah, I've been caught with that before. But look at that. Ta-da! 555 timer board fully assembled. That was really easy. I don't

**Dave Jones:** know, I wasn't timing that, but it doesn't take long at all. Um it would have been uh quicker if I didn't uh have the camera going and wasn't taking my time and just went all over the place. Sorry, that's just

**Dave Jones:** blurry. That's just going too quick cuz I can uh solder really quickly if I am so desired. So, here you go. Going to screw in the yeah, terminals on that and make it look like a real 555 timer. I just noticed here

**Dave Jones:** the tips on that how to solder. Got really nice little uh diagrams here. I rather uh like that. But they say um but step um two, of course, you know, uh or step two, place the solder against the

**Dave Jones:** joint that you wish to connect. So, and put the solder on fir- uh touch the solder to the joint first and then touch the iron to the solder joint for about 1 second. That's no, that's back-to-front. You need to put the iron onto the joint

**Dave Jones:** first and then the solder. Although you may have noticed, you know, do as I say, do as I say not as I do. You may have noticed that I sort of, you know, might have put them on at the same time when I

**Dave Jones:** was doing that, but yeah, you're supposed to heat up the joint first then apply the solder. That's how it works. That is the industry way to do it. And these funky looking IC legs just screw in there with

**Dave Jones:** these little cap head screws. Rather annoying that it's not Phillips, you've got to go find your uh um hex driver for that, but still that looks really neat. You know, the black matches the black solder mask and I love

**Dave Jones:** cap head screws. They're just really neat. So that's just beautiful. And there's all the pin tails. Keep those, folks. They can come in real handy. Trust me, always have a component drawer full of offcut pin tails. They're just

**Dave Jones:** great. Ta-da! There's the finished article. Isn't that cute? I love it. That's just great concept, brilliant, and the thumb screw terminals on here even got red and black for the power and the five or six other pins. Sorry for all

**Dave Jones:** the control signals. The only issue with this that immediately comes to mind as well. Okay, I've got to hook this damn thing up now and I like the thumb screw terminals, but if I have to get, you know, a resistor from over here to over

**Dave Jones:** here, it's not going to reach. I'm going to like it's not just like a breadboard where everything's nice and tight and all the components, external components, are designed to, you know, fit around the regular sized IC on your breadboard

**Dave Jones:** and it doesn't do that. So you've got to use like clip leads and wire and things. Goodness, but jeez, it's fun and you get to play around with the individual segments and probe stuff inside your 555. Brilliant. And once again, very detailed

**Dave Jones:** instructions on this thing. So, you know, if you're really after a beginner's kit, this one, you know, is really quite good in terms of, you know, soldering through-hole stuff and just, you know, getting a nice little practical circuit to play around with.

**Dave Jones:** And they've given you a suggested test circuit. What I even like more is that they point to Colin Mitchell's Talking Electronics site for more stuff. Definitely check out Colin Mitchell's Talking Electronics site. And I've done some interviews with

**Dave Jones:** Colin Mitchell, one of my heroes who taught me electronics way back in the old days. So, there you go. And let's wire up this 555 LED blinker. Well, see if it blinks. I've probably goofed something up. Probably won't work.

**Dave Jones:** Bloody Murphy. Well, of course, astute viewers will know that my first mistake is to think that pin four was ground. It's not on a 555 timer. Pin four is reset. The 555 timer goes against the regular, you know, opposing side

**Dave Jones:** pinout on there. Oh, I just, man, I was not thinking this was a 555 for some reason. I don't know. Geez, I've known the 555 timer pinout for, you know, 30 years or more, but, you know, still screwed it up because I'm

**Dave Jones:** too busy yapping away. I'm just not paying attention. And of course, I don't follow instructions. There we go. Now, we're ready to go. So, here we have it all wired up. And yes, it's a bit messy to actually use it in this

**Dave Jones:** configuration. Yes, you can get resistors directly from point to point like that. So, the classic astable configuration like this, you do need, you know, a couple of wires coming around here. I didn't want them going over the top like that because we're

**Dave Jones:** going to be probing stuff on here. I've got a 3.3 V 3.3 mic cap 450 V. I think it'll do it. Anyway, that's what I got out of my junk bin. I got a jumbo LED as well. Considering that this is a

**Dave Jones:** jumbo 555 and here it is, classic astable configuration for the 555 timer. It does warn you though, it's not a direct replacement if VCC is greater than 6.5 do not connect reset directly through cuz normally the reset pin four

**Dave Jones:** would be connected directly to pin eight up here, but it says you got to put a 100k in series. So, that's a limitation. So, it's not a direct functional equivalent. Although they recommend they say that it should be in most

**Dave Jones:** uses and configurations, but that is one small trap there. So, we've got a 100k pulled up there and we should blink our LED at I don't know a hertz or two, something like that. Haven't done the calculation, but flip the switch and

**Dave Jones:** I've got it powered from 9 V. Let's have a look. It's on. Hey, it's blinking. It's blink. We have a blinker. There we go. Works a treat. We obviously don't need anything on the control voltage really cuz it you

**Dave Jones:** know, it doesn't matter a rat's ass. That's just basically some internal bypassing and stuff. So, really we're looking pretty. Look at that. It works. Bobby dazzler. Oh, and by the way, this isn't a plastic. It's a hard cell PVC foam. So,

**Dave Jones:** you can actually get in there and dent that if you really want to, but that's really neat stuff. You can make some cool stuff out of that. It's lightweight and rigid, but easy to cut and mold. The model making industry use it

**Dave Jones:** extensively, you know, the props industry and model making type stuff use this hard cell PVC foam pretty extensively. Now, here is where we're going to get a bit messy, but stick with me and apologies at the start. I haven't

**Dave Jones:** thought this through. So, I'm a kind of winging this, but we're going to have a look at the 555 circuit diagram here. Now, this is one of the more disappointing things with Well, the most disappointing thing with the kit is that

**Dave Jones:** it's designed to, you know, allow you to play with and a transistor-based replica of a 555 timer. And it neatly divides them into the threshold comparator, the trigger comparator, the flip-flop, and the output, and the reset, and all that

**Dave Jones:** sort of stuff. But, what it doesn't do is give you a circuit description of how any of this works. And I think that's greatly lacking for people who want to It almost defeats the purpose of the kit, really, cuz who

**Dave Jones:** wants to play around with the outside? You want to get in there with your scope and look at waveforms and do things like that. So, it really, you know, would pay for them to have some sort of, you know,

**Dave Jones:** a deep description or, you know, at least some sort of description of how the arrangement works in here. Anyway, I'm going to have a crack at it and do a few notes, if I may. Now, the first thing I notice is that

**Dave Jones:** this these three resistors here aren't part of this trigger comparator. So, I'm going to draw a dashed line down there like that because these a And they should be, by the way, 5 K because well, 555 555. Now, of course, Hands on Cams

**Dave Jones:** in, I think, has actually said that no, that has nothing That's not why it was named that because it actually had, you know, the five nominal 5 K resistors in there. The number was just a, you know, next in their sequence or

**Dave Jones:** something like that. I don't know. It's got nothing to do with it. But, by coincidence, it does have 555 in there. And that's just a resistor divider in there to generate the threshold voltages. And of course, the control

**Dave Jones:** voltage pin is directly connected to one of those taps here. Now, what I've got is basically the same diagram that's on my 555 timer shirt. This is the typical internal block diagram of the 555 timer, and we'll see how these modules relate

**Dave Jones:** to these items in here, like the threshold comparator. There's the comparator, of course, uh connected to the threshold pin. We've got our trigger comparator, sometimes called the upper and the lower comparators. This is the that goes to the trigger pin in there.

**Dave Jones:** Um and there's the 555 5K resistors in there. They set the threshold values for those trigger comparators. Then, we've got ourselves a flip-flop here, which we'll take a little look at. And then, we've got our output driver here, and

**Dave Jones:** then our discharge um pin over here, and the reset is tied into the flip-flop. So, we're going to come back to this um periodically, but let's uh start out with, say, the threshold comparator over here and see what we've got. Now, in the

**Dave Jones:** threshold comparator, it looks a bit complicated. They've got all these transistors connected in weird and wonderful ways like this, but it breaks down fairly simply. And let me briefly explain. What we've got here basically are two inputs to our comparator. One

**Dave Jones:** here, which is the threshold pin, the other comes from the voltage tap on our 555 um resistor ladder there. So, these are the two inputs to our comparator, just like you'd get a regular uh comparator, you know, LM311.

**Dave Jones:** You've got your positive and your negative input there. And this is a um typical arrangement. What it is is basically a differential pair amplifier. And uh but it's working as a comparator cuz there's no external feedback to make it

**Dave Jones:** work as an amplifier. And usually, these are pretty crude amplifiers, but they do work uh reasonably well as comparators, but not on their own. You've got to have some current sources, which we've got up here, that just make them a bit less

**Dave Jones:** sucky as comparators. So, uh what we've got here actually is these two transistors here and here, there's nothing unusual about these arrangements at all. That's just a Darlington pair. So, you know, if you're familiar you should be familiar with the Darlington

**Dave Jones:** transistor pair, there it is. So, they've just got extra uh gain in there so that the um input current on the pins is very small for a particular gain. So, they're just increasing the gain with a pair of Darlingtons. No issue at all. No

**Dave Jones:** magic going on there whatsoever. Once again, there's nothing tricky going on up the top here um at all really. It's a standard building block component called a current mirror and that's what this uh these arrangements of these two

**Dave Jones:** transistors um does here. Now, what we've actually got here, okay, is this You see how the the uh base is connected to the collector here on this one and this one. Well, basically what that is acting as is a diode. So, essentially

**Dave Jones:** what this thing is here is just a diode connected like that. And this arrangement I won't go into how current mirrors work, but basically that's a you know, I could do it like a Fundamentals Friday video on that, but

**Dave Jones:** basically the current flowing in there and down there like that is going to be equal. So, that's all there is to it. And likewise on this side over here, they've got exactly the same thing. This arrangement is going to be a

**Dave Jones:** diode like that and by current mirror action we'll call it the current flowing down here is equal to the current flowing down here. And that's all you got. So, they've got two constant current generators. Sometimes they'll have the

**Dave Jones:** constant current source down in the bottom resistor down here. They'll replace that with the constant current, but what they've got it is the constant current up the top, and I won't go into the pros and cons of various

**Dave Jones:** arrangements, but that's what they've decided to do in this arrangement. So, constant current feeding this so it acts as a, you know, a decent comparator, and then the output in this case is tapped off here, and this is one of our

**Dave Jones:** outputs. In fact, that is the reset output coming out of our comparator into here. So, we can go over here and label that input uh on our flip-flop there. So, that's all there is to it. So, that is not too

**Dave Jones:** dissimilar to just a regular comparator chip that you would buy off the shelf. Now, over here in the trigger comparator, it's essentially uh the same function. It's just a comparator because, look, it's it's really no different except we've

**Dave Jones:** got our external input going to the negative input, but they've decided to configure this transistor arrangement differently using PNP transistors down here instead of NPN. And actually, this is a more typical uh comparator arrangement you'll find in uh commercial comparator chips which you

**Dave Jones:** can just uh buy off the shelf, but it essentially works just the same. We've got a constant current going down here by virtue of this transistor over here. Once again, we've got our current current mirror arrangement. This is

**Dave Jones:** actually, once again, we've got ourselves a diode in there. So, the current um flowing down here is going to be a constant current setting the bias for this comparator down here. Very simple. And once again, we've got another Darlington

**Dave Jones:** arrangement there as well, but with uh PNPs instead of NPN. And then we've got our output being tapped off here, and so that becomes our set input to our And there's the output of the comparator. That's the set input going

**Dave Jones:** into our flip-flop block over here. So there you go. We've got our two comparators there with the R and S inputs to the flip-flops. Too easy. This one here is not actually one of part of this functional block arrangement. They're

**Dave Jones:** just got like a jewel current sourcing arrangement here. That's actually I think that's probably clever. Hans has probably done a trick or two in there to save the odd transistor, I think. That could be neat. That could You could go into more

**Dave Jones:** detailed analysis of why that is done. But as you can see, it's pretty much following this arrangement we've got here. So as I said, this one helps provide constant current to both of these points down here. So we've got

**Dave Jones:** Basically, let's have a look at our flip-flop arrangement now. Now, technically, it's probably not correct cuz it's not really a clocked flip-flop as such. The more correct term would be an RS latch. And that it should have four two

**Dave Jones:** inputs two output Sorry, three inputs and two outputs. Reset pin. We've already got our R and S here. And of course our reset arrangement comes from over here into there. So there it is. So that's our Well, RS. So we'll call that RST. Reset

**Dave Jones:** there going into our flip-flop. And these here are our So that's our Q output, and that's our not Q output from our flip-flop block. So how does this RS flip-flop block work? Well, it's rather interesting. Now, a normal RS, you know,

**Dave Jones:** textbook RS latch like this made up of two NOR gates like this cross-coupled NOR gate and of course you might have a a third input here for your reset you know, external reset pin, but that is not what we find here because we have

**Dave Jones:** a look at a typical old school data sheet for a NOR gate. I mean, look at how many transistors we've got. We've basically got an inverter and some NAND gates and inverts the output and that's you know, basically how it does it. Now,

**Dave Jones:** you in fact often you'll see this configuration in a 555 timer you know, block diagram instead of just showing it like this. They might actually show these cross-coupled RS flip-flops, but look at how many transistors we've got to implement and

**Dave Jones:** that's just for one NOR gate. So, we'd have to have two of those in all of this up here and we don't have that. We've just got some constant constant current source up here. That's pretty much it. So, these transistors down here we don't

**Dave Jones:** have enough to implement this classic arrangement. Well, we don't have to cuz what they've done is what Hans has done is implemented the classic two transistor arrangement like this. RS it does exactly the same job and you'll notice it may not look like the same as

**Dave Jones:** this, but it actually is. Follow with me here. Let's assume that this is the Well, we know this is the set input here, okay? So, this is the base of the set transistor here. This is our set transistor and that then feeds back via

**Dave Jones:** a resistor here back to the base of the reset transistor. There's our reset input. So, this is our set transistor down here. This is our reset transistor and you'll notice it is cross-coupled back. Here it is, cross-coupled back

**Dave Jones:** there to there, but there's no resistor in there. Where is that resistor? Well, we don't need it because we've got that constant current source coming from over here. So, we don't need that series resistor. So, we're not going to blow

**Dave Jones:** our transistor. It already is limited by the internal constant current arrangement of this chip. And it's very common for the chips like this to have constant current generators everywhere. Like a typical comparator might have three or four constant current

**Dave Jones:** generators in it all over the place. And things like that. So, that's the way they've got away with directly connecting the transistor in there like that. And by the way, this um array this particular uh circuit is taken directly from the original

**Dave Jones:** Signetics triple five time data sheet, which is fantastic, which I'll link in down below. They've got some excellent drawings in there as in hand-sketched uh little cartoony drawings. Fantastic. But anyway, that was a little aside. We've got this

**Dave Jones:** classic arrangement using these two transistors here. Very minimalist uh design. Fantastic. They don't even need that resistor in there. And it's um and you'll once again notice this arrangement here is our diode. So, we've got a effectively a diode like that, and

**Dave Jones:** that's what allows us to feed this external reset into basically the uh same arrangement as the into the uh reset flip-flop, which then is buffered from the output of here. So, we've taken We're basically taken the output from our reset There it is. We're

**Dave Jones:** taking our output from here, like this, from our reset uh uh transistor. Sorry, not reset flip-flop, reset transistor. And that is then driving that through this constant current generator here, and that is driving our complementary outputs of Q

**Dave Jones:** and not Q. That's all there is to it. It's a very clever implementation of a basic RS latch. I really like it. And then from our Q and not Q, we can see how these drive the output buffer

**Dave Jones:** and the discharge transistor down here. Here's the output buffer block and you can see that it is driven by the Q output there. And basically that's a totem pole arrangement. Once again, we have ourselves a diode in there like that. And so that is just a

**Dave Jones:** buffer to drive this totem standard totem pole output like that. Too easy. So these are all just you know standard building blocks. So when you know your circuit building blocks like your totem pole output, like your diode from the

**Dave Jones:** transistor, you got your Darlington pairs, you've got your current mirrors, and you know, it all sort of starts to make sense and come together this convoluted circuit diagram. Once again, here is the uh um not Q output coming via a resistor

**Dave Jones:** there. There it is. Straight into the open collector output discharge transistor. Too easy. So there you go. I hope you found that brief walk through somewhat interesting. And of course you could play with this to your heart's content.

**Dave Jones:** And that's the beauty of this kit. You can get in there. You can see what the current mirror mirrors are doing. You can see how the RS latch is working. See how the totem pole output works, the comparators, everything like that at the

**Dave Jones:** transistor level. It's brilliant. And it's a shame that this kit doesn't come with a really detailed circuit explanation of how this works cuz it's a great learning tool I think for discrete transistor design. And yes, I've probably goofed something up in there. I

**Dave Jones:** haven't really thought about this in detail. There's probably a few nice little tricks in there that Hans put in to sort of optimize this and lower the transistor count and get the performance required and you know stuff like that.

**Dave Jones:** So not really going to go into deep analysis of this thing. By the way, the LTSpice circuit simulator the free one from Linear Tech comes with a transistor level 555 timer circuit. It's or it's not too dissimilar to this. It is you

**Dave Jones:** know functionally identical to this. It's a drawn a bit different of course uses the transistors in a different sort of arrangement but it allows you to play around with a 555 timer in a circuit simulator and that's one of the examples

**Dave Jones:** that come with it. So I highly recommend you download that have a play with it although I haven't played around with it myself so I don't know how it performs and simulates but I do know it's there. All right, let's take a look at some

**Dave Jones:** external scope waveforms or external to the chip and we're basically following our standard got our a stable circuit built as shown here. Now the yellow waveform is pin six which is the threshold comparator pin. The green waveform there is pin seven

**Dave Jones:** which is the discharge open collector discharge output and the blue waveform of course is our output voltage and you'll notice that well there's our output voltage and you see the blue waveform like that and that's that's what when it goes high of course it's

**Dave Jones:** switching on our LED because we've got it driving the LED via the anode there. Now if we have a look at our yellow waveform here the charging that's the main capacitor that's the one 3.3 micro farad capacitor charging up via

**Dave Jones:** the 200k resistors there. So 200k in series via 1 micro farad and that's the charging waveform, so you can use your formulas to calculate how long that's going to take to charge up, and then it is when it

**Dave Jones:** reaches the threshold voltage, if we have a look at our internal block diagram of a 555, the comparator, because of the 555 K resistors in there, it's 2/3 the threshold comparator is 2/3 of the supply voltage. In this case, the supply

**Dave Jones:** voltage is 9 V, so our threshold voltage is going to be 6 V. And is it? Here's ground. We're at 2 V per division, 2 4 6. It switches at exactly that 6 V threshold limit. And then, once that

**Dave Jones:** happens, our discharge pin kicks in, so our not Q output turns on the discharge transistor, which then discharges the current. Please excuse the crudity of all this. Then it discharges the charged 1 microfarad capacitor, which is currently at 6 V, and discharges it through the

**Dave Jones:** 100 K resistor down to ground like that. And that's exactly what we're seeing there. It's discharging back down. It's taking half the time that it took to charge up, because it's only going through a 100 K resistor instead of the

**Dave Jones:** 200 K. And of course, then our trigger comparator down in here is measuring that value at 1 because of the 55 K resistor divider in there. It's 1/3 of the supply voltage or 3 V. And bingo, look, it

**Dave Jones:** discharges from 6 V down to 3 V, and then the cycle starts again. And of course, I'm preaching to the converted. Most of you know about a standard 555 timer operation. So there it is. It's all confirmed and verified. Works a

**Dave Jones:** treat. Now, what we can do with our fourth channel, the pink channel here, which I'm uh touching it my finger, we can probe around the circuit here and uh have a look at some of the waveforms, shall we? Let's uh take a look at our um

**Dave Jones:** reset input of our RS of our flip-flop latch here. So, that's the collector of Q6, and luckily they have labeled emitter base collector on the overlay, and there it is. You can see that our output there because it's it's

**Dave Jones:** actually quite small. That's uh 500 mV per division. So, it's about 600 mV, one diode drop. So, that But, that is basically switching that uh constant current source off and on there, which goes then into um our flip-flop over here. And let's have a

**Dave Jones:** look at our set one. That should be much lower. We should be looking at diode drop switching there. So, look at base of Q15, which is There it is. Base of Q15, and there we go. We're not actually

**Dave Jones:** getting a pulse. Uh well, what are we getting? Just a pulse on that. Check that out. Up. No, there we go. My trigger point's a bit off, but yeah. You can see we're just getting that little um set

**Dave Jones:** pulse down in there. Just once again, that's only a single diode drop. There it is, 500 mV per division. Single diode drop just to switch that transistor back on and change states. Then we can have a look at things like this uh constant

**Dave Jones:** current output here, which will be uh switching, of course. That's our drive, the buffer drive going into our uh Q and not bar output. So, let's have a look at the uh collector of Q19A. There we go. Collector of Q19A, and

**Dave Jones:** there we go. It's switching. Now, if we have a look at our Q output here. Let's have a look at that. That is the collector of Q20. Yeah, where is it? Emitter, base, collector. No. Collector. There it is. And that is our

**Dave Jones:** Q output going into our final output buffer stage, nice and squared up. Huge voltage there, almost full swing. And our not Q output here is once again only small. We're only talking, you know, a diode drop sort of level there. There we go. And we

**Dave Jones:** can have a look at the things like, you know, the constant current output here for example of our Q9. So, let's take a look at the collector of Q9 there, and you'll see that that that was just a some contact bounce

**Dave Jones:** there, and you'll see that that is basically just a steady state voltage, that steady state current. And of course, we're only looking at the voltage here, but basically that's going to be a constant current source coming out of there to bias all of our trigger

**Dave Jones:** comparator circuitry down here. So, you can just probe around the circuit here to your heart's content and figure out exactly what's going on, and maybe compare it with the So, it's a really handy kit to figure out how this sort of stuff works. Of

**Dave Jones:** course, there's going to be, you know, process technology differences between a discrete transistor design like this and the actual manufactured 555 timer IC of course, but you know, functionality-wise, it's going to operate fairly similar. Now, if we actually probe the outputs of

**Dave Jones:** our set and reset transistors here inside our latch, so we'll probe the collectors there, you'll see that they'll be opposite polarities, both single diode junction. So, let's have a look at the set Q15, the collector of that and you'll notice

**Dave Jones:** how that is There you go. It's positive. Whoop. Positive going while the output is low and we should get the opposite on Q 16 down here, the collector of that one and we do. There we go. It is low when the

**Dave Jones:** output is low. So, there you go. I hope you found that interesting. If you're still with me after what's it been an hour or so, uh well well done sticking in there. But, uh yeah, I was going to do a few more

**Dave Jones:** things for this uh 555 timer video, but uh you know, things happen and uh they just don't get done. Maybe for 556, I don't know. But, anyway, um if you enjoyed it, please give it a big thumbs up and if you want to discuss it, jump

**Dave Jones:** on over to the EVblog forum. Catch you next time. Good on you, Hans. What a beauty.
