---
video_id: xlvqUts9H9c
title: EEVblog #33 1of2 - Capacitor Tutorial (Electrolytic, Tantalum, & Plastic Film)
url: https://www.youtube.com/watch?v=xlvqUts9H9c
source: youtube-asr
timestamps: {"0": 11, "1": 25, "2": 43, "3": 61, "4": 75, "5": 86, "6": 97, "7": 109, "8": 122, "9": 138, "10": 151, "11": 172, "12": 185, "13": 196, "14": 208, "15": 223, "16": 235, "17": 251, "18": 263, "19": 274, "20": 285, "21": 299, "22": 314, "23": 327, "24": 339, "25": 351, "26": 362, "27": 373, "28": 385, "29": 401, "30": 415, "31": 429, "32": 442, "33": 454, "34": 469, "35": 483, "36": 499, "37": 516, "38": 530, "39": 551, "40": 566, "41": 586, "42": 594}
---

**Dave Jones:** Hi, this blog is going to be all about capacitors. The what, why, how, and where of using capacitors. I've got 10 minutes. Let's start now. Okay, the first type of capacitor is the electrolytic capacitor.

**Dave Jones:** You've seen them before, these things in the metal cans. They've basically got an aluminum foil in them filled with a liquid electrolyte. And these things are absolutely horrible. They are awful capacitors in in almost every respect.

**Dave Jones:** Try and avoid using them if you can. But, the problem is the advantage of them is that they come in massive capacitance values for their size. So, really you you really can't avoid using them for things like power supply filtering and uh large bypassing and things like that.

**Dave Jones:** And power storage and some AC coupling applications for very low frequencies. It's hard to avoid these things. So, unfortunately, they're a necessary evil. You've almost certainly noticed this little vent mark on the top.

**Dave Jones:** This is actually a pressure vent that in the case of these things overheating and overloading, uh the vent is supposed to break and release the energy so that they don't explode and air foil goes everywhere.

**Dave Jones:** Well, they don't always work. These suckers can explode. They're dangerous. Be careful. One of the hugest problems with these things is that they dry out over time. Heat can kill these things.

**Dave Jones:** The liquid in there dries out and this increases the equivalent series resistance, the ESR. And really, to measure this, you've got to have an ESR meter, not a capacitance meter, an ESR meter.

**Dave Jones:** I use this Bob Parker one. Thumbs up. You've got to have something like this if you want to test electrolytics, because the life of these things is inversely proportional to the temperature they're used at.

**Dave Jones:** So, the higher the temperature, the shorter the life. Now, these will have a rated life on the data sheet at a certain temperature, but you can easily shorten that life if you mount this thing near a heat sink or something like that inside your product.

**Dave Jones:** These things need to be kept cool, but don't make them too cool cuz then they their ESR just shoots through the roof at cold temperatures. They're horrible. High ESR on these things is probably the number one failure mode in consumer products.

**Dave Jones:** If your plasma TV fails or your digital set-top box or DVD player fails, it's probably because one of these has dried out in the power supply. Odds on. Now, if you want the best reliability for electrolytic capacitors, you need to stick to the name brand ones and check the data sheets and use the high-quality ones.

**Dave Jones:** There's tons of fake ones and dodgy ones on the market, and you can get duped into it. Another major problem with these things is that they have a maximum uh charge and discharge or ripple current they can handle.

**Dave Jones:** So, make sure you read the data sheets and you don't exceed that ripple current, because if you do, they can heat up internally and, like I said, shorten the life.

**Dave Jones:** If you want really reliable designs using these things, you put two or more in parallel. That way they share the ripple current, they share the heat, and they lower the ESR, and it increases your reliability in your system.

**Dave Jones:** So, parallel is a really good way to go. And you can also get low ESR versions of these things, and they're good for using switch-mode power supplies and low-dropout voltage regulators and things like that.

**Dave Jones:** Now, the temperature variation of electros is pretty horrible. Can be anywhere from +5 to -40%, -50%. So, I just watch out for it. And of course, they're polarized. You have to put them in the circuit the right way.

**Dave Jones:** That's a major disadvantage. Now, they have a maximum reverse voltage of about 1.5 V. Anything over that continuous and you're going to damage these things permanently. Sometimes you're going to need a non-polarized electrolytic capacitor.

**Dave Jones:** And you can actually buy them, but if you haven't got one, you can do it by putting two in series back-to-back like this with the two negatives together or the two positives together.

**Dave Jones:** It doesn't matter which way around. Sometimes in high voltage applications, you need to put two electrolytic capacitors in series. It's not recommended, but if you have to, you can do it.

