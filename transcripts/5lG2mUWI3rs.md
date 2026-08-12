---
video_id: 5lG2mUWI3rs
title: EEVblog 1735 - Power Rail Probing & Oscilloscope DC Offset EXPLAINED
url: https://www.youtube.com/watch?v=5lG2mUWI3rs
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 29, "3": 44, "4": 57, "5": 71, "6": 86, "7": 103, "8": 120, "9": 134, "10": 148, "11": 161, "12": 176, "13": 189, "14": 202, "15": 217, "16": 232, "17": 249, "18": 263, "19": 279, "20": 294, "21": 305, "22": 319, "23": 331, "24": 345, "25": 363, "26": 383, "27": 400, "28": 413, "29": 428, "30": 441, "31": 455, "32": 470, "33": 481, "34": 498, "35": 517, "36": 534, "37": 548, "38": 562, "39": 577, "40": 589, "41": 603, "42": 618, "43": 634, "44": 647, "45": 661, "46": 675, "47": 694, "48": 710, "49": 725, "50": 741, "51": 756, "52": 768, "53": 785, "54": 799, "55": 811, "56": 823, "57": 837, "58": 852, "59": 865, "60": 879, "61": 896, "62": 916, "63": 929, "64": 940, "65": 958, "66": 972, "67": 991, "68": 1007, "69": 1024, "70": 1040, "71": 1060, "72": 1080, "73": 1097, "74": 1108, "75": 1121, "76": 1131, "77": 1146, "78": 1158, "79": 1174, "80": 1191, "81": 1209, "82": 1225, "83": 1239, "84": 1253, "85": 1269, "86": 1282, "87": 1293, "88": 1305, "89": 1317}
---

**Dave Jones:** Hi, I showed in a previous video how you can use one of these cheap relatively cheap and simple power rail probes here to actually measure the performance of a power rail that you've got in your circuit. In this particular case, I'm

**Dave Jones:** viewing a 5-V power rail on a Raspberry Pi powered from an external battery in here. And this has a 2-GHz bandwidth, which is way more than my 1-gig scope here. And you can see the power rail probe waveform there. But I also

**Dave Jones:** compared it to a very expensive 2-GHz active probe. This is a Agilent/Keysight jobby, matched for this scope. And you can see I'm probing exactly at the same point. And we're getting a similar performance, slightly better with the power rail

**Dave Jones:** probe. But we'll go into the reasons why that's the case. But what this video is about, I want to show you that you don't actually need a proper power rail probe to probe power rails at high bandwidth. You can actually do it using your

**Dave Jones:** regular probes. Let's go. Now, we're not talking about doing noise measurement, which is what I've done a video on in the past, which is typically when you want to measure like a power rail noise, like P2P or RMS noise, you're generally

**Dave Jones:** going to do that over a like a 20-MHz bandwidth limit. And that's why oscilloscopes will have a 20-MHz bandwidth limit on them. It's for historical reasons as well. But also, that is like a standard way to measure noise. And you can see that we can

**Dave Jones:** actually bandwidth limit that down to 20 MHz. But that is really only specific for noise measurements. But when you're actually measuring the actual signal fidelity of the rail, you want to see all these transients in here. And you

**Dave Jones:** want it to be high bandwidth and super accurate. Cuz we're talking about high frequency information here. Look at this. We're 10 ns per division, right? These transients in here, this ringing on the power rail, is hundreds of megahertz and that depends on the slew

**Dave Jones:** rate of the circuit that you're trying to measure but even basic microcontroller stuff, you can get hundreds of megahertz. And this of course depends upon which point of your power rail you're measuring in circuit, what sort of decoupling you've got on

**Dave Jones:** the rail, trace inductance, loop inductance and depending upon where your source and your load is and the whole loop area and all that sort of you know, signal fidelity stuff. I'm just measuring the 5-V rail of a Raspberry Pi

**Dave Jones:** here but just as just an example but you could be measuring a more critical power rail in your WizBang widget. And if we actually expand that time base out here, you can see that there's that high frequency information like that and

**Dave Jones:** there's also going to be lower frequency information in there as well. And this is why when you're doing power rail probing signal fidelity, you do not want AC coupling. You actually want to include the DC component cuz the AC

