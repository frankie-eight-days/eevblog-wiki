---
video_id: aVBmnVKDJQg
title: EEVblog #1032 Part 5 - John Kenny Keysight Interview
url: https://www.youtube.com/watch?v=aVBmnVKDJQg
source: youtube-asr
timestamps: {"0": 9, "1": 21, "2": 30, "3": 45, "4": 58, "5": 68, "6": 75, "7": 86, "8": 96, "9": 104, "10": 111, "11": 122, "12": 131, "13": 143, "14": 157, "15": 166, "16": 187, "17": 195, "18": 208, "19": 221, "20": 239, "21": 248, "22": 261, "23": 273, "24": 284, "25": 293, "26": 307, "27": 321, "28": 332, "29": 349, "30": 358, "31": 364, "32": 373, "33": 382, "34": 395, "35": 404, "36": 423, "37": 437, "38": 443, "39": 454, "40": 462, "41": 468, "42": 475, "43": 482, "44": 502, "45": 515, "46": 525, "47": 536, "48": 548, "49": 558, "50": 571, "51": 581, "52": 592, "53": 601, "54": 608, "55": 619, "56": 627, "57": 634, "58": 644, "59": 656, "60": 663, "61": 676, "62": 686, "63": 696, "64": 707, "65": 716, "66": 724, "67": 734, "68": 744, "69": 755, "70": 761, "71": 771, "72": 788, "73": 797, "74": 811, "75": 820, "76": 833, "77": 842, "78": 853, "79": 862, "80": 870, "81": 881, "82": 888, "83": 896, "84": 907, "85": 921, "86": 930, "87": 939, "88": 945, "89": 955, "90": 963, "91": 971, "92": 984, "93": 994, "94": 1006, "95": 1017, "96": 1027, "97": 1038, "98": 1044, "99": 1053, "100": 1064, "101": 1071, "102": 1082, "103": 1088, "104": 1100, "105": 1106, "106": 1118, "107": 1132, "108": 1139, "109": 1152, "110": 1164, "111": 1171, "112": 1182, "113": 1192, "114": 1209, "115": 1223, "116": 1229, "117": 1237, "118": 1248, "119": 1256, "120": 1267, "121": 1276, "122": 1285, "123": 1297, "124": 1305, "125": 1316, "126": 1328, "127": 1336, "128": 1343, "129": 1351, "130": 1358, "131": 1370, "132": 1376, "133": 1390, "134": 1404, "135": 1411, "136": 1417, "137": 1425, "138": 1442, "139": 1455, "140": 1467, "141": 1481, "142": 1492, "143": 1499, "144": 1507, "145": 1517, "146": 1526, "147": 1539, "148": 1553, "149": 1563, "150": 1574, "151": 1581, "152": 1590, "153": 1600, "154": 1607, "155": 1615, "156": 1624, "157": 1631, "158": 1640, "159": 1650, "160": 1668, "161": 1679, "162": 1693, "163": 1704, "164": 1715, "165": 1730, "166": 1737, "167": 1745, "168": 1753, "169": 1759, "170": 1766, "171": 1778, "172": 1787, "173": 1795, "174": 1803, "175": 1811}
---

**Dave Jones:** I'd love to know the design phases of this thing. You worked on this? Yeah. Yep. Well, you designed the front panel. But you worked intimately on managing Did you manage the development?

**Dave Jones:** No. No. No. Okay. No. So, I'm a technology manager. I one of the things I do is I work with teams to create common building blocks they could choose between all the projects.

**Dave Jones:** Okay. Got it. And I'm often brought in to help them go over a particular difficult technical challenge. So, for example, on the high-end function generator, they had some horrendous problems with the switching power supplies to power up all the high-power ASICs creating spurs Yeah.

**Dave Jones:** Yeah. into the output of the function cuz at 120 MHz Oh, yeah. it doesn't take much to get bad noise output. And I brought in some power supply people to help them redesign all the power supplies to reduce the noise cuz our power supply group is really good at low noise switching.

**Dave Jones:** Yeah. They were not good at low noise switching, but they had tons of power requirements cuz they had giant ASICs in there. A giant FPGA, I should say. And some really high current DACs and ADCs or not ADCs, but you know, just high power circuits.

**Dave Jones:** So, the the switching circuits they put in were like larger than they'd ever designed before. And Mhm. they're not experts on switching power. But the folks in New Jersey are.

**Dave Jones:** So, I got involved and I got another guy involved and we redesigned their entire power subsystem for them so they could stay on track on the project. There's When they hit a wall, rather than say, "You guys better fix it.

