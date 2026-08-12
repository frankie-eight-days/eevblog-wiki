---
video_id: OXsu29K_Ap4
title: EEVblog #392 - 555 LED PWM Hack
url: https://www.youtube.com/watch?v=OXsu29K_Ap4
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 30, "3": 48, "4": 66, "5": 81, "6": 98, "7": 112, "8": 128, "9": 146, "10": 158, "11": 177, "12": 191, "13": 216, "14": 234, "15": 252, "16": 272, "17": 289, "18": 306, "19": 320, "20": 340, "21": 357, "22": 380, "23": 402, "24": 417, "25": 430, "26": 448, "27": 464, "28": 480, "29": 494, "30": 508, "31": 524, "32": 537, "33": 556, "34": 572, "35": 588, "36": 606, "37": 624, "38": 640, "39": 655, "40": 669, "41": 683, "42": 697, "43": 711, "44": 724, "45": 741, "46": 763, "47": 780, "48": 795, "49": 807, "50": 821, "51": 839, "52": 855, "53": 871, "54": 885, "55": 901, "56": 917, "57": 936, "58": 957, "59": 986, "60": 1007, "61": 1024, "62": 1038, "63": 1054, "64": 1072, "65": 1088, "66": 1103, "67": 1117, "68": 1140, "69": 1161, "70": 1176, "71": 1189, "72": 1208, "73": 1232, "74": 1253, "75": 1274, "76": 1287, "77": 1310, "78": 1334, "79": 1349, "80": 1370, "81": 1385, "82": 1399, "83": 1414, "84": 1430, "85": 1445, "86": 1464, "87": 1480, "88": 1505, "89": 1523, "90": 1538, "91": 1555, "92": 1576, "93": 1590, "94": 1601, "95": 1613, "96": 1631, "97": 1644, "98": 1657, "99": 1675, "100": 1690, "101": 1703, "102": 1719}
---

**Dave Jones:** Hi, in a previous video I reviewed this Mantis 3D microscope and I complained that the LED brightness wasn't adjustable on it and for the price, well, it damn well should be. Um, so I wanted to uh actually take a look at

**Dave Jones:** that and uh see if it can be modified, if it has any internal regulation circuitry or anything like that. So, um as it turns out, it's pretty easy to uh take this sucker apart. I'll switch it off here and uh it this uh top cover

**Dave Jones:** here just pops off and then we've got a little diffuser thing for the LED and let's zoom in a bit more and on this we've got this whole assembly just comes apart here nice nicely screwed in with metal

**Dave Jones:** uh threaded inserts and everything and bingo, there's the PCB. Um there'll be one on each uh side here and check this out. It's just got a little DC jack on there. You can just pull that off. Very nice, nicely engineered and there's all

**Dave Jones:** the metal threaded inserts. It's really quite a nice design. As you can see the LEDs are around there in a circular fashion angled at a you know, they've engineered it at a very specific angle so the uh diffuser

**Dave Jones:** plate sits in there like that and it's all angled like that and it's very beautiful. I like it. But look at this, there's no circuitry on there at all. It's just dropper resistors. That's it. So uh I'll uh measure the

**Dave Jones:** rest of it uh to make sure it just comes through from the but I think it's just uh directly from the 9-volt plug pack straight through a dropper resistor for each LED. So, too easy to modify this thing um

**Dave Jones:** to use um PWM uh to get uh the brightness adjustment or you don't even need PWM. You can just use an LM317 linear regulator or something. And it looks like those little plastic clips there. They're like sort of those molded in

**Dave Jones:** type. So, I don't really want to break the board out there. So, I'll just measure these resistors and can do that just fine. Bang, 82 ohms. There you go. So, all they do and all they do is just

**Dave Jones:** driving this directly from the 9-V source. I think. Okay, so what I'm going to do is I'm going to measure the to see if there's any internal circuitry in here or whether or not the 9-V jack just passes

