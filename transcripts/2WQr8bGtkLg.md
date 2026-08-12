---
video_id: 2WQr8bGtkLg
title: EEVblog 1676 - Lab Timer HACK
url: https://www.youtube.com/watch?v=2WQr8bGtkLg
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 28, "3": 42, "4": 54, "5": 66, "6": 78, "7": 92, "8": 109, "9": 122, "10": 135, "11": 149, "12": 160, "13": 172, "14": 186, "15": 199, "16": 210, "17": 223, "18": 236, "19": 251, "20": 263, "21": 278, "22": 292, "23": 304, "24": 314, "25": 328, "26": 339, "27": 353, "28": 367, "29": 380, "30": 394, "31": 406, "32": 422, "33": 432, "34": 445, "35": 456, "36": 469, "37": 482, "38": 494, "39": 506, "40": 522, "41": 541, "42": 557, "43": 574, "44": 595, "45": 612, "46": 632, "47": 649, "48": 669, "49": 685, "50": 699, "51": 715, "52": 731, "53": 746, "54": 759, "55": 776, "56": 793, "57": 809, "58": 819, "59": 833, "60": 860, "61": 875, "62": 885, "63": 897, "64": 910, "65": 922, "66": 933, "67": 947}
---

**Dave Jones:** Hi, I was just working on a new video here, a part two to my fuse follow-up. I'll link it in if you haven't seen it, where I tested a 400 milliamp multimeter fuses. Very comprehensive, very interesting video, but I thought I'd

**Dave Jones:** thought I'd follow up on a part two video with new 630 milliamp fuses for the BM2257. So, what I need to do there is time how long it takes for fuses to actually blow. And spoiler alert, if you haven't

**Dave Jones:** seen the video, it can take quite some time. Like minutes to tens of minutes, many tens of minutes, like half an hour for fuses to actually blow, depending on the current that you've got going through them, and depending on the

**Dave Jones:** tolerance and everything else. I'll link in the video, check it out. But, it's annoying to sit there and actually watch to see when the fuse actually blows. But, not only do I have to time it, I want to be able to go do something else

**Dave Jones:** and then just hear a beep in the other corner of my lab to know that the fuse is blown, so that I can come over and check it. So, what I thought I'd do is use my lab timer here. This is a Brymen.

**Dave Jones:** It's probably not made in England, but anyway, English company Brymen, they make like lab equipment and stuff like that. And this is what's called a lab timer. It's just like a basic like start, stop, you know, lap. And it's got

**Dave Jones:** two different modes, cumulative come there and lap here. So, yeah, it's just a very basic timer. It doesn't do anything. But, the good thing about this is that it does have external trigger inputs. So, it's got a common terminal here,

**Dave Jones:** like this. And basically, if you short out these two terminals, that simulates like externally pressing the start stop button. And likewise, if you short out these two terminals here, it simulates doing the pressing the split lap reset button here. So,

**Dave Jones:** this is not a really great lab timer or that versatile, but at least it does have the external inputs, which unfortunately is all I've got at the moment, so it'll have to be good enough for Australia. So, I thought maybe I

**Dave Jones:** could tie this into doing the fuse thing. But the problem with testing a fuse like this is that you're going to get a very low voltage across the fuse, i.e. the burden voltage. I've done quite a few videos on that. My entire

**Dave Jones:** microcurrent product is based around that. Anyway, there's a low voltage across the fuse here, and then when the fuse blows, then the 12 volts that you're applying well in my particular case, the 12 volts, the compliance voltage, whatever the compliance voltage

**Dave Jones:** of your power supply is that you're actually using in constant current mode. You can see I'm putting 400 milliamps through that fuse at the moment, and it's got a burden voltage of 0.3 volts. In fact, that's not just the fuse,

**Dave Jones:** that's actually cuz I'm only using a two-wire measurement, that's drop on the cables as well. The fuse is probably only you're going to be about 0.2 or something like that. But if I disconnect my fuse like that, i.e. my fuse blows,

