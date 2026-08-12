---
video_id: uT4hKd66UY4
title: EEVblog #141 - AA Alkaline Battery Capacity Measurement
url: https://www.youtube.com/watch?v=uT4hKd66UY4
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 31, "3": 43, "4": 67, "5": 78, "6": 93, "7": 108, "8": 122, "9": 137, "10": 152, "11": 178, "12": 189, "13": 201, "14": 212, "15": 230, "16": 243, "17": 258, "18": 274, "19": 301, "20": 328, "21": 347, "22": 359, "23": 376, "24": 387, "25": 400, "26": 415, "27": 425, "28": 447, "29": 467, "30": 478, "31": 490, "32": 507, "33": 518, "34": 538, "35": 552, "36": 565, "37": 579, "38": 597, "39": 607, "40": 617, "41": 630, "42": 643, "43": 664, "44": 676, "45": 691, "46": 703, "47": 720, "48": 732, "49": 745, "50": 758, "51": 774, "52": 787, "53": 801, "54": 829, "55": 840, "56": 851, "57": 864, "58": 883, "59": 901, "60": 915, "61": 928, "62": 941, "63": 951, "64": 963, "65": 981, "66": 993, "67": 1002, "68": 1016, "69": 1028, "70": 1039, "71": 1052, "72": 1068, "73": 1083, "74": 1096, "75": 1106, "76": 1117, "77": 1129, "78": 1138, "79": 1156, "80": 1171}
---

**Dave Jones:** Hi, welcome to the EEV blog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi. The previous blog was a tutorial on battery capacity.

**Dave Jones:** Now, I thought I'd follow that up just quickly with a very uh quick little practical demonstration of how to measure battery capacity. Now, as I mentioned previously, there's two different ways to measure or specify battery capacity.

**Dave Jones:** Well, the first one is W hours and the second one is amp hours. Amp hours is a more simplistic figure uh as I explained in the previous blog. I won't go through it again, but the true capacity is measured in W hours.

**Dave Jones:** Now, let's have a look at this. If we've got our uh the voltage of our battery on the y- axis on this left hand y axis here and the current on the right hand y axis and time discharge time on the x-axis then as we've as we saw last time the voltage of the cell is not constant it will drop or the voltage of the voltage pack

**Dave Jones:** depending on what you're actually measuring doesn't have to be just one cell could actually be multiple cells in series parallel a combination of both uh etc it will have a characteristic curve which may look something like that.

**Dave Jones:** Now, if you're measuring a simple amp hour capacity down here like this uh and you're using you'd typically use just a constant current uh discharge. So, the current curve won't change over time.

**Dave Jones:** It'll just be completely flat like that at one continuous figure. But if you're trying to measure W hours like this down here, then you have to monitor both the voltage and the current and uh you would do the WHour one typically using a constant power source like that.

**Dave Jones:** And well well you don't have to but that's what you might typically uh do because a constant power might be uh to characterize say an ideal DC toDC converter or something like that.

**Dave Jones:** So in that case your uh you won't have constant current. Your current will change with the drop in of the cell voltage. So as the cell voltage drops like this the current will increase like that.

**Dave Jones:** As you'll see to measure W hours is a bit more complicated and requires a bit more gear than a simple amp measurement. For just to measure amp all you need is a constant current like this constant current load which I used in the previous vlog.

**Dave Jones:** very simple to build build quite trivial and all you need is a stopwatch to time it and a multimeter hooked across the battery to determine the cutout voltage which we'll call VC cut but W hours to measure that uh you need to log over time you actually need a data logger um either a PC or a multimeter that can data log and you've got to measure both the voltage and the

**Dave Jones:** current until the desired voltage cutout point. So, here's what you need to measure W hours or amp hours. For watt hours here, as you can see, it's quite complex.

**Dave Jones:** You got your battery or your pack which you're actually measuring. You need a current shunt resistor like this to be able to measure the current. You can put it in the low side or the high side depending on which amp you got, but you know, it typically might go on the low side.

**Dave Jones:** You've got your constant power load. Once again, that's got to be fairly intelligent. To get a constant power load isn't as simple as a constant current load. So take that into account.

