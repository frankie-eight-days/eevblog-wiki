---
video_id: zdbuSZVYewg
title: EEVblog #149 - Agilent Infiniivision 3000 X Series Oscilloscope Review
url: https://www.youtube.com/watch?v=zdbuSZVYewg
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 29, "3": 43, "4": 53, "5": 66, "6": 77, "7": 89, "8": 110, "9": 126, "10": 145, "11": 161, "12": 180, "13": 196, "14": 211, "15": 224, "16": 238, "17": 256, "18": 269, "19": 279, "20": 292, "21": 310, "22": 323, "23": 336, "24": 347, "25": 361, "26": 378, "27": 394, "28": 406, "29": 423, "30": 434, "31": 453, "32": 464, "33": 481, "34": 493, "35": 511, "36": 531, "37": 544, "38": 562, "39": 573, "40": 589, "41": 597, "42": 621, "43": 638, "44": 665, "45": 685, "46": 698, "47": 712, "48": 730, "49": 743, "50": 756, "51": 772, "52": 783, "53": 796, "54": 805, "55": 831, "56": 842, "57": 867, "58": 878, "59": 893, "60": 907, "61": 920, "62": 940, "63": 952, "64": 963, "65": 979, "66": 997, "67": 1011, "68": 1026, "69": 1047, "70": 1057, "71": 1072, "72": 1092, "73": 1103, "74": 1114, "75": 1125, "76": 1155, "77": 1166, "78": 1181, "79": 1193, "80": 1209, "81": 1223, "82": 1233, "83": 1242, "84": 1251, "85": 1263, "86": 1276, "87": 1288, "88": 1297, "89": 1313, "90": 1322, "91": 1341, "92": 1355, "93": 1363, "94": 1375, "95": 1389, "96": 1404, "97": 1421, "98": 1440, "99": 1458, "100": 1472, "101": 1485, "102": 1497, "103": 1513}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's review time again, and it's another Agilent oscilloscope.

**Dave Jones:** This time it's the big brother to the 2000 series X series I reviewed last time. It's the 3000 X series InfiniiVision oscilloscope. Woohoo! 1 million waveform updates per second for about 3 grand.

**Dave Jones:** Haha, love it. Now, because there's so much to test on a scope, and there's so much similarity between the new 3000 series and the new 2000 series, I've already done a 1-hour review of the 2000 series.

**Dave Jones:** I'm not going to cover any of that again in this review for this. So, if you think I'm missing something, go check out the 2000 review cuz they're next to identical.

**Dave Jones:** So, I'll only go through the major differences, or I'll only show you the major differences that you get with the new 3000 series scope. And here we have the 3000 series on the left and the 2000 series on the right over there.

**Dave Jones:** And if you can't spot the difference between them, well, that's not too surprising cuz there is essentially very little difference at all. They basically share the same platform, the same design.

**Dave Jones:** They've got exactly the same case. They use the same chassis internally. Only the PCB is different. They share the same user interface control layout. All the controls are identical.

**Dave Jones:** All the labeling is identical between the units. They've all got the function gen, the logic analyzer, USB, the demo signals and all that. And the only real difference that's noticeable visually is that the 3000 has the smart probe interface on it, those gold contacts along the bottom that let you use our smart active probes.

**Dave Jones:** And of course, the 3000 series is higher performance. So, you will get extra bandwidth and extra waveform update speed and extra some extra software functionality as well. But, apart from that, identical scopes.

**Dave Jones:** They're based on the same platform. Now, here's a demo of the update rate to show the 1 million waveforms updates per second on the Agilent 3000 series here as compared to the 2000 series, which only has 50,000 only 50,000 waveforms updates per second.

**Dave Jones:** Now, we're generating a test signal with a runt pulse that actually has one missing that has one runt pulse every 50,000 cycles. And as you can see on the 2000 series, it updates roughly once once or twice per second.

**Dave Jones:** So, it's capturing that the exact same signal is captured repeatedly on the 3000 series with the 1 million waveform updates per second. And if we do the exact same test again, but we have a runt pulse that is only every only once in every 1 million cycles.

**Dave Jones:** Then as you can see on the 3000 series with 1 million eight waveform updates per second, you're capturing at about once or twice per second like that. But, the 2000 series, which still has a an excellent 50,000 waveform updates per second, whoop, there we go.

**Dave Jones:** It was just there then. But, you're lucky to catch that, you know, once every 30 seconds or something like that. So, if you're trying to find an elusive fault like that, then something like even 50,000 waveform updates per second isn't enough.

