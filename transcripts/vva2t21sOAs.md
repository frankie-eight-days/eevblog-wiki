---
video_id: vva2t21sOAs
title: EEVblog #167 - Atten 858D Hot Air Rework Review
url: https://www.youtube.com/watch?v=vva2t21sOAs
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 34, "3": 51, "4": 65, "5": 81, "6": 95, "7": 106, "8": 119, "9": 138, "10": 150, "11": 164, "12": 180, "13": 194, "14": 203, "15": 216, "16": 229, "17": 241, "18": 253, "19": 272, "20": 285, "21": 305, "22": 317, "23": 332, "24": 347, "25": 363, "26": 377, "27": 390, "28": 407, "29": 428, "30": 442, "31": 457, "32": 473, "33": 485, "34": 504, "35": 520, "36": 537, "37": 553, "38": 568, "39": 580, "40": 594, "41": 611, "42": 622, "43": 639, "44": 651, "45": 667, "46": 682, "47": 698, "48": 712, "49": 725, "50": 738, "51": 751, "52": 767, "53": 778, "54": 795, "55": 811, "56": 827, "57": 841, "58": 859, "59": 874, "60": 889, "61": 904, "62": 916, "63": 929, "64": 943, "65": 953, "66": 967, "67": 983, "68": 997, "69": 1011, "70": 1026, "71": 1042, "72": 1057, "73": 1069, "74": 1082, "75": 1096, "76": 1110, "77": 1127, "78": 1139, "79": 1155, "80": 1176, "81": 1187, "82": 1201, "83": 1216, "84": 1241, "85": 1254, "86": 1267, "87": 1281, "88": 1291, "89": 1303, "90": 1322, "91": 1334, "92": 1350, "93": 1364, "94": 1380, "95": 1395, "96": 1408}
---

**Dave Jones:** Hi, welcome to the AAVlog an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product review time again and I haven't done one of these before, but it's an

**Dave Jones:** essential bit of kit for practically every electronics lab these days. It's the hot air rework station and in particular, it's the Aoyue model 858D plus super duper cheap. Let's check it out. And here it is. It's a very basic

**Dave Jones:** unit, but it's pretty much all you need for a hot air rework station. And the great thing about this is that it's ridiculously cheap. I got this for 82 Australian dollars delivered to my door from China or Hong Kong or wherever it

**Dave Jones:** was straight off eBay. Now, I can't find this particular model the 858D on the Aoyue website. It seems to be a more modern version of what they're selling. They sell like a the Hakko rip off. They they look very much like the Hakko

**Dave Jones:** units, but this one is a new style. It's got a digital LED readout. It's got air flow adjustment and temperature setting. That's all you need. So, it's probably the cheapest hot air rework station on the market probably by far. If you go

**Dave Jones:** buy a quality brand like a Hakko one, cost you an arm and a leg, but one of these things will it do the job? Well, 82 bucks, let's find out. So, what exactly is a hot air rework station?

**Dave Jones:** Well, it's nothing fancy. It's basically a heater that blows hot air. That's it. It's just like a you know, a $10 hot air gun you can buy from the hardware store, but a little bit more advanced cuz it

**Dave Jones:** allows you to dial up the specific temperature and the air flow rate and stuff like that. And what it's good for these days is SMD stuff. So, if you're designing like little boards like this or you're reworking them, anything to do

**Dave Jones:** with SMD components, which is pretty much most designs these days, even hobbyists are using, sometimes almost exclusively, SMD parts. And really, if you don't have one of these, you're really not in the game. So, it's a very essential bit of kit for, um, not only

**Dave Jones:** SMD rework, it allows you to take components off the board really easy. That's one of the key features. Uh, instead of butchering it with a soldering iron, if you've got, like, a, uh, SO package IC, sure you can get

**Dave Jones:** around there with your side cutters and you can cut off the legs and do all all that sort of stuff, but it's pretty nasty. Get out one of these babies and boom, within a couple of seconds the chip is off. Not to mention the, uh, BGA

**Dave Jones:** chips, like that one, for example. If you want to get that off, you can't do it with a conventional soldering iron. Forget it. It's just not possible. So, pretty much, um, these things are essential for not for actually getting parts off the board,

