---
video_id: 1hs_9vx9APw
title: EEVblog #772 - How To Calculate Wasted Battery Capacity
url: https://www.youtube.com/watch?v=1hs_9vx9APw
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 53, "4": 69, "5": 85, "6": 105, "7": 125, "8": 141, "9": 157, "10": 173, "11": 193, "12": 209, "13": 229, "14": 241, "15": 261, "16": 273, "17": 289, "18": 305, "19": 321, "20": 337, "21": 357, "22": 369, "23": 389, "24": 401, "25": 421, "26": 433, "27": 449, "28": 469, "29": 485, "30": 501, "31": 517, "32": 537, "33": 553, "34": 569, "35": 585, "36": 601, "37": 613, "38": 629, "39": 641, "40": 657, "41": 673, "42": 685, "43": 705, "44": 717, "45": 729, "46": 745, "47": 766, "48": 782, "49": 798, "50": 814, "51": 830, "52": 843, "53": 855, "54": 875, "55": 891, "56": 908, "57": 924, "58": 940, "59": 952, "60": 969, "61": 981, "62": 997, "63": 1017, "64": 1034, "65": 1046, "66": 1062, "67": 1078, "68": 1094, "69": 1110, "70": 1127, "71": 1143, "72": 1159, "73": 1171, "74": 1195, "75": 1211, "76": 1223, "77": 1243, "78": 1255, "79": 1275, "80": 1291, "81": 1315, "82": 1335, "83": 1351, "84": 1371, "85": 1391, "86": 1411, "87": 1431, "88": 1447, "89": 1467, "90": 1483, "91": 1503, "92": 1519, "93": 1535, "94": 1551, "95": 1563, "96": 1583, "97": 1599, "98": 1619, "99": 1639, "100": 1659, "101": 1679, "102": 1695, "103": 1711, "104": 1731, "105": 1747, "106": 1763, "107": 1783, "108": 1803, "109": 1819, "110": 1831, "111": 1851, "112": 1871, "113": 1895, "114": 1915, "115": 1931, "116": 1943, "117": 1963, "118": 1987, "119": 2007, "120": 2027, "121": 2043, "122": 2063, "123": 2083, "124": 2103, "125": 2115}
---

**Dave Jones:** Hi, in this video I'm going to show you how to calculate the remaining energy capacity in a battery like this. For example, your AAA, AA, CD size alkaline batteries you might design into your product. How do you know how much of the remaining

**Dave Jones:** capacity you're actually wasting in here, i.e. the area under the curve? Well, let's take a look at it, because, well, some people just can't seem to understand the concept. So let's say you're designing a product which runs on a couple of AA batteries, either a single one or a couple

**Dave Jones:** in series, or whatever it is. How do you actually know how much of the energy that you're wasting in the battery? And yes, unless you design your product to work down to 0.8 volts cut-off voltage, as I've explained in several videos before, then you're not utilizing the maximum capacity

**Dave Jones:** of your battery. Now, I've actually done several videos on battery capacity before, what it is, how you calculate it, and how to do measurements and all that sort of thing, so I won't go over too much of that detail again here. You can watch those in-depth here, so I'll link them in,

**Dave Jones:** click here if you haven't seen those. Now, I won't go over all that detail again, recap very quickly here only. The energy that you've got available in one of these batteries is measured in watt-hours. It's not measured necessarily in milliamp-hours, it's not measured in voltage, it's not measured in current,

**Dave Jones:** it's measured in watt-hours. It changes over time. And if you've got a discharge curve which looks like this, this is a typical constant current curve, then the energy that you have in your battery is all this under this discharge curve here. And your discharge curve drops off extremely quickly

**Dave Jones:** after 0.8 volts. It's an industry standard figure to use. Anything under 0.8 volts, it just basically drops off like a rock. That is pretty much the lowest cut-out voltage you could have. Now, if you've got a product which you design with, say, a 1 volt per cell cut-off voltage, which is fairly typical

