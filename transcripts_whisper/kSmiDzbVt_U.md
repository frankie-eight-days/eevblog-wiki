---
video_id: kSmiDzbVt_U
title: EEVblog #216 - Gaussian Resistor Redux
url: https://www.youtube.com/watch?v=kSmiDzbVt_U
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 45, "4": 65, "5": 77, "6": 97, "7": 121, "8": 137, "9": 153, "10": 173, "11": 189, "12": 205, "13": 221, "14": 241, "15": 261, "16": 277, "17": 297, "18": 313, "19": 333, "20": 345, "21": 365, "22": 393, "23": 413, "24": 425, "25": 449, "26": 465, "27": 485, "28": 497, "29": 513, "30": 533, "31": 545, "32": 561, "33": 573, "34": 585, "35": 601, "36": 621, "37": 633, "38": 653, "39": 669, "40": 681, "41": 697, "42": 721, "43": 741, "44": 757, "45": 781, "46": 801, "47": 821, "48": 841, "49": 857, "50": 877, "51": 897, "52": 913, "53": 925, "54": 945, "55": 965, "56": 981, "57": 997, "58": 1009, "59": 1029, "60": 1041, "61": 1053, "62": 1069, "63": 1085, "64": 1109, "65": 1125, "66": 1141, "67": 1153, "68": 1165, "69": 1181, "70": 1201, "71": 1221, "72": 1241, "73": 1257, "74": 1273, "75": 1293, "76": 1313, "77": 1333, "78": 1349, "79": 1365, "80": 1393, "81": 1425, "82": 1445, "83": 1469, "84": 1513, "85": 1533, "86": 1549, "87": 1569, "88": 1581, "89": 1601, "90": 1621, "91": 1641, "92": 1657, "93": 1677, "94": 1693, "95": 1713, "96": 1733, "97": 1753, "98": 1773, "99": 1785, "100": 1805, "101": 1825, "102": 1845, "103": 1865, "104": 1885, "105": 1905, "106": 1929, "107": 1949, "108": 1965, "109": 1989, "110": 2005, "111": 2021, "112": 2041, "113": 2057}
---

**Dave Jones:** Hi. I got an excellent response from the previous blog on the Gaussian resistor distribution and measurement and how you can expect, well, what can you expect from a plus-minus 1% tolerance resistor. And there were quite a lot of people asking me to do

**Dave Jones:** more measurements, to get some, get A, another brand of resistor that, you know, a cheap 100 low brand type, and also 1% metal film, same as last time, but get a different brand instead of a good quality Philips one, what would be the result?

**Dave Jones:** Good question. And also get a 5% carbon film one and see what would happen. And a whole bunch of other things. So, I've done just that. Here we go. I've got a couple of boxes of 1,000 5% carbon film and 1% metal film.

**Dave Jones:** And yes, they are direct from, genuine from the 100 low factory in China. Let's go. And the other thing I thought I'd do is kind of semi-automate, or try and automate as much as possible the process of measuring and logging this data. Because before I just

**Dave Jones:** used some alligator clips and I hooked it up and I read the value off the multimeter, I typed in the spreadsheet, press enter, disconnect, reconnect to the next one, and well, it wasn't that much fun. Now I've got a box of 1,000 resistors.

**Dave Jones:** I'm going to hopefully try and do 1,000 of each type. That's 2,000 resistors. Not going to use these leads. I think I'll spend at least an hour or two just jewelry rigging something. See if I can get something semi-automated. And these are the resistors we're going to be measuring today.

**Dave Jones:** Genuine one hung low. I love it. And here we go. There's 1,000 bandoliered 1% 50 ppm metal film resistors. And we've got, and just to represent their lower quality, plain cardboard case of course, direct from the factory. We've got our 5% tolerance carbon films, 3 band

**Dave Jones:** and they're both 1K of course, exactly the same as before. I thought I'd keep that consistent. So there you go. Let's give these things a go. And of course one of the first ideas that sprung to mind to automate this thing was some sort of feed mechanism

