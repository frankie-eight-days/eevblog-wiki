---
video_id: 8f-2yXiYmRI
title: EEVblog #820 - DC Fundamentals Part 5: Mesh & Nodal Circuit Analysis Tutorial
url: https://www.youtube.com/watch?v=8f-2yXiYmRI
source: youtube-asr
---

**Dave Jones:** Hi, welcome to another Fundamentals Friday video. This is a follow-on to a previous video I did on Kirchhoff's current law and Kirchhoff's voltage law. So, click here if you haven't seen that cuz that was a build-up video to what

**Dave Jones:** we're going to do in today's video, which is have a look at some basic DC circuit theorems. Specifically, nodal analysis, mesh analysis, and superposition theorem as well. And we're going to actually apply Kirchhoff's voltage law and Kirchhoff's current law, which we

**Dave Jones:** learned in the previous video, to analyze a real basic circuit like this. It doesn't get much simpler than this, but you'll find there's actually a little bit of math involved, little bit of cleverness in how you actually solve

**Dave Jones:** this. So, what we're going to do here is we're going to solve this basic circuit in three different ways: nodal analysis, mesh analysis, and superposition theorem, and hopefully come up with the same answer for all three. Three different methods to analyze it. First

**Dave Jones:** one we're going to take a look at is nodal analysis. Now, nodal analysis uses KCL, Kirchhoff's current law that we looked at in the previous video to actually solve this value. And what we want to solve is the current through

**Dave Jones:** this resistor here. So, what we've got is a basic circuit with three resistors and two voltage sources here. This is one of your like your more classic textbook circuits they give you when you're learning nodal and mesh analysis

**Dave Jones:** and Kirchhoff's current laws and things like that and solving them. And it's a little bit tricky. It's actually not obvious at first glance. Um by all means, go away right now if you don't know about Kirchhoff's current laws and

**Dave Jones:** try and solve this and see what you get without using a circuit simulator. Yes, we can just whack this into a circuit simulator and calculate the current down R2 here. Easy peasy, right? Done in a couple of minutes. But really, we're

**Dave Jones:** trying to learn fundamental electronics here. It's a fundamental theory, nodal analysis and mesh analysis, that enables really deeper, rich mathematical treatment and calculation of lots, tons of stuff in electronics. But, we're going to look at a basic circuit

**Dave Jones:** today so that you can understand how these techniques work. In this case, nodal analysis. Fun.

**Dave Jones:** Right. So, what we've got? Two different voltages just to mix it up a little bit. This one's 10 V positive up the top. This one's 1 V I've labeled them E1 and E2. So, there's two voltage sources and

**Dave Jones:** three resistors like this. We want to determine the current through R2. We've got three different value resistors here. I've just chosen them different values because we can. And basically, we've got a node here. Hence, the name nodal analysis. And this is

**Dave Jones:** important to understand. We've got one node in this circuit. I've labeled it A. And you'll see why in a minute. Now, we could actually use the same nodal analysis technique to analyze any number of nodes in a circuit. But, today we're

**Dave Jones:** going to simplify it to one because there's already going to be enough involved in actually solving just one node here. And you might think, "But, Dave, we've got two nodes. There's this other one down here." Well, no, because

**Dave Jones:** what we've got is when doing nodal analysis, we need a reference point. So, we're going to call it ground like that. We're just going to put the ground symbol. We're going to say this is our reference point. So, we don't have to

**Dave Jones:** worry about this node. We really want to solve this node up here cuz what we want is like the voltage at node A relative to our reference point here. This point is exactly the same. So, there's no point analyzing that node. So,

**Dave Jones:** basically, only got one node in this circuit that's of particular interest to us and we want to solve for. Now, of course, in nodal analysis, we can actually choose any reference point we want. It's pretty much arbitrary. But,

**Dave Jones:** hey, we're just going to pick this. It makes it easy and familiar to you. Now, this node is a junction, is it not? We learned in the previous video Kirchhoff's current law that uh the current entering into a junction must

**Dave Jones:** equal to the current leaving the junction. Or, in other words, the algebraic sum of the currents at a particular junction is equal to zero. And we're going to use that formula we learned last time to analyze all the

**Dave Jones:** equation that we uh learned last time to analyze this thing. Now, by convention, although you don't have to do this, by convention, we are going to assume that all currents uh leaving the node like this. There's no current flowing in. And yeah, that's

**Dave Jones:** not possible in practice, okay? But to But trust me, it'll work out in the end cuz technically, we don't know. Without, you know, analyzing the circuit, we don't know which way the currents are flowing. Depends on the voltages, so

