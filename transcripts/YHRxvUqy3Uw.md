---
video_id: YHRxvUqy3Uw
title: EEVblog 1438 - The TOP 5 Jellybean Regulators & References
url: https://www.youtube.com/watch?v=YHRxvUqy3Uw
source: youtube-asr
---

**Dave Jones:** Hi, I've got another top five jelly bean component for you. This is a follow-up to my previous video which was very popular linked up here and down below if you haven't seen it where I looked at the top five jelly bean op amp

**Dave Jones:** components. So, today we're going to take a look at ta-da, top five voltage linear voltage regulators and references. So, let's get down to it. Now, a jelly bean component is basically an industry standard component that has been around for a long time. It's been

**Dave Jones:** around forever. In case of the first one we're looking at here, like been around for like 40 plus years. So, a long time. And they're still used today as the go-to component for this particular function. They have they set the

**Dave Jones:** industry standard footprint and they're available from many different manufacturers including ones in China that you've never ever heard of. And you're practically guaranteed to be able to get these parts even in the current component shortages crisis cuz there's

**Dave Jones:** just at any one point in time even during times like these, there's going to be millions of these parts out there off the shelf you can use. And if you can't get a particular manufacturer, you can go to another one. The whole idea of

**Dave Jones:** jelly bean components is that the specs are so generic that really it doesn't matter which manufacturer you actually use. You can just drop in a different manufacturer and you're good to go. So, jelly bean components are just something that every

**Dave Jones:** hobbyist or engineer should have knowledge of. You should know the basic specs and you should have them in your CAD packages with all the various footprints and everything and different manufacturers in the related bomb items. And then when you're designing products,

**Dave Jones:** you can just drop in these parts. Oh, I need a regulator. I need an op amp. I need a comparator. Whatever it is, you can just pull it from your jelly bean components library and just drop it in

**Dave Jones:** there knowing you're good to go. Bob's your uncle. First up is linear voltage regulators. None of that uh low dropout rubbish either. This one is an absolute classic. You've guaranteed to have already used this thing. So, but it is the jelly bean

**Dave Jones:** part. When you think of a jelly bean voltage regulator, you think of the 7805 or the 78XX series as it's uh called. And as you can see, dated up here, May 1976. This thing's been around forever. You can get it from

**Dave Jones:** countless manufacturers. But this is a classic uh fixed voltage regulator. So, the 7805 is the 5-V regulator, 78 uh 12 is 12 V, 7815 is 15 V, and there's other little variations in there um of different voltages. But really easy to remember,

**Dave Jones:** classic part. They're almost uh bulletproof, and you should have these in your junk bin, just ready to go at a moment's notice in all different uh types of packages for any scenario. How current? Well, this particular one's up to 1.5

**Dave Jones:** amps, but generically, like the 7805 is typically a 1-amp regulator. So, if you're limited to 1 amp, then you'll be able to go across uh more manufacturers. It's got a thermal overload protection as well. So, if it heats up, you didn't

**Dave Jones:** have adequate heat sink or some fault in your product or something like this, this thing will safely shut down if it gets uh too hot. But if you're getting there, mhm, something's horribly wrong. And it doesn't matter if you short

**Dave Jones:** circuit these suckers, they're short circuit protected, no worries. And it's got safe area compensation. What that means is that uh it will automatically reduce the output short circuit current based on uh the voltage drop across the regulator. It's another protection uh

**Dave Jones:** mechanism, really quite nice. So, yeah, they're incredibly simple to use. Just voltage in, and you get your fixed voltage out. You can actually use these as adjustable regulators, but you generally don't. Um we'll look at adjustable regulators in a minute. And

**Dave Jones:** contrary to popular belief, you do not actually need an output capacitor on these for uh, stability. You don't actually need this uh, 0.1 microfarad on the output. It's actually stable with no output capacitance. You don't need it. And you actually don't need the input

**Dave Jones:** uh, capacitor either unless uh, the regulator is a certain distance um, you know, a large distance away from your input uh, filter cap. But as a general rule, you just put like caps on the input and output. Just uh, because warm

**Dave Jones:** fuzzies. So, it comes in various uh, prefixes. There's the UA here, which is classic. But also TI also do the LM um, 7805 as well. And it's also known as the LM340 as well, but that's not as generic

**Dave Jones:** across different brands. It's just like the 7805, but they're basically identical. And they come in many different packages, which is another uh, jelly bean trait. Old school TO3 here. Oh, yeah. Thank you very much. Or of course, the one you're most

**Dave Jones:** familiar with, the TO220. But one of my personal favorites, the SOT223 here or the uh, D-Pack. And then as I said, it's available from every obscure manufacturer you've never heard of. I I just picked a couple at random. A

**Dave Jones:** Pullup. A Pullup. Or I love this one here. Blue Rocket Electronics. Um, fantastic. Like everyone's got a 7805. It's so jelly bean. And as far as accuracy goes, you can get them down to the one-ish uh, percentage region. On

