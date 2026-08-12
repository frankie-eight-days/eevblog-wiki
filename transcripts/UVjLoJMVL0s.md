---
video_id: UVjLoJMVL0s
title: EEVblog #1328 - uCurrent OPA189 Measurements
url: https://www.youtube.com/watch?v=UVjLoJMVL0s
source: youtube-asr
---

**Dave Jones:** Hi, in a previous video linked in down below and up here and at the end if you haven't seen it, this is part of the series of designing a better microcurrent. And the last video we took a look at the OPA189

**Dave Jones:** and how it looked like in most respects it was better than the MAX42384239 that we use in the microcurrent. So, I ordered some. Here you go. OPA189IDBVR. This is the SOT23 five package. It is available in different packages, but I

**Dave Jones:** got the SOT23 five because it is actually directly pin out compatible with my existing microcurrent. So, what we're going to do in this video is we're going to actually compare the original design microcurrent to one that uses the

**Dave Jones:** drop-in replacement OPA189 and measure the noise and other performance characteristics of it. Let's go. But, it's actually not completely pin out compatible because here's the existing MAX4239. It's actually a six-pin SO. You can see it's got three pins on the top here, but

**Dave Jones:** the OPA189 only has two pins on the top. It's a five-pin SOT23 package. The only thing it's missing is the enable disable pin, which we don't actually use on this. We just tie it high. So, we can simply

**Dave Jones:** simply remove the existing chips and solder in the new one. Doesn't matter. Beauty. So, to make this comparison as fair as possible, what I've got here is two identical boards from actually the same batch, just a serial number apart.

**Dave Jones:** So, they use all the same parts that you know, come from the same reels and everything. So, they're basically as identical as you can get, but one uses the 189, one uses the original MAX4239. Now, the problem is though I can't use

**Dave Jones:** the coin cell battery to do the comparison test because the OPA189 has 4.5 volts minimum supply voltage, whereas the MAX4239 can go down much lower like 2.3 V or something if I recall correctly is the dropout voltage, something like that.

**Dave Jones:** Anyway, but it only goes to 5.5 V maximum. So, I'm going to run this from a 4.5 V battery, so just enough. I've got three AAA's here, which will give us if I use brand new cells, it'll give us just over

**Dave Jones:** 4.5 V. So, yeah, that'll be good enough for Australia. Right, so we're going to start out by measuring the noise. Now, as I said previous video linked in down below where I've actually really quite a while ago this video is where I use my

**Dave Jones:** HP 35 660A dynamic signal analyzer to actually measure noise floor of op-amps. And that's a really great video from about I think it's from about like 2015 20 minutes onwards in the video is where I show you extensively how to set up a

**Dave Jones:** dynamic signal analyzer to measure noise to match the data sheet noise density actually, which is nanovolts per root hertz. Now, to do this of course you can't just have the boards flapping around in the breeze on your bench.

**Dave Jones:** You've got to have a nice diecast shielded box like this. So, I've got that with a BNC output going into our input. So, we'll put the batteries and everything else inside the diecast box just so we eliminate any external noise,

**Dave Jones:** any you know, external 50 hertz. All right, first thing we're going to do is just measure the power supply current because the OPA189 is supposed to take more current. So, let's get the old one 4239. I've actually removed the dropper

**Dave Jones:** resistor for the LED here, otherwise the LED will draw like you know, 7 milliamps or you know, a huge amount of current like that. So, let's give it a whirl. This is the MAX 4239, 1.31 milliamps. And the 189?

**Dave Jones:** Ah, 2.68. So, you know, what what 1.3 milliamps more overall for the two op-amps. And you know there's some residual uh you know other current which will remain the same but yeah you know that's it's neither here nor there

**Dave Jones:** really unless you're after some ultra low power design so nice. Now I know that we only have a sample size of one here so take that with a grain of salt but let's just see it'll at least tell us if

**Dave Jones:** anything's grossly wrong with the offset voltage. So I've got the max 4239 I've got it set to the 10 milliohm shunt so it's effectively shorted and we're getting about 61 microvolts or thereabouts offset and that's you know fairly

