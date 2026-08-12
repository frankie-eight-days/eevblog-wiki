---
video_id: 889TkOQmCjY
title: EEVblog #1296 - Alkaline Battery Leakage Testing 2 - Electric Boogaloo
url: https://www.youtube.com/watch?v=889TkOQmCjY
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 35, "3": 50, "4": 80, "5": 98, "6": 116, "7": 137, "8": 154, "9": 170, "10": 188, "11": 205, "12": 222, "13": 238, "14": 252, "15": 266, "16": 289, "17": 306, "18": 319, "19": 339, "20": 354, "21": 371, "22": 384, "23": 400, "24": 416, "25": 430, "26": 445, "27": 458, "28": 469, "29": 485, "30": 499, "31": 519, "32": 541, "33": 559, "34": 578, "35": 595, "36": 611, "37": 629, "38": 642, "39": 678, "40": 708, "41": 738, "42": 768, "43": 798, "44": 828, "45": 858, "46": 888, "47": 918, "48": 948}
---

**Dave Jones:** Hi, yes, it's alkaline battery leakage time again. I thought we'd revisit this after my previous video, linked in down below at the end and up on the card here, if you haven't seen that, where I go through some long-term, like, nine-month testing of various brand alkaline batteries to see if they leak.

**Dave Jones:** Unfortunately, that video didn't produce any results, so I'm going to redo it again. Yes, I'm glutton for punishment, with a different testing methodology this time. Check the previous video for how I did it last time. Anyway, I thought it'd be fun to redo it, and maybe we'll get some results this time.

**Dave Jones:** I just looked through, like, a random old battery box, and I found this Varta, this made-in-Germany Varta battery, and wow, that is a shocker. So, what you're looking... What you're looking at here is leakage of potassium hydroxide from the battery through the seal in the negative end of the battery, and that's where the seal is.

**Dave Jones:** There's no seal on the top. That's why you'll never see them, like, leak from the positive terminal of the battery. And so that eventually leaks out, and then that potassium hydroxide forms as carbon dioxide in the atmosphere, and that forms all these little dendrite-y growth crystalline structures that you see here.

**Dave Jones:** And it's rather funky to look at, actually. I do actually enjoy looking at that, and even though it kills all your gear that you've got these things in, never leave, like, discharge batteries long-term in your, um, any product, because this could be the end result, at least for, um, alkalines anyway.

**Dave Jones:** This, uh, phenomenon is particular to the chemistry used in alkaline batteries, but, ugh, crusty. So, once again, I just got a whole bunch of different, uh... brands and stuff. Uh, these are the only energizers that I could get from my, uh, local supermarket.

**Dave Jones:** They're currently, you know, in, like, social distancing lockdown. Anyway, that's, uh, Energizer Max Plus. I've got two different types of Duracells, because, uh, Duracells are notorious, of course, uh, for leaking, so I wanted two different types. Got the regular, uh, Copper Top and the Duracell Copper Top Ultra, uh, as well.

**Dave Jones:** Then I've got, uh, Toshiba Jobbies. I've got Philips, I've got Maxil, so all, uh, quality brands. Uh, Panasonic that I used last time. Two different Panasonics, actually. One's the E-Volta, uh, type, which is supposed to have leakage protection in it, so that'll be interesting.

**Dave Jones:** Uh, two different types of made-in-Germany Vata ones. Uh, one's a high-energy, one's just a long-life job. And then I've got a couple of, uh, just no-name cheapies. I've got Wallaby. What do you want to be? Want to be a Wallaby? I've got, uh, Colesbrown.

**Dave Jones:** Colesbrown, which is just like my local, uh, supermarket, uh, chain brand. So who knows who makes those? And just some generic eBay one called Juice Bank. And all of these have reasonable use-by dates on them. So that, really, the use-by date's not going to factor into it a huge amount.

**Dave Jones:** Um, although, you know, if they're expired, you wouldn't leave them in products. Uh, the self-discharge is, uh, probably going to kick in. But anyway, um, it's not a concern for this particular test. They're all welcome. They're all within date. And for those curious, here are the batteries that, uh, from the previous test.

