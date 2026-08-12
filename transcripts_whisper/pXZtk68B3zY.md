---
video_id: pXZtk68B3zY
title: EEVblog 1655 - How to Discharge Capacitors SAFELY using a Multimeter!
url: https://www.youtube.com/watch?v=pXZtk68B3zY
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 35, "3": 49, "4": 72, "5": 90, "6": 107, "7": 123, "8": 144, "9": 161, "10": 182, "11": 197, "12": 214, "13": 229, "14": 246, "15": 263, "16": 279, "17": 294, "18": 308, "19": 328, "20": 348, "21": 363, "22": 384, "23": 402, "24": 422, "25": 441, "26": 455, "27": 471, "28": 490, "29": 508, "30": 526, "31": 536}
---

**Dave Jones:** Hi, just a valuable multimeter tip you might not have been aware of that your multimeter's capable of. Let me show you. You know, if you like measuring a mains power supply like this, we've got, you know, a full wave bridge rectifier and we've got these main filter caps on there and we've got like a really high voltage on that, right?

**Dave Jones:** 400 volts DC. And these circuits can be quite dangerous because those capacitors can hold a charge. So let me switch the mains off here and you'll see that the voltage still remains because there's no, the designers have not put in like discharge resistors in there to discharge those capacitors.

**Dave Jones:** So it'll hold that charge for a long time. That can be very dangerous. There's a lot of energy stored in those capacitors. Now, of course, one way you can discharge this, if you've got a lead that has like a resistor in it, you can put it across it and you can discharge it that way.

**Dave Jones:** But some multimeters actually have a low Z or low impedance. Mode. And of course you can switch it over to that and that puts a 1K series resistor and a PTC resistor as well in series and that discharges that voltage. So we turn it back and bingo, it's the voltage is safely discharged.

**Dave Jones:** But what happens if your multimeter doesn't have a low impedance mode like this? How do you discharge it? Aha, there's a trick. So what I'll do is turn that voltage back on and then off again. And if we want to safely discharge our capacitors, but we don't have that low impedance mode,

**Dave Jones:** well, what we can do is just disconnect one of them like this. We can switch to the ohms range and just put it back on like that. Now, basically any decent multimeter will have a high voltage overload protection on the ohms range like this.

**Dave Jones:** And the ohms range actually contains an internal PTC similar to the low impedance mode. And it'll be discharging the cap. Now, believe it or not, that capacitor is now safely discharged. Let me switch it back to voltage mode there. It's only 2.3 volts.

**Dave Jones:** There you go. We've safely discharged that capacitor and we can now work on our circuit using the ohms mode. Beauty. Now, you notice that I actually disconnected the circuit before I switched over to the ohms range. And there's a reason for that is because while I like I've switched it off now and I can actually with this particular me,

**Dave Jones:** I can actually switch it over to the ohms range for a couple of seconds while it's connected like this and switch it back. But it's recommended that you don't do that. And once again, it's discharged here. But it's recommended that you don't do that because if you have a high voltage DC there and you actually switch it,

**Dave Jones:** you could potentially get some arcing across your switch contacts. And if you do that enough times, it could potentially degrade the switch contacts on your multimeter. But, you know, if you do it once or twice, it's probably OK. But no, correct practice for doing this is to actually disconnect your thing, switch to the ohms range and then reconnect it.

**Dave Jones:** So make sure you do actually follow that practice of disconnecting before you actually switch ranges like that. And so I'll test a couple of more meters and show you and I'll do it the not the best way by actually switching the contacts and show you that it still works.

**Dave Jones:** But just remember that. And obviously, if your multimeter doesn't survive like 240 volt mains or some like. High voltage DC like we have here on the ohms range, then we could probably argue that you probably shouldn't be using a meter when you're working on such circuits anyway.

**Dave Jones:** So, yeah, just be aware of that. So potentially, if you try this at home with a meter that's not capable of doing this, you could actually damage your meter. Just be aware of that. But any decent multimeter should have sufficient overload protection on the ohms range where this isn't a problem.

**Dave Jones:** We've got the EVBlog clamp meter here also doesn't have low ohms, but no worries. We can switch that over to ohms for a couple of seconds, switch it back. Beauty. Look at that. Discharged. And that'll work with practically any multimeter in this little Fluke 101 here, 290 volts.

