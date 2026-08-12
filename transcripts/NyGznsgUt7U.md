---
video_id: NyGznsgUt7U
title: EEVblog 1747 - Schottky vs PN Diodes & Measurement Traps
url: https://www.youtube.com/watch?v=NyGznsgUt7U
source: youtube-asr
---

**Dave Jones:** Hi, I found this very simple, but in very interesting question posted on X by Blind Vio, who's an excellent follow by the way. Um, and I'll link it in down below if you want to join the discussion on X, but I thought I'd shoot a video

**Dave Jones:** explaining what's going on here because we're going to go down a rabbit hole with diodes that you might not be aware of, especially if you're a beginner, because it's non-obvious. And there can be a big difference between different

**Dave Jones:** types of diodes and what applications you use them in. Can be a big trap for young players. So, the circuit posted is a simple diode flowing from a 5-V USB input to power whatever circuitry is on the other side. We don't care. It's

**Dave Jones:** common to use a diode as series input protection like this, but just in case your input voltage is reverse biased for whatever reason. You don't want to blow up your circuit, and the diode, of course, only allows current to flow in

**Dave Jones:** one direction. So, it allows to flow in from the power supply, but it doesn't allow it to flow out. Hence, the why a diode looks like an arrow. And you can see that the arrow is pointing inwards from the 5-V USB. So, the question is,

**Dave Jones:** shouldn't the diode be preventing voltage or current flowing back to the input? And the answer is, well, yes, it should. So, let's build it up and see what's going on here. So, what I've got here, I've got a 5-V power supply, and

**Dave Jones:** I've got a diode in series. I'm using a surface mount one, so I had to mount it on a board here, but trust me, there's nothing fancy going on here. And if you want to know what it is, it's an STP

**Dave Jones:** 2SL60A here. We'll have a look at that later. And we've got our voltmeter over here, available on evblog.store, by the way. All the best multimeters are on evblog.store. So, we've got the diode in series, and of course, the diode has an

**Dave Jones:** anode and a cathode. Yes, cathode is marked with a K, and it's spelled with a C. Uh, don't ask why. Just is. And you can see that the diode simply shaped like an arrow here pointing in this direction like this. So, current is only

**Dave Jones:** going to flow in that direction. It's not going to flow backwards. That's what a diode does. It literally stops the current from flowing backwards. So, this is actually the same as our Twitter question here except the power supply is

**Dave Jones:** simulating the circuit which would normally be powered from an external power supply here. So, the current flows in to the circuit and powers your circuit. And here was using a voltmeter to measure the USB port. So, I've got

**Dave Jones:** that diode in series and sure enough we're like our circuit's at 5 volts and our diode's pointing in this direction. So, why are we reading 5 volts on our multimeter? Shouldn't we be reading 0 volts? You might be

**Dave Jones:** thinking, "Oh, Dave, you've got the diode back to front." Okay, well, let's put it in the opposite direction, shall we? We're still measuring 5 volts. Is this diode blowing? What the hell's going on here? So, I've got another type

**Dave Jones:** of diode here. For those playing along at home, it's an SS24. You know, these are quite decent diodes. We getting the same thing. And you can see the negative mark on the diode there and the positive terminal. So, I do have that diode wired

**Dave Jones:** backwards. Why are we still seeing 5 volts? Shouldn't that voltage be reading 0? Well, yes, it should. So, let's try a different diode. We get the classic 1N4148 signal diode. It's as jelly bean and as simple as it gets. Negative terminal

**Dave Jones:** there. Hopefully, you can see it and we put it in. We're reading 0. That works just fine. And then if we change the polarity of that, it lets the voltage through because it's forward what's called forward biased. And then when you're

**Dave Jones:** reverse biased, we read 0. So, why does this diode work and the other two didn't? Let's try another diode here you'll be familiar with the classic power diode, the 1N4001. We put that reverse biased, we read zero volts out. And if we change the polarity

**Dave Jones:** of that, sure enough, we're going to measure out five volts. No worries. There's a very little voltage drop on there because there's very little current flowing through that diode because we've got a 10 meg input resistance on our meter here, but you

**Dave Jones:** can see it works as a diode. So, is there something wrong with these diodes? Well, no, they're actually pretty decent diodes. In fact, they're better than these diodes, but they're not better for this application that we're using it in

