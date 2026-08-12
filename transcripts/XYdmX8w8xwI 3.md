---
video_id: XYdmX8w8xwI
title: EEVblog 1599 - TOP 5 Jellybean Bipolar Transistors
url: https://www.youtube.com/watch?v=XYdmX8w8xwI
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 26, "3": 35, "4": 48, "5": 62, "6": 86, "7": 98, "8": 115, "9": 130, "10": 145, "11": 158, "12": 169, "13": 180, "14": 200, "15": 219, "16": 231, "17": 246, "18": 265, "19": 285, "20": 298, "21": 313, "22": 324, "23": 336, "24": 354, "25": 362, "26": 376, "27": 392, "28": 409, "29": 428, "30": 441, "31": 452, "32": 462, "33": 475, "34": 487, "35": 503, "36": 514, "37": 529, "38": 545, "39": 557, "40": 568, "41": 588, "42": 595, "43": 608, "44": 621, "45": 633, "46": 645, "47": 659, "48": 671, "49": 685, "50": 699, "51": 707, "52": 718, "53": 729, "54": 747, "55": 758, "56": 775, "57": 788, "58": 801, "59": 817, "60": 828, "61": 853, "62": 865, "63": 875, "64": 887, "65": 907, "66": 922, "67": 937, "68": 947, "69": 958, "70": 970, "71": 982, "72": 996, "73": 1006, "74": 1018, "75": 1028, "76": 1046, "77": 1057, "78": 1070, "79": 1085, "80": 1103, "81": 1114, "82": 1130, "83": 1148, "84": 1163, "85": 1169, "86": 1181, "87": 1190, "88": 1207, "89": 1219, "90": 1228, "91": 1238, "92": 1252, "93": 1260, "94": 1276, "95": 1293, "96": 1305, "97": 1321, "98": 1342, "99": 1358}
---

**Dave Jones:** Hi, it's jellybean component time again. I've done three previous videos on this jellybean op-amps, uh jellybean regulators, and jellybean comparators. Today, we're going to do the top five, or thereabouts, maybe a few more special mentions, uh transistors.

**Dave Jones:** In particular, BJT transistors, bipolar junction transistors, not MOSFETs, because that's a whole can of worms in its own right. So, what makes a jellybean component? Well, there's a couple of things that go into it.

**Dave Jones:** The first one is that usually it's been around forever, for a long time. In fact, some of the ones here date from like the late 1950s. So, yeah, pretty old.

**Dave Jones:** So, everyone knows them, everyone's familiar with them. The second criteria is that it has to be available from multiple sources. If you can only get a component from one or two manufacturers, then it's not really jellybean.

**Dave Jones:** In the case of the ones we're going to see here, they're available from countless different manufacturers, not only Western manufacturers, but Asian manufacturers as well. The third criteria is that they have to be cheap and in stock from all of your component distributors.

**Dave Jones:** If you can't get millions of them, then it ain't jellybean. And pretty much the specs of the jellybean components have to be so generic across all the different manufacturers that if you specify in one of these jellybean components, then it doesn't really matter whether or not you get it from TI or ON Semi, or whether or not you get it from some weird Asian manufacturer you've never heard of before, they all

**Dave Jones:** should perform pretty much the same. And that's the case of all the parts we're going to look at today. So, our first jellybean BJT transistor, and yes, I'm aware it's bipolar junction transistor transistor, it's like saying AC current, alternating current current.

**Dave Jones:** Whatever. Anyway, it has to be the classic 3904/3906. The 3904 is the NPN part, the 3906 is the PNP part. So, that's what we'll do today, we'll get the PNP equivalent of the NPN one.

**Dave Jones:** But, NPNs are generally more popular, so we'll just say the 3904. How popular is a 3904? Well, it's got its own Wikipedia page. It's pretty popular. It's been around since the 1960s, okay?

**Dave Jones:** It's been around forever. So, the 3904/3906, let's have a look at Digi-Key here. And by the way, any jelly bean part, if you're searching, you should exclude marketplace products here, and you should do in stock and normally stocking.

**Dave Jones:** So, if you can't find a jelly bean part using in stock and normally stocking and excluding marketplace parts, then it ain't jelly bean. And you can see it's available from all these different manufacturers here, many of which you've never heard of before.

**Dave Jones:** And it's let's take a look. Available quantity, 2 million in stock. And it's 1.6 cents in 3,000 quantity. And 75,000, 1 million in stock, 5 million in stock here.