**Dave Jones:** Work 12-hour days for the next 3 months." No, that's not how we're going to do it. We're going to bring in people who know how to do it and get it right quickly so you don't delay the project 3 months and don't burn out.

**Dave Jones:** Do we get it done right and get it done once. So, I'll do that. I'll the folks who developed their SMUs didn't know how to do this kind of graphics interface.

**Dave Jones:** So, I had the the team that developed it the the firmware for this and our hardware design for this and we transferred that stuff to our Japanese team that did the SMU.

**Dave Jones:** So, the Mount the Mount Fuji project was our our new SMU to compete with our our folks in Cleveland and they leveraged all that stuff from the other designs.

**Dave Jones:** They use the same same circuit designs. They took the schematics and transferred them. Yep. And then they built it up from there. Um that's what I do is I help make those connections.

**Dave Jones:** So the development process, you need a replacement Mhm. for the what is it 340 3401. 34401. Um did you come up was it what shipped was that the original concept?

**Dave Jones:** How many ever or what sort of evolution did you go through? So did you go like we're going to have a graphical screen that's going to have the it's going to have the graph in and it's going to have this and how We already had the um the function generator at that point.

**Dave Jones:** Oh, okay. The function generator was pretty much the first major product. The counter and the function generator were developed more or less in parallel. Um so we had the basic structure, but it didn't meet the cost target.

**Dave Jones:** So that's when we had to kind of crush it and and reduce the cost dramatically and that's where I got heavily involved. But the DMM technology, believe it or not, was actually taking the We had done a research project on replacing the 3458 which we ended up putting aside and that team stopped working on that and then we had them go and do a dramatic cost reduction to fit it in these kind of

**Dave Jones:** price points Interesting. and strip it down and simplify it and then the team, you know, in in our Loveland, Colorado site came up with the the voltmeter to make it meet the cost targets.

**Dave Jones:** I came up with the the new low cost front panel and we merged the whole thing together. But this architecture is dramatically different than the 34401. Yes. The 34401, the the fundamental problem with the voltmeter is that it's isolated.

**Dave Jones:** Mhm. And the 34401 has the entire processing core next to the measurement engine. Yeah. And it directly controls the measurement engine and the entire front panel is floating Right next to Yeah, yeah, yeah.

**Dave Jones:** at the measurement potential. That worked back in the day of GPIB and RS232 cuz we can isolate GPIB and RS232 over very simple UARTs. There's a chip called the um the protocol, which basically takes and isolates that and brings it across isolation into a custom ASIC.

**Dave Jones:** And that's great for GPIB and RS-232, but when you get to USB and LAN, it can't be done. You need processing right next to the LAN and USB cuz it's all grounded.

**Dave Jones:** You can't isolate USB and LAN very easily at the high speeds. So So you changed the architecture entirely to put the processing ground, which did control the screen and did all the processing right at the back end, so to speak.

**Dave Jones:** That's correct. That would be what we call the ground potential. So the the front panel display also, because this is would be floating, that was a problem. Isolating this with safe with a flat panel display is a little bit more challenging than with a vacuum fluorescent display.

**Dave Jones:** It's a little bit easier to keep the cracks from giving you, you know, shock hazard. So um This also the LCD display has to be directly connected to the processor.

**Dave Jones:** 24 lines. I mean, it's a very wide bus. So all that had to get moved to ground. So they had to develop a whole new protocol to a much smaller set of hardware that controlled the actual measurement engine.

**Dave Jones:** So they developed a whole new system to do that for this project and that's what enabled these products to do what they did using the same processor platform for the most part that's in the counter, the function generator, and our power products as well.

**Dave Jones:** Got it. So we did end up using FPGA for the measurement? There's an FPGA and a single chip. And a single What's the single chip? The single chip does the communications across isolation and does the slower state machines and the FPGA does the high-speed processing of the delta sigma A-to-D.

**Dave Jones:** So it does the big fur filter that basically takes this this A-to-D converter, you know, doing high-speed sampling and multiple bit and then turning that into a slow, very high resolution reading.

**Dave Jones:** So cost was paramount, was it the entire driving factor behind this? And well, there were two. One would be complete compatibility with the existing product cuz it was so ubiquitous and integrated into the largest largest selling product in test and measure.

**Dave Jones:** In your company's In my company's probably in any of my test and measure company's just the we're the biggest but the 34401 at its peak sold over 25,000 a year.

**Dave Jones:** Yeah. We're not back up to that with this but we're heading there with some of it is cuz competitors have come in and taken some away but and it's still growing.