**Dave Jones:** coupling is not going to pick up all that low frequency stuff. So you don't want to go using AC coupling. You want DC coupling but therein lies the problem. Take for example the 5-V rail that we're measuring on this Raspberry

**Dave Jones:** Pi here. You've got 5 V of DC offset because you don't want to use your AC coupling mode which removes the DC offset. You want to include that 5 V DC. So that signal on your oscilloscope we're using the active probe here DC

**Dave Jones:** coupling only. There's our ground where it 1 V per division, 1, 2, 3, 4, 5. Sorry, you can barely see the graticule on there but five divisions and there's the information that we want to measure. Look how tiny it is in there. So if you

**Dave Jones:** want to see that information, not only is it advantageous to have a like a 4 a 12 or 14-bit oscilloscope like modern oscilloscopes now are 12 bits is now pretty much you know, the entry level even entry level scopes have a 12-bit

**Dave Jones:** performance. 12-bit ADC it means that you can actually zoom in on that information better. But, there's another factor, DC offset on your oscilloscope. Aha. So, what we do is we want to use our DC offset knob like this to get this

**Dave Jones:** right down. Let's put it in the center of the screen like that and it well, you change the vertical again. You keep it to wind it down again. You change the vertical and you See how it's off screen? And you can see here that we can

**Dave Jones:** adjust the 5-V the offset the DC offset on the input of our oscilloscope to that 5-V. So, it gets rid of that 5-V DC and we adjust the offset it'll come in soon and there it is. And then we can get it

**Dave Jones:** on the input like that. But, oscilloscopes are not magic. Not all oscilloscopes are created equal. Not all of them have the DC offset required. In fact, the DC offset that we've got here is not coming from the oscilloscope,

**Dave Jones:** it's coming from this active probe. This active probe here actually has the ability to go to I think it can do a 12-V offset. Let's go to 13, see if it can do that. Nope, the control is at its

**Dave Jones:** limit. It can actually do plus minus 12-V offset. But, that's not the oscilloscope hardware doing that. That is a built-in DC offset of this active probe. And you'd want to want to be a decent because, you know, that's many

**Dave Jones:** thousands of dollars. Just for the probe. And that's where something like this cheap PRP-1 power rail probe, this is only like a hundred bucks or so. I'll put a link in down below. It's may or may not be available

**Dave Jones:** yet, but it can actually adjust plus minus 24-V, which is really nice. So, if you've got a you know, a 20-V rail that you're trying to measure, then well, this thing will do it and that multi-thousand dollar probe won't. But,

**Dave Jones:** anyway, you just go to our regular oscilloscope input here, and on channel one, and have a look at the DC offset there, how far can we go? Well, we can wind this up and find out. Uh -1.95 V. We can go to +2, and it'll go, "Nope,

**Dave Jones:** it's plus minus 1.95 V." So, this wiz-bang super high-end uh 40-bit 1-gig um HDO um 3 series oscilloscope, fantastic. But, if you're measuring your power rails directly with a 1:1 probe, which we'll get into, then you can only do 2 V

**Dave Jones:** DC offset, which isn't much. All right, so let's try a 10:1 passive probe. So, we're going to get a 10:1 division ratio as opposed to a uh 1.3:1 that we've got with this uh power rail probe over here. So, with a What you

**Dave Jones:** want is a lower division ratio. The higher division ratio, if you go to a 10:1 probe like this, yes, you can get 500 MHz of bandwidth here, no worries whatsoever. That's good enough. This is 2 gig, but, you know, 500 meg, pretty

**Dave Jones:** schmick. But, if you're measuring low-level signals like we're on 50 mV per division, we've already divided that by 10. So, uh on the input of your scope. So, you're going to increase your noise floor. So, you know, it's a

**Dave Jones:** trade-off. But, hey, your scope already has these. And I've got my low impedance uh ground clip on there as well. And I'm just going to calibrate this sucker. And that's a little bit off, so we'll just uh tweak the probe with our tongue at

**Dave Jones:** the right angle and get a nice square wave on there. So, we'll just tweak that. Tongue at the right angle. Ah, there we go. Bobby Dazzler. So, here we go. We've got the blue waveform, which is our uh times 10 passive probe,