**Dave Jones:** Right, there's just no shortage of stock available. And same over here on Mouser as well, available from all these manufacturers. And we've got hundreds of thousands, if not millions, in stock.

**Dave Jones:** No worries. And if we go over to LCSC, which is the Asian equivalent of like your catalog supplies here, like Digi-Key and Mouser, then you'll get all of these manufacturer names, some of which will be familiar, like Diodes Incorporated, sort of like Western names, but all of these Asian names you've never heard of.

**Dave Jones:** The 3904 is available, you know, there's even Toshiba in there. And but all these names you've never heard of. And once again, you go down here and you go filter for in stock, and they're 0.3 cents each, and they're available, and there's the MMBT, and 150,000 in stock, and hundreds of thousands, if not millions, in stock.

**Dave Jones:** No worries. So, the 3904 here is a general purpose NPN low power transistor. So, we'll categorize these. We start at low power, then we'll go medium power, then we'll go high power.

**Dave Jones:** And it's available in many different packages, but these days, cuz everything's surface mount, it's regular SOT-23 package. This is why it's called the MMBT3904, but your old school people might know it as the 2N3904, which is in a plastic TO-92 package.

**Dave Jones:** But you can see here, it's available in many different packages. DFN packages, SC-70s, SOT-223s, if you're a SOT-223 fanboy, and on and on and on. And of course your classic through-hole TO-92 packages as well.

**Dave Jones:** And here's the thing about jellybean parts, you should be building these into your CAD component libraries in all of these different footprints, so that you go, "Ah, I need a 3904, just a general purpose low power NPN jellybean transistor, and but I've got a different design requirement because I've got an ultra-small package this time.

**Dave Jones:** Okay, like I might need it in this tiny 0.6 mm by 0.8 mm package. Look. Look at this. It's tiny, but it's the exact same transistor, just available in many different footprints for many different applications.

**Dave Jones:** And that's why it's jellybean. And the SMD marking on this is 1A. So, you'll see that everywhere in teardowns that I do, if you see 1A on there, then you know it's a some variant of the 3904 from whatever manufacturer.

**Dave Jones:** You know, this one here might have some like some date codes after it, but it's basically a lot of them will just have 1A. And the PNP equivalent is the 3906 here, and it has a 2A marking on there.

**Dave Jones:** So, 1A, 2A, easy to remember. If you see that in teardowns, you know it's a jellybean 3904 3906. As with all jellybean parts, don't set the world on fire, but they're good enough for most applications.

**Dave Jones:** This particular case, a 40 V collector-emitter breakdown voltage here, and the current gain or HFE is pretty reasonable, can be up in the couple of hundred uh range, depending on uh the current here, and the VCE uh voltage can be as low as 1 V, so you can use them in fairly low voltage applications.

**Dave Jones:** And it's actually reasonably quick, can go up to 300 MHz here. I've used uh these in FM bug applications at, you know, 100 MHz, and they work just great.

**Dave Jones:** And it has a maximum collector current up to about 200 mA, so that's why it's a low power uh jobbie, and that's all you need for a ton of applications like just, you know, driving a buzzer, driving a little array of uh LEDs or something like that.

**Dave Jones:** Does the business easily. And it's got a maximum saturation voltage here of like 0.3 V, which, you know, good enough for most applications. And of course, uh power dissipation, you only get like a couple of hundred milliwatts here, uh maximum power dissipation in the SOT-23 package.

**Dave Jones:** And we won't go into the characteristic curves of any of the transistors uh here today, but suffice it to say, if you just need a low power uh NPN transistor that's cheap and readily available in many different packages, the 3904 3906 is going to do the business.

**Dave Jones:** I know, I know, I can hear the comments typing away furiously down below, "Uh the 2N2222." Okay, the 2N2222, it's actually even more famous than the 3904, and it was actually developed in the 1950s and was popular in the 1960s in a metal can uh package like this.

**Dave Jones:** And this is where the uh 3904 came about because it was a plastic package at the time back in the '60s, and that was a big deal, replacing the metal can uh package at a cheaper price.

**Dave Jones:** Blah blah blah blah blah. So yes, the 2N2222 is still spectacularly uh popular, and it's actually just about in available in just as many varieties, and it actually has a higher current uh capability.

**Dave Jones:** So let's check it out on Digikey here. Yes, it's available from all these uh same manufacturers that we got before, and yes, it's available in the millions like this, and uh yes, it's 1.7 cents.

**Dave Jones:** So, I think technically a bit more expensive possibly than the 3904 and the 2222 can do 600 milliamps. So, that's basically like major major difference between that and the 3904.

