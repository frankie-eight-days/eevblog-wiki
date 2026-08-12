---
video_id: SrZgN_EuRGw
title: EEVblog 1507 - Mida: A surprisingly good cheap portable Electric Car EVSE Charger
url: https://www.youtube.com/watch?v=SrZgN_EuRGw
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 28, "3": 44, "4": 61, "5": 73, "6": 87, "7": 99, "8": 111, "9": 125, "10": 143, "11": 155, "12": 171, "13": 187, "14": 199, "15": 211, "16": 224, "17": 238, "18": 252, "19": 265, "20": 278, "21": 291, "22": 304, "23": 318, "24": 337, "25": 349, "26": 363, "27": 374, "28": 387, "29": 397, "30": 409, "31": 422, "32": 434, "33": 447, "34": 456, "35": 470, "36": 481, "37": 500, "38": 511, "39": 527, "40": 542, "41": 558, "42": 572, "43": 588, "44": 601, "45": 612, "46": 624, "47": 639, "48": 654, "49": 671, "50": 683, "51": 696, "52": 709, "53": 724, "54": 737, "55": 749, "56": 766, "57": 780, "58": 792, "59": 806, "60": 821, "61": 836, "62": 851, "63": 864, "64": 877, "65": 894, "66": 908, "67": 922, "68": 935, "69": 946, "70": 957, "71": 971, "72": 984, "73": 998, "74": 1013, "75": 1027, "76": 1040, "77": 1051, "78": 1064, "79": 1074, "80": 1088, "81": 1105, "82": 1118, "83": 1129, "84": 1143, "85": 1156}
---

**Dave Jones:** Hi, it's quick teardown time. I got one of the cheapest EVSEs, or electric vehicle supply equipment, as they're known, which is basically a what people call an EV charger. I got one of the cheapest ones, if not the cheapest one

**Dave Jones:** you can get in this country. And this one is actually a 15 amp jobby. If you don't know your Aussie plugs, the larger 15 amp one, as opposed to the 10 amp one, is exactly the same as a regular 10

**Dave Jones:** amp Aussie plug, except the earth pin is actually bigger on that. And that's a 15 amp outlet. They're not hugely common. This is actually can give me 15 amps of charge at 240 volts, or up to, you know, whatever your

**Dave Jones:** mains supply voltage is. Here in Australia, it's 230 volts plus minus 10%. So, mine's typically 200, around 240 to 245 volts here at the lab and at home. And this will just allow me in a portable scenario to actually charge

**Dave Jones:** quicker if I've got a 15 amp outlet. But anyway, this one's about 150 Yankee bucks, and it comes from a company called Myida. And it turns out that Myida power are actually like a quite a big maker, it

**Dave Jones:** seems, of EV charging equipment. And that's all they do. They even make like faster CCS DC chargers. Yeah, they're, you know, it's not just kind of some company slapping together an EV charger. So, I thought we'd do a

**Dave Jones:** quick teardown and take a look at this. And it is actually available in a up to a 16 amp version, but it depends on which country you're in. This is the official Australian certified one. Meets, you know, all the Aussie

**Dave Jones:** standards and everything. So, this is limited to 15 amp here. But you can actually select with the button on the front, 6, 8, 10 amps, or 15 amp charge current. I don't know why you'd want to go lower, but, you know, if you're

**Dave Jones:** sucking some power from like solar and you need to power some other stuff or something, yeah, maybe. Anyway, it does have the type two plug on the other end and the cable, what have we got here? Looks like it's TUV approved, 2.5 mm

**Dave Jones:** square, which is what you'd want for a 15 amp plus the 0.5 square mm that would be for the control, 450 750 volt Changshu Ping Dao Electron Code. Anyway, it looks like and feels like a decent quality bit of kit, especially for the

