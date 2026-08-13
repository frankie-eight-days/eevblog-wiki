---
video_id: ZvoB3Zg1H4g
title: EEVblog #88 - There's More To Electronics Than Just Circuit Design
url: https://www.youtube.com/watch?v=ZvoB3Zg1H4g
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 24, "2": 46, "3": 60, "4": 92, "5": 106, "6": 136, "7": 158, "8": 179, "9": 207, "10": 225, "11": 253, "12": 270, "13": 290, "14": 307, "15": 317, "16": 333, "17": 352, "18": 372, "19": 388, "20": 403, "21": 426, "22": 443, "23": 460, "24": 480, "25": 498, "26": 522, "27": 536}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for another stream of consciousness drive time rant and once again this one comes from a user feedback or a user comment and it has to do with my last blog about the electronics

**Dave Jones:** design merry-go-round and how you can spend so much time searching for and optimising parts for things like cost. In particular, that was what my current project that I did an example of was very cost sensitive. So I was doing all this work to try and find the lowest cost components.

**Dave Jones:** And his question was that why am I bothering to do that up front? Why is this my first task to find, to go and search, spend weeks searching for all these low-cost parts? Why don't I just build the circuit, build the prototype and then optimise for cost?

**Dave Jones:** And well, I think that's an excellent question and let's talk about it. Now, the thing you've got to realise is that electronics design isn't just about circuit design. If it was, then sure, you would design the circuit first, you'd build your prototype, you'd troubleshoot it and debug it and then you'd

**Dave Jones:** build another one and then you would optimise for cost. And that's the traditional way that you would do it. You get your circuit working first but in some cases for a lot of projects, especially the one I'm currently working on, the circuit is borderline trivial.

**Dave Jones:** I know the circuit's going to work, it's no problem at all. But the secret, the secret source, so to speak, in this design is the low cost and novel nature of how it's implemented, I think, anyway. So that's why the circuit, you know, there's no point me building it up and seeing if it works

**Dave Jones:** because I know it's going to do what I want. And if cost is my overriding factor for the design, then of course it makes sense to actually do that up front and spend all your effort on it. I haven't prototyped a thing but I'm going to all this effort to see if I can meet what I deem to be

**Dave Jones:** a suitable bill of materials cost target. And if I can't do that, then I think I'm going to change the design aspect completely or I'm just going to scrap the project and go on to something else, I think. Because if I can't make it for a certain cost, then I'm probably not going to bother with

**Dave Jones:** this design. So it's actually important to do all that stuff up front. Now this thing about electronics design not just being about circuit design, you know, it's also the same for a whole host of other products and niche little industries. One example I can give is the current calculator

**Dave Jones:** design I'm working on, or my calculator watch project that you've seen. Now that's where, you know, the circuit is trivial. It's a microcontroller, it's some switches and an LCD and some software. In fact, most of the effort goes into the software in a project like that.

**Dave Jones:** But, you know, anyone can do that. But to develop a novel form factor, a calculator is ultimately a hardware form factor. And if you can't get that form factor right, well, there's really no point doing it. It's just going to be an ugly breadboarded circuit or some, you know, just an ordinary looking PCB with an LCD

**Dave Jones:** and some switches on it, which is, you know, pretty stupid really. When you think about it, it's pointless. Anyone can do that. Everyone does that as a, you know, either a hobby project or a school project or something like that. There's no point to it, apart from, you know, the learning aspect.

**Dave Jones:** So if you want to produce a really good product, you know, one that meets a little niche market, often the form factor or the functionality is going to be the key thing, or price or something like that. So if you don't put all the effort, you know, 90% of your effort up front into that,

**Dave Jones:** then your projects, you know, you could spend a lot of time on this project and it can just be doomed to failure because you're never going to meet that cost target. And also when you build a circuit up front and then, you know, you prototype it, build it, and then you go, okay, let's now

**Dave Jones:** optimize for cost. Well, you know, there's only so much you can do at that point because you've got to find you're already, you know, you might find you're already locked into certain footprints, you're locked into certain design circuit topologies, and things like that.

**Dave Jones:** So if you want to, if you suddenly find a lower cost part that's one-fifth the price or something like that, but it's a different, you've got to change your circuit topology, well, you're back to square one, you've got to re-prototype and redo the whole thing.

**Dave Jones:** So a lot of that effort that you went into at the start is just wasted. So really, electronics design is a lot more, can be a lot more than just circuit design. Remember that. It's the same thing with a project case or something like that.

**Dave Jones:** Often, I will, I've mentioned this before somewhere, but I will spend a lot of my time just choosing a suitable case because that can make or break the product. If you build up your board first and then try and fit it to some case later, it's usually going to be a, it's usually going to be a bodge,

**Dave Jones:** and it's going to be ugly, and it can make your product, you know, it can turn your winning project into a loser. So, or a very unattractive project. So it's important to put effort into, say, the case up front. So I'll often, you know, spend a week looking for a suitable case for a

**Dave Jones:** project at the start. So there you go. There's something to think about in that respect. So that's the end of that. Now, I just posted on the forum before I left that I'm thinking about doing a live EEVblog event via Ustream or BlogTV or one of those other things.

**Dave Jones:** I think, I've already set up an account on both, I think, and, you know, I'm thinking about doing this live show. So I have no idea if anyone would want to watch such a thing. So if you do, let me know, and if you don't, let me know too.

**Dave Jones:** If you think it's a stupid idea, I'm just wasting my time, well, let me know. I think it'd just be fun. I have no idea what the format would be or anything like that, probably just a question and answers feedback, because you can get like a live,

**Dave Jones:** apparently the actual viewers can type in stuff live and things like that, so I can see what you're typing as I'm actually filming it. I'm going to have to do a quick trial, just a secret little trial one to actually, just to test out the technology and see how it works and things

**Dave Jones:** like that, and then I might go for say, you know, like a half hour live show or something like that. Um, no idea what'll be in it, just be off the cuff as usual, no script, it'll just be based on any questions people throw at me, or maybe I'll just show a bit of gear I've got or something

**Dave Jones:** like that. So let me know if that's a good idea, and we'll give it a go, because it seems to be, you know, quite a few other ones, quite a few other bloggers and things, they all seem to do these live shows. I'm also not sure how popular they are, but everyone seems to be jumping on the

**Dave Jones:** bandwagon, so I thought, hey, why not, I'll give it a go at least once and see what it's like. So give me your feedback. The best time for me to do it is around 7am to 9am in the morning, just before I leave for work, because that's the time that I often, well, that's really most of the

**Dave Jones:** time I get to do the blog and work on things like that. So, you know, the wife's not home and it's just, it's just easy and there's no pressure, so I should be able to do that, and if it's a success, maybe it can be a weekly thing or something like that.

**Dave Jones:** So let me know your feedback. See you next time.
