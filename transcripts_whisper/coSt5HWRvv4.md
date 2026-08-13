---
video_id: coSt5HWRvv4
title: EEVblog #837 - Reverse Engineering A Valve Headphone Amplifier
url: https://www.youtube.com/watch?v=coSt5HWRvv4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 34, "3": 46, "4": 64, "5": 81, "6": 97, "7": 115, "8": 131, "9": 150, "10": 167, "11": 187, "12": 202, "13": 224, "14": 246, "15": 267, "16": 289, "17": 307, "18": 332, "19": 349, "20": 364, "21": 380, "22": 395, "23": 413, "24": 428, "25": 446, "26": 464, "27": 481, "28": 496, "29": 511, "30": 532, "31": 550, "32": 567, "33": 584, "34": 600, "35": 619, "36": 633, "37": 646, "38": 662, "39": 677, "40": 689, "41": 707, "42": 725, "43": 743, "44": 767, "45": 783, "46": 797, "47": 813, "48": 828, "49": 846, "50": 859, "51": 876, "52": 895, "53": 906, "54": 920, "55": 940, "56": 955, "57": 972, "58": 986, "59": 1004, "60": 1017, "61": 1031, "62": 1052, "63": 1068, "64": 1090, "65": 1106, "66": 1121, "67": 1134, "68": 1154, "69": 1173, "70": 1190, "71": 1212, "72": 1230, "73": 1251, "74": 1268, "75": 1288, "76": 1308, "77": 1325, "78": 1335, "79": 1353, "80": 1374, "81": 1393, "82": 1416, "83": 1430, "84": 1445, "85": 1461, "86": 1474, "87": 1490, "88": 1508, "89": 1528, "90": 1550}
---

**Dave Jones:** Hi. In a previous mailbag video, we took a quick look inside this Zanzu X2U808 valve-based hi-fi amplifier you can get on eBay for like, you know, 50 bucks or something like that. It's one of these things. It uses two JFETs with pilot lights here.

**Dave Jones:** And you can see the little pilot lights in there. Look at them. And of course, yes, it's got the obligatory wanky blue LEDs in there to make them look all fancy-pantsy. Now, a few people asked, do the valves actually do anything in this thing?

**Dave Jones:** Are they actually hooked up at all, or are they just, you know, just there for show? And it's just an absolute joke, because they've just got a couple of regular audio-grade op-amps inside this thing, as we saw last time. But, you know, clearly the heaters are on.

**Dave Jones:** Look, the pilots are on. There we go. We can see them actually heating up there. So it's obviously doing something. And there was another video someone linked in and posted. Somebody else did a teardown of this thing. And they were actually connected, but how are they connected?

**Dave Jones:** Does it, is it, how is it actually in the signal path? Because valves are usually high-voltage operating devices. And we've got, it comes with a 6-volt plug pack, 6-volt DC plug pack here in the back. And we saw some, maybe some boost converter circuitry in there and stuff like that.

**Dave Jones:** But anyway, I thought we'd do a little reverse engineering of this thing, of the circuit in here, and just see what it actually looks like. Let's go. Now, as we saw last time, these are 6J9 valves, and it just so happens we do have the data sheet for these.

**Dave Jones:** These are from Sylvania. So we can get the pinouts for this puppy and trace out the circuit. I'll link in the data sheet down below. And if we have a look at the actual board here, you can see two audio-grade op-amps, classic NE5532s, nothing wrong there at all.

**Dave Jones:** And we've got ourselves our valve sockets, and as we noted last time, it looks like we have a couple of switch mode controllers here, little tiny 5-pin SOT23 there. You can tell it's a switch mode converter, because we've got ourselves a diode, we've got an inductor,

**Dave Jones:** and we've got some output capacitance here, and a controlling element here. So it's clearly a switching converter. We've got another one down here as well. So we've got two switching converters, and what they're actually doing, what voltages they're generating, what for, etc., we won't know until we actually take a look at the circuit.

