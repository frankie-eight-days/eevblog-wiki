---
video_id: Nj-Q8FQxHhU
title: EEVblog #961 - Monkey Debouncing
url: https://www.youtube.com/watch?v=Nj-Q8FQxHhU
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 36, "3": 56, "4": 76, "5": 88, "6": 108, "7": 128, "8": 144, "9": 160, "10": 177, "11": 193, "12": 213, "13": 233, "14": 253, "15": 270, "16": 290, "17": 306, "18": 322, "19": 334, "20": 350, "21": 366, "22": 382, "23": 399, "24": 415, "25": 431, "26": 447, "27": 472, "28": 488, "29": 508, "30": 524, "31": 545, "32": 565, "33": 581, "34": 601, "35": 625, "36": 642, "37": 658, "38": 674, "39": 690, "40": 715, "41": 731, "42": 743, "43": 759, "44": 775, "45": 787, "46": 808, "47": 824, "48": 840, "49": 856, "50": 872, "51": 893, "52": 909, "53": 929, "54": 949, "55": 970, "56": 990, "57": 1002, "58": 1022, "59": 1038, "60": 1058, "61": 1075, "62": 1087, "63": 1107, "64": 1123, "65": 1144, "66": 1156, "67": 1172}
---

**Dave Jones:** Hi. Do you remember Probes the Monkey from the Batteryzer videos? Well, let's say that you wanted to use Probes the Monkey for a test where you actually wanted to count the number of times that he clapped like this. And he usually uses cymbals, but, you know, these are

**Dave Jones:** actually pretty loud, and well, you don't want that yapping on for hours and hours. So I've removed these little cymbals here. I've screwed in some crimped wires into here, so that when they make contact, bingo! We close the circuit, and we can count the number of times that Probes the Monkey actually claps.

**Dave Jones:** Here we go. Go Probes! Yeah! So you might think this is a pretty easy thing to do, just have a circuit that counts the number of times that these contacts close like this. So you might think if you've got a frequency or a universal counter

**Dave Jones:** in your lab, a universal counter is not just a frequency counter, it's universal. It counts stuff. So you could actually hook up to your frequency counter like this, and put it into what's called a totalize mode like this, which actually just counts up the number of times that the input goes through the

**Dave Jones:** threshold. In this case I've got a power from a couple of AA batteries, just got a pull-up resistor here, so every time that this shorts out, it shorts out to ground and it should count the number of pulses. But let's actually try it, shall we?

**Dave Jones:** Hmm, let's just manually do it for starters. Oh! Oops, 225! Oops! You're no doubt familiar with this problem, it's contact bounce. When these contacts close like this, you don't just get one edge, you get multiple edges. And we can actually have a look at that

**Dave Jones:** if we actually hook our scope up here to our input. Let's have a squeeze, shall we? And put in single shot capture mode, you'll notice it was high there, and let's just capture, boom! One little pulse like that, look at that! We've actually got not just one, not just the one nice

**Dave Jones:** we do have actually one nice pulse there, but after that look at all the crap that we've got there. There's lots of stuff happening with the contacts here, the screws, the surface you know, corrosion on the screws, and all sorts of weird and wonderful stuff.

**Dave Jones:** Look at that, I mean, that's why we're getting hundreds of pulses counted at any one time on our frequency counter here. So we have to debounce those contacts. So if we've got a switch like this with our typical pull-up resistor, we're going to get

**Dave Jones:** contact bounce or switch bounce on those contacts. Pretty much doesn't matter what switch it is. Any mechanical switch, be it a proper mechanical one that you actually buy, a push button or toggle or whatever, or a probes the monkey here. Well, how do we actually debounce this?

**Dave Jones:** Well, one of the obvious and common ways to do it is to add a capacitor across the switch, and that's exactly what I've done here. I've added a 330 microfarad capacitor on there, I think I've got a 5k6 pull-up on there Let's give it a try now.

**Dave Jones:** Alright, here you go probes, let's count Oops, we're already screwed. We've got 2 here, it counted 2 instead of 1. And, but look at our waveform now. We now have a beautiful classic exponential capacitor rise like this classic RC time constant you're familiar with.

**Dave Jones:** And check out that edge that we've got there, it is beautiful! Look at that, there's no contact bounce in there whatsoever, because now that we've got the capacitor across the switch, when you activate the switch, the very first instant that switch goes low, then it shorts out the capacitor, and then