**Dave Jones:** straight through. So, going to get the I've got this plugged in here. I've got the ground here. And no. No, it doesn't. Hey, all right. Now, I think there's the inlet DC jack switch on there. So, you've actually got

**Dave Jones:** to plug the thing in. So, that cuz I can't believe the ground's not connected. So, it must be. Yep. There you go. So, that ground is connected straight through to there. Now, all we need to do is check the

**Dave Jones:** center jack on that. And the center pin here. And what do we get? Aha, well, there's something 0.6 meg Let's I suspect is there a diode in there perhaps? Let's whip that around.

**Dave Jones:** And have a look. There we go. That looks like a diode drop, but it seems to be in the wrong direction. So, I'm not sure what's going on there. There is definitely something in there though. And I cracked it open and yeah, look

**Dave Jones:** what we have here. We have an LM317 in here and also you can see the spring as well going all the way up that uh shaft up there. That's how it gets its nice uh retention uh system. Very nice spring. I like it

**Dave Jones:** and it's attached to there. It's insulated. It's got a little uh seal pad washer on there. So uh but they're using that as a heat sink and um LM317. So I'm curious to know if that's a um just it like a voltage regulator or a

**Dave Jones:** constant current or set up as a constant current source. Well, of course it's got to be a constant current source because there's only two wires coming in and out of this in the positive supply there. So it goes

**Dave Jones:** through the switch into it and then out to the uh LEDs. So they've got this thing set up as a constant current source. And there you have it, folks. Now, we could have uh uh you know, discovered all this without

**Dave Jones:** taking off that heat shrink, but that would have been no fun. But there you go. It's an LM317 constant current source. They got total of 2.5 ohms. So 1.25 volts divided by the which is the reference voltage of the

**Dave Jones:** LM317 divided by the 2.5 ohms is around about 500 milliamps constant current. So we've got 24 LEDs in this thing. So assuming that they're evenly spread across all the LEDs, we should be looking at about 20.8 milliamps per LED.

**Dave Jones:** Let's measure that and see if we get it. Now, I've already established that these resistors are 82 ohms each. So, assuming the current is shared across all of them equally, it'll be roughly something like that. Then, uh 420.8

**Dave Jones:** uh milliamps per LED we're expecting * 82 ohms, we should get about 1.7 V across each resistor. So, let's have a look. Ta-da! There you go. There you go. 1.7 So, it looks like the current is pretty evenly shared

**Dave Jones:** across all these. Not entirely spot on, but fairly well shared across all these LEDs. There you go. So, these things are operating at about 20.8 milliamps per LED. So, how do we go about dimming this thing? Well, obviously, cuz we have access to the

**Dave Jones:** circuitry in here now, we can add our own stuff in there, but I mean, that's that's quite nice, but anyone who wants to mod this thing themselves, it it's not that great they have to actually crack this thing open. So, it's probably

**Dave Jones:** better to put something in series with this lead here, so you don't have to modify anything on your Mantis at all. So, anyone should be able to do this and add the mod in or remove it as they need

**Dave Jones:** to. So, that's a better way to do it, but this is a constant current output. So, it's giving us half constant current. So, we need a circuit in here to dim these LEDs. And well, we can do that with PWM. So, let's lash up a quick

**Dave Jones:** little circuit and see what we can do. And there's plenty of ways to do this, but well, why not use the classic 555 timer? You can get a 555 timer to do a 0 to 100% PWM fairly easily. So, what we

**Dave Jones:** got here is I'm going to use a triple five timer here in the PWM configuration. This is my DaveCAD drawing, PWM LED dimmer. It's a classic triple five circuit and there's not much to it at all. We've got our input over here and

**Dave Jones:** our output here. And now, because this is a constant Usually, you don't do this with a constant current source on the input here, but it should still work, I think. So, you know, normally this is just a voltage source and you