**Dave Jones:** Semi, for example, do 1 1/2 uh, 2% and 4% uh, tolerance ones down here. But generally, they're well under 5%. They're in the couple of percent uh, region. So, your 5-V regulator is going to be easily within the 5-V TTL spec of

**Dave Jones:** plus minus 0.25 V. No worries. And then if you're wondering what's typically inside one of these, well, look, it's just a Zener here and a resistor, and then that just that's just an emitter follower there, and then it just does

**Dave Jones:** some business, and that's Bob's your uncle. Gives you your output voltage. No worries. And specifications like line regulation here, it's pretty good. Load regulation, it's pretty good. Quiescent current, it can take a little bit there. So, then not the best solution for like

**Dave Jones:** low power stuff. Yeah, the TI UA is like 4 milliamps there. Anyone doing any better? Over here, it's only going to specify a maximum of six, you know, meh. How does the pull-up stack up? Quiescent current, yeah, 4 milliamps. And you can

**Dave Jones:** actually get higher peak currents out of this, like, you know, 2.2 amps, for example. So, but yeah, you generally you treat this as a 1 or 1 and 1/2 amp regulator. Once again, if you're using jelly bean parts

**Dave Jones:** and then you're worried about things like this or you're designing your product around a a particular spec in here, then you're not really using a jelly bean part. You're not in the jelly bean category. The whole idea of jelly

**Dave Jones:** bean is that you can just Yeah, no worries. I'm in a pinch. I can just throw in a different manufacturer, and it's going to work. You don't even have to worry about the specs. So, if you are quibbling over all, this variant from

**Dave Jones:** this manufacturer is Oh, it's tighter than this manufacturer here on this spec, then yeah, nah. You might as well choose something else. And it's a positive voltage regulator. If you need the negative voltage regulator, it's the 79 XX series. Once again, I won't go

**Dave Jones:** through the data sheets. They're just the negative versions. Consider them exactly the same as the positive 78 XX series, except they're designed for negative rails. So, we salute the 7805, probably the jelly bean component for like 45 years at least. Still used in I

**Dave Jones:** don't know how many billions every year. It's just crazy. So, open up any product that doesn't have any like strict uh spec requirements, you need a voltage regulator, you're going to find a 78XX and a 79XX regulator in there. Almost guaranteed.

**Dave Jones:** Now, if you need an adjustable regulator, that brings us to our next jelly bean part, the classic LM317. You should definitely know these. Should have these in your kit ready to go cuz they're used absolutely everywhere. It's got all your favorite specs from the

**Dave Jones:** 7805, uh 1.5 amps nominal. It's got short-circuit current limiting. It's got thermal overload protection. It's got the safe area compensation, etc., etc. It's got more than adequate uh performance on noise, power supply rejection ratio, regulation, and all sorts of things. Um and oh, look at all

**Dave Jones:** the applications. Oh, look, if you're building your femto base stations, this is the ticket, Laddy, let me tell you. These are incredible like the application stuff is just it's so funny to just look at data sheets just for the

**Dave Jones:** application uh things that they put in here. It's just ridiculous. Now, of course, uh it Why do they just put a battery charger circuit? Normally, you don't have the output uh series resistor here. You just have the two resistors here to set the

**Dave Jones:** value. The formula's in the data sheet. Won't go into the details, but voltage in, voltage out. The good thing is it can go to 1.25 volts cuz it's got a 1.25 volt voltage reference in here and we can have a look

**Dave Jones:** at the internal diagram. There it is there. It's got an internal 1.25 volt reference. So, you can go down to that. So, that's very useful for all sorts of modern electronics with low power supply uh rails. And the good thing about uh

**Dave Jones:** having an adjustable regulator in your um jelly bean kit is that it's you only have to stock the one part and then you can use it for all different regulation voltages that you need cuz the 7805's 78XX series, it only goes down to 5

**Dave Jones:** volts. Can't Can't use it anything under that. But the 317, it'll go up to 37 volts here. So, anywhere from 1.25 to 37, absolute killer. All you need is two resistors in there. It's available in all your favorite biggie packages like

**Dave Jones:** this. And once again, this is not a low dropout regulator. We'll have a look at that in a second. One of the downsides is it does have a lower dropout voltage. Uh here we go. Input to output differential voltage, uh 3 volts minimum

**Dave Jones:** typically. So, that's more than the 7805. So, uh but once again, this is not a low dropout regulator. Just be aware though, there is a big trap for young players with the LM317, and this is the minimum load current to maintain

**Dave Jones:** regulation. And given that it's a voltage regulator, you want to maintain regulation. That's kind of its job. And so, you need 3.5 milliamps minimum. So, that's still on par with like the 78XX series, which didn't have a minimum load

**Dave Jones:** current but it had the higher quiescent current. So, it's effectively like it's neither here nor there. They're both are the same in that regard. So, you need that minimum current. So, if you're designing micropower circuits and stuff like that, these aren't the regulators