**Dave Jones:** And I've, uh, kept them in filing cabinet in there, in the drawer. And you can see that there is no leakage on any of them. So even after all that time, yeah, bugger. So the difference to last time is that I just had these battery holders here.

**Dave Jones:** And I had one half-discharged and one fully-discharged because I thought, like, reverse-charging one of the batteries might have, uh, done the business. And you can see in the previous videos, um, that some cells did actually, uh, reverse voltage. They reversed charge. And that is actually a thing.

**Dave Jones:** But none of them leaked. So what I'm going to do is, uh, before I had a, uh, just this AA, um, 2AA holder and a single 47-ohm resistor on here. And I just left these on here indefinitely. And as I said, I think that load was too low.

**Dave Jones:** And, uh, it didn't have time for the pressure to build up inside the battery. And hence, uh, cause the leakage of the rubber. See, uh, plastic, rubber, whatever material they're using on the negative terminal of the battery. And that's how it leaks out.

**Dave Jones:** So I thought this time I would actually discharge the batteries either 90% or 100% in quote marks. Um, and then put, like, a light load on it. Like 100k, for example. So 101 volt divided by 100k is 10 microamps. And 10 microamps is a fairly typical, like, stand-product standby, uh, current figure.

**Dave Jones:** So I figure. Like, you know, because you get, uh, leakage in a lot of this equipment that has, like, soft power buttons and standby and things like that. Of course, you can get them with absolutely no standby power at all. But anyway, I thought I would, uh, so I'll change these to, uh, 100k.

**Dave Jones:** Please leave it in the comments down below if you don't necessarily agree with that limit. But, meh, it's something, right? We've got to try something. But because I've already got a whole bunch of these things already made up, um, I figure I will use these to actually discharge.

**Dave Jones:** The, uh, battery itself. Now, um, let's have a look at a data sheet for a typical alkaline here. We've got the Duracell Copper Top AA. Nominal 1.5 volts, 120 milli-ohms at 1 kilohertz for those playing along at home. Yes, if you want to measure the true battery impedance, you have to measure it, uh, AC at 1 kilohertz.

**Dave Jones:** Anyway, um, that's just a nominal figure. It's just like the ESR for capacitors, for example, is measured nominally at 100 kilohertz. Why? It's just a nominal figure. It's just, you know, you've got to pick up. It's just like, why does every oscilloscope have a 20 megahertz bandwidth limit?

**Dave Jones:** Even today, many decades after, you know, we've gone way beyond 20 megahertz analog bandwidth scopes, do they still have a 20 megahertz analog bandwidth figure? And why is that 20 megahertz, uh, the standard for measuring power supply noise, for example? Check out the specification.

**Dave Jones:** I know I'm going off on a tangent here. That's what I do. Sorry, can't help myself. Check out a power supply data sheet. The noise, for example, will be measured over 20. Why 20 megahertz and, well, bigger scopes have a 20 megahertz bandwidth limit.

**Dave Jones:** Why do they have a 20 megahertz bandwidth limit? Meh. It's just a, it's just an industry, a value the industry picked, um, and a de facto standard. Same thing here. 1 kilohertz. There you go. Anyway, so there's a couple of ways to discharge this battery.

**Dave Jones:** Could use a constant, uh, current load, for example. I've got, uh, several, uh, proper electronic loads here, of course. And, but doing, but driving. Draining every one of these batteries could take, like, 24 hours a pop, for example. And I want to do, like, dozens of these batteries.

**Dave Jones:** So, I could string them all in series, of course. I can get, uh, two of these per thing. And I can, like, wire them all up in series. And then do that because the load has, I think my load takes up, one of my loads takes 60 volts maximum compliance voltage or something.

**Dave Jones:** Or a couple hundred volts. Anyway, um, so I could string them all in series and do it that way. But the problem is, uh, I don't know the exact capacity of these batteries. And they're all different brands and different types. So, you don't want any to, sort of, like, um, reverse charge and be completely out.

