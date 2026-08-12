---
video_id: 0h7lKgIFFXA
title: BitAxe Ultra $80 Bitcoin ASIC Miner REVIEW
url: https://www.youtube.com/watch?v=0h7lKgIFFXA
source: youtube-asr
timestamps: {"0": 0, "1": 11, "2": 23, "3": 47, "4": 57, "5": 69, "6": 85, "7": 101, "8": 117, "9": 128, "10": 138, "11": 150, "12": 164, "13": 171, "14": 187, "15": 199, "16": 208, "17": 222, "18": 242, "19": 255, "20": 269, "21": 282, "22": 304, "23": 321, "24": 329, "25": 343, "26": 361, "27": 373, "28": 383, "29": 393, "30": 404, "31": 419, "32": 427, "33": 435, "34": 444, "35": 455, "36": 464, "37": 474, "38": 486, "39": 508, "40": 519, "41": 534, "42": 543, "43": 552, "44": 568, "45": 583, "46": 598, "47": 619, "48": 636, "49": 649, "50": 677, "51": 688, "52": 698, "53": 708, "54": 720, "55": 733, "56": 745, "57": 764, "58": 775, "59": 787, "60": 799, "61": 811, "62": 819, "63": 826, "64": 845, "65": 860, "66": 875, "67": 888, "68": 903, "69": 915, "70": 931, "71": 946, "72": 957, "73": 972, "74": 986, "75": 1000, "76": 1009, "77": 1021, "78": 1038, "79": 1047, "80": 1059, "81": 1066, "82": 1077, "83": 1091, "84": 1106, "85": 1117, "86": 1132, "87": 1145, "88": 1154, "89": 1171, "90": 1183, "91": 1192, "92": 1205, "93": 1212, "94": 1222, "95": 1232, "96": 1241, "97": 1255, "98": 1264, "99": 1282, "100": 1300, "101": 1309, "102": 1319, "103": 1338, "104": 1348, "105": 1360, "106": 1378}
---

**Dave Jones:** Hi, today we're going to take a look at an open source Bitcoin miner from DTV Electronics and it's the Bit Axe Ultra here. It's a 99 Yankee bucks and it's actually um fully open source.

**Dave Jones:** This is an OSMU project Open Source Miners United. Yes. Um by purchasing this product you are supporting the great work of engineers, developers, and designers in the open source mining space.

**Dave Jones:** More info at osmu.wiki. I'll link it in down below. Established in Bitcoin block 723,420. So for 99 bucks, you're not going to get much hashing capability. I believe this one's about 500 gigahashes and we'll talk about that later, but it's a nice little introduction if you want to you know find out what Bitcoin mining is, you know, experiment with it.

**Dave Jones:** Doesn't take a lot of power. It's only 15 watts or something like that. So um yeah, it's just a you know, nice introduction if you want to figure out what the whole Bitcoin mining thing's about.

**Dave Jones:** And it uses an ASIC uh Bitcoin miner chip which is used in the Antminer machines. The Antminers are kind of like you know, one of the like the gold standard in mining ASIC mining machines.

**Dave Jones:** So the company is Bitmain. Unfortunately, there's not really any public data sheet or info on the chip used in this, but this is otherwise all open source and people have like you know, reverse engineered it and you know, they they figured out how to use it and they've written their own Bit Axe OS for this thing.

**Dave Jones:** So it's supposed to be like really simple to set up and use. Let's give it a burl. Okay, so let's unbox it and see what we get here and for our 99 bucks, register 12 months warranty inside.

**Dave Jones:** Beautiful. There you go. Thanks in various languages. Excellent. We get a plug pack with yes, the Aussie adapter with the approved installation. Of course, we get with some of these weird ass bloody ones as well.

**Dave Jones:** Look at them all. Oh, unbelievable. We've got ourselves a 25 W plug pack there cuz this is supposed to be like 18 W. So, uh yeah, no well, does that Yes, does that go in there?

**Dave Jones:** Clips in. Beauty. All right. So, that's uh 5 V at uh 5 A and there you go. If you overclock or adjust the default settings, it will invalidate the product's warranty.

**Dave Jones:** So, overclock at your own risk. But there you go. It's very cute and uh oh, reset and boot. Oh, they're not there. You have to really get in there sideways.

**Dave Jones:** They're PCB mount um reset and boot switches. Yeah, cuz you don't want to accidentally touch those. So, that's actually good thinking to actually not have them vertically on the outside, but have them horizontal on the PCB like that.

