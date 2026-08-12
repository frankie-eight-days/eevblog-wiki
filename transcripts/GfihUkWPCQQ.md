---
video_id: GfihUkWPCQQ
title: EEVblog 1470 - AC Basics Tutorial Part 3 - Complex Numbers are EASY!
url: https://www.youtube.com/watch?v=GfihUkWPCQQ
source: youtube-asr
---

**Dave Jones:** Hi, this is part three in the AC Basics tutorial series. We're going to cover complex numbers and they're not that complicated or they're really incredibly easy to understand and it's how we do maths operations on AC waveforms because anytime you

**Dave Jones:** introduce, as we saw in the previous video on phases, anytime we introduce a reactive element, a capacitor or an inductor in a circuit, it causes current and voltage phase shifts in a circuit. So, this is from the previous video,

**Dave Jones:** part two, linked up here down below. Check it out. First of all, it's important to learn phases before we move into complex numbers about how waveforms can lag and lead. And as we saw in the previous video, you can actually do

**Dave Jones:** mathematical operations on phases and vectors and get a result using graphical methods, but nobody really does that anymore. We use what are called complex numbers to analyze our AC circuits when you start including a phase component in them. Because in DC fundamentals, you

**Dave Jones:** don't have any phase components. There's no difference in phase between waveforms. It's just DC. It's direct current. It's direct voltage. Whereas in AC, it's alternating current, alternating voltage and you can get phase differences. And this is where we

**Dave Jones:** need to get a bit more clever in our mathematics to actually solve these sorts of things. And you're going to find out now why every basic scientific calculator like this has this mysterious R to P and P to R button on here. What

**Dave Jones:** does it do? Well, let's find out with complex numbers. So, we saw previously, once we start dealing with AC circuits, alternating current and alternating voltages, we end up with sine wave or other waveforms, but we'll just stick with sine waves for all of this.

**Dave Jones:** That not only have a magnitude like this, they have a peak voltage or an RMS voltage, however you want to look at it, they also have a phase component in them designated by phi here. And then you can

**Dave Jones:** have a phase difference between a reference waveform. You always have a reference waveform, as we'll see. And the other waveform has a phase difference, either positive or negative phase difference from that waveform. So, once you start talking about AC, you

**Dave Jones:** can't just apply regular Ohm's law anymore. It's more complex. Get it? I'm here all week. Um so, V = I * R, we have to now start talking about vectors. As we said, it's the same formula, but resistance now actually becomes

**Dave Jones:** impedance, and that impedance will actually have a when you put a show it as a vector over the top, it means that vector has a phase component, as we saw before. So, if you've got a number line like this, you're familiar with your

**Dave Jones:** This is your real number line from zero to whatever. It could be positive, negative, or whatever. Then, once you start introducing phase angles, you have to introduce what's called the complex plane, which is in this direction, like this. And as we saw previously, the

**Dave Jones:** magnitude of this vector determines the amplitude, the peak amplitude of the signal. But then you've got that phase angle as well in here. You've got that phi angle or the difference between your reference waveform and the other signal. So, we have to start using

**Dave Jones:** what's called an Argand diagram, which shows complex numbers. And this is a complex number plane. On the x-axis here, we have real numbers, and on the y-axis like this, this is what's called an imaginary number plane. Now, there's

**Dave Jones:** nothing imaginary about these numbers at all. They're very real. And in fact, they represent real phases. But when we start talking about AC and phases, we have to introduce another number method to actually do this. And we do that

**Dave Jones:** using the complex plane in this direction. So, we saw this equation before, which is the equation for AC voltage over here or AC current. You just replace V with I. And it's kind of complicated, which is why we don't deal

**Dave Jones:** with this sort of stuff cuz it's got all these trig functions like sign in there and it's got time and frequency and stuff. And we don't want to deal with that sort of sort of stuff when we're doing our AC our circuit calculations.

