---
video_id: -W5zEtqJJIo
title: C/C++ Interrupt Undefined Behavior
url: https://www.youtube.com/watch?v=-W5zEtqJJIo
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 32, "3": 58, "4": 79, "5": 101, "6": 123, "7": 147, "8": 166, "9": 191, "10": 207, "11": 231, "12": 250, "13": 263, "14": 286, "15": 301, "16": 324, "17": 337, "18": 366, "19": 390, "20": 407, "21": 421, "22": 442, "23": 465, "24": 484, "25": 500, "26": 517, "27": 540, "28": 553, "29": 576, "30": 604, "31": 630}
---

**Dave Jones:** Hello. So, I'm just going to demonstrate an issue with GCC, yet another one, because that compiler just keeps giving. And yes, I'm pretty bitter about that damn compiler. I can't wait for Clang to come on embedded in a serious way and have some proper quality control because

**Dave Jones:** I know on the desktop they're somewhat more reliable, so I assume it's going to be the same with embedded systems. Now, despite my frustration, this could actually be my fault. I could not know something about the way optimizers behave in a very specific situation.

**Dave Jones:** So, what I have here is a USB microcontroller. I've got a HID interface set up and I'm periodically transmitting data. This is a test, okay? So, this isn't real code, this is just me dumping the alphabet and a bunch of miscellaneous characters at the end with a new line and

**Dave Jones:** then doing it again. So, inside the transmit function, if there is some data, it doesn't do anything, it just returns false because the USB bus is busy transmitting. If there isn't data, then it's okay to initiate its own transfer and do that. The software 1-level

**Dave Jones:** up is responsible for retrying in a sensible manner when failure occurs. In each of these, we record this thing called a length point. A length point isn't a formal term. So, this is just a stupid name for something. All it does is record the line of code where the

**Dave Jones:** macro is called and it records a single integer of some kind. In this case, it records size. All right, let's see if we have that. Okay, so it will only transmit if a previous transmission is complete. That's pretty important because you don't want to steamroll over the currently

**Dave Jones:** pending transmission. All right, so when a transmission is complete, the microcontroller calls this function, transmitComplete, and if it's N.1, which is the only thing we care about, so I might as well just minimize this, get rid of the noise for people, it runs this.

**Dave Jones:** It pops the amount of data that was in the packet from the transmit buffer. The packet isn't infinite size. It has like 30 bytes, 32 bytes. Well, it has 32 bytes, but it's a bit more complicated than that, but it's irrelevant. So, it has some bytes and it pops

**Dave Jones:** it from the buffer. Now, it doesn't pop negative. So, if the capacity was 10 bytes, for example, and the tf.data was 8, it pops down to 8. So, it pops 8 bytes. It doesn't pop more bytes than exist. That's not possible. This is a noexcept type function, so it always succeeds

**Dave Jones:** and it's a useful approach. So, after the pop, if there's still data in the buffer, then I need to continue transmission. So, I call, if there's still data, which means it's not empty down here, I call transmitContinue once again. So, what's the problem?

**Dave Jones:** How could this really have a problem? Well, apparently, compilers can be annoying. Now, I'm going to give you some background about the volatile keyword. The volatile keyword, apparently, I might not know something about it, but I'll tell you what I do know. The volatile keyword

**Dave Jones:** is usually used for memory that may change without the compiler knowing about it. It is not used for atomics. It is not used for memory ordering. It also can't be used for splicing. It can't be used in bit fields in the way that most people use them, because

**Dave Jones:** the micro can only access one byte at a time, for example. So, does it access, if it's a volatile, right, and two bits are volatile, does the compiler optimize the remaining six bits in a byte as a constant, or does it, what does it do?

**Dave Jones:** So, this is actually one of the contentions with volatile keyword, and it's why C++20 might deprecate a lot of its uses. But one of the uses that probably won't be deprecated is the use with registers, which is like, a register is something that has flags in it, maybe, like an interrupt