**Dave Jones:** That's neat. We've got a little fan on there. Uh you could uh well, don't know how noisy it is. We'll find out. But uh anyway, you could could replace it with a better fan.

**Dave Jones:** But uh but there you go. Woah. Got a little display and that's it. Um there's no Ethernets because it's all uh Wi-Fi based. Beauty. And you know what we say here at the EE EVblog, don't turn it on, TAKE IT APART.

**Dave Jones:** THERE YOU GO. We're in like Flynn. There is the base of the board there. And of course, this is um all um open-source stuff. So, you can actually um build this yourself.

**Dave Jones:** But anyway, let's take a look at the top here. And um yeah, I won't go taking off the heat sink. But uh the main um ASIC is under there and that's it.

**Dave Jones:** And they've got an expressive um ESP32 uh Wi-Fi module on there. There you go. For those playing along at home. And just a little um OLED uh display. And Bob's your uncle.

**Dave Jones:** So, yeah, really simple. Either a USB-C or DC barrel jack. Nice implementation. I like it. Um I wonder if you could turn I wonder what heatsink would be required to actually turn this into like a completely passive thing where you wouldn't need, you know, would you need a heatsink like this big or something to, you know, probably.

**Dave Jones:** Anyway, that's beyond the scope of this video. And metal threaded inserts, nice. So, they make sure you read that before you peel it off. Oh, come on. And that's a what what what what?

**Dave Jones:** That's unbelievable. No, get a better sticker than that. Absolute fail. God, unbelievable. Before I go, it's even going to go into the bloody USB connector. You got to be kidding me.

**Dave Jones:** Going to need the giant knife for that. Come on. You turd. So, we'll just power it on. Oops. Screen's a bit little bit how you doing? There you go.

**Dave Jones:** Wi-Fi, no no AP access point found. Wi-Fi for setup once. So, yeah, we're going to set this sucker up. Now, because I don't actually have Wi-Fi on my desktop PC here, I had to use my shoe phone here to actually connect to the this is a Wi-Fi access point basically.

**Dave Jones:** So, you connect to that and then you do 168 192.168.4.1 and then it just loads it up. Bitaxe. Okay, so they're grayed out the SSID and password. So, I'll have to enter my local Wi-Fi password here and that's where it's going to connect to cuz this thing needs the internet.

**Dave Jones:** So, it's just its own access point when you're setting the thing up. And you'll set up the pool in here as well, I think if you want to use a pool.

**Dave Jones:** I think we might have missed that, but yeah, it says it was connected to my Wi-Fi hotspot. So, yeah, you missed it there. That was actually connecting to my my Wi-Fi hotspot and are we mining already?

**Dave Jones:** I think we're mining. Stratum host public pool io, okay? bitax IP 1921680152. So, that's the one I'll be able It's at 42°. Probably rising. And 300 gigahashes per second.

**Dave Jones:** And that's uh joules per terahash, is it? Stratum host public pool.io, which is where it is by default. But you can um you don't have to use the uh pool if you don't want to.

**Dave Jones:** So, um I'm going to go to 152. And sure enough, I am in on the uh web browser. I'll go um I'll actually do that tomorrow cuz it's very late at night here.

**Dave Jones:** So, I'm actually going to leave that running. That was incredibly easy and simple to set up. And there it is, 400 uh gigahashes uh per second there. And um yeah, I am mining.

**Dave Jones:** Like it's my you know, so I really hardly had to set up anything there. It was just basically set up my Wi-Fi connection. And that was it. Bob's your uncle.

**Dave Jones:** Um and it's mining. So, yeah. I It's very late here at the lab, so I'm headed home. And I'll come back tomorrow. And we'll see what's happening. But I can already see um what's happening on the uh browser over there.

**Dave Jones:** See you tomorrow. So, that next day turned into a couple of months later. Um so, I'm shooting this a couple of months later. You know, uh things just got in the way.

**Dave Jones:** And anyway, I've been ha- I've had this uh bitax running like in the background in the corner and tucked away in the corner of my lab for the last couple of months.

**Dave Jones:** Um so, we can actually have a look at the uh data for this thing to see how much we've earned from cuz that's what everyone cares about, right? How much you actually earn from this thing.

**Dave Jones:** And buckle up, Dorothy. It's Kansas is going bye-bye. So, here's the bitax uh OS. Here you just get a web page out of the thing. You just go to the um local IP address here.

**Dave Jones:** It's very nice. Um and uh so, it actually hasn't been running continuously for the last couple of months. It looks like it's shut off a couple of weeks ago or something for some reason.