**Dave Jones:** but they're also pretty darn handy for if you're assembling SMD boards. A lot of people assemble their own SMD boards. You can do it with a traditional soldering iron, of course, and very fine solder and you can solder each joint.

**Dave Jones:** But a lot of people will use solder paste, dab that on the joint. I have to do a another whole video on that one, I think, but there's videos out there if you want to check them out. You dab some

**Dave Jones:** solder paste on and then you place the component and then you just run along with the hot air, it melts the solder and it or it reflows the solder, it's called reflow soldering, and Bob's your uncle, your board's assembled, easy. And

**Dave Jones:** just being a general purpose hot air gun, it's great for, like, heat shrink, uh, on wires and stuff like that, too. Pretty versatile bit of gear. Now, I've never actually had one of these in the EE blog lab before because I've always

**Dave Jones:** relied on work having pretty advanced SMD gear. So, I've never really needed it here. If I want to rework a board, ah, I just take it to work and do it at lunchtime. No problems at all. But, uh,

**Dave Jones:** because I'm working from the lab these days, I thought I'd just search I just searched eBay, got the cheapest one I could I could get. It looked pretty good for 80 bucks. I figured you couldn't go wrong. So, let's crack it open, see

**Dave Jones:** what's inside. And there we go. There's not much, uh, in it at all. As you can see, there's a just a, uh, small transformer in there to power the electronics itself. That wouldn't actually power the heater. There's the IEC connector right up the

**Dave Jones:** back. Nicely, I don't know if you can see in there, but they have put, uh, silicon sealant around that IEC connector because they have been known to actually, um, pop out if you pull the plug out hard enough. So, that's a nice

**Dave Jones:** little touch. And apart from that, here's the front panel. Board, let's take a look at that in detail. And there's the controller in it. It's a HT46R23. That's a Holtek brand 8-bit, uh, microcontroller. Nothing fancy, it's just a 8-bit micro with some ADCs and

**Dave Jones:** and other stuff. That's pretty much all you expect in this sort of thing. Um, it's really all you need. It's a single-sided board. They've really lowered the cost on this one. This is how they've, uh, got the price down to

**Dave Jones:** that incredible level there. But, um, it's it's not bad at all, really. Um, for the price, you can't, you can't complain. There's that, uh, silicon again. They've dobbed the silicon around the, uh, cable uh, clamp there and the

**Dave Jones:** main switch on the front, which goes back to the, um, the main transformer. And not a problem. It's just I don't know. It's it's not bad. It's pretty much what I expected. There's certainly nothing wrong with it. And interestingly, there's a test jumper

**Dave Jones:** there. They've got a little uh, a little header connector there for some sort of test. I might have to whack a jumper on that and see what it does. But as you can see, it's all basically goes is actually connected

**Dave Jones:** straight through to the through to the front panel. There's no wiring on the bottom. You can see the seven-segment displays for the LED. They are soldered directly on the back of the buttons. They're on. That's the cal pot.

**Dave Jones:** There's a hole in the front for for adjusting the calibration on this thing, which you can tweak yourself if you wanted to. And there's the control pot as well right in there which goes through to the knob on the front panel.

**Dave Jones:** Pretty basic and not a bad design at all. And judging by the date code there, 2010 410, there you go. It's a fairly recent model. And it's time to take the handpiece apart. Now, there's only two screws here by the looks of it. And this

**Dave Jones:** bit here looks like it just screws off like that. I like it. And we'll take those two screws out and see what's inside. Oh. Tada! There it is. There you go. And that's pretty much exactly what I expected.

**Dave Jones:** There's a centrifugal fan here which is also called a squirrel cage fan or a blower fan, something like that. It It takes in the air through here which comes through the case through the vent holes in the case.

**Dave Jones:** You'll note that the other side actually has fake vent holes. They're just there to match it visually, but they don't actually have anything cuz there is no intake on the other side of the fan. Now, that's a 24 V. There we go. It's a

**Dave Jones:** 24 V 0.1 amp blower fan. And as you can expect, the intake is here, and it just comes out. And this here is actually a rubber outlet. It has its own little holder there to actually prevent to to prevent the air that comes out

**Dave Jones:** from back flowing into the design like that, I guess. That's the whole idea of it. And it just blows through, and there's the heater element goes down in there. I won't take that apart any further, I don't think. I