**Dave Jones:** So, we use our complex plane now as it's called with the real component and the imaginary component with the phase angle in there. And that takes into account our trig functions like sign and cos. So, we don't have to muck around with

**Dave Jones:** that sort of stuff. We can just do all of our basic mathematical operations in our to analyze our circuits using the complex number plane without having to use these trig functions. It's really neat. So, with the complex plane in

**Dave Jones:** math- -ematics, not in engineering mathematics, what they use is the letter I here because it's the imaginary axis in this complex plane. So, in this particular case, you can this phaser here, this vector, has the equation X + I Y with X being

**Dave Jones:** Assume it's like at, you know, 45° here or whatever. Anyway, you drop that down to the real axis and this first part of it is that X value when you drop it down. And then you can take your line across there like that.

**Dave Jones:** And this becomes the imaginary complex part of the number. Remember, these are complex numbers. So, this is what the form of a complex number looks like. You've got the real component and then the imaginary component, which is designated with I. But, that's only in

**Dave Jones:** mathematics. In engineering, we don't use I. Sorry. We use J. Like that. Why? We want to be different. Uh mathematicians hate it. But yeah, this So, this is called the J axis. But it's the imaginary axis. We just happen to

**Dave Jones:** use J instead of I. Uh So, this is called the J operator. But it I know you might think it start looking like sort of nasty, but it's not. There's even a actually a simpler form to this because this uh in this

**Dave Jones:** particular form um of our complex number, this is called rectangular. But there's two different forms in complex numbers. Rectangular form is one of them, and it's that form. There's a real component and an imaginary component, but we can also represent it exactly the

**Dave Jones:** same way in what's called the polar form. So, let's say the length of this phaser here, the length of this vector, let's just call that R. So, in this case, Z would be equal to R, and then we

**Dave Jones:** use a real handy notation which represents angle like that, and we just uh angle theta like that because theta is our angle in there. So, that's exactly That's the same quantity, the same number, the same vector, the same

**Dave Jones:** phaser, the same component just represented in two different forms. So, there are two forms of complex numbers, polar and rectangular. You remember how I mentioned the calculator before, the P to R and R to P? P and R. It's to

**Dave Jones:** convert between polar and rectangular form. And it's so important that it's included on like real ancient scientific calculators. That's how important complex numbers are and to be able to deal with them on your calculator. So, this J operator here, you can think of

**Dave Jones:** that like any other operator, addition, subtraction, everything else. But, what it does is J represents uh turning the real component like this through 90° like that. So, let's say that you've got a vector like that, a real uh

**Dave Jones:** thing, a real value that's say, I don't know, three, something like that. If you rotate that, change the phase angle by 90°, three becomes J three. Cuz J represents shifting it 90°. Now, with the J operator, when we go in the

**Dave Jones:** anticlockwise direction like this, it's positive, okay? So, anywhere from uh here right over to 180° like that, that is positive. But, if you go in the other direction like this, it actually becomes uh negative like that. So, if we took our

**Dave Jones:** example here of our vector of length uh three, our our real number of uh three, could be 3 V or whatever, and we rotated it like this, it would become negative J three. Got it? Or, if you're a polar

**Dave Jones:** fanboy, and there's reasons to use rectangular and polar, and why it's so important that it's on buttons on your basic scientific calculator to convert the between the two, as we'll uh see in a minute. If you want to do this in

**Dave Jones:** polar form, well, it's right, three is just three. If you want to write it in the uh complex form, it's just three angle zero, cuz there's no angle like that. But, if you rotated it like that, up 90°

**Dave Jones:** like that, you remember, it's uh positive. It Well, it was positive before, it would become three angle 90 like that. Um you can call it angle I just happen to use like angle. It's probably better term for it. Or, if

**Dave Jones:** you rotate it 90° this way, it'd be three angle minus 90. That's the polar form. These are completely equivalent and you can convert between polar and rectangular using basic trigonometry you learn in like early high school. And you'll never get more than plus or minus

