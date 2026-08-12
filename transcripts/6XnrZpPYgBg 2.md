---
video_id: 6XnrZpPYgBg
title: EEVblog 1496 - Winning Mailbag
url: https://www.youtube.com/watch?v=6XnrZpPYgBg
source: youtube-asr
timestamps: {"0": 3, "1": 25, "2": 41, "3": 62, "4": 81, "5": 95, "6": 120, "7": 137, "8": 154, "9": 171, "10": 188, "11": 204, "12": 218, "13": 254, "14": 287, "15": 299, "16": 324, "17": 359, "18": 375, "19": 392, "20": 416, "21": 438, "22": 461, "23": 480, "24": 495, "25": 517, "26": 550, "27": 578, "28": 596, "29": 621, "30": 641, "31": 679, "32": 700, "33": 718, "34": 751, "35": 772, "36": 799, "37": 828, "38": 862, "39": 886, "40": 901, "41": 920, "42": 952, "43": 976, "44": 990, "45": 1006, "46": 1024, "47": 1058, "48": 1078, "49": 1113, "50": 1138, "51": 1158, "52": 1188, "53": 1220, "54": 1237, "55": 1255, "56": 1283, "57": 1308, "58": 1345, "59": 1363, "60": 1376, "61": 1406, "62": 1435, "63": 1472, "64": 1501, "65": 1536, "66": 1557, "67": 1576, "68": 1605, "69": 1626, "70": 1657, "71": 1679, "72": 1707, "73": 1729, "74": 1749, "75": 1774, "76": 1791, "77": 1805, "78": 1822, "79": 1850, "80": 1875, "81": 1892, "82": 1907, "83": 1932, "84": 1959, "85": 1992, "86": 2018, "87": 2036, "88": 2055, "89": 2071, "90": 2091, "91": 2114, "92": 2140, "93": 2159, "94": 2180, "95": 2204, "96": 2234, "97": 2246, "98": 2281, "99": 2314, "100": 2342, "101": 2375, "102": 2395, "103": 2411, "104": 2440, "105": 2459, "106": 2478, "107": 2503, "108": 2522, "109": 2545, "110": 2572, "111": 2598, "112": 2620, "113": 2649, "114": 2676, "115": 2701, "116": 2742, "117": 2768, "118": 2799, "119": 2812, "120": 2837, "121": 2864, "122": 2889, "123": 2911, "124": 2938, "125": 2965, "126": 2985, "127": 3009, "128": 3021, "129": 3043, "130": 3061, "131": 3096, "132": 3117}
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. We have a special guest who's dropping something off and picking up. Say hi to Josh. Hi. Well, he's if you've seen the winner of the $5 J car Digitech special scope and he's local here in Sydney. He's your 13?

**Dave Jones:** Yeah. 13 and he's got his own lab and making his own stuff and he's starting to sell boards for the new framework laptop. Laptop. So, what boards? You've got like several different boards. Um well the one I'm about to sell is a UART board.

**Dave Jones:** Yeah. Um I have an ethernet one which failed and then the company came out with one so I stopped working on that. I have a serial adapter for networking gear so it has a RJ45 port along with a basic serial adapter to a DB9 connector.

**Dave Jones:** And you've got pre-orders for these? Uh not quite. I have I have interest. Yep. Uh I think seven or eight people for the UART one specifically. Oh. But otherwise I'm going pretty well. Excellent. And you and you're going to make these in-house by hand?

**Dave Jones:** Yep. Yep. Awesome. I'll link it in down there'll be a link. I presume you'll give me a link to put down below so where people can follow this. starting to get set up. Cool. Well, we'll try and put the link down below. Anyway, awesome. Well done.

**Dave Jones:** Framework, what's what's the interface? What's the framework It's just both standard USB-C. Oh, it's just USB-C. Okay, so your little adapter boards convert USB-C into anything. Whatever. Yeah. Nice. Awesome. Is there like a like a I haven't looked at it really the framework module? Is it like a is it like a defined space or volume of is it like a plug-in thing or is it It's It's It's internal, isn't it?

**Dave Jones:** Is it Well, you can swap them out. Hot swap. Okay. And they're the length of them is You can't change that, but the um you can extend out the laptop a bit. Got it along. Yeah. Nice. Awesome. Well, anyway, here it is, the scope. Ta-da!

**Dave Jones:** You haven't got a scope. How How are you designing these boards without a scope? Same Same way I used to. Well, most time designs are quite simple, and the data sheet covers Yep, everything, and most time my designs, as soon as I assemble them, they work.

**Dave Jones:** Oh, I hope they I hope your next one fails. Sorry, but seriously, I hope it fails so that you can troubleshoot it with your new scope. And uh yeah. And then you learn a lot more if your stuff fails. If it works first time, it's like, "Yeah, it's okay. You've learned some stuff." But if it fails, then you Yep. That's where you really learn.

**Dave Jones:** My ethernet one, I messed up on the differential pairing. Yeah. And I I had these capacitors and resistors for um the USB signals, and I just removed them, so it went back down to USB 2, and it worked fine.

**Dave Jones:** Nice. Oh, okay. So, it was a signal integrity thing, you think? Oh, okay. Well, that's even this is not going to help with that, unfortunately. It's too higher frequency stuff, but yeah. Nice that you figured that out. And yeah. The job's back down. Awesome work. Anyway, thank you. So, enjoy the scope.

**Dave Jones:** Yeah. Fantastic. It's got some probes with it as well. So, yep. And you're dropping this off. Where did you get this from? Um my dad's lab. Your dad's lab. What does your dad do without giving away too much?

**Dave Jones:** Industr- He's a industrial chemist. Right. All right. Okay. So, it came from an industrial chemistry lab. Yeah. Well, Mrs. EVBlog might know. But anyway, yeah, this is a It's quite hefty. It's a It's a Mettler Toledo made by Wag. It's got two big outputs here, high voltage outputs, and it's what 7 kV or something? 6.6.7 kV at 5 mA. Except it's European, so it's got instead of the decimal point it's got the comma.

