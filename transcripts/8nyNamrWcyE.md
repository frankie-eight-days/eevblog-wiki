---
video_id: 8nyNamrWcyE
title: EEVblog 1406 - DC Fundamentals Part 7: DC Circuit Transients Fundamentals
url: https://www.youtube.com/watch?v=8nyNamrWcyE
source: youtube-asr
---

**Dave Jones:** Hi, welcome to another fundamentals video. We're going to carry on from our previous series on DC fundamentals by introducing DC circuit transients or more in particular LC circuit transients, i.e. inductors and capacitors because with our previous videos we've looked at, they've just

**Dave Jones:** dealt with voltage sources, current sources and resistors. And when you deal with those sorts of circuits, when you make a change to the voltage or the current, they change instant taneously. And these resistive circuits we've looked at, they're called steady state

**Dave Jones:** circuits because well, when you change something, it just instantly changes and then it's steady. That's not what happens when you introduce capacitors and inductors into your circuit. They actually take time to charge up and discharge and do other stuff. So, it's

**Dave Jones:** we're not in the realm of steady state anymore, we're in the realm of what's called transient circuits. So, we have to start this off by quickly recapping what is a capacitor, what is an inductor and then we'll get into series and

**Dave Jones:** parallel capacitors, series parallel inductors and then how they charge and discharge and do other stuff. Let's go. Interestingly, it's always referred to as LC. It's never CL. Don't know why that is. It's just a thing. Now, the thing with capacitors and inductors is

**Dave Jones:** they can actually store energy. Capacitors actually store energy in the form of an electric field across a dielectric material and inductors store energy in a magnetic field. And we can actually use these properties to, you know, to useful effect as we'll see in

**Dave Jones:** future videos. But it's the fact of when you build up the the energy in these devices, then that's why it takes time to build that energy up and then to discharge that energy from them. Whereas something like a resistor, it will be

**Dave Jones:** dissipating power when you apply a voltage to it, but it will never store energy. As soon I said before, as soon as you remove the voltage, for example, there's no more power in a resistor. It just It just instantly vanishes. Whereas

**Dave Jones:** these suckers, they can store things, and that makes things a bit complicated. Now, a capacitor is just two metal plates separated by a dielectric material. So, there's no direct electrical connection. It's essentially an insulator. And that dielectric material can just be air. You can just

**Dave Jones:** have two plates or two wires side by side like that. And that's a capacitor. There's capacitance between me and that camera I'm looking at now. It's just You can actually calculate it. In fact, a common tricky exam question

**Dave Jones:** might be, "What's the capacitance between the Earth and the Moon?" Figure it out. Anyway, that dielectric material, it can be air or it can be any of the poly put the kettle on materials for those poly whatever capacitors that

**Dave Jones:** you got. It can be one of the various types of ceramic material for your ceramic capacitors or whatever. And the Basically, air is has a dielectric constant of one. Most other materials are going to have a dielectric constant greater than that.

**Dave Jones:** And that just basically, as you increase the dielectric constant, it just increases the amount of capacitance that a capacitor actually has. But anyway, when you got two plates and you apply a voltage in here, then you'll actually get charge build up,

**Dave Jones:** positive and negative charges on both of the plates like that. So, a capacitor will charge up until the voltage across the capacitor reaches the voltage source, and then that becomes a steady state. But once you you then remove the

**Dave Jones:** voltage from the capacitor, that voltage stays on the capacitor. It's stored in there. There's energy or charge stored up in that capacitor. And one of the basic equations that we've actually got is charge is Q equals C times V, or the

**Dave Jones:** capacitance times the voltage. That's one of the basic electronics formulas you've got to remember. And charge is in coulombs. A one coulomb is actually 6.24 * 10 to the 18 electrons. So, it's a build-up of electrons. And your

**Dave Jones:** capacitance is measured in farads, and a farad is actually a lot of capacitance. And V, of course, measured in volts. But that's your basic formula for charge. You don't often have to use this, but it's important to know. It's one of the