**Dave Jones:** as I've shown in a previous video, then if you draw a line like that and down like that, okay, this is the amount of energy under the curve here that you are wasting in the battery. So this is how much is remaining in this battery if you have that particular

**Dave Jones:** cut-out voltage. And if you're designing a product that uses nickel-metal hydride rechargeable batteries, for example, as well as alkaline, then you basically must design your product to have a cut-off voltage of at most, at absolute most, 1.1 volts. Otherwise, it's not going to work.

**Dave Jones:** If you set it for 1.2, well you're going to be wasting most of your capacity in your battery. And this is why, as I showed in a previous video, I've done tests on products, and basically almost any decently designed product on the market that

**Dave Jones:** works with both rechargeable batteries and primary cells must have a drop-out voltage of 1.1. Typically it's between 1.1 and 1 volts here. So take this rechargeable battery here, if you set your cut-off voltage to 1.1 volts and you draw a line across there, where it intersects, bingo, that is how much capacity

**Dave Jones:** in your battery that you've wasted. As you can see, not a huge amount, but how much is actually wasted? That's what this video is about. And when you look at data sheets for batteries like this, one critical thing to remember is this cut-off voltage here, all these characteristic discharge

**Dave Jones:** curves, this is the battery voltage under load. Now it is absolutely and totally incorrect to measure the battery voltage when it's not under load, i.e. to take your battery back out of your product and then measure it with a multimeter. It is fundamentally the wrong measurement, because batteries will actually regain

**Dave Jones:** their voltage when you actually take them out of the product, i.e. you remove the load because of the internal resistance of the battery. That is why every single data sheet for every single battery on the planet specifies a cut-out voltage here which is under load.

**Dave Jones:** And I can actually demonstrate that here with this load. I've got a brand new battery, let's take it out of the packet. Here we go. Let's hook it in here. Haven't turned the load on yet. There we go, 1.58 volts, it's brand new.

**Dave Jones:** If we switch the thing on, I've got it set to a constant current of half an amp. So let's just draw that, and we'll instantly see the voltage drop right down. That's due to the internal ESR, the equivalent series resistance in the battery.

**Dave Jones:** So now it'll, you know, it's got a fair amount of energy in there so it can actually generate that voltage for quite some time. It'll slowly discharge. Curve, there we go, went down a little digit there. But when we switch the load off, the voltage will actually jump back up.

**Dave Jones:** So that is why you never measure the battery voltage unloaded like this when you're talking about or specifying capacity of the battery. It's just meaningless in that respect. It's an okay measurement to see whether or not that battery is still relatively fresh, but it is

**Dave Jones:** not the correct way to do it when you're talking about discharge curves and remaining capacity. It's just not. But some people just get this basic fundamental thing wrong about battery voltage. In the case that I've done a previous video on, click here if you haven't seen the Batterizer,

**Dave Jones:** which is an Indiegogo campaign for this DC to DC converter battery clip-on thing. They claim that it's 1.3 volts cutoff voltage, and it's absolutely not, because they measure, and they show this and demonstrate it in their videos, that you measure the voltage of the battery when it's not under load.

**Dave Jones:** Fundamentally incorrect. That's battery 101 stuff. This voltage must be measured under load. So this video is going to be about, well, let's say we designed our product with 1.1 volts cutoff voltage and it was drawing, for example, 100 milliamps constant current from the battery.

**Dave Jones:** And I'll explain that in a minute. There's the characteristic discharge curve, and we're using the Duracell copper top battery, we draw our line across there, we draw it down like that, and this is the amount of capacity that we're wasting in your battery.

**Dave Jones:** And, well, there might be a reason why you set it to 1.1 volts for various technical reasons in your product, and you just have to live with the fact that you're wasting that amount of capacity inside your battery. Now, as I said before, the total amount of energy in this battery