**Dave Jones:** Weird Europeans. Anyway, so So, do you know know if this works or not? Um I haven't plugged it in, but I did take a quick look inside and it's not It definitely looks like something has happened. Oh, okay. All right, something's happened. All right, the magic smoke escaped. All right, so I I looks like some sort of Yeah, it generates high voltage. Probably some ionizer thing, something like that, or some other thing where when you generate high voltage, you can actually it actually attracts particles. That's how ionizers

**Dave Jones:** work. And And that's how the new space suits work, by the way. They're going back to the moon. Do you know this? Little factoid. They're going back to the moon, but the space suits actually have embedded conductive fibers in them.

**Dave Jones:** So that dust on the moon is such a problem that they have to have the embedded conductive fibers and they charge themselves up to I I don't know what you know, several kV or something. And it actually it actually repels the dust. So it stops the dust getting on them. So the new space suits have They're not going to lug around one of these babies, but yeah, anyway. Little factoid there. So there you go. Anyway, thanks thanks for dropping that off.

**Dave Jones:** We'll do a 2-minute teardown. Well, I'll do it in several days when I'll shoot a mailbag video. So we're just shooting this while you happen to be here picking this up. So enjoy. Thanks, Ross. Thank you. All right, let's crack it open. Here it is, 6.7 kV, 5 mA, and there's the huge triaxial app Well, they're not triaxial but you know, like big high voltage insulated coax type connector outputs like that. Of course, it's going to be a differential thing like this. That's why you know,

**Dave Jones:** both of these are mains earth connected by the big ass stud on the side and that's it a switch and it just generates a high voltage that they use for some ionizing gadget, I guess in the in the lab.

**Dave Jones:** What a day code on the bottom there? 2017. It's got 6.7 here. So I assume that's 6.7 kilovolts. I assume you can get like different voltage models. I got the screws off. How does There we go. Oh, we're we're in. There you go.

**Dave Jones:** Just whoa. Big ass transformer and wow, that's some crusty rust. Yeah, I can well, you know, you'd expect it because it's but it's what ionized off all the rust from the transformer. I don't know but but jeez, it's basically just a transformer and that's it.

**Dave Jones:** There's your primary coil and that's your secondary there and that's that's completely sealed on the output. So yeah, we won't be able to I mean, I don't think we can take that cap off. Can we? Man, that's crusty as. Wow.

**Dave Jones:** I don't know if that's a natural consequence of the high voltage and like ionizing the air because when you ionize the air, particles like stick to things and that's the whole idea. You can get like, you know, the electrostatic air filtration systems when you ionize the particle the dust particles in the air, they cling to the fabric of your filter.

**Dave Jones:** Actually, I just changed my lab filter the other day. You've seen this. This is my Blueair jobbie. God, the filters are expensive. And you can see how dirty that is and it attracts all this dust. And mine is an electrostatic model. So, it does actually ionize the particles in there.

**Dave Jones:** And yeah, and they can and they cling to the fabric when they're ionized. And in the bottom of that, we've just got a big ass 1K power resistor there. I'm not sure why. It's not really across the output.

**Dave Jones:** It's not like discharging the output or something like that. Sure, why do we need a load there? Jeez, check out the rust on the earth connection. Look at it. Wow. Yep, this is all chemistry, folks. Um There's a reason why that has accumulated so much rust. I'll leave that up to the chemists, but oh jeez.

**Dave Jones:** That's terrible, Muriel. But I don't know. Like has this been used in an atmosphere that causes rust like this? But it's obviously, I think it's been accelerated by the by the high voltage in this sucker. Anyway, if you know precisely, then please leave it in the comments down below. But yeah, I don't know if there's anything in here. Is there like an output filter there or whatever? I I doubt. I think it's just a direct like step up transformer. Really?

**Dave Jones:** I think that's all there is to it. We've got a couple of caps down in there. That could be just some mains input filtering. And that's maybe what the resistor is to discharge those caps, maybe. But jeez, that seems overkill. Yeah, so I'm not going to try and power this up cuz I don't think I have a high voltage probe that goes high enough for that to see the waveform. And certainly, I don't know how I'd probe down in there. I mean, jeez, these things are deep. I mean, that's that's

**Dave Jones:** the cap that came with it. Hard time getting that out, but yeah, I'm interesting. Let us know if you've ever used one of these and for what purpose. So, thank you very much, Josh, for bringing that in and I hope you enjoy your silly scope.

**Dave Jones:** I've actually filming this many days later and he's already reported a few issues with the scope. Nothing major, but uh yeah, he's certainly giving it a workout. Hello to all my viewers in Norway. I kid you not, this one's from Thor. Yes, Thor, who comes from Bloomenholm in Norway. Hello to all my viewers in Bloomenholm.

**Dave Jones:** So, let's have a look. What? I was a bit sitting up tongue at the right angle there. This one contains one of my favorite items and hopefully one of yours, too. Let's have a squeeze. It is protected. I see the name, WHICH I I WOW! IT'S NO, IT CAN'T BE. It can't be.

**Dave Jones:** There's no note in here. Surely this is not a Casio VI-9850 9850GB. Or is that the um No, Casio TV interface. Ooh, is this one of these like overhead projector ones? But What weighs a ton? What? PAL? It's PAL output. This This looks new in box. I I know they make the I've got one of the Casio projection ones. What the heck? What the heck is this? It's a foldery stand thing.

**Dave Jones:** I don't get it. Um gee, LOOK AT THAT. THICK AS. LOOK AT THAT. LOOK AT THE MANUAL. IT'S ALL IN ENGLISH, TOO. WOW, THAT'S A thick ass user a Um here it is. This is new in box. Um, must have picked it up. Casio calculator TV interface.

