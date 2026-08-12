---
video_id: Z-m-7jex88k
title: EEVblog #789 - Batteriser Monkey BUSTED!
url: https://www.youtube.com/watch?v=Z-m-7jex88k
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 21, "3": 29, "4": 44, "5": 54, "6": 70, "7": 80, "8": 95, "9": 108, "10": 123, "11": 136, "12": 152, "13": 175, "14": 188, "15": 197, "16": 219, "17": 235, "18": 254, "19": 265, "20": 275, "21": 299, "22": 306, "23": 323, "24": 347, "25": 364, "26": 376, "27": 394, "28": 408, "29": 427, "30": 454, "31": 464, "32": 477, "33": 495, "34": 511, "35": 533, "36": 556, "37": 566, "38": 592, "39": 605, "40": 620, "41": 631, "42": 646, "43": 658, "44": 674, "45": 687, "46": 709, "47": 716, "48": 728, "49": 737, "50": 748, "51": 758, "52": 775, "53": 786, "54": 802, "55": 812, "56": 820, "57": 835, "58": 844, "59": 861, "60": 882, "61": 889, "62": 901, "63": 921, "64": 929, "65": 949, "66": 969, "67": 980, "68": 992, "69": 1008, "70": 1019, "71": 1034, "72": 1050, "73": 1063, "74": 1075, "75": 1085, "76": 1100, "77": 1111, "78": 1125, "79": 1134, "80": 1151, "81": 1167, "82": 1186, "83": 1200, "84": 1216, "85": 1226, "86": 1242, "87": 1247, "88": 1258, "89": 1269, "90": 1288, "91": 1314, "92": 1327, "93": 1341, "94": 1357, "95": 1368, "96": 1389, "97": 1399, "98": 1416, "99": 1435, "100": 1447, "101": 1462, "102": 1479, "103": 1491, "104": 1503, "105": 1513, "106": 1523, "107": 1535}
---

**Dave Jones:** Hi, just a quick follow up video to my previous video which is a response to the Batteriser monkey video where they tried to explain why power supplies are different to batteries.

**Dave Jones:** And it's actually quite a misleading video and I went in detail and explained why they didn't actually measure it correctly and all sorts of stuff. So click here if you haven't seen that.

**Dave Jones:** I just wanted to do another quick follow up video because one of my viewers, Andrew, sent in the real monkey. It's the same one that Batteriser used in their video.

**Dave Jones:** Thank you very much, Andrew. So I wanted to repeat their test where they showed the monkey working down to 2 volts on a power supply and why it didn't work with batteries measuring 1.25 volts per battery open circuit.

**Dave Jones:** Thought we'd reproduce it and see what we get. The answer's pretty obvious to anyone who knows about batteries. Let's go. Oh, by the way, this is Probes, the monkey.

**Dave Jones:** So we'll call him Probes, too. Let's say Probes. So my test setup is very similar to before. I've got a BK Precision 8500 electronic load. I've got AA battery holder this time and I've got big high current leads leading to there.

**Dave Jones:** Not that that matters cuz this time I've actually got this extra sense wire tapped off here going around to the back of the BK Precision load. That's the sense input.

**Dave Jones:** So we're actually compensating for any loss whatsoever in any of those leads and that's soldered directly onto the contact points here. The contact points also go in over to the Keysight 34470A so we can actually log the discharge curve.

**Dave Jones:** Now this What I didn't show last time is that the BK Precision 8500 electronic load actually has a battery test mode. If I actually go in there, shift battery, for example, I can go up.

**Dave Jones:** There we go. I can actually set a minimum voltage here of what I want this thing to cut out at. So I can set my constant current load so it'll just continue to do a draw constant current from the battery until it hits whatever voltage we specify here, and then it'll automatically cut out.

**Dave Jones:** So, the plan is to discharge two brand new batteries two until they get to about 1.25 volts open circuit voltage, even though that's the wrong way to measure it, and there's lots of traps in doing that.

