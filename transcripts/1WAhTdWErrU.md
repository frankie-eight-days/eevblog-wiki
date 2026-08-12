---
video_id: 1WAhTdWErrU
title: EEVblog #215 - Gaussian Resistors
url: https://www.youtube.com/watch?v=1WAhTdWErrU
source: youtube-asr
timestamps: {"0": 0, "1": 26, "2": 36, "3": 54, "4": 69, "5": 94, "6": 110, "7": 133, "8": 156, "9": 171, "10": 184, "11": 194, "12": 207, "13": 215, "14": 230, "15": 256, "16": 274, "17": 294, "18": 308, "19": 319, "20": 331, "21": 346, "22": 357, "23": 376, "24": 387, "25": 409, "26": 422, "27": 438, "28": 453, "29": 469, "30": 489, "31": 502, "32": 516, "33": 531, "34": 545, "35": 566, "36": 576, "37": 586, "38": 609, "39": 621, "40": 633, "41": 647, "42": 663, "43": 680, "44": 713, "45": 746, "46": 767, "47": 794, "48": 808, "49": 826, "50": 839, "51": 851, "52": 874, "53": 888, "54": 903, "55": 913, "56": 932, "57": 948, "58": 971, "59": 980, "60": 991, "61": 1005, "62": 1019, "63": 1032, "64": 1044, "65": 1053, "66": 1067, "67": 1090, "68": 1104, "69": 1127, "70": 1146, "71": 1159, "72": 1171, "73": 1186, "74": 1203, "75": 1214, "76": 1238, "77": 1251, "78": 1284, "79": 1304, "80": 1314, "81": 1336, "82": 1351, "83": 1366, "84": 1384, "85": 1399, "86": 1423, "87": 1437, "88": 1449, "89": 1468, "90": 1477, "91": 1488, "92": 1500, "93": 1522, "94": 1536, "95": 1557, "96": 1570, "97": 1599, "98": 1611, "99": 1624, "100": 1651, "101": 1660, "102": 1671, "103": 1689, "104": 1724, "105": 1738, "106": 1754, "107": 1787, "108": 1802, "109": 1821, "110": 1831, "111": 1845, "112": 1859, "113": 1877, "114": 1897, "115": 1907, "116": 1918, "117": 1936}
---

**Dave Jones:** Hi, we've talked about the humble resistor on here a fair bit over the time and I've done the recent blogs on the decade resistance boxes and how you can build your own and we've talked about tolerance a fair bit, but what exactly is the tolerance and how does it vary in your typical metal film resistor like this and it's a good question and it's something you can't

**Dave Jones:** really find in the data sheet cuz you read the data sheet for one of these things and it says, you know, it's plus minus 1% metal film resistor. Well, okay.

**Dave Jones:** Where is that actual value of this resistor going to fall within that 1%? Is it completely random? Is it shifted towards one end? Do they manufacture 10% tolerance resistors and measure them and and then mark these ones and sell these ones as 1% and sell the other ones as 5%, sell the other ones as 10%, etc.

**Dave Jones:** How do they do it? They don't really tell you on the data sheets and getting info on that sort of thing is hard. So, just what is the probability distribution, that's the technical term, of the values of a typical resistor like this?

**Dave Jones:** You damn well can't really find it in the data sheets and is it that I've always assumed, I've never actually measured it, I've always assumed and you know, I have from industry knowledge, it's just assumed to be a typical bell-shaped or what's called a normal distribution or Gaussian distribution response, but is it?

**Dave Jones:** I don't know. I've never actually seen the manufacturing graph for a resistor or not that I can recall. Maybe I have, but I don't know. If you can find one somewhere from a manufacturer, point it out, but I thought, bugger that, it'd be interesting to actually measure it.

**Dave Jones:** What are these resistors and what is their probability distribution? Well, it's easy to find out. You get a whole bunch of resistors and you measure them. Let's go. As you saw in the decade resistance box video, if you take a bunch of 1% resistors and you put them in series, then your total as what That's how a decade resistance box works.