**Dave Jones:** It doesn't say it. Yeah. Wow. I had no idea such a thing existed. Look at that. So, it's a regular, you know, 9850 calculator or whatever it is. And um, but they've added a TV interface with an output.

**Dave Jones:** With a composite output. I didn't know such a thing existed. This pairing up never go. Well, this thing's so big and long, I have trouble fitting in the frame. Luckily, this is wide screen. Check it out. Yes, it is one of these color uh jobbies. It's the color model. And of course, the 9850 is incredibly popular uh calculator in um schools and stuff like that. And it's got a composite video output. Obviously, for educational use, it makes sense. I mean, you can get the overhead projector one, uh which

**Dave Jones:** I've got. So, why not have one of these? And yes, you've seen this before, which is the overhead uh projector version where you For those kiddies who don't know, I we used to have overhead projectors, which you put a uh a film sheet on and it would uh shine light through and then it go through a big reflector and magnifier and put it up on the uh wall at school.

**Dave Jones:** And that's how the teacher could, you know, magnify and display things um to the students. But now, it's all digital, you know. So, you plug it in digitally. So, it makes sense to uh transition from the overhead uh projector model to, I guess, composite. I mean, nowadays, it'd be HDMI, but jeez, that'd uh that'd really chew some power, wouldn't it? I mean, this one obviously needs a separate adapter for the um output. I mean, it's just working from the uh four batteries at the moment. There you go,

**Dave Jones:** 4.8 W. Oh, jeez. So, that's that's chewing the juice, I guess. So, if you turn that on. Anyway, the uh colors are pretty piss-poor on these. But, I guess the whole idea is that, you know, color just does add some value in there. But, you know, if you're just doing normal operations, then it's just your regular LCD and your regular contrast, which isn't too shabby at all. Okay, let's just do some current consumption measurements.

**Dave Jones:** That's a standby power. It's just charging up the caps there. Switch it on. There you go. In normal operation, 2.4 milliamps. That's with the projection off. Let's do it with the projector on. Yeah, I think the projector my the projector the well, you know, the the projector output. Obviously, this is designed to go composite output is designed to go into a wall-mounted video projector, which of course displays the screen out there. So, yeah, I think you need the uh plug pack for that cuz uh 2 milliamps uh consumption,

**Dave Jones:** that'd be what you'd get uh just for the calculator itself. Is the adapter? It's got one of those weird ass plugs on it. Uh so, I'll have to find an adapter for that. But, uh there you go. Made in Japan. All the best stuff's made in Japan. 4.5 watts. It's got a mysterious sync button there. I don't know. Is that like you put a a pin through and push it? Um I I don't know. I even RTFM'd. Telefunken.

**Dave Jones:** Built by born perfectionists. I love it. And well, there you go. It works. Um doesn't that look pretty groovy? But, it's not uh full frame. So, I don't know what the deal is there. And I can switch that off.

**Dave Jones:** And if we switch it on, how long Yeah? Yeah, it just pops up. And if we switch the calculator off, it stays on. I've switched the calculator off. And yeah, I can't operate it. So, I switch calculator on, and now I can operate it.

**Dave Jones:** There you go. Hey, groovy, huh? And wow, there you go. Check that out. Look at the huge board they've got on there for that video processing. Obviously, this is a standard 9850 calculator up here. We tore one down one before, but yeah, that's all that's all bog standard stuff. I love the battery contacts flapping around in the breeze up here. Nice, that goes into the plastic work. And we've got a ribbon cable also going over here to the slide on off uh button on the top. And

**Dave Jones:** interestingly, that says fuse. So, I TO-92 fuse, anyone? Well, sure enough, that's an ICPN10 fuse. And I've found a data sheet that has like ROM and branding as well. So, yeah, there you go. I can't say I've seen a seen a fuse in a TO-92 package.

**Dave Jones:** Interesting. I love how they going for that Japanese tradition of just uh saying, "Ah, bugger it, we don't need a connector. Just a wire straight through." They've used a connector over to here just to you know, aid aid in assembly and stuff like that.

**Dave Jones:** But yeah, just just solder pads on the bottom. Yeah, no worries. And you'll notice that the red and yellow wires here, these are just ground connections going to this grounding pad here and over to here. So, not through the connector. So, that's an afterthought.

**Dave Jones:** The blue one as well. The blue one's ground, too. So, they had some they had some even layout or even EMI issues there and they needed join the grounds. I don't know. Well, absolutely no surprises for finding a couple of Sony jobbies in there.

**Dave Jones:** So, there you go, custom. And then it looks like I'll put a high-res photo over on my Flickr account as always. And you can go for your life, but that's interesting. What's that NEC part there? Just I wasn't expecting something that denser footprint. It almost looks like it's you know, it's a flash memory or something. Sure enough, that's a 256 K bit static RAM. So, they're using that to bitmap all the stuff. So, they transfer it into that and then yeah, that's the that holds the bitmap

**Dave Jones:** image for the screen. But, that didn't make sense based on the pin count here to actually control that. It turns out we do have the data sheet for this. It's a video sync thingy. I'll put it up here briefly. But, anyway, thought I'd have a sneaky peek on the bottom. I thought there was more to it and my hunch was right.

**Dave Jones:** Tada! There you go. And Altera Max FPGA on the bottom. And that's how they're doing it. Interesting. I didn't see that one coming. So, there you go. Yeah, going old school implementing all that in the Altera Max. And obviously, you know, back in those days, they didn't have a huge amount of internal memory. So, they're obviously using the external memory to map that. So, that's an interesting design how they've taken just the basic 9850 calculator, made it into a thicker case and put the engineered a big

**Dave Jones:** you know, output and then bodged it into essentially the existing 98 50 calculator. Like bodged the data output and then they use an FPGA to process that, bitmap it into the memory and then they shoot it out. So, yeah. And and then they put put it in a larger case and extend it up and put a on-off switch and external power and stuff and Bob's your uncle. Neat, huh? I don't think they sell, you know, these in huge volumes.