**Dave Jones:** typical for a max 4239 base micro current and the OPA189 well there you go 73 microvolts neither here nor there good enough for Australia 67 look at that oh it's going down it's going down dropping oh it's plummeting. There you go let's turn

**Dave Jones:** filtering off there filtering back on. So there you go like 53 you know microvolts like in the order of 50 microvolts so that's fine and we didn't really expect a huge amount of difference cuz as we saw like on average based on the binning

**Dave Jones:** it's basically equivalent to the max 4239 but it does have slightly wider offset margins but as I said sample size of ones but still and that's really shouldn't change with our range so that's our that's our next range and our nano amp

**Dave Jones:** range. Whoa our nano amp range has jumped up but that's because the input's not shorted let me short the input there we go it's back down to 50 microvolts nice and just to check the ranges make sure the accuracy is there

**Dave Jones:** it's still not you know mucking up we're generating one micro amp here with my Keithley 2400 source measure unit and we're getting out 0.999 8. Yeah, that's good enough. Um like I haven't like properly calibrated any of this, so like

**Dave Jones:** and the MAX4239 0.992. So, there you go. That's more out than the 189 is, but hey, it's to do with all the other stuff involved, all the other range resistors, everything else. And MAX4239 generating 1 mA on the mA range

**Dave Jones:** down or the microamp range down there. Um yeah, 0.9999. And the OPA189 1.00011. No worries. That's like, you know, 0.01%. Beautiful. Generating 1 amp here OPA189 we're getting 1.0023. I know that's like 0.23%, but I've had an issue with the

**Dave Jones:** range resistor on here and that's what I'm yielding at the moment. So, anyway, we should expect uh very similar with the with this one as well. And the 4239 board 1.0014. Look, don't worry about these values. It's to do with the precision of the

**Dave Jones:** 10 m current shunt down here. As I said, I've been having like batch issues with that. So, yeah, it's all fine. I just wanted to show that it's all working. And I assume it's working, but just want to

**Dave Jones:** double check to make sure that the split rail is working just fine. 2.3 and -2.3. No worries. Okay, so let's measure the noise. First, I'm going to just measure the baseline noise of the system here as I've done in a previous video,

**Dave Jones:** but I'm going to include the box and everything else. So, we'll whack our lid on there and we need to set it up. Now, this is not trivial. Now, I've covered this in more depth in the previous video, but we'll just go over the basics

**Dave Jones:** here. We're going to go over the full span here 0 Hz to 100 kHz here. It's 102, but that's to do with the binning and everything else. Now, of course, what we want here is nanovolts per root hertz or power spectral density, which

**Dave Jones:** is uh what is the value which is included in the data sheet. And uh by default, um uh this is set up for, you know, DB volts RMS. That's not we what we want. That's not a power spectral

**Dave Jones:** density. So, the first thing we have to do is go into measurement data over here, and you can see that we're just getting the normal spectrum, but we want the PSD or power spectral density. Because if we don't choose that and we

**Dave Jones:** just use regular spectrum, if we go to scale over here, and then we go into our vertical units, you'll notice that there is no uh power spectral density. There's no nanovolts per nothing per root hertz, which is noise density. So, we have to

**Dave Jones:** go into measurement type here, choose power spectral density, and bingo, volts RMS per root hertz. But, we don't want the RMS part here, so we go back into the scale. We go into our vertical units, and bingo, volts per root hertz.

**Dave Jones:** We now have that or nanovolts per root hertz, but it's it's the same thing. It's volts per root hertz. It just happens to be nano. So, we can do that, and now we've actually set up our things. Okay, the next thing we want to

**Dave Jones:** do is that we want to go into the input type here, and we want to do channel one setup, and we actually want uh grounded input. We don't want a floating. I won't go into the difference between floating

**Dave Jones:** measurements, and we also want uh DC as well. Don't worry about the units there. That's just uh the engineering units. Um so, we want ground, and we should see Yep, that noise floor drop. Nice. Next, we want to go into scale over here, and