**Dave Jones:** for you. So, if you actually do want to use the 317, and you do actually only want to draw like 1 milliamp from it or something like that, then you're going to have to put a resistor on the output

**Dave Jones:** to get that minimum current. I do actually I like the on semi data sheet a bit better here. Now, this is the typical application circuit. Once again, you do not actually need the output capacitor for stability, but you

**Dave Jones:** put it in there as a matter of course. You just need uh you usually this is a fixed resistor. 240 is the nominal value, and then you put your adjustable resistor in here. So, a good thing for your bill of materials, if you're using

**Dave Jones:** jelly bean component like the LM317, you always have a like a 240 ohm resistor uh like loaded on your pick and place machine ready to go for all your LM317s that you're using in your circuit and then you try and like reuse that 240

**Dave Jones:** ohms somewhere else. Yeah, you might typically use that then elsewhere in your circuit. You might find you need or a 220 ohm somewhere in your circuit, but I've already got a a 240 for my LM317. So, I'll just use it elsewhere in the

**Dave Jones:** circuit. Parts consolidation. And it shows the packages you can get here. TO-220 classic of course, this up 223, the D pack and there are others available. But this is actually this is where there is actually multiple versions available. This is the LM317M

**Dave Jones:** and this is only a 500 milliamp version. So, the regular LM317 an amp and a half, the M version is 500 milliamps and we'll have a look at a lower power version shortly. And there's your classic formula there for uh calculating your

**Dave Jones:** voltage output and you can rearrange that for your resistor for generating like R2 here. No worries. And the LM317 along with the 7805 actually 78XX is you can turn it into a constant current regulator by just simply shorting the adjustment pin out

**Dave Jones:** to the output and then uh putting a resi- a single resistor in here or this case a pot for adjustable and that makes a really neat constant current circuit. And for like an SLA battery uh charger for example, you might put this constant

**Dave Jones:** current limiter circuit in uh series in front of then a voltage regulator so you have a constant voltage and constant current modes. And that's a classic like you know, sealed sealed lead acid battery charger circuit. So, there's the

**Dave Jones:** 1 and 1/2 amp version. There's the M at 500 milliamps and there there's also an LS317L and that's a nominal 100 milliamps as well. Apart from that, pretty much identical and you'll find these in lots of uh low power circuits. But this is

**Dave Jones:** not really a low power regulator. It's just I love my LM317. It's jelly bean. I want to reuse it, but I only need like up to, you know, 50 or 100 milliamps, something like that, you're whacking the LM317 instead. It's a bit cheaper. But,

**Dave Jones:** the good thing is the packages are small scale as well, SOIC, TO-92, absolute classic. There's a SOT-89 and there's a TSOP package as well. So, there you have it, the LM317, the absolute classic jellybean adjustable voltage regulator. You still find it used in its millions,

**Dave Jones:** probably even billions today. Now, the disadvantage with the two previous regulators we've looked at is that they're not LDOs or what's called a low dropout voltage regulator cuz as you saw, like 2 and 1/2 to 3 volts voltage

**Dave Jones:** differential you've got to have minimum across that regulator. Not only does that dissipate a lot of power, but in a lot of circuits, and especially if you've got cascading regulators, like one power one regulator power from another, etc., you

**Dave Jones:** can find that you just don't have that differential voltage margin available. So, you want a low dropout regulator, and you could argue that this one, the uh 1117, don't worry about the TLV, once again, there's different uh letters in front of them, it doesn't

**Dave Jones:** matter. It's known as the 1117. This is our jellybean low dropout voltage regulator. And the good thing about this is that you can actually get it in its adjustable and fixed. So, you can get the adjustable version just like the

**Dave Jones:** LM317. In fact, the pinout uh is identical, and the formula for calculating the resistor um divider down here is absolutely identical you can think of it as just a low dropout version of the LM317 or 7805. So, you

**Dave Jones:** you could argue that the 1117 is probably more ubiquitous these days. I don't know. Like doing teardowns of stuff, I'm still seeing the 317 and the 7805, but the 1117 is just like low dropout can be really nice sometimes.

**Dave Jones:** So, a lot of designers, a lot of companies will consider the 1117 as the jelly bean version because it has sort of like all the advantages of the 78 XX series and the LM317, but lower dropout regulation. But, it doesn't come without

**Dave Jones:** any downsides. The downside is that this output capacity here is absolutely critical. Stability of low dropout voltage regulator, it's not just the 1117, but low dropout voltage regulator regulators in general is that yeah, they can become unstable if you don't meet

**Dave Jones:** the output capacitance requirements or the output impedance requirements. And you'll see this in the typical application here. Look at how the back protection diode here. This is the same on 317 and 7805 and stuff like that. You've got your

**Dave Jones:** voltage divider here, which you adjust with R2 down here. The formula is identical and you can include an optional capacitor across the just pin it like this and I see note B. Here it is. There you go. Can be in use to

