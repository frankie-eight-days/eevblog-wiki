---
video_id: iwUqE6ZJqgA
title: GCC Embedded Linker Followup
url: https://www.youtube.com/watch?v=iwUqE6ZJqgA
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 12, "2": 34, "3": 52, "4": 75, "5": 94, "6": 122, "7": 142, "8": 156, "9": 181, "10": 200, "11": 219, "12": 240, "13": 256, "14": 289, "15": 303, "16": 319, "17": 354, "18": 374}
---

**Dave Jones:** Hey, so this is a follow-up video to update you on what has happened with the LD linker issue. So the last time I was working on this, the LD linker was crashing and it was crashing for a very strange reason, an undocumented error, LD exit status 253.

**Dave Jones:** Turns out that signal 11 on Linux being on various distros or using different things in Linux didn't help at all. Using a different IDE didn't help at all. Using dozens of different compiler and linker flags didn't help at all. So what was the issue?

**Dave Jones:** Well, the issue was related to a few different things. The issue was stack related. It was a stack overflow. The linker was having a stack overflow, but it's interesting why. Interesting why a stack overflow could happen in a linker. So the answer lies in

**Dave Jones:** something called VLAs. This is a GNU extension. This isn't part of the C++ language, not part of the C language, but it is part of the GNU compilers, the GNU toolchain. So why are they a problem? Well, a VLA is something that is allocated on the stack and on various operating systems, Linux,

**Dave Jones:** Windows. The stack has a fixed size unless you specifically tell it otherwise. And by the way, people who are thinking pass the flag into GCC, no, that doesn't do what you think it does. That applies to the XE it's compiling. Anyway, so I've tried that anyway.

**Dave Jones:** It doesn't work. Well, a VLA is a GCC extension and a good compiler will tell you that. It will tell you warning, ISO C++ forbids variable length arrays and this is the root cause of the error. What is a VLA? A VLA is an array whose size can be defined by a parameter or a variable.

**Dave Jones:** It is defined on the stack, unlike the vector, which is defined on the heap. This vector. And it has its advantages on that you can keep everything on the stack, but it has massive disadvantages. Some insecurity, and the one that I was facing was that

**Dave Jones:** if someone were to put a very large P size value here, then you can just completely fill the stack and crash the program and the program will have no awareness that that's happened. It might just end, but it won't be able to report a sensible error.

**Dave Jones:** So, that's the problem. And here's GNU's libivity implementation and this is roughly what caused the error. So, you can look at this CDMangle print callback, got some options, and you've got a bunch of things in the parameters, then you've got this DPI variable.

**Dave Jones:** It's a struct and it receives its information from print in it. Okay, fine, whatever. But, you'll notice this. DPI, numSaveScopes, numSaveTemplates, has no maximum. And it's clearly not tracking how close it is to the stack limit. So, without the program being aware at all, it can completely fill the stack and blow the program.

**Dave Jones:** The program will crash and end. So, that's what was happening. GCC 7.2 was producing an enormous amount of symbols and that caused the VLAs to be loaded with a very large number of items. Now, symbols can be quite large in and of themselves.

**Dave Jones:** And GCC was producing way too many of them. Now, GCC 8.2, as far as I'm aware, still uses VLAs. Actually, I think it uses this same code here. But, the compiler itself produces far less symbols. So, I no longer have to change the stack size in

**Dave Jones:** Windows and Linux for GCC 8.2. Okay, so Linux and Windows actually use stack very differently. On Windows, the stack size, the maximum stack size, is defined by the executable itself. This means that ahead of time, programmers need to know how much stack a program could conceivably use.

**Dave Jones:** On Linux, they don't. This is a good and bad thing. And I won't go into why. But, basically, it was smacking through the stack on Windows. And the reduction is an order of magnitude in 8.2. So, I no longer have the error. And in the process of debugging the problem, I ported the program to a CMake

**Dave Jones:** project. And this means you can now develop, if your developer wants to contribute to the project, once the product is out, you can contribute via your own CMake project on Linux or Windows. It's very easy. I use VS Code because it works with CMake no problem.

**Dave Jones:** And also, there's Visual Studio Code on Linux and Windows and Mac and probably some other platforms as well. They seem to put it everywhere. Everything the Chromium browser was on, Visual Studio Code is on. So, okay. And just for the satisfaction of it, let's see it build with no errors.

**Dave Jones:** So, let's clean it and then let's build. It's gotten stuck. Hooray! Success. So, as you can see, the error is now gone. So, if you're having a similar error, if you're having a signal status 11 from Linux or you're having exit status 253 on Windows,

**Dave Jones:** the solution is to do one of two things. One, compile GCC-LD yourself with custom linker size with your own stack size defined. Or you can upgrade to GCC, the GNU toolchain 8.2, and it should fix itself anyway. So, I hope that was interesting.

**Dave Jones:** Bye. Bye.
