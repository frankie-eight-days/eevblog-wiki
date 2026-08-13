---
video_id: tF2krfxYc68
title: EEVblog #30 - Jaycar Bench Lab Power Supply Review
url: https://www.youtube.com/watch?v=tF2krfxYc68
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 41, "3": 59, "4": 83, "5": 105, "6": 123, "7": 147, "8": 166, "9": 182, "10": 200, "11": 216, "12": 233, "13": 249, "14": 268, "15": 290, "16": 306, "17": 322, "18": 338, "19": 355, "20": 374, "21": 391, "22": 418, "23": 438, "24": 454, "25": 472, "26": 495, "27": 512, "28": 525, "29": 542, "30": 562, "31": 578, "32": 593}
---

**Dave Jones:** Welcome to the EEVblog. I'm your host, Dave Jones, and this is episode number 30. We haven't had an equipment review for quite some time, so I bought a couple of these for work the other day and I thought, let's take a look at them.

**Dave Jones:** This is a Jaycar bench power supply. It's the Powertech brand, the MP3086, and it's a 30 volt, 3 amp bench supply. It's one of the cheapest on the market. I only paid $150 Australian dollars for it. Every time you get a new bit of gear, there's two things you've got to do, and I mentioned it before.

**Dave Jones:** The first one is taking that new product smell. This one doesn't really cut the mustard there, I'm afraid, but what do you want for $150? And the second thing is, don't turn it on, take it apart. Let's take a look inside here. What do we have?

**Dave Jones:** This is pretty much what I expected. We have a front panel board, which does the sampling, obviously, and the display. Now, I would also expect a current shunt. There's the output current shunt. It's pretty standard technology. And the main control board over here, let's have a look at this.

**Dave Jones:** An interesting aspect is that it uses sockets. I'm quite surprised at that. You don't see that too often these days. So sockets are a bit unusual. They're probably op amps, I can't read the number there, but most likely they've got some trim pots for setting, things like that.

**Dave Jones:** There's a couple of relays, as you'd expect, to switch the output taps. This is your bridge rectifier, and you've got your series pass output transistor there. They're both on the heatsinks. They actually use spring washers and insulators, so that's actually done right. Let's look at the mains socket down here.

**Dave Jones:** Now, they've actually scraped away the paint on the chassis to get a good earth connection. That's done right. Once again, there's a spring washer in there. But these are insulated here, but they're not overall insulated, so you've got exposed mains there. It's just a standard fused IEC outlet, of course.

**Dave Jones:** And if we take a look at the mains wiring, let's follow the mains wiring. Now, it's, you know, it's got cable ties on it, it's nice, OK? Until it gets to here, where they actually start bundling the mains wires. They bundle the mains wires with all the other signal stuff.

**Dave Jones:** Look, there's tiny output signal stuff bundled with the mains wires. Not even sure if that's legal. It's crazy, anyway. On the backside here, we can see the solder joints. See the solder in there? This is the control board, this is the single-sided board.

**Dave Jones:** It's not too bad at all. Notice how the, um, I'm not sure if you can see it on the screen here, but these, these supports, they're actually bent. So, it looks, it looks like they haven't got the engineering right on that. And when they've gone to install it, they've just gone, ah, well, let's just bend them.

**Dave Jones:** We don't want to have to redo it. We don't want to have to redo the board or redo the chassis. Now, let's take a look inside here, and you can actually see, I don't know if you can see right down there, but this, this output board here, they've actually got, ah, filter caps directly on the output board.

**Dave Jones:** And they look like, ah, low ESR ones or something. And, or high temperature ones, high performance ones. So, that's not too bad at all. Don't know if you can see it, but down under the bottom here, you'll probably have to trust me, is a, um, output diode protection.

**Dave Jones:** Um, as you'd expect, it looks like it's got a big beefy diode. So, that's all nice and good. Once again, internal, ah, the actual, ah, wiring construction. They've actually got nice proper spring washers and everything. So, that's, that's actually done quite well. Got a 16 series PIC.

**Dave Jones:** It's a 16F690 PIC. And, so there you go. I wouldn't have, ah, expected that, but, you know, they've used a PIC, and they've obviously got a display controller here. I'm not sure what that is. Now, I don't like the look of these two, um, TO220.

**Dave Jones:** Sorry, these TO220 voltage rigs. They're just freestanding. And, if you're experienced with, ah, PCB component construction, and, ah, vibration, and testing, and things like that, you'll know that this is a classically bad technique. These should be bolted down. They should be secured in some way.