**Dave Jones:** And look, I mean, the valves are clearly connected in here in some way, shape, or form. At least, you know, a good lot of the pins are. I'm not sure if every pin's actually connected. But yeah, there's not a lot of complexity in that circuit at all.

**Dave Jones:** So we shouldn't have too many problems, actually, reverse engineering that. One of the issues with reverse engineering, and I've done a video on this, on how to reverse engineer. In that case, it was the Rigol DS1054 analog oscilloscope front end. So I'll link that one in if you haven't seen that.

**Dave Jones:** So I won't go into detailed explanations of how to reverse engineer this. Suffice it to say that it's much easier when you have a double-sided board like this. And, you know, through-hole parts, fairly easy to trace everything, so shouldn't take me too long.

**Dave Jones:** Well, I thought I had the data sheet, and here it is. It's the 6J9 from Sylvania. And this has 6J9 written on it. And it's a triple triode. Okay, fantastic. Basically, essentially, three JFETs with pilot lights in the one package. But it's in a 10-pin bulb, and that didn't register until I went to look at the pin out here.

**Dave Jones:** I labeled things, you know, there's the cathodes, the gates, the plates, the heaters. Everything's fine, but this one is only 9 pins. There is no tenth pin for the cathode. So I'm not sure if it's the same thing, but without the cathodes, making two of them essentially useless.

**Dave Jones:** Two of the triodes useless, or what? I've no idea, what the? And as it turns out, I look inside this thing, and this pin here, you can see, is not actually connected to anything at all. So, yeah, what the? Nothing matches up. Ah, trap for young players.

**Dave Jones:** Even though this is a 6J9, it's actually got 6J9 space-based, you know, J, sort of like hanging on the end of it. And this is apparently a replacement, and if you look at the eBay ad, they actually say that that valve is actually a replacement for,

**Dave Jones:** it's not actually a genuine 6J9 from Sylvania, which we had the data sheet for, which didn't actually make any sense, because it's a triple triode, you know, designed for RF amps and VHF stuff. You know, it didn't, too complicated, too high frequency, didn't seem to make sense.

**Dave Jones:** But it's actually a substitute for the E180F, which they also mention in the ad as well, in the eBay ad. So, you look up the data sheet for that, and sure enough, it's a pentode designed for wideband application. And this is pretty much what you'd expect in something like this.

**Dave Jones:** A pentode is quite common in these types of, you know, now vintage, you know, tube audio amps. And we've actually got some better data. We've actually got some graphs, characteristic graphs and stuff. So, beauty. Now let's take a quick look at the pentode,

**Dave Jones:** if you haven't seen it before, if you don't know your valve stuff. It's one of the more complex valves, due to the many various elements in here. It's more complicated than a triode. For example, you might have heard of that. Well, this is a pentode.

**Dave Jones:** Why pentode? Well, because it's got 5 different elements. 1, 2, 3, 4, 5. There you go. So let's take a look at them. Up the top here is the plate, which is also called the anode. Then we've got a couple of grids in here.

**Dave Jones:** We've actually got 3 grids. The next grid down is what's called the suppressor grid. And then the one below, one in the middle there, is the screen grid. And the one at the bottom here is the control grid, otherwise known as the gate.

**Dave Jones:** So compared to a JFET, which is essentially what valves really are, they're JFETs with pilot lights. The pilot light being the heater down here, of course. So you hook up typically a 6-volt heater here, and that just heats up the cathode, which emits all the electrons,

**Dave Jones:** and they flow through the various grids, if they're allowed to based on the grid voltages, to the plate up here, to the anode. And yes, this is electron current flow as opposed to conventional current flow, which you're probably more familiar with circuit design.

**Dave Jones:** But essentially, what it comes down to is just like a JFET, this is basically our gate, our input here. And then we've got our cathode and our anode here. And if we take a look at a little Davecat joint of a rudimentary pentode amplifier,

