---
video_id: qqBU8-f8h2s
title: EEVblog 1427 - An INFURIATING Electronics Exam Question!
url: https://www.youtube.com/watch?v=qqBU8-f8h2s
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 31, "3": 46, "4": 62, "5": 76, "6": 93, "7": 112, "8": 130, "9": 149, "10": 163, "11": 174, "12": 187, "13": 199, "14": 213, "15": 228, "16": 243, "17": 257, "18": 270, "19": 286, "20": 299, "21": 309, "22": 323, "23": 336, "24": 353, "25": 371, "26": 388, "27": 405, "28": 421, "29": 437, "30": 452, "31": 468, "32": 481, "33": 493, "34": 505, "35": 520, "36": 538, "37": 551, "38": 564, "39": 575, "40": 592, "41": 609, "42": 623, "43": 639, "44": 653, "45": 668, "46": 681, "47": 697, "48": 714, "49": 728, "50": 742, "51": 755, "52": 769, "53": 785, "54": 797, "55": 811, "56": 822, "57": 832, "58": 846, "59": 860, "60": 872, "61": 886, "62": 901, "63": 915, "64": 929, "65": 944, "66": 960, "67": 974, "68": 988, "69": 1001, "70": 1013, "71": 1024, "72": 1037, "73": 1051, "74": 1067, "75": 1080, "76": 1095, "77": 1109, "78": 1124, "79": 1139, "80": 1151, "81": 1165, "82": 1175, "83": 1188, "84": 1203, "85": 1216, "86": 1232, "87": 1247, "88": 1258, "89": 1272, "90": 1284, "91": 1300, "92": 1314, "93": 1330, "94": 1343, "95": 1361, "96": 1376, "97": 1387, "98": 1402, "99": 1415, "100": 1430, "101": 1445, "102": 1461, "103": 1473, "104": 1484, "105": 1501, "106": 1515, "107": 1534, "108": 1549, "109": 1561, "110": 1578, "111": 1589, "112": 1601, "113": 1613, "114": 1628, "115": 1642, "116": 1657, "117": 1674, "118": 1691}
---

**Dave Jones:** Hi, it's infuriating exam question time. This one comes from the EEVblog forum. I'll link it in down below if you want to join the discussion and you should be on the EEVblog forum. Um, this question comes courtesy of Atmel

**Dave Jones:** from Sweden. Hi to all my Swedish viewers and I presume Atmel is doing some sort of course on electronics and this looks like an some sort of exam question. I don't know. I don't think put more details in here. Anyway, it

**Dave Jones:** seems pretty simple. It's got four LEDs in here or LEDs for those who don't like me calling it LEDs. LED, it's easier. Hello, how would I calculate the current at the different points in this circuit? Now, the only information we're given is

**Dave Jones:** that VCC equals 4 volts. So, we've got a 4-volt rail up here. We've got the forward voltage of the LED is 2 volts at 20 milliamps. So, they only give us the forward voltage at the 20 milliamp current, which is very typical for a red

**Dave Jones:** LED and R1 is 100 ohms. So, we have to calculate the current through the LED resistor with the resistor dropper here and then the current in one branch of this circuit here and the of one of these LEDs in two LEDs in

**Dave Jones:** parallel and then then the other LED down here. So, we've got a series parallel combination string here. Now, the first time you see this, you just go why on earth are they like this is a completely flawed question and it's

**Dave Jones:** infuriating. And if I was I've had similar actual questions like this in exams and I don't care if I get the Well, I would try and get the right answer that they're expecting, but then I would also put a huge diatribe of how this is like

**Dave Jones:** complete and utter bull im- impractical So, it's one of these differences between uh uh theory you know, theory and uh practice, of course. But, um yeah, it it doesn't even make sense sort of in theory, really. It's Well, it does, but

**Dave Jones:** it's it's dumb. But, anyway, actually, I really think this could be a potentially good question for a job interview candidate if you're looking for an employer or something like this. Throw something incredibly simple question like this and see what see the response. It It's For

