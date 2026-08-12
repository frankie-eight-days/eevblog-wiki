---
video_id: 5lG2mUWI3rs
title: EEVblog 1735 - Power Rail Probing & Oscilloscope DC Offset EXPLAINED
url: https://www.youtube.com/watch?v=5lG2mUWI3rs
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 25, "3": 35, "4": 47, "5": 57, "6": 74, "7": 89, "8": 101, "9": 125, "10": 143, "11": 153, "12": 164, "13": 178, "14": 189, "15": 198, "16": 215, "17": 232, "18": 249, "19": 260, "20": 276, "21": 287, "22": 301, "23": 309, "24": 321, "25": 333, "26": 351, "27": 375, "28": 386, "29": 400, "30": 413, "31": 426, "32": 435, "33": 445, "34": 455, "35": 469, "36": 479, "37": 506, "38": 524, "39": 538, "40": 556, "41": 565, "42": 577, "43": 587, "44": 603, "45": 618, "46": 634, "47": 641, "48": 653, "49": 666, "50": 682, "51": 700, "52": 714, "53": 725, "54": 741, "55": 761, "56": 785, "57": 794, "58": 807, "59": 816, "60": 823, "61": 840, "62": 850, "63": 863, "64": 877, "65": 902, "66": 916, "67": 927, "68": 939, "69": 948, "70": 969, "71": 980, "72": 997, "73": 1009, "74": 1021, "75": 1031, "76": 1048, "77": 1060, "78": 1075, "79": 1092, "80": 1102, "81": 1110, "82": 1121, "83": 1131, "84": 1143, "85": 1158, "86": 1168, "87": 1188, "88": 1207, "89": 1223, "90": 1233, "91": 1253, "92": 1269, "93": 1282, "94": 1291, "95": 1303}
---

**Dave Jones:** Hi, I showed in a previous video how you can use one of these cheap relatively cheap and simple power rail probes here to actually measure the performance of a power rail that you've got in your circuit.

**Dave Jones:** In this particular case, I'm viewing a 5-V power rail on a Raspberry Pi powered from an external battery in here. And this has a 2-GHz bandwidth, which is way more than my 1-gig scope here.

**Dave Jones:** And you can see the power rail probe waveform there. But I also compared it to a very expensive 2-GHz active probe. This is a Agilent/Keysight jobby, matched for this scope.

**Dave Jones:** And you can see I'm probing exactly at the same point. And we're getting a similar performance, slightly better with the power rail probe. But we'll go into the reasons why that's the case.

**Dave Jones:** But what this video is about, I want to show you that you don't actually need a proper power rail probe to probe power rails at high bandwidth. You can actually do it using your regular probes.

**Dave Jones:** Let's go. Now, we're not talking about doing noise measurement, which is what I've done a video on in the past, which is typically when you want to measure like a power rail noise, like P2P or RMS noise, you're generally going to do that over a like a 20-MHz bandwidth limit.

**Dave Jones:** And that's why oscilloscopes will have a 20-MHz bandwidth limit on them. It's for historical reasons as well. But also, that is like a standard way to measure noise. And you can see that we can actually bandwidth limit that down to 20 MHz.

**Dave Jones:** But that is really only specific for noise measurements. But when you're actually measuring the actual signal fidelity of the rail, you want to see all these transients in here.

**Dave Jones:** And you want it to be high bandwidth and super accurate. Cuz we're talking about high frequency information here. Look at this. We're 10 ns per division, right? These transients in here, this ringing on the power rail, is hundreds of megahertz and that depends on the slew rate of the circuit that you're trying to measure but even basic microcontroller stuff, you can get hundreds of megahertz.

**Dave Jones:** And this of course depends upon which point of your power rail you're measuring in circuit, what sort of decoupling you've got on the rail, trace inductance, loop inductance and depending upon where your source and your load is and the whole loop area and all that sort of you know, signal fidelity stuff.

**Dave Jones:** I'm just measuring the 5-V rail of a Raspberry Pi here but just as just an example but you could be measuring a more critical power rail in your WizBang widget.

**Dave Jones:** And if we actually expand that time base out here, you can see that there's that high frequency information like that and there's also going to be lower frequency information in there as well.