**Dave Jones:** they could be flowing in, out, we don't know. So, we're choosing an arbitrary reference point. And as I said, by convention, nodal analysis, just have all currents leaving the node like this. So, we'll draw direction arrows. Now, we'll start off by deriving the

**Dave Jones:** equations for each current, which I've labeled I1, I2, and I3 here. So, we're fairly consistent. R1 equals I1, etc. So, you know, it just keeps it nice and tidy. So, we start by deriving our equation, okay? So, I1

**Dave Jones:** What What's I1 equal to? Let's go back to Ohm's law. We know I1 is flowing through R1. So, how do you calculate the current through a resistor? Voltage and the resistance, right? So, we can go VA because the current is flowing A is more

**Dave Jones:** positive. We're talking about conventional current flow. A is more positive than this point over here. So, we go VA minus this voltage here, which is actually E1. We could have called it like node B if we're doing, you know, a multi-node um

**Dave Jones:** analysis and things like that. But in this case, it's E1. So, VA - E1. That is the voltage difference across the resistor, the voltage drop across the resistor there. And divided by V on R. I = V on R, Ohm's law. R 1.

**Dave Jones:** Too easy. And we can just plug in the numbers that we know. R1 is 10 ohms, E1 is in this case 1 volt, and we drop the units here. It just makes it easy, trust me. And so, our our now our equation is

**Dave Jones:** VA - 1 / 10. That is the equation for I1. Beauty. Two more to go. So, let's do I2. What is it? Wow, it's pretty easy. Remember, it's always a referenced back to this reference point, VA, the voltage

**Dave Jones:** at point A. What's the differential voltage, just like we got here? Instead of E1, look, it's ground. It's connected directly. So, VA, it's minus nothing. So, it's just VA on R. Too easy. Ohm's law. And I forgot that's

**Dave Jones:** actually R2 there. And we plug in the number that we know. We know R2. We still don't know what VA is. We have no idea. It'll come out in the wash. And so, it's VA on 20. And I3, well, pause

**Dave Jones:** the video and try and do it yourself. It's easy peasy. Look, it's going to be once again VA, our point. Look, our current is flowing out. So, VA is the more positive side according to the current that we've chosen arbitrarily.

**Dave Jones:** So, VA minus Well, the voltage on this side to get the differential voltage across the resistor. In this case, it's not E1 like before, it's E2. So, it's minus E2. It's exactly the same uh formula that we got before over R

**Dave Jones:** 3. Too easy. And then we can just plug in the numbers that we know. We've got VA minus E2 is 10 volts, drop the units, over R3 30 ohms. Bingo. We now have the equations for all three of our currents.

**Dave Jones:** Beautiful. Now, we apply Kirchhoff's current law. Remember Kirchhoff's current law? The algebraic sum of the currents at a junction equals to zero. There's our currents, I1, I2, I3 equals zero. Bingo, we just write it down. I1 plus because it's the algebraic sum,

**Dave Jones:** well, it's the sum plus I2 plus I3 equals zero. That is our Kirchhoff's current law equation for this node. So, that's called our nodal equation and we know all these value, well, we know the equations for I1, I2, and I3. So, we

**Dave Jones:** just plug them in. There we go, VA minus one on 10. That's I1 and then I plus I2 plus I3 equals zero. Now, all we got to do is solve the nodal equation and our value VA of voltage at that node will

**Dave Jones:** pop out. And that's the idea, whole idea of nodal analysis, we can calculate the voltage at a particular node. Even though I think I said right back at the start we won't actually calculate the current I2 down here. Well, nodal

**Dave Jones:** analysis is actually calculating voltages, but once we get VA here, bingo, it's just relative to earth. Ohm's law, VA on R2, that'll give us our current. So, this looks a little bit tricky and if you're not good at

**Dave Jones:** algebra, then well, you might just whack it in a calculator or Wolfram Alpha or something like that and just, you know, VA will just pop out. But hey, we'll do it simply. We'll just like expand this out. So, VA minus one on 10 can be

**Dave Jones:** written as VA on 10 minus one on 10. So, you just expand that term out and then VA on 20 still remains VA on 20 and do the same expansion here, VA on 30 minus 10 on 30. So, just expand that out equal

**Dave Jones:** to zero. That just makes it a bit easier to reduce it down and get the value of VA. At least that's how I do it. And then we can just further rearrange this and expand it out so that we just

**Dave Jones:** looking so there's no divisions in there. We're just looking at additions and multiplications here. This is just the way I happen to do it. So VA on 10 is 0.1 * VA. You just bring the 10 up minus 1 on 10 0.1 plus so VA on 20 now