**Dave Jones:** It is a bit higher current capability. So, if you need that but whether or not you stock the 3904, 3906 or the 2222, it doesn't really matter. Six one half dozen the other.

**Dave Jones:** And if you want the PNP equivalent of the 2222, it's the 2907. So, for me, it's not as easy to remember as the 3904, 3906 and if we go into single BJTs down here and we go into in stock normally stocking and exclude marketplace products and we apply.

**Dave Jones:** There you go. Once again, it's available from all and sundry and the price is like 3.6 cents. You'll get it cheaper from LCSC and stuff like that. You know, 7 million at the factory.

**Dave Jones:** Blah blah blah blah blah. Um but I would argue that possibly the 3904, 3906 is probably more popular these days than the 2222. But hey, argue all the way down in the comments, but I'm going to say the jelly bean is 3904, 3906.

**Dave Jones:** And of course, there would be the BC547 fanboys. Let's just like it never ends. It's like religion. And the other good thing about the 3904, 3906 is you can get them in multiple transistor packages like this.

**Dave Jones:** So, if you need like an array of transistors, you can get them pretty cheaply in like various packages. Really neat. So, you can see in this Fairchild data sheet, you can get dual versions.

**Dave Jones:** Beware of different pinouts here. You can come a gata or you can get a quad like this. Just very handy if you need an array of general purpose low power transistors.

**Dave Jones:** So, now we're going to talk about medium power BJTs. I put medium power at, you know, round about 2 amps or something like that. So, if you need more than a couple hundred milliamps or the 600 milliamps of the 222, then, you know, you need like an amp or two um particularly in like a small surface mount package, then you're looking at a medium power transistor.

**Dave Jones:** You don't want to have to go up to a TO220 package or, you know, a big D-pack or something like that. You just want an amp or two in a nice little SOT23.

**Dave Jones:** Well, I got two picks for you. So, I don't know. I'm just going to include them both. Um so, I would go for the FMMT 619, but there's actually three variants.

**Dave Jones:** There's the 617, the 618, and the 619. But, you can see here that they have hundreds of thousands here, and they have millions at the factory. And it's available from at at least from Digi-Key from three different manufacturers, which is not great, but it's not too bad.

**Dave Jones:** But, if you go over to LCSCE, it's available from more manufacturers over here. Once again, they're all in stocks in big quantities, and they're only like, you know, 3 cents to a couple of cents each something like that.

**Dave Jones:** So, let's take the 619 from Diodes Inc. here. It's a 50-V collector-emitter rating here, but it's a 2-A continuous collector current in a SOT23. So, that's not too shabby at all.

**Dave Jones:** 625-mW maximum power dissipation in that package. It's got less than 200 mV VCE saturation voltage at 1 amp. They even specify the milliohms, 68 milliohms for the on resistance here.

**Dave Jones:** And the HFE is characterized up to 6 amps for high current gain stuff. So, you know, it's it's pretty good. And if you want the PNP equivalent, then you're looking at the FMMT 720.

**Dave Jones:** And I told you about the 617 version. It basically trades off the maximum collector voltage for the current. So, it has a maximum voltage now of only 15 V, but that's still plenty for like, you know, like 12-V applications or even lower.

**Dave Jones:** No problems. But, you actually get a higher current capability in this particular 3 amps maximum current continuous current capability, but you can get 12 amp peak pulse current in this thing.

**Dave Jones:** So, it's not too shabby at all. So, maybe keep both one keep for the higher voltage one and 619 for the higher voltage stuff. Or you can argue the 617's probably more valuable.

**Dave Jones:** So, I'd say like the 617's more jelly bean because most people aren't designing stuff in the you know 50 40 50 volt region something like that. You know, you usually like 12 volts is plenty.

**Dave Jones:** So, the 617 really does the business in most applications. Just look at those specs. And if you want the PNP equivalent, it's easy to remember. It's just the 717 instead of the 617.

**Dave Jones:** And once again, from LCSC, you can get these for like 2 cents a pop available from you know quite a few different manufacturers here. And mostly they're going to have stock not as popular as the jelly bean 3904s for example, but for medium power transistor, yeah, this does the business.

**Dave Jones:** Now, the next one I'm going to include here in the medium power category is the even more popular SS8050. And you'll see it's available from quite a lot of manufacturers here.

**Dave Jones:** If you go over to LCSC, it's available from a lot more. Look at these. Look at these. No wonder this is massively popular in China. So, if you tear down a lot of like Asian products, odds are you might find an SS8050 in here.

