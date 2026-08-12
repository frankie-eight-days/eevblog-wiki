---
video_id: ZvT9hHG17tQ
title: EEVblog #572 - Cascading Opamps For Increased Bandwidth
url: https://www.youtube.com/watch?v=ZvT9hHG17tQ
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 28, "3": 44, "4": 61, "5": 78, "6": 93, "7": 107, "8": 121, "9": 134, "10": 149, "11": 165, "12": 174, "13": 186, "14": 198, "15": 211, "16": 225, "17": 242, "18": 257, "19": 268, "20": 281, "21": 295, "22": 311, "23": 328, "24": 342, "25": 355, "26": 369, "27": 383, "28": 402, "29": 419, "30": 435, "31": 449, "32": 461, "33": 475, "34": 492, "35": 507, "36": 520, "37": 532, "38": 543, "39": 557, "40": 570, "41": 585, "42": 597, "43": 612, "44": 624, "45": 634, "46": 648, "47": 663, "48": 680, "49": 695, "50": 710, "51": 722, "52": 736, "53": 749, "54": 764, "55": 775, "56": 788, "57": 803, "58": 815, "59": 829, "60": 845, "61": 858, "62": 874, "63": 892, "64": 905, "65": 922, "66": 938, "67": 949, "68": 970, "69": 985, "70": 1000, "71": 1013, "72": 1027, "73": 1040, "74": 1057, "75": 1071, "76": 1086, "77": 1103, "78": 1118, "79": 1133, "80": 1147, "81": 1163, "82": 1178, "83": 1192, "84": 1204, "85": 1219, "86": 1233, "87": 1253, "88": 1270, "89": 1285, "90": 1295, "91": 1307}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at how I got the increased bandwidth on my microcurrent design cuz a few people have asked about it and it's really simple and it uses an old trick with

**Dave Jones:** op-amps where you can cascade op-amps together in series to increase your bandwidth. So, hence the title, cascaded op-amp bandwidth. Let's go. Now, let's start out with the simplest design which is what I used in my previous microcurrent design, just what's called

**Dave Jones:** a single-stage op-amp. It's one stage because it only has one op-amp. In this case, a basic non-inverting configuration. Totally familiar with this or you should be. Jelly bean circuit times 100 gain. I've chosen the resistors here to give us, you know,

**Dave Jones:** amplify the signal by 100 times. Now, op-amps have what's called a gain bandwidth product and what that is is the bandwidth of the op-amp at a gain of one. So, if you just short the output back to the input, you just have an

**Dave Jones:** op-amp buffer like that. It's the minus 3dB bandwidth. So, you'll find this GBWP figure, gain bandwidth product, on your data sheets or it's also known as unity gain bandwidth because you've got a gain of one, unity gain. So, it's the same

**Dave Jones:** thing. They're equivalent. Now, what we'll do is we'll assume that we've got an op-amp with a 1 MHz gain bandwidth product here. And as the name says, the bandwidth is the gain times the bandwidth. P is product, in

**Dave Jones:** multiplication. So, we're multiplying the gain times the bandwidth. So, if you want to get the bandwidth, all you got to do is divide that figure by the gain that you're using in your circuit here. And all things being equal, it's pretty much

**Dave Jones:** a constant linear factor. So, we can use this to calculate the bandwidth of our op-amp at higher gains. So, that banner spec that you'll see on the op amps, the gain bandwidth product, might be a megahertz and you

**Dave Jones:** might think, "Great, I can use it at a megahertz." Well, only at unity gain. If you uh start adding times two gain, times five, times 100, whatever, your bandwidth is going to drop accordingly in a linear relationship like that. So,

**Dave Jones:** let's take the example, 1 megahertz gain bandwidth product, a times 100 amplifier, exactly the same uh value as what I had in my original microcurrent design, 1 megahertz gain bandwidth product divided by our gain of 100 here. Gain is also known as AV. Then, our

**Dave Jones:** bandwidth has dropped to a lousy 10 kilohertz. Ah, that sucks. But, let's say that we want more bandwidth out of our op amp. And for some reason, we have to stick with this op amp. And in my microcurrent, it was

**Dave Jones:** There was a real legitimate reason why I had to cuz it was a very low offset chopper amp, etc. There's not too many on the market that can do the job. So, I pretty much had to stick with this op

