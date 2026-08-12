---
video_id: UVjLoJMVL0s
title: EEVblog #1328 - uCurrent OPA189 Measurements
url: https://www.youtube.com/watch?v=UVjLoJMVL0s
source: youtube-asr
timestamps: {"0": 0, "1": 7, "2": 20, "3": 38, "4": 53, "5": 69, "6": 81, "7": 92, "8": 105, "9": 125, "10": 139, "11": 159, "12": 175, "13": 182, "14": 194, "15": 205, "16": 214, "17": 232, "18": 243, "19": 256, "20": 288, "21": 315, "22": 341, "23": 358, "24": 377, "25": 402, "26": 417, "27": 433, "28": 446, "29": 456, "30": 472, "31": 491, "32": 499, "33": 513, "34": 529, "35": 544, "36": 552, "37": 561, "38": 573, "39": 583, "40": 594, "41": 610, "42": 627, "43": 641, "44": 652, "45": 670, "46": 680, "47": 693, "48": 703, "49": 712, "50": 725, "51": 734, "52": 746, "53": 759, "54": 770, "55": 779, "56": 788, "57": 807, "58": 820, "59": 837, "60": 854, "61": 869, "62": 892, "63": 908, "64": 922, "65": 929, "66": 942, "67": 955, "68": 964, "69": 979, "70": 995, "71": 1009, "72": 1028, "73": 1042, "74": 1053, "75": 1076, "76": 1086, "77": 1096, "78": 1109, "79": 1121, "80": 1131, "81": 1147, "82": 1158, "83": 1187, "84": 1199, "85": 1211, "86": 1226, "87": 1244, "88": 1252, "89": 1280, "90": 1301, "91": 1326, "92": 1350}
---

**Dave Jones:** Hi, in a previous video linked in down below and up here and at the end if you haven't seen it, this is part of the series of designing a better microcurrent.

**Dave Jones:** And the last video we took a look at the OPA189 and how it looked like in most respects it was better than the MAX42384239 that we use in the microcurrent.

**Dave Jones:** So, I ordered some. Here you go. OPA189IDBVR. This is the SOT23 five package. It is available in different packages, but I got the SOT23 five because it is actually directly pin out compatible with my existing microcurrent.

**Dave Jones:** So, what we're going to do in this video is we're going to actually compare the original design microcurrent to one that uses the drop-in replacement OPA189 and measure the noise and other performance characteristics of it.

**Dave Jones:** Let's go. But, it's actually not completely pin out compatible because here's the existing MAX4239. It's actually a six-pin SO. You can see it's got three pins on the top here, but the OPA189 only has two pins on the top.

**Dave Jones:** It's a five-pin SOT23 package. The only thing it's missing is the enable disable pin, which we don't actually use on this. We just tie it high. So, we can simply simply remove the existing chips and solder in the new one.

**Dave Jones:** Doesn't matter. Beauty. So, to make this comparison as fair as possible, what I've got here is two identical boards from actually the same batch, just a serial number apart.

**Dave Jones:** So, they use all the same parts that you know, come from the same reels and everything. So, they're basically as identical as you can get, but one uses the 189, one uses the original MAX4239.

**Dave Jones:** Now, the problem is though I can't use the coin cell battery to do the comparison test because the OPA189 has 4.5 volts minimum supply voltage, whereas the MAX4239 can go down much lower like 2.3 V or something if I recall correctly is the dropout voltage, something like that.

**Dave Jones:** Anyway, but it only goes to 5.5 V maximum. So, I'm going to run this from a 4.5 V battery, so just enough. I've got three AAA's here, which will give us if I use brand new cells, it'll give us just over 4.5 V.

**Dave Jones:** So, yeah, that'll be good enough for Australia. Right, so we're going to start out by measuring the noise. Now, as I said previous video linked in down below where I've actually really quite a while ago this video is where I use my HP 35 660A dynamic signal analyzer to actually measure noise floor of op-amps.

**Dave Jones:** And that's a really great video from about I think it's from about like 2015 20 minutes onwards in the video is where I show you extensively how to set up a dynamic signal analyzer to measure noise to match the data sheet noise density actually, which is nanovolts per root hertz.

**Dave Jones:** Now, to do this of course you can't just have the boards flapping around in the breeze on your bench. You've got to have a nice diecast shielded box like this.

