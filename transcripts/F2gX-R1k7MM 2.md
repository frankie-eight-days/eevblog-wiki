---
video_id: F2gX-R1k7MM
title: EEVblog #855 - Ceramic Capacitor Piezoelectric Effect
url: https://www.youtube.com/watch?v=F2gX-R1k7MM
source: youtube-asr
timestamps: {"0": 0, "1": 21, "2": 34, "3": 61, "4": 91, "5": 113, "6": 135, "7": 171, "8": 206, "9": 224, "10": 257, "11": 289, "12": 318, "13": 332, "14": 365, "15": 405, "16": 422, "17": 462, "18": 480, "19": 504, "20": 536, "21": 565, "22": 598, "23": 630, "24": 653, "25": 682, "26": 704, "27": 737, "28": 770, "29": 794, "30": 825, "31": 841, "32": 883, "33": 900, "34": 928, "35": 956, "36": 971, "37": 985, "38": 1002, "39": 1028, "40": 1049, "41": 1077, "42": 1091, "43": 1126, "44": 1167, "45": 1186, "46": 1210, "47": 1243, "48": 1272, "49": 1306, "50": 1328, "51": 1342, "52": 1354, "53": 1373, "54": 1391, "55": 1410, "56": 1425, "57": 1456, "58": 1483, "59": 1514, "60": 1540, "61": 1555, "62": 1578, "63": 1593}
---

**Dave Jones:** Hi, this should be an interesting little video. It involves my new EE Blog BM235 multimeter and this is something I didn't realize, but uh people who have bought this um a couple of reports started to flow in that it actually produces a high-pitched uh whine when you turn the backlight on like that.

**Dave Jones:** There's a very faint, if you put your ear like some people can like hear it from you know like standing distance away, other people have to like put it right up to their ear to hear the thing, but it's producing a high-pitched tone.

**Dave Jones:** Now, I didn't actually notice this when I uh evaluated the original unit and um ordered these things. Um but uh sure enough it is on the original one as well, but I've got to hold this trust me right up to my ear to sort of do that. So, there see and I've tested various um I had like you know still had 20 or something here and I tested various ones and there seems to be quite a significant difference between units.

**Dave Jones:** Some are louder than others and there seems to be a slightly different uh frequency between uh units as well. So, I thought we'd just do an investigation, but it's already been done by um some forum uh members and people on the uh EE Blog IRC channel. Yes, there is such a thing. Apparently, there's people who hang out on the EE Blog IRC channel and uh they discovered the uh problem in this thing and uh so, we do know the solution, but hey, I thought we'd just

**Dave Jones:** take a look at it because it's interesting and it's something I've mentioned way back in episode number 33 part two back when they YouTube had 10-minute time limits. I had to do two parts. Hmm. Now, I'll do my best to try and get this sound on the microphone here. It's incredibly difficult. I've tried different microphones and things like that, but I'll give it a bash. Here we go.

**Dave Jones:** And that if I speak very softly and whisper, I've got my gain turned all the way up. And maybe you can hear it. Shh. So, that's the backlight on and I'll turn it off.

**Dave Jones:** That's now off. It should be gone and back on. So, there you have it. You clearly heard that tone there. It's around about 5 kHz or so and it's clearly coming on when you turn the backlight on. Otherwise, it's a completely silent. So, it's something to do with the backlight inverter circuit that's actually driving the LEDs in here because this thing is only powered from two AA batteries, right? So, they're 1.5 V maximum 3 V maximum. So, the white LEDs in here obviously need at least that to work.

**Dave Jones:** So, when the batteries drop, they haven't got enough voltage. So, there needs to be some sort of boost converter in here to actually drive these LEDs and that's what the the problem is. So, I won't leave you hanging. Yes, it is the backlight circuitry in here. But, if we have a look at inside this thing, then when you hear something like this, there are three typical reasons why you would hear some sort of whine or tone coming from an instrument. But, all of them involve some sort of electromechanical

**Dave Jones:** process that you know generate to something needs to vibrate to generate the sound the audible sound that you're hearing. And of course, the prime culprit might be Look, we have a little piezoceramic buzzer inside this thing. It's designed to generate sound. Is it that perhaps?

**Dave Jones:** So, you'd naturally think of that. But, that's fairly easy to rule out. Now, the second one is in inductors. Inductors can actually um they're they're coils of wire and at the right frequency they can actually uh vibrate and do things like that. Well, the only inductor in here is this puppy on the bottom, but and and it looks like Oh, look, here's the backlight the springs for the backlight down here. Here's the backlight board with the LEDs on it down here and you might think Oh, it's going over to the