**Dave Jones:** Certainly not like they'd sell to the kiddies in the class, you know, it's it's got to be like two orders of magnitude. So, there you have it. That's a great example of how you would like repurpose an existing a for a different or a slight in this case a slightly different market. The teacher market instead of the student market.

**Dave Jones:** And that's how you would integrate it. That's how I'd probably budget together too instead of like designing the whole thing from scratch or something like that. They took all you know all the existing plastics and everything probably and just like and just you know did a new bottom shell and stuff and they just re-kept the existing board and then budged it in by the looks of it and then like made that into I another calculator line specifically aimed at teachers. So thank you for sending that

**Dave Jones:** one in. That was that was brilliant. It seems these are relatively rare out there you know so nice addition to the calculator museum. Thank you very much Jayden from Belmont in Western Australia. All the way my viewers in Western Australia. Oh no I was no I was I was duped. I thought that was the edge there. It wasn't. That was just the paper. Anyway all my viewers in Belmont I don't think I've been to Belmont in Western Australia. I don't know. It's lots of suburbs. Australia's a big

**Dave Jones:** place. We have a note. We have a shopping a cold shopping bag. I'll keep that. I reuse my shopping bags. Thank you very much. I've got a um a it's a very strange thing for Australia. It's a baseball.

**Dave Jones:** I don't know if I've ever thrown a baseball. I don't think so. It's just not a thing here. Um rocket the trash pandas. That's a good name for a baseball team the trash panda. OH SMARTER EVERY DAY. OH be a thinker and a doer. There it is.

**Dave Jones:** It's a smarter every day Destin. I've actually met Destin when he came to Sydney nice bloke. What else we got in here? It looks like it might be a random assortment. We've got something this is like a um I don't know something you plug into the mains and you press it and I don't know, random bit of kit. Looks like a security doorbell thing. Ah, second suck of the sav. Um and I swear I'm not using for e-waste disposal. I had a Kogan smart doorbell um that kicked the bucket. I

**Dave Jones:** took it yeah and to see Oh okay, so this is the receiver. Fun 2-minute teardown, yep. Um there are a couple of screws that went walkabout but other than that the parts are there. Yeah, smarter every day baseball cuz I somehow managed to get two of them. Feel free to keep it or pass it on as desired. I think I'll keep that. I don't know. I like Smarter Every Day so like having some merch. It's going straight to the pool room. So this is a Kogan video doorbell. For those who

**Dave Jones:** don't know, Kogan um is a Ruslan Kogan I believe his name is. He started out from his garage selling imported TVs and stuff. Now he's this huge conglomerate um here in Australia that basically imports and sells everything electronic um and he's the one who actually beat me to buying the rights to Dick Smith um the the Dick Smith head the Dick Smith trademark and name and stuff. I actually officially own as well in conjunction with somebody else. We actually made a bid on when Dick Smith was folding and Ruslan

**Dave Jones:** Kogan he had more money so yeah. He got the rights to Tricky Dick's famous head and trademark and website and stuff. Anyway, let's rip it apart. Well, it's just uh full of batteries, isn't it? But then again, I guess it is a video Oh no, they're not that deep.

**Dave Jones:** But it is a video doorbell. There's another Is that the That looks like a charging board under there. I don't know. Is that Well, there's no button. That's the buttony dude interface. Oh, there you go. That one's a bit beefier.

**Dave Jones:** Look at that. Oh, there you go. Whack them in series. They just got Oh well, this one wasn't quite big enough So, we'll just, you know, whack and use a bit more extra space and just whack another, ah, one in there. So, let's rip that out. And, ah, yeah, they got wires connecting, ah, this battery ring board and the power board. Is that the secret screw? Oh, there's a secret screw interface on the back. There you go, missed that. Ah, and there you go, got an SD card. Right, okay, so you can, ah,

**Dave Jones:** I don't know, does it like detect movement and record it? And, ah, like stuff like that? I I don't know. And I'm not going into huge detail here. Those playing along at home can have a look at, ah, that part number and decode it. You know, it's just like a, ah, purpose design ASIC for this sort of job that, ah, would be used in dozens and dozens of different branded products. There you go. Ooh, something's something's cracked off there. Ah, it's dodgy little plastic support. Look at

**Dave Jones:** those dodgy little plastic standoffs. They're pretty how you doing. Wow, ah, yeah, look look at that. Just shattered, poor quality plastic. Ah, wow, that's terrible, Muriel. Yeah. Wow, that's They're awful. Anyway, that's just, yeah, like a plastic insert thing in there. So, we've got a board-to-board interconnect there and there's your there's your Wi-Fi or whatever. I assume it's like a Wi-Fi interface, ah, um, type thing. So, yeah, they've got that's on a separate daughter board there and a board-to-board interface. Can we get this out?

**Dave Jones:** You bet you we can. Mister screw. Ta-da. And there's your camera module. That's, I don't know. Yeah, just, ah, ah, there you go. No, it's actually, yeah, it's straight on the straight on the board down the bottom there. There's the sensor. Then you've just got your lens on top. That's pretty common. And, ah, that looks like it's all sort of like custom designed to go into this. So, they haven't like bodged on a uh like just an existing camera module.

**Dave Jones:** They have sort of integrated that into the USB. And oh, no. No, you would see those in like those little cube cameras and stuff. So, maybe No, I don't know. Anyway, there's a uh per um movement sensor. So, yep. Yep. So, I just I'd say yep, the per just it just sits there powered down. And as soon as the uh per detects a movement, it will um then enable and trigger and uh record video to the S and or screenshots, I don't know. Still images, whatever to

