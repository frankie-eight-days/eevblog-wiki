---
video_id: _k5MrB99lpU
title: EEVblog #1118 - Why Are Studio Monitors Noisy?
url: https://www.youtube.com/watch?v=_k5MrB99lpU
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 33, "3": 55, "4": 64, "5": 77, "6": 104, "7": 113, "8": 122, "9": 130, "10": 144, "11": 152, "12": 166, "13": 180, "14": 193, "15": 204, "16": 212, "17": 226, "18": 239, "19": 251, "20": 261, "21": 275, "22": 285, "23": 295, "24": 307, "25": 319, "26": 328, "27": 343, "28": 360, "29": 380, "30": 393, "31": 404, "32": 417, "33": 429, "34": 442, "35": 453, "36": 469, "37": 482, "38": 492, "39": 516, "40": 530, "41": 549, "42": 569, "43": 597, "44": 610, "45": 625, "46": 651, "47": 663, "48": 691, "49": 705, "50": 720, "51": 734, "52": 749, "53": 758, "54": 767, "55": 775, "56": 790, "57": 803, "58": 819, "59": 836, "60": 854, "61": 865, "62": 874, "63": 891, "64": 907, "65": 923, "66": 946, "67": 959, "68": 973, "69": 989, "70": 1001, "71": 1016, "72": 1028, "73": 1037, "74": 1060, "75": 1073, "76": 1089, "77": 1099, "78": 1114, "79": 1131, "80": 1143, "81": 1160, "82": 1169, "83": 1188, "84": 1202, "85": 1221, "86": 1232, "87": 1246, "88": 1258, "89": 1275, "90": 1303, "91": 1312, "92": 1323, "93": 1335, "94": 1344, "95": 1358, "96": 1368, "97": 1381}
---

**Dave Jones:** Hi, you've seen my KRK Rokit or Rocket 6 powered studio monitor speakers that I use for my video editing before. I've done a repair video on these which was really fascinating which I'll link in down at the end or down below.

**Dave Jones:** There's one interesting thing, not with not just specific to these KRK monitors, but most studio monitors on the market regardless of the brand, it doesn't matter whether they're KRK, they're Yamaha, they're JBL, they're Alesis, you know, Mackie, any of the top brands, they will have a noise floor to them.

**Dave Jones:** These powered monitors that have the amplifiers built in. If you don't apply any signal to them whatsoever, and you actually put your ear up to the tweeter like this, and the woofer to some respect as well, but it's more pronounced on the tweeter, you can actually hear a low-level hiss on there.

**Dave Jones:** And it's got nothing to do with system interconnections or anything else. It's got nothing to do with the fact that I've repaired these or the black existing black gunk or anything like that.

**Dave Jones:** It's basically inherent in most studio monitors. There are reported to be some that don't have any audible background noise floor hiss on them, but I think they're, you know, reasonably rare.

**Dave Jones:** So, it's as common as mud for these things to have them. And I thought I'd just investigate why that's the case. First of all, though, I'll get my mic and I'll actually put it right up to it and I'll get see if I can actually record the noise floor for you.

**Dave Jones:** Okay, let's see if we can actually do some simple analysis of or at least look at the FFT response of our audio captures here that we got from the woofer and the tweeter.

**Dave Jones:** Now, this is the woofer file here. This point in here is uh just the background noise when I had it switched off. So, from here to here is the power up mute function.

**Dave Jones:** It lasts for about a half a second second or something like that. And then this is the woofer noise in here. And we can see the spectrum down the bottom here.

**Dave Jones:** Now, I'm using um NCH WavePad here, Australian software. I don't know why they don't um annotate these axes on here. So, anyway, it's frequency and we can see the frequency on the curve.

**Dave Jones:** So, you can see it here. This is a peak at around 100 Hz. This is what we're uh interested in with the woofer. See how it's right there They're in mute mode.

**Dave Jones:** There was a 100 a significant uh quite louder 100 Hz uh peak there. Now, we're listening to the woofer. You can see that the spectrum here is actually quite broadband compared to the bass room noise.