**Dave Jones:** fundamental equations. And of course, you can deep dive down into the physics side of all this and things like that. And we won't do that. We're sticking to the practical electronics side of things. Speaking of practicality, capacitors in series and parallel. I've

**Dave Jones:** drawn three here, but you can have as many as you want, or you can have two. And the formula you might actually recognize from our resistor videos. The total capacitance CT of these three capacitors in series is one over all of

**Dave Jones:** 1 over C1 + 1 over C2 + 1 over C3. And that formula should be familiar to you because it's exactly the same as the parallel resistance formula, except it's kind of flipped now because our capacitors are in series, whereas that

**Dave Jones:** exact equation, just replace C with R, and it's exactly the same for parallel resistors. And yes, just like parallel resistors, if you've only got two of them, then you can use that alternative formula, C1 * C2 over C1 + C2 gives you

**Dave Jones:** your total capacitance. But if you've got more than two, then that formula applies. And for parallel capacitors here, the total capacitance is just C1 + C2 + however many capacitors you got in parallel. And of course, that's the same

**Dave Jones:** as your series resistors. So, just think of resistors and capacitors as opposite. The same formula applies, just in the opposite case. Easy. Now, let's go to back to capacitors in series here for a second because it's important to

**Dave Jones:** remember that the total charge uh, Q is the same on each capacitor. It's a bit counterintuitive. The charge on C1 will be the same as the charge on C2, which will be the same on charge on C3, and

**Dave Jones:** that equals the total charge of the circuit. Now, with ideal capacitors, when you actually have them in series like this, you will actually get an equal voltage on each capacitor like this. V1 will be equal to V2, which will

**Dave Jones:** be equal to V3. Assuming they're ideal capacitors, they're all balanced and everything else. Sometimes you'll actually find what's called, uh, balance resistors actually in parallel with series capacitors like this. You'll find these commonly in, uh, like a power

**Dave Jones:** supply high voltage power supplies and things like that. Just so there's, uh, just to help balance out the capacitors due to just, you know, practical differences in the capacitors. So, anyway, that's just a useful thing to know. And it also helps discharge them

**Dave Jones:** as well. Handy. So, I'm going to take a little bit of a tangent here and actually, uh, use the fact that the cha- the total charge is equal also to the same charge on each of these capacitors. And that we can actually

**Dave Jones:** derive the formula based on this, um, for that using that particular fact. So, I've squeezed it all in down here, so please forgive me. I ran I ran out of room, but, uh, charge Q equals capacitance times voltage up there. So,

**Dave Jones:** as I said, the total circuit charge is equal to the charge on C1, which is equal to the charge on C2, which is equal to charge on C3. You don't add them up. So, um, the charge is equal to C1 times V1 is equal

**Dave Jones:** to C2 times V2 is equal to C2 C3 times V3. And if And if we rearrange this formula, voltage equals charge on capacitance, therefore, voltage one here equals, uh, the charge, Q1 on C1, and voltage two equals charge on Q on C and

**Dave Jones:** the same for the voltage across the three as well. Now, if we take this formula, the total voltage equals the voltage across C1 here plus the voltage across C2 plus the voltage across C3. The voltages add up and if you just

**Dave Jones:** substitute that in, I should have a uh arrow pointing over to that. Then uh V is equal to Q on C which is in V1 is equal to Q on C1, Q on C2, Q on C3 which then translates into our formula over

**Dave Jones:** here. 1 on C, well, that should be CT total. 1 on CT equals 1 on C1 plus 1 on C2 plus 1 on C3. So, you just move those over and you get that formula. 1 on C1 plus C2 plus C3. And that's how you can

**Dave Jones:** actually derive that from that. It's just an interesting little aside. So, you can think of the charge as the current in a series circuit. I I I know this is not a good way, but it's basically the current will be the same

**Dave Jones:** for all of them cuz it's series. Likewise, the charge will be the same for all of them. So, we'll work on transients after we've covered inductors. So, let's have a look at an inductor. When you pass a current

**Dave Jones:** through any wire whatsoever, any component, any PCB trace, doesn't matter what it is, when you pass current through, there will be a magnetic field. So, that's why I've got a wire here, just a straight wire like this. You've

