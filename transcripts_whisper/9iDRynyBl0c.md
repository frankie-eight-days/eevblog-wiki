---
video_id: 9iDRynyBl0c
title: Proof that Telstra Bigpond is Throttling Youtube Bandwidth in Australia?
url: https://www.youtube.com/watch?v=9iDRynyBl0c
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 41, "3": 64, "4": 79, "5": 95, "6": 113, "7": 127, "8": 143, "9": 164, "10": 184, "11": 199, "12": 215, "13": 235, "14": 259, "15": 283, "16": 309, "17": 329, "18": 349, "19": 371, "20": 393, "21": 409, "22": 426, "23": 446, "24": 462, "25": 484, "26": 511, "27": 529, "28": 543}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, this isn't going to be a usual blog because I've got something I need to rant about and something that ticks me off.

**Dave Jones:** What is it? It's Telstra, my internet service provider here in Australia. What they're doing is they're throttling YouTube. They're throttling the speed of YouTube, capping it to essentially a pretty much a fixed level for all their users. And I reckon I've got fairly decent proof that they're actually doing this.

**Dave Jones:** The really annoying thing is, is that it seems to be only Telstra. They seem to be the only internet service provider in the country who are actually doing this, deliberately capping YouTube. As far as I know, it's nothing else. It's only YouTube. Now, as a YouTube content provider, I've got over a hundred videos uploaded on YouTube.

**Dave Jones:** So I'm a fairly heavy YouTube user, not only as an uploader, a content provider, but also as a viewer as well. And it just ticks me off that when I try to watch something, you know, it's got the little streaming bar down the bottom

**Dave Jones:** and how much is actually cached before, you know, as you're watching it, and it always jerks. And sometimes I've got to actually leave the thing for, you know, five minutes to let it download before I can play it. And it's really annoying. And I don't get this problem anywhere else.

**Dave Jones:** It's only if I use the Telstra connection. And to make matters worse, I've got what is probably one of the fastest internet connections you can get in your home in Australia. I've got the Telstra BigPond Elite plan, which is like an unlimited, essentially unlimited speed.

**Dave Jones:** It's like 30 megabits per second or something like that via cable, directly via cable. And, you know, I don't have ADSL or anything like that. And so I've got the fastest internet connection, you know, you can get almost. It's like $100 a month.

**Dave Jones:** It's not cheap. It's a very expensive internet connection, top of the line. And they bastards are capping YouTube. Ticks me off. All right, I know what you're going to say. Why don't I just move to a different internet service provider? Well, I would if I could.

**Dave Jones:** I'm more than, I'm like 5.5 kilometers from our exchange. So basically, ADSL is pretty much out. I've tried ADSL before, and it's awful. It's horrendously unreliable at my house. So I just, I really can't do it. And the only thing I've got is Telstra cable.

**Dave Jones:** I'm not going to go wireless, because that's hideously unreliable. I need a reliable, solid, high-speed internet connection. The only way I can get it is with the Telstra cable. Now, to keep this in perspective, Telstra BigPond internet service, Telstra are the biggest internet service provider in this country.

**Dave Jones:** They've got like over 3 million users, I think. And that's like, if you look at it, that's like one-third of Australian households. It's massive. They are the biggest in the country, and supposedly, you know, the biggest and the best. Not necessarily the best value for money, that's for sure.

**Dave Jones:** They're definitely not. They're shit at that, actually. There's tons of tiny little other internet service providers around, that a lot of them will feed off the Telstra, I think, I believe, correct me if I'm wrong, they'll feed off the Telstra connection, or something like that.

**Dave Jones:** But it's obviously the unfiltered part of the backbone, or something like that, because these tiny little ISPs you can sign up for don't throttle YouTube bandwidth. But Telstra do. Now let's actually take a quick look at what you'd expect for a typical performance versus time graph for an internet connection.

