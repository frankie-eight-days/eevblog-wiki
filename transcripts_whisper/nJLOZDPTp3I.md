---
video_id: nJLOZDPTp3I
title: EEVblog #896 - Space Electronics
url: https://www.youtube.com/watch?v=nJLOZDPTp3I
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 47, "3": 72, "4": 86, "5": 105, "6": 120, "7": 138, "8": 156, "9": 182, "10": 201, "11": 217, "12": 232, "13": 245, "14": 268, "15": 285, "16": 299, "17": 313, "18": 332, "19": 347, "20": 361, "21": 374, "22": 399, "23": 416, "24": 439, "25": 463, "26": 482, "27": 495, "28": 514, "29": 537, "30": 562, "31": 584, "32": 603, "33": 623, "34": 640, "35": 654, "36": 671, "37": 686, "38": 703, "39": 718, "40": 730, "41": 743, "42": 759, "43": 773, "44": 788, "45": 806, "46": 821, "47": 844, "48": 860, "49": 876, "50": 894, "51": 906, "52": 927, "53": 945, "54": 962, "55": 976, "56": 994, "57": 1014, "58": 1035, "59": 1049, "60": 1065, "61": 1082, "62": 1098, "63": 1115, "64": 1130, "65": 1145, "66": 1157, "67": 1172, "68": 1189, "69": 1203, "70": 1218, "71": 1235, "72": 1252, "73": 1267, "74": 1285, "75": 1297, "76": 1310, "77": 1325, "78": 1341, "79": 1360, "80": 1372, "81": 1390, "82": 1406, "83": 1421, "84": 1434, "85": 1449, "86": 1464, "87": 1476, "88": 1490, "89": 1506, "90": 1520, "91": 1537, "92": 1552, "93": 1567, "94": 1582, "95": 1601, "96": 1616, "97": 1633, "98": 1651, "99": 1672, "100": 1686, "101": 1702, "102": 1719, "103": 1735, "104": 1749, "105": 1766, "106": 1779, "107": 1795, "108": 1808, "109": 1825, "110": 1841, "111": 1855, "112": 1871, "113": 1885, "114": 1902, "115": 1923, "116": 1938, "117": 1953, "118": 1970, "119": 1986, "120": 2001, "121": 2018, "122": 2039, "123": 2056, "124": 2072, "125": 2089, "126": 2108, "127": 2131, "128": 2151, "129": 2175, "130": 2202, "131": 2227, "132": 2256, "133": 2282, "134": 2304, "135": 2322, "136": 2366, "137": 2411, "138": 2456, "139": 2492, "140": 2522}
---

**Dave Jones:** Hi, I'm here with Carsten yet again and we've got the Audi Quattro Lunar Rover and we're going to talk electronics. Yeah. Excellent, because you are the Senior Electronics, you're the Head of Electronics Development for the whole project. Yeah, exactly. So I've been doing the electronics for the Rover for quite a while now.

**Dave Jones:** Got it. But you've also been involved in lots of the mechanical stuff as well. Yes. We're pretty general, aren't we, us electronics guys? Yeah, yeah, yeah. Awesome. All right, what's the processor? Oh. Everyone's going to ask, what processor's driving this thing? Yeah, so the interesting thing is in the beginning we had like a central FPGA, like it was a Vortex 5, it was a power PC on it.

**Dave Jones:** And then we ran into some problems because if you have a central processor and then we had also central motor drivers, which meant that we were driving high currents over long distances and this led to some problems. And so with the new Audi Lunar Quattro, we actually decided to go away from this concept and we developed a more like distributed system.

**Dave Jones:** So this is, what you can see here, in this unit there's a motor and there's the electronics actually sitting on top of it. Yep, which we'll take a look at, we'll get a shot later. Yep. That's probably the only thing we can tear down at the moment, sorry.

**Dave Jones:** But yeah, okay, so you've got the drive electronics in here. Yep. And you were saying each wheel can operate autonomously? Exactly. Right, okay. So there is a processor in each of those. Yep. Which processor? It's an Atmel. It's an Atmel what? It's an 80 mega something.

**Dave Jones:** For all you Atmel fanboys, are you scared about the new microchip buyout? No. Microchip buying them, no, they're still going to pay. So there's a radiation section going on at Atmel, which is pretty strong. Right, okay. And so we can take one of those.

