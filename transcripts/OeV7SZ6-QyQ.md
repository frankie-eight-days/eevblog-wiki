---
video_id: OeV7SZ6-QyQ
title: EEVblog 1559 - PCB Design: Trace Current Rating
url: https://www.youtube.com/watch?v=OeV7SZ6-QyQ
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 28, "3": 40, "4": 52, "5": 61, "6": 80, "7": 91, "8": 106, "9": 120, "10": 129, "11": 139, "12": 151, "13": 161, "14": 171, "15": 179, "16": 188, "17": 198, "18": 213, "19": 225, "20": 245, "21": 258, "22": 267, "23": 277, "24": 288, "25": 299, "26": 315, "27": 335, "28": 342, "29": 353, "30": 365, "31": 375, "32": 389, "33": 399, "34": 408, "35": 416, "36": 430, "37": 443, "38": 457, "39": 468, "40": 478, "41": 489, "42": 503, "43": 512, "44": 524, "45": 536, "46": 546, "47": 555, "48": 566, "49": 576, "50": 588, "51": 599, "52": 611, "53": 621, "54": 631, "55": 642, "56": 666, "57": 675, "58": 687, "59": 695, "60": 703, "61": 720, "62": 729, "63": 741, "64": 753, "65": 764, "66": 776, "67": 789, "68": 798, "69": 809, "70": 818, "71": 837, "72": 851, "73": 862, "74": 883, "75": 895, "76": 904, "77": 916, "78": 931, "79": 947, "80": 956, "81": 967, "82": 984, "83": 1002, "84": 1019, "85": 1033, "86": 1040, "87": 1052, "88": 1063, "89": 1074, "90": 1096, "91": 1108, "92": 1128, "93": 1142, "94": 1152, "95": 1164, "96": 1173, "97": 1184, "98": 1197, "99": 1207, "100": 1224, "101": 1239, "102": 1251, "103": 1263, "104": 1275, "105": 1287, "106": 1297, "107": 1305, "108": 1316, "109": 1327, "110": 1337, "111": 1348, "112": 1361, "113": 1372, "114": 1384, "115": 1396, "116": 1407, "117": 1425, "118": 1445, "119": 1453, "120": 1463, "121": 1477, "122": 1488, "123": 1505, "124": 1514, "125": 1536, "126": 1549, "127": 1560, "128": 1569, "129": 1583, "130": 1593, "131": 1604, "132": 1619, "133": 1626, "134": 1635, "135": 1652, "136": 1663, "137": 1677, "138": 1699, "139": 1707, "140": 1721, "141": 1733, "142": 1745, "143": 1754, "144": 1762, "145": 1774}
---

**Dave Jones:** Hi, it's Twitter question time. Let me know, leave it down in the comments down below if you want me to do more of these. I do, of course. Follow me on Twitter, none of that X rubbish, follow me on Twitter, and you can ask me questions anytime, and I'm always answering questions there, but I thought this one might just make an interesting video.

**Dave Jones:** This I have covered it in bits and pieces in previous videos, but we'll go into it a little bit more here. It's a simple question. Abhinav, sorry I'm butchering that pronunciation.

**Dave Jones:** I'm uh sure, but he asks uh he's designing a PCB trace for a 70 to 80 amp, so a substantial amount of current. How should I design the trace from the connectors to a MOSFET uh device for this current rating?

**Dave Jones:** Is it possible to use only one layer? And it's a through-hole uh device. So, we won't go go into like the routing and all that. So, is it possible using only one layer?

**Dave Jones:** So, I presume that he's asking that because well, he's got other routing uh constrains and doesn't want to chew up the bottom or internal uh planes, assuming it's even a multi-layer board.

**Dave Jones:** It might just be a double-sided, don't know, cuz it is a through-hole uh device. So, could only be a double-sided board, but you know, you don't know. Anyway, the first thing you want to do is you want to um basically, when you pass current through any uh conductor, of course, copper is on the PCB is a conductor, and of course, Ohm's law, if you got resistance, yeah, at a certain