**Dave Jones:** And then you need two differential amplifiers which is very important as we'll see in the practical demonstration. And then you need some way to log it. Uh it can be I've done it as a as a PC into a data acquisition card or you can do it with two data logging multimeters or something like that.

**Dave Jones:** You need some way to accumulate all that data over time so that you can do your individual WHour calculations over time and then accumulate them all up to get yourself a total W hour figure.

**Dave Jones:** Now that's you know it's fairly complex to do. You got to have the gear to actually do uh W hours. But amp hour measurement it's simple. You've got your battery under test, a simple dumbass constant current load, which is a FET and a O op amp and not much else really, and a multimeter and a stopwatch.

**Dave Jones:** And that's it. Um, and you just measure the um uh you just set it up and just uh count the time with the stopwatch until it gets from the uh the voltage on the cell gets from fresh right down to your cutff voltage.

**Dave Jones:** Simple. So, anyone can do a power measurements. watt hours bit harder as I mentioned in the previous blog there's two ways to get your W hour uh capacity figure actually to actually log it one is to get the uh the voltage and current curves I've represented V * I up here so your power curve effectively and then do an integral of the area under that curve but you've got

**Dave Jones:** to do integrals and well you just don't have to because there's an easier way one is to simply take the um the uh regular measurements say like it might be at 1 second intervals like that and because the voltage isn't going to change a massive amount in one second usually um for most applications then it's a very good estimate and you can calculate the watt second figure for

**Dave Jones:** that particular chunk and then you do it I've expanded that because it might take hours to discharge but if you accumulate and just add up all these what uh second measurements you can get a total figure when you come to the end a total figure in what hours or you know what seconds or whatever you want or jewels doesn't matter.

**Dave Jones:** So that's how we're going to do it in today's practical experiment. So what actually is the true W hour capacity of a double A cell? Well, we can't get it from the data sheet.

**Dave Jones:** So let's measure it, shall we? Now, it just so happens I've got this brand spanking new metro hit energy multimeter here, which actually allows me to measure uh not only voltage and current at the same time, but it allows me to actually measure capacity in W hours as well.

**Dave Jones:** Fantastic. So, what we're going to do is discharge this cell at a known constant current using my constant current um load here, which you saw in a previous blog.

**Dave Jones:** and I'm going to discharge a cell a um standard aoublea energizer alkaline and see what we get. Now, as I mentioned before, there's two ways to actually measure the W hour capacity of a battery.

**Dave Jones:** One is to get the characteristic curve and then integrate it uh over time and do some math and actually integrate it. Or you can use log the voltage and the current directly on the cell over time and that will build up a W hour figure for you.

**Dave Jones:** And that's exactly what the metro hit energy meter does. So, let's give that a go. As you can see, it actually displays the cell voltage and it displays the cell current.

**Dave Jones:** There we go. 260 milliamps. It's actually 262.4 milliamps and it's drawing 291 watt. And then it actually when you go into the energy measurement mode, you can actually reset the time here and it actually times how much how long you've actually been discharging or in this case discharging a battery, how long we've been measuring.

**Dave Jones:** And then it you can see the accumulation there of the W hour or the millh figure. And by the time this battery gets flat, it'll actually get down to um a it should get down to a W hour figure, which we guesstimated is probably about 2 1/2 W hours for a standard Energizer AA cell.

**Dave Jones:** Now, the Metro HIT Energy uses what's called a three terminal measurement system. It's got a volts terminal, COM, and an amp just like a normal multimeter. But because it can sample both at the same time, this is my little Dave CAD drawing here.

**Dave Jones:** And you can see that we've actually inserted the current uh measurement part of it into the negative terminal of the battery. We've got our constant current load here which I'll set for 250 milliamps.

**Dave Jones:** And we've got the cell. Now the disadvantage what with this three terminal measurement is that this value here because this internal voltmeter here okay is actually measuring the differential voltage between the two input terminals like that.

**Dave Jones:** The ADC is there. Then any current flowing through this wire down into here from the cell over to here, that is actually going to cause a voltage drop and upset the measurement.

**Dave Jones:** So that's a disadvantage of this three terminal measurement. So what we want is a big chunky wire as short as possible right here. Now, as a practical measurement here, I've set this up and it's drawing about 260 milliamps as you can see, but the metric energy is only measuring 1.037 037 volts.