**Dave Jones:** This is exactly what Battery Riser did in this video. So, we were I'll actually drain these things down using about half an amp, which is roughly what the monkey here, we'll call him probes, probes the monkey, what he actually takes, you know, roughly on average.

**Dave Jones:** Okay, what I've done with this first battery here is I've discharged it to 1 volt at half an amp. So, it but it recovered to 1.38 volts. I wasn't sure what because you're never sure what voltage is actually going to recover to cuz that's due to the ionic resistance of the battery battery, which is extremely dynamic, has to do with all sorts of factors.

**Dave Jones:** So, yeah, I discharged it to 1 volt from fresh in the pack, and well, we only got to 1.38 recovered. And we actually extracted almost 1 amp hour. You'll notice I just turned this back on.

**Dave Jones:** It's not in battery mode again. Once again, we're still drawing half an amp constant current, and it was 1.38. I just switched it on then, and it's slowly it's very quickly dropping.

**Dave Jones:** So, it doesn't immediately drop back to 1 volt. As I said, that ionic resistance of the battery extremely dynamic chemistry at play inside this thing. But as you can see, it'll should very quickly in the scheme of things cuz it actually took like a 3 hours to discharge this thing or whatever to a volt or 2 and 1/2 to 3 hours.

**Dave Jones:** So, it's going to it should get back down to 1 volt pretty quickly. So, what I'll do is I'll discharge it down to 0.9 volts, and you know, see if we can get around about that 1.25 volt open circuit voltage, even though the open circuit voltage is not the right way to do it.

**Dave Jones:** Hey, we want to reproduce what Batteriser did. And bingo, it's just finished discharging to 0.9 V and we sucked out an extra 0.44 amp hours. There we go. From going from 1 V turned down to 0.9 V cut off after that constant discharge curve.

**Dave Jones:** And you can see it's jumped right back up to 1.2 V. And this second battery is finished and that took about 2 and 1/2 hours I think or thereabouts and it's jumped back up to 1.2 V.

**Dave Jones:** Actually, I'm not really happy with that at all. As you can see they're recovering to 1.32 V. I think I'm going to discharge these down to 0.85 V. Let's go.

**Dave Jones:** So, shift battery 0.85 go. There we go. Okay, discharging the second battery and we're going to log that one as well to 0.85 V. And after that third discharge down to 0.85 V, we drew a total of 0.2 another 0.22 amp hours out of the thing.

**Dave Jones:** That's not too shabby. Geez, there can't be much juice left in it. Okay, discharging the second battery and we're going to log that one as well to 0.85 V.

**Dave Jones:** All right, I've now got two batteries that have been discharged three times. So, really there's hardly any juice left in these things. We've got 1.24 V there. And we've got 1.27 V there.

**Dave Jones:** So, just over 2.5 V exactly the same open circuit voltage as Batteriser used. So, let's stick them in the monkey. These are incredibly discharged batteries but I think we'll find they'll still work because they've got still some energy left.

**Dave Jones:** Just a little bit. Should be enough to operate probes the monkey. Let's have a look. Here we go. No problems at all. They work just fine and dandy. Why is it so?

**Dave Jones:** Watch. I'm pushing that finger. I'm pushing it. I'm Did you see, Mr. Clark, that the stick did not tip? So, I call your attention to the title of all my shows.

**Dave Jones:** Why is it so? Why is it so? There you go. So, why did the monkey under test work with my batteries at 1. 25 V each or a total voltage of 2.5 V open circuit just like Batteriser's ones?

**Dave Jones:** It's very simple. It's the internal resistance of the battery. Everyone knows about this. It is a hobby level stuff. As I've explained, my batteries, even though I brutally discharged them here, you get three discharge curves.

