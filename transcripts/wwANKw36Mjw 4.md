---
video_id: wwANKw36Mjw
title: EEVblog #742 - Why Electrolytic Capacitors Are Connected In Parallel
url: https://www.youtube.com/watch?v=wwANKw36Mjw
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 25, "3": 36, "4": 48, "5": 64, "6": 75, "7": 89, "8": 102, "9": 116, "10": 133, "11": 140, "12": 162, "13": 173, "14": 186, "15": 204, "16": 218, "17": 231, "18": 246, "19": 255, "20": 272, "21": 287, "22": 297, "23": 307, "24": 320, "25": 334, "26": 344, "27": 355, "28": 367, "29": 387, "30": 399, "31": 410, "32": 421, "33": 431, "34": 445, "35": 467, "36": 477, "37": 498, "38": 507, "39": 518, "40": 530, "41": 543, "42": 556, "43": 565, "44": 583, "45": 603, "46": 627, "47": 644, "48": 659, "49": 669, "50": 684, "51": 732, "52": 753, "53": 777, "54": 804, "55": 812, "56": 836, "57": 851, "58": 863, "59": 873, "60": 889, "61": 903, "62": 920, "63": 927, "64": 939, "65": 955, "66": 970, "67": 979, "68": 992, "69": 1004, "70": 1015, "71": 1030, "72": 1040, "73": 1056, "74": 1073, "75": 1084, "76": 1098, "77": 1117, "78": 1127, "79": 1138, "80": 1157, "81": 1165, "82": 1177, "83": 1203, "84": 1224, "85": 1239, "86": 1262, "87": 1274, "88": 1289, "89": 1304, "90": 1320, "91": 1328, "92": 1339, "93": 1351, "94": 1363, "95": 1378, "96": 1402, "97": 1413, "98": 1433, "99": 1446, "100": 1464, "101": 1476, "102": 1488, "103": 1503, "104": 1514, "105": 1529, "106": 1543, "107": 1564, "108": 1570, "109": 1582, "110": 1594, "111": 1605, "112": 1618, "113": 1637, "114": 1645, "115": 1656, "116": 1665, "117": 1683, "118": 1694, "119": 1702, "120": 1711, "121": 1725, "122": 1739, "123": 1751, "124": 1764, "125": 1782, "126": 1802, "127": 1812, "128": 1824, "129": 1840, "130": 1863, "131": 1886, "132": 1896, "133": 1910, "134": 1925, "135": 1936, "136": 1963, "137": 1984, "138": 1991, "139": 2007, "140": 2018, "141": 2030}
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. This one comes from a forum post from a user named Lorie. Thank you very much Lorie for asking this very interesting question. Why do you parallel electrolytic capacitors?

**Dave Jones:** You do a teardown of a product, you open up and you see multiple electrolytic capacitors in parallel. It's quite common to actually find this thing in power supplies and all sorts of applications.

**Dave Jones:** Why do we do it? There's actually quite a bit to it. Let's take a look. Now, I will just stick to what Lorie asked here specifically about electrolytic capacitors.

**Dave Jones:** I won't go into for example, you often see you'll have a 100 nanofarad in parallel with a 10 nanofarad in parallel in parallel with a 1 nanofarad across bypassing say a modern FPGA for example.

**Dave Jones:** That's a different thing entirely. And I have covered that before. So, we'll just take a look at electrolytic capacitors generally in power supplies like this and other sort of big higher power applications.

**Dave Jones:** Now, you might typically see these parallel electrolytic capacitors in say your standard linear power supply. We've got a AC transformer, full wave bridge rectifier, and then you might see more than one.

**Dave Jones:** Sometimes you'll only see one, other times you might see you know, two or three or you know, five or even 10 in some sort of extreme example. And also you'll see them in for example DC to DC converters like this.

**Dave Jones:** So, we've got DC in, we've got DC out, whether or not it's a boost or a buck, step up, step down, doesn't matter. But you'll typically see you know, generally a couple of electrolytic capacitors on the output.