**Dave Jones:** amp. So, this is one of the reasons why I had to cascade them. Ordinarily though, you should always try and do all of your gain in the one one op amp because it's going to be better in a

**Dave Jones:** couple of ways. But, anyway, we're going to have a look at the cascaded configuration, how you can use multiple op amps. So, now we've got a two-stage circuit here because we've got two op amps, both identical op amps, both with

**Dave Jones:** a 1 megahertz gain bandwidth product. And uh but now, we still want our same times 100 gain out of here. But, of course, we don't do it in one stage, we do times 10 and times 10. So, we change

**Dave Jones:** our resistor values there. We've still got our times 100 gain, but what does that do do our bandwidth? Now, deriving this might be a little bit tricky, but in the end, there's a fairly simple formula which uh can calculate the total

**Dave Jones:** system bandwidth here for as many stages as you want. On one big assumption, the assumption is that all of the op amps are identical bandwidth product and identical gain. But, in our case, hey, that's perfect. So, the formula here is

**Dave Jones:** the total bandwidth, the total system bandwidth, is equal to the bandwidth of one stage here, which we'll take a look at in the formulas down here, multiplied by the square root of 2 to the power of 1 on n, n being the number of stages. In

**Dave Jones:** this case, it's two stages. So, it'll be 2 to the power of a half and then minus 1. So, square root of all that, bingo, we can pop this into the formula and determine our bandwidth. Let's have a

**Dave Jones:** go. So, looking at our two-stage design here, we're just going to use this formula up here and plug the numbers in. Now, the bandwidth of one individual stage is now, using this formula up here, cuz we've now got a gain of times

**Dave Jones:** 10 instead of times 100 here, it's not a 10 kHz like this, it's 100 kHz because it's the 1 MHz divided by our gain of 10, which gives us 100 kHz here. And we multiply that by the square root of 2 to

**Dave Jones:** the power of 1 on n, n being two stages, so 2 to the power of a half minus 1. Oh, spare you the details of doing that on the calculator, the answer is a bandwidth out of here at times 100 gain of 64.36

**Dave Jones:** kHz. Bingo. By adding this second stage and a second op amp and cascading them, we've now gone from a 10 kHz bandwidth with a single stage for a times 100 gain, for exactly the same gain, our bandwidth is now, look, 6.4 times

**Dave Jones:** better. Awesome. So, we got ourselves a real Bobby Dazzler of an improvement going from one stage to two stage in terms of bandwidth. We increased it by an improvement of 6.4 times. Fantastic. But, do we get that same improvement

**Dave Jones:** when we go to three stages? Well, let's take a look at it. Now, instead of times 10 gain, we need our final times 100 gain. Remember, our system gain has to stay exactly the same. So, uh a cube

**Dave Jones:** root of uh that of 100 is 4.6416. And yes, it does have to be that precise, especially if you're doing a precision circle like I was on the microcurrent, you know, 0.05%. You know, you really have to get those gains

**Dave Jones:** pretty precise, which I'll talk about in a second. So, with for a three-stage one, we punch in the formula again, but our bandwidth is not 100 kHz if each stage is not 100 kHz anymore. It's improved. It's more than doubled. It's

**Dave Jones:** now 215.44 cuz it's a 1 MHz divided by 4.64 blah blah 215 kHz. So, we've improved our bandwidth on each stage now by lowering the gain, obviously, based on this formula. But does that have an overall net improvement? Well, yes, it does.

**Dave Jones:** Punch the numbers in. Our total system bandwidth is now 109.8 kHz or thereabouts, which is a decent improvement on 64, but it's not the huge 6.4 times improvement we got here. It's only an extra 1.7 times. And if you go

**Dave Jones:** to four stages and etc. etc., you get just get diminishing returns on your bandwidth. So, I calculated a four-stage which has a gain of 3.16 blah blah, and our bandwidth is only approa- you know, increasing to 137. So, you know, and

**Dave Jones:** with an improvement of 1.25 times. So, really, you know, a practical limit you're going to stop at three or four stages, even though you could keep going on. So, with my microcurrent, I stuck with a two-stage design here. Why? Well,

**Dave Jones:** you know, yeah, I could have increased the bandwidth by adding a third stage, but hey, there's extra cost. The chip isn't cheap, but the main reason why is because of this weird-ass gain value here. Trying to select off-the-shelf,