**Dave Jones:** This is still growing quite nicely but uh So there was compatibility and there was cost seemed to be the two Absolutely. driving factors. Nothing else. Well and also differentiation.

**Dave Jones:** We had to add new capabilities. We had to do the new graphics display. We've added data logging. We've added histograms, things like that which you know today They're very useful.

**Dave Jones:** Exactly. But the point is you got a graphics display damn it use it. You know? And that's it's not just a different way to control the thing cuz the menuing system on the 34401 is not as easy to use as this but it it's hard to justify switching all that just for that.

**Dave Jones:** Right. might as well get more data and there's more things we'd like to do with the display but you know and they did some newer things I think with the 65 and 70 if I'm not mistaken they have dual parameter information.

**Dave Jones:** Yes. Yes. Yes I do. There is a dual display. That wasn't in the first one. We we didn't have enough time to fit that in. They wanted to but when we got the 65 and 70 they added that and frankly with the 34410 and 11 they had the dual parameter in a vacuum fluorescent and when we first introduced the the more basic models we didn't have it and we

**Dave Jones:** got feedback that was a problem. They liked the dual display. So we they fixed it and they they rolled it out in the 65 and 70. The biggest challenge in this was when they developed the 34401 literally they were on the second floor of a building and the manufacturing center was on the first floor.

**Dave Jones:** So good. So it was very easy to optimize cost and learn what how you're going to cost this what the rules for engagement were to optimize in the right way.

**Dave Jones:** Now this thing is manufactured in a CM not even in our Penang operation. Oh okay. And our the supply chain of the the transformer is made in Quantan Malaysia.

**Dave Jones:** Right. Okay? And back then we bought it from a local vendor. All right? And therefore optimizing it the perfect shielding you get the common mode noise all those things was much easier.

**Dave Jones:** You got in your car, you drove to their site and in an hour you have a meeting, you get the thing and you get to move the shield this way.

**Dave Jones:** Yep. You know, no problem. Now, it's a third-party through our Penang operation back to the States and and getting the cost of it and getting the performance of it is much more difficult.

**Dave Jones:** So, one of the other things I do is I help I go to Penang fairly frequently and they had an issue with the vendor we were using, they weren't meeting the cost.

**Dave Jones:** I actually traveled to China to visit another new company to cuz I I do a lot of magnetics materials work for people cuz our power supply background and I did visit the new comp this new company and vetted them out and made sure they could do a quality job and and help communicate our technical needs and they're now meeting cost on that much better than they were before.

**Dave Jones:** Is the reason you went to a contract manufacturer a CM for that you were using the terminology there? Is it Is that purely a price point thing? Or like why don't you mean you've got your own huge manufacturing facilities?

**Dave Jones:** We do. And it's an interesting story. It Some of it I think in retrospect, we might not have done but let me play the whole thing out. First of all, keeping up with the latest surface mount board loading technology.

**Dave Jones:** It's very expensive and it's constantly changing. But you're not going high density and stuff like this. Well, we're not as high density as some products, but we're we're certainly using smaller and smaller parts everywhere.

**Dave Jones:** And fine pin pitch BGAs and pain in the butt things. and even our 201s in some cases and DFNs which you know are almost as bad as BGAs. Um and you know, we're moving toward you know 3 and 4,000 traces and spaces.

**Dave Jones:** So, Oh, okay. things get denser only because that's what the packages are coming out in and they're smaller and you're trying to fit more functionality in less space. If you have to.

**Dave Jones:** But the point was our company made a decision to get out of board manufacturing cuz we This was back we got back after just went surface mount and the equipment was already starting to evolve and change and keeping up with it and doing it in a quality way and as RoHS happened too, Yeah.

**Dave Jones:** we didn't want to make that investment. Better off leave it to the experts. Yeah. you can buy that service. moved the boards out and when we moved the boards out, we still did the assembly of the final product in our own site in Penang.

**Dave Jones:** But then we were still part of the This is kind of a related thing is that we were still part of Agilent at the time. All right. Agilent was still building their life sciences products in the states.

**Dave Jones:** Ah. And in fact in Delaware and a few other locations and they looked at our cost of manufacturing was much lower in Penang and they said, "We want to move that stuff to Penang."

**Dave Jones:** Ah, now they're about to invade. Well, our factory is only so big. And they said, "You guys got to move out to make space for them to move in."

**Dave Jones:** Ah, goodness. basically started We went to the CMs who were building our boards and said, "We want you to build our products." And they said, "That's no problem. We'd love your business." And we started to move a lot of the products out of our local.