**Dave Jones:** don't really want to damage it. I don't care. There's just a heater element in there with a temperature sensor. And that's pretty much it, really. But this down here is a magnetic reed switch because the unit itself has a fancy feature, which

**Dave Jones:** we'll see later, that when you place this in the when you place it onto the holder like that, it actually switches off. The reed switch actually engages like that, and it switches it off. Nice little safety and convenience

**Dave Jones:** feature. I really like it. So, that's how they've implemented that. And underneath here is a tiny little board. Doesn't It's really just a interface board, but it's actually labeled. It's quite nice. There's There's the It's got labels for the heater, for the

**Dave Jones:** fan, for the sensor. There's ground, and there's a U1B. I'm not sure what that is, but yeah, it's just a little interface connector board. I'm sure if I take that out, there's no circuitry on the back there. Now, this is rather interesting. Look at

**Dave Jones:** the fan here, and it's had a huge big chunk almost I thought, well, you know, maybe there was, you know, somebody goose something during manufacture, or it's just something weird, but it's got a matching one on the other side here. I

**Dave Jones:** don't know why. Have they ground that down to make it fit in? I don't think so, cuz I think it, you know, it would have fitted anyway. Maybe it Maybe they did have some sort of ear on there or

**Dave Jones:** something like that. I'm I'm not too sure, but there's a reason why they've actually chopped out those or ground out those two bits. Weird. Now, let's check out the unit in a bit more detail, shall we? It's a nice

**Dave Jones:** funky-looking modern design. I like it. It's really lightweight. There's no big, bulky, heavy transformer in there, so it's all electronic, really. And it's a nice small footprint sitting on your bench. I love it. It doesn't take up much room at all. And of course, it's

**Dave Jones:** got a nice little stand on the side, which is absolutely essential because when you've when you're done working with this thing, you just whack it back on there and you know you're not going to burn anything on your desk unless you

**Dave Jones:** have it sitting next to your scope like that. And well, that would be a bad idea, but generally, it's pretty darn good. I like it. Um really simple user interface. This controls the fan speed. It's just air. 1 through to 8. I don't know what that

**Dave Jones:** actually means in terms of flow rate, but it's got the ability to adjust your temperature up and down, on off, and that's all you need. And on the back here, just a standard IEC input connector. But beware, if you're buying

**Dave Jones:** this, it's This is a 220 V model only. So, it will not do It's not a universal input supply. So, just be very careful when you're ordering these on eBay. Make sure you order the right one. Now, these hot air rework stations come

**Dave Jones:** in two types. The first type is the one that has the fan inside the main unit itself. And it will generally have two cords coming out or a combined one. One is for the power to drive the heater inside the element

**Dave Jones:** inside the handpiece itself, but it will have an air output, which will also connect up to here. But this one doesn't. It actually has the the fan and the air intake built into the handle. Now, there's pros and cons

**Dave Jones:** both ways really. This is a simpler design, I think, just from a design point of view, but it could be louder because the fan is inside the unit itself. But this is an incredibly lightweight unit. It's not heavy at all.

**Dave Jones:** I like an ergonomically ergonomically, mind you, it is actually quite nice. I like it. And the holder as well, this can actually be mounted on the other side. It's got the uh screws over here. So, left or right handed or left or

**Dave Jones:** right side of the bench. So, that's really quite handy. Let's switch it on and give it a go, shall we? As you can see, it switches on and it instantly goes into SLP mode or sleep mode because of the sensor I told you

**Dave Jones:** about in the handle, which sits in here. There's two magnets either side of that. And if you lift it off, bingo, it starts it starts going. There you go.

**Dave Jones:** 118, 135. So, all you do is you set your temperature like that. Let's see how low it goes. It goes down to 100 is its lowest temp, which is great for heat shrink cuz a typical heat shrink might be rated at

**Dave Jones:** say 125 degrees. So, it's just nice to be able to go down to that low. Obviously, it's got to take some time to get back down there because it jumped up to the higher amount. Let's see if it

**Dave Jones:** keeps the temperature when we actually switch the unit off. I've set it to 105 degrees there, like that, and let's switch it off and switch it back on and has it? Yes, it has. 105 degrees. It kept that

