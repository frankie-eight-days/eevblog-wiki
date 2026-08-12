---
video_id: CBD9vwKcvtY
title: EEVblog #1117 - PCB Power Plane Capacitance
url: https://www.youtube.com/watch?v=CBD9vwKcvtY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 38, "3": 64, "4": 79, "5": 94, "6": 110, "7": 132, "8": 149, "9": 166, "10": 183, "11": 205, "12": 229, "13": 248, "14": 267, "15": 282, "16": 297, "17": 315, "18": 331, "19": 351, "20": 368, "21": 387, "22": 411, "23": 430, "24": 449, "25": 467, "26": 483, "27": 499, "28": 519, "29": 536, "30": 554, "31": 573, "32": 592, "33": 610, "34": 631, "35": 654, "36": 667, "37": 682, "38": 702, "39": 713, "40": 735, "41": 750, "42": 770, "43": 789, "44": 808, "45": 820, "46": 837, "47": 850, "48": 868, "49": 886, "50": 904, "51": 917, "52": 932, "53": 946, "54": 968, "55": 987, "56": 1011, "57": 1036, "58": 1055, "59": 1070, "60": 1090, "61": 1109, "62": 1131, "63": 1145, "64": 1166, "65": 1182, "66": 1202, "67": 1220, "68": 1234, "69": 1252, "70": 1277, "71": 1296, "72": 1316, "73": 1337, "74": 1353, "75": 1369, "76": 1387, "77": 1403, "78": 1421, "79": 1437, "80": 1453, "81": 1471, "82": 1492, "83": 1509, "84": 1526, "85": 1546, "86": 1561, "87": 1582, "88": 1599, "89": 1615, "90": 1629, "91": 1646, "92": 1663, "93": 1690, "94": 1706, "95": 1727, "96": 1746, "97": 1762, "98": 1778, "99": 1793, "100": 1804, "101": 1839}
---

**Dave Jones:** Hi, in a second channel video, which I'll link in down below and at the end if you haven't seen it, and I highly recommend you subscribe to EEVblog2, there's tons of videos that I put over there, hundreds and hundreds of videos that sort of don't make it to the main channel.

**Dave Jones:** Anyway, we took a look at this super low-cost JLC PCB. It was $72 delivered for a four-layer board, five of them. Absolutely insane. Anyway, somebody asked the very good question, hey, what about the internal ground planes inside this thing? And we'll take a look at this in a minute up close under the microscope.

**Dave Jones:** There's actually four layers on this board. I've got an internal ground and power plane covering this entire board. And hey, how effective is the capacitance between those? Because the capacitor, remember, is just two metal plates separated by a dielectric material. The dielectric material in this case is the epoxy resin fiberglass inside this thing.

**Dave Jones:** But, you know, I'm sure I've mentioned this in previous videos on, you know, controlled impedance tracers and all sorts of other stuff. I'll link them in if I can find them. In that, if you put ground and power, for example, in this case ground and 5 volts,

**Dave Jones:** inside those inner layers which go all over the board like this, that can actually be a decoupling capacitor that goes across effectively your entire board. But how effective is it? Can we actually measure the capacitance in this power plane? Yes, we can measure the capacitance.

**Dave Jones:** Let's do that right now. But we can do more than that. I've got the probes connected into just one of the bypass capacitors here. Doesn't really matter which one, and we'll test that. We'll actually verify that later on. But let's have a look.

**Dave Jones:** We've got a nominal capacitance here of, let's call that bang on 2 nanofarads. And if we actually change, that's at 1 kilohertz. If we change the test frequency here, 10 kilohertz, it's basically the same thing. Doesn't change much. So at 100 kilohertz, you know, 1.91 nanofarads.

**Dave Jones:** So you can see that it's, you know, even at 100 hertz, there we go, 2 nanofarads. So it's quite even across the board. And the dissipation factor, look at that .005, the lower value, the better at the different frequencies. That's actually pretty, that's a pretty good capacitor, isn't it?

**Dave Jones:** It's not too shabby at all. So there you go, somebody asked 2 nanofarads capacitance on this particular board. But it's going to depend upon the stack-up of the board. And as it so happens, so I've actually ground down this board, and we can see the internal layers.

**Dave Jones:** Let's go to the Mantis microscope, have a look. But you can see that there's an internal layer up there, but you can see the top copper layer in there, our internal copper, and the bottom internal copper along there. And of course then you'll have the outer copper layers, top and bottom.