**Dave Jones:** And the idea too was that was to lower our indirect overhead. They were more efficient at manufacturing cuz they do a whole lot more of it than we do and it was even less expensive.

**Dave Jones:** And also one of the other benefits is that they often have small shops in the US that we can work with for prototypes even at the final product level.

**Dave Jones:** And for some products where the volume is very small, we would just stay in the US. So, we could we could do more localized manufacturing and get quicker turnaround and faster response time for low volume specials and high value products.

**Dave Jones:** So, we made a decision to move our manufacturing out of our factories to local vendors right in the Penang area or down in Johor and places like that. Um that created some challenges, some transition challenges.

**Dave Jones:** We're not completely through that, but we're mostly through it. Most of the stuff is moved out. Some of the very old products we didn't move cuz we're not going to keep them for that much longer.

**Dave Jones:** So, if you go in Penang now, you'll see production lines for our products, but they're mostly the old through hole and all the old stuff that we don't want to spend the money to move it cuz it cost a fair amount of money to transfer all the test sets and training and all that kind of stuff to other people.

**Dave Jones:** So, one of the challenges for this was this was introduced as we were starting to make some of those transitions. Right. And we were we were still able to keep We tried to do the new products in our factory and then move it at first.

**Dave Jones:** Now we do direct to CM. The new products go right to the CM product. This product was still built in uh Penang operation and moved out after it went into production.

**Dave Jones:** But the newer versions of the product are going right to that. I noticed that. I've got one of the original made in Penang ones. Yeah. Everything's made in Malaysia, but all the stuff is made in our factory.

**Dave Jones:** So, it's it's an interesting challenge and I I think the CMs have been exceptional, frankly, at doing a a good job. It still takes a lot of scrutiny on our part and review and keeping the quality high.

**Dave Jones:** But these are big big corporate company. They know how to do a good job and they we think the flexibility long term is going to be good for us.

**Dave Jones:** Excellent. to move things around, you know, if if a customer needs a special and they have a facility one one of the three, I'm not going to name all the CMs we use, but is really good at transferring between the different sites.

**Dave Jones:** They're That's one of their skills. And we're seeing that as a potential way for us to respond quickly for modifications and specials and new needs. So, we'll see how that pans out.

**Dave Jones:** Some of these things, you know, I wouldn't do myself. Mhm. I'm not saying this one is or isn't, but Yeah, this one's worked out okay. Okay. goal is long term is to lower cost and get more responsiveness.

**Dave Jones:** Yes. Back, do you know what the issue there was? Absolutely. It's Yeah, oh, you do? Tell us. Very interesting story. Tell Oh, tell us the interesting story about how this was re-spec.

**Dave Jones:** It came out of a 1,000 V volts spec and then did somebody realize or did you guys realize that there was an issue? There wasn't an issue. Oh, there wasn't an issue.

**Dave Jones:** Was it blown out of proportion? of blown out of Okay, do do tell us anyway. Okay, so what happened was we had a customer who was very interested in our voltmeter to reduce the amount of calibration they had to do and they wanted us to create a custom version of it they built into their system.

**Dave Jones:** Oh. And And you would do that for a big enough customer? For a big enough customer that would pay us enough, sure. Right. Right. And it was also strategic in that we wanted to learn more about their needs.

**Dave Jones:** So, sometimes we justify things by saying this is a door in to learn more about their needs. In certain growth areas we like to do that. And the team that was going to do that was in one location and they took the design of this and they were going to reform factor it into a card that went in the customer system.

**Dave Jones:** So they're going over the design, effectively doing a complete design review and they noticed that one of the parts in the design, the the voltage across the part was above the rating on the part.

**Dave Jones:** Which part? Do you know? I'm not going to say. Not going to say. Okay. And what happened was they said this is unacceptable and they can't do this and they they said it's a safety issue, which it wasn't and they alerted some people and uh And panic ensued.

**Dave Jones:** And panic ensued and the the knee-jerk reaction was to make a change to cuz safety first. And they changed to the spec, you Changed to the spec and said don't do that cuz we said this could be a safety issue.

**Dave Jones:** And the reality was that upon further review, it was not a safety issue. But but you did publish the spec, you did revise it and published it and hence why it was noticed by people on the forum.

**Dave Jones:** Oh, big time, sure. Yeah, yeah. And it's not a safety issue and the part is acceptable to use in that application that way and we since then have pushed it back to 1,000 volts.

**Dave Jones:** And so you've changed the spec back and everything's hunky-dory. Yes. So there were no changes made? No changes made. New people looked at it and said this isn't Right.

