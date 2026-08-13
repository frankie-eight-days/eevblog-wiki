---
video_id: b_eictfFUao
title: EEVblog #774 - Low Battery Discharge Testing Part 1
url: https://www.youtube.com/watch?v=b_eictfFUao
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 61, "4": 81, "5": 93, "6": 109, "7": 121, "8": 137, "9": 153, "10": 169, "11": 189, "12": 205, "13": 221, "14": 237, "15": 253, "16": 265, "17": 281, "18": 301, "19": 321, "20": 333, "21": 349, "22": 369, "23": 389, "24": 405, "25": 421, "26": 433, "27": 449, "28": 465, "29": 481, "30": 497, "31": 513, "32": 529, "33": 549, "34": 565, "35": 577, "36": 593, "37": 609, "38": 625, "39": 641, "40": 661, "41": 673, "42": 689, "43": 705, "44": 721, "45": 733, "46": 757, "47": 773, "48": 793, "49": 813, "50": 829, "51": 845, "52": 857, "53": 873, "54": 889, "55": 905, "56": 925, "57": 945, "58": 961, "59": 977, "60": 989, "61": 1005, "62": 1021, "63": 1033, "64": 1049, "65": 1069, "66": 1077, "67": 1093, "68": 1101, "69": 1117, "70": 1133, "71": 1145, "72": 1165, "73": 1185, "74": 1209, "75": 1229, "76": 1245, "77": 1261, "78": 1277, "79": 1297, "80": 1317, "81": 1333, "82": 1357, "83": 1373, "84": 1389, "85": 1409, "86": 1425, "87": 1441, "88": 1457, "89": 1473, "90": 1485, "91": 1501, "92": 1517, "93": 1533, "94": 1561, "95": 1577, "96": 1601, "97": 1617, "98": 1633, "99": 1649, "100": 1665, "101": 1681, "102": 1693, "103": 1709}
---

**Dave Jones:** Hi! I thought I'd do a video looking at how much energy is left in AA and AAA batteries under 0.8 volts. I mentioned this in a previous live video, because I don't think there's much, if any, real data out there on just that energy under 0.8 volts, because as I've mentioned

**Dave Jones:** many times in many videos over the years, the manufacturer's data sheets, their characteristic discharge curves stop at 0.8 volts. It's like the industry standard cut-off voltage level, where everyone pretty much agrees that there's basically bugger-all energy left in these batteries once they hit 0.8 volts.

**Dave Jones:** And that's true in most cases, of course. But, of course with circuits like the Dual Fief and other really ultra low-power boost converters, there is actually some energy under there, but how much? So the data sheets typically stop at, you know, like 100 milliwatts or something like that, so

**Dave Jones:** I thought, like, what? For really low-power drains is there anything in there? Is there anything usable? And really it's, I know there's something usable for some applications, but how much as a percentage of the total battery at very low discharge levels? You know, things like products that work for a year or something

**Dave Jones:** like that on a set of batteries. Is it worthwhile actually designing your products to go less than 0.8 volts? Down to say 0.5 volts or 0.6 volts is like a typical figure. So I thought we'd take a look at it because it's hard to get data on this sort of stuff.

**Dave Jones:** So this is going to be some really long-term testing, but I just wanted to do this part one, even though we won't get any real results here. We need to do long-term stuff. Just to show you the setup that I'm going to use, and just an

**Dave Jones:** initial overnight test I just did here. I set it up last night and just did a quick test to make sure all my setup's working. I'll show you exactly what I'm doing here, and then I'll get some, I'll start out with some AAA batteries and then I'll get some AA batteries

**Dave Jones:** and only one brand at the moment, Duracell. Maybe I can do more brands and compare them, things like that. But really, I wanted to discharge them at, get multiple characteristic curves that say maybe 100 milliwatts, 50 milliwatts, you know, 10 milliwatts, things like that.

**Dave Jones:** Really low power levels. So I'll show you the setup, we'll have a look. Let's go. Now I started out just wanting to use my BK Precision 8500 electronic load here, and I've done a previous video on this where I've done some discharge testing of lithium polymer

**Dave Jones:** batteries. So click here if you want to see that video. So this actually has a battery test mode built in. You might be able to see battery, well, just under there. And it's got some real crappy software that comes with it. That also does

