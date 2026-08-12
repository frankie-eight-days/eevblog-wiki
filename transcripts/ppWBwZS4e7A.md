---
video_id: ppWBwZS4e7A
title: EEVblog #486 - Does Current Flow Through A Capacitor?
url: https://www.youtube.com/watch?v=ppWBwZS4e7A
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 35, "3": 51, "4": 70, "5": 85, "6": 103, "7": 118, "8": 131, "9": 148, "10": 162, "11": 178, "12": 196, "13": 212, "14": 229, "15": 245, "16": 259, "17": 276, "18": 292, "19": 305, "20": 322, "21": 341, "22": 354, "23": 368, "24": 383, "25": 404, "26": 423, "27": 439, "28": 456, "29": 468, "30": 485, "31": 499, "32": 513, "33": 530, "34": 550, "35": 566, "36": 583, "37": 604, "38": 619, "39": 638, "40": 654, "41": 671, "42": 686, "43": 699, "44": 713, "45": 732, "46": 749, "47": 765, "48": 781, "49": 797, "50": 812, "51": 825, "52": 843, "53": 858, "54": 869, "55": 883, "56": 899, "57": 915, "58": 936, "59": 951, "60": 964, "61": 980, "62": 996, "63": 1013}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. This one comes about because of something I said in a previous video. I mentioned that current flows through a capacitor and I had a couple of people comment that "No, that's wrong. Current doesn't

**Dave Jones:** flow through a capacitor. You're crazy, Dave." Well, am I? Does current flow through a capacitor? Turns out it's an interesting question. Let's take a quick look at it. And when I say quick, I do mean quick because to actually answer

**Dave Jones:** this and get to the bottom of it and understand it all actually takes a couple of semesters at university and lots of physics and math and Maxwell's equations and all sorts of stuff. But to answer the question, does current flow

**Dave Jones:** through a capacitor? The answer is, I can tell you right now, yes, exclamation mark. But with a little asterisk next to it. And that's where this video comes in. We're going to talk about the asterisk. And of course, it all starts out very

**Dave Jones:** basic, doesn't it? You've got a battery here, a switch, and a resistor, then if the switch is open, no current flows. But as soon as you close the switch, current I flows through there. Let's not mix up conventional and electron current flow,

**Dave Jones:** shall we? That's a whole 'nother can of worms. But you close the switch, current flows. Ohm's law, all that stuff, Electronics 101. It really is. But what happens if we put a capacitor in here like this? Well, of course, that's very easy, too.

**Dave Jones:** In fact, it's almost insulting. You know what happens. The capacitor charges up, current still I still flows in the circuit, and it charges up a voltage on that capacitor. In this case, Uh, VC, the voltage across the capacitor, a

**Dave Jones:** capacitor when you first, if it's got no charge on it, when you first apply start having current flow through the circuit, it has a voltage of zero. So, that's this black graph here. So, the X So, the Y axis here is the voltage across the

**Dave Jones:** capacitor. It starts to charge up until it reaches a point where it's fully charged and the voltage just sits at the fixed level, which is your battery voltage over here. And of course, the current starts off incredibly high because the capacitor is

**Dave Jones:** effectively a short circuit when you close that switch. So, the current is at maximum and then it slowly tapers off, a direct mirror image of that until the current goes to zero. So, the answer to this question seems bleedingly obvious.

**Dave Jones:** Does current flow flow through a capacitor? Yes. I see. Look, current is flowing in that loop. It's in series. How else Where else can it go but through that capacitor? And of course, you got some standard formulas you learn

**Dave Jones:** in Electronics 101 to go along with this. Charge Q equals C * V. And then you've got I = dQ or the change in the charge over dT, the change in the time. Oh, some people, you know, that they

**Dave Jones:** don't like to use d in there. You could, you know, use like delta or something like that. It just means change. So, the current equals the change in the charge on versus the change in time. And that's where that graph comes from. It's not

**Dave Jones:** rocket science. Current is flowing in the capacitor. And because charge equals C * V, you can write that again. I = C * dV dT like that. And you know, and there's all sorts of equations for currents flowing

**Dave Jones:** in various circuits. So, current does flow through a capacitor. Or does it? And just so nobody nitpicks, yes, I know it's actually IT in there. I didn't add the T in there. And if you put a current source in series with a

**Dave Jones:** capacitor like this, which is essentially what we did in the previous video, which caused all this ruckus to begin with, then the T drops out of that and I just equals C times V on T. And the VC, the voltage across the capacitor,

**Dave Jones:** will charge up will uh rise in a linear fashion like that, just as we saw in the previous video. So, there's current flowing in here. So, it's time to ask ourselves, what is current? Well, electronics 101 again, right? Current is the flow of

