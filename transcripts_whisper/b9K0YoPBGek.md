---
video_id: b9K0YoPBGek
title: Why Isn't My Electricity Bill Zero with a Home Battery?
url: https://www.youtube.com/watch?v=b9K0YoPBGek
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 40, "3": 55, "4": 67, "5": 85, "6": 96, "7": 116, "8": 135, "9": 152, "10": 172, "11": 190, "12": 207, "13": 228, "14": 245, "15": 261, "16": 279, "17": 295, "18": 313, "19": 331, "20": 351, "21": 366, "22": 383, "23": 396, "24": 414, "25": 429}
---

**Dave Jones:** Hi, just a quick update on my solar power system and home battery storage system. I got my bill, my recent electricity bill, and it's $12.38. Aussie, that is. None of that Yankee rubbish. But they did change my plan. It was on a quarterly plan, and that's how most Australians are.

**Dave Jones:** They're on a quarterly electricity plan, but because I had the new smart meter installed, they decided, eh, nah, we're going to change it to a monthly bill. So, I didn't get any choice in it. So, that's $12.38 for the last month. And you can see that from the 20th of December to the 19th of January, they're 31 days.

**Dave Jones:** So, yeah, pretty darn cheap. It's almost zero, but why is it not zero? That's an interesting question, which I have covered in a previous video, but I'll just go over it again and show you. We've got Jens Schoenfeld here, who follows me on X.

**Dave Jones:** He asked the question, is summer down under and you still have a monthly bill above zero? Can mean only one thing, you didn't follow the Prime Directive, laying out a PV system, you can always fit one more panel. Yes, I can always fit one more panel.

**Dave Jones:** But I don't think I've done, no, I haven't done a video on this yet, but if you follow me on X, you would have got the update that my Hoy-Miles micro-inverter system seems to have failed. Somehow, those two extra micro-inverters that are hooked up to the Hoy-Miles 2-channel inverter,

**Dave Jones:** I stored an extra two panels on my roof into the generator port of the DI, that has failed. Haven't had a chance to look at it yet, so I have no idea what's wrong. I've tried turning the DI back on off and in again,

**Dave Jones:** I've tried turning the power to the Hoy-Miles back off and on again, hello IT. And, yeah, nothing. So I'm going to have to go up there and troubleshoot that. So stay tuned for that video. But anyway, why is my bill not zero? And, interestingly, I have been away for the last, all this time here.

**Dave Jones:** I've been away for all, I've been on holiday, so there's been nobody home here yet. You can see these little blue peaks here. Look at this, 0.89 kilowatt hours, 0.63, 0.9, 0.5, 1.11, 1.67, right? So that's one, so what does that average to?

**Dave Jones:** Like one kilowatt hour per day, or something, maybe, right? Even when I'm not there. Why is it not zero when I've got a battery storage system? Well, as I explained in a previous video, it's because of, you can see here, here is actually today's usage here in the morning,

**Dave Jones:** and you can see this consumed graph, which is that purple one, right, is actually above the brown one, which is the produced one here. But produced, when there's no sun, means it's being delivered by my battery, right? So it's being delivered by my storage battery overnight,

**Dave Jones:** because this is 12 a.m., 1 a.m., etc., right? So the sun's not up, so it's delivering the battery as if the sun is still up, right? So that's why my solar analytics monitoring system here just thinks that the sun's still up, because it doesn't know the difference whether it's coming from the actual solar panels and the inverters,

**Dave Jones:** or whether or not it's coming from the battery and the DI hybrid inverter. So why is that? You can see that there's little peaks above here where the produced does not match the consumed. That's because of the control response loop inside the DI hybrid inverter.

**Dave Jones:** Any hybrid inverter's going to have this. It doesn't respond instantly. So when you suddenly turn on your EV charger or your oven or your fridge, compressor starts up, for example, then those spikes in current are going to actually come from the grid. They're not going to come from your hybrid inverter.

**Dave Jones:** They're not going to come from your battery via the hybrid inverter. It doesn't have the control loop response time. It's deliberately slow like that for reasons. I'll leave it down below. If you design inverters, you don't want them to respond instantly. Now, of course, if you go completely grid-independent,

**Dave Jones:** then it all has to come from the inverter, and they might have a faster response time. I don't know. I've never looked into that. Does an off-grid inverter have a faster response time than an on-grid inverter like mine? Don't know. But yeah, apparently, like, it's really quite slow.

**Dave Jones:** So those ones above the graph, unfortunately we don't have the resolution here to really see it, because the solar analytics is only like a five-minute thing, like sampling period or something. But yeah, that's the basic problem here, and why I'm getting, like, a residual one kilowatt hour

**Dave Jones:** coming from the grid even when I'm not home doing nothing. It's because what all these spikes are here during the day, or during the night here, when we're not actually, even when we're home, we're not using anything at nighttime, that is the fridges and freezers, the compressors turning off and on,

**Dave Jones:** because we've got three freezer things. So that's all of them coming on, plus we've got a home ventilation system that operates all night, that's taking like another hundred watts now, and any other phantom power stuff. So that's the nighttime consumption. But yeah, the control response loop of the battery hybrid inverter

**Dave Jones:** is why I will always be taking power from the grid unless I go completely off-grid, and that's just silly to do if you've already got a grid connection. It's just dumb. Why would you? It's like I'm paying a small connection charge now, and as I said, $12 a month, by the looks of it,

**Dave Jones:** is my new bill, which is basically that residual power plus a connection fee minus, actually, minus the credit. At the moment, I'm $15 in credit like this, because the electricity company that I'm with also, not only did they change them into monthly, they also lowered the feed-in tariff.

**Dave Jones:** I was getting paid $0.07, which was not much, to feed back in my excess solar power, which I do have. You can see all the yellow here going negative. This is all excess solar. And even when I'm, like, home, like, at the moment, we're still here,

**Dave Jones:** and we're feeding in all this, exporting, because we can't use it all. We get so much power in summertime that, yeah, we're feeding it back out to the grid. Look at that, 30! Yesterday, 33 kilowatt hours sent out to the grid. We couldn't use it all.

**Dave Jones:** It was so much. Crazy. So, yeah, I'm only getting paid $0.05 per kilowatt hour now, and I'm sure that'll eventually go down to zero. You know, I might look at different plans and stuff like that. Oh, sorry, you didn't see that there. You didn't see that.

**Dave Jones:** My head might have been covering that. So, yeah, I might get a bill of zero if we have, like, a huge excess. But I'm paying $0.30 per kilowatt hour, I think, for that residual one kilowatt hour per day. So, you know, I'm basically paying $0.30 a day,

**Dave Jones:** pretty much, for coming from the grid, and then minus whatever excess at $0.05 per kilowatt hour per day. So, yeah, I'm never going to draw zero from the grid. So there's always going to be the connection charge plus any residual power. So there you go.

**Dave Jones:** Hope you found that interesting. If you did, give it a big thumbs up. As always, discuss down below. Catch you next time.