**Dave Jones:** the um thing and then alert your receiver e-doohickey. So, there it is. Um there's your receiving antenna. Cool bananas. Um yeah, and this just this is the doorbell. When somebody presses the uh button on the front, they uh but I'm sure it does all that movementy uh job as well. But um yeah, that's it.

**Dave Jones:** So, there you have it. Um it's just that's just a wireless doorbell and video intercom. I mean, it's not it's Kogan branded, but um yeah, it probably is sold under many different names. So, I don't know. If you know who manufactures that, leave it in the comments down below. But yeah, it's probably like a little uh one of the low-end um Sony sensors or something.

**Dave Jones:** Like Sony dominate. They absolutely dominate the uh market for um you know, image sensors and stuff. It's incredible. But yeah. There you go. Pretty simple. Don't know how long the battery would last, but yeah, that'd be going into uh deep powered down. Just um yeah, the uh passive infrared. Those per sensors uh don't take much because well, you can get uh wireless versions of those that last for, you know, years or whatever um on one like CR uh 123 battery or something like that. So, there you go.

**Dave Jones:** Thanks for sending that in. Interesting 2-minute teardown. And all my viewers in Tasmania, which is like an optional part of Australia. Um Thank you uh to Justin VK7TW for those amateur radios out there in uh South Hobart in Tasmania. So, let's have a squeeze.

**Dave Jones:** Whoop, whoop, whoop, whoop. I ripped some I hope it's not valuable documentation. I ripped it. I cut it. So, what have we got? Shoestring packet radio. Oh, Tom Moffatt. Yes. Yes. Tom Moffatt um sadly passed away like, I don't know, 5-6 years ago or something like that. Um yeah, yeah, used to enjoy Moffatt's Mad House column in um EA. And I think he had in other uh publications as well. Um so, yeah. So, this is a listening post.

**Dave Jones:** Oh, it's a listening post kit. Okay, cuz this is the listening post um project. I remember seeing that back in EA back in the day and thinking, "Oh, that's pretty interesting. And I wouldn't mind getting into that." But, I wasn't really into the ham radio stuff. Aha, another name I know. Uh you can blame Peter Parker VK3YE for this package. Good day, Peter.

**Dave Jones:** Um while this uh while he was down in in VK7 visiting family, got to talking about the Moffatt's Mad House column in EA magazine. I mentioned that ended up with Tom's uh box of kits. Oh, you actually inherited Tom's box of kits. Um cuz he was selling these kits. Was he? I I presume he was. I didn't know he was selling them direct, but that makes sense. To remember a little Electronics Australia royalty. Yes, indeed. I've dug out the EA articles included them in the kit. I used to read with great interest

**Dave Jones:** Moffatt's Mad House and even built a packet uh pocket packet modem back in the '90s when I got into amateur radio. Um thank you very much, Justin. So, was this um actually packed by Tom himself? This is This is one of his one of his kits. And is some his packet radio like still a thing? Like, can you still like are they still transmitting?

**Dave Jones:** Can you still get stuff? Can you still receive stuff? I don't know. There you go. Um yeah. Wonder where he got his board from. This was part of Tom Moffatt's original kits, you know, from 1992 94. And oh, awesome. I've mentioned this many times.

**Dave Jones:** Uh back when I was a boy, like you know, in in the '90s like this or in the '80s, you'd take it for granted. You get your double-sided solder mask plate through uh you know, PCB with you know, 6 6 thou uh rules for you know, a couple of bucks delivered straight from China, which is insane. You get five of them or something, you know? It It's insane, but back then you either had to roll your own boards. If you got them made commercially, um just even getting like

**Dave Jones:** a single-sided one um would would cost you very significant coin. It could cost you like hundreds of dollars for the setup fee and then just getting like a panel made. There was none of this shared panel rubbish. That was Jeez, shared panels maybe came around mid to late '90s, something like that.

**Dave Jones:** Then when I used my first shared panel, I think. But before that, you had to buy the whole panel and it was, you know, it was pretty costly to get a board made. Anyway, yep, nice single-sided tin plate jobby. You would You wouldn't get the solder mask. Oh, that was fancy pantsy.

**Dave Jones:** So, you just got the um tin plate and yeah, just the rolled tin finish on your PCBs. Nice. Good on you, Tom. Thanks for all the articles, mate. So, that's just brilliant. Some original Tom Moffatt uh kits here for the for the listening post. Please leave it in the comments.

**Dave Jones:** Hands up if you built one of Tom Moffatt's listening post. It was a hugely popular project, I think, back at the time that spurred like many variants, I think. And um yeah, and Tom Moffatt, of course, he wrote Moffatt's Madhouse. I used to love Moffatt's Madhouse, but Morse ready weather facts transmissions and stuff like that. You you it up to your computer, I think, didn't you? And you decoded it. Yeah, there it is. IBM compatible world full ATP picture quality. Must have a VGA system that uses an analog type color

**Dave Jones:** monitor. That's good. False colors are not normal ones in the EGA system as well. And they talk about CGA 320 by 200 doesn't hold a candle to the VGA images and stuff like that. Oh, that's just That is just great, right? Weather facts. Is it like do they still transmit this? Can you still receive it? I I don't know. Sorry, I'm not going to go to the Oh, there you go.

**Dave Jones:** Wow, orbit followed by the meteor meteor satellite. Wow. Like you could really That'd be really funky back in the day. I was tempted to get one, I think, but yeah, I never did get around to it. I've no idea what this article's about here, but I just found this funny.

**Dave Jones:** Just complained the presentation of New South Wales Department of Administrative Services. Sir Edward A. Portly Bolding expert gave a talk on behalf of the department. Echo explained that a routine like this can go for a couple of minutes. I got like what? What is this?

**Dave Jones:** Here you go. You typically put it in a do-it-yourself box like that and hook it up to the computer and it's We've got some scope waveforms there. Back when that's how you actually got way a scope waveforms back in the day. Actually took a photo of the CRT. Yeah, one of the most popular electronics construction projects in recent years was Tom Moffett's listening post. Yeah, Tom did this one as well, but it looks like Jim wrote the article and oh, they talk about a micro B computer and stuff like

