---
video_id: p-eLu1z7-cs
title: Rigol HDO1000 Serial Boot Capture for Hack + R&S MXO4 play
url: https://www.youtube.com/watch?v=p-eLu1z7-cs
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 22, "3": 45, "4": 59, "5": 76, "6": 88, "7": 100, "8": 115, "9": 130, "10": 143, "11": 151, "12": 166, "13": 179, "14": 190, "15": 201, "16": 210, "17": 229, "18": 239, "19": 254, "20": 271, "21": 282, "22": 295, "23": 304, "24": 314, "25": 328, "26": 336, "27": 355, "28": 365, "29": 381, "30": 396, "31": 409, "32": 419, "33": 435, "34": 444, "35": 455, "36": 470, "37": 488, "38": 499, "39": 512, "40": 526, "41": 534, "42": 547, "43": 557, "44": 569, "45": 588, "46": 598, "47": 609, "48": 623, "49": 637, "50": 659, "51": 675, "52": 684, "53": 697, "54": 715, "55": 724, "56": 737, "57": 750, "58": 777, "59": 785, "60": 800, "61": 818, "62": 828, "63": 839, "64": 852, "65": 865, "66": 878, "67": 884, "68": 894, "69": 920, "70": 931, "71": 944, "72": 954, "73": 964, "74": 975, "75": 986, "76": 999, "77": 1013, "78": 1025, "79": 1045, "80": 1058, "81": 1074, "82": 1083, "83": 1095, "84": 1101, "85": 1116}
---

**Dave Jones:** Hi, just a quick uh second channel video. I'm going to see if I can get a UART uh boot debug output from this uh new Rigol HDO1000 uh series scope, which is identical to the HDO4000 uh series.

**Dave Jones:** Um I haven't released that video yet, but I'm sure this these two videos are probably coming out the same time. So, what we need to do is find a debug header on this thing.

**Dave Jones:** Now, just some uh general advice, of course, if you see a header like that, obviously, um yeah, we've got this jobby up here, but that is almost certainly an FPGA header because you can tell by the uh number of pins, and you can see if you you follow the money, the traces down there, it's going over like it's near the FPGA.

**Dave Jones:** So, you can pretty much uh be safely assured that that is a JTAG uh pinout for the FPGA. And we don't want that. We actually want the uh debug uh header for the processor cuz this um runs a uh what is it?

**Dave Jones:** Android. Yeah, I think it's a Android operating system. So, there should be like a serial uh debug output here. Um and sure enough, if you've seen the teardown, so you look around for a what looks like a pin header, and sure enough, there's a four-pin header there here.

**Dave Jones:** There is no standard, and unlike uh JTAG type stuff, which often has uh standard, sometimes they're, you know, custom, but often they are a standard interface, but serial, you probably won't find a standard uh interface for that.

**Dave Jones:** Um so, yeah, we've got four pins here. So, my guess is uh there'll be transmit, receive, ground, and maybe power or something to power a uh thing. So, okay, let's actually probe that.

**Dave Jones:** So, we'll get the meter, and we'll see what's what here. So, let's go ohms-y. So, uh the ground I want to almost certainly, okay, it'll be logic ground, and logic ground will be connected to the metal shudgy ground in here.

**Dave Jones:** But because I've got pro tip, because I've got uh the mains input is connected to this metal up here, and this metal is not screwed into this metal, there's no earth wire that comes over here, and you don't want to rely In fact, let's measure it actually.

**Dave Jones:** I will disconnect. Haven't actually done this. Helps if I had the multimeter in shot. Measure between there and there. And it is. Oh, scope probe. Scope probe. Trap for young players.

**Dave Jones:** Yeah, I physically had it was going through there. Let's check that Let's recheck that now. No, there we go. So, there's no physical connection connecting those two ground points.

**Dave Jones:** So, scope's still going to work. Could be noisy or whatever, but you know, it it it doesn't matter anyway. So, what what I've done is actually connect just a shorting clip from here down to here just to join the two, okay?

**Dave Jones:** So, now we can safely measure that. No worries. And we can connect our scope probe up to the metal chassis here, okay? Ground it. Now, we'll have a look for Now, we'll probe the pins.

**Dave Jones:** That's pin one. Nope. No 32 ohms, okay? So, that's some sort of driver. Oh, no. See, the multimeter is oscillating there. That means it's some sort of active driver.

**Dave Jones:** It could be giving out some sort of pulse signal already. There could be some serial output there that's doing Generally, you can probe. It's not a problem. Like you can use your multimeter ohms range.