**Dave Jones:** Put them in series and you'll end up with the same tolerance as the single resistor. So, if you've got a 1% tolerance resistor, you put 10 in series, it's 10%, but you put them in uh in parallel uh combinations, you can actually end up with a better Like if you put If you want 1K and better than 1%, but you've only got 1% resistors.

**Dave Jones:** If you put 10 10K resistors in parallel, you should end up with a better tolerance resistor than that 1% if it is actually a true uh bell-shaped Gaussian normal distribution around that center mean value.

**Dave Jones:** If it's not around the center mean value, if that center mean value shifted to one side or the other as it could be, then you you're not going to end up with that 1K, you're going to end up with something shifted down the side.

**Dave Jones:** And it all gets quite complex. If you want to actually do the math behind it, it can that can actually get quite complex, too. So, anyway, I thought we'd measure them and see what we get.

**Dave Jones:** Now, there's actually two sides to this issue. One is the case where you've got all these resistors and they're manufactured from the same batch because they're on the same bandolier.

**Dave Jones:** You can uh pretty much be assured that these were manufactured at the same time on the same bit of equipment on the same day by the same operator with the same materials, etc., etc., etc.

**Dave Jones:** at the same temperature, yada, yada, yada. So, there are quite a lot of uh process variations. So, um but because these are all from the same batch, that's one uh issue in itself.

**Dave Jones:** What is That's one thing we want to find out. We want to know what is the probability distribution of the resistors in a same production batch. And then the second issue is if okay, if you take 10 resistors and put them in parallel, but they're from if you get one resistor from separate batches that are all a year apart, well, is that distribution going to be the same as what you get

**Dave Jones:** from a one manufacturing batch distribution. It sounds complicated, but they are two separate issues. But because I don't have you know, knowing separate resistors from separate batches, you know, and all that sort of stuff, we'll just look at this case today, but this should reveal, hopefully, something interesting.

**Dave Jones:** Cuz when you measure and plot data, you'd be surprised at what can come out of the end of it. I don't know what we're going to find. Could be boring as bad And as always with electronics, you find some real interesting stuff when you start measuring things, collecting data, and just a simple aspect of graphing it.

**Dave Jones:** In this case, we're going to get a probability distribution. And we may or may not find something really interesting, but we don't know unless we actually try it, take those measurements, go to the effort to do it, see what pops out the other end.

**Dave Jones:** I have no idea, but it's going to be fun. Let's find out. Now, the resistors we're going to use today are some I've had in my possession for quite some time.

**Dave Jones:** They're Philips brand. I don't know the exact part number. Might be out in It's torn off, as you can see there, but they believe they are 1% metal film resistors.

**Dave Jones:** Now, this will probably only be valid for this particular type, metal film, cuz there are many different types of resistors. There's, you know, carbon composition resistors, and there's thick film resistors, thin film, and there's wire wound, and all sorts things.

**Dave Jones:** So, you know, we're only going to do metal film today. Now, just because we don't know the exact part number for this resistor, doesn't mean we can't figure out what it is based on the color-coded bands.

**Dave Jones:** Now, it just so happens this is one of these six-banded resistors. Now, in this case, it's got brown, black, black, brown, brown, red. And this red one, this this sixth band on the end here indicates the coefficient.

**Dave Jones:** And that can vary. If if this last band here, the sixth sixth band was actually brown, it would mean 100 ppm. But because it's red, it's actually 50 ppm.

**Dave Jones:** And if it was orange, it'd be 15 ppm. And yellow would be 25 ppm. So, you can actually work out the temperature coefficient of that resistor. Now, of course, if this was a regular three-band resistor, you know, a 5% tolerance 1 ohm or whatever, if it only had three bands, then it would of course for 1k it would be brown, black, red.

**Dave Jones:** And if it was a four-band resistor, it would actually have brown, black, black, brown. Now, the fifth band actually indicates the tolerance. In this case, it is brown, and that indicates plus minus 1%.

