---
video_id: LtoPHevexTM
title: EEVblog #483 - Microcontroller Voltage Inverter Tutorial
url: https://www.youtube.com/watch?v=LtoPHevexTM
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 27, "3": 35, "4": 47, "5": 61, "6": 76, "7": 96, "8": 110, "9": 129, "10": 149, "11": 163, "12": 177, "13": 193, "14": 216, "15": 230, "16": 241, "17": 256, "18": 268, "19": 279, "20": 292, "21": 305, "22": 326, "23": 346, "24": 357, "25": 385, "26": 397, "27": 408, "28": 424, "29": 435, "30": 455, "31": 465, "32": 481, "33": 504, "34": 518, "35": 536, "36": 547, "37": 556, "38": 570, "39": 585, "40": 606, "41": 616, "42": 629, "43": 641, "44": 653, "45": 665, "46": 676, "47": 689, "48": 702, "49": 710, "50": 725, "51": 742, "52": 755, "53": 769, "54": 784, "55": 795, "56": 809, "57": 819, "58": 829, "59": 849, "60": 865, "61": 876, "62": 892, "63": 906, "64": 920, "65": 931, "66": 945, "67": 957, "68": 973, "69": 990, "70": 1002, "71": 1018, "72": 1029, "73": 1037, "74": 1048, "75": 1062, "76": 1075, "77": 1092, "78": 1110, "79": 1134, "80": 1156, "81": 1168}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Couple of episodes back we looked at the microcontroller voltage doubler, otherwise known as the Dickson doubler, or the diode charge pump voltage doubler. And quite a few people asked about the inverter configuration of that.

**Dave Jones:** So, let's run through it. Should be pretty quick. If you haven't seen the previous video, watch that. It'll be linked down below. So, this is what we had previously with the Dickson doubler.

**Dave Jones:** We had our VCC voltage at might be say 5 V or 3.3 V or whatever your system voltage is. Um and then we feed in a square wave from our microcontroller.

**Dave Jones:** Doesn't have to be from a micro, could be from something else, but let's just say it's from a microcontroller. And based on the Dickson doubler here with the output filter, the output voltage is uh Vout equals two times VCC.

**Dave Jones:** So, you double your VCC voltage minus your diode losses, of course. But, we won't get into that yet. We're talking about the ideal case. Now, how do you get a voltage inverter?

**Dave Jones:** Well, it's very simple. Instead of doubling, we want to invert. So, what do we do? Hmm. We erase these diodes here, and we draw them the other way around.

**Dave Jones:** Like that. But, that's not all we have to do. We also have to get rid of VCC here. That's no longer VCC. That is ground. Like that. And bingo, we keep our um signal from our square wave from our microcontroller.

**Dave Jones:** There goes from zero to VCC. And in this case, our output voltage Vout is going to be not doubled, it's going to be minus VCC. Once again, ideal case assuming no diode losses.

**Dave Jones:** Bingo, that's our voltage inverter. That's all there is to it. Sorry, I don't think this one has a fancy name, but it can go under other names like uh charge pump, voltage inverter, diode voltage inverter, diode charge pump inverter, all sorts of combinations like that, but eh it's a voltage inverter.

**Dave Jones:** Great if you want to um if you have just a single uh supply can be operating from batteries or just from a uh single regulated uh main supply or something like that, and you want to generate a negative supply for an op-amp or maybe an offset voltage for a a voltage regulator to go down to zero volts, which we've talked about in the past or something like that.

**Dave Jones:** Very useful, but like all these uh diode charge pumps, they're pretty low power. You know, you're only going to get you know, a couple of milliamps out of this, sort of you know, tens of milliamps absolute top.

**Dave Jones:** So, really it's not for anything high power. And once again, you can also follow this with a negative voltage regulator if you need regulation. There is, however, one more thing that we have to invert, which I haven't shown here yet.

**Dave Jones:** Invert, no pun intended. Before, with our doubler, our capacitors were like that. If you used polarized capacitors, they'd be positive there and positive there. In this case, no, we have to reverse those.

**Dave Jones:** So, if you're using polarized capacitors, positive is here because our output voltage is negative. Got zero volts here. This is more negative than this. So, it doesn't make sense unless you actually think about it connecting the positive of the capacitor to ground, but because that's negative, of course, the capacitor is still has a positive voltage or the correct polarity across it.

