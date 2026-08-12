---
video_id: mN4obUsJXVY
title: EEVblog 1539 - NEW PROJECT Part 3 - STM32L vs PIC24F
url: https://www.youtube.com/watch?v=mN4obUsJXVY
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 30, "3": 41, "4": 52, "5": 69, "6": 78, "7": 91, "8": 105, "9": 117, "10": 130, "11": 154, "12": 174, "13": 190, "14": 206, "15": 216, "16": 232, "17": 247, "18": 259, "19": 276, "20": 289, "21": 298, "22": 312, "23": 328, "24": 345, "25": 362, "26": 373, "27": 397, "28": 423, "29": 435, "30": 456, "31": 470, "32": 479, "33": 487, "34": 501, "35": 517, "36": 530, "37": 542, "38": 553, "39": 565, "40": 585, "41": 598, "42": 608, "43": 619, "44": 629, "45": 647, "46": 660, "47": 668, "48": 680, "49": 689, "50": 701, "51": 714, "52": 728, "53": 738, "54": 749, "55": 769, "56": 782, "57": 799, "58": 822, "59": 832, "60": 846, "61": 861, "62": 879, "63": 894, "64": 911, "65": 919, "66": 931, "67": 956, "68": 968, "69": 984, "70": 994, "71": 1004, "72": 1025, "73": 1052, "74": 1073, "75": 1101, "76": 1124, "77": 1144, "78": 1156, "79": 1169, "80": 1180, "81": 1193, "82": 1207, "83": 1216, "84": 1231, "85": 1242, "86": 1252, "87": 1264, "88": 1280, "89": 1291, "90": 1300, "91": 1313, "92": 1326, "93": 1339, "94": 1348, "95": 1356, "96": 1367, "97": 1379, "98": 1393, "99": 1412, "100": 1423, "101": 1432, "102": 1441, "103": 1452, "104": 1462, "105": 1476, "106": 1490, "107": 1501, "108": 1514, "109": 1527, "110": 1544, "111": 1559, "112": 1577, "113": 1601, "114": 1608, "115": 1622, "116": 1644, "117": 1659, "118": 1673, "119": 1681, "120": 1693, "121": 1704, "122": 1711, "123": 1719, "124": 1732}
---

**Dave Jones:** Hi, yes, I called it the ST fan boys have come out of the woodwork and they said in my previous video, part two of my new project series that I'm doing here is that I chose the wrong microcontroller because I I stopped when I Look, there are dozens of different types of microcontrollers that can do this application.

**Dave Jones:** I'm sure of it. And what are you going to go through every single one? Sometimes you've just got to stop, pick one, run with it because it suits your application.

**Dave Jones:** But, it's interesting to compare microcontrollers. You can do it until the cows come home. So, let's actually do it. Yes, the STM fan boys, they're as rabid as the Apple fan boys.

**Dave Jones:** They've all come out of the woodwork and they've said, "No, I chose the wrong microcontroller. We should be using the the ST STM32L0 series because they're lower power. Didn't you know?" Okay.

**Dave Jones:** Yes, I'm pretty sure they are, but that's not the only part of the equation. I'm actually very well aware of the STM 32L series because I actually specified the STM32L1 series, not the L0, the L1 series, into the 121GW moldimeter.

**Dave Jones:** Pretty powerful. It was relatively cheap at the time and and available at the time. We'll get into that. Um and I had the you know, the LCD driver signals.

**Dave Jones:** It was pretty low power and you know, all that sort of stuff. So, yeah, I'm very familiar with that. So, let's do a quick comparison here between the STM32L0 and the PIC24FJ128.

**Dave Jones:** It's not going to be hugely in-depth because if you're want to go down the rabbit hole, you might not even be able to get the power consumption figures from the data sheet because it depends on all the peripherals that you're using, you're driving the LCD, what's your type of LCD like, how are you driving it, all that sort of stuff.