**Dave Jones:** characteristic discharge curves of batteries, and that's all fantastic. But unfortunately, the battery discharge test mode on this thing only supports constant current. And I wanted to do constant power just to make things easier and you know, maybe a bit more valid for modern products that use DC to DC

**Dave Jones:** converters, for example. So I could have done use the test mode and just used constant current, but yeah, I really wanted a constant power type thing. And this of course does constant power. I can enter in 100 milliwatts, I can go to 1 milliwatts resolution.

**Dave Jones:** I think it's actually 0.1 milliwatts resolution. Not sure if it's actually capable of that, but it at least allows me to enter that. Anyway, still haven't, you know, actually checked the performance verification of this thing right down at the low levels. But anyway, I can set constant power

**Dave Jones:** discharge. So it'll just act as a constant power load all the way down to hopefully 0, which we'll take a look at in today's video. But unfortunately, that stupid software, the only way you can log data out of this thing, it's got an RS-232 port on the back and I've got the

**Dave Jones:** isolated cable for it and everything. The software that comes with it does not allow you to do constant power either data logging or battery discharge testing. It's ridiculous. And then, even if you did, the software is so buggy that it doesn't even allow you to export the data

**Dave Jones:** to an Excel file. It's got that capability, or a CSV file. It's got that capability but it just doesn't work. It's just, rawr! I hate horrible software on bloody, this is an otherwise really good product. But the software is just shit, it really is.

**Dave Jones:** David too, he said, oh yeah, look, I'll just, you know, it should be fairly easy, I'll just write some software for it. So yeah, I said, you know, it's only RS-232 interface, it's probably like a serial command structure, you know, send it a command like, you know,

**Dave Jones:** please read voltage or set constant power mode, all in ASCII text and things like that. And within like five minutes you realize, mwah, nope, it doesn't use regular ASCII you know, text serial commands. It's actually got a 26 byte, I think, or 24 byte packet structure

**Dave Jones:** with checksums and all sorts of commands and it's all in hex and, ah, it's horrible! RS-232 interface, why it can't just use bloody serial strings commands anyway, so we abandon that, and yeah, I've just got my own interface now, using my HP Benchmeter.

**Dave Jones:** Now, because I want to use constant power mode, we can just use this as a constant power load, and the only thing we need to measure is the voltage across the battery, hence why we only need a multimeter to actually log the data.

**Dave Jones:** We don't have to log the current, it doesn't matter, as long as we are confident in this load that it gives constant power all the way down to zero or whatever cut-off voltage we want to use, it'll be zero in this case, then

**Dave Jones:** you know, everything's hunky-dory, we only need to measure the voltage, perfect. And yeah, you could use like a handheld data logging multimeter for example, but often, because this, some of this testing could take a week or more, you know, maybe a thousand hours or something, or things like that, so the actual, if you used a battery-powered

**Dave Jones:** multimeter, it would actually run out of battery before you could actually test this single AAA or AA battery at very low power levels, so of course you use a proper bench multimeter I'm using my very nice 34470A 7.5 digit meter here, which actually has a data

**Dave Jones:** logging mode, so we can actually go in there and set up the interval time and everything like that. Absolutely perfect. Now here's the setup, I've just got a AAA battery holder, I also have one for AA as well now the important thing to do is actually tap the voltage directly off

**Dave Jones:** the pins itself. It doesn't necessarily matter so much at these ridiculously low currents, because these huge beefy wires, at these currents it's not going to drop anything, right? But hey, you do it properly so I've tapped off there and there, I've just got some pins going into these

**Dave Jones:** heavy-duty connections into there. So if you wanted to do, you know, large currents, that'd be really important. So that's all we need to do. And then we can go into here and data log, and then start it, and then start our load here.

**Dave Jones:** Now I've actually got this data overnight I just used like a Fuji battery here, it's just one I had lying around it had already been discharged a little bit, so this isn't a real test I just wanted to test that the whole thing ran overnight and I got the data out

**Dave Jones:** to graph it and everything else, just to test the methodology, so we'll take a look at that in a second. And I've been discharging overnight at 100 milliwatts here, and there is a 100 milliwatt curve in the Duracell datasheet as well, so we can actually

**Dave Jones:** compare that. So if we go out of there we can see that it's doing a weird thing here, it's like jumping up and down in voltage, like this is like fully discharged to zero overnight so it's doing something weird here, so that's most likely like the constant power