**Dave Jones:** you know, E96 uh value resistors or something like that to try and get an exact gain of exactly what I wanted. It's just ugly. No, didn't want to go there. But with a times 10 gain that I had in the two-stage circuit there,

**Dave Jones:** times 10 is easy with E12 values. I just had 1K here and 2K2 and 6K8 in series and they gave me 9K there and 1K, your standard non-inverting formula, that was a times 10 gain precisely. So, that's why I went with this two-stage one and

**Dave Jones:** didn't try and squeeze the extra bandwidth out of it. But hey, it was good enough when I changed from the which had a gain bandwidth product of not 1 MHz, but 6.5 MHz. So, you can plug those numbers into the formula and see

**Dave Jones:** how it all goes, but it was pretty decent bandwidth, much more, couple of 100 kHz, much more than the 100 kHz I was aiming for. Now, as I mentioned before, this magic formula over here is only valid for

**Dave Jones:** stages that have exactly the same gain and exactly the same gain bandwidth product. If you change the op amp used in here or you change the gain, which you might want to do for example on the front end because you might want to

**Dave Jones:** minimize your noise, so you have as much gain on the front end here as possible, which we'll talk about in a second, but yeah, it's only valid for that. If you change any of those parameters, the bets are off. Eh, I'll leave that up to you

**Dave Jones:** to calculate using oddball gains and oddball different op amps with different gain bandwidth products. Now, I know what some of you might be thinking, "Dave, you've done a video on op amp noise before." And yes, I have. I'll link them

**Dave Jones:** down below if you want to check it out. So, what happens if we cascade these op amps? Aren't we just going to get increase our noise problem? Well, yes, we are, but it's not nearly as bad as you might think. In fact, it's

**Dave Jones:** borderline trivial. So, but the noise will be dominated by this first op amp as we'll see here. So, really you want the maximum gain on your front end here if noise is an issue for you. Now, let's take the case of 1

**Dave Jones:** microvolt noise here RMS noise. Now, I won't go into the different types of noises, the current noise and input referred noise and all sorts of stuff. Uh let's just keep it simple. 1 uh microvolt of noise. We've gone back to

**Dave Jones:** times 10 amplifiers here. So, uh our 1 microvolt of noise obviously gets amplified by the uh gain of there and we're getting 10 microvolts noise out of here. No problem, right? But, does that 10 microvolt noise get multiplied by 10

**Dave Jones:** and the 10 again? Well, yes, it does. So, your noise would be exactly the same if you had a times 1,000 amplifier here. One you're still going to get 1 mV noise out 1,000 microvolts noise out of here

**Dave Jones:** with a single stage. And it's going to be the same, almost the same, just a smidge more um out of here like this. So, let's take a look at it. 1 microvolt noise in, 10 microvolts noise out of

**Dave Jones:** here. And then we've got to add in our extra 1 microvolt noise of this op amp here. But, of course, that's not 11 microvolts. So, it's not 11 * 10, which is 110 microvolts out of here. No. You

**Dave Jones:** remember, noise uh when you add noise sources, it's the root sum of the squares like this. So, the noise number one here uh it gets squared and then added onto noise number two. And if you do the math there, well, it's only it's

**Dave Jones:** not 11, it's only 10.05. So, a little bit smaller than what you might think. So, hopefully you can see that the noise just once again a vanishing returns here each time you cascade. So, in this case, it's 100.5 + 1. Whack that into our uh

**Dave Jones:** root sum of the squares here and our total output noise is 1,005.05 microvolts. We've just dropped cuz this one only adds 1% again, 1% each time. It's bugger all, half a bee's dick. It doesn't really matter. If you had a

**Dave Jones:** single stage here, you'd still get 1,000 microvolts of noise. What's the difference between 1,000 and 1,005 there? Well, 0.5%. Ah, it's nothing. Forget about it. So, there you have it. That's cascaded op amp bandwidth. And as usual, we'll go

**Dave Jones:** over to the bench and we'll build this up thing up and see if we can verify that we can get these multiplication factors here when we increase our number of stages. Uh, we're not going to measure noise. That's too tricky and

**Dave Jones:** really quite pointless. And we should be able to measure it at least to within the ballpark of these multiplication factors that we get here based on our system bandwidth formula up here. But, the gain bandwidth product does vary