**Dave Jones:** me, a question like this, I would like, rather than just have a multiple-choice answer or just, you know, have like just tell me the current. I would want like a big description of what's going on here. Sort of like, you know, explain

**Dave Jones:** the issues with this circuit or something like that. So, I think this could be a really interesting job interview question just to see how people respond to it. Do Do they just go in and blindly try and calculate stuff

**Dave Jones:** or do they put their thinking cap on and go, "Uh, this doesn't really make sense because XXXX, but I'll still try and answer your question." But, you know, like if I got this question in a job interview, I'd immediately want to go to

**Dave Jones:** the whiteboard. There's usually uh often you have have your job interviews in a like a boardroom uh kind of thing at a company. There's usually a whiteboard in there. Um, yeah, I'd go to the whiteboard and and explain. Um, that's

**Dave Jones:** classic little uh job interview tip there. If you can, go to the whiteboard. Get up. Be animated and start doing stuff. So impressed, they'll hire you on the spot. Anyway, so, let's look at the issues here. And there are quite a few

**Dave Jones:** uh responses down here, by the ways. But, I haven't actually read them all yet. But, anyway, let's think about this, okay? The first thing is is that you never ever put a voltage source, presumably a low-impedance voltage source. You have

**Dave Jones:** to assume that because it's driving 20 milliamps, it's at least reasonably low impedance, right? Uh Um that you know, you don't put a voltage source directly across a non-linear element like an LED here. It's just It's just ridiculous.

**Dave Jones:** So, yeah, you wouldn't do that. Okay? But, we are told that the forward voltage is 2 volts here. Okay? So, there's 2 volts drop across this one, and there's 2 volts drop across these two in parallel cuz they're in parallel,

**Dave Jones:** so they'll have the same voltage drop. Okay? So, this midpoint here um is going to be like 2 volts. It's half rail. So, it all kind of makes sense. So, you know, you can sort of brush that the practical aspect of that

**Dave Jones:** away and go, "Okay, there's 4 volts VCC, and we're going to have 20 milliamps." That means the answer um for B here, it must be 20 milliamps. Okay? There must be 20 milliamps flowing through B here. But, then you engage

**Dave Jones:** your brain for 2 seconds, and you suddenly realize, "Well, there's 20 milliamps through here." Kirchhoff's current law says um that you know, the current entering the nodes must equal the current leaving the nodes. I've done a video on that.

**Dave Jones:** I'll link it in up there and down below if you haven't seen that. Kirchhoff's current law, and you'd explain this if you're in a job interview and this was exam question. You go, "Oh, Kirchhoff's current law, right? The current, if you

**Dave Jones:** got 20 milliamps like coming out of this node here through this LED, which we know, right? Is it the voltage is going to be split across these, then you must have 10 milliamps each coming through these LEDs, assuming that they're matched, of

**Dave Jones:** course. And it But, here's the problem. Like, they only tell us 2 volts at 20 milliamps. They only give us the one data point, of course. But, of course, a LED is a non LED is a non-linear element. So, let's just go to a data

**Dave Jones:** sheet here. This is literally a universal LED, right? A 5-mm universal. Love it. Um Anyway, this so happens to be, you know, typical voltage, 2 volts. There we go. Forward voltage at 20 milliamps. So, this is bang on.

**Dave Jones:** It literally is a universal LED, okay? But, of course, you go down here, and here's the characteristic curve. Of course, it is it's non-linear. Forward voltage, sure enough, forward voltage, 2 volts at 20 milliamps there. But, if you got 10 milliamps, it's

**Dave Jones:** instantly, which we know is in both of those legs, right? be due to assuming they're matched, due to Kirchhoff's current laws, then you're looking at like 1.8 volts, maybe? 1.85 or something like that? Like, it it's just it's completely

