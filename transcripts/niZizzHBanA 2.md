---
video_id: niZizzHBanA
title: EEVblog #629 - How To Design a Microphone Preamplifier
url: https://www.youtube.com/watch?v=niZizzHBanA
source: youtube-asr
timestamps: {"0": 11, "1": 39, "2": 63, "3": 88, "4": 104, "5": 126, "6": 143, "7": 164, "8": 180, "9": 207, "10": 229, "11": 251, "12": 278, "13": 302, "14": 321, "15": 339, "16": 355, "17": 377, "18": 399, "19": 418, "20": 434, "21": 455, "22": 481, "23": 502, "24": 515, "25": 535, "26": 551, "27": 568, "28": 581, "29": 603, "30": 626, "31": 639, "32": 661, "33": 677, "34": 702, "35": 731, "36": 750, "37": 775, "38": 790, "39": 810, "40": 821, "41": 832, "42": 858, "43": 885, "44": 906, "45": 923, "46": 955, "47": 982, "48": 995, "49": 1018, "50": 1039, "51": 1058, "52": 1079, "53": 1096, "54": 1120, "55": 1140, "56": 1160, "57": 1182, "58": 1205, "59": 1227, "60": 1252, "61": 1273, "62": 1293, "63": 1317, "64": 1329, "65": 1352, "66": 1383, "67": 1411, "68": 1433, "69": 1454, "70": 1472, "71": 1489, "72": 1520, "73": 1540, "74": 1561, "75": 1579, "76": 1599, "77": 1621, "78": 1642, "79": 1657, "80": 1673, "81": 1680, "82": 1698, "83": 1721, "84": 1747, "85": 1770, "86": 1789, "87": 1805, "88": 1823}
---

**Dave Jones:** When we were discussing previously the typical valve topology or tube topology for a uh condenser mic, we're looking at uh bias supply, you know, plus 60 volts or whatever, gain down to the This is the microphone capsule. And capacitor coupling off that into something a bit like that.

**Dave Jones:** Okay, we've got two high-value resistors, two very high-value and relatively expensive resistors, Yeah. and a coupling cap that uh it's not allowed to be leaky. Sure. So, what type we talking about? Uh usually uh polypropylene, uh polystyrene, poly put the kettle on.

**Dave Jones:** And what values did you need in there? A nanofarad or so. Oh, okay. Yep, that's doable in those technologies. Basically, when you've got uh 50 puff and a nanofarad, then that doesn't represent much series loss. Sure. When we went to the FET-based circuits, I wanted to try and get rid of one or the other of those resistors.

**Dave Jones:** Mhm. I had a cunning plan. Ooh, do tell. Well, yeah. Which was this. First of all, get your JFET.

**Dave Jones:** You'll probably want to fix its bias with, you guessed it, a high-value resistor. Yep, higher the better. Yeah, somewhere. Why don't we simply connect that to our microphone? And a high voltage supply. Yes. Let's face it, the same the same.

**Dave Jones:** Yeah. So, let's say that's Let's say that's sitting at I don't know, 60 volts. Well, actually I think we took that up to 90 volts. Just for the hell of it. And let's say that's sitting here at 10 volts.

**Dave Jones:** Which And there's a good reason for that sitting at 10 volts. We get 80 volts across there. Yep. We get one resistor only. As long as we don't have any leakage in the microphone capsule, the gate is sitting at 10 volts. And there's we've gotten rid of an expensive resistor, a surplus capacitor.

**Dave Jones:** Yep. And in principle, what we should have with a typical depletion mode JFET, if that's at 10 volts, that might be at say 10.2 volts or 10.5 volts or whatever.

**Dave Jones:** Let's use that as the front part of a closed-loop unity gain voltage follower. Okay, let's do. So, what we might do here is put a resistor there. We'll put a PNP transistor there as a voltage gain stage. Um We'll I'll come back to that in a second. We'll load that with a current source.

