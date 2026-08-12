---
video_id: fHoHYEZnVIg
title: EEVblog 1401 - DC Fundamentals Part 6: DC Power, Efficiency, & Maximum Power Transfer Theory
url: https://www.youtube.com/watch?v=fHoHYEZnVIg
source: youtube-asr
timestamps: {"0": 1, "1": 9, "2": 23, "3": 39, "4": 49, "5": 74, "6": 94, "7": 104, "8": 119, "9": 130, "10": 141, "11": 155, "12": 164, "13": 179, "14": 196, "15": 207, "16": 216, "17": 229, "18": 239, "19": 252, "20": 261, "21": 275, "22": 284, "23": 298, "24": 310, "25": 324, "26": 335, "27": 357, "28": 367, "29": 391, "30": 415, "31": 427, "32": 451, "33": 466, "34": 486, "35": 496, "36": 507, "37": 517, "38": 534, "39": 551, "40": 563, "41": 582, "42": 591, "43": 602, "44": 615, "45": 631, "46": 649, "47": 663, "48": 676, "49": 701, "50": 718, "51": 729, "52": 745, "53": 755, "54": 773, "55": 787, "56": 807, "57": 826, "58": 840, "59": 850, "60": 862, "61": 871, "62": 886, "63": 898, "64": 912, "65": 924, "66": 939, "67": 953, "68": 962, "69": 975, "70": 988, "71": 1001, "72": 1007, "73": 1026, "74": 1040, "75": 1055, "76": 1063, "77": 1078, "78": 1086, "79": 1106, "80": 1121, "81": 1136, "82": 1151, "83": 1163, "84": 1174, "85": 1185, "86": 1196, "87": 1212, "88": 1228, "89": 1241, "90": 1253, "91": 1261, "92": 1277, "93": 1288, "94": 1301, "95": 1313, "96": 1321, "97": 1335, "98": 1345, "99": 1356, "100": 1370, "101": 1380}
---

**Dave Jones:** Hi, it's electronics fundamentals time again and in this video we're going to finish off a basic DC circuit theory or steady state DC circuit theory cuz we haven't covered transients yet.

**Dave Jones:** That's got to be next. Anyway, we're going to have a look at DC power efficiency and maximum power transfer and this is basically the end of the DC circuit theory which we covered in voltage and current sources.

**Dave Jones:** We did mesh analysis, nodal analysis, superposition theorem. We did Thevenin equivalent circuits, Norton equivalent circuits. So basic DC circuit power and efficiency will finish all that off nicely. Let's take a look.

**Dave Jones:** So in any linear resistor at all here, yeah, I've used the square box symbol. You can, I know, for all you fan boys, here you go. I'll use the zigzag symbol.

**Dave Jones:** There you go. Anyway, you've got a resistance and that resistance can be anything as we explained in previous videos. It can be inside a battery, inside a power supply, any voltage source, the internal resistance of a voltage source, it could be a resistor in your circuit, it could be a PCB trace, it could be wiring, it could be transformer resistance, it could be inductive resistance, it can be almost

**Dave Jones:** anything and when you pass current I through that resistance, you will get a voltage drop based on Ohm's law and it will also dissipate power in watts, which is also joules per second, not to be confused with the rate of energy consumption which I've covered in another video, not to confuse power and energy.

**Dave Jones:** So I'll link that one in up here and down below. So once again, we've got some basic formulas which you absolutely have to remember to do any basic electronics at all.

**Dave Jones:** If you're not remembering these formulas in these red boxes here, then well, you don't know electronics. They're just like you use them absolutely everywhere. So briefly, Ohm's law of course, you can think of it as the Ohm's law triangle, as it's called.

**Dave Jones:** It's just a nice visual representation of voltage, current, which is I, and R, which is resistance. And you can just if you visualize that, and we've got an equivalent one for power, too.

**Dave Jones:** If you visualize that, then you can you don't actually have to remember the formulas. If you visualize that, you can create the formulas. Voltage equals current times resistance, cuz they're next to each other, so it's like dot, it's times.

**Dave Jones:** And current, here, is voltage over resistance, like that. That little bar in there, you can think of that as like divided by. So, I equals V on R. And likewise for resistance, it's voltage on current.

**Dave Jones:** So, there your basic Ohm's law formulas. Now, we have a similar one for I've called it the power law, but that's not really what it is. It's just It's just power.

