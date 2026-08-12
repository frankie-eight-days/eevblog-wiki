---
video_id: t1R9IQF0Y9s
title: EEVblog #1224 - uBeam is Sinking!
url: https://www.youtube.com/watch?v=t1R9IQF0Y9s
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 14, "2": 45, "3": 58, "4": 68, "5": 97, "6": 142, "7": 148, "8": 178, "9": 178, "10": 208, "11": 208, "12": 238, "13": 238, "14": 268, "15": 268, "16": 298, "17": 328, "18": 358, "19": 388, "20": 388, "21": 418, "22": 447, "23": 448, "24": 478, "25": 478, "26": 508, "27": 508, "28": 538, "29": 538, "30": 574, "31": 598, "32": 598, "33": 628, "34": 658, "35": 658, "36": 699, "37": 718, "38": 738, "39": 748, "40": 761, "41": 785, "42": 802, "43": 818, "44": 837, "45": 856, "46": 887, "47": 903, "48": 919, "49": 931, "50": 944, "51": 964, "52": 986, "53": 1007, "54": 1028, "55": 1052, "56": 1075, "57": 1099, "58": 1115, "59": 1129, "60": 1146, "61": 1164, "62": 1178, "63": 1193, "64": 1211, "65": 1229, "66": 1246, "67": 1260, "68": 1281, "69": 1300, "70": 1316, "71": 1334, "72": 1354, "73": 1369, "74": 1383, "75": 1400, "76": 1416, "77": 1435, "78": 1454, "79": 1472, "80": 1486, "81": 1504, "82": 1516, "83": 1536, "84": 1555, "85": 1572, "86": 1590, "87": 1609, "88": 1629, "89": 1651, "90": 1668, "91": 1686, "92": 1700, "93": 1715, "94": 1729, "95": 1769}
---

**Dave Jones:** Hi. Yes, everyone's favorite impractical technology, Ubeam, is back in the news because, well, it looks like they're finally coming to gutter, but not without some last-minute hilarity. So let's take a look at it. They've been in the news for several reasons. One is that definitely check out Paul Reynolds' blog.

**Dave Jones:** Paul Reynolds, if you don't know, he writes the Lies, Damn Lies and Startup PR blog. Awesome. You should subscribe to this. How do you subscribe? One of those newfangled RSS things. Former Chief Technical Officer, CTO of Ubeam, and they've, Ubeam, have apparently laid off around half their employees.

**Dave Jones:** So, yeah. Oh, look, we've got some transducer technology down here. So anyway, it's a very lengthy article. Highly recommend you take a look. And by the way, Paul's also on Twitter, so you should follow him over there. And I'm also on Twitter as well.

**Dave Jones:** You should follow me on Twitter because I tweet like a boss. Anyway, I've always tweeted. Look, I just found this network switch in the dumpster. Oh, look at that. Latest teardown video. Spoiler alert. Yeah, follow me on Twitter. Anyway, Ubeam have a new funky-looking website.

**Dave Jones:** Look at this. Always on wireless energy through ultrasound. Ultra safe. You'll see this safe thing mentioned over and over again. Ultra simple. Sound technology. Now long-range wireless power reliably and safely are always on. We'll get into the long-range part of it shortly. Ubeam's proprietary transducers, transmitters, receivers, and software deliver wire-free power at a distance of meters to units ranging from Internet of Things devices, medical and aerospace systems to portable electronics products, a turnkey hardware and software solution.

**Dave Jones:** Turnkey. They've now magically just got a turnkey. Turnkey solution. You can just, because if you don't know, like, did we cover this? No. I think Paul definitely covered it on his blog that Ubeam, they sacked, of course, their CEO, Meredith Perry. They booted her ass out the door and they replaced her with the chief financial officer, the CFO.

**Dave Jones:** Oh, what high-tech startup-y type company has a... Chief financial officer promoted to CEO. Ubeam, of course. Anyway, then they finally got someone decent in as CEO to steer the Titanic until it sinks. And that's what it's looked like happening now with, yeah, sacking half the company.

**Dave Jones:** They just ran out of money. Well, they couldn't raise any more money going through a huge cash burn rate. All the details are sort of in here. Speculation of what's, you know, the reasons behind it. But it's almost certainly... That they simply just run out of cash.

