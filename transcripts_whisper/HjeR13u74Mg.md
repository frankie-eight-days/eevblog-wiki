---
video_id: HjeR13u74Mg
title: EEVblog #1066 - Uber Autonomous Car Accident - LIDAR Failed?
url: https://www.youtube.com/watch?v=HjeR13u74Mg
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 21, "2": 38, "3": 56, "4": 67, "5": 84, "6": 107, "7": 124, "8": 141, "9": 159, "10": 175, "11": 187, "12": 205, "13": 226, "14": 240, "15": 258, "16": 276, "17": 301, "18": 316, "19": 337, "20": 357, "21": 381, "22": 393, "23": 412, "24": 429, "25": 453, "26": 470, "27": 489, "28": 502, "29": 523, "30": 538, "31": 554, "32": 572, "33": 581, "34": 597, "35": 608, "36": 640, "37": 651, "38": 669, "39": 681, "40": 703, "41": 727, "42": 749, "43": 769, "44": 786, "45": 803, "46": 815, "47": 836, "48": 856, "49": 877, "50": 896}
---

**Dave Jones:** Hi, I wanted to talk about this recent incident with a fatality, the first fatality involving an autonomous car. In this case it's an autonomous Uber car in Tempe, Arizona in the U.S., and unfortunately there was a fatality. Someone was crossing the road and they got hit by this

**Dave Jones:** autonomous Uber car. There was a driver behind the wheel, but they weren't in control of the car at the time. It was in fully autonomous mode apparently, and it's the first accident of its kind, and it could have wide-reaching ramifications for, well, at least the near-term future of

**Dave Jones:** autonomous cars. So I thought it's important to have a look at it and talk about it, and the Tempe police have just released the footage from inside the car of the accident. They just released it like an hour ago, which really raises an interesting point, because before this

**Dave Jones:** it was just all speculation about, well, did the person just dash out in front or whatever? Could the autonomous car, should it have detected this and avoided it? And I'll show the footage shortly, but let's have a look at the original news report from this, shall we?

**Dave Jones:** ABC 15, big questions about this early morning crash in Tempe. A bicyclist seriously hurt in a crash with a self-driving Uber vehicle on Mill Avenue near Curry. We don't know right now whether there was a human driver at the controls at the time of the crash or not.

**Dave Jones:** We also don't know the condition of the bicyclist. It appears the injuries are serious. Tempe PD just letting us know that Mill Avenue has reopened. This is just north of Tempe Town Lane. Now unfortunately, as I said, the pedestrian did actually die in this incident, and there's a huge investigation into this, so I'm sure that,

**Dave Jones:** you know, the full details will eventually come out. But it was very interesting that very soon after the incident, the Tempe Police Chief came out and says an early probe shows there were no, there was actually no fault by Uber. From viewing the videos, it is very clear

**Dave Jones:** it would have been difficult to avoid this collision in any kind of mode, autonomous or human driven, based on how she came from the shadows right into the roadway, Moore, who's the Police Chief, said. They have not released the video, but now they have just an hour ago, and we're able to

**Dave Jones:** take a look at this to see how bad it is. Now of course, autonomous cars, they shouldn't just have visual-based systems, because as they said, if they come out of the shadows, you can't see them. This is very typical of pedestrian and other, you know, animal accidents and things like that.

**Dave Jones:** When you're driving at night, they jump out of the shadows and slam. You know, you don't have time to see them coming or to stop. But of course, autonomous cars are expected to be better than this. They're expected to have, you know, LIDAR-based radar type systems that are supposed to, you know,

**Dave Jones:** ping out in front of the car or in all directions, essentially, and know where objects and other things are. They shouldn't just rely on visual aids. And here's the actual Volvo we're talking about, the Uber one here with their, this is Uber's own driverless package.

**Dave Jones:** It's not actually a Volvo thing. It's got a top-mounted LIDAR unit, provides 360-degree, three-dimensional scan of the environment. So that's actually a rotating laser that spins around, and then they receive the data from that. They can build up a LIDAR map image of that.

**Dave Jones:** A forward-facing camera way to focus on both close and far field, watching for braking vehicles, crossing pedestrians, traffic lights, and signage. So, like, the problem with just, if you just designed an autonomous car that used optical, like camera-only based systems, they're just not as good as the eye.