**Dave Jones:** And this is why when you're doing power rail probing signal fidelity, you do not want AC coupling. You actually want to include the DC component cuz the AC coupling is not going to pick up all that low frequency stuff.

**Dave Jones:** So you don't want to go using AC coupling. You want DC coupling but therein lies the problem. Take for example the 5-V rail that we're measuring on this Raspberry Pi here.

**Dave Jones:** You've got 5 V of DC offset because you don't want to use your AC coupling mode which removes the DC offset. You want to include that 5 V DC.

**Dave Jones:** So that signal on your oscilloscope we're using the active probe here DC coupling only. There's our ground where it 1 V per division, 1, 2, 3, 4, 5. Sorry, you can barely see the graticule on there but five divisions and there's the information that we want to measure.

**Dave Jones:** Look how tiny it is in there. So if you want to see that information, not only is it advantageous to have a like a 4 a 12 or 14-bit oscilloscope like modern oscilloscopes now are 12 bits is now pretty much you know, the entry level even entry level scopes have a 12-bit performance.

**Dave Jones:** 12-bit ADC it means that you can actually zoom in on that information better. But, there's another factor, DC offset on your oscilloscope. Aha. So, what we do is we want to use our DC offset knob like this to get this right down.

**Dave Jones:** Let's put it in the center of the screen like that and it well, you change the vertical again. You keep it to wind it down again. You change the vertical and you See how it's off screen?

**Dave Jones:** And you can see here that we can adjust the 5-V the offset the DC offset on the input of our oscilloscope to that 5-V. So, it gets rid of that 5-V DC and we adjust the offset it'll come in soon and there it is.

**Dave Jones:** And then we can get it on the input like that. But, oscilloscopes are not magic. Not all oscilloscopes are created equal. Not all of them have the DC offset required.

**Dave Jones:** In fact, the DC offset that we've got here is not coming from the oscilloscope, it's coming from this active probe. This active probe here actually has the ability to go to I think it can do a 12-V offset.

**Dave Jones:** Let's go to 13, see if it can do that. Nope, the control is at its limit. It can actually do plus minus 12-V offset. But, that's not the oscilloscope hardware doing that.

**Dave Jones:** That is a built-in DC offset of this active probe. And you'd want to want to be a decent because, you know, that's many thousands of dollars. Just for the probe.

**Dave Jones:** And that's where something like this cheap PRP-1 power rail probe, this is only like a hundred bucks or so. I'll put a link in down below. It's may or may not be available yet, but it can actually adjust plus minus 24-V, which is really nice.

**Dave Jones:** So, if you've got a you know, a 20-V rail that you're trying to measure, then well, this thing will do it and that multi-thousand dollar probe won't. But, anyway, you just go to our regular oscilloscope input here, and on channel one, and have a look at the DC offset there, how far can we go?

**Dave Jones:** Well, we can wind this up and find out. Uh -1.95 V. We can go to +2, and it'll go, "Nope, it's plus minus 1.95 V." So, this wiz-bang super high-end uh 40-bit 1-gig um HDO um 3 series oscilloscope, fantastic.

**Dave Jones:** But, if you're measuring your power rails directly with a 1:1 probe, which we'll get into, then you can only do 2 V DC offset, which isn't much. All right, so let's try a 10:1 passive probe.

**Dave Jones:** So, we're going to get a 10:1 division ratio as opposed to a uh 1.3:1 that we've got with this uh power rail probe over here. So, with a What you want is a lower division ratio.

**Dave Jones:** The higher division ratio, if you go to a 10:1 probe like this, yes, you can get 500 MHz of bandwidth here, no worries whatsoever. That's good enough. This is 2 gig, but, you know, 500 meg, pretty schmick.

**Dave Jones:** But, if you're measuring low-level signals like we're on 50 mV per division, we've already divided that by 10. So, uh on the input of your scope. So, you're going to increase your noise floor.

**Dave Jones:** So, you know, it's a trade-off. But, hey, your scope already has these. And I've got my low impedance uh ground clip on there as well. And I'm just going to calibrate this sucker.

**Dave Jones:** And that's a little bit off, so we'll just uh tweak the probe with our tongue at the right angle and get a nice square wave on there. So, we'll just tweak that.

