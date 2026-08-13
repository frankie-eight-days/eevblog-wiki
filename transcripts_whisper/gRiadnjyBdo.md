---
video_id: gRiadnjyBdo
title: EEVblog #553 - Mailbag
url: https://www.youtube.com/watch?v=gRiadnjyBdo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 14, "2": 37, "3": 57, "4": 86, "5": 105, "6": 123, "7": 143, "8": 162, "9": 182, "10": 202, "11": 218, "12": 238, "13": 259, "14": 273, "15": 289, "16": 306, "17": 324, "18": 348, "19": 363, "20": 378, "21": 398, "22": 412, "23": 428, "24": 448, "25": 468, "26": 484, "27": 502, "28": 516, "29": 530, "30": 546, "31": 568, "32": 584, "33": 604, "34": 626, "35": 644, "36": 656, "37": 672, "38": 690, "39": 708, "40": 730, "41": 750, "42": 764, "43": 778, "44": 792, "45": 804, "46": 818, "47": 834, "48": 850, "49": 866, "50": 886, "51": 902, "52": 920, "53": 940, "54": 962, "55": 980, "56": 994, "57": 1016, "58": 1032, "59": 1046, "60": 1064, "61": 1080, "62": 1100, "63": 1130, "64": 1146, "65": 1168, "66": 1182, "67": 1196, "68": 1208, "69": 1224, "70": 1240, "71": 1256, "72": 1274, "73": 1296, "74": 1320, "75": 1340, "76": 1356, "77": 1372, "78": 1400, "79": 1422, "80": 1438, "81": 1452, "82": 1472, "83": 1490, "84": 1506, "85": 1522, "86": 1540}
---

**Dave Jones:** Hi, welcome to everyone's favourite segment, Mailbag. Where people just send me stuff and I open it. Why? I don't know. Everyone seems to like it. I like it, so that's what we do. Mailbag. If you want to send me stuff, send it to

**Dave Jones:** ThatCrazyAussieBloke at P.O. Box 7949 Balcombe Hills, NSW 2153, Australia. Not Austria. Let's get into it. First suck of the Sav here, M. Welch from Mission, British Columbia in Canada. One of my favourite countries. It is a computer cable. So, no idea what sort of computer cable.

**Dave Jones:** Let's have a look. Ah, sorry, guilty of the zoom-in thing again. The problems of not having a video operator. Which, no, there's various reasons why I don't have someone operating the camera. It just wouldn't be worthwhile. Oi! We're in! Oh! Hang on. Yes!

**Dave Jones:** Ah! DIN 41612 extender cable. I think he clued me up that he was actually sending this. And it's an extender cable for, well, the DIN 41612 connector used in my HP DSA. So that is, and I think he wired this thing up, soldered this gender changer himself.

**Dave Jones:** He's got like a protection cap on there. And there you go, I think he went to the effort to solder that up. Like that. Brilliant. That's fantastic, that will allow me to test my HP DSA. And other people have sent in some extender cards as well.

**Dave Jones:** Let me get them and show you. And I think it's trackman44 on the EEVblog forum sending these to Sony. They've actually got Sony on them, so obviously used in some Sony product, I'm not exactly sure what. Extender cards for some sort of, you know, Sony product,

**Dave Jones:** but DIN 41612 connector, both the full-way and the half-way version. The half-way could be very important, because I've got a half-way version in the HP DSA for some of the lower boards in there, as you've seen in the previous video. So that will come in handy, I'll just have to like, you know, saw that down there.

**Dave Jones:** And unfortunately, the reason this board won't work off the bat is because, see some of the pins down there are shorted together on this power bus. Look at this, they've gone to a lot of effort, shorted those three pins there together, and then got these three huge traces going like that on that side.

**Dave Jones:** And unfortunately I have checked the pinout on the HP DSA, and those pins aren't shorted together. So this is like designed for like a Sony custom pinout. But all the other pins are all running separate traces all the way along there, except in some of these other ones, yeah, it's not just those first three over there,

**Dave Jones:** those ones there, there and there. So those first four columns of pins there are all commoned up. And unfortunately, to get this to work as an extender card, I'd have to get in there and break those connections all the way in there. And it's a bit messy, but this is the only half-width extender card I've got.

**Dave Jones:** So I'm going to have to rework this one to make it work on the analog board. So excellent, thank you very much trackman44. And you can see they've done the old solder tin coating on there to increase the current handling capacity of those boards.

**Dave Jones:** So I've got two of them, if I goof one up. So that's fantastic. And also, where is it? Ronald, I believe, sent me this one. And this one's a real beauty, it's from Worth Electronics. I believe you can, Roth Electronics, sorry. You can, I think you can still buy this thing.