**Dave Jones:** Okay, cool. So they will be able to supply your parts, the radiation hardened parts and everything. Can you order any of their parts to order as radiation hardened? No, no, no. So the thing is that, well, radiation is very interesting. We'll talk about that in a separate video.

**Dave Jones:** It's not like stuff doesn't work magically and it's not like you don't need to have a certificate to be able to run it. But there is some gradually differences between them. Got it. And right, so we've got a processor in each wheel and there's one main processor in the thing.

**Dave Jones:** Is that it? Which one's that? So there's a Smart Fusion 2, which is an FPGA with a Cortex M3. Yep. And there's also the on-board computing unit, which is, oh wait, this is on a Lander. Sorry. Right. So in the Lander we have another computer, which is taking all the control of the spacecraft, which is more suited for the radiation environment.

**Dave Jones:** In terms of the mission. Once the Lander lands on the moon, it's done, its job's done and it just dies and the rover takes over. Yep. Got it. Right. So the Lander, it has its own power source? Yeah. It's not solar powered? No, no, it's solar powered.

**Dave Jones:** Oh, it's still solar powered. Everything's still solar. Everything's still solar? Yeah. Right. In space it's used this way together. I was asking about those radio heaters. Right. It gets trickier with the paperwork. Thermoelectric generators. Thermoelectric power generators is the correct term. I'm going to get there eventually.

**Dave Jones:** And, right, so too much paperwork. So it was funny. I was at a conference and opposite was the guy that is responsible for the new radioisotope generators. Yep. I asked him how much paperwork it would be for us to launch it and he said like, oh, that's a very good question.

**Dave Jones:** You should write me an email. But I'm afraid I don't want to go on the blacklist anyway, so I didn't bother. But he said that it would be an order of 20 to 30 million on paperwork to get it launched on a rocket.

**Dave Jones:** Wow. Really? Yeah. 20 or 30 million just to ensure that it doesn't fall on some city and the city gets polluted. Wow. Okay. So what battery solution are you going with? So actually we are just testing some of the regular lithium iron batteries.

**Dave Jones:** I would have thought you'd go for a more hardy battery. I thought the temperature swings would be too much for the. Yes. So if you would put it on the surface of the moon, then the temperature would be too high. Right. But if you look at the rover, it's designed in a very peculiar way.

**Dave Jones:** I mean, it's sitting up because we want to have the ground clearance, obviously. Of course. But we also, if you look at the soil, it has about a temperature of about 100 degrees Celsius when we are landing. Yep. And. That's because the sun's hitting it.

**Dave Jones:** Yeah. On the dark, where there's no sun. It goes down to minus 180 degrees Celsius, which is why our mission only lasts one lunar day. Right. Because this is very difficult. And how long is the lunar day? It's about 14 days. It's about 14.

**Dave Jones:** It's a half a month. You're right. Yes, of course. Right. But what if you land in, there's no hills nearby that can shade? What if you accidentally landed in next to a, you know. We try to avoid that. Right. Okay. But that could be a potential screw up if you land in the wrong spot and shady and whoops.

**Dave Jones:** There are many screw ups and this is one of them, yes. Right. Okay. So there is no backup. You have to have the sun to power it when you land. Yep. Right. So we have battery power that can drive it for about two hours.

**Dave Jones:** Yep. Which is sufficient to drive the 500 meters. Right. Yeah. Okay. But, you know, we're not thinking about the 500 meters. No, no, no. You're right. If we only would drive 500 meters, we would be very disappointed. Right. Even though this would be a huge success, you know, if you look at it from a general

**Dave Jones:** picture. Of course. You land there, the whole crowd cheers. Yeah. But we would be very sad about it. Right. And one of our sponsors probably as well. Right. Okay. So we don't want that bloody Audi Quattro's crap that goes 500 meters and breaks down.

**Dave Jones:** Yeah. Right. We need to avoid that one. Got it. So why those particular, back to the processes, electronics, why those processes? Because you're the head electronics guy and that's what you like. What are the requirements that drive that? Yeah. So the thing is that sometimes it's really just what you like, you know.

**Dave Jones:** On the main processor that we had in the previous generation, there was actually QNX running on it because I like QNX. Right. Why I don't like VXWorks as I've found out. We won't go there. Yeah. It's like, you know, but Atmel, for example, has a good reputation in the space industry.

