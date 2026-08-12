---
video_id: 9inGSp2QnfI
title: EEVblog #1245 - A Most Excellent REPAIR: IBM PCjr Keyboard
url: https://www.youtube.com/watch?v=9inGSp2QnfI
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 0, "2": 28, "3": 58, "4": 58, "5": 88, "6": 118, "7": 118, "8": 148, "9": 161, "10": 178, "11": 198, "12": 217, "13": 238, "14": 251, "15": 268, "16": 296, "17": 298, "18": 330, "19": 349, "20": 364, "21": 382, "22": 398, "23": 414, "24": 427, "25": 443, "26": 461, "27": 477, "28": 493, "29": 509, "30": 529, "31": 547, "32": 563, "33": 579, "34": 595, "35": 613, "36": 630, "37": 644, "38": 664, "39": 678, "40": 694, "41": 712, "42": 734, "43": 752, "44": 770, "45": 786, "46": 802, "47": 818, "48": 834, "49": 849, "50": 861, "51": 875, "52": 891, "53": 905, "54": 921, "55": 941, "56": 955, "57": 971, "58": 983, "59": 999, "60": 1019, "61": 1035, "62": 1048, "63": 1064, "64": 1080, "65": 1094, "66": 1112, "67": 1130, "68": 1146, "69": 1168, "70": 1188, "71": 1204, "72": 1218, "73": 1238, "74": 1253, "75": 1269, "76": 1287, "77": 1305, "78": 1321, "79": 1335, "80": 1353, "81": 1369, "82": 1385, "83": 1405, "84": 1419, "85": 1437, "86": 1451, "87": 1467, "88": 1487, "89": 1504, "90": 1518, "91": 1536, "92": 1552, "93": 1564, "94": 1578, "95": 1592, "96": 1608, "97": 1624, "98": 1638, "99": 1652, "100": 1664}
---

**Dave Jones:** Hi, it's repair time, the classic IBM PCjr keyboard. Now, this comes from my older IBM PCjr teardown video and where I got that partially up and running. I'll link in both of those videos, main channel and the second channel video if you haven't seen it.

**Dave Jones:** It's a rather interesting and in-depth teardown of probably the most successful failure in IBM's history, the IBM PCjr. Anyway, this keyboard didn't work. It actually, it's an infrared wireless keyboard. I've already, yes, I've already taken it apart a bit. Infrared wireless keyboard, but it's also got a wired connection as well.

**Dave Jones:** Now, the wired connection was causing the computer not to boot up. So, yeah, it's a problem and I've tried to put the batteries in there. I've tried it. The computer works, but the wireless keyboard doesn't either wired or wireless. So, I thought we'd take it apart, have a look.

**Dave Jones:** Of course, all the yellowing's happened and from people using it, it's all, you know, the smooth edge down here and all the rest of it. So, let's take a look inside. Here, it's got, I mentioned this in my previous video, probably the worst designed battery holder I've ever seen with the rails in there and you've got to slide the batteries under.

**Dave Jones:** It's just really, really bad. Anyway, let's take this thing apart and let's have a squiz inside and ta-da. That's why people hate it. It's because it's a rubber membrane keyboard. It's not a proper IBM keyboard. Look at that. But, you know, I think it feels okay.

**Dave Jones:** There's nothing hugely wrong with it. I won't take all that out. Anyway, I think it's okay. What we're looking at is the main board. There's something wrong with this. Now, the first thing, you may not notice it, but I can. I can just bend that board.

**Dave Jones:** Like that. That is not a 1.6mm PCB because you wouldn't be able to bend a 1.6mm PCB that big like that. That's 0.8mm PCB. Why they've used a 0.8mm PCB? Why? Why? To give it a little bit of give when you push down on a key?

**Dave Jones:** I don't, unbelievable. Not a huge amount of stuff on here. Just some 4000 series CMOS. You want it to be at low power, of course. The main processor, 80C48, which was a common motherboard. Mask programmable. None of that flash or E-squared prom rubbish.

**Dave Jones:** It was a one-time programmable. Very common in the IBM keyboard. In fact, keyboards today still have the 80C48, don't they? I think so. Anyway, just some 4066s. Oh, I've got a 74HC03 in there. And there's not much else. We've got our infrared LEDs there.

**Dave Jones:** And yes, I've actually checked it because you can actually hold up any infrared remote control. Up to a video camera like I'm using at the moment. And it'll be able, the sensor in the video camera will be able to see the LEDs flash.