**Dave Jones:** is the area under that, this characteristic discharge curve here. So how much of a percentage is this area compared to all the rest of it? Well, you can kind of sort of eyeball it and go, oh, I don't know, it's maybe 20% or something like that.

**Dave Jones:** But what this video's going to be about is how to actually calculate this properly, using proper engineering, not just guesstimates. Now, if you look at the data sheets here, of course, you'll find that you typically might get characteristic discharge curves like this that are both constant current

**Dave Jones:** and if you flip it over here, you'll also get constant power ones as well. And you might also get constant resistance. Which one do you use for what products? I'm glad you asked. I just so happen to have a Davecat drawing here, which

**Dave Jones:** shows your basic two different ones, your constant power and your constant current. I've gone over this in the previous video, there's a lot more detail in there if you want to check it out. I'll recap briefly here. If you're powering your product, this is the battery power of the product, and you use a typical linear regulator

**Dave Jones:** like a 7805. Not very efficient, but hey, simple and, you know, quite common. This is a constant current. It's drawing a constant current from the battery. Why? Because there's basically no current flowing through the control pin of the linear regulator here, so the output current is going to be equal to the input current.

**Dave Jones:** So if you've got a con- let's assume it's a constant resistance load, constant voltage, then you're actually going to have a constant power in the load. But don't confuse that with constant power from the battery, as we'll see in a second. So what we're actually drawing there is constant current from the battery.

**Dave Jones:** So in this particular case, you would want to use the constant current discharge curve here, not the constant power one. But if you had a DC to DC converter inside your product, then you're going to actually get a constant power from the battery.

**Dave Jones:** How does that work? Well, as the battery voltage discharges, like it did up here, your- the DC to DC converter might be, say, you know, 80% efficient, 90%, whatever it is. You're actually going to get a bit of power wasted in your DC to DC

**Dave Jones:** converter. So you've got constant power in your load, but as this battery voltage drops, because you're going to have assuming a constant efficiency in your DC to DC converter, the input current, i.e. the current from your battery, is going to change as the battery voltage drops, even though

**Dave Jones:** you've got a constant voltage on the output here. So it's actually different to your linear regulator up here, which draws a constant current. You're going to have a constant power in this case, so you want to go over to your data sheet and you want to use your constant power discharge curve.

**Dave Jones:** That's for any product which uses a DC to DC converter. Now, of course, I won't go into the concept of how DC to DC converters aren't perfect. As the input voltage drops, they actually don't have a completely flat response, i.e. the efficiency is not constant over the

**Dave Jones:** entire input voltage range. But for the purposes of today's talk, we'll assume it is. And for product evaluations and things like that, it's not a bad approximation to make. It depends on the design of your DC to DC converter. And if you're wondering about the

**Dave Jones:** constant resistance graph here, that's just like, you know, a real old school one. There's not too many cases of product design these days where you actually have a constant resistance load. So these are your two major ones, constant current and constant power. That's why most data sheets,

**Dave Jones:** most good ones, will have both of those in there. But that being said, the constant resistance graph is actually kind of like, you know, a bit of an industry standard test. So that's why they include the characteristic curves in here, so that you can actually compare different battery types.

**Dave Jones:** But of course, the problem with most data sheets for these batteries is that you only get a limited set of characteristic discharge curves for constant power. 250 milliwatts, 500, up to 1 watt, for example. Constant current here, you, well, this is actually not a bad set.

**Dave Jones:** You get 5 milliamps, 10, 25, 50. You can go over here. You get, you know, up to an amp. But what if your product is in the middle here? Well, you can kind of sort of, you know, draw your own curve in there and sort of guesstimate.

**Dave Jones:** And that's not bad for, you know, back-of-the-envelope type battery capacity calculations, how long your product's going to last, how much, you know, energy you're wasting in your battery, and things like that. But hey, we want to do it the proper engineering way. I'll show you how.