**Dave Jones:** screwed up. Anyway, so the answer for C here is, of course, 10 milliamps. And, of course, then the answer for A down here, then you have to do your LED dropper thing. So, let's go through that calculation. We know there's 2 volts uh

**Dave Jones:** drop across the LED here, okay? Because that's the only information we're given. So, we have to run with that. So, that So, that means 4-volt rail minus 2 volts means that must be 2 volts across the 100-ohm resistor. And, of course, 2

**Dave Jones:** volts across 100 ohms is 20 milliamps. A is 20 milliamps, B is 20 milliamps, C must be 10 milliamps. I mean, that's the answers that they're obviously after. But, yeah, I would just write a whole Like, I'd really go to town. I wouldn't

**Dave Jones:** even care if I got this answer wrong, damn it. I'd I would want to give them hell in the uh comments, you know? I So, anyway, let's see what some other people here say. It's just a dumb question. It doesn't take a practicality

**Dave Jones:** into account at all. Um cuz, you know, LEDs are non-linear devices. Um that's just like we we know this. That's actually information that we're giving. We're We're actually Even though we're giving given these figures up here, we are given the schematic symbol for an

**Dave Jones:** LED, and we know that it's Every LED is going to have a you know a non-linear response like this. So, it just it it just makes no sense. It's dumb. So, you could build that up, and I think somebody did down below, and you

**Dave Jones:** could see the results. But, the results are going to be on the type of LED that you have. Okay. Copernicus says You don't have to think the exact numbers when you do this. I think that people do too much math and

**Dave Jones:** not enough real thinking when they do electronics. This circuit is so basic. Why bother calculating any number at all? But, Copernicus is saying so the right is definitely a lot brighter than the left because it has a resistor in

**Dave Jones:** series. But, no, there's actually 20 milliamps flowing through this one as well. And of course, the brightness is not a function of the voltage. It's a function of the current. There diodes are essentially including LEDs light emitting diode. It's in the name. It's

**Dave Jones:** essentially a current driven device basically. It just the voltage drop happens to be a result of driving it at a particular current. But, they're not voltage driven devices. That's not their intention, which is why it's stupid to not have a current

**Dave Jones:** limiting resistor or some sort of constant current circuit driving an LED. Don't do it. But, then there's people who say, "Oh, those little keychain flasher things, they put the LED directly across the battery." And well, batteries have internal resistance. So,

**Dave Jones:** you do effectively have a series resistance in there. So, here comes the tricky bit, right? Which are not one xor one picks up. So, you would get 20 milliamps through the left branch with with the resistor, of course. But, he's

**Dave Jones:** saying you would get something more than 20 aliens through the right one seen as that there are two LEDs in parallel. That means less current less voltage drop. With real components etc., you'd get on the left side and larger

**Dave Jones:** variations of burnt LEDs on the right. Well, see, here's the thing, right? If you rigidly stick to that VF 20 milliamps, you'd have 20 milliamps through here, 20 milliamps through here, and then you'd have 40 milliamps Kirchhoff's current current law must

**Dave Jones:** hold. You'd have 40 milliamps flowing through this one down here. But then it like it non-linear nature up here, 40 milliamps you're up to you know 20 30 40, right? You're up to like 2.2 volts per LED, which

**Dave Jones:** is just no, it's dumb. And Marush here, if I'm pronouncing that correctly, um so if we assume an ideal circuit, the LEDs are fully open at 2 volts and the wire has no resistance, then those LEDs would simply blow up cuz there's nothing to

**Dave Jones:** limit current going through them. Well, you know, that's another sort of like theoretical question. It's like Oh god, I hate this question. This is dumb. But here's the point as Jay Melson points out, the current in the right

**Dave Jones:** branch is uncontrolled. Very slight variations in VCC or LED forward voltage will cause huge changes in LED current. That's why all practical LED circuits use a series resistor or a current source. Yes, the current bit as a homework exercise, the current in the

