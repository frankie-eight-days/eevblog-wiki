---
video_id: dxc5aHCVQzA
title: EEVblog 1390 - NEGATIVE Household Solar Consumption? WHY?
url: https://www.youtube.com/watch?v=dxc5aHCVQzA
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 49, "3": 78, "4": 104, "5": 130, "6": 150, "7": 172, "8": 190, "9": 207, "10": 227, "11": 250, "12": 280, "13": 298, "14": 310, "15": 323, "16": 340, "17": 365, "18": 391, "19": 411, "20": 428, "21": 442, "22": 458, "23": 465, "24": 480, "25": 500, "26": 518, "27": 536, "28": 550, "29": 566, "30": 580, "31": 595, "32": 609, "33": 626, "34": 642, "35": 659, "36": 674, "37": 689, "38": 701, "39": 714, "40": 731, "41": 754, "42": 769, "43": 787, "44": 804, "45": 821, "46": 842, "47": 860, "48": 874, "49": 890, "50": 911, "51": 931, "52": 949, "53": 968, "54": 988, "55": 1006, "56": 1023, "57": 1042, "58": 1059, "59": 1080, "60": 1094, "61": 1112, "62": 1127, "63": 1144, "64": 1158, "65": 1177, "66": 1193, "67": 1210, "68": 1225, "69": 1240, "70": 1258, "71": 1276, "72": 1293, "73": 1307, "74": 1326, "75": 1343, "76": 1358, "77": 1376, "78": 1395, "79": 1409, "80": 1421, "81": 1438, "82": 1456, "83": 1472, "84": 1491, "85": 1507, "86": 1530, "87": 1547, "88": 1562, "89": 1577, "90": 1593, "91": 1606, "92": 1627, "93": 1647, "94": 1662}
---

**Dave Jones:** Hi, I promised I'd do a follow-up video showing an unusual issue I had with my new solar power system I had installed, the Enphase system, and also to do with my old solar analytics system as well, because I've got essentially two separate systems installed.

**Dave Jones:** I've got my original 3kW solar array installed, hooked up to my existing Sunnyboy SMA string inverter, which is monitored by a solar analytics system, and I've done videos on all these things, I'll have to link them in if you haven't seen them. So that's a complete monitoring solution, we just move that 3kW system from one side of the roof to the other, so then we can have room for the more optimized new 5kW Enphase system, which has the 14 Enphase microinverters,

**Dave Jones:** going into the Enphase Envoy monitoring system, which we have here. So these two systems are totally independent, and they're running side by side, so I've got two different generation sources, two different inverter systems, and two different measurement systems. So, yep, I've got two different systems here, and I can access the analysis, data analysis and graph pages for both of them, so the solar analytics, this is my old 3kW system thing, this is back on the 2020.

**Dave Jones:** So this is my old 3kW system thing, this is back on the 2020. So basically installed at the start of the month, 1st of March, so this was just before I installed it, and you can even see, the yellow is the production curve, i.e., you know, energy coming from, or power coming from the panels, it's not energy until it's over time, power coming from the panels, so at each moment in time, that's the peak power there, so 2.3kW produced, etc, etc.

**Dave Jones:** And the purple one here is how much I'm actually consuming during the day. And the purple one here is how much I'm actually consuming during the day. And the purple one here is how much I'm actually consuming during the night. I've got two fridges, we're running two fridges, so that's, apart from any, like, phantom power devices, you know, standby power, that's pretty much all we're running, so only like, you know, 150, 200 watts or whatever during the night for the two fridges, and then we, you know, nobody's home during the day, then we come home, we use some appliances, and we switch them on, and all that sort of stuff, everything's hunky-dory.

**Dave Jones:** We've got energy produced and energy consumed, and then something interesting happened. After we did the installation, that's the day we installed it, so don't worry about that, and then the next day, this is what I started getting on the exact same solar analytics system, all we did was move the panels from one side of the roof to the other side of the roof.

**Dave Jones:** What's going on here? You'll notice that the purple graph now goes negative, negative 4 kilowatts consumed. What? How do you get a negative consumption? That's a bit weird, and then, you know, at like 6pm, it goes positive again, and what's going on here?