**Dave Jones:** So rather than just draw your own curve in there, you actually want to measure it. And I won't actually show you the technique for measuring. I've done a previous video on that, which I'll link in below. But you basically want to get your own

**Dave Jones:** measured discharge curve like this. And of course, it is the best way to do that, and most accurate, of course, is to do it based on your real product. So what you would do is you would have your real product here, which includes your DC to DC converter.

**Dave Jones:** You'd stick your voltmeter on there like that, and you would actually log the discharge curve and you'd end up with a curve like this, be it a constant current or a constant power. Or, in the case of your real product, your actual real product, because your product might be switching, going into different modes,

**Dave Jones:** it's not going to need constant power, things like that. So ideally, best case you want to actually do it with your real product. But hey, if you can't do it with your real product, because you haven't built your prototype yet or whatever, or it's

**Dave Jones:** just not convenient for some reason, then you can actually use a constant current or a constant power dummy load. And I've done a previous video on this. Click here if you haven't seen it. It's a very popular video. A lot of people are making these themselves.

**Dave Jones:** It's your own constant current dummy load. You don't need much. You need an op-amp, a couple of resistors, and you need a MOSFET. And that's pretty much it. Build your own. No problems whatsoever. Very common thing to do in the industry, just roll your own dummy load.

**Dave Jones:** Or you could use a commercial dummy load like these. This one, for example, does constant current and constant resistance. This one does both constant current, constant resistance and constant power. And there's a lot of these types of dummy loads on the market. And actually one like this, you can actually hook up to the PC and do

**Dave Jones:** data logging as well, and you can actually get your battery discharge curve directly from it. Now let's jump on over to our spreadsheet here and analyze the data. Let's just assume that we've got the data into a spreadsheet. Whatever mechanism you use, as I said, you could use a data logger, for example,

**Dave Jones:** multimeter or some other data logger to measure the voltage, or you could do it old-fashioned way, pen and paper. Every minute, just write down a voltage reading. And so we've got the data into a spreadsheet, however way you want to do it. And you can see down here we've logged the voltage.

**Dave Jones:** It starts out at 1.65 volts, and that's a fresh cell of course. And then we're going to nominate a cut-off voltage of 0.8 volts here, and we've got a test current here of 0.1 amps. Now you don't actually have to measure the current if you know you've got a constant current load,

**Dave Jones:** but in this case, the current has been measured and we've got the exact value here. But you don't necessarily need that. All you need is the voltage value and the known discharge current. If you're just measuring the product itself, well, the product is the product that draws whatever power, whatever current

**Dave Jones:** that it actually does. All you care about is that voltage there. That's what you really want to log, and that's what we've got here on our graph. And just in case anyone's wondering, those little jaggies there are to do with data decimation that I've done

**Dave Jones:** here, because there was a lot more data than this. There was actually like 100,000 data points. And I might actually do a separate video on that, how to actually decimate data. It'll be very simple. Anyway, you can see that we've got the typical

**Dave Jones:** characteristic discharge curve here, and this is a real measured battery discharge curve under load. Remember that it must be under load. It's just pointless to specify a battery voltage that's not under load if you're talking about battery capacity, energy, or anything else. And that's where that Batterizer product is

**Dave Jones:** just so wrong. They use the open circuit voltage of the battery to talk about energy, remaining energy capacity. It's just ridiculous. Totally meaningless. And if you want to know how good a fit real measured battery characteristic curve is to the data sheet curve, well, there we go.

**Dave Jones:** There's one of the data sheet curves. I could muck around a little bit, but there you go. It's a pretty darn close match, but that's exactly what you expect, because the manufacturer measures it exactly the same way. I promised I'd show you a way to

**Dave Jones:** measure the true remaining battery capacity, or the wasted battery capacity in your battery. So let's do that now. We need to calculate the energy, so the watt-hour energy. Now we'll do this as the amount of energy used as the battery discharges first. Okay?

