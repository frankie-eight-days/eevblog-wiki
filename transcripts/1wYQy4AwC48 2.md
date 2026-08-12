---
video_id: 1wYQy4AwC48
title: EEVblog 1658 - TUTORIAL: Mean vs Median
url: https://www.youtube.com/watch?v=1wYQy4AwC48
source: youtube-asr
timestamps: {"0": 0, "1": 38, "2": 52, "3": 86, "4": 116, "5": 146, "6": 181, "7": 213, "8": 230, "9": 263, "10": 283, "11": 310, "12": 337, "13": 368, "14": 396, "15": 417, "16": 446, "17": 464, "18": 496, "19": 525, "20": 556, "21": 585, "22": 599, "23": 620, "24": 655, "25": 687, "26": 719, "27": 736, "28": 748, "29": 776, "30": 798, "31": 815, "32": 837, "33": 848}
---

**Dave Jones:** Hi, just a quick tutorial video on the difference between mean, median, and average. Because if you don't get this right, you can sound like a real dolt, or people can take advantage of you by manipulating numbers. As Mark Twain said, "Lies, damn lies, and statistics." Doesn't matter who it is, engineers, scientists, the media, the government, they can manipulate you by sneakily using, interchanging these terms to give you a result that they want, and what may not represent the true reality, or it may shift the data one way or the

**Dave Jones:** other, depending on what they want you to think. So, if you know how all this works, you can spot potential manipulation and go, "Uh, you said mean. Give me the median value, please." So, we'll start out with mean. What is mean?

**Dave Jones:** Well, mean in general parlance is the average. The average when people say use the word average, they typically mean the mean. Ha, get it? They mean the mean. I'm here all week. But, the mean is actually a specific type of average that's actually called the arithmetic mean. So, when people say mean, they actually that's the terminology that they actually mean. So, or if they say average, that's generally what they mean. There's just too many means. Wow, this is heavy. Anyway, let's go through an example here to show you because

**Dave Jones:** almost all of you are surely are familiar with what an average is. And an average is simply if you've got a collection of data like this, you've got a number of values, the average or the mean or the arithmetic mean is simply all of those numbers added up and divided by the number of numbers that there are, the number of values. So, that's written the mean is in this particular case X1 + X2, so X is the value, so X2 + + + to XN, so the nth

**Dave Jones:** value divided by the number of values here n, and that gives you your mean or average value. Simple. And of course there's tons of stuff in engineering and real life where the average or the mean value is exactly what you want. It's going to give you the result that you want. But there are many cases where using the mean or the average value is going to give you a a skewed result.

**Dave Jones:** Potentially deliberately skewed result. As I said, people can manip- use these terminologies to manipulate data for nefarious means to try and persuade you one way or the other. Things can sound worse than they are, things can sound better than they are. They can do that by simply using a different type of average. So we'll go through this example here. I'm measuring 11 different resistors, okay? They're all supposed to be the same, but there's some tolerance in there. So I've got 98 ohms, 102, 103, 100, 103, 101, 97, 99, 100, 101, and 500

**Dave Jones:** ohms. So 11 different values. You get the mean or the average of those, it's 136.8. Hmm, can you smell what I can smell? Yeah, dodgy data. In this particular case, it's obvious that something's gone wrong in my measurement here. Could be the contact resistance or whatever it is, doesn't matter. 500 ohms doesn't sound right when all the others are supposed to be like near enough to 100 ohms. So of course you could just throw away that data point and not include it in your data set, but sometimes you want

**Dave Jones:** to leave that data there cuz it might be legitimate data. Let me give you another example. So let's take the classic example of home prices for example. You're almost certainly familiar with this cuz you hear it all the time, every day in the legacy media. Um, let's say these are house prices.

**Dave Jones:** 980,000, 1.02 million, 1.03 million, 1.01 million, and some Richie Rich down here in your suburb has just sold their McMansion for 5 million bucks. Well, that's kind of like an an outlier, but it is an actual real value. So, you've got to include it in your data set. So, what happens if the media or the real estate agent is trying to tell you that HOUSE PRICES ARE GOING TO THE moon in your suburb, they might use a mean or an average value. They might tell you the