**Dave Jones:** And they don't flash. So, Houston, we have a problem. So, first thing, first, like visuals, of course, it looks okay. The caps aren't leaking. There's nothing else in there, really. So, we'll power it up with a lab power supply. We'll set that to 6V, 100mA current limit because, well, you know, it shouldn't draw more than 100mA.

**Dave Jones:** I'm pretty sure I've got that around the right way. Towards there. So, that looks correct. Looks like we've got some diode protection there. So, let's power that up and see what's what. That's good. It's only drawing 4mA. That's what you'd expect. Okay, I'm shorting some of those pads out.

**Dave Jones:** And I don't see the current changing. I would have expected the current to go up because it would have been driving the LEDs. So, and of course, first thing first, thou shall measure voltages. So, ground and power on our micro. 5.8V. Well, that's all right.

**Dave Jones:** This, because it's a CMOS version, it can go up to 6V. So, that's all right. And check to see that we've got a clock. Yep, 6MHz. No worries. All right. So, what I did is look for a schematic for this thing. Unfortunately, I can't find it.

**Dave Jones:** They do have an awesome technical reference manual for this. And they also have a hardware repair service manual as well. Unfortunately, that doesn't actually contain the schematics. But I did find something useful in the manual. It said when you plug in the keyboard, it actually disables the infrared transmitter.

**Dave Jones:** So, obviously, our processor's running, because this is not an oscillator. So, it's just a crystal. So, the oscillator needs to be running in the processor. So, it's running and it's doing something. So, when you plug it in, there's a signal apparently that disables the infrared, which would explain it.

**Dave Jones:** So, I'm just going to give this. A nice visual. I'm not going to do it on the screen here. I'll go look at it under the microscope just to see if there's any funny business. See if there's any pins shorted out inside there.

**Dave Jones:** I'm just probing the pins here. Found a 400kHz signal there. So, obviously, the chip is doing something. So, it's not like it's dead. I can get some pins to vary when I touch some of the pads. But apart from that, I'm getting zippity-doo-dah.

**Dave Jones:** If I short it out, we can get all the switchy bounce. No matter what I do, I can't get it to actually trigger the infrared LED output. So, I don't know what the deal is. And I'm getting no signal on the keyboard either, like any of the keyboard lines.

**Dave Jones:** Oop! That was just a staticky impulse. And we get this little wiggly signal here on the power rail. But if you see, we're one microsecond per division. Count the rough number of cycles in there. Ehh, there's six. Six megahertz. We've got a six megahertz

**Dave Jones:** crystal. That's just, yeah, like, lack of bypassing on the, uh, rail. So, nothing doing there. Okay, apart from the, uh, 400kHz on one of these pins, there is absolutely no activity on any other pin on that micro. I've checked every pin when I'm, like, activating

**Dave Jones:** a button like this. And, like, there's no scanning. There's no nothing. So, I've just got the clock. Six megahertz. clock. And a 400kHz, uh, signal on one of those pins. And, that's it. I'm gonna, I don't know, trace that 400kHz. See where it goes.

**Dave Jones:** And, of course, it went to the very last chip that I scanned. 'Cause you go around and you scan all the pins like this with power off, of course. And, I finally get across here. And, bingo. Got it. Last one. Bloody Murphy. And here's where your, uh,

**Dave Jones:** studio lights come in handy. You can see right through the board. 'Cause, uh, some of these, like, I can't see. I couldn't actually trace that, uh, 400kHz, uh, signal out of there. So, it went up here somewhere. Couldn't see it. And, I can't see where

**Dave Jones:** this pin goes. 'Cause it's on the top side. It buggers off under here somewhere. Well, that's interesting. I hooked the board back up, having a polka-doke. And, it's now drawing nothing. So, it was drawing four milliamps before. Now, it's drawing bugger all. Whaaat?

**Dave Jones:** Wow. This is interesting. Some sort of intermittent fault. Uh, we're getting five volts on our chippy, but we're getting nothing on our oscillator anymore. All that 400kHz signal. Of course, we're not gonna get the 400 if the main oscillator's not working. The oscillator's dead.

**Dave Jones:** The micro's getting five volts. Interesting. I just replaced the crystal with another six megahertz one. And, we're back up to four milliamps. And, it's, we're back to our oscillator. So, uh, dodgy intermittent crystal. But, that wouldn't explain why the keyboard's not working, though.

**Dave Jones:** Okay. So, we're back to it. Let's follow the money. This is this 400kHz signal, and we don't get any variation in that when we do the keys. So, if we follow the money, it actually goes down to, including the chip up here, goes down to this resistor