**Dave Jones:** If it was red, it'd be plus minus 2%. If it was green, plus minus half a percent. Blue, 0.25. Violet or purple would be 0.1%. And if it was gray, it can go down to 0.05%.

**Dave Jones:** Now, I know that this is probably enough because 1k plus minus 1% is 10 ohms. So, it's it's going to be plus minus this second digit here. But, you know, I I just want extra resolution.

**Dave Jones:** And this is where resolution counts. And also, with this sort of test, you're going to want stability. And once again, the Fluke 87 is more than stable enough for a measurement like this, but hey, I've got a HP 3478A bench meter with an extra digital resolution and better stability.

**Dave Jones:** So, hey, why not? Let's use it. So, let's gild the lily, shall we? And use the five-digit mode. I mean, you know, the 3478A has got a four-digit mode to mimic the Fluke 87, or even a three-digit mode if you're that way inclined, but we'll use the five-digit mode.

**Dave Jones:** It's warmed up, so it's nice and stable. And the other thing which can affect this sort of measurement is the change in temperature over time. So, we'll just monitor that as well, but I, you know, I wouldn't expect a major change.

**Dave Jones:** These are fairly low PPM value resistors. They're probably 50 PPM or something like that. So, but I'll just monitor the temperature change over the span of like, I don't know, what, an hour it's going to take me to actually measure these things or something.

**Dave Jones:** The temperature shouldn't change that much. So, but if you're doing, you know, this sort of stuff seriously, then you have to take those sort of things into consideration. The, you know, any changes in temperature, just physically even.

**Dave Jones:** Just physically handling a single resistor like that can actually heat it up and change its temperature, even touching the leads. You're actually heating up that resistor. So, you know, you've got to Handling can be important.

**Dave Jones:** Those sort of things. And of course, the other thing you have to consider is the repeatability of your probing system. Now, in this case, we've just got these regular 4 mm banana plug to alligator clip leads, you know, fairly cheap ones, but they they should do a fairly decent job of actually biting through any oxidization on the leads.

**Dave Jones:** And but And because we've got 1K, it's not going to be a huge differential. If we were measuring like a 100 ohm resistor or something, it might matter. Or a 10 ohm resistor would be worse.

**Dave Jones:** then the contact resistance could vary a bit, but on 1 K, it's pretty good. And if we short them out, let's have a look. And there we go, it's a 160 mΩ, 150 mΩ.

**Dave Jones:** Take it apart, put it back together, there you go, it's it's going to be within plus minus, you know, one least significant digit there. And if we just disconnect there, wiggle these around, all that sort of thing, just make sure you test the repeatability of your system.

**Dave Jones:** I'm fairly happy with that. Now, let's actually put it when you short the things out, but let's actually put it on a resistor leg, shall we? And yeah, there we go, it's the same.

**Dave Jones:** So, we're obviously, you know, we're biting through any contact resistance there, wiggle those around, and that looks pretty repeatable to me. And you know, down to the order of, you know, 100 100 mΩ.

**Dave Jones:** And there's our first resistor in this batch here, and really I've left it for a while, and it really hasn't varied much at all, you know, plus minus at most two least significant digits.

**Dave Jones:** So, you know, I'm I'm fairly happy with that. I've played around with the probing, and I've swapped it around, and I've also got it on fixed manual range here, so it won't auto range or anything like that.

**Dave Jones:** No, I'm fairly happy that this consistent results. So, I'm going to go through, measure each one of these resistors one by one. Maybe I won't do the two the whole lot, I'll do it until I get bored, and enter the values into an Excel spreadsheet, so we can do some analysis.

**Dave Jones:** Woohoo, data analysis, great fun. And just to make sure that there's no funny business with this bandolier and the Well, there's there's a little bit of glue that's actually used inside there, and you know there could be some contaminate you know some impedance across there between resistors so there might be a little bit in parallel who knows well let's check that here 999.510 let's take it off