**Dave Jones:** we want to auto scale like that. So, now we get a resemblance of a noise floor, and we're looking at well, it's jumping around, but we're in uh like, you know, tens of e to the minus nine, which is

**Dave Jones:** nanovolts per root hertz. And of course, you know, you want to clean up all this waveform, so you want to go over here, turn on some averaging. Averaging on. How many averages we got? We've got 10. Uh let's go to 100. There we go. Now we

**Dave Jones:** can actually start that, and it will give us a well, it'll average down to a nice waveform. So that's actually significantly different to what we got with just the BNC 50 ohm input. So let me actually show you that. Let's restart

**Dave Jones:** that. There you go. That's much nicer, and that's what we were getting in the previous video, you know, around like 30 nanovolts per root hertz floor. But unfortunately, you know, just our measurement setup here, this is just I

**Dave Jones:** don't know, what is it? IU58 or something. Coax and the box and everything else not going to be perfect, but you can see, plug this back in, there is a significant difference between the noise floors there. So we've got some peaky-dy

**Dave Jones:** stuff happening up here. I'm not sure why it's tailing up here. But hey, that's what we've got to work with. That's fine. Because you've got to remember we've got times 100 gain on here, so the noise floor of our op amps

**Dave Jones:** is going to be multiplied by 100. So you know, we aren't going to be down here. We're going to be, you know, much significantly higher than this. So it's neither here nor there. And we probably want that on a log axis as well. So we

**Dave Jones:** go into scale and log. Thank you very much. There we go. That's better. Let's do that again. And as I mentioned in the previous video, we're only going to get because of our 400 lines of resolution on this

**Dave Jones:** thing, we're going to get large steps like that. We're not going to be accurately able to measure over the full 100 kilohertz bandwidth. But hey, let's actually run with that. So right, so just remember that. That's our baseline

**Dave Jones:** noise floor for our setup here. Okay, so let's put in the 4239 first. I'll hook up the output. Okay, so I'll put it on the 10 milliohm shunt range, so it's effectively, you know, shorted on the input. And let's whack that in

**Dave Jones:** there. And yeah, my battery's on. And of course, uh, it's not just going to be the noise of the op amps because we've got the split rail thing that could introduce noise. And, you know, we're just measuring the whole system here.

**Dave Jones:** So, we're not measuring the actual individual op amp. I'd have to do a, you know, like a proper jig like I did in the, uh, previous video to do that. I'm more interested in, um, in the actual current microcurrent application.

**Dave Jones:** Current? Microcurrent application? Yeah, I said that right. All right, so let's not change anything. Let's start that again. And so, you know, 44 nanovolts per root hertz, around about there. What's that cursor at? Don't know. Whoa, there we go. There we go. It's jumped

**Dave Jones:** up. 6 microvolts per root hertz. But let's get it, you know, sort of at one of its like lowest points like that. There you go, you know, 3 and 1/2 microvolts per root hertz. Let's call it. Like that. So, you know, that that's

**Dave Jones:** what we get over here. Now, you might be wondering, what is that spike in there? Well, can tell you what, that'll be around about 15 kilohertz, that'd be my guess. 13 13.3? Why did I know that was the,

**Dave Jones:** uh, that it'd be around about that frequency? Because that is the, uh, chopper frequency because these are auto zero amplifiers. Just call them chopper amps. There is a difference between auto zero and chopper, but we won't go into

**Dave Jones:** that. Anyway, it's an auto zero amplifier that has a chopping frequency. And if you read the MAX4239 data sheet, it tells you that's typically it is like a spread spectrum, uh, kind of thing. It's not one fixed frequency. It did it

**Dave Jones:** they add some dither in uh, to it. But, you know, it's around about, uh, 13 kilohertz. And that's exactly what we're seeing there. And if you actually sweep uh, the microcurrent, you can actually see little bit of low amplitude funny