**Dave Jones:** And this is a proper extender card. No shorted pins, they're all individual. The outer ones are larger for carrying, you know, larger currents. But you can tap off, you can break each individual wire, including that ground path as well. So they've got all the dip switches and pin headers as well,

**Dave Jones:** where you can tap signals off. I mean, that is just a fantastic, not only is it an extender board, but it's a breakout board as well. And I have actually tried this. I've put it in, powered up my DSA, and it seems to be doing the business,

**Dave Jones:** but I haven't gone any further than that. So thank you very much Ronald, that is awesome. And now I have a beautiful extender cable as well that I can use to extend out multiple boards. So I can use this one, I can use this one,

**Dave Jones:** plus I can extend out using that halfway one too. Beauty. Thank you very much guys. Yes, I will get back on to the HP DSA repair videos as soon as I have time. Next up, David Walsh from Kent in England. Fantastic, love England.

**Dave Jones:** Faulty electronics from Her Majesty's Royal Mail. It won't be Her Majesty much longer. When is she going to croak it really? How old is she? Sorry for all you royals out there, but gee, she's been hanging on for like ever. We have some faulty electronics.

**Dave Jones:** Oh, Sinclair! Woo-hoo! We have a Sinclair... Oh, is it the television? It's the Sinclair television. I've got a note! Hi Dave, I thought you and your viewers might be interested in this. It's a Sinclair portable flat screen TV from the early 80s. And yes, I am certainly interested in this

**Dave Jones:** because I have been looking at these on eBay. I was going to get one. So thank you very much, Dave. That saves me the effort to have to source my own. The CRT, as far as I know, the world's only flat screen TV that used a CRT.

**Dave Jones:** The CRT is very unusual. Only mad Professor Sir Clive Sinclair would produce something like this. It must have had his engineers pulling their hair out trying to make a CRT project around corners. Oh man, I can't wait to see inside this thing. Interestingly, in this model, the CRT is transparent

**Dave Jones:** so you can see the plates. Fantastic. The EHT voltage is 2.4 kilovolts which is produced by an overworked Zetex ZTX655 and lots of multipliers. That'll be interesting. The custom Ferranti IC is missing from this unit. Ah, bugger. I used it to repair another one

**Dave Jones:** which is now working as a peak-driven alarm clock. I should get out more. Yeah, we all should. Everyone watching the EEVblog should get out more. That's my advice. The lithium batteries only last about 15 ounce and cost a fortune which is one of the reasons

**Dave Jones:** the product failed. Keep up the good work. Thank you very much, Dave. Oh, schematic and service manual can be found here. Fantastic. I'll link it in down below. Thank you very much, Dave. That is awesome. And you can see there's our antenna on the top, by the way.

**Dave Jones:** And it's just one of those telescopic rod ones. It's interesting that you can really see right down inside that thing. It really is bizarre. I'm going to enjoy taking this sucker apart. There's just on-off and volume and tuning and that's it. You can see it going

**Dave Jones:** across. So obviously it's got some sort of some sort of trimmer cap slider type thing happening there. So that will be the next Teardown Tuesday. I'm sure. I'm going to keep everyone waiting because, well, that's what good performers do, don't they? Keep everyone wanting to watch

**Dave Jones:** Teardown Tuesday. So that will be coming up. Thank you very much, Dave. We have one from Po Yu Chen from Taiwan. Don't get too many from Taiwan, so thank you very much, Po Yu Chen. Some lovely flora there. Fantastic. So let's rip this sucker open.

**Dave Jones:** What have we got? Was there a description on the front? I forgot to look. It's flat and let's have a look. Yes, I'm working on Sunday. Yes, the joys of working for yourself. Hi Dave, greetings from Taiwan. I'm guessing I'm one of the very few

**Dave Jones:** viewers from your country. Yes! I'm not sure where Taiwan stands on the YouTube subscriber list, but I don't think it's up there anyway. All of you, they've been very helpful. E-student. Excellent. There's just lots of stuff they don't teach you in school. No kidding.

**Dave Jones:** I came to realize that to become a true electronic engineer, one has to learn so much stuff and I barely touch any of them. Well, I'm still barely touched anything after doing it for 30 years. Yeah, it took me 30 years and I still know nothing.

**Dave Jones:** Include the several photos I took. Oh, film photography is my other hobby. The tall building is Taipei 101, once the highest building in the world. Other shots I took at various trips. Oh, instead of postcards, I get photos. Brilliant. That's a lovely artistic shot actually of the Taipei