**Dave Jones:** improve the ripple rejection ratio. But, then you'll notice it says if C adjust is used, it's optional, but if you do use it, then the C out must be larger than C adjust. Otherwise, it's going to get all it's going to get

**Dave Jones:** the heebie-jeebies and go unstable on you. So, 100 microfarad output cap and that's one of the disadvantage cuz output capacitors, well, voltage divider resistors, they're cheap. The output capacitor requirements that match the stability, the value, and the impedance needed for the to make

**Dave Jones:** your regulator stable can often come at a high cost. So, jelly bean typically implies lower cost. But, anyway, with low dropout regulators, you don't get a free lunch there. And often there'll be an entire section in a low dropout regulator data sheet

**Dave Jones:** actually devoted to the output capacitor selection. This case it's got output capacitor selection is critical for regulator stability. Larger C out values benefit the regulator by improving transient response and loop stability. Devices designed to be stable with tantalum and

**Dave Jones:** aluminum electrolyte caps with ESR between 0.2 and 10 ohms. So once again, it's not just a matter of having the correct value or the minimum value capacitance there, it's got to be the right type of capacitor and it's got to

**Dave Jones:** have the right equivalent series resistance. If you don't get that right, especially in tran- sients and stuff like that. Like it might work fine during normal operation and then you might get a transient and whoop, if your capacitor's right on the edge of your

**Dave Jones:** stability requirements, then your regulator can start ringing and doing and become unstable, get the heebie-jeebies and go So just be careful with low dropout regulators, not just the triple 17. And they also give layout requirements here for a reason. So yeah, you want to keep

**Dave Jones:** your loops a bit tight. So I said they're available in fixed voltages as well. So you might keep a stock of those uh just available so you don't need the resistors, especially if you're space critical, you can't afford the resistors

**Dave Jones:** in there to adjust it. And they typically add a dash on the end of it, so dash 15, 1.5 volts, 1.8, 2.5, 3.3, 5. And again, available from countless different manufacturers. Here's a data sheet for the cheapest one I could find

**Dave Jones:** on LCSC and it's from Shenzhen tofu semiconductor corp. It's all in Chinese here, you know. And there's the regular packages available. Once again, they have them in the fixed versions as well as just the the they put the ADJ on

**Dave Jones:** there for the adjustable version. And it's the same part. You can just drop it in. You can get it from dozens and dozens of manufacturers. I almost forgot to tell you the dropout voltage. It's going to be a as with all

**Dave Jones:** regulators, it's going to be a function of the output current. So they usually specify it here at different output currents. So at 800 milliamps, it's going to be up to 1.2 volts. So, just consider it like under 1.2 volts here.

**Dave Jones:** What does this uh cheapy here say? 1 to 1.1, something like that. But, if you have factor in 1.2, yeah, that's good enough. But, the 1117 is not the lowest dropout voltage regulator. Like, if you need like in the

**Dave Jones:** order of, you know, 50 millivolts, 100 millivolts dropout, or something like that, then you're going to have to choose other parts. But, this is it is significantly better than the uh 317. That's for sure. So, this is more than

**Dave Jones:** capable of, for example, having like a 3.3 volt rail using the 1117 after like a 7805, or something like that. Whereas, you couldn't use an LM317 there because it would need that like 3 volts voltage drop uh minimum. So, you just can't get

**Dave Jones:** your 3.3 volt rail from a 5 volt rail, for example. Next part we're going to take a look at is a voltage reference, or in this particular case, a micropower shunt voltage reference because often you're need a better precision, better

**Dave Jones:** temperature uh coefficient than you can get with a voltage regulator. A voltage regulator, okay, you've got an LM317, and you can trim it to whatever voltage you want, and you can use it as a voltage reference because you've trimmed it, and

**Dave Jones:** you know, the one you can get them in 1, 1 1/2%. That might be good enough, but often you want better than the couple of percent initial accuracy you can get from a voltage uh regulator. And more often than not though, with a voltage

**Dave Jones:** reference like uh ADCs and other uh precision comparators and stuff like that, you're doing like detecting voltage threshold levels and doing all sorts of other things, you need a voltage reference that is not only initially more accurate than a voltage

**Dave Jones:** regulator, but also has a lower temperature coefficient. And the one we're going to take a look at is the classic LM4040 and 4041. And once again, these date way back. I've got a Microchip one here cuz it actually combines both versions in the

**Dave Jones:** one data sheet, which is nice. But, of course, we could go to the TI data sheet here and LM4040 precision micropower shunt voltage reference. And it looks and acts like a Zener diode. In fact, that's what they actually, you know,

**Dave Jones:** that's the symbol that they actually show here. But, as you saw, that's actually not what's inside this thing. It actually contains an op amp, some transistors, and like an internal precision Zener and stuff, and like an output driver as well, so it can sync some

**Dave Jones:** current. So, these act and look like a Zener, but they're way better. So, these 4040 micropower references, it's the jelly bean go-to part. You can get them in various different grades that range from like only a percent accurate down