**Dave Jones:** Well, it turns out that this is actually a very common issue when you have two systems installed independently side-by-side like this, and they're not, well, I'm not going to say not installed correctly, but they're not set up correctly, and they don't know that each other.

**Dave Jones:** And a lot of people who don't monitor their data just ignore, like, you would just never notice this sort of stuff, all you care about is your net metering, that's all they care about is how much electricity they pay, but, you know, nerds like me who follow the data, it's like, what?

**Dave Jones:** It's gone negative. So it turns out this is actually a relatively common problem when you have two different systems installed like this, doesn't happen if you just have one system installed. And there's actually a fairly significant... So let's go through it. Just a quick check, though, of the N-phase one.

**Dave Jones:** This problem not only happened on my old 3-kilowatt system here, it also happened on my N-phase one. This is where, like, it was installed here, but I don't know, they didn't switch the data monitoring on until there. And, look, 200 watts consumed, and then during the day, this one's the yellow one is the actual consumption in this particular case.

**Dave Jones:** It's going negative, minus 880 watts consumed, and then mysteriously, at night, the consumption goes positive. What the? Now, when I posted this on Twitter, quite a few people said, oh, your current clamps must be installed backwards. And that, you know, seems a legit thing, because, well, after the installation, we're now getting negative current consumption, right, on both of these systems here.

**Dave Jones:** It turns out... It turns out, no, the current clamps weren't on backwards. So if you aren't aware, it's current clamps like these ones that they install on these monitoring systems to allow you to measure the current, not only from your solar panel, so you can measure the production power coming from your panels,

**Dave Jones:** but you can also measure the consumption of your house, and you can measure the current going out to the grid as well. And you can see, maybe you can see just on the top of there, there's a little arrow. And you have to install these the right way.

**Dave Jones:** And sure enough, if you install it back to front, and the current goes in the other direction, then, well, it's going to give you a negative output. And, yeah, that's a real thing. You've got to install them the right way. But that's not what's going on here, though.

**Dave Jones:** So, anyway, let's go back to this graph here. Now, you might notice the shape of the production curve, i.e., the sun, right? So the sun is producing this yellow curve. It just... Look, it dips here, and then the purple is the consumption. The purple also...

**Dave Jones:** When the sun dips, it also dips when the sun dips, whaaat? It's, look, it's almost like they're a mirror image of each other, hmm, what's going on? So it turns out this kind of mirror image thing is not a coincidence. There's a reason that the consumption matches what the sun is doing, and why, when the sun goes down at like, you know, it's all gone at like 5:00 or 6:00 p.m.,

**Dave Jones:** our consumption suddenly goes positive again. Can you pick it yet? Stop this video and try and figure out what could possibly be wrong with two systems on your roof and two different measuring systems giving the same negative power during the day. And once again, if you zoom into this, you'll find that the envelopes, once again, they match here.

**Dave Jones:** So the orange one consumed goes up when it, uh, when the value drops, and look, and even during the day, look, it actually went positive. Like this, during the day when that was up. So see if you can figure it out before I give you the answer, because it's, it's rather a subtle thing, and you've got to put your thinking cap on to figure out what's going on here.

**Dave Jones:** So the best way to explain what the problem is here and how it's, uh, solved is to go over to the whiteboard. So let's take a look at the potential problem you have when you have two separate solar generating units like this and two separate monitoring solutions like this connected to the one house.

**Dave Jones:** Now, we've got our grid up here. We've got our grid up here. Here it is, and we've got our line coming in. Now, of course, the power can either be coming in from the grid like this, or it can be going out, depending on whether or not you're using, consuming all of the power from the panels.

**Dave Jones:** If you're producing more power in your combined solar arrays than you're using inside your house, you're going to be exporting out to the grid. But if you're consuming more in your house down here than your poor panels can provide, or it's nighttime or whatever, then you're going to be pulling power from the grid.

**Dave Jones:** But if you're consuming more in your house down here than your poor panels can provide, or it's nighttime or whatever, then you're going to be pulling power from the grid. So current can both flow in from the grid and out to the grid like this.

