---
video_id: UESc7ms4efo
title: EEVblog #588 - How To Do PCB Production Testing
url: https://www.youtube.com/watch?v=UESc7ms4efo
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 38, "3": 54, "4": 63, "5": 79, "6": 89, "7": 108, "8": 116, "9": 126, "10": 145, "11": 154, "12": 170, "13": 185, "14": 196, "15": 209, "16": 222, "17": 233, "18": 255, "19": 272, "20": 286, "21": 294, "22": 305, "23": 322, "24": 332, "25": 343, "26": 355, "27": 364, "28": 381, "29": 393, "30": 407, "31": 430, "32": 441, "33": 497, "34": 513, "35": 528, "36": 537, "37": 548, "38": 560, "39": 573, "40": 585, "41": 609, "42": 620, "43": 631, "44": 640, "45": 654, "46": 663, "47": 681, "48": 689, "49": 709, "50": 729, "51": 758, "52": 769, "53": 782, "54": 797, "55": 816, "56": 828, "57": 838, "58": 847, "59": 857}
---

**Dave Jones:** Just a very quick video showing you testing of my new production microcurrent PCB panels because it's actually quite important. Up until now, I've been testing these myself, but I'm going to manufacture another 1,800 of these and well, testing them all myself not that great even though it's very quick as you'll see here no doubt.

**Dave Jones:** So, I'm going to test five panels here today, 50 boards total to get a reasonably, you know, accurate average time of how long it like this. These are Here's my new production panel assembled by a company called Soldering Co.

**Dave Jones:** Up the coast here from Sydney. They're a couple hours up the coast so they are local and they've been assembling my boards for me doing a good job, but I'm also going to get them to do the testing as well cuz that's very common in the industry.

**Dave Jones:** I'm not going to test 1,800 myself. I promised I'd test a couple of hundred and that's what I've done, but these ones Yeah, I'm going to get them to do the production testing.

**Dave Jones:** So, that's very common in the industry to actually get your assembler to do that. It just makes sense and almost all assemblers will do, you know, production testing. They might even do a whole what's called a turnkey thing where they order all your parts, they do your assembly, they do your testing, they do your packing, everything else.

**Dave Jones:** In fact, they're doing more than the testing. They'll be doing the packing as well. You know, wrapping them up and putting them in the things and all I've got to do is slap on the labels and ship them.

**Dave Jones:** So, beauty. Now, what this entails is that I need to write some testing documentation which I haven't done yet. What I'm going to do today is test these five panels to get an average time and that's important cuz I have to know cuz an assembler will typically charge you, you know, per hour of assembly time.

**Dave Jones:** So, if it if I can test all five of these in an hour, well, you know, it's only going to cost me, you know, a few tens of dollars to get these all tested.

**Dave Jones:** So, you're going to pay by the hour. So, I just want an accurate indication and I'll show you some of my test jigs. I've got very quickly I might go into more detail on this.

**Dave Jones:** But, anyway, let's give it a go. Now, there are of course many different ways to skin this testing cat and it depends on you know how much effort you want to put into it, how many you're manufacturing or which assembler you're using or you know all sorts of stuff.

**Dave Jones:** And well, you know, look I'm not manufacturing tens of thousands or hundreds of thousands of these. I'm only manufacturing you know 1,800 or just a couple of thousand really.

**Dave Jones:** So, it doesn't warrant full big bed of nails tested. If I was doing this for a company, I might automate it more than this. For example, like you would do a big bed of nails with little pogo pins which come down, contact with some of the pads and power up the boards and things like that.

**Dave Jones:** And that's one of the things with this. It actually takes you want to minimize every operation possible when you're doing production testing like this. For example, if I have to insert a battery, a coin cell battery into every one of these, that takes time.

**Dave Jones:** And then because I'm not allowed to ship the coin cell batteries, I've just got to take those back out anyway. So, it makes sense to actually have a test jig which powers these up.

**Dave Jones:** Now, I've done a video on this before. I've actually added power routing traces around the outside of my panel coming to this test connector on the side. And well, this allows me to power up all the boards at once with a little battery box like this.

**Dave Jones:** There's three AAA batteries in here and that just powers up. There you go. LEDs are all coming on. So, all these ones actually work and I can switch individual ones off of course and stuff like that.

