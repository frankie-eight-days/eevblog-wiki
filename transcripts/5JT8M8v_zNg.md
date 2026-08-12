---
video_id: 5JT8M8v_zNg
title: EcoFlow Delta Pro - RTFM Dummy!
url: https://www.youtube.com/watch?v=5JT8M8v_zNg
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 32, "3": 48, "4": 63, "5": 79, "6": 93, "7": 109, "8": 127, "9": 141, "10": 160, "11": 177, "12": 191, "13": 205, "14": 219, "15": 232, "16": 249, "17": 263, "18": 280, "19": 297, "20": 312, "21": 330, "22": 346, "23": 361, "24": 373, "25": 385, "26": 399, "27": 414, "28": 431, "29": 447, "30": 461, "31": 470, "32": 483, "33": 495, "34": 515, "35": 528, "36": 540, "37": 550, "38": 563, "39": 576, "40": 585, "41": 597, "42": 610, "43": 623, "44": 640, "45": 655, "46": 674, "47": 689, "48": 702, "49": 715, "50": 728, "51": 738, "52": 755, "53": 767}
---

**Dave Jones:** Hi, I'm back in the old garage lab here where I've got the EcoFlow Pro battery here which you've seen the teardown video of. And if you see my recent AC transfer switch video, you'll know that I was going to install that to

**Dave Jones:** have this 3.6 kWh battery actually power all three of my fridges. There's a chest freezer there and I've got a fridge over there and there's another one inside and I've actually rewired them. And I was going to install my

**Dave Jones:** transfer switch in this DIN enclosure here, but I I don't think so now cuz I think I've found an issue with it. Well, two issues with this that make it really not suitable for the application that I want

**Dave Jones:** here. So, yeah, I was actually going to use like a physical mechanical tie in factor for the last like 3 days or whatever. I have actually been using a physical mechanical timer here that comes on at you know, 9:00 a.m. in the morning. So,

**Dave Jones:** you know, when the sun comes up and shuts off at like 4:00 so that this battery can be recharged from my solar existing solar systems. That's a just a neat simple trick you can do without having anything fancy. You can just have it come on

**Dave Jones:** during the day and if if the sun's out it's you know, it would only like charge slow charge at 400 watts or whatever over that time. And anyway, so I've got three outputs powering my fridges here, but the first issue I had was like it

**Dave Jones:** was working fine for like 3 days and then last night it just all of a sudden just switched off like the actual AC output here just magically switched off. And it's like well, I've only been having it going like 3 days or whatever

**Dave Jones:** and it's already switched off once. That doesn't vibe well for the long term Uh, know, like viability of this thing. So, um, yeah, that's not terrific at all. Sure, the AC transfer switch would would supposedly cut in and fix

**Dave Jones:** um that issue, but that's kind of not the point, you know? Um, the point is that the AC transfer switch would only cut in when the power fails anyway. I've got my mixing portable scope here. So, that that's problem number one, okay?

**Dave Jones:** Second problem here is that um when this was actually when when the timer would switch off, okay? And the mains input was disconnected, I heard the fridge compressors go, you know, ka-thump, as in they had like briefly, momentarily lost power and the fridge

**Dave Jones:** was actually recycling itself. So, yeah, I I suspect that this AC mains output here is not continuous when you actually switch input sources. I believe it's actually discontinuous. So, I'm going to try and capture trigger this on the

**Dave Jones:** scope here. Okay, so what I've got set up here is I'm triggering on a condition on a pulse. I I've got trigger type set to a pulse less than uh you know, about 9 milliseconds or something. I had this sort of thing, so

**Dave Jones:** it'll like if there's any like dropout in the waveform, it should actually trigger on that, okay? So, I'm going to put that on single sequence and I'm using my high voltage differential probe here and just for convenience sake I

**Dave Jones:** just opened by a Silicon Chip Energy Meter here and I'm just probing in there. It's just convenient place to probe the mains. There's nothing special about that. I just don't I forgot to bring a lead from the lab that like a death lead that

**Dave Jones:** actually had just bare ends on it. So, anyway, that's just a dodgy way to probe it. Anyway, here we go. I'm going to single sequence capture this and we'll see what What to do is I'm going to disconnect. So, it's