**Dave Jones:** with guide rails top and bottom like this. You know, thin little guide rails that kept them positioned and sliding through some sort of jig like that. And then some sort of probe which either pushed down on top so you would pull it through

**Dave Jones:** one extra resistor. You'd push down the probes onto the top and then you'd move it along and so forth. But the problem with that is that unless you actually go to the trouble to add like-up motors and rollers to actually advance this thing a certain amount, you've got to do it by hand, you've got to do it by

**Dave Jones:** eye anyway. And you've got to, and it's almost a two-step process. If you pull it through and then push it down, something like that, then you've got two hands on that operation. How are you going to push some button to enter the data in if you have to do that or something

**Dave Jones:** like that? And then I had the idea, not of a push-down one but I had a similar idea, maybe using some battery spring terminals or these hangers even. You know, something like that where these sat in some sort of jig. Instead of pushing down

**Dave Jones:** they would, you know, and you would pull it through like that and it would make contact like that but the surface isn't that great and you've got to rely on the tension of the resistor and it can pull out and make it short to the ones next to it.

**Dave Jones:** It was all messy. I didn't really like that approach at all and it just seemed too complicated. So unless I did actually go to the trouble to physically automate the thing with, you know, a hydraulic thing that comes down and motors which advance it and they know the average distance

**Dave Jones:** and it can step it through and stuff like that, it probably wasn't worthwhile. You're probably better off just doing it by hand, especially when you've just got a one-off situation like this. And this is actually quite common in the industry. If you're a beginner or you're studying and you wonder what some of the

**Dave Jones:** common things you do in the industry, well building custom test jigs like this is one of them. You'll find it's very common. I've built countless ones over the years, over the decades to test various things, test concepts, test PCBs and all sorts of stuff.

**Dave Jones:** So building up jigs like this and having to automate them is a skill which you're probably going to need sooner or later in electronics engineering. But anyway, I decided to simplify it and just do a hand-based system. So let's take a look at that.

**Dave Jones:** And this is what we're going to use today. We're going to use what's called a pogo pin. And these are like an industry standard way to build up PCB test jigs and things like that. They're really great. And as you can see, they actually plunge down

**Dave Jones:** like that. So they're also called plungers. So if you search for like a plunger pin or something like that, or a serrated plunger as we've got here, you can see that on the tip of it there is actually all these little serrated, jaggy, sharp points.

**Dave Jones:** And you can get many different types. You can get ones with a single sharp point that are designed to penetrate oxide on a PCB. In this case it's multiple sharp points, which is exactly what we want for going on to a resistor. Test lead, I think.

**Dave Jones:** You can get ones that are concave as well, like they go over test posts and things like that. In this case, the one we've got here is it's from Farnell slash Element 14. There it is. It's a serrated plunger. And they're quite cheap.

**Dave Jones:** $1 each or $2 each. And they're available in many different types, many different widths as well. This is a 1.6mm wide one. So you drill a 1.6mm hole, or a 1.5mm hole in your... whatever you're using as the basis for your testing. Be it a piece of clear acrylic,

**Dave Jones:** or any type of those engineering materials. But what we're going to use today is just this little prototyping board. And hopefully we're going to install these on here so that we can actually get just a nice little hand you know, just a little hand-press

**Dave Jones:** board that allows us to press down onto the pins. Now normally you would drill, you would use this as a board as a template and the pin would, you know, you'd drill out a certain size hole and then you'd put it through like that and you'd glue it in place.

**Dave Jones:** And then you can do all sorts of clamp mechanisms. And I've showed examples of these test PCB test beds before, but in this case we want a hand-based test so that we can just push down with our hand onto the resistor pin. Now the problem with this is that it can, you know, because it's got

**Dave Jones:** those serrated pins on the top there, once it bites down on there, it's pretty good. It's not going to slide off, okay? If you've got one with a single point, of course, that won't work. But these serrated ones work nicely and even if you get it sort of on the edge, it's still going to bite