**Dave Jones:** You could also see one, but it's fairly common to see two or three. Why? Why not just use one? Well, basically when you design a circuit or a product, you're going to have a whole bunch of specs you're going to meet.

**Dave Jones:** At least if you design it properly. I mean, you know, you can't just go, "Oh, I'll just bung in a 100 mic cap, you know, she'll be right, no worries." But, if you actually design it properly, you could have a whole bunch of specifications for your electrolytic capacitors here.

**Dave Jones:** Some of them can include, well, the main one of course is generally going to be your capacitance value. It could be 100 microfarads for example, could be 1,000, 10,000, whatever.

**Dave Jones:** You're going to have a maximum ESR value for example, 0.1 ohms. That's very common in DC to DC converters for example for stability. They need a either a mini- minimum, maximum, or sometimes like a window where the ESR, you have to get the correct ESR which is the equivalent series resistance inside the capacitor.

**Dave Jones:** Biggest remember, capacitors aren't ideal. You have to deal with the real world where your typical capacitor like this actually has an ESR in here. This is the equivalent series resistance in there.

**Dave Jones:** It's going to have a certain resistance value. It can depend on the frequency and all sorts of complicated things. Then you're actually going to have the capacitor itself, the ideal capacitance in there, and then you're going to have a little bit of lead inductance as well.

**Dave Jones:** Quite a complex little beast, your practical capacitor. There's no avoiding this stuff. So you typically read your data sheet for your DC to DC converter and it might say you need a certain amount of capacitance for that particular load, maybe a either a minimum, maximum, or a window of the ESR value.

**Dave Jones:** So you've got to meet that. The other main thing is size. You know, you don't have an infinite amount of room inside modern products. Sometimes you do, you got the luxury of you know, space isn't a problem.

**Dave Jones:** But with today's miniature modern electronics and everything else, be it surface mount or through hole here, everything we're talking about is going to be applicable to both surface mount and through hole electrolytic capacitors.

**Dave Jones:** But yeah, you might have to meet a a volume envelope. Typically, uh height is a major requirement for capacitors. And well, it can go into, you know, you may be forced to use several different ones because of different height restrictions.

**Dave Jones:** Then you got cost restrictions, for example, which will go into. That may be a reason why. And then you have operating life as well. There's quite a few specs in here.

**Dave Jones:** So, let's go through all the reasons. I think we'll find quite a few why you might want to parallel electrolytic capacitors instead of using just one. So, I've come up with a list of nine different reasons why you might want to parallel capacitors.

**Dave Jones:** And they're all going to intermix, as you'll see. There might be one specific reason or a combination of reasons that push you towards either using a single capacitor, nothing wrong with using a single capacitor if it meets all your requirements, or as the question asks, why do we parallel them?

**Dave Jones:** Let's find out. Now, some of them have been copied from the specs over here, and we'll talk about them in more detail, but there's at least double the number of reasons in here.

**Dave Jones:** Whoa. Let's take a quick look. Hopefully quick. Hmm. Now, the most obvious one, of course, is your capacitance value. Take, for example, your linear power supply here. You got a full wave wave bridge rectifier.

**Dave Jones:** So, we're getting a 100 Hz typical full wave bridge, as you should be familiar with, standard building block circuit. Well, we have to generally meet a ripple voltage requirement on here.

**Dave Jones:** So, if the black one there is the output of your bridge rectifier, your capacitor is going to smooth that, and depending upon your load, is going to be dependent upon how much ripple you actually get there.

**Dave Jones:** And it's basically dependent upon three things: your load current, your capacitance, and your frequency. Your frequency, of course, here in Australia, 50 Hz mains voltage. Your full wave bridge rectifier doubles it.

**Dave Jones:** Going to have a 100 hertz, for example. So, it's only dependent upon your load value and your capacitance and the ESR and stuff doesn't really come into Well, kind of does, but let's not go there.