**Dave Jones:** So, what I thought, I've already got these made up. They've already got a 47-ohm resistor on them. I thought I'd just whack, uh, two of them in series like this. And hence, I, there's less risk of one of them reverse charging, for example.

**Dave Jones:** Whack two in series, 47-ohm resistor, that should do it. So, let's go take a look at the, uh, curves down here and see how long it lasts. Uh, the Duracell, not all data sheets are going to have the same characteristic curves. The Duracells have constant.

**Dave Jones:** Constant current curves like this. Uh, these ones for low currents down here, 5 milliamps to 50, 100 to 1,000 milliamps over here. You don't really want to draw more than an amp from a AA alkaline, uh, because of the ESR up here. You can come and gutter.

**Dave Jones:** Anyway, we've also got constant power curves. Meh, whatever. But bingo, constant resistance curves. This is what we want. And look, we've almost got one that matches the 47 ohms on here. We've got 43 ohms. Meh, good enough for Australia, right? So, I could.

**Dave Jones:** Use the 47 ohms on here, but unfortunately, to discharge this thing, like, let's say 90% of its capacity is lost at around that 0.8 volts, uh, cutoff voltage. So, we're talking, I don't want to have to wait a hundred and, what, a hundred and plus hours, uh, for these batteries to discharge.

**Dave Jones:** So, I might just resolder these with, say, a 10 ohm resistor, for example. Don't want to make it too low, but, uh, a, a 10 ohm resistor and maybe constant resistance discharge them. That'll take. Say, after 24 hours, oh, maybe not 24, but say after 20, I'll come back after 20 hours and I'll check the voltage on the things and any that are, like, uh, really low, I'll have to, uh, take them out or whatever.

**Dave Jones:** But, yeah, I probably want to get it down to about 0.8 volts or, eh, something like that. I don't want to, definitely don't want to go beyond that. Basically, anywhere below 0.5 volts is, like, there's no, 99.9% of the capacity the battery's got.

**Dave Jones:** But, not necessarily due to the electrochemistry, no, I don't have a battery here, this is a battery holder. Anyway, imagine that's a battery, due to the electrochemistry on there and depending on how you discharge it and at what rate you discharge them, uh, you can actually, uh, recover some of that, uh, charge back into it after you've discharged it.

**Dave Jones:** So, you might think you've discharged it 100%, then you take the load off, if you discharge it vigorously, then you might find that, uh, some of the charge, like 5% or something, you may, there still might be, like, 5%. Um, and, or I'm sure all the chemistry experts, uh, can explain why that's the case.

**Dave Jones:** But, anyway, um, yeah, like, I don't know, I, I don't know, maybe, like, discharge them to a volt, maybe, something like, if I come back 20 hours, uh, later, so I come back, um, during the day tomorrow, it's, what is it now, uh, almost 3.30.

**Dave Jones:** So, just after lunch tomorrow, I'll go around, check all, measure all the voltages on all the cells, and, um, if they're around. At about a volt, I might actually take them out, say, and then I might do more, I might actually do another lot, down to 0.8, perhaps, um, because I want to get different types.

**Dave Jones:** I don't really know, this is kind of like trial and error here, I don't know whether I know at what point I can discharge them, like, fast, this is fast, over 24 hours, and then slowly discharge them with a 100k resistor, for example.

**Dave Jones:** So, yeah, I, I'm just going to suck it and see, and, unfortunately, I won't know. I don't know the results, for months, like, many, many months, six months, nine months again, something like that, so, uh, anyway, if you think I'm doing this wrong, I can always, uh, if you, uh, like, don't just go, oh, you should do this, like, if you've got some other proof, like, technical documentation, research, whatever, um, from various battery manufacturers or somebody else that shows that you're more likely to get leakage if you do this particular discharge or whatever, then please let me know later.

**Dave Jones:** Leave it in the comments, or send me an email, or whatever, because I need to, like, I, I've had a look, and, really, there's not, I couldn't find anything, so let's kind of just suck it and see here, um, pretty much, so, yeah, anyway, hopefully we'll get a result, ha, ha, Murphy won't let me, but, you know, we'll give it a go, anyway, so, basically, yeah, anything beyond 8.8 volts, I think, from memory, it's like, um, you know, 95% of the capacity of the battery's gone at 0.8 volts.