**Dave Jones:** temperature. Likewise, if we do 110, let's try that again. And switch it back on. Bingo, 110. It keeps it. Nice. There's one other thing with these uh the fan in the handle is how loud they are cuz you typically you

**Dave Jones:** will have this much closer to you than if your bench unit is sitting like halfway across the bench because as you know sound drops with the square of the distance. So really it's sound is important but as you can hear it

**Dave Jones:** Well, I don't know. It's it's hard to get a relative indicator but trust me that is not very loud at all. It's really quite nice. I like it. And that's at maximum fan volume by the way. If I fan well fan flow rate if I

**Dave Jones:** turn it right down I can barely hear that at all and really that is quite a low fan rate. So in terms of sound not a problem at all. Certainly the Hakko ones I'm used to at work are much much louder than this one.

**Dave Jones:** So I give that a big thumbs up. And as for the manual well don't write home about it. This is it. It's all in Chinese. There is no English language version at all but it does have a couple of little specs here. Let's

**Dave Jones:** take a look at it. The sound less than 40 dB. That would be my guess. Two it certainly wouldn't be any louder than that. Um Let's the adjustment range is 100 to 450° C and the flow rate I presume that's a

**Dave Jones:** maximum of 120 L per minute and it's got a 700 W heating element in there. They have got two models here. They've got the A and the D plus. I guess D is digital plus the only difference I can see is that

**Dave Jones:** well it says it's got LED here but there's some different characters there and it's got 1° C there for the D version. So I guess the D version is the one to get. I haven't actually seen the A so I don't know what

**Dave Jones:** the differences are. Of course one of the big questions with these sort of things is they will eventually uh wear out and can you get spare parts for them? I have no idea. Uh A 10, not exactly a uh

**Dave Jones:** top-quality brand, but they're not a One Hung Low either. Uh they do have an internal assembly drawing with what looks like maybe uh a parts list. I am not sure. Um so, maybe you can get different parts for

**Dave Jones:** it, but I wouldn't count on it. But for 85 bucks, jeez, or $82 I got this for, I'm not too concerned about that. One of the things I am going to test is the temperature accuracy, or I'm going to

**Dave Jones:** try to anyway. I've got my Fluke uh thermocouple probe here, and I've got to be careful. This only goes up to about 260 maximum, um I I believe anyway, but let's uh see if we can see if the temperature

**Dave Jones:** matches. I don't expect it to match precisely. So, there you go. If I steady that a bit and keep it consistently right in front of there, I am getting uh it's it's telling me it's around about 170, but you know, really I'm not

**Dave Jones:** sure of the uh exact distance or uh you know, how to measure uh temperature airflow like that. If there's a standard distance, I don't know. Some people might know more than that. Let me know, but it's not too bad. Check it out. At a

**Dave Jones:** at a usable, say, 1 in from from the device, something like that, which is a typical distance you might use it or closer than that, it seems pretty darn close to that 150. It's I I certainly wouldn't complain about that at all, so

**Dave Jones:** I'd say that's a pass. The temperature regulation seems to work just fine. And of course, one of the useful things of these hot air rework uh stations is for doing heat shrink nicely. This is a typical heat shrink. It's rated at 125°

**Dave Jones:** C. Let's give it a go. I've set it to uh 125 there. And let's see. Wait. Yeah, it should that should shrink uh nicely, and it does. Not a problem. You can you know, better than using your soldering

**Dave Jones:** iron or a match or something dodgy like that. It's just nicer to use a nice controlled temperature. So, that's a very useful feature of having this go down to 100° C. I like it. There's some heat shrink that

**Dave Jones:** actually melts at a bit lower than 100. I think you might even be able to get 80° heat shrink or something like that. But, that's just really handy. So, you don't damage the wires or anything else that you're actually heat shrinking.

**Dave Jones:** Beautiful. There is one thing to note when you put it back onto the handle like this, it doesn't switch off instantly. Presumably to actually protect it to allow time to cool down. But, it's you can see it's actually

**Dave Jones:** dropping now. It's actually switched off the element in there, but it's still blowing the fan just to keep that. And you'll find that when you when it hits 100° C, it will switch it off. So, okay, I know what