**Dave Jones:** This is like a just a rough rule of thumb formula that you can use to calculate your ripple voltage. So, you might be using a 7805 voltage regulator, drops out at 7 volts, for example.

**Dave Jones:** So, you don't want your minimum ripple current there to be under certain value. So, you're going to have a certain amount You plug the numbers in and you figure out, "Okay, I need a 1,000 microfarads of capacitance, for example, to give me my required ripple current." Now, of course, you can just stick in one capacitor of a 1,000 microfarads and Bob's your uncle, right?

**Dave Jones:** You've done the job. Okay, in this basic example, that might work, but aha, there's a whole bunch of other stuff which could influence your decision to use more than one.

**Dave Jones:** Now, the first one, of course, might be physical size. You might only have 10 mm height available, but you need 1,000 microfarads at, say, you know, 15 volts or something like that.

**Dave Jones:** So, you look through the catalogs and data sheets and you find that Well, you know, it's really quite difficult to get a cap that meets that physical height requirement.

**Dave Jones:** So, you might have to go for a shorter cap. So, you might only be able to get, say, 330 microfarad 16 volt cap in the height you want and the diameter you want and everything else.

**Dave Jones:** So, hey, bingo, you have to use It might force you into using three 330 mic capacitors. Mic is short for microfarad. Capacitors in parallel instead of one 1,000 mic cap.

**Dave Jones:** Obvious. So, I've covered two things, capacitance and physical size. Well, what about cost? Well, you once again, you look through your Digi-Key catalog or whatever, who wherever you're sourcing your parts from, you might find that, hey, these three 330 microfarads at 16 volts might be cheaper than the equivalent 1 uh 000 microfarads at 16 volts for example.

**Dave Jones:** So, hey, you might go just on cost reasons alone if space wasn't an issue or whatever. That could be a driving factor. Who knows? And another big one, bomb reuse.

**Dave Jones:** Bomb is bill of materials. You might find elsewhere in your design you're already using a 330 microfarad capacitor for example. So, well, why specify another 1 000 microfarads in your bill of materials if you can get away with just reusing three of the ones you already use?

**Dave Jones:** And if they're surface mount for example, you can buy them all on one big ass reel like this, which is much more economical. These are what? 220 microfarad 16 volts.

**Dave Jones:** So, if you're already using these in your design, hey, you get a bulk price and you only get to take up one of the feeders in your pick and place machine.

**Dave Jones:** Beautiful. That can be reason enough to use multiple capacitors. Another one that might be important for specific products is product configuration. Let's for say for example you had an audio amplifier, okay?

**Dave Jones:** It needs a big DC voltage rail with lots of bypass caps because it's, you know, 100 watts per channel or something like that. Well, let's say you had two models that had one was 50 watts and the other was 100 watts.

**Dave Jones:** Well, you're the amount of filter capacitance you're going to need is going to change depending on the model. So, you might lay out your PCB to have the multiple footprints for the capacitors and you might only populate the number that you actually require.

**Dave Jones:** You might have one or two in a particular design and then you might have four for one that has twice the power or something like that. Now, here's a big one which has an impact on many different reasons here.

**Dave Jones:** This is the ESR, the equivalent series resistance. As I showed before, the model of a capacitor is the ESR in series with the capacitance itself in series with a bit of lead inductance, and there's some other little niggly stuff in there we won't worry about like leakage resistance and dissipation as well.

**Dave Jones:** But what we're concerned with is this ESR here. Now, if we take the case of a 100 microfarad capacitor that's got 0.1 ohms ESR, for example, that is equivalent you can build that same capacitor up by putting two capacitors in parallel of 50 microfarads each.

**Dave Jones:** Of course, that's not like a preferred value, so you choose like 47 mic near enough. Electrolytic capacitors are typically like plus minus 20% anyway. So, yeah, near enough. Anyway, these can have a 0.2 ohm ESR, which means that they can be smaller cuz the ESR is going to be pretty much determined by the physical size of the capacitor.