**Dave Jones:** current, it's going to drop uh voltage using uh Ohm's law. So, that could be a problem, but we won't go into the design aspects of like the voltage drop and things like that, but that is one of the things that you have to consider in the design.

**Dave Jones:** But, also uh the power dissipation is going to heat up, I squared R losses. Um I, you know, the current squared times the resistance of uh the trace, and you can have a big giant plane, it's still going to have resistance on it, and you have to sort of like take that into account.

**Dave Jones:** One of the things you really need to do uh with this is like there's a few rule-of-thumb things, and you can have little, you know, simple charts and stuff like that, which give you a rough, uh, trace diameter for a certain current and stuff like that.

**Dave Jones:** There's much more engineering and science actually behind it. So, you really need, at at a minimum, you need a, uh, PCB trace calculator. And, uh, the one I use here, I'll show you.

**Dave Jones:** It's, uh, Saturn PCB design. You've It's free. You can just download it. I'll leave a link, uh, down below. And it's got all sorts of stuff. Like, it it's got tons of stuff.

**Dave Jones:** I won't go into all the stuff it's got. But, one of the things it does is it's got conductor properties here. So, we can put in the various parameters, uh, up here, and then it will give us the conductor DC resistance, how much resistance that trace has got.

**Dave Jones:** So, we can use Ohm's law and then we can calculate the, uh, voltage Well, no, it already calculates the voltage drop for us. There it is. Um, and the maximum conductor current that it's capable of.

**Dave Jones:** But, there's a lot of stuff that goes into this. So, let's have a look. There are three major things that dictate how much uh, maximum current a particular PCB trace can handle.

**Dave Jones:** One, of course, is the diameter of the trace. Now, obviously, got a little tiny thin, you know, 10 thou trace, uh, it's not going to, uh, carry much current at all.

**Dave Jones:** So, you thicker, the wider trace you make it, the more current because it's going to lower the resistance. It's going to have le- less I squared losses. It's going to It's not going to heat up, uh, as much.

**Dave Jones:** So, that's the first thing. But, not all copper is the same. So, the second thing is the thickness of the copper cuz PCB comes in different copper thicknesses. And none of this, uh, metric rubbish.

**Dave Jones:** We want imperial for this, um, because we work in imperial. And when you order your, uh, PCB from manufacturer, you should be specifying the copper thickness of every layer in your PCB stack up.

**Dave Jones:** And I've done videos on stack up in, you know, not specifically on that, but you've covered it in previous videos. But, basically, every piece of copper in your like, you know, if it's an eight-layer board, you've got eight layers of copper in there.

**Dave Jones:** And you can individually specify the thickness of each layer and the copper in your PCB stack up, it's called. So, if you've got If you want to run like real heavy current on one particular plane or one particular layer of your board, then you can specify, "Okay, I want much thicker copper on that layer." And the manufacturer will do that for you.

**Dave Jones:** And if you don't specify any of this, they'll just give you the standard stack-up, which might be 1 oz copper, which is 35 micron thickness. You can change it over to metric there it is there.

**Dave Jones:** 1 oz copper is your standard thickness, but if you've got a multi-layer board, they'll often use half oz thick or maybe even quarter oz thick copper on those inner layers.

**Dave Jones:** So, if you don't specify it, the manufacturer is just pot luck what you actually get. You won't get more than 1 oz because, you know, copper's expensive, right? And they want to keep the cost low.

**Dave Jones:** So, your standard board, you won't get any more thickness than 1 oz copper on your on any of the layers on your board if unless you specifically ask for it.

**Dave Jones:** Then you might jump up to Usually, you'd jump up to 2 oz for that. So, it's twice as thick. So, it's going to be lower resistance. And you know, like once you get to like four, five, something like that, that's really thick as, right?

