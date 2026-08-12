---
video_id: TDDoi70cxw0
title: EEVblog #33 2of2 - Capacitor Tutorial (Ceramics and impedance)
url: https://www.youtube.com/watch?v=TDDoi70cxw0
source: youtube-asr
timestamps: {"0": 10, "1": 23, "2": 37, "3": 50, "4": 62, "5": 79, "6": 92, "7": 110, "8": 127, "9": 140, "10": 153, "11": 174, "12": 192, "13": 205, "14": 221, "15": 238, "16": 251, "17": 265, "18": 278, "19": 292, "20": 310, "21": 322, "22": 337, "23": 353, "24": 368}
---

**Dave Jones:** Now, the next type of cap is ceramic. Now, this so tiny I'm not even going to show you, but the move to ceramics is almost complete. The The advances in ceramic technology over the years is just amazing and it keeps getting

**Dave Jones:** better. They used They're probably the most popular capacitor by far on the planet and they used for all sorts of things. Now, when you're talking about ceramic capacitors, there are two basic classes defined by the EIA, class one and class

**Dave Jones:** two. Class one ceramic capacitors are the NPO and COG types. They do come in other types, but they're the two main ones. And the advantage of class one ceramic caps is that they do not change with temperature. They're very, very

**Dave Jones:** stable, but they only come in low values. That's their major disadvantage. Now, the second type is class two type capacitors and there's more varieties than you can poke a dead stick at, but some of the more common ones, you'll

**Dave Jones:** hear terms like X7R, X5R, Y5V, Z5U. And this is a code. The first character means it's the minimum temperature. In this case, X is better than Z. The second character defines the maximum temperature of the capacitor. And in

**Dave Jones:** this case, a higher number is better. Seven's better than five. And the third digit is the temperature coefficient, how much change in capacitance you get with that temperature range. And in this case, R is better than U. Uh R might be

**Dave Jones:** plus minus 15%, but these Once you get down into V and and U, they're absolutely horrible. Minus 82%, minus 56%. These things are absolutely shocking. Atrocious. Now, generally ceramic capacitors are known as multi-layer capacitors due to their construction of

**Dave Jones:** multi-layers between the two end caps and that's their more more common term now, multi-layer chip capacitors. Ceramic capacitors are used by the zillions. You can't count these things and they're used for general purpose stuff like bypassing and filtering and

**Dave Jones:** things like that cuz there's a whole grade and whole variety of ceramic capacitors for all these different purposes. Some are very stable, some are just absolutely atrocious that you only use for, you know, rough decoupling applications and things like that. So,

**Dave Jones:** it's very important to choose the right type of ceramic capacitor. You can't just whack any ceramic capacitor in there. It probably won't work. Now, one weird thing about class two ceramic capacitors, because of their because they're ceramic and their

**Dave Jones:** multi-layer construction, they are absent they are actually what's called microphonic. Due to the piezoelectric effect, any sound or vibration in either directly into the cap or via the board can actually flex it and it can generate a voltage just like a microphone. These

**Dave Jones:** things will actually pick up and uh translate sound. And this phenomenon also works backwards. So, uh if you drive this with a voltage at some audio frequency or something like that, you can actually these things will actually flex and they'll actually generate sound

**Dave Jones:** and the PCB can be used the PCB substrate can actually act as an amplifier and these things can you can actually hear these things. It's a it's it's it's not fairly common, but if you're working on precision uh audio

**Dave Jones:** stuff, this can actually be quite important. Uh microphonics, watch out for it. Now, this uh same microphonic phenomenon can also happen in other caps like film caps as well, but not as much. And it can also happen in uh cables and other

**Dave Jones:** things cuz cuz remember, cables are capacitors too and they can have uh microphonics and triboelectric effects as well. Go and Google that one. Uh ceramic capacitors uh can fail short circuit, but they usually the main problem with them is that they are very,

**Dave Jones:** very brittle, very, very fragile. You can damage them soldering on the board with excess temperature, handling, and flex on the PCB as well. If you mount them in one direction and you flex the board like this, you can actually crack.

**Dave Jones:** They can get microcracks in them, and that can be a real problem for long-term reliability and things like that. So, just be very, very careful with how you mount and handle multi-layer ceramic capacitors. Right, so that's the end of

**Dave Jones:** the capacitors, but I think we've got a couple of seconds to explain an important characteristic of capacitors, which is pretty neat and a lot of people don't understand it. Now, it's the impedance versus frequency characteristic of a capacitor, and it's

**Dave Jones:** going to look something like this. Now, the model of a capacitor is the ESR in series with the capacitive reactance, which changes with frequency, and the inductive reactance as well, which also changes with frequency, and this is the

**Dave Jones:** total impedance. So, the graph is the impedance versus the frequency, and it looks like this. Now, at low frequencies, the the actual capacitive reactance is going to dominate, and then at higher frequencies, the inductive reactance is going to take over, and

**Dave Jones:** that's going to dominate the total impedance of the capacitor. And there's going to be a resonant point here where these two things are equal, and you know, and that's the best place to operate the capacitor at in terms of

**Dave Jones:** impedance. Now, the important thing about this is that it comes into play. You've probably seen multiple capacitors in parallel, all these different values across a chip for decoupling. And what the reason they do this is because each capacitor will have a different

**Dave Jones:** characteristic like this, each value. So, your total will look something like that, and you get a much lower capacitance the entire frequency range. And that's why you put them in parallel. It's not as silly as it sounds. It's

**Dave Jones:** actually quite a valid technique that can gain you quite a considerable performance in terms of decoupling and EMI and things like that. So, there you go. Huh, that's it. There you go. That's the end of capacitors. How do you choose a

**Dave Jones:** capacitor? I don't know. Don't ask me. It's too complicated.