**Dave Jones:** 500 MHz bandwidth. And uh we've got our power rail probe again as uh the yellow one here. I've expanded the time base out to 2 ms per division because you can see lower frequency content like this. And that's the sort of stuff you may not

**Dave Jones:** be able to see if you use AC coupling or it can cause a problem. But anyway, we've got enough memory depth that we can actually zoom in and see what's going on here. And there you go, it does

**Dave Jones:** a pretty good account of itself. And if you're wondering why the blue waveform is before the yellow waveform here even though I'm probing the exact same spot, well, that is a skew difference between the probes because the length of this

**Dave Jones:** passive probe on channel 3 here does not match the the entire probe length of the power rail probe here. So, you if you really want to time correlate the signals correctly, you have to do skew correction of your channels just a

**Dave Jones:** we're getting 20 nanoseconds per division. So, there's about like you know, a half a division or something in there difference. So, there's about a 10 nanosecond propagation delay difference between those two cables. But you can calibrate that out on your scope. No worries. But

**Dave Jones:** in our particular case, we're just looking for the signal fidelity here. And look at this, the times 10 probe gives a fantastic account for itself. There's hardly any difference. You can say that the power rail probe is a bit

**Dave Jones:** lower noise in there, but jeez, it's not much considering that you've already got those times 10 passive probes with your scope. They'll of course match the bandwidth of your scope except if you got like a 1 GHz scope like this one,

**Dave Jones:** you can't get a 1 GHz passive probe unfortunately. Although, Tektronix do make a 1 GHz passive probe. I do actually have one here, but anyway, it's not going to be the 2 GHz bandwidth of a proper power rail probe or an

**Dave Jones:** active probe like this one. But if you don't have this oscilloscope bandwidth to do that, then well, you know, what's the point? You're just gilding the lily. Um but yeah, times 10 probe works fantastically. No worries. But only if

**Dave Jones:** your scope can actually do the 5-V offset required. And that's the important point. But of course, if you're using a 10:1 probe like this, you are attenuating your signal 10:1, but that means your in this case 5-V signal

**Dave Jones:** is down to 500 mV. So, your scope only needs 500 mV offset in order to do that. And I'm pretty sure almost every scope out there is capable of 500 mV. I think everyone in the lab I've got

**Dave Jones:** here is. And if you try and capture the signal without using any DC offset, I've captured it at 1 V per division and shifted it down with an 8-bit oscilloscope, old school like this, yeah, you can see the individual bits.

**Dave Jones:** It's not much help, is it? In fact, you might think that you've got like a square wave happening on your signal there. You don't. But as always, there's a trap for young players. This is the DSOX 1200 Keysight. Nice little scope,

**Dave Jones:** but it's only an 8-bit jobby, so you don't get the same dynamic range as a 12-bit or the 14-bit scope that we saw before, but that's okay. Does it have decent DC offset? So, we'll switch to channel two here, okay, and then we'll

**Dave Jones:** look at the probe. I've got the probe set to 10:1, which I am using a 10:1 probe, so that is set correctly. And if we actually change this, I don't I'll just make it quick. Look. Look check out

**Dave Jones:** the DC offset. You might think this thing is a champion. It's going to go up to Look at this. 20 V. WOW, THIS THING'S KILLER, RIGHT? Wha No, it's not. It's actually only 2 V. If I go to the probe and I set that

**Dave Jones:** back to 1 to 1 and then we do the same thing again, you'll see it's now only 2 V offset. That's its true offset voltage. So, don't be fooled by a scope thinking that it has a 20 V offset like it

**Dave Jones:** actually on the front end it's able to offset plus minus 20 V. It's not. It's only plus minus 2 V. It was fooling you by having that um by multiplying that with the times 10 indicator. But Dave, this is a 10 to 1

**Dave Jones:** probe. So, the 5 V that we're feeding in here should come out of here at 500 mV. So, it should be able to offset that. So, once I apply the correct offset, you can see that that times 10 probe there matches quite