**Dave Jones:** Now, if we get the fluke here and actually measure the voltage directly across the battery like this, you'll find it's actually 1.20. So, what's going on? There's a discrepancy here.

**Dave Jones:** Now, if we actually move this voltage terminal from the end of the battery to the actual input jack, you'll see it's 1.056, which is basically the same as what it's showing here.

**Dave Jones:** So that little tiny bit of wire there going jumping from there over to there and the contact resistance of the spring terminal and all that sort of stuff is enough to cause that voltage drop at 250 milliamps.

**Dave Jones:** Now you notice if we turn the current right down 1.259 volts and we'll measure the battery voltage. There we go. One point. It's practically spot on because there's no current causing a drop in that little tiny lead there.

**Dave Jones:** So, we have to work on optimizing that. Now, normally you would actually do this with what's called a four terminal measurement, which I've mentioned in another blog for resistance measurements.

**Dave Jones:** But in this case, you would actually measure the differential voltage straight across the cell into an amplifier like that. And you take it off and then you'd measure the current into another amplifier.

**Dave Jones:** and you would actually log the voltage and current using a PC or data acquisition card or something like that. But in this case, we've only got the three terminal resistance measurement on the metro hit extract.

**Dave Jones:** Now, what I've actually done is I've squeezed the wire in there between the spring terminal and the battery just to avoid that actual spring terminal. Now, now let's see if that makes a difference.

**Dave Jones:** Take it up to 250 where we were before. and 1.25 volts. Now, let's measure directly across the cell. We can actually measure here and here. 1.253. There we go.

**Dave Jones:** Pretty close. So, it was the spring terminal actually causing the problem with our measurement there. Now, the actual cell I plan on measuring is actually a Juracell Pro cell.

**Dave Jones:** It's a standard alkaline, just a rebadger to stop pilering. Go figure. Um, it's exactly the same as a regular alkaline. It's March uh 2016 expiry, so it's it's not brand spanking new, but it is straight out of the uh box.

**Dave Jones:** It is original condition, so shouldn't have dropped too much capacity at all. Let's consider it brand new. And we're going to do 250 milliamps, which um corresponds to the characteristic curve here.

**Dave Jones:** And we should get about 9 hours uh use out of it down to 0.8 volt. So, it's um late night here. So, I'll head to bed now. I'll set this up and I'll leave it running overnight and we'll accumulate the charge on here and see what we get.

**Dave Jones:** And here we go. It's 1.52 volts at 250 milliamps. a smidg in over, but let's not worry about that. And let's start the uh energy measurement. Here we go.

**Dave Jones:** It's reset and it's counting down. Well, it's counting up. So, I'll come back in uh 8 or 9 hours and we'll see. It's accumulated millwatt hours already. Look at it go.

**Dave Jones:** Look at the resolution on this thing. All right, it's morning time and as you can see, 7 hours and 53 minutes later. Not quite 8 hours. We've got 2.06 W hours total.

**Dave Jones:** And as you can see, the current has dropped drastically to 37 milliamp. So, it looks like it's completely dead. If we switch back, yep, the battery is only 144.6 m volts at 36 milliamps.

**Dave Jones:** It's completely died. So, there it didn't even get close to meeting its uh spec here of Let's take a look at it. It was supposed to at uh uh 250 milliamps there.

**Dave Jones:** It was supposed to get at least 9 hours down to 0.8 volts. We didn't even get 8. So, it's dropped off completely before that. Unbelievable. So, let that be a lesson to you.

**Dave Jones:** You can't always trust batteries to meet their performance spec even when they're well within date, even when they're quality brands like this. So the answer is for a quality alkaline cell like this Duracell Pro cell with with four years left on its sh on its stamped shelf life fresh out of the box has got just over 2 W hours capacity at 250 milliamps continuous current discharge.

**Dave Jones:** So what did we get from that practical measurement? Well, as it turns out I didn't get here quick enough and it had already gone past the 0.8 8 volts cut off voltage that I wanted.

**Dave Jones:** So I'm going to round it down to say to roughly guess that it was at about round about the 7.5 hour mark that it got down to 0.8 volt.

**Dave Jones:** So that and we know the actual the meter because it's really cool. It can calculate W hours for us. We know the actual W hour figure of that battery even below.8 volts but it drops off sharply is around 2.06 W hours.