**Dave Jones:** then basically what we've got is the gate here that you saw before. The gate here is essentially, that's the control grid down here. So that's basically the input, or the gate of the JFET, so to speak. And then we've got our cathode resistor down here,

**Dave Jones:** which sets the bias and things like that. We've got some bypassing on there. And then typically the suppressor grid is going to be strapped down to the cathode down here. And then your screen grid here is typically connected up to your positive voltage rail here,

**Dave Jones:** which we'll call the HT rail, the high-tension rail, or you can call it whatever's more traditionally used with valve amps and things like that. Anyway, that's just got some bypassing on that. Won't go into details of why all that sort of jazz is done.

**Dave Jones:** But then we've got our anode resistor up here, which then just AC, is just AC coupled off to give our output. It doesn't have to be AC coupled, but you know, it likely is in a typical circuit. So that's basically, you know, hence why valves

**Dave Jones:** are effectively JFETs. They're transistors. They're, you know, it's just that they use old school. They're filled with vacuums, and they use a little heater element, but essentially they're transistors. Or more specifically, of course, field effect transistors because there's electric fields in here. Get it?

**Dave Jones:** That's what JFET stands for. Junction Field Effect Transistor. Eh, same thing. JFET with a pilot light. Now without having actually started on the reverse engineering of this board, i.e. tracing out every single trace and seeing where everything's hooked up, maybe we can just have a quick look of where

**Dave Jones:** the pentode is actually in this thing. Is it used as the input preamp? Because we've basically got our input here, stereo of course, hence we've got two op amps and two pentodes up here. There's got to be one for each channel. So, you know, here's our input, and here's our headphone output.

**Dave Jones:** So is the pentode used as the headphone output driver? Power, like, you know, power amplifier for the headphone? Or is it used as the preamp input? Well, my guess is it's typically used as a preamp input. So that's what I think we'll find here.

**Dave Jones:** And if you check it out, you'll notice that our input here, there's a trace going off. It goes over to our pot here. Okay, so it looks like our pot is like directly on our input. That's our volume control pot, so it's effectively attenuating the input here.

**Dave Jones:** And then, if you have a look here on the bottom, that goes over here to these two caps, so they're AC coupling that. And bingo, these go over to the pentode here. So it's obviously used as an input preamplifier. And of course the first thing you want to do with this

**Dave Jones:** is avoid Murphy and make sure you get the pinouts right. This is actually the bottom view, and the way I was able to figure that out, if you don't know like the internal structure and stuff like that physically, see it, look, they've got a not connected pin here,

**Dave Jones:** and it was fairly obvious to see which pin was not connected. So that's actually pin 1, it's a bottom view, and when you flip that over, there we go, that becomes pin 1, that becomes pin 1. Make sure you mark them, and you don't come a gutter.

**Dave Jones:** And sometimes it's just easier to desolder things to look under them, like you remove the chips here, you might be able to see some traces going under there, that's very handy, just otherwise, you know, you start to randomly, you know, buzzing out pins.

**Dave Jones:** And you can see the trace from there to there, which you wouldn't have seen necessarily unless you took that out and you didn't know there was a resistor under there, for example, hidden under the socket. So it's well worth taking out. And there's the blue LED of course, the wanky blue light.

**Dave Jones:** And it goes without saying, you only have to do it for one channel. Once you've traced out one channel here, the other channel's going to be identical, so just don't bother. And during the process, you end up with some sort of gibberish like this,

**Dave Jones:** which you have to redraw because it doesn't really make much sense. Hmm. So after a little bit of doodling, you end up with this. Here it is, here's the Davecad reverse engineering edition of this Hi-Fi headphone amplifier. Now you'll notice here that the screen grid is actually connected

**Dave Jones:** up to the plate up the top here. And what this does is it actually converts it from a pentode into a triode. So it's effectively working, you know, you might as well have put a triode in there. Now, you know, the pros and cons between a pentode and a triode