**Dave Jones:** So, I've got that with a BNC output going into our input. So, we'll put the batteries and everything else inside the diecast box just so we eliminate any external noise, any you know, external 50 hertz.

**Dave Jones:** All right, first thing we're going to do is just measure the power supply current because the OPA189 is supposed to take more current. So, let's get the old one 4239.

**Dave Jones:** I've actually removed the dropper resistor for the LED here, otherwise the LED will draw like you know, 7 milliamps or you know, a huge amount of current like that.

**Dave Jones:** So, let's give it a whirl. This is the MAX 4239, 1.31 milliamps. And the 189? Ah, 2.68. So, you know, what what 1.3 milliamps more overall for the two op-amps.

**Dave Jones:** And you know there's some residual uh you know other current which will remain the same but yeah you know that's it's neither here nor there really unless you're after some ultra low power design so nice.

**Dave Jones:** Now I know that we only have a sample size of one here so take that with a grain of salt but let's just see it'll at least tell us if anything's grossly wrong with the offset voltage.

**Dave Jones:** So I've got the max 4239 I've got it set to the 10 milliohm shunt so it's effectively shorted and we're getting about 61 microvolts or thereabouts offset and that's you know fairly typical for a max 4239 base micro current and the OPA189 well there you go 73 microvolts neither here nor there good enough for Australia 67 look at that oh it's going down it's going down dropping oh it's

**Dave Jones:** plummeting. There you go let's turn filtering off there filtering back on. So there you go like 53 you know microvolts like in the order of 50 microvolts so that's fine and we didn't really expect a huge amount of difference cuz as we saw like on average based on the binning it's basically equivalent to the max 4239 but it does have slightly wider offset margins but as I said sample size

**Dave Jones:** of ones but still and that's really shouldn't change with our range so that's our that's our next range and our nano amp range. Whoa our nano amp range has jumped up but that's because the input's not shorted let me short the input there we go it's back down to 50 microvolts nice and just to check the ranges make sure the accuracy is there it's still not you know mucking up

**Dave Jones:** we're generating one micro amp here with my Keithley 2400 source measure unit and we're getting out 0.999 8. Yeah, that's good enough. Um like I haven't like properly calibrated any of this, so like and the MAX4239 0.992.

**Dave Jones:** So, there you go. That's more out than the 189 is, but hey, it's to do with all the other stuff involved, all the other range resistors, everything else. And MAX4239 generating 1 mA on the mA range down or the microamp range down there.

**Dave Jones:** Um yeah, 0.9999. And the OPA189 1.00011. No worries. That's like, you know, 0.01%. Beautiful. Generating 1 amp here OPA189 we're getting 1.0023. I know that's like 0.23%, but I've had an issue with the range resistor on here and that's what I'm yielding at the moment.

**Dave Jones:** So, anyway, we should expect uh very similar with the with this one as well. And the 4239 board 1.0014. Look, don't worry about these values. It's to do with the precision of the 10 m current shunt down here.

**Dave Jones:** As I said, I've been having like batch issues with that. So, yeah, it's all fine. I just wanted to show that it's all working. And I assume it's working, but just want to double check to make sure that the split rail is working just fine.

**Dave Jones:** 2.3 and -2.3. No worries. Okay, so let's measure the noise. First, I'm going to just measure the baseline noise of the system here as I've done in a previous video, but I'm going to include the box and everything else.

**Dave Jones:** So, we'll whack our lid on there and we need to set it up. Now, this is not trivial. Now, I've covered this in more depth in the previous video, but we'll just go over the basics here.

**Dave Jones:** We're going to go over the full span here 0 Hz to 100 kHz here. It's 102, but that's to do with the binning and everything else. Now, of course, what we want here is nanovolts per root hertz or power spectral density, which is uh what is the value which is included in the data sheet.

**Dave Jones:** And uh by default, um uh this is set up for, you know, DB volts RMS. That's not we what we want. That's not a power spectral density. So, the first thing we have to do is go into measurement data over here, and you can see that we're just getting the normal spectrum, but we want the PSD or power spectral density.

**Dave Jones:** Because if we don't choose that and we just use regular spectrum, if we go to scale over here, and then we go into our vertical units, you'll notice that there is no uh power spectral density.