**Dave Jones:** So, you might find, yeah, that the on paper one micro might be lower power than the other, but when you actually use it in your application, the only way to tell is to actually build it up and measure it.

**Dave Jones:** So, let's have a squeeze here at the 32 L0 ultra-low power MCUs. Now, they're going to be lower power cuz they're using a better process mode than the older PIC24F series.

**Dave Jones:** So, you know, you can normally get a lower power. They they claim to be the world's lowest power consumption at 125° C. And that's another trap for young players is that on the top-level better spec for the power consumption, you know, the micro amps per megahertz figure might be lower, but then you might use your application in a you know, it's working in a 50° C environment or something like that or

**Dave Jones:** even 125° for example, and yeah, it's not the same power consumption. It can radically go up with temperature. So, yeah, you got to be careful with that. Once again, that's something that you may not actually get from the data sheets and you may actually if you're really critical about your power consumption, you may actually have to build it up and test it.

**Dave Jones:** Current consumption reference values, dynamic run mode down to 49 microamps per megahertz. And right off the bat, I know that that's actually lower power than the 24F series. We're going to have a look at that in a minute, but that's with an external DC-to-DC converter.

**Dave Jones:** Whereas the actual figure if you use the internal LDO cuz I believe this has an internal LDO in it, it's 76 microamps per megahertz. As a comparison, the PIC24FGA family here, once again, this is not in the data sheet.

**Dave Jones:** This is just like a top-level family spec. Run current down to 150 microamps per megahertz. So, we're basically talking double the power consumption. And that sounds pretty horrible, right?

**Dave Jones:** You go, "Well, of course, that's the wrong choice, right? The 24F series, why would you use that when this bad boy here is is half the power consumption in run mode in at one at a 1 megahertz reference value, which might be a frequency that I'd be using my particular project at.

**Dave Jones:** Well, it's horses for courses. Now, there's a couple of things you need to consider when you're talking about and analyzing battery power consumption for a your product design like this.

**Dave Jones:** A, the first thing is is how often does it run in that say for example that 1 MHz mode. My particular product, it's probably going to be spend most of its time sleeping and just updating a clock display.

**Dave Jones:** You Most of the time, you could say 99% of the time, for example, it's not actually operating at that 1 MHz figure. The fact that the PIC 24F was double the power consumption of the STM 32 one really doesn't make a difference.

**Dave Jones:** And the next thing to consider is what type of batteries you're using. My product might use for example, haven't finalized it yet, but might use a couple of double A batteries for example.

**Dave Jones:** Let's run the numbers. Let's get the confuser out here. Even at 25 mA discharge, you would still get like 3,000, you know, approaching 3,000. You can see that on the graph here.

**Dave Jones:** This is actually a good graph to look. It's got the mA hour capacity here versus the drain current. And of course, we're operating down because we're using a segmented LCD and you know, it's drawing that all, right?

**Dave Jones:** Sniff of an oily rag stuff. We're almost approaching 3,000, but let's call it 2,500 mA hours. So, even if we were running this thing continuously 24/7 365 days a year at that full operating frequency, which we're not, but let's just take that as a worst case.

**Dave Jones:** Well, 2.5 amp hours, okay, divided by 150 microamps, that gives us 16,666 hours divided by 24 hours in a day divided by 365 days in a year is 1.9 years.

**Dave Jones:** Okay, so we are approaching two-year battery life in our product from a couple of double A's even when it's running at slam full 1 MHz, right? Processing 24/7/365, which it's not, but even if it was, right?

**Dave Jones:** You're still talking two years battery life. And that might be fine. So, you can see why for a particular application, in this particular one, it doesn't matter that this thing is like half the power consumption.

**Dave Jones:** Okay? You might get four years Okay, and it might be better, all right? And that might make a difference. Okay, if you're powering it from like a CR2032 coin cell or something, you know, yeah, okay, you need to start, you know, considering this sort of stuff, but really it's, you know, the fact that it's half the power consumption sounds fantastic, but really it's not a reason that you go, "Oh, I