**Dave Jones:** well. It's a little bit, you know, a little bit noisier, but um not too shabby. So, we can still with the times 10 probe, we can still measure a 5 V rail because it's only 500 mV offset due

**Dave Jones:** to the times 10 division, which means that our 2 V offset scope can still do it. Beauty. And you've seen this in previous videos on uh probing. I'll link it in if you haven't seen it. This is a

**Dave Jones:** coaxial cable probe with a series 1 K resistor in there and this is called a Z0 or Z not uh probe and it's uh basically a do-it-yourself gigahertz bandwidth on this depending on the uh coax you use and it's basically a a 1 K.

**Dave Jones:** Uh you got to use 50 ohms on the other end on the uh oscilloscope, but you can get a high bandwidth probe for practically nothing. It's just a bit of coax and a resistor and that's it. So, with 1 K resistor and 50 ohm load, we

**Dave Jones:** get just over uh 20 division ratio. I can program that in directly on this particular scope, but so it's a high division ratio, but you can choose your own resistor. It's just a uh DC loading thing. And if you're measuring a power

**Dave Jones:** supply, you know, a 1K load or a bit lower is is neither here nor there, really. And there you have it. Look at the result. That is my Z0 probe in blue there. And it's just you can make it for

**Dave Jones:** a couple of bucks. It's easy. And once again, this is the power rail probe there. So, fantastic, isn't it? Look at that. So, you don't actually have to buy one of these Wizbang power rail probes or one of these beat Wizbang active

**Dave Jones:** probes to get a high bandwidth like power rail probing solution. You can just use your 10 to 1 probe. You can't use a 1 to 1 probe cuz I've done a video on that breaking down the issues with 1 to 1 oscilloscope probes. They've

**Dave Jones:** got a very low bandwidth, only like 5 MHz, 10 MHz, something like that. So, yeah, you're not going to get the bandwidth out of it. But hey, you can just roll your own coax here and Bob's your uncle. And provided you have some

**Dave Jones:** sort of divider on there, that's going to allow you to use your DC offset voltage on the input of your oscilloscope here. Most oscilloscopes, as you saw like that Keysight one, only had 2 V. Most are going to do plus minus

**Dave Jones:** a couple of volts. Some other ones do better. But here's the interesting thing to note about DC offset on oscilloscopes. It will change depending on the volts per division setting you're on because the front end actually has relays in there that click different

**Dave Jones:** attenuators and amplifiers in there to give you all the different ranges, of course. So, if I put my microphone up to this, hopefully you can hear it switch. Listen. Between 100 and 200 mV there, there is a relay click. So, it's actually changing

**Dave Jones:** the front end. So, that's also going to potentially change your maximum DC offset range, as well. And there's another click between 1 and 2 V. So, that's going to change it as well. So, if we go to our

**Dave Jones:** 100 mV per division, you'll see that it's maxing out at plus minus 1.5 V here. It'll always be the same on the positive side as it is on the negative side. But, if we jump it up to that 200

**Dave Jones:** mV range, we'll find that we can actually go above that. In fact, we can go a long way above that. But, typically when you're using measuring power rails, you you usually at low voltages. And bingo, it goes to plus minus 15 V.

**Dave Jones:** Isn't that neat? And once again, you've got to test this at the appropriate ratio of 1 to 1 so that you're not input referred multiplying your range there. And if we go up to 2 V, where it clicks

**Dave Jones:** again, then let's go let's go. Look at this. >> [laughter] >> We can really go up in the offset voltage, too. You guessed it, offset. But, it's not actually offsetting it by 150 V. It's because there's attenuators in

**Dave Jones:** there that attenuate the signal before it gets to the amplifier which has the offset adjustment. So, it there's not actually 150 plus minus 150 V voltage rail on your analog to digital front end there. That's not how it's uh working.

**Dave Jones:** It's all working with dividers and whatnot. This Rigol DHO 800 uh series 12-bit jobby, um it the scale jumps. I can hear the relay clicking at 50 mV. So, that's where we'll take our offset from. And on the lowest range there, you

**Dave Jones:** can see that we're going to max out at one plus minus 1 V there. Not much, but that will go up if you choose 100 mV range instead. Looks like 200 mV range, we should find uh yeah, there we go. We can go to 8 V. So, not