**Dave Jones:** mode trying to compensate, and it's sort of like looks like it's oscillating or doing something weird like that. If we actually switch it off, we'll see the voltage in the battery actually start to recover a little bit. Look, so I've actually had that effectively pretty much shorted

**Dave Jones:** overnight with the load anyway, you know, constant power load of 100 milliwatts, and you see it's ramping back up. But of course if we set that to zero, there's no energy. When you remove the load you're not really recovering the energy in the battery.

**Dave Jones:** Yes, the voltage goes back up due to the chemistry, the internal ESR and other complex things that are happening inside the battery, but you're not really recovering any energy. So if you put that load back on that 100 milliwatt load, it's just going to drop instantly right down to zero.

**Dave Jones:** There's just nothing there. But if we set that, if we set the current, for example, of say 10 milliamps .01, okay, so I'll put that in there, and we'll switch on constant current mode, we'll actually see it will be able to deliver some energy, because constant power is a different

**Dave Jones:** thing, it's got to do math and then compensate. Constant current is probably used as a different thing internally. So if we switch that on, you can see that we can actually get, you know, a continuous 10 milliamps out of this still flat battery at .56 volts, and it's going to

**Dave Jones:** drop and drop and drop. We can actually maybe increase that, see if we can get, can we get 50 milliamps out of the thing. But it's very low current, remember that. If you want the power, just multiply it, there we go, it's dropping.

**Dave Jones:** So we can still get 50 milliamps out of it at .4 volts. But it's slowly, there's not much energy left there at all. Wah, it's gone. And of course the BK Precision's still showing that it's actually still delivering 20 milliamps there at, well, you know, no voltage, bugger all.

**Dave Jones:** Oh no, look, it just vanished. So yeah, there's like something really at the low end with this thing, so we need to check that. But anyway, let's go have a look at the data. So what I actually had running overnight here, I had the, I'm using

**Dave Jones:** the data logging mode here. I'm at the sample interval, 60 seconds. So I'm taking one sample every 60 seconds, and that one sample is like just your regular DC volts mode. I've got a fixed 10 volt range here, 10 power line cycles just

**Dave Jones:** to do, that's just standard to do a little bit of averaging to get a reasonably stable reading. And so it's taking one sample every 60 seconds, and you can actually duration I put in, I'm doing number of readings. So I calculated that our 2000 should be plenty.

**Dave Jones:** Because unfortunately, that's the problem with this method using the multimeter. And as opposed to the one with using this allows us to program, if we just use the electronic load, we could program in a cutoff voltage where it would actually stop logging at.

**Dave Jones:** Whereas this one, with just the multimeter, doesn't allow us to do that. So you have to do a little bit of math up front, know what the capacity of your battery is, know how many readings you're going to want, or you can do it in

**Dave Jones:** duration as well. But I decided to just calculate based on sample interval and the number of samples roughly how long I'd need overnight, and then I doubled it or something. I figured I'd need like 1000 samples or something. And there was no delay,

**Dave Jones:** we just started it straight away. And then I logged it to an external USB key on the thing, so into a CSV file, which we can take a look at. So all you need to do to do this thing is to start your

**Dave Jones:** data log in here, just start it, and then turn on your load at whatever power load that you want, and bingo, you just leave it there for a day, a week, however long it takes to discharge the thing. And you've got the CSV data

**Dave Jones:** on this stick. Let's go take a look at it. So please excuse the crudity of this data and graph, I didn't have time to build it to scale or to paint it. Now the CSV export from the Keysight meter is actually quite good.

**Dave Jones:** And there we go, it's very simple. The reading number here, and then all the readings there in voltage. If you didn't fix it to say the 10 volt range for example, it might switch to like exponent mode. So instead of doing 0. 0.08 and things like that,

**Dave Jones:** it would give you e to the minus 2 and stuff like that. So anyway, here's our graph, I just graphed that very quickly. And you can actually see it, look, drop off, like practically brick wall response at that 0.8 volts. Anything actually under 1 volt, you can argue there's not much there.

**Dave Jones:** So we're actually discharging this, remember, at 100 milliwatts. So you know, not a huge amount of power. In fact the Duracell datasheet I mentioned before, it only has a characteristic curve to 250 milliwatts for constant power. The Energizer one does, I'll show you that in a second.

**Dave Jones:** But look, it's just like even below a volt, there's not much left, let alone 0.8. And if we go and actually have a look at the data in here and actually see our individual data points, even though we've got 642 data points, by the time it drops out, look, we've only got

