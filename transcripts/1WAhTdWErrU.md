---
video_id: 1WAhTdWErrU
title: EEVblog #215 - Gaussian Resistors
url: https://www.youtube.com/watch?v=1WAhTdWErrU
source: youtube-asr
---

**Dave Jones:** Hi, we've talked about the humble resistor on here a fair bit over the time and I've done the recent blogs on the decade resistance boxes and how you can build your own and we've talked about tolerance a fair bit, but

**Dave Jones:** what exactly is the tolerance and how does it vary in your typical metal film resistor like this and it's a good question and it's something you can't really find in the data sheet cuz you read the data sheet for one of these

**Dave Jones:** things and it says, you know, it's plus minus 1% metal film resistor. Well, okay. Where is that actual value of this resistor going to fall within that 1%? Is it completely random? Is it shifted towards one end? Do they manufacture 10%

**Dave Jones:** tolerance resistors and measure them and and then mark these ones and sell these ones as 1% and sell the other ones as 5%, sell the other ones as 10%, etc. How do they do it? They don't really tell

**Dave Jones:** you on the data sheets and getting info on that sort of thing is hard. So, just what is the probability distribution, that's the technical term, of the values of a typical resistor like this? You damn well can't really find it in the

**Dave Jones:** data sheets and is it that I've always assumed, I've never actually measured it, I've always assumed and you know, I have from industry knowledge, it's just assumed to be a typical bell-shaped or what's called a normal distribution or Gaussian distribution response, but

**Dave Jones:** is it? I don't know. I've never actually seen the manufacturing graph for a resistor or not that I can recall. Maybe I have, but I don't know. If you can find one somewhere from a manufacturer, point it out, but I thought, bugger

**Dave Jones:** that, it'd be interesting to actually measure it. What are these resistors and what is their probability distribution? Well, it's easy to find out. You get a whole bunch of resistors and you measure them. Let's go. As you saw in the decade resistance box

**Dave Jones:** video, if you take a bunch of 1% resistors and you put them in series, then your total as what That's how a decade resistance box works. Put them in series and you'll end up with the same tolerance as the single resistor. So, if

**Dave Jones:** you've got a 1% tolerance resistor, you put 10 in series, it's 10%, but you put them in uh in parallel uh combinations, you can actually end up with a better Like if you put If you want 1K and

**Dave Jones:** better than 1%, but you've only got 1% resistors. If you put 10 10K resistors in parallel, you should end up with a better tolerance resistor than that 1% if it is actually a true uh bell-shaped Gaussian normal distribution around that

**Dave Jones:** center mean value. If it's not around the center mean value, if that center mean value shifted to one side or the other as it could be, then you you're not going to end up with that 1K, you're going to end up with something shifted

**Dave Jones:** down the side. And it all gets quite complex. If you want to actually do the math behind it, it can that can actually get quite complex, too. So, anyway, I thought we'd measure them and see what we get. Now, there's actually two sides

**Dave Jones:** to this issue. One is the case where you've got all these resistors and they're manufactured from the same batch because they're on the same bandolier. You can uh pretty much be assured that these were manufactured at the same time on

**Dave Jones:** the same bit of equipment on the same day by the same operator with the same materials, etc., etc., etc. at the same temperature, yada, yada, yada. So, there are quite a lot of uh process variations. So, um but because these are all from the same

**Dave Jones:** batch, that's one uh issue in itself. What is That's one thing we want to find out. We want to know what is the probability distribution of the resistors in a same production batch. And then the second issue is if okay, if you take 10

**Dave Jones:** resistors and put them in parallel, but they're from if you get one resistor from separate batches that are all a year apart, well, is that distribution going to be the same as what you get from a one manufacturing batch

**Dave Jones:** distribution. It sounds complicated, but they are two separate issues. But because I don't have you know, knowing separate resistors from separate batches, you know, and all that sort of stuff, we'll just look at this case today, but this should reveal,

**Dave Jones:** hopefully, something interesting. Cuz when you measure and plot data, you'd be surprised at what can come out of the end of it. I don't know what we're going to find. Could be boring as bad And as always with

**Dave Jones:** electronics, you find some real interesting stuff when you start measuring things, collecting data, and just a simple aspect of graphing it. In this case, we're going to get a probability distribution. And we may or may not find something really