**Dave Jones:** They can't raise any more. The investors don't want to give them any more. I think there is still money, you know, like, promised to them, but they're being held back and, like, I don't think they're dumb enough to give them any more money.

**Dave Jones:** Anyway, so they've got to be frugal and, yeah. Looks like everyone, including the chief financial officer, is now gone. You can go check up her profile on Twitter. I won't bore you with the details. But anyway, let's take a look at the website.

**Dave Jones:** Oh, look at this. Look at this. Look at their new transmitter they've got here. Look at this. It's super small. If you actually go to Ubeam's Twitter page, I've had to log out here in a different browser because they've blocked me. I wonder why.

**Dave Jones:** Anyway, you can see the history of their, like, their transmitters over here. Here we go. January 2018. It was this enormous thing here. Probably taken hundreds of watts input, a kilowatt or something because it's not very efficient. And then they've shrunk that down in March 2018.

**Dave Jones:** Good on them. And now it looks like they've got it down to what looks like this thing here. So that's their new transmitter, which I think they give away with their, if you join their partner thing and you want to team up with them because they don't sell products anymore.

**Dave Jones:** Ubeam, obviously, completely given up on the dream of selling any sort of product, especially to charge you. Phone as we'll get into. So, yeah, they're looking for B2B or business to business customers. Now, that's where they've pivoted to. They should have pivoted to that.

**Dave Jones:** You know, how long have you been going? Seven, almost eight years or something. They should have pivoted to that like six years ago. You know, a year into it could have told you that this thing just, you know, charging your mobile phone just was a ridiculous idea.

**Dave Jones:** Anyway, so they shrunk that down. Whether or not they're getting the same output power from that or not. Or physically smaller arrays are still 145 dB output power. We don't know. But with the transition to the Internet of Things stuff, they it may just be a physically smaller transmitter because they've realized it's not very efficient and we can't transfer, you know, watts, tens of watts, hundreds of watts, thousands of watts that they were promising previously on their website where, you know, they'd power large flat screen TVs that take hundreds of watts.

**Dave Jones:** They'd be powering everything. Unbelievable. Anyway, so they've got this new small transmitter. Look at this smart agriculture. Yeah, we'll get into the distance thing. But yeah, if you've got a big sort of, you know, greenhousey type thing, as we'll see in the power figures shortly, per distance, which the CEO has just published, thank you very much, that you're not going to get more than a couple of meters.

**Dave Jones:** And even then you're looking at tens of milliwatts to power little sensors. It's just silly. Anyway, so industrial, look at this, industrial Internet of Things. Look at all these things that you can be powered. Wow, in the factory. Fantastic. Smart, even though already, like, you know, you've got like power running all along the walls here and everything else.

**Dave Jones:** But no, no, use U-beam. Sure. Where's it go? Oh, yeah, there we go. They've got the transmitters up on the roof. There you go. So brilliant. Smart living, of course. Look, it can power like sensors up on the roof. On the wall. Is that there?

**Dave Jones:** No, that's not there. That's a one of those nest, stupid, nasty things. I've got a thermostat controller can power your iPad. Yeah, sure. Consumer electronics. Look, there's still some it can power your laptop. There's still tablets and everything else all at once. One transmitter.

**Dave Jones:** Sure. It's just going to be able to handle all of these devices on the bench. Yeah. Aerospace. Look at this. Put one of the U-beam things inside a jet engine. That's where you need it. Because, oh, yeah, you want to transmit it from one side of the ferry into the other and get power of a little sensor on the other side of the ferry.

**Dave Jones:** You want the super awesome, reliable U-beam technology inside a jet engine. Yeah, sure. And the wheels. Look, wheel sensors. You can have like a little U-beam transmitter on the bottom of the plane and it could like beam the power down to the wheels as they come on.

**Dave Jones:** Automotive, because you want to use it. Inside a car and medical. Look at this. You can power everything in your medical suite using just pump out 145 dB of ultrasound everywhere all over your operating theater. That's what you want. No whackers. All right.