**Dave Jones:** There's a lot of stuff that goes into the technicalities of this, but generally the dynamic range of the eye is better. It's much better up at picking, you know, low light, you know, little glints and movements and other stuff than especially a video camera-based system.

**Dave Jones:** But of course it needs, that's why this Uber car has all these other sensor packages as well, like this 360-degree radar coverage. So not only LIDAR, but radar as well. Where those sensors are, I don't know, but they're kind of showing them on the front here.

**Dave Jones:** A roof-mounted GPS, of course, side and rear faces and cameras working in collaboration to construct a continuous view of the vehicles surrounding. So it's seven cameras, one laser, inertial measurement units, custom compute and data store, 360-degree radar coverage. Something obviously went wrong there with the algorithm or whatever.

**Dave Jones:** This stuff has more than enough technical capability to see somebody pushing a bike in front of the car. Unfortunately something went wrong. Now from the news footage I've been able to determine the exact location where this happened. It was just over the Tempe Town Lake here, just past this overhead

**Dave Jones:** bridge, right about here on North Mill Avenue, just before East Currie, the intersection with East Currie Road here. And if we actually go in and have a look at the street view down here, we can see as you'll see in the footage very shortly, there's a lamppost right here.

**Dave Jones:** This lamppost here provides the light coming across where the pedestrian comes out of the shadow here. So the impact happened like just right about here, and the bike ended up some way up here, just past this blue sign here with the palm trees, as you'll be able to see in that news footage before.

**Dave Jones:** So the bike ended up here, the impact was down there. And what's actually sad about this is this is actually a bike lane going along here, there you go, and further up here the person could have actually crossed up at the lights up here.

**Dave Jones:** It is a long way, but hey, look, let's not put blame on anyone for crossing anywhere or doing whatever. We're just talking about the technicalities of the, should the self-driving car have actually detected the person crossing across like this. In this case with their bike going across the road, but with the lasers and the lidar and the radar and everything

**Dave Jones:** else, along with the 20 cameras on the car, should it have been able to detect such a simple thing as something coming across in front. First let's take a look at Uber's self-driving car. The one involved in the accident and the modern ones that they're using are a Volvo XC90, I believe.

**Dave Jones:** They started out using a Ford Focus test cars like this, but have a look here. The cars themselves were packed with around 20 cameras, seven lasers, GPS, radar and lidar technology that measures the distance reached by outgoing lasers so cars can see and interpret the action around them.

**Dave Jones:** So it's got all the bells and whistles, it's got everything that should be required to detect somebody walking in front, even if they're coming out of the shadows as the police chief said, and as we'll see in the video, this is certainly the case.

**Dave Jones:** A human probably would not have been able to avoid this accident, I suspect, based on the footage which you'll see shortly, but it certainly had everything there that should have done the business. So, and it was, the car has been determined it was in full autonomous mode at the time, so it looks like, based on this,

**Dave Jones:** it, with all that technology, something went wrong, unfortunately. And it should be noted that the one in the actual accident, look, it's got the scanning, it looks like that's probably the scanning laser on top, plus the cameras and everything else, so it's got that full car width

**Dave Jones:** sensor package actually going across there. So it looks a bit more streamlined than, you know, it's just like the package on the front. So it's obviously like a newer one than the full-on one that they actually had in these early prototypes, so they seem to have improved that, but it should

**Dave Jones:** have the full sensor suite in there. Now I'm going to point out this interesting article that I found, and I will link it in down below. It is a year old, from March 24, 2017, and it's from Recode. Inside Uber's self-driving car mess.

**Dave Jones:** Apparently, I won't go through the whole thing, but of course Uber's future pretty much depends on self-driving cars, because they're not doing very well financially. They know the future self-driving cars, and if they can get the drivers out of the loop and have a fully autonomous service, it's going to probably have a much

**Dave Jones:** better return for them. So they're betting big time on autonomous cars, as they probably should. No one blames them for that, but anyway, apparently like a year ago, granted this was a year ago they've had, they said here that the company's autonomous efforts are in turmoil

**Dave Jones:** according to exclusive interviews they had with current and former and current employees of their self-driving unit, which they got. They bought a truck, self-driving truck company called Otto, and that's where a good lot of the talent came from. But turmoil, internal tension among its

**Dave Jones:** executive leadership, granted this was a year ago, issues a wave of key talent departures and problematic demos. At least 20 of the company's engineers have quit since November. That would have been 2016 at the time. Anyway, I'll link it in down below, and you can read it for yourself