**Dave Jones:** got current I passing through it. It will generate a magnetic field around it. And you might ask, which direction is the magnetic field flowing? Well, there's a handy little rule which you should remember which is called the right-hand rule and it involves exactly

**Dave Jones:** this. It involves a big a single funds a thumbs up. It's the right-hand rule. Take your right hand like this. Point your thumb in the direction of the conventional current flow, not that electron current flow rubbish. conventional current flow like that and

**Dave Jones:** your fingers like this will point in the direction of the magnetic field. That's called the right hand rule. So there is a magnetic field around every inductor. That's why you can add like a little ferrite bead. You've probably seen these

**Dave Jones:** on circuits, a little wire with a little ferrite bead around it and that is essentially an inductor. The ferrite bead just helps sort of contain the magnetic field in there, makes it a bit more effective. But anyway, the way you

**Dave Jones:** usually make inductors more effective is to have multiple turns. I.E. make them into a coil and they can be a physical air coil like that. Open any RF radio tuner, something like that, you know, old school ones and you'll find

**Dave Jones:** then they actually have like little just coils of wire like that. And when you coil them like that, the magnetic fields actually add up and pass through the multiple coils. So that's why you wind inductors into a coil because and and

**Dave Jones:** then you can put like ferrite cores through them or you and you can make them into transformers and you can do all sorts of stuff. That's going to have to be the subject of a future video. But yeah, inductors are more efficient when

**Dave Jones:** you wrap multiple turns around them. So the magnetic fields just add up in the coils and it's more betterer than just a straight wire like that. So just like a capacitor, we can actually store energy inside the magnetic field like this. So

**Dave Jones:** when we apply voltage to it, we'll look at how they charge up and discharge in a minute. But we can actually store energy in a magnetic field so that when you actually release it, there's a few traps for young players. When you release a

**Dave Jones:** voltage or the load from the inductor, if voltage can skyrocket, we'll take a look at that in a minute. Anyway, I'm getting ahead of myself. We've got another basic formula, bread and butter stuff you've got to learn. You won't use

**Dave Jones:** it all that often, but you've got to understand the concept is basically the voltage at any instant in time. That's why it's the instantaneous voltage in volts, of course, is equal to the inductance, which is measured in henries. Once

**Dave Jones:** again, a henry is a very big, just like a farad is a very, very big value of capacitance. A henry, very big value of inductance. And that's multiplied by d i d t. And don't freak out. It's Basically, that just means the change in

**Dave Jones:** the current i over the change in time, like that. So, some people might write it as, you know, delta i or delta t or something like that. But d i d t is just how your mathematicians, you know, put

**Dave Jones:** it. And it's And these are lower case v, i, and t to designate that they're sort of like instantaneous uh values. So, at any instantaneous point in time on the graph, as you will see shortly, that's what your voltage is going to be

**Dave Jones:** equal to. So, if you've got a one henry inductor here, and you've got your current changing one amp per second, d i d t, change of current in over time, one amp per second, that'll give you one volt. Got it? It's a basic formula. And

**Dave Jones:** I don't like to do this, but I'll briefly mention it just for a bit of completeness. Uh then we're talking about Faraday's law of electromagnetic induction, and you can go look up that up. But we get more into the physics side of things,

**Dave Jones:** and that is e uh in volts is equal to minus n, which is the number of turns, and d phi d t there, as it's called, that's the rate of change of magnetic flux in webers per second. Now, the

**Dave Jones:** negative here, this is actually Lenz's law, and you can go look up that and that up. But it basically uh says that uh the voltage is going to be the opposite of what change actually produced it. So, it That's where the

**Dave Jones:** negative comes from. Anyway, that'll actually be important in the discharge side of inductors when we look at that next. So, anyway, inductors in series and parallel, it's opposite to capacitors and it's the same as resistors. When you have inductors in series like this, it's

**Dave Jones:** just the total inductance L is just L1 + L2 + L3 in henries. And when you put them in parallel, the total is once again the same equation. It's exactly the same except you replace C with L like this in parallel. So, if you simply

