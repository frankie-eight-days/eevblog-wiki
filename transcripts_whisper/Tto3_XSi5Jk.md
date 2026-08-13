---
video_id: Tto3_XSi5Jk
title: EEVblog #65 - Umm, I Design Computers
url: https://www.youtube.com/watch?v=Tto3_XSi5Jk
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 31, "3": 52, "4": 65, "5": 88, "6": 111, "7": 130, "8": 153, "9": 176, "10": 193, "11": 205, "12": 224, "13": 247, "14": 271, "15": 290, "16": 314, "17": 342, "18": 363, "19": 387, "20": 407, "21": 426, "22": 442, "23": 458}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, yes, it's another drive time blog. I'm heading to work again and I thought I'd just rant on again because quite a few people

**Dave Jones:** actually, I got a lot of feedback on the drive time rant and a lot of people thought it was a good idea. There are a few people who thought it wasn't a good idea, but oh well, I'll keep it on topic and here we go.

**Dave Jones:** Now, I've actually got a new camera mount for the window. It's really quite snazzy. I might have to take a photo of it. I don't know how it's going to work or not, but I'm actually filming this upside down, so I'll have to flip it back over in the editing.

**Dave Jones:** So, once again, I think I've got the settings correct, but oh well, we'll find out later. If it doesn't work, you won't see it. If it works, you'll see it. So, what I thought I'd talk about is something that always seems to come up in, well, just everyday life.

**Dave Jones:** People ask, what do you do for a living? And well, you say, I'm an electronics design engineer, and the first reaction is that their eyes usually just roll in the back of their head, and what? What is that? Something to do with computers?

**Dave Jones:** What is it? And, you know, you either, you wait. Generally, I weigh up the person to see if they're the least bit interested, and if they're not, if it doesn't seem that they're the least bit interested in that at all, then I'll just say, oh, I design computers, or, you know,

**Dave Jones:** I design robots, or I design, or I design mobile phones, or, you know, something a bit more technical might be, or I design the circuit boards which go into computers and mobile phones, and they go, oh yeah, okay, and they nod, and, you know, think that they understand, because most people have actually

**Dave Jones:** heard of circuit boards, so, you know, if you mention that, then that generally, right, okay, they sort of understand and get the drift, and then a lot of the reaction you'll get is, oh, so you can, so you fix TVs and things, and it's like, no, that's a TV repair technician, well, that's a TV service

**Dave Jones:** technician, I'm, I actually design, and then you've got to say, I design TVs, because otherwise, they just don't understand, they just don't get it, so, yeah, it's really awkward trying to explain being an electronics design engineer to someone, it's just, I've got to come up with a decent

**Dave Jones:** comeback that I stick to all the time, because usually I make something up on the spot, because I'm taken back, and I come up with something with a different sound and explanation every time, that's, that's crazy, and then, yeah, I, you always ask, if they hear you're an electrical engineer, an

**Dave Jones:** electronics engineer, or just sort of any sort of engineer, they go, oh, you can fix, I've got a broken TV, my TV's broken, can you take a look at it, can you give me a quote on how much it is to fix, and

**Dave Jones:** then you've got to explain to them that, no, I can't really fix TVs, oh, I could, but it would take me a very, very long time, because I'm not familiar with them, and I'm, and I don't have access to the parts, really, you know, you've got to explain to them that you have to, that they should, they're much

**Dave Jones:** better off taking it to their local service tech, who can, TV service tech, who can, who can fix the thing 10 times quicker than I can, because that's, that's just the way it is, this was actually brought up on the forum yesterday, is, you know, somebody asked, can I fix, you know, I'm,

**Dave Jones:** am I any good at fixing TVs, and hi-fis, and other bits of consumer gear, and well, the answer is, no, no, I'm not ashamed to say that I suck at it, because, you know, I'm very good at, I think I'm very good at troubleshooting things, but if it's something I'm not familiar with, if it's something

**Dave Jones:** I haven't seen before, then, well, you, you're going to look like a turkey, and you're back to square one, you can go through the basics, of course, but, you know, that doesn't really help much, because, well, you know, you might find the fault easily, but if it's something more detailed, then, you know,

**Dave Jones:** a repair technician who's familiar with that gear, who does, who repairs them day in and day out, will be infinitely more efficient at finding, and diagnosing, and fixing the repair than I would, you know, it's just, that, that's just the way it is, I mean, my, my first job, actually, was, well, part of

**Dave Jones:** my first job was testing, and repairing, testing, and troubleshooting, closed circuit television, CCTV, slash, video switching, slash, alarm equipment, that was my, that was my first job when I was 17, and, and I got, I got very good at it, it was a very niche product, and, well, it's, I could, I could

**Dave Jones:** have easily said that, at that particular time, I was the best person in the world, the most efficient person in the world, to fix that particular, um, bit of gear, because, well, I was the most familiar with actually repairing them, uh, if I went back now, I'd, I'd be starting from square one, you know, that was,

**Dave Jones:** that was, uh, 20 years ago or so, and, um, that's just the way it is, it's, just because you're an electronics engineer, and just because you've, you know, you've, you've studied electronics, and electrical design, doesn't, doesn't mean that you can fix stuff, uh, troubleshooting is an art in itself,

**Dave Jones:** it really is, um, and, and, you know, there are basic, uh, rules to follow, I mean, the, the golden, the first rule of troubleshooting is, thou shalt test voltages, and, well, that's the first thing you do, you check the voltages, you check the voltage rails, and make sure everything's okay,

**Dave Jones:** and then you, then you work from there, so there, there are basic steps to troubleshooting gear, but in the end, it comes down to being intimately familiar, that person is, no matter how, it doesn't matter if they're not educated at all, they will beat the pants off you

**Dave Jones:** at troubleshooting that particular gear, it's the same with design, just because you've, you know, just because you've studied your degree, or done your course, or whatever, um, you may have been studying, or like, you may have been doing electronics design for 40 years, or something,

**Dave Jones:** and it, and it makes no difference, some guy can, some uneducated guy can come along, and will know something, um, about a particular aspect of electronics design, that, that you won't, because you've, you've never, you've never touched it, or you haven't touched it in 20 years,

**Dave Jones:** or, you know, you haven't studied it in, since, you know, 1970, or something like that, so, familiarity, that's, that's what it's all about.