**Dave Jones:** one data point there under 0.8 volts. So that was with that 60 second sample interval which we actually got up here. So you know, really, we actually have to sample a lot more data than that if we wanted increased resolution on this drop off here.

**Dave Jones:** Having one sample per minute just didn't cut the mustard there. So you can actually see there that even if you design your product that drew 100 milliwatts to work down to 0.5 volts, you're so proud of yourself. Oh yeah, it's extracting every last drop of energy in there.

**Dave Jones:** It's only, this is a one minute time interval. You're only going to get maybe an extra minute or two tops out of the thing before it dies. So you went to all that trouble and expense, and you might have had to use a

**Dave Jones:** much more expensive bill of materials cost DC to DC converter, you might have to change your architecture, I don't know, whatever, to work down to 0.5 volts, and you're just wasting your time at 100 millivolt product discharge. Not worth it. And yes, of course I could actually speed

**Dave Jones:** up all this testing by really heavily pre-discharging the battery down to a volt under load, for example, and then just get the fine data right at the end. But there's, technically that's not the best way to do it, and people might complain that

**Dave Jones:** the proper scientific way to do it is, hey, we've got a product it draws a constant 100 milliwatts or whatever over the life of its product by the time you put it in. Let's not talk about the efficiency curves of DC to DC converters and things like that.

**Dave Jones:** As the battery voltage drops, it can change. Anyway, let's assume that a product draws a constant power all the time, which is a product designed with a DC to DC converter already in it. So we want to get some real data, a real characteristic curve of what it looks like, even though

**Dave Jones:** this series of videos I'm going to do, I'm only worried, I'm only interested in this tiny little part under 0.8 volts here. And clearly, for 100 milliwatts, we're getting bugger-all data. And even if we actually did sample it once per second instead of once per 60 second, and we might have been able to get, you know, an extra

**Dave Jones:** half a dozen sample points in there, look at the area. It's just nothing compared to the bulk of the rest of it. It's not even 1%. It's bugger-all. But the idea of these videos is that we can go down to really low powers, you know, 50 milliwatts,

**Dave Jones:** 10 milliwatts, you know, maybe even lower, and see what the characteristic discharge curves look like. In theory, they should be a little bit better than that. They might, like, extend out and drop off more gently for example under 0.8 volts. But hey, that's...

**Dave Jones:** but it may not. It may still drop off like a brick wall. So only one way to find out. Actually do the long-term testing. Now you can actually see the weirdness happening here right at the end of the like after it's fully discharged.

**Dave Jones:** It discharged, sat at 0 for a while, and then maybe due to the battery chemistry, it decided, oh, you know, I'm going to start doing something weird. And then the constant power mode, as you saw before when you could actually see the readings just

**Dave Jones:** jumping around, it's doing some sort of oscillation there, doing something weird right down at that level. So I actually now just want to do a quick test on the 8500 electronic load and see what its performance, its constant power performance is like right down at low voltages.

**Dave Jones:** Let's check it out. So this is a real easy test to do. We get our Rigol power supply here, like a nice precision power supply that can go all the way down to 0 volts. Not all power supplies can, but a good bench laboratory power supply can go down to 0 volts.

**Dave Jones:** And by the way, this isn't like a 0.05% class instrument, so is the Rigol here, and of course the Agilent 7.5 digit meter is the duck's gut. So, you know, no problems with any sorts of precision in our measurement. But, you know, it doesn't matter.

**Dave Jones:** We're looking at the characteristic discharge curve. We could, you know, 1% absolute accuracy in our voltage measurements would be fine. You know, and 1% in our power, for example, would be, you know, 1% power load. It'd be just fine. In fact, I'll check the data sheet on this and we'll

**Dave Jones:** have a look at the data sheet for the electronic load, see how accurate it is in constant power mode. I think it's going to be less than what it is in constant current mode and things like that, because it has to do some math.

**Dave Jones:** So you've got some additional errors introduced there. Anyway, so we've got our, we've got it hooked up here. We remove our battery, of course. You don't want your battery in there. And we just plug the power supply straight in, easy peasy. So we're outputting a

**Dave Jones:** volt at the moment, it's on. So we've got 1 volt, and of course we're measuring a volt on here, but I haven't turned on the load yet. We're also measuring a volt. We don't need this. We can just rely on both of these.