**Dave Jones:** to like like 0.1% or so. So, right off the bat, its initial accuracy is better than a voltage regulator. But, when you actually want a voltage reference for an application as opposed to a voltage regulator, you want two things. You want

**Dave Jones:** the initial accuracy, of course, but you also want and often is the most important thing is temperature stability. Now, actually, things like the 7805 aren't that bad in terms of stability. Go to the data sheet here. So, this is a fixed voltage regulator.

**Dave Jones:** Temperature coefficient of output voltage in millivolts per degree C, of course. It's actually 1.1 millivolts per degree C. And if you get your confuser out and put 1.1 millivolts into 5 volts and get a percentage, it's 0.02% per degree Celsius, which actually isn't

**Dave Jones:** too bad. That's actually 200 ppm. That's, you know, almost practically as good as a bottom-of-the-range voltage reference chip. But, a voltage reference doesn't need to deliver a lot of power. So, let's go for an adjustable voltage regulator, which is the 317L here, and

**Dave Jones:** the low power jobby, and temperature stability here. You can see that it doesn't specify per degree C. It just says 0.7% of VO, and well, okay. Yeah, it's poorly specified, too, because we're talking about references. You're talking about PPMs per degree C. You

**Dave Jones:** want to know exactly what the temperature coefficient is, not just some uh typical Look, they don't even give you a maximum figure here. It's just uh you know, it's nothing's guaranteed. This is why you can use a voltage regulator as a crude voltage

**Dave Jones:** reference if you you know, trim it. It It's okay, but it'll get you out of a pinch, but uh yeah, voltage references are where the action is. So, if you go over to the jelly bean voltage reference, the 4040, you can see it

**Dave Jones:** specifies uh uh you know, 100 PPM. You can get like a D grade one at 150 PPM uh per degree C, and it specifies that, and it'll actually guarantee that. It'll give you a maximum. So, not only is that

**Dave Jones:** a banner specification at the top of the data sheet, that's how you can tell it's important, it'll also be a banner spec here, and it'll give you a a maximum. Here it is, 100 PPM per degree C. So,

**Dave Jones:** they've actually been rather generous, cuz often data sheets can be sneaky, and they'll put like the banner specification right at the top of the data sheet will be the typical figure, but they've actually put the worst-case. The typical figure is actually in the

**Dave Jones:** order of like tens of PPM, right? 15 or 20 PPM here. And you know, when you're designing stuff, I you really you should be designing about your maximum uh to take into account your maximum worst-case specification, of course, but in this case, like

**Dave Jones:** typically, like this is an order of magnitude better than a voltage reference in terms of temperature stability, and that's what you care about with a voltage reference. And as you can see here, you can get different grades from 1% down to 0.1% depends on

**Dave Jones:** how much you want to pay. And they come in various fixed output voltages, which are really handy. 2 and 1/2 volts is probably like the most common. Uh but you can actually get 5 volts if you want a precision 5 volt

**Dave Jones:** uh reference. And you can actually use these voltage references as low-power precision voltage regulators. So, if you've got uh say a microcontroller that uses uh your voltage rail as the uh reference for its internal analog-to-digital converter, uh for

**Dave Jones:** example, and it doesn't have an internal reference or you want a better one than what the internal reference is. So, you can actually use one of these voltage references as a voltage regulator, provided of course that you don't uh

**Dave Jones:** exceed the maximum current of these things, which is usually like 10 20 milliamps, in the tens of milliamps region. But if you've got a low-power product, then you can actually use a voltage reference as a voltage regulator. Pretty cool tip. And they

**Dave Jones:** don't call it micropower for nothing, because these can operate from 45 milliamps to 15 milliamps. Oh, yeah, that depends on the resistor value that you set here. So, if you're designing low-power circuit and you need a precision voltage reference in there,

**Dave Jones:** then you can set uh the choose this resistor for this uh basically uh quiescent current here to be as low as 45 milli- microamps, and it will still uh maintain its uh reference and specs. But sometimes, of course, you want to uh

**Dave Jones:** uh uh uh tweak a pot on there to actually get a precision reference. You want to calibrate uh your product uh to get that precision reference and then have it stable um with temperature. You can't, unfortunately, do that with the uh 4040

**Dave Jones:** because it's just got the single resistor like this, and you get what you get, and you don't get upset, as they tell the uh preschool kids. Um but you can get the LM4041 here, which is the same basically the

**Dave Jones:** same part, but it has an extra pin on here. It's got a feedback, it's got an adjustment pin, and you just use the a resistor divider here, and Bob's your uncle, you can set whatever output voltage you want well within reason.

**Dave Jones:** So, this is actually a good time to learn a PPM here cuz if you go into like it depends on the data sheet and they can vary like it specifies okay for the 2.5 V part here for example, it tells