**Dave Jones:** And likewise, this one here. So, how does this work? Well, you guessed it, very similar to how our previous Greinacher and Dickson doublers have worked. Instead of doubling and level shifting, we're actually inverting in this case.

**Dave Jones:** So, let's assume that our current is flowing through the diode like that. So, our diode is conducting. Once again, ideal diodes, no losses at all, 0 V voltage drop on that.

**Dave Jones:** And let's assume that we've got where our input waveform is at VCC and this capacitor has had time to charge up. Now, when this diode conducts, okay? What is it?

**Dave Jones:** It's an ideal diode, it's got no losses. This point here is going to equal this point here and here it's going to be ground. So, our reference point one, which I've shown in green, and this will be the green waveform here.

**Dave Jones:** By the way, that's the output filter, we're just ignoring that at the moment. We're only looking at signal number one here, the green waveform. I should probably draw that in there.

**Dave Jones:** Number one, there it is. Then our this point, number one, is 0 V there. But remember, I said our capacitor is charged up. And if you remember, capacitors can't change their voltage instantaneously.

**Dave Jones:** So, we've got What have we got? A charged capacitor here with 0 V here, 5 V here. What happens when this now switches down to 0 like this, we've now got 0 V here.

**Dave Jones:** What point does this become? Well, our diode is no longer is now going to be reversed biased. So, our current, well, it's going to be reversed biased. So, our current is trying to flow through it like that, but that this point, it can't flow through the diode because it's open.

**Dave Jones:** So, if we've got now 0 V here, but we've got plus 5 V, well, VCC, not 5 V, whatever your VCC voltage happens to be. So, what happens when this is now at 0 V and our capacitor is charged to positive here and negative here?

**Dave Jones:** Well, this point is a nice solid zero volts now because our driving circuit, our microcontroller, or whatever it is, it's got a reasonably low output impedance. It's going to be a nice solid zero volts here.

**Dave Jones:** So, this point has no choice. Now, because we've got um plus VCC across this capacitor, this is zero, that VCC voltage just doesn't suddenly vanish. What happens is our current tries to flow in this direction, our diode becomes reverse biased, and this point, i.e., when a diode's reverse biased, no current flows at all, and this point has no choice.

**Dave Jones:** But, if we've got zero volts here, but we've still got VCC on our capacitor, look, zero, then this point becomes minus. There's that negative. It becomes minus. It drops down like that to our minus VCC.

**Dave Jones:** And that's all there is to it. And just for completeness, we should actually draw this input waveform on here as well. So, let's call that number three, shall we?

**Dave Jones:** And what happens here? It's not zero. Remember, we our condition was starting out at VCC to charge that cap, so it's like that. So, remember we said when this point drops down to zero here, it inverts.

**Dave Jones:** There it is, it drops down to zero, and bang, it inverts, produces our inverted waveform output. And then, of course, we add on our output filter. Yes, it's just a simple uh diode filter.

**Dave Jones:** You're familiar with those from your linear power supply. But, yeah, the diode's backwards cuz we're dealing with negative supply voltages, but it works exactly the same. All it does is filter out this negative and produces our nice solid, if we've got no load, of course, a nice solid negative output voltage at minus VCC.

**Dave Jones:** Once again, assuming ideal diodes. Once you start putting a load on there, well, and in real diodes, as we're going to see when we build up the circuit, it's going to drop.

**Dave Jones:** But, that is the basic operation of a voltage inverter. Too easy. Once again, for the cost lousy cost of two diodes and two capacitors, you can generate a negative rail from any circuit that has a switching component like that.

**Dave Jones:** And of course, that switching component, as we said, can be a microcontroller, could be a 555 timer, or uh often they will do this as well. If you've got a DC a positive DC to DC converter, you can actually tap the switching signal off that and use this inverter circuit to generate a low current negative supply.

**Dave Jones:** And of course, you can get dedicated charge pump or capacitor charge pump chips to do this. You know, the classic 7460 voltage inverter, which also you can configure that the other way, as we've said before, works as a voltage doubler as well.

**Dave Jones:** But, that's a classic inverter. I think on the milliamps or something. The usual jelly bean ones like 10 odd milliamps uh max output current. Really low stuff because you really can't put much charge in these capacitors cuz that's what you're using you're doing.

**Dave Jones:** You're using the capacitor as an energy storage element. And well, a little tiny wimpy cap uh and to the breadboard we go. We've got exactly the same circuit we just saw on the whiteboard build up.

