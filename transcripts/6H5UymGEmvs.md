---
video_id: 6H5UymGEmvs
title: Return Youtube Dislike Count Plugin TESTED - Is it accurate?
url: https://www.youtube.com/watch?v=6H5UymGEmvs
source: youtube-asr
timestamps: {"0": 0, "1": 23, "2": 38, "3": 47, "4": 58, "5": 72, "6": 81, "7": 89, "8": 113, "9": 130, "10": 148, "11": 160, "12": 173, "13": 188, "14": 197, "15": 208, "16": 226, "17": 243, "18": 254, "19": 280, "20": 300, "21": 313, "22": 326, "23": 338, "24": 363, "25": 372, "26": 384, "27": 394, "28": 405, "29": 414, "30": 424, "31": 437, "32": 453, "33": 463, "34": 481, "35": 491, "36": 503, "37": 514, "38": 526, "39": 550, "40": 558, "41": 568, "42": 578, "43": 594, "44": 603, "45": 621, "46": 630, "47": 650, "48": 663, "49": 673, "50": 684, "51": 695, "52": 707, "53": 719, "54": 740, "55": 756, "56": 764, "57": 777}
---

**Dave Jones:** Hi, you remember when that YouTube removed the dislike count? They kept the dislike count button, but yeah, they hid the count and Mr. Shiteating grin here announced it all and well, yeah, it wasn't very well received, but as you know, many people can still access and get the dislike count figures and so can I.

**Dave Jones:** You can see I can still see that this video has 572,000 dislikes. How can I do this? Well, I am the bring back the dislike count channel. Yes, I surpassed 100,000 subscribers.

**Dave Jones:** Yes, that is genuine. Yes, I will link in a video of how I actually got that. This is genuine YouTube silver award. There it is, 100,000 subscribers bring back the dislike count.

**Dave Jones:** So anyway, I didn't do that. Some smart cookie wrote a browser plugin to actually get this back. It's called return YouTube dislike plugin. I've got Chrome here. I mostly use Chrome.

**Dave Jones:** I've got it installed. I'm not sure what browsers is available on. I think it's available on some other app thing somebody mentioned. But anyway, there is a GitHub source code here, so I'll link it in down below if you want to install it and I recommend that you do.

**Dave Jones:** And I believe millions of people, somebody I think someone said like 4 million people had installed it or something. It was quite a lot of people. And I don't know where they got the figure from.

**Dave Jones:** But anyway, the source code's here if you want to check it out that it's legit and it's not doing anything nefarious in the background and stuff like that. So it returns the dislike count.

**Dave Jones:** How does it actually do this? Because YouTube have actually hidden this data. How do we actually get this dislike count? Well, there seems to be some debate about there whether or not this these numbers are legitimate because a lot of like, you know, news and current affairs and bloggers and stuff are using this they've got this plugin and they're using these numbers for, you know, videos that might be, you

**Dave Jones:** know, talked about at the moment and, you know, 2.8 million dislikes. Where is this uh number coming from? Well, um they actually tell you, and we'll have a look at this, but I wanted to see uh whether or not we could actually back this up with data, because I'm a creator.

**Dave Jones:** We can still actually see the dislike, cuz Mr. Shady McGrin here, he uh told us that one of the reasons that they removed it was to protect us creators, so that, you know, we wouldn't uh be mentally harmed by seeing this uh you know, dislike value, and they'd hide it away to make sure.

**Dave Jones:** And of course, that was utter, utter rubbish, and I've done a video on this. Here is my YouTube uh creator dashboard, and it's complete and utter lie that's done to protect creators.

**Dave Jones:** This is the view that we use every single day, multiple times, day in, day out as a creator. You can see over here, like versus dislike, and I move my mouse over it, not only can I see the dislike percentage, but I can see the actual number.

**Dave Jones:** The actual number of dislikes, and we will go through this. So, we will see we So, we can use this data that creators like me can see, and we'll see if it uh kind of matches up with what this YouTube uh return the dislike button is doing.

**Dave Jones:** So, how does this actually work? Well, we can go over to the frequently asked our questions here. So, where does it get uh the data from? Well, it says a combination of Google API and scraped data.