**Dave Jones:** inductor, but if you actually follow the traces, it's not. I believe that inductor, I don't have the schematic for this, but I believe the inductor is actually part of the um electric field detection uh circuit. So, it's got nothing to do with the backlight at all. Now, another common one is uh transformers. Of course, they've got laminations of material in there and if they're not uh very tightly mechanically bound, they can actually vibrate. And you may have heard that classic, you know, 50-60 Hz transformer hum coming from an

**Dave Jones:** instrument. Well, it's clearly not that. We don't have any uh transformers in here. They're not uh whining, you know, especially like a switch mode DC-to-DC uh transformer which operates at higher frequencies, which can be in the audible uh range, by the way, if they're uh you know, that lower frequency. Usually DC-to-DC converters are a higher, you know, frequency in the you know, in the non-audible range, i.e., greater than 20 kHz, you know, maybe a couple of hundred kHz, even in the MHz uh range. So, generally you're

**Dave Jones:** not going to get them from DC-to-DC DC converters, although I have heard them happen in some that operate down in the audible range. But actually, as you can see, there's no traditional DC-to-DC converter in here, no uh transformer, anything like that. So, it's not that.

**Dave Jones:** So, the last remaining one, you have to actually go back to uh episode number 33, part two, as I mentioned uh before, way back in the old lab, when I did a tutorial on uh capacitors. And I mentioned ceramic capacitors and in particular multi-layer ceramic capacitors. As you've no doubt you know little 0603 ceramic capacitors and stuff like that that you typically see in all modern electronics. Well, these can actually be microphonic. They can actually pick up sounds. So, if you're I'm talking now, and trust me these

**Dave Jones:** little multi-layer ceramic capacitors in here will actually be picking up that sound and due to microphonics, they will actually um it be generating a minute might be microvolts, but they'll be generating minute voltages across the capacitor. And that comes about because of the name of the things. It's a dead giveaway, multi-layer ceramic capacitors. And they're constructed using as it name implies multiple layers in there and they're ceramic. So, they actually become piezoceramic transducers just like this little puppy up here. Just like those transducers you used to in all sorts

**Dave Jones:** you've seen all sorts of products. Those little flat piezoceramic transducers. Exactly the same thing is going on except you've got multiple layers inside these multi-layer ceramic capacitors. So, not only are they microphonic and they can pick up sounds, it works in the reverse as well.

**Dave Jones:** They actually exhibit the piezoelectric effect just like a piezoceramic transducer up here. If you apply a voltage to them an AC voltage in the audible range, they may actually vibrate and emit a tone and the PCB can actually help amplify that and other stuff. But, yeah, these things can actually little tiny capacitors in here can generate sound. Amazing. So, given that this buzzer is under software control, comes directly from one of the pins, I don't think it's that given that we don't have any inductors in there in the

**Dave Jones:** circuit. I don't think it's that. We haven't got any transformers in there. Nah, it's not that. What's left? These multi-layer ceramic capacitors. Bingo. Let's go to the data sheet, as you should have done first, and you could have it would have been probably obvious what the culprit was.

**Dave Jones:** So, here we are at the data sheet. The HY2613C is the one we have, and bingo, right here it tells you building charge pump, a LED backlight building charge pump. So, if we go down, we should be able to find this. Um I hope you can read your Chinese, but uh yeah, um internal, we can't see it. Is there a charge pump in there somewhere? There's got to be.

**Dave Jones:** It'll show you somewhere anyway. If we keep going all the way with LBJ down here, then wait for it. Wait for it. Wait for it. All timing diagrams, fantastic. Bingo, here it is. There's our LED driver charge pump, and your typical capacitor charge pump, and you can see that it's actually got a current sense resistor uh down here, so it can actually control uh the current going through the LED. So, it's going to be a constant current generator operating at some frequency.

**Dave Jones:** That frequency we don't know. It's not in the uh data sheet at all, at least well, if you can't read uh Chinese. There it is. Is it 15 milliamps? Is that the uh maximum? Obviously, it's going to probably the maximum. It's going to depend on the resistor value down here, but we can see that we have this uh 10 microfarad Well, assuming that they've uh followed the application note here, there's going to be a 10 microfarad output uh smoothing cap, and there's going to be a 1 microfarad uh charge

**Dave Jones:** pump cap in here. So, there it is. There's the culprit right there, C44 10 microfarad multi-layer ceramic capacitor, and it's probably one of those dodgy, you know, Y5V dielectric material or something like that. You know, the ones that are really horrible, have really horrible thermal and electrical characteristics, but they're great for bypassing applications and you know, stuff like that. They're just fine for it. But, they're a horrible dielectric and they can in theory be more susceptible to this sort of problem. And by the way, this problem