**Dave Jones:** I don't know. Maybe I unplugged it or did something dumb or maybe it locked up. I don't know. So, I plugged it in 31 minutes ago and this is what it's been doing.

**Dave Jones:** Okay? So, the hash rate is around about 440 gigahashes per second. And when you're talking about mining, crypto mining, you're talking about how many hashes. And a hash is like solving a mathematical problem.

**Dave Jones:** So, what a hash is is basically a mathematical computation, a mathematical guess on what to solve each Bitcoin block. And because of the astronomical odds involved in actually guessing Bitcoin correctly guessing a Bitcoin block to actually solve a Bitcoin block.

**Dave Jones:** And if you're able to personally solve a Bitcoin block due to just that one single computation, you just happen to guess it, then you're actually rewarded with not just one Bitcoin, but it actually keeps going up.

**Dave Jones:** I think the current reward is like 3.1 or 3.2 Bitcoins or something like that. So, with each Bitcoin being worth like 100,000 US dollars, there's a lot of money involved here if you can just solve one block.

**Dave Jones:** And you can technically do that with your tiny little piss ant bit axe here. It's it's certainly possible. But you only get that if you're solo mining, which we'll talk about.

**Dave Jones:** So, we're actually running well, it's just dropped down a bit. It did like it varies all over the shop as you can see here. Like this is a live it can get up to like 530 gigahashes per second.

**Dave Jones:** So, it's running 3 533 * 10 to the power of nine hashes computations per second. And that's how fast these ASIC miner chips is. And this is just the runt of the litter.

**Dave Jones:** This is just like a little itty-bitty tiny and just one ASIC chip. And you can actually pull the big ASIC miners, um, like boxes, they actually have like hundreds of these chips in them all, uh, burning away at once.

**Dave Jones:** And yeah, so it's doing a lot of computations per second, but even that is not Sounds like a lot, but it's not. To solve an average Bitcoin block, it's like 10 to the power of 32 hashes or something like that.

**Dave Jones:** That's why everyone's got to combine all of their, um, hashing power together to try and solve a block, but we'll talk about that in a minute. So, the goal is to solve a Bitcoin block, and basically you have one in So, every time you do a computation with your little ASIC chip here or your GPU miner or CPU miner or whatever it is, every time you do one of

**Dave Jones:** those computations, you have a chance. You have a chance of solving a Bitcoin block. You have one in the power of 10 to the 32 or something like that average chances, but there's a chance.

**Dave Jones:** >> So, you're telling me there's a chance? YEAH! >> SO, IT'S POSSIBLE at any moment for my little piddly seven I think it's dropped down to $79 $79 US ASIC miner here.

**Dave Jones:** I've got 358 * 10 to the power of nine chances per second of solving that Bitcoin block. But, the odds are so astronomically high that the odds of me solving one, uh, and I've been had this thing running for months and I have not solved any Bitcoin block, obviously, um, because it's it's just mathematically insanely, um, unlikely that I'm going to do it.

**Dave Jones:** But, DTV, um, the manufacturer of this actually sold me that told me that, um, I think somebody actually did solve a block with one of these things. Um, with a Bitaxe.

**Dave Jones:** I don't know if it was their one, but the whole Bitaxe community cuz it's open source, you know, there's many different companies making these bit axe things. This is just, you know, one of them.

**Dave Jones:** And I I do believe a bit axe somewhere has actually solved a block. So, hats off. So, the interface is really cool here. We can see the ASIC temperature here.

**Dave Jones:** The fan's a little bit noisy. So, you know, you wouldn't want to run it in a completely quiet office. It might and it ramps up and down. It's temperature temperature controlled, but you know, it's not running that hot.

**Dave Jones:** It's running at 2,900 RPM here. You know, it's got all the stats. Everything's cool and dandy. But, now we have to talk about the difference between pool mining and solo mining, cuz there's a huge difference.

**Dave Jones:** And what I've been doing for the last couple of months is pool mining. Just to show you how much we can earn with this thing. So, we're in the pool mining settings here and there's many different pools that you can join.

**Dave Jones:** A pool is just like a website where like you can join and then you can combine your computational hashing power with everyone else. And then, if somebody in your pool of miners solves a block, then you will split that evenly based on how much computational power that you've actually put in.

**Dave Jones:** So, the downside of pool mining is that if it's your little bit axe here that happens to solve the block, because only you know, it's it's not the combined resources.

**Dave Jones:** It's it's one little computer with one computation that just guesses and solves the Bitcoin block, you don't get the entire Bitcoin. It's split up with everyone else. So, that's the disadvantage.