**Dave Jones:** it goes up to the voltage that I've set on my power supply, which is called the compliance voltage in this particular case. That's just the industry parlance. So, what this thing to trigger when I apply 12 volts to well, either one of

**Dave Jones:** these. I don't care whether it's start, stop, or it's you know, a lap thing like that. Makes no difference. So, I want to modify this so it when I apply a positive voltage to either of these terminals with respect to the common

**Dave Jones:** terminal here, I want it to beep at me and stop like that so I can come over and take my reading. Unfortunately, as I said, it only works when you short out these two terminals, i.e. you drive it

**Dave Jones:** with a like a an open collector transistor driver, for example. That's basically what it's designed to do. So, I thought I'd just have a little go at just modifying this, change one of the terminals here, probably this lap reset

**Dave Jones:** one, add a little mod board in it to change it from shorting out to applying 12 volts on there, and I want it to stop. So, how can we do that? Well, it's not that hard. We've got a Dave card here.

**Dave Jones:** Um where as I mentioned, we're going to have an open collector transistor here. In this particular case, a NPN jobbie, uh 2N2222 jellybean component. I've done a jellybean video on bipolar transistors. I'll link that in. And this is one of

**Dave Jones:** the classic jellybean parts. It's not critical. Almost any NPN uh will work here. And the reason we need an NPN instead of a PNP is because we've got positive 12 volts here, assuming that the negative is connected through to the

**Dave Jones:** coms here. So, a positive here, we want to then turn on the base like this, and then the transistor effectively we're using the transistor as a switch, and then it should just short out the lap and the com terminals. And because this

**Dave Jones:** is a battery-powered uh thing, there shouldn't be any issues with like conflicting grounds or anything like that. Um even if uh this external uh power supply here is mains-earth reference, it doesn't matter a rat's because this is all internally

**Dave Jones:** battery-powered. So, if we connect the collector and the emitter across the uh lap terminal and the com terminal of uh our timer here, it could it doesn't have to be the lap, it could be the start-stop, it doesn't matter, but I'm

**Dave Jones:** going to use the uh lap uh terminal, and then it effectively operates like a switch. Now, of course, a bipolar transistor is not the only thing you can use here. You can use a MOSFET, you could use a relay, you could use a

**Dave Jones:** solid-state relay, um you know, whatever you want to actually uh do this as long as we short out those two terminals there. So, if we apply 0 volts on the input, then there's no base current here for the uh base-emitter uh junction.

**Dave Jones:** Therefore, the transistor will turn off, it'll be a high impedance, and the timer won't think that there's anything connected there at all. But as soon as you apply voltage on here, then you'll get enough base current flowing through

**Dave Jones:** here, the transistor will turn on, saturate, and give a low resistance between here, and it'll think that you're just connecting these terminals. bingo, it's going to stop uh the timer. But, a particular quirk of what I'm trying to do here,

**Dave Jones:** because I'm using a fuse, it's going to have a quite a significant burden voltage across it all the time. Like it's going to have 0.2 volts, a volt, even millivolts as you've seen in if you watch the previous video. It can have

**Dave Jones:** like up to like 8 volts or something like that on it at just before it actually breaks. So, I don't want this to false trigger with like a volt on here or something, which of course it will because a base emitter junction only

**Dave Jones:** needs like 0.6, 0.7 volts to actually switch on. So, yeah, if the burden voltage on this gets too high, we get a false trigger. So, the way I avoid that is by adding in this Zener diode here. I've chosen a 10-volt Zener diode, so it

**Dave Jones:** basically this is going to drop, you know, roughly 10 volts. Zener diodes aren't that precise. I've done a whole video on Zener diodes. I'll link that one in down below. Check it out. Very informative, but they're not very

**Dave Jones:** precise, but it's good enough for Australia. And basically, so we need to get to at least basically 10 volts, maybe a bit under, something like that on our terminal here before this transistor will switch on. So, we're just dropping those voltages there. You