**Dave Jones:** Tongue at the right angle. Ah, there we go. Bobby Dazzler. So, here we go. We've got the blue waveform, which is our uh times 10 passive probe, 500 MHz bandwidth.

**Dave Jones:** And uh we've got our power rail probe again as uh the yellow one here. I've expanded the time base out to 2 ms per division because you can see lower frequency content like this.

**Dave Jones:** And that's the sort of stuff you may not be able to see if you use AC coupling or it can cause a problem. But anyway, we've got enough memory depth that we can actually zoom in and see what's going on here.

**Dave Jones:** And there you go, it does a pretty good account of itself. And if you're wondering why the blue waveform is before the yellow waveform here even though I'm probing the exact same spot, well, that is a skew difference between the probes because the length of this passive probe on channel 3 here does not match the the entire probe length of the power rail probe here.

**Dave Jones:** So, you if you really want to time correlate the signals correctly, you have to do skew correction of your channels just a we're getting 20 nanoseconds per division. So, there's about like you know, a half a division or something in there difference.

**Dave Jones:** So, there's about a 10 nanosecond propagation delay difference between those two cables. But you can calibrate that out on your scope. No worries. But in our particular case, we're just looking for the signal fidelity here.

**Dave Jones:** And look at this, the times 10 probe gives a fantastic account for itself. There's hardly any difference. You can say that the power rail probe is a bit lower noise in there, but jeez, it's not much considering that you've already got those times 10 passive probes with your scope.

**Dave Jones:** They'll of course match the bandwidth of your scope except if you got like a 1 GHz scope like this one, you can't get a 1 GHz passive probe unfortunately.

**Dave Jones:** Although, Tektronix do make a 1 GHz passive probe. I do actually have one here, but anyway, it's not going to be the 2 GHz bandwidth of a proper power rail probe or an active probe like this one.

**Dave Jones:** But if you don't have this oscilloscope bandwidth to do that, then well, you know, what's the point? You're just gilding the lily. Um but yeah, times 10 probe works fantastically.

**Dave Jones:** No worries. But only if your scope can actually do the 5-V offset required. And that's the important point. But of course, if you're using a 10:1 probe like this, you are attenuating your signal 10:1, but that means your in this case 5-V signal is down to 500 mV.

**Dave Jones:** So, your scope only needs 500 mV offset in order to do that. And I'm pretty sure almost every scope out there is capable of 500 mV. I think everyone in the lab I've got here is.

**Dave Jones:** And if you try and capture the signal without using any DC offset, I've captured it at 1 V per division and shifted it down with an 8-bit oscilloscope, old school like this, yeah, you can see the individual bits.

**Dave Jones:** It's not much help, is it? In fact, you might think that you've got like a square wave happening on your signal there. You don't. But as always, there's a trap for young players.

**Dave Jones:** This is the DSOX 1200 Keysight. Nice little scope, but it's only an 8-bit jobby, so you don't get the same dynamic range as a 12-bit or the 14-bit scope that we saw before, but that's okay.

**Dave Jones:** Does it have decent DC offset? So, we'll switch to channel two here, okay, and then we'll look at the probe. I've got the probe set to 10:1, which I am using a 10:1 probe, so that is set correctly.

**Dave Jones:** And if we actually change this, I don't I'll just make it quick. Look. Look check out the DC offset. You might think this thing is a champion. It's going to go up to Look at this.

**Dave Jones:** 20 V. WOW, THIS THING'S KILLER, RIGHT? Wha No, it's not. It's actually only 2 V. If I go to the probe and I set that back to 1 to 1 and then we do the same thing again, you'll see it's now only 2 V offset.

**Dave Jones:** That's its true offset voltage. So, don't be fooled by a scope thinking that it has a 20 V offset like it actually on the front end it's able to offset plus minus 20 V.

**Dave Jones:** It's not. It's only plus minus 2 V. It was fooling you by having that um by multiplying that with the times 10 indicator. But Dave, this is a 10 to 1 probe.

**Dave Jones:** So, the 5 V that we're feeding in here should come out of here at 500 mV. So, it should be able to offset that. So, once I apply the correct offset, you can see that that times 10 probe there matches quite well.