**Dave Jones:** money. This is only 150 Yankee bucks. Bare rock bottom price for an EVSE charger. Anyway, let's tear it down. I think we've got some screws here. Let's check out the build quality. So, I've done a video on my Zappi charger and in

**Dave Jones:** that I've demoed and explained how EV chargers work. This is not a charger, okay? There's no active circuitry inside here that charges the car. The charger is actually inside your electric car, at least for the AC charging. For the

**Dave Jones:** really high power CCS DC chargers, no, they charge directly into the battery pack and that's why they have to be hugely complex and expensive things that you install at, you know, a service station. But for AC chargers like this one and

**Dave Jones:** ones up to like 7 kilowatts or whatever or it can be even 22 kilowatts depending on whether it's a single or three phase. Car, my 2020 Ioniq EV is only capable of single phase charging so it'll only do

**Dave Jones:** up to 7 kilowatts or so and that's what my Zappi charger does at home. But the AC chargers um all all that the EVSE here does, even though we call it a charger box, is all it does is actually switch

**Dave Jones:** through. It's just got a big relay in there that switches through the AC and then it's got a little micro in there which just sends out a PWM signal to the car to tell it what charge current is available

**Dave Jones:** and then the char and then the car will actually regulate that. So, right off the bat here, oh, I'm seeing metal threaded inserts. That's very nice. Oh, jeez. That looks nice. Really liking the look of that. Look at

**Dave Jones:** those current transformers in there. That's really neat. Just right off the bat. Loving the crimped end. Yeah, they've got a shake-proof washer on the bottom of those. I love the interface on that. This is really good. It's got an O-ring

**Dave Jones:** seal around there for some weather proofing and that goes into the top board which just has a micro on the that's that's just one button on the top end the well, that'll be the LCD driver will power it up at the end of this and

**Dave Jones:** I'll show you. But what's going on? What's this over Oh, that's just a lead Yeah, lead bar graph. Does like, you know, earth leakage detection and thermal overload protection and stuff like that. But basically, it has a big

**Dave Jones:** relay switching in here and all it does is essentially, if the conditions are right and it detects that it's plugged into the car and it sends out a PWM signal to the car. The car will then know which of what power levels is

**Dave Jones:** available. Then the car will only take that amount. But basically, all it does is switch the active and neutral will be switching both it just through and that's basically it. And the car will charge the EV battery with its own

**Dave Jones:** built-in charger. So, this thing is just a very smart relay with some you know, safety features and some PWM stuff. But isn't that layout very very nice? I'm impressed with that. We can easily get in there, measure stuff. It's

**Dave Jones:** repairable. That'd be the PWM control wire going over to the car. Looks like it's got another Phoenix connector under there. But that's not going anywhere. So, maybe there's another interface model or something. Yeah, it looks very well clamped down here. I'm just liking

**Dave Jones:** the build quality of that. That looks absolutely first class. And you got to remember this is like bottom of the line pricing, too. Like you can pay two to three times the price of this. Small touches here, they've just put some

**Dave Jones:** silastic down for whatever that is on there. Oh, that's just a cap. I see it's labeled C. Yeah, then we've just got Is that a current transformer? Is that like a Hall effect jobby in there? But, anyway, yeah, that'd be measuring that

**Dave Jones:** looks like it's measuring the active. So, this relay here would be switching the active like that, and that'd be the active going over there. And then this relay here would be switching the neutral, which is the blue one, you

**Dave Jones:** know, colors. Um, here here in Australia, we have brown for active and blue for neutral and green for earth. So, that'd be measuring the uh charge current. And then this one here would be measuring uh the imbalance between

**Dave Jones:** active and neutral. So, this'd be like an earth leakage circuit breaker type thing. Oh, I had that back to front. This is actually the output here, and this is the input. I should flip it around. All right, so we've got mains

**Dave Jones:** input over here, okay? So, basically, if the current flowing through the active like this out here into the right out here into the car, and it doesn't come back, if it's out of balance with the current that flows through here, then