**Dave Jones:** The current is incredibly low, so you're not going to damage any active circuitry or anything like that. A lot of multimeters back in the old days I've done a video on this, haven't I?

**Dave Jones:** Used to have a low ohms function. And what that meant is not It's not measuring low ohms. It actually puts a low output compliance burden voltage on there of a maximum that's under the .6 volt diode drop, so it wouldn't turn on any junction, so you could measure like stuff in circuitry better, and it wouldn't turn on any active diodes or anything.

**Dave Jones:** It's got nothing to do with damaging, really. A uh a multimeter is not going to um output enough current. So, yeah, anyway, so that that could be oscillating. So, then we'll check that one.

**Dave Jones:** There you go, bingo, found it. There you go. So, pin three there is ground, and what's pin four here? Once again, that's oscillating, so let's put that over to volts here.

**Dave Jones:** And let's measure pin four again. 3 volts. There you go. It's not 3.3, it's 3. Okay, let's measure the others. Three. So, looks like three. Okay, so 3 volts might actually be the supply rail for this thing instead of 3.3.

**Dave Jones:** That's interesting. So, anyway, pin three is ground. We don't have to actually connect it through like actually ground onto that pin. You can just keep it on the chassis here, no worries.

**Dave Jones:** We don't care about signal integrity. So, I'm going to put that on pin number one. Got to start somewhere. Yes, the probe does actually fit in here. Just be careful if you leave it hanging like that, and you accidentally hit it, you can break your probe tip, and that will ruin your day.

**Dave Jones:** Oh, yeah, I'm feeling lucky. Feeling lucky, punk? Yeah, I am. Okay, so let's actually boot this up. Going to be using the new Rohde & Schwarz. Look at this bad boy.

**Dave Jones:** This is the baddest ass scope I've got in the lab here. I've already shot a little bit of footage with it, but this is the new MXO 4 MXO 4 series.

**Dave Jones:** This is the MXO 44 1.5 gig 12-bit ADC. This is got some absolute killer specs. So, anyway, I just wanted to play with it. So, let's let's play with it.

**Dave Jones:** Um a couple of annoying things, actually. Let me show you. So, there's our 3.6 volt signal. That's actually very clean. What if I I might be able to make that dirty.

**Dave Jones:** Let's Let's be dirty buggers, okay? So, what I'm going to do is I'm actually going to move my ground probe from here. I'm going to move it up to here, my ground clip, that means we've got a massive big long like antenna ground lead that goes all the way down here and back.

**Dave Jones:** Will that change our noise? Yeah. Yeah, there you go. Our signal's much noisier now. You can see that in there. Can I adjust the How do I adjust the multi-use?

**Dave Jones:** Does that How do I adjust the variable intensity? Ah, there we go. I've got to push that there. Yep. There you go. So, yeah, that is much noisier. But, that's neither here nor there when you're measuring like just you want like a 3-V TTL signal like this.

**Dave Jones:** So, you can see we're getting a high signal there. Nothing's oscillating. Let's go to pin number two. I've got a very slow time base here. What 1 meg points of memory, so yeah, it's No, it's 3-V and the other one pin four, nope.

**Dave Jones:** Okay, so let's leave it on pin number one. And let's do a boot on pin number one. First of all, I've got to set to normal mode. I've got my trigger set to positive edge trigger.

**Dave Jones:** So, normal mode, positive edge trigger, single shot acquisition. Oh, I forgot to show you the annoying things. Front end like this, okay? I wanted to set a Times 10 probe.

**Dave Jones:** This is the first time I've tried to do it. Where is the Times 10? Right? It's It's not here. And I'm using a switchable 10:1 probe that doesn't have the pin on it cuz obviously we can actually get the auto probe detection down here.

**Dave Jones:** But, it hasn't got it. So, like I'd expect when I call up my menu for the vertical channel, I want my like terminations in there, 1 meg, 50 ohm.

**Dave Jones:** Great. Okay, but where is like I just want 10:1. Like I Where's my probe attenuation? Okay, sure enough. Okay, I can go into probe menu, but there's no simple times 1 times 10.

**Dave Jones:** Okay? It's like it has like this user-defined thing, right? It's got user-defined. It's got all the other probes, which is absolutely great, right? If you're using active probes and current probes and all sorts of stuff, it'll set up for you.

**Dave Jones:** Fantastic, right? But, I've got to select like user-defined, and then what like where like manual attenuation 1 V per volt, okay? So, now I've got to go to 10 V per volt, or is it like point 1 V per volt?

