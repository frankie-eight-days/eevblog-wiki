---
video_id: EYx46kRv2Bw
title: Myenergi Zappi 7kW EV Charger Installation & Testing
url: https://www.youtube.com/watch?v=EYx46kRv2Bw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 26, "2": 45, "3": 61, "4": 80, "5": 95, "6": 115, "7": 134, "8": 151, "9": 175, "10": 193, "11": 212, "12": 237, "13": 260, "14": 280, "15": 296, "16": 317, "17": 332, "18": 344, "19": 366, "20": 376, "21": 394, "22": 414, "23": 433, "24": 449, "25": 470, "26": 489, "27": 508, "28": 527, "29": 545, "30": 562, "31": 578, "32": 593, "33": 605, "34": 626, "35": 645, "36": 661, "37": 682, "38": 706, "39": 725, "40": 743, "41": 762, "42": 778, "43": 792, "44": 809, "45": 830, "46": 847}
---

**Dave Jones:** Hi, I'm in the garage installing the Zappi, MyEnergy Zappi electric car charger. There's my new 32 amp outlet, 6mm copper, I've pulled an Ethernet cable through, so I've got plenty of cores for the current transformer. I'm only going to install one, but I might install a second one later.

**Dave Jones:** I've installed the plugs here. They give you a nice handy little template here, which comes with the cardboard box, which is nice. We're screwing it on. And yeah, look at the leaves everywhere. It's pretty terrible. It's windy today. It's blowing in everything. Anyway, so installing a cable gland.

**Dave Jones:** This is for my 32 amp cable there. I'll install a smaller cable gland for the Ethernet. You've got to drill those. They don't actually come with it. Yeah, and there's my cable. I'll just cut that to length. It's already terminated in there, so cut it to length and she'll be right.

**Dave Jones:** No wuckers. It's a real pain in the arse pulling the Ethernet cable through the roof, though. Probably should have gone for that wireless solution, but she'll be better in the end, I think. There you go. That's some nice looking cable glands ready to go.

**Dave Jones:** And so I'll just hook those up now. I haven't hooked up the sensor to the other end yet, but yeah, I'll feed that into one of the pairs of the Ethernet. It's got to be a twisted pair all the way, of course, to get rid of all your common mode noise.

**Dave Jones:** Well, there you go. That ain't coming off anytime soon, I can assure you. The brickwork wasn't exactly flat, so it did rock until I screwed it in. Three screws there if you want. It does have a two center ones down here. If you want it like you have to install it on like a beam or something like that,

**Dave Jones:** then you can do that. Otherwise, you install it three like that. So all I've got to do now is cut that cable to length. Just leave a bit of hang on there and terminate the Ethernet cable and terminate that through and then attach my current sensor and Bob's your uncle.

**Dave Jones:** All right, let's fire it up for the first time. I've checked my earth. I've double-checked my mains connections. So let's give it a go. I haven't actually tested this PowerPoint yet, so I assume it's fine, but let's switch it on. Here we go.

**Dave Jones:** Ta-da! Verifying firmware. My energy's happy. Someone said that's the theme from Final Fantasy or something. Anyway, current transformer's not hooked up yet and it's not programmed and the EV is disconnected. But yeah, didn't blow up. That's a start. Check this out. I just discovered it's actually got a knock sensor on it,

**Dave Jones:** which actually also works with this. You don't need an electrical connection in there like a micro switch or anything like that. It just detects the physical thing on the case. So that's very nice. Anyway, I better set it up first before I do charging, I guess.

**Dave Jones:** All right, I've set up some basic stuff. Probably not complete, but good enough for Australia. So I'm going to do my first charge. It's got a five meter cable. So let's go over here. Let's plug her in and see if she detects. Yep, I heard the car do the lock.

**Dave Jones:** So it's locked. And I heard it over here. Yeah, we've got green. Oh, charging, charging. 5.5, 6.7 kilowatts. Oh, installation limit. Okay. Yeah. All right. I haven't set it up properly. Something's wrong, but you saw it. It was charging. Yeah. All right. How do we stop?