**Dave Jones:** Really thick and expensive copper. And you do that for like really exotic, you know, applications. If you want really high current board, but it's got to be really dense, for example, and you can't make your trace really thick cuz you got real tight routing in there and stuff like that, you might have to go to 4 or 5 oz copper.

**Dave Jones:** It could even get an exotic one even thicker than that. And the third parameter, which is not as important, but it matters, is whether or not the copper's on the top external layer of the PCB, so the top or the bottom, or whether it's in the internal layers of the PCB cuz they'll have different thermal properties.

**Dave Jones:** Because if your conductor is dissipating heat and it's wedged in the middle of the sandwiched in the middle of the board like this, fiberglass is a pretty good insulator, right?

**Dave Jones:** So, it the heat can't get out. So, the temperature will rise like it'll that heat will get trapped. It can't escape. So, it'll get hotter, which will increase its resistance and right?

**Dave Jones:** Well, it doesn't run away, but right? It's It's going to get higher resistance the hotter it gets. Whereas, the outer layers, they're going to cool more easily. And also, the solder mask over the traces can make a difference as well.

**Dave Jones:** If you've got solder mask over there, that's an insulative layer on your copper. So, that can matter as well. But generally, you know, unless you're really getting down to the nuts and bolts of it.

**Dave Jones:** Yeah, you know, there's only two major ones. The thickness of the copper thickness of the copper and the width of the copper. But the layer stack matters, too. But it's not like a copper trace just suddenly bursts open and catches on fire or breaks, you know?

**Dave Jones:** Because you can actually use a PCB as a fuse. A PCB trace is a fuse. And there's a bit of art and science that I goes into that. I might have even covered that in a video somewhere.

**Dave Jones:** Can't really remember. It doesn't just suddenly magically stop carrying current. It just gets hotter and hotter and it might delaminate from the board. It might, you know, it glows red hot or whatever.

**Dave Jones:** Right? So, it's all about the temperature rise that you're willing to tolerate in your design. Now, you can see here this is one of the parameters. 20° C temperature rise.

**Dave Jones:** Me personally, I prefer to put a 10° C temperature rise if I'm doing these calculations, but it's There's no reason for that. It's just my own personal rule of thumb for a 10° C temperature rise.

**Dave Jones:** And then there's ambient temperature as well. If you want to get really fancy pantsy, okay? So, let's actually start using this to do a basic thing. Let's say we've got standard 1 oz copper here, okay?

**Dave Jones:** And we've got no plating, okay? The plating is another thing that matters. It's not only the solder mask over the top that can impact, but most boards are usually solder mask over bare copper or SMoBC.

**Dave Jones:** So, you can just say bare PCB like that, okay? And we're going to use external layer. So, we've got an external PCB layer here. And uh we've got a bare PCB which will have the uh solder mask over the top.

**Dave Jones:** Uh it doesn't really matter whether it has the solder mask. In fact, they don't even have the solder mask in this calculation, but technically can make a little teensy bit of difference.

**Dave Jones:** So, 1 oz copper and 10 mils is ridiculous, right? So, let's go for 100 thou. Right, 100 thou trace. 100 mil trace. Not that millimeter rubbish. And the conductor length here um we don't know.

**Dave Jones:** So, it depends on your particular layouts. So, the total resistance will depend on the conductor length uh of course. And then uh that will determine the voltage drop which you're willing to tolerate cuz that might be part of your electrical design rather than the third You've got two issues here.

**Dave Jones:** You've got electrical and thermal um as well. And you might even have high frequency stuff. That's why they've got like skin depth over here and skin skin depth uh percentage.

**Dave Jones:** Anyway, we won't definitely won't go into that. We're talking about like DC current. So, 100 mils plain present no hollow conductors doesn't matter uh for purposes here. Ambient temperature, we're just going to run that.

**Dave Jones:** It's an external layer. So, let's solve that, okay? There you go. It's 5 milliohms there for a 100 mil wide trace. And that can do a nominal 3.28 amps.