**Dave Jones:** Which one is it? You've got to like you've got to actually think about it, right? I No. Give me times one, times 10. Like where is that? I don't understand why it's not there in that format.

**Dave Jones:** Like And then, if you set it there, it doesn't actually tell you what it is down there. It just says user-defined. Anyway, that's enough quibbling with my minor things.

**Dave Jones:** Let's put single shot capture. Well, let's turn the scope off first. Double-click of the soft power button does that. Okay, I've got positive edge trigger. I've got a slowish time base 40 ms per division.

**Dave Jones:** Yes, it is 1 2 This is weird. Actually, this one does 1 2 4 and 5 sequence. 1 2 4 5. It doesn't do 1 2 4 and then 1.

**Dave Jones:** It does doesn't do 1 2 5 and then 1 does 1 2 4 and you get the extra 5. That's probably like to optimize the you know, the dynamic range and the amount of memory and stuff like that.

**Dave Jones:** Anyway, just thought that's interesting. So, let's turn it on. See if we get So, this is pin number one. Oh, yeah, we got something. But, there's no data packet.

**Dave Jones:** I don't see any data packet in there. So, it it could actually come later. Can't turn it off until it's booted. There we go. Relay's clicked. Okay, so let's try this.

**Dave Jones:** I've got channel number one. Let's turn it off like that. Single shot trigger again, slowish time base. I've got yeah, 40 milliseconds per division. Negative edge trigger cuz otherwise if we do positive edge trigger, we'll get it as soon as it powers up cuz we saw that the default state before was high.

**Dave Jones:** So, let's try it. Yeah, and a trigger level about in the middle, you know, 1 and 1/2 volts. Nothing. It's gone high and it's not going low again unless I've goofed my trigger.

**Dave Jones:** I don't think so. Nope, there we go. That was just it looks like that was just contact bounce there. Let's try it again. Just turn my intensity up there so you can see it.

**Dave Jones:** Okay, so this is number two. That's channel two. Could be some data in there. Okay, so single shot. Negative edge trigger. Pin two. Did I say channel two? Aha, bingo.

**Dave Jones:** There you go. That is a data data packet. That is a data packet. There you go. So, we can Well, there's something something on power on. Okay, so I've definitely got something on power on.

**Dave Jones:** Yeah. Yeah, there we go. Yep. Oh, what's Oh, what's going on there? Check Check that out. Look. What? It's like that and then it's like that. It's Oh, that's doing That's the sine x on x.

**Dave Jones:** Is it? What's going on there? That's interesting That's an interesting quirk. That's got to be a quirk. Check it out. Yeah, look. That looks absolutely fine. That's it So, I'm one one meg points memory.

**Dave Jones:** Okay. And then boom, it goes like that. So, it's hiding. Maybe all that's there, you know, cuz our signal integrity is like really poor here. Okay, it's not great, right?

**Dave Jones:** So, I expect kind of rubbish, but why does it take it away at the shorter time base like that. That's interesting. Anyway, we definitely have serial stuff here, okay?

**Dave Jones:** So, no lockers like and zoom in there and that'll do the same thing. Yep. Okay. So, I definitely got a serial pin, okay? So, let's go back. Aha! That was I was just probing pin number four and that is a decay like that.

**Dave Jones:** So, I think pin number four is a power rail. When when you see like a decay like that, that's not like a logic output going low. That's like a classic power rail going low.

**Dave Jones:** So, yeah. No worries. Over 5 milliseconds, something like that. Yep. Okay. Same time base we had before, 40 milliseconds per division. Pin number four. Yeah, we're getting no negative edge at all.

**Dave Jones:** So, yep, that's just no negative edge trigger. That mean if we do it again, if we if we trigger it on positive edge, you'll see it go up. So, yeah, I think pin number five is a rail there and you could try and probe that out to another 3-V rail to confirm that.

**Dave Jones:** So, there you go. Pin number two is transmit and pin number one is receive. Pin number three is ground. Pin number four is looks like 3-V power. Okay, unfortunately, due to a very serious lock up I had on the MXO 44, which I have not been able to figure out.

**Dave Jones:** I've put that on my second channel, but I haven't released yet. I've sent it to Rohde & Schwarz to see what happened. I had some serious issues there. So, I've had to get another scope out.

**Dave Jones:** So, I got my Keysight 3000 cuz I knew this is going to be a high board rate. So, I knew this could actually capture the board rate. And if we get the cursors up here, you can see that we're talking about 660 nanoseconds there.

**Dave Jones:** You invert that on a calculator, that's about 1.5 meg board rate. Megabits per second, basically. Meg So, if we turn curses off um and we go into the serial uh decoder here, I can actually manually set a user-defined uh board rate here.

