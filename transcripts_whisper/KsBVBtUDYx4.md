---
video_id: KsBVBtUDYx4
title: Alesis M1 Active 520USB Studio Monitor Teardown
url: https://www.youtube.com/watch?v=KsBVBtUDYx4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 19, "2": 37, "3": 52, "4": 70, "5": 88, "6": 103, "7": 121, "8": 133, "9": 154, "10": 172, "11": 196, "12": 214, "13": 229, "14": 250, "15": 268, "16": 292, "17": 310, "18": 331, "19": 352, "20": 367, "21": 382, "22": 397, "23": 415, "24": 430, "25": 457, "26": 475, "27": 490, "28": 508, "29": 523, "30": 544, "31": 562}
---

**Dave Jones:** Hi, I thought we'd take a look at my Alesis M1 Active 520 USB studio monitor speaker. These are the speakers that I use for all of my video editing, have done for many years now. And I like it, not only because they are small and compact, the 520

**Dave Jones:** means it's a 5-inch main driver here. But I like it for the fact that I can use it as a 5-inch main driver. But I like it for the fact that A, it's got the volume and power switch on the front, and I'm always using this and

**Dave Jones:** I don't have to dick around with like the software or an external box or anything like that. It's got the headphones on the front which I use for podcasting and it's USB, as the name says. It's actually a USB interface as well which is handy.

**Dave Jones:** It just means that there's, you know, one less box on my bench, I don't need an external DAC or to use the crappy sound card inside the computer. So I rather like these. There's not too many like USB monitor speakers on the market, and they don't make this one anymore.

**Dave Jones:** They do make the 320 USB which is a 3-inch driver version. But anyway, and I do like the fact that it uses nice beefy XLR connectors for the to go to the other speaker. All of the driver is inside this one. The other one is just a speaker, it's got bass boost

**Dave Jones:** and a rear port on the thing. And also, tonally, I really like these because I do video editing where like speech is everything. Like I don't have any music, I don't do any music editing or anything like that. And apparently the crossover in these

**Dave Jones:** has been designed to avoid the mid-range of the voice. So they're potentially a bit better than some others on the market in terms of voice reproduction and stuff like that. Anyway, I think they're a cool little monitor speaker. And as is typical for these studio monitor speakers,

**Dave Jones:** they're screwed in around here into the MDF cabinet. Shouldn't have to take off any of the inner ones, that's just holding like the power amp, PCB, and the heat sink and all that sort of jazz in there. And the various input connectors. So, whoop, there we go.

**Dave Jones:** We are we're in like Flynn. They just leave enough room to swing it out. Oh, barely. And we can see the damper material inside here, very common. 4 ohm 30 watt driver, I'm not sure if Alesis actually make them or not, or whether it's where they get them from, no idea.

**Dave Jones:** And the tweeter at the top, let's get all the cables out. Looks like they've got some connectors on them, hopefully we can just disconnect them. Actually, this all looks rather nice. Look at this, nice shielded transformer here. Nice mains connection, mains earth connection

**Dave Jones:** down there. We've got the rubber sealing vibration mat under, yep, underneath the transformer. Very nice cable tying on all the mains stuff there. We've got the hot snot sealing right around there. We've got all the heat shrink around there, fantastic. So acoustically, sealed very well, and of course it's got the seal material

**Dave Jones:** around the outside which presses against the rear case because these monitor speakers, you want them to be completely sealed and then all of the engineering goes into designing well, the enclosure shape, but also the tuned port on the back or front or wherever it happens

**Dave Jones:** to be. You can see the Loctite type stuff just sealing all the connectors in there so they don't vibrate off. Very nice. So that came off easily, now you can see all the filler material inside here. Let's take a look at the tweeter up in there.

**Dave Jones:** 5 ohm 15 watt job, soldered directly on. Everything's looking just fine and dandy. Check it out, they've actually done really well. Look at this huge foam block propping this board up. I'm not entirely sure why they've done that but to get that height, I'm not sure why