**Dave Jones:** 101 building. I presume it is. That's awesome. We have sunset, ducks, and... what is it? Some sort of flower with arty brocade effect happening there perhaps. And some lovely bush. Thank you very much. One from Daniel Wood from Focus Designs in Washington in the United States

**Dave Jones:** of America. We have a t-shirt, love t-shirts, and a paperweight. What's a Lichtenberg figure? I have no idea what a Lichtenberg figure is. So let's do it. Does this have one of these rip-stop things? One of these rip-open things? No, it doesn't. Okay, whatever.

**Dave Jones:** I'll just rip... Ah, there we go. We have our figure, and we have a nice t-shirt. Oh, it looks like a quick... one of the quick-dry ones. Extra small size. Excellent. I am small size by the way. And postcards! Woohoo! Ah, he's plugging

**Dave Jones:** his wares here. Look, it's a what looks like an electric unicycle. This is focusdesigns.com $17.95, I presume that's United States dollars. But doesn't that look spunky! Wow! Geez, I want one of those suckers. That looks really good. I wonder if it's like a

**Dave Jones:** Segway balance-y type thing or not. I guess we'll find out. Convenient. Only weighs 27 pounds. I don't know, what's that in kilos? Divided by 2.2. Foldable. Fits anywhere. Practical. Travel to work. Green technology. Used seamlessly with public transport. Yeah, you just pick the sucker up and go.

**Dave Jones:** It looks like it has just a maybe a quick... is that a quick release there for the seat height or something like that? So maybe you can just drop it down on public transport and pick it up? Does it have like a handle on the

**Dave Jones:** side? I guess you'd carry it by the seat, I guess. Geez, that's not a good look, is it? You know, let's carry it by that. Hmm. 12.5 miles an hour. Geez, what's that in kilometers an hour? Bloody miles. 30% inclines. That's pretty good.

**Dave Jones:** Up to 10 mile range and 325 pound capacity. That's a big person at 325 pounds. What am I, 170 pounds soaking wet or something like that? Thrilling ride. Beautiful design, advanced technology. Lean forward to go, lean back to stop. Okay, so it is like a Segway type

**Dave Jones:** thing. Sit or stand to ride. Wow! I want one! Yeah, a self-balancing unicycle. Oh man! I want one! Goes on my Christmas list. And I'll link to the page so you can see it in more detail, but there it is. It's a thing of beauty.

**Dave Jones:** It really looks very nice. Starting from $17.95. What are there? Options? I don't know. What sort of options would there be on this thing? No idea. Turn assist. Ooh, smart sense. Fantastic. Push back. Motion learning technology. Ooh, it learns. The SBU seamlessly interacts with the human body to ensure a smooth

**Dave Jones:** ride. Our motion learning technology, trademark, uses state-of-the-art sensors and thousands of calculations per second to actively learn your motion intent and deliver a unique ride experience. That is interesting from a, you know, a learning algorithmic point of view. It's not just one, it learns your individual

**Dave Jones:** technique, I guess, to better balance you. You know, out of the box it might not perform as well. You know, I'm sure he's going to jump in in the comments or on the forum and tell us all about it if you've got any questions, but this looks really

**Dave Jones:** jazzy. You know, I'd love to sort of, you know, if you're travelling to work on a train or something like that, carrying something like that, much more convenient than a bike. That is brilliant. Excellent work. Five reasons why you need this. Go running with your

**Dave Jones:** wife now. Well, that's a bit sexist, isn't it? 5% of my audience are female. They might go running with their husband or partner. Jeez, doesn't have to be men and a woman. Really explore your city. Inexpensive midlife crisis, that's what I'm going through.

**Dave Jones:** And it's got to be inexpensive, otherwise she who must be obeyed gets a bit upset. No parking fees. Brilliant. And you'll be the coolest guy on the block. I want to be the coolest guy on the block because I am totally uncool. Because I'm a nerd.

**Dave Jones:** Speaking of which, all the nerds here at work watch your videos regularly and usually greet each other with the famous Dave Jones. Hi. Pretty generic term. I wanted to send you a couple of shirts and a Lichtenberg figure just to say thanks for making us

**Dave Jones:** even nerdier. Thank you very much, Daniel. And the nerds here at Focus Designs. Excellent. How many people you got working there? How many of these things you sold? We need answers to questions. In Washington State, not Western Australia, of course. Hi to all my viewers in

**Dave Jones:** Western Australia and Washington State. I've been to both Washington State, Washington DC, which is totally different to Washington State, and I've been to Western Australia. Love them all. Beautiful shirt. Love it. This is the extra small one. And it's still a bit, you know,