**Dave Jones:** only happens to class two ceramics. I don't believe there's a single case of it ever happening with class one NPO type ceramics. Those zero temperature coefficient ones that are much lower value. So, what we want to do is actually get in here and probe this thing and see what happens. See if we can measure some stuff on here. But, as you can see, the battery compartment has these two springs here and they contact these little pads down here and it's really annoying. I'd have to like solder

**Dave Jones:** some, you know, contacts on there because if I put the go put the board back in, well, we can't probe anything, can we? It's really annoying. Maybe like I could solder some wires on and then bring it back out for example and then screw the board back in and bring it back out. That's one way to do it. And another way to do it, which is what some of the guys on the forum have done, is just physically remove the screen like that, whack the board well, back in back

**Dave Jones:** in. There we go. And then you can access and probe stuff through the front here. But, of course, we're disconnecting the load from this puppy. We're disconnecting the LED. So, I think I'll do it the other way. I'll put the screen back in. I'll solder some wires on to some various places and then we can bring that back out. All right, what I've done is solder four little wires on here. We've got ground and the out main output 10 microfarad filter cap, which is the culprit here. And then we've got

**Dave Jones:** the charge pump capacitor. So, both wires coming out there. I've just bent them around like that. I could actually try and bring it out the optional LED hole here. Well, optional. It's not an option on this model, but there's actually curiously there's a footprint down there. So, maybe I should install an LED on there and see if it you know, see if it does anything.

**Dave Jones:** Anyway, maybe we can probe that. Anyway, I'm going to sit that on there and it is a little bit tricky and we can actually get eventually get contact and power it up. Beauty. And here we go. I'm probing directly across the 10 microfarad output capacitor that C44. That's the output filter capacitor. It's a constant current drive boosted constant current drive and I've got it set to a DC coupling here and my ground points right down there 500 millivolts per division.

**Dave Jones:** So, 1 volt, 2 volts, 3 volts. There we go. So, it's around about that 3 volt level, but we can AC couple that and uh bring that back up here. Bingo. Now, if we have a look at the signal here, you notice that not only does it have this interesting looking uh little bump in there like that, okay, but it's jumping around like a jack rabbit, okay? And if we stop it, you'll notice that there's Look, there is another period inside there. It's sort of oscillating like that as well.

**Dave Jones:** And you'll also notice it's not a fixed frequency either. You can actually see the difference between that that peak and that peak is shorter than the time period between that one and that one. And you can actually hear this. Sorry, I can't mix it directly with the Well, actually, I probably can mix it with the microphone. Hmm. But you can see it jumps between you saw There we go.

**Dave Jones:** Almost perfect, right? It jumps between periods of almost perfect and this is touch sensitive. Try I was getting it before. Trust me, now it's not cooperating. The white coat syndrome. But you can see I can actually get it where it is almost a perfect tone, okay? And you can actually hear it as well. I'll try and mix in the audio in a second if I can get this damn thing to cooperate. But, it is sensitive to all sorts of and it can what There it is. There it is. Bang.

**Dave Jones:** You saw it, right? It was almost perfect. And if you've got your ear up to it, you can actually hear a perfect tone. Okay, I'm whispering again. Hopefully, you can hear this. I'm trying to mix in the audio. I'm using my external wireless mic, and I've really got to turn the gain right up. Here we go.

**Dave Jones:** That's perfect tone. And hopefully, you can hear it glitching. So, as you can see, it's jumping around like a jack rabbit there. I had smoothing mode on before, by the way. I've just turned it to refresh update mode. So, yeah, that charge pump seems to be jumping around like a jack rabbit, like it's got some sort of maybe pulse skipping mode or something like that in it. So, yeah, it's, you know, not a pure tone at all, and it just it it varies like all the time. Just like sitting

**Dave Jones:** like randomly, it seems seems to also vary like just sitting there, it'll vary, and it also seems to vary when I physically touch and, you know, play around with the unit as well. And if we have a look at the frequency of this thing, you know, the frequency counter up here, I don't know what it's detecting anyway.

**Dave Jones:** It's still updating cuz it's a hardware frequency counter in the background. But, I've got my cursors here, and you can see delta T here is 3. 86 kHz. There we go. And if we turn the cursor over to that shorter period there, we're looking at 5.12. So, it's going to, you know, vary and jump between those two frequencies. That's why I it often sounds very muddied. It's not a pure tone at all.