**Dave Jones:** the capacitor will remain a short circuit and only charge up based on the resistor value and the capacitor value that classic RC time constant like we get like that. So that is why we only get the one switch transition in there which is absolutely beautiful, but

**Dave Jones:** why on earth did we get a count of 2 on here? We got a count of 2 on here because our universal counter here is not a Schmitt trigger input. I've done a whole video on Schmitt triggers so click here if you want to see that Schmitt trigger video that explains

**Dave Jones:** everything in detail. This counter is not designed to debounce inputs, but as I pointed out in my Schmitt trigger video and demonstrated when you've got a slow rising input signal like that into any sort of digital logic input, which this counter effectively is really, ultimately, then it can

**Dave Jones:** cause multiple transitions due to noise on that signal. But I think what we might have here is a pebcac, a problem exists between keyboard and chair, i.e. me. I haven't set up this universal counter properly, and I don't think I've shown setting up a universal

**Dave Jones:** counter before. Let's take a look at it. Now, you might be able to just see under there that there's a 100 kHz filter, I've got that switched on so it's a low pass filter, filters out any noise above 100 kHz. But, you know, we could have some higher frequency noise

**Dave Jones:** on here for the threshold and stuff like that, so that could still be an issue. But let's take a look at the setup, shall we? You'll notice that there's an AC-DC mode here, DC LED is not on, so we're actually in AC mode.

**Dave Jones:** So we're AC coupling our input. So our input here is being AC coupled, we don't know what the value is and all that sort of stuff, so we don't want that. What we want is DC mode like this, okay? And then let's go and have a look

**Dave Jones:** at our trigger. Okay, our auto-trigger's off, that'll just reset the thing I might demo that later. But look, our threshold is set at 0 volts. So now we're in DC mode, we definitely don't want our threshold at 0 volts, because that'll be right down the bottom here, and you might see that there's actually a time

**Dave Jones:** you know, there's some noise down there, so if our threshold was 0, that's not going to work. Actually, let's try that and see what we get, shall we? So let's go back into our run mode and nah, it's actually not even working at all.

**Dave Jones:** So yeah, we get absolutely nothing there. So let's go back in and set our threshold, what we want is DC mode our level, let's say we want it to trigger at say 1 volt, this is 500 millivolts per division, say like right in the middle of that, on the positive going edge

**Dave Jones:** you can set it on the negative going edge, yeah, it doesn't matter. In fact, in this case you probably would want the negative going edge, because you want the count to occur exactly when the switch contacts come together. So let's go in, and we'll

**Dave Jones:** set that up to 1 volt, there we go and positive, it's currently set to positive edge, we'll change that, we'll have negative edge, thank you very much. What else have we got? Sensitivity high, low, medium, I can't remember off the top of my head what that

**Dave Jones:** actually does, it could be some sort of window, hey, I'll have to read the manual on that, so RTFM. Anyway, let's leave it to high, shall we? So we're all hunky-dory ready to go, let's try that again. Come on probes, here we go.

**Dave Jones:** Let's try it, oh! Cheated! Hang on, there we go, we're running, and it should instantly count the split second that we touch these together. Boom! 1, and it's counted up 1! Beautiful! So now we're working. Let's do it again. 2, 3, oh, no, see?

**Dave Jones:** See? There's our second problem. If we try and do this too quickly, it's not charging up to that 1 volt. So obviously, you know, we have to choose our capacitor value correctly, so if you had something, it depends on your object that you're having.

**Dave Jones:** So if you've got an RC debounce circuit, you really need to know how fast your input's occurring, all that sort of stuff. So if you've got a fairly controlled device like probes, the monkey, you know how often he's going to clap and stuff like that, and you can then tweak your capacitor value to do that.

**Dave Jones:** Obviously, he's not going to count things that are so quick that that capacitor can't recharge. Okay, so let's try and capture this on the scope. Let's just do, look, we can see that, whoa, like that all these multiple pulses here didn't count because we didn't get to our

**Dave Jones:** 1 volt threshold that we set up on here. So yeah, it's possible to use our universal counter, tweak the capacitor value, tweak our trigger sensitivity, all that sort of stuff for our MUT, our monkey under test here, good old probes the monkey, and, you know, get sort of the output that we actually