**Dave Jones:** flappy. I do like tight-fitting t-shirts. What are you, Yanks? You know, extra small? Give me a break. Gave me a small one as well. Excellent for dagging around. I like the quick-dry fabric on these things. Self-balancing. New inside. Look at that. Beautiful. And the

**Dave Jones:** best part. Full frontal nerdity. Yeah! And here's this Lichtenberg figure. I'd never heard of this before. I googled it and sure enough, there is a wiki page for it. And what it is, is the electrical discharge, a high-voltage electrical discharge, on the surface or inside of an

**Dave Jones:** insulating material. In this case, like a, you know, some sort of polycarb type thing. It looks like it's happened right in the center there. So I'm not sure how they generate it. It's not like they've done it on the surface and, you know, and just joined

**Dave Jones:** these two together. So it looks like they've applied, you know, high voltage on here and it's penetrated through to the center. Presumably some sort of, you know, weaker point in it. I don't know how it actually forms like that, but look, it's like a fractal

**Dave Jones:** type pattern. And you see these in lightning strikes, you know, and the wiki page shows these sort of Lichtenberg type figure lines if you're on a person's body, if they've been struck by lightning and stuff like that. So really fascinating phenomenon. That is really

**Dave Jones:** awesome. Let me see if I can get a good close-up of that. There we go. Look at that. That's just terrific. Look at those branching lines off. It is very, very fractal, random, but very fractal-like. It is just brilliant. And just physical phenomena like

**Dave Jones:** this just really interests me. It is fantastic stuff. That's the penetration point on the top there, that's physically quite rough. And then it's penetrated into the center as we saw. Ah, this is beautiful. Thank you very much, Daniel. Please let us know where you actually

**Dave Jones:** got this thing from. Did you generate it yourself or did you buy it somewhere? So there it is looking into the side again. And it's not just, you know, it's fairly narrow and flat like that, but it is quite furry, I guess you could

**Dave Jones:** call the pattern inside there. But wow! That is just truly remarkable. Tell you what, that would make like a terrific, you know, pendant, jewellery type item. You know, if you get it encased in that polycarbonate like that, you could really polish and round

**Dave Jones:** that off and that's just a thing of beauty. One of the best mailbag items ever. And I find it also interesting to note that they haven't gone to the edges there. So I wonder if that is a deliberate phenomenon, because it doesn't look like

**Dave Jones:** this block has been like manufactured, as I said, like, you know, glued in some way or something like that. So it looks like they've got the block and then just applied the high voltage to it in some way and, but it hasn't gone

**Dave Jones:** out to the sides. And it is that square shape around there to match, you know, I'm assuming that if you had a round block of polycarbonate, you'd probably get a round pattern of these fractal branches coming off and then sort of dissipating, kind of

**Dave Jones:** thing, at the outer thing. So anyone who's done any research into these things, please let us know in the comments or on the forum. Last and hopefully not least from Derek White in Taylorville, IL, Illinois, I guess? USA. I can vaguely read that out.

**Dave Jones:** I think it says oscilloscope. 38, oh no, 15, 250, I don't know. Anyway, something oscilloscope. Ooh, it doesn't weigh a huge amount. It's a bit, you know, big. So what is it? Like a handheld scope or something like that? Only one way to find out.

**Dave Jones:** Crack it open. Let's have a look. Let's have a look. And... ta-da! Oscilloscope! Ooh! Ooh! Hey! Bit of a tech DMM oscilloscope! Wow! Check that out! I have never seen that before. Tektronix 213. Jeez, that's, you know, it's got the real old Tektronix

**Dave Jones:** symbol on it. And what have we got here? We've got input coupling. Look, it said common, milliamps, ohms, external trigger, power on off, external DC. Is that? Oh no, that's external DC trigger. Level slope. It's got no knobs on it. They've all vanished.

**Dave Jones:** But input coupling, that is weird. Horizontal magnification, trace rotate, vertical gain. Wow, this is really old school. I wonder what the age of this sucker is. There's the, oh, oh, oh! Hello! Jeez! Whoa, look at that! Isn't that gorgeous? Oh, I didn't see

**Dave Jones:** the side there, all I saw was the top like that and I thought it was some sort of plug-in or something like that, that did something, but oh! Oh! That is just gorgeous! Look at that! I wonder if it works. I'm sure there's a note in

**Dave Jones:** there. Let's have a look. After watching episode 430, the Fluke 91 scope meter teardown, I thought I would send you an analog scope meter. In quote marks that I've had laying around. It's a Tektronix 213. Got it on eBay a couple of years ago and never used it.

