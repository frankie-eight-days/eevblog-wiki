---
video_id: _pGk6GYDnes
title: EEVblog #17 - I hope your next project DOESN'T work!
url: https://www.youtube.com/watch?v=_pGk6GYDnes
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 31, "2": 50, "3": 68, "4": 94, "5": 120, "6": 139, "7": 158, "8": 174, "9": 193, "10": 218, "11": 244, "12": 267, "13": 287, "14": 305, "15": 334, "16": 350, "17": 369, "18": 385, "19": 400, "20": 420, "21": 440, "22": 468, "23": 488, "24": 516, "25": 539, "26": 558}
---

**Dave Jones:** Hi, welcome to the EEVblog. I'm your host, Dave Jones, and this is episode number 17. Now, in a previous blog I spoke about, well, I actually mentioned findchips.com, which is a really handy website for searching for parts. It'll, you know, you type in the manufacturer's part number or a partial part number and it'll find, it'll search all the major manufacturers, you know, DigiKey, Mouser, Newark and, you know, a whole bunch of others.

**Dave Jones:** And it'll give you results of, you know, stock availability and price and all that sort of stuff. And it's fantastic. Now, since that blog, somebody else put me on to octopart.com. And it's a similar sort of thing, but it's got some ads and, you know, it's a bit busier.

**Dave Jones:** But it basically does a similar sort of thing to findchips.com and, you know, I really like it. It's not quite as good as findchips.com as far as search results. I found, you know, it actually doesn't find some of the stuff that findchips.com does.

**Dave Jones:** But it searches some more obscure actual suppliers and actually returns a, the list is much better formatted than findchips.com. So, you know, so they really complement each other. So I find that, you know, pretty much every day now I'm using both findchips.com and octopart.com.

**Dave Jones:** So check them out. They're really good. Recommend them. Now, over the years, I've had a lot of young people ask for my advice on what's the best way to learn electronics. And, you know, to get a real good in-depth understanding of it, you know, is it through, you know, self-study, actually reading books, or is it, you know, building stuff?

**Dave Jones:** And, you know, my opinion is that you've got to have both. You've got to have that hands-on practical experience and you've got to, you know, read up on the theory and just, you know, you have to be fairly well grounded. But the biggest thing you can do, not only build stuff, but debug stuff.

**Dave Jones:** So here's my wish for your next project. I hope your next project doesn't work. I hope you build it, you switch it on, and it does absolutely nothing. Why? Because you'll learn more than anything else about electronics when you have to actually debug a design.

**Dave Jones:** If you just, you know, follow a circuit and you build it up and, you know, and it works first go, you haven't really learned much. You've learned how to solder or you've learned how to construct and you've learned how to wire things, but you haven't really learned about electronics design.

**Dave Jones:** And debugging stuff, debugging the designs you build, is one of the best things you could do. Especially those really elusive problems that can take you days to track down or something like that. It is the best way to learn. So, next time, I hope your project doesn't work.

**Dave Jones:** And I mean that in the nicest possible way. It's time for another story from the bench. And this one happened to me some time back. I was called over to actually debug a design I built. And, you know, one of the software guys was working on it, trying to get up and running, and we were having a weird problem with it.

**Dave Jones:** Right, so I do a basic block diagram of what we were actually working on. And what it consisted of is an audio chip, and it's an I2S output audio device. And we had an FPGA, and this had an internal processor, which was running some code, of course.

**Dave Jones:** And this was trying to sample audio data from the I2S chip. You know, it was sampling audio, converting it into a serial I2S data stream, and feeding it into the FPGA. And what we found, we were getting, well, it wouldn't work at all.

**Dave Jones:** The software guy was going, oh, you know, it's, you know, he's coding here, he ported it from something else, and there were no known problems with it. And he was, you know, pretty sure it was actually a hardware fault. You know, he was actually fairly cluey hardware-wise, and he was, you know, fairly sure he narrowed it down to a hardware fault.

**Dave Jones:** So, you know, I believed him when we started probing around. And on one of the inputs here, we actually measured, and we actually got out a waveform, which I won't draw it here. I've actually got a screenshot of the typical one, and I'll show you that now.

**Dave Jones:** Now, that waveform actually has the classic, instead of being a, you know, a, if this is 3.3 volts and ground, instead of being a complete, you know, low-voltage TTL signal that goes from 3.3 volts to ground, it wasn't. It was, it looks like it was shorted to something else.

**Dave Jones:** Now, that is a classic indication of a hardware problem. Okay, we've got a short on the board, you know, it was a prototype board, I think it was. And so we were probing around, trying to find shorts, and, you know, it took us ages.

**Dave Jones:** And we were, you know, trying to figure out why this thing, and because it was an FPGA, these inputs were all programmable. We thought, aha, maybe the short's actually occurring inside the FPGA, something wrong with the FPGA design. And, you know, the outputs are mapped, and it's shorted, it was a very complex design.

**Dave Jones:** It did other things as well, and it's very easy to mix up the outputs, and, you know, get errors like that. So we couldn't actually find, you know, we took the board, we looked at it under the microscope, and we couldn't actually find any actual hardware shorts on the board.

**Dave Jones:** It was shorted out somewhere, so we spent ages trying to, you know, figure out, you know, something wrong with the FPGA. I told the software guy to go back and, you know, try and figure out what was happening in the FPGA. He came back and said, you know, I can't find anything, what is it?

**Dave Jones:** And so we looked around a bit more, and I looked, I was scratching my head, I was looking at this waveform that, you know, I knew it was shorted somehow. And, but we were driving the output like this, and then we looked at the schematics for the chip, and this was supposedly an input signal.

**Dave Jones:** So we, you know, we're driving an input with a, you know, with what looks like short, where is it shorted? And it finally clicked after a while that, aha, on a lot of these devices, not just I2S, but, you know, all sorts of chips these days, the pins can be used for dual purpose.

**Dave Jones:** They can be both inputs and outputs, depending on what mode or something like that it's in. So we checked out the circuit diagrams for it, and it showed it was only an input. But as it turns out, I checked the datasheet, I double checked, and the datasheet, sure enough, this pin we were probing and getting this short on, was both an input or an output, depending on what mode you were actually in.

**Dave Jones:** And this had another control line here, I think it was an I2C line, and as it turned out, when this device powers up, this is actually an output. And it only becomes an input after you send the correct codes through to it, to actually, you know, to actually switch it to an input.

**Dave Jones:** So as it turns out, it was a problem in the code, in the processor, that was driving the I2C line, a totally unrelated line, setting up this chip, and it hadn't set up this pin properly as an input. So another part of the FPGA design, another part of the software, was driving it this way, and this was an output, so we actually got this shorted-like signal.

**Dave Jones:** And this pin just happened to output some clock signal or something like that, that's why there was this clock signal superimposed on it. So there you go, that can be a real trap for young players. Just be careful of it next time, just because a circuit diagram might show that the pin's an input, it may not, or an output, it may not be.

**Dave Jones:** It might be dual-purpose, especially on microcontrollers and things like that these days. So just be careful of it. Dual-purpose pins. They can be a pain in the butt, and they can cause all sorts of hardware, it can take you hours to debug, or days, and you might think it's a hardware problem, and it's not.

**Dave Jones:** It's software. Dual-purpose pins. Bit evil, but flexible.