**Dave Jones:** becomes 0.05 so 1 on 20th * VA. So 0.05 VA. You typically don't show the multiplication sign in there. You just go 0.05 VA. It's typically some people put the little dot in there. Whichever way you want to do it. I'm just going to

**Dave Jones:** leave it like that. And then this term here can become 0.333 VA minus 10 on 30 is 0.333 equals zero once again. It's looking pretty easy now. So what we do now, this is all basic math. You're you know, probably familiar with if

**Dave Jones:** you've done any sort of you know, high school type math. You should know all this. Then we can gather our like terms. So we can actually just ignore the brackets. You can take those out. Our minus 0.33 comes over the other side of

**Dave Jones:** the equal sign becomes plus 0.333. The minus 0.1 comes over and becomes plus 0.1 over here. And then we can actually group these terms together for VA. 0.1 VA 0.05 VA and 0.333 VA becomes 0.1 plus 0.05 plus 0.0333

**Dave Jones:** * VA. So now we've only got the single VA equals that. We can now easily solve for VA. So it's simple. We just add all these up. That becomes 0.1833. Take it to the other side. Divide it. This is 0.445.

**Dave Jones:** Just do that. VA equals 0.4333 divided by 0.1833. It it equals 2.3636 repeater actually volts. Bingo. Tada! We've just solved We've just done nodal analysis to solve for node A using Kirchhoff's current law. Beauty. So, as we originally asked, what is the current

**Dave Jones:** through R2 here? What is I2? Well, Ohm's law because we've already done our nodal analysis beauty, we know what VA is. Uh VA um I2, Ohm's law equals VA on R2. .233636 repeater on 20 0.1181 Oh, 0.11818 repeater actually.

**Dave Jones:** Amps. That's it. Beauty. So, hopefully that wasn't too hard and you followed through and it looks like but it's easy. Kirchhoff's current law and we just did some but derived some basic equations for the various currents, used our Kirchhoff's current

**Dave Jones:** law equals to zero. You see how I promised it would be powerful to analyze this sort of circuit and we went through and just plugged in the numbers we derived and we got our answer. We worked out what VA

**Dave Jones:** here is and we can from that we can work out anything else. And as I said, we can do that for any number of nodes. You would just repeat this process for all the different nodes and then you'd end

**Dave Jones:** up with actually some quite complex equations where you're going to have to do some uh matrices you know, determinants and things like that to actually get your final answer. It's a bit more messy, but there you go. That's

**Dave Jones:** the sort of working. You can see it's not that hard once you actually sit through and go and do it. But yeah, it does look ugly. I got to admit. It's easier just to type it into Wolfram Alpha or use your formula solver on your

**Dave Jones:** calculator, but we're learning. So, you're now an expert at nodal analysis. Let's go on to mesh analysis and use exactly the same circuit and see if we can get the value of current through R2 again like we got before. We want

**Dave Jones:** Remember, we're looking for the answer 0.11818 repeater. That's the answer we want to get. Let's see if we can repeat it using mesh analysis. I'm pretty confident in the basic laws of engineering. And I was just testing you because I got

**Dave Jones:** something wrong. At this I had 333 here. It should be 0.033 and yeah, there you go. Fixed. I was just testing you. And if you're wondering, what use is this in the real world? Well, you know that circuit simulator you take for

**Dave Jones:** granted and just produces magical results. How can analyze the circuit with hundreds of nodes in it and do it does it at each time step? How does it know what the voltages and currents are? I'll give you one guess.

**Dave Jones:** Now, next up we have yet another DC circuit theorem. This one's called mesh analysis and just like nodal analysis before, this one uses Kirchhoff's laws it but instead of using Kirchhoff's current law like we used last time, you'll notice I've changed it to KVL,

**Dave Jones:** Kirchhoff's voltage law. That's what's used in mesh analysis. Now, the difference here is that nodal analysis is what you would typically use to calculate a voltage at a particular node or junction within a circuit. But if you want to calculate a current like as what

**Dave Jones:** our original question was, then mesh analysis might be a better technique to use cuz we're going to look at calculating the current through I2 this time and that's what mesh analysis is good at, calculating currents in a circuit. We don't care

**Dave Jones:** about nodes. In fact, I haven't even labeled this node node A. It doesn't actually matter and we don't need any circuit reference point like we did last time cuz we're not calculating any reference voltages like this. We're looking at loop currents. So, what is a

**Dave Jones:** mesh? What is mesh analysis all about? It's a little bit confusing, but stick with me. A mesh is an individual loop within a circuit. So, for example, E1, R1, and R2 here, if we have a current which goes around

**Dave Jones:** like this, that is a mesh. And likewise, I'll draw it in a different color, you'll see why in a minute, we can have another loop all around here like this. This is also a mesh. Now, we've also got another loop around the

