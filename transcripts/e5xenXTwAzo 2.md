---
video_id: e5xenXTwAzo
title: EEVblog #616 - How Microphone Phantom Powering Works
url: https://www.youtube.com/watch?v=e5xenXTwAzo
source: youtube-asr
timestamps: {"0": 11, "1": 42, "2": 71, "3": 108, "4": 138, "5": 170, "6": 188, "7": 211, "8": 225, "9": 248, "10": 269, "11": 294, "12": 319, "13": 335, "14": 352, "15": 372, "16": 390, "17": 415, "18": 428, "19": 452, "20": 486, "21": 506, "22": 523, "23": 539, "24": 567, "25": 587, "26": 619, "27": 638, "28": 665, "29": 686, "30": 703, "31": 729, "32": 750, "33": 774, "34": 791, "35": 815, "36": 840, "37": 859, "38": 876, "39": 898, "40": 926, "41": 941, "42": 962, "43": 979, "44": 996, "45": 1016, "46": 1033, "47": 1051, "48": 1069, "49": 1090, "50": 1104, "51": 1129, "52": 1152, "53": 1174}
---

**Dave Jones:** I think that the next thing we'll have a look at is some real microphone designs. Some mine, some legacy designs. In order to do this, we'll probably want to have a look at phantom powering. Phantom powering of microphones has been used for 60 years or more, and it's a well-known technique for running power to a microphone down the same wires as you're putting the audio back up.

**Dave Jones:** Now, Let's do it. Yeah. Over on this side, we have the the mixer, or the microphone preamp, or whatever it is that's going to receive the microphone signal. Down over on this side, we have the microphone itself. And in between, we have a twisted pair.

**Dave Jones:** It's got to be twisted pair. Yes. With shield. Yep. With typically XLR connectors. Yes. Any brand preferences? Amphenol. Amphenol is the way to go. Yeah. Uh Okay. Why do we go to all of this effort of using twisted pair with screen instead of just plain coax, or even just twisted pair? Uh well, first of all, the screen keeps out electrostatic noise.

**Dave Jones:** Electrostatic noise is any noise which is capacitively coupled from, say, a a high voltage wire down here, a mains wire, into these conductors. So, the screen keeps out the electrostatic stuff. Mhm. The fact that they are balanced twisted pairs keeps out any of the noise that can be coupled by magnetic fields, 50 hertz transformers, adjacent transformers, uh current carrying conductors, that kind of thing.

**Dave Jones:** So, typically what we've got over here in its simplest format might be say a dynamic microphone, which is Yep. a coil. Uh and over here we've got effectively an instrumentation amplifier, whose gain we vary. And that might wrap around there as a again a Faraday shield and electrostatic screen, and that's grounded over there so that any capacitive current that's induced into there has somewhere to drain to.

**Dave Jones:** Mhm. That's a mistake that uh some of the Americans tend to make in their 110 volt gear. They kind of actually forget to connect that ground to real ground. As a result of which any mains leakage entering there makes the shell of the microphone effectively electrically hot.

**Dave Jones:** Got you. So, grab hold of a microphone, grab hold of a grounded microphone stand, and see the shaking. It's all part of the All right. Now, the whole purpose of an instrumentation amplifier is that it will respond to differential variations in the voltage between those two conductors.

**Dave Jones:** differential amp. Yep, but it won't respond to common mode changes. That means that we can induce quite a lot of common mode noise on that, and it's completely ignored at the output over there.

**Dave Jones:** That's all fine and good while you're using a dynamic mic. All falls over when you want to use a circuit over here that draws some power. Mhm. This is where we adopt phantom powering whereby in its original incarnation going back six, seven decades, however long, we would put a transformer in there.

**Dave Jones:** Mhm. Instead of having our solid-state differential amplifier, that would typically then go off to a valve stage, center tap that, connect that via resistor to a supply voltage. Over here, we'd have a transformer from which we could extract Yep.

**Dave Jones:** a voltage. So, between there and there, we've got a DC voltage that powers the circuitry, which is in turn driving the transformer. Okay, the DC path, because it's flowing through both halves of that transformer, gives a net zero magnetic uh or magnetization of the core.

**Dave Jones:** So, uh how do you put it? The The core in this transformer are not being stressed by any DC magnetization. Same thing applies over there. Mhm. The um How do you put it? The standard P48 phantom powering uses a 48-V supply, a 3.3-k resistor.

**Dave Jones:** Excuse me. Uh which limits your How do you put it? Your short-circuit current over here to something like about I think it's 14, 16 milliamps, something about there. Mostly though, you might be using about 8 or 10 milliamps consumption there.

**Dave Jones:** Mhm. If you're pulling 10 milliamps here, well, that causes 33-V drop across there. That 48-V drops to about uh what, 15 V? And so, you're getting 15 V at 10 milliamps there. Yep. That's enough to power a fair bit of analog circuitry.