**Dave Jones:** So, this is just picking up from the microphone. And then that is the inherent noise floor of the uh woofer and the low frequency amplifier in there. So, you can see, you know, there's not a huge amount difference in there.

**Dave Jones:** Once again, you have to put your ear right up to almost touching the cone to hear this. But, you'll notice that there is that 100 Hz peak there. So, of course, 100 Hz we have 50 Hz mains here in Australia.

**Dave Jones:** So, the 100 Hz is the full wave bridge rectified uh frequency of this thing. So, that's obviously coming through the 100 Hz ripple on the power supply. So, that's coming through.

**Dave Jones:** So, that's not great system design, is it? They could have you know uh put some extra measures in place to filter that out, but they didn't. But, as I said, it's very low level.

**Dave Jones:** So, it's not really a problem, but it's just you know, it's there and you can technically hear it. Everything else is like fairly broadband noise as you'd expect. So, the tweeter this is the switch on point here.

**Dave Jones:** This is the uh mute period and this is the noise. As you can can it's quite high and you can see that it is fairly broadband right across the uh spectrum there, as you'd expect.

**Dave Jones:** So, this is the background. This is when it's switched off. So, this is the background room noise. And then that is the signal level. You can see it's much higher than we saw before on the woofer.

**Dave Jones:** So, it is quite significant. You can see some roll off there at uh what, 15 odd kHz there. So, I don't know whether or not that's the measurement mic or, you know, the speaker rolling off.

**Dave Jones:** You get fairly consistent broadband noise across the band there, and that's what you expect from uh typical component thermal noise and resistor thermal noise and all the rest. You expect a broadband response, and that's what we get.

**Dave Jones:** We get no 100 Hz uh there at all because it's a um high-pass filter. So, it filters out, you know, anything below I think crossovers like 2.8 kHz or something like that.

**Dave Jones:** So, you wouldn't have expected that to come through, and it doesn't. So, there you go. Just an interesting look at the spectrum response of this. Room noise, tweeter. Hmm.

**Dave Jones:** And this noise has absolutely nothing to do with the uh the volume or, you know, high frequency adjust or anything like that. Makes no difference whether you turn that volume all the way down.

**Dave Jones:** It's an inherent system noise floor. Um and that's just manifests itself with the uh wide dynamic range uh speakers and the gain of the amplifier. But, where is that noise coming from?

**Dave Jones:** That's what I'm interested in. And the other thing you got to remember is that this noise, although you heard it uh like it sounded really bad there, it is barely audible.

**Dave Jones:** You've got to put your ear practically right up to the tweeter or the woofer in order to actually uh hear it. So, you know, maybe in a dead silent room you can hear it at a little bit of a distance, and some monitors are worse than studio monitors are worse than others in this aspect.

**Dave Jones:** You can sort of, but know, hear the background hiss from further away, but it's really not an issue because when you play your music or your audio, whatever it is you're mixing on your studio monitors, then it's you know, so far in excess of this noise floor that it's not a problem.

**Dave Jones:** You just don't hear it. It's literally down in the noise floor. Now, if we have a look inside, we've got our main power amplifier board down here which main has our main power amplifier chip in it for both there's a separate one for both the high frequency and the low frequency driver.

**Dave Jones:** It separates them and it does that over on this board here which is the input board which has Japan Radio Corp 4580 op amps on there classic audio amplifier chip.

**Dave Jones:** You know, they're quite low noise, low distortion, everything else. But we don't know. Is the noise coming from these? Is it coming from the power amplifier chips? Is it a combination of both?

**Dave Jones:** It is inherent system noise floor. No, it's got nothing to do with that these boards aren't shielded or anything else, you know, like in terms of can shielding. It's got the metal plate on the back, but you know, it's got nothing to do with that.

**Dave Jones:** It's inherent electrical noise floor of the circuitry. But where does it come from? So what I'm going to do is I'm going to separate this preamp and filter board from the audio amplifier.

**Dave Jones:** Now, the audio amp and power amplifier has its own pull down resistor on the input. So if we disconnect the cable from the input, it should be fine. The signal will be pulled down to signal ground and not a problem.

**Dave Jones:** So we First thing to do is just isolate whether or not noise is coming from here or whether it's inherent in the power amplifier on the back board. Okay, so I've got it disconnected here.