**Dave Jones:** Now, it's also available as the S8050, but that's a lower current one. So, the SS8050 is a 1.5 amp jobby. So, not as good as the 617 619, but good enough.

**Dave Jones:** Like if you need like an amp or an amp and a half something like that, then it's going to do the business. And it's only available in SOT-23s 323s and old school TO-92 packages, but for most applications, that's good enough.

**Dave Jones:** And it's like a .08 cents uh example. And available from yeah, all these manufacturers. And uh stock is no problem whatsoever. Like one 1.1 million here, 863,000 from all these different manufacturers, and they're all pretty much the same.

**Dave Jones:** Open up any random uh data sheet, and they're all going to be equivalent. 1.5 amps here, and you're going to get a 40-V maximum rating, good enough for most applications, and you know, it it does the business.

**Dave Jones:** It's got reasonable gain, it's got reasonable frequency, you know, 100 100-ish MHz, uh and reasonable gain at uh current. So, it it's cheap, it's available from more manufacturers, but if you need slightly higher power, I'd recommend having the uh 617 in your uh kit as well as the SS80 uh 50 because, well, this is going to be cheaper than the 617 and more readily available, but slightly lower

**Dave Jones:** power. But, they're both I'd categorize them as medium-power transistors. And just remember, if you see that marking code of Y1, you'll see that in tons of teardowns that I've done, uh then you know it's an SS80 50, but be careful.

**Dave Jones:** You can also get the Y1 marking on the S8050 as well. And just remember, there is an S version instead of the SS of the 8050, but it's lower voltage, uh 25 V and only half an amp here.

**Dave Jones:** So, if you're stocking a medium-power transistor, 500 milliamps, ain't it? You might as well use the 2222 at that uh point. So, yeah, but the SS8050 definitely goes along with the 617 619.

**Dave Jones:** And the PNP equivalent's going to be the SS8550 here, available from many different uh manufacturers, and the marking code is going to be Y2 instead of Y1. So, easy to remember when you're looking at uh teardowns, and you basically get uh the same 1.5 amp uh 40-V rating on there, except it's PNP equivalent.

**Dave Jones:** And now, jelly bean high-power transistor, which I would classify as or greater. You can't go past the classic 3055, the 3055. And yes, of course, it has its own Wikipedia page.

**Dave Jones:** It's been around forever, like 1967. There you go, from RCA. And of course the classic package is the TO big TO3 package here. But of course it's available in tons of different packages.

**Dave Jones:** Classic TO220 like this. You've got your D-pack. That'll do 60 volts at 10 amps. So it's reasonably high voltage as well and can do like 10 or 15 amps capability.

**Dave Jones:** And well, just there's no other, is there? I don't know. Flame away. But the 3055 can't be beat for jelly bean high power transistor. So there is the little beastie.

**Dave Jones:** Look at this D-pack and I-pack as well from On Semi here. And the PNP equivalent, easy to remember, is the 2955 here instead of the 3055. Simple to remember.

**Dave Jones:** And the letters at the front here, of course you might be familiar with 2N. Well, that's your traditional metal can package. But then the MJD here might be like these D-packs and I-packs.

**Dave Jones:** And then you might get MJE here. Then you might get NMJV. And they're basically all different package types. Then you might get the TIP3055 here in the big baddie TO247 package.

**Dave Jones:** That's a bad boy. And yeah, so we can look at that. Look look look at it. Look at it. Look at it. Oh. So we've got a 60 volt maximum rating here and either 10 or 15 amps depending on the type.

**Dave Jones:** And you know, it doesn't have super high gain or anything. But when you got high current like this, you don't expect that. And frequency-wise, like it's only a couple of megs.

**Dave Jones:** So like if you're working at those sorts of frequencies, you're not in at high power switching. You're not in the jelly bean domain anymore. So it doesn't matter. Yeah, no.

**Dave Jones:** Now, I wasn't going to talk about MOSFETs, but the 3055 actually go search for 3055 in Digikey here. Look, there's 43 items in BJT transistors bipolar junction transistors, but FETs, MOSFETs, there's 81 items.

**Dave Jones:** So, the 3055 is the only part I know that basically has an equivalent BJT and MOSFET as well. All right, leave it in the comments uh down below. There's probably others, but the 3055 is most famous.

**Dave Jones:** So, it's a jelly bean MOSFET as well. So, 60 V 3 A SOT-223 package available in the SOT-220 package as well. Then, you can go up to bigger packages here.