**Dave Jones:** interesting, but we don't know unless we actually try it, take those measurements, go to the effort to do it, see what pops out the other end. I have no idea, but it's going to be fun. Let's find out. Now, the resistors we're going

**Dave Jones:** to use today are some I've had in my possession for quite some time. They're Philips brand. I don't know the exact part number. Might be out in It's torn off, as you can see there, but they believe they are 1% metal film

**Dave Jones:** resistors. Now, this will probably only be valid for this particular type, metal film, cuz there are many different types of resistors. There's, you know, carbon composition resistors, and there's thick film resistors, thin film, and there's wire wound, and all sorts things. So, you

**Dave Jones:** know, we're only going to do metal film today. Now, just because we don't know the exact part number for this resistor, doesn't mean we can't figure out what it is based on the color-coded bands. Now, it just so happens this is one of these

**Dave Jones:** six-banded resistors. Now, in this case, it's got brown, black, black, brown, brown, red. And this red one, this this sixth band on the end here indicates the coefficient. And that can vary. If if this last band here, the sixth sixth

**Dave Jones:** band was actually brown, it would mean 100 ppm. But because it's red, it's actually 50 ppm. And if it was orange, it'd be 15 ppm. And yellow would be 25 ppm. So, you can actually work out the temperature coefficient of that

**Dave Jones:** resistor. Now, of course, if this was a regular three-band resistor, you know, a 5% tolerance 1 ohm or whatever, if it only had three bands, then it would of course for 1k it would be brown, black, red. And if it was a

**Dave Jones:** four-band resistor, it would actually have brown, black, black, brown. Now, the fifth band actually indicates the tolerance. In this case, it is brown, and that indicates plus minus 1%. If it was red, it'd be plus minus 2%. If it

**Dave Jones:** was green, plus minus half a percent. Blue, 0.25. Violet or purple would be 0.1%. And if it was gray, it can go down to 0.05%. Now, I know that this is probably enough because 1k plus minus 1% is 10 ohms. So, it's it's

**Dave Jones:** going to be plus minus this second digit here. But, you know, I I just want extra resolution. And this is where resolution counts. And also, with this sort of test, you're going to want stability. And once again, the Fluke 87 is more

**Dave Jones:** than stable enough for a measurement like this, but hey, I've got a HP 3478A bench meter with an extra digital resolution and better stability. So, hey, why not? Let's use it. So, let's gild the lily, shall we? And use the

**Dave Jones:** five-digit mode. I mean, you know, the 3478A has got a four-digit mode to mimic the Fluke 87, or even a three-digit mode if you're that way inclined, but we'll use the five-digit mode. It's warmed up, so it's nice and stable. And the other

**Dave Jones:** thing which can affect this sort of measurement is the change in temperature over time. So, we'll just monitor that as well, but I, you know, I wouldn't expect a major change. These are fairly low PPM value resistors. They're

**Dave Jones:** probably 50 PPM or something like that. So, but I'll just monitor the temperature change over the span of like, I don't know, what, an hour it's going to take me to actually measure these things or something. The temperature shouldn't change that much.

**Dave Jones:** So, but if you're doing, you know, this sort of stuff seriously, then you have to take those sort of things into consideration. The, you know, any changes in temperature, just physically even. Just physically handling a single resistor like that can actually heat it

**Dave Jones:** up and change its temperature, even touching the leads. You're actually heating up that resistor. So, you know, you've got to Handling can be important. Those sort of things. And of course, the other thing you have to consider is the

**Dave Jones:** repeatability of your probing system. Now, in this case, we've just got these regular 4 mm banana plug to alligator clip leads, you know, fairly cheap ones, but they they should do a fairly decent job of actually biting through any

**Dave Jones:** oxidization on the leads. And but And because we've got 1K, it's not going to be a huge differential. If we were measuring like a 100 ohm resistor or something, it might matter. Or a 10 ohm resistor would be worse. then the

**Dave Jones:** contact resistance could vary a bit, but on 1 K, it's pretty good. And if we short them out, let's have a look. And there we go, it's a 160 mΩ, 150 mΩ. Take it apart, put it back together, there you go, it's

**Dave Jones:** it's going to be within plus minus, you know, one least significant digit there. And if we just disconnect there, wiggle these around, all that sort of thing, just make sure you test the repeatability of your system. I'm fairly happy with that. Now,