**Dave Jones:** It's powered on. Can't hear a thing. Aha. What I'm doing now is I've taken the front panel off. I've connected my voltmeter across AC voltmeter across the 4 ohm tweeter here, and let's have a look.

**Dave Jones:** We're getting about This has like a normal like a 100 kHz plus bandwidth, so it's more than capable of getting the average AC noise level. Now, if we switch it off, just to show you that we actually get nothing there, just a little bit of residual book.

**Dave Jones:** There we go. So, we switch it on, and it goes through It's got an auto mute thing for a couple of seconds before it turns on. There you go.

**Dave Jones:** You know, 245 microvolts AC or thereabouts as well. But, let's try the high frequency adjust here. It's dropping. Look at that. It is going down. So, that does show that this is, of course, on the input filter side of it.

**Dave Jones:** So, here's the schematic for that. You can see where that is. So, it looks like the noise is coming from that front end. With the Japan Radio Corp 4580 op amps.

**Dave Jones:** If we actually disconnect the front end like that, hardly anything at all there. So, yeah, but it's certainly not at the same level we're getting before. That's interesting. And we can see that the volume control here does have a little bit of effect.

**Dave Jones:** So, we're talking like, you know, five or six microvolts here of extra noise. But, so, if we knock the high frequency adjust right down and the volume right down, we can go down to 220 odd, but yeah, like it's We can still hear it.

**Dave Jones:** Anyway, as you can see on the schematic, we've got U1 here, which is the input balance and unbalanced amplifier and then it goes into the control pot VR1 here, which is the the back panel volume control and then that branches off into the low pass amplifier, the low frequency amplifier and the high frequency amplifier part of which half of which is in U2 here.

**Dave Jones:** So, we know the volume pot has some factor into the noise. We know that the high frequency gain adjust here has some impact on the noise and things like that.

**Dave Jones:** So, yeah, we need to start isolating the amplifier, but what's interesting here is the type of op-amp, too. You notice that it's the JRC 4580D and that D on the end actually matters because you can buy this chip in two different classes.

**Dave Jones:** If you have a look at the data sheet, you can see that the not the standard non-D part is actually only specifies a typical noise floor figure of 0.8 microvolts and we won't worry about the conditions under which that's under, but you can see below that that the D part doesn't specify a typical, but it actually specifies a maximum of 1.4 microvolts equivalent system noise floor.

**Dave Jones:** So, there you go. So, they are actually using the higher quality part in here, which has a guaranteed noise floor. Nice. Now, this is where you might have to start getting into resistor noise as well.

**Dave Jones:** You know, you've got to take this into account. So, let's take the RH 10 there, which is a 20K resistor. A 20K resistor at over a bandwidth of 20 kHz has an inherent thermal noise of 2 microvolts, you know, which is enough all, but when you're around with this sort of stuff, you might have to take that into account, but let's go, you know, the resistors aren't the

**Dave Jones:** problem here. If you're curious to know what I'm getting between the two uh ground points RH10 over here and uh R uh 29 over here, yeah, 50 microvolts. And that does actually go away if I switch it off.

**Dave Jones:** But relatively speaking, across um RH10 there, which is the one including the ground reference here, that goes over the cable to the uh power amplifier, then that's our noise floor going into the power amp.

**Dave Jones:** And yeah, that would almost explain it cuz the power amp has a gain as well. Okay, what I've done is actually lifted RH9 in there so that the signal's actually decoupled from all the input amplifier and everything else.

**Dave Jones:** And look at this, it's much higher. It's uh that's referred back over the cable to the basically the input of the power amplifier. So, we've disabled Well, there's a there's a resistor on here.

**Dave Jones:** We're measuring across the resistor, but that's about it. It's it's disconnected from the rest of the circuit. And yeah, look, I can feed in noise. There you go. Feed in crap just by touching that.

**Dave Jones:** And if you're curious to know, do we get still get the noise? Well, I can hear it from here. But here's the problem with uh audio system design like this.

**Dave Jones:** But we don't have a wire flapping around in the breeze. Kind of. Not the input wire cuz we're still got that 20K resistor that we're measuring across in that board.