**Dave Jones:** Um and you know, you can get 60 V 11 A for example. And these are MOSFETs. So, if you need the particular requirements of MOSFETs, and I won't go heavily into the differences, but BJTs are basically they're more robust than MOSFETs.

**Dave Jones:** Like, you can't easily damage them static-wise, and they might have more better overcurrent capabilities and stuff like that. You can think of BJTs if you need just simple, rugged kind of stuff, and and easier potentially easier to drive over MOSFETs, which are a bit more trickier.

**Dave Jones:** And BJTs can work at really ultra-low uh voltages as well, whereas MOSFETs might have particular higher requirements and trickier to drive and bias and you know, stuff like that.

**Dave Jones:** But, yeah. So, stock the 3055 in whatever flavor package you want in for your MOSFETs as well as your BJTs. And likewise, you can get the complementary the P-channel MOSFET in the 2955 here, and they're going to have no shortage of those as well.

**Dave Jones:** Once again, on LCSC BJTs, you got 31 here, and you've got 88 MOSFETs here. So, yeah, there's just no shortage of them. And if you want to have a look at the manufacturers, the different manufacturers here, not a huge number, but good enough for Australia, that's for sure.

**Dave Jones:** And you know, available in a few different packages here. But, because these are higher power applications, they're not used in the same sort of volumes you'll get in the medium and low power transistors that we saw before.

**Dave Jones:** You know, so availability, you know, you might be looking in the thousands, something like that. But, you can actually get different sources, and that's kind of the whole point.

**Dave Jones:** So, we've covered low power, medium power, and high power transistors. What category's left? Well, I'm going to leave out RF because if you're talking RF, you're talking about you have really specific requirements.

**Dave Jones:** So, I wouldn't say, but leave it down below if you've got a jelly bean RFR transistor. I'm not going to include one. So, I'm going to go for high voltage because you might need a high voltage BJT transistor.

**Dave Jones:** That's going to be, I guess, more common than an RF BJT. So, I've I'm going to go for the FMMT 458 here with the PNP equivalent, the 558. And look, you can get, you know, a couple of million at the factory and hundreds of thousands at Digikey.

**Dave Jones:** And, you know, 11 cents each. And if we go to LCSC here, we've only got three manufacturers to pick from here. But, like we're getting a bit exotic here at high voltage transistors.

**Dave Jones:** When I'm talking high voltage, I'm going to say 400 volts or higher. So, over here, you don't actually get as much stock as you do at Digikey, for example.

**Dave Jones:** And at Mouser over here, you got 233,000 in stock, so no worries. So, the 458 and 558, what are we talking about here? Well, a 400 volts collector-emitter voltage.

**Dave Jones:** So, really, you know, any high voltage like mains type stuff or anything like that, you'd be looking at something like this. 1 amp peak peak pulse current, but 220 milliamps continuous collector current here.

**Dave Jones:** It does a reasonable job for a general-purpose jelly bean high voltage transistor. And as I said, if you want the PNP equivalent, you're looking at the 558, the FMMT.

**Dave Jones:** But, that's a SOT-23. If you want something a a bit gruntier, you can go for the FZT 558 for example and you can get that in a nice sort 223 package instead of the sock 23 and it's just a little bit more better.

**Dave Jones:** And yes, I know there's BD139 fanboys out there but I'm sorry it's yeah, it's old school jelly bean but it it it doesn't cut the mustard these days but you know, if you like your sock 32 packages, go for it.

**Dave Jones:** Knock yourself out. So there you go. I hope you like that look at the top five-ish jelly bean BJT bipolar junction transistors and the one little MOSFET jobby there.

**Dave Jones:** So I hope you found it interesting and yes, of course if I left out your favorite one, please leave it in the comments down below and there's nothing against if you've got your favorite one that you always use and because you know, it's you found it's the best for your particular applications and stuff like that, go for it.

**Dave Jones:** There's there's countless ones. So there's no right or wrong answer here but you know, I'm going to say like the jelly bean one that you must have is the 3904 3906 and then the other ones can be thrown around but I've just given you some basic examples of what I think are the jelly bean parts but if you've got something different, that's fine.

**Dave Jones:** I'm not going to argue. Anyway, thoughts and comments down below and as always if you like it, give it a big thumbs up and discuss on the EVBlog forum or in the comments or wherever and I remember I've got a merch and products available on the EVBlog store at EVBlog.store.

**Dave Jones:** That's the web address. Catch you next time.