**Dave Jones:** And you can see that the internal copper layers are very close to the outside copper layers of the board. And these are very thin prepregs, they're called. They get these from the raw PCB supplies. They don't make them themselves, they order them from various companies

**Dave Jones:** who manufacture these prepreg and core layers. So they actually get two double-sided boards that are incredibly thin, and then they glue together what's called a core in there. And the core in this case, because this is a 1.6mm outer thickness board, then the internal core will be typically about 40 thou,

**Dave Jones:** or 1mm thickness. And then they glue the two-layer boards, top and bottom, to those as part of the manufacturing process. So the problem with this is that having a 1mm core in there, there's actually quite a big gap between the internal copper layers.

**Dave Jones:** So the bigger the distance between two plates of a capacitor, the lower the capacitor, and the less effective it actually is. So in this particular stack-up that you get, and you don't have any choice in this, because when you order a, like a really cheap, you know, four-layer board like this,

**Dave Jones:** you get whatever stack-up the manufacturer gives you. But you can actually order your own stack-up. It's just like a more custom job, and they'll charge you more for it. But you can actually do that. You can specify. So instead of those copper layers being, like, so far apart like that,

**Dave Jones:** and near the top and bottom surfaces, you can say, hey, I want a two-layer board in the middle, please, a very thin prepreg in the middle, so that my power planes are as close as physically possible together, so that you get increased capacitance.

**Dave Jones:** You get a greater effective capacitance that way. But the trade-off is, well, the good thing about the one that we've got here is that having the copper, internal copper, as close as possible to the top and bottom layers, it's easier and more effective to do a, to route controlled impedance

**Dave Jones:** traces on the board. And I'm sure I've done a video somewhere on controlled impedance traces. But the thing with this is that, well, you can do it the other way. You can say, hey, I want those two layers together in the middle to give me a greater plane capacitance,

**Dave Jones:** because that is a more important parameter to me. But then, because the internal distance between the internal, the thickness between the internal plane and the top and bottom signal layers is greater, you have a harder time doing those controlled impedance traces. For a given controlled, like, say you want to do a 50-ohm transmission line,

**Dave Jones:** you need a much wider trace the greater the thickness of your material between the signal layer and the ground plane to do a microstrip. For example. So it's all a trade-off. If you wanted the best of both worlds in this case, you would have to go to a 6-layer board.

**Dave Jones:** Now let's actually try a different board. Let's get this Altium Nanoboard 2, which is an 8-layer board. So once again, I've ground away the layers in here. Let's just pick one of the ones, which I believe is the 3.3 volt rail. So it's going to have a rather large ground plane on here.

**Dave Jones:** We dedicated the ground planes to the various rails, but 13.5 nanofarads, because they're closer together. And check it out, this one's actually much more interesting than we had before. You can actually see the 8 layers in there, count them, and you can see how they actually pull back from the edges,

**Dave Jones:** and you can actually see the plating on the through-hole, you know, the main mounting hole there. So that really is quite fascinating, but you can see how they're actually made up of little individual pairs. As I said, these are bought bare as, like, 2-layer boards,

**Dave Jones:** very incredibly thin ones. Then they just glue them together with these various thickness cores to make up your stack. That's why it's called a stack-up, to stack all the layers together to give you your final 1.6mm board. And the exact thickness of the actual prepreg and cores used

**Dave Jones:** depends upon what outer diameter board you want, you know, 1.6 nominal, but the 1.6 may include the copper or may not, and also the copper thickness, the copper weighting, whether you want 1 oz, 1.5 oz, 2 oz, whatever it is, that increases the thickness of the copper.

**Dave Jones:** That all adds up, so they've got to adjust for that to give you a particular stack-up. And you can, as I said, you can actually specify this with the manufacturer. You can go, hey, I want this specific thickness with these prepregs, and you can order specific material.

**Dave Jones:** You might order, like, a Rogers brand material, for example, because you've got the data sheet for it, it has the proper controlled dielectric you need and everything else. So you can specify all this sort of stuff until the cows come home, and you can see that the internal cores are much closer together.

**Dave Jones:** So using, you know, a basic capacitor manufacturing formula, you know, it's basically, capacitance is the square area times the distance between those particular plates. So I don't remember which actual pair inside there is the rail that we're actually measuring, but it's one of those,

