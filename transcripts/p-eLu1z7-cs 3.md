---
video_id: p-eLu1z7-cs
title: Rigol HDO1000 Serial Boot Capture for Hack + R&S MXO4 play
url: https://www.youtube.com/watch?v=p-eLu1z7-cs
source: youtube-asr
timestamps: {"0": 0, "1": 30, "2": 61, "3": 92, "4": 124, "5": 137, "6": 168, "7": 187, "8": 212, "9": 233, "10": 249, "11": 283, "12": 300, "13": 329, "14": 344, "15": 359, "16": 372, "17": 386, "18": 402, "19": 435, "20": 467, "21": 496, "22": 526, "23": 553, "24": 572, "25": 588, "26": 602, "27": 618, "28": 640, "29": 662, "30": 680, "31": 692, "32": 727, "33": 756, "34": 768, "35": 795, "36": 830, "37": 847, "38": 863, "39": 892, "40": 929, "41": 952, "42": 977, "43": 995, "44": 1018, "45": 1045, "46": 1074, "47": 1101, "48": 1120}
---

**Dave Jones:** Hi, just a quick uh second channel video. I'm going to see if I can get a UART uh boot debug output from this uh new Rigol HDO1000 uh series scope, which is identical to the HDO4000 uh series. Um I haven't released that video yet, but I'm sure this these two videos are probably coming out the same time. So, what we need to do is find a debug header on this thing. Now, just some uh general advice, of course, if you see a header like that, obviously,

**Dave Jones:** um yeah, we've got this jobby up here, but that is almost certainly an FPGA header because you can tell by the uh number of pins, and you can see if you you follow the money, the traces down there, it's going over like it's near the FPGA. So, you can pretty much uh be safely assured that that is a JTAG uh pinout for the FPGA. And we don't want that. We actually want the uh debug uh header for the processor cuz this um runs a uh what is it? Android. Yeah, I

**Dave Jones:** think it's a Android operating system. So, there should be like a serial uh debug output here. Um and sure enough, if you've seen the teardown, so you look around for a what looks like a pin header, and sure enough, there's a four-pin header there here. There is no standard, and unlike uh JTAG type stuff, which often has uh standard, sometimes they're, you know, custom, but often they are a standard interface, but serial, you probably won't find a standard uh interface for that. Um so, yeah, we've got four pins here. So, my

**Dave Jones:** guess is uh there'll be transmit, receive, ground, and maybe power or something to power a uh thing. So, okay, let's actually probe that. So, we'll get the meter, and we'll see what's what here. So, let's go ohms-y. So, uh the ground I want to almost certainly, okay, it'll be logic ground, and logic ground will be connected to the metal shudgy ground in here. But because I've got pro tip, because I've got uh the mains input is connected to this metal up here, and this metal is not screwed

**Dave Jones:** into this metal, there's no earth wire that comes over here, and you don't want to rely In fact, let's measure it actually. I will disconnect. Haven't actually done this. Helps if I had the multimeter in shot. Measure between there and there.

**Dave Jones:** And it is. Oh, scope probe. Scope probe. Trap for young players. Yeah, I physically had it was going through there. Let's check that Let's recheck that now. No, there we go. So, there's no physical connection connecting those two ground points. So, scope's still going to work. Could be noisy or whatever, but you know, it it it doesn't matter anyway. So, what what I've done is actually connect just a shorting clip from here down to here just to join the two, okay? So, now we can safely

**Dave Jones:** measure that. No worries. And we can connect our scope probe up to the metal chassis here, okay? Ground it. Now, we'll have a look for Now, we'll probe the pins. That's pin one. Nope. No 32 ohms, okay? So, that's some sort of driver.

**Dave Jones:** Oh, no. See, the multimeter is oscillating there. That means it's some sort of active driver. It could be giving out some sort of pulse signal already. There could be some serial output there that's doing Generally, you can probe. It's not a problem. Like you can use your multimeter ohms range. The current is incredibly low, so you're not going to damage any active circuitry or anything like that. A lot of multimeters back in the old days I've done a video on this, haven't I? Used to have a low ohms