**Dave Jones:** Okay. And because it's making space hard processes as well. Right. And for the smart fusion too, it's because it's a flash-based FPGA. So you don't have the problems with bit flipping stuff, at least not in the configuration area. Sure. And also there's radiation reports for every part they bring out.

**Dave Jones:** And so you can read out all the data. You can see how it does in the radiation environment. And this is critical for what we are doing. Oh, excellent. Right. Okay. But there were endless choices though that you could have chose. Yeah. The thing is that you can choose from any components you want, but you have to judge what the risk of using that particular component is.

**Dave Jones:** Mostly this is constrained by the radiation environment. So you don't want to use something where you have zero data about the radiation or you need to run a test campaign about it. Correct. MSP430 does have those FERM, for example, which is inherently radiation hard in some way.

**Dave Jones:** So that's, for example, interesting. Okay. Interesting. Yeah. Right. But the particular tests of the devices didn't show up so well. And then you're like, oh, this is a nice technology. It should be nice. And then you figure out actually it's not that good.

**Dave Jones:** And there's a lot of experience in there. Let's talk about the energy of this thing. How much power does it use? How much battery storage does it have? How fast does it charge? Can you live with lunar dust on the cells? Will that be a problem when you land if it kicks up enough dust?

**Dave Jones:** Will these cells get covered and you're screwed? What's going on? Yeah. So there are a lot of questions. A lot of questions. So let's start at the beginning. The solar cells that you can see here can produce about 93 watts. 93 watts? In the space environment because you don't have the atmosphere.

**Dave Jones:** Of course. So you have about 1,357 watts per square meter. Which on, if people don't know, on land here in best case condition, normally 1,000 watts per square meter. So you get 1,300. Yep. Sweet. Okay. So it's automatically. And so this power then is used to charge the battery in principle.

**Dave Jones:** And the battery is about 250 watt hours. Okay. And it's mostly used for the motors because you have those spikes and you cannot drive them. No, you've got to have a low ESR to drive. Yeah, exactly. Got it. So essentially that's architecture. We're trying to charge the battery constantly and use the energy

**Dave Jones:** that's available for the driving. Got it. How much power does the electronics take? Well, so it's about 30 watts when we're not doing anything. So you can charge with about 60 watts if we are not doing anything. But the peak energy consumption actually for driving uphill

**Dave Jones:** at the best conditions is actually not significantly more than the 90 watts actually we're taking. Okay. Interesting. Could you do this without having the tiltable solar panels? Yeah. So the question is really just how much pauses do you need to take. Oh, okay.

**Dave Jones:** To let it charge back up and then drive again. But you can continuously charge? You can continuously drive? Maybe. So we're aiming at the ability to continuously drive. Yep. This is what we really want to do. We want to do the continuous stream of video 24-7 for the 11 1⁄2 days.

**Dave Jones:** As somebody goes yee-haw as I'm controlling the – because it's almost real time. We're talking about a second and a half, so three seconds total delay. So you mentioned how you're going to do that. Can you explain how you're going to do that?

**Dave Jones:** You're going to have a three-second buffer in there? Yeah, so it's probably not as much as yee-haw. It's more like oh. Right. The basic idea, for example, dealing with the three-second delay is that you use the stereoscopic images to build a 3D scenery,

**Dave Jones:** and then you project a virtual rover into that and hope that the actual rover is following your projection. This would be one way of dealing with it. Because the problem is you're not seeing the rover from the outside as you're seeing it when you're driving remotely on Earth.

**Dave Jones:** Yeah, of course. But you only have the vision of your camera head. It can turn, but it will do with a three-second delay. So this is quite some challenge. So you see your actual camera, but when you're starting, you'll see a virtual rover driving.

**Dave Jones:** Oh, you'll see a virtual rover driving three seconds ahead. Yeah. Right, okay. But this is really just like a driving assistance that you have. Right. In the end, people are asking us, why is the rover so slow? And the three-second delay is actually the answer.

**Dave Jones:** We could drive 50 kilometers per hour, but with a three-second delay, you don't want to do that. No, you're just going to slam into Apollo 17. Yeah, exactly. You're in trouble. That should be avoided. So you think you've got the energy problem licked?

**Dave Jones:** Yeah, so the funny thing is that the energy was actually the one driving thing that got us from growing. I was going to say, because you started out shoebox-sized, right? Yes, exactly. And you did the numbers on the back of an envelope? Kind of, yeah.