**Dave Jones:** Now, in this particular case, we're going to look at my exact example. We've got the 5-kilowatt system, the new one with the Enphase microinverters. And then we've got the existing 3-kilowatt system with the solar analytics monitoring system. Doesn't matter that you use a Sunnyboy string inverter.

**Dave Jones:** We're just looking at the solar analytics is the monitoring system that we're using, and the Enphase Envoy is the monitoring system we're using for this. The inverters don't matter. So both of these systems, indeed, any solar monitoring system is going to be measuring the production, what's called the production, i.e., the power, the current flowing out of the panels like this.

**Dave Jones:** So they'll have that little current clamp transformer around physically the one wire coming from the Enphase inverters. And remember, this is after the inverter. So this is after it's generated the 240 volts required and put it onto the mains. So as I said, doesn't matter whether it's a microinverter.

**Dave Jones:** There are inverters up here or a string inverter. This has nothing to do with it. It's not actually measuring the DC. It's after the inverter. So measuring the production from the panels is easy and simple. You can't goof it up. You just put a current clamp on there and it goes into the input to the either the Enphase Envoy monitor or the solar analytics monitor.

**Dave Jones:** So each system has its own current clamp measuring that. And as we saw, that wasn't the problem, although, as I said, you can actually put the transformer on back to front if you goof it up and, well, you'll get negative. But that's not what's going on here.

**Dave Jones:** What's going on here is we have a problem measuring the consumption, the load. Why is it going negative? And why does that pattern follow the production from the panels? I.e. why does it follow the sun? It's negative during the day and it's positive during the night.

**Dave Jones:** What's going on? Well, this is where it gets a little bit tricky. Now, of course, the obvious solution is to simply have a current clamp on here that measures the load like that. And, of course, you'd have a second one here. And that would go up into there like that.

**Dave Jones:** So each system knows about the load and consumption. And once again, you can't really goof that up unless you put the current clamp on backwards. But then it would always read backwards. It wouldn't go negative during the day and then positive during other times.

**Dave Jones:** So what's actually going on here? Well, it has to do with the switch box and the sort of limitations in there for being able to put these load measurement clamps. Right. So let's have a look at our system. Let's have a look at our switch box here.

**Dave Jones:** We'll expand that out. And we've got like a 60-amp breaker here. This is like the main one for the house. Just like go with these numbers. They're different for different scenarios. But then like inside the switch box, we've also got the 5-kilowatt solar arrays wired inside here as well.

**Dave Jones:** The 3-kilowatt solar arrays. So it's pumping that in. And then you've got this wiring. Once again, it's all in parallel like this. Like goes through to separate breakers. Each power point circuit might be 20 amps, for example. Light circuits might be 8 amps.

**Dave Jones:** You might have like oven, stove, or hot water. You know, different fuses like this for different parts of your circuits. But the problem is all of this stuff in here is like all higgledy-piggledy. It's all kind of like wired together into points and all.

**Dave Jones:** It's a real rat's nest of a thing. That's how it is in my particular fuse box. So unless you had a fuse box that had like one wire coming up. It would have to be one wire coming off here like this. And then going out into all these ones like this.

**Dave Jones:** You would have to like break this off like this instead of separate wires. You'd have to have one wire there which then just went to all the other breakers like this. So that then you could put your current clamp into there. And you could take that reading off there.

**Dave Jones:** But because your power board is like it's got one thing coming in here. And then it's, you know, like because the power can come back in here. And it's all running on the same wires. And it might flow out like that. But it might flow back in.

**Dave Jones:** It's all a mess. You want to measure just your isolated load for your house down here. So the physical construction of your fuse box. And the fact that you have all these different fuses for all these different circuits. And it's all wired in there all together.

**Dave Jones:** And they're effectively like all just in parallel. Then it makes it quite difficult. Not impossible but difficult on lots of fuse boxes. To be able to put one simple current clamp in there. And so that's why it's actually common practice to put the clamp outside of here.

**Dave Jones:** And put it up here like this. So the current clamp for the consumption actually goes on the grid side. Like this. So that goes in there like that. And you would have another one, a second one like this. That then goes down into there like that.