**Dave Jones:** that. Groovy. So there you go. You like there wasn't a huge amount to it. Facts weather things and I don't know a satellite geosynchronous plots and stuff like that or something. So I'll leave it in the comments down below. I'm sure someone will know if this thing if these things would still work, but yeah, you would have to like get I don't know. Can you get like new software if it does still work? I assume that there's new software and receivers that just receive it all or you just get it on the

**Dave Jones:** interwebs or whatever, but there you go. Tom Moffatt would have packed these kits himself. Good on you, Tom. Thanks for all the fish, mate. So, we've got the listening post we sat station here, if that's how you pronounce it. And there's a schematic for it. Looks like it's only a HC408 4046 regulator, couple of op amps, and Bob's your uncle there. So, that interfaces to that it'd be going to the parallel port of the PC. And that's you know, that's all she wrote. Or but the software was available in

**Dave Jones:** Amiga version and a PC version too. So, so yeah, that's the PC port interface end. There you go. Ordering the kit, this is what I used to do. When I published my things, if you want this software or kit or whatever, then you'd put your address in there. And then people would send you like a money order or sometimes a lot of the time I got cash in the mail and I'd ship them a um that stuff back. And that's how it was done back in the day.

**Dave Jones:** So, there's also the shoestring packet radio, the pocket packet modem here. And oh, look at that. Is that an original Toshiba T1000 series? Oh, I'd die I want one of those. I want one so bad. They Some of the models have DOS in ROM. Absolutely fantastic.

**Dave Jones:** MS-DOS in ROM. It boots instantly. Absolutely brilliant. I totally remember this article. I remember this photo. And there's what you can get out of these things. And the schematic for this one quite significantly different. Uses a TCM 3105 modem chip. I wonder if you can still get that. I might have a I doubt it.

**Dave Jones:** Anyway, yeah. Hands up if you built one of these as well. But these are the kits here. So, we have an original pocket packet kit from '92 and includes all the parts and like Alfoil down in there. Wrapped in Alfoil. Absolutely brilliant.

**Dave Jones:** And yeah, that it'd still work. The tin plate PCB jobbie in there. Was that like a from RCS radio or something? Maybe. And there's a 94 listening post kit. Although the original article is 1992. So, maybe he updated it or something like that. But yeah, there you go.

**Dave Jones:** Classic kits from Tom Moffatt. Oh jeez, that's a real blast from the past and I really enjoyed Tom's Moffatt madhouse column as well as his project articles. Even though you know, I would read every project article and like you know, consume them even though I had like really you know, I thought oh that'd be cool but you know, like and had no interest in actually building one or whatever.

**Dave Jones:** Yeah, that's just what you did when you're a hobbyist. There was no internet back then. I won't do the research now but somebody will no doubt tell me in the comments down below if these things would still work and if I could actually build them up and like and get the old DOS software or is there you know, I'm sure there's more. If they are still transmitting this sort of stuff then I'm sure there's like better ways to get it these days but hey, that was the early 90s. So, you

**Dave Jones:** know, we're talking like 30 years ago. Anyway, Tom Moffatt absolute legend of the Australian electronics industry. Hi to all my viewers in Germany and thank you AK module bus computer. That rings a bell. So, we might have a second sucker the sav alert alert.

**Dave Jones:** Paul Robinson. So, let's check it out. You have a note. Aha, yes, I think I they said they'd email me to this and they'd email I got an email from them I think saying that they would send one of these because we've seen this before and I've used their LCR box on several videos.

**Dave Jones:** This is a reference capacitor box. So, it's I don't think it's a it's not a decade capacitance box. It's a like a literally a reference capacitor. So, I don't know if they've included like, you know, a cow sheet with it. Reference capacitors, 1% tolerance jobbies, although the 100 mics are 5% tolerance and they've measured them.

**Dave Jones:** Doesn't say measured with a Mas Tech MS5308. I'll have to look that up one up, but I assume that's a serious LCR meter with much better tolerance. As a rule of thumb, you generally want when you're doing calibration, you generally want like an order if you can, an order of magnitude better accuracy than what you're actually measuring than the device under test that you're actually measuring. But, you know, in the ultra high-end metrology end of things, which you can read all about on the EV blog forum, you

**Dave Jones:** know, you might only get a couple of times and then it's all voodoo magic and, you know, but anyway, cool. So, we've got a knob on there and we've got reference caps. That'll be handy for very handy for like testing multimeters.

**Dave Jones:** And apparently, it sells astonishingly well considering the very limited market. Yeah, well, people love their calibration stuff. Seriously, people are obsessed with calibrating their multimeters and having standards to check against them. Well, why not? All right, so here it is and it's just got a bunch of different types of one mostly 1% reference caps on here. And then, of course, yeah, there's nothing in there. It's just, yeah, a couple of banana plugs and a switch to connect them through. And they're through-hole jobbies, so you don't have any issues

**Dave Jones:** with potentially damage them due to reflow soldering that you get with surface mount parts. So, anyway, it comes with this sheet here and they're they're using a Mas Tech MS5308 LCR meter and that's that's the nominal spec of that LCR meter. So, they're not using a high-end LCR meter at all to to measure these um, So, um, but like I don't have my good HP bench jobby anymore. I sold that quite a few years ago. I shouldn't have done that, really. Um, anyway, so they've given us measured values

**Dave Jones:** here, but because, um, you know, we're using 1% caps here for anything 1 mic and below and 5% um, above that. That's nominal, of course. Um, you know, the whole idea of getting buying one of these is that you actually get the measured values. Unfortunately, with the LCR meter, like it's going to be better than 0.5%, right? It could be an order of magnitude better than that, but you don't actually know. It's not, you know, a really high-end, uh, benchtop LCR meter with like 0.1% um, at nominal, um,

