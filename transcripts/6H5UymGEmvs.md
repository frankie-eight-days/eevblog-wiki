---
video_id: 6H5UymGEmvs
title: Return Youtube Dislike Count Plugin TESTED - Is it accurate?
url: https://www.youtube.com/watch?v=6H5UymGEmvs
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 38, "3": 51, "4": 65, "5": 77, "6": 85, "7": 98, "8": 113, "9": 128, "10": 143, "11": 158, "12": 171, "13": 184, "14": 197, "15": 212, "16": 226, "17": 239, "18": 254, "19": 270, "20": 282, "21": 298, "22": 309, "23": 326, "24": 343, "25": 357, "26": 370, "27": 384, "28": 397, "29": 411, "30": 421, "31": 430, "32": 446, "33": 460, "34": 475, "35": 488, "36": 503, "37": 516, "38": 533, "39": 551, "40": 564, "41": 576, "42": 588, "43": 601, "44": 615, "45": 630, "46": 646, "47": 661, "48": 675, "49": 690, "50": 705, "51": 722, "52": 736, "53": 747, "54": 760, "55": 774}
---

**Dave Jones:** Hi, you remember when that YouTube removed the dislike count? They kept the dislike count button, but yeah, they hid the count and Mr. Shiteating grin here announced it all and well, yeah, it wasn't very well received, but as you know, many people can still

**Dave Jones:** access and get the dislike count figures and so can I. You can see I can still see that this video has 572,000 dislikes. How can I do this? Well, I am the bring back the dislike count channel. Yes, I surpassed 100,000 subscribers.

**Dave Jones:** Yes, that is genuine. Yes, I will link in a video of how I actually got that. This is genuine YouTube silver award. There it is, 100,000 subscribers bring back the dislike count. So anyway, I didn't do that. Some smart cookie wrote

**Dave Jones:** a browser plugin to actually get this back. It's called return YouTube dislike plugin. I've got Chrome here. I mostly use Chrome. I've got it installed. I'm not sure what browsers is available on. I think it's available on some other app thing

**Dave Jones:** somebody mentioned. But anyway, there is a GitHub source code here, so I'll link it in down below if you want to install it and I recommend that you do. And I believe millions of people, somebody I think someone said like 4

**Dave Jones:** million people had installed it or something. It was quite a lot of people. And I don't know where they got the figure from. But anyway, the source code's here if you want to check it out that it's legit and it's not doing

**Dave Jones:** anything nefarious in the background and stuff like that. So it returns the dislike count. How does it actually do this? Because YouTube have actually hidden this data. How do we actually get this dislike count? Well, there seems to be

**Dave Jones:** some debate about there whether or not this these numbers are legitimate because a lot of like, you know, news and current affairs and bloggers and stuff are using this they've got this plugin and they're using these numbers for, you know, videos that might be, you

**Dave Jones:** know, talked about at the moment and, you know, 2.8 million dislikes. Where is this uh number coming from? Well, um they actually tell you, and we'll have a look at this, but I wanted to see uh whether or not we could actually back

**Dave Jones:** this up with data, because I'm a creator. We can still actually see the dislike, cuz Mr. Shady McGrin here, he uh told us that one of the reasons that they removed it was to protect us creators, so that, you know, we wouldn't

**Dave Jones:** uh be mentally harmed by seeing this uh you know, dislike value, and they'd hide it away to make sure. And of course, that was utter, utter rubbish, and I've done a video on this. Here is my YouTube uh creator dashboard, and it's complete

**Dave Jones:** and utter lie that's done to protect creators. This is the view that we use every single day, multiple times, day in, day out as a creator. You can see over here, like versus dislike, and I move my mouse over it, not only can I

**Dave Jones:** see the dislike percentage, but I can see the actual number. The actual number of dislikes, and we will go through this. So, we will see we So, we can use this data that creators like me can see, and we'll see if it uh kind of matches

**Dave Jones:** up with what this YouTube uh return the dislike button is doing. So, how does this actually work? Well, we can go over to the frequently asked our questions here. So, where does it get uh the data from? Well, it says a combination of

**Dave Jones:** Google API and scraped data. And unfortunately, um they they use their own database. So, the app talks to it So, the plugin talks to its own database, uh which it can store data on there. Now, uh sometime after YouTube