**Dave Jones:** in there nicely like that. They are actually really very nice. And they do a really good job of biting on to that lead. And because they're very sharp, they've got very sharp serrated jaws on there, then it should bite through the oxide, any oxide on these

**Dave Jones:** resistor leads. And trust me, there is going to be oxide even on brand new resistors. You're still going to get that. So you've got to avoid that. So these, this is probably an ideal plunger slash pogo pin for this application. But unfortunately, it's not big enough.

**Dave Jones:** Ideally I'd want, you know, like a real huge thing. So because this is a line by hand, it's not some automated machine, ideally I'd like a big 5mm diameter one like that. You just go bang! You know, even Stevie Wonder could probe this thing.

**Dave Jones:** But because this has only got a 2mm head on it, it is possible to miss it like that. And, you know, that can be really annoying. It can ruin your day and waste a lot of time. So, what I'm going to do is widen that to a 4mm pogo

**Dave Jones:** pin. I'm going to solder a couple of pins together like this, and then bang! Even if you miss one of them, you're still going to get at least one. And if you get both on there at the same time, of course, then you're going to have both come down.

**Dave Jones:** But I think that's going to work pretty good. And there's a fair good margin for error there when you press that down. So let's try and use two pogo pins each side. Now it just so happens that this board is, I think, a really

**Dave Jones:** quite a nice width for this particular job. So if you put two pins on one end of the board, and then two pins up on the other end of the board, then that's a fairly good distance. You don't want to get right into the resistor

**Dave Jones:** because if you've got the thing laying on the bench like this, you know, there's going to be the resistors, actually, because the body is thicker than the lead. It's, you know, you don't want to probe it right in there like that. You want to probe it out here where it's flat on the bench.

**Dave Jones:** So I think we'll just put two pins on this side and two pins on that side, and it'll be hunky-dory. Now we can't lay them flat, of course, like that. Because if we laid them flat, then obviously they're the wrong orientation. They'd be like that.

**Dave Jones:** We want to flip it 90 degrees like that. So I'm going to tack two together like I've done here, put it on there, strap it down in there, and strap it through those holes, which are nice. If we line it up, say, there, we can strap it through this hole

**Dave Jones:** up here on the top, like that. Strap it through that hole and strap it through the hole on the other side of it, hold it in place, put a buttload of solder on there, and it should hold it really quite firmly. And here's our completed board.

**Dave Jones:** I think it worked out quite well. You see I've put those pins on vertically like that. I've put two straps up here like this on the ends here, and soldered them on the front, and that should be reasonably robust and should last for a fair number of

**Dave Jones:** well, you know, test actuations, I guess. And all I do is hold it like this, it's not bad, hold it in one hand and I can just go press like that. And each resistor I can just go along, bang, bang, bang, bang, like

**Dave Jones:** that. I've got to be careful, of course, not to have my fingers too far down so that they're not touching these terminals here. I could strap that with some tape just to make sure. In fact I probably will strap the whole thing with tape.

**Dave Jones:** And then, bang, bang, bang, bang, bang, I can go along like that! Brilliant! I love it! And here's the completed unit wrapped up in tape. I've got some reasonable length leads on here, about a foot long just for flexibility into 4mm banana plugs

**Dave Jones:** and I can't accidentally touch those pins so there's no question about that. And I rather like that, it works quite well. But let's test the repeatability of it, shall we? So I'm going to probe a resistor here, bang, there we go, 1.0003k and let's wiggle that around, jiggle it like that

**Dave Jones:** probe it again, same resistor, same resistor, right up the top end, bang, bang, only light pressure light amount of pressure, tiny amount of pressure, and it looks like that does a really excellent slide along does a superb job! More than repeatable, very happy with that.

**Dave Jones:** So, part one solved! We've got a semi-automated anyway, way to probe our resistors. Beautiful! Not as efficient as a fully automated one, but it's going to save a hell of a lot of time having to unclip to... unclip and then reclip two alligator clips onto each resistor.