**Dave Jones:** flag, and that will happen independent of the execution of the code. So, the compiler will never be able to figure out whether that will change or not, because it isn't changing it. The code isn't changing it. Something else is. So, that's what the volatile keyword

**Dave Jones:** does. So, what is the problem here? Well, the compiler, it seems to not believe the length stored in here, this variable here, changes. It thinks it's a constant in only one setting. This setting. Or, it may not think it's a constant, that could be wrong.

**Dave Jones:** Or, it operates on two separate versions of that, and this is the bloody insidious case, I hope it isn't this, it's a really stupid bug if it is. Operates on two separate instances of it. And why do I think that could be possible?

**Dave Jones:** Well, because if I transmit more than the packet capacity, it does successfully transmit two different bytes, with the correct lengths. And that pretty strongly indicates that this condition works just fine. And if I, so, and I also, when I'm executing the code, if I call transmit a second time after a first

**Dave Jones:** successful transmit, the first successful transmit calls this, and when the bug exists, the second transmit calls this, even if the TX data is truly empty. So, to me that almost says it's storing length separately for each of the call sites of the data view size function.

**Dave Jones:** So, that would be a bloody weird thing to happen. But, here's the thing. So I'm just going to show you the device run. So, here's the little terminal application that we have. And, okay, it's succeeding. Bloody hell, I forgot to, okay, well, so there is it running

**Dave Jones:** correctly. Now, the only thing I'm going to change now to make it break is one keyword, volatile on the length. Length is not a register. The length does not change independent of the code execution. It changes because of code execution. It changes in code.

**Dave Jones:** So, I mean, it doesn't look like a register. It's not a register, okay? And it's also not stored in a mysterious block of memory which has strange alignment conditions. It's stored in normal memory. And I have no alignment conditions on this anyway. So, it's not that.

**Dave Jones:** It's just, it's just a stupid thing. Okay, so let's just run the application thingy there. And here, bloody mouse isn't working. So, here we go. See, it's frozen after the first call here. Now, if I, if I pause this, I can view those L points, those L length points

**Dave Jones:** right here. So, the first call site is interface at line 34. So, the first time transmit enters, it goes straight in, no problem at all. Length point recorded as zero because it hasn't been inserted yet. That's what it should be. The next time that a length point is recorded

**Dave Jones:** is at 228. 228 is inside the transmit complete function. And 228 is in this line here. So, that is basically just saying there is data inside the TX. And that's correct because I'm doing 35 bytes. And so, the first time it transmits 30 of those bytes.

**Dave Jones:** So, I've got five left. So, that's correct. And it should record like five or something. Yep, five. There you go. So, then, after that's complete, so, there's two things we expect here. The next thing, it should, it should be done with the data at that point.

**Dave Jones:** So, the next line it calls is this line here, line 224. So, at that point, we know TX data is empty, at least from the perspective of this call site. So, how could this go wrong? How could this possibly go wrong? Well, quite some time later, and I mean really quite some time,

**Dave Jones:** the polling interval is pretty slow compared to the speed it can output data. It calls this. TX data is empty. So, it should enter here and then record zero. But it's not doing that. Instead, it's going into here and recording 35. Okay. So, we're at line 252.

**Dave Jones:** And the line before it, the recorded length was zero, right here. Nothing mysterious apart from my choice of naming, which is very mysterious. So, the length is zero and it was recorded just again for thoroughness right here. Nothing different to every other record site.

**Dave Jones:** All right. So, the next time that length is recorded, some mysterious way, without it ever entering this section, TX data is now 35 bytes again. I can tell you it's not, okay? And this is a bloody mystery to me. I hate compilers. So, that's it.

**Dave Jones:** It works when this length variable here is volatile and that should not be needed. And you want to avoid volatiles on variables like this because it prohibits optimizations in all kinds of places. All right. Well, that's the problem. I hope you found this interesting.

**Dave Jones:** If you did, hopefully you know the answer. Leave a comment down below. Bye. That's the wrong program.