**Dave Jones:** and they're going to be very close together to get that huge capacitance. But hey, we can do more than just measure the capacitance of this thing. We can get the full impedance plot versus frequency, because we have the Bode 100 analyzer, which you've seen in previous videos.

**Dave Jones:** We'll just use the jig, and we'll just hook some wires over to the ground plane, and we can calibrate out the wires, and we'll get a full impedance versus frequency plot, and get the capacitance as well, versus frequency. Let's do it. Okay, so let's use the analyzer software

**Dave Jones:** when we want the impedance measurement here. We're using the test jig that we used for, you know, with the little slots. So we can actually measure some real capacitors as well, and we'll compare the ground plane of the two PCBs with some real bypass capacitors.

**Dave Jones:** So let's do it. So what we want is 100 hertz to 50 meg. No worries. Let's get a lot of data points. Let's get 800, 13 dB. Let's lower our receiver bandwidth, just because we can. And we have to do the calibration first.

**Dave Jones:** So let's go full, perform new calibration. Now, open short load. We've got, you've seen this, we have a short and a load thing. It's got a 50 ohm resistor on it. So we'll do the open compensation. You have to do this to get rid of, to compensate for the test leads

**Dave Jones:** and the test jig and the contacts and everything else. We'll do the capacitors first. So open, short, and load. Done. Sweet. And now, we can measure some real capacitors. So first up, we'll get a 2.2 nanofarad ceramic, which is close to the nominal 2 nanofarads that we measured.

**Dave Jones:** And so let's whack that in. And let's give it a boil. What we want, though, is admittance here. And we want the parallel capacitance there. So let's run that. Single sweep. And it'll scale properly. We can, well, we can scale it now. Now, of course, the impedance, it's linear with frequency like this.

**Dave Jones:** And then there'll be a resonant point, and it'll go back up. It'll go up, like that. But in this particular case, because it's such a small value, it'll probably be beyond the 50 megahertz. So we probably won't see it go back up. Whoa!

**Dave Jones:** You can just sort of see it start to tail off there. So it would have gone down and then back up like that. But we can get different values to show that. So we can just optimize that. There we go. And then we can get our cursor here.

**Dave Jones:** And what's the capacitance? You can see it there, up the top there. Those values change in 2.3 nanofarads. There you go. And, of course, that, it drops off like at higher, at this frequency. It really starts to change. You can start to see that the lead inductance and the other parasitics of the capacitor

**Dave Jones:** are starting to change that. And the capacitance is going up, and up, and up, and up, and up, and up, and up, and up, up, and up. Well, it's not been going up by much, 2.9. But you can see that it varies with frequency.

**Dave Jones:** All right, I'll save that one. There we go. We've got a 100N film capacitor. Let's whack that in. Give it a burl. Single shot. Here we go. Of course, it's a different impedance. You'd expect that. But the, uh, what, we'll turn off the, well, we can leave, we can leave the other one there.

**Dave Jones:** No, we'll turn it off. And here we go. The scale, we'll optimize it in a second. But we should see, this one should be within the range. Will it come back up? Boom. Optimize. There we go. There we go. There's our nice response.

**Dave Jones:** There's our resonant peak right down there at about, what, uh, 8.5 MHz or thereabouts. And you can see that, uh, the capacitance is, uh, near enough to 100N, 96N, like that. It's a bit of a, bit of a peak there where it jumps up to 140.

**Dave Jones:** And then it goes negative. But don't worry about that. That's just a, a negative in quote marks. That's a, uh, quirk of the, uh, calculation in this case. But, uh, yeah. There's our resonant peak. All right. Now we've got a, uh, ceramic, 100N, instead of the film.

**Dave Jones:** Measure that one. Just so that we have some baselines to compare, baseline, uh, frequency response impedance curves to compare against the, uh, ground plane. You can see that it's very similar. Slightly higher in capacitance. But it should, maybe, will it have the same resonant point?

**Dave Jones:** We, we just don't know. Um, it's not based on the capacitance. It's based on the lead frame and everything else. See, that one's a bit, that one's a bit peakier. So, there you go. It's got a, it's got a sharper dip down here.

**Dave Jones:** That's probably due to the longer, or maybe not due to the longer leads on that. Meh, hard to tell. Anyway, the parasitics of that capacitor, uh, that, uh, that has a sharper peak like that. And it's a slightly different, uh, frequency, you know, like 7MHz or something like that.