**Dave Jones:** now. And the application matters. These are actually different types of diode to your regular 1N4001 and your 4148. These are regular PN junction diodes. If you've studied diodes, you're familiar with that. A diode is a a semiconductor PN junction. That's how it works. I

**Dave Jones:** won't go into the physics of it, but it allows current to flow in one direction and not the other direction. Well, why didn't these diodes do that? Well, they do do that, but they're different types. These are what's called Schottky diodes,

**Dave Jones:** named after Walter Schottky. Don't confuse it with Shockley, the more famous Shockley who invented, co-founded, and co-invented the transistor. No, different person, same field, but yeah, Walter Schottky. And if you go back to the original question schematic, aha, you would have noticed

**Dave Jones:** it's not a regular diode symbol. It's a Schottky symbol which has these little like square tails like this. And that indicates that that's a Schottky diode. And it goes by its more formal name of a Schottky barrier diode. So, some people

**Dave Jones:** call them just a barrier diode, but probably more common just to call them a Schottky diode. And they're different to a regular PN junction diode like your 1N 4001 or your 1N 4148 here. These are just a PN junction, but the Schottky

**Dave Jones:** diode is what's called a metal semiconductor junction. It has an extra metal layer in there, and that gives you a huge advantage in terms of voltage drop. So, let's measure these diodes with a diode tester on a multimeter.

**Dave Jones:** Let's have a look. You can see that it works fine, and we put in the other direction, it reads nothing. It works exactly like a regular diode. And the other one here? Look at that. No worries. It looks and tests exactly

**Dave Jones:** like a regular diode. But you might have noticed something there on that reading. Look at this. 0.142 V. That's a low voltage drop. So, let's get the classic 1N 4001. Ah, we've got half a volt drop. And the 1N

**Dave Jones:** 4148 diode? Once again, half a volt drop. The Schottky diode's their huge advantage is that they're a much lower voltage drop than your regular PN junction diodes, and that's why people use Schottky diodes in switch-mode power supplies when you care about efficiency.

**Dave Jones:** You don't just want to throw away your power willy-nilly in the losses in your diode. So, that's why Schottky diodes are really useful for like high-frequency switch-mode power supplies with low losses. That's where you want to use them. But Dave, if it

**Dave Jones:** tests like a regular diode on a diode tester, why is it like feeding back the voltage back out? Look, I've got that's a reverse-biased Schottky diode. So, to figure out why it's doing this, so instead of our voltmeter here, we're

**Dave Jones:** going to turn it into a current meter by moving our jack over here. Oh, insertion error. Warning, Will Robinson. Put it over to microamps over here, and we're going to have a look at what reverse bias current flows through that diode at

**Dave Jones:** 5 V cuz 5 V is going to matter. And look, there's a non-zero reverse current. It's only 2.4 microamps, right? Microamps, that's not much, but it's enough to upset the apple cart in the example circuit that we just had.

**Dave Jones:** That leakage current is the huge downside of Schottky diodes. Schottky diodes, as we'll see in a minute when we go to the data sheet, are about three orders of magnitude worse leakage than a regular, even jelly bean PN junction

**Dave Jones:** diode. You pay a price for having that Schottky barrier construction with the extra metal layer in there. But going back to our original question here, why are we reading 5 V on here when the diode is reverse biased? And if you use

**Dave Jones:** a, you know, 1N4001, it shows zero. Why are we getting something here? It's because multimeters, digital or analog, have an input impedance here, and you might You should know that it's around about 10 megohms. Could be 10, could be

**Dave Jones:** 11. It depends on the meter design internally. But let's just say it's 10 megohms input impedance. So effectively, our multimeter is a 10 megohm resistor. And you saw that we had some leakage current, some reverse leakage current in

**Dave Jones:** this diode of like, what is it? 2.5 microamps or something. And if you get you confused around here, I think it was 2.2 microamps times, just Ohm's law, 10 meg resistor, what do you get? 22 V. But we've only got a 5 V power supply, so

**Dave Jones:** we're going to read a maximum of 5 V here. If it was 22, we'd be able to measure 22. In fact, we can wind up the voltage. So if we wind the voltage up there, you can see it's going to track,

**Dave Jones:** but once we get above that like 22 V or thereabouts, Like we were up to like I I think this is a 40-V diode. So, I'll just go to 40-V maximum there. You can see it's now only reading 30-V because

**Dave Jones:** the leakage of this diode cha- A, changes with voltage as we'll see in a minute in the data sheet in the characteristic curves. Um and we've got a 10-M resistor there. And sure enough, if I put my fingers across there, I'm