**Dave Jones:** So, that's what the batterizer tried to do, the batterizer tried to tap into that extra, like, 5% and get 800% the battery, the life of the, oh, God, let's not go there again, yeah, that died in the ass, I think this website's still there, but, but I don't think they sold many, they didn't get that big Kmart order they wanted, yeah, so let's just pull up some random curves here that I found, uh, AA alkaline cells discharged at 1 amp, here we go, you know, 500 milliamps or whatever, and you can

**Dave Jones:** see that, basically, once at 0.5, 0.6, 0.7, 0.8 volts there, you can see that there's very little area under the curve, we're talking, you know, like, as I said, like, 5% tops, and, as I said, at the higher currents, uh, for example, like, let's go, geez, 1 amp, you know, that's a decent discharge, and, uh, 0.5, oh, what's wrong, 6, 7, 8, okay, so 8 is in there, just the line's gone, that's, oh, that's got a reasonable amount of capacity left, I don't know, it's the

**Dave Jones:** area, but once again, you know, you're not gonna get much more than 5% of the capacity left at, uh, 0.8 volts, some people might argue I should discharge it to 0.5, but, yeah, no, no, I don't think so, I'd, I'd be happy with 0.8 max, um, I might even stop it at a volt, uh, for example, so most of the capacity is gone, and then we'll just slow discharge it with our 100k resistor at 10 microamps or so, anyway, that's the plan, let's suck it and see, so I think the plan will be, uh, two

**Dave Jones:** batteries of each particular brand and type discharged to 1 volt, and then I will, with the 4, with the 10-amp resistor, and then I'll put, I'll replace the resistor with a 100k, and then I'll leave both of those two in series of the same, uh, brand, and then I'll just leave it for months and months and months as it slowly, uh, effectively, or not quite self-discharges, but, like, really ultra-low load, like, as I said, like, sub-10 microamps, uh, standby load,

**Dave Jones:** and see what happens, but I think I'll also do another two sets of each brand and type battery, and then just leave them with no load, or I might just, yeah, might as well do two, because I've got to discharge two at a time, so I might just do two of each type, so therefore, I'll, I'll have four batteries of each brand and type, so this is quite a large, uh, test, it's not, you know, but ultimately, to get data from something like this, we're probably, we're really relying on luck here, we're relying on, uh,

**Dave Jones:** the characteristic manufacturing bell curve of the, uh, batteries to have, like, just outlying faults in the pressure vents in them, and that's really what we're trying to determine, so really, you know, I, you really need, like, hundreds of batteries at each type to get, like, to sort of guarantee a result that maybe, you know, like, one of them's gonna leak or something, you know, you've got, like, a 1% failure rate, so one in 100, for example, might leak, so, yeah, we're, I don't know, but if we can say get both,

**Dave Jones:** of a particular brand, uh, leaking through, uh, both of their negative, uh, terminals, then that'll be a, like, a really good result, given the number of cells that we're actually testing, that's, that'll be positive proof that that particular brand has, you know, not so good manufacturing on their end seals, uh, for example, so, anyway, that's the plan, but, uh, place your bets down below, set up a pool on the EVlog forum about, uh, take your bets of how, uh,

**Dave Jones:** whether or not I'm gonna get a result after six months, anyway, any updates will go on my secondary EVlog2 channel, if you're not subscribed to EVlog2, there'll be a link down below and at the end, and you should subscribe to EVlog2, because that's where I dump a whole bunch of videos, which you'll never see otherwise, and don't forget to subscribe to my library channel, because I might occasionally put, uh, some, uh, exclusive videos on there as well, if I'm gonna make exclusive videos, I'm gonna put them on my Patreon, uh, account, my supporters section on the forum, and, uh,

**Dave Jones:** and on my, uh, library channel as well, that's the plan, anyway, so, there's already an exclusive video over there, you should go watch it, my library channel, link down below, anyway, fingers crossed, catch you next time. Subtitles by the Amara.org community
