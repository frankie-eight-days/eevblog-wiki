---
video_id: WBfAEeEzDlg
title: EEVBlog #819 - DC Fundamentals Part 4: Kirchhoff's Laws Tutorial
url: https://www.youtube.com/watch?v=WBfAEeEzDlg
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 23, "3": 37, "4": 56, "5": 66, "6": 74, "7": 87, "8": 105, "9": 115, "10": 129, "11": 145, "12": 156, "13": 175, "14": 191, "15": 200, "16": 215, "17": 226, "18": 240, "19": 256, "20": 268, "21": 290, "22": 305, "23": 316, "24": 332, "25": 342, "26": 359, "27": 372, "28": 386, "29": 398, "30": 415, "31": 423, "32": 433, "33": 453, "34": 468, "35": 481, "36": 495, "37": 511, "38": 527, "39": 536, "40": 544, "41": 556, "42": 567, "43": 578, "44": 593, "45": 613, "46": 625, "47": 644, "48": 658, "49": 669, "50": 684, "51": 702, "52": 725, "53": 738, "54": 750, "55": 761, "56": 792, "57": 809, "58": 821, "59": 836, "60": 848, "61": 862, "62": 877, "63": 885, "64": 905, "65": 921, "66": 932, "67": 942, "68": 955}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at one of the most fundamental laws in electronics, as fundamental as Ohm's law. It's called Kirchhoff's laws, or more specifically, Kirchhoff's current law and Kirchhoff's voltage law.

**Dave Jones:** Now, you've probably heard people, including myself, in a lot of my videos just throw away the term Kirchhoff's law. Oh, and you know, by Kirchhoff's law, blah blah blah blah blah.

**Dave Jones:** And some people don't actually know what it is, but I bet you you already fundamentally know it, even if you've never heard of it. Now, we're actually going to get into a little bit of math today, but don't worry about it.

**Dave Jones:** Kirchhoff's laws are simple, dead simple, even simpler than Ohm's law, because they're just laws that you don't even have to remember a formula. They're just basically a concept, a very powerful concept that allows us to do some pretty advanced mathematics in electronics, although we're going to stick to some fairly simple stuff today.

**Dave Jones:** As with many things in electronics, named after the person who discovered it, Gustav. Good on you, Gustav Kirchhoff, in about 1845 or thereabouts. Now, there are two fundamental Kirchhoff's laws.

**Dave Jones:** The first one we're going to take a look at is Kirchhoff's current law, or KCL for short. The other one is Kirchhoff's voltage law, and we'll do that next.

**Dave Jones:** So, let's take a look at the current law. It's real easy. How easy? Let me show you. Kirchhoff's current law states in a roundabout way, the sum of currents into a junction equals the sum of currents out of a junction.

**Dave Jones:** Current in must equal current out. That's it. That's That's the entirety of Kirchhoff's current law. Nothing more complicated than that. So, just like the fundamental laws of physics, like the conservation of energy, effectively what Kirchhoff is saying here is this is a conservation of charge.

**Dave Jones:** If you put charge into a loop circuit, it must come out. Charge in equals charge out. Or in this specific case, we're talking about a junction point in a circuit.

**Dave Jones:** Current in equals current out. It's that easy. You already know it. It's fundamental. It's obvious. So, fundamentally, that's it. You don't need to know any more than that. You now know Kirchhoff's current law.

**Dave Jones:** Current in equals current out. It's too simple. But, eh, there's some powerful things we can do with it. So, let's take a look at an example, shall we? We've just got a resistor here and two resistors in parallel here that we've got current flowing in I1 here.

**Dave Jones:** Let's just assume it's flowing in here and it's into this junction. You remember we're talking about a junction here. And then, we've got two paths coming out. So, we've got I3 coming out and I2 coming out here.

**Dave Jones:** So, we can actually have a formula. We can go I1 = I2 + I3. Remember, the sum of the currents into the junction, in this case we've only got one, but we could have more than one, and equals the sum of the currents out of the junction.

**Dave Jones:** So, I1 is in, I2 and I3 are out. That's it. And if we had another current coming in here, for example, like this, and going in, and we can call that I0, it'll just be I0 + I1.

**Dave Jones:** Remember, the sum of the currents in equals the sum of the currents going out. But, sometimes it's actually more powerful mathematically to say this, which is exactly the same.

**Dave Jones:** We're basically just rearranging it. We can go I0 + I1 I2, and I'll explain why in a second, - I3 = 0. It's basically just a rearrangement of that formula.

**Dave Jones:** So, what this rearrangement of the formula means, and you typically would write this like directly like this straight off the bat. And we'll do this in further examples to come.

**Dave Jones:** Basically, any current flowing into a junction, you define that as a positive current. So, I0 is flowing in, so it's positive I0 plus I1 is also flowing in to the junction, so it's a positive.

**Dave Jones:** But, I2 is flowing out of the junction, so you actually define that as a negative current. And likewise for I3 three there, it's a negative current as well. So, you come up with this equation like this.

**Dave Jones:** And you can write the equation for any number of currents flowing in or any number of currents flowing out of a junction, even if you've got one current flowing in and one current flowing out, you can still write the basic equation.

