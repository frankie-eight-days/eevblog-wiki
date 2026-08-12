---
video_id: y5aAjd9YPok
title: EEVblog #685 - What Is Oscilloscope AC Trigger Coupling?
url: https://www.youtube.com/watch?v=y5aAjd9YPok
source: youtube-asr
timestamps: {"0": 1, "1": 18, "2": 34, "3": 52, "4": 65, "5": 83, "6": 95, "7": 111, "8": 124, "9": 139, "10": 155, "11": 166, "12": 180, "13": 196, "14": 210, "15": 224, "16": 240, "17": 256, "18": 269, "19": 283, "20": 302, "21": 316, "22": 333, "23": 346, "24": 362, "25": 378, "26": 392, "27": 405, "28": 418, "29": 429, "30": 440, "31": 455, "32": 470, "33": 484, "34": 504, "35": 521, "36": 540, "37": 556, "38": 570, "39": 586, "40": 597, "41": 609, "42": 624, "43": 636, "44": 654, "45": 668, "46": 684, "47": 699, "48": 710, "49": 723, "50": 737, "51": 751, "52": 764, "53": 779, "54": 793, "55": 810, "56": 825, "57": 840, "58": 855, "59": 868, "60": 884, "61": 900, "62": 917, "63": 928, "64": 941, "65": 959, "66": 971, "67": 984, "68": 999, "69": 1011, "70": 1029, "71": 1042, "72": 1059, "73": 1075, "74": 1089, "75": 1101, "76": 1114, "77": 1126}
---

**Dave Jones:** Hi, in a recent video I looked at a few problems with the new Rigol DS1054Z oscilloscope and also the DS2000 series oscilloscope. I discovered a problem with the AC trigger coupling and well, as it turns out this is actually not a

**Dave Jones:** new problem in the DS2000. It was reported back in July 2013. So, apparently Rigol haven't fixed it and it seems new to them again. Anyway, they responded very quickly. They said yes, they're looking into it, they're working on it and all that sort of

**Dave Jones:** stuff, but a lot of people seem to have an issue with exactly what AC trigger coupling on an oscilloscope is. And so many people confused it with input AC input coupling, the usual AC/DC input coupling that you're used to. In fact, a lot of

**Dave Jones:** people who've been using oscilloscopes for years said, "I have no idea what AC trigger coupling does. And so I just leave it on DC all the time. I don't know what the problem is." And this bug in the Rigol oscilloscope only occurs

**Dave Jones:** with the AC trigger coupling. So, I thought I'd do a very quick video explaining what AC trigger coupling is and exactly why you would want to use it. And even Rigol seemed a bit, you know, perplexed about this. They said, "Well, why does pretty

**Dave Jones:** much anyone want to use AC trigger coupling when you've got a DC input signal?" Well, anyway, let's take a look at the overview and we'll go straight to the bench. All right, what I've drawn here is an old school analog CRT

**Dave Jones:** oscilloscope just because it looks nicer, but digital scopes work pretty much exactly the same way. So, most people are familiar with what's called AC input coupling or just input coupling, input channel coupling. When you select that menu for your channel

**Dave Jones:** one or channel two input, it says, "Do you want AC or DC coupling?" And I'm pretty sure everyone understands that well, DC coupling just lets all of your DC signal all of your signal straight through. Whereas AC, if you switch it to

**Dave Jones:** AC coupling here, then it removes the DC component. I.E. So, only frequencies from like a you know, a couple of tens of hertz upwards are displayed. So, if you've got an input signal here that is offset by a DC amount, in this case 1

**Dave Jones:** volt, if you turn on AC input coupling, then it simply removes the DC component like that. Pretty easy. I think everyone understands that. So, that's basically how your inputs work. We've got an input amplifier here, which you can select AC

**Dave Jones:** or DC coupling. Do you wish to remove the DC component? And then you can select well, do you want to display channel 1 or channel 2? We won't go into how they're uh multiplexed and all that sort of stuff, but we can select which

**Dave Jones:** channel we want to display, and then this amplifier goes and drives our vertical our vertical plates here and moves our waveform up and down in response to the input. Pretty easy. And you've got that duplicated for channel 1

**Dave Jones:** and channel 2. But, what a lot of people don't realize is that oscilloscopes, both analog and digital, have AC trigger coupling as well. So, this is input coupling and this is trigger coupling. And I've drawn the trigger circuit in