**Dave Jones:** going to lower the effective resistance of that and it's going to go up to the maximum 40-V Not not quite. Have to wet my fingers maybe. And once again, that is not going to happen with a regular PN junction diode.

**Dave Jones:** But once again, if I put my fingers across there, I'm adding leakage by effectively putting a resistor across there. And you can think of that reverse leakage current as an equivalent resistor across the diode. It's a very high value. It's like, you know, mega-

**Dave Jones:** tens of megaohms, but it's there. So, let's have a brief look at what's going on here. I'll link in this website from TTI. It's a just a very nice uh page here with uh basic resources. And if you

**Dave Jones:** want to go into the uh physics of this, which I definitely don't want to do, I'll link in this uh Purdue University uh Schottky diode thing down here. And it's it's basically uh we've got instead of a PN junction, we've got a metal and

**Dave Jones:** N junction here. So, they're physically constructed quite different to a PN junction diode. It's not a PN junction plus metal. It's just the N junction plus a metal junction like this. So, technically, it's easier to manufacture. You don't have to do any of the extra

**Dave Jones:** doping and things um to do that. But you can get into the physics of it. You can go right down the rabbit hole, which yeah, we do not want to do. But bit time reading, go for it. So, the symbol is

**Dave Jones:** quite different to our regular diode, which is just the straight line. We have these little curly bits on the end. Sometimes they add the little bit going down and sometimes it's just a like that. Um whatever, but that could be if you just

**Dave Jones:** if you don't add the bit that goes down there, then you could easily confuse that with a Zener, which is an angled one. So, don't confuse it with Zener. I've done a video on Zener diodes. I'll link that in as well. So, I've got some

**Dave Jones:** N-type silicon and just a metal junction. So, it really is that easy. And you can physically see inside a barrier junction diode here. They just have a bit of metal and there's the N-type silicon there. Easy peasy. And by

**Dave Jones:** choosing a different type of metal here, you can actually adjust the effective barrier size in there. You can change the characteristics of your Schottky diode. So, you might use platinum, titanium, nickel, aluminum, tungsten, or you know, all different types of metals. You can

**Dave Jones:** actually select them or even alloys, I guess. If you want to go into the that deep, you can adjust the properties of your Schottky diode. You can't do that with a PN junction diodes. It's just a PN Well, you can. You can adjust the

**Dave Jones:** doping and things like that, but it's a very different physical construction and being able to adjust the properties of your barrier in there. So, anyway, that's the physics of it. So, here's a classic diode characteristic curve we've got current

**Dave Jones:** of forward current versus forward voltage here in this quadrant over here, and then we've got reverse voltage in this direction and reverse current in this direction. So, a normal diode is shaped like this and so its junction voltage is forward bias voltage is quite

**Dave Jones:** high. You saw it was like half a volt, but when you increase the current, it goes higher like 0.7 volts, a volt, so even more at really high current. So, voltage drop ain't that good. And if you try and use these regular PN junction

**Dave Jones:** diodes in switch-mode power supplies and things, where efficiency matters, you can be like losing a lot of um heat, a lot of power in your diode. So, you'll use a Schottky diode here, which has a much lower forward voltage drop. But, when

**Dave Jones:** you reverse bias, uh the voltage on a Schottky diode, this is its curve down here. It actually has like a little lip there that goes down like that. But, don't worry about that. So, the reverse current is going to be much higher. It's

**Dave Jones:** This is not to scale. It's kind of As I said, it's like three orders of magnitude more reverse bias current, leakage current on a Schottky than a regular PN junction diode, even a jelly bean one. So, you'll have much greater leakage current at um

**Dave Jones:** even very low reverse bias voltages like we saw there, 5 V. That's nothing burger. Um you Yeah, we'll get in microamps of leakage current. And this changes greatly with temperature as well, as we'll see in a minute. So,

**Dave Jones:** let's look at the data sheet of a Schottky diode versus say a 1N4148 regular signal diode. They tell you right up the front, very small conduction losses, extremely fast switching, low forward voltage drop, high frequency operation. That are some

**Dave Jones:** of the main advantages of Schottky. They're higher frequency switching, they're lower voltage drop, they're even lower noise if that matters to you, and they have no reverse recovery uh charge, and all sorts of things. They really are excellent diodes, which is why they're