**Dave Jones:** outside here, but that is not a mesh. And this is pretty critical. You can't have a mesh within inside a mesh. So, a mesh is just sort of like the smallest loop possible within a circuit. So, this one has this circuit has two meshes, and

**Dave Jones:** we'll actually solve these individually, and then bingo, out will pop our answer for the current through R2 at the end. And yes, mesh analysis is more fun than a barrel of monkeys. Oh, let's go. First of all, we need to label these currents

**Dave Jones:** here. So, I'm going to label this I1, and I'm going to label this one I2. And just like we did in nodal analysis, and analysis, we're going to get some equations for these two currents, and then solve them. Exactly, you know,

**Dave Jones:** basically the same technique as what we did in nodal, except we're solving currents now instead of solving node voltages. Now, mesh analysis is sometimes known as loop analysis or loop equation analysis or something like that. And you can see why, because it's

**Dave Jones:** to do with solving current loops through a circuit. Now, what is Kirchhoff's voltage law? If you remember from the previous video, it's the algebraic sum of the voltages around a closed loop must equal to zero. Bingo. What You're probably guessing

**Dave Jones:** what our equation's going to look like. Now, just like nodal analysis, our current directions that we've drawn in here are arbitrary. They can be any direction as long as you're consistent. But by convention, when you're doing mesh analysis like this, you should use uh

**Dave Jones:** clockwise current flow like this. That's why I've drawn them in going clockwise. And this is conventional current flow. You always do conventional, not electron current flow. But as I said, you can actually do it in the opposite direction. You can use electron current

**Dave Jones:** flow if you want, and it'll, you know, all the numbers will come out in the wash, but this is the convention. Now, this is the magic part about mesh analysis. We've assumed that the current is going in a clockwise direction like

**Dave Jones:** this. Now, it could actually be flowing in the other direction. The current through R1 might not be flowing that way. It could be flowing that way. It and uh R2 likewise, look, you'll see that I1 is actually flowing down R2,

**Dave Jones:** whereas I2 is flowing up R2. This can't happen. You can't have a current flowing down and up, right? It's impossible. And yes, that's true. But this is just for the purposes of mathematical analysis. And this is the magic part you'll see in the end how

**Dave Jones:** that if we've assumed the wrong direction for the current flow, it'll come out as a negative answer at the end. And that actually tells us something, gives us information about our circuit. Wait and see. It's magic. So, we're going to choose this starting

**Dave Jones:** point down here. We're going to derive our equation for the various voltages and voltage voltages generated and the voltage drops in this particular loop, I1 here, okay? And as I said, it must equal zero. That's Kirchhoff's voltage law, okay? So, I start out with E1 here.

**Dave Jones:** So, E1 We'll start out with this point, okay? E1, it's positive up here. So, it's going the current flow is going from negative up to positive. So, that means it is a positive voltage. It's generating a voltage in the circuit,

**Dave Jones:** okay? So, we don't go E1 it's positive. You don't have to put the positive in there. It's just not negative, okay? So, it's actually generating a voltage. And then, we have a look R1 here. What have we got? It's a

**Dave Jones:** voltage drop. So, we're actually going to have a positive voltage here and a negative voltage here. As opposed to this one, we went from negative to positive. So, it's a it's generating a voltage. So, it's positive. This one is

**Dave Jones:** going from positive to negative cuz resistors drop voltage, okay? We know because it's a resistor. You know how resistors work. They don't generate voltage. They actually drop voltage when you pass current through. So, it's a voltage drop. So, it's actually minus.

**Dave Jones:** And what is the voltage drop on here? Easy. It's uh one. You got it. Times I1. Ohm's law. Voltage equals I * R or R * I. I'm going to put it in R first, but it doesn't matter. You'll see

**Dave Jones:** why in a minute. And then, well, we've got another one. It flows down through R2 here. This is going to be positive. This is going to be negative here. So, we've got another voltage drop. So, it's minus uh

**Dave Jones:** two in this case. And the current is I1. So, that's our voltage drop. And we're back to our point here. But, we're not finished yet. Look, I2 is also flowing through here. So, we have to take I2 into account. And what is I I2

**Dave Jones:** is going from a negative to a positive, right? So, in this case, it's negative to a positive. It's like it's generating a voltage because it's going in the opposite direction to I1 here. Now, here's the tricky bit, and

**Dave Jones:** you'll have to stick with me with with this. You can see that I2 is flowing in this direction. So, just like I1 flowed in this direction and we have a positive here and a negative here, the same thing's going to happen here. And I'm

**Dave Jones:** going to draw it in blue because it's of by I2 here. So, we're going to have across R2 positive and negative like that. And you'll notice that it's actually the opposite polarity. But, we're writing our term for I1 here. So,