**Dave Jones:** It's a little bit, you know, a little bit noisier, but um not too shabby. So, we can still with the times 10 probe, we can still measure a 5 V rail because it's only 500 mV offset due to the times 10 division, which means that our 2 V offset scope can still do it.

**Dave Jones:** Beauty. And you've seen this in previous videos on uh probing. I'll link it in if you haven't seen it. This is a coaxial cable probe with a series 1 K resistor in there and this is called a Z0 or Z not uh probe and it's uh basically a do-it-yourself gigahertz bandwidth on this depending on the uh coax you use and it's basically a a 1 K.

**Dave Jones:** Uh you got to use 50 ohms on the other end on the uh oscilloscope, but you can get a high bandwidth probe for practically nothing. It's just a bit of coax and a resistor and that's it.

**Dave Jones:** So, with 1 K resistor and 50 ohm load, we get just over uh 20 division ratio. I can program that in directly on this particular scope, but so it's a high division ratio, but you can choose your own resistor.

**Dave Jones:** It's just a uh DC loading thing. And if you're measuring a power supply, you know, a 1K load or a bit lower is is neither here nor there, really.

**Dave Jones:** And there you have it. Look at the result. That is my Z0 probe in blue there. And it's just you can make it for a couple of bucks. It's easy.

**Dave Jones:** And once again, this is the power rail probe there. So, fantastic, isn't it? Look at that. So, you don't actually have to buy one of these Wizbang power rail probes or one of these beat Wizbang active probes to get a high bandwidth like power rail probing solution.

**Dave Jones:** You can just use your 10 to 1 probe. You can't use a 1 to 1 probe cuz I've done a video on that breaking down the issues with 1 to 1 oscilloscope probes.

**Dave Jones:** They've got a very low bandwidth, only like 5 MHz, 10 MHz, something like that. So, yeah, you're not going to get the bandwidth out of it. But hey, you can just roll your own coax here and Bob's your uncle.

**Dave Jones:** And provided you have some sort of divider on there, that's going to allow you to use your DC offset voltage on the input of your oscilloscope here. Most oscilloscopes, as you saw like that Keysight one, only had 2 V.

**Dave Jones:** Most are going to do plus minus a couple of volts. Some other ones do better. But here's the interesting thing to note about DC offset on oscilloscopes. It will change depending on the volts per division setting you're on because the front end actually has relays in there that click different attenuators and amplifiers in there to give you all the different ranges, of course.

**Dave Jones:** So, if I put my microphone up to this, hopefully you can hear it switch. Listen. Between 100 and 200 mV there, there is a relay click. So, it's actually changing the front end.

**Dave Jones:** So, that's also going to potentially change your maximum DC offset range, as well. And there's another click between 1 and 2 V. So, that's going to change it as well.

**Dave Jones:** So, if we go to our 100 mV per division, you'll see that it's maxing out at plus minus 1.5 V here. It'll always be the same on the positive side as it is on the negative side.

**Dave Jones:** But, if we jump it up to that 200 mV range, we'll find that we can actually go above that. In fact, we can go a long way above that.

**Dave Jones:** But, typically when you're using measuring power rails, you you usually at low voltages. And bingo, it goes to plus minus 15 V. Isn't that neat? And once again, you've got to test this at the appropriate ratio of 1 to 1 so that you're not input referred multiplying your range there.

**Dave Jones:** And if we go up to 2 V, where it clicks again, then let's go let's go. Look at this. >> [laughter] >> We can really go up in the offset voltage, too.

**Dave Jones:** You guessed it, offset. But, it's not actually offsetting it by 150 V. It's because there's attenuators in there that attenuate the signal before it gets to the amplifier which has the offset adjustment.

**Dave Jones:** So, it there's not actually 150 plus minus 150 V voltage rail on your analog to digital front end there. That's not how it's uh working. It's all working with dividers and whatnot.

**Dave Jones:** This Rigol DHO 800 uh series 12-bit jobby, um it the scale jumps. I can hear the relay clicking at 50 mV. So, that's where we'll take our offset from.

**Dave Jones:** And on the lowest range there, you can see that we're going to max out at one plus minus 1 V there. Not much, but that will go up if you choose 100 mV range instead.