**Dave Jones:** Stop. Boost not available. No. Stopped. There we go. Okay. Well, it did charge for a second anyway. Okay. I upped my grid limit up. Yeah, up my grid limit there. 7.2 kilowatts. I'm successfully charging at 7.2 kilowatts. If I go inside, there it is.

**Dave Jones:** 7.2 kilowatts. Winner, winner, chicken dinner. You still got to play around with the settings, though. But yeah, it does work. All right. The last step is to install the current clamp. You notice there's the arrow going that way. This is feeding into the house.

**Dave Jones:** So this is my grid feed here. So there you go. I've got that connected. I spliced it into my Ethernet cable, which is a 30. In fact, the whole run is 35 meters. So yeah, that's a long way, but let's see if it works.

**Dave Jones:** And sure enough, winner, winner, chicken dinner. There it is. 4.3 kilowatts. It's jumping down. It's very shady. It just comes in and out at the moment. So I like how the size of the arrow there seems to grow based on the amount of power going out, I think.

**Dave Jones:** Look, it's going to get bigger as the sun is going to come out. Yeah, yeah, there we go. Yeah, it's actually growing in size. Check it out. That's pretty cool. OK, it's now saying surplus there. So it's got all these different messages depending on.

**Dave Jones:** So we have surplus solar there and it just switched into charging mode. RCD, it just checks the RCD every time. But there you go. I just want to. Yeah. What I want to do is check that. No, five kilowatts. Oh, yeah. So there you go.

**Dave Jones:** It just dropped. So we're now import. We're importing a little bit exporting. It's going to jump around a little bit. Yeah, but it's basically charging at the lower rate. So I mean, the eco plus plus mode now. So this will now change that charge rate depending upon how much excess solar.

**Dave Jones:** So as soon as the shade comes over, I'm not sure of the sample rate, you know, once a second or something like that. It seems to be it would be every update right there. So, yeah, once per second or something. It would. So it's shaded now.

**Dave Jones:** The sun, the shade just came over. So it's dropping. Yep. So it's working. That's eco plus plus mode. So it's that's doing its job. So that PWM should be changing. So if I actually go in there. So if we go into readings there.

**Dave Jones:** Pilot PWM. There it is. Twelve percent. Fifty. It's normally at 50 percent. But there you go. It's dropping. I set a minimum of 10 percent. So that's the minimum it's going to charge at. So it looks like it will actually draw from the grid as an absolute minimum.

**Dave Jones:** If. Yeah, because you can only go down to 10 percent. I don't know why that. Yeah, look, yeah, we're importing a little bit from the grid. So it looks like it's not absolutely perfect. I don't think you can't absolutely guarantee that every electron is going to come excess from the solar.

**Dave Jones:** I don't know why that minimum is there. That minimum PWM. But anyway, that's that's pretty cool. So one point two kilowatts. But unfortunately, it's shaded one point three. There you go. So that's pretty close. And that will it's just coming in and out.

**Dave Jones:** I guess it's I guess perfect and annoying at the same time for this test today. But there you go. That's the there you go. Two point seven, two point six. So there you go. It does. It works with the the zappy works with the ionic in that it it changes the PWM and the ionic response reads that PWM signal.

**Dave Jones:** It looks like in real time, like every second samples at once per second and then adjust the charging rate. Cool, huh? So there you go. I'm very happy with that. That worked an absolute treat works as advertised. Yes, I will install a second current sensor to actually get the production value as well.

**Dave Jones:** Presumably that will show up on the display there because I've installed that four pair Ethernet cable. And yeah, it goes the full 20. It goes, I think, yeah, no, 35 meters, 35 meters of cable that works over. No problems whatsoever. But as I said, you've got to use a twisted pair for that.

**Dave Jones:** And Eco++ mode works as advertised, but if I wanted to, I can override that. I can fast charge that. Is that going to update straight away or do we have to boost? Boost not available. But there you go. It's going now. It's now going at the full seven kilowatts.

**Dave Jones:** If you go, oh, bugger it. I really need to go out. You put in fast mode. That's great. That works a treat. And you don't have to look at the numbers, by the way. You can just look at the LED here. And when it's green like this, that means all of the charging power is coming from your solar.