**Dave Jones:** mean or the average, which includes this real outlying data point here, which gives you a mean value or an average value of 1.36 million. And you thought your suburb was only worth, you know, roundabout an average of like 1 million, but no, it's jumped up to 1.36 million.

**Dave Jones:** Unbelievable. So, using the arithmetic mean or average uh value actually has problems when you have data points that are like really outlier data points, but they might still be genuine. Or uh your data is skewed in one direction or the other. And by skewed, I mean here's an example, or in mathematical terms, they call it skewness. You can see that the data is sort of bunched up one end here, or in this particular case, the data's all bunched up in the other end here.

**Dave Jones:** And it can make a quite a substantial difference whether you use mean or median when your data is skewed one direction or the other, or you've got big outlier values. So, how do we get around these problems? Well, we use what's called the median. Once again, median is just another type of average, and there's actually many different types of averages here. I'll put up a list, and you might have to zoom in on this one. There's a ton of different type of averages. Mean and median are

**Dave Jones:** just two of them. For example, RMS is actually another form of mean. It's a mean squared, hence RMS, root mean squared. So, it mean squared is actually another type of average. So, how does median work? Well, it's very simple. All we've got to do is take our data and just sort it. So, it's a a sorted data set now. So, at 97, we get our lowest value, we put that up the top here. Top or bottom, it doesn't matter which direction you sort it, as long as it's sorted, right? So, you sort

**Dave Jones:** it from lowest to highest like this. So, 500 down the bottom, and once you sorted your data like that, you just take the actual value, the individual value that sits in the middle. So, you have an equal number of data points here, in this case five on the upper side and five on the lower side, but it doesn't matter. You can have 5 million data points. You pick the one that's right in the middle, and bingo, that value becomes your median value. So, you can see that median is actually really

**Dave Jones:** simple to calculate. It's even simpler than the arithmetic mean, because you don't have to do any division or whatever. You just pick the number, sort them, pick the number that's in the middle. No worries. So, the advantage this gives is that it pushes these outlier values right out to the end, cuz you typically don't have many of these outlier values, and they can be massive.

**Dave Jones:** This This could be, you know, a 500k or something like that, and it makes no difference. Or it could be a 500 million dollar mansion resort thing um that if we use the mean, it would have skewed that mean or average value right to the moon. But because it's only a single value in in a data set of 11 values, but it might be a couple of values in, you know, a data set of a thousand houses that sold or something else. Then, it it really those become completely

**Dave Jones:** insignificant. So, what would have happened over here to the mean if we'd actually removed this data point, this extreme outlier one? Well, run the numbers, we've got 10 of them there, and you'll find that the mean um instead of being in median of 101, the mean is actually 100.5.

**Dave Jones:** So, it's very close to the median. So, you can see that in this particular case, just by sorting them like this and choosing the middle value, we've effectively eliminated the data without actually removing it from the data set, which you don't want to do in the case of house prices or in the case of wages, for example. The government might be telling you that your average wages have risen by $10,000 this year and you go, "Yeah, I don't think so." It's because they're using the average value. Let's

**Dave Jones:** say you worked at a company, for example, and they said, "Oh, the average wage at this company is $100,000 a year." But, you know that everyone's only earning $50,000 a year. But, because the CEO is earning 50 million bucks a year, if you use the mean, that's going to push up the average value. But, if you use the median, then, you know, the CEO and the board of directors, all their massive wages, they don't uh really play a huge part as long as you've got a lot of other employees

**Dave Jones:** that are earning a similar sort of thing. So, you're getting a more real-world value when you use the median. That's why the median is used for house prices, it's used for wages, and other things that, you know, really matter to people where you can get like a lot of outliers, Richie Riches out there in the world that can actually skew the data. And there can be a ton of other examples where outlier data or skewed data will give you a substantially different result if you use the mean versus the median. Now, in