**Dave Jones:** How U-beam works. U-beam is a proprietary transmitter. We've seen the ASIC before beamforming algorithms. The computer vision optional tracking. As you'll see, this transmitter that they've actually got up here. I don't believe this does any tracking. Whatsoever. We'll see this in the video in a minute.

**Dave Jones:** It's purely they've demoed this before theater here. The demo summit or whatever. Oh, yeah, there it is. There's like an early version of it. There you go. Didn't have the extra things on the top. Looks very similar. You can see that it is not see that it is not tracking.

**Dave Jones:** It has no phased array tracking at all. But they're bigger one over here, which didn't work at first. And then it eventually it eventually did. That one has the vision tracking with the silly little white square on the back of the little doodad there.

**Dave Jones:** You might have been able to see that. And it it just visually tracks that. And it's just silly. Of course, in the previous video, I've done debunking this thing. Of course, it's no practice. There it is. The little white tracking window on there.

**Dave Jones:** And of course, that's absolutely no use whatsoever. Because, well, you got your mobile phone. You have to sit face down and you can't use it when it's let's just not go there. It's ridiculous. I've already debunked it. And here it is. So safe.

**Dave Jones:** The safety of sound. Yeah, because they've probably realized that you can't pump out 145 dB. So I reckon the new transmit is not doing that. I reckon it's doing at a lower level for this internet of things stuff that they've pivoted to. Anyway, they've got a new video.

**Dave Jones:** Do you want to see it? Of course you do. Welcome to a world powered by Ubeam ultrasonic wireless energy. We're safe and reliable contact free wireless power can keep your look at this, right? The guy that like this still implying that you can charge your mobile phone.

**Dave Jones:** I it doesn't even have their ridiculous, like big brick. Yeah, it doesn't even have this ridiculous big brick thing on the back of it. And right, doesn't even have that. And you and of course, your hand would be even if you had it on the back there, your hand would be covering the damn thing.

**Dave Jones:** I know I've done this in the debunking video. It's ridiculous. You're turning your head all the time. And like, it's just Oh, anyway, they're still implying that you can do your mobile phone and you can do the monitor, the monitor. It only takes like, you know, 20 watts, 30 watts for a monitor or more.

**Dave Jones:** Unbelievable electronic devices running, no wires, no battery changes in any application. industrial, any applicant, any application. It's that good. It's that universal. Remember, it's a trillion dollar idea. So Mark Cuban or whoever said, Oh, yeah, it's a trillion dollar idea. Absolutely. Look at this.

**Dave Jones:** I did a forklift, a forklift. What on earth? And do you like a what? Who comes up with this crap? Right? And then what they got a transmitter on the roof or your parents something on all these industrial machines. Oh, yeah, look at the baby.

**Dave Jones:** Oh, yeah, look, the blender over here. Power your blender with you baby. Yeah, they're only like what 1000 watts or 500 watts or something for a blender. No workers. And what is it lights up here? I don't know the range hood. Look at that.

**Dave Jones:** You've got the lamps in your range hood. Wow. Yeah. And the sensor up on your wall here. comes up with this stuff consumer electronics and look at this and this is just ridiculous as if they're going to power all these things and the phone is face upwards you can't use it when it's

**Dave Jones:** face upwards where are they going to put the transmitter uh the receivers in in the keyboards of these notebooks as we get into you can't even get the power out of the thing smart agriculture agriculture yeah because you know that's only like that's only like 10 20 30 meters away

**Dave Jones:** 50 meters away from the transmitters it's going to work a treat you're lucky if you get micro watts out of it at that distance aerospace there's the jet engine medical all the medical stuff automotive oh yeah because you know you definitely want it in your car in the entertainment like navigation

**Dave Jones:** consoles and stuff that are already in there and hardwired into the car that's where you need your power your ultrasound just have it up above you in the car and then you can just beams everything down and you can just put it in your car and then you can just put it in your car and then you can just

**Dave Jones:** put it in your car and then you can just put it in your car and then you can just put it in your car wherever you need to keep critical devices charged and always on you can you let the nest is so bad can you imagine combining a nest i i don't know if this is an

**Dave Jones:** actual nest but imagine combining the boondoggle that is the nest sensor with you being technology it's a match made in heaven it's on u-beams turnkey hardware and software solutions this receiver works with these leads apparently the leads are just directly connected across the

