---
video_id: QCCmqosHT-o
title: EEVblog #1068 - Autonomous Uber Incident Update
url: https://www.youtube.com/watch?v=QCCmqosHT-o
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 25, "2": 44, "3": 66, "4": 82, "5": 102, "6": 120, "7": 137, "8": 154, "9": 175, "10": 191, "11": 211, "12": 231, "13": 252, "14": 264, "15": 290, "16": 306, "17": 326, "18": 346, "19": 365, "20": 382, "21": 406, "22": 425, "23": 443, "24": 470, "25": 488, "26": 507, "27": 526, "28": 543, "29": 565, "30": 585, "31": 606, "32": 626, "33": 647, "34": 665, "35": 683, "36": 696}
---

**Dave Jones:** Hi. Just an update on the Uber self-driving autonomous car fatality that I did in a previous video. It's not looking good for Uber, as you could have guessed. All the stories coming out at the moment are that Uber disabled Volvo's SUV safety system before the fatality.

**Dave Jones:** And, well, this is actually not surprising, because they have to install their own autonomous system. That's what they're testing, their own one with their own, what is it, seven cameras, the scanning laser, LIDAR on top, the radar, you know, their own sensor suite of packages that they have to do this.

**Dave Jones:** So they probably didn't want the car's existing collision avoidance systems actually interfering with that. So, yeah, it's not surprising that they did that, but, or what it sounds like, deliberately defeated the collision avoidance system, which, as we'll see, probably could have detected this incident and automatically break the car,

**Dave Jones:** if it was a factory Volvo XC90 that we're looking at here. And the reason that these stories are coming out is because the supplier, Aptiv, of these systems, which uses the Intel Mobileye chipset, which we'll take a look at, has come out and they want to distance themselves from this,

**Dave Jones:** saying that, hey, our system could have detected this and it wasn't used. They actually, they must have disabled this. And actually Intel themselves, which manufacture the chipset, here it is. They actually took the very poor quality dark dashcam footage, so they took the second-hand dashcam footage,

**Dave Jones:** fed it through their Mobileye chipset that's used in the factory XC90, which Uber, as the car Uber use for their autonomous driving cars, and also the car used in this incident, and it was able to detect the pedestrian coming across with their, walking their bicycle across,

**Dave Jones:** a second before it happened. So of course it would have processed that maybe in like a tenth of a second, say 0.1 seconds, it probably would have had almost a second to decelerate. And of course, if that was the case, then they couldn't have probably prevented the accident.

**Dave Jones:** The car couldn't have stopped in time, it wouldn't have had the distance to do that from, what is it, 43 miles an hour or something that the car was actually traveling at. But hey, it would have lessened the impact. And that's from just the second-hand really dark dashcam footage, as we'll see later on in this video.

**Dave Jones:** So they're saying, look, our system would have performed much better if it was a factory Volvo. And it sounds like Uber have deliberately disabled that, so that could get them into a lot of trouble. Anyway, let's have a look at the Volvo XC90, which is, this is the 2017 brochure,

**Dave Jones:** but as we'll see, the technology's been around since like 2013, I think. And it's used in lots of cars. Volvo aren't the only one that have it, the XC90. Lots of cars on the market, even your cheaper ones now, have these collision avoidance detection systems,

**Dave Jones:** not only lane guidance, but detection avoidance as well. Here it is. It's looking out for you, city safety, blah blah blah blah blah. City safety can identify other vehicles, pedestrians, cyclists, and large animals in your path. It warns you of any hazards, and if necessary will brake automatically to help avoid and mitigate collision.

**Dave Jones:** So there you go. It's built into the car. And even like older model cars, it's got exactly the same, you know, 2016 brochure and going back. And if we have a look at Mobileye here, it's now an Intel company. And I've actually done a teardown video of one that was used in a Hyundai.

**Dave Jones:** I'm not sure which Hyundai it is, but it uses the older technology, the Q2 chipset. And you can see the camera here, it's got just a built-in camera with a very high data rate through to the chipset. Because this thing does like, I think the new chipset, the Q3, does 0.25 trillion operations per second.

**Dave Jones:** So it's really amazing, I'll show you in a second what it can do. So this is generally mounted up in the front of the car. I'm not sure of the exact details of the XC90 used in the Uber here, used by Uber here.

**Dave Jones:** But it would have had a similar camera, and they must have disabled this module, which could have detected and automatically braked for pedestrians and things like that. So it's very impressive what this technology can do. So we'll just roll some footage here. And of course, look at the detection tracking of all the pedestrians, cyclists, people walking across, cars in front.

**Dave Jones:** And it can do lanes. Of course, this is daytime, so obviously it's going to perform really well. But you can see how advanced this is, and this is not new. And if we have a look here, you can see that the one that I tore down, the IQ2 chipset, that's actually from 2010.

**Dave Jones:** But the Q3 chipset, dating from 2014, that's used in lots of cars on the market, not only the Volvo, it's got autonomous braking system for pedestrians, it even does animal detection and things like that. Holistic path planning, road lane reconstruction, and all sorts of collision avoidance.