**Dave Jones:** But, there you go. That that you know saves a whole ton of time and once I and I'll test them in the panel like this and once I've done that, then all I've got to do is chop them out and bang, wrap them up and they're ready to go.

**Dave Jones:** Or my assembler is going to do that anyway. And to do this testing, as I said, could have done a bed of nails tester, some automated jig. I did allow for I did bring the outputs of all of these out to this card edge connector, but in the end I decided really essentially wasn't worth it because I had to plug in the test current anyway.

**Dave Jones:** I didn't bring out didn't have enough room to route out the test current uh well, the input current traces on each board as well. Um so, yeah, that would have had to have been done with a big bed of nails thing and it would have had to have automated switching because they're all ground reference.

**Dave Jones:** I've mentioned this before. The outputs are all ground reference, so I'd need isolated current generators for each one. Gets really, really messy. And yeah, if I was working at a company as I've done I've produced countless number of these uh production test jigs and things like that.

**Dave Jones:** And yeah, I might go to more town, you know, I might go to town on it cuz I might have, you know, a month to set up a test system or something like that.

**Dave Jones:** So, yeah, here it doesn't really warrant it. So, all I'm going to do is power them all up and I figure that well, I had to plug them in anyway.

**Dave Jones:** I had to plug in the current source, so why not do the monitoring as well. So, instead of using this, I've now got myself a little uh microcurrent uh test jig board with uh basically there's a there's a power LED on there and there's a offset uh thing to measure the output offset voltage was within spec.

**Dave Jones:** And then there's an in spec LED there with the uh with a window uh comparator on that. So, it just uh and this is uh very accurate. It's all trimmed and ready to go.

**Dave Jones:** So, I can plug that into here like this and then I can plug my current source into here and bang, I can just go around boom boom boom boom boom like that.

**Dave Jones:** It's literally that easy. It might take, you know, 10 or 20 seconds, you know, 20 seconds maybe, 30 seconds to go around and test all boards. Certainly less than a minute.

**Dave Jones:** So, all I have to do is plug in my battery box in the top there. Sorry, I've got it on this orientation so that you'll be able to actually see the LEDs on this light up.

**Dave Jones:** I've got my precision, in this case it's the 1 milliamp current source going into there. So, it feeds the precision 1 milliamp into there and I've got this all powered up and all I've got to do is well, ensure that the switches are all set to the to the microamp position because I'm getting 1 volt out.

**Dave Jones:** So, I'm feeding 1 milliamp, I get 1 volt out of here and my window detector is designed to detect that 1 volt plus minus the .05 spec. So, I simply plug it in there and bang, there it is.

**Dave Jones:** My green light comes on and I just go along and test them like that. That is how quick it is. Awesome. And of course, depending on which turns out to be the most efficient way to do it, usually batch is.

**Dave Jones:** So, if you had five panels like this, I would go along, I'd set all these switches to one position on all of them and then go along and then swap the panel and do the next one with the same current source like this and then so do them all on the nanoamp range, do them all on the microamp range and then go along and do them all on the milliamp range as well.

**Dave Jones:** But, it depends. I can have, you know, build multiple versions of these so I can just do the one panel like this, go along 10 times, test, get the next one, plug change all the switches, get the next one, boom, boom, boom.

**Dave Jones:** But, as you can see, it's going to be really, really quick. There's no test leads or anything else mucking around required. Now, unfortunately, I haven't actually built up my 1 amp precision current source yet so I'm going to have to use external calibrated external power supply.

**Dave Jones:** So there you go. That was just under 50 minutes to test all three ranges on every board on all five panels for all 50 boards. So that's only calculates out to about 17.4 seconds per PCB tested.

**Dave Jones:** And that includes, you know, switching the ranges, plugging the things on, around, maybe doing the odd measure manual check and things like that. That's very impressive. Rounded up to, you know, 20 or 25 seconds or something like that.

**Dave Jones:** And you know, that's bingo. You've got your average time taken to test each board. And yes, there were a couple of failures. This one for example, I marked them up here.

**Dave Jones:** This one just failed on the amps range. I checked it, it was getting no output. So let's have a look at that and see if we can troubleshoot that one.

**Dave Jones:** Now let's take a look at the board here. And because it only failed on the amps range, but passed the other ranges, that tells me that basically there's likely something wrong with the current shunt down here.