**Dave Jones:** Right. And it turned out it was right but people it's one of these things we've done it that way for so long no one remembered anything about it. But it turned out one of the things that got it back to the right was we took our competitors' products they did the same way.

**Dave Jones:** Ah. And then finding the people who had not looked at this in a long time said you know maybe we need to rethink is this really wrong and figured out it wasn't wasn't wrong.

**Dave Jones:** Okay. And then it's back on track. You know, we don't get everything perfect every time. There's such a complex set of situations. Safety is we take very very very seriously.

**Dave Jones:** So I say if we're going to have any jerk reaction, I'll I'll take it there. Right. Okay. Okay. And unfortunately it did upset people and it was a mistake and we we undid it.

**Dave Jones:** Yeah. And everyone's happy with it now? Everyone accepts your explanation? Well, then maybe they will now. Um I don't know if they're looking at this but that's that is what happened and it was a it was unfortunate that it caused a disruption and wasted our customers' time, wasted our internal time.

**Dave Jones:** But the fact is that you get judged by when you get it right. Yep, the end. Yes, exactly. We're sorry that we accidentally thought something wasn't as safe as it really was.

**Dave Jones:** Yep. But that's But on the cautious side. That's right. Yeah, a lot of companies would have just don't worry about that. We probably could have gotten this one right sooner and not have the Right.

**Dave Jones:** Okay. But I think it was it was a little knee-jerk on a on our part, but if we're going to do a knee-jerk I'll take it here. Yep. Okay.

**Dave Jones:** So that's what happened. I was actually involved in that. Oh, okay. Yeah, cuz power supplies have a lot of safety issues, especially switching offline power supplies. So I was pretty familiar with it and I was one of the people that knew it wasn't a problem.

**Dave Jones:** But the certain people felt there were too many opinions in the room and told me to stand down and I said Right. Okay. Okay. And they finally came around.

**Dave Jones:** You know, I'm not saying I'm glad I was right, I'm glad that they got that they got it right. That's what matters. All right. It wasn't one of our best days.

**Dave Jones:** Got it. But it all worked out well. Yes. Excellent. Say um compliance, you know, the cat testing and stuff like that. Not so much the bench meters, but hand very important in handheld meters and things like that.

**Dave Jones:** Have you ever sent something away that's, you know, like failed and they've come back and say hey or hey, this is not going to pass or something like that or you do you guys always get it right first time?

**Dave Jones:** You're so experienced there. get it right first time. It's a challenge and and frankly the new IEC 61010 that we comply with it's much more challenging. Yes. One of the subtle things What's what's the major change for those?

**Dave Jones:** One of the biggest changes is that you have to anticipate likely mistakes the customer might make. All right. If that causes safety hazard, it's a problem. As in operational mistakes, probes in the wrong, everything.

**Dave Jones:** Probes in the So for example, on our new power analyzer which can measure 1,000 V. Right. And isolated 50 amps of current isolated from the 1,000 V. Um we have BNCs for the the current input.

**Dave Jones:** If you want to put an external transducer on the current input, and when we went to put the triggers that are a ground reference, we can't see cuz they could plug the 1,000 V isolated thing onto the BNC.

**Dave Jones:** the chassis. two connectors. Yeah. You know, you can't just put a label on the back saying don't do that anymore. Right. They have to anticipate likely mistakes, and it still has to be safe.

**Dave Jones:** We could have had it hook up to there if we made it a 25-amp BNC. Right. Okay? That's the kind of thing, you you know, that's going to start shifting us into doing new ways.

**Dave Jones:** You can't just put a label saying if you're stupid, you're going to get hurt. Right. It's not good enough. It's not acceptable. It won't pass compliance. That's correct. And that's relatively new, and uh But that's not a bad thing.

**Dave Jones:** No, it's a No, that's good. It's a smart thing, but you know, certainly something that you you see examples where that was the that was the way you handle it.

**Dave Jones:** You just said, you know, "Oh, can't we just put a label?" You can't You don't do that. Right. You can't just put a label anymore. Um we we're having an issue in in some of certain of the power supplies where the the binding post could only handle 20 amps.

**Dave Jones:** Right. And we're going to we're going to have 40 amps. So, what do what do you do? Well, if they pull 40 amps out of a 20-amp binding post, it melts.

**Dave Jones:** Yep. And it can create a hazard. It's hot to touch, it can burn your hand. So, we can't do that anymore. Used to be just, you know, we'd put a uh sense leads on the front panel that say, you know, uh 20 amps max, and that was it.

