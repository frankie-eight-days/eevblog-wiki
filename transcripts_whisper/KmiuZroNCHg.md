---
video_id: KmiuZroNCHg
title: EEVblog #83 - Do You Suck At Hardware Or Software?
url: https://www.youtube.com/watch?v=KmiuZroNCHg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 50, "3": 65, "4": 89, "5": 108, "6": 125, "7": 142, "8": 165, "9": 190, "10": 211, "11": 232, "12": 253, "13": 274, "14": 297, "15": 313, "16": 331, "17": 348, "18": 369, "19": 395, "20": 416, "21": 444, "22": 466, "23": 487, "24": 502, "25": 524, "26": 544, "27": 569, "28": 596, "29": 609, "30": 631, "31": 643, "32": 664, "33": 681, "34": 700, "35": 721, "36": 742, "37": 758, "38": 774, "39": 789, "40": 815}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for another DriveTime rant. And once again, this one comes from the forum that I read this morning, so thanks to whoever posted it.

**Dave Jones:** What it basically is, is hardware versus software. And, well, which one should you choose as a career? Basically, which one, well, in particular, which one should he get into? He's got a Bachelor of Computer Science majoring in electronics or something like that. And it sounds like he's got some experience and he's been getting more into the software side of things.

**Dave Jones:** And I find that, well, he found that, well, he doesn't really, well, I think his own words were, I suck at it, or something like that. So he sucks at software and he wanted to know, should he, you know, start specialising in hardware?

**Dave Jones:** Or can you actually master both? Is it possible to actually master hardware and software? And I thought it's a real interesting question. So let's talk about it, shall we? Hardware versus software. Now I've got a new lapel, yet another lapel microphone. It's a Sony wired one this time.

**Dave Jones:** I'm not using the wireless, so I hope the audio works fine. It's a mono one. I haven't actually chopped the lead to turn it into a stereo one. So it feeds the signals into both channels. That's actually a problem. You buy a new mic and you plug them into these camcorders, all except stereo input.

**Dave Jones:** But if you get a microphone with a mono plug, it only feeds it into one channel. And that's really annoying when you go to edit. Because you have to actually duplicate the audio on the other channel to produce stereo output. And it's another step and it's really annoying.

**Dave Jones:** So generally when I get a new mic, I just chop the plug off and wire that mono signal. So it just feeds it into both channels. And I find that's just much easier than having to post-process it. Anyway, enough of that. Hardware versus software.

**Dave Jones:** Now the first aspect of that is, the first question is, is it possible to master both? And well, I'm not going to say no. Because I do know some guys who are brilliant at both. But generally, no. The answer is no. You can't master both.

**Dave Jones:** It's the same with anything. I mean, you can master microcontrollers or something. And then you can not work on them for five years and you can forget a lot of stuff. And same with software as well. You can be an excellent programmer. But then if you go on and do something else for five years, you can lose a lot of your skills.

**Dave Jones:** And it takes some time to pick them back up. Or the tools change in that time, which is another common thing. You know, the industry shifts and all the tools change and things like that. So basically, no. I don't think you should try to master both hardware and software.

**Dave Jones:** But basically, pretty much everyone in electronics design these days should be able to do at least some software. Some microcontroller software in C or something like that. Or maybe even a bit of VHDL. But you should be able to do some programming, even if you suck at it.

**Dave Jones:** Like this guy said. And sometimes I suck at software too. I think I'm reasonably good at C, I think, in embedded environments. And I can do PC software and Visual Basic and stuff like that. But anything more advanced. All this latest web stuff.

**Dave Jones:** Databases and web and Java. And all these weird sounding names for all these web-enabled application programming languages or scripts or whatnot. I have no idea. Zoom. Straight over my head. Really. So I don't think there's any way that I'm going to master that.

**Dave Jones:** So I'm not even going to try. So pretty much I stick to, personally, I just stick to hardware with a bit of embedded plain vanilla C thrown in. Like C++. I have no idea about object-orientated programming. I suck at that too. So I'm not going to try and master that.

**Dave Jones:** Because the problem with trying to be very good at software is that there's so many geeks out there. And nerds who are graduating with computer science degrees. And you just won't be as good as them. They're just brilliant. And there's so many of them.

**Dave Jones:** And they flood the market. So, you know, if you're trying to specialize in software, you have to be really, really good and really, really talented at it. I think, anyway. So that's important. And if, you know, if basically this guy on the forum said, well, you know, I pretty much suck at it.

**Dave Jones:** I realize I'm not very good at software. Well, I think that's a dead giveaway not to try and specialize in software anymore. If you think you suck at it, go with your gut instinct, really. And probably switch to hardware. Spend more time on the hardware.

**Dave Jones:** Now, here's the other aspect of the question that, you know, what was it? Let's see if we can frame the question better for the purposes of this exercise. Which is to get the, is hardware, you know, should you specialize in just one particular area?

**Dave Jones:** Like PCB design or FPGAs, like focus on that area. And this guy's afraid that if he doesn't spend time focusing on one area, he'll never be a master of anything, really. And I think that's pretty much true. You really have to get down, dig your heels in, and do some, you know, if you want to get into PCB design, you've got to do some serious PCB design.