**Dave Jones:** ultrasonic uh sensor so it if it receives enough energy it powers the lead right i believe this directly i don't think there's any active circuitry inside this thing in fact they implied as much in the uh demo look you can see that this thing is moving yet the leads aren't really moving much

**Dave Jones:** in there look what are all these dead spots and things like like it's not even like it's pointing up if you look at the angle maybe there's some parallax like the angle they're filmed at that but like it moves and the lead hardware software solutions give you the ability to keep network

**Dave Jones:** sensors and devices running harvest and learn from the data build a more robust and powerful look at all this look at all this factory equipment you can power all without using radio frequency waves infrared lasers or electromagnetic interference yeah with the infrared lasers there that's the

**Dave Jones:** uh we charge that i've uh also i haven't really debunked that that does work but it's like once again it's impractical u-beam works in quote marks it's just impractical interference of any kind the ultrasound waves bounce right off the body you've been safe for you and everyone around you she looks

**Dave Jones:** out ultra safe ultra simple she's ultrasound around you and everyone around you ultra safe ultra sound technology frequency waves who do they target this crap too obviously they've pivoted towards b2b customers that's a fact and as if any company any technology company looking for a wireless charging solution like this is going to go look at u-beam and go uh

**Dave Jones:** oh yeah look at her watch this video go oh i'm sold yeah we need to partner with them because we can integrate into all of our products it'll just be magical it's unbelievable i'm going to be like what no wonder they haven't announced and they're not going to get any customers taking this

**Dave Jones:** seriously somebody's probably just sitting in the background who might need this for some really niche technology and i don't like it there is still some niche value in this for niche applications maybe you know ultra low power internet of things sensors that uh you know you have a

**Dave Jones:** direct transmitter at it because it's the best solution you might need it over two or three meters or something like that you might need you know like a few little tens of milliwatts or something like that and it may and you don't care about the efficiency it may

**Dave Jones:** be you know there's got to be niche applications for it but it's definitely not going to make them any money so there's probably some supplier or manufacturer or whatever just sitting back oh you beam are going to go under they're going to go i'm just going to pick this up for pennies

**Dave Jones:** on the dollar they're just not going to buy why why license the technology now when you can pick it up in six months time when they go bust you'll be able to pick up the ip for a song automotive your power your wireless world your wireless world fantastic i i i'm sold

**Dave Jones:** thank you very much you be 125 issued patents and applications unlimited potential unlimited potential if you partner up with ub always on wireless energy it's just absolutely ridiculous anyway there's more there's more because the ceo this is actually old this happened back in april

**Dave Jones:** um the ceo presented at this summit thing and it's got some interesting stuff in the video so let's have a look this guy does know his stuff but he's like obviously been handed the empty bag you know he's doing his best so i love this uh this meme that somebody hacked the basic human needs which

**Dave Jones:** you know is basically battery life wi-fi because we walk around with our our point to mean connectivity to the internet it's useless so what we really need to do is solve the second half of the problem which is always on wireless energy without wires without battery sounds exhausted without

**Dave Jones:** having to worry about charging or changing batteries so enthusiastic i don't know if it's um he's not very good at public speaking or whatever or he's just knows he's been handed the soggy bag of technology and he's just trying his best i got like i feel sorry for him he's trying his best but he's just yeah it's like i've got to try

**Dave Jones:** and flog this technology to someone and that's what i've been put a ceo for to just find a buyer for this turd and it's just poor guy feel sorry for him anyway he came from energis energis which is of course i haven't done a video on energies but paul reynolds has done heaps of videos on

**Dave Jones:** energist and it's basically a scam it's a it's floated on the stock market it's a basically a competitor uh rf uh technology to uh wireless uh charging a competitor to u-beam and well yeah that's just anyway he comes from there so from one sinking ship to another i'd be putting short

**Dave Jones:** options on energies let's just say that so they're just like projecting what the market's going to be for wireless energy opportunities and they think they've got a chance with the impractical technology they've got some some chance in some niche application but as i said

**Dave Jones:** somebody who's just buying for pennies on the dollar in six months when the money eventually runs out and once again yeah they're just targeting like not phone not really consumer anymore they're targeting internet of things and warehouses and also agriculture and all that sort

