---
video_id: iDF3qy23zyM
title: Compiler Optimisations & Why You Should Care
url: https://www.youtube.com/watch?v=iDF3qy23zyM
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 13, "2": 35, "3": 56, "4": 74, "5": 85, "6": 111, "7": 133, "8": 152, "9": 181, "10": 198, "11": 214, "12": 232, "13": 258, "14": 276, "15": 292, "16": 308, "17": 336, "18": 353, "19": 364, "20": 382, "21": 398, "22": 425, "23": 442, "24": 461, "25": 477, "26": 495, "27": 511, "28": 526}
---

**Dave Jones:** Hey, so I'm going to be talking about various compiler settings for embedded systems and why you might care, why you might want to do one thing over another, what are the trade-offs, what are the benefits. And I'm going to start at a pretty basic level.

**Dave Jones:** I don't know how far I'm going to go with this. So let's just get started. So first I'm going to be talking about just compiler optimizations. I'm going to just be focusing on two of the main ones. And these, you could argue which of those two

**Dave Jones:** are, because there's various transformations and all that you can do. But I'm just going to be talking about inlining and loop unrolling, because when with their powers combined, your binary size explodes. So why would you want to inline? Why would you not want to inline?

**Dave Jones:** So the reasons you would want to inline is because maybe you have a program that is very speed critical. Every time you call a function, there is a time associated with that call. It takes a while for the program count to move over there

**Dave Jones:** and it takes a while to put items on the stack. And probably less than you'd think, actually. It's very fast. And a lot of the times the parameters of a function don't need to be copied or whatever. But there is an associated overhead with a function call.

**Dave Jones:** For example, with the assembly instruction call in x86. So like, there's an overhead, right? So what about with, so that's why you would want to do it. You remove that overhead. You don't need to push things on the stack so much. You don't need to pop things from the

**Dave Jones:** stack as much. Anyway, so if you, see there's a penalty for doing that. Imagine you had an LCD library. And within that library, you had some geometry drawing functions. For example, let's just, I'm just going to make code up. This is all pseudocode, not a library I have.

**Dave Jones:** So let's say there's a thing called screen, a type, and screen. And I want a screen.clear, whatever. And then I want to draw a rectangle. Draw rectangle. And the rectangle is going to start at zero, zero. It's kind of a width of 100 and a height of 200.

**Dave Jones:** Now, if I was drawing four rectangles, and this was not inlined, the binary from drawRectangle, the code that that compiles to, is included once in the binary. The call is included four times. Fair enough. You get the overhead. But you actually save, you use a quarter of the memory

**Dave Jones:** because you're not inlining them. Now, it's not going to actually be a quarter. It's going to be less than that a little bit for many reasons. But the gist of, the point I'm trying to make is that by actually having the function call, you no longer need to include all this.

**Dave Jones:** So there's been a trend in computers to have enormous amounts of RAM. And everyone just wants to increase the lowest level caches on processors. And the bigger it gets, the more you can inline, the more aggressively you can justify inlining without really hitting

**Dave Jones:** any limits. So in a lot of compilers, you can do things like attributes, like attributes that tell the compiler to always inline. So certain functions like drawRectangle, if you needed to call it extremely quickly, don't know why you would, but maybe you need a certain

**Dave Jones:** frame rate or something. You can tell the compiler always inline, attribute always inline. You can't write, strangely, in C and C++, you can't do this, inline void my function. This function, depending on what's inside here, may or may not inline. This keyword is a compiler hint.

**Dave Jones:** So that's something that most people don't realize. Inline does not mean it will be inline. Always inline does, but even then, it doesn't mean always inline because some functions can't be inlined. Yes, really. And in fact, in GCC, you'll get a warning about it.

**Dave Jones:** You'll get a warning that says, cannot always inline. So if I inlined this, the binary for this would be included four times. So four times the memory, a bit less, but. In these examples, I'm going to say that's the flag 03 for the one that inlines

**Dave Jones:** everything, uses much more memory, and OS for the ones that keep the function call and uses less memory. So at the cost of speed, you save memory with the flag OS. And 03, which is the optimize for speed, basically, you sacrifice memory for speed.

**Dave Jones:** It's a tradeoff. You might have enough memory on your system to do 03, even in an embedded system. So there are plenty of other settings, and a lot of them are related to debugging. And the thing about 03 and OS, for that matter, is without some other flags, you get no debugging information.

**Dave Jones:** Actually, I think it might by default have them, but your setup may not. So you need another flag, which tells it to have debugging information. And if you don't have that, then nothing happens in the debugger. You can't step through your code, you can't put break

**Dave Jones:** points and stop there and view variables and all that nice stuff. You can't do that without debugging information. And the debugging flag very rarely changes the binary, and I thought it would never, but apparently it might. And I'm going to show you the example here.

**Dave Jones:** So here I have an example with string. We have 44 lines of assembly. Okay. And I have no debugging information included. If I go G3, all the debugging information included, I'm doing this. As you can see, the assembly hasn't actually changed, not by one line.

**Dave Jones:** But now, this tool here, Compiler Explorer by Matthew Godbolt, is able to determine where each line of code is represented in assembly. And that's sort of how break points and all that works. So, again, changing this flag did not change the binary. What about loop unrolling?

**Dave Jones:** Loop unrolling, in this case, is another form of optimization that you do see when you use the O3 flag. And it produces more binary. And, like, this, with loop unrolling, is exactly the same assembly. Because at compile time, this is just copied four times, and this line

**Dave Jones:** is deleted. Loop unrolling. You've unrolled it. So imagine if you had inline code with loop unrolling. That means you could have, now this doesn't happen in practice because compilers are smarter than this, but you could conceivably have, with a dumb compiler, 100 duplicates of the drawRectangle code with these constants plugged in.

**Dave Jones:** It is a complete waste. So, obviously, in that case, instead of doing that, you would probably just use the call. The call function. That's what happens in O3. That's why you get more binary. You get more inlining and more unrolling. And you also get a bunch of other optimizations

**Dave Jones:** which make it certain variables just vanish into thin air and lots of other, like, algorithmic optimizations, which I'm not going to talk about at all. Now, here's where it became interesting. It became interesting when I was compiling the microsupply code and it started blowing the stack when I was using release mode with the OS flag.

**Dave Jones:** It would work and not blow the stack when I had debugging mode enabled. But it wouldn't when it was disabled. Now, this is really strange to me. See, I don't, I do not know the answer to this. Fortunately, I had enough memory in the product to just go, yeah, screw it.

**Dave Jones:** I'll optimize with O3 problem solved. Stack not blown. And the other solution I have is just reduce my buffer sizes. It's very easy to do that. I increase the buffer sizes based on the amount of stack I had available, so I can reduce it easily too.

**Dave Jones:** But I wanted to make good use of my hardware, which means making good use of your stack. And, you know, clearly I didn't leave enough margin, but really strange. So if anyone has any ideas down below, leave a comment because I don't know why that would be the case.

**Dave Jones:** Debugging mode does not get involved with any of them as far as I know. So help me. Anyway, yeah, have a good day. Bye.