**Dave Jones:** Anyway, so let's go into constant power mode. Our 0.1 watts, our 100 milliwatts, which we were doing before. So we switch that on, okay, and we now draw in, there we go, 100 milliwatts, at least significant digit. Who cares, right? They basically totally agree, okay?

**Dave Jones:** But that's at 1 volt. Now, if we start winding our wick down, hang on, I'll zoom in for this one, just so you can see it a bit better, okay? So if we wind our wick down, I've got my cursor on the second decimal place there,

**Dave Jones:** so it can 0.99, and we can see it drop, okay? Now what we're looking for now is that this stays at a constant 100 milliwatts, okay? Near enough to 100 milliwatts. Once again, we don't care if it's, you know, a few least significant digits out.

**Dave Jones:** And you'll notice that our current is going to increase, because voltage times current equals power. So if our voltage drops, our battery voltage drops, then our current must increase to compensate. And that's one of the disadvantages of DC to DC converters down at low voltage.

**Dave Jones:** As I explained in a previous live video, it's like a snowballing effect the lower the voltage you get. And you'll notice that it's still hanging in there at 100 milliwatts. So we're just testing the ability of this 8500 electronic load here to actually still maintain constant power performance

**Dave Jones:** right down at low voltages. So it's still dropping, and it's still maintaining our 100 milliwatts there. No problems whatsoever. So yep, down at 0.6, still not a problem. At 0.5 volts, which is really what we care about, I guess it's still fine. So yep, this is, load is more than suitable.

**Dave Jones:** But we go down. Alright, no. No, it's still 100 milliwatts. Let's keep going. I won't bore you to death. 0.2 volts. It's still 100, oh there we go, we're getting some error. So down at, let's say, at 0.2 volts here. So yeah. Yep.

**Dave Jones:** Or is that, yeah. Maybe, because we're looking at half an amp. Look, we're trying to draw half an amp at 0.17 volts. That's a lot of current. So you've got to you know, like we might, this is where the drop in these leads could be quite significant.

**Dave Jones:** But it's not. Because look, we're still getting 7, this is where our Agilent meter up here can still help, because we're actually tapping that point there. But these are really thick beefy cables. If they weren't, these were just really thin wires. Half an amp would get

**Dave Jones:** a significant voltage drop across there, and this wouldn't be accurate. As you can see, no problems whatsoever, but we're still, like we're 10% out there. Now here's actually where we get to the limitation of our test setup. Yeah, we might be showing an error here, but that's not actually an error caused by

**Dave Jones:** this load. We're now getting the error caused by the voltage drop here. Because look, multiply 0.15 volts times 0.66 amps, you get basically precisely the 100 milliwatts which we've programmed into the thing. So this load is still doing the business down at 0.15.

**Dave Jones:** Down at 0.1, it's hard to do the resolution of this thing. There we go, exactly 1 amp there. Right? So that's still exactly 100 milliwatts. So this thing is actually still working absolutely perfectly, even though we're getting like 40% error over here. That's due to, even though we're using

**Dave Jones:** huge, big, thick, beefy cables here, these things are monsters. Big binding post terminals, this wire is bloody really thick as well, and these massive binding posts, we're still getting that drop on there because we're at an amp. It's amazing the drop you can get at an amp.

**Dave Jones:** And especially in this sort of situation, it can cause a 40% error. But this sucker still works perfectly fine, so it's no problems whatsoever. So the hiccuping we must be seeing in this thing must be like the battery chemistry causing an effect where, okay, it draws a bit of current,

**Dave Jones:** the voltage drops, it rises back, and this thing is trying to has a software loop in it which calculates the power and then affects the load, which backs off the load a bit, and then the battery rises back up in voltage a bit and then drops back down,

**Dave Jones:** boom, boom, boom, boom. So then it just hits the bottom and this thing just starts bloody well oscillating. Battery oscillation! Beauty. But hey, I'll just check another power mode, I'll do 10 milliwatts now, okay? And just see how good it is in 10 milliwatts.

**Dave Jones:** There we go, we're down at 10, our resolution is right down there, you know, we can get better instruments to measure this more, there's better techniques to measure this more accurately, but yeah, that's good enough. Once again yeah, 10 milliwatts down to 0.24,

**Dave Jones:** 0.21, 0.15 volts, we're still getting our 10 milliwatts, eh, near enough. So I'm happy with that setup, it passes the test, so let's go and measure some real batteries. Sorry I won't be able to give you the data today, this is going to take a long time, we'll have to do