**Dave Jones:** business going on, uh, you know, at around about that 13 to 15 kilohertz mark or whatever. That's you know, that's a loosey-goosey spec. It's not going to be exactly that, but that's around about the frequency that we're measuring there. So, there you go. So,

**Dave Jones:** yeah, I'm going to call that like maybe 3 and 1/2 microvolts per root hertz. Okay, let's measure the OPA189. Okay, the OPA189. Got to make sure trap for young players that none of this shorts out. So, okay, so we'll whack

**Dave Jones:** that in there and once again, I've got it on the uh 10 milliohm current shunt. Let's run that again, shall we? So, 3.5 microvolts. Ah, it's lower. Oh, our ref What? dBm per hertz. What did I touch? What did I touch? Okay, let's try that

**Dave Jones:** again. Doll. Here we go. Now we're talking 800 900. Yeah, we're talking Yeah, it's it's lower noise. So, we went through from 3 and 1/2 microvolts per root hertz to roundabout one might Let's call it one microvolts per root

**Dave Jones:** hertz. So, yeah, the MAX4239 in this implementation of the microcurrent is about 3 and 1/2 times worse noise than the OPA189. So, yeah, it certainly is quieter and the switching frequency of the OPA189 that I don't think they tell you

**Dave Jones:** exactly, but it's up in the like somebody said it's up in like the hundreds of kilohertz range. They measured it or something. Unfortunately, we can only go to 100 kilohertz with this. Um and you can see a little something in

**Dave Jones:** there, but I don't think that's it cuz somebody else said they've that they've measured it in a project and it was in the couple it was in the hundreds of like 250 kilohertz or something. So, 25 kilohertz, that doesn't sound right. So,

**Dave Jones:** there you go. That is a our scale has actually changed a little bit here, but our input range I believe is our range same? Oh, I have to double-check that. Damn it. There we go. I just set it back

**Dave Jones:** to exactly the same range, 10 microvolts per root hertz at the top there. And you can see, yep, that's 1 microvolt per root hertz, let's call it. So, 1 microvolt per root hertz versus 3.5 microvolts per root hertz. Winner,

**Dave Jones:** winner, chicken dinner for the OPA189. Nice. Even right at the top there, it's only 1 and 1/2, so it's still twice as good. Okay, let's just measure the noise on the scope here. I've got it 20 megahertz bandwidth limited times one

**Dave Jones:** input with the coax coming out of the shielded box. And peak-to-peak we're not that concerned about. We're 2 millivolts per division cuz the Siglent has a 500 microvolt per division front end, but let's just leave it on that scale. And I

**Dave Jones:** see 7.4 millivolts peak-to-peak, but we're more concerned about the RMS noise here. 940 odd microvolts. So, that's for the OPA189. If you want to see the noise floor when the microcurrents are disconnected, there you go. So, let's just reset those stats, and that's the

**Dave Jones:** noise floor with the microcurrent completely disconnected inside the shielded box. So, we're only down around 90 microvolts RMS there. Reset the statistics, max 4239. See, it is significantly more, 12 and 1/2 millivolts peak-to-peak, and 1.6 millivolts RMS noise. So, there you go.

**Dave Jones:** It's not like 50% worse or something like that than the OPA189. So, significant noise improvements just using the OPA189 in the standard microcurrent circuit configuration. Nice. Okay, I'm just curious to see how much noise was actually generated by the 200K

**Dave Jones:** resistors there and the split rail generator. Basically, because we are we have seen noise greater than what you'd expect for the baseline noise of the OPA189 Uh plus the time multiplied by the times 100 gain. So, we're going to get some I

**Dave Jones:** mean the noise of course you're going to get your thermal Johnson noise on your resistors, but they're not actually directly coupled into the input as such. So, you're talking about through the power rails common mode rejection ratio all that sort of stuff. Anyway, I've

**Dave Jones:** I've left the resistors in there cuz it's a nothing burger, but I've removed the LMV321 op-amp because unfortunately you can't just whack in these OPA189s in here and a higher voltage you get it to work because the LMV 321 op-amp that