**Dave Jones:** Just for simplicity's sake. So we start out at zero. Obviously at the first time period we measure, we haven't actually used any energy in the battery. So we'll just say zero there, for example. Now here comes the tricky bit. We have to calculate the accumulated energy at each

**Dave Jones:** point as we go down here. Now I've put watt-hours here, but you don't actually for the purposes of what we're doing today, you don't actually have to care about the exact units. It's just accumulated energy. So it's not necessarily watt-hours. It could be watt-seconds or whatever, right?

**Dave Jones:** It doesn't actually matter. So you can just title that accumulated energy, for example. So what we need to do here is we have to do a formula, okay? We've got to go equals to the previous value, okay? So we're going to choose the previous

**Dave Jones:** cell. We started from zero, so in this case it's going to be cell D5. And then we've got to add on the current power that we're using. So to get that, we of course, power is voltage multiplied by current. So it's 1.6 volts.

**Dave Jones:** The cell in this case, C6. And then we've got to go multiply by now we could just put in 0.1 amps because it's a constant current, but we actually measured it. So let's actually use the real measured value here. And we go bingo, like that.

**Dave Jones:** And we've got a figure an accumulated energy figure here, okay? And if you wanted watt-hours and stuff, you'd put divide by 3600 to convert seconds to hours, and all that sort of jazz, right? But anyway, we've got our accumulated energy. Now we can just drag

**Dave Jones:** our formula down here, all the way down, and this is where your spreadsheet does all the magic for you. It gets your total accumulated energy. So we started out using zero amount of energy, zero watt-hours, and then at each point, at each sample point

**Dave Jones:** it just, we're using more and more and more and more energy from the battery until we get the final figure right down here at our 0.8 volt Cut out voltage. Beauty. Now we can go and graph this and do some useful stuff with it.

**Dave Jones:** Now of course plotting a graph is trivial in Excel or in this case I've been using LibreOffice slash OpenOffice and we do want to scale it, okay, to 0.8 volts at the bottom end here. And why we want to do this will be important as you'll see in a minute.

**Dave Jones:** So we don't want for our minimum, you know, we don't want like a graph like that because that's just going to be silly. So we want to make sure we set that minimum value down to 0.8 volts and the maximum value up there to our

**Dave Jones:** scale for the y-axis here, our actual min and max value. Now the next thing we want to do is we actually want to create another y-axis here on the right-hand side. We want to have two different axes because we're going to have battery capacity

**Dave Jones:** on this right-hand axis, and we're going to have, as we've already got, voltage on the left-hand axis here. And you can do these in spreadsheets if you haven't done it before. Very powerful technique, use multiple axes. So we can just go in here like this, and we can insert, delete

**Dave Jones:** axes like this, and we can have the primary axis, or we can have the secondary axis. So we can have an extra y-axis here, and we've created one. Bingo! The next thing we want to do is we actually want to scale this axis here from 0 to 100% capacity.

**Dave Jones:** So we want to get rid of the automatic one there, change it from 0 to 100% like that. We can just fix up the axes there, we don't want that, so we want 10 for our minor and major there. Bingo! So now we've got our remaining battery

**Dave Jones:** capacity from 100% down to fully used here. Okay, so what we want to do now is we want to go into this graph and we want to add a second line on here that's a reference to our new right hand y-axis here. So we can go in here

**Dave Jones:** and we can, whoops, helps if I go into the graph. Sorry, this is like how to use spreadsheet kind of stuff, and it's kind of like telling you how to suck eggs I guess, so excuse me if you already know about this stuff.

**Dave Jones:** But if you don't, then here we go, okay, we'll add a second data series, and then we'll actually choose all the data here, come on, there we go, and bingo, we now have a second graph. So now we want to make sure that this line here, this data set,

**Dave Jones:** is associated with the secondary axes, so we have to actually select the secondary y-axis there, and it already is because I've already been mucking around, but there it is, remaining energy capacity in percentage, but it doesn't quite look right, does it? Hmm, we can fix this.