**Dave Jones:** 180 here cuz once you rotate this around to 180°, well, you're actually, you know, if you're down here, you're actually closer to back here and your negative phase angle um so, you know, it's it's not like 190° you'd be minus 170. So, we've got two

**Dave Jones:** complex number forms, polar and rectangular and it's easy to convert uh between them and it's just that basic trigonometry. Yes, it can it comes in useful that trigonometry uh you learn in basic high school, right? You've got your triangle like that, you've got your

**Dave Jones:** angle theta in here. We'll just call this side R here and this side is length A and this one is B um but because we're talking a complex plane, we'll just add the J in there, but you can just ignore

**Dave Jones:** that. So, you can represent it in either form, either uh length R like that with the phase angle in there, theta, or you can represent it as length A like that or JB because it has the J because it's

**Dave Jones:** in that direction, the imaginary uh direction. And they're the two different forms it's written in. And then um basic trigonometry that you learned that you can then uh do the conversions between polar and rectangular form and that's how you do

**Dave Jones:** it. And that's exactly what your Confuser here is doing when you push the P to R and R to P buttons. It's just doing these calculations internally, saving you the trouble to having to remember these formulas and convert

**Dave Jones:** them. Confuser does it for you. So, we can plot points on our complex plane now. Remember we have the real reference plane like this, just like your regular number line, you know, we've got zero and it's and negative like this. These are real

**Dave Jones:** voltages, real currents, real reactances, right? Everything's like real. And then you've got your complex plane in this direction, uh and you've got positive values this way and negative values this way. These are positive and negative J. This is your

**Dave Jones:** complex plane. So, we can plot points on this and get the rectangular uh form for your complex number. So, if we had a point like that on our uh complex plane here, then that would be two because the

**Dave Jones:** real component first plus J, and then it would be J three cuz we're in the positive direction like this. Then if we had another point down here like the opposite side like this, this would be once again two is the real component,

**Dave Jones:** but it would be minus J three like that because it's in the minus J direction. And if we have say this point here, well, that's minus five is the real component, but it would still be plus J three. So, it's not minus J because

**Dave Jones:** we're we're only minusing the real, remember? This the left side of the plus sign here is the real component, and then the complex J component is on the right-hand side of the plus. So, that would be minus five plus J three. And

**Dave Jones:** the same thing down here, you guessed it, it would be minus five again minus J three. And then, of course, you can draw in your phasor like that. And then, as we looked at before, you can actually convert that

**Dave Jones:** into polar form between rectangular and polar. Cool, huh? So, I know you're asking, "Why are we even bothering with all this polar and rectangular form and converting between them and all this sort of rubbish?" What benefit does it

**Dave Jones:** gain us? Well, it gains us a huge benefit. And why? It's on every single scientific calculator. It's because once we start talking with AC components, doesn't matter whether it's voltage, current, impedance, or whatever it is, when we start talking AC circuit

**Dave Jones:** analysis, then they will have an angular phase component, and we have to start doing trig functions. If you stayed using that formula that we showed before with the sine function and the trig function, then when you're doing your AC

**Dave Jones:** circuit analysis, you'd be solving trig functions all day until the cows come home. So, what we do is we want to actually eliminate trig functions completely from this. We don't want to use a sine, cos, tan, and all that arc

**Dave Jones:** rubbish either. We don't want to use any trig functions at all. And this is what polar and rectangular forms do. Once you've got your complex voltage, current, impedance, or whatever you know, we're dealing with in our circuits, once you've got it in complex

**Dave Jones:** form with a phase component in it, then we can do simple multiplication, addition, subtraction, and division using just regular math. It takes the trig all out of it. And this is the beautiful thing with polar and rectangular form. Let's have a look