**Dave Jones:** You can actually go up to um what is it? Hang on. I can actually go up to eight 8 megboard there. There you go. So, we can actually go down to 100 bits per second.

**Dave Jones:** No. Let's go to 1.5 meg and uh come on. I can type it in direct. But, the Keysight has the best velocity control, by the way, of any scope.

**Dave Jones:** Let's set it to 1.5, which is like a really high. I've never encountered one this high before. Leave it in the comments. Um you know, like there are special cases, but like if for a just a um like product like this, yeah.

**Dave Jones:** Um haven't really seen it before. And I've already uh captured that at 1.5 megboard. I could do it again, but there you go. We got it. We got it.

**Dave Jones:** We actually got some legible text. DDRS and then version once you see, you know, like actual ASCII text like that, you know you've got something. Version 1.6 1.26 and so on, okay?

**Dave Jones:** So, and then we can look at our table up here. I don't know why my table has vanished now. I had I had it all up in my table before.

**Dave Jones:** Maybe I have to uh sample again. Anyway, let's actually actually I'll do that. I'll capture that again. So, leave it at that time base. Capture. Boom. Got it. There you go.

**Dave Jones:** And it's in my list there and I can scroll through my list there. So, I carriage return line feed, blah blah blah. So, 1.5 megboard. Unfortunately, and I just checked and both of the uh term PC terminal programs that I use for capturing boot data like this, both Termite and uh Tera Term, they neither of them support that higher board rate.

**Dave Jones:** They don't go over 250 uh 6K baud. So, yeah, I it can't do 1.5 meg. So, I'm going to have to look at some of my other PC-based scope options.

**Dave Jones:** We're just not going to be able to get it here. I don't I I don't know if Well, the Keysight wouldn't have the memory to dump it because this it's like a 1-minute boot period or something for this scope to boot or 30 seconds or whatever it is to boot and it's constantly putting out data.

**Dave Jones:** So, we want to capture the whole lot. So, yeah, we can capture a little bit like this, but I want to capture the entire boot log over the whole 30-second or whatever boot period.

**Dave Jones:** So, to do that, you need a a basically a you know, infinite memory like a you know, like a PC actually capturing and dumping it into a text window.

**Dave Jones:** And I'd like to use my Rohde & Schwarz RTB 2000 to do it. I like it's serial decoding. Unfortunately, it only goes to a maximum of 1 megabit per second.

**Dave Jones:** So, we can't do our predefined. Actually, can it go higher? User? Can Can it go higher than that? Never tried it. 1.5 meg. Oh, yeah, it can. Look at that.

**Dave Jones:** Okay, let's try it. Ha, I can capture that, but it's being smart down there and it's tell me telling me that it's aliasing. So, oops. I don't know why it told me that.

**Dave Jones:** Anyway, it's working just fine. And just a zoom into a random party here MR24 = 0x8c l something like that. So, don't know what any of that means, but it's captured it anyway.

**Dave Jones:** 1.5 megabits per second, which is really annoying. So, I've got to go and find a PC-based solution for that so I can dump it to a text file so then I can upload it to the forums.

**Dave Jones:** All the nerds can start working on the hack. So, we're over here on the workbench and I've got my Saleae Logic hooked up. I was using my serial UART decoder, but as I said, that's only like slow board rates, like a couple hundred K maximum, but I was able to use the Saleae Logic software and it does actually have Check it out.

**Dave Jones:** Does actually have a data terminal mode and I set it to 12 meg sample per second and 1.5 megabits per second. I entered that manually and bingo, we got it.

**Dave Jones:** There you go. Here's the boot. DDR version 1.26 in channel zero. So, this is the whole lot here. I will actually post it on the Oh, it tells you the DDR4 memory speed.

**Dave Jones:** There you go. Um so, yeah, I'll post this. I'll dump this over on the EV blog forum. I assume I can download this. There it looks like there's a download button there.

**Dave Jones:** I've never actually used this terminal mode before. It's really cool. So, I like it. There you go. So, and then you've just got all of these zeros and that's it for the entire boot sequence.

**Dave Jones:** I think I got I just And then I shut it down right at the end and it didn't add anything. Didn't have any shutdown data or anything like that.

**Dave Jones:** So, there it is. Um yeah, see, this is where you need a specific solution that can actually handle this this high board rate and let's see if I can actually dump that.

**Dave Jones:** No. What was that? No, that was just go to the bottom. Oh. I can highlight it. I can copy and paste, I'm sure.
