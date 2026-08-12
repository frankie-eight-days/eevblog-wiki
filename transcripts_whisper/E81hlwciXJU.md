---
video_id: E81hlwciXJU
title: EEVblog #1306 (5 of 5): Spooky Action - Hardware Testing
url: https://www.youtube.com/watch?v=E81hlwciXJU
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 27, "2": 40, "3": 64, "4": 83, "5": 113, "6": 133, "7": 151, "8": 165, "9": 188, "10": 207, "11": 227, "12": 246, "13": 265, "14": 283, "15": 304, "16": 327, "17": 347, "18": 369, "19": 387, "20": 417, "21": 440, "22": 458, "23": 473, "24": 495, "25": 512, "26": 524, "27": 538, "28": 551, "29": 564, "30": 585, "31": 594, "32": 601, "33": 629, "34": 643, "35": 672, "36": 690, "37": 713, "38": 736, "39": 748, "40": 766, "41": 780, "42": 797, "43": 813, "44": 832, "45": 852, "46": 867, "47": 888, "48": 908, "49": 921, "50": 943, "51": 969, "52": 984, "53": 1001, "54": 1024, "55": 1034, "56": 1052, "57": 1068, "58": 1081, "59": 1098, "60": 1113, "61": 1134, "62": 1150, "63": 1163, "64": 1177, "65": 1193, "66": 1211, "67": 1224}
---

**Dave Jones:** Hi, welcome to the final part of our Paduk 3-cent microcontroller programming series where we build up some open source hardware and software to program these 3-cent microcontrollers. Now, in part 4, we took a look at actually using the SDCC compiler, the small device C compiler, to actually program a file and generate an Intel hex file, which then we can use on our programmer to program our little chip.

**Dave Jones:** So we're basically just taking an existing pre-written example file and compiling it, generating the Intel hex file, and then simply running the command line programmer to program that Intel hex file into our chip. Sounds easy, but you guessed it, Murphy. Hmm, yeah, this is going to be a pain in the ass.

**Dave Jones:** You'd be amazed at what can go wrong with just doing that. Let's check it out. And there it is. I didn't bother with any of that bypass capability. Pass it to rubbish, don't need that. And yes, I'm going to say it, winner, winner, chicken dinner, of course it works.

**Dave Jones:** And I have no doubt that actually says hello world if we actually go in there and single shot capture that. And, uh-oh, does it? Ooh, that looks very clock-like to me, actually. That doesn't look like a hello world. Oh, have we come a gutter?

**Dave Jones:** It's outputting something. Oops, dumbass Dave. Eagle-eyed viewers will no doubt see that I probed the wrong damn pin. There we go. Ooh, ooh, hang on. That does... Oh, does it need a pull-up? Aha, that looks better. I think we have a dodgy connection issue because it's all over the shop.

**Dave Jones:** Anyway, yeah, that's actually probing, though. That's actually not probing. The zero, um, the, uh, bit zero. So, uh, pin zero, or whatever. So that's probing one over. So, I, yeah, hmm. Anyway, that's the one I get the signal out on. Wow, check this out.

**Dave Jones:** Yes, I had to swap our scopes to this brand new, uh, Siglent 2000X Plus series because, uh, my Keysight, my little Keysight 1000, um, I didn't have the series. I had the serial license, so I couldn't, um, yeah, do any serial decoding. So, I've switched anyway.

**Dave Jones:** Watch this. Watch this. This is really weird. Now, like, you think, okay, we're getting data out. It's not on the correct A. It's not on the correct pin we expect. But watch this. Watch this. If I put my hand near it... Oh, look, look, look.

**Dave Jones:** Magic voodoo. Ooh, ooh, spooky action at a distance. I'm not kidding. Like, this... And if I put my finger on the probe, look, if I, if I touch it very lightly, and if I touch it harder, it, I can make it completely vanish.

**Dave Jones:** Wow, look at that. So, we're actually, that's the pin that we're supposed to be getting out, and we're not. We're just getting some crusty stuff on the ground there. So, it's that pin there, which is pin six. And pin five, we're getting something as well.

**Dave Jones:** Just realize that. Pin five seems... No, but look, if I hold my fingers on there, take them off, I'm trying... This is literally spooky action at a distance. Yes, I've put a bypass cap on there. I've checked the connections and everything else. So, when you start seeing weird stuff like this happening, right?

**Dave Jones:** There we go. There's our packets. When you start seeing weird stuff like this happening, and, like, spooky action at a distance, you have to assume that... There's some sort of floating input happening, and it's, of course, picking up, like, the 50 hertz from my fingers, right?