**Dave Jones:** Literally? Yeah, yeah. It just can't work. Yeah. You can't do what you want. So it's not completely impossible. Right. So it depends on the architecture that you have. For example, if you say, okay, the lander is a relay, so then you can use like a Bluetooth connection,

**Dave Jones:** which is very low power. Yep. But the problem is that when you have a Bluetooth connection, you cannot go very far. Exactly. And so we wanted to have something that's really useful, and not just to win the money, but useful in doing exploration.

**Dave Jones:** Yep. And so we want to have something that can communicate to us directly, and this is why we need to have more energy. How far into the process did you decide that that was the only way forward, that you had to have a rover that could transmit directly back?

**Dave Jones:** That was actually pretty early on. Pretty early on, you came to that conclusion. So the second generation is already pointed at this direction. Oh, okay, right. But the first generation was what? The first generation was very optimistic. Just put it this way. But I wasn't in charge of the electronic sensor.

**Dave Jones:** Maybe that's why. Right. It was a couple of hobby motors with a little frame. Actually, no, it was already quite some nice motors, but it never drove, unfortunately. Right. Got it. The second generation was the first one I was driving. Right. So which generation is this?

**Dave Jones:** So this is the fourth generation. Fourth generation. How different from the third generation one? Not much, actually. Okay. So the third generation was almost the same size. The wheels were 20% smaller. Yep. But overall, really no big change. Just that there was a reason we called the former generation the tank.

**Dave Jones:** Right. So it was a little sturdier, you know, and a little more functional looking. Right. So this one definitely looks more sleek. This one is sexy, I've got to admit. Even lights up blue on the front. That's just sweet. That was cheap to have.

**Dave Jones:** Yeah. A couple of blue LEDs never goes astray, right? It's actually RGB. I can remove it. Oh! So you're sitting back in the control room remote. Oh, I think we need some red on the front now. Yeah, pink looks pretty freaky. Audience is getting a bit bored, the worldwide audience.

**Dave Jones:** Let's just... That's sad. Engineers. Yeah. We will not send that to the moon, by the way. Right. So is it one big board in here that does everything? Yeah, so this is one of the things that we thought about a lot, especially in the beginning.

**Dave Jones:** So in the beginning we anticipated to have a concept where we had one backplane and where we plug different parts into it. Plug in modules and that's... Engineers always go the modular route. They think, oh yeah, that'll be a good solution. Yeah, the thing is that...

**Dave Jones:** Why is it not? It is a medium good solution. Right, yeah, yeah. You can test each component on your own, which is a nice addition to it. And also production-wise it's not horrible. Exactly. But having a PCB of this size with connectors on it,

**Dave Jones:** it's like we were like... Connectors, you got vibration, you got contact issues. Yeah, so now we decided that we have cards, which plug in there, which are CubeSat size, which helps us to... That's right. You were saying, you've designed this around CubeSat. Yeah.

**Dave Jones:** And it's CubeSat size technology. Exactly. Tell us why. So the thing is that in the space industry, the CubeSat community is growing ever bigger. And if you want to do something on the cheap, the CubeSat community is probably providing you something. For example, radios.

**Dave Jones:** There are a great number of radios that we can actually use, which are CubeSat size. So you will use like an off-the-shelf radio? Yes. Oh, okay, great. Great, so you don't have to roll your own solution. No, developing a radio is not an easy task.

**Dave Jones:** Yeah, of course. Buying an off-the-shelf is probably a good idea. Right. What other modules can you get? Well, actually the radio is about the only part that we buy. Or is that where it starts? Yeah, we do all our own electronics. Everything is really custom-made for everything.

**Dave Jones:** So this is something that we started to develop very early on. We started with it in 2010. We started to develop our own PCBs, and ever since we just went ahead with it. It's not hard to lay out boards. In the scheme of building a rover, a board is not…

**Dave Jones:** Tell us, is it rocket science? One board in isolation on your lap works pretty well. Right. But eventually you have to think about EMC, for example, which gets funky. Why do you have to think about EMC? Well, not because of regulations. Right. And this is what I'm going to say,

**Dave Jones:** because I come from the marine electronics background, where you didn't care about that. It's in the middle of the ocean. You don't care about how much you radiate. It just wasn't a problem. So why is it not a problem yet it is? For example, in the beginning,

**Dave Jones:** we had a central motor driver unit. Exactly. And those are very high current conductors. They're horrible. And they get into everything you do. They do. And this can lead to some issues. And so this is something that we learned that we have to take care of.