**Dave Jones:** Most of the energy is gone. There's still enough energy left in there to operate this monkey. No problems at all. So, the batteries that Batteriser used, even though they measured exactly the same open circuit as the batteries I used here, their ones were There was no energy left in them.

**Dave Jones:** They must have discharged them down to bloody bugger all. No wonder it didn't work. And ironically, this test, the test that they used in their video for this monkey to prove that batteries are different to power supplies, as if anyone didn't know about internal resistance, ironically, the monkey is actually a very poor choice because this thing can extract virtually all the energy out of the batteries.

**Dave Jones:** It doesn't need the Batteriser. And the reason why they didn't actually put the bat- the dead batteries on the batterizer and put them in the monkey because it wouldn't have worked.

**Dave Jones:** It doesn't matter how magic your boost converter is, they're not going to work cuz there was no energy left in the batteries. Ah! Goodness! How embarrassing! How could they put out a video like that?

**Dave Jones:** It's incredible. So, this is why the batterizer monkey video is not only wrong, but it's misleading because it's making out that the open circuit voltage of the battery uh showing that their 1.2 volts per cell implies that there's actually energy left in the battery.

**Dave Jones:** When in their case, there is not. There is clearly no energy left in the battery. That's why people do not measure the open circuit voltage of the battery. It doesn't happen in industry cuz it's a very extremely poor indicator of whether or not there's energy left in this battery.

**Dave Jones:** Even batterizer's own video showed that this monkey works down to 0.5 volts per cell. It use it extracts almost every drop of energy from the batteries. But with a power supply, the monkey will operate even when we bring the voltage down all the way to 0.9 volts.

**Dave Jones:** However, when using two batteries with a total voltage of 2.5 volts, the monkey will not operate. Of course the monkey won't operate because those batteries aren't 1.25 volts per cell when you stick them back up the monkey's butt because you didn't do what I tried to explain in the previous video that you must probe right here.

**Dave Jones:** And that is why using a power supply is exactly the same as using batteries when you actually measure the voltage where you should, which is right up the monkey's butt.

**Dave Jones:** And that's the trick which batterizer don't seem to understand is that one battery that measures 1.25 volts and another one that measures the same 1.25 volts open circuit when you actually put them in a product one cannot work at all because it just plummets because of the internal resistance, the chemistry, there's no energy left in the battery, but the other battery that measures exactly the same open circuit may still have some

**Dave Jones:** energy left in it due to how it was discharged and all sorts of complex, you know, factors involved in the battery. The open circuit voltage doesn't tell you that.

**Dave Jones:** Everyone knows this except Energizer. So, my batteries at 1.25 volts open circuit still had a little bit, not much, but a little bit of energy enough to make this monkey work cuz this monkey extracts practically all the energy from the battery.

**Dave Jones:** So, the batteries they used clearly had zero energy left because batteries can recover to a higher terminal voltage. That's how ionic resistance and the chemistry inside a battery works.

**Dave Jones:** That's why you never ever measure the open circuit voltage. And here's an example of this in a previous video you saw that I very slowly discharged at a constant power a couple of AAA batteries.

**Dave Jones:** This one was discharged at 100 mW continuous and I have to do a follow-up video showing the data for this and this one was but here's a quick look at the data.

**Dave Jones:** This one was discharged at 50 mW and this one here was discharged at 20 mW, okay? So, let's have a look at the voltage left in these batteries open circuit with no load 1.2 volts.

**Dave Jones:** 1.15 volts. I discharged these things right down to zero and they even oscillated down around zero. I left them there in continuous, you know, practically shorting the things and they still recovered to 1.2 volts.

**Dave Jones:** That's what these the battery chemistry can do, but it doesn't mean there's much if any energy left in these. There is actually some due to the ionic resistance and the chemistry is a tiny little bit, maybe 1% of the energy still left to these discharged completely discharged batteries.

**Dave Jones:** It could be less than 1%, so it might operate, you know, something a low power device for another hour or something like that. And that's what you can do, of course.