**Dave Jones:** let's actually put it when you short the things out, but let's actually put it on a resistor leg, shall we? And yeah, there we go, it's the same. So, we're obviously, you know, we're biting through any contact resistance

**Dave Jones:** there, wiggle those around, and that looks pretty repeatable to me. And you know, down to the order of, you know, 100 100 mΩ. And there's our first resistor in this batch here, and really I've left it for a

**Dave Jones:** while, and it really hasn't varied much at all, you know, plus minus at most two least significant digits. So, you know, I'm I'm fairly happy with that. I've played around with the probing, and I've swapped it around, and

**Dave Jones:** I've also got it on fixed manual range here, so it won't auto range or anything like that. No, I'm fairly happy that this consistent results. So, I'm going to go through, measure each one of these resistors one by one. Maybe I won't do the two the

**Dave Jones:** whole lot, I'll do it until I get bored, and enter the values into an Excel spreadsheet, so we can do some analysis. Woohoo, data analysis, great fun. And just to make sure that there's no funny business with this bandolier and the

**Dave Jones:** Well, there's there's a little bit of glue that's actually used inside there, and you know there could be some contaminate you know some impedance across there between resistors so there might be a little bit in parallel who knows well let's

**Dave Jones:** check that here 999.510 let's take it off pull it out and 999.52 there you go not a problem I'm I'm happy with that and it actually took until resistor 129 until I found one that shows spot on 1.00000

**Dave Jones:** K ohms on my meter what does that mean it means absolutely nothing because it's not even true because I haven't zeroed the thing out yet but anyway I just thought I'd share that with you resistor 129 winner well there you have it I did

**Dave Jones:** actually get through all the resistors and it stopped at 400 there were like 402 but there you go 400 nice round number lots of data to work with I really like it the temperature only changed 0.1 degree over that time not that it really

**Dave Jones:** matters but got a lot of data to work with now it's time to graph it play around with it and see what pops out because often you can get some mysterious results pop out but only if you try it okay here we go we've got our

**Dave Jones:** data and let's do some analysis shall we now column a here is the all the 400 measured values which I entered directly from the meter but I didn't the meter didn't zero out the lead resistance so I've done that here in column b here as

**Dave Jones:** you can see I've actually subtracted 0.15 there which was the constant lead resistance and contact resistance we had I subtracted those and so they column b is the true measured value of the resistor. Now, column C here I've calculated the

**Dave Jones:** variation from a nominal in percentage from a nominal 1K value. So, that gives us our plus minus deviation which we're interested in because the resistor obviously has a claimed spec of plus minus 1%. So, it's better if we easier

**Dave Jones:** for us and clearer if we work in a percentage based value. So, that's exactly what I've got. So, column C here is the data we're actually going to plot and work from. Now, if you go down here and you plot column C there on a

**Dave Jones:** regular XY graph here, you'll see on the X axis here are all of our 400 values. And you'll notice that they're scattered pretty much as you'd expect. No surprises in the actual scattering and the mean is pretty close to spot on zero

**Dave Jones:** there. You know, if you just do it by eye, close one eye and squint a bit and you can see that the nominal's going to be, you know, reasonably close to zero. So, no surprise there at all. But, one

**Dave Jones:** of the big surprises I found is that no value went over plus point six or minus point six. Actually, it's about plus point five. No value went over that. So, that was a surprising result. I expected to get values very close to the nominal

**Dave Jones:** to the claimed spec of plus minus 1%. But, it turns out these resistors seem to be much tighter tolerance. I mean, out of 400 resistors, I expected at least a few outlier ones to be right out near that, you know, point nine, point

**Dave Jones:** eight percent at least variation. But, we didn't see that. It's the the biggest values are plus half a percent and minus six. Very surprising. And if you're curious to know what the actual uh nominal average value is, it's 999.72

**Dave Jones:** ohms. There you go. And I guess the other thing to note is that uh the resistors zero through four uh one through 400 here are actually uh in sequence as I measured them on the bandolier from one end of the bandolier

**Dave Jones:** to the other end. So, uh there are no sort of oscillations or anything like that in there that are immediately apparent. Uh so, they are actually truly randomly uh scattered. So, I think if you mixed up those resistors and