**Dave Jones:** here. So, why both forms? Well, if you want to do addition and subtraction on complex numbers, then you have to do it in rectangular form. If you want to do a multiplication and division, you have to have it in polar form. And it just makes

**Dave Jones:** your life so much easier. And why your calculator allows you to convert easily between those two. Because when we're solving our AC circuit analysis problems, we want to add voltages together, we want to subtract them, divide them, multiply them, all that

**Dave Jones:** sort of stuff. And this is how easy it is to do. Let's take a look at if you want to multiply two complex voltages together. Okay? V1 and V2. Now, you they will be in complex form, so you will

**Dave Jones:** have a real component and a phase component like we uh showed before. We'll call it R1 here because we had that on the graph before. This is not resistance, okay? It's not resistor one. It's just like real Think of that as the

**Dave Jones:** real component, so we'll call it R1. You can label it anything you like, really. Like we've got A's and B's and C's and D's over here. You can label it anything, right? So, we've got R1 and phase one like this. This is our complex

**Dave Jones:** form of V1. And we want to multiply that by V2, so we V2's in its complex form. We'll call that R2 and phase two. So, how do you multiply two complex numbers? It's simple. You take the two real

**Dave Jones:** components and you multiply them. So, R1 * R2, and that gives you your resultant real component. And then, not multiply, but you have to add the phase components. So, it becomes angle like this, phase one plus phase two. Simple.

**Dave Jones:** You've eliminated all trig functions from your calculations. This is just great. And it's so simple. Same with uh division. Well, except you subtract them. So, you've got V1 and V2. So, your real and your phase uh components. So,

**Dave Jones:** it becomes R1 phase one / R2 phase two. Well, you take your two real components like this and you divide them, and that gives you your final result. But, uh for the phase, instead of adding them like for multiplication, we subtract them.

**Dave Jones:** So, phase one minus phase two, and that gives you your answer. You've just multiplied and divided two complex numbers. It ain't And it's very similar if you want to add and subtract. Well, we need them in polar form like this. So, our

**Dave Jones:** voltages, do you remember our voltages can exist in either polar or rectangular form? So, if we want to add add two of two voltage complex voltages together, we put it in its rectangular form, which is A + J of B. As I said before, A and B

**Dave Jones:** are just generic letters uh we've chosen, and I've chosen C and D here uh not cuz they represent anything, it's because so we don't confuse them with A and B over here. But you got two complex numbers you want to add together, all

**Dave Jones:** you do is once again, you add the two real components like this, and you simply add the two imaginary components like that. So your answer is A plus C plus J B plus D. Easy. And subtraction's just as easy as

**Dave Jones:** well. You take your complex voltages here, you put them in their rectangular form, and it's A instead of A plus C, it's A minus C. You take the real components, you subtract them, you take the imaginary components here and here,

**Dave Jones:** and you subtract them. And that gives you answer. Whoever thought complex numbers were complex is a fool. Complex numbers are incredibly simple. These Just remember how to do these operations like this, and you can perform any maths you want on any

**Dave Jones:** complex AC circuit problem. So how does this tie into real circuit components? Well, I'll have to do a future video on this, I think I we might have to cover it. But let's just take an inductor for example. You remember I mentioned civil

**Dave Jones:** before, and voltage V represents voltage, I represents current, and for an inductor L, the voltage leads the current. Okay? So voltage leads the current. So Ohm's law, V on I would normally equal R, but we're actually talking about a reactive

**Dave Jones:** component now. So we actually designate it X. Anyway, let's see how to get down here. So it's actually omega, which is 2 pi F. So it's omega L, the inductance. So the reactance of the inductor, or the effective AC resistance of the inductor,

**Dave Jones:** so to speak, has to have that phase component in it, and it's dependent upon frequency. So because voltage leads the current, it's angle 90 degrees like that. And if we convert that into complex notation, V on I equals J omega L. So, we've introduced