**Dave Jones:** As I get close, there's capacitive coupling through the air into the pins. Now, of course, this thing doesn't use... Oh, there we go. I can make it die completely. These things, it doesn't have... You saw the code. The code doesn't have any input whatsoever.

**Dave Jones:** It's supposed to be using an internal oscillator, and then simply... outputting data, but those keen-eyed might have seen that in the code before that this actually works on interrupts. So, that's what I'm thinking, is that it's got the wrong chip target in there

**Dave Jones:** because I believe the code was for the PMS-154. We've got the 154C, and I'm wondering if that makes a difference. So, anyway, we'll look into the code in a minute, but, yeah, start seeing spooky action at a distance like that. Something's floating. So, what I'm going to do is just ground some of the inputs

**Dave Jones:** because they're all floating at the moment, and see if that makes a difference. Aha! I just tied pin 2 high here, and that's already killed the output. So, yeah, something's going on. Let me just lift that. Oh! Whoa! Whoa! Ha-ha! This is weird stuff.

**Dave Jones:** Nah. I, uh, you know, I'll lift it. Okay. There it is. Let me touch that. Yeah. Look at that. I can change that just by touching that input. Wow. And, by the way, these are, this is 0 to 5 volts. These are real genuine totem pole-driven hard, you know, outputs.

**Dave Jones:** These aren't, you know, this micro's not mucking around. It's actually genuinely driving those output signals hard. So, it's, you know, it's not just. Uh, the output flapping around in the breeze. Something's causing, my guess would be something's causing the, um, input. Um, there's some input somewhere because the chip's configured wrong somehow.

**Dave Jones:** Um, it's goofed it up because, I don't know, it might have the wrong chip type or whatever. And the configuration registers were different or something. And it's just configured it oddball-y to have some sort of an input which might have an effect on the interrupt routine, um, that's, you know, sending the output data.

**Dave Jones:** Hmm. Oh, look at this. The PFS154. The PFC. No, I've got the PMS. Ah, it's like, uh, all these confusing, uh, numberings and things like that. I mean, P, PMC154. Can you even buy that? Is it a thing? No. Is it on the Padauk website?

**Dave Jones:** PMC. There it is. We've got different types. The PMC153, 156. The PMC154's not even there. I can't like it. It's just, oh, anyway. So, I, I would imagine that because, look, they've got different, uh, they've got if, uh, if defs in here, right?

**Dave Jones:** If define, uh, if it's the PMS173, if it's the PFS154, the PFC. That's why we've come and got some, because these, it has different register addresses for all this sort of stuff. So, it's a wonder it works at all. Um, so, it looks like there are subtle differences between all the modules.

**Dave Jones:** And I am, we would imagine that the PMS is different as well. And we could go in there and search all the register entries and stuff like that and try and fix this up. So, I think I'm better off just going over and finding some other code, uh, like this one.

**Dave Jones:** Does this one work? Here we go. I found, like, a blinky thing with the timer. Uh, does it say anything about, uh, timer IRQ blink? This one actually doesn't say anything. This one just says, um, right. So, here's the original mini C code, they call it, which is, I guess, PDUXC.

**Dave Jones:** And they've commented all that out. And here is the new code. But it doesn't say which one this is actually will compile for. But, hey, it takes me, like, a minute. To, like, compile this and program a new chip. And I've got lots of chips, even though they're one-time programmable.

**Dave Jones:** I've got a few. So, um, yeah, we can afford to do this. And, and that's the thing. Like, even though these aren't Flash, you can still, like, these are so cheap. They're three cents a pop. So, you can actually afford, I know it's like a waste.

**Dave Jones:** But you can actually afford to, uh, refine your code like this. And once you get it perfect, um, and just go through, you know, even if you have to go through 50 of these things. To perfect your code. Once you do, bingo, it's set in stone.

**Dave Jones:** Because these programs aren't big. You know, they're pretty easy to test and actually refine and get working absolutely perfectly and thoroughly. Um, so that, yeah, you can be confident that you can program these one-time chips once your program's all debugged and stuff like that.

**Dave Jones:** Or you can go, or you can buy the emulator and use the emulator and stuff like that if you really want to do that. But, anyway, yeah, at three cents a pop, um, you know, I wouldn't be complaining about, uh, burning through a few of these, literally.

**Dave Jones:** Ha! You're all weak. Now, interestingly, on the EEVblog forum post over here, I found an extra, uh, option, programming option here. DPFS154. So, like, or PMS15C, and I actually just tried that, uh, compiling this, adding that option in. And it does actually work.