**Dave Jones:** must use the STM32 over the PIC because it's half the power consumption." It It just doesn't really matter in this particular case. So, here's where we can start going down the rabbit hole, and trust me, this video would be hours and hours long if I actually went down the full rabbit hole on power consumption comparison between these two devices, and you can spend a week actually, you know, really

**Dave Jones:** comparing devices like this if you're, you know, doing like a watch product or something like that, really ultra-low power type stuff, you know, you can you really have to go down the rabbit hole here, and look, let's go into the PIC 24FJ.

**Dave Jones:** Let's actually have a look at the LCD, for example, because not only are there many different modes, both microcontrollers have many different modes, they have sleep and deep sleep, and you know, wake up, and then full run mode, and partial run modes, and all sorts of interrupt modes, all sorts of different modes, right?

**Dave Jones:** Ones where you're running your ADC, one where you're not, and you know, all sorts of things like that. But in this particular case, really all our micro is doing is when it's running, okay, it's running at say the 1 MHz frequency range.

**Dave Jones:** So we've got the knowing current for that. And then you've got the current for the LCD. So incremental current driving a segmented LCD. And you've got different modes here.

**Dave Jones:** You've got low power resistor ladder mode, you got medium power resistor ladder power high power resistor ladder mode, you know, depending on contrast and stuff that you actually want.

**Dave Jones:** So this is the incremental current above, so the delta current, that's why it's got delta LCD. So the additional current required above the operating current of the microcontroller. And then we've got typical and maximum figures here.

**Dave Jones:** And this is from 2 V to 3.6 V operation for example. And yes, the STM 1 I think goes down to 1.65 V. So if you really needed like, you know, to go down to a lower voltage, that might be a better part.

**Dave Jones:** That might be a deal breaker for you in this particular case. 2 V minimum operation is just fine. Typical figure for an LCD here though, it might be, you know, you might have the high power resistor ladder mode, you know, that could be 64 microamps.

**Dave Jones:** So it could be worst case if you're doing worst case design figures, which you know, you probably should be, right? It's 140 microamps. Once again, that'll be at like the higher temperatures.

**Dave Jones:** And they've got different figures for the 2 V and 3.3 V here. So it's going to dynamically change as your battery drops in voltage for example. There's an extra 100 microamps right there.

**Dave Jones:** Anyway, if you're talking specific devices here, we really have to use, you can see down here, we have to use the STM32L0X3 cuz the X3 is the only one that has a segmented LCD driver down here.

**Dave Jones:** We don't need much memory for example, right? Even 32K and 8K of SRAM is overkill, right? So only talking about cuz you want the cheapest uh device you can, we're only talking about these two parts down here, the LO53C6 or the LO53R6.

**Dave Jones:** So, here's our data sheet, okay? Yeah, as I said, uh 1.65 to 3.6 V uh operation, uh point, you know, 270 nA standby mode, 400 nA stop mode, uh and then then you've got the RTC as well.

**Dave Jones:** We haven't even gone into the RTC, which I'm going to have. Um and that 88 microamps per megahertz in run mode. Half uh the value of the nominal PIC.

**Dave Jones:** But, let's see if we can find uh some LCD uh consumption data, shall we? Optional LCD power supply scheme. So, yeah, it's got internal thing for a step-up uh converter and stuff like that.

**Dave Jones:** That's all cool and groovy. Supply current characteristics. We We're getting there. These things are often buried in the parameters of the data sheet. You You really got to have a look.

**Dave Jones:** Oh, hello. Right off the bat, what's going on here? Is that banner spec Can you smell some BS in the banner spec? Maybe. Look Check this out, right? Under these conditions, uh range 3 V core is 1.2 V, so that's the core voltage that it's running at.

**Dave Jones:** As I said, it's got an internal um uh low dropout regulator in there. At 1 megahertz, 165 typical microamps. What happened to the 88 or whatever we were running at?

**Dave Jones:** Supply current in run mode, code executed from flash. Once again, you've got to go into all the different modes and the clocking sources, all sorts of jazz like that.