**Dave Jones:** the imaginary component in there, the complex component. So, the reactance, or the AC resistance, so to speak, of our inductor here is J omega L in ohms. So, when you start talking reactive components like inductors and capacitors as well, you can go through exactly the

**Dave Jones:** same thing for a capacitor. And this is where you have to take into account that voltage and phase component. And so, the reactance component, so J. So, when you start doing your AC circuit analysis problems, you'll have like reactance

**Dave Jones:** values for inductors and capacitors in complex form. So, then you can start doing all your regular circuit calculations, but instead of doing them in DC, you do them in AC, and they'll have that J component. But, that's for a

**Dave Jones:** future video. I just want to show you how it's relevant. And just for completeness, we'll do the capacitor because now current for capacitors, current leads the voltage like this. So, if we do Ohm's law and get our which

**Dave Jones:** would normally equal resistance, but because we're talking about AC, it's now and it's reactive component, we're now talking we want the value of XC, AC like the AC resistance. So, it's one on omega C angle minus 90 now cuz it's 180° or

**Dave Jones:** anti-phase or out of phase compared to the inductor. And that's assuming it's a pure capacitor and pure inductor, of course. And so, you can work that out, and the capacitive reactance is now minus J one on omega C instead of plus J omega L for

**Dave Jones:** the inductor. Got it? So, just a simple worked example for multiplying two voltages here. Got them in the complex form, five angle 20, so 5 V could be 5 V RMS with a 20° phase angle, and you want

**Dave Jones:** to add it to a 2-V RMS signal, you usually use RMS for this. With 30 degrees phase angle, well, you multiply the real components like that, so that becomes 10, and then you add the phase components, 20 + 30, which becomes

**Dave Jones:** 50. And say for example if this one was -30 degrees, it was you know down here on the graph, so one was up here, one's down here like this, what would you end up with? Well, you would it would be 20

**Dave Jones:** + -30, which would be -10 degrees. Easy. What would that look like on our polar diagram here? Well, we've got 5 5 V at angle 20 like that multiplying this one, which is 2 V, so it's shorter at an angle of -30, and it gives a

**Dave Jones:** result of 10, so that's much longer at an angle of -10 degrees like that. Beauty. And the power of rectangular and polar forms don't just stop at your regular four arithmetic functions. You can do powers and roots as well. Like

**Dave Jones:** powers are for example in polar form here, so you've got R angle theta, it's just R to the power N then all that to the power of N. So if you want to take your voltage to the power of N, well,

**Dave Jones:** it's just the real component to the power of N angle the power of N times the phase angle. That's it. And roots, you actually do a similar way. So if you wanted to get a square root of your complex voltage, it

**Dave Jones:** would just be the real component to the power of a half cuz that's what a square root is. And if you wanted a cube root, then it'd be the power of one on three. And angle theta times a half.

**Dave Jones:** It's really easy. No trig functions involved. So there you go. Hopefully I've given you a very simple overview of why we use complex numbers and why we put them in polar and rectangular forms and why even though it's basic

**Dave Jones:** scientific calculators from way back, this FX-82 actually has P to R and R to P, polar to rectangular and rectangular to polar conversion on it because it's so damn useful for engineers. So, and that's why it's got like the engineering

**Dave Jones:** display mode as well. You know, these things were made for engineers and engineers invented these sort of things to do AC circuit analysis. And in future videos, I might be able to show you look at the Ohm's law for AC, basically. And

**Dave Jones:** it's exactly the same as Ohm's law for DC and all the stuff we learned in DC fundamentals, it's exactly the same for AC except your voltages and your currents and your reactances and stuff, they now have phase components to them. So,

**Dave Jones:** everything's in complex form, but your Ohm's law remains the same. You're just dealing with complex numbers instead of real numbers. And complex numbers ain't complex. It's really easy to add them up and hopefully I've given you a good idea

**Dave Jones:** how they represent with phases and everything else. So, hope you found that useful. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.