**Dave Jones:** and then you would uh just PWM the output then you choose the drop resistor based on and we could do that if we ripped out the circuitry. We could just have the 9-V source and then we can calculate Well, we can actually put a a

**Dave Jones:** voltage regulator in there, calculate what voltage is required to give the same maximum current of 20.8 mA per LED that we had before or 500 mA and uh you know, made it all too hard. So, we want to leave in that constant

**Dave Jones:** current source. So, I think this circuit will still work even though it's constant current because we're just switching the constant current off and on off and on instead of the voltage. Now, this is the classic triple five PWM

**Dave Jones:** configuration. We've got an adjustment pot here which adjusts our pulse width modulation value from roughly 0 to 100%. It's not going to go over the entire range, but it's going to be pretty close. And we've got two steering diodes here and the uh and you

**Dave Jones:** know, it's quite a basic configuration. Now, how this circuit works is pretty simple. Uh when you first power it on, this capacitor is going to be a short circuit. So, the trigger pin is going to set this output high here and the output

**Dave Jones:** PNP transistor will be switched off because we've got a high here, we've got a high here. Uh This transistor only switches on when this output pin goes low. So, the output goes high. So, the um LED is starting

**Dave Jones:** switched off, and then we're going to charge up this capacitor through this 1K resistor here, through this diode, and through the and through the pot here. So, the pot is going to set our um uh frequency as well as our uh PWM

**Dave Jones:** cycle. And then once it reaches the threshold, bingo, we're going to switch the other direction. And then our discharge pin is going to discharge that capacitor through the other diode there. Easy. Because if you remember our triple five circuit configuration, I got my

**Dave Jones:** triple five timer t-shirt, which you can get from my Zazzle store, by the way. I hand drew this. It's how the triple five operates. And you can see that the uh output here, when the output switches, it is a flip-flop. So, the not Q output

**Dave Jones:** turns on the discharge transistor here. And that's exactly what we have in the circuit configuration. And this will uh come important later, I think, for a variation on this circuit. So, I've got my circuit built up on the breadboard

**Dave Jones:** here. Matches this precisely, except for one thing. Um the lab's a bit of a mess, and for the life of me, I couldn't find a 1N4148 diode to go in there, a 1N914, or whatever signal diode you want to use.

**Dave Jones:** So, um I had some uh LEDs handy, just sitting here on the bench. So, I used two LEDs instead of the two uh signal diodes there. It's going to work exactly uh the same, or it should. Um and except

**Dave Jones:** uh it's going to change it's going to alter the uh frequency, but we don't really care. Um we just want to get this thing working. So, that's the breadboard built up. I've got the um BD136 PNP output power transistor here because

**Dave Jones:** we're talking about half an amp. So, you've got to choose a transistor here which has an adequate continuous collector current in it and this is like a 1 and 1/2 amp transistor. So, it should handle that fairly decently. A

**Dave Jones:** 470 ohm base resistor here should give us enough current to drive that output at a half amp. Well, there's only one way to try it. Let's give it a go. And here we go. Using those values I had

**Dave Jones:** here, I am going to turn my pot here. Got a 10K pot and well, it starts down here and you'll notice we're getting a duty cycle of a maximum 8.8%. Now, this is the output on pin three of the 555 timer and you'll notice that

**Dave Jones:** it changes PWM all the way up to 99.6% duty cycle. So, that's not bad at all. Now, uh unfortunately, because we're using a PNP output transistor configuration here, this is actually going to be inverted. So, this will be our on period. So,

**Dave Jones:** really we're we're not getting close well, we're going to be 8 or 9% down from our 100% on period. So, it's going to be on for only, you know, 91% of the time or something like that. So, we're not going to get absolute maximum

**Dave Jones:** brightness out of this thing, but that's okay. Not a problem. And I've got my supply I'm just powering this from the bench supply, by the way. This is not coming from the um uh constant current source of the