**Dave Jones:** Absolutely. May plus maybe light up some idiot leads or something like that if you really want to. Uh a variant on that, if you don't like transformers, and let's face it these days who does because they're expensive and they're bandwidth limited, and the only kinds of people who really like transformers are the ones who also like tubes.

**Dave Jones:** Okay, let's take that away. Instead of using a center center tap transformer and a pair of 3K3 resistors, we'll feed each leg from something around about double that resistance.

**Dave Jones:** Yeah, if you want to round off let's call it 6K8 each from the 48 48 volt supply. Mhm. So far so good. We're still feeding them balanced. Okay, we've loaded the line by a total of well, what 13K, but hey, big deal because we've generally got something with fairly low source impedance down there.

**Dave Jones:** Capacitor couple off that into our differential amplifier. Beauty. That's what we do down that end. Okay, what do we do up here? Mhm.

**Dave Jones:** We can do a few things. The easiest one is to pick up from both of those some DC voltage. Okay, which we can then come over and we can do things like Zener regulate those with reference to that ground there, and then use that voltage there to run our circuitry.

**Dave Jones:** Which we then use to drive back into these fellows here. Mhm. Capacitively coupled. Now, if you've got a balanced source over here, Yeah. then beauty, you don't have to go any further. Now, Are you a differential driver? Yeah. And incidentally, an example of that might be a very simple FET circuit consisting of resistor, JFET, and resistor.

**Dave Jones:** Any voltage that you put in there appears there Mhm. and in anti-phase there. So, you can quite happily couple those straight over to there. Nice. Not so nice because uh the source impedance there is low. Yeah. The source impedance there is equal to that resistor there.

**Dave Jones:** So, we haven't maintained a balanced impedance and it makes the thing susceptible to noise. Got it. One of the cleverest circuits, I think, was come up with by the company Schoeps, microphone company. Right. S C H O E P S.

**Dave Jones:** I'm not certain of my facts here, but I think this is who came up with the circuit whereby you get one of those and uh Now, all this is going to be tricky to draw. This is going to be tricky to draw.

**Dave Jones:** Uh Okay, ground. Okay, over here, uh basically what we're doing is feeding into the emitter of a PNP transistor and into the emitter of a PNP transistor. Mhm. Uh Those collectors go into the thing that forms our positive supply, which is actually used there.

**Dave Jones:** Those uh bases there uh starting to look like a differential. Yeah. Yeah. Uh biased down to the collectors with high value resistors, typically about 100k, and we capacitor couple the signals onto those bases. Yep. Ah, that's an elegant circuit diagram.

**Dave Jones:** It's just a different It's like a differential front end on an op-amp. It is rather. Uh the only unusual features are the fact that Mhm. this Zener here Yep. has kind of locked the collector voltage, which in turn locks the base voltage at being Maybe you know, half a volt higher, depending on the bias currents flowing up here into those bases through those resistors. But it's it's very close. The emitters are only about a volt and a bit away from the collectors Yep.

**Dave Jones:** and fixes those at pretty much that voltage. Nice. Low output impedance because they're emitter followers. Exactly. These resistors act as the load resistors for those emitters. It's It's elegant. It's nice. I like it. Yeah. Uh and uh Is it still used?

**Dave Jones:** Ah, you know, half a Brazilian Chinese studio uh condenser microphones can't be wrong. They're all using this this kind of topology mostly. Uh and it doesn't have a lot of downsides. Uh one of the few downsides is that uh I'm just trying to think.

**Dave Jones:** If for some reason you get a short from one of those lines to ground, Yeah. uh ah yes, you've got enough uh capacitance there that and that's typically sitting at 15 volts, you've reverse avalanche those transistors by shorting that to ground.

**Dave Jones:** You can basically cure that by putting in a couple of uh uh reverse bias diodes there if you're sensible enough to do so and that fixes that problem. The other problem involves this phase splitter over the front here.

**Dave Jones:** Which on a good day from there to there you get a gain of about 0.7 or 0.8. It's not a particularly good follower. J fits they're a follower but they're not as solid as a bipolar. So typically from there to there it'll have a gain of about 0.7 and therefore from there to there it'll have a gain of about minus 0.7.

**Dave Jones:** Total gain from there to there about 1.4 1.5. Okay so far beautiful. All good. The only problem is okay you've got this very small source capacitance feeding that. I've run out of board space here.

**Dave Jones:** Okay that's being fed by Yeah maybe 50 puff. Depending on the fit that you've selected there it's going to have capacitance here and it's going to have capacitance there. Typical order of magnitude let's call that 50 puff and let's call that about say 10 puff.

**Dave Jones:** It's being a bit generous. No because these are used these are tiny tiny fits these are next level up in junction size etc. Reason because you're after fairly low noise. That might be 10 puff and that might be say about 30 puff.

**Dave Jones:** Okay now here's where Mr. Miller enters the scene. Okay from that point there to that point there we said we had a gain of minus 0.7. So the total voltage from there to there if you like is 1.7 times the input voltage, that 10 puff looks like a about a 17 puff Mhm.