**Dave Jones:** And unfortunately, um they they use their own database. So, the app talks to it So, the plugin talks to its own database, uh which it can store data on there.

**Dave Jones:** Now, uh sometime after YouTube disabled this, they still had API access uh to the dislike data. So, anyone could actually pull for any video the API data, but I believe they shut that off now, and they actually tell you what happens if the API um is actually shut off.

**Dave Jones:** Here it is. What will happen if the YouTube stops returning dislike counts, like it has now? The back end will switch to using a combination of archived dislike stats estimated extrapolated from extension user data and estimates based on view like ratios for videos whose dislikes weren't archived at archived and for outdated dislike archives.

**Dave Jones:** So, for all new videos updated after a certain date when they turned off the API, there is no new there is no existing archive API data to scrape. So, where do they get the count from?

**Dave Jones:** Well, they've got a formula here which I think might be they might have that upside down. I have to read have to think about that closely. But, anyway, basically what it does is that the plugin actually when you watch a video like so if I'm watching this video and I've got this plugin installed, the that plugin actually sends whether or not I thumbs up or thumbs down this video, not just

**Dave Jones:** thumbs down but also thumbs up. It sends that data back to their own database. So, they keep their own independent third-party statistics there, right? On their own website and it uses that data to then calculate it basically gets the the this is the plugin uses like count divided by the dislike count times the public like count.

**Dave Jones:** So, it's basically taking the number of people who use this plugin as and how many have clicked up vote and how many have clicked down vote. It gets that ratio and then multiplies it by the public thumbs up ratios.

**Dave Jones:** So, let's say there's 10,000 users of this plugin and they watch a particular video and they thumbs up and thumbs down it. And let's say that 50% of them choose thumbs down, 50% choose thumbs up, right?

**Dave Jones:** That's a ratio of one. So, they would multiply the 1.1 million here that is public data by that ratio of one. So, it would equal 1.1 million down votes.

**Dave Jones:** So, it just basically reflects the ratio of the users of that plugin to the public up vote here. And that's how they give the dislike. And And of course, as the ratio changes in either direction, it doesn't have to just be in the favor of dislikes, it can also be in the favor of likes, um it just takes that ratio and then uh figures out um what the number

**Dave Jones:** of down votes is. And there's people who think this is not legit. So, I want to um actually look at the data from my own videos and see if we can see if it correlates, okay?

**Dave Jones:** So, here's uh let's just take these uh some videos of mine. Here's all my latest ones, okay? So, let let's take like a large number, right? Then my biggest view, 149,000 views, okay?

**Dave Jones:** For uh 1489 mystery teardown here, okay? There we go. I'll zoom in there. We can look at that. That's 89 thumbs down. You can see that there. It popped up.

**Dave Jones:** Now, if we go have a look at that, What is that? Is that the actual figure over here that the plug-in is giving me? It's giving me 60. So, it's actually giving me less.

**Dave Jones:** It's actually uh you know, it's it's erred on the lower side rather than the high side. And you can work out the percentage there if you really want to, okay?

**Dave Jones:** So, it's it's giving me that this figure here, it's not because I'm logged in. It's not giving me the genuine count. This is coming from my plug-in. If I didn't have the plug-in installed, then I I wouldn't be able to see the dislike uh count there.

**Dave Jones:** Okay, so that one's erred on the low side. So, if we go to another high one here, let's say this um Energizer uh leaking battery one, that's got 91,000 views, that's pretty decent, and that's got 87 thumbs down, okay?

**Dave Jones:** 87 thumbs down. And here it is here, and it's giving 75. Once again, it's erring on the lower side. So, that's interesting. Two videos. Let's try another high one, 72,000 for the EcoFlow uh battery here.

**Dave Jones:** That's got 87 thumbs down. What is the count over here? 82. Once again, it's erring on the lower side. So, there you go. Three out of three of my own videos have erred on on the lower side.

**Dave Jones:** So, that's a good indication that, you know, something like this is not inflated. I know there's bias and everything else. How many people are using the app? And a lot of people claim that the people who use the app are the ones who are most likely to, you know, dislike something.

**Dave Jones:** Well, doesn't really reflect in my data. So, that's like busted in my data there. I mean, I can try another one. So, let's try this film capacitor failure one.