**Dave Jones:** You can't just throw down a few, you know, triple five timer chips on a board and go, right, I'm, you know, I'm experienced at PCB design. It's just, you know, it's just not going to happen. You really have to get down and do some meaty projects before you can consider yourself, you know, competent in that particular area.

**Dave Jones:** And if it's PCB design, you know, you've got to do high speed PCB design. You've got to know all about signal integrity, EMI, DFM, design for manufacturing, design for manufacturability. You've got to know how the PCBs are manufactured, assembled, tested. And there's a whole, you know, there's a whole slew of different things you've got to know about just for, just to become a really good PCB designer.

**Dave Jones:** And the same thing with FPGAs, for example. You know, you can't just, you know, slap down a hundred lines of VHDL and think you know all about FPGAs. It's just, you know, it's not that simple. But once again, you can know all about FPGAs.

**Dave Jones:** Like I'm one example. Like I know one of my day jobs is dealing with many different varieties of FPGA hardware and designing them and laying out the boards. So I know intimately all about FPGAs. But can I do VHDL? Barely. You know, I pretty much suck at VHDL.

**Dave Jones:** I could probably learn it a lot better, and I probably should. But I realize I suck at it, so I generally try and avoid it, if at all possible. I just toss it over to the software guys who are, you know, who are much better at that sort of thing.

**Dave Jones:** And once again, if you want to master something like VHDL, for example, there's many ways to write really shitty VHDL code, let me tell you. It's really easy. You know, you can have all the experience. I know, you know, guys have been working on FPGAs, and girls, working on FPGAs for, you know, ten years or something like that.

**Dave Jones:** And churned out millions of lines of VHDL, but it's horrible. And the projects, you know, the end product is unstable. It's untested. It's, you know, it's not characterized properly, and it's, yeah, it's just crap. So really, just a simple aspect like VHDL, you think you can master it.

**Dave Jones:** But, you know, if you're not really, you know, trained to, or, you know, get experience in doing meaty projects that are, you know, actually peer-reviewed and tested and stuff like that, to find out if you've got any weaknesses in, you know, in actually developing VHDL, then you might never master it.

**Dave Jones:** So, yeah, hardware versus software. You know, I think there's just so many hardware, sorry, software people out there that, man, seriously, if you're on the, if you watch the EEV blog, then it pretty much means that you're interested in electronics and hardware. So, you know, to go specialize in software, I would, as a general rule, advise against it.

**Dave Jones:** But I know there are people who actually watch the blog, and they're mainly software guys, and they, you know, they used to do hardware, or they like to keep their hand in. That's why they're actually watching the blog. Woo-hoo, we're going through the M2 tunnel.

**Dave Jones:** Whee! It's dark and spooky. I'm using auto-exposure this time, by the way, because the manual exposure didn't work. It's very hard to manually expose and get me in, get me exposed properly, as well as the bright outside sun. It's just, you know, it's just almost impossible.

**Dave Jones:** So, and I get complaints that people want to see out the window and stuff like that. I don't know why, really. In fact, I don't know why people watch this video. That's why I now do a podcast version and audio version of this.

**Dave Jones:** So if you just want to listen to the audio, you can certainly do that. So, hardware versus software. Yeah, my advice to this guy in the forum is basically go stick to hardware, and yes, go specialize in one or two areas. Or spend, you know, six months, 12 months specializing in a couple of areas and see how you go.

**Dave Jones:** Because really, ultimately, I think I may have mentioned this before, ultimately, if you're just a real generalist in electronics, you're probably not going to get beyond the gopher level of just, you know, being the gopher guy around the lab or something like that.

**Dave Jones:** Because ultimately, you've got to specialize in at least a couple of aspects of electronics design to actually be, you know, to be valuable and to be useful. So whether or not it's, you know, whether or not it's PCB layout or VHDL and FPGAs,

**Dave Jones:** or whether it's embedded software and operating systems, or whether it's, you know, power electronics, motor drives, whether it's RF, you know, or audio, stuff like that, or, you know, system level design. Heck, you don't even have to design electronics. You can be a, you know, a system engineer or something like that.

**Dave Jones:** And you can, you know, more of that system level design and things like that. So, yeah, there's many, many areas that you can specialize in, and you should. You should try and specialize in something. Otherwise, you're probably going to find yourself, you know,

**Dave Jones:** not being suitable for a particular job. Because if I'm sorting through, you know, if I'm hiring someone for a job, and I'm looking through resumes, I'm looking through hundreds of them, you know, I'm going to sort it out. You know, if I need a guy who can, you know, design microcontrollers or design FPGAs,

**Dave Jones:** I'm going to look for that specific experience, either in their job history or in other personal projects they've worked on. I don't, you know, I don't want to, I'm just going to, you know, if you just say, oh, yeah, I've studied FPGAs at uni, I've done a course,

**Dave Jones:** I'm just going to toss your resume in the bin, because I know you're not going to be able to do the job. Right? You know, I don't care that you know about them. You know, any good electronics person should know about, generally know about, you know, a good lot of aspects of electronics,

**Dave Jones:** but do you specialize in it? Can you actually do the job? And, you know, I want examples of real projects that you've actually done. So, there you go. I hope that's useful. And once again, it's another stream of consciousness rant, and I have no idea if what I said was comprehensible or not.

**Dave Jones:** But, yeah, see you next time.