**Dave Jones:** Mantis. That's the next step. I'm powering it from about 6 volts at the moment. I can drop it down. We're 2 volts per division there and as you can see, I mean, the frequency is going to change. We were at what, 300 hertz

**Dave Jones:** before. I get down to, you know, 5 V power supply a 5 V supply there and we're looking at 40 hertz or something like that. Go up to 6 V and it changes. The, you know, is this thing is not stable in terms of

**Dave Jones:** frequency, but for our purposes it doesn't matter. And we can go up like if we go up to 10 V, 12 V, something like that, we're still going to operate over and so 99.7% to 9.2%. So our minimum or our maximum,

**Dave Jones:** cuz we're inverted, drops there at 12 V. So anyway, we're this thing is going to be working at less than 9 V. So it should work over that range quite nicely. So let's hook this up to our constant

**Dave Jones:** current source and see if it still works and we can dim our LEDs. All right, first of all, let's take a baseline here. So I've got my mantis plugged into the existing 500 milliamp source. I got my light meter here and I've turned off my

**Dave Jones:** main LED lights above me just so it's, you know, the ambient doesn't interfere with it that much, but we just want to get a ballpark. We want to see if this circuit gives out pretty much close to the maximum and

**Dave Jones:** then dims. So our benchmark there is about 1630 lux. So let's plug this circuit in series with that and see what we get. And here we go. I've got it bodged into it there. So I've got it in line and

**Dave Jones:** we're getting we're not quite getting the maximum there as we expected because the PWM isn't going to 100%, but maybe we have to tweak our base resistor there. So that's maximum on the pot. So if I just the uh

**Dave Jones:** adjust the pot. Look at that. There we go. That dims quite nicely, fairly linear with the uh turning of the pot. So, let me I'll show you the show you the pot here. So, and then it switches right off at the

**Dave Jones:** bottom there. 177 lux. Turn it on. That's pretty nice. I like that. I think we have a winner. It doesn't quite go to the maximum lux we're getting before. So, I'm going to uh drop that base resistor a bit. I've got uh

**Dave Jones:** 470. Let's get a uh Here we go. A 220. Let's give that a go. So, let's go from 470 to 220 ohms and see if we can Hello. 16. So, we're getting It's a little bit better. Bumped something here. So, we're getting 1,500

**Dave Jones:** lux out of that thing. Let's plug the original Mantis back in. Yeah, 1,600. So, we're only losing 100 lux there. Not a big deal. So, with our values in the circuit, we're operating from 733 Hz. It jumps up a bit.

**Dave Jones:** Jumps all over the place as you adjust the duty cycle down to a low of 310 Hz. So, 300 Hz to 700 Hz or thereabouts um with our constant current source. Not a problem. I mean, we don't particularly

**Dave Jones:** care about the frequency. That's uh uh much higher than um any, you know, flicker that's going to be a problem. So, no drama. And if you're wondering what the current output waveform looks like, the output waveform is uh channel one

**Dave Jones:** here, the yellow one. And uh the green channel two signal here is the out is the pin three output, the Q output of our 555 timer flip-flop. So, let me adjust the uh So, let me adjust the pulse width there.

**Dave Jones:** And uh as you can see, as I said before, it's actually uh inverted because we're using a PNP transistor there. So, we're going from, you know, like down under a percent there to right up to, well, you know, close to

**Dave Jones:** 98%. So, that's pretty good. I'm pretty happy with that. And if you're curious to see our charging discharge waveform, i.e., uh pins two and six, it's the bottom waveform there, and the top one is our pin three Q output. So, you can

**Dave Jones:** clearly see that uh 0.1 microfarad cap charging up there until it hits the uh threshold value, and then the uh discharge pin kicks in, uh shorts to ground, and that then shorts out the cap, and bang, it goes back back like

**Dave Jones:** that. And it oscillates. That's how the 555 works. Now, we can't just leave it at that. I think this thing has got too many components, and I think we can get rid of one. So, I've got another circuit