**Dave Jones:** That's why they're out here. Yeah, exactly. That's one of the reasons. Yeah, yeah. It just gets rid of your problems. Yeah, yeah. And the other is inside the metal cage in there. Exactly. So the reason for having the module like this is also because you need to have some similar parts

**Dave Jones:** for it to get rid of the heat. Because you're in a vacuum. I've got it. You can't just plug in a heat fan. Because yeah, now you were saying before the thermal side of things, we've got 120 watts, sorry, 120 degrees C. Infrared radiation from the bottom.

**Dave Jones:** From the bottom. 120 degrees C, effectively, cooking the bottom of this. Exactly. So when the panel tilts this way, the electronics can cool out this side. Exactly. Because there is no breeze. Exactly. There's nothing. How do you get, how are you coupling the internal heat

**Dave Jones:** out to the body, for example? Because that's it. Otherwise, it'll just cook inside, won't it? Exactly. You won't be able to, oh no, no, it can thermally radiate from inside to the walls and then to the outside. Exactly. But it's not as nicely,

**Dave Jones:** is that what you're relying on? No, no. This is actually, so we're not just relying on it by accident. Right, no, of course. But we're actually thermally engineering it in such a way that the thermal conductivity is conducted to this side. Yep. And not to this side,

**Dave Jones:** which is the bottom part. Oh, the bottom, of course. Because this is where you get all the infrared, right? You get all the infrared. Right. So there's some thermal insulation goal for it happening on the bottom part. Got it. And some infrared radiation

**Dave Jones:** away to the black space on this side. So there's a very specific reason why it's shaped like that in there. Exactly. This side gets hot, this side you use to cool. Exactly. Because this is facing the lunar surface. Yeah, this is going to space.

**Dave Jones:** Yeah, it's going to space. And it's shaded by the other one. Brilliant. Yeah. When did you figure that out into the design process? Oh, boy. Yeah. Actually, our second generation already had kind of the tunnel, as we call it, but it wasn't, you know,

**Dave Jones:** really thermally designed in such a way. But in the second generation, we actually were like, oh, let's place all the electronics below the solar panel, which is not a good idea. Interesting. So we've got a 90-watt panel on this puppy. Yeah. We've got lithium-ion storage.

**Dave Jones:** I'm still surprised at the lithium-ion. Can that handle the temperature extremes? Because you've got no, this is not a thermally regulated environment inside there, is it? Is there insulation? Is there thermal insulation that helps? So the thing is that this part, so you have the angle part,

**Dave Jones:** this part, and you have this part here, and this is where the batteries are sitting, which is the coldest part. Ah, okay. So it will not get anywhere near 70 degrees. It will be 60 degrees. Right. Because the lithium-ion batteries are exothermic. They heat up.

**Dave Jones:** Yeah. So you don't, so cooler is cooler. Yeah, but the thing is that, for example, this is why we are running test campaigns with those batteries. Right. For example, the runaway is happening. If you peck them closely to each other, then the heat goes to the other cells,

**Dave Jones:** and then you get a runaway with all the cells. Got it. But if you put them into like a metal casing, for example, and you attach it to a thermal control surface, then you can control how much the runaway, you can kind of contain it,

**Dave Jones:** so to speak, and prevent that. Interesting. Thermals are a big thing. Space, electronics is a lot of thermals. Yeah, so one of the things, for example, about the Lander is it's flying in what's called a barbecue mode, which is... Oh, it rotates until such time

**Dave Jones:** as it gets close to the surface, then it orients it, and then it lands properly. The barbecue mode, it's really cool. It's really a good space term for it. I find it funny. It's that, you know, you heat one side, and because it changes,

**Dave Jones:** and your... because the other side gets very cold, and so you... You have to rotate it. ...try to even it out. If people don't know, that's why the, you know, when they went to the moon, you see in the movies, they rotate, the capsule rotates.

**Dave Jones:** It's got a slow rotation. Also, you have some spin stabilization happening. Oh, it's in spin stabilization, but yeah, it's so it doesn't bake. Yeah. That's one of the reasons, yeah. Awesome. So, reckon you've got all the thermal problems licked? No problems with thermal expansion

**Dave Jones:** of metals and stuff like that? Yeah. The panels? Oh, the panels are space-rated, right? Yeah. So you don't... Right. But the similar thing is that... Yep. ...why we are only talking about 11 1⁄2 days of emission is because when the temperature goes from

