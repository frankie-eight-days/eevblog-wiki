---
video_id: mBvUJ19NBos
title: EEVblog #71 - Happy Birthday to Us!
url: https://www.youtube.com/watch?v=mBvUJ19NBos
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 31, "3": 49, "4": 67, "5": 80, "6": 102, "7": 122, "8": 140, "9": 162, "10": 175, "11": 193, "12": 205, "13": 236, "14": 259, "15": 274, "16": 299, "17": 312, "18": 330, "19": 348, "20": 361, "21": 380, "22": 395, "23": 415, "24": 436, "25": 453, "26": 468, "27": 484, "28": 495, "29": 513, "30": 536, "31": 547, "32": 562, "33": 580, "34": 598, "35": 623, "36": 642, "37": 662, "38": 681, "39": 691, "40": 715, "41": 738, "42": 750, "43": 769, "44": 788, "45": 805, "46": 816}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, and yes, I'm still here in my lab. I haven't sold out. Those who watched my last blog, well, some of you may not have realized

**Dave Jones:** that was an April Fool's joke. I can't believe I fooled, well, quite a few people at least. I was quite impressed. I'd be happy if I just got one person, but no, I haven't sold out to the manufacturers at all. I'm still here.

**Dave Jones:** It was all a load of bullshit, and sorry, but I had to do something for April Fool's Day. I wanted to do something technical, but as you know, I went on holidays and, well, it just never panned out. So I threw that together at the last second and

**Dave Jones:** it seemed to fool quite a few people. So I had fun anyway. So I hope you enjoyed it. I hope I didn't lose any viewers over it. So I hope anyone who unsubscribed actually comes back and watches me again. There's probably a few who just turned up morbidly fascinated to know, well, what would

**Dave Jones:** actually happen this week. So no, I'm still here. Sorry to tell you. Sorry there won't be any electronics content in this blog this time around because I'm going to talk about the big anniversary. It's the first anniversary of the EEV blog. That's right.

**Dave Jones:** The 4th of April last year, 2009, I got the stupid idea to sit in front of a crusty old 320 by 240 webcam. It was propped up on a whiskey bottle container. Even though I don't drink, I had to put on something. So I was sitting

**Dave Jones:** there in a whiskey bottle container in my study in front of my computer, and I just yapped on. I didn't have a script, and I didn't have any idea what I was doing or what I was getting into, but I thought I'd talk in front of a camera, make a complete dick out of myself, and upload it onto

**Dave Jones:** YouTube and post it on Oz Electronics and Sci Electronics Design, I think I posted it on, and what do you know? Some people actually seem to have liked it, and they subscribed from day one, and it's taken off from there. Others said, well, I did make a complete dick out of myself,

**Dave Jones:** but there were actually quite a few people who commented and emailed on that first video, as crap as it was, and I look back on it now, and it really was crap, but there's quite a few people who could actually see the potential future in it, and that there was actually something in the idea,

**Dave Jones:** and well, I thought I'd do it a second time, a third, and before I know it, here I am. This is my 71st blog in a year, so on average more than one per week, which I'm quite impressed with. I haven't gotten bored with it at all.

**Dave Jones:** I'm enjoying it now more than when I started, so that's one of the curious things. I really thought that either it'd die completely, because I wouldn't get any viewers, that was most likely, or I would just lose interest in it and go on to something else,

**Dave Jones:** and I wouldn't find anything good to say each week, but I have, and I haven't run out of ideas. In fact, I haven't even started tapping the ideas that I've got for the blog, and well, here we are, and if you look at the stats where I am now, a year later, I still can't believe it.

**Dave Jones:** I've had over 412,000 views on YouTube of all my videos. I've got 1,444 YouTube subscribers as of today. I've got 3,500 total viewers, because there's another 1,800 via my RSS feed who watch the podcast version on their iTunes thing or their iPhone or whatever, and well, that's like 3,500