**Dave Jones:** Looks like 200 mV range, we should find uh yeah, there we go. We can go to 8 V. So, not 10, but 8. This Siglent SDS 800X uh series HD, new 12-bit jobby, very nice.

**Dave Jones:** Plus minus 8 V. Beautiful. The duxiest of ducks guts, the MSO 4 from Rohde & Schwarz, let's have a look. It can go to 5 plus minus 5 V.

**Dave Jones:** But, there's not just a difference between brands, there's actually a difference between models as well. This uh Siglent SDS 2000X HD series, it'll actually go to plus minus 16 V.

**Dave Jones:** Groovy, huh? The Rigol HDO 4000, unfortunately, once again, only plus minus 1 V. And the Rigol HDO uh 1204, well, once again, plus minus 1 V maximum there. So, um yeah, nothing you can really do there.

**Dave Jones:** That just seems to be a limitation of their uh new front end. But, it's a super cheap front end. Um you get the bandwidth for nix, but plus minus 1 V is still usable.

**Dave Jones:** If you use a times 10 divider probe, you can easily do your 5 V rail. You could even do a 10 V rail. And I know it's going to be the same.

**Dave Jones:** The MSO 98 1 GHz bandwidth for practically nothing. Um and yeah, it's only uh 1 V as well. But, of course, like you can go to There's a relay click.

**Dave Jones:** You can go up to 100 mV. If you do that, you're going to go all the way with your old mate J right up to 10 V. And you're still and down at you know, 100 mV per division, which is pretty decent.

**Dave Jones:** So, you know, it's good enough for Australia. Now, for your very keen eyed, you would have noticed a big difference between both the uh Key- Keysight and Rohde & Schwarz and the Rigols and the Siglents.

**Dave Jones:** So, the two big name ones versus the two uh like lesser name ones, there's actually a big difference. Let me show you. You'll notice as I move the trace down, I'm adding that DC offset, okay, in the front end, but it's showing up as positive.

**Dave Jones:** It's showing up as plus voltage. And the further I go down, the more it goes positive. It doesn't display negative. So, then if I move it up like that, does it go negative?

**Dave Jones:** But look at the Siglent here. As I go down, it's increasing, but it's showing up as a negative voltage there. So, both the Siglent and the Rigol show negative when you go like in the down direction, whereas both Keysight and Rohde & Schwarz show it as a positive.

**Dave Jones:** Isn't that interesting? What's going on there? It's really It depends how you think of it, whether or not it's like input-referred, um so to speak, which means that, okay, I've got to shift my waveform down by 5 V.

**Dave Jones:** In that case, Siglent and Rigol saying, "I've got to add negative voltage negative like 5 V in there." Whereas the Keysight and the uh Rohde & Schwarz show that, "Well, I've got to offset it by 5 V."

**Dave Jones:** I It doesn't think about adding the negative kind of thing. So, I don't know. Which one's right? Which one's wrong? Eh, six of one, half a dozen of the other.

**Dave Jones:** Leave your thoughts in the comments. Who's got it right? So, I hope you found that video interesting, how to probe a high-bandwidth uh power rail on your circuit, cuz you may want to do this for all sorts of uh reasons, you know, signal fidelity uh stuff, things like that, decoupling, um all sorts of, you know, ground system issues and stuff like that.

**Dave Jones:** You often need high-bandwidth probing of your power supply. And you can do it pretty cheap and simple just using your times 10 probe. Good enough for Australia. A cheap and simple uh coax Z0 probe the series resistor, no worries.

**Dave Jones:** Um most of the oscilloscopes are going to have with an input divider, they're going to have enough um DC offset range to do that. Although, something like this uh power rail probe like a hundred bucks, you know, really good value.

**Dave Jones:** It can do up to plus minus 24 volts um offset. And uh you saw this active probe, even though it's a couple of thousand dollars, it can do like uh yeah, plus minus 20 volts offset.

**Dave Jones:** So, you do get the higher offset uh advantage there. But, you know, using your basic um probes that you already have, no worries. Anyway, if you like that video, please give it a big thumbs up.

**Dave Jones:** As always, discuss down below. And you can support the EEVblog by going to the EEVblog.store, buy a multimeter or something. Catch you next time. >> [music]