**Dave Jones:** remember your resistance parallel and serials series formulas, you'll know that capacitors are opposite because they're not resistors. They're They're an open circuit. Whereas inductors are basically the same as resistors because measure an in go and measure an inductor

**Dave Jones:** at DC and it's practically zero ohms cuz it's just a piece of wire. It's a resistor. So, the formulas actually work out the same except your inductors can actually store a magnetic field and your pure resistances can't. Although in

**Dave Jones:** practice, when you're talking about practical electronic component in components, every resistance has a little bit of inductance. Every uh capacitor has a little bit of inductance in the leads. And then every inductance has some capacitance across the coils

**Dave Jones:** and there's Oh, it's just the practicalities of real components is yeah, they're never ideal, but for most purposes, near enough. And once again, just like we uh derive the formula down here like this, you can actually do the

**Dave Jones:** same thing uh from your basic uh formula uh to derive this from this. Try that at home. So, now we move on to the transient part of this. We'll first look at RC transients and then we'll look at

**Dave Jones:** LC transients, i.e. resistor capacitor transients. And as I told you before, there's a charge curve and there's a discharge curve because these aren't resistors. These actually uh store energy. You build up charge or energy into them, and then you can extract uh

**Dave Jones:** energy out of them. So, this is our charge curve. This is our discharge curve. We've got a basic RC circuit here. We've got a voltage source of V. We've got a switch that we can just uh switch to in the up position here. It

**Dave Jones:** charges up the capacitor through this series resistor R here. So, once it's charged up, then we can switch this over to short it out uh to ground, and we can discharge the capacitor through that same resistor. So, let's take a look at

**Dave Jones:** what happens here. So, what we've got is capacitance C, resistance R in farads and ohms, of course, and then we've got a voltage across the capacitor, which is designated uh VCT. That just means that it's uh changing over time because remember, we're

**Dave Jones:** talking about differential calculus here, basically. Ooh, scary, but we're talking about a change in voltage over time here, something changing. That's what differential calculus is. It's just uh like looking at things changing over time. So, uh in this case, we've got our

**Dave Jones:** voltage here versus time, and the voltage is going to rise up like this. And you might notice this curve, it's an exponential curve, and hence why in the formula down here, we've got E, which is an exponential function. So, let's

**Dave Jones:** assume that our switch is down here. Our capacitor is completely discharged. There's no voltage on it whatsoever, and then we suddenly switch it over up to here, and we've got our voltage of, say, 1 V here. Then, it's going to charge up

**Dave Jones:** until it eventually gets to V here, or 1 V. It's going to slowly charge up like this. And that time constant is going to be dependent on the value of the resistor and the capacity here. Now, I should have actually wrote this rule on

**Dave Jones:** the board, but I kind of ran out of room. So, here's the number one rule with capacitors. When they're discharged, when you suddenly apply a voltage to them, they act as a short circuit. Because, remember our formula up here, Q equals C times V. If there's

**Dave Jones:** no charge on the plates of those capacitors, it's completely If it's completely discharged, then the capacitance, it doesn't matter, 1 microfarad, it can be a farad. It doesn't can be a million farads. Doesn't matter what it is. If you've got no

**Dave Jones:** charge, then you're going to have no volts, because volts equals Q divided by C. Zero on C is zero. So, that's why as soon as you apply the voltage over here to a discharged capacitor, this capacitor, it's a short circuit. And

**Dave Jones:** this is why you can actually get lots of issues with large values of capacitances, particularly in power supplies. Have you ever wondered why when you often plug a mains cable into a big, uh, power thumping power supply that has big, uh, DC capacitors there

**Dave Jones:** after the rectifier, and you might get a spark or something like that. That's because there's a lot of current flowing because the capacitors are a short circuit. So, you're going to get this surge of current flowing, and the

**Dave Jones:** current, of course, will be, because this is a short This capacitor is a short circuit, will be just V divided by I. And that series resistance in, say, a mains 240-V power supply, there's really not much resistance there. You've got

**Dave Jones:** the connectors, the wires, and then you've got the basically the diode bridge the equivalent DC resistance of the diode bridge rectifier, and that's pretty much it before it gets to big thumping capacitors. So, the inrush current is going to be very large. This