**Dave Jones:** So, pool mining is guaranteed that you're only going to earn a pittance, really. And it pretty much is a pittance these days. So, I there's many different pools out there.

**Dave Jones:** I've just joined this one that they recommended Ocean. So, if we go into the ocean.xyz pool website over here, we can see that I've been you know mining this thing for months.

**Dave Jones:** So I think it looks like it actually shut off in 1st of November. I'm not sure why and I didn't notice cuz it was tucked away in the corner of my lab.

**Dave Jones:** But you can see that my minor has been contributing to the pool here and it's currently offline cuz I don't think it's reported back yet cuz I've only had it on for half an hour.

**Dave Jones:** But anyway, the pool I belong to has actually solved some blocks. So I actually do have I actually did get a share of this and my lifetime earnings here my lifetime earnings for the last couple of months is .00002801 BTC Bitcoin.

**Dave Jones:** And there's a reason why Bitcoin is always displayed with eight decimal places here like this. It's because that least significant digit there that is one Satoshi it's called after named after Satoshi Nakamoto who basically developed Bitcoin.

**Dave Jones:** So nobody knows who Satoshi Nakamoto is but as we say in the Bitcoin field we're all Satoshi. So we can actually change that to display in sats or sats as or satoshis as they're called.

**Dave Jones:** So yeah, I've earned 2801 satoshis. What's that worth in Yankee bucks? You want to know for my couple of months of effort expending my 15 watts or whatever it is about two bucks 60 US.

**Dave Jones:** So yeah, it ain't much. You're not going to get rich by pool mining Bitcoin. In fact, even if you have free power available it can almost not be worth the hassle of pool mining.

**Dave Jones:** Let me show you some numbers. There's a ton of different profitability calculators that you can use online to calculate how much you're going to earn with your computational power roughly.

**Dave Jones:** So we can choose our algorithm here which which SHA256. We can put in our um hash rate, which is 500. It's not peta hashes, it's not exa hashes, it's giga hashes um because we're right down in the run to the litter of Bitcoin mining.

**Dave Jones:** And uh we can calculate here. And as you can see, approximate income if you join NiceHash, that's just a pool mining uh website. Um yeah, basically um you can earn 2 cents a day.

**Dave Jones:** 2 cents a day. Yeah, it ain't much, BUT OH, LOOK AT ME. I'M GOING TO USE it with my GPU. I've got an Nvidia RTX 5090 here. Is that the Is that the super duper latest?

**Dave Jones:** I don't know. I don't keep up. Let's calculate what happens if you're thrashing your um RTX 5090 GPU. How much will we get? How much will we earn? What what what what 62 cents a day.

**Dave Jones:** Um so yeah, as I said, even if you've got free power available to thrash a top-of-the-line Nvidia GPU like this, um 62 cents a day? Why would you bother?

**Dave Jones:** It's not worth your time and effort, really. So um yeah, pool mining is is pretty how you do it. It's I don't recommend uh pool mining, but I just wanted to show you that that's the kind of thing we're talking about here.

**Dave Jones:** It's just It's practically not worth it. So here's another calculator here, uh 500 gigahashes per second, which is the average of what we're going to do with our little uh Bit Axe here.

**Dave Jones:** Even if you've got paying for zero power, um then yeah, like 30 cents a month. Yeah, it's it's I've earned $2.60, okay? So it's it's not much at all.

**Dave Jones:** And and then if your power consumption is 15 watts, and then your cost is, say, 30 cents per kilowatt-hour, um we're losing money. We're losing money. So I've actually probably lost money on this thing.

**Dave Jones:** Oops. So, anyway, if you did want to run multiple ones of these, you can like actually have a swarm of these. So, you can join it together. That's pretty cool.

**Dave Jones:** And also, the you can like download like the latest firmware and stuff like that directly from the web interface. So, it's it's pretty nice. I like it. So, as you've seen, pool mining is pretty how you doing.

**Dave Jones:** It's really not worth the effort. You're not going to make any money with it, even if you've got free power. It's pretty much not worth your time or effort.

**Dave Jones:** So, what you're better off doing with Bitcoin mining is just like going for that Hail Mary shot of your particular device actually solving one of the blocks just by pure luck.

**Dave Jones:** And if you run enough computational power for long enough, you might get lucky. So, how you do solo mining is once again, you can do it using a website.

**Dave Jones:** And there's many solo mining websites out. The one I'm just going to happen to use here is ausolo.ckpool.org. It's actually solo being because I'm I'm in Australia, I'm using the Australian specific one, but it's solo.ckpool.org.