**Dave Jones:** And we can calculate the milliamp hour figure as well because that's trivial because we were using a constant current load of 250 milliamps. We uh know it's well or we guessed it's 7.5 hours and that gives us a capacity of 1875 milliamp hours.

**Dave Jones:** So what does that tell us? Well, it actually doesn't tell us very much at all. And this is the crux with battery capacity measurements. We know accurately what the figure is for a 250 milliamp hour constant current load.

**Dave Jones:** But is your load for your product going to be 250 milliamps constant current? Probably not. So really, you can't use this data, this milliamp figure or this W hour figure down here to calculate the capacity for your product.

**Dave Jones:** um you really have to measure the uh the capacity of the battery for exactly the type of load you're going to have on your circuit. So really we can't say much at all what will happen.

**Dave Jones:** Um well we can because we know that anything above 250 milliamps constant current due to the IR this capacity is going to drop. It's not going to go up.

**Dave Jones:** It's going to drop. But at lower capacities, say if at 100 milliamps constant current discharge, we could expect this figure to go up and the W and the corresponding W hour figure to go up as well.

**Dave Jones:** But how much it goes up by or how much it goes by down by, we don't know. We have to do further measurements. And here are two simple examples where constant current and constant power might be used.

**Dave Jones:** And which one you might have to use to measure your battery capacity. Now constant current uh you would might typically use that if your circuit here if this resistor represents your circuit and let's say your circuit is drawing roughly a constant average amount of power.

**Dave Jones:** It might be pulsing or something like that but let's not complicate it. Okay? It's drawing a constant amount of power cuz it has a constant voltage. It's being driven by a something you should know a 7805 voltage regulator.

**Dave Jones:** Right? It generates a constant voltage over a constant resistance which gives you a constant current load. Okay? And a constant power load. And that's going to give you a fixed current into here.

**Dave Jones:** Now, because of the nature of linear voltage regulators like the 7805 or the LM317 or something like that, this input current here is going to be the same as the output current.

**Dave Jones:** There's a little tiny little bit lost down here, but you know, let's not include that. Input current equals output current. So it's effectively constant current being drawn from your battery.

**Dave Jones:** So that's an example of where you might use constant current. Constant power on the other hand requires something like a DC toDC converter. It's exactly the same load. This is your product down here.

**Dave Jones:** It's once again a fixed voltage. Let's say it's 5 volts or something powering your circuit drawing once again a constant amount of current. It's drawing exactly the same amount of power as it was up here.

**Dave Jones:** But in this case, because of the nature of DC toDC converters, the input current will actually vary. It'll vary as the input voltage drops. So if when your battery voltage drops, as it follows the characteristic discharge curve, your input current is going to go up.

**Dave Jones:** So as you can see, you can't just measure the current because the current from the battery will not be constant. It will vary. So you have to actually log or measure both the battery voltage and the battery current to get power.

**Dave Jones:** And that's what you want to do because it's a constant power in the load. We're assuming an ideal DC toDC converter. I won't go into details about how the efficiency of converters, you know, drops at both ends of the current scale.

**Dave Jones:** But let's not go there. If it's an ideal DC toDC converter, which for the sake of many arguments, you can say it is an ideal converter, then you want to me be measuring constant power.

**Dave Jones:** So that's why when you're measuring the capacity of the battery, you want to simulate a constant power load. So as you can see, battery capacity measurement and specification is not easy.

**Dave Jones:** It all depends on a whole bunch of factors. And so if anyone tells you comes along and says, "Oh, this battery has a capacity of X." Tell them they're they don't know what they're talking about.

**Dave Jones:** Tell them to provide more information or say that's assuming a constant current or that's assuming a constant power or something like that. What does it happen under pulse loads?

**Dave Jones:** What does it happen under this? What happens when the battery voltage drops, etc., etc. Far too complicated. Anyway, that's a simple battery capacity measurement. And in case you're wondering, it's Australia Day here in Sydney, January 26, and it's pretty darn hot in the here in the AEV blog lab.

**Dave Jones:** Over 35° C Fahrenheit. No idea. You yanks, figure out what 35 Celsius is. It's getting quite warm and I'm sweating. Time to go back into the air conditioning. See you.

**Dave Jones:** [Music]