**Dave Jones:** you yep it's it's typically 2.5 V and the tolerance is it tells you that in millivolts. So, if you wanted that in percentage you have to take that. So, if you get your calculator out what is it 12 mV divided by 2500 equals that times

**Dave Jones:** 100 equals 0.48%. So, that's you know basically 0.5% accurate part for that one at 100 microamps. So, it varies and you might have to look at some characteristic curves if you you know really getting into the nitty-gritty detail of it. But as I said, jellybean

**Dave Jones:** parts typically if you're worrying about the real nitty-gritty detail you're probably not using a jellybean part. You're probably specifying in a slightly better part. But as I said, yeah learn your PPMs because parts which is parts per million because it'll give you

**Dave Jones:** typically a coefficient in parts per million or it might give you accuracy in part per million. It depends on the manufacturer. Other good thing about them is no output capacitor required. You don't have to bypass them and it

**Dave Jones:** tolerates a capacitive load as well. As I said, if you're using these as a voltage regulator to power your circuits you might typically have like some still have some bypass caps on your chip. This is going to tolerate

**Dave Jones:** any bypassing on your supply rail. And we won't go into noise and things but these aren't like the lowest noise reference parts. They're just jellybean parts. They're you know in the same order as like a voltage regulator for

**Dave Jones:** example. But they're the specs are quite adequate. So, if you just need a basic voltage reference from analog to digital converter or maybe uh your microcontroller using the internal converter it might have an internal reference, you might need something a

**Dave Jones:** bit better than that. Well, all the baseline one you're going to go looking at is the 4040 and 4041. And as I said, they are available in different grades at different price points. So, you might want to choose one of these at a higher

**Dave Jones:** grade, pay a little bit more cost, but you might get more initial accuracy. You might get slightly better temp tempco, and all this can vary uh between the manufacturers, and there's lots of manufacturers that will make you a 4040

**Dave Jones:** or and 4041 equivalent part. And there's lots of uh cool application examples for the 4040. You don't just have to use them as a voltage reference, but because they're a uh precision part, you can do like precision clamps and things like

**Dave Jones:** that. Uh this one over here, it's got like a floating a current source, you can do that, or you can use these as a uh precision uh regular like a high-power precision regulator in combination with a series pass transistor. And determining the

**Dave Jones:** resistor value here, it's not trivial. to take into account, just like with a uh Zener, I've done videos on uh at least one video on uh Zener volt uh references. So, you've got to take into account the current IZ here, and also

**Dave Jones:** the load current you're trying to uh drive. Usually, you'd be driving like a high-impedance ADC input or something like that. So, the load current here is kind of negligible. Uh but as I said, if you're using it for a precision voltage

**Dave Jones:** uh regulator, for example, then, you know, powering your circuit up to like 10 15 milliamps or so, then yeah, you really got to take that into account and choose the right RS here, and there's the formula for it. And just be careful

**Dave Jones:** if you are actually using this as a regulator to power a circuit. If you've got like large uh changes in your circuit current, you know, you might turn on LEDs or something, and they go up to to like 10 milliamps or something

**Dave Jones:** like that, and then it drops and your circuit drops down to like 100 microamps, then that can upset the apple cart with RS here, and you might have to do something better like a series uh pass transistor or something like that.

**Dave Jones:** And these come in through-hole and surface mount, usually a TO-92 old school standard SOT-23 or a smaller SC-70 if you're really cramped for space. Okay, I saved the most interesting component to last. It's yet another precision programmable reference. It's a

**Dave Jones:** TL431 here, and you might think, "Well, how is this different to the like 4040 adjustable uh regulator here?" It looks exactly the same. It's got a Vref pin, but uh-uh, the TL431 is used everywhere. It's uh once again, it's practically

**Dave Jones:** definition of jelly bean part, not just as a voltage reference, but in many different circuit applications. It's used in practically every isolated main switch mode power supply on the market uh for example, because it's just simple and flexible and versatile and you can

**Dave Jones:** use it for a lot more applications than you can the uh 4041 adjustable programmable reference. So, let me show you what's going on here. This is the 4041 adjustable reference like this, and uh you'll notice that it it's got the pass transistor with the op

**Dave Jones:** amp, and this is the uh TL431 here. It's It looks exactly the same on the surface. It's got the pass transistor here, it's got the op amp here, and it's got the internal uh reference, in this case 2.5 V or bust,

**Dave Jones:** you don't get a say in it. Um but, there's something a bit different in the topology of what's happening here. You'll notice that the reference input here is basically going directly to the non-inverting input of this op amp here,

**Dave Jones:** and there's no internal feedback at all. It's operating in completely open loop mode. But, you'll notice that the 4041 here, the non-inverting input, we've got a current source here with a transistor, and we've got another current source up

**Dave Jones:** here. So, it's not completely open loop like you've got on the TL431 here. They're actually slight subtly different topologies which makes a big difference in the applications for this circuit. So, this op-amp here is effectively a comparator and the output here is either