**Dave Jones:** you'll have a differential in the current between these two. They won't cancel out each other out anymore, and it can detect the difference. That's probably that uh circuitry down there, and it can detect that's an earth leakage um circuit breaker. Well, it's

**Dave Jones:** basically a core balance um relay thing, and then that will trip and disconnect the whole thing as a uh safety feature. So, that's really nice. And what else we got in here? Well, up the top here, looks like this is just the mains uh

**Dave Jones:** power supply, which, you know, so this'd be the mains coming in here again. We've got another Or maybe these Phoenix connectors are here for factory test, cuz I don't know what their version of the product would use Phoenix

**Dave Jones:** connectors. Maybe, I don't know. I don't know. Anyway, um if you know, leave it in the comments. But, it wouldn't be too hard to do better nails when you got the huge big contacts like this so you could

**Dave Jones:** have, you know, a big lid with pins that come down and make contact with these, and then you could uh test your boards at uh the production factory stage. But anyway, this would be an isolated switch mode supply for powering the circuitry.

**Dave Jones:** A bunch of series resistors up there, so they're getting they're putting those in series so that they can get a high voltage resistor in there to get the voltage drop on that. As for the relays in here, what have we got? HF. So the

**Dave Jones:** big question is are these Japanese relays? Not Japanese relays unfortunately. These are Hongfa brand, but they are serious relays for this sort of application and also certified as well. So these are actually 50 amp relays. So they might actually use this same board

**Dave Jones:** in they might I think they make a 32 amp version of variant of this. It looks slightly different but you know, maybe they use the same relays in that as well. They certainly could. And these are actually latching relays, so they

**Dave Jones:** don't need coil power to keep them in the latched state. And I don't know why you'd use a latching relay for this sort of thing. It's not like the coil current consumption is an issue. And really I would prefer that like if it lost power,

**Dave Jones:** I don't want it to be latched in a certain state. I'd rather see it like like normally open and then it has to require the active electronics to then keep it energized and switched on. And the input is fused as you'd expect. You

**Dave Jones:** can see that little SMD jobby down there. That's for the main switch mode from the mains input side. Nice. Anyway, interestingly there is an NTC thermistor temperature sensor input there. I mean the micro's probably got a temperature sensor in it as well because I can't

**Dave Jones:** imagine that it's not measuring the internal temperature in a sealed enclosure design like this. My guess would be that given the proximity of this thing, they would actually have in the higher amp models, but not in this one, they would actually have a

**Dave Jones:** thermistor measuring the temperature inside the mains plug because when you start talking 32 amps you start talking you know serious like 15 amps is like mad like you know I I wouldn't bother. That's why they haven't got it fitted in here but

**Dave Jones:** yeah it can become a problem. You know you get dodgy connections on your mains input plug and that can overheat and that can be ruin your day. So yeah you would want to add a thermistor in there and then they would use

**Dave Jones:** a non-standard mains cable and they'd have like an extra pair going up there to the thermistor and then that would just plug in there and there doesn't seem to be another input there for like any sort of you know moisture ingress

**Dave Jones:** sensor cuz like this is a portable one so you might use these like out in the rain. Back side of the board only a single sided load and they've got some extra current carrying capacity by removing the solder mask and just

**Dave Jones:** leaving the solder plate on there but it's exactly what I expected. Nice spacing, everything's hunky-dory, nice solder joints on there too. It's all looking pretty schmick. All right, let's just go briefly through the PCB. Down the bottom here this is actually

**Dave Jones:** interesting. This is an STMicro jobby so there's tons of like Asian alternatives but they use an ST one a Viper 27. Why can't all chips be given decent names like Viper 27? I love it instead of like LM12345.

**Dave Jones:** Come on. Give me a Anyway, it's an offline high voltage converter here so exactly what you expect. It's just an isolated offline converter optocoupler feedback that's in there somewhere but yeah plain vanilla stuff. I just a bit surprised that they used an ST part