**Dave Jones:** in terms of a front-end preamplifier like this, but I believe that connecting it as a triode at least offers lower noise. But there's a whole bunch of other downsides as well, which I won't necessarily go into. One of the disadvantages of that, apparently,

**Dave Jones:** is that you're going to need a higher dry plate drive voltage up here. So, yeah, I, you know, meh. But doing this also apparently gives it the triode sound, in quote marks. Oh, God, let's not go there. Anyway, they quote this thing. The spec is like 0.005% distortion, okay, in the passband.

**Dave Jones:** And, you know, yeah, valves are supposed to do funky things sonically when you overdrive them and stuff like that. But who the hell's going to overdrive a headphone preamp front-end like this? It's just, I don't know, it just seems like a complete wank.

**Dave Jones:** Anyway, what else we've got here? The plus 6 volts power directly from the plug pack, it's going straight to the heater. And by the way, of course, we've only got one channel here. There's going to be an identical channel, because it's stereo for the other channel.

**Dave Jones:** So only need to draw one here. And then there's two DC, oh, anyway, so this, the filament heater voltage here, not surprising because it's a, you know, valves are 6 volt heater voltages. That's why they use a 6 volt plug pack. Didn't need any extra parts for that.

**Dave Jones:** Those two DC to DC converter switch modes that we saw in here, not that little 5 pin SOT23 and the SO8 there. One generates the negative voltage, which I think was this one down here. We've got three output caps, 100 mic, 16 volts,

**Dave Jones:** so there they are, three there. We've got three for the positive 12 volts, so this is the plus 12 volts switch mode. And these two will be the input filter caps for those, which I didn't draw. And sure enough, they do have the suppressor grid connected

**Dave Jones:** down to the cathode down here, which is, you know, fine and dandy, as we saw in the original DaveCAD one over here. But you'll notice that it is different. They've got it on the high side here, and they've taken the output signal from the cathode

**Dave Jones:** instead of from the plate. So if you compare that with a FET circuit or even a BJT circuit, what happens if you tap off what is effectively the source or the emitter here on a regular transistor circuit, which you might be more familiar with?

**Dave Jones:** Well, it's an emitter follower, a source follower, or in this case, a cathode follower. So basically, this thing is not a preamp as such, it's just a buffer. It just takes our high impedance input here and just buffers it, and that's it. And this did confuse me for a second,

**Dave Jones:** because I was kind of, I don't know, I had it in my head that there would be a preamp in here, but, oh, you know, of course, because this is a line input, it's not like it's a microphone input and it needs a microphone preamp.

**Dave Jones:** It's designed to take line-level signals and give you your headphone out, so you don't really need, well, you don't need a preamp on the preamplifier, you just need a buffer. That's pretty much it. In fact, they probably could have got away with the buffer

**Dave Jones:** and gone straight into the op-amps. As I said, wank factor. You know, tubes look cool, they light up, eh, what's not to like? And it's not even a complicated, you know, biased arrangement for a cathode follower, for a tube cathode follower. You can get, you know, much more complicated ones,

**Dave Jones:** so it's as simplistic as you can possibly get. It's almost as if, you know, yes, they have just thrown the tube in there for the sake of having a tube. And with the fairly generic tube they've got here, and the simplicity of the circuitry,

**Dave Jones:** the fact that they're using it as a buffer, it's like, like, why? It's just complete wank factor, that's all it is. It's gotta be. But anyway, after that, what they're doing, the NE5532, the AC coupling, that, and then we're basically, this looks a bit convoluted.

**Dave Jones:** You might not have seen this before, but, you know, let's just take the DC condition first, okay, when you're trying to analyze circuits, taking the DC condition to figure out what's going on, it's not a bad way to do it. So C12, a capacitor's gonna be open circuit, okay?

**Dave Jones:** So pretend they're not there, right? What have you got? Well, also pretend that this op-amp is not here, okay? Because it's just a voltage follower, okay? So it's effectively doing nothing, okay? So you can take all that out of the circuit and just connect that through to there.

