---
video_id: WBfAEeEzDlg
title: EEVBlog #819 - DC Fundamentals Part 4: Kirchhoff's Laws Tutorial
url: https://www.youtube.com/watch?v=WBfAEeEzDlg
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 30, "3": 44, "4": 58, "5": 72, "6": 85, "7": 101, "8": 115, "9": 129, "10": 143, "11": 156, "12": 172, "13": 187, "14": 201, "15": 223, "16": 240, "17": 256, "18": 268, "19": 280, "20": 292, "21": 307, "22": 323, "23": 335, "24": 351, "25": 370, "26": 386, "27": 400, "28": 412, "29": 423, "30": 439, "31": 453, "32": 466, "33": 481, "34": 493, "35": 513, "36": 525, "37": 537, "38": 552, "39": 563, "40": 575, "41": 586, "42": 600, "43": 617, "44": 630, "45": 652, "46": 667, "47": 684, "48": 698, "49": 716, "50": 730, "51": 743, "52": 761, "53": 783, "54": 803, "55": 818, "56": 837, "57": 852, "58": 865, "59": 879, "60": 892, "61": 905, "62": 917, "63": 932, "64": 944, "65": 957}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at one of the most fundamental laws in electronics, as fundamental as Ohm's law. It's called Kirchhoff's laws, or more specifically, Kirchhoff's current law and Kirchhoff's voltage law. Now,

**Dave Jones:** you've probably heard people, including myself, in a lot of my videos just throw away the term Kirchhoff's law. Oh, and you know, by Kirchhoff's law, blah blah blah blah blah. And some people don't actually know what it is, but I bet you you already

**Dave Jones:** fundamentally know it, even if you've never heard of it. Now, we're actually going to get into a little bit of math today, but don't worry about it. Kirchhoff's laws are simple, dead simple, even simpler than Ohm's law, because they're just laws that you don't

**Dave Jones:** even have to remember a formula. They're just basically a concept, a very powerful concept that allows us to do some pretty advanced mathematics in electronics, although we're going to stick to some fairly simple stuff today. As with many things in electronics,

**Dave Jones:** named after the person who discovered it, Gustav. Good on you, Gustav Kirchhoff, in about 1845 or thereabouts. Now, there are two fundamental Kirchhoff's laws. The first one we're going to take a look at is Kirchhoff's current law, or KCL for short. The other

**Dave Jones:** one is Kirchhoff's voltage law, and we'll do that next. So, let's take a look at the current law. It's real easy. How easy? Let me show you. Kirchhoff's current law states in a roundabout way, the sum of currents

**Dave Jones:** into a junction equals the sum of currents out of a junction. Current in must equal current out. That's it. That's That's the entirety of Kirchhoff's current law. Nothing more complicated than that. So, just like the fundamental laws of physics, like the

**Dave Jones:** conservation of energy, effectively what Kirchhoff is saying here is this is a conservation of charge. If you put charge into a loop circuit, it must come out. Charge in equals charge out. Or in this specific case, we're talking about

**Dave Jones:** a junction point in a circuit. Current in equals current out. It's that easy. You already know it. It's fundamental. It's obvious. So, fundamentally, that's it. You don't need to know any more than that. You now know Kirchhoff's current

**Dave Jones:** law. Current in equals current out. It's too simple. But, eh, there's some powerful things we can do with it. So, let's take a look at an example, shall we? We've just got a resistor here and two resistors in parallel here that

**Dave Jones:** we've got current flowing in I1 here. Let's just assume it's flowing in here and it's into this junction. You remember we're talking about a junction here. And then, we've got two paths coming out. So, we've got I3 coming out

**Dave Jones:** and I2 coming out here. So, we can actually have a formula. We can go I1 = I2 + I3. Remember, the sum of the currents into the junction, in this case we've only got one, but we could have more than

**Dave Jones:** one, and equals the sum of the currents out of the junction. So, I1 is in, I2 and I3 are out. That's it. And if we had another current coming in here, for example, like this, and going in, and we

**Dave Jones:** can call that I0, it'll just be I0 + I1. Remember, the sum of the currents in equals the sum of the currents going out. But, sometimes it's actually more powerful mathematically to say this, which is exactly the same. We're

**Dave Jones:** basically just rearranging it. We can go I0 + I1 I2, and I'll explain why in a second, - I3 = 0. It's basically just a rearrangement of that formula. So, what this rearrangement of the formula means, and you typically would write this like

**Dave Jones:** directly like this straight off the bat. And we'll do this in further examples to come. Basically, any current flowing into a junction, you define that as a positive current. So, I0 is flowing in, so it's positive I0 plus I1 is also flowing in to the

**Dave Jones:** junction, so it's a positive. But, I2 is flowing out of the junction, so you actually define that as a negative current. And likewise for I3 three there, it's a negative current as well. So, you come up with this equation like

**Dave Jones:** this. And you can write the equation for any number of currents flowing in or any number of currents flowing out of a junction, even if you've got one current flowing in and one current flowing out, you can still write the basic equation.