**Dave Jones:** what effect does I2, because it's interacting on I1, what effect does it have relative to the direction of I1? Well, if I1, you remember it's going from negative to positive in this case because it's being influenced by I2. I1

**Dave Jones:** relative, so I just picture I1 coming around here going on this side here. It's going from a negative to a positive. What does that mean? Just like here, it's going from a negative to a positive. It's a positive voltage. It's

**Dave Jones:** generating a voltage in a circuit. Even though it's a resistor, the effect of I2 flowing in this direction, which which which we've chosen arbitrarily, remember, flowing in this direction is causing a voltage to be up induced into the circuit. So, it's

**Dave Jones:** a positive voltage just like as if it was actually a little battery, a little power supply in there generating that voltage. So, it's going to be positive uh two again times not I1, it's I2. Like that. Bingo. And that is our

**Dave Jones:** equation equals to zero like that. And you can see how the color coding really helps you identify which terms are relative and caused by which particular currents. So, we've actually got four terms in our equation there. Even though you might

**Dave Jones:** think with at first glance I1 is only being influenced by three particular parts in the circuit, you're forgetting that I2 is having an influence as well. And if we had if this was a bigger circuit and we had another mesh up here

**Dave Jones:** like this and a current circulating around here, we'd have a fifth term on here doing the same thing. We'd have to take into account I3 up here, and it'll be I1 * I3, and that'll be another positive term in here because the

**Dave Jones:** current would be flowing in a clockwise direction from negative to positive like this. Now, let's do the equation from I2. Once again, we have to start a choose a starting point, and I can choose down here, but I'm actually

**Dave Jones:** going to choose up here and go down and do the voltage first just so our terms are like in the same order here. It doesn't matter. It, you know, it makes no difference. It's just I want it to be

**Dave Jones:** a bit neater. So, I'm going to start with this point up here. So, our current is flowing in a clockwise direction. So, this is our starting point. Our current is actually flowing from Look, a battery is positive to negative. It's different

**Dave Jones:** to what we had over here. It was flowing from negative to positive. So, it was actually producing voltage in the circuit. Now, it's flowing from positive to negative just like it was here. So, this battery is effectively working like

**Dave Jones:** a voltage drop based on the arbitrary current direction that we chose. So, you guessed it. It's negative E2 just like it's a drop. Haha, brilliant. So, you've got to be so careful doing these things. You can easily miss that and go, "Oh, it's a

**Dave Jones:** voltage. It generates voltage in a circuit." But, no, it can be a drop. Depends on the current direction. And you know, once you do this a few times, you'll get to, you know, you'll get to know and love this technique, and trust

**Dave Jones:** me, it'll all come out in the end. It's brilliant. So, what's our next term? Our next term, okay, we've done this point here. Our current Now, we're looking at R2. So, it's flowing from positive to negative. It's a drop. Okay? So, it's

**Dave Jones:** negative R2 I2. Okay? So, that's our voltage across there, and then it goes through R3 like this. So, once again, it's positive negative like that. It's a drop cuz it's just a resistor. So, we've got drop drop drop. Everything's dropping. God, where

**Dave Jones:** are the voltages being generated? Wait for it. Okay, so we've got uh R3 this time times I 2. But, aha, just like before, we have a fourth term, which I'll draw in red because I1 now interacts with I2 over

**Dave Jones:** here. Now, we've got to look at the direction that it does that. Once again, this is flowing around like this. It's positive negative, so it was a drop before in the previous equation. Where is it? R2. It was a drop. It was

**Dave Jones:** negative. But, now you can see that relative to I2 a certain Look, just imagine this blue arrow going around on this side now. It's going from negative to positive. Aha, it's a voltage generated. Brilliant. So, that's a plus. So, I1 is

**Dave Jones:** actually generating a voltage into the I2 loop equation here. Fantastic. I love this. Aha. So, we're looking So, what does it do? R2 plus R2 times I1 cuz it's I1 doing the interacting. And then Ta-da! Equals to zero. We have

**Dave Jones:** two loop equations. Now, all we have to do is solve them. So, just like before in the nodal analysis, we've got some unknowns in this circuit. We know what the resistor values are. We know what the voltage values are. So, we can plug

**Dave Jones:** those into our equation here. I've moved the one we just derived down here cuz I need some space to actually do this. So, what we look at at E1? E1 is 1 V. Okay, it's positive 1 V, and then minus

**Dave Jones:** R1 is 10. We don't know what I1 is yet. It's going to come out in the wash. So, 10 I1 minus R2, which is 20 ohms, times I1, still don't know what I1 is. And then, we can go plus