**Dave Jones:** Imagine if you had a runt pulse which happened once per day or something like that. You could be sitting here until the cows come home trying to find it on even a 50,000 waveform update per second scope.

**Dave Jones:** And as with the 2000 series, the claimed 4 gig samples per second is only in interleave mode. So, what that means is if you're only using one channel, you get your 4 gig samples per second, as you can see here.

**Dave Jones:** But, as soon as you switch in a second channel, you only get 2 gig samples per second. It drops in half. But, one of the advantages of getting the four-channel version is that because these are segmented, these these two separate channels, it handles them separately.

**Dave Jones:** If you turn on channel three, look, it stays gig samples per second. So, you can actually still run two channels side by side, both at 4 gig samples per second, because it can handle that inside the ASIC.

**Dave Jones:** But, you switch on the that one, and it just can't do it. So, there's a little trick. And the memory depth is going to halve, too, if you turn on the secondary channel, just like the sample rate.

**Dave Jones:** One nice feature, which is also available on the 2000 series to a lesser extent, is where it shows these trigger violations. So, you can actually search for and set up trigger violations.

**Dave Jones:** You can see that little white up there, and you can see quite clearly here where it's violating certain conditions. So, what we've got set up here is we're actually searching for a rise and fall time edge violation.

**Dave Jones:** So, you can see the different rise and fall times there. There's a faster one and a slower one. And the slower one is what we're actually triggering on. We're triggering on that violation.

**Dave Jones:** So, if we go into the search, if we press the search button up here, you'll find that we can choose different types of search events. And one of them is rise and fall time.

**Dave Jones:** So, if we're searching for rise and fall time, you've got various settings and thresholds which you can actually set up. And you'll notice that we're not It It hasn't found any violations at the moment, okay?

**Dave Jones:** There's no white triangle up above there. But, if we go into settings and then we adjust the time here, if we adjust the time, increase that, it's 30 30 nano.

**Dave Jones:** If we keep going up, we'll find, bingo, we've suddenly got violations and you can see where it's actually violating that time there. Bingo, it just comes and goes. You can set those thresholds and it will pick it up.

**Dave Jones:** It's fantastic. And of course, you can stop and capture that and you can actually uh scroll through and it'll go through the event search like that. You can press the left and right buttons here and it will jump to the next event.

**Dave Jones:** It's You can see it's found 55 events where it's violated that and you can just jump from one to the other instead of having to scroll through, which you normally would with your horizontal your horizontal position like that.

**Dave Jones:** You can still do that if you want, but it's just easier to jump straight to the violation like that, each individual violation. And you can do that same violation search on edge, pulse width, rise, fall time, runt pulses, and serial decoding as well if you got the serial modules installed.

**Dave Jones:** One of the differences, as you'd expect on any high-performance oscilloscope, is 50 ohm input termination. So, if we go into the vertical menu here, you'll see you've got input impedance.

**Dave Jones:** You can choose 1 megaohm, standard 1 megaohm, or 50 ohm input impedance. And once again, the coupling, AC or DC. You don't get a ground option because presumably they put the um the little ground symbol on the side of the screen here so you know where the ground reference for your waveform is.

**Dave Jones:** But, well, I just want my ground option, please. And one of the major items you don't get on the 2000 series is the optional and I highlight the word optional serial decoding.

**Dave Jones:** So, you you hit the serial and you've got all the different modes. You've got I squared C, you've got um I2S, SPI, CAN, LIN, and UART RS232. Not a bad selection uh at all, but I think there's one missing there and that is USB.

**Dave Jones:** It can trigger off USB. If you go into trigger here, we can see that the list of trigger options, we can actually trigger from USB, but we can't actually do uh real-time decoding in USB.

**Dave Jones:** So, that's a bit of a shame really. I I I was a bit disappointed with that one, but uh at least you can trigger off USB, so you can decode it manually, but um the serial options allow you to trigger on data like this and you can trigger on all sorts of things.

**Dave Jones:** Start conditions, stop conditions, missing acknowledgers. This is uh I I2C. I've got a I2C uh signal being fed into this. So, you've got your um your SCL clock line and your SDA data line and you can trigger on uh all sorts of various items and you'll see it does real-time hardware decoding.

**Dave Jones:** And if you hit serial again, you can actually call up a lister, which will actually um list the data here, which is very very nice. And there's various other options as well.

**Dave Jones:** I won't go into them, but it really is quite a nice option for um serial decoding. And once again, that's done all in the hardware. It's so you don't get a performance penalty or pay a performance penalty by enabling the serial decoding cuz it's all done on the ASIC in real-time.