**Dave Jones:** here, optimized, and you'll notice that the differences between them aren't Well, there's only uh basically spot the difference. We've removed this 1K resistor up here, but we've swapped pins three and seven like that. So, now the discharge pin of the 555 timer here is

**Dave Jones:** uh turning on our PNP output transistor here, and then our uh Q output of our 555 timer is doing the uh charge and discharge cuz we don't need that pull-up resistor anymore in there because um the uh cuz we did need it before because the

**Dave Jones:** discharge pin is an open-collector uh output. So, it doesn't have It's not a totem-pole output, so it doesn't have anything to pull it up. So, we need the 1K to pull it up, but the uh pin three of the 555 timer, the Q output, is not

**Dave Jones:** an open-collector output. So, we can do away with that pull-up resistor. So, we've just optimized the circuit there, and we've got gotten rid of one resistor. Let's try it. So, this is circuit number two. We'll leave it here.

**Dave Jones:** So, let's just uh modify that. So, we'll There's our pin seven pull-up. So, we'll get rid of that, and we'll uh this base resistor here has to change. That's got to go over to pin Hang on. This is going to This is going

**Dave Jones:** to get messy. Uh So, we want our LED on pin three. Let's just switch this thing off, shall we, for a second? And So, we want that through to pin three. Our other diode through to pin three. It's working well with these LEDs, not a

**Dave Jones:** problem. And we want our base resistor the transistor to go up to pin seven up there. So, we've gotten rid of our one resistor. We've optimized that out. Let's hook this thing back up, and give it a go. Hey, hey. It is still

**Dave Jones:** still working. Our lux meter is switched off. Our lux meter is still reading. Oh, it's reading What's it reading? There we go. We're up to 1600 lux. And we're going all the way down to There you go. Not a problem. So, let's

**Dave Jones:** take a look at those waveforms again and see what duty cycles we get. They should be near identical. All right, let's have a look at the output. We're measuring the duty cycle of the of input two now, which is our

**Dave Jones:** top waveform, which is our pin seven discharge pin. And if we adjust our PWM value, we're going down to 0.3%. Brilliant. Smoothly. Once again, the frequency does change, but whoopty-doo. All the way up to 99.2%. Lost our trigger there a little bit, but

**Dave Jones:** there you go. Just getting a more accurate value of the maximum. There you go, it's close to 99%. percent. Ah, this works really quite well. I like it. 0.3%. To 99, greater than 99%. Terrific. So, just why were we able to swap pins three

**Dave Jones:** and seven? Well, here's the discharge pin here. And as you can see, it's the Q, it's the not Q output of this RS flip-flop. And the regular output is just a buffered version of the Q output. So, really, these are just going to be

**Dave Jones:** complementary outputs. So, there's no in this particular circuit configuration, there's no problem with swapping these two pins. And by virtue of doing that, we managed to save a resistor. Beauty. So, there's our final circuit. Base resistor there, around about 220

**Dave Jones:** ohms. I'm using a 10K pot. I'm using LEDs in there, but we can just use regular signal diodes if you want. It's still going to work just a treat. 100 n timing cap here. I'm just putting on a, uh, 10 in, uh, compensation cap

**Dave Jones:** there. You don't necessarily, uh, have to do that. It might still work. Um, and of course there's a bypass cap across the, uh, rail there. But that's all there is to it. And the BD136 has, uh, plenty of grunt to drive, uh, the 500

**Dave Jones:** milliamp, uh, constant current LEDs in this thing. And it no, it doesn't, uh, really get warm at all. So there's no power dissipation issues there. And the whole thing works a treat over the whole, uh, duty cycle range. Very

**Dave Jones:** smooth, very linear, really, um, in terms of the pot. I'm using a linear pot, by the way. I'm not using a logarithmic one. Um, and it works just fine. So, all that's, uh, left to do is build this thing up and put it in series