**Dave Jones:** going to be a one or a zero effectively one or a zero. It basically means this series pass transistor here is going to switch on or off. Fully on, fully off. That's basically it. Depending on whether or not the external reference

**Dave Jones:** input voltage is above or below the internal reference 2.5 V voltage reference. So, it's you're going to get a switching waveform like this. Then you've got the internal schematic over here which is significantly different to if you compare it to the 4041. I'll

**Dave Jones:** leave that up to you playing along at home. And you'll notice that it's also got a reverse biased diode here. Very handy for certain applications. You don't get that on the 4041. But, you can actually close the loop by tying the ref

**Dave Jones:** pin up to the cathode up here just like they showed at the start of the data sheet and you put a series resistor and it's going to act just like a shunt reference. You're going to get your 2.5

**Dave Jones:** V out of here. The reference voltage. How does this work? Well, if you remember your op-amp theory, we've got our 2.5 V voltage reference. Our anode's going down to ground here. Okay? This op-amp is going to do whatever it needs

**Dave Jones:** to do with this pass transistor to make the two inputs the same voltage. So, I've got our ref pin tied to our cathode here. Then this op-amp is going to do whatever it needs to do to drive this

**Dave Jones:** transistor to make sure the non-inverting and the inverting inputs are the same. I.e. 2.5 V. So, you're going to end up with you've got your resistor like here like this. You're going to end up with your 2.5 V out there. So, it

**Dave Jones:** works as a basic shunt regulator in that uh closed-loop mode. But, the beauty of the 431 is that you don't have to use it in that mode. In fact, if you're just using it as a shunt reference, I don't

**Dave Jones:** know, should you use a 431 over the 40? I don't know. It depends. Is it cheaper? Nah, whatever. Anyway, and the whole idea is that the reference input here is uncommitted, so then you can actually use it as a comparator, and that's what

**Dave Jones:** it's useful for like uh power supply feedback and things like that. Now, it's not as precision as the uh 4040 4041 because, you know, look a B-grade uh part here. Standard part is 2%. It goes down to 0.5%. You might be able to get a

**Dave Jones:** bit lower from that from some manufacturers, but it's not like designed as like a really precision voltage reference. It's like a good enough precision uh programmable reference, but it's not as good as you can get in the grades in the 4041 uh for

**Dave Jones:** example. But, its current sync capability you can go up to 100 milliamps, so it's order of magnitude better than what you can get with the 4041. As far as temperature coefficient goes, it's pretty decent, but they don't really often tell you it in PPM to

**Dave Jones:** compare it to like the 4041. But, uh this um on semi data sheet does. It's 50 PPM at typical. And if you actually search for PPM, it should give you like the formula used for that. Let's have a

**Dave Jones:** look. There you go. Digest that to your heart's content. But, basically what pops out at the end is roughly 50 PPM per degree C. So, that's too shabby. It's better than your standard uh 4041, not as good as your highly spec uh

**Dave Jones:** 4041s, but not bad at all. And the reason you have to do these calculations here is because it really only tells you uh the temperature deviation over the full range. Basically, the change in total millivolts over the full

**Dave Jones:** temperature range. So, you got to take the temperature range and then work it out. Uh it's annoying, but yeah, roughly 50 ppm, not too shabby. So, it's available in the popular packages TO-92, very common. If you see a TO-92 in the

**Dave Jones:** uh secondary side of a main switch mode power supply, then it's most likely a TL431. It's available in SO-8, old school DIP, and a microwave rubbish. So, you can use it as a basic shunt regulator reference like adjustable uh

**Dave Jones:** like this if you want, or as I said, a fixed uh 2.5 V. Um but, it's it Where it comes into its own is all the different applications you can use it for due to its slightly different topology uh

**Dave Jones:** compared to the 4041. So, here's a precision high series uh current uh regulator, for example. Once again, they've got a Darlington uh configuration here for uh like series pass uh transistor there. It's got a You can use it with a 7805. You can do this

**Dave Jones:** with like the 4040 as well for some of these uh things. But, you know, a high current uh shunt regulator, another series pass transistor there. You can get a crowbar circuit, which is common on like um high-quality power supplies.

**Dave Jones:** They'll actually short uh the output of the power supply and and pop the fuse or whatever protection uh system you got in there um instead of destroying your equipment if something goes if your voltage on your uh power supply goes Say

**Dave Jones:** you got 5 V. If it goes above 5.25, which is the, you know, nominal uh TTL output, the crowbar can switch on, and that can protect your $10 million board that you've got connected up to this wimpy little power supply. So, you can

**Dave Jones:** use it with the 317 here. You're going to once again a single a simple series uh pass transistor. Um this one's simple. You can actually a precision 5-V regulator. You know how I told you the internal reference is 2.5 V. They're

**Dave Jones:** exactly the same because the output will be double the voltage reference here. So, if the internal reference is 2.5 V, you'll get your 5 V out here. And because this is an emitter uh follower uh transistor here, The output voltage,