**Dave Jones:** pull it out and 999.52 there you go not a problem I'm I'm happy with that and it actually took until resistor 129 until I found one that shows spot on 1.00000 K ohms on my meter what does that mean it means absolutely nothing because it's not even true because I haven't zeroed the thing out yet but anyway I just thought I'd share that with you resistor 129

**Dave Jones:** winner well there you have it I did actually get through all the resistors and it stopped at 400 there were like 402 but there you go 400 nice round number lots of data to work with I really like it the temperature only changed 0.1 degree over that time not that it really matters but got a lot of data to work with now it's time to graph it play

**Dave Jones:** around with it and see what pops out because often you can get some mysterious results pop out but only if you try it okay here we go we've got our data and let's do some analysis shall we now column a here is the all the 400 measured values which I entered directly from the meter but I didn't the meter didn't zero out the lead resistance so I've done that here in column b here as

**Dave Jones:** you can see I've actually subtracted 0.15 there which was the constant lead resistance and contact resistance we had I subtracted those and so they column b is the true measured value of the resistor.

**Dave Jones:** Now, column C here I've calculated the variation from a nominal in percentage from a nominal 1K value. So, that gives us our plus minus deviation which we're interested in because the resistor obviously has a claimed spec of plus minus 1%.

**Dave Jones:** So, it's better if we easier for us and clearer if we work in a percentage based value. So, that's exactly what I've got. So, column C here is the data we're actually going to plot and work from.

**Dave Jones:** Now, if you go down here and you plot column C there on a regular XY graph here, you'll see on the X axis here are all of our 400 values.

**Dave Jones:** And you'll notice that they're scattered pretty much as you'd expect. No surprises in the actual scattering and the mean is pretty close to spot on zero there. You know, if you just do it by eye, close one eye and squint a bit and you can see that the nominal's going to be, you know, reasonably close to zero.

**Dave Jones:** So, no surprise there at all. But, one of the big surprises I found is that no value went over plus point six or minus point six. Actually, it's about plus point five.

**Dave Jones:** No value went over that. So, that was a surprising result. I expected to get values very close to the nominal to the claimed spec of plus minus 1%. But, it turns out these resistors seem to be much tighter tolerance.

**Dave Jones:** I mean, out of 400 resistors, I expected at least a few outlier ones to be right out near that, you know, point nine, point eight percent at least variation.

**Dave Jones:** But, we didn't see that. It's the the biggest values are plus half a percent and minus six. Very surprising. And if you're curious to know what the actual uh nominal average value is, it's 999.72 ohms.

**Dave Jones:** There you go. And I guess the other thing to note is that uh the resistors zero through four uh one through 400 here are actually uh in sequence as I measured them on the bandolier from one end of the bandolier to the other end.

**Dave Jones:** So, uh there are no sort of oscillations or anything like that in there that are immediately apparent. Uh so, they are actually truly randomly uh scattered. So, I think if you mixed up those resistors and measured them all again or or just unsorted the you know, just uh did a different sort on on that and just randomized it, you'd get the same result.

**Dave Jones:** So, that brings up another interesting point. What do we get if we actually sort all of the values from lowest to highest or highest to lowest? It doesn't really matter.

**Dave Jones:** Uh so, we're going to select these columns over here. We sort ascending. And as you can see, the values in column C there are now sorted. What does that give us on the graph?

**Dave Jones:** Bingo, there it is. And no surprises for me at all. This is exactly I've seen this countless times. This is exactly what I expect from a bunch of uh random data and a Gaussian distribution at that, which we'll get on to.

**Dave Jones:** Uh uh uh sorted uh graph of just uh random uh data. Because if it's a bell-shaped Gaussian distribution, you'd expect to sort of get most of your values like this.

**Dave Jones:** So, the slope in the middle here um to be quite uh shallow. And the slope just gets steeper and steeper at the ends where the outliers are cuz there's fewer outlying values.