**Dave Jones:** So just from a physical way. From a wiring access point of view. It makes sense to do that. But now you can probably see the problem. What you've got now is a situation where each of these monitoring systems does not know about the other one.

**Dave Jones:** So if you've got your current clamps outside of here. The easiest way to understand it is just to put some numbers in. Let's say that here our house is taking one amp. Okay. And our solar systems here. They're both generating two amps each.

**Dave Jones:** Right. The sun's out. They're both generating two amps. Okay. So we're drawing one amp into the house. And we want to read that as a positive number. We want to read. This solar analytics system wants to read one amp. But what it's actually going to read is the total production from the two different systems.

**Dave Jones:** One of which it doesn't know about. Two amps plus two amps. So there's going to be four amps pushing in this way. Like this. One amps going down here. What's going to happen? Well, you're going to get three amps flowing out like that.

**Dave Jones:** So during the day because your current clamp's there. You're going to actually get a consumption reading of minus three amps. Because the current's flowing out. Not in like you're trying to read. And then magically night falls. This drops to zero. This drops to zero.

**Dave Jones:** And you're drawing. You're still drawing. You're drawing your one amp load. Instantly you're now not reading minus three amps. Because there's nothing flowing back out. You're drawing everything from the grid. You're going to have flowing that way. You're just going to have your one amp.

**Dave Jones:** So it's going to start reading correctly once the sun goes down. Now during the day when you've got your production curve like this of course. You've already got the clamp on your three kilowatt array here. So it knows how much this one's producing.

**Dave Jones:** Right? So it can actually take that. The example that we had before. During the day. Two amps here. Okay so let's add the axes here. Like two amps. Let's say during the day. The three kilowatt system's generating two amps like this. It knows about that.

**Dave Jones:** Because it's measuring. But it doesn't know about this system up here. So the output that this clamp here is measuring is actually four amps. It's not two amps. You've got the extra difference in here. The extra two amps caused by this array here.

**Dave Jones:** Which it doesn't know about. So even though having the current clamp here is a perfectly fine solution. But only if this one doesn't exist. Then it would know how much it's actually producing. And then it can subtract the consumption from that figure. And give you the correct positive figure always.

**Dave Jones:** But it doesn't. Because this is pumping an amp. It's pumping an extra two amps into this system inside here. And likewise for this end phase system here. It's got no idea that this other system here is pumping out two amps here. All it can measure is its own production plus the consumption up here.

**Dave Jones:** So during the day it's going to show negative as well. It's going to show that it's exporting energy when you're actually consuming it. So how do we solve this? Well you can actually solve it simply. By paralleling current transformers. Because what is a current transformer?

**Dave Jones:** It is simply a core like this. Ion core. And it has a bunch of turns on here like this. And it's simply a transformer. And your wire going through like this is one turn. And you've got multiple turns here. So if you've got your one amp flowing through here like this.

**Dave Jones:** You might get one milliamp flowing out of your coil like this. So what you can do is actually wire a second current transformer in parallel with the first one onto your other. Coming from your other production line up here. So this input has two current transformers.

**Dave Jones:** One to measure the production from here. Another to measure the production from here. And in this case if you've got say one amp production here. And you've got two amps production from the other panel. Then you get one milliamp out of here. Let's assume it's you know like a thousand to one turns ratio.

**Dave Jones:** Then you've got two milliamps coming out of here. Because you've got two amps here. So you'll get a total of three milliamps. Which is the total of the production of these two systems. So bingo. Your both systems. The solar analytics and the Enphase will now know about the total production.

**Dave Jones:** So that then you can have the load measurement transformer. Current transformer outside here like this. Because of the limitations of your switch box. And then you're always going to get a positive value. Because it now has the correct value to subtract. You got it?

**Dave Jones:** Clear as mud? I can probably make this easier. But you get the idea. Is that each system doesn't know about the production from the other one. And the way to solve it is to put two current transformers in parallel on each one. Of course if your system had like another input here for production.

**Dave Jones:** And you were able to set it up in software and things like that. Then you could do the same thing. But even if your system only has the one input. And it's not designed to measure multiple arrays. It doesn't matter. Just wire the current transformers in parallel.