**Dave Jones:** But, I've got a figure here of 165 microamps. That's basically the same as the as the PIC. And this one up here was flash code executed from flash. Well, wouldn't you execute your code from flash?

**Dave Jones:** Isn't that a given? Okay, and it starts to lower with the flash switched off, 135 microamps. Okay, we're still not like at the 87 88 or whatever it was.

**Dave Jones:** Okay, supply current in sleep mode, flash off, all right. Hats off to the ST data sheet here. They're they're giving you like really comprehensive figures here, but but this is in sleep mode.

**Dave Jones:** I can go into the different modes and everything, right? But but we're still talking 50 7 microamps, right? 43 microamps. This is not nanoamps, right? This is microamps in sleep mode.

**Dave Jones:** Supply current in low power run mode. This is where it's going to work. Oh, no. Okay, so that's only low power clocks. Okay, cuz it has an internal RC 32 kHz clock.

**Dave Jones:** Okay, so that's that's not our 1 MHz mode anymore, which is great if you're in clock mode or something, you know, your product shut down and you're just updating, you know, a clock display or something like that.

**Dave Jones:** Then that's that's that's fine and groovy. That's why you can get, you know, 4.7 microamps and stuff like that. Yeah, no. Where's this 88 87 microamps? Where are we seeing that?

**Dave Jones:** In the data sheet, right? Maybe I can search for 88. Can I do a control F? 88? No. No. No. No. No. So, if we go back to the pic over here, and then if you want to Once again, go down the rabbit hole, there's a little three next to that, right?

**Dave Jones:** If you go down here and have a look at three, base idle current is measured with all of these different modes, right? So, this is why I'm saying if you're really serious about this sort of stuff, and you're really comparing devices like this.

**Dave Jones:** If I was designing a professional product at a, you know, at at a professional company and you had all the money and all the time and all the resources to actually, you know, choose a proper microcontroller like this, to choose like the optimum absolute optimum part for the application, then I would be building this up.

**Dave Jones:** I'd be building building up two different, you know, I'd narrow use data sheets to narrow it down to, you you two, maybe three, you know, competing micros that I'm trying to use and then I would build up just demo boards for them and then just use that and then design onto those boards like proper little current consumption shunts and like you know, jumpers and all sorts of things that I

**Dave Jones:** can easily you know, measure the in-circuit current consumption. I do run code on both of them, right? But this takes time and effort, right? So you've got to have the time and the resources to actually do this.

**Dave Jones:** It doesn't cost much to spin up a cheap board and buy a couple of one-off parts and you know, hand assemble them, right? But you know, it's it's time and effort, but you would do that if you were genuinely trying to do a shootout between you know, a couple of different competitors.

**Dave Jones:** There's just so many variables in here. It's just it's just absolutely nuts, right? And especially when you're driving LCDs and you're using timers, you might be using ADCs, you might be using comparators and other peripherals coming out the wazoo, right?

**Dave Jones:** And and in different modes and things like that. And then yeah, you'd have to write, you know, test um, software cuz you wouldn't write the full application generally, just write some you know, test operations that drives the LCD, you know, it does your ADC thing, whatever you want to do, it does does the timer things, it does, you know, your comparator stuff and things like that.

**Dave Jones:** The things that you know, that you're operationally drawing power with, but anyway. But first thing on the table here for the PIC, I'm seeing operating current IDD, right? We're talking like max 350, typical 208 for example.

**Dave Jones:** So you know, that's actually operating at 1 MHz, okay? So that's at half half a mill mips is million instructions per second. And if you're really comparing, it's not just microamps per MHz, it's you know, how many instructions per microamp.

**Dave Jones:** It's it's great to run at 1 MHz, but if you can only process half as much as compared to the other device or whatever, then that could make a difference.

**Dave Jones:** It's how many instructions per microamps really. But once again, that's only on the processor side of things, right? When you're talking about all your sleep modes and power down modes or low power modes and stuff like that.