**Dave Jones:** So, that's a very typical uh Gaussian type uh response for random data. And this, uh, particular method is useful for showing, uh, offsets better and, uh, things like that.

**Dave Jones:** Ideally, you would, um, if you had zero, you'd expect it to be right smack in the center of the graph there, but you can see there is a little, uh, tiny offset in there.

**Dave Jones:** And, uh, this is just a useful, another useful way to interpret the data, but no surprises there at all. So, I think we're going to get our Gaussian uh, bell-shaped response when we do our frequency analysis.

**Dave Jones:** Now, what we want to do is some frequency analysis. Now, it's similar to the difference between time domain and frequency, uh, domain that you're probably used to. In this case, this, uh, data over here, uh, it can be considered the time domain data and this and the data we're now going to analyze to get our histogram is the frequency domain data.

**Dave Jones:** And the way this works is, uh, you create uh, different bins. In this case, um, I've got, uh, 21 bins ranging from 1% uh, down in 0.1% uh, increments down to minus 1%.

**Dave Jones:** And we want to find out, uh, how many of, uh, these particular values appear in each one of those bins. So, we're doing a frequency, uh, sort here. So, we're going to use, um, the frequency command, which is available in Excel or, uh, OpenOffice, which is what we're, uh, using here.

**Dave Jones:** And, um, it it, uh, takes all of this input data in column C here and, uh, it it, uh, analyzes all this data and counts how many of a particular, um, uh, how many items actually fall within each one of these bins over here.

**Dave Jones:** And the way you do this is you use the frequency command. It accepts two input parameters here. And uh, uh as you can see in the help uh pop-up here, it's got um data.

**Dave Jones:** So, the first uh part of this is the data set, in this case C. We want column C here, and we want all of the data. Now, a little trap here is you've got to put in the dollar signs there and there, there, and there.

**Dave Jones:** Now, the reason you have to do that is because when you uh when you actually create this thing and then drag it down like this, you want all of um other it will actually uh increment um that C value unless you put the dollars in there.

**Dave Jones:** And for each one of these, you want to sort through all of the data. So, putting the dollars in there ensures that you actually uh do that. Now, the second um one up here is actually called classes, but it's uh it's bins and is the other name for it, which we're going to use here.

**Dave Jones:** So, these bins are in column I, I 2 to I 22 down here, as you can see. And we've got those 21 bins, and the frequency command is just magic.

**Dave Jones:** It just goes through and calc and counts the data in those bins and converts it effectively into the frequency domain. So, then, once we've got the data here in column H in the frequency domain, we can just plot it exactly the same as we did before, exactly the same plot, except we're doing a column uh graph, and bingo, this is the response we get out of this, and that is our

**Dave Jones:** histogram. And as you can see, it does show that normal distribution exactly as we were expecting. No surprises there at all. It's centered uh preci- it's centered on zero there, around about zero.

**Dave Jones:** And it but the big surprise, of course, is that it only extends to plus minus half a percent. There are no outlying values uh out right out here, as we saw in our other graph, but it's uh clearer here that the uh um because this effectively represents this gra- this uh distribution, normal or Gaussian uh bell-shaped distribution, uh effectively represents the uh probability of one of these resistors

**Dave Jones:** actually being manufactured out here in the outliers. As you can see, most of them are going to be within the you know, tight 0% bin there, a good lot of them are going to be, you know, plus minus 0.1% either side of that, and you know, a fair number uh plus minus 0.2%, and then you start getting into the outliers out here.

**Dave Jones:** And once you get to 0.5%, well, there's just almost nothing left. There's only a couple of items down in, you know, five or under in these sort of bins.

**Dave Jones:** Now, it's not a perfectly shaped uh uh bell-shaped curve there or Gaussian response. You've got to use your imagination a bit. Um like this one here in the 0.3%, it, you know, should have been up a bit, and this one should have, you know, these should have been down, this one should have been up a bit here and up a bit, and well, you know, in an