**Dave Jones:** want from this thing. So let's turn him on, let's see what we get. There we go. So we only get him to count once per, you know, like cycle, so to speak. So he doesn't count those individual pulses there. So that's actually pretty good.

**Dave Jones:** You could say that, you know, it depends on what you counted. Did you want to actually count individual contacts or did you want to count cycles of probes the monkey? So cycle's not too bad to go, oh no, there we go, what happened there?

**Dave Jones:** Whoa, you see that jump up? I think we've got problem number 3. You'll notice that when probes is chirping like this, the count can actually go up. This is caused by, look, look at that! The contacts aren't even closing. We've got our big

**Dave Jones:** antenna wires here picking up coupling from, oh, probes the monkey is causing some counts to go up. So we're picking up just crap even though he's not doing anything. So we have a noise pickup issue in our system. You know, just testing something like probes the monkey, there's a lot of tweaking and messing

**Dave Jones:** around involved in getting something like this working. So we certainly have a problem there with probes, just the movement of his head action and his chirping causes noise pickup in the wires and we can solve that. That's not something that I want to solve today.

**Dave Jones:** But just be aware that that's a problem that we encountered in this particular test setup, and that might need its own solution. Shielded cables, whatever. But there's another potential problem that I want to discuss. We're probably not going to see it here today, it might be hard to demo.

**Dave Jones:** But have a look, this is your traditional RC debounce circuit, the switch directly across the capacitor. Now when you short out the switch of course you short out the, when you press the switch, you short out the capacitor and then when you release the switch, the capacitor slowly starts to charge up until it reaches

**Dave Jones:** your supply voltage up here. And we've got a 330 microfarad cap on there, it's a fairly sizable cap, it's going to store, you know, a reasonable amount of energy in there. So if we let it charge all the way back up to say our 3 volts from our 2 AA batteries here, and then we short it out

**Dave Jones:** again, we're generating a large short circuit current through that switch there. And that could also cause interference problems similar to what we're seeing here, because a very fast high current discharge like this generates lots of EMI, lots of electromagnetic interference lots of big loop current in here, with the switch and everything else

**Dave Jones:** through these wires, through these very long wires that we've got here massive loop area, and that could upset your measurements as well. And, you know, I'd have to go to some effort to design something to actually show you that working. So, to, you know, this RC

**Dave Jones:** circuit, your traditional one, you know, works reasonably well, but it does have that problem of generating potentially a large current, especially if you're using a large value cap in here. So you're better off, of course, using a much larger value pull-up resistor and a smaller value capacitor to avoid that problem.

**Dave Jones:** But just be aware of that. So to solve that problem, you can put an additional series resistor in here between the switch and the cap, so that when you press the switch, you don't directly short out the capacitor. Instead, you're discharging it through

**Dave Jones:** R2. And R2's, you know, generally going to be a smaller value than R1, so you want it to discharge fairly quickly. Once again, depends on your monkey under test, and what you're actually, and what the timings are of your, you know, to choose that capacitor value correctly

**Dave Jones:** specifically for your particular setup. You'd also have to choose R2 to get exactly the right conditions as well. And I won't go through all the particular calculations of RC time constants and things like that, because this is not a really an in-depth switch debounce tutorial.

**Dave Jones:** But suffice it to say that can solve any potential issue with shorting out a large value of capacitance here. But of course, you might have noticed that now R2 is in series with R1 for your charging circuit, and when you're driving a Schmitt trigger, depending on the threshold levels, the upper and lower

**Dave Jones:** threshold levels for the Schmitt trigger, it might cause issues with the values you choose and everything else. So another common technique to avoid that is to put a diode in parallel with R2 here. It's got to be in that orientation. So it effectively

**Dave Jones:** bypasses R2 when you're charging up, but it reverse-vices and does nothing when you're discharging like this. So it can just charge up faster and basically almost takes R2 out of the equation there in terms of charging. So you might have to do something like that.

**Dave Jones:** But as you can see, there's a lot of, you know, little things that can go wrong with just a simple RC debounce. A lot of things to consider depending on your test setup, your monkey under test, your MUT. And it really does require, you know, a little bit of thought.

**Dave Jones:** I mean, you don't have to go through the charge equations for the capacitor and everything else. You can just sort of, you know, do basic back-of-the-envelope calculation rules of thumb, or just even trial and error. Oh, the 330 microfarad doesn't work. I think it's a bit high.