**Dave Jones:** And we've got another one. Um, just another lead. I won't bother doing, like, a surface mount one. There's no point. We just want to get a couple of caps. Twiddle your thumbs. Of course, you know, you can get more data points and you can lower your receiver bandwidth

**Dave Jones:** and take, get more resolution and take more time and stuff like this. But they, you know, this is good enough for our purposes. Similar, whoa! A different response there again. So, there you go. You can see the, uh, different, this is the yellow ceramic.

**Dave Jones:** Highly technical, uh, description. The yellow one versus the orange. These come from my junk bin. Um, film cap and the, uh, 2N2 ceramic. So, there you go. We've got a nice little collection of responses. Now let's go to the ground plane. Now, what I'm going to have to do, because I'm going to use these leads

**Dave Jones:** to, uh, jump over from the test jig over to the board. They've got inductance in them. They're inductors. Remember, every piece of wire, every trace on a PCB, everything, every conductor has inductance in some way, shape, or form. Even the, uh, ground plane has spread inductance.

**Dave Jones:** So, um, yeah, I'll recalibrate, open short load at the end of these test leads. Just so we, you know, take those out. Because, you know, these are equivalent to having long leads on your ceramic like this, and really, like, sticking out of your board.

**Dave Jones:** So, you know, we just want to get a bit better. Okay, so what I'm going to do is put it in one of the bypass capacitor holes down here, down near the edge of the board. And we will do another test, which is not near the edge of the board,

**Dave Jones:** just to show that there will be a little difference. You'd expect a little difference, but not much. The ground plane is generally the ground plane. It's just, like, one big capacitor. There'll be, you know, subtleties in there, but, like, not much at all.

**Dave Jones:** So, remember this measured about, uh, 2 nanofarads? So here we go. We've got it in there. And I've done the open short load compensation with the leads in place. Let's go. Here we go. And the impedance is going to be different. Oh, yeah, here it comes, here it comes, here it comes.

**Dave Jones:** Will we get it within the frequency range? Will it, uh, will the resonant point be within there? Let's give it a burl. Come on. Hey, there we go, it's going back up. Look at that. Has a nice response. Wow, that's a real, that is really good.

**Dave Jones:** That is a superb capacitor. It, because you ideally, you want, you don't want a really sharp resonant point. You want a, you know, a broad range like that. So, that is, that is superb. And it was, where's our cursor? There we go. So, sorry, I'll turn these off, because that's a bit, that's a bit messy.

**Dave Jones:** The comparison. And we'll optimize, yeah, here we go. So, what's our capacitance? There we go, 1.8 nanofarads, 1.8, 1.85, and then it drops off 1.7, and then it starts to, uh, really taper off down there. And, boom, she's gone-ski at, uh, you know, 50 megahertz.

**Dave Jones:** But, that's really interesting, you know, resonant frequency's about 14 points, you know, 15 megs, something like that. But it's a really broad response, especially compared to, let's, well, compared to the 2N2, let's, you know, there's the 2N2, uh, ceramic we had before. Unfortunately, we don't have the frequency range,

**Dave Jones:** but it's gonna have a dip similar to the other ones we've seen here. But let's look at a 100N film cap. Well, let's look at that one. It's a nice dark color. There we go. There we go. And, look, it's a really sharp, uh, resonant peak there,

**Dave Jones:** whereas the ground plane is really, and quite an awesome, But that's what you'd expect, because a ground plane is just two sheets of copper separated by a dielectric, just like a capacitor. It is a capacitor. Okay, so let's see if it makes a difference going towards the middle of the PCB.

**Dave Jones:** Oh, sorry, if you can't see this. I'd expect to see subtle differences, but not big ones. Because it shouldn't matter, because the interconnect, you're just looking at, like, edge effects of the plane and stuff like that. So, uh, but the actual connection is the same.

**Dave Jones:** So it shouldn't actually matter. So, here we go. Boom. It's almost, look at that. It's almost identical, but we could see a difference in the resonant peak down here, perhaps. But I doubt it. Not with that broad response. If we had a nice sharp response, a really sharp peaky response,

**Dave Jones:** nah. Nah. It's identical. There you go. Makes no difference where you actually connect the ground plane. It's exactly the same. Alright, we're going to do the Altium ground plane now, and I've got to hold this with my fingers, but trust me, I'm not touching it,

**Dave Jones:** and it doesn't make a difference. So let's run that. Remember this one was, what, 13 nanofarads? Something like that, was it? There we go. This one, once again, it's going to be an excellent... Sorry, I screwed that up. Let's do it again. Here we go.