**Dave Jones:** red here. Now, what the trigger circuit is, you've probably seen like on a traditional two-channel oscilloscope, digital or analog, it'll typically have a third input here called external trigger input. And it just allows you to use both channels with and then an

**Dave Jones:** external trigger signal to get a stable waveforms. There's a selection switch either on the front panel of the scope or in the soft menu for the trigger menu that allows you to select do I want my trigger signal to come from channel 1,

**Dave Jones:** from channel 2, or from external? Pretty simple. But then, you'll notice that the trigger circuit has exactly the same AC-DC coupling selection as we had up here in the input. Here it is here. It on DC trigger coupling mode, which on

**Dave Jones:** most digital scopes is the default, whereas on analog oscilloscopes, AC is actually the default. We'll talk about that in a minute. So, all it's exactly the same thing. So, it takes the signal before it's coupled here, okay? Before

**Dave Jones:** it's coupled here on the inputs, and then you can have AC or DC selection. Then we've got the trigger circuit, and of course the trigger circuit and horizontal sweep drives our waveform across or it drives it in here. You If it was a

**Dave Jones:** digital scope, you'd have a digital analog converter and all that sort of jazz, but makes no difference. So, that's the basic input architecture, both the analog channels and the triggering channel on either a digital or an analog scope. But, I will say that

**Dave Jones:** modern digital scopes like the Rigol DS 1054Z, they do all of their triggering in the digital domain. So, it's not like that they actually have a signal picked off here and then a physical AC coupling cap here. They They actually take it.

**Dave Jones:** This goes into the analog to digital converter, and then they take that into the trigger signal, and then they do it in software. It's all done in the digital domain. But, hey, it's an oscilloscope. It is supposed to

**Dave Jones:** work like a real oscilloscope, i.e. an analog oscilloscope or any oscilloscope people are used to. So, if digital oscilloscope has AC-DC trigger coupling, it should do exactly the same thing as it does on an old school analog scope,

**Dave Jones:** regardless of whether or not it's done in the digital domain or whether it's actually tapped off a signal here and a real cap and a real relay there to select the signal and done in the analog domain. Anyway, enough of that. Let's go

**Dave Jones:** to the bench. Now, if we have a look at both an old school analog oscilloscope like this Tektronix 2225 and this Rigol DS1054Z oscilloscope, which does, as I said, all the triggering in the digital domain. But, hey, essentially it is and does and

**Dave Jones:** is supposed to work exactly the same way. So, if we take a look at our analog oscilloscope here, you'll notice that we have our trigger coupling down here, not to be confused with your input coupling over here, AC and DC, entirely different

**Dave Jones:** things. Now, you'll see that it's got AC and DC down the bottom. We won't concern ourselves with the low frequency and high frequency reject there. They're just uh variations of the AC coupling there. So, what we've got is the AC

**Dave Jones:** coupling trigger coupling is there by default. It's up the top. There's a reason it's up the top is because on analog oscilloscopes, you pretty much, by default, want to use AC trigger coupling, and I'll show you why in a

**Dave Jones:** minute. Now, on our analog oscilloscope here, we have the mode control as well, and we've got it on normal mode, okay? I'll explain that in a second. And we've got our level control, which adjusts our trigger point, which starts our sweep

**Dave Jones:** all the way over here. So, you'll notice that is the start of a trigger point, whereas on a digital scope, it's in the middle. So, we can adjust our level control here, and the trigger point, once it gets up to there, boom, it's

**Dave Jones:** gone cuz it's no longer triggered. Our trigger lead has gone off, and we can take it all the way down. Bingo, it's gone right off the bottom of the waveform. Oh, it's very intermittent. It doesn't know how to trigger on. That's

**Dave Jones:** right on the edge. So, input coupling is obvious. If this is This is our ground level reference here, if we switch it to DC coupling and I change our input signal, I can raise up the DC offset there. And as I said, if you switch it

**Dave Jones:** over to AC coupling, it will simply remove that average DC level and shift the waveform down. Easy. Now, I'll show you how AC trigger coupling works, okay? We've got it set to AC over here. Our input signal is DC, but as I said, it

**Dave Jones:** the trigger takes the signal from basically directly from the input connector, so it doesn't matter. The trigger circuit, it doesn't care whether this is AC or DC like this. But, we've got AC coupling here. You'll notice that the start of the waveform, the trigger

**Dave Jones:** point is basically in the middle of that waveform, okay? And if we adjust the DC offset on the input, look, that trigger level remains exactly with the the trigger position remains exactly the same regardless of where of the DC value of that