**Dave Jones:** It didn't recognize lowercase, as you can see, but it recon-- So, uh, maybe I could recompile the other one with that DPMS154C. So, uh, maybe I could recompile the other one with that DPMS154C. So, uh, maybe I could recompile the other one with that DPMS154C.

**Dave Jones:** So, uh, maybe I could recompile the other one with that DPMS154C. So, uh, maybe I could recompile the other one with that DPMS154C. option and see if that works. That'd be an interesting test. So anyway, I thought I'd just redo that project. I goofed it.

**Dave Jones:** I did text again. Test, test. There we go. So it actually compiles that. So now if I go test.c and test.rel, and then I hate, you really need a script to do this stuff. You know, like a program, someone can do like a simple program that just puts all these

**Dave Jones:** options in you. Like checkbox, I've got this chip and it automatically knows it's a 14-bit architecture and it puts in the option for that and stuff like that. So anyway, test.rel, test.ihex, boom. Okay, so I now have a new test.ihx. Yep. Okay, so I'm going to program.

**Dave Jones:** PMS154C, right, test.ihex. Okay, I've got my chip in. I should have probed it first. PMS154C, right. Done. Ha, let's try that. No, that was worth a shot, but it's doing the same voodoo thing. So yeah, that didn't make a difference. It's, it's the code.

**Dave Jones:** Anyway, what I'm going to do is this interrupt driven lead blinky program over here, which is for a mysterious chip. Never know your luck in the big city. So let's try that. I've got that saved as test2, and PMS154 device, boom. Test2.rel, test2.intelhex, boom.

**Dave Jones:** And if you're wondering why I've changed my t-shirt, it's not because I've come back later or the day later, because I'm filming this over multiple days. It's because the other one I was wearing was just generating too much static and I didn't want to be like, hey, I don't want to have to ESD strap.

**Dave Jones:** So yeah. Right. Test2. Done. This is too easy. Winner, winner, chicken dinner. And let's see if there's any funny business going on here. This is just like doing like a one second thing. What's the time base there? 500 milliseconds per division. Yeah. And, uh, nah, it's still doing it.

**Dave Jones:** I don't know how to get roll mode on this thing. It's just acquiring and then it's got to update the screen. Um, this seems to work fine. If I do the other pins, nope, nope. I only get, uh, whoop, there we go. I just disconnected.

**Dave Jones:** I only get that. So that works. Um, so yeah, if we want to get the hello world thing, uh, working, I think we have to, uh, go in and figure out what registers are wrong there. And like, you know, what, what's actually up with that.

**Dave Jones:** So that could require a debugging. I'm not sure I'll do that. Would have liked it. It was seen like a UART output with hello world. We almost got it there. It's just some silly bugger business going on. Anyway, there you go. Dumbass Dave didn't see the roll button over here.

**Dave Jones:** There you go. So that's our, uh, and if we probe the other, other pins, you can see we get zippity do dah because that's actually not an output. So we're actually picking up crap there. So yeah, if I touch that, we're picking up my 50 Hertz there.

**Dave Jones:** So yeah, they're configured as inputs, not as outputs. Only pin seven there is configured as the output. So we get in our like one Hertz signal and that comes from an internal interrupt, uh, using like timer based, uh, interrupter divided by the main internal clock.

**Dave Jones:** Fantastic. So there you go. We proved that we can, uh, program a chip. No worries. Wah, wah, wah, wah. Be careful pulling these out of your breadboards. There's the spring. Uh, where's my other spring down there? Oops. All right. So I just might have a quick look in header format here.

**Dave Jones:** Register mapping scroll, right? I don't know what that is, but, uh, programmer notes. Ooh, special code found in PMS one five four B I've only got C what the special aha register mapping. Here we go. This is what I want. One five four PFS one five four.

**Dave Jones:** There you go. So we should be able to PMS PMS one five four. I assume it's the same for the one five four. Is it the same scroll? Yeah, that's why it said scroll. Yes. Cause you got to scroll across one five. Has it got the other ones?

**Dave Jones:** One five four PMS one five PFS one five four PMS one five two. Yeah. So I think the one 50, this is the one we want. I think the PMS one 50 C cause we've got the C version. So I think all the ones they're just

**Dave Jones:** like different, uh, size pinouts and stuff. So the internal registers should be the same. So our program, our code over here is written for this PFS one five four. Here it is PFS one five four. So we have to modify anything that's related to the PFS one five

**Dave Jones:** four, change it to whatever we can get to the equivalent one for the one 50 C and hopefully we can get our program working because what's actually causing that weird ass fault. I like, I can only imagine it's getting an interrupt from an input pin, a floating input pin somehow.