**Dave Jones:** right branch cannot be calculated unless you assume the LEDs draw exactly 20 milliamps at 2 volts. It is a pathological circuit and should not even be given as a homework question. It's pathological. Love it. Even with that assumption, it

**Dave Jones:** doesn't work unless they assume VF is abs- absolutely constant from 10 to 20 milliamps, which is not. And it's just AG6QR says the two LEDs in parallel in top half of the right side must each be getting a portion of the current that

**Dave Jones:** goes into the bottom LED on that side, so they can't possibly all three be conducting 20 milliamps at 2 volts. That's the thing. But because this is like a theoretical question, you have to just make the dumb-ass impractical

**Dave Jones:** assumption that well, Kirchhoff well, I would I would say above everything else, you have to assume that Kirchhoff's current law holds. If you're going to learn basic electronics like this, you've probably already uh would you have been taught you'd probably have

**Dave Jones:** been taught Kirchhoff's current law at this point. It's well, essentially based on my DC circuit fundamentals are series. Yeah, this would be you know, it's one of the first things that you actually uh learn. So, you know, it it must hold and

**Dave Jones:** you've been stated that the forward voltage is 2 V at 20 mA. So, you have to assume that, you know, look because these are in parallel, so you have to assume it's just one, right, in terms of like a

**Dave Jones:** voltage divider thing. So, you have to assume that it's 2 V, 2 V. You'll have to assume 2 V at that midpoint junction there. It's just it's just something that you even though it's infuriating, you have to assume that. And once you

**Dave Jones:** assume that and you assume that Kirchhoff's current laws hold, you've been told 2 V at 20 mA, therefore the current must evenly split. And because you're making these ideal assumptions, yeah, C up here must be 10 mA. But it's

**Dave Jones:** it's infuriating. So, I would never write down just the numbers for this answer here. I did No. No. Rebel against the system. You've got You've got I'd write down an explanation of why you made various assumptions and things like

**Dave Jones:** that. And I would never say somebody is wrong. I once And if they explain why they came up their reasoning, I would never say that they're actually wrong unless they were unless the answer from their assumptions was actually

**Dave Jones:** wrong. But yeah, that's this is why I think this makes a really good interview question cuz it it provokes you know, heated discussion, right? And it it shows what the person knows and they're, you know, it shows that they

**Dave Jones:** know Kirchhoff's current law. It shows that they're willing to put their thinking cap on and know, no, this this can't be right, you know, and and how to analyze the situation. Um it it it's it's it might be deliberately designed

**Dave Jones:** like this. I don't know if the question actually has like a a text box, you know, explain your answer um as a lot of questions are and jeez, I'd I'd need a whole page to, you know, I'd really let

**Dave Jones:** them have it. Anyway, X runner's got it all breadboarded up. Yep, the right side is not acting predictable as suspected because the two LEDs are not identical. Exactly, they're not matched. However, the left side pretty much matches calculations. Yes,

**Dave Jones:** it will because you've got a low impedance current source. Your power supply is a very low impedance output as like milliohms, right? It's it's really small. So, it's going to force, unless you've got the current limiter, uh you

**Dave Jones:** know, set, um then it's going to it's going to force 4 V to this point and these diodes on the right-hand side they've just got to sort themselves out, the poor bastards. But this one over here, nicely designed with this current

**Dave Jones:** limiting resistor, then yes, it's going to get the proper 20 mA treatment there, assuming you've got the exact LED that, you know, gives you that exact value. But even then, you're going to have temperature and process uh variations,

**Dave Jones:** manufacturing variations over here. This is why over here in the data sheet, look, forward voltage 20 mA, right? It's And can you see that? Yeah, there you go. It's typical of Sorry. Um yeah, no, maximum of two unit three?

**Dave Jones:** What? What's wrong with the Why is that unit three? What does that mean? Müller Müller Müller Um I don't get that. So, here we go. X runner's gone to town here, hats off. Uh set the input voltage to 4 V on the breadboard,