**Dave Jones:** So that your system knows about the total consumption. The only downside to this configuration. Is that if you really wanted them to be separate. And you wanted this say the solar analytics to only measure the total production from here. Then there's not really much you can do about it.

**Dave Jones:** You could really accurately measure the production and the consumption at the same time from this isolated system. With the current transformer up here. You would have to move the transformer down to here. You would physically have to have it down there like that.

**Dave Jones:** So anyway as a lot of installations like my one. That's not really practical. So that measurement load transformer has to be on the outside. And it turns out that Enphase do actually know about these sort of installation issues. And if you go over to the system over here.

**Dave Jones:** We can actually look at our. They've now added the photo on there by the way. Which is quite nice. So this is now like a real photo of my roof. With the actual panels installed in there. And I can actually go and like look at individual data and graph.

**Dave Jones:** For each particular one. Here's the temperature for example. Like you can get the temperature. Like that's the temperature of each micro inverter. Not the actual panel. But it's interesting. But anyway if we go over to devices over here. Okay. And we take a look at our Enphase integrated consumption meter.

**Dave Jones:** Right. Which is part of the Envoy thing. Check it out. They've actually got the two configurations here. And the one mine's set up to is the load with solar production. So the Enphase system knows it's supposed to subtract the consumption from the production.

**Dave Jones:** Because they share the same current clamp. And they're on the grid side. But you can actually change it. If you happen to have a panel that allows you to install. The current clamp on the load like this. Then well the load data. Which is the problem that we've been having with this thing.

**Dave Jones:** Whereas it was the load. The actual consumption data. Which was being goofed up and going negative. The production data always worked. It was the load one that was goofing up. Then it knows that there's nothing else it has to compensate. Doesn't have to compensate for the production of these two panels.

**Dave Jones:** But even though the Enphase system has support for this. You saw how it goofed up right at the start. Because there's no way. That the Enphase system can know about the production. From the other system installed. Even if there was like a field for an offset or something.

**Dave Jones:** It's a variable figure. So how does it know? It doesn't. There's no way it can know you've got another solar production system. Panels over here. Actually pushing current back into the grid. Or into the load. Alright so let me show you what's happening on the switchboard here.

**Dave Jones:** And please forgive me this is a bit difficult. I've got three hands to keep the switchboard open unfortunately. And like poke at things at the same time. Anyway here's our main 60/80 amps. I don't know what it actually is. But main breaker. Main fuse coming into the property.

**Dave Jones:** So this is the side that we want to actually put a current clamp on. To measure both the incoming. And like consumption coming in. And also going back to the grid as well. So that needs a current clamp on it. For both the solar analytics system.

**Dave Jones:** Which you've seen before. I've done a whole video on that. And there's the three current clamp inputs down there. And I used to have one channel for the production. I.e. coming from the solar panels. Another for the consumption. I.e. coming into the house.

**Dave Jones:** What we're actually consuming. And then another one that did the air conditioning as well. But I'll explain the air conditioning consumption. But I'll explain that in a minute. And of course we've got the new Enphase. Envoy box up there. And so let's have a look at what's actually going on here.

**Dave Jones:** So let's have a squeeze around the back here. And this is not the best is it? But anyway. As you can see. We've got two current clamps there. There's the solar analytics current clamp. And there's the Enphase current clamp. And both of those are on there.

**Dave Jones:** They are directional. So you have to actually get the direction correct on those. So both of those are measuring the current. Coming into and out of the property. So it depends on which way it flows. As to whether we're consuming power. Or we're actually exporting power to the grid.

**Dave Jones:** And here's the breaker for the main existing three kilowatt system. And if we go around here. You can see how it comes out there. And it's got two. Once again. Two current clamps. That's the bigger one there. Is the new Enphase one. And the smaller one.

**Dave Jones:** Just down in there. Is the solar analytics one. So both systems now. Actually are able to measure the current. They know what the current is. Coming from the existing three kilowatt panel. Okay. I'm trying to keep this panel open with my elbow. But anyway.