**Dave Jones:** pack here. So, it's a 104. And, on the other side, nothing. Hmmm. Let's trace where the other side goes to. I think it goes to this, uh, 74HCO3 here. But, why? You get a signal on one side of a 10k resistor, and not on the other.

**Dave Jones:** Maybe it's a pull-up. Aha! That's, I thought this was a through resistor like that, like individual ones. It's not, uh, 104 is 100k. And, sure enough, if we measure, I've powered it off. Measure across there, 200k, 200k like that, which means one of them's common.

**Dave Jones:** It's probably this one up here. Yep, 100k, 100k, yeah, 100k common. Okay, so that's just a pull-up. So, it's not going through a resistor to there. That's just a pull-up on that 400kHz line. That's okay. Okay, there was nothing wrong with that crystal, 'cause I turned this thing off and

**Dave Jones:** on, and I'm still, it's gone back, like, it's failed. Again. So, it's gone back. So, what I'm gonna do is just, I'm gonna look at my current sly, and just give that a bendy bend. Like that. Nah, my current just stays on zero.

**Dave Jones:** So, we've got an intermittent start-up. Geez, I hate these things. When you get intermittent problems like this, it just makes troubleshooting a real pain. Okay, so next thing I'm gonna do is trace the reset line of the micro, which is pin 4, and

**Dave Jones:** see if it's getting a reset. I got lucky this time. I was just dragging along there. And it's connected to pin 7 there, of this 4011. And then I trace that over, goes over to this via, which goes up to pin 1 of this 4013

**Dave Jones:** up here again. Geez. It's going everywhere, man. And it goes off to another pin. This 4013. So, 4013 is pretty important. Then you might think, oh, okay, there's some sort of RC thing happening, but there's nothing. Like, you scan over all the passives.

**Dave Jones:** Good thing about through-hole like this. And just scan across, and, like, there's nothing. So, there's no, like, RC uh, like, reset thing. At least, not directly. Right, so at this point, it starts to get a little bit ugly, without the, uh, schematic. You know, it's almost as if, like,

**Dave Jones:** you're starting to reverse-engineer this. Okay, the micro's not starting up. So you look at the reset pin. Where's the reset pin going? Oh, it's going over to a couple of chips, uh, pins over here of this gate. And so, without a schematic, you go, well, what do I

**Dave Jones:** do? You know, like, suck out the 4013 and, uh, test that? Get out an old-school IC tester. Geez, that'd be fun. And when you power it on, the reset line is permanently low, like that. So, there's something forcing that reset line low. And they're destroying NAF all, because it's

**Dave Jones:** in static condition. They're all CMOS. And maybe I should've traced this, but just for kicks, I, uh, sucked it out, and all the pins are bent over. So, you gotta, with your solder sucker gun, you've gotta sorta, like, bend 'em up, and then you gotta get in there, and

**Dave Jones:** you gotta just give 'em a little bit of wiggle, wiggle, wiggle, yeah, and, uh, should pop out. Nice. No pads lifted. No nothing. Beauty. Now, we can get an old-school IC. Well, it's not an old-school one, 'cause I actually designed an IC tester

**Dave Jones:** way back. We're talking 25 years ago or something. It doesn't work anymore, but, uh, I have one that does. Let's go. It's the upgraded one to that I originally had. It's the TL8662 Plus at zgecu.com. Anyway, um, it's got an IC tester built in.

**Dave Jones:** So, check this out. It's got logic ICs, and devices 4013, which is exactly what we have. Place it in the socket. I have. Let's press test. And test normal, test normal, test normal, oh, test normal. Wah, wah, wah, wah. Well, I ruled that out.

**Dave Jones:** Like, I don't know how comprehensively it tests it, but it knows that there's X gates in there, and I assume it exercises all options for all the stuff. So, yeah, um, um, okay. I'll tell you what, just for kicks, I decided to start this thing back

**Dave Jones:** up without the chip in there, and yes, it oscillates now. We're getting that, uh, 400 kilohertz that we were getting before, and I thought that I'd just probe the lead over here, and then just do the shorty short thing. We're actually getting trend, uh, packet transmission.

**Dave Jones:** There we go. Look, we're now sending data. We're sending data without the chip. Wow, look at that. Something's going on there. The signal level is just, that's the voltage drop of the, uh, lead there, the infrared lead, um, from the positive rail. Wow.