**Dave Jones:** measure resistance of R1 was 98.7, good enough for Australia. Path A measured current was 17 mA and VF was 2.14 and you could like you could like go in there and like trim things and stuff. But yeah, the

**Dave Jones:** left-hand side branch doesn't matter cuz it's it's going to do its own thing. It's the right-hand path that you're going to worry about. So here we go. Path B current was 10 milliamps. There you go. So it did actually split and VF of LED B

**Dave Jones:** was 2.1 volts. So it did actually share the current because Kirchhoff's current laws got you know, those those LEDs will sort themselves out. Now here's where it differs in practice. Path B current was 10 milliamps and VF across LED B was 2.1

**Dave Jones:** volts. And if we go up to the top, this is actually 10 milliamps through here at 2.1 volts. So I've got 2.1 volts across here, we're going to have like 1.9 volts left across here like this. So you know,

**Dave Jones:** these things have sorted themselves out and they've determined they talked among themselves and going, "Right, we're going to have 10 milliamps through here." So the current, assuming these LEDs were like from the same batch and reasonably split, so I expect C to be

**Dave Jones:** roughly half of that or five-ish milliamps. And sure enough, path C was 1.93 volts. The current through each of the LEDs in parallel was very touchy. I got from two to four milliamps depending on the stability of the connection I

**Dave Jones:** made with the probes or tapping on the desk. In fact, any slight push on either LED resulted in both LED variations of light output yet due to slight resistance changes in the breadboard connection. Um so this is all sorts of

**Dave Jones:** stuff that you could talk about in your job interview. Uh you know, if you got given this question or something like that, you can really go to town on the whiteboard like you you know, talking about this sort of stuff. In in other

**Dave Jones:** words, it's very unstable as as was suspected but that's only because of the physical breadboard and stuff like that. But if you actually soldered them, yeah, you'd So yeah, I think you'd actually have to have multiple meters in there.

**Dave Jones:** You have to have like three different meters in there all measuring that. But suffice to say and like if if we had this over here was branch D, if we had a meter there measuring branch D current, C plus D would always equal B even if

**Dave Jones:** they're you know, it's changing over time due to the connections or thermal when the leads are just going like this. Yeah, at any instant in time the current C plus the current D will equal the current B. Kirchhoff's current

**Dave Jones:** law must hold. And then Tom Wroshki here has gone to town given the pathological nature of I love that term. Nature of the question along with the limited amount of data we can approach it with a certain ideal conditions. All diodes are

**Dave Jones:** exactly the same temperature. All diodes are identical. The ideal diode equation applies going into the diode equation so we're getting into the physics side of things. Look up the various terms. Yeah, I look this video is not going to go into

**Dave Jones:** details. And I I haven't gone through his calculations down here. So I got you know, I did look I I don't know. But yeah, you can treat it sort of more mathematical like this. And it hasn't given a summary like that. So

**Dave Jones:** anyway, I'll leave it up. There we go. There's a homework for those playing along at home to uh give a reply. Go go to the forum and give a reply to Tom Wroshki. Yeah. Great work. I think everyone is trying

**Dave Jones:** to add reality to a homework problem. No issues with the Well, it's not You've got to add reality cuz the question itself is completely dubious. Cuz it's telling you it's a physical LED, right? It's an LED uses the symbol.

**Dave Jones:** And that just tells you right away this is a practical circuit problem. And it's just yeah, it's just infuriating. So yeah, Astofek basically comes to the same conclusion I did that current A is 20 milliamps, current B is 20 milliamps,

**Dave Jones:** current. C is it must be half 10 milliamps due to Kirchhoff's current law. No info No other information was presented. I think the ideal component is all you can use. How you justify the 10 milliamps across the parallel LEDs? I

**Dave Jones:** don't know. And yes, the 10 milliamps is correct. Whether that would actually produce 2 volts isn't given in the problem statement. So yes. So yeah, I put my response down here and then I just went, "Ah, no, bugger it. I'm

