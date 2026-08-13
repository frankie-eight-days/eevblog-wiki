---
video_id: _nzI6Ai_KIg
title: Dodgy Smart Meter - Part 2 Electric Boogaloo
url: https://www.youtube.com/watch?v=_nzI6Ai_KIg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 39, "3": 56, "4": 75, "5": 95, "6": 115, "7": 127, "8": 150, "9": 161, "10": 185, "11": 210, "12": 227, "13": 243, "14": 263, "15": 291, "16": 313, "17": 331, "18": 341, "19": 360, "20": 377, "21": 405}
---

**Dave Jones:** Hi, just a follow-up on my dodgy smart meter, where I was trying to figure out where this excess import energy is coming from on my smart meter. Because in theory, and according to the data I've got, my new battery installation should provide all of my power during the night, and I've got more than excess solar during the day.

**Dave Jones:** So I'm not sure why I'm getting a little residual, like 1.8 kilowatt hours a day on average, coming, sucking in from the grid. So, yeah, let's have another look at it, because I've got some more data. Let's have a go, and like, into like 30 minute data.

**Dave Jones:** So, let's have a look. Now there's quite a few people who said it's probably the grid trickle feed setting, which is down here, you can see it. Now, when I originally installed this thing, I set this to 5 watts, because I think I read somewhere that you shouldn't set it to 0, so I did just, you know, 5 watts.

**Dave Jones:** Because it needs some sort of grid supply to actually, you know, keep it running, and keep it active so it doesn't think it's disconnected from the grid, or whatever, right? So I set it to a low 5 watt setting. So, as an experiment, for 5 days, I actually set it to 50 watts, to see if that would make a difference.

**Dave Jones:** To see if all those average figures jumped up. 50 times 24, 1200 watt hours, right? So 1.2 kilowatt hours. It should have shifted from like these average values that you can see here, and here's where I switched it on this day here, on the 12th of September.

**Dave Jones:** And sure enough, it jumped up to 2.62, but the average is only like 0.38 difference, and then I switched it back off yesterday. So, yeah, I'm not seeing it. So I'm not seeing that average shift. So it's not that grid trickle feed thing doing it.

**Dave Jones:** Now, I discovered that I can actually download from the provider, the energy provider, I can download the actual 30 minute data from my smart meter, and this is great. So, here it is here. So it gives me, I've sorted this by general usage.

**Dave Jones:** You can go right down the bottom, and it gives you solar, and it interlays the two rows. So I've had to sort by solar, which is basically my export, feeding out to the grid by feeding, as it's called, and then I've got up top, I've got general usage, which is what I'm pulling from the grid.

**Dave Jones:** And it gives me the readings, presumably in kilowatt hours here, for each 30 minute time interval. Great! So I get 24 readings per day. This is awesome. So what I've done is I've actually plotted some data, and you can see that, look, it does actually go to 0, right?

**Dave Jones:** It does go to 0 quite a few times. It goes to 0. So that completely rules out the theory of the grid trickle feed thing. It ain't that. Otherwise, you would not be getting a figure that goes to 0, especially during the days down, well, I'll show you.

**Dave Jones:** Even when I set it to 50 watts grid trickle feed, okay, so this is the 4th of September here, you can see it actually goes down to 0. So, yeah, so there's all these little residuals. Now there's a big spike here, which presumably, I don't know, we switched on something, and then we, you know, its peak current might have been, for 10 minutes, might have been above what my battery can provide, which is 5 kilowatts power max.

**Dave Jones:** So this is at night time here. So, and curiously, there's several spikes at a similar time here, right? So presumably, yeah, okay, we switched an oven on, and we had the dryer on at the same time, or something like that, right, that the battery couldn't provide.

**Dave Jones:** So fair enough. But all these other little ones over here, this is, it's really interesting, especially like at midnight here, right? So at the start of the day, we're talking, yeah, it's like 1am, right? Should be sleeping. And yeah, we're just getting these little draws and stuff.

**Dave Jones:** And sure enough, when we wake up or whatever, maybe there's some extra stuff going, happening here. But even during the day, when we've got tons of solar, anyway, the point is, look, even down here on the 12th, like here's another, here's the big spike again, but then there's a big spike up here like this.

**Dave Jones:** And, but even on the days when I had that 50 watt grid trickle feed setting, look, zeros, zeros, all the way with LBJ there. And then it's just, it's like kind of like all over the shop. So maybe it's a combination of, as a few people suggested, it could actually be within the accuracy, like the actual, you know, a couple of least significant bits of the ADC in there.

**Dave Jones:** And it's just, you know, measuring like just residual stuff. The resolution seems to be 0.1 kilowatt hours, yeah, odd and even, so 0.1 kilowatt hours there. But anyway, yeah, some sort of residual error thing, because apparently the standard is 1% or whatever for the meters.

**Dave Jones:** So yeah, is it within, somebody's done some calcs, I'm not going to do the calcs now, but yeah, you can see it's kind of like all over the shop, isn't it? Like little small amounts here or there. I can't imagine we're turning on that many appliances that draw a total of 5 kilowatts for like brief periods here and here and here and here.

**Dave Jones:** I'd expect to see like a flat kind of thing if we like turned on something, turned on the oven for two hours and we had the aircon on and then we were drawing, you know, a constant thing. We haven't had the aircon on recently, by the way, at all.

**Dave Jones:** So yeah, I'm just not seeing it. It's more like it's down in the random noise or something. Although, I admit, these peaks are way too coincidental. Something's going on there, like yeah, we are drawing more than the battery, and okay, fair enough, you know.

**Dave Jones:** But yeah, like sometimes we're getting 0, 0, and 0. What's that one? That's kind of like an oddball one, isn't it? It's not as random as the other ones, and it's just, yeah, it's kind of all over the shop. It's really weird, huh?

**Dave Jones:** So there you go. So this is the energy that I'm pulling in from the grid at night time. I mean, I haven't got time down here, but imagine that's midnight there, and that's midnight the next day divided into 48 samples there. And yeah, so this is midday here, and yeah, I'm just not seeing a reason why, apart from yeah, I admit, maybe an appliance can come on there that's drawing more.

**Dave Jones:** But apart from that, I don't know. Once again, leave it in the comments down below. Catch you next time.