**Dave Jones:** charging at the moment 2.2 kW. Oh. Oh, hey. Hey, you see why did you just drop? You You saw that, right? That That wasn't just me. It just dropped. Why did it just drop? Huh? It should be a continuous

**Dave Jones:** charging power. Like it should draw a continuous amount of power. I don't know, maybe there was something inside some mechanism inside that was I don't know, it briefly checks the state of the battery and just disconnects that lowers the charge. I

**Dave Jones:** don't know. You got any idea? Leave it in the comments. Anyway, I'm going to switch it off. So, I'm going to switch like the mains input to here off. And let's see. Yep. Yep. Bingo. Bingo. Captured. Look at that. The

**Dave Jones:** output is not continuous. What uh time period or on 10 milliseconds per division. So, you can see dropped out there. 10 milliseconds took 20 30 milliseconds before it started back up again. And bingo, that is why I am

**Dave Jones:** actually getting like my fridges like the compressors or whatever. I don't know really how fridges work but like the the compressors are like restarting or whatever. Um and I can occasionally hear that hiccup um because they're getting a disturbance in

**Dave Jones:** the mains there. This is not a continuous thing. Um you can see that I'm getting 234 V RMS here. And uh yeah, it's just dropping out. That should not happen. I would expect this output, right? Cuz this comes from the internal inverter.

**Dave Jones:** You've seen the teardown, right? The internal inverter should continue to operate regardless of the source whether the source at the moment is coming from the internal battery in here, right? And it's drawing all my three fridges depends on which ones are on whether or

**Dave Jones:** not they have the freezer compartments off or on. So, this varies a lot anywhere from like zero um to 40 to 100 to 300 to 800, something like that, depending on uh where cuz they're all asynchronous essentially, all three fridges. Um so,

**Dave Jones:** you don't know which one's going to be on at any one time or which, you know, freezer or fridge uh compressor, you know, thing is going to be on or whatever. Um and uh yeah, if it's got like an auto defrost, the these

**Dave Jones:** chest freezers generally don't have an auto defrost, and this one doesn't. Um but I think the fridges have like an auto defrost cycle, and yeah, that can take a X amount of power. But anyway, I was actually successfully for 3 days

**Dave Jones:** powering my fridges overnight um after 4:00 p.m. and it would just cut off, and the battery would just last. It was just enough to last overnight until 9:00 a.m. the next morning. But yeah, I I would hear the fridges actually, um you know,

**Dave Jones:** the compressor start again. So, it's got a dropout. So, obviously, this thing is is not a continuous inverter. When it uh loses, well, when it switches the input, maybe it's it's actually Well, we saw the teardown. There were

**Dave Jones:** physical relays in there. So, it's probably relay switching the input sources. The input sources being the battery, the internal battery, the AC mains at the back, which, you know, has its own uh charger uh circuitry, right? Or the so or I

**Dave Jones:** presumably the solar input um as well. And this is not continuous. I would have liked to I really want a continuous, you know, output uninterrupted output. They should have electronic switching on the input to that. This should be

**Dave Jones:** seamless. You can't have like, you know, your waveform dropping out like that. That's just That That is not good enough. Um no. NO, I DON'T WANT my fridges to, you know, who knows what, you know, start I think some people in

**Dave Jones:** the comments have mentioned that, you know, if you start and stop the compressors a lot or if they lose power or whatever, then it would um yeah, it would shorten the life of the compressors. They can lock up or

**Dave Jones:** something. I don't know how how compressors work, but um yeah, leave it in the comments um if you're knowledgeable in that sort of field, but I don't I DON'T LIKE THE IDEA OF USING this to power my fridges now. So, I think I'm

**Dave Jones:** going to have to um ditch this for powering the fridges and I'm going to have to go with well, I was going to go with my hybrid inverter solution. I was going to replace my Sunny Boy inverter. Um oh, I can show you that actually.

**Dave Jones:** Let's go outside. You've seen my Sunny Boy inverter before. Well, it's wet and miserable today. There's my Sunny Boy inverter. There she is. It's currently producing even the overcast rainy still This is my old 3 kW system. It's still producing 770 W