**Dave Jones:** ideal world, that would be an ideal-shaped curve. And really, with a random a true random set of data, um as you'll get with a manufacturing uh process uh like this, you will ultimately um get that provided two things.

**Dave Jones:** Uh provided A that you have enough data. Now, in this case, we've only got 400. Now, 400 sounds like a lot um when you're and and it is a lot when you're plotting just uh the data like this.

**Dave Jones:** That's an awful lot of uh you know, data, more data than you can poke a stick at. But, when you're doing frequency analysis like this, you're left with uh fewer and fewer uh actual items in each bin uh when you actually convert it into the frequency domain like that.

**Dave Jones:** Now, um we can uh change we can change this by increasing the number of bins we've got. And that's what I'll do over here, but um then you effectively halve your number of uh data in that particular bin.

**Dave Jones:** So, when you're doing frequency analysis like this, the more data you have, the better. It's very important. And in theory, if we had an infinite number of infinite amount of data to work with, and we did a large enough number of bins, then we would find ultimately that it would average out, and we would get our perfect uh normal distribution Gaussian response curve.

**Dave Jones:** So, as you can see, this one's a bit rough and ready here. It's a you know, it it really is a rough as guts kind of thing, but you can still see because we are expecting uh that Gaussian response, you can actually see it.

**Dave Jones:** And and it is there. But what happens if we increase our number of bins? Now, I've done exactly the same uh thing here, except I've got 41 bins instead of 21.

**Dave Jones:** I've actually uh doubled the number of bins here. And as I said, you halve the number of items when you do that. So, you need so you can't just uh you know, increase the number of bins to an infinite amount, cuz then you'll end up with no data at all um in each bin or one item in randomly spaced bins, and it'll be useless.

**Dave Jones:** So, um but the more data you have, the uh it it's beneficial to uh have a higher number of bins like this. And you know, our highest number here is uh 61.

**Dave Jones:** Here, that's not too bad, but uh you know, when you start getting to the outliers down here, you know, this one's zero, and this one's one, and you know, it's a bit it's a bit over the shop there.

**Dave Jones:** But anyway, I've done exactly the same uh thing exactly the same formulas here, except I've got twice as many bins. And when you plot that and you go over here, here it is.

**Dave Jones:** There is your response. And as you can see, it's a bit more fine detail cuz we've doubled our number of bins. And as you can see, there's probably a slight offset there on the negative side of things as you'd expect when because we've got a slight negative offset.

**Dave Jones:** If you look down here, you remember we had a slight negative offset in our average value. And also you saw that on our sorted graph. And that manifests itself on the histogram here by having a slight offset.

**Dave Jones:** And if you're not centered around the mean, this histogram will actually move either side like this. But I'm very impressed and not really surprised that the manufacturing tolerance for these good quality Philips resistors are actually right on that 0%.

**Dave Jones:** Now, the really interesting thing though is that as we've said before, it sort of peters out at 0.5 plus minus 0.5% not the plus minus 1% which you were expecting.

**Dave Jones:** So this kind of Well, it doesn't really bust the myth, but it does in this case in for this particular batch from Philips, the metal film resistors at this particular time manufactured in this factory, they clearly weren't targeting as a lot of people claim that they manufacture say 5% resistors and then they test them all and the ones that passed to a plus minus 1%, they sell

**Dave Jones:** them as mark them and sell them as plus minus 1% and the others they sell as plus minus 5%. Well, that's clearly not the case because if that was the case, you would expect Well, I would expect a response which is much shallower.

**Dave Jones:** It would still kind of be like the peak the top sort of peak of that Gaussian response. So, I would have because imagine if this is plus minus 5% here, okay?

**Dave Jones:** And then we're getting the plus minus 1% bin. So, we'd only be seeing that little bit over there like that. So, that would manifest itself maybe in a graph which started out say at 30 here and all the let's say 20 at 20 here and sort of went up and peaked like that pretty quick and then rolled off sort of, you know, once again down at say