**Dave Jones:** If you've got a thousand resistors or something, that's just crazy, so this should help automate that. The second part of it, we need to automate the actual measurement or, once again, semi-automate this measurement. Now, ideally I'd like to use my HP 3478A which we used last time, because it's the highest precision

**Dave Jones:** highest resolution instrument I've got in the lab here. But, unfortunately, it's only got an old-school GPIB interface there, and well, I don't have any GPIB cards anymore. I've probably got an old ISA card somewhere, but I don't have a computer that has an ISA port anymore.

**Dave Jones:** Crazy! So, we're going to have to ditch the 3478A. Bummer! And we're going to have to use a data logging multimeter. So I thought I'd use the Agilent U 1272A. Now, whether or not we use a handheld multimeter like the U 1272A or the HP 34

**Dave Jones:** 78A bench meter, the process is pretty much the same. You want to connect it up to the PC and you want the PC to automate the measurements. Now, in this case ideally, what I'd want is for every time that I push this down onto the resistor, I would like for the software

**Dave Jones:** to automatically sense that I've probed the resistor, waits for the reading to stabilize, takes the measurement, saves it to the Excel file, and then doesn't take another measurement until I physically disconnect it and it measures it open, and then it starts measuring the next resistor.

**Dave Jones:** And so I don't have to actually press any keys, because the thing that took up all the time last time was pressing the keys. Of course, I'd have to not only hook on the alligator clips, I'd have to read the measurement, type it in, press enter into the Excel spreadsheet, and make sure

**Dave Jones:** I got it right too. So, you know, prone to human error there. But ideally I want the software to just bang, auto-sense that it can do that. Now, I've looked at the software for this, the U 1272A, the Agilent data logging software, and it doesn't seem to have the capability.

**Dave Jones:** I can upload the measurement results from this, I can start data logging measurements and stuff like that with time intervals and triggers, but yeah, it doesn't really do what I want. But, aha! Here's where I don't have to muck around. Oh, sure, okay, I could write my own

**Dave Jones:** software, right? I could, you know, write a little visual basic program or whatever, some script, which talked to the commands and issued them and did all that, but I don't want to waste my time. I just want to take some measurements and plot some data.

**Dave Jones:** So, this thing has got 10,000 sample... 10,000 sample memory built in. So, if you only want to measure 1,000 resistors, not a problem. We can push each one, press the button, bang! Store, store, store, store, like that! So, let's give that a go.

**Dave Jones:** Now the U 1272A actually has three different data logging modes, and we can get into it here by pressing the setup and going into the DLOG or data logging menu like this. Now, we can then select which data logging mode we want. Trig, we can do hand mode, or we can do

**Dave Jones:** auto mode. Now, the hand mode sounds like the one we want. That's basically where you manually push a button to store each measurement. Aha! But, there's always a trap if you read the manual. It tells you that's only got, for some bizarre reason, 100

**Dave Jones:** sample memory, 100 samples in this mode, not the full 10,000. Crazy! I don't know why. It doesn't tell you why. So, if we look at the other modes, auto mode is like an automated time interval. So, it'll take one sample every second, or once per minute,

**Dave Jones:** or once per hour, or something like that. We don't want that. Obviously, we want to store them manually. So, as it turns out, we can go into trigger mode. Now, what this mode is normally used for is you can set it up so

**Dave Jones:** if it goes over or below a certain threshold or something like that, then it will, like if it finds a new min or max, it will store that event in the data memory. But, well, that's no good. But, it also has a mode where

**Dave Jones:** exactly the same as the hand mode, where you can just press the hold button here and it will store it in memory. So, that's the one we want. We'll use that. We'll select that, and we'll go out of there, and we'll try and

**Dave Jones:** sample this into memory. And we'll start data logging by holding down the log button here. And as you can see, it popped up with the first event there. It pops back to the temperature there. I don't know why. I don't know how to get it to stay

**Dave Jones:** exactly on that thing. But as you can see, it's got log written up there. And let's probe our first resistor. Any resistor, doesn't matter. And let's press the trig auto hold button down here, that's pretty stable. And bang! It's, right, we're on trig auto hold mode now.