**Dave Jones:** It's powered on before shipping, but make sure it still works. It might be interesting for a teardown to see some old school and high tech for the era, I'm sure it was. Get a date code on this sucker and we'll tear it down.

**Dave Jones:** Obviously not. I think we've been going for a while here on the mail bank so once again, as always in show business, I'll keep people commenting more and this will be a teardown Tuesday item along with our Sinclair TV. So we've got two

**Dave Jones:** CRT items to teardown but oh, thank you very much Derek. Look at that, it's just beautiful! Look at this! Ah! So cute! It's got a tilt stand and all the controls on the side and look at that. I wonder what the switching arrangement is for that.

**Dave Jones:** It'd be you know, a multi-ganged switch of course, so I'd expect to see you know, a really sort of impressive bit of gang switching, probably direct PCB mount, I'd say. You're not going to piss away space in this thing with wiring and things like that.

**Dave Jones:** I reckon this is going to be that'd be my guess anyway or very closely coupled. And look! They've got the ganged mechanism on the switches there. That's just old school pornographic. It really is. And here we go, we're going to power it up.

**Dave Jones:** I've got my step-down transformer, 110 volt step-down, because this is, looks like it's 110 volt powered. It does look like it says it accepts 45 to 62 hertz there so it'll handle the 50 hertz no problems at all. So here we go. Let's stoke this thing up and

**Dave Jones:** hopefully the magic smoke won't escape from this really cute Hey! Look! We have a trace! Beautiful! Oh. Hang on. Oh no, because we're in ohms functionality. Hang on. DMM? RM? Huh? What's RM? I don't know. Oh, look at that. That is just beautiful.

**Dave Jones:** They've got the readout as digits. Oh! That's fantastic! Is that the vertical scale? I'm not sure. 5 milli, 10 milli, you know 10, 100, it's not going to go up to 100 volts per division, is it? That'd be absolutely enormous if it does, because there's your horizontal

**Dave Jones:** knob down here, which is going to have no effect on your DMM, of course. Look at the volts. Look at that! And it's got current, it's got resistance, we can whack some leads in there and have a look. How do we get our

**Dave Jones:** scope out? Okay, I didn't read it. Geez, I should have read the manual. There we go. Where's our, oh, there's our sweep down the bottom, so it looks like we have to vertical gain, oh, there we go! There we go, there's our oscilloscope sweep.

**Dave Jones:** This is beautiful! Oh! Still works! Trace position, there we go. No worries at all. Wow, this thing is so small and light too. Oh, no. There's the intensity. It's really, there's no burning on it by the looks of it, so it works really

**Dave Jones:** well. Horizontal magnification, slope, power on off button. There it is. And if anything, I'd say that's slightly out of focus there, but you know, it's still workable, there's a focus adjustment on the side, got to get a trimmer right in there to do that, but let's, well,

**Dave Jones:** let's whack it up to my resistance box and see if we can measure anything. And look at that! Not too far off whatsoever for my 10k resistance standard here. And if I whack it around on my 1k standard, and it's got multiple positions here,

**Dave Jones:** you can see it, there we go, so let's whack it around to 1k. Look at that! That's probably still within spec, I'm not sure what the spec of this sucker is, but that is just hunky-dory, I'm happy with that. And that looks like it works a

**Dave Jones:** treat as well! Look at that! And just displaying a simple 1kHz sine wave on that sucker. And that, it's not going to trigger at the higher magnitudes, let me, oh, yeah, it's a bit touchy on the trigger there, but I like it, this is just,

**Dave Jones:** oh, it's just beautiful! Brings a tear to the eye, it really does. There we go, that triggers a bit better now on the higher end stuff. It's on auto-triggering at the moment, so, but it's, you know, it's not a magic auto-trigger, that's for sure, but

**Dave Jones:** still, that's really beautiful. I don't even know the bandwidth of this thing! I wonder what the specs are! It turns out it's a 1MHz unit, so, you know, it's usable, especially for its day. It was $2100 list price for this thing back in its day.

**Dave Jones:** I'm still not sure of the vintage, it didn't have that in the specs there at all, but gee, I don't know, what is it, late 70s? Maybe, something like that? Oh, beautiful! And it still works a treat! And yes, that is 100 volts per

**Dave Jones:** division. Fantastic! Well, thank you very much Derek! The mail bag just gets cooler and cooler! I love it! And I'll definitely have to use this in some videos too, just because I can! Why not? It's just absolutely gorgeous. And there'll be a Teardown

**Dave Jones:** Tuesday coming up, bet your bottom dollar! Catch you next time! Thanks for watching!