**Dave Jones:** Oh, and then it throttles it. No, no, there's no throttle. It just says don't do that. Don't pull more than 20 amps out of this. That's not acceptable anymore.

**Dave Jones:** Ah. It was up until I see the new the rev three of the IEC 61010. So, those are some of the standard challenges. And one of the other things we did many many years ago for our power products was we switched from an offline system to a 48-volt grounded system.

**Dave Jones:** We use a distributed DC system. And that's made safety a lot easier to meet for us. Shortened development times because even though our output floats a lot off ground to the 240, our input is only 48 volts, and it's grounded.

**Dave Jones:** Got it. As opposed to being 400 plus with a PFC front end. So, that's actually simplified safety for us a lot and shortened development times and made our performance higher.

**Dave Jones:** Um and that directly because we found that the time was taking to all that primary-related circuitry to pass safety was was increasing test times and compliance testing and certification dramatically.

**Dave Jones:** Now we buy a pre-certified brick, if you will, that handles the left thing. And you're seeing that with a lot of other products they they buy these choke snake things or they you know the phone charger type solutions for low power and all the safety's inside that Yes, that's right.

**Dave Jones:** And that makes things a lot simpler. You're going to see more of that for low cost products. You may even see it for low cost voltmeters. Ah, interesting. Okay.

**Dave Jones:** Because it's just to do all the compliance testing and the cost to do it is it's quite a bit higher and those choke snake things and the little plugs in the wall for the phone chargers are getting higher and higher in power.

**Dave Jones:** Yep. You know, the nowadays you can Ah, it's crazy. Your phone your your phone can put out can take in like 60 watts now. For fast for quick charge three can take in like 12 volts at 5 amps or something like that.

**Dave Jones:** So, you can get little tiny plugs that can put out 100 watts in a 1 inch That's more than enough to power a voltmeter. Oh, easy. It's crazy. Speaking of power, um is does standby power consumption, you mentioned power factor correction and all that sort of stuff, is that a big deal in test and measurement?

**Dave Jones:** Is it a requirement like do you a requirement. It is something we care about. I know the new one we just came out with people are a little upset cuz the the the power when it's off is not really off and we're actually working on the the newer ones and we're going to make it lower.

**Dave Jones:** The newer what? Which product, sir? I can't tell you what Oh, okay. All right. We're continuing to refine that and we're continuing to refine that and we're continuing Still under development.

**Dave Jones:** We're continuing to refine that And somebody internally went, "Hey, this is drawing X amount of watts." Well, we noticed the fan was spinning very slowly. Oh, okay. Okay. your board.

**Dave Jones:** You noticed the fan was spinning because we don't completely turn the power off and it turns out that we use a a PWM fan and PWM fans can make the fan go much slower, so it's quiet, but they never stop completely.

**Dave Jones:** Right. So, in new designs we have to add a switch to turn the fan off, so you won't notice it's spinning because it's not. So, it's just a little nuisance, if you will.

**Dave Jones:** So, there's no requirement if a scope take, you know, has a power factor of 0.5 or something. You don't need Well, something that requires power factor full power PFCs, you know, even low power the PFCs are available down to what less than 100 W?

**Dave Jones:** So, you will have a power factor almost any product today will have a power factor of 0.98 or 0.99. All right. It used to be PFC was only used at 600 W and up.

**Dave Jones:** Now, it's even a 45 W brick has a PFC. Right. Yeah, because the chips have gotten so cheap and it actually above a certain power level, it's actually cheaper to have PFC than not.

**Dave Jones:** The components the amount of loss savings in the parts makes up for the extra cost of the circuit. You can get a PFC the whole PFC fits in a single little hybrid that they make for 50 cents.

**Dave Jones:** Oh, really? Yeah, it's super cheap now. That's right. You still need a choke and things like that, a little bit bigger input filter, but uh no, we we we do care about power efficiency at full power.

**Dave Jones:** I thought you were asking about energy Oh, I'm I'm a pest. It's a cheap power question. We are interested in getting the power lower on the bench. People do not like when it sits there and consumes a lot of power, but there's kind of a threshold about 10 W.

**Dave Jones:** Energy Star is like a 10 it to be below something, but it's not regulatory for test and measurement equipment. It is for consumer products. It's against the law for consumer products.

**Dave Jones:** Got Yeah, right. So, test and measurement gets a free ride. Well, PFC we got a free ride, but we still pay attention to it cuz it's it's a free ride for us to get it.

**Dave Jones:** Yeah, yeah. All right. But, we do we do have to pay attention to it for standby power because people don't like the those big ugly push switches are a pain.