**Dave Jones:** shooting this video." So there you go. One of those stupid theoretical questions. And if you ever see something like this in an exam, let them have it. Damn it. Do not stand for these impractical problems in these um

**Dave Jones:** exams. But of course, it's obvious what answer they're after. But yeah, I really hope a question like this would have a please explain your answer uh box. I would never like Seriously, that's a serious fail of a lecturer if they

**Dave Jones:** produced this as an exam question and did not give you a please explain your answer box, then that is a failure on their part and you should tell them that. Um yeah, seriously. Might get thrown out, but you know, hey,

**Dave Jones:** it's worth it. But I'll say if they did give that please explain your answer box, then you know, hat tip. Cuz this is a This is an interesting one. And as I said, great job interview question cuz it just

**Dave Jones:** promotes discussion. And And you can really extract a lot out of an interviewee if you um you know, actually provoke them with a question like this. So anyway, I hope you found that interesting. If you did, leave your

**Dave Jones:** thoughts and comments down below. And I'll link to the EEVblog forum. If you're not on the EEVblog forum, join in the discussion down below. That's where everyone hangs out. And uh we can see who's there at the moment. There you go.

**Dave Jones:** Xrunner, Amy K, me, um RFX, Auston Entis, seven guests are viewing this topic. Probably a lot more after this video. But there you go. I I thought I'd share. Thank you very much, Etna. So, Etna has not actually replied to this

**Dave Jones:** yet, but 10 posts, so you know, not not a complete newbie. So, I assume Etna will come back and join back join the discussion. But, yeah, please join the discussion in this one. Let us know how you would solve

**Dave Jones:** this and if you think this is an insulting question without having a please explain box, cuz I think it is. I think this question, yep, it's anyway. Thoughts and comments down below. Catch you next time. Oh, all right. I know people aren't going to be

**Dave Jones:** happy unless they actually build this thing up. So, I've actually managed to find after some searching um four red LEDs that are pretty damn bang on to 2 V at 20 mA. And trust me, it wasn't easy to find, BUT I FOUND THEM. ANYWAY, um

**Dave Jones:** so, I'm using my external Keithley current source here. So, I've set that to um you know, pretty close to 20 mA. It's only three digit adjustment, unfortunately, but you know, that's good enough for Australia, right? 20 mA. Let's uh measure each LED uh the voltage

**Dave Jones:** drop across each LED at 20 mA to make sure they're reasonably matched. And wouldn't you know it, I've actually blown one. Um I must hooked it up backwards. And then my comply I thought my compliance voltage was as low as possible was down

**Dave Jones:** at 10 V, but still Oh, no, what? Anyway, LED number one 1.98. Not too shabby. There you go, it's dropping. She's actually uh warming up a bit. LED number two, 1.94 V. Not matched, but you know, good enough for

**Dave Jones:** Australia. Number three, 1.99 V. There you go. Oh, no, 1.98. Right. So, anyway, I'm going to use those three matched and this one um is the diode. I don't know if there was a physical failure or whatnot, but um

**Dave Jones:** look, I'll go find another red LED and I'll use that in the left-hand circuit, cuz it's it's not going to matter. I mean, the whole point is what happens on that right-hand current circuit with the three LEDs in series parallel. Look at

**Dave Jones:** that. I was able to find another one, 2.02. That's not too shabby, 5 mm jobby. Okay, so I've just got the single resistor on the left-hand side of the circuit. So, that's our 4 V input. There you go. And across the resistor, this is

**Dave Jones:** bang on 100 ohms. So, 1.96. So, I know 19.6 milliamps is flowing through there. Ohm's law. Don't even need to get the current meter out for that. So, here you go. I'm now going to move it over to put

**Dave Jones:** the other LEDs in series. Let's see what happens. I'm going to apply 4 V. Tada! Yep, they all come on. Okay, so I've actually set 50 milliamp current limit on my power supply. And they've all come on. I'll put it