**Dave Jones:** disabled this, they still had API access uh to the dislike data. So, anyone could actually pull for any video the API data, but I believe they shut that off now, and they actually tell you what happens if the API um is actually shut

**Dave Jones:** off. Here it is. What will happen if the YouTube stops returning dislike counts, like it has now? The back end will switch to using a combination of archived dislike stats estimated extrapolated from extension user data and estimates based on view like ratios

**Dave Jones:** for videos whose dislikes weren't archived at archived and for outdated dislike archives. So, for all new videos updated after a certain date when they turned off the API, there is no new there is no existing archive API data to scrape. So, where do

**Dave Jones:** they get the count from? Well, they've got a formula here which I think might be they might have that upside down. I have to read have to think about that closely. But, anyway, basically what it does is that the plugin actually when

**Dave Jones:** you watch a video like so if I'm watching this video and I've got this plugin installed, the that plugin actually sends whether or not I thumbs up or thumbs down this video, not just thumbs down but also thumbs up. It sends

**Dave Jones:** that data back to their own database. So, they keep their own independent third-party statistics there, right? On their own website and it uses that data to then calculate it basically gets the the this is the plugin uses like count

**Dave Jones:** divided by the dislike count times the public like count. So, it's basically taking the number of people who use this plugin as and how many have clicked up vote and how many have clicked down vote. It gets that ratio and then

**Dave Jones:** multiplies it by the public thumbs up ratios. So, let's say there's 10,000 users of this plugin and they watch a particular video and they thumbs up and thumbs down it. And let's say that 50% of them choose thumbs down, 50%

**Dave Jones:** choose thumbs up, right? That's a ratio of one. So, they would multiply the 1.1 million here that is public data by that ratio of one. So, it would equal 1.1 million down votes. So, it just basically reflects the ratio of the

**Dave Jones:** users of that plugin to the public up vote here. And that's how they give the dislike. And And of course, as the ratio changes in either direction, it doesn't have to just be in the favor of dislikes, it can also be in the favor of

**Dave Jones:** likes, um it just takes that ratio and then uh figures out um what the number of down votes is. And there's people who think this is not legit. So, I want to um actually look at the data from my own

**Dave Jones:** videos and see if we can see if it correlates, okay? So, here's uh let's just take these uh some videos of mine. Here's all my latest ones, okay? So, let let's take like a large number, right? Then my biggest view, 149,000

**Dave Jones:** views, okay? For uh 1489 mystery teardown here, okay? There we go. I'll zoom in there. We can look at that. That's 89 thumbs down. You can see that there. It popped up. Now, if we go have a look at that,

**Dave Jones:** What is that? Is that the actual figure over here that the plug-in is giving me? It's giving me 60. So, it's actually giving me less. It's actually uh you know, it's it's erred on the lower side rather than the

**Dave Jones:** high side. And you can work out the percentage there if you really want to, okay? So, it's it's giving me that this figure here, it's not because I'm logged in. It's not giving me the genuine count. This is coming from my plug-in.

**Dave Jones:** If I didn't have the plug-in installed, then I I wouldn't be able to see the dislike uh count there. Okay, so that one's erred on the low side. So, if we go to another high one here, let's say

**Dave Jones:** this um Energizer uh leaking battery one, that's got 91,000 views, that's pretty decent, and that's got 87 thumbs down, okay? 87 thumbs down. And here it is here, and it's giving 75. Once again, it's erring on the lower

**Dave Jones:** side. So, that's interesting. Two videos. Let's try another high one, 72,000 for the EcoFlow uh battery here. That's got 87 thumbs down. What is the count over here? 82. Once again, it's erring on the lower side. So, there you

**Dave Jones:** go. Three out of three of my own videos have erred on on the lower side. So, that's a good indication that, you know, something like this is not inflated. I know there's bias and everything else. How many people are using the app?

**Dave Jones:** And a lot of people claim that the people who use the app are the ones who are most likely to, you know, dislike something. Well, doesn't really reflect in my data. So, that's like busted in my data there. I mean, I can try another