**Dave Jones:** you're all thinking. Does it actually remove components from the board? Well, let's try and remove this BGA device in here. It's a small microcontroller. Let's try and get that off. With we should have no chance in hell of

**Dave Jones:** doing that with a regular soldering iron. So, let's give that a go. Let's uh sort of adjust this up to safe. Let's go to uh I don't know, 410, whatever. Let's go to 410. I've got my uh air turned up to Let's Let's not turned

**Dave Jones:** up to max. Let's turned up to about six, shall we? And let's give that a go. Okay, here we go. Let's give it a go. I probably should be holding this. There's a couple of ways to actually do this.

**Dave Jones:** One is to hold it upside down so gravity will make it pop off. But, I'll just go around. I've got a thin nozzle tip which will talk about in a sec. But, let's just go around the chip like that and see if we can

**Dave Jones:** see if we can pop it off. There we go. It's coming. Tada! Oh, it's yeah, the problem is I haven't held my board, but there it is. Bingo. Now, with these things you got to be careful because uh they can the board

**Dave Jones:** is still actually uh quite hot. I can feel that whole board has heated up. I can barely touch because it's got copper around the outside, but there you go. It got that BGA off no problems. And if you

**Dave Jones:** wanted to get those pads, you would just uh suck that off with some solder wick to get the excess solder off the pads and then you can rework the device. It works quite well. Now, let's try say a uh TSOP package

**Dave Jones:** here. Let's Let's try and suck say this one here off, okay? Now, because this is a little TSOP, uh it's it's hard to get say your uh well, it's actually impossible to get your cutters in there and trim each leg as you could do maybe

**Dave Jones:** do for say an SO package. I've taken some SOs off in that way, but it's much nicer to uh suck it off with the hot air gun. So, let's give that a go. Let's see if we can uh suck out that TSOP chip.

**Dave Jones:** Bingo! There it goes. Not a problem at all. Too easy. And uh the chip can we could we could actually reuse that chip if we wanted to because it's still intact. There's no problem there at all. And if you want to clean

**Dave Jones:** up those pads, as I said, just use some solder wick. Not a problem, but you can suck uh most components off like that without doing any major damage to your board. Now, the uh temperature is is quite important. I used um you know,

**Dave Jones:** over 400° there at that you know, it depends on the quality of the board. This is a very high quality high temperature um, FR5 uh, board. So, so it is actually designed to do uh, quite high temperatures, but you may want to watch

**Dave Jones:** the temperature the uh, temperature and the air flow rate. There's a bit of art in that.

**Dave Jones:** And there we go. Lift straight off beautifully. And let's try this little 5 by 7 mm uh, oscillator module, shall we? Let's give that a go.

**Dave Jones:** There we go. Lift straight off. No problem at all. Love it. Ta-da! Now, there's the BGA device which we sucked off and as you can see it's a very small uh, ball pitch. I think it's less than 0.5 mm pitch and that came off

**Dave Jones:** quite nice. Now, you could actually reball that BGA, but there's a whole art in doing that and there's machines that allow you to do that sort of stuff, but there you go. And it comes with various uh, size nozzles as well, but I found I

**Dave Jones:** really virtually never use the large ones. I typically only need to use the uh, smaller nozzle like this, but your choice. It comes with them anyway. So, that's the Atten Instruments 858D plus hot air rework soldering station. There's not much you can really review

**Dave Jones:** on hot air station. It works. I've been using it in the lab here for a while now and it works pretty well. No problems at all. Compares pretty favorably with the Hakko and other brand uh, ones I'm familiar with in the industry in terms

**Dave Jones:** of uh, you know, capable thermal capability to get parts off the board and stuff like that. Not a problem. It's got everything you need. It's got adjustable air. It's quiet. I like it. Ergonomically, it's pretty good. It's lightweight. Uh, it's you know, it's got

**Dave Jones:** digital readouts. Seems to maintain its temperature pretty well. Well, what more do you want? It's incredible value for money. I got just over 80 Australian dollars delivered. Unbelievable. There's absolutely no excuse for not having a hot air rework

**Dave Jones:** station in your lab. So, go out and grab one at that price. Ridiculously good value for money. I guess the only question mark is what's its long-term reliability like? I don't know. That remains to be seen, but the price, you

**Dave Jones:** can't go wrong. Catch you later.