**Dave Jones:** And there's one other thing to remember with the serial decoding option. You don't actually, if you buy the option, you don't actually get all of them at once. You have to buy them separately or in groups, which is a bit crazy.

**Dave Jones:** I don't I don't like that. You should just be able to get them all, but I guess if you're only working on, say, I2S bus, then you only have to buy the I2S bus option, but, jeez, I think that's a bit tight-ass.

**Dave Jones:** And I forgot to mention one item which you won't find on here as well, which is JTAG. It's a shame that they don't have a JTAG decoder as well.

**Dave Jones:** That would have been awesome. Yet another improvement over the 2000 is the trigger options. You actually get the top three of the same. You get edge, pulse width, and pattern on the 2000, but on the 3000, you get extra rise and fall time triggering, nth edge burst, and runt pulse triggering, and setup and hold time as well, which is excellent.

**Dave Jones:** Plus, you get the USB decode and the serial decode as well. So, they're very valuable options, and they aren't optional. They are built in. And once again, if we go into help here, we have training signals, but I forgot to mention in this in the previous one, these are actually optional as part of the training package, I I believe.

**Dave Jones:** So, they're not actually standard with the scope. But with the 3000, you do actually get a few more because you get the test signals for the various serial buses as well, which is very nice for, you know, schools or just for setting that up in general to make sure that you can actually set up your scope before you try and trigger on your actual circuit under test.

**Dave Jones:** And if we turn on the waveform generator option, as per the 2000, it is an extra cost optional extra. You get the function generator output down here, and it's exactly the same, which is quite surprising because on the 3000, you actually pay a bit more for that function generator option, but it's identical.

**Dave Jones:** It's got the same function, sine, square, ramp, pulse, DC, noise, and it doesn't have arbitrary. Once again, it doesn't have any of that. So, it's really exactly the same function generator.

**Dave Jones:** And as I didn't as I forgot to mention in the 2000 review, the even though it's got like a trigger output on the back, it does not have one thing that's missing is a modulation input connector.

**Dave Jones:** Because any good function generator will have modulation capability so that you can use a secondary or in this case they could have had it built in to the firmware, I'm sure if they wanted to, modulation options for frequency and amplitude, for example, and that would have been brilliant.

**Dave Jones:** But once again, it's probably deliberately crippled to not eat into their function generator. Otherwise, you'll be getting you know, a top-of-the-line 20 MHz function generator built into this thing.

**Dave Jones:** And it's a real shame. I think it is. There's a smart probe interface I was telling you about and the 500 MHz unit comes with 500 MHz passive probe, which is pretty much identical.

**Dave Jones:** It's a slightly bigger case to the 200 MHz one which came with the 2000 series. I did find one extra feature buried away in the measurement menu here. It's got an extra extra statistics option for your main measurements and you can switch that on or off.

**Dave Jones:** It comes up on the screen here and we can reset the stats like that and it calculates the stats on the current waveform. There's some extra math functions too on the 3000.

**Dave Jones:** So, if we go into math here and they've got a couple of operator options. They've got They've got They've got They've got integral. They've got D on DT and they've got square root as well.

**Dave Jones:** So, that's a couple of extra math functions over the 2000 series model. And this table here is a short summary of the difference between the 2000 series and the 3000 series scopes.

**Dave Jones:** As you can see, only eight channel digital whereas you get 16 channel on the 3000, 70 to 200 MHz bandwidth as opposed to 100 to 500 MHz bandwidth. You've got basically double the sample rate and there's a huge memory difference, only 100k points maximum there as opposed to 2 meg points standard and optional if you buy the memory upgrade, you get 4 meg points.

**Dave Jones:** Once again, maximum but that changes depending on which mode you're in. And the huge difference, the big selling point is the 1 million waveform updates per second, which is phenomenal on the 3000 series.

**Dave Jones:** So, to get that on a $3000 class oscilloscope really is quite amazing. And once again, you don't get anything else standard really as part of the major options. You do get the search and navigate function and the serial protocol analysis functions, but really you don't get the segmented memory, you don't get the mask limit, you got to pay extra for those.

**Dave Jones:** You do get the auto probe, but and there's a couple of other minor things like the math and other things that we've seen. There's a few minor differences, but yeah, I expected a bit more standard functionality in the 3000 series.

**Dave Jones:** So, I was a little bit disappointed there, I've got to say. And for the 3000 series, they've got even more model options, 14 of them, count them. 14 model options, which is crazy.

