---
video_id: GkVRX3h_A30
title: EEVblog #50 - Solid State Cree LED Lighting, and How Thermal Design Sucks.
url: https://www.youtube.com/watch?v=GkVRX3h_A30
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 20, "2": 40, "3": 54, "4": 82, "5": 107, "6": 125, "7": 140, "8": 161, "9": 177, "10": 202, "11": 220, "12": 244, "13": 264, "14": 280, "15": 299, "16": 317, "17": 343, "18": 363, "19": 382, "20": 403, "21": 419, "22": 440, "23": 461, "24": 484, "25": 496, "26": 522, "27": 540, "28": 552, "29": 573, "30": 585, "31": 611, "32": 633, "33": 649, "34": 667, "35": 683, "36": 693, "37": 723, "38": 745, "39": 766, "40": 786, "41": 807, "42": 828, "43": 854, "44": 874, "45": 894, "46": 912, "47": 934, "48": 954, "49": 968, "50": 988, "51": 1008, "52": 1028, "53": 1047, "54": 1058, "55": 1084, "56": 1097, "57": 1121, "58": 1132, "59": 1149, "60": 1168, "61": 1179, "62": 1198, "63": 1218, "64": 1236}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, this time around we're going to talk about solid state LED lighting. Why? Well, I just built myself a new outdoor deck and I put a

**Dave Jones:** new roof over it and everything and it's really quite cool. It's an outdoor room and to finish it off we need to install some lights to, you know, to light the place up and well, you know, our old one had like, you know, these old style spotlighty, you know, these are compact fluoro

**Dave Jones:** G10, what do they call them? Yeah, GU10 bulbs and things like that and we're going to use these again but I thought, hey, why not give LED lighting a go? So I decided to give these Cree solid state LED lights a go. You've seen them, these little Cree ones.

**Dave Jones:** Now, I decided to get basically the, pretty much the best ones on the market. It's the Cree X-Lamp XPG and the data sheet claims some really amazing things for them. You know, things like 132 lumens per watt. It's incredible. I mean, you know, one of these compact fluoro, this is a standard compact fluoro

**Dave Jones:** and this one is 57 lumens per watt, right? Less than half and this one here, one of these circular ones, this is 70 lumens per watt whereas these little tiny itty-bitty Cree XPG LEDs are up to 132 lumens per watt. Unbelievable and, you know, if you use these

**Dave Jones:** circular fluoros, these T5 circulars, they're better than these compact fluoros in efficiency but they're still not as good as these little LEDs. Is it bullshit or do they really work? So I thought I'd get some and try it out. So the first thing I did was take a look at the data

**Dave Jones:** sheet, you know, 132 lumens per watt, that's its, you know, that's its maximum sort of efficiency if you drive them at one amp, you know, but I was only going to drive them at 700 milliamps just to be on the safe side and also because that's a typical value you can get out of these constant

**Dave Jones:** current controllers that are powered from the mains. So I thought I'd drive at 700 milliamps and I did some rough calcs based on our, the old roof we had out there and the old lighting system and it looks like, you know, that maybe, you know, a dozen or, you know, 16 of these

**Dave Jones:** LEDs might be, you know, might actually do the job, it might be good enough. So I borrowed some old Cree LEDs, these star versions from a friend and they're not the XPG ones which are the latest super efficient series ones but I got some of them as a trial.

**Dave Jones:** I put a couple of them on a alloy strip, an aluminium strip or aluminum, sorry for you US people, you don't know what alloy, you know, aluminium is because, you know, you've got to heat sink these things because they get quite hot. So I didn't do any thermal calculations or anything like that because,

**Dave Jones:** you know, those sort of things are traditionally very tricky and well I knew this would be plenty, you know, it's a 25 millimetre wide aluminium strip, you know, I was going to have them a metre and a half long and I was going to mount eight of these LEDs per strip and it's a three millimetre

**Dave Jones:** thick strip so, you know, plenty of heat sinking I thought and, yeah, so I wired them up and here's some photos. And it turned out that with 16 of these Cree XPG LEDs running at 700 milliamps each gave more than adequate light and here it is.

**Dave Jones:** As you can see it's hard to get a photo of it but I'll take some video after this and I'll hopefully show you it on live video to see what it's like. But it worked really well and, well, that's the end, you know, normally that would be the end of