**Dave Jones:** And the thing about this is it's not a formula that you have to remember. It's just a concept that current in equals current out. Now, of course, I can build up a boring circuit and actually demonstrate that current in equals current out, but there's no point, but I'll just give you one little simple example here you where you might use Kirchhoff's current law in the real world, for example, to analyze a circuit

**Dave Jones:** here. Let's take an op amp. We've got an inverting configuration. You should be familiar with something like this. We've got a positive voltage here, and by op amp action, one of the basic rules of the op amp is our non-inverting terminal here is at 0 V.

**Dave Jones:** It's a ground, so therefore the inverting terminal is also at ground. So, we're going to have a current flowing through like this. So, remember, look, we've got a current flowing into a junction point right here, okay?

**Dave Jones:** Where does it flow? Well, it can't flow into here, can it, because the input impedance of an op amp is supposed to be infinite or an ideal one. So, it's got to flow all the way up here like this.

**Dave Jones:** So, we've got a current coming out. But, in the real world, a practical op amp will have some input leakage current in here, okay? So, we've got IL there, for example, leakage.

**Dave Jones:** So, this could be, say, I out and this is I in. So, in this case, you can actually come up with the equation that I in equals I out plus I L.

**Dave Jones:** Because, remember, current in must equal current out. We've got two currents coming out of a junction. The one that goes up this resistor, the feedback resistor here, and the tiny little current in there, they must be equal.

**Dave Jones:** And if you've got a practical op-amp and you've got good enough you can actually measure the leakage current in there and this current up this resistor plus this leakage current must equal the current going in.

**Dave Jones:** It's a fundamental law of physics. It's Kirchhoff's current law. And you'll notice that I actually called currents going into the junction positive and those coming out negative. I put them here in the formula like that.

**Dave Jones:** That doesn't have to be the case. You can basically do it make them positive or negative. It makes no difference as long as you're consistent. And we'll actually see this further on in the video where we can actually get negative results and things like this, which actually tells us something fundamental about the circuit that we're trying to analyze.

**Dave Jones:** So, that's it. I know we went into a bit of detail and we came up with some equations here, but it's just a concept. Current in equals current out.

**Dave Jones:** Got it? Beauty. Let's move on to Kirchhoff's voltage law. Kirchhoff's other law is called Kirchhoff's voltage law or KVL for short. And just like Kirchhoff's current law, it's incredibly simple.

**Dave Jones:** It's just a concept. No formula to remember at all and you probably already know it. It's obvious and intuitive, really. What it basically says in a roundabout sort of way, the sum of the applied voltages around a loop, it always has to do with, remember, a circuit doesn't do anything unless you have a loop.

**Dave Jones:** So, the sum of the applied voltages around the loop equals the sum of the the drops around that loop. Simple, right? So, if we take a look at the circuit here, we have a voltage source here, E1, and we have three series resistors like this.

**Dave Jones:** As simple as it gets. So, just like we did for Kirchhoff's current law, we can make an equation. E1 equals Remember, this is the sum of the applied voltages.

**Dave Jones:** In this case, we only have one applied voltage. E1 equals what? The sum of the voltage drops around that loop. So, of course, we're going to have when current flows, we're going to have a voltage drop across We're going to have VR1, voltage drop across R2, voltage drop across R3.

**Dave Jones:** So, you can probably do this yourself even if you're not good at math. It's easy. E1 equals V R1 plus Remember, it's a sum. plus VR2 plus VR3. Bingo.

**Dave Jones:** We have an equation. Easy. So, you might be thinking at this point, "Well, this is all very academic and obvious. Like, what's the point of this? You're just doing math for the sake of, you know, equations for the sake of equations." Well, we'll see later how they actually can come in useful analyzing circuits.

**Dave Jones:** But, yes, this is quite an academic uh concept. And, of course, you just use it every day in circuit theory. Like, you know, you don't even think about it.

**Dave Jones:** You go, "Oh, of course, current in equals current out of a junction." And, of course, uh the voltage drops around the circuit must equal the voltage applied. It's simple.

**Dave Jones:** And it is. There's nothing more complicated about Kirchhoff's uh current law and Kirchhoff's voltage law. And, if you just take that away from this video, then, hey, you've learned the concept.

**Dave Jones:** You don't necessarily have to get into all the academic stuff of deriving equations and solving circuits and all that sort of stuff. But, if you understand the concepts, they're still quite powerful in their own right.

**Dave Jones:** Even if they're bloody obvious like this. You can at least, you know, when you're explaining circuits to people, "Oh, yeah, and just throwing out because of Kirchhoff's current law, blah, blah, blah." You know, it it just makes you sound like you know what you're talking about.

**Dave Jones:** And just like Kirchhoff's current law, we can add more things to this and just expand our equation here. In this case, let's actually be kind of tricky and put in another battery here, but we're actually going to put it a reverse polarity to what we have before.

**Dave Jones:** And let's see what that does to our equation, okay? We've still got E1, okay? The sum of the applied voltages, okay? But, because this voltage here, you have to go around the loop and look at you have to determine a direction of current around the loop like that.