**Dave Jones:** 10, but 8. This Siglent SDS 800X uh series HD, new 12-bit jobby, very nice. Plus minus 8 V. Beautiful. The duxiest of ducks guts, the MSO 4 from Rohde & Schwarz, let's have a look. It can go to 5 plus minus 5

**Dave Jones:** V. But, there's not just a difference between brands, there's actually a difference between models as well. This uh Siglent SDS 2000X HD series, it'll actually go to plus minus 16 V. Groovy, huh? The Rigol HDO 4000, unfortunately, once again, only plus

**Dave Jones:** minus 1 V. And the Rigol HDO uh 1204, well, once again, plus minus 1 V maximum there. So, um yeah, nothing you can really do there. That just seems to be a limitation of their uh new front end.

**Dave Jones:** But, it's a super cheap front end. Um you get the bandwidth for nix, but plus minus 1 V is still usable. If you use a times 10 divider probe, you can easily do your 5 V rail. You could even do a 10

**Dave Jones:** V rail. And I know it's going to be the same. The MSO 98 1 GHz bandwidth for practically nothing. Um and yeah, it's only uh 1 V as well. But, of course, like you can go to There's a relay

**Dave Jones:** click. You can go up to 100 mV. If you do that, you're going to go all the way with your old mate J right up to 10 V. And you're still and down at you know, 100 mV per division, which is pretty

**Dave Jones:** decent. So, you know, it's good enough for Australia. Now, for your very keen eyed, you would have noticed a big difference between both the uh Key- Keysight and Rohde & Schwarz and the Rigols and the Siglents. So, the two big

**Dave Jones:** name ones versus the two uh like lesser name ones, there's actually a big difference. Let me show you. You'll notice as I move the trace down, I'm adding that DC offset, okay, in the front end, but it's showing up as

**Dave Jones:** positive. It's showing up as plus voltage. And the further I go down, the more it goes positive. It doesn't display negative. So, then if I move it up like that, does it go negative? But look at the Siglent here. As I go down,

**Dave Jones:** it's increasing, but it's showing up as a negative voltage there. So, both the Siglent and the Rigol show negative when you go like in the down direction, whereas both Keysight and Rohde & Schwarz show it as a positive. Isn't

**Dave Jones:** that interesting? What's going on there? It's really It depends how you think of it, whether or not it's like input-referred, um so to speak, which means that, okay, I've got to shift my waveform down by 5 V. In that case, Siglent and Rigol

**Dave Jones:** saying, "I've got to add negative voltage negative like 5 V in there." Whereas the Keysight and the uh Rohde & Schwarz show that, "Well, I've got to offset it by 5 V." I It doesn't think about adding the

**Dave Jones:** negative kind of thing. So, I don't know. Which one's right? Which one's wrong? Eh, six of one, half a dozen of the other. Leave your thoughts in the comments. Who's got it right? So, I hope you found that video interesting, how to probe a

**Dave Jones:** high-bandwidth uh power rail on your circuit, cuz you may want to do this for all sorts of uh reasons, you know, signal fidelity uh stuff, things like that, decoupling, um all sorts of, you know, ground system issues and stuff

**Dave Jones:** like that. You often need high-bandwidth probing of your power supply. And you can do it pretty cheap and simple just using your times 10 probe. Good enough for Australia. A cheap and simple uh coax Z0 probe the series resistor, no

**Dave Jones:** worries. Um most of the oscilloscopes are going to have with an input divider, they're going to have enough um DC offset range to do that. Although, something like this uh power rail probe like a hundred bucks, you know, really

**Dave Jones:** good value. It can do up to plus minus 24 volts um offset. And uh you saw this active probe, even though it's a couple of thousand dollars, it can do like uh yeah, plus minus 20 volts offset. So,

**Dave Jones:** you do get the higher offset uh advantage there. But, you know, using your basic um probes that you already have, no worries. Anyway, if you like that video, please give it a big thumbs up. As always, discuss down

**Dave Jones:** below. And you can support the EEVblog by going to the EEVblog.store, buy a multimeter or something. Catch you next time.

**Dave Jones:** >> [music]