**Dave Jones:** I might actually see if the keyboard actually talks to the PC now. Like, I've removed the chip. This is hilarious. I, I, like, I thought it'd just start up. I just, just for kicks, I thought I'd do that. This is hilarious. Okay, I'm just going hacky-hack like this,

**Dave Jones:** and, uh, no, it doesn't seem to be doing anything, so, you know, like, the 4013 could have something to do with the encoding, of course. Alright, don't try this at home, kiddies, but what I'm going to do is put my meter in, uh,

**Dave Jones:** the microamp range, and I'm actually going to short out the reset pin. The chip's back in there now, soldered it back in. It, it, it doesn't work. We're back to our original, uh, configuration. It's drawing 4 milliamps, and, and, yeah, oh, no, geez, it just, it

**Dave Jones:** started drawing zero again. Ah, give me a break. Alright, it's working again. I just kept powering it up and mucking around with it until, uh, it drew 4 milliamps instead of, oh, it's dropped to zero again. I just bumped it. What's going on?

**Dave Jones:** Okay, I might have sussed it. If I hold a key down, uh, like short one out when I'm powering it up, it seems to come good. Anyway, I'm not going to worry about that now. What I want to do, okay, so I'm going to probe

**Dave Jones:** my lead here, and don't try this at home, kiddies, but I'm going to put my meter on, uh, current, uh, mode, so just, uh, microamps here, and I'm going to short out that reset line, because that reset line, pin 4 here, is currently

**Dave Jones:** low, so it's keeping the processor in reset, and if you read the datasheet, the oscillator does actually start up in that mode, so the oscillator is, uh, actually running, but it's obviously, but it can't execute its program, obviously. Okay, so what I'm going to do is hold that, uh,

**Dave Jones:** pin, the reset pin, I'm going to actually force it to the positive rail here, it's drawing an extra 6 milliamps on my power supply, sorry you can't see that, but, so we're forcing it to operate, and look! You saw that? We're now getting

**Dave Jones:** data on our scope. So now I've forced it out of reset mode, and it seems to be doing the business, working, sending the packets, so obviously, um, this thing is being held in reset mode, so we've got to figure out why it has

**Dave Jones:** to do with the 4013. It's flippity flop time. By the way, I've never heard of sync semiconductors wise componenties, um, what? Anyway, um, I've got no idea, is that like Spanish or something? I, sorry, I've got no idea. Anyway, never heard of them, it's

**Dave Jones:** just the first one that pulled up when I searched for PDF. Anyway, um, all I know is that, uh, the Q1 uh, output of the flippity flop here, uh, that goes to our uh, not reset line of our processor, that's what's staying low, so it

**Dave Jones:** needs to go high in order for this thing to work. And that's actually tied to pin 9, which is, uh, the second data pin of this flippity flop here. I haven't traced anything else. This is where the schematic, uh, would be, yeah, really quite

**Dave Jones:** handy. Anyway, we're gonna, uh, check our, see that our input's here. I'll just try and, uh, single shot capture some of these, like, uh, clock, for example, when we power it on. So this is our, uh, clock signal. This is when it was,

**Dave Jones:** uh, powering down, like this, so power's on, we, there's no extra clock in there, but, uh, we don't know, we haven't time correlated that against the power on. So, uh, yeah, we need to do that. This is where you need a two channel scope.

**Dave Jones:** Well, lucky I got one. So I traced out, uh, pin 3, the clock line there, it goes to Q4 of the 4060, which is down here, and that's a good old, uh, binary ripple counter here, and, uh, yeah, so that's a Q4 output.

**Dave Jones:** Aha! Is, so obviously, this is maybe some power on delay or something, uh, for the reset that they're doing, so I'm gonna now focus on the 4060, I'm not gonna bother, uh, checking the rest of this anymore, if we're not getting a clock

**Dave Jones:** in there, which is, uh, the, well, there's two ways to change your output here, your reset, you can use your set and your reset pin, but what's the point? Anyway, so, but the fact that the clock goes off to this ripple counter tells me that this ripple

**Dave Jones:** counter's important, probably some power on timer or something else that, um, is, is not working, so, meh. So it's just a quick check of the cap down in there, it's gonna be that smaller one, not the yellow one, that'll be the bypass. 10 nanofarads, alright.

**Dave Jones:** Gonna measure those two resistors in there as well, they're, uh, bang on, as close, bang on as they will be, uh, in circuit, so that's not a problem, 10 nanofarads sounds about right, uh, um, yeah. Okay, so the 4060 is a, uh, binary ripple counter, of