**Dave Jones:** Now remember how I said before that all we care about is the 0 to 100% scaling of our figure, but look, we haven't got 0 to 100%, we're going from 0 to almost 12 there, and that's exactly what we're seeing on the graph.

**Dave Jones:** So that is of no use to us. We have to actually scale this data here from 0 to 100%. Now of course that's really easy to do, we can just go equals like this, the current cell which is D5 here, and then we can divide

**Dave Jones:** that by the very last cell down the bottom. But I'll show you an old spreadsheet trick which we have to do here, we have to go instead of cell D99 is the one we want to reference, but we want to do $D $99 like this.

**Dave Jones:** This gives us an absolute value of the cell down the bottom, so when we drag this formula down like this, it won't increment D99, it won't go D100, D101, etc. like it will with the D5 here, it'll go D5, D6. We want that absolute value

**Dave Jones:** cell to be exactly the same, it's like entering a constant in there. And we just multiply that by 100, and we've got our formula in there, no problems whatsoever, OK? And we've scaled our data from 0 to 100%, and then we can go back into our graph here

**Dave Jones:** and then we can go, we can reselect our values here to be this column instead of the other one, and now we'll get a nice graph of 0 to 100% scaled. Beautiful! Look at that! But unfortunately, this is not in a usable form, it's actually going in the opposite direction

**Dave Jones:** we don't want it increasing like this because it's remaining energy capacity, we actually want to start out at 100% on the left hand side here, and then decrease down like that, because that's what we want, remaining energy capacity. This graph would be OK if we had energy, if it was energy capacity used

**Dave Jones:** but you'll see why in a minute we want remaining energy capacity. So we need to fix that. Now you might be thinking that we could just go in here and flip this axis for example you can actually reverse direction of the scale like this, and you can go like

**Dave Jones:** that. And well, that's OK, and our data's perfect, that's exactly what we want here, but our axis doesn't make, the labeling on our axis doesn't make sense anymore. It starts out at 0, and what, 100% remaining right at the end? No, we want 0, so we have to go back into the data and actually

**Dave Jones:** fix this up. So what we need to do is actually a bit fancier formula than what we had before. We have to go $D$99, so reference that absolute the maximum value, and then we have to subtract the current value we've got, D5, and then

**Dave Jones:** we'll close brackets, and then we divide by that maximum value again $D$99, like that. And then we've got to multiply that by 100 to get our 0 to 100% scaling, and bingo, we're starting out with 100 here. So if we drag this down, our graph will

**Dave Jones:** instantly, there we go, we're going down to 0! Ta-da! And look, that's exactly what we got! Bingo! There's our money shot, there's our remaining energy capacity from 100% down to 0%. Beauty! Now we can do the fun stuff. Now you remember how I said before

**Dave Jones:** that if we didn't scale this graph over here properly, for example, if we had this going all the way down to 0 like this, and these two graphs don't line up at these points here, then well, we can't actually do anything useful with this graph.

**Dave Jones:** So it's an old graphing trick, data analysis trick, that you actually, when you align the data point at the start and the end like this, and you have the correct axes that you want, then you can actually directly draw stuff on this graph and

**Dave Jones:** intersect lines and do other stuff, and read off both axes. So you'll see this in a minute, why this is the case, but it's absolutely critical that you have the exact same start point up here and the exact same end point, and of course you have to

**Dave Jones:** have the same type of scale as well, they're both linear scales. And those with a keen eye might have noticed that this red data series here is not quite a straight line. There's a slight bow in it, a downwards bow in that. Yes, this is actually deliberate, this is the way

**Dave Jones:** the math works out when you get changing voltage, and maybe a little bit changing, but essentially a fixed current here, and accumulated energy over time. You're actually not going to end up with a linear straight line with that. Now, we could of course have just put in a straight