**Dave Jones:** there, which is more than enough to like um you know, power those uh that battery and um power the fridges or whatnot. Um you know, recharge a battery for the system. Anyway, I was going to replace This is a 3 kW

**Dave Jones:** inverter. I was going to replace this with like a 5 kW inverter um and I was going to expand this solar on my pergola roof, add a four extra panels, so an extra string. This one does actually have two string inputs, but I'm already

**Dave Jones:** maxed out on the 3 kW. So anyway, I was going to get a hybrid inverter. Um there's various ones on the market uh that can do this and then I can plug in a battery to the hybrid inverter and

**Dave Jones:** that will provide me a an emergency power output and B, it will um store energy during the excess energy during the day and then uh it will let me um reuse that at night. It's not a full AC

**Dave Jones:** backup battery solution, but um I don't need that cuz the power rarely fails here in Sydney. A lot of people ask me that. No, it's incredibly rare for the power to fail here and if it does, it doesn't do it for very long. But anyway,

**Dave Jones:** I was going to do that. So it looks like I'm going to have to replace that with a hybrid inverter and a battery solution, and then if the power does fail, I'll still have an emergency output um thing, and then I don't have to dick

**Dave Jones:** around with all sorts of uh you know, like isolating the house, cuz the hybrid inverter will do the isolation on the house side here. It'll isolate all of this, so if the mains power fails, you want your inverter not to feed power

**Dave Jones:** back into the grid. So, you want this uh so it'll automatically isolate the grid side of it, and then it'll have another output coming into the battery, and then it'll have another emergency out power output, which then I can emergency

**Dave Jones:** power, you know, the fridges and freezers and other things. If we do rare happen to get one of those rare power outages. So, yeah, um so I'm going to have to do that. So, anyway, let me try that again. Let's single sequence that.

**Dave Jones:** Let's Let's see if it does it when it powers on. Oh, briefly, look. Look, briefly there, right? So, it is actually not not as bad. Not as bad, so I do think this will actually vary if I do it multiple times.

**Dave Jones:** So, but you can see it. It did glitch there. So, this is certainly not a continuous thing. Um and yeah, I could do more capture um like cuz it hadn't actually started up at that point, I don't think. So, anyway, yeah, it's not

**Dave Jones:** a continuous output. So, let me do that again. Power off. Charger off. Boom. Yep. It's done exactly the same thing. Exactly the same response there. That looks like like input relay source switching. You can see a part of the part of the sine wave

**Dave Jones:** there, but yeah, it's No, it's that's input relay switching. So, there you go. That's mechanical relay switching instead of electronic switching, and I don't think that is suitable to power my fridges. But anyway, leave it in the comments down

**Dave Jones:** below if you don't think I should use this. I I don't think I'm not getting the vibe from it anymore. Like it's fine for its intended purpose, which is like a portable, you know, backup generator and stuff like that. You know, great. And you take

**Dave Jones:** it camping, you throw it in your trailer, and you get the big solar panels and everything else. But for a home solution like this, I know. I want I I don't want that. Switching like that, especially a couple of times a day

**Dave Jones:** when this thing is going to switch off and on a couple of times a day during charging. So, anyway, that's disappointing. So, I think I'm going to scrap that idea. I was all ready to install my transfer switch and everything, but I noticed

**Dave Jones:** these two issues there, and I don't know why it just like it switched off. Was that like an earth leakage detection thing? But I've never had it happen before with any of my fridges here, and we've got earth

**Dave Jones:** leakage circuit breakers in the fuse box, and yeah, it's never I've never seen it happen. So, and I've got an additional one on the wall. In fact, this one. Which I I was actually using until yesterday to power this, and yeah. So, I don't

**Dave Jones:** know, but this yeah, like the inverter was still working. It still had like 60% battery or something. And last night, the actual output just switched off. So, I don't know. So, there's two issues there. That should have electronic

**Dave Jones:** switching. So, yeah, fine for its intended purpose, but just not I don't think suitable for what I want it to do. Anyway, let me know your thoughts. Catch you next time.