**Dave Jones:** of wanky stuff but yeah anyway there's some interesting stuff in this video now um here is this is interesting they've got their own sensor transducer technology which is very murata off the shelf uh like but we've seen various incarnations of their possible sensors we saw

**Dave Jones:** a photo uh back there as well with the perforated holes around the outside of uh what looks like a focusing array or a focus in a cone on the uh top or something like that and they've got this interesting transducer act like heat map energy heat map by the looks of it now i won't go into

**Dave Jones:** the details here because paul's already done that things here well there's the sensor tech yeah here he talks about the uh the heat mapping of course he's the former cto he knows what he's talking about so he goes into some detail about the technical you know tries to analyze it all

**Dave Jones:** so i won't go through that uh again you can read that for yourself i highly recommend you do and and here they've got a the delivered power at a distance and here you go you mean technology can deliver watts up to one meters in fact we'll see

**Dave Jones:** the next slide contradicts this slide because they can't do watts past a meter so um yeah i can't even do watts at a meter so this is tens of hundreds of milliwatts from one to two meters and 10 milliwatts uh beyond two meters i think that might say down here and they've got

**Dave Jones:** this interesting focused power here distance and paul shows in his blog he actually from the array size he actually calculates uh the focus and they say it's at two meters here but he calculates the focus point based on the dimensions and everything else at 1.2 meters and that's actually

**Dave Jones:** about where the energy so i think paul's spot on that's about where the hot spot energy is it's not at two meters so i don't know whether or not that's real data whether it's just simulated data we we just don't know anyway silly and they don't have any side lobes um grating lobes or anything

**Dave Jones:** like that which is kind of weird but anyway paul goes into all that uh detail in his blog so if you're interested in the technical details of that now here's the money shot here is the money shot they've never released once they've never released their efficiency figures this

**Dave Jones:** doesn't include efficiency but this is usable power on the y-axis here versus distance and look there's got here's the u-beam ultrasound technology in the blue here this is the current generation and this is the u-beam ultrasound next generation which their employees who are no longer with them are going to work on so yeah oops there will be no

**Dave Jones:** next generation u-beam and as if they can suddenly double the efficiency or more of it come on give me a break anyway look currently i look i love how they've put these big ellipses in here to sort of like pad it out and make it look like it's sort of better than what it is you can

**Dave Jones:** actually draw to get the real figure which will be a best case figure because they always do best case in these sorts of uh scenarios is to draw a straight line from there from the tip down to this tip down here so a straight line through there like that is what you'll realistically

**Dave Jones:** realistically get best case because there's no way they're going to leave their best case off the table and look at this it one watt one watt right which is nowhere near even the 500 milliamp charging current of the old school phones at two and a half watts up here at five volts like it's just nowhere

**Dave Jones:** near it and that's it like what 15 to 20 centimeters like this far away they can't even pump out one one like can't even barely do one watt there they could actually deliver i'm sure they could deliver more power uh do that you just pump more power in but there's air saturation and

**Dave Jones:** things like that but um i'm sure they could if they pumped enough energy in but they probably realize well they can't do that because there's various requirements and safety standards for like they can't pump out the 145 db they claimed before so this new transmitter they got may actually pump

**Dave Jones:** out a lot less than that and that's why they're only getting the one watt here but they won't tell you the efficiency the efficiency is going to be horrible um paul actually says it could be as high as like 30 percent the efficiency and that's possible but he doesn't think it's that

**Dave Jones:** high but he sort of calculates that based on the numbers but he still doesn't believe it so yeah it's going to be much worse and and as as it drops off with the distance it's going to be bugger all so yeah and look at this at a meter you're only talking like 0.7 watts or something

**Dave Jones:** like that and at two meters you're only talking like 0.3 0.35 watts i mean it's bugger all so they're never going to get this next generation thing they're not going to suddenly magically the oompa-loompas at the uh ultrasonic sensor factory aren't going to pump out suddenly twice

**Dave Jones:** as efficient transducers so yeah it's just not and they've got no staff to work on it anyway so sinking titanic so that's the best case so they haven't published sort of this sort of stuff before it's interesting to think that they think there's a huge market in this and based on this