**Dave Jones:** So, generally at So, if you try to put 3. uh 3 amps through a 100 mil wide conductor, and we can convert that to metric for you metric fanboys, 2.54 millimeters.

**Dave Jones:** There you go. It's going to at 3.3 amps it's going to rise 10° C if it's on the outside of your board. Is that acceptable to you? I don't know, right?

**Dave Jones:** So, we're talking 80 amps here, okay? 80 What was it? 70 to 80? 70 and 80. So, let let's take 80 amps metric, right? 25 mm wide trace, right?

**Dave Jones:** A 1-in trace. Let's actually solve that. With 1 oz copper is only going to do 12.6 amps. So, we're going to have to let's double it to 2 oz copper.

**Dave Jones:** Okay, so twice as thick copper. So, we go from 12.67 to 20.9 there. It's not quite doubling. If we go a four again, will it get to 40? No, it gets to 34, right?

**Dave Jones:** It starts to limit it. So, you can see that you got like really thick copper here for a 1-in wide trace. Okay? So, this is getting quite an issue.

**Dave Jones:** So, he talks about like putting it on a single layer. You're really starting to push it like 4-oz copper. That's pretty specialized. You're going to have some PCB house cheap PCB houses just won't do that.

**Dave Jones:** And you won't get this on your regular, you know, your $5 prototype board, right? You're not going to get that. They might give you 1/2 oz copper. And then you're only limited to 8 amps.

**Dave Jones:** So, really we need double that. In a 25-mm wide trace, like a 1-in wide trace, you probably don't want to make it any wider than that on your PCB, right?

**Dave Jones:** That takes up a massive massive amount of room. So, you might want to actually you know, put some solder coat over the top of that, right? So, you can get a tin plate for example.

**Dave Jones:** So, you know, but unfortunately right this plating thickness doesn't actually take into account like the tin plate process. That's really hard to control. So, if you go I want if you go to your PCB manufacturer, I want a tin plate on that please, then it's the the control thickness is it's I've done a dedicated video on that and how much difference a tin plate actually makes.

**Dave Jones:** I've done some practical experiments on that. I'll link it in, but you can't really control that. But you might be able to tell them to actually you know, plate it a certain thickness or whatever, right?

**Dave Jones:** But once again, this is big increase in manufacturing costs. PCB manufacturers will do absolutely anything. The good ones will. They'll bend over backwards. They'll do anything you tell them to do.

**Dave Jones:** But they'll charge you for it. Okay? So, if we did that, you know, 1-oz plating thickness, we're still only at 40 oz, right? We still have to double that.

**Dave Jones:** Even when you go into like we're still not there. So, let's just go to a random PCB manufacturer here, and you'll notice that they go from 1 oz up to 13 oz copper.

**Dave Jones:** This is insane, but there's trade-offs there with they actually tell you minimum track space requirements and all that sort of stuff. But, they say they can do 13 oz, and they they can, but generally they're only going to go up to I think this manufacturer only says like 3 oz kind of like our standard process.

**Dave Jones:** So, you know, anything over that they're going to like order the material special. They may not have it in stock, and they're going to get it's going to cost you an absolute fortune and all that sort of stuff, right?

**Dave Jones:** And then, you've got the surface finish over here, okay? And generally, you're going to get a what's called a HASL, right? Which is a hot air surface level finish.

**Dave Jones:** So, they just put basically solder coat. That's That's basically what it is. And then, you're familiar with like the gold flash boards, the you know, the immersion gold. And I've shown my boards before that have come with immersion silver, for example.

**Dave Jones:** You can get immersion tin, and you can get, you know, there's all sorts of stuff. And you get nickel plated ones and all sorts of stuff. Right, plain copper, you generally as I said, if you want Here's an example.

**Dave Jones:** If you want your traces to be coated with solder coat like this one here, okay? Yeah, that can increase your current handling capacity, but it's not really a controlled process.