**Dave Jones:** You can see another clamp here. This is the solar analytics clamp. And this cable here. Comes from the AC. From the new panels. Okay. So this is what we had to change. This one was actually measuring the air con system before. But I've now sacrificed the measurement of the air con power.

**Dave Jones:** That's just now included in the total power. And I've moved that. To actually on here. To measure. The current coming from. The new five kilowatt system. And I've put that in parallel. You'll notice that. It's got a red. Marker. On there. And the other one.

**Dave Jones:** Down here. Is brown. That's the current. Coming from. The new five kilowatt. System. And I've put that in parallel. You'll notice that. It's got a red. Marker. On there. And the other one. Down here. Is brown. So I've wired. Both of those. In parallel.

**Dave Jones:** In there. On that first. Channel. Up there. And the existing one. On channel two. There. Which actually. Measures. The current. Coming into. And out of the house. Up here. So by putting. The two current clamps. In parallel. On channel one. The solar analytics.

**Dave Jones:** Now knows. The total consumption. Of the entire system. So then it's able to do. The basic addition. And subtraction. Required. To figure out. What is. Like. Being consumed. By the property. And that was. It was totally unknown. Before. So this solar analytics system.

**Dave Jones:** Is now aware. Of both. Production sources. Here. And here. And. Likewise. Up in there. I won't show you. But they're also. Paralleled. Up in there. As well. As I said. There's one here. And you can see. Actually. The arrow there. So it's actually.

**Dave Jones:** Coming out of here. And it's measuring. And it's putting. That effectively. In parallel. With another current clamp. Which is actually. Up in the box. There. Rather than. In the switchboard. But it's doing. Exactly the same thing. So both. The end phase system. And the solar analytics system.

**Dave Jones:** Now. Are aware. Of. The two. Different. Of each other's. Sources. And that's not done. In software. That's done. By simply. Paralleling. Up. The current clamps. Because. The electronics. You can whack them. In parallel. And then. You just get. The combined. Current. Out of both of them.

**Dave Jones:** So there you go. I hope that is clear. As mud. And it is. This is one of. You know. The major issues. With. Having. Two different production. Systems. I.E. Two different solar panel systems. On. Site. Is that they're always going to combine. Like this.

**Dave Jones:** And really. Unless. We totally scrap. This entire switch box. Because. You know. We're going to have to. Disassemble. It. Eventually. If we install a battery system. That's the recommendation. Is to get rid of this ancient thing. Although it's not that ancient. This is.

**Dave Jones:** Mid 80's. This house was built in the mid 80's. So. This is. A typical. Style. That was in. Back then. Well at least in this area. Anyway. And it's. It's not uncommon. At all. But anyway. Just due to the physical wiring configuration of this.

**Dave Jones:** We weren't really able to put the current clamps. On. The. The way we could really put them. Is. Over here. And. Which is the main feed. Coming in. From the street. And. Well. That just. Screws everything up. When one system. Like this one.

**Dave Jones:** Doesn't know about the production from here. And. This one. Doesn't know about the production. From here. So you solve that. By whacking. Transformers in parallel. Neat. And I didn't have to buy a new transformer. I just reused one. From my aircon. So now.

**Dave Jones:** My solar analytics. Can't measure. The aircon separately. But. Anyway. I hope you found that interesting. Because. It. Really is an interesting scenario. Caused by. A. You know. A physical. Like. Space. Wiring. Configuration. Issue. Inside. The switch box. If you had a switch box that.

**Dave Jones:** As I said. Enabled. This. Like. Measurement. Inside. Here. And you could easily put the current transformer there. To measure all these different circuits at once. Then. Well. Everything's hunky dory. But. That's why. Software. Like the Enphase. System. Actually has a specific. Setting. To.

**Dave Jones:** Tell you. Where you want that. Current transformer. Because. This is a known. Issue. In the industry. And. You can fix it. By putting. Transformers in parallel. But there is that slight limitation. That you can't then independently measure things. And. It's all too hard.

**Dave Jones:** So anyway. I hope you found that interesting. If you did. Please give it a big. Thumbs up. As always. Discuss. What you think. And. Subscribe. To. My. Channel. Thank you. And. I'll see you. In the next. Video. Bye. Bye.