**Dave Jones:** Otherwise, they actually vibrate off. If you had this power supply on a trolley, or something like that in a factory, these things would just fall off in a matter of days or weeks through sheer vibration. They've actually used, ah, sockets here on the front board.

**Dave Jones:** That's rather surprising, because, um, that costs extra, really. They've actually gone for the more expensive 5 or 10 turn trim pots here, rather than the, ah, rather than the cheap single turn ones they use over here. So, they've actually gone to a bit of trouble.

**Dave Jones:** And, it looks like there's a couple of optocouplers there. So, they're, they're doing the proper design. This board actually looks like it's designed fairly well. And, it's got, it's a Sarko brand. I'm not sure if you can see it, but it's actually done by Sarko.

**Dave Jones:** And, Sarko are the ones who make this supply, because I saw Sarko branded on the internal packaging. As for the transformer, you can see that's assembled properly. Once again, they've got proper, ah, shake-proof washers in there. And, they're actually the, um, shake-proof nuts as well, captive nuts.

**Dave Jones:** And, you know, it's, it's really quite, it's really quite good. A major thing I found with this, I noticed straight away, is that when you turn the knobs, it's got a horrible noise to it, and a, and a weird feel. It almost feels like it's actually a wire-wound pot.

**Dave Jones:** But, it's, it's not. They're clearly, ah, carbon, because one of them has the standard, ah, feel and noise of a carbon pot. And, the other one is just a bit, I, I'll see if you can, I'll put up the mic here, see if you can hear this.

**Dave Jones:** And, the other pot, the other pot. Hey, well, let's just switch it on and see what the display looks like, shall we? Clunk, and it's really, look at it. That's a real sexy looking display. I really like it. If we turn up the voltage, let's see where the relays kick in, shall we?

**Dave Jones:** Oh, there we go. One, it kicked in at about six odd volts, so that's the first tap on the transformer. Second one, at about 14. Then at 19, 20 volts, it kicks in another tap. And, they do that, that's standard practice, they do that just so,

**Dave Jones:** so they reduce the power in the, um, series pass transistor. They don't want to waste excess heat, so they just choose a different transformer tap. And, if you can see here, it's actually got, it switches between constant voltage mode, and if you turn the current right down, I've got no load on it,

**Dave Jones:** but it'll actually go into constant current mode, so it tells you which mode it's in. That's actually quite nice. Now, one of the most important characteristics of a power supply is its switch-on performance, to see if it overshoots its switch-on. Now, I've got the scope set up here to trigger, and let's give it a try.

**Dave Jones:** Let's switch it on, and let's see what we get, shall we? Wham! There is big, check it out, there's huge overshoot there. That's 5 volts per division. That's massive overshoot. Check it, I mean, I've had the supply on before, but that's, that's crazy, look at that.

**Dave Jones:** OK, let's try this overshoot again, and let's switch it on, and whoop, it ramps up very nicely there. So that thing we had before was just a furphy, based on the, based on a previous output voltage, but still, that, that wasn't very good.

**Dave Jones:** That's something to watch out for. I'm just testing the noise here at the moment, and it's claimed to be 1 millivolt on 2 millivolts per division, so yep, it's right down there. I mean, I should be doing this on an analogue scope, really,

**Dave Jones:** but yeah, it's, you know, it's really quite low noise output. It's interesting to note that on the back heatsink here, they've actually gone to the effort to put a protection plate over the output transistor, just so that you can't, you know, something on the bench can't accidentally short it out,

**Dave Jones:** and it'll go bang. And that's, that's really quite a nice touch for such a low-end supply. The internal construction of these things is, is really quite, quite unusual to see. It's, it's quite remarkable. They've got the old-fashioned single-sided board in there for the control board,

**Dave Jones:** but then they've got a nice, modern, properly designed double-sided board with a PIC micro and a display controller and optocouplers and all sorts of things, and it's just, you know, it's just an unusual blend, almost as if, you know, two entirely separate design teams.

**Dave Jones:** There's one who designs the control boards, and there's another who just slapped together a supply based around that control board, and they do the other board, and they goof up the internal wiring, and they do the current shunt and all that sort of stuff.

**Dave Jones:** It's, it's just rather unusual. I don't, I don't think it's been entirely done by one design team.