**Dave Jones:** And, of course, it's going to be a higher capacitance. You can see it up there. Yeah, 13 point something. Right? 13 odd nanofarads. And where will our resonant point be? Will it be here? Will it have a similar... Oh, yeah, there we go.

**Dave Jones:** Look at that. It's even broader. It's a broader response. Wow. That's really great. Look at that. Compared to the light blue. Um, the... with the other one. So, well, I don't know, they're very similar if you move it, and, yeah, you know, similar anyway.

**Dave Jones:** Nice broad shape. They're beautiful capacitors, ground planes. Fantastic. Winner, winner, chicken dinner. So whilst a ground plane does have that beautiful response like that, um, it doesn't, you know, it's not a real peaky response, which can get you in trouble sometimes with, you know,

**Dave Jones:** if you have an LC resonance thing, you don't... you can really come a gutser. And it's not just ground planes, by the way. It's, you know, like just regular bypass capacitors. I've mentioned this before, I'm sure, is that, you know, if your thing is switching at the correct frequency,

**Dave Jones:** if your circuit's switching at just the right resonant frequency and you combine that with the inductance of your tracers with the impedance of the resonant point of your bypass capacitor, you're... you can really screw things up, okay? So, actually, so that's one of the dangers of putting

**Dave Jones:** too many bypass capacitors on there of different values is you might potentially hit a resonant point at some switching frequency and that can just cause your circuit to go completely screwy. Anyway, the impedance of... have a look at the maroon-colored one here, and its impedance is down in the, you know, it's like tens of milliohms,

**Dave Jones:** stuff like that, whereas the impedance of the ground plane is in the order of, like, you know, 6 ohms for the... something like that. What is it? Yeah, 4.6 ohms there for that, and maybe, like, 11 ohms or something for the other Gigatron board.

**Dave Jones:** So, you know, they're not as lower impedance. Whilst they have an excellent capacitive response, their impedance just isn't as low at the certain frequencies. So, you know, they're not as good there. And there's the film cap that goes down to 100 milliohms impedance.

**Dave Jones:** So, you know, and there's the 2N2 ceramic. Yeah, that one's lower as well. So the ground planes aren't particularly low impedance, but they do have a proper capacitive response, as you'd expect. Now, I've just spent about 20 minutes showing you that internal layers of a PCB actually work as a capacitor.

**Dave Jones:** They are actually a capacitor, and in theory you might think that they are low inductance because they're a ground plane, right? They don't have, like, little leads coming out of them and stuff like that. And that's kind of, sort of true, but when you put a chip on it

**Dave Jones:** that you actually want to bypass, that's where the problems start coming in. So you might have this massive ground plane that's, like, this big, like this, and it's just solid copper all over it, and it's one big capacitor. Yeah, it might be tens of nanofarads that we saw before,

**Dave Jones:** but can that actually replace an actual 10 nanofarad bypass capacitor? The answer is no, and it's obvious why you actually, if you actually think about it. When you, if you've got a large plane like this, the capacitance is spread over the whole surface of it.

**Dave Jones:** So that's the whole, you know, 10, 20 nanofarads. If you're, but you're looking at a little chip which wants to bypass between the, right at this point, between the positive and the negative rail, power and ground, it needs to do it at that point.

**Dave Jones:** It doesn't want to have to go right across the board to get the capacitance. So if you're trying to bypass one pin, which is one little point like this, on an otherwise big board, then the amount of actual capacitance in that little area is actually rather small.

**Dave Jones:** It drops away at a bugger all. So it doesn't actually retain much charge, which is what a bypass capacitor does. It holds charge so that when a digital circuit switches suddenly really fast, it can take that gulp of current from, directly from that little bypass,

**Dave Jones:** that little source of energy, which is the bypass capacitor right there. So having a capacitor that's this big doesn't really help you because that one point source, in effect, which might be low impedance, technically, from that, you know, just at that one point,

**Dave Jones:** if you want to take the whole capacitance right over the whole thing, then it's got to spread out across there, and therefore the inductance spreads out. And it's actually a phenomenon called inductance spreading that spreads across the ground plane, which makes a ground plane,

**Dave Jones:** or power planes, just rather ineffective as bypass capacitors. Because that inductance spreading across the ground plane, jazz hands, spreads across, then that tends to dominate over the small amount of capacitance that you're talking about at that one little point source in your board.