**Dave Jones:** Just switch it over to ohms like that for a couple of seconds, switch it back. Bob's your uncle. Look at that, 12 volts. No worries, safely discharged. Of course, the voltage is going to come back a little bit there. That's due to dielectric absorption in the capacitors, but it's no longer dangerous.

**Dave Jones:** So how does that work? Well, let me show you just quickly here. I've got the 121 GW schematic. And if we zoom on the input connectors and the range switch here, we can see what's happening in both the low impedance mode and in that ohms mode as well.

**Dave Jones:** So we've got our positive input here, and then this is the switch position. So that's the off position, and this is the low impedance position. So the wiper comes down and basically shorts out those two, those two, those two, and those two there.

**Dave Jones:** And you can see that we've got the ohms mode all the way down here like this. So in low impedance mode, let's see what happens here. We've got our input coming in here. Then it goes through these two PTC resistors here, 1.5 K each, but they're not a fixed 1.5 K.

**Dave Jones:** They will increase in value. That's what PTC stands for, positive temperature coefficient. The resistance will increase in a positive direction when the temperature increases. So we go through here like this, and then it goes up here and goes to. Analog ground, and analog ground is just over here like this.

**Dave Jones:** So you've basically just put two 1.5 K PTC resistors across the input there. That's a perfect value for discharging capacitors. It's not too high that it causes a massive current flow, and it changes, and the resistance changes as they heat up. And that's why you can put 240 volts mains across here.

**Dave Jones:** And if you just had normal 1.5 K resistors, they'd burn up pretty quick. Use your ohms light. That's law, but because the resistance will rapidly increase as soon as the current flow and hence power dissipation inside these things gets too high and they heat up, then it sort

**Dave Jones:** of like self-regulates itself. They protect themselves. So it's basically the perfect way to discharge a capacitor bank like this. So what happens in ohms mode? Well, in ohms mode, when you switch it over to ohms, it goes through another PTC and then through a 1 K resistor, that's often a fusible resistor, and it goes down here and across

**Dave Jones:** here, and then whoop, up here, and you can see it goes up here and across here. Sorry, it's a little bit complicated, but look, and we have a TVS here, which is for peak overload protection to protect against, you know, like lightning surges and ESD discharges

**Dave Jones:** and stuff like that. But that's not what's going to save us here. What's going to save us are these two transistor clamps here. Now I've done a whole video on this. These act as a low voltage Zener. So a back-to-back Zener diode. So it doesn't matter which polarity you have, these will conduct and then save whatever

**Dave Jones:** circuitry is then connected off to here. So I'll link in that video if you haven't seen it, Zener clamping circuit, very clever. So if you didn't have the PTC over here like this, then yeah, you might be in trouble if you just had these clamping Zener's over here, just effectively being the low impedance.

**Dave Jones:** But because we've got the PTC in there, it's protected. It works like it is in low impedance or low Z mode. So effectively your ohms range works like a low impedance mode. Beauty! And if we go to the classic Fluke 87 multimeter schematic, same thing happens.

**Dave Jones:** Here's our positive input here. We've got a 1K fusible resistor. They actually specify it as fusible. There's the plus T. That means a PTC, positive temperature coefficient. And then there, trust me, there is a dot there. And in ohms mode, it goes through here.

**Dave Jones:** Aha! There's our Zener clamping circuit yet again. Going down to ground. Beauty! So that is going to clamp this point here, which then goes through to all the sensitive stuff over here, which goes into your main chip. So it's fully protected. It's going to clamp at that Zener voltage, which is only, you know, like 8 volts, 10

**Dave Jones:** volts, something like that. And the Fluke 17B multimeter, same thing. We've got our positive volts ohms input here. We've got a thermistor here. That's why it's RT1 and not R1. And then we've got another thermistor here. Optional 1K resistor in stall either, but not both.

**Dave Jones:** And then, bingo, if you're in ohms mode, what have you got? You've got a clamping circuit, slightly different, but basically doing exactly the same thing. Clamps it down at a low voltage, and then your PTC does the rest, handles it. And that's why you can use ohms mode to safely discharge your capacitor bank without damaging

**Dave Jones:** your multimeter, at least if you've got a half-decent multimeter. No worries. So I hope you found that video useful. If you did, please give it a big thumbs up. Let me know which ways you can discuss down below in the comments or over on the EEVblog

**Dave Jones:** forum. And you can get my EEVblog branded meters over on eevblog.store. Catch you next time.