**Dave Jones:** it in part 2, but anyway, I've got myself some brand new Duracell copper top Duralock ones, just got them from the local shopping centre, they're factory fresh. And as you can see, the Duracell one only used constant power down to 250 milliwatts here,

**Dave Jones:** it doesn't have anything better than that. But you know, if we jump over to an equivalent Energizer AAA battery, it does actually have a characteristic curve down 100 milliwatts, which is what I just did overnight on that Fuji battery and yeah, it's a similar sort of hour, you know, 11, 12 hours,

**Dave Jones:** something like that to discharge. So I will do now 100 milliwatts, we'll start that as our baseline, so I'll discharge one overnight I'll get the data tomorrow, then I'll do another one at maybe, I don't know, 50, then another one at 10 and have a look at the data, and then I might do them

**Dave Jones:** in between that or whatever. So yeah, we'll give it a go. So how many data points do we have to do? Well if we go back to our graph that we had before, as I said, like we just didn't have the resolution down here, only had that

**Dave Jones:** single data point. So we want, you know, like, we want better than that. This is once per minute, so let's do it once per second. Okay, let's really go to town. And this took 642 samples at once per minute, so let's just say we had

**Dave Jones:** 1,000 samples because this wasn't a full battery. Let's say we've got a full one, maybe, you know, 1,000 samples should be plenty at once per minute. Well if we want once per second, well, let's set our Agilent meter to say 60,000 samples at once per second.

**Dave Jones:** Alright, so let's do this. We've got the Duracell Coppertop Duralock thing, guaranteed for 10 years in storage and don't leak. Hmm. Yeah, right. Anyway, they were manufactured 10th month 2014, so they're pretty fresh. That's the freshest one I can find at a local supermarket.

**Dave Jones:** So we'll whack that open. So let's whack that in there. And ta-da! 1.60 volts. We've got our power set to 100 milliwatts. Everything's hunky-dory. We're ready to go. And we've got data logging once per second here. 60,000 readings should be plenty. I can

**Dave Jones:** stop it, I don't have to go to 60,000, I can just press stop there, no problems whatsoever. So we can sample interview, data log, everything's fine, I've got my manual 10 volt range, everything's ready to go. Right, here we go. So we want to actually

**Dave Jones:** start our data logging. There we go. 1.601 volts, it's fine. Okay, you want to start it first before you start your load, we can always chop out a couple of samples in our data set, and here we go. Ta-da! Bingo! 1.63, and we'll just leave it running.

**Dave Jones:** And here's where a nice 7.5 digit or 6.5 digit or even 5.5 digit meter comes in handy. You can actually, even at low discharge levels, this is a reasonable, I mean this is 64 milliamps, you know, it's a reasonable amount of discharge, 100 milliwatts, but

**Dave Jones:** even at low levels with a high-resolution multimeter, you can actually see the drop in the reading. So you can just see it slowly counting down there, and if we went down to 10 millivolts, we'd see it be, you know, like 1 tenth of that speed, for example.

**Dave Jones:** So yeah, very handy to have a high-resolution meter like this. So there you go, I hope you found this useful, even though it was just setting up, you know, a test rig like this, there's actually, you know, a lot to it. If you haven't done this before, hopefully that's

**Dave Jones:** some useful info in there for doing battery discharge testing like this. So yeah, I'll leave this running overnight, get the 100 milliwatts, then I'll probably do 50, then I'll do 10, and you know, have a look at the data, analyze it, and then decide if I want to do more or less, and then

**Dave Jones:** of course this is only for the AAAs, I'll also do the AA ones as well, if people want me to do different brands, but there's nothing in it, this is not a brand comparison thing, this is a test to see if there's any useful data under 0.8 volts, and

**Dave Jones:** well, I think we're going to see much. You certainly saw bugger all at 100 milliwatts, it was like, you know, not even 0.1%, it was half a bee's dick. Anyway, I hope you liked that video, if you did, please give it a big

**Dave Jones:** thumbs up, because that always helps a lot. Comments and all that stuff down below, links to everything. If you want the shirt, I'll probably link in. The Teespring store, where I crowdfund, it's sort of like a yeah, it's not really a crowdfund-y thing, but anyway, you can buy the shirt, it'll link

**Dave Jones:** down below somewhere. Catch you next time.