**Dave Jones:** Anyway, if you go to, like, application notes for FPGAs, like this Xilinx one, I'll link it in down below. It's very comprehensive, you know, it goes into all sorts of stuff, you know, the equivalent circuit of a capacitor and the impedance response curve that we had,

**Dave Jones:** and how vias can make a huge difference on, you know, the inductance of vias makes a massive difference, and all that sort of stuff, and good and bad techniques. And they actually talk about plane inductance here, and they talk about power plane inductance spreading in particular.

**Dave Jones:** Inductance per, you know, picohenries per square, for example, and, you know, capacitance per square, and it just spreads across. And whilst it does something, it's really not a replacement for, like, a one nanofarad, for example, and these application notes will often show you

**Dave Jones:** that you put a one microfarad, a 100N, a 10N, and a 1N, all in parallel across there. And, you know, they give various reasons for that, and I've done a video, and we can go down here, it's the whole idea is that you spread,

**Dave Jones:** you create, as I said, create a larger frequency band of lower impedance. So when you put the multiple capacitors in parallel, but unfortunately the ground plane is not a replacement for one of those smaller capacitor values due to inductance spreading and the big nature of the power plane,

**Dave Jones:** the big nature of the plate of the capacitor. But having said that power planes aren't really effective as bypass capacitors, that's not a reason not to keep them closely spaced, and one on top of the other, just like we saw before, with a thickness as minimum as possible.

**Dave Jones:** Because if you, when you keep them close together like that, you get a small little maybe benefit from the capacitance, but that's not the reason you do it. You keep them like that so that the effective inductance, loop inductance, and plane inductance, and everything else is the lowest possible.

**Dave Jones:** So you don't want to just go, oh, power planes are useless as bypass capacitors, so therefore I'll put one on the top layer and one right on the bottom layer and just separate them by the biggest distance. No, you're creating more problems. So you do actually get benefits, but in other ways,

**Dave Jones:** by actually keeping them as close together as possible and actually having them on the same prepreg inside. So you have ground and power on a small little prepreg. That's where you get the most benefit. And then, of course, you've got the inductance dropping the via down

**Dave Jones:** from the top and bottom layers through to the ground and power planes. But having the planes together is a greater overall benefit than not. And there's actually a good paper on this by Steve Weir. It was an old DesignCon paper. I'll link it in down below.

**Dave Jones:** It's from TerraSpeed. And it actually talks about and actually models and demonstrates built practical examples of why spreading inductance doesn't work. And he actually sets up experiments and that sort of stuff. I won't go into a huge amount of detail in it, but he basically builds up two different boards and things like that

**Dave Jones:** and probes them and all that sort of stuff. And he also makes the claim that it, and provides data to back it up, that it's not necessarily the best thing to do, to add the multiple values of capacitor in parallel, like the one mic, the 100n, the 10n.

**Dave Jones:** You can actually get away with the same value in parallel just in multiple locations and stuff like that. And, you know, that's going to be true and not true, depending on circumstances. There's so many different things going on here that it really is difficult to model and actually measure,

**Dave Jones:** practically measure this sort of stuff. So a lot of bypass engineering is like, just like follow the best practice and cross your fingers and hope nothing hits some resonant peak or something like that. Because it's not that you can go, oh, my output is going to switch at precisely 20.2 megahertz,

**Dave Jones:** therefore I have to select this capacitor to avoid this and do this. Maybe, in theory, you know, if you're going to Pluto, you might have the time and effort to be able to, you know, analyze and model and build and simulate and measure that kind of stuff.

**Dave Jones:** But in most cases, you know, you just whack multiple different values in parallel. Follow the application note from, you know, Xilinx or Altera or whoever it is and just, you know, she'll be right. Oh, look, I'm big. Anyway, I hope you found that interesting.

**Dave Jones:** It is a fascinating subject. And you can go down the rabbit hole on this one if you really want to. It really is quite a complex subject, just bypassing stuff. You know, you have a bypass capacitor. It stores energy at a point and a point.

**Dave Jones:** No, there's a lot more to it than that, if you really want to get into it. But anyway, I hope you did find that interesting. If you did, please give it a big thumbs up. As always, you can discuss in YouTube comments down below

**Dave Jones:** or over on EEVblog forum. And I've mentioned it before, but I'll mention it again. My patrons often get to see videos including this one early. So if you want to do that and want to support me on Patreon, link is down below. Catch you next time.

**Dave Jones:** Thank you.