**Dave Jones:** the plus 120 degrees Celsius, it goes down to minus 180 degrees Celsius. At night, after... Exactly. Well, lunar night. Lunar night, yeah. And so the thing is that while the mechanics of dealing with that, well, not easy, but known, you know, the electronics part

**Dave Jones:** is very tough to do, you know. Got it. You have all the components and we are using off-the-shelf components and then the bonding goes boom and traces break and stuff like this. So we are not expecting to be alive on the next lunar day,

**Dave Jones:** unfortunately. Got it. But if anyone calculated there is a 2% chance it might, I don't know, cross your fingers and, you know. Yeah, you can always pray, you know. Right, yeah, that's going to work. So... Engineers don't pray. They calculate. Yes. Do statistics.

**Dave Jones:** Yeah, but the thing is, you know, you can, if you go to a manufacturer and like, you know, how is this component rated for minus 180 degrees Celsius? You are like, what? What? No. Please don't do it. It's very difficult to get it to,

**Dave Jones:** to get a vacuum chamber down to minus 180 degrees Celsius because, you know, just throw it into liquid nitrogen, for example, which is a different test. Have you been able to simulate the environmental conditions? Have you been able to do it? Yeah, we can,

**Dave Jones:** it's easy to go down to minus 60, for example. Oh, yeah, of course, yep. You can get regular thermal ovens, you know, industrial ones. Yeah, so this is some of the tests we do. We cycle the electronics up to 100 degrees and then minus 60 degrees.

**Dave Jones:** But below that you can't. So you can't really simulate the minus 180 that it would get in during the night? No. It would be very hot. You're right. Got it. It's going to die on the surface. What a shame. Well, maybe not. The only way,

**Dave Jones:** well, maybe not. The only way to get around that would be to have a thermoelectric generator in there because it's nuclear and it would last 50 years or whatever and continuously generate heat. You could keep everything warm. People ask us, why don't you use

**Dave Jones:** a big battery to heat it up? But the problem is that our design is specifically designed to get rid of as much heat as possible which is exactly the opposite of what you want to do if you want to survive through the night, right?

**Dave Jones:** Because you can't win. Yeah, it's very difficult to win. It's not impossible but very difficult. And it would screw up your mission requirements and everything else if you win. If you took that seriously as a requirement that, yeah, we really want a good chance

**Dave Jones:** of surviving that cold period which lasts for 15 days. Yeah. Right, so... The thing is that if you... This is why, for example, the space agency missions get significantly more expensive than our mission is because we say, well, we have 14 days of fun

**Dave Jones:** and then we are dead. Yeah, that's it. But if you say you want to have longer mission durations then you need to account for that and do more engineering and more mass and more mass means bigger rocket and this is why the mission to the moon

**Dave Jones:** from the space agency costs 600 million instead of... Right. Presumably, you have to land on the start of the... Sun cycle. A little bit later. A little bit later. A little bit later. Otherwise, it's not enough? Well, the thing is that the reason why

**Dave Jones:** you want to land on the beginning of the lunar day is because you need some shadows to see where the craters are. Ah, okay. So you've got an imaging, camera imaging system in the lander that... Yeah, yeah. Exactly. And because you need contrast, right?

**Dave Jones:** You need that light, dark contrast to get the depth. And so... But in the beginning of the day, the shadows are extremely long and it's very difficult but also the temperature is too low. Okay. So you need to land in about the second

**Dave Jones:** or third day of the lunar day cycle. Interesting. Right. Okay. So you've only got 12... That's why you've only got 10 days or something. 11 and a half days is what you're aiming at. You have bodged on. I'm calling you out. You'll see this

**Dave Jones:** in the unboxing video. I noticed this straight away. It's a $2 eBay headlamp. Hot snotted onto the front of your million dollar lunar rover. Yeah, the audio designers were going probably to kill me but... They haven't seen it yet? No, no. Ah, yes.

**Dave Jones:** I wouldn't show it to them. We're not going to show the public, do we? No, we're going to show my 350,000 subscribers. Sorry. But why do you need a light on the front? Yeah, so this is... We were doing some testing where we wanted to see

**Dave Jones:** if the light is helping with the driving in partially shaded areas. Okay. So have you got like a simulated lunar environment? Yeah, so this is in Berlin. We're actually currently building a 10 by 20 meters test bed where we can actually drive our lunar rover on.