**Dave Jones:** electric charge. And when you have conductors like you do in electronic circuits, they're made up of conductors and wires and resistors and stuff like that, then it's the flow of electrons through that circuit. Now, let's not get into drift velocity and stuff like that.

**Dave Jones:** There's a whole 'nother can of worms where the electrons, you know, move it like a 1 mm per second through the entire circuit. Uh, Google that one. But, yeah, it's just the flow of electrons in this circuit. That's why when you break the

**Dave Jones:** switch, no electrons can flow in this circuit at all. But, isn't a capacitor just like an open switch? Look, that this symbol itself tells you that there's a break. What's the difference between a switch symbol and a capacitor

**Dave Jones:** symbol? It's they're all they're identical, right? And that comes down to your what you basically know about capacitors, right? They block DC and they allow AC or changing currents to pass through them. Hmm. So, now we'll take a brief look at

**Dave Jones:** inside a capacitor here. And that requires a whole separate video, so it's going to be very simplistic. Well, you know that a capacitor is just two metal plates like this or it can be two bits of wire just sitting in the air like

**Dave Jones:** that like a switch, remember? A switch has capacitance as well. Tiny amount between the contacts. Any two wires in any space is effectively a capacitor. Anyway, it's got two plates in there and it's got a dielectric material in the

**Dave Jones:** middle of it. And what that does is actually creates when you charge up a capacitor, you're actually building up a charge on both of these plates. They're going to be equal and opposite charges between the two plates and you're going to set up an electric

**Dave Jones:** field between the two plates. But, because it's like an open switch, no actual electrons actually flow through the material. And once again, we're talking about an ideal capacitor here. In practice, yes, there's a tiny little bit of resistance in there like that. So,

**Dave Jones:** there's some electrons do actually sneak through the dielectric material, but we're just going to ignore that because as well, that's just going to confuse the issue. No electrons actually pass through a capacitor like this. It's just a capacitor is just defined in terms and

**Dave Jones:** understood in terms of electric charge building up on the plate. Yes, we've got current flowing into and out of the wire, for example, and current can flow down these plates cuz they're actually metal, right? You can get electron flow up and down these

**Dave Jones:** plates like this, okay? But, well, nothing can go through the middle. It's like a switch. It's open. No electrons can flow. So, what's going on? How can current flow through a capacitor? It's sort of, you know, we know current flows

**Dave Jones:** through because it's a series circuit and well, you can actually measure it and you You all of basic electronics 101 formulas that tell you current flows through a capacitor, but when you look at it in terms of electric fields and

**Dave Jones:** how it's two separate plates and an insulator in between, that's what a dielectric is, it's an insulator, be it air or mica or ceramic or whatever material it happens to be, no electrons can actually flow. What's going on? So, to grossly simplify this

**Dave Jones:** thing, which as I said at the start, I have to do because this whole concept and understanding all this sort of stuff takes, you know, semesters of understanding at university and most people come away from it scratching their head anyway trying to figure this

**Dave Jones:** sort of stuff out and it depends on how you look at it and there's a big difference between uh physics, fundamental physics, and practical electronics as we'll uh get into right at the end to close out on this thing.

**Dave Jones:** So, to understand this, we have to look at electromagnetism for a minute and Maxwell and the famous Maxwell equations. Now, before Maxwell came along, uh electricity and magnetism were thought to be two separate things, but Maxwell, incredibly smart dude, combined the two

**Dave Jones:** into theory of electromagnetism. And to cut the long story short, to make it all work, he had to come up with the concept of a displacement current that um in this case flows flows through a capacitor and that's how what we're

**Dave Jones:** using up here in all of our general electronics equations in a practical sense. So, what it comes down to is that we've actually got two different types of current. There's electric current, which we explained right back at the start,

**Dave Jones:** is, you know, the uh flow of charge and electrons, and but we know that electrons can't actually go through an insulator in a capacitor or anything else. So, um what Maxwell came up with is a concept called displacement current, and

**Dave Jones:** that gives us a second definition of current. And in practical electronics, when anyone uses the term current, they're including both of these terms under the same umbrella. And to try and separate them, then you start getting away from practical electronics into

**Dave Jones:** theoretical physics, and it gets nasty. So, Maxwell, with this idea of the displacement current, it's There's many different ways to look at it and try and understand the concept, but it is a term which he came up with

**Dave Jones:** which was required and is required to complete the theory of electromagnetism and electromagnetic waves and you know, radio waves and the whole concept that we know as electromagnetism today. It's an essential part of it. And that displacement current is what

**Dave Jones:** actually flows through or flows through, I use that in quote marks, flows through the capacitor. But, that's why it's still valid to say that there's current flowing through the capacitor in the world of electronics because essentially there is cuz our day-to-day equations