**Dave Jones:** You can stick these batteries into some low power device like this, for example, and it will still operate. So, here we go. We'll measure that, 1.15 volts. There it is.

**Dave Jones:** We'll stick it in here and we'll find that this thing will still work. It's a, you know, it's pretty dim, okay, but it still works. There's still a tiny amount of energy left in there.

**Dave Jones:** And now let's measure the voltage in there. There we go. It's because this thing takes, you know, absolutely nothing at all, really, except maybe when it beeps. There we go.

**Dave Jones:** Just see it drop when it beeped. So, look, you can even still put them in something like this multimeter and it will still work. Look at that. It's not even showing low battery.

**Dave Jones:** That's because it hasn't dropped to low enough voltage yet. Look, it's still There you go, 2.32, okay? It'll even have just enough energy left to still operate the backlight like that, okay?

**Dave Jones:** However, you know, it might be running at 5 milliamps or something, which is not much power at all. But if you measure the voltage in there, you'll see it, it's dropping and it's going to continue to drop and it's going to drop off pretty quickly.

**Dave Jones:** There's, you know, you might get another half an hour's use out of this multimeter out of the 300 odd hours that it normally operates. And no, don't jump to all the excitement that aha, that's a usage case for the batterizer.

**Dave Jones:** Well, yeah, okay, it is, right? If your product doesn't extract all the uh or most of the energy from the battery, but it's how much do you get out of it?

**Dave Jones:** An extra couple of percent. And when you slap on the boost converter on this thing, it's going to be draining a lot more current than if you just put them in here like this.

**Dave Jones:** Cuz you've not only got the efficiency of the converter, but you've also got the increased current of the product because it's operating at 1.5 uh volts per cell instead of, you know, down around 1 volt per cell or whatever these happen to be at the times.

**Dave Jones:** So, just be very careful when you get all excited about a boost converter like the Batteriser. It's not magic. It's all to do with the amount of energy left in the bas- battery.

**Dave Jones:** Physics 101. And this other battery I discharged at 20 millivolts. What happened to it? Well, let's take a look here. 1.11 volts. Why is it so? Take a look at it.

**Dave Jones:** It has leaked. Look. This is what can happen if you don't get the batteries out quick enough and you continue to drain them right down to zero. I must have I might have left this one in for an extra, you know, couple of hours or a day or something like that um to when compared to the other ones and it leaked.

**Dave Jones:** And this is one of these Duracell Duralock ones that is a not supposed to leak. They're supposed to have, you know, 10-year life and blah blah blah. There we go.

**Dave Jones:** I've got all that I've got a bloody leak. Unbelievable. Well, that's the danger of discharging batteries right down to zero and not getting them out quick enough. So, here's the discharge curve that I actually got from this thing.

**Dave Jones:** And you can see that I did three discharges here from here to this point where then it recovered and then as part of the ionic resistance of the battery, it recovers very quickly and then it tapers off like that and slowly if you keep going it actually recovers, you know, probably up to 1.4 volts eventually or maybe just a little bit under.

**Dave Jones:** And then I started the discharge again, and then, right, it jumps down straight away, but due to the ionic resistance of the battery, it starts to slowly discharge like that.

**Dave Jones:** It doesn't drop back to exactly this point because it's the dynamic electrochemistry of the battery, okay? You're not gaining any extra energy by doing that. The battery only has a fixed amount of energy in it, but the that's that's why the voltage really is not telling the whole story there.

**Dave Jones:** So, it gets down and down. So, we extracted some more energy from here, and we turned it off, and then we extracted some more energy. Three different periods, and um the battery tester measured 0.797 amp hours, 0.44 amp hours, 0.22 amp hours for a total of about 1.63 amp hours, 1,630 milliamp hours.

**Dave Jones:** Now, just to clarify something here, amp hours or milliamp hours is not the true measure of battery capacity cuz it's not taking into account the voltage. It's not power.