**Dave Jones:** there. I didn't look at what brand caps they're using on the output here but yeah so you got your mains input here. You've got your common mode choke. You've got some X and Y class caps here by the look of it and the just the

**Dave Jones:** offline converter and there's your secondary. So I'll flip to the back side of the board which is like you're looking through the board so I flipped it and oriented so we'll see like the output down here like this. And if we

**Dave Jones:** flip over the you can see that there it is there. There's the secondary output there. And you can see that that powers all the stuff along the top side here. So that includes this chip we'll take a look at, this one we'll take a look at,

**Dave Jones:** and this one here. This one obviously it's right near the PWM output here. It would control the relays as well. You can see a couple of back EMF diodes in there, can we? Um this one here is obviously to do with the current sense

**Dave Jones:** here, the core balance relay like this. And this one over here, I thought was just like a driver going over to the like the LC like a shift register or something, but no. It's not. It's more interesting than that cuz this is the

**Dave Jones:** mains input here and you'll see that it's actually going off through these caps, right? So you got a capacitive resistor divider thing happening here. So what is this chip? Like I thought, you know, right near these pins, I got

**Dave Jones:** fooled. It's actually this thing. We've got a HighTrendTech chipset here. What it is is an energy monitoring chip. I didn't expect an energy monitoring chip. There you go. 22-bit sigma-delta ADC. I expected just basic current limiting, you know, is like limited to

**Dave Jones:** X amount of current. Like there's no need to measure the real power and apparent power, but maybe it's just for like overload and it's maybe it's cheapest chips. I'm here all week. This one over here can measure the current that's doing the

**Dave Jones:** current measurement so I don't know how that's getting back over to here like this. There you go. There's the current transformer there or the Hall effect sensor and that's going these traces going back over to there. So it is

**Dave Jones:** actually measuring the current and the voltage so we can actually measure the real power consumption, real and apparent power consumption of this thing. So according to the manual, comprehensive as it is, it seems to only have a voltage and

**Dave Jones:** current display. It doesn't have a power display, let alone a kilowatt hour like an energy uh display to tell you how much accumulated energy is put into your car. And this one in here is exactly what you'd expect. This is uh the chip

**Dave Jones:** that connects to the um hall effect current uh sensor thing here. I don't know what it is. Um but it's an FM2147. And all this circuitry will no doubt match the application note over here. This is a Fude and microelectronics

**Dave Jones:** group company limited. And this is a very specific uh earth leakage monitoring chip. It's designed for exactly this application here. And uh it's got a block diagram here, but it's also got an application schematic. I bet you this is going to be pretty darn

**Dave Jones:** close to the application circuit. And our um it's got the input specific input there for the uh current transformer here. It just measures the imbalance. I don't know what you set set it to. Like there's no adjustment thing in here.

**Dave Jones:** Maybe it's like you know, fixed to some standard 30 milliamps, 50 milliamps, something like that current. I don't know. Maybe you'd have to translate it from the voltage coming out. I don't know. Anyway, yeah, that's a dedicated earth leakage um breaker chip, as you'd

**Dave Jones:** expect. And this up here, I thought would have been a micro to drive this pin, but it looks like it's an ST um 2902, just a Joe Blog's um quad op amp. Anyway, that makes sense because you've got a capacitor dropper Well, you've got

**Dave Jones:** two capacitor droppers down here, and then a high voltage series resistor. And there, the trace you can see that going off over to here. So, that's doing some sort of monitoring uh for the car side over here. But anyway, the micro must be

**Dave Jones:** over on the main board. And the main board, as you can see over here, that is an STM32 uh micro. So, once again, bit surprising that they didn't use some, you know, Asian Asian sourced uh micro in here. Guess they already have