**Dave Jones:** So, the larger the capacitor for the same capacitance, typically the lower the ESR. So, you can get away with two smaller capacitors in parallel of a higher ESR figure, and that's equivalent because they act like parallel resistors.

**Dave Jones:** So, you just use your standard parallel resistor formula, you get 0.1 ohms at total. They're exactly equivalent. But apart from the size issue, where this really matters and we get in a couple of things down here, the ESR, of course, it's a resistor.

**Dave Jones:** When you pass current through it, in this case ripple current that we saw before, especially in high power sort of applications, you can get, you know, a lot of current like amps or something like that.

**Dave Jones:** You're going to get power dissipated in that equivalent series resistance inside the capacitor body itself. That little aluminum cased electrolytic capacitor is going to heat up internally due to the power dissipated in the ESR.

**Dave Jones:** In an ideal world, in an ideal capacitor, there would be no power dissipated, but doesn't work like that in the real world. You're always going to get some for you know typically a high power product like a television or something like that gets quite hot in there use a lot of power you need a lot of capacitance and they all get hot internally and it can shorten their life and

**Dave Jones:** typically all you need to do to fix a product might be just a replace the capacitors because the dielectric has dried up in there they've got a finite life take a look at this data sheet for example of a typical Rubicon capacity here and you'll see that they can have anywhere from say 4000 hours life up to say 10,000 hours the larger the voltage rating of the

**Dave Jones:** capacitor typically the longer the life the bigger the diameter the longer the life all that sort of stuff because they don't heat up as much internally the physically larger capacitors so this is going to make a huge difference to your product and you'll notice down in the table down in here you have different ripple current ratings for different size and values and voltages of capacitors and that ties into the life

**Dave Jones:** up here where it tells you that it's going to have X you know thousand hours life at 105 degree C rating is a typical high temperature capacitor for example they typically come in two temperature grades either 85 degrees Celsius or 105 you can get slightly higher than that but they're the two major ones and it's going to have a rated life based on a certain temperature and that's all determined by

**Dave Jones:** your uh, ripple current your ESR and everything else. And of course, a specific size of capacitor is going to have a specific ability to be able to dissipate that internal heat.

**Dave Jones:** And roughly, it might be equivalent to the outside surface area of the capacitor. For example, you know, just ignoring like internal, uh, construction and things like that. So, uh, for a typical cylindrical, uh, radial capacitor like this will have an an area determined by the outside of the capacitor, and then we'll have the area on the top as well.

**Dave Jones:** And you know, your typical formula is area of a circle is pi r squared, and then the outside layer of the aluminum, uh, casing is going to be, uh, pi times the diameter times the length of the capacitor, i.e., the height of the capacitor.

**Dave Jones:** And you can add those together, and you got a total surface area. And for those really keen, you could go into all the thermodynamics of it, and how to actually, uh, attempt to, uh, calculate and model, uh, temperature rise of the capacitor.

**Dave Jones:** And it has to do with, do you have any air flow over it? Is it radiated? Is it in a, uh, you know, a sealed enclosure? How can it radiate to the air inside?

**Dave Jones:** And then how does it radiate outside the casing? And, uh, thermal, um, calculations like this very ugly, very complex. But generally, the more capacitors you have, the greater the total surface area you're going to spread the ESR across.

**Dave Jones:** Remember, in this case, we had two separate capacitors of 0.2 ohms ESR each. They're going to share the current. They're going to share the, uh, power dissipation between them.

**Dave Jones:** So, you're going to end up with a typically a longer life than your, uh, single capacitor with equivalent electrical specs. So, your longer life here can be a major, major reason for having multiple capacitors in parallel.

**Dave Jones:** Might be the only reason to do it. And you might have done the calculations to figure it all out, or you might have gone, "Well, this product needs to be reliable.

**Dave Jones:** It's industrial. It's in a a hot environment, for example. So, the temperature rise inside the capacitor, of course, is going to be above ambient. So, if you design your product to work up to 50° C, then you got to design margin on top of that.