**Dave Jones:** They They can't really Yeah, it might be hot air finish. You might be able to see like, you know, like a few bubbles and stuff in there, right? Right, it's not It's not really a controlled that controlled a process.

**Dave Jones:** You can't really guarantee what your resistance is going to be. It's just hot air It's whatever the process just happens to be. But, it can increase your current. Now, the way you do that is to remove the solder mask.

**Dave Jones:** You have to remove the solder mask over that trace. Otherwise, when they do the board, you're just going to end up with that uh copper. Because as I said, uh the copper under here is just bare copper.

**Dave Jones:** It's SM OBC, solder mask over bare copper. I'll show you. See, if I scrape away that uh solder mask there, you can see that is just bare copper underneath there.

**Dave Jones:** So, the process that they do it happens after they put the solder mask on. So, if you want your traces coded like that um in whatever, you know, uh surface finish that you actually uh choose here, whatever surface finish you choose, if you want that coded you have to leave the solder mask off.

**Dave Jones:** So, back at 1 oz copper here, like I'm I'm being tight-ass Dave Dave. I'm only allowing for a 10° C temperature rise, right? So, if we go to 20° rise like that, okay, you go from 12 to 17 amps there, right?

**Dave Jones:** And then if you go up to your 4 oz thick uh copper, you know, you but you're still not getting a huge amount extra there. Like, you I'm I'm willing to make it go 50° above ambient.

**Dave Jones:** So, your PCB trace will be 70°, right? Remember, this is temperature rise above the ambient temperature. Okay? Solved. We get to our 80 amps. Okay? So, if you want to do this single layer and you and you're willing to fork out for 4 oz copper uh board material, and you could maybe get it it's going to rise 50° C.

**Dave Jones:** But once again, these are actually calculations. There's no Well, there are there are formulas for this and this is where it gets it from, but it's based on really empirical uh data.

**Dave Jones:** And this goes on like it tells you here, this is uh based on the IPC standard 2152 with modifiers. Um and you have to go read the IPC standards.

**Dave Jones:** There's actually two um IPC standards that cover this. There's the earlier uh 2221 standard here. And I I just googled the first thing I got was this Altium uh article here.

**Dave Jones:** Anyway, they link to some calculators. I'm not sure which which ones, but uh yeah, basically uh there's two different standards that'll cover this same thing. The IPC 2221, and they note here that uh the 2221 that was based on charts in the linked articles.

**Dave Jones:** Someone way back in the early days did some charts. Like, actually old-school charts, and they've got them in the standards. You can look it up. They're hand-drawn charts or whatever, or they, you know, uh these plotted uh charts, and that's where everyone's gotten sort of this data uh from back in the old days.

**Dave Jones:** But, there is another standard, the IPC 51 122, which is more accurate. I don't remember the exact details. It's been a long time since I've uh looked at the uh standards in this uh regard.

**Dave Jones:** But, just realize that the formulas are kind of based on, uh, sort of like experimental, um, you know, measured data. So, it's a bit how you doing, but it's the best we got.

**Dave Jones:** Now, interestingly, let's see if internal layer actually makes a difference here, and it it doesn't, right? Internal or external layer actually doesn't make a difference here. Which is interesting because in practice, it it kind of sort of does.

**Dave Jones:** Although, once your board's heated up, uh, you know, the like it depends on your, like, your thermal but the physical uh part of your design matters. Like, if you've got a fan in there, and you're blowing over the board, for example, the outer traces, yeah, they can get better um thermal properties than the inner uh traces in there.

**Dave Jones:** But, it's obviously not taken into account in the IPC 22 2152 standard, and it's going to matter whether or not you actually whether your trace is uh adjacent to like a big plane, for example, because you can get conduction between your little trace in the tiny uh thin prepreg in there.

**Dave Jones:** Um, it's not much different uh diff- distance between thickness between your uh trace on, say, an inner layer and the uh prepreg, for example. If you've got it on the outside, it's a bit uh further apart.