**Dave Jones:** the story and I wouldn't do a blog on it because it's not very interesting. Okay, solar state lighting works, they're great but, hey, what makes it more interesting? Well, I decided to do some measurements. Now I'm here to tell you that thermal heat sink design is really tricky business.

**Dave Jones:** There's so many variables involved in it that, you know, it's really hard to do it accurately for all but very simple calculations. Now you would think this one would be very simple to calculate it. You've got a strip of aluminium and you've got some LEDs mounted on there, you know, the dimensions

**Dave Jones:** and the thickness and everything like that and it should be pretty easy to calculate but it's not. Trying to calculate something like this it's, well, it's not impossible but it's very, very difficult and I tried to do some basic calculations of this. I found some graphs which I thought were,

**Dave Jones:** you know, a pretty good source of data for a three millimetre aluminium plate and for roughly the surface area which I had here, which was 1.5 metres by 25 millimetres wide, I got, you know, an answer of like 3 degrees C per watt and that

**Dave Jones:** sounded quite large to me and based on the amount of power I was putting into these eight Cree LEDs on here, it wasn't getting anywhere near hot like you would actually predict from those graphs, so something was up. So I decided to take some measurements and get

**Dave Jones:** some data because I love data and I love plot and stuff because it's great fun. So what I did is I attached some thermocron eye buttons. I've mentioned these in a very old blog, little temperature loggers. I attached them to the aluminium strip at various locations along and here's a photo of the

**Dave Jones:** actual installation of them and as you can see, and I used one for ambient temperature as well, just hanging down there and I attached them to the strip and this is what I got, okay. I got this data out. I did it the other night and basically what it is, is temperature in degrees C versus

**Dave Jones:** time and this goes from about 6pm up to about 8.30 or something like that, so just over a couple of hours. Now I'll put up a more detailed image of this later but as you can see, the ambient started out at around about 37, 38 degrees.

**Dave Jones:** Now yeah, it was hot in Sydney just the other night. It was really hot and then it started to cool down a bit and then it started to drop fairly drastically. It dropped down to like 32 pretty quickly and as you can see, this is where I took them from inside and

**Dave Jones:** the other three are the temperature sensors. So as you can see, these were inside and I took them out and they stabilised and this is where I switched on the light and you can see it ramp up and it hits a pretty stable equilibrium here as you'd expect and so you know, this didn't look

**Dave Jones:** too remarkable until I plotted the difference between each one of these three temperature sensors and the ambient and this is what I got. Once again, I'll show a higher resolution version and this shows the difference. So zero degrees up to about 13 degrees was the maximum difference and

**Dave Jones:** as you can see, it ramped up fairly quickly and then it sort of stabilised a bit here but then it ramped up a bit further and then it did some jigging about here and then there's a real sudden drop just about here. It's very remarkable and very sharp.

**Dave Jones:** Why? And why did it do that? It should basically reach a thermal equilibrium and then stay flat but it didn't and it took a couple of seconds sort and then I realised, aha, a storm came through and it's not because the temperature was dropping, it's because the wind picked up and the wind was causing a cooling

**Dave Jones:** effect on the heat sink. It was drastically increasing the efficiency of the heat sink because of the wind blowing across it and that's why you get these sudden falls and then, you know, these peaks and jaggies. If you're in a perfect pristine environment you would have, or a very controlled

**Dave Jones:** condition in a lab, you would have got basically a flat line but we didn't so I thought that was rather interesting. So I decided to do some calculations and see what I could come up with. Now I basically, I modelled the system something like this.

**Dave Jones:** The Tj is the junction temperature actually in the LED itself, okay, and that's an unknown. I, you know, I just wanted to know that out of curiosity. Now Pt is the total power that I'm, that LED is wasting or putting into the heat

**Dave Jones:** sink. Now we'll talk about that in a minute because that's a rather curious one. Now the data sheet, if you read it, it says that the thermal resistance of the LED to its solder junction is 6 degrees C per watt and also it comes on, the LED comes on a little base.

**Dave Jones:** Now I didn't use one of these star ones, I used one of these little 10 millimetre round ones and here's a photo of it and they're really quite cool and I couldn't get any data on what that actual thermal resistance of that is but, you know, it's going to be fairly low so it's now iminium based so I don't really