**Dave Jones:** We're going to use three channels of the scope to measure this thing. This will be channel one. This point will be channel two. This point the output will be channel three.

**Dave Jones:** I've got 0.47 microfarad caps here and here. And I've just got crappy 1N4148 diodes in there. So, we're going to get a bit of loss on those diodes and we won't be able to drive much load.

**Dave Jones:** But, we'll start out by viewing the waveforms with no load. And you'll see we'll get exactly what we saw on the whiteboard. And this time, just for fun, we'll use our GW Instek GDS-2304A VPO oscilloscope.

**Dave Jones:** Now, the yellow waveform here is channel one, the blue waveform is channel point two, and the purple waveform there is the output channel three. So, there's our input uh waveform there, 0 to 5 V square wave coming from my function generator.

**Dave Jones:** And point number two, as you can see, it inverts just like we saw on the whiteboard. And then, our output voltage, of course, we've got no load, it's just flat like that.

**Dave Jones:** So, we're getting Oh, by the way, they're all Sorry, that reference point there, they're all referenced to that point there. They're all DC-coupled, of course, and that's our reference ground point.

**Dave Jones:** So, 5 V up here, we're all at 2 V per division, so 2 4 5, and then this one drops down to -5. But you'll notice that if we go up, wrong control.

**Dave Jones:** When you change scopes like this, you'll notice that yeah, you can just see the diode clamping in there. You can see the diode loss in there. It's not precisely zero.

**Dave Jones:** So, the diode clamps it not to zero volts, but to, you know, plus well, you know, 0.6 V. It's actually lower than that because we got bugger all current, but it does clamp it to that diode loss.

**Dave Jones:** And likewise, you'll notice that the purple waveform there, even though they're all referenced precisely on the zero-volt line here, there's a diode loss in there from the blue waveform to the purple waveform.

**Dave Jones:** And once again, that will depend on the loss in your diode at a particular current. So, a particular output current. So, you would have to look up your diode characteristic curve to find out what that's going to be.

**Dave Jones:** Now, let's have a look what happens when we put on a lousy 1 meg load. Lousy, I mean it's really high, okay? Lousy amount of current. We're only talking if it stays at 5 if our output voltage stays at 5 volts, we're only talking 5 microamps.

**Dave Jones:** So we're drawing bugger all current. Here we go. This is with currently with no load and let me whack it on here. Get the alligator clip. Bang. There it is.

**Dave Jones:** You can visibly see that change. That changed quite significantly. And we'll just add a few little measurements in here to make our life easier. So let's have a look and see what I've done here.

**Dave Jones:** I really like the measurement capability of this GW Instek. Works quite well in both adding and removing measurements. And this little window down here shows all our measurements. Now what I'm able to do here is I'm actually able to add the uh peak at what the max value up here.

**Dave Jones:** So if we have a look, that is our maximum value of Well, you can choose your channel. In this case, channel one. So our yellow waveform there, I've got the Well, sorry.

**Dave Jones:** Not the not the max value. I've got the high value there, which doesn't include any overshoot or anything like that. So there you go. We're going to get a high volt there our high value there, 4.96 volts.

**Dave Jones:** As I said, this is coming direct from my function generator, so it's going to be pretty close to 5 volts. It's low impedance output from the function generator. So and well, it is very very close to 5 volts as you'd expect.

**Dave Jones:** And then what I'm able to add there is for channel two. Now we're on to the blue waveform here. I'm able to add the low value, so the bottom of the blue waveform down there.

**Dave Jones:** There we go, 4.48 volts. And then I'm also able to add the high value up here, which then can show our diode loss in that direction. And there it is, 320 mV.

**Dave Jones:** And as you can see, it's above 320 mV. Well, it's just jumped up to 400 above that reference point there. It's not going to be hugely accurate, of course.

**Dave Jones:** We've only got an 8-bit analog-to-digital digital converter in here. It depends on how you've input scaled the waveforms and stuff like that. Anyway, so that can show our diode loss there.

**Dave Jones:** Pretty neat. And then our Then I've got the mean value selected here of channel 3, which is our output waveform. And there's our output voltage of -4.2 V. Of course, we expect that to be 5 V, but it's not because of our accumulative diode losses there.

**Dave Jones:** We've got two diode losses in there. You remember this one, the low value. There it is. It's only -4.48, -4.5 V. So, we've already lost 0.5 V in our diode drop going negative like that.