**Dave Jones:** what do you mean big ugly? I like them. Big clunking power switch. a lot of space up. Yeah, I know. Yeah, you got to have a plastic rod to go back and forth.

**Dave Jones:** you wouldn't believe how easy those things break and how much space they take up. broken a few. You doing tear downs? Yeah. So, well, not even tear downs. They break during assembly.

**Dave Jones:** During assembly. Ah, right. Or maybe they get a bit brittle and then break in the field. That's right. Right. So, everything so we're doomed towards We're going to more soft switching for sure.

**Dave Jones:** It also helps boot times because we pre-boot. There's it's it's sort of waiting it's halfway through the boot process, so you hit the switch it comes right back up.

**Dave Jones:** But, it does draw a slight amount of power and we're working to get that lower and lower over time. How low can you get? Like, what do you do you have like a ti- like anything under a watt cuz it's a nice round number or Well, we're Like limited is cuz we're using brick supplies.

**Dave Jones:** Right. This is using a transformer which means that the transformer's engaged and the the power supplies on the output of that are engaged. So, this is actually there's a limit to how low we can get this, but with the the the little supply, the brick switching supplies, they actually are designed for consumer products.

**Dave Jones:** So, they can often spec that they go less than a watt when they're in standby. Um and then then they have a small power supply that comes out that keeps a little bit of circuitry alive.

**Dave Jones:** No different than your TV. has just a small amount of circuitry. That's for the infrared to for the infrared to detect you want to turn it on, you know.

**Dave Jones:** Yeah. So, that that architecture is slowly seeping into our products to minimize the power. And you can get those down to like very very low, like 100 mW or something like Right.

**Dave Jones:** that. Fantastic. Yeah. The that one button is separate from all the other buttons, basically. The speaking of the competitors, yes, like especially in the power supply market, I mean, it's a ridiculous what you can get for like on E- you know, you can get a bench power supply for 50 bucks on eBay, including delivery, probably.

**Dave Jones:** Right? No, maybe not. Consider it's still a bit heavy unless it's a switch mode. Right. But it's it's just crazy. Are you like at what price point at what price point of instruments will you not go at?

**Dave Jones:** Is there a price point where you'll go, "Look, we won't bother."? Today, there's probably a price point that's 500 something like that. Right. You see the new scopes start at 500.

**Dave Jones:** Um but that's just a temporary situation. Our long-term goal is Long-term goal is to go lower? Go where we need to go to be effective. Interesting. If someone makes something that we don't think customers should have on their bench cuz it's going to cause more problems than it's worth, Right.

**Dave Jones:** we won't go there, obviously. Just cuz someone else makes it doesn't mean we want to put that product out. So, that $25 product may be fine if you're powering up a a non-electronic load, for example, but it's going to have tons of ripple.

**Dave Jones:** It's going to be slow. It's it's not going to necessarily be reliable. It's not going to be easy to use. You know, we're never going to make that product, to be honest with you.

**Dave Jones:** But, there's there's no reason we can't do a $500 product, as evidenced by the oscilloscope. We can We can address those spaces. Right. And in power, um and everywhere.

**Dave Jones:** It takes time for us to turn our organization around to really get the efficiencies and the infrastructure we need to be effective, but we're on a path to do it.

**Dave Jones:** Awesome. Is there enough margin still at that low end? There is. To make it or do you have to make it up in volume? Like, it's a Well, you obviously volumes Volumes are the point of Volume makes a big difference.

**Dave Jones:** Common design, common parts, and excellent engineering. Got it. It really requires some of the best engineering. It's actually, to me, just like you're doing a 6 1/2 or even an 8 1/2 digital DMM requires some of the best engineering in the world.

**Dave Jones:** Low-cost product design is an art unto itself. Component obsolescence. Big pain in the butt. Big issue. butt. It's total wasted effort. You know, you already got a design that works, you can ship it, and you got to spend money to make it continue to ship.

**Dave Jones:** And the problem is anything you change in that digital domain, you have to repeat all the testing, all the environmental testing, RFI, ESD, ESD. the new chip could be sensitive when the old chip wasn't.

**Dave Jones:** Of course. That stuff costs big bucks. And strangely enough, you may have tested it last time and gotten lucky. Right. know, and then you test it the second time and had nothing to do with the change you made to it.

**Dave Jones:** Yes. last time maybe they changed the test set up slightly or the you the units you tested last time were a little less sensitive, and you fail and had nothing.