**Dave Jones:** And so if it goes orange, it means that it's coming, you know, it's doing both or something. Anyway, you can read the manual for that. But yeah, that's really cool. And after you're finished here, it tells you what percentage was used with solar power.

**Dave Jones:** There's 62 percent because I was actually running the fast charge of the hair for most of the majority of the time there. But there you go. Very cool. So at the moment in full sun, you can see that there's zero to or from the grid,

**Dave Jones:** which is exactly what you want because all of the solar is going into the car minus what the house is using. So, yeah, if I get another current clamp on there, which is easy to add, I'll be able to get that figure coming from there.

**Dave Jones:** But I can get that figure coming from my other monitoring systems. It's just not conveniently on the screen here. But yeah, that works well. We're taking nothing from the grid and we're exporting nothing from the grid. All my excess solar at the moment is going into the car.

**Dave Jones:** And if that shade comes over, it'll drop. And, you know, you might see some fluctuations there as it, you know, one second sampling difference and stuff. Well, sampling difference and stuff like that. But yeah, that's that's working well. Very impressed. And you get a total kilowatt hours there that's going in.

**Dave Jones:** So we are going to see some residual offset here just as like the shade comes in and out. It takes X amount of time for the car to respond to the chain. Well, X amount of time for this to respond to the measurement, change the PWM, and then the car's got to change its charge rate.

**Dave Jones:** Here we go. Yeah, 0.4 because the sun's just coming in and out. And yeah, so the car's got to respond. It's a whole, you know, very slow loop on this thing. But yeah, like if the sun's just out and it's not coming in and out, in and out, in and out,

**Dave Jones:** then it does settle down very quickly to zero net import energy there. Right, I just completed a couple of hours long cycle purely on Eco+. So let's actually stop this now and see what I've put in total of 8.19 kilowatt hours. It's supposed to tell us the percentage.

**Dave Jones:** Hang on, I'll unplug it. There we go. When you unplug it, you get, so they have a 97% Eco, so from the sun. So it basically, it followed it almost perfectly, even when the shade was coming in and out. Of course, if you've got perfect sun with no shade, you'll probably get 99 or 100%.

**Dave Jones:** The fact that shade came in and out, it actually stopped and restarted charge a couple of times. Yeah, that's, it's very impressive. So I like it. Check this out. This is really fascinating. This is the live output from my solar analytics monitoring system as I was charging.

**Dave Jones:** And the yellow curve here is the solar produced total from both of my independent systems. And the purple one is the consumption of both the EV and the house as well. And you can see how perfectly it matches like this. It's absolutely amazing.

**Dave Jones:** It only deviates incredibly slightly for like brief periods here, as I said, as part of like the loop of like the car has to respond and then the zappy has to respond and so forth. But that's absolutely incredible. Until it got to about 1.2 kilowatts or thereabouts,

**Dave Jones:** I think around about 5 amps or something like that, which equates to about 5 amps at 240 volts, something like that. And then you can see that the car actually stopped charging. It won't go under that. The car will actually switch off charging.

**Dave Jones:** But the solar, of course, continues to actually produce there. And you can see that I've actually captured it again. Extending that, you can see how the purple one here, this is the base consumption of the house. So the car is actually drawing nothing there.

**Dave Jones:** So the house is drawing a few hundred watts or something like that, just the fridges and whatnot. And then once it reached like about 1.2 kilowatts or so again, something around that area anyway, then it starts. The car automatically starts charging back up again and it matches it perfectly.

**Dave Jones:** It's brilliant. So and the zappy during this period was showing up waiting for supply or whatever. So it didn't have enough supply to turn on the car. But yeah, that's great. So there you go. I'm very happy with that install. That was pretty easy and it works fantastically.

**Dave Jones:** And I have had it on for a little bit before and I couldn't feel any of the six millimetre cables warming up or anything like that. But I will do another video where I get my thermal camera, go in the roof and check out the six square millimetre copper here at the full charge rate.

**Dave Jones:** But yeah, very happy. Catch you next time.