**Dave Jones:** And if we press it once, bang! We've stored it in, and as you can see, it's automatically jumped to number two. So we get the next resistor here, and we press it again, bang! It automatically unsettles the reading and jumps to number three.

**Dave Jones:** It really is quite nice. And as you can see, if 4, 5, and we can go along and bang! That is really quite neat. We just press a button, probe, press, probe, press, and everything's happy. Now, if we go out of log mode, once we're finished, assuming we've done say a thousand resistors or something

**Dave Jones:** like that, we can go into view mode by holding down view down here. And as you can see, it's got seven events, and we can toggle through those events, bang! That we measured. There we go. The first one was open, I don't know what it did there.

**Dave Jones:** But the second one, bang! Bang! Bang! Bang! Bang! And there you go. And we can upload that data later, once we've done our 500 or 1000 resistors. We can upload that to the PC, save it to an Excel file. Nice! It looks like we've eliminated a fair bit of time, not only

**Dave Jones:** and potential operator error, by typing in the values manually into the spreadsheet. All we've got to do is push a button to store it. And you know what I've discovered? I was going to use this trig hold mode where you have to push the button

**Dave Jones:** but I found that you don't. You can actually use the auto hold mode in log mode. I'll show you. Watch this, okay? Well let's reset it, and this is absolutely brilliant. I won't have to push any buttons. Watch this. Go into log mode, okay?

**Dave Jones:** I'm still up to event 12, but you know, we can start from event 1. And we hold down trig hold mode, and we're in auto hold, not trig hold mode. And if we go in here and we just push it on there, it takes a stable

**Dave Jones:** reading, and then it automatically saw that, it logged it in to the next event. And let's probe the next resistor. Bang! 14! There we go. And take it off, disconnect, 15! It automatically is logging and storing each resistor. I think it's brilliant, but

**Dave Jones:** it seems if you do it too quickly it doesn't do it. Like if I go between that one and that one, it hasn't had time, so I'll leave it off a bit. And there we go, it stores it again. So you've got to be careful that

**Dave Jones:** you are actually logging that event each time, but there you go! This meter's brilliant! It allows us to log these resistors without pushing, automatically, without pushing a single button, without writing any script or software or anything like that. Fantastic! Now what would make this really perfect is if I could get the damn thing

**Dave Jones:** to beep whenever it stored that event in memory. I'm going to have to search through the menus here and see if I can enable some sort of event beep function. And sure enough, Agilent thought of everything! I did have the beep turned off, I went in the setup,

**Dave Jones:** turned it back on, I'm in data logging mode, and watch this! I put it on beep, event 23! And no, I did it too quickly there. That's the only disadvantage to this, is that if you can't do it too quickly, but beep 24!

**Dave Jones:** There it is! I don't even have to watch the meter! All I've got to do is listen for the beep and I know I've captured that resistor! This is just brilliant! It's automation that I've only traditionally seen in software. I love it! And just for a bit of fun, it just so happens

**Dave Jones:** that I have a very high precision 0.01% metal foil resistor, 1k, so I thought we'd hook that up and have a look what absolute value we've got. I've nulled that out, I was getting 1k before, it's slightly different now, it is 0.9999, so there you go, it's pretty spot on.

**Dave Jones:** Okay, it's not a genuine calibration, it's a transfer standard using a factory resistor, but 0.01% of 1k is 0.1 ohms, or the least significant digit there, so our absolute values are going to be pretty close to spot on. One of the other good things about the U1272A

**Dave Jones:** is that it does delta measurement auto-ranging as well. As I said, I nulled that out, so I shorted those particular leads out, and I actually, well, if you do it properly, it nulls it out like that, and there you go, but it keeps that

**Dave Jones:** on the other ranges too, it doesn't manually range, there you go, it auto-ranges up to megohms. Beauty! And of course, before we start, we want to zero this thing out, so let's do it. There we go, I like it, and is it repeatable?