**Dave Jones:** And the thing about this is it's not a formula that you have to remember. It's just a concept that current in equals current out. Now, of course, I can build up a boring circuit and actually demonstrate that current in equals

**Dave Jones:** current out, but there's no point, but I'll just give you one little simple example here you where you might use Kirchhoff's current law in the real world, for example, to analyze a circuit here. Let's take an op amp. We've got an

**Dave Jones:** inverting configuration. You should be familiar with something like this. We've got a positive voltage here, and by op amp action, one of the basic rules of the op amp is our non-inverting terminal here is at 0 V. It's a ground, so therefore the

**Dave Jones:** inverting terminal is also at ground. So, we're going to have a current flowing through like this. So, remember, look, we've got a current flowing into a junction point right here, okay? Where does it flow? Well, it can't flow into

**Dave Jones:** here, can it, because the input impedance of an op amp is supposed to be infinite or an ideal one. So, it's got to flow all the way up here like this. So, we've got a current coming out. But,

**Dave Jones:** in the real world, a practical op amp will have some input leakage current in here, okay? So, we've got IL there, for example, leakage. So, this could be, say, I out and this is I in. So, in this case, you can actually come

**Dave Jones:** up with the equation that I in equals I out plus I L. Because, remember, current in must equal current out. We've got two currents coming out of a junction. The one that goes up this resistor, the feedback resistor here, and the tiny

**Dave Jones:** little current in there, they must be equal. And if you've got a practical op-amp and you've got good enough you can actually measure the leakage current in there and this current up this resistor plus this leakage current must equal the

**Dave Jones:** current going in. It's a fundamental law of physics. It's Kirchhoff's current law. And you'll notice that I actually called currents going into the junction positive and those coming out negative. I put them here in the formula like that. That doesn't have to be the case.

**Dave Jones:** You can basically do it make them positive or negative. It makes no difference as long as you're consistent. And we'll actually see this further on in the video where we can actually get negative results and things like this,

**Dave Jones:** which actually tells us something fundamental about the circuit that we're trying to analyze. So, that's it. I know we went into a bit of detail and we came up with some equations here, but it's just a concept. Current in equals

**Dave Jones:** current out. Got it? Beauty. Let's move on to Kirchhoff's voltage law. Kirchhoff's other law is called Kirchhoff's voltage law or KVL for short. And just like Kirchhoff's current law, it's incredibly simple. It's just a concept. No formula to remember at all

**Dave Jones:** and you probably already know it. It's obvious and intuitive, really. What it basically says in a roundabout sort of way, the sum of the applied voltages around a loop, it always has to do with, remember, a circuit doesn't do anything

**Dave Jones:** unless you have a loop. So, the sum of the applied voltages around the loop equals the sum of the the drops around that loop. Simple, right? So, if we take a look at the circuit here, we have a

**Dave Jones:** voltage source here, E1, and we have three series resistors like this. As simple as it gets. So, just like we did for Kirchhoff's current law, we can make an equation. E1 equals Remember, this is the sum of the applied

**Dave Jones:** voltages. In this case, we only have one applied voltage. E1 equals what? The sum of the voltage drops around that loop. So, of course, we're going to have when current flows, we're going to have a voltage drop across We're going to have

**Dave Jones:** VR1, voltage drop across R2, voltage drop across R3. So, you can probably do this yourself even if you're not good at math. It's easy. E1 equals V R1 plus Remember, it's a sum. plus VR2 plus VR3. Bingo. We have an equation.

**Dave Jones:** Easy. So, you might be thinking at this point, "Well, this is all very academic and obvious. Like, what's the point of this? You're just doing math for the sake of, you know, equations for the sake of equations." Well, we'll see

**Dave Jones:** later how they actually can come in useful analyzing circuits. But, yes, this is quite an academic uh concept. And, of course, you just use it every day in circuit theory. Like, you know, you don't even think about it. You go,

**Dave Jones:** "Oh, of course, current in equals current out of a junction." And, of course, uh the voltage drops around the circuit must equal the voltage applied. It's simple. And it is. There's nothing more complicated about Kirchhoff's uh current law and Kirchhoff's voltage law.

**Dave Jones:** And, if you just take that away from this video, then, hey, you've learned the concept. You don't necessarily have to get into all the academic stuff of deriving equations and solving circuits and all that sort of stuff. But, if you

**Dave Jones:** understand the concepts, they're still quite powerful in their own right. Even if they're bloody obvious like this. You can at least, you know, when you're explaining circuits to people, "Oh, yeah, and just throwing out because of Kirchhoff's current law,

**Dave Jones:** blah, blah, blah." You know, it it just makes you sound like you know what you're talking about. And just like Kirchhoff's current law, we can add more things to this and just expand our equation here. In this case, let's

**Dave Jones:** actually be kind of tricky and put in another battery here, but we're actually going to put it a reverse polarity to what we have before. And let's see what that does to our equation, okay? We've still got E1, okay? The sum of the

**Dave Jones:** applied voltages, okay? But, because this voltage here, you have to go around the loop and look at you have to determine a direction of current around the loop like that. And by convention, as we'll see later, we choose a