**Dave Jones:** cap out of there. On the other hand, that 30 puff cap, well, we've got uh one unit of voltage there, 0.7 there, 0.3 across it, 0.3 * 30 is about nine puff. So, basically our 50 puff uh cap capsule is loaded by an additional 26 puff of capacitance.

**Dave Jones:** That's huge. Uh it's fairly large. Well, 26 puff against 50 puff, you're looking at probably 3 dB down, 3 dB attenuation compared to the open circuit voltage there. So, it's a bit of a downside. Uh the other downsides are limited linearity.

**Dave Jones:** Not so much due to that, but due to the fact that these can only swing so much. Remember I was saying that they're only Yeah, a a volt and a bit away from there. So, it can only swing down so much, and they can only swing down so much. Can swing up as far as you feel like, but Yeah.

**Dave Jones:** So, limited output headroom on that kind of circuit, but still immensely successful developed, I think, probably three, four decades ago, you know, back back in the dawn of semiconductors almost. Bloody good circuit. Excellent. Okay. But, let's improve that a little.

**Dave Jones:** Okay. We're still phantom powering over there. All right. Redo my terminations. is still a typical configuration used today. Absolutely. by everyone. Yep. Yep. Everything from your little cheap Mackie or Behringer Right. Yeah. through to your monsters. Right. And through to uh some of your multi-thousand dollar single channel studio preamps. They'll be doing that.

**Dave Jones:** Uh once you go beyond your couple of thousand dollar into your ten thousand dollar plus stuff, you're probably looking at a transformer again because that's the wanker market that you're dealing for. Yeah. Okay. I'm going to get shot down in flames for that.

**Dave Jones:** It's all right. I'm going to hell. We're all going Oh, now in that last circuit, this shunt circuit, uh I did point out the fact that the impedances there were both low Mhm. and balanced. Yes. Okay. So, we get all that benefit of noise rejection.

**Dave Jones:** Common mode noise common common mode noise rejection in the system. Did the transistor pair have to be matched over here? Uh not brilliantly, but yeah, 10 or 20% will do the job for you. It's mainly more about DC bias conditions than about anything else.

**Dave Jones:** Okay. Let's once again matched? No, it doesn't matter. Uh not hugely. It helps. All right. But it's not a decider. Let's once again extract power off those with a couple of resistors, whack that into a dirty great big electrolytic, etc.

**Dave Jones:** Absolutely. Whatever regulation you feel like. And again, we're coupling signal into those. The main criteria that we're after is to get the impedance on those two matched. Yep. Now, what happens if we've got, say, a lovely single-ended mic Hang on.

**Dave Jones:** Mhm? What about the mismatch on the caps? Uh Impedance on the caps? Yes, it does come into the scheme of things. Yeah. You have to make those caps large enough Yep. that uh uh over the frequency range of interest, and especially down to the magic 50 hertz mark, Mhm.

**Dave Jones:** that their contribution to the uh let let let's just say that that's the impedance of those two or yeah the the overall system. Uh Over here you might be looking at system impedances of well, say 6K8. Say. Mhm.

**Dave Jones:** You want that to be maintained down to well below 60 hertz before they decide to start Absolutely. going up at different break points. Yep. So, you want their You want You want their reactance to be low enough Mhm.

**Dave Jones:** at 50 hertz compared to the system reactance that a little mismatch there doesn't hurt and it only really takes effect down in the sub-hertz region. Nice and easy. So, you'd be typically looking at using electrolytics Yes. for that. Hence why I said cuz they're you know, they're going to be plus minus 20% or something horrible like plus 50.

**Dave Jones:** Yeah. Huh? Yeah. Huh? So, if they're going to be plus minus 50% just put them down at such a low frequency that plus minus 50 doesn't matter. Doesn't matter. Yep. So, you've come up with this circuit. You've got a lovely preamp there at single-ended.

**Dave Jones:** Mhm. What do you do? That's real easy. We've gotten as far as here. We've developed the world's brilliantest single-ended preamp. What the hell do we do? Okay, how about we I don't know. Well, why did you design it single-ended to begin with? Why didn't you do a diff amp Uh a diff amp Basically because diff amps are going to be intrinsically always noisier than a good single-ended.

**Dave Jones:** Oh. There's another video. Ah, yes. Let's couple that on onto there via a resistor so that we get a defined output impedance. This is typically got a near zero output impedance but just for the hell of it, we might give that yeah, maybe 50 ohms or 100 ohms or 200 ohms or something like that.

**Dave Jones:** And let's simply match that impedance Mhm. and connect it to ground. And And all of a sudden we've created a microphone which only uses a single-ended amplifier but still has completely balanced impedances so we get all the benefits of system noise reduction and the system immunity from induced noise.

**Dave Jones:** Oh, yes you do. Just with simplicity. Right. Because we don't need a balanced topology amplifier anymore. Got it. Let's have a look at a balanced topology amplifier. Let's do it.