**Dave Jones:** I can hear it all from here. The hum is really actually quite loud, but if I actually disconnect this, the hum is gone. You'll have to trust me. It's now not loud.

**Dave Jones:** But the hiss is still there. So, it's nothing to do with the input uh amplifiers there at all. Nothing to do with the balance input amps. Nothing to do with that uh high-pass uh stage and all that sort of stuff.

**Dave Jones:** It's still there. It's coming from that cable or the power amp. Finally isolated it. So hopefully you can see the almost futility in trying to track down system stage noise with a multimeter like this and these the big antenna leads.

**Dave Jones:** We we got some useful information back when over on like 29 over here was it where but it's like low impedance. So when you got probing those low impedance stuff all the crap you're picking up from your test leads and everything else isn't going to matter a rats.

**Dave Jones:** But when we've got like just a 20K input resistor which is the one over here that we're measuring and we disconnected that we've got a relatively high impedance now and when you start having these big antenna cables flapping around in the breeze just picking up all sorts of whatnot crap it just introduces more noise than you're actually trying to measure.

**Dave Jones:** But of course you know we were just mucking around trying to trace some system noise voltages there. We didn't have to do that. We could have easily come to this conclusion without a multimeter at all.

**Dave Jones:** We could have just gone to the schematic and gone well let's just disconnect RH9 there which disconnects basically all of the internal circuitry but leaves the cable in place going over.

**Dave Jones:** Bingo we've still got effectively the same noise. We can hear it in the tweeter so therefore it's none of the input circuitry here. So if we went and you know if we were an audio fool and went in and started changing all our op amps to some super whiz-bang thing wouldn't have made a rats ass difference.

**Dave Jones:** Let's go over to the main power amplifier board and instead of disconnecting the cable over here which affects the mute and everything what I've done is desoldered one end of input AC coupling cap for the thing.

**Dave Jones:** So really now this power amplifier is not connected to that input cable at all. It's only got its own internal resistors caps and traces and everything else. Switch it on.

**Dave Jones:** It's still there. Might even say it's a little bit lower. Turn it the right angle. Yeah, but it's still there. And you kind of expect that in theory of course cuz those all those op-amps on the input pre-amp and filter stages the NJM 4580s they're really not low noise and they've even specified the particular part for that.

**Dave Jones:** But if you have a look at the power amplifier used in the tweeter amp high pass high frequency amplifier here, you notice it's input referred noise is only a couple of microvolts as well.

**Dave Jones:** But if we have a look at the schematic here and look at the feedback resistor 12K and the input resistor it's got a gain of about 26. So any input referred noise is going to get multiplied by that gain.

**Dave Jones:** Once again, if you look at the data sheet and that input referred noise figure, then it's only a couple of microvolts and you multiply that by the 26 gain, that doesn't get the output noise that we actually measured across the 4 ohm speaker.

**Dave Jones:** But if you look at the maximum figure, it could be as high as 10 microvolts and in that particular case, yeah, multiply that by 26, that's almost the exact figure that we're seeing.

**Dave Jones:** So are we seeing just the worst case amplifier noise here? I don't think so because and that would be like this is inherent across all the speakers. It's not just this oddball one that I've got here.

**Dave Jones:** So it's you know, we're going to get our typical figures there. So that noise, there must be some extra noise being introduced somewhere in the power amp. But there's something interesting here.

**Dave Jones:** We didn't hear it when we disconnected the input cable which I believe puts it into mute mode. And sure enough, when I power this thing up, there is no noise at all.

**Dave Jones:** No, really no audible noise. Maybe the tiniest little half a bee's dick of noise. But, if you have a look at the schematic which shows how the mute system actually works, it's just switching between a different input which either goes to ground via a 22k resistor or goes via the input that capacitor that we disconnected up here and a parallel 10k resistor.

**Dave Jones:** So, the thermal noise of a 10k resistor around about, you know, just under 2 microvolts or thereabouts over the bandwidth that we're talking about. So, really it can't be that.