**Dave Jones:** right there. Yep, we're still got 4 There we go, 4 V. Now, let's see what we get across the center tap of this string here. Will it be 2 V? I don't know. Oh, there we go. That's not too Wow,

**Dave Jones:** that's pretty That's pretty close to bang on, isn't it? Interesting. There you go. So, let's measure the top one. Of course, we must have 1.98 across there. Well, 1.9. Well, yeah, you can see Yeah, like it's it's varying a little bit and

**Dave Jones:** that's going to have to do with the dicky connections on the breadboard. So, it's going to be jumping jumping a bit all over the shop there. But, as you can see, uh it Yeah, we've got 2 V across there.

**Dave Jones:** How much current's actually flowing through there there? Well, we'll have to measure that. Now, of course, burden voltage of your multimeter could get out the micro current and stuff. Couldn't be bothered. So, what I'll do is I'll just

**Dave Jones:** whack it on amp's range and we'll put it on amp's jack here and that will give us a 0.1 milliamps resolution, but really like you know, low burden voltage, okay? Yeah, you can see those LEDs flicker when I actually move that resistor in

**Dave Jones:** there. I don't Well, I I I think you can. Yeah, that's just like maybe dirty crappy contacts on the on the resistor lead and or breadboard. But anyway, what I'm going to do is put it in there, ready? I'll turn it

**Dave Jones:** on and let's see what we get. To 24 milliamps, that's 25 milliamps, 28, 30? More? There you go. So, we are actually getting In this particular case, we are getting um higher current. It's backwards. All the electrons are

**Dave Jones:** flowing out the wrong way. There we go. All right, now now it's down to 25. There you go. 26. But it is certainly higher than the other branch. So, there you go. That's interesting. Just give that a few

**Dave Jones:** wiggles in there just to clean those contacts. This is an old resistor from a junk bin, so, you know, bear with me. Okay? So, what I'm going to do now is this resistor, I don't know if it's left or right. Doesn't matter,

**Dave Jones:** take your pick. And there you go. It is half. It's roughly half. We've got our 10 milliamps flowing through the LED. There you go. Winner winner chicken dinner. So, that because these these three LEDs are all reasonably matched, then they're going

**Dave Jones:** to roughly share the current. But of course, that uh total um current through there, you saw that was higher, could be up to 30 milliamps, something like that. But definitely, when you put two in parallel like this um and they're

**Dave Jones:** reasonably matched, then you're going to get a reasonable uh 50/50 split in the current between there. So, and of course, the remainder of the current must be in the other LED. So, I don't need to I can put multiple

**Dave Jones:** like meters and stuff. But then you have to like get like, you know, like soldering them into proper banana jacks so that you've got, you know, proper cabling and everything set up. And it's all like I couldn't bothered.

**Dave Jones:** That just shows that the current does split between those two upper ones and the combined current Kirchhoff's current law, that one. Even though I can't really see any difference in the brightness between these two and this it's not just the camera. It's really

**Dave Jones:** hard to actually discern that difference and this is a thing even though this has more current and twice the current as these two here, they appear similar apparent brightness uh to the eye. That's just a trick on the eye. So, you

**Dave Jones:** know, there's no need to run um LEDs at like 20 milliamps. It's you could easily half your current there and if anything, those two actually look a bit brighter than that one. I don't know, it's just cuz I wasn't looking straight on, but

**Dave Jones:** yeah, anyway uh That's just a function of our eyes really. If you actually got proper measurement instruments that were measuring the millicandelas or the lumens out of this thing, then you'll find that yeah, the brightness would be proportional to the current cuz that's

**Dave Jones:** pretty linear. Having said that diodes and LEDs are non-linear devices, they are in terms of voltage drop, but in terms of output lumens output per current per milliamp through them, then that's a pretty linear relationship for the most part.

**Dave Jones:** So, there you go. I hope you enjoyed that bit of pointless fun. If you found it interesting though, give it a thumbs up and as always discuss down below. Catch you next time.