**Dave Jones:** incredibly widely used in all sorts of power applications. But, there's two big downsides to Schottky diodes. One is that reverse leakage current we've been looking at. The other is that they're generally not as high a voltage. You're only talking like 100, 200 V maximum

**Dave Jones:** reverse uh voltage on a uh Schottky diode. You can get like a really specialized ones that go a bit higher, but PN junction ones can go very high, like, you know, 500 V or even 1,000 V or something like that. But, um yeah, the

**Dave Jones:** reverse leakage is a killer. So, So, is the one uh used in the uh example. And right off the bat, we've got our electrical characteristics here. We're going to maximum average reverse current at rated DC blocking voltage. So, at 40

**Dave Jones:** V or whatever this diode is. Look, it's it's milliamps. It's milliamps. We got 1 MILLIAMP. >> [laughter] >> AND AT 100° C, it's 10 milliamps. Not the microamps anymore, milliamps. Unbelievable. That's just incredibly high leakage. Crazy. But, our 1N4148,

**Dave Jones:** our jelly bean PN junction diode, uh reverse current nanoamps. And 25 nanoamps typically at 20 V, which is quite a high voltage. Um so, yeah. But, you know, it'll go up to you can get microamps at, you know, when

**Dave Jones:** you're talking about 150° C, for example, but still like, you know, it's as I said, like can be three orders of magnitude lower at regular uh temperatures and voltages. So, for the 4148 PN junction, we've got the reverse leakage current here. And

**Dave Jones:** you can like it's microamps here. And you can see that at 25, they've got three different characteristic curves for three different uh temperatures. At 25° C, we're only talking like my 0.01 microamps. We're talking 10 nanoamps here, right at like 20 V.

**Dave Jones:** That's just like right there. That's crazy. But, here's the Schottky diode. Once again, at 20 V here at 25° C, we're in the milliamps now for our reverse leakage current. So, we're talking So, we're talking about like four microamps

**Dave Jones:** there, which is basically in around the region that we were measuring there um at the lower voltage, you know, we were measuring like 2.2. So, yeah, it's basically bang on to the data sheet here. We were just using the SMD version

**Dave Jones:** of this. Um so, very similar characteristic uh curves. So, that's why we're measuring a couple of uh microamps, but when you go back and you compare that to the PN junction, you're talking nanoamps. Three orders of magnitude. That's a

**Dave Jones:** thousand times, if you don't know what order of magnitude is. I've done a video on order of magnitude. Look at it. So, to answer the original question, let's go back to the diagram here. We've got What was missing was the 10-megohm

**Dave Jones:** resistor inside the Fluke 77 multimeter here, around about 10 meg, and we've got our reverse-biased uh Schottky diode here, cuz it's a Schottky diode. It's got three orders of magnitude more leakage. So, there's going to be a reverse leakage current through there.

**Dave Jones:** What is that value? We can calculate it with Ohm's law. We've got 4.73 V divided by 10 megohms. Get your computer out. And that value is 473 nanoamps or 0.473 microamps. Doesn't sound like much, but when you've got a high input impedance

**Dave Jones:** multimeter like this, it's going to matter. And that's why you're reading the voltage there, and that's why with a Schottky diode of 10 nanoamps, run it again. So, 10 meg * 10 nanoamps, should be able to do that in your head. It's

**Dave Jones:** 0.1 V. So, that's why we're reading like we weren't reading precisely zero. We were reading close to zero. It was 0.05 or 0.1 or something, you know, it was in that order because we're getting nanoamps of leakage current. So, this

**Dave Jones:** particular question is interesting because it's a measurement thing when the old-school trap of your multimeter has an input impedance. But, if you had another multimeter like a bench multimeter, they can have gigaohms, essentially almost infinite, not quite, but gigaohms of input impedance on the

**Dave Jones:** lower voltage ranges. It's It's simple Ohm's law. You've got current flowing through that circuit from your 5-V rail here. And that current will increase based on the voltage. So, if we go back to our curve here, we can see here that

**Dave Jones:** the leakage current does increase with voltage like this. It depends on the Schottky diode could be better or worse than this, but it's going to increase. And the PN junction diodes, they'll increase as well. Um you know, a similar sort of order

**Dave Jones:** differential increase with increased reverse voltage here, but we're still three orders of magnitude lower than a Schottky. And there's some other differences with Schottky diodes compared to PN junction. PNs will have avalanche breakdown as opposed to the breakdown of a Schottky, which is more