**Dave Jones:** Wow. I honestly could not cover it even for a relatively simple application like this which is just driving an LCD really. To do a shootout between two different devices is I did like hours, many hours worth of videos and then building up like comparison boards to actually seeing that they you know that they're not BS'ing you in the specs and they do actually perform as claimed.

**Dave Jones:** Or you simply cannot get all the information in there. Anyway, we've got like operating current, okay, which is IDD. Then we've got idle current. So it's sitting there idle.

**Dave Jones:** It's not in some power down mode, but it's but no, it says it's doing one MIPS. So once again, you'd have to go into the differences between idle mode and one MIPS at 2 MHz cuz this is lower consumption.

**Dave Jones:** Okay, you'd have to go down here and check what things are all turned on and stuff like that. This one's actually lower power consumption at twice the MIPS as this one here.

**Dave Jones:** Like, what the? And this is this is half the MIPS, half the frequency, and it's more cuz it's probably got more stuff on. Anyway, back to the SST. I'm still trying to find some LCD power consumption.

**Dave Jones:** I haven't found yet where it's getting this 88 microamp per MHz figure from. Okay, now they do have some figures for the LCD controller. They're saying the ILCD. So is there a voltage for LCD pin and that's only three typically three microamps.

**Dave Jones:** Low drive resistor network, right? There's a high drive resistor network. That's what Microchip were specifying, but that's it, right? They're not they're not telling you So going back to the microchip over here actually the microchip is lower typical right one micro amp for the low power resistor ladder 1.3 micro amps typical could be a maximum as could be as high as 12 over here we're talking about

**Dave Jones:** three micro amps but you know once again this is the Delta current on top of the operational so we we're still not sure what the operational current of the STM is over here look I'm sure a whole bunch of people are yeah I've measured that no it's in here this page of the data sheet but I'm like not readily finding stuff and it's just I LCD but anyway the

**Dave Jones:** resistor divider is like across the rail so let's say you're operating at even even the two volts right you know your battery's right down you're operating at you know the minimum battery right so two volts divided by 240k we're talking like eight an additional eight micro amps there but I don't know the microchip over here is LCD plus you know charge pump and low power resistor ladder okay 10 micro amps

**Dave Jones:** over here and then LCD high power resistor ladder it's like we have to go down the whole rabbit hole of what resistive ladder we're using what charge charge pumps we're using for the LCD what type of LCD we've got and you know the contrast that we want and all sorts of things this is why from the data sheets you would if you wanted to do a real shootout you

**Dave Jones:** as I said you'd probably got to build these things up and measure it so yeah I'm not sold on this 88 micro amps per megahertz in run mode it might be taking that from a like a higher frequency figure and dividing it or something like that because like you go in here supply current in run mode even when you're executing the code from RAM I assume how

**Dave Jones:** easy is it to copy the road from flash to RAM I don't know it might be trivial but you know if you actually even when you're executing it from RAM, I'm getting like 135 microamps at 1 MHz.

**Dave Jones:** Uh, wouldn't be the first time that a manufacturer has, you know, rubbed some snake oil on the top-level banner spec. Leave it in the comments down below. Am I missing it?

**Dave Jones:** Is it somewhere else in here? In run mode, code with data processing running from RAM. And if it's running from flash, it's like it's on par with the with the PIC or even potentially worse.

**Dave Jones:** So, anyway, as I said, huge absolute huge rabbit hole, many many hours of videos just to do that. Um, and many many weeks of work if you wanted to actually build up to and compare it.

**Dave Jones:** But, of course, one of the things with the STM that they're infamous for, the chipageddon, the component supply crisis. Everyone's projects stopped cuz they couldn't get STM um micros, right?

**Dave Jones:** They built a STM It was the flavor of the month. Everyone was going giddy over the STM micros. And then, the component supply crisis happened and you couldn't get them, right?