**Dave Jones:** line like that, and not worried about just the minor discrepancy here, but hey, this tutorial is designed to show the correct engineering method behind it, and there's no point going this far, and then just fudging it by doing a straight line. You've got real data,

**Dave Jones:** if you have real data, always use your real data, so we'll get a really accurate, there's no guesstimates, there's no estimates, nothing we're going to be 100% accurate with the real data. But yeah, you're actually not going to get a linear result there.

**Dave Jones:** Now I've exported that graph as an image file, and opened up in earthenview, so that we can actually draw on it and do some fun stuff. Now first up, if you don't believe me that that red line's not linear, then we can actually draw

**Dave Jones:** a line in there. Boom! There it is, it definitely deviates, that actually deviates a fair amount, and you can actually get quite significant error if you just assumed it was linear. Now sorry this video's taken so long, but we've finally gotten to what we actually wanted to do here, and use the

**Dave Jones:** graph to actually properly calculate the remaining energy capacity in a battery. And we can do this because we've lined up these axes. As I said, the start data point up here, and the end data point, so we can actually draw lines on here and intersect things, and work it out.

**Dave Jones:** Now let's say that we designed a product with a cutout voltage under load of course, as I've said, of 1 volt here, okay? So we can actually go along here and draw a straight line across here until it intersects our voltage graph okay?

**Dave Jones:** And then once at that point there, we actually drop a line down vertically until it intersects because it's the same time period, we want exactly the same time period, that's why we're dropping that line vertically, drop it down until it intersects our remaining capacity graph, and then we can

**Dave Jones:** draw, and then we can actually extend that horizontally out to our new right-hand y-axis here, to get and read off directly our remaining energy capacity. So if we design our product with a 1 volt cutoff, and we're using a Duracell copper-top AA, it could be multiple ones in series, at 100 milliamps

**Dave Jones:** constant current discharge, so 1 volt per cell then if our remaining energy capacity after the product shows low battery, look, it's not quite 5%, it's maybe 4%, you know, we could round it to 5, but yeah look, it's bugger all, so we've wasted hardly any

**Dave Jones:** of our energy there. So if we go back to what we originally did at the start of the video, and you remember, the wasted energy in our battery is the area under that curve at that point there. So all that area there, would you have guessed

**Dave Jones:** that that was like 4%, between 4 and 5% of that total? Or would you have picked 10%? So you don't know. Right? So until you actually go in here, draw the real graph, get the extra axes on here, and actually extrapolate that. It's only 4%.

**Dave Jones:** So, you know, you're wasting bugger all. So if you go design your batteriser product to extend your battery life, or you're building your DC to DC converter into your product to try and, you know, get down to 0.8 volts, you're only getting an extra 4% at that particular current.

**Dave Jones:** It's going to change, you know, based on the current drawing, things like that, but this is how you get the real data. So it's not worth trying to get that extra 5% out of the battery in most cases. You know, you don't want the extra bill of materials cost or whatever, you might have other

**Dave Jones:** technical issues going down to 0.8 volts instead of 1 volts, for example. And so on. So if we now go back to what Batteriser claim for example, that they have now admitted that it's 1.1 volts under load, is your typical product, they say

**Dave Jones:** like 1.3, not under load. Well, we can do that as well. But to show the fallacy of that, maybe in another video. But look, you extend 1.1 volts across here, like this, then you drop that down look, you're only wasting just barely over 10% of your capacity.

**Dave Jones:** So that entire Batteriser product that they claim, oh, it cuts out at 1.1 volts load voltage, your average product look, 10%! So much for, you know, the claim of 8 times and all that sort of stuff. It's just absolutely ridiculous. So if you go and use something like the Batteriser

**Dave Jones:** on your product that has a cutout voltage of 1.1 volts, and it happens to be drawing 100 milliamps constant current like this, and you're at 1.1 volts per cell, you're only going to get, at best just over 10% extra capacity, and that doesn't