**Dave Jones:** Uh plus the fact that the in mute mode, you're going across a 22k resistor which is more than double. So, yeah, it's not that. I still think maybe it's a, you know, a small contribution, but I think the noise is coming from somewhere else.

**Dave Jones:** It's got to be like system related, layout, ground, everything else. So, what I've done is actually just for kicks shorted out R H100 here, which is that 10k input resistor.

**Dave Jones:** And nope, just tested it, noise is still there. It ain't that. And even if you disconnect that input trace, which is what then takes the trace all the way up to the top to the cap which we've taken out up here, then it's still there.

**Dave Jones:** So, it's all happening down around that power amp. If you have a look at the power amp here, this is the trace that comes down from the input that AC coupling cap, jumps over this goes over this jumper here, goes across.

**Dave Jones:** There's our 10k down to ground, and there's a parallel cap as well, and that just goes into pin seven of our amp there. So, it doesn't get any simpler than that.

**Dave Jones:** So, our power amplifier is now simply terminated with a 10k resistor and a cap there. That's it. Yet, it still generates the hum. So, yeah, we've isolated it down to just the amp.

**Dave Jones:** And if you might think it's, you know, something to do with the mute path, well, the pin five is the mute input there and there's the resistor you're jumping straight over to the same ground there.

**Dave Jones:** So, no problems whatsoever. It's not sneaking in there. And even if I disconnect uh H106 here, which goes off to the mute function via the diode off to the input and I ground that, so I'm actually uh disabling the mute function altogether and always having it in play mode, I still get the noise.

**Dave Jones:** When when this amplifier goes into mute mode, it actually mutes the output properly, even though it's just switching the input according to the schematic. Aha, check this out. It's different to the schematic.

**Dave Jones:** The schematic just shows that the mute function just switches between the inputs here, right, and doesn't disable the output pair amp. So, that's why I was getting you know, noise when I selected the pin seven here.

**Dave Jones:** When you select the non-mute function, the just the regular play mode, and you disconnect the capacitor here, you disconnect all the traces, you've only got a 10K going to ground and we get the noise.

**Dave Jones:** We get the hiss. But then you select mute mode pin five here and you don't get it, which has the exact same Well, it's got a double the amount of resistance going to ground.

**Dave Jones:** But if you actually go look at the actual internal schematic, aha, there it is. You can see that the mute standby switch here goes through into these two comparators here and these are the voltage threshold limits.

**Dave Jones:** So, anything below 1.8 volts, it actually uh, switches into shutdown. Here's the output amplifier block and it shows it it going into there and disabling the output amplifier. So, that's why there is no noise.

**Dave Jones:** It's completely silent when you put it in standby mode. So, that explains that why it's silent in mute mode. And but anyway, it looks like all the noise is coming from the power amp itself because it as I said, if I disconnect CH100 there and all the traces going to it, even if I disconnect the mute, you know, I thought maybe there's some, you know, cross talk between the mute pin

**Dave Jones:** and noise coupling over or, you know, some weird thing like that. So, removed RH106 here, we still get the noise with just this 10K input resistor here. What do you do?

**Dave Jones:** I mean, it's only got a couple of microvolts noise, a couple of microvolts for the chip. It doesn't really add up to what we're measuring. It's inherent in that.

**Dave Jones:** I don't know, is there any pin compatible one you can whack in that's inherently low noise, but it's already pretty low noise. But with the thing the massive high dynamic range of this tweeter, even a couple of 100 microvolts noise is audible.

**Dave Jones:** You can hear it, you know, it's down in the microwatts region or whatever, but you know, it's like 80 dB down on 1 watt, but you can still hear it.

**Dave Jones:** And they actually designed the preamplifier input with spec those low noise op amps, so it didn't really contribute much if anything to that system noise level, which is quite nice.

**Dave Jones:** Couldn't really hear the difference when I like disconnected the input amp. So, those 4580 op amps really aren't contributing pretty much anything at all to that. So, there you go.

**Dave Jones:** Fascinating. We narrowed it down inherent in the amplifier. Anyway, I hope you found it interesting. If you did, give it a thumbs up. And as always, you can ask down below or on the EEVblog forum.

**Dave Jones:** Catch you next time.