**Dave Jones:** measured them all again or or just unsorted the you know, just uh did a different sort on on that and just randomized it, you'd get the same result. So, that brings up another interesting point. What do we get if we

**Dave Jones:** actually sort all of the values from lowest to highest or highest to lowest? It doesn't really matter. Uh so, we're going to select these columns over here. We sort ascending. And as you can see, the values in column C there are now

**Dave Jones:** sorted. What does that give us on the graph? Bingo, there it is. And no surprises for me at all. This is exactly I've seen this countless times. This is exactly what I expect from a bunch of uh random data and a Gaussian distribution

**Dave Jones:** at that, which we'll get on to. Uh uh uh sorted uh graph of just uh random uh data. Because if it's a bell-shaped Gaussian distribution, you'd expect to sort of get most of your values like this. So, the slope in the middle here um to be

**Dave Jones:** quite uh shallow. And the slope just gets steeper and steeper at the ends where the outliers are cuz there's fewer outlying values. So, that's a very typical uh Gaussian type uh response for random data. And this, uh, particular method is

**Dave Jones:** useful for showing, uh, offsets better and, uh, things like that. Ideally, you would, um, if you had zero, you'd expect it to be right smack in the center of the graph there, but you can see there is a

**Dave Jones:** little, uh, tiny offset in there. And, uh, this is just a useful, another useful way to interpret the data, but no surprises there at all. So, I think we're going to get our Gaussian uh, bell-shaped response when we do our

**Dave Jones:** frequency analysis. Now, what we want to do is some frequency analysis. Now, it's similar to the difference between time domain and frequency, uh, domain that you're probably used to. In this case, this, uh, data over here, uh, it can be

**Dave Jones:** considered the time domain data and this and the data we're now going to analyze to get our histogram is the frequency domain data. And the way this works is, uh, you create uh, different bins. In this case, um, I've got, uh, 21 bins

**Dave Jones:** ranging from 1% uh, down in 0.1% uh, increments down to minus 1%. And we want to find out, uh, how many of, uh, these particular values appear in each one of those bins. So, we're doing a frequency, uh, sort here. So,

**Dave Jones:** we're going to use, um, the frequency command, which is available in Excel or, uh, OpenOffice, which is what we're, uh, using here. And, um, it it, uh, takes all of this input data in column C here and, uh, it it, uh, analyzes all this

**Dave Jones:** data and counts how many of a particular, um, uh, how many items actually fall within each one of these bins over here. And the way you do this is you use the frequency command. It accepts two input parameters

**Dave Jones:** here. And uh, uh as you can see in the help uh pop-up here, it's got um data. So, the first uh part of this is the data set, in this case C. We want column C here, and we want all of the data.

**Dave Jones:** Now, a little trap here is you've got to put in the dollar signs there and there, there, and there. Now, the reason you have to do that is because when you uh when you actually create this thing and

**Dave Jones:** then drag it down like this, you want all of um other it will actually uh increment um that C value unless you put the dollars in there. And for each one of these, you want to sort through all

**Dave Jones:** of the data. So, putting the dollars in there ensures that you actually uh do that. Now, the second um one up here is actually called classes, but it's uh it's bins and is the other name for it, which we're going to use here. So, these

**Dave Jones:** bins are in column I, I 2 to I 22 down here, as you can see. And we've got those 21 bins, and the frequency command is just magic. It just goes through and calc and counts the data in those bins

**Dave Jones:** and converts it effectively into the frequency domain. So, then, once we've got the data here in column H in the frequency domain, we can just plot it exactly the same as we did before, exactly the same plot, except we're

**Dave Jones:** doing a column uh graph, and bingo, this is the response we get out of this, and that is our histogram. And as you can see, it does show that normal distribution exactly as we were expecting. No surprises there at

**Dave Jones:** all. It's centered uh preci- it's centered on zero there, around about zero. And it but the big surprise, of course, is that it only extends to plus minus half a percent. There are no outlying values uh out right out here, as we saw in our

**Dave Jones:** other graph, but it's uh clearer here that the uh um because this effectively represents this gra- this uh distribution, normal or Gaussian uh bell-shaped distribution, uh effectively represents the uh probability of one of these resistors actually being manufactured out here in

**Dave Jones:** the outliers. As you can see, most of them are going to be within the you know, tight 0% bin there, a good lot of them are going to be, you know, plus minus 0.1% either side of that, and you