**Dave Jones:** And, this is why they actually have a plane present thing here, right? So, if we click yes here, then this is our current carrying trace and you can see it's jumped up.

**Dave Jones:** It's It's quite substantial. It's jumped up from 78 amps here for a once again a 1-in wide trace for a 50° C rise, you know, and and then it jumps up to 121 amps.

**Dave Jones:** And we're not running the current through that plane. It's not going through this big blue copper plane down here. It's purely the proximity. This is why they give you Yeah, here it is, distance to plane, right?

**Dave Jones:** 10 10 mils here. So, metric, you know, it's it's only .25 mm away. So, if we actually go from .25 mm to 1 mm there, it should like it it goes up a bit, right?

**Dave Jones:** Cuz this is all thermal conduction through to the plane. Even though the current's not running through that plane, simply having the plane present it's it's more betterer. Anyway, it gets As you can see, like there's a lot of stuff involved in this if you really want to go down the rabbit hole, but in answer um to the question here, um is it possible to use only one layer?

**Dave Jones:** And the answer is probably No, not really. Um not unless you use like massive traces and you allowed for you know, a huge temperature rise and stuff like that.

**Dave Jones:** So, yeah, you'd be using you know, at least two traces, possibly part of your internal plane as well. Um to get 70 80 amps is quite substantial. Or you could as I said, you could like tin plate, you could solder plate the top of those traces and that increases your current handling capability.

**Dave Jones:** So, but once again, that's not going to be factored into this calculator. You can't really calculate that cuz the thickness of of the applied solder you know, coating on top is it's not really a controlled process.

**Dave Jones:** So, you go I want it lower resistance. Let's you know, I want to carry more current. I'll just you know, solder coat it. So, you'll see that on all sorts of boards.

**Dave Jones:** So, let's take it back to a 10° C rise, a one a 1-in thick a 25-mm wide trace, which is like you know you know quite decent, you know, probably the biggest one that you want to run on a board for example, you know, 35 amps.

**Dave Jones:** Yeah, nah nah, you got to look for at least I'd be using double-sided. And then you got to ask yourself, well, do I want to via stitch down between the two layers?

**Dave Jones:** So, you stitch them together. It doesn't really help in the resistance side of things, but it helps with you got extra copper there. It does help a little bit with the thermal dissipation and stuff like that.

**Dave Jones:** So, you might want to you might want to via stitch along there just as a matter of course, but you don't want to via stitch until the cows come home because that just takes away from like your surface area of your copper effectively.

**Dave Jones:** So, like yeah, not really. Just run two thick traces top and bottom, probably you know, an extra internal plane to be sure. Yeah, you can get away with this 70-80 amps.

**Dave Jones:** You can get away with this on a double-sided board, but yeah, you're going to have to use a thick copper unfortunately cuz if you use your standard 1 oz stuff, you know, like 12 oz double it even use four layers, you're still not going to get enough really.

**Dave Jones:** So, yeah, you're going to want to be using to specify that thicker copper from the manufacturer. And then if you really need like a compact design and you don't like have layout room on your board, you might consider like a bus bar approach.

**Dave Jones:** I found one example here. You can see that this board uses these physical bus bars, which run right across the board like this. And of course, you can get you know, you can make those thick as, right?

**Dave Jones:** And but you know, you have to get those like custom manufactured and you'd have to go to a company that manufactures those. So, you know, a specialist manufacturer that makes those.

**Dave Jones:** But yeah, bus bars you know, quite common on like really dense, um, you know, highly populated boards. So, it's definitely worth considering something like that. Like this one here has got like three um ones.

**Dave Jones:** In this particular case, it's carrying power to like all all the devices across the board like this. But, you know, you can get one just one specific one that will you can actually like, you know, screw it down.

**Dave Jones:** You can even make it yourself. You know, you can get a bit of like alloy rod and then like screw it down into like a like a threaded insert into your board or something like that.