**Dave Jones:** sort of like smooth and gentle and things like that. And we could maybe if you want a follow up video of you know, stuff like that, let us know in the comments, but there you go. I hope you

**Dave Jones:** found that as interesting a question as I did. There it goes into the differences between different types of diodes. They can make a huge difference depending on the application. So, Schottky diodes in this sort of application uh you want as lower voltage

**Dave Jones:** drop there as possible. And also, if you're using it as a reverse polarity protection like a clamping reverse voltage clamping protection, for example, having this Schottky diode clamp at like you know, 0.2 volts or something, that means that you're

**Dave Jones:** protecting other PN junctions, transistors, integrated circuits in your circuit that you clamp them below the typical silicon uh threshold of like 0.6 volts. Whereas, if you used a regular PN junction diode as a reverse clamping diode, it might be 0.6, 0.7 volts, even

**Dave Jones:** more as it clamps the you know, really high current through there. And then that 0.6 volts can turn on or higher voltage can turn on PN junctions in your circuit that you're trying to protect. And well, yeah, you can release the

**Dave Jones:** magic smoke and come a gutter. So, a Schottky diode is yeah, the perfect thing to use in like a forward voltage drop protection application like this um that just stops reverse current going in this direction, but not leakage current. So, it'd be an

**Dave Jones:** excellent uh reverse clamping uh diode in here to actually protect this point in your circuit uh from any uh reverse voltages. So, um yeah, better than a PN junction diode. It's just, yeah, in this particular case, it's it's just a measurement thing. But,

**Dave Jones:** in this particular case, Line Ve was probably troubleshooting whatever uh circuit this is and just happened to be probing around and saw a 5 V on this point and went, "I haven't got the USB 5 V USB supply plugged in. Why

**Dave Jones:** am I measuring 5 V here if this diode is supposed to block it? Should be reading zero." Nah, it's because of the pesky leakage and the internal resistance of the multimeter. That's really interesting. And of course, the classic

**Dave Jones:** uh trap with uh using multimeters in circuit for measuring voltage is that you've got any point in your circuit, if you're measuring this point here in your circuit, just be aware that you're putting that 10 megaohm resistor across there. And if you're measuring

**Dave Jones:** voltages in high impedance circuits, that can really ruin your day. You can get false readings because your multimeter has a 10 megaohm input resistance or thereabouts on almost every voltage range, AC or DC. So, to show you the difference what the input

**Dave Jones:** impedance of your multimeter makes and how you can actually come a gutser in this particular case uh with a digital multimeter and its high input impedance, this is one of your more rare examples where lower input impedance helps. So,

**Dave Jones:** we've got 10 megaohms input impedance here, but let's get an old school analog multimeter. In this case, we've got a Bobby Dazzler. It's the Triplett 630-NA. I've done a teardown video on this. And you can see ohms per volt there. So,

**Dave Jones:** it's got 10,000 ohms per volt. So, we're on the 12-V range. 12 V * 10,000 is 120k, not 10 meg. There you go. Using another ohmmeter, we can actually measure that. 120k input impedance, as opposed to 10 meg. So, with our reverse biased

**Dave Jones:** Schottky diode here with 10 meg, we're measuring practically the 5 V. Now, if we plug in our analog meter in parallel, so we've got 10 meg in parallel with 120k, WHICH IS BASICALLY 120K. WHAT? There you go. It's dropped to 0.33 V.

**Dave Jones:** And if we actually lower the range down to three, well, we can barely see it. 3 V there. Look, 0.08 V. Now, if we go to 0.6 V range, then we're even lower input impedance on this multimeter, and we're

**Dave Jones:** measuring zero, exactly as we should. And if I go to the 6-V range, which I can because I've got a voltage doubler here, and if we forward bias our diode, there we go. We're measuring our 5 V, or

**Dave Jones:** 4.91 V with a bit of a forward bias voltage drop there. See? Input impedance, it's everything. Or another way you could have done this is use your low impedance range down here to actually measure. You're going to get like a 2k auto range, but it's so

**Dave Jones:** low, it's not going to measure it. But, it will measure the 5 V in the other direction. We're getting a bit more voltage drop there, 0.2 V because it's a lower value load. It's about 1k, 2k, something like that. So, there you go.

**Dave Jones:** Hope you found that video as interesting as I did. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.

**Dave Jones:** >> [music]