**Dave Jones:** They had 12 on the 2000 and I thought that was too many. Now, they've got the 100 MHz analog bandwidth models here and here. Why? That overlaps with the 2000 series model, it's just crazy.

**Dave Jones:** I mean, the the 2000 series model goes to 200 MHz, it makes sense to start the 3000 series from 200 MHz and go upwards. I don't mind those options, 200, 350, 500, not bad options at all.

**Dave Jones:** Get rid of the 100. Tight asses I reckon they should have given you the 200 MHz in the standard price. But of course, having said that, I still think the 100 MHz model entry level is still excellent value for money, but I think they could have killed the market and gone a bit better by giving you 200 MHz.

**Dave Jones:** Come on, Agilent. Once again, there's a mistake in the data sheet. There is no ground coupling on the input. God, what are you doing? The digital logic analyzer is improved in the 3000.

**Dave Jones:** Still 1 gig sample per second, but you get two midpoints maximum record length, but that does drop to 500 K points if you got the analog and the digital same is sampling at the same time.

**Dave Jones:** So, if you got the mixed signal interface, just something to be aware of. So, as you can see, the 3000 series has quite a few nice extras over the 2000 series, including a hardware frequency counter I forgot to mention as well, which the 2000 doesn't have.

**Dave Jones:** Now, you've really got to make the choice up front which model you want to go for because even though they're based on the same or similar platform hardware platform, you can't upgrade a 2000 series to a 3000 series with just a firmware upgrade.

**Dave Jones:** So, that's not possible. You got to decide up front. And decisions that might want to drive that are the million waveform updates per second, the serial decode, stuff like that, a few of the extra other, you know, some of the triggering, advanced triggering capabilities, things like that.

**Dave Jones:** So, you've just got to, you know, make that choice up front. Do I want to go with the low cost version or do I need serial decode and higher performance and better triggering in the 3000 series?

**Dave Jones:** Overall, I think Agilent's done a pretty darn good job of positioning the 2000 and the 3000 series models. A lot of thought's gone into it. And Uh, there is, you know, these things are so good that it comes down to the fact is like you buy either like a real low-end, you know, a little $400 Rigol or something like that.

**Dave Jones:** There's that price point, you know, the sub $1,000 price point, or there's the $10,000 plus price point, which is a different kettle of fish. And in between, you've got these.

**Dave Jones:** You've got the 2000 and the 3000 series. There's not much other choice. They blow most of the other scopes in that segment out of the water. It's amazing. Now, the base model unit starts at around 2800 US dollars.

**Dave Jones:** And that's for the two-channel 100 MHz version. And that's pretty darn good value for money, I think. It I would highly recommend though you go for the four-channel version if, regardless of what bandwidth or anything else you get, go for the four-channel version, which is about 570 odd dollars extra.

**Dave Jones:** Don't quote me on that, but it's not a huge amount extra when you're talking about that sort of money. And with the extra four channels, it gives you the twice the sample rate if you're only using two channels.

**Dave Jones:** So, it's it's highly worth buying the four-channel up front cuz if you buy the two two-channel, you can't upgrade it to a four-channel version later because the hardware is actually not built in.

**Dave Jones:** The hardware that you buy a two-channel, it only physic- physically comes equipped with two channels. So, I recommend you get spend a little bit extra, get the four up front.

**Dave Jones:** Now, unlike the 2000 series model that is fully bandwidth software upgradeable from 70 to 200 MHz, the 3000 series isn't quite like that. There are differences. Now, the 100 MHz version can be software upgradeable via a license key to 200 MHz, but the 350 and the 500 MHz versions um, use a totally different higher performance front end.

**Dave Jones:** So, if you want to upgrade from the 100 or the 200 MHz version to the 350 or 500, you physically have to send your unit back to Agilent and they'll replace the main board for you.

**Dave Jones:** Now, I don't think that actually, uh, costs any extra. Don't quote me on that, but yeah, you do have to physically send it back. Uh, but if you say bought the 350 MHz version, you can buy the 500 MHz version just buy the, uh, software license key.

**Dave Jones:** Something to think about. And the four-channel 200 MHz version, that starts at about, uh, four grand. So, that's pretty darn good value for money for a million waveform update per second scope.

**Dave Jones:** But, once you go above that, the prices start to creep up pretty darn quick for that extra, uh, bandwidth. If you go to the, uh, 3 50 MHz, uh, bandwidth, you're looking at about $7,500 if you for a four-channel version.