**Dave Jones:** Awesome. And you've got light studio lights set up. You can simulate different conditions as the... That would be nice. But you can do some envelope calculation on what kind of lamp you need to do a proper lunar illumination with 1,357 watts per square meter.

**Dave Jones:** So that's about 200 square meters. Yep, yep. So we have a flat light coming from the top with LEDs and it's about studio light. Okay. It's a shame to honestly but everything else would be like driving the cost to infinity and beyond. Is the electronics

**Dave Jones:** a big deal in this? How many lines of code? How many... Like is it... What's the hardest part of doing this? I mean presumably the electronics is like yeah, we can just do that. Is it a given that the electronics is going to work?

**Dave Jones:** So the thing is I would say the hardest part about electronics is the integration of the multiple components. Right. So you have on your lab bench you have one motor driver with one motor and on your lab power supply, right? Yeah. And you drive it

**Dave Jones:** and it works perfectly and then you have eight of those and you start to turn left and go full speed at the same time with all eight motors and then stuff gets very interesting, you know. It really checks your power design and this is where

**Dave Jones:** I would say the hardest part is really the power supply design actually. Okay. Interesting. How you're not using any one hung low brand caps in there. How do you design a space power supply? Yeah, so the interesting part is that you so for example

**Dave Jones:** if you you cannot just use any capacitor you find, you know. So electrolyte capacitors They have a liquid in them. They have a liquid in them. Oops, they can freeze. They can freeze. Yeah, but the hardest part is actually they if you're driving

**Dave Jones:** in a vacuum then you know it boils off and Oh, okay. Yeah, but they're sealed. They're hermetically sealed to a point. Yeah. Because they're a pressure vessel as well. They're a Yeah, but yeah, not not well enough to be just using it. Right.

**Dave Jones:** So there are some hermetically sealed capacitors actually some of them which you are using but you buy so one capacitor is about 50 to 200 euros and you don't want to have That's nothing. That's nothing for a capacitor. You don't want to have

**Dave Jones:** too many of those, right? Right. So you're probably going with a tantalum or ceramic capacitors. Right. So for example if you're on a PCB that you see we actually mostly have ceramic capacitors because of that. Okay. Because those are those are pretty safe.

**Dave Jones:** And also from a vibration point of view if you have components that are standing off too high Yep. the vibration is The vibration. Tell us about the vibration testing in this because that's a big deal. I've had a lot of experience vibration testing electronics

**Dave Jones:** and parts you never think would vibrate off. You hit the resonant point on the board and boom it just popped it just pops off. Have you had any failures? No. How many? So far we're quite good actually. Okay. Right. So you thought about it

**Dave Jones:** because you knew you were going to you're in a about the most rugged environment. And also you know the PCBs itself are mostly small. Right. So you know if you have bigger ones then you're running into the edge if you don't support the board in the middle

**Dave Jones:** it can hit a resonant point it's going to lower resonant frequency and it can And also you know because we need to be firmly attaching to all these components Right. You know you also have those dampening points so Got it. Would you pot your boards?

**Dave Jones:** Encase them in a like In a pretty like That's a lot of rugged environments will do that military environments they will just like we don't care about vibration because we're going to pour our goo in Is that something you've looked into or Yeah.

**Dave Jones:** So that's Because you can get the rock hard ones you can get the rock hard ones or you can get gel like silicon gel one like gel ones that are re-enterable Yeah. You know so you can repair things and then fill them back up and

**Dave Jones:** Did you look into potting Yeah. We looked into some of those we also want to the thing is as I told you we're in a vacuum so you don't have any conductivity or convection going on so you need to thermally connected so this is why

**Dave Jones:** so you can get thermally encapsulate materials as well. Yeah. Yeah. Exactly. This is why those are for example interesting for some of our publications Are you using those thermally conductive stuff This is something very currently investigating what we need to do Right. Okay.

**Dave Jones:** I worked on a military thing once and nitrogen is a very good heat conductor so it would conduct the heat from the core board out to the metal case and things like that and it got tricky you know it was Yeah. But then you need

**Dave Jones:** to seal it You need to seal it and we had to buy a whole machine that would actually sniff the seal to make sure there's no leaks and horrible Yeah. Don't go there. Tell us about the camera Yeah. So the camera is pretty neat

**Dave Jones:** It's got three eyes and two wide angle cameras which are used for driving Those are actually color sensors Yep. It's debatable whether you need color or not I was going to say but they come as color so Yeah. So we can also if you