**Dave Jones:** You know, actually in a lot of the teardowns I've done, I think a recent one with the Keysight high current power supply, I'll try and include a photo of that here.

**Dave Jones:** And they use like big bus bars to take the current over and stuff like that. So, you know, when you start talking, you know, 70, 80 amps, something like that.

**Dave Jones:** So, you can do it on your PCB. But then, once you get like if you go to 4 oz copper here, and you only need it for that one trace, for example, then you you're wasting all that copper on the rest of your board.

**Dave Jones:** And they'll charge you a lot more cuz you've got to they've got to etch all the more copper off. And then, the thicker copper also limits it increases your trace space on your board.

**Dave Jones:** So, you can't do like your 4 thou 4 thou or you might not be able to do your say your 4 thou 4 thou traces on there. Your really thin traces on your board anymore with that 4 oz copper.

**Dave Jones:** You might have to put those on another layer, which is your 1 oz copper or 1/2 oz copper, and then dedicate your 4 oz layer to all your power and for this um, you know, big current traces that you actually need.

**Dave Jones:** But, yeah, but bus bar things are also very often used option. But, you know, it's a custom part, it's another bill of materials part. It's, you know, it's everything else.

**Dave Jones:** But, that might be a better trade-off. That might actually work out cheaper than the PCB, especially if you've got like a large board. You don't want to waste like, you know, a big 4 oz board like this and you only one little trace like that, you wouldn't do it on the board.

**Dave Jones:** You'd You'd design your custom little bus bar there. Yeah, no worries. But, there's several ways you can actually do that with threaded metal inserts and, you know, just screw down a little aluminum block and then screw it in and tighten it up and Bob's your uncle.

**Dave Jones:** And a little trick if you didn't want to get a custom bus bar manufactured, no worries. You wouldn't be the first person to run just a giant wire link across there.

**Dave Jones:** Just get a nice thick ass gauge wire and just you cut it to length and solder it on at the production stage. And, you know, unless you're building a million widgets, then that's a perfectly acceptable solution, especially if you're only got like one trace or one or two traces that that you need to do.

**Dave Jones:** Just get your regular 1-oz or 1/2-oz copper board or whatever, then just put on a big thick ass trace and then just bypass your PCB entirely. No worries. And the good part about that is you could have like a This is not a dense layout, but you can have a really dense layout and then you can like snake it around components and you can just, you know, squeeze that wire in anyway.

**Dave Jones:** No worries. And you can carry like 80 amps on that thick ass wire. Not a problem. And you'll see that selecting DC here just removes your skin effect thing down here.

**Dave Jones:** It has no difference to do with the amps down here. Now, if we actually go up into the program options here, we can actually change the IPC standard. So, we can use the old standard.

**Dave Jones:** Okay, obsolete for amperage and so they claim. A lot of people swear by the 2221 all the way now this 2152 rubbish. Right, so let's just take, right, a 1-in trace with 1-oz copper here, right, the 12.67 amps.

**Dave Jones:** And let's actually change that and see how much difference that actually makes. The old 2221, it's gone up a lot. Look, it's gone from 12 amps to 25 amps.

**Dave Jones:** Okay, just just between switching between the old and the new standard. Okay, so obviously the new standard much more conservative. And then we can do that add little modifiers here, but that's just you know, tweaking around the edges, right?

**Dave Jones:** So, but yeah, there's massive. So, if we actually choose the old standard here, um and we choose our 4 oz oz copper, we practically get to our 70 amps, you know?

**Dave Jones:** So, maybe, right, for our 10° C temperature rise, which one do you actually believe? There's a reason that they, you know, people thought that 2221 wasn't adequate cuz it was based on the old characteristic curves and you know, like you know, back from I don't know, the '60s or something, whenever they measured somebody, I don't know, um who measured it, if you know who, leave it in the comments down below.

**Dave Jones:** But um yeah, see, it makes it it makes a huge difference, massive difference. So, your mileage may vary. Anyway, if we remove the modifiers here, then we can actually solve for conductor width here, okay?