**Dave Jones:** If you use an 85° caps, you can calculate the ripple current and the temperature rise inside, or typically you might do empirical measurements, actually put a thermocouple and use a thermal camera, actually get some temperature measurements on the prototypes, for example.

**Dave Jones:** Is it good enough? Then you can calculate, are the capacitors going to be the Achilles' heel in the reliability of your product or not? And you might decide to spread it across five or even 10 capacitors, something like that, because in this case they just all parallel up.

**Dave Jones:** So, if we wanted to go to the extreme and say use 10 capacitors, we'd use 10 10 microfarad capacitors with 1 ohm ESR each could give us the equivalent capacitance here.

**Dave Jones:** And in that case, each of the 10 capacitors is only dissipating 1/10 of the power. So, depending on the, you know, the thermal performance of the thing, the temperature rise is going to be very, very small compared to a single capacitor.

**Dave Jones:** So, you you might have increased your lifetime by several orders of magnitude. Now, another big thing is redundancy. Okay? If you've got a single cap, then you've got a single point of fire.

**Dave Jones:** If that capacitor fails, you've just got, you know, you're not going to be able to fill the air power supply anymore. Your DC-to-DC converter is going to go crazy, whatever, and your product's going to muck up.

**Dave Jones:** But if you had, say, two in parallel like this, well, then one, if due to, say, manufacturing reasons, could have a defective cap or something like that, then, well, the other one might be able to take over if you design in sufficient engineering margin into there.

**Dave Jones:** So, you've added redundancy to your design just by adding an extra capacitor in parallel to take it out because capacitor failures heat up. It's sort of like a snowballing type effect.

**Dave Jones:** The more it heats up, the more the dielectric dries out as the dielectric material inside dies out, then the ESR goes up and the ESR goes up, it's going to dissipate more power and it's a snowballing thing and these capacitors can start to fail very quickly.

**Dave Jones:** But if you have multiple capacitors in there, you can add a bit of redundancy to your system just to ensure reliability. You can see how it's all starting to come together, all these many factors to determine reasons why you might or might not use multiple capacitors in parallel.

**Dave Jones:** But generally speaking, it's a pretty good idea to do too if you're designing a reliable product. Now last and maybe least or it depends on what sort of requirements you got, uh the peak current considerations.

**Dave Jones:** Now if you have one capacitor for example and one load, let's say we just have one capacitor. This is looking down onto our PCB. We're talking about physical PCB implementation here.

**Dave Jones:** So the red just imagine these two capacitors don't exist. You got one capacitor here, it's driving the load, then all of the current including peak currents has to flow through that particular trace and depends on your you know on really high power designs you can get a lot of loss in those PCB traces.

**Dave Jones:** But if you went for three capacitors in parallel for example, you wouldn't just wire them straight here. You might have a separate trace going to the load like that.

**Dave Jones:** So you share uh current through each particular trace so you can have smaller traces, less drop going to the to a specific start point over here at the load.

**Dave Jones:** So you're going to have a a current flowing through this trace, this one and this one which will be 1/3 the current you would have with only one capacitor and then you would get smaller of drops across their Ohm's law because we're going to have a certain PCB resistance depending on the thickness of your copper.

**Dave Jones:** Typical 1 oz copper, for example, you're going to have a voltage drop. As small as it might be, it can in big high-power systems, this can be a real consideration.

**Dave Jones:** So, now you've split your current up three times like this, you're going to have much smaller voltage drops, and your load's going to be much much happier because you've used multiple capacitors in parallel.

**Dave Jones:** So, you might have physically implemented them as three separate capacitors like that, but on your schematic, you're just going to show them as three like that. But, typically, if you're good designer, you'll have a note on your schematic like that saying explaining to the PCB layout person, which might be you because you might forget, explaining to lay it out in this sort of configuration because it's important.

**Dave Jones:** And a different configuration yet again, well, you might dedicate one of your capacitors, for example, to another load out here just so that you don't have to share the same copper here because if this load here is a pulse load, for example, and it's it's pulsing, then you know, physical layout of your PCB and your traces matter.