**Dave Jones:** And if we have a look at the waveform on one side of the charge pump capacitor, you can see that or you can see it's switching where it actually switches on here. So, yeah, that's, you know, it's doing Yeah, it's pretty consistent there, actually. But as I said, it varies and the chain the tone changes when I actually disconnect the probe. So, see if we can see a change up here when I disconnect this.

**Dave Jones:** Yep, see? I changed it. The capacitance of the probe. And there's the other line there, not a huge amount of difference. But you can certainly see if I disconnect that probe, I will upset that. There we go. Upset the apple cart. Oh.

**Dave Jones:** Doesn't like it, but it's actually more stable when I actually load it down with the probe. I'm using a times one probe here. I'm not using times 10. If I switch it to times 10, then uh it's still loaded it down somewhat.

**Dave Jones:** There we go. And check out the high-frequency ringing on that. Look at that. Wee! And if we go over here, we'll see it here as well. Love it. Look at that. Beautiful. Okay, everyone wants to see the money shot, which is the microphone.

**Dave Jones:** So, I've got my uh wireless mic the output here. I've got like max gain, so, you know, it's going to be pretty horrible. Channel two, the blue waveform here is obviously my voice. Check it out. There we go. That's my voice and uh I haven't turned the backlight on. So, we'll turn the backlight on, but this is the background level. Okay, so let me show you that.

**Dave Jones:** Bingo. Correlation time. Now, at first it may just look like crap, right? And it doesn't correlate at all. I mean, look, this peak here doesn't line up with this one, but aha, watch this. This is the acoustic delay. If you shift this over to here, and you shift this one over by the same amount, they line up.

**Dave Jones:** So, we've just got some delay there. That's all. A tiny little bit of delay, but it basically this here correlates with this here. This one correlates with that, and so on. This one correlates with that. Bingo. So, it's really difficult to actually pick this up. I'm sorry about that, but we can at least see the correlation there. And of course, if I switch the backlight off, here we go.

**Dave Jones:** There we go. We've just got the background, and you can see that there's no high frequency stuff on there at all. Ah, this is better. I've increased the output gain on the microphone here, and this is what I'm getting. Here we go.

**Dave Jones:** This is much better. And you can have a look at See those peaks? Look at that. Those bottom peaks precisely correlate with a fixed amount of delay. The delay is the acoustic delay. So, um look, I mean, there's, you know, it's not an exact match for the for the voltage waveform on the capacitor, but this has to do with all the piezoceramic nature of the thing and how it actually produces sound. But, as you can see, the frequency correlates, and that is what matters. That's what's producing the

**Dave Jones:** sound there. So, that pain in the ass 10 microfarad multilayer ceramic capacitor, got you. And if I start that again, and then turn off the backlight, that's the normal background. It's just picking up the regular background hum and other crap here in the lab, but none of that 5 uh frequency content. So, that's all very interesting, but what is the fix for this thing? Well, the fix is to uh change that capacitor. Now, this could have happened between uh various batches as well, depending on what uh

**Dave Jones:** 10-microfarad cap, if they didn't specifically specify in manufacturing in the bill of materials a specific part number and model of capacitor always from the same manufacturer, which is, you know, not all that untypical um when you're just talking about a Joe Blog's 10-microfarad uh bypass cap like this.

**Dave Jones:** You might think, well, you know, what's the big deal? It's a 10 Its value doesn't exactly matter, you know, it can be half that, it could be double, you know, it's not a huge big deal. It's just for a backlight here. So, they're, you know, wouldn't surprise me if they haven't specified that. So, the uh purchasing people can just go and choose, you know, I'm pretty much free to choose, if it's not specified, free to choose any capacitor they can get from anywhere, as long as it's a, you

**Dave Jones:** know, exactly the same size, the same voltage rating, it's 10 microfarads, blah blah blah. But, this is a problem that is most definitely going to uh vary between manufacturer of capacitor, between model, between dielectric, between different physical sizes, be it 0603, 0805, 1206, etc. Um what sort of uh current that we're actually what it's filtering, things like that. It's going to vary a lot. So, how can we fix this thing? Well, we can simply try and change the cap either to uh another 10-microfarad, but it's a different

**Dave Jones:** brand, different dielectric, whatever. I don't know. I'll just find one I've got lying around here, replace it, see if it goes away. And here's the first 10-microfarad cap I found uh lying around, 25 V. It's an X5R dielectric, so none of this Y5U rubbish or anything like that, but I don't know what is actually inside this thing. And yes, the X uh 5Rs, you know, your um X7Rs, they can have exactly the same uh piezoelectric effect as well. So, anyway, I'll whack one of these in and