**Dave Jones:** accuracy or uh, something like that. But anyway, these are the measured, uh, values here. So, unfortunately, um, as I said, I don't have a good LCR meter. So, the best I can do here is actually, uh, use my Agilent, uh, one and could also try out my, um, IET, uh, one as well. But anyway, there you go. So, that's our 1 nanofarad one. That is substantially above what we measured, uh, here, um, 0.999. So, I'm measuring 1.0107, uh, nanofarads and we got, uh, 0.99 on the data sheet. So, that is a difference

**Dave Jones:** of, you know, about, uh, 1. uh, 2%, 1.1%, something like that. But once again, like you don't know, right? We don't have a serious instrument, but I do actually have the only reference capacitor I have here in the lab is this Arco 1. And this is, um, this dates from 1967.

**Dave Jones:** This is actually a serious bit of kit. This is what you'll find in This is a transfer standard, a reference standard capacitor. Very expensive. These are These go for hundreds of dollars each. And, uh, these are incredibly stable with time. You could argue that the older it is, the more stable it is.

**Dave Jones:** Anyway, this is a nominal 0.1% tolerance, but I have actually measured it on, uh, things and it like it seems to be bang on. So, I can actually um give you that on my Agilent jobbie here and we are measuring at 1 kHz, by the way, and it's bang on, right? So, it's bang on. So, I'm you know, I'm fairly confident in this Agilent meter. Once again, this is not good metrology, you know, you'd have to go to Xdevs, um someone like that to actually uh do this kind of stuff. But,

**Dave Jones:** the whole idea is that you'd use something like this not as an absolute reference, but more like a uh just a reference over time so that you can compare uh different instruments and stuff like that. So, you can, you know, see if your meters are drifting over time and stuff like that cuz generally, yeah, these will have a temperature coefficient. So, these are uh PP types.

**Dave Jones:** These are uh polypropylene uh types except for PET uh types down here in the high values. Um there are more stable uh dielectrics and stuff, but these will have a temperature coefficient. And maybe I can demonstrate that. Let's see if we can freeze it.

**Dave Jones:** There we go. She's going up. She's going up. It's got a negative tempco, which yeah, don't freeze your uh reference capacitors, please, because you'll come a gutser. So, but that will come back down. Like if you The whole idea is that your lab is at a relatively stable temperature. You can use your air con to keep it at like plus minus a degree or something. So, you know, it's it's pretty good. So, what does that measure on my IET?

**Dave Jones:** Uh higher higher again on the IET, but I think my Agilent one is the higher uh spec meter here. There you go, 0.999 and we got 9.995 there. So, this is actually reading a bit low according to my uh meter here.

**Dave Jones:** And 99.85. But, once again, right? It's The whole idea is that you can use it to see if your uh meter's drifting and or your um if you're comparing different instruments. And of course, I don't have the best leads here, right? So, you know, these are relatively long. I don't have short leads. There's the 1 microfarad jobbie. There's the 10 microfarad jobbie.

**Dave Jones:** And 100 microfarads, which is this big beast here. Uh wow, look at that. Wow, 100 mic. Thank you very much. Um yeah, and there are different dielectrics. So, you can go into the whole argument about, you know, what's the proper type to use. And I have looked at the uh data sheets for these. I couldn't find the F46461 in a 1% tolerance. So, I don't know where he's getting a 1% uh tolerance from. So, they they might be a special order, but uh the data sheet um didn't

**Dave Jones:** seem to indicate about that. But, the other ones are like um you know, you can actually order them special order. Normally, they're not a 1% uh tolerance. So, you have to read the data sheet and probably get a uh special order for those. Anyway, that will be very useful here for the lab so that I can compare uh meters. And that's, you know, that's one of the cool things. You know, capacitors are really hard to get like absolute ones. Like in the as you can see here, right? 0.1%, right? This is

**Dave Jones:** basically one of the best reference capacitors you can get on the market. 0.1% um initial tolerance. But, the whole idea is that you, you know, use them as transfer standards, and you can do your metrology magic, um and you can um you know, certify them to a greater uh standard than than that um than their marked value. Of course, the whole idea is stability with time and temperature.

**Dave Jones:** The absolute value doesn't actually matter as long as it doesn't drift with time and temperature. Unfortunately, these polyprop ones do. They're they're not the best um dielectrics. You probably can get better uh more stable dielectrics, but a lot of them uh these days are like SMD ones, which as I said, you know, you can cause issues if you don't reflow solder them properly, you could damage them, and and you just don't know. So, it's a bit how you're doing. So, any reference capacitor box I would much prefer through hole jobbies.

**Dave Jones:** Anyway, thank you very much, Roger. Um I'll link in the module A AK module bus DE. I always forget the URL cuz it's quite hard. Um and I'll link it in down below if you want one. It's 46 euros that. So, yeah, it's an interesting useful bit of kit to have around the lab, especially if you like you know, evaluating instruments and doing all sorts of other things and you care about you know, if your meter's drifting or something like that. It's you know, obviously like you can once you get it

**Dave Jones:** get it in a stable temperature, you record the values. It doesn't even matter what the reference values are. Once you record them on your own instrument and then you can you know, come back in a month time you can measure it every month and see what's drifted. It's unlikely the caps have drifted or aged much in terms of that if you use them at the same temperature, but even then temperature doesn't make a massive difference, but it can. And I've already opened this one up because they

**Dave Jones:** didn't put mailbag on it. If you want to send something in, put mailbag, PO Box 7949 Northwest, New South Wales 2153, Australia, not Austria. Thank you very much, Creative. They've sent me these wizbangy Bluetoothy thingamajig earbuds. So, they've got a wanky little packet here and I really despise these little like hearing aid kind of um silicon things which are supposed to sit in your ear. I just I I like them I like them earbuds that just sit on the outer bit of the ear.