**Dave Jones:** yeah, it'll be twice that. So, nice little shunt precision 5-V power supply. They got a PWM converter with reference here. What else have they got? Look, they got a voltage monitor here. So, you know, the LED turns on when the voltage

**Dave Jones:** limit is there. There are voltage monitoring ICs out there, but hey, you can use the TL431. Cuz I don't Could you class any voltage monitor as a jelly bean part? I don't know. Well, some of the TI parts

**Dave Jones:** may be, but they're not really falling into the jelly bean category. We've got a delay timer here. We've got a precision current limiter here. Got a precision constant current sink. But where this puppy actually shines is on semi have an

**Dave Jones:** entire like little application note here on its use in control of switching power supplies as the feedback reference part in here. And they go into the details. I can link this in, but basically, how is regulation performed? Textbooks only

**Dave Jones:** describe op-amps in compensators. The market reality is different. TL431 rules. And And sure enough, there it is. TL431 is the most popular choice in nowadays designs. So, yes, basically does optocoupler control. Of course, you need isolated feedback. You've got your switching

**Dave Jones:** transformer and for your mains power supply and then your optocoupler feedback. And it's tied into the optocoupler feedback here. And it's absolutely perfect for that. And you can control based on these resistor values here whatever output voltage you want.

**Dave Jones:** And they go into all the math behind that, but check it out for yourself. Bias currents can be a big problem. And there's small signal analysis for all you small signal analysis fanboys. And it can get rather complicated. But

**Dave Jones:** because this part is the jelly bean part in almost every mains switch mode power supply out there, yeah, all this stuff matters. Jeez, now we're getting serious. Look at this. Woah. Anyway, that's crazy. I'll have to link that one down below. Speaking of which,

**Dave Jones:** TI also have a design in with the advanced TL431. Um here it is. Here's once again the the isolated feedback from the switch secondary side of the switching power supply and how it does it drives the optocoupler feedback there. Now, here's

**Dave Jones:** one of the traps for young players. Um you know how I said the TL 40 40 40 41 is stable with capacitive load? Well, unfortunately, the TL431 is not. So, you've got a stable region and you've got an unstable region, just like with

**Dave Jones:** low dropout regulators and stuff like that. You can't just whack a capacitor on the output and it's yeah, not going to be stable. There's going to be an unstable region there and you can completely come a gutser. I won't go

**Dave Jones:** into the details, but I will also link in this data sheet down below for application note down below. Suffice it to say that yeah, if you don't get the capacitance right, uh you can really come a gutser and it can go unstable and

**Dave Jones:** ruin your day. But there it is, there's the isolated, there's your isolation transformer and your optocoupler feedback for your mains input power supply. Cool. It's a very versatile part. There's tons more applications you can use it for. Bonus part, because the fanboys

**Dave Jones:** won't let me off the hook if I do a top five list without the REF01, which is basically the jelly bean really ultra precision reference. So, how good is it? Well, it's you know, it's typical accuracy here is not that great, but the whole

**Dave Jones:** idea is that you can you know, trim it to exactly what what you want. The good part about it is, look at this, 8.5 ppm per degree C maximum schmick as. So, you'd use this in like precision converters, precision references, and

**Dave Jones:** stuff like that. If you need something better than the 4040, there are better parts out there than the REF01, but it's it is the jelly bean part. And there's one cool thing about it, too, is not only does it have a trim input here, so

**Dave Jones:** you can but it also has a temperature output as well, a compen a temperature compensation output. So, you can use it as a temperature reference, not only for your own system, like a temperature sensor for your own system, but then you

**Dave Jones:** can also use it to compensate for uh the reference as well. You could potentially feed it back and So, there you go. The output voltage of the temp pin is taken directly from the band gap core, and as a result varies

**Dave Jones:** linearly with temperature. So, there you go. You could buffer that 1.9 mV per degree C, and you could potentially compensate for that like 8 ppm drift of this thing if you really wanted to. Neat. And because it's on the die,

**Dave Jones:** directly on the uh reference itself, you don't have any thermal effects inside your case. You don't have to like strap a temperature reference to the can of your uh voltage reference and stuff like that. It's built in. It's a pretty

**Dave Jones:** schmick part. So, there you go. That's my top five or so jelly bean voltage regulators and voltage references. I'll link them in down below, and I hope you enjoyed that. If you did, please give it a big thumbs up. As always, leave

**Dave Jones:** comments down below. You can't dislike videos anymore, apparently, cuz YouTube has disabled the thumbs down. Bastards. Done a video on that. I'll link that in, too, if you want to see it. Unbelievable. Having said that, check out my Odyssey channel, over 64,000

**Dave Jones:** subscribers over there, doing a gangbusters. And you can leave a splat or a dislike if you don't like my video, unlike bloody YouTube. Anyway, if you want me to do another top five video on another like set of components, let me

**Dave Jones:** know in the comments down below. Hope you enjoyed it. Catch you next time.