**Dave Jones:** And by convention, as we'll see later, we choose a clockwise current like that. So, if you go around, you notice this battery is going from positive to negative, whereas this one, the current is flowing from negative to positive.

**Dave Jones:** So, E1 will define as positive, but if we define E1 as positive, then uh sorry, E2 here, E2 is negative relative to E1. So, E2 uh E1 - E2 equals the voltage drops.

**Dave Jones:** Aha. So, now maybe you might be able to start to see how we can start forming equations and possibly solving much more complicated circuits using Kirchhoff's current law and Kirchhoff's voltage law, but that's it.

**Dave Jones:** But hey, once again, we can start doing some silly academic stuff, rearranging formulas, but it's kind of important, so let's do that. Let's say let's just rearrange this formula we've got here.

**Dave Jones:** Let's say we just want E1 on the one side here. We can go E1 equals VR1 + VR2 + VR3, exactly the same as before, but the negative E2 becomes a positive E2 like that.

**Dave Jones:** And you can actually see that kind of makes sense if you think about it. If we're talking about a voltage drop across R1, voltage drop across R2, voltage drop across R3, but because E2 is the other direction according to the current flow we chose, it's also a drop.

**Dave Jones:** And the sum of the applied voltages equals the sum of the voltage drops. Bingo. We've got this one is applied, all the others are drops. So, this voltage source, even though we sort of we had it as an applied voltage before, you can also think about it as a voltage drop, depending on which side of the equation it's on.

**Dave Jones:** Like I said, it's academic, but it makes sense. And just like Kirchhoff's current law, you often see it stated as equal to zero. And in fact, that can be one of the definitions of Kirchhoff's voltage law, as well.

**Dave Jones:** You don't necessarily have to think about it like this, you can think about it like this. Our Kirchhoff's voltage law is the algebraic sum of voltages around a loop.

**Dave Jones:** Algebraic is just a fancy word for just for taking into account the sign of the voltages. So, just like we showed here, that this E2 you've got to get its actual sign correct.

**Dave Jones:** That's what algebraic means. It just means taking that into account. So, now we can actually rearrange this formula to make this true as well. We can go VR1 + VR2 + VR3 + uh, E2, exactly the same as before, but E1 now becomes minus E1 equals zero.

**Dave Jones:** Bingo. We've now got this expressed as an algebraic sum of voltages around a loop. And I've probably lost everyone now. You're probably going, "What the what? Why?" Yes, it's all kind of academic, but this concept of being equal to zero, of things adding up around a loop is useful in analyzing complex circuit.

**Dave Jones:** And just like Kirchhoff's voltage law here, Kirchhoff's current law, which I forgot before, you can actually express it as the algebraic sum of currents at a junction equals zero.

**Dave Jones:** Exactly the same concept, rearrange it to zero. And just like Kirchhoff's current law is basically stating the conservation of charge, Kirchhoff's voltage law is essentially stating conservation of energy.

**Dave Jones:** The voltages applied around a circuit must equal the voltages dropped. You know, that power in, power out, conservation of energy, laws, those basic laws of physics, you know? Can't outrun the laws of physics, Captain, you know?

**Dave Jones:** Gustav, smart guy. So, I'm actually going to leave it there for this video and let you digest this. And we'll follow on in the next video, click here to check it out, where we actually apply Kirchhoff's current law and Kirchhoff's voltage law to actually analyze some circuits.

**Dave Jones:** And we'll use some of these equations that we've got here. It's a bit, you know, too advanced for this video just to explain what Kirchhoff's current law and Kirchhoff's voltage law actually is because I could have done this video in 2 minutes.

**Dave Jones:** I could have just said, "The sum of the applied voltages equals the loop, and that's it." And not worried about any of these equations. And it's really just stating the obvious.

**Dave Jones:** Same thing with Kirchhoff's current law as well. And you can, as I said before, think of it that easy. If you just take away from the video that current in equals current out, and the sum of the voltages around a loop actually equals zero, or the voltages applied must equal the voltages dropped, then, well, that's good enough.

**Dave Jones:** You can use that in everyday circuit analysis. But, like I said, it's probably already obvious to you. But, the next video we'll go into what I've got up here in the heading, which is looking at some DC circuit theorems where we apply Kirchhoff's current law, Kirchhoff's voltage law to actually analyze circuits.

**Dave Jones:** So, if you found that useful, please give it a big thumbs up and as always comments down below on YouTube, on the blog website, or in the forum linked down below as well.

**Dave Jones:** If you want the t-shirt, I'll link in my merch page down there where you can sign up and get one of these puppies. So, I'm not sure if it was actually worth 15 minutes explaining this sort of thing.

**Dave Jones:** I went into a bit of detail, but hopefully as you'll see in the next video, I am actually setting this up so that we can actually use these and it is actually a very powerful concept the deeper you go into real, you know, steep circuit theory.

**Dave Jones:** Kirchhoff's current and Kirchhoff's voltage laws and how things equal to zero. Very powerful stuff. So, stick around for the next video. Catch you next time.