**Dave Jones:** know, a fair number uh plus minus 0.2%, and then you start getting into the outliers out here. And once you get to 0.5%, well, there's just almost nothing left. There's only a couple of items down in, you know,

**Dave Jones:** five or under in these sort of bins. Now, it's not a perfectly shaped uh uh bell-shaped curve there or Gaussian response. You've got to use your imagination a bit. Um like this one here in the 0.3%, it, you know, should have

**Dave Jones:** been up a bit, and this one should have, you know, these should have been down, this one should have been up a bit here and up a bit, and well, you know, in an ideal world, that would be an

**Dave Jones:** ideal-shaped curve. And really, with a random a true random set of data, um as you'll get with a manufacturing uh process uh like this, you will ultimately um get that provided two things. Uh provided A that you have

**Dave Jones:** enough data. Now, in this case, we've only got 400. Now, 400 sounds like a lot um when you're and and it is a lot when you're plotting just uh the data like this. That's an awful lot of uh you

**Dave Jones:** know, data, more data than you can poke a stick at. But, when you're doing frequency analysis like this, you're left with uh fewer and fewer uh actual items in each bin uh when you actually convert it into the

**Dave Jones:** frequency domain like that. Now, um we can uh change we can change this by increasing the number of bins we've got. And that's what I'll do over here, but um then you effectively halve your number of uh data in that particular bin. So,

**Dave Jones:** when you're doing frequency analysis like this, the more data you have, the better. It's very important. And in theory, if we had an infinite number of infinite amount of data to work with, and we did a large enough number of

**Dave Jones:** bins, then we would find ultimately that it would average out, and we would get our perfect uh normal distribution Gaussian response curve. So, as you can see, this one's a bit rough and ready here. It's a you know, it it really is a

**Dave Jones:** rough as guts kind of thing, but you can still see because we are expecting uh that Gaussian response, you can actually see it. And and it is there. But what happens if we increase our number of bins? Now, I've done exactly the same uh

**Dave Jones:** thing here, except I've got 41 bins instead of 21. I've actually uh doubled the number of bins here. And as I said, you halve the number of items when you do that. So, you need so you can't just

**Dave Jones:** uh you know, increase the number of bins to an infinite amount, cuz then you'll end up with no data at all um in each bin or one item in randomly spaced bins, and it'll be useless. So, um but the

**Dave Jones:** more data you have, the uh it it's beneficial to uh have a higher number of bins like this. And you know, our highest number here is uh 61. Here, that's not too bad, but uh you know, when you start getting to the outliers

**Dave Jones:** down here, you know, this one's zero, and this one's one, and you know, it's a bit it's a bit over the shop there. But anyway, I've done exactly the same uh thing exactly the same formulas here, except I've got twice as many bins. And

**Dave Jones:** when you plot that and you go over here, here it is. There is your response. And as you can see, it's a bit more fine detail cuz we've doubled our number of bins. And as you can see, there's

**Dave Jones:** probably a slight offset there on the negative side of things as you'd expect when because we've got a slight negative offset. If you look down here, you remember we had a slight negative offset in our average value. And also you saw

**Dave Jones:** that on our sorted graph. And that manifests itself on the histogram here by having a slight offset. And if you're not centered around the mean, this histogram will actually move either side like this. But I'm very impressed and

**Dave Jones:** not really surprised that the manufacturing tolerance for these good quality Philips resistors are actually right on that 0%. Now, the really interesting thing though is that as we've said before, it sort of peters out at 0.5 plus minus 0.5% not the

**Dave Jones:** plus minus 1% which you were expecting. So this kind of Well, it doesn't really bust the myth, but it does in this case in for this particular batch from Philips, the metal film resistors at this particular time manufactured in this factory, they

**Dave Jones:** clearly weren't targeting as a lot of people claim that they manufacture say 5% resistors and then they test them all and the ones that passed to a plus minus 1%, they sell them as mark them and sell them as plus

**Dave Jones:** minus 1% and the others they sell as plus minus 5%. Well, that's clearly not the case because if that was the case, you would expect Well, I would expect a response which is much shallower. It would still kind of be like the peak the

**Dave Jones:** top sort of peak of that Gaussian response. So, I would have because imagine if this is plus minus 5% here, okay? And then we're getting the plus minus 1% bin. So, we'd only be seeing that little bit over there like that.