**Dave Jones:** R2, which is 20 again, and we don't know what I2 is yet. Once again, it will come out in the wash. So, bingo, we can now reduce that and solve it. And just like before, we can leave it like that and

**Dave Jones:** just shove it into our equation solver, how solve it, whatever method you prefer. But we can actually reduce that a bit further. We can just group like terms yet again, 1 minus Uh in this case, we've got two I1 terms here, so we

**Dave Jones:** can just 10 minus 20 like that, so we can go minus 30 I1, and then we can just go plus 20 I2, and that equals zero. And likewise, with this one down here, we can go minus E2, which is 10, minus R2, which is 20,

**Dave Jones:** I2, minus R3, which is 30 ohms. Once again, we take out the units, I2, and then we go plus R2, which is 20, and then I1, which we don't know yet, and bingo, equals to zero. So, I've reduced

**Dave Jones:** that one as well, just gathered the like terms, 20 and 30 there, and bingo, we now have our two equations which we need to solve. Now, let's take a look at these. You can see that they contain two

**Dave Jones:** unknown terms, I1 and I2, I2 and I1 there. And that's a bit tricky. You know, usually you might solve that with by determinants, with a matrix. For example, you might, as I said, plug it into your the formula solver on your

**Dave Jones:** calculator, which does the same thing. You can actually expand it out and do some things and try and solve it manually and I probably don't have the space to do here. So, let's solve this a modern way, shall we? We'll go to the

**Dave Jones:** internet, we'll use Wolfram Alpha to actually plug these equations in and we'll get the answers for I1 and I2, our two unknown terms. I know a lot of people say that's cheating, but this is not a math video. I'm not going to show

**Dave Jones:** you how to solve for two unknowns in these equations. You know, do it however, you know, whatever floats your boat. Let's go to the internet. Okay, so here we go. We got to cheat like any modern student does and we're going to go to Wolfram

**Dave Jones:** Alpha, but you could do this formula solver on your calculator or you can do it in your head or you can do it with a pencil and paper, however you want to do it, whatever method you want to do to

**Dave Jones:** solve for two unknowns. So, we can actually enter the equation here. I've entered the first one in here and then we can actually enter the second one by going comma like that and then typing in our second equation and it'll automatically

**Dave Jones:** know that we've got terms in there. Now, I can't label them I1 and I2 cuz I think it thinks they're complex numbers or something like that. So, I1 is going to be A and I2 is going to be B. So, you'll

**Dave Jones:** notice that we've got two unknowns in there. So, let's just press enter. Magic happens. Magic happens. Wait for it. Ta-da! We've got our answers as actual fractions cuz it tries to give you an an exact form, but you can

**Dave Jones:** actually go to approximate form here and bingo, there's our two answers. A, which is I1 equals -0.13636 amps and B, which is I2, is approximately equal to -0.25455 amps. Let's go back to the whiteboard. So, Bob's your uncle. We've solved our

**Dave Jones:** two unknowns, I1 and I2. So, we know everything in this circuit now. We know the voltages, we know the resistances and we know the currents flowing through each component. Well, we kind of do, and this is the magic I was telling you

**Dave Jones:** about before. You remember how we started out going clockwise? We assumed that the current was looping around clockwise, but we got an answer. Both of them I1 is negative. Our answer popped out of our equation as negative, and so did I2.

**Dave Jones:** What does that mean? It means that we chose the wrong direction. Both of these currents are actually flowing anticlockwise, like that. So, what does that mean for R2 here, for example? So, I1, for example, is flowing we assumed it

**Dave Jones:** was flowing down R2 like that, but we got a negative result. So, I1 is actually flowing up like that through R2. And I2 here, that's also a negative. We assumed it was flowing up, but it's actually flowing down because it's negative. So,

**Dave Jones:** it's flowing down R2 like that. Now, we can actually work out the current through R2. D2. So, what do we do now to actually calculate the current through R2? Well, we've got to subtract one current from the other cuz they're flowing in

**Dave Jones:** opposite directions. They're still flowing in opposite directions because they're both negative. So, one is actually I1's actually going up there, I2's going down there. So, we've got to subtract them to cancel them out. Now, here's where we can actually drop the

**Dave Jones:** sign, and we know that the larger value, 0.25455 amps, is flowing down. So, that's larger value, absolute, than the other one, so our final current is going to be flowing down. So, we just subtract the smaller value, 0.13636,

**Dave Jones:** from 2.5455, and we get What do we get? 0.11819. It should actually be 18. Repeater.