**Dave Jones:** Anyway, we'll run with that. Similar power triangle, we'll call this. P is over I times V. So, power in watts is current times voltage. And likewise, current is power divided by voltage.

**Dave Jones:** And voltage is power divided by current. That's it. Memorize them. You'll need to know those. And of course, anytime you're dissipating power in watts in any sort of resistance at all, it's going to heat up.

**Dave Jones:** It's going to generate power, and that can lead to non-linearity and things like that, which we don't really want to get into, cuz this is all DC step like linear DC circuit uh theorem here.

**Dave Jones:** But basically, you know, like a light bulb, for example, is just a resistive wire in it. As it heats up, it goes up in resistance. And we won't get into temperature coefficients and all that sort of stuff.

**Dave Jones:** But you just need to know that uh can and almost always changes with temperature. There are very low temperature coefficient materials. Oh god, I'm getting into it. No, don't worry.

**Dave Jones:** P, learn these. Now, P equals I times V, but there's some instances where you may not know the current because you haven't measured it or you may not know the voltage because you haven't measured it.

**Dave Jones:** So, these uh this actually uh derives out into two other formulas which are very common and you must know these as well. Arguably, just as important as these cuz you'll use them everywhere.

**Dave Jones:** So, the way it works is we can assume, well, we don't know what voltage is, but Ohm's law says voltage is current times resistance. So, we just substitute that in here.

**Dave Jones:** So, it's current times current times resistance, and that works out to I squared R or current times current times resistance, but that's how it's written, I squared R. And that formula is used everywhere.

**Dave Jones:** You want to impress someone at a job interview or something like that, just say, "Oh, yeah, that's due to I squared R losses." You'll get that everywhere cuz there's I squared R losses in everything.

**Dave Jones:** As I said, PCB traces, wires, inductors have I squared R losses. Like, why is that inductor heating up? I squared R losses. Why does a transformer heat up? I squared R losses.

**Dave Jones:** Well, there's magnetic reasons as well, but I squared R losses. And then, because there's series resistance in practically every active component out there, it may dissipate a little bit of power.

**Dave Jones:** It may have some I squared R losses in it. Even a capacitor, for example, is got an equivalent series resistance, lead resistance on the physical capacitor. Even if it's a surface mount uh capacitor, those little end caps in there, they've all got resistances.

**Dave Jones:** Your solder joints have resistances. Your PCB traces, everything has resistance, and they will have I squared R losses when you pass any current through it at all, you'll have get I squared R losses.

**Dave Jones:** So, that's a really cool term to throw around. I squared R losses. Nobody really goes around saying, "Oh, V squared on R losses." Nah, even though it's the same thing because we can once again, how we substituted before it when we didn't know the voltage if we don't know the current then what current equals voltage on resistance so we can just substitute oh here it is substitute

**Dave Jones:** I here with V on R so it's V on R times voltage and of course V times V is V squared and then don't forget your R divided by R.

**Dave Jones:** So there you go there's your two formulas for power as well as these but you'll use those all time as well. Cuz you don't often know both of those parameters because you haven't measured them and because you may want to convert from one specific voltage current resistance or power to another particular thing there are actually more formulas which you derive from these like current for example is square root

**Dave Jones:** of P on R and voltage is equal to square root of P times R and there's actually what's called an Ohm's law circle Ohm's law pie chart which actually like lists all of these formulas and there's like you don't have to remember them all once you know you can actually just derive them when you need them like it's not hard to derive these from here I mean you know P equals I squared R for

**Dave Jones:** example well you want to get I out well you got P on R so you take out the R P on R and then I squared well you have to get the square root of that and that's how you get the equation anyway there's a few more.

**Dave Jones:** So this leads us into the second thing we're going to talk about today which is efficiency one of three things. Now anytime of course you're dissipating power in a resistor when you involve power you're talking about efficiency how efficient is it to convert that electrical energy in watts into whatever it is you're trying to do whatever work you're trying to do.

**Dave Jones:** Now there is actually such a thing as a 100% perfect efficiency it's called a resistor because when you actually dissipate 1 W in a resistor, that is 1 W that's generated as heat.

**Dave Jones:** It is 100% efficient. But the resistor is pretty much the only thing that's 100% efficient. Now, unfortunately, when you want to convert electrical energy into another form of energy, be it mechanical energy through a motor, light for example through an LED, you might want to convert it into some sort of magnetic form as well.