**Dave Jones:** What have you got? You've got a 10k resistor. Don't worry about this capacitor here, it does nothing at DC, it's open. So you've got a unity gain amplifier there. The reason that they've put in the second op-amp here is for extra drive capability.

**Dave Jones:** So it's the same signal, exactly the same signal, but they're now buffering that with a second op-amp and then driving the output of this op-amp is driving through this 47 ohm resistor to the output and this one's driving through the 47 ohm resistor.

**Dave Jones:** They've got the effectively parallel drive there from the two op-amps. Not necessarily uncommon. But in the AC condition, of course, then these capacitors are going to matter. I didn't measure the values of this so I don't know the necessary roll-offs. But of course you will start then getting some gain at AC

**Dave Jones:** because this R12 down here is a very low value, 4 ohm 7. It's effectively, basically just shorts this out to ground. So, you know, depending on the frequency here you're going to start getting a bit of gain in this thing. So how flat the passband gain is in here,

**Dave Jones:** you know, presumably over the audio bandwidth, I don't know. You'd have to get the exact values and measure the performance of it. Now I actually posted a photo of this while I got the wrong data sheet. I posted it on Twitter. And some people said that apparently this 6J9J or slash E150F valve

**Dave Jones:** is, you know, just a pretty crap quality valve. It's just, you know, generic because it's popular because, well, there's lots of stock of it or whatever. And, well, yeah, I don't know either way. But, yeah, and then they haven't hooked it up as a pentode.

**Dave Jones:** They've hooked it up as a triode. So, yeah, go figure. The performance of this thing is probably meh. Now, just to prove that this is indeed a cathode follower, so the output is going to be the same as the input. Or actually, not quite.

**Dave Jones:** The output here is always going to be slightly less. The gain is always going to be slightly less than one that has to do with various parameters in the pentode itself. And it has to do with all sorts of stuff to do with valve amps.

**Dave Jones:** And I certainly won't go into it. But, you know, the amplification factor mu comes into it and the output impedance and, you know, everything else. And interestingly, they give you the characteristics when it's wired as a triode. Exactly as we've got here. Look, the G2 is connected to the anode.

**Dave Jones:** Exactly what we have here. So, this data sheet's really nice. They give you those values for this particular configuration. Because it is going to change as opposed to, here are the characteristics for just as it's used as a pentode. And the other thing here, I mean, as we said right back at the start,

**Dave Jones:** the nominal operating voltage of valves is, you know, very high. It's like hundreds of volts. And in this case, what this 1 means is it's its nominal anode supply operating voltage at 160 volts. Well, we've only got a plus minus 12 volt rail here.

**Dave Jones:** So that really changes the characteristics of this thing. But it may not hugely matter in this sort of low signal level application. Although I think they are doing the right thing here. Although I'm no expert on valve amps, that's to be certain. But the cathode resistor here is usually, a rule of thumb,

**Dave Jones:** it should be an order of magnitude lower than the load impedance, which we've got here at, well, you know, AC coupled 47k. So, you know, they're at least got the right order resistor value for the cathode resistor. Although that's probably as high as you'd want to go, you know.

**Dave Jones:** Ideally, probably the lower the better. So let's actually power this thing up. And I won't measure the performance of it, so don't get all excited. No, it's got 0.008 percent distortion instead of 0.005. No, not going to happen. But I'm just basically feeding in a signal from my function gen over here.

**Dave Jones:** I've just got half a volt peak-to-peak, 1 kilohertz sine wave, nothing fancy. So let's switch this puppy on and see what happens. The yellow trace is the input, so that's the control grid input. So right down here, I'm measuring the control grid input, that's the yellow waveform.

**Dave Jones:** And then we're measuring the cathode on channel 2. So that'll be the blue signal here. So let me switch this thing on and see what we get. And we expect, again, close to 1, no phase issues or anything like that, no inversion, it's a cathode follower.