**Dave Jones:** There's no nanovolts per nothing per root hertz, which is noise density. So, we have to go into measurement type here, choose power spectral density, and bingo, volts RMS per root hertz.

**Dave Jones:** But, we don't want the RMS part here, so we go back into the scale. We go into our vertical units, and bingo, volts per root hertz. We now have that or nanovolts per root hertz, but it's it's the same thing.

**Dave Jones:** It's volts per root hertz. It just happens to be nano. So, we can do that, and now we've actually set up our things. Okay, the next thing we want to do is that we want to go into the input type here, and we want to do channel one setup, and we actually want uh grounded input.

**Dave Jones:** We don't want a floating. I won't go into the difference between floating measurements, and we also want uh DC as well. Don't worry about the units there. That's just uh the engineering units.

**Dave Jones:** Um so, we want ground, and we should see Yep, that noise floor drop. Nice. Next, we want to go into scale over here, and we want to auto scale like that.

**Dave Jones:** So, now we get a resemblance of a noise floor, and we're looking at well, it's jumping around, but we're in uh like, you know, tens of e to the minus nine, which is nanovolts per root hertz.

**Dave Jones:** And of course, you know, you want to clean up all this waveform, so you want to go over here, turn on some averaging. Averaging on. How many averages we got?

**Dave Jones:** We've got 10. Uh let's go to 100. There we go. Now we can actually start that, and it will give us a well, it'll average down to a nice waveform.

**Dave Jones:** So that's actually significantly different to what we got with just the BNC 50 ohm input. So let me actually show you that. Let's restart that. There you go. That's much nicer, and that's what we were getting in the previous video, you know, around like 30 nanovolts per root hertz floor.

**Dave Jones:** But unfortunately, you know, just our measurement setup here, this is just I don't know, what is it? IU58 or something. Coax and the box and everything else not going to be perfect, but you can see, plug this back in, there is a significant difference between the noise floors there.

**Dave Jones:** So we've got some peaky-dy stuff happening up here. I'm not sure why it's tailing up here. But hey, that's what we've got to work with. That's fine. Because you've got to remember we've got times 100 gain on here, so the noise floor of our op amps is going to be multiplied by 100.

**Dave Jones:** So you know, we aren't going to be down here. We're going to be, you know, much significantly higher than this. So it's neither here nor there. And we probably want that on a log axis as well.

**Dave Jones:** So we go into scale and log. Thank you very much. There we go. That's better. Let's do that again. And as I mentioned in the previous video, we're only going to get because of our 400 lines of resolution on this thing, we're going to get large steps like that.

**Dave Jones:** We're not going to be accurately able to measure over the full 100 kilohertz bandwidth. But hey, let's actually run with that. So right, so just remember that. That's our baseline noise floor for our setup here.

**Dave Jones:** Okay, so let's put in the 4239 first. I'll hook up the output. Okay, so I'll put it on the 10 milliohm shunt range, so it's effectively, you know, shorted on the input.

**Dave Jones:** And let's whack that in there. And yeah, my battery's on. And of course, uh, it's not just going to be the noise of the op amps because we've got the split rail thing that could introduce noise.

**Dave Jones:** And, you know, we're just measuring the whole system here. So, we're not measuring the actual individual op amp. I'd have to do a, you know, like a proper jig like I did in the, uh, previous video to do that.

**Dave Jones:** I'm more interested in, um, in the actual current microcurrent application. Current? Microcurrent application? Yeah, I said that right. All right, so let's not change anything. Let's start that again.

**Dave Jones:** And so, you know, 44 nanovolts per root hertz, around about there. What's that cursor at? Don't know. Whoa, there we go. There we go. It's jumped up. 6 microvolts per root hertz.

**Dave Jones:** But let's get it, you know, sort of at one of its like lowest points like that. There you go, you know, 3 and 1/2 microvolts per root hertz. Let's call it.

**Dave Jones:** Like that. So, you know, that that's what we get over here. Now, you might be wondering, what is that spike in there? Well, can tell you what, that'll be around about 15 kilohertz, that'd be my guess.

**Dave Jones:** 13 13.3? Why did I know that was the, uh, that it'd be around about that frequency? Because that is the, uh, chopper frequency because these are auto zero amplifiers.