**Dave Jones:** with supply voltage, which we may be able to show. And there's a big margin on it anyway. But, hey, should be able to get close and prove that this thing actually works. All right. So, what we've got here is

**Dave Jones:** just a jelly bean dual op amp. I've got a TS912 from ST. It doesn't really matter. Just sort of pick one at random. We've got a two-stage times 10 amp here for a total gain of times 100, but I will change the configuration

**Dave Jones:** around. This will be the final configuration. We'll start out with a unity gain amplifier. Just so I just short in input and output on a single stage, measuring that. And if we have a look at the data sheet here, the good

**Dave Jones:** thing about this one is that it has different parametric tables for different supply voltages as I show you. So, this is what we're going to operate at as plus minus 5 volts, which gives us a total rail of 10 volts. And if we go

**Dave Jones:** down here, here we go. Gain bandwidth product measured at a gain of 100 with under those at under those conditions there. But, we're getting, you know, it's telling us a typical figure is 1.4 MHz. We may or may not get that. Doesn't

**Dave Jones:** give us a minimum figure. You know, it could be higher. It's likely to be that or higher. It's unlikely to be under. So, let's hook up that as a unity gain amp and see what we get. All right, what

**Dave Jones:** I've got here is two waveforms, yellow and green. You can see that. They're different ones here. And there the green one there, channel two, is our input voltage, which I'm going to set to 10 mV. I have set to 10 mV RMS. I'll have

**Dave Jones:** to tweak that during the experiment to keep it at 10 mV due to the non-linearity of the Well, the flatness of the built-in function gen of my Agilent scope here. Anyway, that's just a little trap if you're doing these sort

**Dave Jones:** of tests. Don't assume that your function generator has a constant output amplitude over frequency. It may or may not. So, anyway, I'm using the building one. And our output voltage, there we go, is exactly the same. Hey, it's unity

**Dave Jones:** gain, and we're measuring that at 100 kHz. Not a problem. So, what we want to do now is increase our frequency until our output voltage drops to -3 dB, 0.707 of that 10 mV there. And you'll notice that it's actually going up. And that's

**Dave Jones:** due to the characteristic of this circuit, which has a non-flat frequency response. You know how the frequency responses should ideally be flat and then falls off, of course, at 6 dB per octave or whatever. Then this one's not. It's got a little You

**Dave Jones:** know, it's it's got a bit of peaking at the output there. But anyway, that's not going to concern us. We just increase our frequency until we get that 0.707. I'll go into frequency fine here. And you'll see that the input amplitude

**Dave Jones:** drops. So, I've got to just, you know, tweak that up a bit just to keep that at that 10 mV figure. And then we're looking at getting the frequency at 0.707 of 10 mV. You know, thereabouts. Near enough. Hey, look at that. We're getting

**Dave Jones:** 2.3 MHz, much higher than the 1.4 MHz on the data sheet. But, hey, that's to be expected. Typically, the op amp's going to perform better than or at or better than its typical figure. And now I've got the times 10 amplifier configured

**Dave Jones:** there, and as you can see, 10 mV in, and we're getting, you know, a times 10 of that out. Not a problem. We're only down at 7-odd kHz here. So, let's try and find the minus 3 dB point of that. And

**Dave Jones:** remember, before we had a unity gain bandwidth of measured, not from the data sheet, but measured from this chip, of 2.3 MHz. So, we expect this to drop to 70.7 mV at 1/10 of that frequency, or 230-odd kHz. And aha, as

**Dave Jones:** you can see, look, we're down at 70.7 mV here. Of course, we get a phase shift at the higher frequency. Now, we're only at 145 kHz. So, it's not nearly as good as we thought it should be, because this

**Dave Jones:** thing is not in this configuration is not going to have a constant gain bandwidth product. So, some op amps may, this one in particular doesn't. So, you've got to actually check this stuff out. So, the data sheet value of a times

**Dave Jones:** 100 gain, you remember that, it said it was specified the gain bandwidth product at times 100. So, let's increase this to 100 times gain and see if we get the typical data sheet figure. Anyway, we do want to note this, because we're going

**Dave Jones:** to be using this is our measured bandwidth. So, when we cascade them, then then we should get, you know, the formulas that we got on the whiteboard. So, we need to note down that figure of 145 kHz. That's our