**Dave Jones:** You might want to convert it into sound. You might want to convert it into a whole host of different types of things. Well, unfortunately, you're not going to be 100% efficient.

**Dave Jones:** So, you're going to get some losses. So, this is where we have another equation which you must know cuz you'll use it absolutely everywhere in engineering. And that's the efficiency equation for power.

**Dave Jones:** Now, if we talk in terms of say a DC to DC converter, which it converts one voltage into another voltage like a 240-V mains AC for example, converts it into DC.

**Dave Jones:** Doesn't have to be DC to DC. It could be AC to DC or AC to AC or DC to AC or whatever it is, right? When you're converting one form of voltage to another, you're going to have an input power in watts, and you're going to have an output power in watts.

**Dave Jones:** And of course, because it's not 100% efficient, the output power will always be less than the input power for anything you've got, any system at all. Because well, if your output power's greater than your input power, yeah, we're talking about over unity wack job central.

**Dave Jones:** And I've done a few videos on that. And because someone will mention there is a thing called coefficient of performance, and I've done that in other videos like air conditioners for example.

**Dave Jones:** A 1-kW air conditioner might have say 3 kW of cooling power. And there's tricky business there. There's other things other outside elements involved in that sort of thing. But any contained system like this, you can't get more output power than you put into it cuz that's called over unity.

**Dave Jones:** Ain't happening. Laws of physics, captain. We'll use another example where you're lighting an LED, for example. You've got an input power coming from your power source, your power supply, your battery, whatever it is.

**Dave Jones:** Um and then you might have a series dropper resistor here. I won't go into why, but a series dropper resistor, that's going to dissipate some power there. So, you're already lost some power there.

**Dave Jones:** But, the LED isn't 100% efficient in turning the current in there or the power that you're putting into that LED into lumens light output. It's going to have what's called a lumens per watt figure.

**Dave Jones:** It's going to have an efficiency figure for just that component. So, you're going to lose power there and you're going to lose power there as well. So, that doesn't quite relate to our power in power out efficiency equation here because we're not power out, we're lumens out, we're other form of energy output.

**Dave Jones:** But, if you're talking about a electrical circuit with electrical power in and electrical power out, this equation applies. Learn it. The efficient You probably already know it. The efficiency in percentage is the output power divided by the input power times 100 and that gives you your percentage figure.

**Dave Jones:** And that's You probably learned that in school. And because we're effectively talking about losses here or the useful power that's actually being used here, the efficiency in percentage is also equal to power out over power out plus losses times 100.

**Dave Jones:** It's just like It depends which way you want to think about it. So, it's incredibly simple. Efficiency in power, it can be 100% if you're just talking about a resistor or it's going to be less than that in terms of like a useful output.

**Dave Jones:** So, if you want useful light output, lumens. If you want useful mechanical, you know, force in Newtons or whatever it is. You've got some actuator or something. Once again, you're going to have some losses in the system due to the conversion process of the actual device you're using to convert, any internal resistances of any sort of all the components, all the wiring, everything else inside the thing, it's

**Dave Jones:** all got losses internal. But, power is never wasted. It's always conserved. So, it even if you're you're not getting all your lumens out, the rest of the power will be dissipated as heat both in this dropper resistor and the heat uh from the LED.

**Dave Jones:** This is why LEDs are mounted on heatsinks. You're most certainly familiar with this with LED lighting. They heat up. Why do they heat up? It's because like LEDs aren't that efficient.

**Dave Jones:** Like they piss away like 70% of their power in heat just in the diode itself. Last thing we're going to look at, and a very important principle in electronics, is maximum power transfer or the maximum power transfer theorem, as it's called, and it's incredibly simple.

**Dave Jones:** When you've got a voltage source like this, and as we learned about in voltage and current sources, there's no such thing as an ideal voltage source, so it must have an internal resistance.

**Dave Jones:** So, we'll call that RS here for source. The source resistance, I'll put the two little dots there. This will power a load resistance. Now, this raises the simple question, at what value of resistance here and series resistance in your source will you be able to deliver the maximum power into your load?

**Dave Jones:** And you might think, "Well, that's easy, Dave. Um if RS is zero, then uh you've always got maximum power. But, yeah, okay, smart alec. Uh there's no such thing as a ideal voltage source.