**Dave Jones:** we can look at the earth Oh yeah. Okay. Yes. Yeah. You want an earth rise shot kind of you know Yeah. Also so we have the middle one is a black and white It's a tele lens and it has a has a filter wheel

**Dave Jones:** in front of it so that we can look at different wavelengths Right. And it also allows us to make a gigapixel panorama Ah nice. Does it stitch that in camera or does it No. No. We do it in earth It's pretty high detail

**Dave Jones:** because you have 2K by 2K Yeah. It's a 2K sensor Yeah. And you said it can do 150 frames per second Well yeah it's Why? It was a sensor for other purposes Okay. And it can do 100 frames per second you know Awesome.

**Dave Jones:** Awesome. We would be driving pretty fast to need that but Yeah exactly but you know but can your hardware sustain that? Can you get the data out that quick? No. No. No. No. No. We are aiming at 15 frames per second Right. Okay.

**Dave Jones:** And how are you processing that? By Ethernet Yeah. You've got Ethernet link inside this thing Yeah. That's interesting. Why? Mostly because it's easy to debug Yeah of course. It's a separate module you can debug anywhere like Yeah this is one of the reasons

**Dave Jones:** you know that you when you're dealing with space stuff you can use always the space stuff but if you're using the space stuff it's expensive Exactly. And so we are aiming at technology that is easy to if you have something that's easy to use

**Dave Jones:** it will be tested Got it. And the more testing you have the better your confidence is in being reliable Exactly. You know and so you don't want to do the funky stuff and do the stuff that works you know and Ethernet is a very good

**Dave Jones:** solution because it's been around for 40 years Yeah. And you can talk to it in any operating system and it's very well supported Yeah. And you can hear the camera and the image processing Oh, okay. You're not buying like a little hub from the $2 store

**Dave Jones:** are you? No. No, no. I didn't think so. Right. There is something fancy going on Okay. There are some switches Okay. So you've got one main camera which filters which is 2K what? The other ones are 2K and the other thing that is

**Dave Jones:** very important for us is to have enough time for testing and if you use different cameras you have to test them all the time Exactly. So we are looking to reuse as much as possible Yep. And so we have 3 cameras there and

**Dave Jones:** one camera which is sitting at the bottom which is not in the water and we need a real big wide angle. Yep. This is something that we for example found out with driving around with this one that it's very difficult to judge what you're

**Dave Jones:** doing if you can't see the wheels and this was one of the things that helped us tremendously. Now this thing is that autonomy is great but it's also computationally quite expensive so one of the constraints is from an energy perspective which results in a thermal

**Dave Jones:** constraint which results in a mass constraint and then you know so essentially we were deciding that we cannot sustain autonomy except for not a real time autonomy that is pretty fancy but something simple for example. Any accelerometers or anything else fancy fancy in

**Dave Jones:** this? Of course there are many temperature sensors and have an IMU which is a gyro and accelerometer three axis. And what's that used for? Well you have to know the temperature and you have to know the temperature and it's very important to know

**Dave Jones:** if you're going down a slope for example but unfortunately magnetometers are quite useless. Right yeah of course there is no magnetic field. And the most fancy sensor we have is the audio. The microphone to the body so we can hear the clunk clunk

**Dave Jones:** clunk clunk okay because yeah it obviously doesn't transmit through the air but it'll transmit through the chassis. Exactly. And this is like an acoustic debugging aid to know what's going on in the rover. I don't think we don't have no no I don't

**Dave Jones:** think we no I don't think they had no any audio at all I think it was just video wasn't it? Yeah. It was just video of them going. And the radio and the radio and the radio but that was that was it. So that'll be

**Dave Jones:** really cool. Clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk

**Dave Jones:** clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk

**Dave Jones:** clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk

**Dave Jones:** clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk clunk CLANK Well... let's start the motor So this is our motor drivers that is in here what you can see is we use those capacitors because the

**Dave Jones:** other ones are a bit tricky with electrolytes but you could use tantal that would work and you tried to but I hope it's added to the protection Alright Carsten we're gonna unbox a Lunar Rover a Lunar Rover unboxing let's do it carefully carefully

**Dave Jones:** carefully here we go oh alright wiggle wiggle wiggle wiggle wiggle wiggle wiggle wiggle we're wiggling we're wiggling a Lunar Rover