**Dave Jones:** You don't want that tied onto here because if this load here, you know, takes a big gulp of current, then you're going to get a voltage drop and a droop on your traces going to this load over here, which may not like it.

**Dave Jones:** So, you might actually show them, once again, electrically all in parallel like that, but physically going off to a different load. But, you know, if you were Once again, you'd put a note there, but if you're a good drawing You're good at drawing schematics and drawing them cleanly, then you'd put that capacitor over against the load on the specific part of the circuit.

**Dave Jones:** But, hey, you might see them drawn like that, and they physically might be right next to each other, but you might actually lay out the traces differently. And it's not just the internal ESR of the capacitor either that heats up the thing.

**Dave Jones:** You've also got connection losses as well. The leads on the capacitor, for example, they've got a certain amount of resistance, your solder joints, everything else. That can propagate They're going to heat up at large currents, for example, even though resistances of of the lead wires are very, very small, right?

**Dave Jones:** In large, high-power applications, it's going to matter. That's why some really, really big caps don't have just leads pins sticking out. They have gigantic lugs on them and big mounts that, you know, you bolt them down to the PCB and everything like that.

**Dave Jones:** So, you know, it's a really high current is a really big deal, and you might have to use proper crimp cables to go up to them in real, you know, if you open up really high-power amplifiers and things like that, they may not just have a couple of leaded radial capacitors stuck into the board.

**Dave Jones:** It can be a real big deal. So, it's those interconnects. Of course, they have a certain amount of resistance. I squared R losses, they're going to heat up as well.

**Dave Jones:** They can conduct the heat into the capacitor itself, and that all contributes to the internal heating of the capacitor. So, it's not just the ESR, but there's a whole bunch of other factors.

**Dave Jones:** So, when you split capacitors like this, you're also sharing the interconnect the the connection losses between the multiple capacitors, and that can make or break your design. So, there you go.

**Dave Jones:** I hope I've answered Lori's innocent question, why do they put multiple electrolytic capacitors in parallel? And I I came up with easily came up with nine different reasons to actually do that.

**Dave Jones:** As you saw, they can all intermix together, and you may only use one of these. Maybe, you know, a a deal breaker, right? I've got to use multiple capacitors because of cost or because of bomb reuse or might be some sort of, you know, weird ESR requirement.

**Dave Jones:** Could be some big physical load requirement. It could be longer life redundancy. That's a very popular one. In fact, that's probably one of the most popular reasons. As I said before, if you're going to design a product and you want it to be reliable, and you've got a capacitor in your power supply and the load is, you know, there's a reasonable amount of load and you might check how much ripple current

**Dave Jones:** you're getting and, you know, all that sort of stuff, especially on DC to DC converters, for example, where ripple peak ripple currents can be very high. Well, you know, one capacitor may not cut it.

**Dave Jones:** What if you get a faulty one out of the batch? Not so good. Then, hey, put some extra capacitors in parallel for redundancy. Now, it's actually quite hard to show a lot of this in practice on the bench, but I've got one little bench example where I'm going to show you how we can actually spread the temperature rise among capacitors by having multiple ones in parallel.

**Dave Jones:** Let's check it out. Okay, what I've got is a simple Vera board here with one capacitor and then 10 capacitors. And we'll see the difference between the heat rise in these things.

**Dave Jones:** Now, one is 100 microfarads 50 volts and the other is 10 10 microfarads at also 50 volts. And yes, they're exactly the same Rubicon brand. I'll link in the data sheets down below so they can have a look at it if you're keen.

**Dave Jones:** Now, I've got this powered from an AC transformer over here. It just allows me to select a voltage. We've got a diode bridge rectifier there, full wave bridge rectifier.

**Dave Jones:** I'm actually powering them both at once and you'll see why in a second. And so, I've got just another additional diode isolator there and just some probes on there so that we can probe the ripple voltage on this thing.