**Dave Jones:** function. And what that meant is not It's not measuring low ohms. It actually puts a low output compliance burden voltage on there of a maximum that's under the .6 volt diode drop, so it wouldn't turn on any junction, so you could measure like stuff in circuitry better, and it wouldn't turn on any active diodes or anything. It's got nothing to do with damaging, really.

**Dave Jones:** A uh a multimeter is not going to um output enough current. So, yeah, anyway, so that that could be oscillating. So, then we'll check that one. There you go, bingo, found it. There you go. So, pin three there is ground, and what's pin four here?

**Dave Jones:** Once again, that's oscillating, so let's put that over to volts here. And let's measure pin four again. 3 volts. There you go. It's not 3.3, it's 3. Okay, let's measure the others. Three. So, looks like three. Okay, so 3 volts might actually be the supply rail for this thing instead of 3.3. That's interesting. So, anyway, pin three is ground. We don't have to actually connect it through like actually ground onto that pin. You can just keep it on the chassis here, no worries. We don't care about signal

**Dave Jones:** integrity. So, I'm going to put that on pin number one. Got to start somewhere. Yes, the probe does actually fit in here. Just be careful if you leave it hanging like that, and you accidentally hit it, you can break your probe tip, and that will ruin your day. Oh, yeah, I'm feeling lucky. Feeling lucky, punk?

**Dave Jones:** Yeah, I am. Okay, so let's actually boot this up. Going to be using the new Rohde & Schwarz. Look at this bad boy. This is the baddest ass scope I've got in the lab here. I've already shot a little bit of footage with it, but this is the new MXO 4 MXO 4 series. This is the MXO 44 1.5 gig 12-bit ADC. This is got some absolute killer specs. So, anyway, I just wanted to play with it. So, let's let's play with it. Um a couple of

**Dave Jones:** annoying things, actually. Let me show you. So, there's our 3.6 volt signal. That's actually very clean. What if I I might be able to make that dirty. Let's Let's be dirty buggers, okay? So, what I'm going to do is I'm actually going to move my ground probe from here.

**Dave Jones:** I'm going to move it up to here, my ground clip, that means we've got a massive big long like antenna ground lead that goes all the way down here and back. Will that change our noise? Yeah. Yeah, there you go.

**Dave Jones:** Our signal's much noisier now. You can see that in there. Can I adjust the How do I adjust the multi-use? Does that How do I adjust the variable intensity? Ah, there we go. I've got to push that there. Yep.

**Dave Jones:** There you go. So, yeah, that is much noisier. But, that's neither here nor there when you're measuring like just you want like a 3-V TTL signal like this. So, you can see we're getting a high signal there. Nothing's oscillating. Let's go to pin number two.

**Dave Jones:** I've got a very slow time base here. What 1 meg points of memory, so yeah, it's No, it's 3-V and the other one pin four, nope. Okay, so let's leave it on pin number one. And let's do a boot on pin number one.

**Dave Jones:** First of all, I've got to set to normal mode. I've got my trigger set to positive edge trigger. So, normal mode, positive edge trigger, single shot acquisition. Oh, I forgot to show you the annoying things. Front end like this, okay? I wanted to set a Times 10 probe. This is the first time I've tried to do it. Where is the Times 10? Right? It's It's not here. And I'm using a switchable 10:1 probe that doesn't have the pin on it cuz obviously we can actually get the auto probe

**Dave Jones:** detection down here. But, it hasn't got it. So, like I'd expect when I call up my menu for the vertical channel, I want my like terminations in there, 1 meg, 50 ohm. Great. Okay, but where is like I just want 10:1. Like I Where's my probe attenuation? Okay, sure enough. Okay, I can go into probe menu, but there's no simple times 1 times 10. Okay? It's like it has like this user-defined thing, right? It's got user-defined. It's got all the other probes, which is absolutely great, right? If you're using

**Dave Jones:** active probes and current probes and all sorts of stuff, it'll set up for you. Fantastic, right? But, I've got to select like user-defined, and then what like where like manual attenuation 1 V per volt, okay? So, now I've got to go to 10 V per volt, or is it like point 1 V per volt? Which one is it? You've got to like you've got to actually think about it, right? I No. Give me times one, times 10.