**Dave Jones:** and make up your own mind in terms of that. But yeah, it wasn't looking good back then, their autonomous car division. They did have issues. So here we go, let's take a look at the footage. The Tempe Police Department have just released this.

**Dave Jones:** It is public, and I have actually taken this footage. It's done as two separate footages, one from the dash cam looking, presumably the dash cam looking forward, or is it the cameras, one of the cameras up on the top? I'm not sure, but anyway

**Dave Jones:** it's looking forward out of the car, and there's the other one looking back in at the driver as well. And what I've done is actually taken this footage, I've inlaid the driver with the front forward looking dash cam footage. I've tried to line them up as much as possible.

**Dave Jones:** The police chief said that actually the first time the driver knew about it was when the impact actually happened. So that's when I've synced it up. So, warning, some viewers may find the footage disturbing. So as you can clearly see here, basically the pedestrian walking their bike

**Dave Jones:** going across the road did actually come out of the shadows there. And granted this is a very common way that accidents happen at night, pedestrian animal accidents and things like that, especially here in Australia. You know, kangaroo jumps across the road, they come out of the

**Dave Jones:** shadows, there's almost no way to see them and respond in time. So even if there was a driver like behind the wheel, actually they may not have been able to prevent this accident. Unfortunately, but that's not what we're discussing here. It's like, should this autonomous car have actually

**Dave Jones:** detected this with all its sensors? And really looking at this footage, I've got to say, I mean, this is a classic case. It wasn't just a person, it was a person with a bike. So you know, it was like, that's a pretty big target to miss, I would say.

**Dave Jones:** So you've got to, I guess, question, and once again, not necessarily putting blame on Uber here or their technology, but let's look at this. A person was walking straight across. Autonomous cars, as I said, I think we expect better from these because of all the sensor fusion technology.

**Dave Jones:** The lasers, the LIDAR, the radar, and the 20 cameras on this thing. Granted, I don't think the cameras could have actually picked up that, but I can't see how the LIDAR or other systems should not have picked this up. So do they have an issue with their sensor fusion technology and stuff like that?

**Dave Jones:** Granted, these are still essentially prototypes that they got out there driving around on these roads. So like, I don't think the driver could have actually seen the pedestrian coming out of the shadows here. So yeah, I can't see how you can necessarily blame the driver in this case,

**Dave Jones:** but as you can see, he was actually distracted, probably maybe looking at a mobile phone or something like that. But in this case, the sensors really should have picked that up, I think. So that's like a classic case of something walking in front of a car, and that's a reasonably big

**Dave Jones:** target. So anyway, there you go. That's the footage. Let me know what you think. Should this Uber self-driving car have picked this up? Do you know about all this sensor fusion technology? Have you got any further technical details on exactly how the Uber

**Dave Jones:** system works and actually fuses all these different sensors together? Does it process them separately? Does it do fuse them together and then do it based on the final output of that? Please leave it in the comments, and as always, EVblogforum down below. But if you want my opinion

**Dave Jones:** on these self-driving cars, and a lot of people have asked, and we've discussed it on the Amp Hour a few times, all the talk in the last couple of years is fully autonomous cars are only a couple of years away. Like that's what everyone was saying.

**Dave Jones:** And even before this accident, I was saying no way that they aren't even close to being able to do what humans can do. Yes, in limited circumstances, geo-fenced areas with fully mapped modes, but I can't see how the technology at this stage can detect stuff that humans can detect.

**Dave Jones:** Just basic stuff, you know, like a big city like Sydney, different work zones and contra flows and, you know, lollipop people will stand there, stop, go, and like all that. Like let alone navigating car parks and navigating, you know, things like that, looking for parking spots and stuff like that.

**Dave Jones:** You know, can the cameras see other human faces over there and see them walking towards their car? They're walking towards their car, looks like they're going to leave, you know, I can wait for a spot there and things like that. Like there's countless different scenarios I can think of and ones I can't think of, that if

**Dave Jones:** you've got them, put them in down below, where current autonomous technology, no matter how good it is, is not going to be able to replace humans anytime soon, except in specific, you know, narrow sort of circumstances. So it's a very interesting question, this autonomous car thing.

**Dave Jones:** It's going to happen, but I don't think it's going to happen on as large a scale and as soon as people think. Comments down below. Catch you next time. Bye.