**Dave Jones:** So it's not, and if you actually go and look at some of the videos, they're actually quite old here. Look, four years ago, Volvo collision avoidance systems demonstrating. Here you go, there's Mobileye stuff dating pedestrian collision warning systems dating back to 2012. This is not new technology.

**Dave Jones:** And at nighttime as well, you might think it's just daytime, but here is the Mobileye chipset at night. It can detect all these cars, it can detect the lanes, and everything else. And this is really quite low-light footage. I'm not sure what, you know, camera, if that's the actual camera used in the car or not,

**Dave Jones:** or whether or not that's a secondary and they're just processing it. But, you know, even at nighttime, it's still very impressive. And it's amazing what it can do in crowds here. Just check it out, it's detecting all these people and crossings and all sorts of like, it detects arrows on the road.

**Dave Jones:** It's like practically just built into this Mobileye chipset, which started out as just a lane guidance type warning thing. It's incredibly advanced now with its .25 trillion operations per second. And it can, look, there's a zebra crossing and there's people and it can do most things that an autonomous car can do with just the camera.

**Dave Jones:** It's really amazing. And Volvo made the news back in 2015 in that their system couldn't actually detect kangaroos here in Australia hopping across the road. And it's a huge problem here in Australia, seriously. Like, especially at dawn or dusk, when kangaroos are typically nocturnal animals,

**Dave Jones:** they come out in the twilight and at night and they hop across the road and you can't see them. Anyway, their software wasn't designed to detect the hopping of the kangaroo. It would actually confuse them. They actually came to Australia in their XC90 and they actually, look, updated their software.

**Dave Jones:** You can see it actually detects the kangaroos hopping across the road. And they updated their software to actually, you know, to get this anomaly just here for Australian conditions. So they're really on top of this stuff. And that was back in 2015. So, yeah, anyway, Volvo haven't commented on this yet, probably, for, you know, sensitive legal reasons, I guess.

**Dave Jones:** But yeah, Mobileye, Intel Mobileye and Aptiv, who supply the sensors, have come out and said, yeah, even using the crap dash cam footage, we could have detected that. Now, of course, you saw the footage in the previous video. And warning, I will actually show it again here.

**Dave Jones:** So it does show someone getting hit by this autonomous Uber. But you saw that footage was really dark and it almost appeared as though they come out of the shadows. But of course, that has to do with the type of sensor used, its exposure conditions and contrast and all sorts of, you know, other things.

**Dave Jones:** So there are quite a few people who actually went out and went to the same location where this accident happened at night and actually shot footage of what it's actually like. But this YouTuber here actually shot this footage in 2015. It just happened to be at the exact same location where it happened.

**Dave Jones:** And this was shot with a stereoscopic camera out the top of the sunroof of the car. So let's actually roll that. And you can see the bridge here. This is the bridge that, it's just past this bridge where it happened. And, you know, see my video, previous video for, look.

**Dave Jones:** But like you can see, here's the dark shadow that the pedestrian, and it happened right about here. But you can see that there was still plenty of light there to actually see this. So it shouldn't have been a big problem. And here's somebody who, Strike Engine, Car TV, actually went and shot footage of what it looks like on a mobile phone.

**Dave Jones:** And with the actual footage, and warning, here it is. And the cyclist will come out any second here. And they synced that up. And you can see that even with the crap sensor in what looks like, presumably like a mobile phone, it's really easily able to see that.

**Dave Jones:** So, yeah. The footage provided by that dashcam from Uber is, I don't know, like it's some old technology, I don't know what's going on there. But that is really very dark, that footage. It really is quite remarkable when you saw it, it's like, wow, look how dark that is.

**Dave Jones:** It's amazing. Whereas the actual visibility, and these are time-synced apparently, huge difference. So, yeah. Not sure what's going on there. And here's another one coming up to the bridge. Looks like this was shot with a mobile phone as well, just hand-held. By the looks of it, let's have a look.

**Dave Jones:** And you can see, look, even pedestrians, here's the shadow, it happened right here. So like, there seems to be no shortage of light there. Yes, there is a dark shadow that just happened to be in that spot, but, jeez, if a tiny sensor in a phone can detect that, yeah.

**Dave Jones:** It's not looking great for Uber, is it? So there you have it. Just wanted to share the update on that, and how lots of cars on the market have this system that probably could have detected this just with visual cameras. But the Uber has the scanning laser LiDAR on the top, just spinning around,

**Dave Jones:** update rates, we've had comments on the previous video from people who've worked on those systems, and they actually give the resolution of that LiDAR, and from memory I think they said like 2 or 3 centimeters resolution, or something like that, updating at least 10 times a second, don't quote me on that.

**Dave Jones:** But yeah, it should have been able to detect it, just the LiDAR alone, let alone the radar, and let alone the 7 cameras that they've got on there. Don't know how many are pointed forward, probably at least a couple could have detected it as well, or should have.

**Dave Jones:** So yeah, it ain't looking good for Uber. Anyway, leave your comments and thoughts down below, and I'll link in my tear-down video of that mobile eye sensor, the older technology one, at the end. Check it out. Catch you next time. www.microsoft.com