**Dave Jones:** see what happens. And here's a close-up shot of uh the cap I took out there. Just desoldered that puppy. Look, for a 10 microfarads, that is very, very thin. It's not thick like this X5R. So, I think it probably most likely is a Y5V uh dielectric um because that's the only way to You need that uh better dielectric, better in terms of giving you greater capacitance um for size anyway, but much poorer uh performance. So, it's most likely one of those, you know, Y5V dielectrics because

**Dave Jones:** look at the physical size of a 10 microfarads, but I don't know the voltage of it as well. This um X5R I've got here is a 25-V one. Um so, yeah, it's a it's a better technically a bit better dielectric and it's higher voltage, hence why it's bigger. So, I'd be absolutely stunned if this thing um uh produced the same uh frequency.

**Dave Jones:** Anyway, if it does produce a tone, I don't think it will. I reckon there's an 80% chance I'll probably uh fix this thing by whacking in this cap. Let's see. So, did it fix it? Let's find out.

**Dave Jones:** Oh. I can still hear something. It's not the same. It's not even close to being the same amplitude.

**Dave Jones:** Ah. It's really I've got to put it right up right up to my ear to hear that, but it's still Something is still there. So, either it's the new 10-microfarad cap or maybe uh it might be that charge pump uh cap doing a bit as well. So, hmm, maybe change that one, too.

**Dave Jones:** All right, I tried replacing the charge pump cap, that 1-microfarad one. I just whacked in another crappy old um Y5V. I don't even know where it came from, but anyway, um, let's have a look. Tongue at the right angle.

**Dave Jones:** Still there. But, jeez, it's so low. Like, you wouldn't even bother worrying about that. It's just like that is ridiculously low. I mean, I don't even know if I'll be able to capture that on the microphone. And that's what I'm getting now with the backlight on.

**Dave Jones:** Sorry, I don't have any uh sync signal anything to trigger from, basically, cuz I've disconnected the wires, but I turn the backlight off. And now on.

**Dave Jones:** There's something there, but it's barely picking it up. And if there is something there, well, we're talking uh 3.1 kHz now. So, yeah, it's changed frequency, which is exactly what you'd expect uh because you're putting a different cap in there. So, it is looks like it is the new 10 microfarad cap I put in there, but you can see like it basically cannot hear the thing anymore. So, essentially, problem fixed. It's just a matter of choosing the right cap. Some are much more susceptible than others. It's going

**Dave Jones:** to depend on all sorts of parameters, which uh it's almost, you know, suck it and see, really. So, there you go. I hope you found that interesting. Thanks to uh the people on the forum and people who've uh bought this meter and actually reported this thing cuz it's something that I didn't notice it was so low, but once it was reported to me, yeah, I can kind of hear it. But, now I've essentially fixed this particular unit. Uh I've reported it to Brymen. They're going to uh research it

**Dave Jones:** and get back to us, and no doubt they'll uh fix the issue. So, that's an interesting little uh practical example of piezoelectric effect in multi-layer ceramic capacitors. Watch out for it. Can be real trap for young player. You can really come a gata. Um Um ultimately though, it's it's an issue with the chipset. The frequency is down in the audible range and that's just dumb. If they switched it at 20 kHz or 30 kHz or something like that, you know, instead of down at 5 kHz, no one would have

**Dave Jones:** noticed a thing. It can go piezoelectric. Your dog might hear it or something like that, but or your cat, but that's about it. So, yeah, it's just a poor choice of frequency. The frequency might be dependent upon the capacitance though. I haven't looked at it. There's no details in the data sheet for that sort of things. I'll link in the data sheet for the LCD controller for this thing down below which has the building lead charge pump. So, there you go. Hope you found that interesting. If you did,

**Dave Jones:** please give it a big thumbs up. Catch you next time. Oh, by the way, while I was playing around with this I and trying to get the microphone to pick this up various different types of mics. I actually thought I'd try my Stanford research filter.

**Dave Jones:** What is it? The SR something or other. I don't know. SR 650 program will filter you've seen in the previous video. I thought, "Oh, if I can filter out all the other crap, I'll get a nicer waveform and stuff like that." You know, if I can like put in a band pass filter at you know, you know, 3 to 6 kHz or something, then I can filter out all the other crap. I'll get a nicer signal.

**Dave Jones:** Turns out the fan in this thing, as I noted in the previous video I did on this I think, is just so ridiculously loud. It just ruined everything. So, I It's time to upgrade the fan in this thing. Bloody task you with noisy fans.

**Dave Jones:** Hate them.