**Dave Jones:** So, that whereas you could still get a lot of the Microchip parts, they weren't hit nearly as hard as uh the STM ones on where I've heard of people who simply folded their business because they built their little hobby business around the product.

**Dave Jones:** They were using STM micro in it and they just couldn't get it and they went, "This is ridiculous. It's years lead time." Right? I've I've did the They they they just shut up shop, right?

**Dave Jones:** Cuz they couldn't get these parts. So, let's get these two different parts, the C6 R6 here, okay? Quantity, uh their prices are pretty much on par between uh the PIC and the STM here.

**Dave Jones:** So, really, it's not There's really no no difference in the price. They're They're two They're two bucks something um in quantity volume. But, look, stock, zero zero zero. Oh, 180.

**Dave Jones:** They've They've got 180 in a tray. 26,400. There you go. So, the future electronics have 26,000, but in trays, once again, like you might prefer them in reels. Right?

**Dave Jones:** And $2.96, so you're actually paying a premium for that. By the looks of it, that's 160 quantity. Looks like you have to pay that minimum. Looks like you may I don't know.

**Dave Jones:** You might get a little bit of a discount for higher quantity on that. Zero zero zero 1900. Right? It's not looking good. Yeah, Aimings holding, so that's some weirdo distributor.

**Dave Jones:** Comsit. Never heard of them. Right? So, there's 29,000 somewhere in Europe, maybe. But yeah, nah. Right? It's It's not a good vibe. Let's Let's try this other part. Stock zero.

**Dave Jones:** Right? So, we're talking Arrow. They're one practically one of the biggest providers. Digi-Key, okay, they have 2600 in stock, but you might get a Oh, there we go. If you got to got to buy 2500.

**Dave Jones:** So, if you bought all of them, you know, you're paying almost three bucks a a part there. Um but zero zero stock zero. Okay, 1400. Right? So, okay, you might be able to get your first run.

**Dave Jones:** Buy the parts before you design the PCB. Just buy the parts. Have them in stock. You know, take that financial risk. Buy them now so that you're guaranteed to have them.

**Dave Jones:** But yeah, not that terrific, is it? So, we can order direct here. Okay? And we can go over to here. Here's the part. All they tell you is that it's in stock.

**Dave Jones:** There's no quantity. Right? Yeah, they've got it in stock. Trust us. Try and order 10,000 of them. But if you compare that to the Microchip part, Digi-Key have 11,000 in stock over here.

**Dave Jones:** Okay? So, that's that's pretty schmick. Yeah, 12,000 is a better vibe. And just based on the history, I would trust being able to get Microchip parts better than I'd trust trying to get the ST parts.

**Dave Jones:** Now, as for the other major requirement in my product was the 32-bit timer here. And this one, it does actually have the ST has actually 9 * 1 16-bit with up to four channels, two 16-bit with up to two channels.

**Dave Jones:** So, somebody said you can actually cascade them internally, and I will believe that. But once again, you'd have to check specifics. But of course, one of the cool things about the Microchip is it had core independent animation of the LCD.

**Dave Jones:** So, you could do autonomous blinking of displays like this. You could do alternating complete alternating displays. Animation happens in low power mode, for example. Can you get the same sort of thing?

**Dave Jones:** Once again, you'd have to build these up, and you'd have to actually measure them. Spend a month of design effort just really comparing, you know, even just two micros, let alone more.

**Dave Jones:** So, does the STM have that? I do believe it has like blinking. Yeah, here it is here. It says it supports blinking mode. Whatever that means. But is that core independent?

**Dave Jones:** Does it operate in low power mode? Can you is it is it just flash a thing off and on, or can you do like complete LCD swaps like you can on the Microchip one?

**Dave Jones:** That could be your decision made right there, because you wanted all that animation capability that the Microchip offered, for example. So, there you go. Up to eight pixels can be programmed to blink.

**Dave Jones:** That's it. So, it can't do the full swap. So, it looks like that would be Yeah, blinking would be core independent. So, I guess you could set the blink rate, maybe, and at which and but you can only blink eight pixels, eight segments.