**Dave Jones:** And I've got the outputs here. So, we've got a standard full wave bridge rectifier and then I've got two constant current dummy loads, my do-it-yourself one, which is seen in a previous video, and the BK Precision one here.

**Dave Jones:** And this allows to set a constant current load so that we can get a nice big ripple value on both of these capacitors. So, both are 100 microfarads, except this one is made up with 10.

**Dave Jones:** And of course, the total surface area here is going to be a hell of a lot more than the surface area here. So, yeah, we should see a temperature difference, and we're going to have a look at that with our Flir E8 infrared camera.

**Dave Jones:** Let's go. Now, I don't currently have anything powered on. You can see that our temperature range is only small at 4°. So, this difference you might be able to see in there some difference in the temperature on the rear capacitors over here.

**Dave Jones:** And that Watch this. I haven't got it turned on, but look at that. I'm adding my hand in here. This is actually reflection of my hand down off the metallic tops, the the aluminum tops on those capacitors, and it's reflecting back.

**Dave Jones:** So, you got to be careful when you're doing thermal measurements like this to make sure you're not actually getting heat reflected, and you've got to set up the emissivity correctly.

**Dave Jones:** And yeah, and the bright aluminum tops on the capacitors isn't the best thing, but anyway, so we could like paint the top of the capacitors black or something like that if we wanted to.

**Dave Jones:** Anyway, so you just got to be careful to block out any reflected heat. I'll show you that. Look, I'll put you I'll put my hand here, and you can see the heat, and I'll put a book in between.

**Dave Jones:** Boom, gone. Now, please forgive me. This is going to be really tricky to get in one shot, but I wanted to power this up and like from cold and show you.

**Dave Jones:** So, you can see there's hardly any temperature uh differential in there at all. You can't see much. Now, if I apply uh power to the thing and then apply So, I'm going to feed in 15 V AC.

**Dave Jones:** Here we go. And I'm going to You can see that the bottom one You can see the diode heat up there. Now, I'll cover that in a minute cuz that's going to affect our uh temperature range, but you can see that I've got 200 uh milliamps on the single 100 microfarad capacitor.

**Dave Jones:** That's the one down the bottom here. This one down here. I've got to be careful not to touch anything. Otherwise, yeah, it's You can see it probably starting to warm up.

**Dave Jones:** Actually, I should do the other one. So, I'll set the other one to 200 milliamps as well. And bingo. Now, we're drawing 200 milliamps from the top one, and you can see that.

**Dave Jones:** You can see Look. You see the 100 microfarad capacitor starting to warm up. So, what I'll do is I'll cover this. I've got a Actually, that was probably bad.

**Dave Jones:** I was touching it for too long. Damn. Um Yeah, that posted note. Anyway, I'm trying to cover up those diodes so it doesn't affect the maximum range of our uh reading there, but you should be able to see after a while it's going to ramp up.

**Dave Jones:** Now, the important thing to note here is that our conditions are identical. Because what do you want when you uh have a simple uh full-wave bridge rectifier circuit like this?

**Dave Jones:** You want to All you care about is the ripple current, okay? And you can see I've got channel one's and and channel two in there, and they're the same ripple current.

**Dave Jones:** You can see that right in there. I mean, this is really extreme, okay? Because I want to be able to heat these caps up. This is not normal design uh you know, that we're doing here.

**Dave Jones:** You wouldn't have uh 20 uh 13.6 V peak-to-peak of ripple there. You just That's insane with the lower voltage there of 10 V. Remember, we're 5 V uh per division there.

**Dave Jones:** So, they're both identical. So, we've got 10 capacitors 1,000 microfarads as we saw in that basic rule of thumb formula before. The ripple voltage is just going to be dependent upon the frequency and the load current.

**Dave Jones:** The load current is the same for both of them. We've got basically the same 100 microfarad capacitance for both of them. So, we're getting the same ripple, but you can really see that bottom one heating up compared to the top ones.