**Dave Jones:** know that so I sort of took that out of the calculations and then there's a thermal adhesive. I actually used a, what's called an Arctic, well it's a brand name, Arctic Silver Thermal Adhesive. Now it's not a thermal paste, it's not like a heat sink compound, it's actually an epoxy, a

**Dave Jones:** permanent epoxy adhesive that's thermally conductive and it's really cool stuff. I highly recommend you use it and if you look at the data sheet for that it's, it's incredible, its thermal resistance is incredibly small, it's like 0.05 or something less than that degrees C per watt for, you know, an

**Dave Jones:** x micron layer of film and I don't know how thick my film is or whatever but, you know, it's very, very low so you can, like, take that out of the equation and then there's the thermal resistance of the heat sink. Now, as I said, I looked at some graphs and things, I found some graphs

**Dave Jones:** and stuff for a three millimetre plate of aluminium and it seemed quite high at, like, three degrees C per watt or something like that and I thought that, you know, that didn't seem right. I knew, my gut instinct told me it was going to be much, much lower than that so, you know,

**Dave Jones:** we'll be able to calculate that in a minute and then there's the temperature of the heat sink down the bottom which we actually know, well, the differential, which was 13 degrees C from that difference graph we saw before. So, let's see what we can come up with.

**Dave Jones:** Okay, so how do you calculate the total power that you're putting into your heat sink? How much, you know, waste heat is that those LEDs producing? Well, you can take the figure of, if you want to be on the real safe side, then you take the figure, the maximum figure and not caring about the efficiency of the LED.

**Dave Jones:** So, you assume the LED is zero percent efficient and in this case, each LED is 3.2 volts at 700 milliamps each. So, they're drawing about 2.2 watts. So, in the worst case, with a zero percent efficient LED, there, you know, there's going to be 2.2 watts of waste heat but, well, you know,

**Dave Jones:** that's a little bit too crude. I just, out of curiosity, I wanted to know what the efficiency of these new LEDs was. Now, if you look at the data sheet, okay, here's the data sheet. It doesn't tell you the efficiency. You think it might, right, because it has on the front page here of, you know,

**Dave Jones:** I can put it up but it says the available with typical efficacy of up to 132 lumens per watt. Okay, now, that's not efficiency. Now, you think, oh, that might be some chinglish word or something like that for efficiency but it's not. It's a different word entirely and it's a trap for young

**Dave Jones:** players. Efficacy, it's different to efficiency. Now, this data sheet does not tell you how efficient these LEDs at all. It doesn't tell you, give you any information as to how much waste heat you're actually going to produce, you know, lower than that. I mean, you know, is the LED 10 percent

**Dave Jones:** efficient, 20 percent, 50 percent, you know, 80 percent? What is it? Well, it turns out what you have to do to find that figure is you've got to actually look at a typical theoretical response. Here it is. Now, I can put it up on the site as a better quality thing but it's basically a lumens

**Dave Jones:** per watt response of white light basically and they're all the different colours of the white light spectrum and you'll see that the maximum possible efficiency of a green, a pure green LED or light source is actually 683 lumens per watt. Now, but because we're using, we aren't using

**Dave Jones:** a green LED, we're using a white LED. So, you actually have to take into account the entire spectrum and as it turns out, depending on, you know, how you actually calculate the eye response and stuff like that, it can be anywhere from, well, okay, so we've got 683 lumens per watt,

**Dave Jones:** that's our maximum efficacy, not efficiency. Now, as I said, the white light spectrum, it can be anywhere from around about 300 to 350 lumens per watt and that's for white light. So, that's the figure. I'll take a value of 330 because, you know, that's a typical figure taken, I believe.

**Dave Jones:** So, we'll take it, the maximum possible efficacy of an LED is 330 for a white LED is 330 and the data sheet for the Cree says it's doing 130. So, what's that in percentage? You just divide it in and you get, bingo, 39% efficiency.

**Dave Jones:** That's how efficient these LEDs are. They're a hell of a lot more efficient than these, you know, standard compact fluoro which is, you know, down around, you know, 15% or something like that, 15 to 20. It's half of what it is, hence the lumens per watt