**Dave Jones:** as a permanent fix. And I'm actually using the, uh, CMOS version of the triple five, the LMC triple five here. But yes, it is a genuine National Semiconductor. And yes, just add, a little bit of authenticity, it is greater than 20 years old. 52nd

**Dave Jones:** week, '91. Nice. Now let's have a look at what it's like when it's completely assembled again. I've got, uh, both LEDs lighting down, uh, nice and evenly. And we're getting basically 4,500 lux or thereabouts, cuz that's a times

**Dave Jones:** 10 range. So, uh, you know, 4,000, yeah. Let's say 4,500 lux. Got my board built up here, ready to go. It's not, uh, uh, heat shrunk or anything, or any case or anything yet. So, let's plug it in.

**Dave Jones:** And bingo, we're getting 40 300 lux. Is that maximum? Let's adjust the pot here. There we go. Look at that. From 500 lux. And now for the big test. Does it actually work through the viewfinder? That's maximum there. I've got uh

**Dave Jones:** constant exposure on my camera and I'm turning the wick down. Turning it down. And it's a little bit little bit touchy at the bottom end there. But uh certainly we have a very nice adjustable range now. I like it. Let's

**Dave Jones:** put our board on a 45° angle there and uh adjust our light all the way down to pretty darn low. I like it. I mean, it's actually brighter than that in uh through the viewfinder. That's just my uh the

**Dave Jones:** constant exposure mode I've got on the camera there. I mean, if I turn constant exposure off. There we go. We're uh I've turned it all the way down and the camera's still going to compensate. So, I'll turn it all the way up.

**Dave Jones:** Constant exposure again. And turn it all the way down. Beautiful. It's a nice smooth linear range. There's no flicker on the camera. Ah. Perfect. What a win. So, that was just a quick uh simple hack there on some

**Dave Jones:** veraboard. Not a problem. There's the output connector which uh helps to if it's a a right angle one like that going in and there's the input socket and the adjust pot. Now, I can mount this in some sort

**Dave Jones:** of case or I'll probably put some large heat shrink over it or something like that and I don't know. Um maybe cable tie it up in all up in place. I don't know. There's a few options for uh

**Dave Jones:** mounting the thing in line. But, you want to sort of keep it as short as possible, I think, and just have it dangling there, really. I mean, you know, it's not often that you have to um adjust this thing. So, really if it just

**Dave Jones:** hangs there, that's fine. So, yeah, I will just heat shrink that. There we go. No problems at all. That'll give it a, uh, nice reasonable protection. And maybe I can, uh, cable tie the thing in place or something like

**Dave Jones:** that, perhaps. And I'll do a second heat shrink pass on this thing so that it, uh, seals in the pot and the pot just sort of mounts on the side there like that and that'll hold it in place

**Dave Jones:** nicely, I think. So, uh, you know, it'll just dangle there. It's, uh, I can put a knob on it, but, uh, you know, frills. Who cares? And it could be mounted in a nice box or something like that, but

**Dave Jones:** there's nothing wrong with just a bit of heat shrink like this and maybe some, uh, hot snot as well. Some, uh, hot melt glue in various places, but there you go. I think that is, uh, quite a nice little solution. I like it.

**Dave Jones:** And there's the finished mod. I've just got it, uh, cable tied up in there and it just sits there really quite nice. It's all hidden out of view. I can just reach around and adjust the brightness as required.

**Dave Jones:** That works an absolute treat. I'm pretty darn happy with that simple hack. Yeah, could have been done better, but don't mind that at all. So, there you go. If you've got a, uh, Mantis, it's, uh, well worth doing this mod to get

**Dave Jones:** variable brightness on your LED. It's really quite neat and you don't have to hack the circuitry inside. It's just using the constant current source straight in. Beauty. If you want to discuss it, jump on over to the EEVblog forum. If you

**Dave Jones:** like the hack, please give it a big thumbs up. Catch you next time. Mhm.