**Dave Jones:** is why a lot of power supplies will actually have a slow-blow fuse. Because if you put a fast-blow fuse in there, you the inrush current caused by the capacitors being a short circuit can blow fast-blow or quick-blow fuses. So,

**Dave Jones:** that's why you put a little fuse in there that's got a little inductor, which we'll get into. It acts kind of like that, and it's a slow blow fuse that will then prevent that large inrush current from actually blowing the fuse.

**Dave Jones:** Slow blow fuses, important practical aspect of this. Right, so your capacitor is a short circuit. It starts out at 0 V here, and over time it starts to charge up like this. Now, the initial rate of charge will be the quickest, and then it

**Dave Jones:** will slowly slowly taper off as an exponential function. And this is our rise formula, that one of these fundamental formulas you should remember. And this formula applies to both capacitors and inductors, as we'll see in a minute. But so, VCT,

**Dave Jones:** which is what I said, is just the change of voltage over time. It's the instantaneous voltage. So, the voltage at any instant in time T here, with I've written VC cuz it's the voltage across the capacitor, is equal to the

**Dave Jones:** maximum voltage. So, you can think of that as V max, or your source voltage, multiplied by 1 minus E, which is an exponential function. That exponential function is that weird little E to the power of X on your computer here, to the

**Dave Jones:** power of minus T. So, minus whatever the time period is you're talking about, divided by capital T. Not the same thing. Capital T is not the time here, that's little T, like this. Capital T is actually R * C. And this is called the

**Dave Jones:** RC time constant. And you'll see this all the time, and it'll give you like a rough ballpark of how long it takes to charge up a capacitor. And you'll see the RC time constant in lots of things, like the 555 timer, for example. The

**Dave Jones:** formula for 555 timer is 1.1 * RC. The time constant we we might look at it why in a minute. So anyway, rises up fairly quickly and then it follows the exponential curve and eventually eventually after about you know

**Dave Jones:** basically after an order of magnitude after about 10 time constants you can pretty much say it's it's equal to V. In theory it never gets there but that's for those math nerds. In the real world it does. And coincidentally this is the

**Dave Jones:** discharge curve that we're going to look at the fall curve but it's also the current because as I said the current will be a maximum. Just imagine that's not V imagine that's I current I current will start out as a maximum which is V

**Dave Jones:** on I you can't get any more than that cuz there's a pesky series resistance then it starts out at maximum and it follows the basically the inverse of this curve like this until we eventually get no current whatsoever. And that will

**Dave Jones:** be designated IT here like that because it's the value of the instantaneous current at any point in time. Now here's an important thing to realize this RC time constant it's actually an important number. It's actually 63.2% of the charge. Let me show you why.

**Dave Jones:** Basically if you follow the initial charge curve like this up to there. Okay, if if at its initial point if you went in a linear fashion like that and then you dropped this down here like this this point here it'll be equal to 63.2%

**Dave Jones:** of the maximum charge and if you take that down there that is 1 T and then you'll have 2 T here and 3 T and 4 T and so on at that time period. That is called the RC time constant. But

**Dave Jones:** that's how it's actually derived. It's 63.2% It's like that number means something. If you ever see 63.2% you know you're talking about RC or LC time constants. So assume our capacitor is fully charged up to 100%. If we now

**Dave Jones:** flip the switch over to here, we start discharging the capacitor like this. So it starts out This is our discharge curve. This is our full curve here. And once again, it's VCT which is the instantaneous voltage at any point in

**Dave Jones:** time. It starts out at V which is what we charged it up to. Starts out at you know, if this is 1 volt starts out at 1 volt and then it discharges like this. And once again, at time constant is

**Dave Jones:** exactly the same thing. If you follow that curve It's a bit dodgy, but if you follow that curve, trust me, and you'll get to a value of 36.8%. Once again, if you see that figure, either of those figures

**Dave Jones:** there, you know you're talking about LC or RC time constants. And there's another formula you have to remember for the exponential decay or exponential fall in voltage. Once again, VCT equals V times exponential to the power of negative T