**Dave Jones:** It's exactly the same as what we got last time. Winner winner CHICKEN DINNER. HIGH FIVE. WOOHOO! SO, Kirchhoff's current law, Kirchhoff's voltage law, they hold. We got the same answer using two different techniques. Nodal analysis and mesh analysis got

**Dave Jones:** exactly the same answer for the current through R2. And freakingtastic. That was easy, wasn't it? Piece of cake. No worries. But now, there's actually a third method we can use to calculate through R2. It doesn't use Kirchhoff's voltage or current laws, but I thought

**Dave Jones:** I'd show you anyway. Let's see if we can get the exact same answer yet again. And I can't really leave this one out because although it doesn't really have anything to do with Kirchhoff's voltage law and Kirchhoff's current law, it is

**Dave Jones:** one of the basic DC circuit solving theorems. And it's called the superposition theorem, the superposition technique, whatever you want to call it. And it's a bit of a mouthful, but this is what it basically states. The current in any element is the sum of currents

**Dave Jones:** produced by each source acting independently whilst the other sources are replaced by their internal resistances. It might be easier if I just show you. Please excuse the crudity of the model. Didn't have time to build it to scale or

**Dave Jones:** to paint it. Now, what it basically means if we want to solve the current through R2 down here, we can do that by the sum of the currents produced by each source acting independently. So, what we do is we can just if we start with E1,

**Dave Jones:** we take out E2, and we replace it by its internal resistance, which is a short circuit. And you should know that from your basic circuit theory. A power supply in ideal power supply is zero internal resistance. An ideal current

**Dave Jones:** source is open, infinite internal resistance. So, we replace it by that and now you should be able to do this. Anyone can do this, right? This is You can now calculate the current through here. But, aha, we then have to It's the

**Dave Jones:** sum, remember? So, now we have to replace this one with a short circuit, put this one back in here, and then we calculate the current through there, and then we sum them is the sum of the currents produced by each source acting

**Dave Jones:** independently. So, you can see how this is much easier. We won't end up with any weird equations and generate any weird equations like we had to with nodal and mesh analysis. It's basically just Ohm's law and current divider stuff. Very

**Dave Jones:** simple. So, let's go through the exact same example we had last time and see if we come out with the same answer. You think we will? I'm pretty confident. Once again, engineering for the win. So, all the way

**Dave Jones:** over here, I've got the original circuit that we wanted to solve, our two voltages with our three resistors, exactly the same as before. I've redrawn it here because we need to solve this twice. Because we've got two sources.

**Dave Jones:** And by the way, the superposition theorem, of course, only applies if you've got more than one source. You got to have multiple sources and they've got to be linear as well. So, let's solve for E1. So, what do we have to do?

**Dave Jones:** We have to replace E2. We have to replace In this case, the other source we have, but if we had more than one source, we would have to replace If we had more than two sources, we'd have to replace all the others with their

**Dave Jones:** internal resistances. And as I said, a power supply, a voltage, a battery, or whatever it is, it has a zero internal resistance. So, we replace it with a short circuit. If it was a current source in our circuit, we would actually

**Dave Jones:** replace that with an open. It would just be open circuit. So, we've got to replace all the other sources. And now, it just becomes a simple question. But, what I've labeled here is I've got a IT, which is total, the total amount of

**Dave Jones:** current coming from this source, and then IR2 down here. So, now we want to derive an equation for the total current first. So, now what we've got to do is derive an equation for our total current here. And that's easy. It's just Ohm's

**Dave Jones:** law. Look, IT equals what? Does current equal voltage divided by resistance. So, in this case, E1, okay, is on top divided by our resistance, which is going to be the total resistance of our circuit, which is R1 in series with R2

**Dave Jones:** and R3 in parallel. Easy, R1 plus R 2 in parallel with R 3. There we go. And if you haven't seen those two lines before, that's just a common way to express parallel. And of course, you can solve your parallel resistors any way

**Dave Jones:** you like. If you're lucky, you might have a calculator that has a parallel key. As far as I know, there's only two calculators on the market that has a the Casio FX-61F and my own microcalc. So, if you haven't

**Dave Jones:** got one of those, you could do it the old-fashioned way. I choose to do it R2 * R3 over R2 + R3. You can do the one over version if you like. So, there you go. I've just expanded that equation

**Dave Jones:** parallel. I've plugged in the numbers that we have. So, we have all of our resistor values. We have our voltage E1, which I forgot to write up there before. Bingo, our answer is 0.04545 repeater. Actually, I like that. That

**Dave Jones:** gives us a bit of confidence cuz we know that our solution is a repeater. So, you know, that gives me the warm fuzzies. Now, we know our total current flowing here. How do we calculate our current flowing down R2? Well, uh along with