**Dave Jones:** Just call them chopper amps. There is a difference between auto zero and chopper, but we won't go into that. Anyway, it's an auto zero amplifier that has a chopping frequency.

**Dave Jones:** And if you read the MAX4239 data sheet, it tells you that's typically it is like a spread spectrum, uh, kind of thing. It's not one fixed frequency. It did it they add some dither in uh, to it.

**Dave Jones:** But, you know, it's around about, uh, 13 kilohertz. And that's exactly what we're seeing there. And if you actually sweep uh, the microcurrent, you can actually see little bit of low amplitude funny business going on, uh, you know, at around about that 13 to 15 kilohertz mark or whatever.

**Dave Jones:** That's you know, that's a loosey-goosey spec. It's not going to be exactly that, but that's around about the frequency that we're measuring there. So, there you go. So, yeah, I'm going to call that like maybe 3 and 1/2 microvolts per root hertz.

**Dave Jones:** Okay, let's measure the OPA189. Okay, the OPA189. Got to make sure trap for young players that none of this shorts out. So, okay, so we'll whack that in there and once again, I've got it on the uh 10 milliohm current shunt.

**Dave Jones:** Let's run that again, shall we? So, 3.5 microvolts. Ah, it's lower. Oh, our ref What? dBm per hertz. What did I touch? What did I touch? Okay, let's try that again.

**Dave Jones:** Doll. Here we go. Now we're talking 800 900. Yeah, we're talking Yeah, it's it's lower noise. So, we went through from 3 and 1/2 microvolts per root hertz to roundabout one might Let's call it one microvolts per root hertz.

**Dave Jones:** So, yeah, the MAX4239 in this implementation of the microcurrent is about 3 and 1/2 times worse noise than the OPA189. So, yeah, it certainly is quieter and the switching frequency of the OPA189 that I don't think they tell you exactly, but it's up in the like somebody said it's up in like the hundreds of kilohertz range.

**Dave Jones:** They measured it or something. Unfortunately, we can only go to 100 kilohertz with this. Um and you can see a little something in there, but I don't think that's it cuz somebody else said they've that they've measured it in a project and it was in the couple it was in the hundreds of like 250 kilohertz or something.

**Dave Jones:** So, 25 kilohertz, that doesn't sound right. So, there you go. That is a our scale has actually changed a little bit here, but our input range I believe is our range same?

**Dave Jones:** Oh, I have to double-check that. Damn it. There we go. I just set it back to exactly the same range, 10 microvolts per root hertz at the top there.

**Dave Jones:** And you can see, yep, that's 1 microvolt per root hertz, let's call it. So, 1 microvolt per root hertz versus 3.5 microvolts per root hertz. Winner, winner, chicken dinner for the OPA189.

**Dave Jones:** Nice. Even right at the top there, it's only 1 and 1/2, so it's still twice as good. Okay, let's just measure the noise on the scope here. I've got it 20 megahertz bandwidth limited times one input with the coax coming out of the shielded box.

**Dave Jones:** And peak-to-peak we're not that concerned about. We're 2 millivolts per division cuz the Siglent has a 500 microvolt per division front end, but let's just leave it on that scale.

**Dave Jones:** And I see 7.4 millivolts peak-to-peak, but we're more concerned about the RMS noise here. 940 odd microvolts. So, that's for the OPA189. If you want to see the noise floor when the microcurrents are disconnected, there you go.

**Dave Jones:** So, let's just reset those stats, and that's the noise floor with the microcurrent completely disconnected inside the shielded box. So, we're only down around 90 microvolts RMS there. Reset the statistics, max 4239.

**Dave Jones:** See, it is significantly more, 12 and 1/2 millivolts peak-to-peak, and 1.6 millivolts RMS noise. So, there you go. It's not like 50% worse or something like that than the OPA189.

**Dave Jones:** So, significant noise improvements just using the OPA189 in the standard microcurrent circuit configuration. Nice. Okay, I'm just curious to see how much noise was actually generated by the 200K resistors there and the split rail generator.

**Dave Jones:** Basically, because we are we have seen noise greater than what you'd expect for the baseline noise of the OPA189 Uh plus the time multiplied by the times 100 gain.

**Dave Jones:** So, we're going to get some I mean the noise of course you're going to get your thermal Johnson noise on your resistors, but they're not actually directly coupled into the input as such.