**Dave Jones:** around about 20 here for argument's sake. So, it would have been that much flatter and we would have seen a a you know, a reasonably large number of resistors out here at the 1% limits.

**Dave Jones:** And that if you get the cheap 100 low resistors or something like that, you buy them from, you know, off eBay and you measure them and they could very well be 5% resistors tested as 1%.

**Dave Jones:** Who knows? I don't know. Maybe they don't do that anymore. Maybe it's a myth maybe it's a myth these days. Maybe they did it in the old days, but these days they would have targeted they they could target their manufacturing processes as you tweak them they can get better and better.

**Dave Jones:** And that's what Philips have clearly done here with these resistors. Their manufacturing processes and tolerances are obviously geared around a plus minus five 0.5% manufacturing tolerance. So, maybe they sell these resistors they target market them as 0.5% resistors and they sell those as plus minus 1% because they know they're going to be well within plus minus 1% and maybe when they sell them and mark them as 0.5% resistors

**Dave Jones:** possibly they, you know, they they lose a few, you know, percent. They might be losing 5% of their resistors out here and out here, but there you go. I I, you know, they're clearly targeting 0.5% resistors.

**Dave Jones:** So, ultimately what these kind of manufacturing normal Gaussian response curves show, which is it's typical not only for resistors, but you know, most other components as well. You're going to get this sort of manufacturing response.

**Dave Jones:** If, you know, you've got a noise floor of an op-amp or something, it's going to have this same type of Gaussian response. And what it basically represents is a probability or the probability of a particular device you buy, in this case it's a resistor, but it could be an IC or an LED with its brightness or whatever, where it's going to fall within this the probability of you getting a

**Dave Jones:** device which falls within this range. And as you can see, the highest probability is going to be smack on zero like this and the next highest, you know, and you've got a fairly good chance that you're going to fall within that plus minus 0.1% range at least for these Philips resistors.

**Dave Jones:** Remember, this may not be the case for some cheap one hung low brand resistors or something like that. So, but your odds of getting a resistor that's, you know, right out here in this case, for this particular batch, the odds of getting like a 0.8% resistor out here are almost bordering on zero.

**Dave Jones:** I'm not going to say it's not possible, but it's very, very unlikely. And getting one right at the 1% limit in this particular case, well, you know, it's pretty rare.

**Dave Jones:** I mean, we had 400 resistors. That's I guess that's not a huge number, but you know, if you maybe if you got 40,000 resistors or or you might see a few that sort of, you know, poke their head out just just like this one did it, you know, 0.55 out here.

**Dave Jones:** Given Ultimately, given enough time, anything is given enough numbers, any probability There's no such thing as a zero probability out here. They can actually appear, but it's very unlikely.

**Dave Jones:** And the other thing to remember with these um uh responses is that they can shift like this. And this will be in in the manufacturing environment, they will actually uh do plots like this, uh you know, either daily or weekly to track their uh manufacturing and how it's drifting.

**Dave Jones:** And you might see the peak actually drift back and forth as you change uh man you know, various uh you know, change materials, you've got suppliers, you change workers who are operating the machinery perhaps um you know, if it if it requires some sort of manual process or manual intervention or something like that.

**Dave Jones:** And you can watch your uh you can watch your processes drift or if your temperature's changing in your manufacturing environment, that can alter things and all sorts of things.

**Dave Jones:** So, you can get really some good insights into manufacturing uh whether components or products or whatever it is you're manufacturing using this frequency analysis. It's a really good tool.

**Dave Jones:** So, I hope you found that interesting. There are a couple of uh surprises in there, but there you go. We got our Gaussian response exactly as we expected. And if you've got more uh data on how they actually manufacture these things um these days anyway, um then yeah, send us the information.

**Dave Jones:** I'll catch you next time. probability distribut So, just what is the probability distribut probability distribution Planes flying over. Got to stop filming, go figure. Geez, you'd think I'm in the flight path or something instead out here in the suburbs.