**Dave Jones:** all assume and know that there is current flowing in this series circuit with the capacitor there even though it's effectively an open circuit. And of course, uh Maxwell just considered what didn't even consider the dielectric constant in here. Even if

**Dave Jones:** it's a vacuum, he said, "Well, a vacuum is just a dielectric like everything else. It's just got a dielectric constant of one instead of Well, most other materials have a dielectric constant above one." But, there's it's just a dielectric constant. So, that's

**Dave Jones:** how electromagnetic waves can travel through a vacuum. And it gets really, really nasty, and I don't have time to go into it. So, as you charge up a capacitor, you're changing the electric field. You're varying the electric field

**Dave Jones:** between the two plates, and of course, the electric current can flow onto the plates like that. And so, current is flowing in to one plate and leaving the other. But, what actually happens in the dielectric material is not electric

**Dave Jones:** current flow. There's not electrons actually flowing through uh the dielectric material. It's the changing electric field between the plates actually also creates a changing magnetic field, and it's that magnetic field concept which causes the displacement current. It gives the

**Dave Jones:** equivalent current in step in terms of electro- uh magnetics flowing through the dielectric material. So, current is still flowing through. You've got I going in here. You've got I popping out there. And well, what happens within inside the

**Dave Jones:** capacitor? Uh it's not magic. It's just fundamental physics and how you understand a displacement current field in Maxwell's equations. And therein lies the trick. When you're on the conductor, i.e., the wire coming in and the plate, you can

**Dave Jones:** talk in terms of electric currents, and everything's just fine and dandy. But, once you leave that conductor and get into the insulator, i.e., the dielectric material, you've got to start talking in terms of uh changing electric fields which creates changing magnetic fields,

**Dave Jones:** which then uh you can have energy um storage and transfer in these magnetic uh fields. And that's how current is able to go through, and it all comes out in the wash in Maxwell's equations. It would take 10 boards worth of equations

**Dave Jones:** for it to all come out in the wash. But, so, you know, you can go in deep into the concept of how you're actually able to get current flowing through the insulator, but it does because Maxwell's equations tell you it does. And a not

**Dave Jones:** too dissimilar thing pops up when you start talking about inductors. And it's like, well, how dare an inductor not pass all of its current through? How can there not be any current flowing through an inductor? It's just a bit of wire. It

**Dave Jones:** should conduct. Well, it's the electromagnetic fields in the thing. And that's uh the sort of inverse relationship between capacitors and inductors. In this case, um capacitors, as the rate of change of the electric field goes up, the greater the

**Dave Jones:** current that can flow through this thing. And conversely, with um inductors, then the greater the change of the magnetic field, the less current flows through it. So, there you have it. That's it in a nutshell. And I'm sorry,

**Dave Jones:** I'm not going to go into any deeper. If you want to know about it, then Google the word displacement current and electric current and go into it and electromagnetism and Maxwell's equations and the whole thing. And you can spend

**Dave Jones:** years and years of your life trying to understand how or if current flows through a capacitor. But as I said, in practical electronics, yes, current flows through a capacitor. And when you use the word current, it means it it

**Dave Jones:** implies the combination of electric current and displacement current, i.e. the flow of actual electrons or electric charge through a conductor. And then, when you don't have a conductor, i.e. you have a capacitor, it's a effectively another case. It's not a

**Dave Jones:** special case. It's another case of using a different type of current called displacement current. And it's a mathematical concept which uh depends on how you want to interpret it, whether you're not a physicist or a practical electronics person. And that's the

**Dave Jones:** point. To say to say somebody's wrong by, "No, current doesn't flow through a capacitor." it's just crazy. It's of no practical value whatsoever. Try and design any practical electronics by thinking that current doesn't flow flow through a capacitor. It's just stupid. Doesn't

**Dave Jones:** work. So, really there's two different worlds going on here. There's the fundamental physics world of electron flow and charge carriers and all that sort of, you know, jazz. And there's, you know, the high-level macro practical electronics thing where we use all our

**Dave Jones:** basic equations and current flows through the capacitor and all the equations work and everything's just fine and that's how we teach electronics, that's how we understand it, that's how we design things with it, the fact that current does flow through

**Dave Jones:** a capacitor. So, as I said, yeah, you can get into deep theoretical physics of how and if actually and what the definition of the term current is, but it's of no practical value because at the end of the day displacement current

**Dave Jones:** it it's no point thinking about it because you can't buy a displacement current meter and whack it in between the plates and measure the displacement current. It's a mathematical concept effectively. So, just don't worry about it. Electric current

**Dave Jones:** flows through a capacitor. Through. So, theoretical physicist, go for your life. Me, I'm going back to the bench using my current meter to actually measure the current.

**Dave Jones:** So, does current flow through a capacitor? Well, let's find out. Yep. Catch you next time.