**Dave Jones:** Like where is that? I don't understand why it's not there in that format. Like And then, if you set it there, it doesn't actually tell you what it is down there. It just says user-defined. Anyway, that's enough quibbling with my minor things. Let's put single shot capture. Well, let's turn the scope off first. Double-click of the soft power button does that. Okay, I've got positive edge trigger. I've got a slowish time base 40 ms per division.

**Dave Jones:** Yes, it is 1 2 This is weird. Actually, this one does 1 2 4 and 5 sequence. 1 2 4 5. It doesn't do 1 2 4 and then 1. It does doesn't do 1 2 5 and then 1 does 1 2 4 and you get the extra 5. That's probably like to optimize the you know, the dynamic range and the amount of memory and stuff like that. Anyway, just thought that's interesting. So, let's turn it on. See if we get So, this is pin number one.

**Dave Jones:** Oh, yeah, we got something. But, there's no data packet. I don't see any data packet in there. So, it it could actually come later. Can't turn it off until it's booted. There we go. Relay's clicked. Okay, so let's try this. I've got channel number one.

**Dave Jones:** Let's turn it off like that. Single shot trigger again, slowish time base. I've got yeah, 40 milliseconds per division. Negative edge trigger cuz otherwise if we do positive edge trigger, we'll get it as soon as it powers up cuz we saw that the default state before was high.

**Dave Jones:** So, let's try it. Yeah, and a trigger level about in the middle, you know, 1 and 1/2 volts. Nothing. It's gone high and it's not going low again unless I've goofed my trigger. I don't think so. Nope, there we go.

**Dave Jones:** That was just it looks like that was just contact bounce there. Let's try it again. Just turn my intensity up there so you can see it. Okay, so this is number two. That's channel two. Could be some data in there. Okay, so single shot.

**Dave Jones:** Negative edge trigger. Pin two. Did I say channel two? Aha, bingo. There you go. That is a data data packet. That is a data packet. There you go. So, we can Well, there's something something on power on. Okay, so I've definitely got something on power on. Yeah.

**Dave Jones:** Yeah, there we go. Yep. Oh, what's Oh, what's going on there? Check Check that out. Look. What? It's like that and then it's like that. It's Oh, that's doing That's the sine x on x. Is it? What's going on there?

**Dave Jones:** That's interesting That's an interesting quirk. That's got to be a quirk. Check it out. Yeah, look. That looks absolutely fine. That's it So, I'm one one meg points memory. Okay. And then boom, it goes like that. So, it's hiding.

**Dave Jones:** Maybe all that's there, you know, cuz our signal integrity is like really poor here. Okay, it's not great, right? So, I expect kind of rubbish, but why does it take it away at the shorter time base like that.

**Dave Jones:** That's interesting. Anyway, we definitely have serial stuff here, okay? So, no lockers like and zoom in there and that'll do the same thing. Yep. Okay. So, I definitely got a serial pin, okay? So, let's go back. Aha! That was I was just probing pin number four and that is a decay like that. So, I think pin number four is a power rail. When when you see like a decay like that, that's not like a logic output going low. That's like a classic power rail going low. So, yeah.

**Dave Jones:** No worries. Over 5 milliseconds, something like that. Yep. Okay. Same time base we had before, 40 milliseconds per division. Pin number four. Yeah, we're getting no negative edge at all. So, yep, that's just no negative edge trigger. That mean if we do it again, if we if we trigger it on positive edge, you'll see it go up. So, yeah, I think pin number five is a rail there and you could try and probe that out to another 3-V rail to confirm that. So, there you go. Pin number two is transmit and pin

**Dave Jones:** number one is receive. Pin number three is ground. Pin number four is looks like 3-V power.

**Dave Jones:** Okay, unfortunately, due to a very serious lock up I had on the MXO 44, which I have not been able to figure out. I've put that on my second channel, but I haven't released yet. I've sent it to Rohde & Schwarz to see what happened. I had some serious issues there. So, I've had to get another scope out. So, I got my Keysight 3000 cuz I knew this is going to be a high board rate. So, I knew this could actually capture the board rate. And if we get

**Dave Jones:** the cursors up here, you can see that we're talking about 660 nanoseconds there. You invert that on a calculator, that's about 1.5 meg board rate. Megabits per second, basically. Meg So, if we turn curses off um and we go into the serial uh decoder here, I can actually manually set a user-defined uh board rate here. You can actually go up to um what is it? Hang on. I can actually go up to eight 8 megboard there. There you go. So, we can actually go down to 100 bits per second. No.