**Dave Jones:** Ohm's law, some of the basic stuff you should learn is the voltage divider equation and also the current divider equation. Very similar to the voltage divider equation. In this case, I1 is equal to I T and then you use your

**Dave Jones:** current divider cuz some goes down here, some goes down there. In this case, it's the opposite resistor. We want R3 like that over R2 plus R3. That is our current divider. Easy. And it's simple. We just plug in our knowns cuz

**Dave Jones:** everything is known. None of this unknown solving equations for unknown rubbish that we did before, and we pop out with an answer of .02727 repeater. Once again, another repeater. Brilliant. So, then we do exactly the same thing for E2. We replace E1 with

**Dave Jones:** its internal resistance, which is a short circuit, and we solve for IR2. Yet again, it's exactly the same way. I won't bore you with all the details, exactly the same uh equation. We generate I, we calculate IT first, the total current coming from

**Dave Jones:** the battery, and then we use our current divider equation to once again calculate IR2. I had that labeled I1 before, that was oopsie, uh mental uh brain fart from the previous one. Um we'll call it IR2A and this is IR2B. And bingo, it comes

**Dave Jones:** out to an answer of . 09 uh point yeah, .090. Once again, a repeater. Brilliant. Feeling pretty confident. So, we've got our two different currents here for uh two IR2s. So, we now have to get the algebraic sum. Once again, we

**Dave Jones:** have to take signs into account. In this case, it just so happens that they're both positive for well, flowing down like that, so there's no negative or whatever, but it could have been depending on uh the circuit that you're

**Dave Jones:** actually analyzing. So, we take those two values, whack those into the equation, just the algebraic sum, to get our final value down IR2, which is what we're trying to get here. So, it's .02727 + .09090. What do we get?

**Dave Jones:** TA-DA! MAGIC. EXACTLY THE same as before and the time before that. Winner. So, there you have it. Sorry about the length of this, but I wanted to go through step-by-step in detail. I hope you enjoyed these uh series of two videos

**Dave Jones:** here. Uh one showing what Kirchhoff's current law and Kirchhoff's voltage law is about and then actually applying it and applying three different uh circuit DC circuit analysis techniques, nodal analysis, mesh analysis, and superposition uh theorem here to solve

**Dave Jones:** exactly the same circuit. We get the same answer three different ways. And you think, "Well, what's the difference? Which one should you use?" Well, you could probably saw here, uh you know, the superposition in this particular instance was the easiest uh probably the

**Dave Jones:** easiest one to do cuz we didn't have to, you know, get some weird algebra with, you know, unknowns and stuff like that. It was just basic Ohm's law and current divider. So, that happened to be the easiest case uh here, but that's not

**Dave Jones:** always the case. Um nodal analysis, as you saw, you would use if you want to calculate a voltage in a circuit. And as I said, that's a popular technique used in uh SPICE uh circuit simulators and things like that. They use various

**Dave Jones:** versions of nodal analysis and they also do some mesh, but it's it's easier to do nodal analysis. Mesh analysis uh easier if you have a lot of uh sources and you want to calculate currents and things like that. So, yeah.

**Dave Jones:** Choose whichever one is appropriate for your particular circuit, but there you go. That's really interesting. So, this is really basic fundamental stuff. So fundamental, it should be taught directly after uh Ohm's law and typically is. You learn Ohm's law, then

**Dave Jones:** you learn what you know, voltage dividers, current dividers, what a voltage source is, what a current source is, and then you learn Kirchhoff's current law, Kirchhoff's voltage law, and then you learn your basic DC circuit theorems for solving circuits. And as I

**Dave Jones:** said, you know, like these are often academic, you know, examples and things like that. And sometimes you don't You can probably spend your whole career and never have to do nodal or mesh analysis or something like that. But hey, it is a

**Dave Jones:** fundamental technique which is so important. Just the mathematics of it goes into actually solving a whole bunch of other stuff. As I said, circuit simulators, all that sort of stuff wouldn't work without stuff like this. So, math for the win. Even if you don't like

**Dave Jones:** math, it's pretty easy. It wasn't that hard at all. So, there you go. You're now an expert Kirchhoff's laws and nodal mesh and superposition theorem. Go have a play. If you like that, please give it a big thumb thumbs up. And if you want

**Dave Jones:** the t-shirt, I'll link that in down below as well. And if you want to discuss it, YouTube comments, blog comments, all that sort of stuff. Support me on Patreon. Thank you to all my Patreon supporters. The link for that is down

**Dave Jones:** below as well. Follow me on Twitter. All that sort of stuff, you know. Rate Subscribe to my YouTube channel. Like, rate. No, they don't rate anymore on YouTube, do they? No. Anyway, catch you next time.