**Dave Jones:** Yep, not a problem. Okay, I'm going to do a quick sanity check here, just to make sure we're getting repeatable values using the auto-hold function, so I'll go 9951, 9956, 9966, now if we go back through and check them again, let's see if we get repeatable results.

**Dave Jones:** 9951, yep, 9956, yep, 60, oh, 66, it's jumped up to 66! There's a 6 differential there. Don't like that at all! That's no good. 7574, yeah, we're within 1, I'm happy if we're within 1, least significant digit here, 75, yep, 659, yep, 61, 59,

**Dave Jones:** 64, yep, okay, so there was only 1 that was out by 6 least significant digits. Let's do that again, number 366, okay, so it looks like it's repeatable again, so I don't know what happened the first time, the first one must have been a bit

**Dave Jones:** out, so let's actually get out of auto-hold mode there, and yeah, that's exactly what it is, 9966, and if we compare them without auto-hold, 51, 56, 66, 75, and wouldn't you know it, I just played back the video to double-check that I actually

**Dave Jones:** wrote them down wrong, and that third one that was 6 digits out, I said 66, but I actually wrote down 60! Bloody humans! ... ... ... ... ... ... Done! And if you're wondering how long that took, there you go, 25 minutes! And that included the answer in the door for the courier guy!

**Dave Jones:** I'm actually rather amazed at this jig, actually, I'm really amazed at the efficiency of this setup. I didn't miss a single reading, I didn't get any double readings or whatever when, you know, if I accidentally touched it twice, it just worked every single time!

**Dave Jones:** Very impressed! 25 minutes for 1000 resistors, that's an average of 1 resistor every 1.5 seconds, and that includes the handle in and everything else! I love it! And if you compare that with using the alligator clips I did last time, that was about 7 or 8 seconds per resistor,

**Dave Jones:** or thereabout, so this little simple jig with the auto-hold function of this meter has gave me a 5-fold increase in testing speed! Beautiful! Now we want to upload the data! I've got the meter connected to the USB port via the USB IR cable, and it

**Dave Jones:** installs the driver, and it's just a COM port, in this case it's a COM14, and we connect to it, and it should show Meter Connected! Bang, there it is down there! And you can change ranges and do all sorts of jazz like that, but we want big event data logging.

**Dave Jones:** It's got manual data logging, auto, and event. But because we use the event mode, we want to load this data in here, and bang! Here it goes! It looks like there's ... here we go! Well, it's going to take a while, and here it is!

**Dave Jones:** Bang! 1,000 loaded! No problems at all! And there's the data table for all of our results, and we can export that to a CVS file, which then we can load into Excel or OpenOffice. Now there's one really annoying thing with this Agilent software,

**Dave Jones:** and that is the value it actually reads in, look, it puts 997.50 space M, so milli, well, you know, okay, whatever. But when it exports that to the CSV file, then when you try and import it, it's not going to import that as a number,

**Dave Jones:** it's going to import that as a text string with that M on the end, and that's going to make it really annoying to actually do that. So you've got to eliminate that M from it somehow. And fortunately you can do that using the space

**Dave Jones:** function, so that it actually eliminated that M and put it in its own column, and then in this column here, you've got the actual data itself. So that's going to work an absolute treat. Bingo! There we go, we've got the data, and we can just kill that column there, and we've got our data in this

**Dave Jones:** column. Okay, I've loaded the data into the same spreadsheet I used in the previous blog, so I won't go through that again. And as you can see, I've plotted all 1,000 resistors on the x-axis here versus their percentage deviation from the nominal 1k

**Dave Jones:** in the center here, plus 1% to minus 1%, and there's two things to note. The first of all is that the spread of the values is around about, you know, that 0.6 value, so it's very similar to that 0.5% sort of variation that we saw

**Dave Jones:** on the Philips brand resistors, so it's a similar sort of tightness in spec. But look at this! It is offset, it's clearly offset, about negative say 0.35 or thereabout on average through the middle of that, offset. There's not a single resistor that is above 1k.