**Dave Jones:** I'll get a closer shot on that. We've only been like powered up for less than 5 minutes. Okay, now I've replaced that Post-it note there with a big aluminum shield and here's my pointer coming in here.

**Dave Jones:** You can see the scale change dramatically there, but we're not talking about a big temperature difference here. I mean, it's showing that the maximum that cap's getting to is basically 27°, but it's a lot, but that is like, you know, a good like 5° more than the other caps, which are all sitting around ambient.

**Dave Jones:** You know, like sort of not far above ambient temperature, just a degree or two. So, you can see the temperature spread between these things. Let alone the like the core temperature inside cuz you're sticking in into the you know, the thermal properties of the capacitor and how it can get its heat out and things like that.

**Dave Jones:** It's like a semiconductor die. The like the die temperature inside is always going to be hotter than the case temperature, for example. And then the heatsink less than the heatsink temperature.

**Dave Jones:** You're going to have losses along the way, but you can see how that capacitor gets much, much hotter. And it's exactly the same ripple current, exactly the same design conditions.

**Dave Jones:** Oh, please excuse the the light popping in there, but you can see that the capacitors at the top only like less than 25°, so it's not too far above the ambient in here, but the 100 the single 100 micro capacitor The there is like 27°.

**Dave Jones:** It's a good few degrees warmer and if we leave it there for longer or we use higher currents and you know, this is just designed to show the difference, but I think that quite dramatically shows the difference how you can actually shorten the life of these capacitors cuz as I said, it's a snowball effect and hey, if you got a high ambient temperature, this is just like free air here in the lab.

**Dave Jones:** It'll be It'll be cooler again if I actually turned on the air con, these top capacitors might actually be more efficient cuz there's more surface area. So when you got air flow either just here in the lab with just the air con on this tiny little air flow can make a quite a significant difference to the temperature or if you designed in your product and your product's got proper

**Dave Jones:** thermal design with fans and everything else, then having all that huge surface area on those 10 caps can be a hell of a lot different to this single 100 microfarad cap here.

**Dave Jones:** Now, if you were sufficiently keen, you could attempt to calculate the temperature rise of the capacitor and you could probably do this using the Stefan-Boltzmann law. This is the thermal energy that is radiated per second per unit area.

**Dave Jones:** So there's the basic equation which you can slightly rearrange to get your thermal energy radiated from a hotter object to a cooler object. In this case, it'd be ambient or whatever environment you've got.

**Dave Jones:** So what we've got is the emissivity of the material here. So you'd have to go look that up and then of course the capacitors like wrapped in that plastic wrap and things like that.

**Dave Jones:** It gets very complicated, but anyway, the emissivity of your radiating material, i.e. the capacitor, multiplied by the Stefan-Boltzmann constant. That's some weird funny number you learn in physics and multiplied by the total surface area and this is the big thing that makes the difference here between the having 10 caps in parallel with a massive surface area compared to just one capacitor, for example.

**Dave Jones:** And then you multiply that by the fourth power of the temperature of the capacitor it's minus the fourth power of the ambient temperature. And of course you could rearrange that formula to get the fourth power under well, to get the temperature of the capacitor after Yeah, after you know letting it stabilize and all that sort of thing.

**Dave Jones:** But it's not going to be that easy. But hey, for all you nerds out there, go for it. See if you can do it. Bit of homework. So there you go.

**Dave Jones:** I hope you enjoyed that rather lengthy look at why do you parallel capacitors? And that seemingly simple subject like that turned into like a half hour epic. Sorry about that, but yeah, anyway, there is a lot to it.

**Dave Jones:** Even like basic things like this in electronics, you can go to town on these sorts of things and the reasons behind choosing certain things. So anyway, if you want to discuss it, jump on over to the EV blog forum.

**Dave Jones:** And as always, if you liked it, please give it a big thumbs up on YouTube. And you can leave comments all over the place. And yeah, stalk me on Twitter and all that sort of jazz.

**Dave Jones:** Catch you next time.