**Dave Jones:** So, that would manifest itself maybe in a graph which started out say at 30 here and all the let's say 20 at 20 here and sort of went up and peaked like that pretty quick and then rolled off sort

**Dave Jones:** of, you know, once again down at say around about 20 here for argument's sake. So, it would have been that much flatter and we would have seen a a you know, a reasonably large number of resistors out here at the 1% limits. And

**Dave Jones:** that if you get the cheap 100 low resistors or something like that, you buy them from, you know, off eBay and you measure them and they could very well be 5% resistors tested as 1%. Who knows? I don't know. Maybe they don't do

**Dave Jones:** that anymore. Maybe it's a myth maybe it's a myth these days. Maybe they did it in the old days, but these days they would have targeted they they could target their manufacturing processes as you tweak them they can get better and

**Dave Jones:** better. And that's what Philips have clearly done here with these resistors. Their manufacturing processes and tolerances are obviously geared around a plus minus five 0.5% manufacturing tolerance. So, maybe they sell these resistors they target market them as 0.5% resistors and

**Dave Jones:** they sell those as plus minus 1% because they know they're going to be well within plus minus 1% and maybe when they sell them and mark them as 0.5% resistors possibly they, you know, they they lose a few, you know, percent. They might be

**Dave Jones:** losing 5% of their resistors out here and out here, but there you go. I I, you know, they're clearly targeting 0.5% resistors. So, ultimately what these kind of manufacturing normal Gaussian response curves show, which is it's typical not only for

**Dave Jones:** resistors, but you know, most other components as well. You're going to get this sort of manufacturing response. If, you know, you've got a noise floor of an op-amp or something, it's going to have this same type of Gaussian response. And what it basically

**Dave Jones:** represents is a probability or the probability of a particular device you buy, in this case it's a resistor, but it could be an IC or an LED with its brightness or whatever, where it's going to fall within this the probability of you getting a

**Dave Jones:** device which falls within this range. And as you can see, the highest probability is going to be smack on zero like this and the next highest, you know, and you've got a fairly good chance that you're going to fall within

**Dave Jones:** that plus minus 0.1% range at least for these Philips resistors. Remember, this may not be the case for some cheap one hung low brand resistors or something like that. So, but your odds of getting a resistor that's, you know, right out here in this

**Dave Jones:** case, for this particular batch, the odds of getting like a 0.8% resistor out here are almost bordering on zero. I'm not going to say it's not possible, but it's very, very unlikely. And getting one right at the 1% limit in

**Dave Jones:** this particular case, well, you know, it's pretty rare. I mean, we had 400 resistors. That's I guess that's not a huge number, but you know, if you maybe if you got 40,000 resistors or or you might see a few that

**Dave Jones:** sort of, you know, poke their head out just just like this one did it, you know, 0.55 out here. Given Ultimately, given enough time, anything is given enough numbers, any probability There's no such thing as a zero probability out

**Dave Jones:** here. They can actually appear, but it's very unlikely. And the other thing to remember with these um uh responses is that they can shift like this. And this will be in in the manufacturing environment, they will actually uh do plots like this, uh you

**Dave Jones:** know, either daily or weekly to track their uh manufacturing and how it's drifting. And you might see the peak actually drift back and forth as you change uh man you know, various uh you know, change materials, you've got suppliers,

**Dave Jones:** you change workers who are operating the machinery perhaps um you know, if it if it requires some sort of manual process or manual intervention or something like that. And you can watch your uh you can watch your processes drift or if your

**Dave Jones:** temperature's changing in your manufacturing environment, that can alter things and all sorts of things. So, you can get really some good insights into manufacturing uh whether components or products or whatever it is you're manufacturing using this frequency analysis. It's a

**Dave Jones:** really good tool. So, I hope you found that interesting. There are a couple of uh surprises in there, but there you go. We got our Gaussian response exactly as we expected. And if you've got more uh data on how they

**Dave Jones:** actually manufacture these things um these days anyway, um then yeah, send us the information. I'll catch you next time.

**Dave Jones:** probability distribut So, just what is the probability distribut probability distribution Planes flying over. Got to stop filming, go figure. Geez, you'd think I'm in the flight path or something instead out here in the suburbs.