**Dave Jones:** Yep. Okay. If What What typically would you have made the current source out of? Couple of A resistor. A resistor. Fancy fancy. A- Actually, you can go anywhere from a resistor to a proper current source. And in various models, I used various different topologies.

**Dave Jones:** Now, in actual fact, I was using that 15 volts there, about uh 7 volts there. That was sitting at about uh 7.5 volts. I that was slightly higher than that. Yep. Uh then what we did there was This is This is going to be look disturbingly like a power amplifier.

**Dave Jones:** Let's put a basically a bias voltage in the middle there and take it off to a It is. Yeah. Yeah, it is. It's a power amplifier. Okay, we've got a voltage amplification stage there. We've got a bias uh In- Incidentally, red LEDs are good for that.

**Dave Jones:** Yes, yes, they are. Yep. Although, LEDs can be noisy. Uh I never came across a noisy one. Okay. All right. Uh certainly the just you know, red LEDs are about uh 1.5, 1.7 volts, uh which allowed, you know, well, 0.6, 0.6 and a few put into a voltage across there. So, that's our output and what do we do with that?

**Dave Jones:** Bang, straight on there. Yep. That's to minimize the crossover distortion, of course. the bias is to minimize the crossover distortion. Uh now, let's just say we've got, say, an 1 mA current source down there or maybe even a 6K8 resistor.

**Dave Jones:** The value of resistance there will determine the FET current. Basically, let's just say that we have a 1K resistor there. That transistor is going to require about 0.6 volts to turn it on. So, guess what? We're going to get about 0.6 You will.

**Dave Jones:** mAs down there. If that tries to drive If that tries to pull more than 6 mAs, it's going to increase the voltage there. That'll pull that lot up. It'll bring that point up. It'll shut that device off, relatively speaking.

**Dave Jones:** So, that's that's the resistor which sets the operating current for the FET. It's operating voltage is set by the fact that that voltage there is 0.6 of a volt less than the supply, and that voltage there is going to be slightly more than the bias voltage. And it's the bias voltage here which sets the output voltage.

**Dave Jones:** All the quiescent conditions explained, and boom, it's unity gain. And because it's unity gain closed loop, its linearity is exceptional. And that's what you want in a good mic. Uh-huh. Yep. Now, the other thing is I was discussing previously the role of capacitances, and I said that we were typically about 10 puff there.

**Dave Jones:** About 30 puff there. Yep. That 10 puff there is it bootstrapped? Not on your nelly, because doesn't matter how big a signal we pump there, the the signal voltage there is naff all. So, our capsule is loaded just by that 10 puff.

**Dave Jones:** Right. How about this 30 puff cap down here? It's a follower. There is no voltage across that cap. It's completely bootstrapped out. Yep. So, our 50 puff capsule is really only seeing a bit of stray wiring and 10 puff.

**Dave Jones:** Clever. So, relatively lower attenuation. Very nice. Now, let's talk about that NT3 microphone. It's It was just a little bit different. Because the So, what was this Was this used in? Yes, that topology is used in, for example, the uh the Rode NT1000.

**Dave Jones:** Okay. Or or almost as shown. Right. Yeah, bugger all difference. Uh the FET the JFET that we using in the NT3, uh rumor has it was originally designed back in the mid to late '90s for use by the CIA in some of their little bug microphones.

**Dave Jones:** Yeah. And uh was uh manufactured by Siliconix. Okay. Uh I wish I could remember the part number because it's cute little beastie consisting of the JFET Mhm. and a pair of back-to-back diodes. Okay. Now, what do you do with them?

**Dave Jones:** Well, the first time I tried using that FET, I had simply used it in the normal configuration where you ground that and you ground that and you Yeah. pull current out the top. Those are horribly non-linear devices. As you'd expect.

**Dave Jones:** Yeah. More than about 10 or 20 millivolts of signal there and it was basically non-linear as Okay. Why would you use those in the first place? Because they actually act very nicely as a replacement for a really high value resistor.