**Dave Jones:** times 10 bandwidth. So, here we go, configured as times 100, our 10 mV in, and we're getting 1 V out. And, Uh, you know, it's at a low frequency. So, let's find the minus 3 dB uh point of that.

**Dave Jones:** And there it is. Uh, 707 millivolts out, 10 millivolts in, times 100, and we're getting a frequency of a bandwidth there of about 13.4 kilohertz. And bingo, that pretty much matches the data sheet of at the gain of 100 of our typical uh

**Dave Jones:** bandwidth of a unity gain bandwidth of 1.4 megahertz. So, we have to divide that by 100, of course. So, we're expecting 14 kilohertz there, and we're getting very close to it. Beautiful. Now, I have a two-stage uh amplifier

**Dave Jones:** hooked up here uh times 10 gain each, exactly like the original uh data sheet value. Now, we were getting a uh 13.4 kilohertz bandwidth before at times 100 gain with the single-stage op amp. Now, what bandwidth do we get with the top

**Dave Jones:** with the two-stage op amp? So, what we expect here, if we've got a measured uh bandwidth at times 10 uh gain, which we've got two of those, then each one is 145 kilohertz. Whack that into our uh formula for our cascaded amps with a

**Dave Jones:** number of two, we should measure about 93.3 kilohertz. Let's see if we get close to that. Might be spot-on, but should be near enough. And there we go. That's not too far off. Uh 707 millivolts, two stages there, 10

**Dave Jones:** millivolts in, 108 kilohertz there. So, that's a little bit better than our 93.3 kilohertz, but uh you know, we didn't actually measure the gain of the other side op amp, but because it's on the same uh die, you'd

**Dave Jones:** expect a similar uh performance there. But hey, I'm going to call that close enough. Now, another interesting thing to note is you want some margin in your gain bandwidth product. Why? Because uh your op amp is typically going to

**Dave Jones:** distort. Now, watch this. Okay? Look at some distortion in there. You can see some distortion in that waveform starting to happen there. If I bring that over, look at that. We're starting to get little bits of distortion. And that's, you know, the

**Dave Jones:** input's still nice and clean, but yeah, look at that. So, you just got to be careful there that you're not trying to push the limits of your amplifier because they are going to distort just like that. Even worse, this one's pretty mild,

**Dave Jones:** actually. Oh, oh, I forgot to show you how the gain bandwidth product changes with voltage or this one for this particular op-amp does. So, this is at plus minus 5 volts at the moment. And in theory, if it was, you know, it didn't

**Dave Jones:** change at all with supply voltage, then we could wind it down and the output should stay the same. But if we lower the voltage to plus minus 2.5 volts or 5 volts total, we'll notice the output voltage drop. Look at that while the

**Dave Jones:** input stays the same. So, the gain bandwidth product is not the same against supply voltage there. So, there you go. I hope you enjoyed that quick little fundamental Friday on cascaded bandwidth there. Sorry we weren't able to measure the exact numbers we got on

**Dave Jones:** the whiteboard, but these things aren't exact in practice, really. So, you know, choose use another op-amp in here and we probably would have got different results again, but it's going to be near enough and in theory on the whiteboard,

**Dave Jones:** that is actually how it works. But in practice, different op-amps change their gain bandwidth product across individual units, across supply voltage, across test frequency, and all sorts of stuff. So, and input voltage, so and output voltage. So, really, you know,

**Dave Jones:** it was unlikely that we were going to get spot-on values, and we didn't. But it showed how you can get increased bandwidth there cascading. In this case, we went from 40 13.4 kilohertz measured with when on a times 100 gain using a

**Dave Jones:** single op-amp to up to 100 kHz bandwidth on the when we just cascaded another one in our dual op-amp here. Easy. So, there you go. It's a nice little trick you can use if you have to, but as I said right

**Dave Jones:** at the start, really you if you need you really should be picking the right op-amp for the job so you can do it in one op-amp. But, if you have to, like I did in the mic current for a precision

**Dave Jones:** application, hey, this works a treat. Anyway, if you want to discuss it, jump on over to the EEVblog forum. And if you like it, please give it a big thumbs up. Oh, my thumb is too big. Catch you next

**Dave Jones:** time.