**Dave Jones:** include the efficiency of the DC to DC converter. By the time you include that over the whole range, you might end up with a net result of 0 because even the best DC to DC converters are barely pushing 90% at a spot figure.

**Dave Jones:** So really, it could go into the negative region, it could be detrimental. And we can actually go backwards as well, and let's take their claim of like, some, now they're saying some they were saying all before, but now they're saying a significant number

**Dave Jones:** only waste 80% of your battery capacity So we can actually go here, and we can go backwards and draw that, and then we can intersect once we drop it down here same time period, intersect here, and bingo, we would have to have an under load, under load cutoff

**Dave Jones:** voltage of just over 1.4 volts to get their claim. Now, yeah, there might be the odd old ridiculously badly designed product out there that might have an under load cutout voltage of 1.4 volts, but, ah, jeez, it's bugger all. They themselves have admitted that the typical product cuts out at 1.1

**Dave Jones:** volts, and my own testing and data and experience in the industry, of course, verifies that. So they've completely changed tune, and 1.4 volts, it's just ridiculous like, it's just absolutely ridiculous So there's going to be very few products out there that are wasting

**Dave Jones:** 80% of the battery. It's just not going to happen. So you can do that with any data curve you like, at low currents, at high currents for example, it doesn't matter what it is, whether it's a resistive load whether it's a constant power load, whether it's a complex load

**Dave Jones:** which is most likely and most common electronic products that have DC to DC converters built in, and as the battery voltage drops your efficiency changes, all that sort of stuff. Once you have the real data, you can actually go in there and see how much energy you're wasting.

**Dave Jones:** Beauty. So this of course is going to change depending on your discharge load and things like that and it's also going to change fairly drastically for different battery chemistries as well. Lithium ion, for example, is a much flatter response going out here, so it's sort of, you know, easier

**Dave Jones:** to design cutoffs to maximize your energy use. But things like alkalines, they have this very poor characteristic or non-flat characteristic discharge curve, and you can actually waste a significant amount of capacity in your battery. But as you saw, any product designed to use rechargeable batteries is going to have at least 1.1 volts

**Dave Jones:** maximum or less, and it's bugger all. And when you look at, for example, all the different currents for example, look, even from 5 milliamps all the way up to an amp here, so it pretty much covers the entire range here. You know, if you have that cutout at 1.1

**Dave Jones:** volts, or a volt or something, which a lot of products are, even at 5 milliamps, look, bugger all, 1.1 volts, 1, look you're, you know, covering the whole range. You're right there. That whole battery riser concept is like look, it's the entire range of currents.

**Dave Jones:** Sure, constant current but constant power is not going to be much different. So you're really only going to be getting that, you know, that 10-20% extra available energy, wasted energy in your battery for, you know, 1 or 1.1 volts cutoff. That's absolute best case.

**Dave Jones:** I mean, there's just no getting around it. So this, you know, 8 times rubbish relies on the fact that the product is extremely poorly designed and has a cutoff here, up here, under load of like 1.4 volts to get your 80%. Crazy. So I know this was a rather

**Dave Jones:** lengthy video, so if you're still hanging in there, thank you for that. But I hope you actually learned something here, because I've actually never seen anyone actually show this technique of getting the remaining capacity using the extra y-axes on the graph here. So it's not something that you'd typically learn in your textbooks or something

**Dave Jones:** like that. It's, you know, one of these applied electronics engineering techniques that practicing engineers actually figure out and use in the field. And this is the most accurate way, it is 100% accurate way to actually determine how much remaining capacity you're actually going to waste in your battery.

**Dave Jones:** So I hope you found that really useful. If you did, please give it a big thumbs up, because that always helps a lot. And if you want to discuss it, jump on over to the EEVblog forum. It's the place where all the comment action happens, but it also

**Dave Jones:** happens on YouTube. I try and read all my comments, and the blog website as well. Catch you next time! www.eevblog.com