**Dave Jones:** one. So, let's try this film capacitor failure one. That doesn't hasn't got many. 51 thumbs down. Go over to here and we've got Oh, it matches. Matches precisely. 51. That's a coincidence. Let's actually choose one where I got a

**Dave Jones:** lot of thumbs down. Like this is like a real outlier. Rarely will I get a video with 80 87% like to dislike ratio. That's very low. I guess a lot of people either they didn't like it. It's about Odyssey and

**Dave Jones:** routers attacking. So, you know, there's people who don't like other. They just like only use YouTube and they'll thumbs down and Odyssey, you know, talking about Odyssey, whatever. But 143 thumbs down. And that has got 77. There you go. That's like half. So, it's

**Dave Jones:** underreported by half. So, that's interesting. If the number of dislike if the number of dislikes goes up on a particular video, the ratio of the users who are using this actually it goes it goes in the opposite direction. I even found one. What's

**Dave Jones:** that? Five now? That they're all reporting on the lower side. So, you know, I can keep going, but I think you get the idea. So, there's a lot of people who say, "Well, okay. There's how many people actually use this app? Is

**Dave Jones:** this based on like 10 people or something?" Yeah, I I I totally agree. It should it should actually pop up and tell you like how many people this is based on. That'd be really nice. You know, it's based on, you know, I like

**Dave Jones:** even if it's based on 100 users or 1,000 users or something like that. Hey, you know, all the all the political polls and other polls that you hear on, you know, phone survey they surveyed 100 people in the population and then that

**Dave Jones:** makes national news like, you know, 80% of the people vote for this or something and it's based on like a survey of 100 people or something. You know, it's right? But yeah, I totally agree. I I would support it actually if it popped

**Dave Jones:** up and, you know, told you how many people that was based on. That'd be really nice. But it doesn't. So, anyway, what I've done is I've actually created a poll. I will refresh this. I did this 5 hours ago and I've got 1,400

**Dave Jones:** responses here and I basically asked people if they could tell me, do you use this app or not? And this specific plugin, not any I think there might be one or two others, but this is by far the most popular one. Do they use it or

**Dave Jones:** not? And 25% of the my audience said they did. So, a quarter and 75% no, they do not use it. So, that's actually quite a substantial percentage, 25%. And I asked on Twitter just to get another number on this and asking the same

**Dave Jones:** thing, 225 votes and 30% said that they use it. So, I'm I'm going to run with 25%, right? A quarter of my audience actually use this plugin to watch my videos. So, that's quite substantial. But once again, these are technical

**Dave Jones:** engineering nerds mostly who watch my videos. So, you could say, you know, over represented to the general population in terms of like willingness to install plugins and stuff like that. But, you know, 25% I'm I'm quite surprised it was that high actually. So,

**Dave Jones:** there you go. Hopefully that's given you some confidence that the number here is at least like not like not like massively over I don't think it's massively over reported here. So, you know, something like this that gets, you

**Dave Jones:** you 2.8 million thumbs down or insert the latest video that everyone's talking about on on the Twitterverse or whatever, you know. And like so I it seems to be working reasonably well. It it doesn't It's certainly not over-reporting figures based on my

**Dave Jones:** audience and my data. So, there you go. I highly recommend that you install this because then it helps if everyone installs this thing, then it really it it doesn't quite recover the original functionality of the YouTube dislike button. It means that we can

**Dave Jones:** tell YouTube, "No, we've got a way around this." And it seems to work reasonably well. The only thing, yeah, as I said, I'd add is like a number here that tells us how many votes it's based on or it only gives you a or it

**Dave Jones:** only does that if it reaches a threshold of, I don't know, 100 or 1,000 or something like that would be nice. But then you wouldn't see it on like some videos that haven't got many views because it's based on an average number

**Dave Jones:** of users who use this plugin. And if people use their shoe phone, then, you know, it may they may not have that available cuz they're using the YouTube app or whatever. Somebody said there's like an another There's another app that actually has

**Dave Jones:** this built in or something that can view it, but Google tried to YouTube tried to ban it or something. I don't know the details. But anyway, I'm reasonably confident that that is not at least not over-reporting stuff. So, anyway, hope

**Dave Jones:** that was useful. Leave your thoughts and comments down below. Catch you next time.