**Dave Jones:** clockwise current like that. So, if you go around, you notice this battery is going from positive to negative, whereas this one, the current is flowing from negative to positive. So, E1 will define as positive, but if we define E1 as

**Dave Jones:** positive, then uh sorry, E2 here, E2 is negative relative to E1. So, E2 uh E1 - E2 equals the voltage drops. Aha. So, now maybe you might be able to start to see how we can start forming equations and possibly

**Dave Jones:** solving much more complicated circuits using Kirchhoff's current law and Kirchhoff's voltage law, but that's it. But hey, once again, we can start doing some silly academic stuff, rearranging formulas, but it's kind of important, so let's do that. Let's say let's just

**Dave Jones:** rearrange this formula we've got here. Let's say we just want E1 on the one side here. We can go E1 equals VR1 + VR2 + VR3, exactly the same as before, but the negative E2 becomes a positive E2

**Dave Jones:** like that. And you can actually see that kind of makes sense if you think about it. If we're talking about a voltage drop across R1, voltage drop across R2, voltage drop across R3, but because E2 is the other direction according to the

**Dave Jones:** current flow we chose, it's also a drop. And the sum of the applied voltages equals the sum of the voltage drops. Bingo. We've got this one is applied, all the others are drops. So, this voltage source, even though we

**Dave Jones:** sort of we had it as an applied voltage before, you can also think about it as a voltage drop, depending on which side of the equation it's on. Like I said, it's academic, but it makes sense. And just

**Dave Jones:** like Kirchhoff's current law, you often see it stated as equal to zero. And in fact, that can be one of the definitions of Kirchhoff's voltage law, as well. You don't necessarily have to think about it like this, you can think about it like

**Dave Jones:** this. Our Kirchhoff's voltage law is the algebraic sum of voltages around a loop. Algebraic is just a fancy word for just for taking into account the sign of the voltages. So, just like we showed here, that this E2 you've got to get its

**Dave Jones:** actual sign correct. That's what algebraic means. It just means taking that into account. So, now we can actually rearrange this formula to make this true as well. We can go VR1 + VR2 + VR3 + uh, E2, exactly the same as before, but

**Dave Jones:** E1 now becomes minus E1 equals zero. Bingo. We've now got this expressed as an algebraic sum of voltages around a loop. And I've probably lost everyone now. You're probably going, "What the what? Why?" Yes, it's all kind of academic,

**Dave Jones:** but this concept of being equal to zero, of things adding up around a loop is useful in analyzing complex circuit. And just like Kirchhoff's voltage law here, Kirchhoff's current law, which I forgot before, you can actually express it as

**Dave Jones:** the algebraic sum of currents at a junction equals zero. Exactly the same concept, rearrange it to zero. And just like Kirchhoff's current law is basically stating the conservation of charge, Kirchhoff's voltage law is essentially stating conservation of energy. The voltages applied around a

**Dave Jones:** circuit must equal the voltages dropped. You know, that power in, power out, conservation of energy, laws, those basic laws of physics, you know? Can't outrun the laws of physics, Captain, you know? Gustav, smart guy. So, I'm actually going to leave it there for

**Dave Jones:** this video and let you digest this. And we'll follow on in the next video, click here to check it out, where we actually apply Kirchhoff's current law and Kirchhoff's voltage law to actually analyze some circuits. And we'll use

**Dave Jones:** some of these equations that we've got here. It's a bit, you know, too advanced for this video just to explain what Kirchhoff's current law and Kirchhoff's voltage law actually is because I could have done this video in 2 minutes. I could have just said, "The

**Dave Jones:** sum of the applied voltages equals the loop, and that's it." And not worried about any of these equations. And it's really just stating the obvious. Same thing with Kirchhoff's current law as well. And you can, as I said before,

**Dave Jones:** think of it that easy. If you just take away from the video that current in equals current out, and the sum of the voltages around a loop actually equals zero, or the voltages applied must equal the voltages dropped, then, well, that's

**Dave Jones:** good enough. You can use that in everyday circuit analysis. But, like I said, it's probably already obvious to you. But, the next video we'll go into what I've got up here in the heading, which is looking at some DC circuit

**Dave Jones:** theorems where we apply Kirchhoff's current law, Kirchhoff's voltage law to actually analyze circuits. So, if you found that useful, please give it a big thumbs up and as always comments down below on YouTube, on the blog website, or in the forum linked down below as

**Dave Jones:** well. If you want the t-shirt, I'll link in my merch page down there where you can sign up and get one of these puppies. So, I'm not sure if it was actually worth 15 minutes explaining this sort of thing. I went into a bit of

**Dave Jones:** detail, but hopefully as you'll see in the next video, I am actually setting this up so that we can actually use these and it is actually a very powerful concept the deeper you go into real, you know, steep circuit theory. Kirchhoff's

**Dave Jones:** current and Kirchhoff's voltage laws and how things equal to zero. Very powerful stuff. So, stick around for the next video. Catch you next time.