**Dave Jones:** RS must be greater than zero. So, how can you actually deliver maximum power into that? Cuz if you're delivering lots of current in here, this internal resistance of your uh voltage source here or your generator, or your battery, whatever it is, it's going to start to heat up cuz it's dissipating power, huh?

**Dave Jones:** And so, at what point are we going to deliver max be able to deliver maximum power into our load resistor? Well, the maximum power theorem states maximum power that should be delivered to the load is when the load resistance is equal to the source resistance.

**Dave Jones:** And at first thought, that doesn't make sense. Because you might be thinking, "Well, if I just make RS smaller and smaller and smaller and smaller, surely I'm able to deliver more power into the load." But, that's not actually the case.

**Dave Jones:** And we'll take a look at actually the graph and data for this in a second. So, it's it's not intuitive that that's the case. At least I don't think so anyway.

**Dave Jones:** And this also has applications in terms of load matching, you know, transmission lines. So, you have to match your 50 ohm transmission line with your 50 ohm source to prevent reflections and things like that.

**Dave Jones:** Anyway, that's way outside the scope of this, but you know, it's it's a similar sort of thing happening. You have to match your load with your source. And that's when you can deliver the maximum power.

**Dave Jones:** Let's move our little troll here and let's have a graph of resistance R here versus P in power like this. Now, if our load resistor's is is incredibly high, it's infinite, it's open, okay?

**Dave Jones:** It's right up here, then we're going to dissipate no power in that load, right? Because well, do you do you do Ohm's everything else we've learned, right? So, let's say it's out here like this, right?

**Dave Jones:** That's our little infinite dot there. Now, if our resistance is a short circuit, it's got zero ohms, and of course, the voltage drop across uh the resistance is going to be zero because well, any current times zero is going to be zero.

**Dave Jones:** And well, the power dissipated in your load here, current times voltage. Well, you can have as much current as you want, if your voltage is zero, you're going to get zero.

**Dave Jones:** So, right over here, we're going to have another dot that's zero. And at some point, the curve's actually going to look something like this. And at this point here, this is our maximum power that we can actually deliver into the load.

**Dave Jones:** And the theorem states, and it's true, that will be the case when RL matches RS. And if you don't believe me, let's run some numbers. First of all, we need the equation for the power in the load here.

**Dave Jones:** And through Ohm's law, power laws, everything we saw before, power in the load equals I squared times R, but we don't know what I is, so we have to calculate it.

**Dave Jones:** Current is just voltage divided by resistance. So, it's the voltage source divided by the total resistance here, which is RS plus RL, like that, and then squared times RL.

**Dave Jones:** So, that's we've just derived our equation using our cool formulas that we have before. It's really easy to calculate the power in the load. So, now let's assume that our voltage source is 1 volt, and our source resistance is 10 ohms here.

**Dave Jones:** That doesn't change. Let's assume it's completely fixed. And let's change our load resistance. So, I've got different value load resistance here. 1 ohm, 5 ohm, 10, 50, and 100 ohms here.

**Dave Jones:** What is the power in the load? Well, get your calculator out, and you can calculate for a 1 ohm load, the power in the load is 8 mW there.

**Dave Jones:** For 5 ohms, it's 22 mW. It's going up. For 10 ohms, it's 25 mW, but when you go above 10, it starts going back down again. 50 ohms here works out to 14 mW, and 100 ohms drops back to 8 mW.

**Dave Jones:** There is a point here. There's going to be a maximum power point on your curve here where you can deliver the maximum amount of power in the load. And it works out, as we saw here, well, if you run enough numbers here, you'll find that it is precisely 10.

**Dave Jones:** When the load resistor is 10 ohms, when it matches the source resistance, that's when you can deliver the maximum amount of power. The best way to have a look at this is let's go to a quick spreadsheet and run the numbers and plot a graph.

**Dave Jones:** Let's plot a graph on Excel, shall we? Now, we've got our source voltage here, our source resistance, and we're going to plot the power in the load resistance RL here.

**Dave Jones:** So, on the Y axis, we've got the power in the load resistance in watts. On X axis, we've got the load resistance in ohms. And over here, we've got the voltage, which we're going to fix, and our source resistance, which we're going to fix.

**Dave Jones:** We're going to have 100 ohms. And I won't spoil it yet by typing in a voltage. And then we've got our load resistance here, which varies in 5-ohm increments.