**Dave Jones:** Aha, of course. Yes. As long as you can keep the voltage across those low, Yep. they act like a high value resistor. Got it. How the hell do I use those? Well, the first thing I did, uh let's just whack a bit of resistance in there.

**Dave Jones:** And yeah, maybe a meg or something like that. And connect that to our Okay, so these came out as a separate pin. Yes. It was a four-pin device. Ah, right. Okay. There, there, there, and of course there. Nice.

**Dave Jones:** One of the selling features of them was really low in input capacitance incidentally. Got it. And I figured I'd use these because again, it gets rid of what was at that time a relatively expensive, very high value resistor.

**Dave Jones:** Yep. But how to use it? Bootstrap the buggers. One meg resistor to our bias supply and then connect that to a capacitor which goes, you guessed it, to Yep. the well, basically the the source connection. Yes. So that It It vanishes.

**Dave Jones:** Yeah. Yeah. So that was one of the really cool things. Maybe somebody on the blog cost? Hm? Or to save cost? Not only to save cost, but it was convenient little package. Right. And if we pull this out, you'll be able to see it living up the front just there.

**Dave Jones:** Yep. That that little five-pin sock 23. Yeah. Right. And look, maybe somebody can do a bit of research and tell us all what the hell the part number on that is because I can't find it anymore. It doesn't appear on data sheets anywhere.

**Dave Jones:** Uh Bummer. But that was an interesting little circuit tweak that saved us a resistor. The other one was uh And these aren't point oh triple oh one cent resistors. Yeah, they're like even in volume, we might be looking at 30 cents or thereabouts cost.

**Dave Jones:** Instead of, yeah, point double oh five cent. Yep. The So saving, yeah, pulling 30 cents out of the product cost is it's an exercise worth while doing. Absolutely. Particularly if you can do it at the expense of, yeah, a point double oh five cent resistor and maybe a one cent capacitor.

**Dave Jones:** Yeah. Oh, let's close the loop. Yes. Okay. The initial prototypes of this microphone, well, they went out for beta testing. Comments came back, they're a bit lacklustre up in the top end. Right. Uh they didn't have enough kind of pizzazz, not enough excitement. Uh And basically Not enough distortion.

**Dave Jones:** Well, uh the frequency response flat. It was The frequency response looked a little bit like that where those ripples were up in the kind of the 15 kHz plus region. aren't big enough. Exactly. You got to have big ripples to Yeah, well, big ripples. And basically what they wanted was a bit of extra excitement up here, you know, a little bit more at about 6 kHz or about added to the data sheet extra excitement.

**Dave Jones:** Yes. Well, now we had to model with excitement. We had to add some more some more bang bang. So, we've got the perfect opportunity here to do a little bit of finishing because it is a closed loop Yep.

**Dave Jones:** circuit. So, I kind of scratched my head and walked around in circles for a while and opted to put in a bridged T circuit right. Yes. in the feedback network. Now, bridged T network has a response that looks like that. It's got a rather minor notch.

**Dave Jones:** Which when you use it in a feedback network gives you you guessed it Yep. Ooh, little peak. So, these microphones have that little bridged T circuit in them just to add a little bit of woohoo to the sound.

**Dave Jones:** How did you choose the frequency you going to put that at? Uh basically the knowledge that they wanted a little bit more woohoo. And you know, the sales guys who were there at the time were kind of canny enough to realize where it needed that little bit more little bit more pizzazz.

**Dave Jones:** And we did a couple of different cut and tries to find out first of all how much and secondly at what frequency. And yeah, it was around about the 6 kHz mark that they wanted the extra squirt. Okay.

**Dave Jones:** And I think about 4 dB thereabouts was So, am I just a bloody amateur because I if I'm looking at the microphone data sheet, I want to see this flat. I'm going to buy the one that's flat as a tack.

**Dave Jones:** But I'm an amateur, clearly. Yeah. No, don't know. If you're after a microphone as a measuring instrument course. Absolutely. If you're after a microphone to measure sorry to record something like an orchestra or something whose sound was absolutely defined and known and you didn't want to muck about with it, pick something flat.