**Dave Jones:** figure. Now, I'll round that down to 35% efficiency because there's going to be, you know, some loss there. We'll round it down. So, if we're powering this thing, putting 2.2 watts into it, the actual waste heat with the 35% efficient LED is 1.4 watts and because I've got eight of these

**Dave Jones:** mounted on the one strip, my total power is 11.2 watts. There you go. What was the point of that? Well, you know, I don't know but it's interesting. Okay, so we know our total power going into the heat sink due to eight LEDs is 12 watts.

**Dave Jones:** So, we've got 12 watts flowing through our thermal resistance system here. So, you can, and we know that the temperature differential on the heat sink down here is 13 degrees because we measured it, the difference on that graph which I showed you before.

**Dave Jones:** Now, that means if you divide that into that, you know, you get approximately 1 degree C per watt for the aluminium strip, you know, based on the total system power and things like that. Now, well, that's pretty good and it shouldn't allow us to calculate the temperature of the

**Dave Jones:** junction of each LED but, well, I don't think it's going to be that easy because we no longer have 12 watts going into the system. We've only got 1.4 watts for the individual LED and we based our, the calculation of this based on the total power of the system and it gets all messy because we've

**Dave Jones:** got a strip like this and we've got eight little LEDs on here like this and so you've got multiple power sources coming into your system like this and it's just, it's all over the shop. It's messy. I don't like it. It sucks and, you know, you can do the calculations, you know, if you've got,

**Dave Jones:** if you've now got 1.4 watts for each LED going through, you know, this is going to, this is going to have an 8.4 degree C rise above here and, you know, this is only going to have 1 degree or something like that and, well, what does it work out to?

**Dave Jones:** Well, bugger if I know but it's not much. That's the thing. So what's the point of all this calculation? Well, we came to the conclusion that it's often just not worth doing thermal calculations because they're just messy and, well, you could spend your whole life trying to analyse the damn things and it's not worth it.

**Dave Jones:** Now, you want to know what a really interesting thing about these LEDs is, is that they're so darn powerful that you can actually feel the light. You can actually feel the heat from the light and it's not coming from the radiant heat sink.

**Dave Jones:** If you, you know, put these things on here, you remember at 35% efficiency, this is going to be putting out about, at 2.2 watts, it's going to be putting out about 0.8 watts in that little tiny surface area in light. So there's 0.8 watts worth

**Dave Jones:** of light there and if you put your finger on the heat sink, when this is mounted on the heat sink, the base of it, okay, it doesn't feel that hot at all. As we showed, it's only, you know, 5 or even 10 degrees above ambient.

**Dave Jones:** It's not much if you mount it on a decent heat sink. It remains pretty cool. And then the base on top of that, you put your finger on that and it's still, it's still quite cool. But if you put your finger over the LED and don't actually touch the metal, it'll burn you.

**Dave Jones:** You can't keep your finger on there. It's because this thing is pumping 0.8 watts of light energy into, you know, a couple of square millimetres of your finger. It bloody well hurts. Now you've got to be really careful with these terms efficacy and efficiency because often they're used

**Dave Jones:** interchangeably by people who don't know the difference or they can actually mean the same thing depending on the luminous efficiency. It can be the same thing as the luminous efficacy depending on the context you're actually using it in and it gets quite complex.

**Dave Jones:** So, you know, look it up and study it. It's quite actually interesting the differences and how people, you know, how you can work out efficiency versus efficacy and things like that over spectrums of light. It's a rather interesting aspect of engineering. Check it out.

**Dave Jones:** So what did I learn from all this thermal calculation rubbish? Well, not much at all because when it comes down to it, engineering is often as simple as wetting your finger and sticking it on there. Is it warm? No, not really. She'll be right.

**Dave Jones:** Yes, I know everyone's going to write in and they're all going to say, oh, my model's wrong and I didn't do this, I didn't include that and I got this wrong and that wrong. Well, look, don't bother because the whole point of it is that thermal design

**Dave Jones:** is messy and, well, sometimes it's just not worth doing. So, does it work? Okay, let's check it out. Ta-da! And yes, it does. Perfect. 16 Cree XPG LEDs. Perfect. Reflecting off the roof. It's a winner. I like it.