**Dave Jones:** You can do whatever resolution you want. 5 ohms is going to be good enough for us to see our graph. And then we're going to calculate the current here, which is the voltage in cell B1 here, divided by D2, which is the load resistance plus the fixed source resistance B2 over here.

**Dave Jones:** And if you're wondering what these dollars means in a formula in Excel like this, it means basically that's a fixed cell. Don't auto increment. So, when we actually when we put our put our formula into here, and then we drag our formula down like that, it's not going to increment.

**Dave Jones:** So, you'll notice that B1 and B2 there with the dollars next to them are not incrementing, but the other cell does. That's how you put a fixed element, a fixed variable into your equation without having to auto increment.

**Dave Jones:** And then we calculate our load power, which is simply E2, which is the current squared, I squared R. Remember that? So, the current result here squared times D2, which is the load resistance, and we're going to plot this.

**Dave Jones:** So, let's put in 100 V, shall we? Ta-da! Magic! There it is. It starts at zero, it peaks up here, and it will eventually, if you go to infinite, it will eventually go back to zero.

**Dave Jones:** It tapers off, but it takes a long time to get this load resistance up to you know, gigohms or whatever, you know, megohms, gigohms that's required to sort of see this drop back down to zero.

**Dave Jones:** So, we can then just muck around with that. So, we can just muck around with this. We can go to 500 ohms and it shifts like this, but there is still a peak point there where you go into get that.

**Dave Jones:** So, it's going to reach a peak value of 25 W there, and that happens at 0.100, which is 100 ohms. There it is there, and of course, that matches that up there.

**Dave Jones:** The source equal matches the load resistance, AND IT DOESN'T MATTER WHAT VALUE YOU TAKE you take it down to 10. Now, we're getting towards the resolution of our 5-ohm resolution here, but if we did we get the exact same smooth graph, and if we zoomed in, it would all be exactly the same.

**Dave Jones:** And we can put 1,000 out here, and it'll peak at 1,000 over here. See? Magic! Love it. But that's not really intuitive, is it? It's Remember, we're talking about power in the resistance here, not the current.

**Dave Jones:** If you were talking about the current, then sure enough, when RL goes to zero, that's when you get maximum current, but we're talking about power, which has this sneaky little squared formula in it.

**Dave Jones:** Now, unfortunately, Excel is really stupid and won't let us plot a logarithmic graph on a simple line chart like this. So, you have to do an XY scatter graph in order to get a logarithmic axis.

**Dave Jones:** And And sure enough, there's our axis. If If I turn off log, there it is. We're getting the same thing happening here, but I I run out of data at this point.

**Dave Jones:** But we turn on our logarithmic X axis like this, and bingo, we get a nice smooth bell curve like that. It's beautiful. That's absolutely fantastic, isn't it? And these values aren't aren't corrected down here down the bottom because you can't seem to label as X-Y scatter graph.

**Dave Jones:** Oh, bloody Excel limitations, unbelievable. So, anytime you see a formula with a squared factor in it like that, you know it's probably going to look interesting when you change your axes to logarithmic.

**Dave Jones:** And as it turns out, this actually also has implementations in other aspects of electronics like sharing charge between capacitors and things like that. That's a real tricky one which we might do a video on one day.

**Dave Jones:** But yeah, it's not obvious because we're not talking about current here. Of course, if you want to deliver absolute maximum current into your load, then of course short out your load.

**Dave Jones:** That makes sense, right? You're just going to increase your current and then all of your power is dissipated in your voltage source here, the internal resistance of the voltage source.

**Dave Jones:** And of course, if you short out your load, well, you can heat up and blow up your voltage source, whatever it is, unless you got protection. So, that's pretty nasty, but at there is a sweet spot in there because we're talking about power.

**Dave Jones:** It's a different beast with different equations. The only way you can deliver the maximum power into that load, doesn't matter what it is, is to actually match the source resistance.

**Dave Jones:** Not intuitive, but it works out when you actually analyze. It's one of those wow moments. So, there you have it. That's DC power, electrical efficiency, and maximum power transfer theorem.

**Dave Jones:** And that finishes out our basic steady state DC circuit analysis. We've pretty much covered everything with all the previous videos. Next thing you probably want to move on to is transients in DC circuits.

**Dave Jones:** So, I guess that one will have to be next. So, anyway, if you like this series of videos, please give it a big thumbs up. As always, discuss down below and check out all my alternative platforms.

**Dave Jones:** I'm not just on the YouTubes. Catch you next time.