**Dave Jones:** Got two capacitors like this. One of them could leak very badly, and that will change the voltage division ratio, and you'll get excess voltage across one of the capacitors, and that can quickly destroy it.

**Dave Jones:** So, what you do is you put ballast resistors across the two caps. And you calculate these values based on the worst-case leakage current of one of the capacitors and the maximum voltage that that capacitor can handle.

**Dave Jones:** The other thing about electrolytic capacitors is a phenomenon called dielectric absorption. And this means that the capacitor can actually rebuild its charge after you've shorted it. You know, 10-20% recovery, something like that.

**Dave Jones:** So, in high-voltage applications, that can actually be dangerous. So, be wary of it. Next up, we have tantalum capacitors. These things, these little resin-dipped ones or these surface-mount tantalum caps.

**Dave Jones:** And these are another necessary evil in a lot of cases. You avoid using them if you can. The first problem with tantalums is that the tantalum material itself is actually a fairly rare metal.

**Dave Jones:** It requires lots of mining, and this can lead to very high prices and shortage of tantalum. A few years, quite a years back, there was a huge tantalum shortage in the market and it sent the market into complete and utter chaos.

**Dave Jones:** And they're talking about it happening again soon. The other major problem with tantalums is that they're famous for blowing up and bursting into flames. The damn things are flammable.

**Dave Jones:** And this is generally considered a bad thing. Tantalums also, just like electros, they hate high pulse and ripple current. So, watch the data sheet and don't go anywhere near those limits.

**Dave Jones:** But, it's not all doom and gloom with tantalums. They do have some good aspects. If you use them within inside their specs, they're actually very reliable, much more reliable than electros in some cases.

**Dave Jones:** But, just like electros, they they're pretty horrible caps generally. They're they're very low leakage though, that's another good thing about them. But, you'll generally find them in just pretty much power supply decoupling and large value energy reserves, things like that.

**Dave Jones:** You're very common for FPGA decoupling these days. That Now, there are many different types of tantalums these days as the technology gets better, organic and polymer tantalums. And look at using those as substitutes, but they're rarer and more expensive.

**Dave Jones:** Now, thankfully, the ceramic technology these days is eating away the need to have tantalum capacitors. Now, another type of main capacitor are these film capacitors, plastic film capacitors. And they come in two major types.

**Dave Jones:** One of the main types of plastic film capacitors are the polyester type. They are general purpose ones you use for bypassing, AC coupling, filtering applications, things like that. You can get quite stable ones.

**Dave Jones:** Their main advantage is that they have a high capacitance per unit volume. Due to their high dissipation factor, you wouldn't use polyester in high pulse, high current, or high frequency applications.

**Dave Jones:** The other major type of cap is polypropylene. Now, these have much higher performance due to their lower dissipation factor and their higher dielectric strength. You use them for high voltage, high frequency, high current, pulse applications and things like that.

**Dave Jones:** So, really grunty capacitors. But, their major disadvantage is you can only get them in small values. Here's a good tip. Polypropylene and polyester capacitors have roughly opposite temperature characteristics.

**Dave Jones:** So, if you actually put the two in two types in parallel, you can get a reasonably stable or a much more stable uh temperature characteristic. The other major type of film capacitor is the polyethylene sulfide, and these are mainly used in SMD caps cuz the other ones are mainly through hole.

**Dave Jones:** And these are very stable and close-tolerance caps. Now, the other type of capacitor out there is mica, and these are very exotic kind of things that are used really for only ultra-high stability, ultra-close-tolerance applications.

**Dave Jones:** So, if you if you need a mica, you're going to know it. I can't do this blog without mentioning mains-rated capacitors. Now, you can't just use any old capacitor when you're hooking these things directly on the mains for like suppression.

**Dave Jones:** These special mains-rated ones come in two different types, two different classes. Class X and Class Y. Now, Class X comes in two types, X1 and X2. X1 are rated for higher voltage, higher pulse applications, but either can be used generally, and they are designed X class are designed to go directly across the mains.

**Dave Jones:** They're not designed for anywhere that can be accessed by people, something for safety and things like that. That's where Class Y comes in. Class Y capacitors are used between either of the mains lines and protective earth.

**Dave Jones:** And you've got to make sure you use the right type. And these The advantage of these capacitors is that they're self-healing. What it means is that if you get a tiny little overload and spark inside the capacitor, basically what it does is it self-extinguishes itself and just breaks it and you lose a tiny amount of capacitor.

**Dave Jones:** It's minuscule, but it means the thing doesn't overload or short or explode or something like that. And you've got to make sure you use these right type of capacitors.

**Dave Jones:** If you don't, your products won't get approved and they can kill someone.