**Dave Jones:** Yep. That's not what happens in studios. Studios are creative environments. You're trying to create the sound that winds up on tape, which is why you have this cupboard or room full of different microphones with different wobbles and different microstructures and different directional characteristics and different amounts of distortion because you want to choose a creative tool that actually kind of sounds like what you really want it to sound like.

**Dave Jones:** Are people still doing that in mics these days? Oh, hell yeah. Yeah? They're not they're not doing it in the Uh other end? No, because look everybody knows it's cheating to do it in your digital audio workstation. Yeah, if you can't do it with a room full of $10,000 vintage microphones, what's the point?

**Dave Jones:** Exactly. Gold plated. So, anyway, that that might be an interesting little trick for anybody who's playing with these. Oh, there's one vital component. What are we missing? missed out of this circuit. It's a closed loop system, is it not?

**Dave Jones:** It is. It needs dominant pole compensation. Oh. There you go. And without that, trust me, it oscillates like a banshee. Yep. How did you pick that? How did you How did you pick that? Uh actually Basically stick it in and it works or did you Uh there there there is actually a perfectly viable technique that I use which is uh uh from there onto any closed-loop system that you would design?

**Dave Jones:** Pretty much, yeah. Yeah. Okay. Uh connect it to a sig genny Yep. square wave. Okay. Have a look at the output and uh find out whether it's going Yep. or Yep. That's it. Yeah. Oh, bear in mind when you want it to optimize.

**Dave Jones:** Yeah. Ideally, you're after something a bit like that. Just taper it, yeah. Just rounds off the You you want to get it up to the point of maybe a a small amount of overshoot. Yeah. In which case you know that yeah, it's pretty good. It's pretty stable.

**Dave Jones:** Right. Uh that is not on. No. Yeah, because Yep. production variations, it's likely to turn into an an oscillator. That. Yes. Yeah. Uh Trap for young players though, there's two kinds of stability issue that you need to worry about in any of these power amp circuits. Uh one is the loop stability Yep.

**Dave Jones:** as governed by your dominant pole compensation or you can go for split pole kind of either way like that. different ways. But the other one involves the simple fact that emitter followers, voltage followers Mhm. uh renowned for oscillating by themselves as a form of negative impedance oscillator whenever you hit them with a capacitive load.

**Dave Jones:** A big capacitive load, yep. And when you get that happening in, for example, an audio power amplifier, a big one, uh you can first of all, start isolating Yeah, you can. inputs with ferrite beads to raise the source impedance at high frequencies.

**Dave Jones:** Uh you can add emitter degeneration You can do that with ferrite beads? They're up in the hundreds of megahertz. Oh, yeah. Look, I've had uh 4 megahertz bandwidth transistors sitting there just one Yep. 4 megahertz bandwidth output transistor sitting there on just mounted on its own on a chunk of heatsink.

**Dave Jones:** Yeah. And just with uh I think it was two resistors and a capacitive load, Mhm. I turned that into about a 30 or 35 megahertz oscillator. And I could tune it by getting my source wire and just running it up and down the the length of heatsink.

**Dave Jones:** Nice. Yeah. So, yeah, nasty. And that's just all about parasitic inductances and stuff like that. Any parasitic inductance up in here is to be avoided. Mhm. Whereas any parasitic inductance here is to be appreciated. Yes. Uh sometimes even some uh local degeneration Yeah, you can.

**Dave Jones:** there Hey, it depends. But, there are these two forms of stability. One involves the loop, the other involves just the output stage acting as a follower with stray inductance here and low impedance at the bases and it forms a I think a Colpitts or a Hartley oscillator or something like that once you hit it with some extra capacitance over there.

**Dave Jones:** Yep. Okay, so that's the uh the basics of a lot of the uh microphones currently being manufactured by Rode. Rode. Yeah. Terrific. Now, let's go one step further. Okay. We got enough time? Yep.