**Dave Jones:** But we do expect the gain to be slightly less than 1. So it takes a while, it's heating up. It's heating up, takes a while for the heater. Come on, you can do it. You can do it, here we go. Whoa! Whee! And boom!

**Dave Jones:** There we go, look at that. That's pretty close. And if we go to channel 2, oops, I switched off channel 2. If we go to channel 2, that's the problem with having, you know, the single control handling all four channels. You never, you know, you've got to check which channel you're on before you hit the button.

**Dave Jones:** You can accidentally turn it off like that. It really is quite annoying. So yeah, I did it again, see? So you've got to make sure channel 2 is selected and then we can center that. And bam! Anyway, that's just a little side rant.

**Dave Jones:** So there we go, we're looking at, again, slightly less than 1. There we go, just a smidgen under. But, you know, that's pretty good. That's pretty good. That's following pretty well, as you'd expect for a cathode follower. And you'll notice if I actually switch this off, okay,

**Dave Jones:** and then I, you know, switch it back on after, you know, a few seconds, a few tens of seconds, then it's going to pretty much come back straight away because that cathode is still hot. In, well, literally hot. So it's, you know, so it doesn't need that 10 seconds or so to warm up,

**Dave Jones:** but you'll find that the data sheet will actually tell you the warm-up time. And sure enough, Bob's your uncle. Check it out, cathode heating time. Nominally 12 seconds, maximum 18 seconds. And curiously, you'll note they've actually specified a distortion here, which is interesting, but once again, I'm not hugely familiar with valve data sheets,

**Dave Jones:** so I'm not sure what particular configuration that actually refers to. But yeah, 1.6% for a 1K load for 100 millivolts RMS input. Hmm, December 1968. Jeez, we hadn't even landed on the moon then. So that's probably all this little one-hung low-brand hi-fi amp actually deserves, I think.

**Dave Jones:** But anyway, I think that was rather interesting to have a look at that thing. And yes, the tubes do actually do something. There you go, they're cathode followers. So I hope you learnt a little bit about tubes there if you haven't seen them before.

**Dave Jones:** And no doubt all of the tube aficionados will come out of the woodwork and rave on, and all the audio fools will come out, and they'll start raving on, and they'll have a big flame war, and it'll be hilarious. Love it. So there you go, I think this has gone for long enough.

**Dave Jones:** I've got 30 minutes worth of material. Ah, goodness, got to go edit this thing before I head off on holidays. Woo-hoo! In fact, when I'm posting this, I'm probably on a beach somewhere. Yes. Anyway, if you liked the video, please give it a big thumbs up.

**Dave Jones:** And if you want to discuss it, jump on over to the EEVblog forum, YouTube comments, all that sort of jazz, you know. Anyway, catch you next time. Wait! Hold on to your hat! I thought I would actually get a second opinion on this thing,

**Dave Jones:** and what better second opinion than one of the world's best audio designers, my mate Doug Ford from Doug Ford Analog Design, who you've no doubt seen on the blog before, and a former head designer at Rode Microphones, former head designer at Jans Audio,

**Dave Jones:** a couple of companies you might be familiar with. And yes, he's designed amplifiers, mic preamps, including tube preamps as well. So he's one of the best in the world. What's his opinion? Well, I asked him quickly, and he said basically, I'm happy to say he came to pretty much the same conclusion I did

**Dave Jones:** in that it's basically a wank, really. You know, there's no point having the tube in there. Yeah, it's going to, Doug says, most likely add some second and third harmonic distortion into there, but ultimately it would perform better, and it'll be cheaper and simpler

**Dave Jones:** if they just use the NE5532 op amp. So yeah, what a wank. Thanks, Dougie. And if you haven't seen Doug's microphone, multi-part microphone design video series, I'll link that in down below. It's fantastic, it's like five parts or something. We sat down for hours at the whiteboard.

**Dave Jones:** It's not just about microphone design, it's all sorts of design techniques and circuit topologies and all sorts of weird and wonderful things, so definitely check that out. Catch you next time. www.mooji.org