**Dave Jones:** If we've got speed in megabits per second up here, 1, 2, 3 megabits, etc., versus time, days, weeks, hours, months, whatever, then you would expect something, a graph which is sort of all over the shop, like this somewhere up there. Because the bandwidth of YouTube, if this is just YouTube bandwidth, by the way,

**Dave Jones:** if you look at it, because there's all sorts of things which affect YouTube's bandwidth, especially in this country. And so it's not going to be a consistent bandwidth over time. But if the internet service provider was capping or throttling the YouTube bandwidth, then you would get something that looks pretty close to a flat line like that,

**Dave Jones:** because it all gets capped down to a fixed level. So how can we keep the internet service providers honest by checking YouTube's bandwidth? Well, it turns out it's very easy. And YouTube actually thoughtfully provide a tool that does exactly this for us. Now, if you go to youtube.com slash myspeed with an underscore, there's the link,

**Dave Jones:** you can actually see your graph, not only for your connection, but for your ISP, your internet service provider, and as an average, and also for your state, your country, and averages like that. Now, here's my one. And this is what we're talking about.

**Dave Jones:** Look at it. Let's say, look at the blue graph there. That's Sydney. Now, Sydney's average, where I am, is 4.69 megabits per second. Similar for New South Wales, which is the state I'm from, and the Australian, our country's average is 3.39 megabits per second for YouTube.

**Dave Jones:** And global, around the world, YouTube say it's 3.41. But look at Telstra, the internet service provider, the yellow one. 1.15 megabits per second. They're clearly capping it. And look at the graph. As I said, you can see that all the other variations in the state and the country

**Dave Jones:** and the global vary with time. But look at Telstra's one. Telstra's the ISP here. The yellow line on the graph is almost completely flat. That is pretty conclusive proof that they're capping or throttling YouTube's bandwidth. Now, you've got to remember, this data is actually compiled by YouTube and their servers,

**Dave Jones:** and it's aggregated over time, which means it's going to be pretty darn accurate and pretty consistent, straight from the horse's mouth. Okay, I know what you're thinking. It might just be something wrong with my connection, right? My individual connection, something's a bit screwy,

**Dave Jones:** or it's just random over time, or something like that. So, what I did to prove that is ask for some of my viewers to send in their screenshots of their captures and what internet service provider they're using. Let's take a look at them.

**Dave Jones:** Now, here's four other Telstra ones. As you can see, the first one, once again, the yellow, 1.15 for Telstra ISP average. And here's another one, 1.15 again, 1.09, 1.11. As you can see, these are different people using Telstra in different parts of the country,

**Dave Jones:** and they all get the same thing. Okay, so what do the other internet service providers get? Well, I'm glad you asked. Let's take a look at that. I've got some data on that too. Here's TPG, here's another big internet service provider, not nearly as big as Telstra, but anyway, check it out.

**Dave Jones:** 2.98, once again, that yellow graph, the ISP one, is 2.98, 3.29, 3.42, 3.83. As you can see, TPG have no problems at all. And if you look at the actual graphs as well, you can see that they're jumping around and they're sort of inconsistent with time,

**Dave Jones:** which shows that they're not actually being throttled. And here's some others. Here's Netspace, 3.58. Here's Internode, 1.87. Here's IINet, 3.44. Here's Exertel, 2.39. So as you can see, all these little smaller internet service providers around the country do not throttle their YouTube bandwidth.

**Dave Jones:** So why the hell are Telstra doing it? The bastards! So there you go. Telstra, I'm calling you out. You are throttling mine and everyone else's YouTube bandwidth. And we want to know why. Why are you doing it? There's no reason to do it at all,

**Dave Jones:** apart from maybe saving some server costs or something like that, because some dickhead managers in Telstra have decided, well, you know, if we can just throttle it or something like that, maybe we can save some dollars here or there, because it's always about the bottom line, I bet you.

**Dave Jones:** Come on, tell us. Why are you actually doing it? We're not going to give up until you give us an answer.