**Dave Jones:** could have put like a whole bunch of series diodes in there to drop like 0.6 volts each or whatever, but you know, a 10-volt Zener, it does the job. So, you can tailor that voltage to anything you want. So, even

**Dave Jones:** if we get 5 volts on here for example, it still should not turn on this transistor. And the 1K resistor here, I haven't calculated this at all, just from experience 1K is like it's going to be good enough. I'm not

**Dave Jones:** going to work out what the Zener currents are and everything else and all that sort of jazz. 1K I think it's going to do the job for the base resistor there. So, anyway, that's the plan. Let's go. So, here's inside the thing.

**Dave Jones:** This is the mod board that I've made. I'll show you that in a minute, but basically we've got our just our battery here, single uh double A. Um we've got a buzzer here, and a nice attention to detail here is this little uh heavy

**Dave Jones:** weight here that just weighs the thing down, uh low center of mass, stops the thing sliding around on the bench. Very nice touch. Um and it's basically just a uh two board uh construction here, nothing much going on at all. Uh just

**Dave Jones:** the front panel uh key switch board. It's just got discrete wiring going over. That's a bit how you doing. Um so, yeah, they haven't production optimized this thing all. And uh we've got our three terminals uh down there, and uh

**Dave Jones:** just a uh just a single PCB here. I won't bother taking it out now, but I've taken it out donkeys years ago, and there's just a little uh from memory, it's just a little uh chip on board, just a single custom ASIC uh chip, and

**Dave Jones:** just a blob, and uh that's it uh driving the LCD. So, yeah, pretty simple. So, I've created the uh mod board here with the uh circuit exactly um as configured there. So, let's give it a go. Uh What? What? What? What? Something is

**Dave Jones:** wrong here. Um It doesn't work. Um Check it out, right? So, here's here's my timer, start, stop, okay? And so, all our buttons work, no problems whatsoever, but listen, when I connect it, it beeped. It um is doing the lap thing, and my lap switch

**Dave Jones:** actually works like this, but if I plug in my uh voltage across the fuse, it beeps at me, and it thinks that it's actually And the button doesn't work anymore. And I've only got 0.6 V across the um terminals there, like from

**Dave Jones:** the uh fuse, cuz that's the voltage drop of the fuse at uh 400 mA. Well, not just the fuse, but the leads and everything else. So, um uh yeah. What? And if I break the fuse, simulate it breaking, I get my 12 V,

**Dave Jones:** and um it it doesn't stop. So, that's like permanently on. Uh I've I've goofed something cuz that should have worked. Uh Well, there's your problem. Um I'm not sure if anyone spotted that before cuz I don't know. I had a

**Dave Jones:** complete brain fart. I was not thinking when I soldered this. Must have been daydreaming. Um can you spot the problem? With our little Zener diode here? Uh yeah, it's back to front cuz there's the black band on it and that is the

**Dave Jones:** cathode and that's going to the base. Whereas our circuit the anode should be going to the base. Oh. OH. NOW, WHILE checking that, I just found something interesting. Look, I'm reading the voltage between the common terminal and the start-stop over here,

**Dave Jones:** it's -1.5 V. So, that is exactly the same voltage as the battery. So, I just assumed that the common you know, what I call the common terminal here, the black one is would have been connected to the battery

**Dave Jones:** negative, but it's it's not. It's connected to the battery positive. Let me double-check that. And yep, the common terminal and the battery positive is uh electrically connected, shorted. So, that's interesting. That this circuit is that the input here I just assumed that

**Dave Jones:** that would be referenced to the internal circuit common or negative, but it's not. It's actually referenced to the battery plus input. Now, that shouldn't actually in theory that that shouldn't make any difference to here cuz as I mentioned,

**Dave Jones:** even though you know, we've got basically -1.5 V on here relative to this terminal, it shouldn't matter because we've got a separate power supply out here and a separate isolated battery supply in here. So, in theory, that shouldn't matter. We should still

