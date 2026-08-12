---
video_id: gqzZHbEfWDU
title: KoradFollowup Charles
url: https://www.youtube.com/watch?v=gqzZHbEfWDU
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 21, "2": 39, "3": 59, "4": 83, "5": 107, "6": 130, "7": 158, "8": 181, "9": 216, "10": 241, "11": 256, "12": 272, "13": 295, "14": 308, "15": 328, "16": 344, "17": 367, "18": 387, "19": 405, "20": 430, "21": 457, "22": 494, "23": 520, "24": 537, "25": 575, "26": 591, "27": 611, "28": 644, "29": 685, "30": 718, "31": 747, "32": 760, "33": 776, "34": 795, "35": 812, "36": 832}
---

**Dave Jones:** Hey everyone, it's Charlie here from Trio SmartCal, and I've got the latest installment in the Co-Rad saga for you. This is the new power supply that they've sent us, and what we're going to do with it is give it a short-circuit test, we're going to give it an intermittent short-circuit test, we're going to give it a full-load test,

**Dave Jones:** and we're going to give it an intermittent full-load test. And hopefully we'll be able to recreate the conditions that Dave did when he blew its predecessor up. So, let's get on and see how the testing goes. And by the way, I'm going to try and see if I can use it as a bit of an arc welder as well.

**Dave Jones:** Okay, well the first test is a short-circuit test. As a short-circuit, I'm using an Agilent U1252A multimeter on the current inputs, so that's pretty close to being a short-circuit. And we've just got the leads. I'm going to short it out there, so basically we're just feeding it straight into the current terminals of a multimeter.

**Dave Jones:** The power supply is set to 1 volt and 5 amps. So let's turn it on and see what happens. Okay, well that doesn't look too bad. We've got 0.6 of a volt voltage drop, as I suspect that's in these connecting leads here in terminals.

**Dave Jones:** There will be some resistance there. And at 5 amps we are going to get some millivolts showing up. We've got 5 amps showing over there, so it doesn't look too bad. Now we'll turn it on and off rapidly and see if that does anything.

**Dave Jones:** Nope, nothing really happening there. So let's now go and select the maximum voltage that it's capable of providing. So I've programmed memory 4 here for 31 volts and 5.1 amps. And that's the maximum deliverable by this supply. So let's turn on and see what happens.

**Dave Jones:** Oh well, we're showing 5.1 amps and we're showing pretty close to 5.1 amps on the display. And we're showing a 600 millivolt drop through these leads. Which is pretty much to be expected. So let's just flick this output on and off rapidly and see what happens.

**Dave Jones:** Yep, that doesn't seem to cause any trouble either. Okay, let's now try a very intermittent short circuit test. So what I'm going to do is disconnect here. I'm going to do this one-handed. There we go. And I'm going to attempt to short out the power supply intermittently.

**Dave Jones:** So let's turn the output back on again. Okay, so we've got no current flow at the moment. And let's see what happens here. So I can get an arc here. And the crocodile clip is starting to look the worst for wear. You can hear the relay selecting the transformer here.

**Dave Jones:** The relay selecting the transformer taps clicking in and out there. Well, all seems to be okay. Let's just put it back up to short circuit again. That didn't seem to give it much of a problem. So anyway, that's the intermittent short circuit test.

**Dave Jones:** The potential arc welder test. And the constant short circuit test. And it all looks good. And by the way, you'll notice that the multimeter display is actually showing a higher reading than before. For those of you who worry too much about these things,

**Dave Jones:** what you'll find is that with a digital multimeter, when they've been carrying a high current for a period of time, the internal shunt actually warms up. And what happens when they warm up is their resistance increases. And they work by using their voltmeter to measure the voltage across the shunt.

**Dave Jones:** So obviously as the shunt warms up, then the voltage across it increases, so the current display is actually increasing. It's interesting though that the power supply has kept a similar level of current showing all the time. So in this instance, I'd be more inclined to believe the actual power supply's display than I would the multimeter's.

**Dave Jones:** I'm sure you all know what this is. It's a car headlamp bulb. And the reason I've got it, is that it actually has a really good load for testing the power supply. It's got a couple of filaments in it. One is a 60 watt filament, the other is a 55 watt filament.

**Dave Jones:** So there's 115 watts there. And that'll give us the ability to draw a bit of current out of the power supply. Now the way these bulbs are wired is that there's a common there, and then one terminal for each of the filaments. But if you go across the two terminals that I showed you earlier,

**Dave Jones:** across the two terminals that I'm not holding, that actually puts the two filaments in series. So that's what we're going to do. So we'll be applying 24 volts to this, and hoping to draw somewhere around four and a half, five amps out of it.

**Dave Jones:** So that's what we'll do. So let's give it a go and see what happens. Well we've wired the filaments and the bulb in series now. As you can see. And we've taken the multimeter and we've connected it so that it's actually measuring the output voltage as opposed to the current.