**Dave Jones:** The only true measure of energy in a battery, either energy used or energy remaining in a battery, is actually in watt hours. So, that's why I've shown in previous videos how you can't just use the voltage.

**Dave Jones:** You've actually got to convert it to power, and it's the total integral under the under the power curve. So, if you do constant power discharge, you can actually just read off uh the percentage directly from the x-axis here, but we're not doing constant power discharge.

**Dave Jones:** We're doing constant current discharge. Anyway, um we've got we we extracted 1.63 amp hours out of the battery, but clearly this could these could still operate the monkey, which is a fairly high drain uh device.

**Dave Jones:** So, it still clearly had some energy left. It might have 5, I don't know, maybe even 10% left. And Duracell don't actually give you uh any data for the uh milliamp hour capacity in this case, but uh Energizer do.

**Dave Jones:** So, Energizer's um alkaline, just as an example here, um here we go, out of milliamp constant current discharge which we did on the Duracell. If you draw a line across there, it's around about 1400 milliamp hours and we extracted actually 1630 from it.

**Dave Jones:** How were we able to do that? Well, because we actually cuz this is continuous discharge, okay? Just in one cycle. We did it in multiple cycles. You allowed it to recover.

**Dave Jones:** So, we can actually get just like you get increased capacity at lower currents, so lower average currents like this. So, you don't necessarily have to discharge it at a lower current.

**Dave Jones:** You can still discharge it at 500 milliamps as we did here, here, and here, but because we let it rest for some time in between. This is not the true time by the way here and here.

**Dave Jones:** This is I just that's only where I stopped doing the data. So, it actually had more time to recover than that. So, the average value is going to be better than this nominal 1400 in one continuous discharge.

**Dave Jones:** Anyway, that's just a quick little look at milliamp hour discharge. But, yeah, like I said, there's probably not much left in this thing. The only way you can do it is to really time it in the monkey itself.

**Dave Jones:** And I know what you're all saying, "Dave, probe the monkey's butt." Well, here it is, the MUT, the monkey under test. I've probed in there. These big probes here go into the banana plugs which you can hook up to the battery or a power supply here.

**Dave Jones:** And then I've also got some leads. It was quite tricky, but I shoved them in the end of the probes right at the contact points right up in there.

**Dave Jones:** So, I've set the power supply to 2 volts. If I turn it on, there we go. So, 1 volt per cell, 2 volts total. As you can see, it's not dropping much at all because there's not much loss in these leads at all.

**Dave Jones:** So, still doing just fine. So, and now I'll do my two batteries and the open circuit voltage of these batteries is 2.59 volts there. Okay? So, this is going to be a little bit uh tricky.

**Dave Jones:** So, bear with me for a second. I've got to uh sort of use all of my hands. Ah, hang on. I got to use my three free hands here and and that's it.

**Dave Jones:** You can see it's dropped down to 1 volt. But, it's not There we go. 2 volts. Okay? So, it's dropped from that 2.5 down to 2 volts because, well, there's not much energy left in the battery.

**Dave Jones:** So, the ionic resistance drops that terminal voltage by a fair amount. And just like batterizer, let's wind the voltage down. Here we go. 1.7 volts. Let's take it Yeah, at a volt at a volt.

**Dave Jones:** So, that's half a volt per cell. The monkey is still working. This is an incredible probes. The monkey is absolutely amazing. But, that's yeah, he's pretty much dead there.

**Dave Jones:** The torque from the motor is just yeah, can't do it. So, that's why these ones still work because there's enough energy left it can keep the terminal voltage up above that uh 2 volts um up above well, double what is required to operate the monkey.

**Dave Jones:** So, what I'm going to do is discharge these things even more until I get to a point where they won't work in the monkey and we'll see what happens.