**Dave Jones:** If you want to jump to the 500 MHz version, you hit the 10K mark for the four, uh, channel version. So, the prices start to creep up pretty quick with the, uh, 350 or 500 MHz, uh, front end options.

**Dave Jones:** But, even when the prices start going up like that for the higher bandwidth models, they're still pretty good value for money. So, you've got to really compare it with the competition.

**Dave Jones:** Go compare it with the Tektroni- and the LeCroixs and, you know, make up your own mind for your price performance, uh, category, really. Um, they they can't match it at the moment.

**Dave Jones:** So, as I said with the, uh, 2000 series, competition's got a lot of catching up to do. And that's the thing you've got to consider when you're comparing scopes.

**Dave Jones:** You can't just look at the analog bandwidth and the sample rate and the sample memory and maybe a few other features. You know, you've got to compare apples to apples.

**Dave Jones:** And if you do that, you've got to include the, uh, waveform update rate as well. Now, you know, you may try and compare this 10 grand you know, you may compare the top of the range 10 grand version of this to another 10 grand scope.

**Dave Jones:** What you've got to look at not only the waveform updates per second. If you do that, you've got to look at how does the turning on some of the features affect that sort of stuff?

**Dave Jones:** On the Agilent scopes, it doesn't at all. You can turn on the serial real-time serial decode, the masking, and those waveform updates per second don't drop. You still get a million waveform updates per second.

**Dave Jones:** It's incredible. And that, depending on your requirements, not everyone's going to have the same requirements, that may be worth its weight in gold compared to you know, a bit extra analog bandwidth or a bit more sample memory or something like that.

**Dave Jones:** But just keep it in mind. Make sure you compare apples to apples. Don't just rush out and say these things are too expensive. And then, of course, you start talking options.

**Dave Jones:** The logic analyzer on this thing is over a grand. And granted, I love the mixed signal capability built into here. It's awesome. But gee, you you pay a bit of a premium for it cuz you can buy a pretty schmick standalone USB logic analyzer for a you know, under a thousand bucks.

**Dave Jones:** So, you know, that potentially has more capability. Granted, it's not mixed signal and built in and it's all convenient and you know, you get the advantage of the mixed signal capability and the cross triggering and all the yada yada, all the other stuff.

**Dave Jones:** But yeah, you're paying a bit of a premium for that, which is a bit of a shame. Same with the function generator. Paying about 700 bucks for the function generator.

**Dave Jones:** And my opinion, it's a little bit crippled. And it's a shame because you can get a standalone arb 20 megahertz function generator for around, you know, five, six, seven hundred dollars for the same price or less.

**Dave Jones:** So, geez, I just wish they would just they it's didn't it as much, but still superb value for money. The The killer, and this is the thing people don't understand.

**Dave Jones:** They think these are expensive, and they're not. You go out and try and buy a million waveform updates per second and this sort of speed. Traditionally, you've had to pay, you know, 10 20 grand, something like that, to get it.

**Dave Jones:** And now, they've they've instantly halved the prices or better. So, that's where the improvement with these scopes come from, and that's where the competition have to catch up. And then, you've got the other software options like segment of memory, masking, the serial decodes, which don't just come in one serial decode package.

**Dave Jones:** You got to buy individual serial decode packages. It's just Ah, man. Agilent, where everything's optional extra. And because Agilent have really tried to target the educational market with this these things, I've heard that they are uh bundling an education option.

**Dave Jones:** So, if you're in an educational institution, or possibly if you're a student, I don't know, uh you'll have to look up the details, but if you buy one, you'll get the free waveform generator option, and you'll get the um training signals and the training manuals and that sort of stuff, plus a 15% discount.

**Dave Jones:** Bargain. Now, I know why they've done the 100 MHz version is to give people a sense of, you know, value down at that bottom end, but I just you know, I There's overlap with the 2000 series there.

**Dave Jones:** I would have preferred if their bottom of the range unit started at 200 MHz and you got that for the 2800, but I don't know. I'm just being a bit greedy, I guess, but only because I see all this filter within the ASIC in here.

**Dave Jones:** I see all this marvelous technology filtering down, and now you're getting the million waveform updates per second for an incredible price, but they they still are in that traditional mindset.

**Dave Jones:** It's not just Agilent here, it's all the manufacturers. They're in that traditional mindset where you've got to pay extra for that bandwidth. So, if you're after a high-performance scope in that mid-level, uh, price category, these offer superb value for money.

**Dave Jones:** Highly recommend them, but go for the four-channel version. It's a winner.