**Dave Jones:** the uh development experience for the ST micro. And this flat flex ribbon here is for the uh switch, which is on the front panel there. It's just got some leads there, which then connect through here and and Bob's your uncle. These dip

**Dave Jones:** switches here, I would uh say that they set the model and region cuz they sell these in the different countries. There's different standards, as I said, this thing this actual model is capable of 16 amps, but they limit it to 15 amps

**Dave Jones:** here in Australia. Don't have a 15 amp outlet in the lab or I did. Although, somebody took it out when they uh I rented this place out and they renovated, but there it is. Oh, no, it does have kilowatt display there. They

**Dave Jones:** got it does have kilowatt hour. There you go. Didn't have that in the manual. 24°, so yep, it's got an internal uh temperature sensor as I suspected. Um it doesn't know the earth is uh missing cuz it's got no way to detect that. I don't

**Dave Jones:** actually have the earth connected. Please excuse the crudity. The model didn't have time to build the scale or to paint it. Put a uh 2.7 K um from the earth through a uh series diode through to the uh control pilot pin here. And uh

**Dave Jones:** then uh that will determine that it is connected. Is it connected? Yes, it is. Winner winner chicken dinner, but it's not actually starting the uh charge current yet. To do that, we have to put the car actually This is normally all

**Dave Jones:** this stuff's normally inside the car. To do that, to make it uh switch through, we have to put a 1.2 K in parallel with it. Boom, I heard a relay switch and it's charging. There you go. No worries. It's Well, it's not

**Dave Jones:** charging. It switched the AC through. Works. And I want to see what happens if I imbalance the uh thing with the diode here. Will it disconnect? No. No, it's still it's still charging. So, it doesn't need the diode. It looks like

**Dave Jones:** it's not doing the um uh imbalance diode protection thing. Okay, so I've got the diode shorted. And no, it's still No, it ignores the diode. so I I don't know if that's a specific standard. I don't know, you'd

**Dave Jones:** have to go into it, but it looks like it doesn't It doesn't matter whether the diode's there or not. Some chargers do, apparently. Anyway, it seems to do the business and meets the basic requirement there. You could get a resistor divider

**Dave Jones:** box out. Nah, I won't bother. By the way, when you switch it off, it doesn't seem to unlatch those relays when it loses power, but it switches the relay back off as soon as you immediately apply power. So,

**Dave Jones:** not a problem, I guess. This was supposed to be a teardown video, so you'll leave it at that and I don't know, you might see an operational thing of this on my EV one day, but actually, I'm very impressed with this. And look,

**Dave Jones:** we can just change that, can we? Yep, yep, 6 amps through to 15 amps and that's it. But I'm very impressed for the price point. I like expected this to just be slapped together and shoddy quality. And I'm impressed by the

**Dave Jones:** quality of the case, too. Just the real thick ABS construction. You saw like the ribs inside and everything. It's supposed to be IP67 rated. It looks It's weather rating looks really good. But IP67 is supposed to survive like a 1-m water immersion for

**Dave Jones:** up to 30 minutes. I don't know if you'd whack this in under 1 m of water for 30 minutes, but you know, it's at least IP66, maybe in theory IP67. know how they done the sealing around the screen

**Dave Jones:** and stuff like that, but the end but the O-ring sealing here and the ends and everything looks hunky-dory. So, as far as weather resistance and ruggedness goes, wow, it's unbelievable for the price. And the quality of the design and

**Dave Jones:** construction of this thing, I was quite impressed. And this is like a bottom of the price unit. There's no need to pay more than you know, this. What was $150? So, if you're after an additional EVSE for your car, usually they're included when

**Dave Jones:** you get an EV, but you might need a second or a third one or something or a replacement one. And yeah, there's There's need to spend more than this. I'm quite impressed with this uh Ryobi uh brand. It's pretty darn good. So,

**Dave Jones:** yeah, I just didn't expect that for the price. Anyway, thoughts and comments are down below. We'll catch you next time.