**Dave Jones:** only has a maximum supply rail of like 5 and 1/2 volts as an A version which I think goes to 6 or something, but yeah basically yeah you can't just do that. You'll have to get another op-amp if you want to get

**Dave Jones:** like it operate this thing from say a 9-V battery or something. Anyway, yeah I've done that and now I'm going to power it from split rails here and we'll see how it goes. So, it's slightly higher voltage 6 volts now, but that's

**Dave Jones:** neither here nor there. If we go back to the scope reset our stats. There you go peak to peak what we getting before? I think it it has slightly dropped 910 weren't we getting like 980 or something mean RMS before? So, it has dropped

**Dave Jones:** somewhat. Okay, I can't remember exactly where we were before on the frequency, but it has dropped a little bit in the does its auto calibration there periodically. So, we're a bit under where we were before, but like it's not

**Dave Jones:** much in it. It should maybe it'll go under one here, but yeah it's you know there's not a huge amount in it. So, basically the op-amp and those resistors weren't really contributing much to that which is as you'd expect because as I said it

**Dave Jones:** goes through the power rail system and then it's effect on the op-amp itself has to do with the power supply rejection ratio. So, it's not actually coupled into the input as such it even though it's a flight like it's

**Dave Jones:** introducing noise into the ground reference the ground reference is still the reference. So even if the reference is jiggling around due to the noise, it's you know, it's not introducing much. So there you go. That's doing some basic test on the OPA189 op amp and as

**Dave Jones:** expected I it was you know, relatively significantly lower noise than the MAX4239 and actual worthwhile upgrade for not much real change power really and it is effectively a drop in replacement for the micro current although as I said

**Dave Jones:** unfortunately that LMV321 op amp that one will have to be changed to one that supports a higher rail voltage. So off hand I don't know just a regular LM321 might do the job. Anyway, I need to investigate that but if you got a micro

**Dave Jones:** current and you want to like have a drop in replacement for lower noise and higher bandwidth this looks like a quite a decent option. Now of course I haven't actually checked the bandwidth yet or other dynamic performance aspects of it.

**Dave Jones:** This video is long enough so I just want to measure the noise make sure the op amps work make sure the micro current gold like still works it works at DC and its noise is lower and everyone's happy. So I think we have a

**Dave Jones:** pretty decent new candidate. I I don't expect any show stoppers in the dynamic performance aspect of this. In fact it could be potentially even better because as we saw the actual chopper frequency is up you know, past 200 kilohertz or

**Dave Jones:** something like that. So in theory you could put a low pass filter on the output as well even more existing micro current or in a new design micro current which we're working on here. You can put in maybe an optional switched output

**Dave Jones:** filter so that the performance of it is completely below the chopping frequency of the zero drift amplifiers in here because unfortunately the micro current it was that you know like 13 to 15 kilohertz or so it's pretty much you

**Dave Jones:** know bang on in like the measurement range that you're trying to do so even if you didn't want the increased bandwidth you could still get the same bandwidth as existing micro current gold but actually put in a low pass filter on

**Dave Jones:** the output and have that chopper frequency outside the operational range so right there another big benefit so yeah I'm I'm liking look of this so OPA 189 it's pretty schmick so anyway hope you enjoyed that and found it

**Dave Jones:** interesting if you did please give it a big thumbs up and let me know down below how you're liking this new series in quote marks which will be just random videos going forth it's not some official design project design series it's just

**Dave Jones:** I'm doing you know the occasional rando videos so this is part three and I'm sure there'll be more parts specially like another one dynamic performance something so let me know if you want to see that in the comments down below and

**Dave Jones:** as always don't forget all my alternative platforms I'm on library I'm on bit shoot I'm on daily motion I'm on video I'm on my own website you can even download the 720p podcast from my own web server on my RSS feed and all that

**Dave Jones:** sort of stuff so yep there's plenty of alternatives outside of YouTube and as always if you want to discuss EV blog forum is the place to do it you know the comments do but forums are better than comments anyway catch you next time