**Dave Jones:** waveform. And why is it doing that? Well, because the we're using AC trigger coupling, so it's taking that input signal and removing that DC component. So, as far as the trigger circuit over here is concerned, it is uh got a basically a signal with no DC

**Dave Jones:** level. So, the trigger level you set here, okay? Um is not affected by that DC input because it's AC coupled. But, if we take that same waveform and switch it over to DC trigger coupling over here, okay? If we adjust our DC offset,

**Dave Jones:** you'll notice that the that the start value is actually changing there. And when it gets to a point, it just loses it like that. So, we're exactly the same as before, except we're losing our trigger and our trigger point is starting

**Dave Jones:** differently because we're DC coupled and we're changing the level of our DC input. So, that's the advantage of using AC trigger coupling on your oscilloscope over here is that it doesn't matter what DC level your input waveform is at or

**Dave Jones:** what type of input waveform, it's going to be easier and simpler to trigger off it. Okay, let me demonstrate this very dramatically where AC trigger coupling is useful in a practical scenario when you're probing a circuit. Now, over here

**Dave Jones:** I've got it on a normal trigger mode. I've got it on AC coupling, okay? So, we're going to see the advantage of it. Input is DC coupled, okay? So, we'll be able to see DC offset. What I'm going to

**Dave Jones:** do is I'm going to probe four different signals. I've got four function generators set up here with different DC offsets, but just assume that we're probing a circuit. We don't know what's going on. We want to find out what

**Dave Jones:** happens, okay? Out Look, our waveform's nice and triggered here, okay? We set our trigger level where we want, but because we've got AC triggering, watch what happens if I change Look, to a different signal with a different DC offset. It still reliably

**Dave Jones:** triggers off that. No problems at all. It's a different waveform. Uh it could be a different frequency or whatever. Let me try a third signal that we're probing. Look, it's a higher frequency. It's a different DC offset. We're still

**Dave Jones:** automatically triggering on that. Fantastic. And if I choose another signal, even higher DC offset again, once again, it's still triggering. But look, if we switch this down to DC mode, what? Useless. There's the third signal. Look, it briefly showed up there for a

**Dave Jones:** second. There's our second signal. Briefly showed up for a second. And we're back to our first air. It can't even trigger off that. We have to tweak it again for that. There you go. There's a dramatic example of a practical use

**Dave Jones:** for AC input coupling. When you're probing an unknown circuit, it just makes it easier to trigger from. And this is precisely why analog oscilloscopes like this always have the AC coupling or mostly always have the AC coupling right up the top as if it's

**Dave Jones:** sort of the de facto default trigger coupling method because it just gives you an easier trigger point to work from and removes the uh coupling here and it makes no difference about the coupling on the input here. And for those who

**Dave Jones:** think the input coupling makes a difference as we saw on the diagram, it doesn't. We'll switch it to AC coupling. There's our signal there. Okay, it's gone off the screen here. Okay, that's no good. So we might want to change the

**Dave Jones:** position back to here. But anyway, let's now switch over to our second signal. Bingo, we're triggered. It's removed the DC, but it's triggered for us. Let's go to our third signal here. Bingo, it's triggered. Let's go over to here. It's

**Dave Jones:** triggered. But if you go to DC trigger coupling down here, it's useless. There's our fourth signal, our third signal, doesn't even show up, our second, and back to our first. Absolutely useless. So the takeaway from that is if

**Dave Jones:** you use DC trigger coupling down here, then every time you probe a new signal on your circuit, an unknown signal, and it might have a different DC offset and you're using DC input coupling like that because you want to see the DC offset

**Dave Jones:** you're probing your circuit. You want to know if there's a DC offset there. So you're using DC mode typically you might do and you've got to manually go in and tweak the level control each and every time if

**Dave Jones:** that DC input varies. Whereas if you got AC coupling, you don't have to do that. You can set typically set one zero trigger point there and it'll the trigger on a good lot of input signals. Whereas DC coupling may not do that. But

**Dave Jones:** I hear people complaining, "Well, digital scopes are different. They're not analog." Well, let's try it. Here we go. We're in our trigger menu. Okay? This is trigger, not input coupling. We go down to settings. This is our AC our

**Dave Jones:** trigger coupling. We select AC. Okay? Once again, different waveforms with different DC offsets. Look, we're triggered there just fine. I switch over to another waveform. Bingo, we're automatically triggered. Look at that. Magic. And then we go over to another

**Dave Jones:** waveform with a different DC offset. Bingo, we're still triggered. I mean, granted, this is going to change if our trigger level is slightly different, but you stand more chance of getting a signal first go by using AC trigger