**Dave Jones:** So, we can actually go in here and we can do our 80 amps like this, right? And then it needs, well, 3 in. 3 in. Okay. Yeah, good luck.

**Dave Jones:** Well, you could get 1 and 1/2 in on each layer, maybe, or if you use like a four-layer board or something, you could use four layers. So, you can get away with it on the PCB.

**Dave Jones:** You can get away with it, but that's 4 oz copper, right? You use the 1 oz copper, 12 in anyone? That's what she said. And if you're wondering about this etch factor here, it basically makes no difference whatsoever.

**Dave Jones:** It's just the when you put it in your etch-away the copper, the copper just doesn't etch square like that. It etches, you know, who knows how much etching you get over-etching and you get breaks in your traces.

**Dave Jones:** That's why you can't have a, you know, you have a minimum trace width. Uh you know, it might be, you know, 6 thou, 4 thou, something like that, or 0.1 mm for you metric fanboys.

**Dave Jones:** And you can't make traces smaller than that because the manufacturer can't guarantee that their etching process is not going to over-etch the copper and break the traces. So, even though they electrically test the boards, they don't want to over test them and like and scrap a whole lot of boards and stuff like that.

**Dave Jones:** That just cost them money or they'll pass it on to you. Um so, yeah, H factor. Um it it makes like when you're talking about really fat traces like this, doesn't matter.

**Dave Jones:** But, when we're in the older standard, the IPC 2221, you can see that basically if you choose the internal and external layer, it makes a heck of a difference.

**Dave Jones:** It's like as I said, the external layer can carry a lot more current, 4 amps here. So, in practice, um that's why you know, the older standard, the 2221, you have to sort of like everyone knew that the external layers like they could handle more current than the internal layers due to the insulation and the heating and everything else, right?

**Dave Jones:** So, obviously the more the newer standard is more conservative and as as you saw, it make it makes it should make no difference to that and we can actually swap that back, right?

**Dave Jones:** So, let's 21 52, swap it back and you'll see that the internal external layer makes no difference to the maximum conductor current. They've taken that into account with their conservative formula, however it works out.

**Dave Jones:** So, um yeah. Nah. So, I hope that's answered the question somewhat and given people at home food for thought and you can as always, you can really go down the rabbit hole on this thing and if you go like there's been lots of controversy over the years about the IPC standards for current carrying capacity and based on the old curve characteristic curves and stuff like that and people what you

**Dave Jones:** know, there's like multiple camps out there of which one's the best one and all sorts of you know, it's you know, nerds will fight about this sort of stuff.

**Dave Jones:** Um but yeah, it's it's an interesting topic, current handling capacity, you know? Basically, yeah, the the two rules are how thick your copper, how wide your copper and what sort of temperature rise you're willing above ambient.

**Dave Jones:** And imagine if it's like a you know, automotive thing and your ambient temperature's has up to 70 degrees or whatever and your temperature rises above that and you thought, "Oh, yeah, you know, 50 degrees C temperature rise.

**Dave Jones:** Yeah, no worries." And if you just went, "Oh, I can do 100 degrees temperature rise. It's a piece of bacon. Handle 100 degrees, can't it?" It'll be warm, you can get a bit brown looking after a few years, but you know, she'll be right.

**Dave Jones:** Look at this, 116 amps. Wow, it's turned red. Why is it turned red? I think it just Yeah, it literally got too hot there. Like it's it's 100 It's like 170 degrees.

**Dave Jones:** I mean, you take it down to 20 degrees ambient and you know, 116 amps. There you go. Anyway, yeah, you're going to Yeah, you're going to need that thick ass copper, I'm afraid.

**Dave Jones:** Anyway, if you enjoyed that video, if you like me answering these sorts of questions even though I waffled on a bit, um give it a big thumbs up. And as always, thoughts and comments down below.

**Dave Jones:** Catch you next time.