**Dave Jones:** There you go! That's what we found from these one-hung low brand resistors. Whereas the Philips ones in the previous blog you saw were pretty much spot on the nominal 1k and then they deviated either side. But these one-hung low brand ones show a negative offset.

**Dave Jones:** Go figure! And of course there's actually no problem with that because they're still within the nominal plus minus 1% tolerance so they're well within it. So not a problem at all, but the problem might come in if you're relying on the fact that the

**Dave Jones:** nominal manufacturing mean is going to be centered spot on 1k right in the center there, and maybe you parallel 10 resistors up and you expect some to be high and some to be low, and you want them to average out to a better tolerance resistor.

**Dave Jones:** Well, that's not going to be the case. This time they're going to actually average out to a value of around about minus 0.35% from 1k. Something to watch out for. And if we take a look at the probability distribution histogram here, it's a very

**Dave Jones:** similar Gaussian-type response like we got with the Philips resistors. Pretty much exactly as you'd expect. But look, we've got this little outlier one down here at minus 1%. There's a few items right out there that have popped their head out, so that's rather curious.

**Dave Jones:** And of course, here's the center line. You can see that minus 0.3% or so offset. Now, that's for 21 bins. Now, if we go down here and increase the number of bins, you can see that the center here isn't actually a nice, smooth response as you'd

**Dave Jones:** expect. Down at this 0.3%, there's a majority, then they've got another 0.35, and then the next bin up goes up again. So it doesn't really follow that classical bell-shaped curve as much. But you know, you could do other bins, but you do get the bell-shaped

**Dave Jones:** response up here. So you know, it's near enough. But once again, those little outliers at minus 1% have just reared their ugly head. There's nothing in there at all, and there's nothing under, well, on the positive side here. There's absolutely not a thing.

**Dave Jones:** Once again, you can see the offset, so it's rather curious. And naturally, of course, there are a few people in response to the previous episode were mentioning the fact that I didn't mention standard deviation. And I didn't really want to, you know, I don't really want to get into standard deviation and how that

**Dave Jones:** response is pretty much what you'd expect if you get what's called a 6 sigma response for 1%. Especially if it was centered, if you remember the previous blog, then the odds, basically, the sigma response and how many sigma you design for will basically dictate the probability of

**Dave Jones:** getting a resistor or getting a value right out at these limits right out here. And that's probably what well, Philips actually designed for. They may have designed for a 6 sigma response for 1% over that range. But you know, you don't really know unless you're actually the manufacturer to know

**Dave Jones:** what actual system they put in place. They may have been thinking to 3 sigma 0.5% instead of 6 sigma 1%, for example. So anyway, if you want to look up standard deviation and sigmas and how it applies to all this statistics stuff, there's better places to learn that than here.

**Dave Jones:** But there you go, it's a rather interesting response, so we'll try the 5% tolerance carbon film resistors and see if we get a different response. I think we will. Alright, I'm not a happy little camper, I'm trying to upload my 5% resistor data, and I've tried restarting the program,

**Dave Jones:** restarting the meter, the data's definitely in the meter because I can view it in there, but I try and load it up and it just doesn't load anything at all! It's nuts! What's going on? Look, it won't even call up the menu anymore, this is a heap of crap!

**Dave Jones:** I don't know what's happening with this bloody software! It's just locked up! Every time it gets to loading the first data item, it just locks up and then that's it! And you can cancel out of it, then it won't load again. I've tried reinstalling the software and doing all sorts

**Dave Jones:** of stuff, and it just doesn't work! I don't know! What's going on? Unbelievable! The data is in here! Here it is! Look! There it is! 1001 samples. If you go back to the first one, there it is! There's the first sample overload, the next one's 2k,

**Dave Jones:** I don't know what's going on there, but there you go! There's all the data, and it's in there! Why can't I bloody well extract it out of here? There's nothing I hate worse than tools that don't work! So, I've had enough for today!

**Dave Jones:** Damn it! I'll finish editing the video, upload it, sorry but you don't get to see the 5% resistor data! Send your hate mail to bloody Agilent!