**Dave Jones:** this is why they make them ellipses like this oh look at the amount of range it's you know it's a psychological trick look at the amount of range of market because really the the area on this graph is the market that you can capture but is that market there like no right and there's

**Dave Jones:** got tons of impractical stuff um in you being that they're not factoring in this is under ideal case with that transmitter which is not phased array it's just direct it's just fixed direction like that just pumping it out and yeah no anyway they they have a small niche and

**Dave Jones:** they're making it look better than what it actually is because look if you're going to be able to do that they're making it look better than what it actually is because look at the induction over here right that's in every mobile phone at the moment right that's

**Dave Jones:** your uh chi charger that's it you know everyone's doing that right you can buy a chi charger for five bucks delivered on ebay um and you can charge your phone currently so anyway that's an interesting graph but once again no efficiency figures i'll never tell you because that's horrible and why ub

**Dave Jones:** always on wireless energy unless you need to track the thing and then no it's not going to work ability to charge devices and distances of five meters without wires or batteries well you're going to run into like you know you're down in the tens of milliwatts region or something you're down

**Dave Jones:** in the bugger all uh proven safe non-invasive technology not limited by fcc power regulations but there are regulations for maximum ultrasound energy and things like that so yeah they can't do the original 145 db they claim simple hardware and software solutions blah blah blah so they claim

**Dave Jones:** solutions available that you as a client a b2b client can integrate into your products whether they do or not i don't know protected by more than 100 patents which will be able to pick up the intellectual property for a song when they go bust in six months freeing us all from battery

**Dave Jones:** anxiety once again the only battery anxiety we have is notebooks and phones these higher power devices which they can't do they're their own graphs and numbers and you could have said that seven eight years ago anyone with any engineer with half a brain could

**Dave Jones:** have seen that with a focus on critical solutions first convenience solutions second so convenience solutions are your consumer stuff and they know that market is shot and all they've got is critical critical no one's going to use it for anything critical that's ridiculous anyway there's some

**Dave Jones:** niche products out there anyway poor um simon mcelray i i feel sorry for him he's got a lot of mcelray i i feel sorry for him he's left holding the soggy bag and he's got to try and promote this he doesn't sound that enthusiastic about his own tech so for true always on power

**Dave Jones:** you feel the energy distances of up to five meters pun intended and proven safe this is the way to do it it's a way to do it entering the marketplace this year entering products entering the marketplace but they they haven't uh named anyone that they've teamed up with no one's gonna bother

**Dave Jones:** because they'll just sit back and it's not gonna happen uh my seven minutes is up thank you um i would take questions your u-beam's seven years is up they're gonski anyway enough of poking fun at ub they're pretty much gonski so if you like the video please give it a big thumbs up and as always

**Dave Jones:** you can discuss in the comments down below or over in the euv blog forum in particular the u-beam fact thread which frequently ask questions which is enormous just like 100 pages long fantastic bedtime reading anyway i thought we couldn't finish off the video without hearing some words

**Dave Jones:** of wisdom from the founder herself meredith perry because well it's just such a fantastic ted talk and i i challenge you to sit through the whole like 15 minutes of it i'll link it in at the end somewhere here and down below but take away meredith for each technological

**Dave Jones:** hurdle deemed insurmountable by the experts i would spend just a few hours thinking about the problem from a variety of approaches so i was able to solve problems when the phd experts couldn't with just a few hours of really simple research every single

**Dave Jones:** argument over why the technology couldn't work has been indisputably wrong this taught me to be skeptical of experts that expertise represented a narrow way of looking at things engineers are inherently linear thinkers and tend to take a very binary approach to solving problems

**Dave Jones:** as a non-expert i had an advantage because i could look at a problem from different angles because i just didn't know what was possible by thinking outside the box by thinking around corners you can out think the top thinkers and now eight months later i have four of the top

**Dave Jones:** ultrasonic engineers in the world working for me or working with me it's going to work and it's going to be awesome and i can't wait to give the middle finger and smile to all the engineers that criticize the crap out of me bye meredith this is why ubeam it will never work on

**Dave Jones:** Thank you.