**Dave Jones:** So, anyway, here it is up close and this is actually rather funky design. It's got the USB-Cs in there and then a battery level for the cuz it does have internal battery. So, you can just take it anywhere and charge them and left and right. And if we open that, there you go. Not sure where It's a bit I got bright studio lights here. There you go. You can see them actually slowly flashing there, which means they're charging. And you can see that they sit in these little this

**Dave Jones:** little charging cradle here. I know, you know, this is like everyone's doing this these days, aren't they? We've got two little pin contacts in there, left and right, and they sit in the cradle, and they just start charging from the internal battery. So, that's pretty groovy. I assume like that's in the back part of it here, the battery and whatnot. Anyway, that's all there is to it. Super X 5 ready or whatever. Anyway, I spent like an hour or two using these the other night, hooked them

**Dave Jones:** up to my shoe phone, and they like sound wise, what can I tell you? Like they're, you know, sounded pretty good for dialogue and stuff, listened to some music as well, and they sound pretty decent. Ordinarily, I use these ones.

**Dave Jones:** These are die cast, and they just like earbud ones, and they sit in my ear, and they're great. The only problem is when you've got metal conductive like this, and you do move around, if you do have static charge on yourself, I can zap myself in the ear, but uh these are Don't know if you can read that, but all glamour or something all glamour ones, and you know, they're not quite as good as these, I don't think. I don't know. Like it's like this is not going

**Dave Jones:** to be an audio review thing. And yeah, I can't really get you the proper audio output of these things unless you had like an artificial ear or something, and then like a microphone plugged into like an artificial ear, and then you can plug it in. But yeah, I don't like how I just don't like this style of silicon thing which goes inside my ear. I don't like having my ears plugged up with these things. It just it it just feels weird. I'm not comfortable. That's just a totally

**Dave Jones:** personal thing. I know other people just absolutely despise these things and think they're horrid and old school, and they love the bass they get with the nice sealed ear plugs, and wank wank wank wank wank. Okay? No, not really a fan, but they do sound okay and they do work and I do like the mechanism uh here and the fact that, you know, you can just take this. I don't know like the specs of how long it uh you know, the battery lasts and and stuff like

**Dave Jones:** that. I assume, you know, you get quite a few, probably dozens of uh charges out of the internal battery, I would have uh thought. So, you can just take it with you and they charge and you take them out and it keeps them in there and they don't rattle around and that's really neat design. I don't know what else to tell you. Um obviously, on a mailbag, I'm not going to do a teardown, but I don't know if you wanted to see a mic uh teardown of one of these mic you know,

**Dave Jones:** the microelectronics inside these things. I don't know. Leave it in the comments, but yeah, they're okay. Um I don't have This is the only Bluetooth earbud thing I have, so it might come in handy. So, they're supposed to be sweatproof as well. They I don't think they're waterproof, so you know, sweatproof instead of waterproof for a reason, so you wouldn't want to swim with them. Um and apparently, it's got active noise cancellation. I didn't try that. I don't like uh noise canceling stuff. I don't need noise canceling

**Dave Jones:** stuff. I don't like tuning out the world. I like listening into the world, uh which is why I prefer like open-back uh headphones and why I prefer um unsealed earbuds like these. Uh there you go. 900 mA hour capacity, 85 mA hour uh capacity in the earbuds. Um is that both combined That'd be each, okay? Yeah, so you'll get, you know, a few charges out of that. That's all right. And wireless uh range up to 10 m. I I actually got more than that. I was getting like on the

**Dave Jones:** other side of my house before they uh decided to uh drop out, so yeah, I was probably getting 20 m, something like that I'd say before they were dropping out. So, I think that's a bit conservative. Yeah, I had no problems with the range at all. I was able to walk around the house, no worries. And I didn't read the uh manual that I've got here, but I figured out uh that you touch them and it speaks to you as well.

**Dave Jones:** Um and you can uh and you can just touch the uh sides that got capacitive touch sense and you can increase and decrease the volume. I figured that one out, and looks like it's got some other functionality as well. Or you can master reset. Just hold them both down. Next up, we got the classic brown masking tape from Hong Kong. Thank you. Hi to all my viewers in Hong Kong. So, let's crack it open.

**Dave Jones:** I won't tell you what it says on the front. It's a bit of a mystery. I don't know. We have a note. I won't actually read it yet. I just want to have a look. Well, spin spin spin spin spin.

**Dave Jones:** It's Don't know if it's new or it it looks Yeah, it looks shrink-wrapped. What What do we got? What do we got? It's a two-in-one oscilloscope. Ah. The Fenesy Nersery again? Fenesy again? What's this? Like the third sucker of the set? And a sig gen. Woah. Look at that.

**Dave Jones:** That looks pretty funky. I like it. It's kind of like colorful, you know? All right. Well, yeah, they might have to be separate videos. I like When you get stuff like this in the mail bag, you can't like do it in like 5 minutes. Not even a teardown, really. It's addressed to the handsome and humorous Dave Jones.

**Dave Jones:** Well, if you insist. Asul from Fenesy. I Look, come on. We we need an official pronunciation. I'm sure somebody's told me, but anyway, I'm Asul from Fersy. May you remember? Yes, I do remember our R&D slowed down the first 2 years, but this a year we released because, you know, something happened of some unspecified unknown origin happened for the last 2 years. Then we will we release a lot of devices. This time we bring you our DSO 2C2, combination of transistor detector transistor detector and oscilloscope.

**Dave Jones:** Please don't tell me they've put a transistor tester in an oscilloscope. It's bad enough when it's in a the In an oscilloscope, do they mean curve tracer? They might No. Oh, look, it's got Oh, yeah. Look, it's got a ZIF socket on the front.

**Dave Jones:** This wishes. Thank you very much. Well, let's check them out uh briefly cuz yeah, um it's going to require a second channel video if people want to see the full Monty.