**Dave Jones:** Now we know that the current metering on the power supply is pretty accurate from what we've seen already. So I don't want the shunt resistance of the multimeter actually in circuit. So we've taken that out and we'll measure that voltage. The other reason is I just wanted to show you the effect of the lead resistance

**Dave Jones:** when you're delivering a higher current to a load. What we'll be getting on the power supply versus what we'll be seeing at the bulb will be different due to the voltage drop actually in the leads. So let's turn it on and see what happens now.

**Dave Jones:** This is going to... All right, there we go. So you can see we've got our 24 volts. We've got 4.6 amps. And if we can see it, we're in constant voltage mode. That's OK. We're showing 23.95 at the output terminals. That's about a 50 millivolt difference there

**Dave Jones:** from the 24 volts that we've asked for. If we just disconnect the bulb for a second... OK, you can see that it's... We're out by about 20 millivolts, 21 millivolts at 24 volts. So you're looking at about 0.1% accuracy there. So that's not bad.

**Dave Jones:** I'll connect this bulb up again. You can see a slight voltage drop from when it was open circuit. And what I'll do now is I'm just going to take this lead from here. And I'm going to connect it onto the headlamp bulb. I'll try and do this without destroying the camera on my phone.

**Dave Jones:** It's connected on there now. If we go back and have a look on the multimeter... See, it's now got 23.87. So you can see there's been a drop of about 0.12 of a volt or so. And that voltage drop's in the lead. And that's why if you are using power supplies and delivering higher currents to a load,

**Dave Jones:** and you want to be sure that you're getting the right voltage at your load, then measure the voltage separately at the load as opposed to relying on what you're seeing on your power supply. There's other ways of doing this called four-wire techniques, which those of you who are into measurement will know all about it.

**Dave Jones:** Those of you who aren't, interesting topic. OK, we're going to move this back again. In the meantime, the power supply's obviously been behaving itself because the bulb's stayed on and we haven't blown it up in voltages. It's stayed stable. So let's just flick it on and off a few times now.

**Dave Jones:** You can also see briefly there, when the power supply is first connected, turned on, we go to constant current mode, then we go to constant voltage mode. And that'll be when the bulb is actually pulling maximum current out of the supply, so it just says, "I've had enough."

**Dave Jones:** I'm going to constant current, and then it drops back to constant voltage, which is what it's at now, but you can't really see that because of that bulb. So we're going to get that out of the way. There you go, constant voltage. If I increase the voltage on the bulb now,

**Dave Jones:** what we'll end up doing is driving the power supply to be delivering its maximum current, and then we'll flip across into constant current mode at a certain voltage. So let's try that. There you go, so 24. Oops. 24, 25, 6. See, the current's going up.

**Dave Jones:** 27. 28. 29. We're in constant current mode now. The bulb went back down. Constant voltage mode. Constant current mode. So we're delivering pretty close to our 5.1 amps. Now, the thing's rated at 5 amps, so it's got a little bit of overrange there,

**Dave Jones:** but if you want your 5 amps, you're going to get it, and obviously it hasn't blown up because we're still being blinded. Multimeter has just done an auto-power off. Yep, it's all working. Let's just hit the M1, M4 button, because that's the 31 volts, 5.1 amps.

**Dave Jones:** Turn that on. Yep, all good. Yep, nothing strange happening there. So we've tried to use this power supply. Well, we short-circuited it. We've given it intermittent short-circuit. We've tried to use it as a makeshift arc welder. We've driven it to full load. We've driven full current.

**Dave Jones:** I'm pretty satisfied with that. We have managed to blow it up. We've done similar to what Dave did with the varying load conditions when the one he did blew up. The interesting thing about this one is this one's got a sticker on the back that says 240 volt.

**Dave Jones:** The ones that we tested previously at 220, now, we were told that they were supposed to be capable of running on 240 volts, and one of the questions that we received from Corad was what are the Australian voltages, and we only received that question today.

**Dave Jones:** So I suspect that we might have had power supplies that were designed for 220 volts and not 240, because even that 20-volt difference, by the time you stick that across your regulator transistors, you're going to be dissipating a lot more power. So if the transistors aren't up to the job,

**Dave Jones:** they're going to go, and I suspect that's what's happened. But anyway, somebody will confirm that or deny it, probably Corad, if they're listening to this. So Chrissie, if you're listening, tell us what you've done, please. We'd like to know. But as far as I'm concerned,

**Dave Jones:** if you send us the parts, we'll modify all the supplies we've got, and when we've modified them and given them a bit of a test, we'll put them back on sale with a two-year warranty. So I'll just do this again, and I'll say this was an enlightening video.

**Dave Jones:** Yeah, sorry about that. Okay. It's now 5:00 to 8:00 in the evening, and there's a beer waiting for me. I'll see you folks. All the best, and thanks for watching.