**Dave Jones:** So, you end up fixing it something it wasn't what you started out to do. Wow. Most most common parts that go obsolete. ROM and RAM. ROM and RAM. By far.

**Dave Jones:** Because DDR has registers that you've got to write specific DDR has registers you have to configure, so you have to change the code sometimes to change the DDR. Like, yeah, cuz I would have thought, oh, it's just pin compatible, right?

**Dave Jones:** They're so jelly bean. Sometimes it is, but you still have to do all the testing. Um and then sometimes it isn't, and you have to change the configuration for the DDR.

**Dave Jones:** That's one of the ones we run into. The The other big one that's been a big headache recently was um and I think it's more of a glitch in time was FPGAs.

**Dave Jones:** Right. Yeah. One of the two big FPGA vendors moved their foundry Mhm. from one company in Taiwan to another company in Taiwan because the first company I guess wasn't working for them very well.

**Dave Jones:** Wasn't on the latest and greatest technology. And they decided they didn't want to build anything at the old company. So they started obsoleting a lot of the parts that we were making in the old company.

**Dave Jones:** Well, it's extremely painful to change FPGAs. They're not Absolutely not. Um the older FPGAs weren't done with full HDL. They were schematic Schematic based. And the new tools don't want that.

**Dave Jones:** They don't accept the schematics. And the documentation on an FPGA is never good enough that you can just hand it to someone else. You get the original engineer involved if they're still around.

**Dave Jones:** And it's just We've spent a lot of money and time doing it. We're getting good at it, but it's never fun. Do you have to get I've worked in uh in industry where we have to get like a guaranteed written guarantee signed by the CEO that they will keep this part alive for a 10, 15, 20 years.

**Dave Jones:** We don't do that. We buy large So when they tell us they're obsolete, oh, okay. Do a last buy. We do a bridge buy. The problem is our products, you know, the test and measurement industry and and power supplies in particular have the longest product lives.

**Dave Jones:** Yep. Yeah, of course. Yeah. 20, 30 years. It's right. Yeah. Now, the newer product families for this particular FPGA vendor since they've moved to the new foundry, they're moving out the deliver the lifetime date they're going to make them for because it's working very well for them and they're not trying to get out of it.

**Dave Jones:** But you know, once bitten, twice shy. Yeah. So we're we're taking a more full documentation approach. We're doing more training so people can take over and move move the design more easily in the future.

**Dave Jones:** Moving completely away from schematic based designs as much as possible to full full HDL which recompiles in any of the tools. Right. So that's going to help us, but hopefully this was a one-time glitch.

**Dave Jones:** The analog stuff, there's been some interesting parts that have gone away, especially in like power supply control, you know, regulators and stuff like that have gone away because companies do it for consumer products like you know, they've done a really high volume part for a consumer product and then they make a better product.

**Dave Jones:** They don't sell any more of the old ones. They don't want to make it anymore. We designed it in foolishly and then we have to fix it. Those are not as big of an issue.

**Dave Jones:** We still have to retest the whole product. You know, and it's a bit of a pain and it of course it's bad if they're bigger but most of the time the switching chips are smaller the next time.

**Dave Jones:** So it's easier and they're more efficient and they work better and So there's advantages to do it sometimes you go through the pain of an advantage doing it in the sense that the product shipping the way it was.

**Dave Jones:** We didn't need to change it. Now we have to spend money and time. So the fact that it's a little bit smaller, well the space was there for the bigger part.

**Dave Jones:** It doesn't help us. Right. Certainly in a new design we'll move to the newer chip but we were forced to get rid of it in the old design. It kind of stinks frankly.

**Dave Jones:** It's And it's a problem that's never going to go away. Really? Is it? goes away by doing more modularization. Okay. And when you do modularization and you put things in the right groupings, we've made some relatively foolish mistakes in some of our products.

**Dave Jones:** We grouped things that shouldn't have been grouped together. So for example, this product was a good example. This product the A2Ds and the the A's are on the same board with the power supply.

**Dave Jones:** Mhm. So that means we have five different versions of this board. So when that A2D changes we have Right. We got to we have to build a couple. Yeah.

**Dave Jones:** So we've done in the newer products is all the digital control is on a little plug-in board the size of a memory module and that snaps in and then we actually use that to upgrade the performance of the product.

**Dave Jones:** We have different versions but also when that part goes obsolete that board is common to all the family. Got it. Okay? And that's helping us so we only have to do it once and then we just pop it in and do the retest.

**Dave Jones:** So making some smart decision about partitioning helps the the part obsolescence quite a bit but sometimes it's just bad. That's