**Dave Jones:** regular viewers every blog, and it's unbelievable. I really never thought anyone would take this blog seriously, but turns out it has, with 3,500 people watching me regularly. In some cases, they just can't get enough of my videos. It's unbelievable. Manufacturers have taken notice,

**Dave Jones:** Microchip, Fluke, Agilent, Goss and Metriwatt, and others, and suppliers are sending me gear now. People seem to love my product reviews for some reason, and well, my no-bullshit attitude to things and telling it like it is, and it just seems to have worked.

**Dave Jones:** I can't believe it. I thought there's no way in hell the manufacturers would even touch me. They wouldn't even come near with me. I thought I'd be getting cease and desist letters from lawyers, but I'm not. Manufacturers can really see the power, and suppliers can really see the power of the new social media,

**Dave Jones:** like blogs and YouTube and other things, and it really is quite amazing, and I really doubt, in fact, I'm absolutely sure that the blog wouldn't have even been one-tenth as successful as it is now if it wasn't in a video format. It just would have died.

**Dave Jones:** It just would have been yet another text blog, but because it's video and people can see me, you know, and actually see a personality, well, I've got some personality, I guess, and at least some people like it, so I guess I should thank some people.

**Dave Jones:** First of all, my lovely wife, Nicole, who lets me work on the blog. She puts up with it, and trust me, if she says, that's it, then that's it. So, got to keep her happy, and second, all my viewers. There's a lot of you who've been

**Dave Jones:** supporting me from day one. Thank you, because without my viewers, this blog will be nothing. I guarantee you, if I only had 10 or 20 viewers, I still wouldn't be doing it, but because I've got a 3,500 or so at the moment, it makes it really worthwhile.

**Dave Jones:** It makes sitting in front of the camera, and I know that you guys are just, you know, a lot of you people don't like every blog I do, but I know you watch them, so thank you, and everyone who's sending ideas and comments.

**Dave Jones:** Everyone's contributed to the forum. The forum's been great. Some of my forum users spend more time on there than I do, and there's a real community feel to the EEV blog now, I think. It's not just me in front of the camera, but everyone on the forum and people who watch

**Dave Jones:** and comment, it's fantastic, and I've got to thank the manufacturers as well for taking me seriously, and taking my viewership seriously as well, and taking the whole video blog concept seriously, because it's, I think it's a really, it really adds something to the electronics

**Dave Jones:** community. There's nothing else like it out there, really, so hopefully we can continue to improve and expand on the current EEV blog. There haven't been too many changes over the last year. It's mainly been technical changes in terms of my camera setup, my audio, my lighting, the formatting,

**Dave Jones:** the, you know, just experimenting with a few technical things, but it's still pretty much just me with no script in front of a camera, off the cuff, and well, it seems to still work. People still enjoy it, but one of the main, one of the hardest things is just trying to please

**Dave Jones:** everyone, really, because so many people like so many different things. Some people love just the product reviews. They can't get enough. Others just want theory. There's a lot of beginners. They just want beginner theory. A lot of advanced people just want advanced topics, and there's,

**Dave Jones:** you know, it's all these people who just like, just, you know, they don't care what I do. They, for some reason, just like to hear me rant on about stuff, so they, actually, quite a few people like my drive time rant, so I'm probably going to keep that up because it's a minimal effort thing,

**Dave Jones:** and I've just started getting some paid advertisers on the blog as well, and really, you guys, the viewers, should support them as well because they're paying to keep the blog alive, and also the Google ads and the other revenue, the merchandise and stuff like that.

**Dave Jones:** It's, you know, it really does help make the blog worthwhile, so please keep it up and support my advertisers. So what does the future of the blog hold? Well, I have no idea, but I know that's looking pretty rosy. It's growing. As I said, it just keeps growing and growing and getting better.

**Dave Jones:** I just wish I had more time to spend on it because it's still a minimal effort production. I just sit in front of the camera for 10, 20 minutes once or twice a week. I do a very quick edit. I upload it to YouTube, and there's mistakes, and I miss things, and I don't go back to re-film things,