**Dave Jones:** course, doesn't have, uh, none of that, uh, Q0 to Q2 rubbish, don't need that, and, uh, it basically, you can hook up an external crystal or an RC, um, typically, and in this case, an RC oscillator on here, but the master reset pin will disable that.

**Dave Jones:** I've checked, uh, pin 9 for any oscillation, there is no oscillation, I've checked pin 12, what do you know? It's high. So, it's an active high input, so this thing ain't working, no wonder that no oscillation, that means no clock on Q5, which means no

**Dave Jones:** flippy, floppy action over here to change your reset, to toggle your reset pin. Aha! What's happening to the reset here? Okay, I've done a little bit more tracing here, and this, uh, reset pin, it goes off to this, uh, NAND gate here, the 4011,

**Dave Jones:** that's a baby next to it there, and this bugger's off, I goofed at the first time, um, this goes through a cap and a resistor over to the keyboard connector over here, so you remember how we had, uh, mentioned before how it had some sort of plug-in

**Dave Jones:** detection, and disabled the, uh, the LEDs on here? Well, I think there might be some plug-in contact in there, so you have a look inside there, focus you bastard, there's those little lever things in there, maybe one of those is not making contact when it should.

**Dave Jones:** Hmm, when it's not plugged in. Worth a shot. I think we're getting somewhere, 'cause this bugger's off to an internal switch, a plug-in switch inside the keyboard connector, which goes up to plus 5 volts, so watch this, this is the connector on the side of the pin there,

**Dave Jones:** so there you go, we're getting our 5 volts, sorry it's hard to see that, but that's basically on the output side, of the, that RC there, if I get in there and I disconnect that, like I'm plugging in the connector, boom, it goes to 0, and then

**Dave Jones:** it goes to 5. It's got a little, uh, lever switch in there that detects the, uh, plug-in. But that seems to be working, actually. Alright, something's going on here, if I look at pin 1, let's measure the voltage on pin 1 here. 2.2 volts.

**Dave Jones:** Wah, wah, wah, wah, that's smack in the undefined region, of the CMOS gate. No wonder the output's, uh, gonna be doing silly buggers. Well, the output's high, which is forcing our, uh, reset, and what's pin 2 doing? Pin 2 is high as well,

**Dave Jones:** so it should be low, so they're both, yeah, something's wrong there. There you go, well, that's supposed to be a 2.2 mic, um, that's just a little, uh, one of those, uh, bugger tantalums, um, but it measures okay. Yeah, confirmed, that's okay. Something else.

**Dave Jones:** And hold onto your hats, because I've, uh, left that capacitor out, I've re-powered it up to, uh, have a play around with it, and, you're gonna have to see my power supply for this, I haven't, uh, used the scope to look at anything, but it's

**Dave Jones:** drawing no current at the moment, but, if I short out a key, bingo! It draws naff all, like microamps, that's probably until you press a key, maybe that's what you'd expect, so all along, four milliamps, we could have been coming to gutter. Anyway,

**Dave Jones:** I think she's working now. Okay, so what I care about now, let's just turn it on, and Bob's your uncle. Now we're transmitting. So, yeah, I could go into the intricacies of how or why, I mean, this cap seems to be okay, um, I don't think it's leakage is

**Dave Jones:** a, uh, an issue, but, um, anyway, well, it could be. Oh, no, no, look, it sort of, like, stays on. Five. Well, and then it drops back down, but maybe that's, it could be some power down state or something. There you go, it's actually drawing, uh,

**Dave Jones:** 65 microamps there, which is, that's kind of what you'd expect for a keyboard, isn't it? Four, I should have tweaked to that. People are probably screaming at me, "Yeah, four milliamps, that's a lot!" You know, double A's, but still, you know, it would have been sucking the juice.

**Dave Jones:** We'll put it in, uh, max mode, in 50 milliamp range there, so it's peaking at about eight odd milliamps there to drive the LEDs. Winner, winner, chicken dinner, it works! Our wireless keyboard! With no cap. It may not actually be the cap, maybe something else,

**Dave Jones:** but the cap is making it work. So, via that, uh, silly plug-in, uh, keyboard switch thing. Hang on, the story's not over yet. Take, take a look at this. This is our reset pin. It's still low. But, when we touch a key, it wakes up.

**Dave Jones:** Go down, can I get it to stay on? Can I get it to latch on? Sometimes I can get it, there we go, it's latched on. And 5.7 volts, so it's high, and then, whoop, goes, and it goes low. Hmm. Brown, black, green, you all know