**Dave Jones:** on T. It's exactly the same equation except there's no one minus. And you can see why there's a one minus in there for this because V you've got to subtract one. Boop. You start out at zero. It just

**Dave Jones:** means you start out at zero. Whereas this one, we don't start out at zero. We start out at V. So we don't have the one there. But it's exactly the same equation. Once again, it's negative T which is the actual time constant in

**Dave Jones:** here over capital T which is our RC time constant. Just multiply the resistance in ohms by the capacitance in farads. Now, we have to get on to inductors. So I've changed it to LC transients here and I've made a couple of changes. It

**Dave Jones:** looks near identical. Of course I've changed it to an inductor. That's our inductor L there in Henry's and I've got the voltage across the inductor VL T and I've got the current through the inductor which is IT here. Same

**Dave Jones:** resistor, same switch, same voltage source, same everything and similar as well identical curves. They're exponential curves and once again the exponential rise here instead of voltage we've now got current equals I I I put I0. You could say Imax. I just

**Dave Jones:** the zero means like time zero. So I or I maximum which will be V on R of course. That'll be the absolute maximum current you can get out of this thing and that's multiplied. It's exactly the same formula minus T over capital T which is

**Dave Jones:** the time constant. The time constant has now changed instead of times C it's now L on R. So you can substitute L on R in there and some people write this equation as minus T on L and it's exactly the same

**Dave Jones:** thing because if you put that and flip it over. Anyway, if you rearrange the formula it's exactly the same thing. And then the exponential decay it's called a quarter fall. It should be decay is the better you know the more traditional more

**Dave Jones:** correct term for it. Anyway, IT it's exactly the same except we've now got instead of voltage we've got current at time zero and times the exponential minus T on the time constant. And that's it. So we've got to have a look at the

**Dave Jones:** graphs now. Now this one is different. This is now it's exactly the same graph as before but it's now the voltage across the inductor here down here and this is the current through the inductor. And as you can see at time

**Dave Jones:** zero there is no current through the inductor cuz that's the rule for inductors. Just like the rule for capacitors was that assume at time zero when you apply your voltage the capacitor is a short circuit. Inductors are the complete opposite. Assume that

**Dave Jones:** they're an open circuit. This inductor no at time zero when you flick this switch like this and there's no magnetic field in the inductor. As soon as you flick that switch no current flows through there at all due to the

**Dave Jones:** inductance of the magnetic properties of the inductor it resists the flow of current until that magnetic field builds up. So it starts out at zero. So the current starts out at zero and it has an exponential rise like that. It's the

**Dave Jones:** same 63.2% for the one time constant. Once you get to five time constants air good enough for Australia it's you know within 1% or less. And because the inductor is effectively an open circuit no current flows then the voltage across

**Dave Jones:** the inductor is going to equal V because there's no no current through the resistor R Ohm's law there's no voltage drop. So it must start out at Oh, I didn't put the maximum in there but it's Vmax it should be V. And it starts out

**Dave Jones:** there and it decays like that to zero. Once that inductor is what's called saturated magnetic field is saturated and it can't you know hold any more magnetic field in it then you're going to be at the point over here where it's basically a short

**Dave Jones:** circuit because an ideal inductor remember has it's just an inductor it has zero resistance in the coil but of course all practical inductors have a series DC resistance. So it's not going to be precisely zero like this. You'll

**Dave Jones:** have to use your voltage divider which we have looked at in previous videos and then and then you'll have with the in series with the DC resistance of the coil and that's what you're left with. If you leave that switch on long enough

**Dave Jones:** it'll eventually decay down to whatever the DC resistance of that coil is. But in theory zero. Now when we discharge the inductor, a really interesting thing happens uh compared to a capacitor. Remember when we had the capacitor there, it had the charge built

**Dave Jones:** up on the capacitor, and when we moved the switch over and discharged it, uh it stayed like the same voltage uh V maximum, and then it, you know, it it slowly decayed. The voltage uh slowly decayed like this. Inductors, something