**Dave Jones:** Let's go to 1.5 meg and uh come on. I can type it in direct. But, the Keysight has the best velocity control, by the way, of any scope. Let's set it to 1.5, which is like a really high. I've never encountered one this high before. Leave it in the comments.

**Dave Jones:** Um you know, like there are special cases, but like if for a just a um like product like this, yeah. Um haven't really seen it before. And I've already uh captured that at 1.5 megboard. I could do it again, but there you go.

**Dave Jones:** We got it. We got it. We actually got some legible text. DDRS and then version once you see, you know, like actual ASCII text like that, you know you've got something. Version 1.6 1.26 and so on, okay? So, and then we can look at our table up here. I don't know why my table has vanished now. I had I had it all up in my table before. Maybe I have to uh sample again. Anyway, let's actually actually I'll do that. I'll capture that again. So, leave it at that

**Dave Jones:** time base. Capture. Boom. Got it. There you go. And it's in my list there and I can scroll through my list there. So, I carriage return line feed, blah blah blah. So, 1.5 megboard. Unfortunately, and I just checked and both of the uh term PC terminal programs that I use for capturing boot data like this, both Termite and uh Tera Term, they neither of them support that higher board rate. They don't go over 250 uh 6K baud. So, yeah, I it can't do 1.5 meg. So, I'm going to have to look at

**Dave Jones:** some of my other PC-based scope options. We're just not going to be able to get it here. I don't I I don't know if Well, the Keysight wouldn't have the memory to dump it because this it's like a 1-minute boot period or something for this scope to boot or 30 seconds or whatever it is to boot and it's constantly putting out data. So, we want to capture the whole lot. So, yeah, we can capture a little bit like this, but I want to capture the entire boot

**Dave Jones:** log over the whole 30-second or whatever boot period. So, to do that, you need a a basically a you know, infinite memory like a you know, like a PC actually capturing and dumping it into a text window. And I'd like to use my Rohde & Schwarz RTB 2000 to do it. I like it's serial decoding. Unfortunately, it only goes to a maximum of 1 megabit per second. So, we can't do our predefined.

**Dave Jones:** Actually, can it go higher? User? Can Can it go higher than that? Never tried it. 1.5 meg. Oh, yeah, it can. Look at that. Okay, let's try it. Ha, I can capture that, but it's being smart down there and it's tell me telling me that it's aliasing.

**Dave Jones:** So, oops. I don't know why it told me that. Anyway, it's working just fine. And just a zoom into a random party here MR24 = 0x8c l something like that. So, don't know what any of that means, but it's captured it anyway. 1.5 megabits per second, which is really annoying.

**Dave Jones:** So, I've got to go and find a PC-based solution for that so I can dump it to a text file so then I can upload it to the forums. All the nerds can start working on the hack. So, we're over here on the workbench and I've got my Saleae Logic hooked up. I was using my serial UART decoder, but as I said, that's only like slow board rates, like a couple hundred K maximum, but I was able to use the Saleae Logic software and it does

**Dave Jones:** actually have Check it out. Does actually have a data terminal mode and I set it to 12 meg sample per second and 1.5 megabits per second. I entered that manually and bingo, we got it. There you go. Here's the boot. DDR version 1.26 in channel zero. So, this is the whole lot here. I will actually post it on the Oh, it tells you the DDR4 memory speed.

**Dave Jones:** There you go. Um so, yeah, I'll post this. I'll dump this over on the EV blog forum. I assume I can download this. There it looks like there's a download button there. I've never actually used this terminal mode before. It's really cool. So, I like it. There you go. So, and then you've just got all of these zeros and that's it for the entire boot sequence. I think I got I just And then I shut it down right at the end and it didn't add anything. Didn't have any

**Dave Jones:** shutdown data or anything like that. So, there it is. Um yeah, see, this is where you need a specific solution that can actually handle this this high board rate and let's see if I can actually dump that. No. What was that? No, that was just go to the bottom. Oh.

**Dave Jones:** I can highlight it. I can copy and paste, I'm sure.