**Dave Jones:** Even though the terminal voltage will be high, they will drop um when you actually plug them in here, it'll just plummet and it'll go under that 1 volt. You bet your life on it.

**Dave Jones:** And discharging to 0.6 volts, we were able to jump back up to 1.11. We were able to extract another 0.31 amp hours. Beauty. All right, here we go. I've drained them a bit more and put them in here.

**Dave Jones:** There you go, 2.1 volts. Okay, so should be enough to operate Probes the monkey and I suspect we will get some juice out. Yes, I soldered some uh plugs onto there.

**Dave Jones:** Here we go. Let's have a look. Ah, just he's getting real slow. Look, 1.48. But you put any resistance on there at all and he's just gone. You're holding him maybe up like that, the torque might be a bit more and he's Ah, yeah, you can see he's virtually dead.

**Dave Jones:** Okay, just drain a little bit more charge out of him by holding that and of course the uh resistance of the motor in that nut. Look, he's gone. He's gone.

**Dave Jones:** Ah, poor Probes. Sorry, Probes. But you can see the batteries that Batteriser must have used, even though they're measuring that terminal voltage, okay? Look, we're getting getting that voltage under load, 1 volt.

**Dave Jones:** So half a volt per cell like he's dead, okay? He's gone. There was no more energy, usable energy left in those batteries. Take it off and here we go.

**Dave Jones:** It'll recover. And if you leave them long enough, it'll probably recover up to a quite a reasonable quite a reasonable value. There we go. It's at 1.78 volts already and climbing.

**Dave Jones:** It'll probably get up to once again that two easily, that um 2. uh 5 volts at 1.25 volts per cell, which Batteriser showed in their video. But you can see that it's just ridiculous and they made out that measuring the voltage of the batteries open circuit was exactly the same as the power supply here and it's not.

**Dave Jones:** It is completely different. Yes, batteries are different to power supplies, but you can see when we actually probe it in there, even with the power supply, it won't work.

**Dave Jones:** It's the terminal voltage of the battery that is dropping due to the electrochemistry because there's no energy left in it. So, a power supply is equivalent to using a battery when you probe it properly like everyone in the bloody industry does.

**Dave Jones:** Except Batteriser. Oh, it's just unbelievable. So, you can clearly see with no doubt whatsoever that a power supply is equivalent for determining the cutoff voltage of battery because the cutoff voltage is probing right up the monkey's butt right on the terminals.

**Dave Jones:** That's all that matters, not the open circuit voltage of the battery, of course. Batteries are not the same as power supplies when you measure the damn things open circuit cuz this doesn't have any electrochemistry.

**Dave Jones:** This thing does. All that matters is the cutoff voltage at the terminals there. So, their very specific claim at the end of the video that me measuring the battery cutoff voltage with this is is wrong and misleading at best.

**Dave Jones:** That was their claim. Here it is right in the video. To use a power supply to show a battery operated device's cutoff voltage ignoring the battery's internal resistance is wrong and misleading at best.

**Dave Jones:** And you can see that's total rubbish because they didn't probe it properly. Unbelievable. It's such a misleading video this Batteriser one. It's completely busted. I don't know how I can bust it any more than that.

**Dave Jones:** So, sorry that video was a lot longer than I was expecting, but as always I like to include detailed information of exactly what I'm doing because people are learning a lot from these videos, and that's the intention.

**Dave Jones:** So, there you go. I hope you found that video useful. If you did, please give it a big thumbs up on YouTube. And as always, the link to the EV blog forum down below for comments, leave them on YouTube, blog site, all that sort of jazz.

**Dave Jones:** And I've got a whole bunch of other battery videos, not just on this batterizer. I've had a whole bunch of videos for years. I've got like 10 battery videos or something crazy.

**Dave Jones:** So, I'll link in the uh playlist, the YouTube playlist here. We can go through and see them all. So, just remember the moral of the story. Always probe the monkey's butt.

**Dave Jones:** Catch you next time.