**Dave Jones:** And then we lose another, in this case, about from -4.5 going to the output here. So, this point here is that blue waveform -4.5. So, we've lost our diode drop there.

**Dave Jones:** And then we lose our diode drop again on the output with -4.28. So, we've lost another 0.3 V across that diode there. Oh, by the way, this is for a 1 meg load still.

**Dave Jones:** And if we open our load, let's do that. Boom. There we go. There it did jump up a bit. Our low voltage here jumped up to -6.64. So, it dropped a 0.14 V there.

**Dave Jones:** And our output voltage jumped up a little bit to 4.4. But let's put the 1 meg load back, shall we? And bingo, you can see those values change. Let's go to say a 100k load.

**Dave Jones:** Okay? There we go. We're now getting an output voltage of minus 4 volts with a 100 K load and then we can let's drop that and be horrible and drop that down to 10 K.

**Dave Jones:** And whoa, now we start seeing some ripple effects. By the way, if you're wondering how I'm doing that, just using my decade resistance box here. Very handy to have build yourself a decade resistance box just for this purpose.

**Dave Jones:** So, we can get a good look at that get rid of the menu there. Get a good look at that ripple now, that output ripple. You can see the capacitor charging and then discharging on that purple waveform.

**Dave Jones:** So, there's that little charge there and then whoop discharge. And once again, this is going to depend on the value of your capacitors and your switching frequency. So, our switching frequency at the moment with this 10 K load is 1 kilohertz.

**Dave Jones:** So, as you can see, it's got the hardware frequency counter in there showing the 1 kilohertz, but we can change that. Of course, let's give that a go. Yeah, sorry, I've got to reach across my bench and let's change it to 10 kilohertz.

**Dave Jones:** Here we go. Boom. Let's expand that out a bit and you can see that we're getting no more ripple in there. The ripple's gone at 10 kilohertz. Exactly what you'd expect.

**Dave Jones:** Get a smoother response like that with less ripple by either increasing your frequency or increasing the value of your capacitor capacitors or both. Let's get really nasty and take that down to what I just shorted that out.

**Dave Jones:** There we go. And take it down to 1 K. Ooh, that's pretty horrible. Where's our trigger level? The reason it was jittery there is cuz our trigger level was right up the top here, right at the top of that waveform.

**Dave Jones:** So, we bring that down to the center, of course. Oh, you can just hit the 50% button on your scope. It whacks it in the middle and there we go.

**Dave Jones:** That's it 1K load and we're still getting out minus 2.76 volts there. So, yeah, your diode losses are starting to kill you now at down at 5 volts as you'd expect.

**Dave Jones:** I mean, you can get better than this by using Schottky diodes and we're only using 0.47 microfarad caps as well, you know, typical ones you might have in there or you might have a microfarad or something like a ceramic cap.

**Dave Jones:** Otherwise, you can get 10 microfarad typical in, you know, basic SMD design these days, but you know, sort of above that you're sort of going to go into the electrolytic territory.

**Dave Jones:** And if we short that load out, boom, look at that. We're even killing our input waveform. So, there you go. There's a diode voltage inverter you can build for practically zero cost cuz you've probably already got some diodes and some capacitors in your bill of materials anyway.

**Dave Jones:** So, it can be an absolute bargain if you just need to generate a a simple low current negative voltage. As I said, for an op-amp or for a negative regulator or for to get a regulator down to zero or for any other purpose that you need that split supply.

**Dave Jones:** And once again, you can add a linear regulator on the output here. If your input voltage is high enough, you could use a low dropout regulator. So, if you had a 5-volt supply, for example, then you could easily use even with at at low currents, even with crappy 1N4148 diodes and low values of capacitors in here, you could you get a fully regulated and clean 3.3 volt

**Dave Jones:** linear supply with a low dropout regulator. Not a problem. But using this particular load, which is 10K at the moment, there's our output voltage 3.64 volts. That's good enough to give us basically, you know, a couple hundred microamps um, output current if we use a low power, uh, low dropout voltage regulator at 3.3 volts.

**Dave Jones:** We'd get a nice clean supply with even these crappy parts. So, there you go. I hope you enjoyed that. If you want to discuss it, uh, jump on over to the EEVblog forum.

**Dave Jones:** The link, direct link to the, uh, individual video thread is down below. And as always, if you like Fundamentals Friday, catch you next time.