**Dave Jones:** and it's, you know, I just wish I had more time to do more polished, you know, a more polished production for you, but, you know, it seems to work with just what I've been doing, so that's what I'm going to continue to do.

**Dave Jones:** I'm not really going to change anything, but I'm getting all sorts of products coming in, so you can expect to see a lot more product reviews. I'll try and do some more theory articles because I know theory blogs because I know people like those, but they

**Dave Jones:** do take more time and effort than just a, you know, just a regular blog where I rant on about something or a simple product review, and well, you know, but keep the ideas coming because, you know, there's a whole list of ideas I haven't even gotten to yet, and I'm just trying to find more

**Dave Jones:** time to work on it because the enthusiasm's still there, so don't worry about that. I won't be losing gusto for the show anytime soon. I still love it. Now, my viewership still seems to be split in half, basically. There's half that watch and subscribe via YouTube directly,

**Dave Jones:** and they don't really know or care about the eevblog.com website, and there's those who actually subscribe and will visit the eevblog.com website regularly and even participate in the forum. Well, that's where they leave their comments. They watch the embedded YouTube videos on the eevblog.com site and comment and view through there, or they view through the RSS feed

**Dave Jones:** via some other player. Now, I'm really still going to have to stick with that format because I think that's the best way to go about it because I can't abandon YouTube. There's no way I'm going to do that at all, and there's no way I'm going to abandon eevblog.com because

**Dave Jones:** that's the central website where I can do so much, and I have the forum and other stuff, and it works really well. And my server's still holding together. I've just got a simple shared server which costs me under $10 a month, but it seems to be hosting the streaming video

**Dave Jones:** pretty well for the podcast, and it seems to be just coping generally well, especially when I get a surge of hits because I'm mentioned on some other blog. But that might have to change within the next year. I probably fully expect to have to pay a lot more for my web hosting and things like

**Dave Jones:** that. I might have to go to a dedicated server just to handle the load, but it seems to be working at the moment. And as for YouTube, you may have seen a couple of changes in the last week or so on YouTube. Well, in their formatting and the comment system and stuff like that.

**Dave Jones:** That's not me. That's YouTube. They're making these huge changes, I think the biggest changes they've ever made. And it really is, quite frankly, it's shithouse, and YouTube have no idea what they're doing. They've completely screwed it up in almost every respect. I thought they couldn't possibly make the

**Dave Jones:** YouTube comment system any worse, but they have. My hat's off to YouTube. They've found a way to make it even shittier. I can't believe it. And things like the upload functionality on YouTube is broken. Can you believe it? I almost didn't get my April 1st, April Fool's blog uploaded in time

**Dave Jones:** because the upload feature wouldn't work. Unbelievable. But yeah, I'm still stuck with YouTube, and hopefully they'll sort things out. But yeah, if you've got any better ideas on how I can better integrate and run the site and things like that, do let me know, please.

**Dave Jones:** And a year on, and 70 blogs later, well, not much has changed really. I'm still sitting here with no script, no idea what my next blog's going to be about really. I've got no clue at all. I sit down in front of a camera and I rave on.

**Dave Jones:** And well, you know, it's more fun now than it was when I started. And I certainly plan on continuing, and I hope it really continues to grow at its current pace. In fact, if it does continue to grow at its current pace, within another year I'll probably

**Dave Jones:** I could even have potentially 5,000-odd viewers or something like that. That'd be absolutely remarkable. So I hope that everyone continues to like it, people continue to subscribe, and if you've got any good ideas for the blog or ways I can help improve and market the blog,

**Dave Jones:** because the more it gets out there and the more popular it gets, the more time the wife's going to allow me to work on the blog, and the more advertising revenue I'm going to get to make it worthwhile to buy gear just to do stuff.

**Dave Jones:** And well, you know, let's see how far we can take this thing. So here's to the next year, and I guess I should blow out the candles.