**Dave Jones:** be able to turn that transistor on. But, if you know your transistor theory, you should know the Ebers-Moll model of the transistor. It's It's actually you can model it with another diode in here as well between the base and the collector

**Dave Jones:** like this as well as the base and emitter. So, that can cause you problems. But, anyway, let's uh fix that bloody diode goof and try that again. All right, let's see if it works this time. Now, one thing I just noticed

**Dave Jones:** is that my fuse actually blew. My 630 milliamp fuse and you saw that was 0.6 volts before. Well, now it's actually 0.2 volts again cuz I've got a brand new fuse on there. So, I just mucking around, I must have been

**Dave Jones:** abusing this poor fuse and it eventually blew. So, anyway, I have reversed my diode in now, so it's exactly as per this circuit now. So, let's see if it works. We've got 0.2 volts on the input, which is the burden voltage across the

**Dave Jones:** fuse, and can we operate it? Yes, we can. And the lap button now works. So, yep. Yep, no problems whatsoever. So, we start our timer. Let's now simulate breaking the fuse. This should jump up to 12 volts, which is the compliance

**Dave Jones:** voltage of our power supply, and it should trigger. Yay! Winner, winner, chicken dinner. So, that works just fine. And so, yeah, it'll now beep at me. I can come along and I can read that reading off there. So, let's find out now what our

**Dave Jones:** essential trigger voltage is. Trigger voltage isn't the correct word, maybe threshold voltage on our input here to overcome Well, to switch on the transistor here to overcome the the voltage of the Zener diode the drop on the Zener diode here. As I mentioned,

**Dave Jones:** it's probably going to be a smidge under um that 10 volts cuz they're not precise and it has to do with the resistor current and everything else. Um the characteristic curves of the Zener. We won't go into uh that detail. You can

**Dave Jones:** watch my video. Yeah, so let's uh start out at 1 volt here and just wind it up until um our transistor switches on here. And so, let's give that a go. So, I've disconnected our fuse here. Let's start at 1 volt and

**Dave Jones:** let's wind up the wick, shall we? And where will it trigger? Place your bets, place your bets. You know, 9 volts, maybe? 9 and a half? Getting there. WHAT? 9.6. OH, THERE YOU GO. 9.6 VOLTS. No worries. So, that is perfect. So, we

**Dave Jones:** can tolerate a not a massive 9.6 volt burden voltage on here without this thing triggering at all. So, that's exactly what I want. So, there you go. So, now I'm going to be able to test these fuses in bulk cuz some of

**Dave Jones:** these can take up to like half an hour to blow. So, yeah, I don't want to be watching this rig. I can just sit on the other side of the lab here and just listen for the beep and then come over

**Dave Jones:** and it's automatically recorded the value here. So, there you go. Hope you enjoyed that video even with that little goof in there. Although, I guess we learned something there. Yeah, double-check placement of the components. For like a dollar for every

**Dave Jones:** time I put a Zener in back to front, I think, "Geez, I'd be rich." Yeah, your mind just thinks, "Oh, yeah, it's a diode." And you don't realize, "Oh, Zener diodes. It's got to go in backwards cuz they're reverse biased.

**Dave Jones:** That's how the breakdown voltage works." Yeah, you can put it the other way. It works as a regular diode just fine, but yeah, not for this circuit. We wanted to drop that voltage. So, there you go. But as I said, didn't have to use a

**Dave Jones:** transistor, could have just whacked on a 12-V relay or something like that. And then the relay would have had the coil of the relay would have had maybe like 6 or 7 V or something to like switch that

**Dave Jones:** on. That that sort of latching voltage on the relay. So, you know, that would have So, you could reduce your parts count from three down to one if you really wanted to for a bit slower reaction time. You know, milliseconds instead of, you

**Dave Jones:** know, practically instant for the transistor here, but um yeah, we're not that fussy. But, anyway, hope you enjoyed that video. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.