**Dave Jones:** coupling. So, let's select that to DC here and see what happens. No, our waveforms, no, it's not triggered properly. Let's go back to our waveform over here. No, it can't trigger on that and it can't trigger on that one here

**Dave Jones:** because on DC trigger coupling, you have to muck around every time you probe a new signal and set your trigger level like this. And that is the difference because with these new digital oscilloscopes, people are so used to

**Dave Jones:** seeing this trigger line and this trigger level, they've just got into a different mindset of using the scope. And every time they trigger us every time they probe a new unknown signal, they go, "Oh, well, I've got to set my

**Dave Jones:** trigger level down here." Well, if you had AC trigger coupling turned on here, you might not have to do that. It is advantageous even on these modern digital scopes. It works the same way, has the same advantage. Now, just as a

**Dave Jones:** little aside, I'll show you something that I don't particularly like about the Rigol digital scopes. This is on the DS1000Z series and also on the DS2000 series, but curiously not on the original DS1052E. Now, you'll notice that the trigger knob

**Dave Jones:** here has pushed a zero on the Rigol 1000 and also on the 2000 series. But on the Agilent X series and also on the Tektronix MDO3000 series, it's got push 450% instead of zero. And this brings us to one of the big advantages of modern

**Dave Jones:** digital scopes. And that, look, right, we've got an untriggered waveform here. We've just probed it. It's brand new. We had no idea what the DC offset was, whatever. And our trigger level happens to be right up here. Well, to get it

**Dave Jones:** triggered, of course, we can move our trigger level down. But we don't have to do that on a modern digital scope. Regardless of where the waveform is, as long as it's within side the capture area of the ADC, look, it's got trigger

**Dave Jones:** push for 50%. So we can just push that and the scope figures out where where the waveform is and automatically puts that trigger level smack in the center. Brilliant. So that's sort of like a one-button solution to not using AC trigger

**Dave Jones:** coupling. So instead of having to always just muck around with this trigger level control, you can just go bang, give it to me. Thank you very much. Works the same on the Agilent and on the Tek. But if you want to do the same thing on the

**Dave Jones:** Rigol, well, here's our level control here. It's around about there. Yeah, we can tweak it and bring it down to trigger our unknown signal, but because it's set the level to zero, if we push it like that, it drops down to

**Dave Jones:** zero. And if you don't have your AC input coupling on, it's fine if you're actually using input coupling of AC, then you know, if you've got your unknown signal, you'll actually trigger from it like like this. No problems at

**Dave Jones:** all, but it doesn't it's not intelligent enough to do to work out a DC to do that. And it's got nothing in the menu to set it to 50%. There's no option. I don't like it. It's the same on the

**Dave Jones:** 1000 and the 2000Z series. I much prefer the 50% level. And here's where it's another step back from the venerable DS1052E. Yes, it has the reset to zero level down here, but it's got a dedicated 50% button. So yeah, we can dick if our

**Dave Jones:** unknown signal, we can dick around with our level control, put in the middle and trigger, or we can just go bang, hit 50%, thank you very much. And some people were confused why, if you go into the trigger menu and you go into

**Dave Jones:** the coupling and you set it to AC, you no longer get that trigger level control there because it doesn't make sense relative to your input channel. So, we don't get that bar anymore even though it tells us our

**Dave Jones:** trigger level is down here. So, it's still displaying it, but it just doesn't make sense to print the level on the screen because we're cuz the trigger level over here is AC coupled from our displayed signal. So, it no longer makes

**Dave Jones:** sense to actually put it in there relative to the graticule and the waveform. So, I hope that clears that up. So, there you go. I hope you found that interesting and why AC trigger coupling, even on modern digital scopes,

**Dave Jones:** is still an advantage when probing unknown circuits. And it's a shame that people don't use it more often. I've seen so many people on the forum and on the comments for the previous videos say, "Well, I've never used AC coupling.

**Dave Jones:** It doesn't matter and blah, I don't care if this thing has a bug in the AC coupling menu on the Rigol DS2000. I don't care. I never use it anyway." Well, you're probably doing yourself a bit of disservice. It's not a bad

**Dave Jones:** feature, AC trigger coupling. Have a play around with it next time. There you go. Anyway, if you want to discuss it, links down below to the EVblog forum. You can leave your comments on YouTube, do whatever. And if you like the video,

**Dave Jones:** please give it a big thumbs up. Catch you next time.