**Dave Jones:** So, yeah, the Microchip wins there, hands down. So, anyway, this video's been long enough. That's a a brief comparison between the STM32L. This is just top top level me off the cuff.

**Dave Jones:** Like I didn't, you know, plan it. I just just pressed record. Once again, if I wanted to do a huge detailed comparison, it would take me days and days of work to actually uh you know, truly go in there.

**Dave Jones:** That's just the data sheets, let alone, you know, building things up. So, yeah, even that like banner spec down here, 88 microamps per megahertz, okay. STM's half the power consumption of the of the PIC.

**Dave Jones:** Well, is it? Doesn't seem to be that clear-cut. So, you can't clearly say you can't confidently say that oh, yeah, yeah, this this part is absolutely the choice over the PIC here.

**Dave Jones:** You just you can't say it. I would just run with the PIC because it's not that hugely critical. As you saw with, you know, the AA, if you power it from AA batteries or something, it it it doesn't really matter much of a rat's ass, really.

**Dave Jones:** But, you know, you just want something moderately low power, you want something that handles the LCDs, that animation thing that was really cool, right? That the PIC can do, and it's it's good enough, and there might be some other, once again, lower power than the STM one again in certain modes.

**Dave Jones:** And, well, you have to go through the whole process for different manufacturers. And, some people talked about the PSoC parts, for example, which have the which have some like hardware routing you know, digital logic blocks built in and stuff like that.

**Dave Jones:** That's that's kind of cool, but there's another whole comparison video. And, and you go down the rabbit hole. Oh god. If you're not used to going down the design rabbit hole on stuff like this in that I cover in like a 20-30 minute video here, it can takes days, weeks, even months to do a real detailed comparison of parts for depends on your application.

**Dave Jones:** Some applications doesn't matter, so you can just use the same micro again and again and again, and there's a lot to be said for that, right? I'm familiar with the PICs, I like the PICs, they've been available for me.

**Dave Jones:** They've they've done me well over decades, right? So, you know, I'm naturally um you know, went for Microchip. But then, the 121 GW actually I'll link in my uh design uh video.

**Dave Jones:** I Well, no, no, it's like a historical video of the of the development of this thing. This actually did use originally used a PIC um micro in it and I specified a PIC micro, but then we desired decided later to actually switch to an ARM micro cuz the company um who designed it, they were you know, wanted to sort of like switch to ARM for other, you know, operating

**Dave Jones:** you know, company reasons and stuff like that. So, I specified in that um STML1 series into there. They were going to use another part that didn't have built-in LCD, but I I specifically found an and a uh suitable L1 uh part and that's been really good.

**Dave Jones:** 32 and I didn't actually program that low-level uh myself. So, you know, whereas the microchips, I have. So, I'm familiar with them. I'm confident with them. So, yeah. So, sorry all you STM um fanboys, um I have not uh changed my mind.

**Dave Jones:** I think I'll still run with the PIC 24 um well, a variant. I think this is the variant I'll probably run with that, but I'll I'll do a double-check.

**Dave Jones:** But, yeah, nah, I it has not changed my mind. The fact that it might be lower power, whoop-de-doo. Um it's the proof's in the pudding when you actually build it up.

**Dave Jones:** So, yeah, and a lot of people have been bitten and refused to use ST um again because they've been bitten by the supply uh crisis. Anyway, that's enough waffle.

**Dave Jones:** Found the video interesting, give it a big thumbs up. And if you like this uh design series even though you don't really know what I'm designing, just I just randomly press, let me know.

**Dave Jones:** Leave it in the comments, please, cuz I know these videos don't get a lot of views. Um so, you could argue that, you know, they're not good for the channel.

**Dave Jones:** the channel down a bit when I do videos like this. But if you do like it, please engage, thumbs up, all that sort of stuff, and uh leave it in the comments to encourage me to do future design videos like this.

**Dave Jones:** Catch you next time.