**Dave Jones:** And they will take a 2% fee if you happen to find the block, but it's probably worth it because we can't actually run on this hardware, we can't actually run a full Bitcoin node on there.

**Dave Jones:** Like if you were doing solo Bitcoin mining on your own machine, like your own super powerful machine at home, then you would run like you might want to run a full Bitcoin node on it, but that requires a large amount of computational space to run the entire Bitcoin node on your machine.

**Dave Jones:** So, a little ASIC miner here, we're going to use a solo pool. So, all we do is put in the host address here, the stratum port, and then the stratum user is your particular Bitcoin address.

**Dave Jones:** Don't use the Bitcoin address in the example cuz that's their one. Put in your particular Bitcoin address, your Bitcoin wallet address in there, and the backup is just the same.

**Dave Jones:** And we And I saved that and restarted that. So, if we go into the dashboard, so I am now solo mining at 500 gigahashes per second. There's still a chance I might actually get a block if I run this for 1,000 years, I might eventually get a block.

**Dave Jones:** But, I might get lucky. It could happen in in the next minute. Who knows? And then I can put my particular Bitcoin address into um this solo pool statistics thing, and you can see that it's actually running here.

**Dave Jones:** So, I know that this is going to pay out to my particular address if I happen to find a block minus their little 2% cut, which I'm happy for them to take.

**Dave Jones:** I guess I'll just sit here and twiddle my thumbs and hope for the best. Anyway, that's a quick look at the Bitaxe. Thank you very much, DTV Electronics, for sending that in.

**Dave Jones:** It's pretty neat. So, if you want to like just like experiment with what Bitcoin's all about. Bitcoin, of course, is not just about mining. You don't have to be involved in the mining side.

**Dave Jones:** But, if you're interested in Bitcoin mining at all, either solo or pool mining, this is a cheap and simple way to get into it. It's all open source, everything else.

**Dave Jones:** So, it's, you know, there's a huge community out there of solo and pool miners and Bitaxe people who develop the hardware and the software for this sort of thing.

**Dave Jones:** You can even contribute to that if you want. So, yeah, it's pretty cool. It's all available on the GitHub's here. You can download. It's got schematics and the manufacturing files.

**Dave Jones:** You can make your own. The Bitaxe Ultra is currently the most used model. There you go. So, it's all there. Hats off. It's great. And it's pretty cheap, you know, 79 Yankee bucks if you want to experiment with little home mining and, you know, only draws 15 watts.

**Dave Jones:** But, allows you to experiment with the system and how it all works and everything else. If you're want to If you're interested or curious about the mining. So, yeah, it's really cool.

**Dave Jones:** I'll let you know if I ever find a block and I cash in and because I technically do have access to free power, I I should be running like a whole bunch of old graphics cards and things and flogging them away, you know, using free power and trying to get hoping to get that Bitcoin.

**Dave Jones:** But of course you don't have to do any of that. You can just go out there and buy coins and by the way, down below evlog.store I do actually accept many different forms of crypto including including Bitcoin on my evlog.store store and you'll get a discount as well if you pay with crypto.

**Dave Jones:** So, check that out. So, instead of holding you can convert your coins into a very nice multimeter and I'll take the coins off your hands. Thank you very much.

**Dave Jones:** Just as an aside, because I've been in the crypto space for quite a little while now, a lot of people ask me what coins do I personally hold? What coins do I hoddle?

**Dave Jones:** Yes, I do hoddle. I personally hold Bitcoin, Ethereum, Ripple XRP, Cardano, Ada, Bitcoin Cash. I've got some Litecoin. Basically a lot of the top ones out there. I don't hold the shitcoins at all.

**Dave Jones:** So, yeah, I don't recommend you get involved in shitcoins at all. But there's like, you know, basically all of the top coins there, they're they're going to survive and they have a big future.

**Dave Jones:** But I don't recommend any particular coin at all except original Bitcoin. So, anyway, so anyway, that's very cool. I do recommend getting into crypto. It is the future regardless of what people say.

**Dave Jones:** You can think whatever you want, but unfortunately it's going to be in your future. So, you're better off getting used to it because whether you like it or not, I can pretty much guarantee that some of your retirement savings are already invested in Bitcoins, Bitcoin ETFs and all sorts of things.

**Dave Jones:** So, yeah, I wouldn't laugh at it. Um you're already invested in it. Anyway, thoughts and comments down below. Catch you next time.