**Dave Jones:** Well, no, I'm actually comparing all this stuff here between the one, uh, the PMS and the PFS one five four. And they're all the same, uh, like the port a register, the port a control, which is the pack register, all the interrupt stuff, interrupt requests.

**Dave Jones:** The timer is all the same. They're all the same. Address. So like, and we're not calling up PDK 15. Uh, so it should give the else. I guess I could simply take out that code just in case it's doing something weird and only have that perhaps, uh,

**Dave Jones:** if I get desperate, but that should work. Um, apart from that, I don't know what, uh, like registered, like what bit operations are happening here. Uh, I haven't gone that far in, but if we've got the right registers, they should operate in the same way across

**Dave Jones:** all of the different devices. You know, like, like the interrupt register should have the same bits in it for all the different devices. Um, it's just a different address that the interrupt register might be at. I don't get it. Factory calibration. I mean, the timer seems to be

**Dave Jones:** working and everything seems to be doing the business, but, ah, very strange, very strange. Uh, port A control. There's the, you know, the bit that we're turning on. I don't even see that actually working properly. So, uh, maybe I can just make them all outputs or something like that.

**Dave Jones:** Make them all outputs. See if that makes a difference. So yeah, I am, I am not seeing it based on that register. So I don't know. Um, maybe people are screaming at me in the comments going, oh, Dave, it's obvious, but I'm, I'm not, I'm not seeing it.

**Dave Jones:** Nah, I was hoping I could just modify some registers, but anyway, I might have muck around, but, um, yeah, if I don't update you on this, it means that my muck arounds weren't successful and nope. Unfortunately, uh, taking out all that stuff, uh, didn't work.

**Dave Jones:** It does exactly the same thing. So I have no idea what's going on there. I could spend ages trying to troubleshoot this. Um, but anyway, that's not really the point of this video. The point of this whole video series was to show you how to take a GitHub project that you might

**Dave Jones:** need for some particular, uh, purpose and actually order all the parts, order the board, assemble it, and then test it, get it working and potentially debug it. And then, uh, get all of the software actually working all these, um, open source programmer software.

**Dave Jones:** It wasn't as trivial, trivial, um, as I thought it might be. And we ran into a few interesting hurdles there that we had to, uh, overcome. So I, I really like it when that sort of thing happens. So anyway, if you like that

**Dave Jones:** video, give it a big thumbs up and as always comment down below, and especially want to hear about this, uh, format. I did ask this of my, uh, supporters. I took a poll and the majority of people said, yeah, they want to see this sort of like longer form, like follow along with Dave as

**Dave Jones:** Dave goes through and bumbles his way through, uh, because like the whole process rather than just some, you know, spit and polish tutorial where nothing goes wrong. Sure. I could edit this thing, uh, till the cows come home to produce like a, a single 10 minute video of here's how to, uh, you know, get the padauk, uh, software actually

**Dave Jones:** working, uh, and the hardware and software working from the go. But, and if you want that, please leave it in the comments down below. Maybe I can take my, this existing, uh, multi-part tutorial and actually condense it down to a more manageable, uh, 10, 15 minute, uh, type

**Dave Jones:** instructional video. But, uh, let us know what you think about the, you know, follow along as things go wrong and we have to troubleshoot and we have to bumble around and figure out this problem and solve that problem and things like that. So yeah,

**Dave Jones:** in the comments down below. And of course, yes, I'm going to shout out my library channel. I think I'm at 20,000 subs. I was like 19, 990 something. So by the time this video comes out, I'm sure I'm over 20,000, which is absolutely fantastic.

**Dave Jones:** And of course I, uh, I rarely mentioned, but I've got a Patreon, uh, as well, where you can often get access to early access to video videos. I actually released them early, including this particular, uh, series as well. So if you want my early stuff, head on over to Patreon.

**Dave Jones:** I'm having a bit of trouble with my Discord server as well. And also I have other channels. I still have my BitChute channel. I still, uh, upload my videos on Vimeo. I batch upload and other places. Heck, I still even have my RSS feed from day one, which

**Dave Jones:** is a 720p one, uh, hosted directly on my own web server, um, as well. So yeah, anyway, that's it. That was good fun. I enjoyed that, uh, process. It, uh, took a little while, but we got there. You know, I expected a few hurdles.

**Dave Jones:** I was hoping for a few hurdles and we got it. Beauty. Anyway, I hope you enjoyed it and found it useful. Catch you next time. Bye.