**Dave Jones:** Because if the other ranges passed, that means the two amplifiers in here are working. The gains of those are spot on. My split supply generator for the power supply for the battery is working.

**Dave Jones:** You know, everything's just fine. So it's got to be that sucker down there. Let me see if I can get a Let's see if we can uh get close into there.

**Dave Jones:** Hello. Hello. Let me get a better angle on that. And there you go. Bingo. Look at that. There's our culprit. It hasn't reflowed. One of them slightly You know, slightly under temperature just cuz this is a fairly large you know, large-ish mass uh thermal component uh especially compared to the other ones with a big large trace coming off here.

**Dave Jones:** It just didn't reach enough reflow temp or the flux didn't clean the uh joint. The flux that's embedded in the solder paste didn't clean the joint properly or something like that.

**Dave Jones:** You know, so there you go. Too easy. I can touch that up and it'll work a treat. And then likewise, I've got another panel with instead of the amps instead uh well, the milliamps.

**Dave Jones:** It's actually the microamps range, but I mark it as the 1 milliamp test current. So, let's uh take a look at that. Once again, it passed on the other ranges.

**Dave Jones:** So, we go down and we have a look at the culprits down in here. Likely to be No, that looks all right. There's the uh There's the shunt for that one.

**Dave Jones:** That looks just fine to me. So, it's not that. So, that's rather strange. Uh let me double-check that. No, that's actually okay. So, I don't know what's going on there.

**Dave Jones:** The other thing it could be is a dicky connection. Oh, hello. Yeah, okay. Not sure if you can see that, but Yeah, look. So, yeah. The assembler hasn't screwed down that screw tight enough on that jack.

**Dave Jones:** There you go. One of them was loose. So, the yeah, Murphy's law there. That just intermittently made uh contact there and just happened to fail on the milliamps range.

**Dave Jones:** Oops. These sort of things happen when you start introducing that human process of actually assembling these things. I mean, you know, surface mount boards as far as reflow soldering goes, once you got your thermal profile down right, you're soldering all your parts on and stuff like that, you know, you can get near, you know, almost 100% yield, fantastic.

**Dave Jones:** But, you know, hey, the operator's not paying attention, they don't screw up that one tight enough. Meh. So, there you have it. That was quite an eye-opener, you know, because I I knew it was fairly quick, but, you know, it's sub 20 seconds per board for all three Rangers and around and plugging things and moving panels around and swapping them.

**Dave Jones:** Very impressive, 15 minutes 450. That's like, you know, 200 better than 200 units an hour. Fantastic. And if you divide the, you know, hourly cost of one of the assembly line workers, which is what they typically charge at plus some, you know, some overhead on that, then really, you know, it doesn't add much cost at all, but it's important to get your production tests down to a suitable

**Dave Jones:** level. And yeah, I can make this one even quicker with some sort of automated bed of nails thing, but, you know, really, it's it's a matter of return on your time and money investment there, and really, it's not worth it.

**Dave Jones:** I'm more than happy at the testing time for these things. And it's probably going to take the same amount of time again to actually cut each individual board out.

**Dave Jones:** You know, it might be another 10 seconds or something to go around and and trim these things out by hand. Yeah, you could probably automate that process as well, and you would if you're manufacturing hundreds of thousands of these things, or you'd figure out a better way to do it or something like that.

**Dave Jones:** But, yeah, as I said, there's more than one way to skin a cat, and then you're going to wrap the thing. So, really, you know, a lot of people put time and effort into trying, you know, automate their bed of nails uh test setup for their board when that could be might be swamped by some other manual process of actually packing and things like that.

**Dave Jones:** So, really, it's not all about the testing. I've got to now cut these out and I've got to wrap them up in their antistatic bubble wrap and and then uh whack them in the padded envelopes and all that stuff.

**Dave Jones:** It's going to take more time than what it took to actually test these things. So, there you go. I hope you enjoyed that little quick look at these uh production test panels.

**Dave Jones:** And if you like the video, please give it a big thumbs up. And as always, the EEblog forum is the place to discuss it. It's linked in somewhere down below.

**Dave Jones:** Catch you next time. Yep, it actually took longer to cut up the bubble wrap and wrap the boards than it did to test them. Go figure. And yep, you guessed it.

**Dave Jones:** Packing takes even longer again. Ah.
