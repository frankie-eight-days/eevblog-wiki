---
video_id: cScVqD6eIaU
title: EEVblog #319 - Lead Free PCB Tinning
url: https://www.youtube.com/watch?v=cScVqD6eIaU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 15, "2": 28, "3": 52, "4": 72, "5": 92, "6": 110, "7": 124, "8": 144, "9": 160, "10": 180, "11": 196, "12": 222, "13": 244, "14": 264, "15": 292, "16": 308, "17": 332, "18": 352, "19": 372, "20": 392, "21": 412, "22": 432, "23": 456, "24": 472, "25": 488, "26": 504, "27": 524}
---

**Dave Jones:** Hi, just a quick follow-up video on the PCB tinning video I did last time. And if you haven't seen it, click here, you'll be able to watch it. It's fairly in-depth. Had a lot of people ask, can I try it with lead-free solder?

**Dave Jones:** Well, I didn't have any last time, but I've got some this time, hence why I'm wearing a green shirt. Eh, green seems to be the colour for lead-free stuff. So, let's give it a go. Repeat exactly the same thing we did last time for the lead one,

**Dave Jones:** with lead-free solder, and see what the differences are. And here it is. I went down to my local Jaycar store and picked up some Duratec by Sonartec, which is an Electus company which is all affiliated with Jaycar, all owned by Gary Johnston. Anyway, it's 99.3% tin, 0.7% copper, so there's no lead in it at all.

**Dave Jones:** And of course, it's got some copper in there, so that'll, you know, lower the resistance. And tin should be, in theory, lower resistance than the 60-40 lead stuff we used last time. So, let's give it a go. And it's green, of course. Gotta love it.

**Dave Jones:** Alright, let's get a baseline figure here. We're using the same Vero board as before, but we're using the strip on the other side. Bare 1 ounce copper, it's definitely confirmed as 1 ounce, just over 1 amp, constant current. We're getting 52.86 millivolts, which is 52.86 milliohms or thereabouts.

**Dave Jones:** So, we'll take that as our reference figure, and then we can add different layers of lead-free solder on here, and see how much it drops by. Alright, we'll start out here by doing a very thin coat, so that we'll get a minimum baseline, and then a maximum baseline, as we did last time.

**Dave Jones:** So, pretty much a minimum amount of solder that you can expect a wave soldering process to put on here. I know we're not doing wave soldering, but it's going to be pretty close, I think. So, let's give it a go. Just a quick safety tip, by the way.

**Dave Jones:** You'll notice that I was actually soldering what is effectively a live circuit here. We're passing current through this thing, and I was soldering at the same time. This is generally a very, very bad idea, unless you have a specific reason to do it, like I was doing.

**Dave Jones:** Because, why? You're soldering on, I won't touch it, that's the hot end, is mains earth reference. The tip is shorted to mains earth. That means, if you don't use a completely floating system while you're soldering, bang! You're going to short it out to something.

**Dave Jones:** Really bad news, you don't want to do it. So generally, never ever solder a live circuit unless you know precisely what you're doing, and it's floating. And by floating, of course, I mean it's either battery-powered, or the supply you're using, like this one, is not mains earth reference.

**Dave Jones:** It's got a floating output. Here is the earth terminal right here, and it's got a shunt shorting link on there, but I've disconnected that from the negative terminal. So this is now a floating power supply. But if that was connected to there, it would be mains earth referenced,

**Dave Jones:** and if you're soldering a live circuit, bang! Alright, I've got a very thin layer of lead-free solder on this thing, and we're basically dropped down to almost, you know, around 46 millivolts, or 46 milliohms, so basically that is a 13% decrease. And before, with the leaded stuff, we got a 15% decrease.

**Dave Jones:** So, you know, really, it's certainly in the same ballpark. If anything, it's actually worse than the lead-free solder. I'm not going to claim that, because it's all about the thickness and everything else. So, you know, roughly, it's pretty much exactly the same. Let's give it a go again, and you'll notice it goes up

**Dave Jones:** instantly when I heat it up with the soldering iron. Wham! You'll notice it just jumps up in resistance. So, let's coat it. Well, I've put on as much solder, I think, as I did last time with the lead stuff, but it's hard to tell exactly how much

**Dave Jones:** you've actually put on, but check it out. 26.1 milliohms. So, roughly, that is, once again, a 50% decrease, or just slightly over a 50% decrease. Exactly what we got last time with the lead-free solder, and, well, in theory, that shouldn't have happened. In theory, we should have had a lower value, I'm not sure by how much,

**Dave Jones:** but a lower value with the lead-free solder. But we haven't. We've got roughly the same. I'm going to try and put some more solder on now. I'm really going to try and pile it on, but like I said, I think I kept it pretty much the same as last time, but there is going

**Dave Jones:** to be some error in there. And I think I've put on the absolute max I can, you know, that really any wave solder in process would put on such a thickness track, really. This is a 4.2mm thick track, and I don't know how that shows up on camera, but that is a

**Dave Jones:** massive amount of solder on top of there. I think that's a lot more than what I put on the lead-free, the lead one, that's for sure. And there you have it, we've jumped to 14.5 milliohms now, or thereabouts. And that is just over a 72, or 72.5%

**Dave Jones:** decrease. So, you know, that is an absolute maximum amount of solder I think you could probably fizzle, you might be able to get a bit more on there, you know, you really go insane. But I've never seen a wave solder in process put this amount of

**Dave Jones:** solder on such a small track before. So I think we're, you know, that's got to be the real extreme upper limit there. So there you have it, that's lead-free solder. 99.3% tin, 0.7% copper, in comparison, rough comparison, to the 60-40 lead solder we did in the previous video.

**Dave Jones:** And in theory, it should have higher conductivity, but I don't think the exercise that we did here can precisely show that difference, because really, we need a more, you know, a much more rigorous method than this, we need to know exactly how much solder went on there.

**Dave Jones:** With hindsight, probably should have weighed it, or measured the amount of solder going on in both cases, and well, you know, you could do this sort of thing until the cows come home, but in the end, roughly ballpark figures, rules of thumb that you can take, industry rules of thumb, would be roughly

**Dave Jones:** anywhere from, say, a 15% decrease with lead-free solder to, say, 70% tops with lead-free solder. So I think there probably is a difference there with the lead-free solder, as you'd expect, in theory. But we'd need more, much more accurate measurements to be able to quantify that, you know, get that actual

**Dave Jones:** value difference. But, eh, it's not going to be double, for example. I don't think it's double the lead solder. So, you know, it might have a difference with the track width as well, because then you get rounding of the solder and stuff like that, that's all going to make a difference.

**Dave Jones:** So we really need further experiments in terms of track width, measure, you know, quantify the amount of solder put on there, somehow, you know, work out its thickness and its conductivity and all that sort of stuff. Maybe we'll do some more videos on it, I don't know.

**Dave Jones:** But I think we've got some good rules of thumb there. And by the way, for those in the previous video who seemed a bit confused when I was talking about percentage increases and percentage decreases, they're not the same. Like I mentioned, a 40%

**Dave Jones:** increase in resistance and a 28% decrease. That's just the way the math works. You've got to know the terminology of percentage decrease. It's a specific term, percentage decrease and percentage increase. A 40% increase is not going to be a 40% decrease. And I won't go into the whole theory of it.

**Dave Jones:** That's what we got. We got anywhere from a 15% to a 70-odd percent decrease in resistance with the lead-free solder. Woo! Hope you enjoyed it. Catch you next time.