**Dave Jones:** So, you're talking about through the power rails common mode rejection ratio all that sort of stuff. Anyway, I've I've left the resistors in there cuz it's a nothing burger, but I've removed the LMV321 op-amp because unfortunately you can't just whack in these OPA189s in here and a higher voltage you get it to work because the LMV 321 op-amp that only has a maximum supply rail of like 5

**Dave Jones:** and 1/2 volts as an A version which I think goes to 6 or something, but yeah basically yeah you can't just do that. You'll have to get another op-amp if you want to get like it operate this thing from say a 9-V battery or something.

**Dave Jones:** Anyway, yeah I've done that and now I'm going to power it from split rails here and we'll see how it goes. So, it's slightly higher voltage 6 volts now, but that's neither here nor there.

**Dave Jones:** If we go back to the scope reset our stats. There you go peak to peak what we getting before? I think it it has slightly dropped 910 weren't we getting like 980 or something mean RMS before?

**Dave Jones:** So, it has dropped somewhat. Okay, I can't remember exactly where we were before on the frequency, but it has dropped a little bit in the does its auto calibration there periodically.

**Dave Jones:** So, we're a bit under where we were before, but like it's not much in it. It should maybe it'll go under one here, but yeah it's you know there's not a huge amount in it.

**Dave Jones:** So, basically the op-amp and those resistors weren't really contributing much to that which is as you'd expect because as I said it goes through the power rail system and then it's effect on the op-amp itself has to do with the power supply rejection ratio.

**Dave Jones:** So, it's not actually coupled into the input as such it even though it's a flight like it's introducing noise into the ground reference the ground reference is still the reference.

**Dave Jones:** So even if the reference is jiggling around due to the noise, it's you know, it's not introducing much. So there you go. That's doing some basic test on the OPA189 op amp and as expected I it was you know, relatively significantly lower noise than the MAX4239 and actual worthwhile upgrade for not much real change power really and it is effectively a drop in replacement for the micro current although as I said

**Dave Jones:** unfortunately that LMV321 op amp that one will have to be changed to one that supports a higher rail voltage. So off hand I don't know just a regular LM321 might do the job.

**Dave Jones:** Anyway, I need to investigate that but if you got a micro current and you want to like have a drop in replacement for lower noise and higher bandwidth this looks like a quite a decent option.

**Dave Jones:** Now of course I haven't actually checked the bandwidth yet or other dynamic performance aspects of it. This video is long enough so I just want to measure the noise make sure the op amps work make sure the micro current gold like still works it works at DC and its noise is lower and everyone's happy.

**Dave Jones:** So I think we have a pretty decent new candidate. I I don't expect any show stoppers in the dynamic performance aspect of this. In fact it could be potentially even better because as we saw the actual chopper frequency is up you know, past 200 kilohertz or something like that.

**Dave Jones:** So in theory you could put a low pass filter on the output as well even more existing micro current or in a new design micro current which we're working on here.

**Dave Jones:** You can put in maybe an optional switched output filter so that the performance of it is completely below the chopping frequency of the zero drift amplifiers in here because unfortunately the micro current it was that you know like 13 to 15 kilohertz or so it's pretty much you know bang on in like the measurement range that you're trying to do so even if you didn't want the increased

**Dave Jones:** bandwidth you could still get the same bandwidth as existing micro current gold but actually put in a low pass filter on the output and have that chopper frequency outside the operational range so right there another big benefit so yeah I'm I'm liking look of this so OPA 189 it's pretty schmick so anyway hope you enjoyed that and found it interesting if you did please give it a

**Dave Jones:** big thumbs up and let me know down below how you're liking this new series in quote marks which will be just random videos going forth it's not some official design project design series it's just I'm doing you know the occasional rando videos so this is part three and I'm sure there'll be more parts specially like another one dynamic performance something so let me know if you want to

**Dave Jones:** see that in the comments down below and as always don't forget all my alternative platforms I'm on library I'm on bit shoot I'm on daily motion I'm on video I'm on my own website you can even download the 720p podcast from my own web server on my RSS feed and all that sort of stuff so yep there's plenty of alternatives outside of YouTube and as always if you want to discuss EV blog

**Dave Jones:** forum is the place to do it you know the comments do but forums are better than comments anyway catch you next time