**Dave Jones:** they need... oh, that much, okay, they need that much height, yep, due to the connectors at the back. Okay. So yeah, their direct PCB mount very nice. So yeah, they've put a custom block in there, not only for the sealing of course but to, as a standoff for that board.

**Dave Jones:** And that board looks pretty jazzy, better than the Rokits, or Rockets as they're apparently supposed to be called. I just call them Rokits. And double-sided load there, and that looks alright. That looks pretty decent no soldering and no black gunk of death like in the Rokits.

**Dave Jones:** I would presume they're just all various op-amps and whatnot. And I like how the boards are right-angle fillet soldered like that. I use that method quite a lot myself. And all those chips are all JRC Japan Radio Corp. They practically own the market for audio op-amps, I think.

**Dave Jones:** Are they just like cheap, or are they half-decent? I don't know, but they're everywhere. And that's quite a decent heatsink block there. Look at the thickness on that puppy. Wow. Uh-oh, caps. Not exactly Panasonics. Not sure if you can see that, but that's a TDA

**Dave Jones:** 7265, which is a dual-channel stereo 25-watt plus 25-watt amplifier. And this is a bit interesting. It's interesting because this is a nominal 30-watt driver, and they're only using they're not actually paralleling those channels to drive it. And here's why. Because if you have a look here

**Dave Jones:** they've got two bridge rectifiers here. They're going to have one for the woofer and one for the tweeter here. Different level of caps. Look, we've got the smaller caps there, that'll be for the tweeter. The reason they have two of them is because we've got two different channels

**Dave Jones:** there. Because you've got to remember, this is not a single channel unit. This amplifier board here actually drives the other speaker as well. The other speaker doesn't contain any of this circuitry at all. You've just got the port and the filler material and the speakers.

**Dave Jones:** Although it does actually claim 30 watts per speaker, which matches up with the 30-watt rating on the main woofer over here. But that's like per speaker, it doesn't actually break that down into like 30 watts plus 15 watts for example for the tweeter.

**Dave Jones:** So whether or not that's total power, that would make sense. But if they are if it is actually capable of doing 30 watts then you've only got a 25-watt amplifier on there. And they use the same TDA chip for both channels. They're reusing their bill of materials there

**Dave Jones:** and why not? You know, it probably doesn't cost a huge amount extra and just saves on the bomb and everything else. So, and that TDA driver chip at 25 watts, because it's not capable of 30. At 25, it's actually normally 10% distortion too.

**Dave Jones:** So like, they're really, like, underpowered. The amplifier. In theory anyway. Aha! Closer inspection of the data sheet. The good old music power output spec with the asterisk next to it. That's rated for 32 watts, so meh. Okay. And as is common in all this sort of gear, single-sided

**Dave Jones:** board. It looks like it's double-sided there but that's not. That's actually just the traces on the bottom side just showing through. It's actually a single-sided board. Got quite a few like a whole unpopulated section here, so I'm not sure what that's for. Probably some additional feature or model

**Dave Jones:** or something like that, but I thought there was only the standard one and the USB one. Hmm. And there's our USB input board down there. You can see it's all like gunked around there to seal that up, so none of the air escapes, and probably uses

**Dave Jones:** I don't know, some Cirrus Logic USB to audio chipset, you know, one of those generic ones. I like the fact though that they've added this shielding board between the mains wiring here. Look! They've actually earthed that. That's a nice attention to detail. I like that.

**Dave Jones:** Now they do actually have some gunk on the board here, and right up in there, I'm not sure next to the connector there, that's to keep the connector in place, but I'm not measuring any problems on that at all. So there's nothing wrong

**Dave Jones:** with using gunk on your board as long as it doesn't become hydroscopic and conduct like they did in the Rokit ones. Anyway, I am generally very impressed by the build quality in these Alesis monitors there. It's ahead of the Rokit slash Rokit ones.

**Dave Jones:** Definitely. Even ignoring the black gunk of death, the build quality's just... it's better. The Rokits were okay, but they were good, but these are... I think these are a step above. There you go for all you driver aficionados. No idea who manufactures that

**Dave Jones:** at all, but you know, it's nothing special. . .