**Dave Jones:** what that is. High value, jobby. And, look, those two pins are shorted. This is where I've removed the cap from. There's nothing, look, over this side here, they're not connected to anywhere. Yet, if I measure that resistor, wow, what? 170k? What the? Well, I found it remarkable,

**Dave Jones:** and a one meg carbon film resistor could fail, and sure enough, it hasn't. Have I missed a trace on the PCB? Oh, yeah, look at that. You can easily come agut, so I couldn't see it under the resistor. Right angle trace. Look at that.

**Dave Jones:** It was hidden by the resistor. Mungrel. Okay, I've just soldered in a ceramic jobby over here. It's not 2.2, but it's near enough. Good enough for a stray. It doesn't have to be that, and we're getting our thing again. This seems to be like, I think if you do

**Dave Jones:** the keys quick, it sort of like latches on like that. I think there's something wrong with that cap. Even though it measures okay, it could be some voltage dependency issue on there. And yep, there we have it at 6 volts. Got 150 microamps

**Dave Jones:** leakage, so combine that with our one mega resistor, and you're gonna come agutzer, and that's why we're getting that mid-rail voltage that we were seeing. So, leaky tantalum. Doesn't have to be much, but when you combine it with that, it's just the design

**Dave Jones:** of having that one mega resistor down in there, it's come agutzer. There you go. Now it's jumped up to 190. It's all over the shop actually. If I change the voltage, is there a point where it drops to naff all? Nah. Leaky bloody tantalum.

**Dave Jones:** Unbelievable. Well, it's not. They're notorious for it. So there you have it. Winner, winner. Chicken dinner. It was a little tantalum. Not one of those tag tans, one of those axial tantalums, that a leaky tantalum. And when you look back on it, even without the complete

**Dave Jones:** schematic, little bit of reverse engineering we did, is that it was, yeah, that would explain it. A leaky tan in there was causing a non-valid logic level in here. This was probably oscillating, doing all sorts of funny things, and that went to the

**Dave Jones:** reset, which buggered everything up. So that explains why I was seeing those, like, it'd sometimes be drawing 4 milliamps, that was probably due to the oscillation or something like that, doing something weird, and then it'd, when it went into zero, um, maybe when it actually went to zero, it would've

**Dave Jones:** worked if I happened to have tested it at that exact point. But it's like, it's just all over the shop. So that explained all the intermittent operation, and how we chased a red herring down a rabbit hole there a bit, you know, it seems this is what's

**Dave Jones:** this video, like 30 minutes or something, it seemed like a long time doing this, and it might be, there's some things in here that I wouldn't have done, I was just doing it for the sake of the video, like sucking out the chip, and just wanted to use the IC tester

**Dave Jones:** and show you that, you know, like, it's not something I would've ordinarily done, and you could've said, oh, if you reverse-engineered it from the get-go, it would've been a little bit quicker, maybe, but all up, like, if I wasn't shooting a video for this, it's not a

**Dave Jones:** really long repair, yeah, it was a pain in the butt, to get to that point, you had to go through most of those processes I went through, unless you got lucky in some other way, to track that down to the axial tent on there, and some people might've

**Dave Jones:** gone, oh yeah, I would've replaced the axial tent from the get-go, okay, well, you know, we were methodically going through testing everything, but that was an absolute classic, I hope you enjoyed that as much as I did, I love it when I get faults like this, that take some

**Dave Jones:** time to track down, and they come down to, you know, that cap, if you test it on your meter, or your LCR meter, it measures fine, but it's actually leaky, and that might not ordinarily be a problem, this cap could still work in many, many other circuits, but when you combine

**Dave Jones:** it with the one meg resistor in there, you're gonna come a gutter, so, oh, look, yeah, it's just, it's all over the shop, that's hopeless, anyway, that was fascinating, so I hope you really enjoyed that, love it when I get repairs like that, it's not very

**Dave Jones:** often, if you did enjoy it, please give it a big thumbs up, and as always, discuss down below, catch you next time, oh, and by the way, this repair came about because I was actually trying another thing, which involves this monitor over here, so I was in the middle of

**Dave Jones:** shooting that video, I was most of the way through it, and I wanted to get this PCjr working, I thought oh, I wanna get the keyboard working, and so I had a go at that, and one thing led to another, so this video

**Dave Jones:** comes out first, catch you next time. Subtitles by the Amara.org community