**Dave Jones:** This is really cool. Okay. So, we've pretty much got the same circuit that we had before. Yep. Uh with the bias network of your choice in the output stage and yada yada yada. Uh what we're actually going to do here is something dirty, dirty, dirty.

**Dave Jones:** Dirty. Like the sound of that. Let's ground that. Let's take this down here to minus 120 V. Yep. Uh okay. Um You haven't changed anything so far. No. We've put in some uh well, get rid of those because we don't need them. Uh we do have it however need that one.

**Dave Jones:** Yeah. Um do you know of any high voltage FETs that'll go in there that'll run at 120 V? No. I do. Not offhand. I do. They've got pilot lights inside them. There we go. Oh, you're Oh, yes. You're a tube fan.

**Dave Jones:** Well, this was for the NT1000. Right. And yeah, sorry people, it's another uh Heretic's microphone. It's got a tube front end, but it's riddled with bipolar. And there's a very sensible reason why you did this. Oh, yeah. Uh first of all, um okay, that that goes off to the output through the capacitive coupling, yada yada yada.

**Dave Jones:** Okay, I want something that gives uh this is a non-inverting, of course. Of course. And I wanted this particular circuit to um uh react such that how'd you put it? Positive positive pressure into the microphone gave a positive output.

**Dave Jones:** Right. Best way of doing that was Was there any absolute need for that? Uh a distinct preference. Right. Okay. Let's put the microphone there. Yep. And bias that through our 5 gig resistor to a voltage of about minus 60.

**Dave Jones:** Mhm. Okay, guess what? Any positive pressure input there, okay, moves the plates closer together, voltage goes up, polarity beautiful. Okay, why these inverted voltages? Why ground up there and minus 60 minus 120. First of all, it keeps the uh metal parts of the microphone Mhm.

**Dave Jones:** substantially at zero volts. Okay. Uh just quietly, there is one other microphone that we did where that's actually sitting at plus 60 and if you operate it with the cover off and put your lips on it, you you will get a belt.

**Dave Jones:** Mind you, who'd be stupid enough to run it with the cover off? I don't know. Right. This This is This circuit was absolutely fearsome in its dynamic range. Right. First of all, with those supplies, we could get an output voltage there of about 35 volts Mhm.

**Dave Jones:** RMS. Nice. Not bad for a microphone preamplifier. Pretty good. 35 volts RMS is That's RMS, that's not peak. Probably about two orders of magnitude higher than most line inputs will cope with. That had implications for how do you put it? The maximum SPL that you could apply to the microphone capsule. In fact, you can put I think it was about 150 something dB SPL on the mic capsule.

**Dave Jones:** So, you're physically limited by the mic capsule, not the circuit. Yeah. Yeah. Yeah. Secondly, uh if you pick the right operating current, again, the operating current is determined by that resistor there. Pick the right operating current for that valve, and the residual noise of the system corresponded to a How do you put it on a a microphone? A noise at the microphone of about 12 dB.

**Dave Jones:** You can express the system noise in terms of how much acoustic noise does that correspond to. So, we had 12 dB SPL equivalent noise. We had, I think it was about 100 and let's call it 155 dB SPL at And this wasn't at clipping. This was at like 1% distortion.

**Dave Jones:** Wow. Okay. Uh subtract that from that, and you get a dynamic range of what's that? 143 dB dynamic range out of the one circuit. Now, there's not too many semiconductor circuits that'll do that. And here's a tube circuit with that kind of dynamic range.

**Dave Jones:** Awesome. Hey. And one of the tests I did now you have to do this. You have to test it. I simply hung a set of headphones off off the output there, and it worked bizarrely well. It was loud in headphones.

**Dave Jones:** Right. Uh incidentally, one uh because I wanted this thing to be capable of feeding 600 ohm loads, uh it's actually got two sets of paralleled output devices, so that it can actually drive a 600 ohm load at those kinds of levels.