**Dave Jones:** weird happens. You remember uh the negative in Faraday's thing over here, which is uh Lenz's law, and I won't go into details, but basically, when that magnetic field starts to collapse, cuz when we switch this put this switch over

**Dave Jones:** to here like this, we've got the energy stored in the magnetic field in the inductor, and when you start discharging the inductor, the magnetic field starts to collapse, and when that happens, this negative sign comes into play. The

**Dave Jones:** inductor will do what it has to do to keep maintaining the current flow in this direction, and that means when we were charging up, it was positive and negative like this, but when we start to collapse that magnetic field and

**Dave Jones:** discharge this inductor, Ah. Whoop. I can't get rid of that. Damn it. This changes voltage like this. Aha. And this is a big trap for young players, and uh but we can actually use this also uh to our advantage. But if

**Dave Jones:** you actually don't um discharge it through a resistor like this, if you just uh like open like put the switch in the middle, just open it, so there's no current flow, the magnetic field still starts to collapse, and when it does

**Dave Jones:** that, in theory, because there's no current flow, it generates an in theory, generates an infinite negative voltage across that inductor. In the in practice, it's never infinite, but it's very high. And this is why you can get large voltage inductive kickbacks, and

**Dave Jones:** these are very useful in some circuits like your ignition uh coil in your car and that's how you can generate like large spikes and things like that to actually magnetic fluoro ballast in the old you know fluorescent lights for example the

**Dave Jones:** collapsing magnetic field generates a large voltage which then creates the arc and starts up the lamp. That's how the starters work in the magnetic fluoro ballast. You can actually generate large voltages by collapsing a magnetic field and this is why inductors have some uses

**Dave Jones:** that capacitors don't. But because of that inductors they used What are they used in? Relay coils of course. So if you're drive if your chip is driving a relay coil like this and then once the once you actually remove

**Dave Jones:** the current from the relay then the magnetic field of the relay is going to collapse and it'll generate a large negative voltage on the inductor and well that could blow your circuit up. So you've got to have reverse diode

**Dave Jones:** protection on your coil like this. So you'll put a reverse bias diode on there so that when this collapses this is positive this is negative your diode will will conduct and it will clamp the voltage across the inductor to negative well 0.6 volts or

**Dave Jones:** negative 0.6 volts. So that's why you can protect your circuit and that's pretty darn essential when you're driving relays or any other inductive loads. And you can see how I said before that when the magnetic field collapses it wants to keep the current going in

**Dave Jones:** the same direction. Well you can see why because if this let's say we flick this switch to open and there's no load whatsoever then the voltage reverses like this and it wants to flow through the diode like that because that's your

**Dave Jones:** anode that's your cathode and the current is still going in the same direction and to do that it's got to flip the voltage. That's just what happens. Can't beat the laws of physics, Captain. So, what actually happens? And go back

**Dave Jones:** to our characteristic graphs like this, we have to actually flip these over. Well, and this actually becomes V like this. Okay, but it actually becomes negative V. So, this will be minus V down here. So, it when it flips like

**Dave Jones:** this, it'll start out with that negative voltage, as I said, and it'll be the maximum which is equal to V, what it actually was the source actually charged up to. And the current will actually start up here. So, this will become

**Dave Jones:** now I. This will become our current, and it'll start at a maximum if the current is still positive, cuz as I said, it still flows in the same direction like that, which is different, opposite to what the capacitor did. When we're discharging

**Dave Jones:** the capacitor, well, sorry, when we're charging the capacitor, current flows in this way, but when we when we're discharging the capacitor, it flows back out this way like this, because the voltage is still like this. Inductors operate opposite. They flip the voltage

**Dave Jones:** like this, and current still keeps going in the same direction. Not really intuitive, but that's how the physics of collapsing magnetic fields actually works. So, yeah, it's it's still starts out, you know, if this is like if we

**Dave Jones:** charged it up at like an initial 100 milliamps, or you know, if it was 100 milliamps up here, it would start out with 100 if it discharged it through the resistor, it would start out with 100 milliamps here, and then it would slowly

