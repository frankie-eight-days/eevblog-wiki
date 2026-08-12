---
video_id: YdbhnmA4M9g
title: EEVblog #1009 - DC Fundamentals Part 1: Voltage vs Power vs Energy
url: https://www.youtube.com/watch?v=YdbhnmA4M9g
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 28, "3": 43, "4": 60, "5": 75, "6": 92, "7": 106, "8": 125, "9": 138, "10": 152, "11": 166, "12": 181, "13": 196, "14": 213, "15": 231, "16": 247, "17": 262, "18": 278, "19": 295, "20": 307, "21": 325, "22": 342, "23": 363, "24": 384, "25": 404, "26": 415, "27": 431, "28": 450, "29": 467, "30": 480, "31": 494, "32": 511, "33": 526, "34": 538, "35": 552, "36": 569, "37": 585, "38": 598, "39": 612, "40": 628, "41": 644, "42": 660, "43": 676, "44": 691, "45": 707, "46": 724, "47": 739, "48": 757, "49": 770, "50": 788, "51": 805, "52": 817, "53": 833, "54": 849, "55": 862, "56": 879, "57": 894, "58": 911, "59": 923}
---

**Dave Jones:** Hi, today we're going to take a look at what I think is one of the most misunderstood and misused terms in all of engineering. We're going to look at the difference between voltage, power, and energy because people mix these up

**Dave Jones:** all the time. Heck, I'm even guilty of it occasionally saying energy when I actually mean power or vice versa. And if you're not careful and you don't know exactly what you're talking about, you can sound like an absolute twit. And

**Dave Jones:** this is actually really important not just in engineering but in broader when talking about technology cuz a good lot of the world these days runs on electrical energy. And we're always talking about solar and we're talking about energy production, energy

**Dave Jones:** consumption. It's pretty much what makes the modern world go around. So, it's important to understand the differences between these three words here. Let's get to it. So, you should be familiar with voltage. It's simply the electrical potential difference. The

**Dave Jones:** potential difference between two different points. And you can have different sources of voltage. You can have a battery, for example. You can have a solar cell or some other junction type device like a thermocouple or a Peltier effect device. Or you can have a

**Dave Jones:** generator where you've got a wire through a moving magnetic field, for example. All sources of voltage. Now, voltage isn't that easy. It can actually also be expressed and often is and probably more correctly so as the difference in electrical potential

**Dave Jones:** energy between two points. We've introduced the word energy. Does that mean voltage is the same as energy? No, it's not. That's the whole point of this video. So, let's dig a bit deeper. Now, if you talk to a physicist, they'll tell

**Dave Jones:** you that voltage is energy per unit charge and they're correct. Energy is in joules and charge is in coulombs. So, you might have seen voltage equals J on C. It's a basic engineering electrical engineering and physics formula, but

**Dave Jones:** that doesn't mean that voltage is energy because you can have voltage with practically no energy. How can you do that? Well, you might be familiar with static electricity. For example, you rub your feet on the carpet and you generate

**Dave Jones:** a big charge and that can generate tens of thousands of volts and you can discharge it, but you're not going to kill yourself or hurt yourself because there's practically no energy in that voltage. You can also say that the

**Dave Jones:** energy here is actually the potential energy, not the energy that we're going to talk about over here. Different thing. So, you can go into the physics of this until the cows come home and all the you know, physics experts will jump into

**Dave Jones:** the comments and no doubt, you know, try and explain things better, but you don't need to know that. Just suffice it to say that voltage is not energy and you can actually have voltage in the absence of energy, essentially. Hmm, makes

**Dave Jones:** sense? Let's move on to power. Now, the unit of power is watts as you most likely know and the power is equal to the voltage times the current. P equals V times I. Basic Ohm's law stuff. Now, what you should understand

**Dave Jones:** in this context of power is power is instantaneous. Power is the amount of power dissipated at that one instant in time. Or is it? Hmm, here's where we kind of dig a bit deeper like we did on voltage. So,

**Dave Jones:** having just said that power in watts is instantaneous, I now have to tell you that watts is actually defined as joules per second or the rate of energy produced per second or the rate of energy dissipated per second, for example. So, there is a time

**Dave Jones:** component to that, that per second, the joules per second component, but as you'll see, it's still not the same as energy. Power is very different from energy. So, we want to get at once and trust me, once we get through the detail

**Dave Jones:** here, I'll then explain the overall concept difference between power and energy. We're getting there. But, suffice it to say that in engineering, in electrical engineering, in a power terms, either circuit theory or uh a power generation or something like