**Dave Jones:** So, From the mic. From the mic. That's disgusting. Did Did anyone actually use it? Did anyone actually use it for this or is it just design overkill? It's pure design overkill. It might be pure onanism on my part, but oh, incidentally, that noise figure there that was based on optimizing the operating voltage and current so that it would suit a very wide cross-section of tubes.

**Dave Jones:** Right. Okay. I could have dropped that noise probably about four or five dB if I'd tuned the operating current for the valves. But if you do that, you make the thing kind of unproducible but yeah, getting that down to about we could get that down to about eight dB SPL.

**Dave Jones:** Wow. The best commercial semiconductor mics are probably the Rode NT1-A, which is about three and a half or four dB noise. Um the Neumann TLM 103, I think it is, which sits around about five and a half or six dB.

**Dave Jones:** That kind of order of magnitude. We could get this tube thing down to pretty close to the best that semiconductors had to offer. With that ridiculous that kind of output level. That's ridiculous. How did you get these in production though?

**Dave Jones:** Uh How now, who did you get them from? How can you still get them? Nobody's making tubes. Yes, they are. Yeah. Svetlana people like that. There's a few companies making tubes. And there's two different types. You can get the new old stock. It's probably been manufactured back in 1970 and just getting in a warehouse.

**Dave Jones:** And then there's the actual new tubes. And I think what Rode are doing, they're they're using new tubes, but they age them quite viciously. They operate them at uh, quite high voltages and currents to burn them in so that when they actually put them in a mic, they're going to be stable for a very long time.

**Dave Jones:** Got it. It's something that they do quite well. How much power were you pissing away heating this thing up? Uh, I slightly run under-running the filament. Uh, they're normally a 6.3 V filament. I think I was running them at about 5.5 V or thereabouts, just slightly under. If you're run too far under, you start stripping the thorium or whatever off the cathode.

**Dave Jones:** Right, yeah, yeah. Um, and can't remember, about 300 500 milliamps. Right. They don't draw huge amounts of power. Right. Yeah, they don't. But how are you getting this from the phantom? Oh, not from not from phantom. No. Not not not this valve. No.

**Dave Jones:** particular valve. Specific power supply. Right, yeah, right. And even now, even the power supply had some quirks to it.

**Dave Jones:** The topology for the power supply, just very quickly we'll finish up on this, I think.

**Dave Jones:** Okay, again, negative power supply. Yep. So, ground up the top and a negative unregulated voltage down here. The first thing we created was a current source, or actually a current sink. Okay, so, over here we've got our main reservoir caps off the bridge rectifier.

**Dave Jones:** Right. A current sink consisting of basically an N-channel FET. Yep. And connected across it, a amplified Zener. Again, consisting of an N-channel FET. So, what do we have out here? First of all, that's low impedance, that's high impedance. Any ripple there is severely attenuated there.

**Dave Jones:** Got it. We had, yeah, maybe hundreds of millivolts ripple there. We were lucky if we get tens of microvolts ripple over here. And of course you can picture that this topology probably looked a little bit like uh Actually, sorry.

**Dave Jones:** uh uh amplified zener There you go. And this one of course consisted of Oh, I might as well draw him down here. Uh one of them.

**Dave Jones:** I'm sure you've seen that one before. And a bias resistor up to who cares. Yeah? Too easy. And that creates a uh current source Mhm. amplified zener Yep. nice little uh supply which is intrinsically short circuit protected Yep.

**Dave Jones:** because that simply soaks up any short circuit current and has devastatingly low noise out there. Fantastic. So So win all around. One of you out there somewhere might have called to use that kind of topology one day. There you go.

**Dave Jones:** I hope. And all Rode mics are still designed and built this way? Yeah. Fantastic. To the best of my knowledge. Mind you, it's what uh 13, 14 years since I've been there, but uh to the best of my knowledge any of their high-end studio stuff Yep.

**Dave Jones:** still uses these techniques. Beautiful. Thanks, Dave. Shh.