**Dave Jones:** That doesn't hasn't got many. 51 thumbs down. Go over to here and we've got Oh, it matches. Matches precisely. 51. That's a coincidence. Let's actually choose one where I got a lot of thumbs down.

**Dave Jones:** Like this is like a real outlier. Rarely will I get a video with 80 87% like to dislike ratio. That's very low. I guess a lot of people either they didn't like it.

**Dave Jones:** It's about Odyssey and routers attacking. So, you know, there's people who don't like other. They just like only use YouTube and they'll thumbs down and Odyssey, you know, talking about Odyssey, whatever.

**Dave Jones:** But 143 thumbs down. And that has got 77. There you go. That's like half. So, it's underreported by half. So, that's interesting. If the number of dislike if the number of dislikes goes up on a particular video, the ratio of the users who are using this actually it goes it goes in the opposite direction.

**Dave Jones:** I even found one. What's that? Five now? That they're all reporting on the lower side. So, you know, I can keep going, but I think you get the idea.

**Dave Jones:** So, there's a lot of people who say, "Well, okay. There's how many people actually use this app? Is this based on like 10 people or something?" Yeah, I I I totally agree.

**Dave Jones:** It should it should actually pop up and tell you like how many people this is based on. That'd be really nice. You know, it's based on, you know, I like even if it's based on 100 users or 1,000 users or something like that.

**Dave Jones:** Hey, you know, all the all the political polls and other polls that you hear on, you know, phone survey they surveyed 100 people in the population and then that makes national news like, you know, 80% of the people vote for this or something and it's based on like a survey of 100 people or something.

**Dave Jones:** You know, it's right? But yeah, I totally agree. I I would support it actually if it popped up and, you know, told you how many people that was based on.

**Dave Jones:** That'd be really nice. But it doesn't. So, anyway, what I've done is I've actually created a poll. I will refresh this. I did this 5 hours ago and I've got 1,400 responses here and I basically asked people if they could tell me, do you use this app or not?

**Dave Jones:** And this specific plugin, not any I think there might be one or two others, but this is by far the most popular one. Do they use it or not?

**Dave Jones:** And 25% of the my audience said they did. So, a quarter and 75% no, they do not use it. So, that's actually quite a substantial percentage, 25%. And I asked on Twitter just to get another number on this and asking the same thing, 225 votes and 30% said that they use it.

**Dave Jones:** So, I'm I'm going to run with 25%, right? A quarter of my audience actually use this plugin to watch my videos. So, that's quite substantial. But once again, these are technical engineering nerds mostly who watch my videos.

**Dave Jones:** So, you could say, you know, over represented to the general population in terms of like willingness to install plugins and stuff like that. But, you know, 25% I'm I'm quite surprised it was that high actually.

**Dave Jones:** So, there you go. Hopefully that's given you some confidence that the number here is at least like not like not like massively over I don't think it's massively over reported here.

**Dave Jones:** So, you know, something like this that gets, you you 2.8 million thumbs down or insert the latest video that everyone's talking about on on the Twitterverse or whatever, you know.

**Dave Jones:** And like so I it seems to be working reasonably well. It it doesn't It's certainly not over-reporting figures based on my audience and my data. So, there you go.

**Dave Jones:** I highly recommend that you install this because then it helps if everyone installs this thing, then it really it it doesn't quite recover the original functionality of the YouTube dislike button.

**Dave Jones:** It means that we can tell YouTube, "No, we've got a way around this." And it seems to work reasonably well. The only thing, yeah, as I said, I'd add is like a number here that tells us how many votes it's based on or it only gives you a or it only does that if it reaches a threshold of, I don't know, 100 or 1,000 or something like that would be nice.

**Dave Jones:** But then you wouldn't see it on like some videos that haven't got many views because it's based on an average number of users who use this plugin. And if people use their shoe phone, then, you know, it may they may not have that available cuz they're using the YouTube app or whatever.

**Dave Jones:** Somebody said there's like an another There's another app that actually has this built in or something that can view it, but Google tried to YouTube tried to ban it or something.

**Dave Jones:** I don't know the details. But anyway, I'm reasonably confident that that is not at least not over-reporting stuff. So, anyway, hope that was useful. Leave your thoughts and comments down below.

**Dave Jones:** Catch you next time.