**Dave Jones:** some cases, the median might be exactly the same as the mean because you just that's just the way the data happens to work out. But, in those particular cases, you won't really have any major outliers. So, if you've got any good examples of mean versus median, leave it in the comments down below. But, I'll give you another example. Here's a report, a a report from UBS. Every year they produce a wealth report that ranks every country in the individual person's wealth in that country. Um and here's

**Dave Jones:** the list here and you can see that number one is Switzerland, number four is the US, number five is Australia. Good on us, you little ripper. But I know what you're thinking. You're looking at that number and going, "Dave, I don't have a wealth of $560,000.

**Dave Jones:** What's going on here?" Well, you know that they're manipulating stuff. But take a look at the the top. What do you see? The word average. Aha, gotcha. But I haven't shown you the full table. In this particular case, UBS know that it's manipulative to actually give you that data. So they give you two sets of data. So here is the full data set.

**Dave Jones:** They give you a table right next to it that has the median value. And look at the difference now. Just by changing that one word, average, to median, Switzerland suddenly gone from number one in the world wealthiest nation or wealthiest individuals in nations to number seven. The US has gone from a respectable number four to 14th in the world now. And Australia's gone from five to number two. You little bloody beauty. So once again, going back to the house price example or the wage example where a lot of richy riches or you know,

**Dave Jones:** rich mansions can skew that data, same thing can happen with this individual wealth. So what that means when Australia jumped from number five up to number two, what it means is that the average Australian has a much higher real world median worth than someone in the US or somebody in Switzerland. Why is that the case? Well, I won't go into the whole housing bubble thing, but yeah, Australians, because we don't have as many richy riches living here as they do in the US or in Switzerland, which

**Dave Jones:** was obviously skewing the results when we used the mean or average value. So median is the correct one to use here. Otherwise, all those richy rich Bill Gateses in the US, they're just skewing that data right to the high side. So, if you're the government or you're the manipulative legacy media, you can take either one of those values, depending on how you want to spin it, you say, "Oh, US is now 14th in the world in wealth because you use the median value." Or you might want to spin it positive, "Oh,

**Dave Jones:** US is so fantastic. Look at us go. You know, we're number four or fourth in the world with median wealth. What are you complaining about?" So, what they're doing is manipulating you to think a certain way based on how they decided to report the data. And the data is real.

**Dave Jones:** The data's in there. It's just how they decide to report it. And of course, UBS are good that they put both the values in there, so it's easy to take out. But you could also take that out if you had access to the raw data as well.

**Dave Jones:** You could just spin it. But that one simple word change, median versus mean or mean versus median or or or whatever. In this particular case, average versus median can make a huge difference. And just one small point, when you're uh calculating the median like this, uh we happen to have 11 values. So, we just happen to have an even number either side like this, so we can just choose the middle value. But what happens if you had an even number of values and and your split right in the

**Dave Jones:** middle ended up between two values? Well, you simply take the arithmetic mean of those two values. In this case, it's it's 101, but you know, let's say it was these ones like this, 101 and 103, then your median value would be the arithmetic mean of those. So, it would be 102.5.

**Dave Jones:** So, whether or not you use median versus mean, it pretty much comes down to whether or not you had, as I said, skewed data or you have really big outlier values in your measurement data. If you had like lots of noise, you might have big spurious spikes, you know, right out there or something like that.

**Dave Jones:** Then, you might want to use the median just to take those out of the average value. So, I hope you enjoyed that video and found it useful. If you did, please give it a big thumbs up and as always discuss down below and over on the EVblog forum. And I've got a new merch store and a new range of merch, not only t-shirts, but mugs and caps and all sorts of stuff at T-Public.

**Dave Jones:** I'll link that in down below as well. Check it out. Catch you next time.

**Dave Jones:** People can manipulate these things for nefarious reasons. Hmm. Oh,