**Dave Jones:** discharge to zero as the voltage on the coil just dropped away to zero. Ohm's law. And then, like I said, if you leave that switch open, if you've got that magnetic field, and all that energy stored in there, and you open it up,

**Dave Jones:** there's no What does it do? It this voltage doesn't go to minus V like this, it goes to as far as it can go in given the physical limits of the actual inductor itself. So, you can get like hundreds of

**Dave Jones:** volts, thousands of volts, when you only charged the thing up when you when your source is only like a couple of volts or 10 volts or something like that. You could get hundreds or even thousands of volts. It depends on the magnetic

**Dave Jones:** properties of the inductor and the amount of inductance you've got. So, phew, scary stuff. And there's more physics to inductors as well, but I won't go into this video has been more than long enough. Geez. RC and LC time constants, we covered a lot of

**Dave Jones:** stuff. We've been at this for like half an hour or something. So, yeah, but it's interesting stuff. Inductors, you got can not only have traps for young players, but it can also be very useful for generating large inductive voltages, which you can

**Dave Jones:** actually take advantage of. It depends what you're trying to do. But, yeah, capacitors have energy stored in a in the dielectric in an electric field, and inductors have their energy stored in a magnetic field within the coil itself

**Dave Jones:** and within the ferrite or whatever material is used for the inductors. And maybe we could go further Well, probably you have to go further into this if you start going into transformer theory and stuff like that, which is

**Dave Jones:** video down the track. So, the next thing that follows on from this video logically is energy stored in capacitors and inductors. And I've actually done a brief video on this on my second channel, the energy equals half CV

**Dave Jones:** squared like this. And that half is a little nasty thing when you start start talking about charging and discharging capacitors. It's a real sneaky math problem, that one. Anyway, I'll link that in down below and probably at the

**Dave Jones:** end somewhere. If you haven't seen that, it was just a test video, but I decided to talk about this. I'll leave it out of this video. So, the rise and decay of voltages and currents in capacitors and inductors, real interesting stuff. So,

**Dave Jones:** you'll be using your confuser a lot for doing these sorts of stuff. And we've only talked about the case where it goes to 100%. If it If you've got a case where it like only goes up to like here

**Dave Jones:** and then starts to discharge again, then well, you've got a substitute your maximum value for, you know, like it's still 63.2 here. So, the time constant thing will still happen like that. It just like starts and ends at a different value.

**Dave Jones:** It's sort of like never gets to there. And you'll get this in like your 555 timers and your other RC time constant circuits and things like that. And RC time constants used pretty much everywhere in electronics, whether it's

**Dave Jones:** in, you know, your microcontroller, for example, you might think, "Well, where am I going to use an RC time constant in a microcontroller?" Well, for the reset pin. I've drawn it here. If you've got the reset pin of your

**Dave Jones:** microcontroller, you want your When you power up your circuit, you want your microcontroller to have a nice clean reset. You don't want it doing, you know, weird stuff while the voltage on your power supply is rising up. No, you

**Dave Jones:** want to keep your microcontroller in reset, and you can do that. Let's say it's not reset like this. So, if the pin is zero, then it's reset. Well, that's what you have a capacitor and a resistor for like this. The capacitor will keep

**Dave Jones:** your reset pin low for the time constant using the formulas that we've looked at until the voltage on this pin reaches This will be a Schmitt trigger, by the way, and I've done a video on Schmitt triggers because, well, you

**Dave Jones:** don't want to use your regular gate in there. Anyway, link in Schmitt trigger video if I remember it. And then, it'll hold the processor in reset for, you know, X milliseconds while the power supply rises up, and your processor not

**Dave Jones:** going to do funny business. It's going to have a nice clean start. So, you know, using RC time constants for your digital stuff. Used all the time. So, this basically ends our DC fundamental series that we've been doing. How many?

**Dave Jones:** Five or six videos or something like that. Pretty much after this and energy stored in a capacitor and inductor and stuff. After that, you pretty much have to move on to AC. Uh DC, done and dusted. Beauty. So,

**Dave Jones:** anyway, I hope you like that video and you found it useful. If you did, please give it a big thumbs up. As always, discuss down below. Catch you next time.