**Dave Jones:** that, power is instantaneous, even though it is the rate of energy per second. So, you've got to have a current flowing to produce power. That's why if you've got no current flowing, then you have no power, even though you might

**Dave Jones:** have a high voltage. But, in terms of electrical energy, circuit theory, energy production, all that sort of thing, when you're talking about power, you're talking about the power that's dissipated in the circuit once current starts flowing, cuz P equals V * I. If

**Dave Jones:** current doesn't flow, if you have a circuit like this with a battery and a resistor, if your switch is open, no current flows, you've still got your voltage of voltage here is still being generated, that potential energy is

**Dave Jones:** still there, but no current's flowing, therefore no power is being dissipated in this load or no power's being consumed from the battery. So, although technically what's actually power has that seconds component in it, so it's only for electrical flow. In terms of

**Dave Jones:** uh actually talking about power, you can basically assume that it's instantaneous. That's the best way to look at it. It is the power dissipated or consumed or generated at that particular moment in time. Now, let's take a look at energy. Energy in the

**Dave Jones:** electrical engineering world is the usage of power, watts, over time. So, it's uh derived units kilowatt-hours, watt-hours, could be watt-seconds, whatever combination you want. So, the energy equals power times time. It goes back to how I said you can think of

**Dave Jones:** power as being instantaneous, whereas energy is power over time. That's the main difference, and it's a huge fundamental difference. Now, here's the big takeaway from this. You can generate power, but you can't generate energy. And vice versa, you can't store

**Dave Jones:** power, but you can store energy. So, it's incorrect to say that this battery stores power. You can't store power. It can generate power by creating a circuit and having the current flow, but it's it stores energy, not power. And that's a

**Dave Jones:** huge mistake a lot of people make. And you'll like often you'll just slip up, even though if you know the difference, you might say energy instead of power or vice versa sometimes. But, you know, if you're trying to be serious and explain

**Dave Jones:** things to people, you need to get the terminology right. Power is not energy, it's very different. Let's take the example of a familiar home solar power system. You might have, say, a 3-kW power system. It can generate 3 kW of

**Dave Jones:** power in ideal sun, for example. That's what it's rated at. That's its power rating in watts. 3 kW, 3,000 W. But, you can't then go and say, "Well, my house consumed 10,000 W of power today." That That's ridiculous. It's meaningless

**Dave Jones:** because you've introduced a the time element of a in this case a day, 24 hours. It's how much power that you take or use from your solar power system over a day or an hour cuz uh you're charged

**Dave Jones:** on your electricity bill, you're charged for energy. You're not charged for power. You're charged in kilowatt hours. You might pay 10 or 20 cents per kilowatt hour over time and that is the big difference. You're not paying for

**Dave Jones:** power, you're paying for how much power you consume per unit of time. So, you don't want to go and say, "Well, my home has a 3 kilowatt hour solar system." You sound like an idiot. Now, let's take the

**Dave Jones:** D cell alkaline battery again as a real good example and see the difference between voltage, power, and energy here. A D cell alkaline battery generates a nominal uh electrical potential difference of 1.5 V. That'll obviously drop when it

**Dave Jones:** uh discharges, but let's say 1.5 V. And what power can this generate? Well, what power can this deliver to a load? Well, that actually depends on the internal resistance the battery. You got to get into the electrochemistry and all that

**Dave Jones:** sort of jazz and you know, I not going to give you an answer, but suffice it to say there will be a maximum power point. Google that one where there will be depending upon the load resistance and the internal

**Dave Jones:** resistance of the battery that when the load is equal to the uh ESR, that will be the maximum amount of power that this thing can deliver. The instantaneous power. Now, the energy, the amount of energy stored in this battery. There is

**Dave Jones:** no power stored in this battery. You remember? You can't store power, but you can store energy. So, there's energy in here and it has a nominal rating of approximately 25 watt hours for a typical D cell alkaline battery like

**Dave Jones:** this. Now, you might see the more familiar, you know, milliamp hour figure of say 18,000 for an alkaline D cell. That's actually strictly incorrect because energy is watts per power per time, power in watts. So, if you're talking in terms of milliamps, you're

**Dave Jones:** not actually correct. And that's why I say take your mobile phone battery, for example, it might have the watt-hour figure printed on there. It might say it's 5 watt-hours and that is the correct energy capacity cuz it's taking