**Dave Jones:** It's not detecting multiple things. Oh, or at 220 or 100 mic, or, you know, you might increase your pull-up resistor value or something like that. Just, you know, experimentation can get the job done, but so can calculation. As long as you know the variables and the threshold levels you're setting up and all that sort of stuff.

**Dave Jones:** So there you go. That's just setting up a universal counter like this to measure something like Probes the Monkey. But we still have that issue with that noise. Hmm. And if you actually have a look at the waveform, you can see it's quite noisy while

**Dave Jones:** Probes the Monkey's actually operating. There's a fair bit of superimposed noise from the motor, whereas if I stop Probes and do that manually, you can see it's much, much cleaner. So yeah, Probes is generating a fair bit of noise there, and you could really come

**Dave Jones:** aguncer on that if you hadn't So there you go, that's certainly worth watching out for. When you're testing monkeys like this, they're pesky little things, let me tell you. So through a combination of settings now, I seem to have got a system that

**Dave Jones:** counts reasonably well. It counts, you'll notice that it counts up on the 1.5 volt threshold voltage set, and I've got medium sensitivity on this, and positive rising edge, I've got the 100 kilohertz filter on, so it's only counting cycles when he actually goes through that one cycle like that.

**Dave Jones:** That's if, that's what you wanted, if you wanted to count the actual clicks here, adjust the RC time constants to do whatever. But yeah, it's kind of a tricky business. Now of course there's another way to do this, obviously if this input was going into a Schmitt trigger of course, you've got to have it going

**Dave Jones:** into a Schmitt trigger, and then going into a microcontroller. A microcontroller, as I pointed out in my previous video, might have a Schmitt trigger input, in fact a lot of them do, but just double-check the data sheet that it does. And you can do software debouncing.

**Dave Jones:** You can, you know, adjust, effectively do a similar thing to what you'd use in the capacity of the RC time constant for, and you can add little software delays in there, tweak the values in your software delay loop to do software debouncing. And you could do that on a micro,

**Dave Jones:** and another way to do it might be a resettable one-shot timer, for example. You can get 74 series or 4000 series CMOS logic to do that, and so for multiple inputs like this it would just generate a single nice one pulse out, then it would reset the timer.

**Dave Jones:** So you could do it that way, you could build up a little hardware circuit if you didn't want to do software debouncing, you know, and if RC didn't do the job you wanted, you know, it entirely depends upon what you're actually using to count your number of monkeys.

**Dave Jones:** But of course we were getting a pretty noisy waveform on this due to the motor in probes here, so I can just hook up a filter in there to clean up that signal. I've got my Stanford Research SR 650 here, which you've seen me repair in a previous video,

**Dave Jones:** and I've just got a low-pass filter in here, 20 hertz, you don't need something fancy like this, you can just roll your own RC filter to do something like this if you want. And of course people are going to want to see probes with the symbols

**Dave Jones:** back on, so here we go, let's reset this puppy, and here we go. There we go, it's counting individual claps now, no problems. And if you have a look at the scope waveform there, you can see we've got our noisy input blue waveform down the bottom, I've just moved them, they're the same

**Dave Jones:** volts per division, and then the nice cleaned up output of the filter there, so that we can trigger off, in this case, the negative going pulses just down in there, the negative edge inside there. So that works a treat. So I hope you enjoyed that little look at

**Dave Jones:** just setting up a test system to count probes, the monkey here, how many times he claps, and lots of subtle little things actually go on in this, in such a setup. You've got contact bounce issues, noise issues, conducted motor, conducted and radiated motor emission shielding, all sorts of, you know, problems.

**Dave Jones:** You might think, hey that's easy, just to count the number of claps, but yeah, you can come and guts it in many different ways, and yes there are other ways to do this, of course you can do it with a setup of micro and count pulses and all that sort of stuff,

**Dave Jones:** but stick around for the next video where I'll show you how you can replace, or well, kind of, sort of, if there's not too much noise, replace all this wonderful setup by hacking a calculator. Check it out, the video will be here somewhere, right at the very end

**Dave Jones:** of this video. And don't forget to give it a big thumbs up and all that sort of jazz, because that really helps these days with the YouTube metrics and, or ranking and all that sort of jazz. Catch you next time.