**Dave Jones:** into account the drop in voltage cuz the voltage is not constant and then suddenly dies, it tapers off. So, it's more correct, in fact, it's 100% correct to say to give a watt-hour energy storage figure in a battery. So, with a

**Dave Jones:** 25 watt-hour capacity battery, it could potentially deliver 25 watts for an hour or 1 watt for 25 hours. Simple. So, I hope you found it interesting and useful, the difference between voltage, power, and energy. The most common misconception, of

**Dave Jones:** course, is the difference between power and energy. One is instantaneous, one is a measurement over time. And just keep in mind these facts about our storage and non-storage and generation and non-generation. But, you know, some people will make the ridiculous claim

**Dave Jones:** that this has 1.5 volts of energy or 1.5 volts of power. It's like Duh, no. And that's what actually prompted this video. I actually uh saw a video of a student actually uh say, "Well, how much energy can a particular

**Dave Jones:** system that he was measuring actually produce?" And the answer was 0.2 volts. Like, no. Duh. So, what we'll do now is just quickly go to the bench and I'll show you an example of energy measurement. Now, let me give you a quick a practical

**Dave Jones:** example of the difference between power and energy. I've got my Gossen Metrahit Energy Multimeter here. It can measure power and energy. I've got a just a 5-V power supply hooked up to my dummy load here. So, So, got 5 volts into a

**Dave Jones:** constant current 1-A load. So, voltage * current, 5 V * 1 A is of course 5 W. That's our power. That's our instantaneous power at this moment in time. If I switch to say 4 V for example, then we'd get 4 W. So, there is

**Dave Jones:** no time component to this. We're just reading out that instantaneous 5-W value. Now, if I switch into energy mode by pushing the function button and I reset the timer, you will notice that we now have a timer in there counting from zero

**Dave Jones:** and you'll notice that the units have changed from watts to milliwatt hours or watt hours basically. So, you can see it accumulating over time based on how much time we're running. And this is exactly how the energy in your home is metered for

**Dave Jones:** example in kilowatt hours. So, we've got an accumulation of power over time that gives us energy. And of course, the rate of this accumulation is going to depend on the value of the power at that point in time. So, if we switch down to say back

**Dave Jones:** down to 3 V instead of 5, it's still building up but it's building up slower. If we go down to 2 V, it'll go slower again. And of course, if we switch back, our timer is still accumulating in the background but our

**Dave Jones:** instantaneous power in watts is 5 W. But our energy is slowly building up over time. There you go. Nice practical example. And we can also do the example of battery capacity using the BK Precision 8601 electronic load here which has a battery

**Dave Jones:** capacity discharge function. Now, if we select the type of load which is constant current, okay, if we set that to 1 A, then we can actually trigger our go into our battery mode here. Let's say our stop voltage, whatever. Okay, we set

**Dave Jones:** our time and then we start it. You can see that once we start accumulating over time, we've got 5 volts. It's drawing 1 amp from the battery. Say Say we've got a 5-V battery, and it's drawing 1 amp here.

**Dave Jones:** You can see that the units are amp hours. It's not watt hours, it's amp hours because we're actually measuring a constant current load, and you can see that it accumulates. That amp hour capacity figure accumulates over time. But, note that

**Dave Jones:** this is not an energy capacity. It's purely a amp hour capacity because it's not taking into account the voltage at all. If you want that, if you want uh an energy capacity of a battery, you have to choose constant wattage. Now, if

**Dave Jones:** you're still having a little bit of trouble understanding this, let's try the standard water analogy for electrical uh circuits. The height of this dam here, we have a very nice-looking dam. It's curved dam, by the way, in case you want to know. The

**Dave Jones:** height of the dam like this This is equivalent to the voltage due to the pressure given by the height of the dam. Now, the water flowing out here like this, the rate of flow of the water is the power.

**Dave Jones:** And if you actually narrow that gate there and control the amount of water flowing out, that's actually the current. But, when let's not go there, shall we? And you guessed it, the volume of water in the dam here is

**Dave Jones:** the energy. Get it? So, this is why you can close off the gate to the dam here and have no water flowing, no power, no current at all, but you have got the energy in the dam. And you obviously can't store a

**Dave Jones:** rate of flow of water. You can't store power, but you can store energy. You can fill this dam up. You The dam is like a rechargeable battery. You can fill it up and store energy in there, but you can't

**Dave Jones:** store the power like this. Get it? Hope that's clear. So, I hope you found that useful. If you did, please give it a big thumbs up, and as always, discuss it down below. Catch you next time.
