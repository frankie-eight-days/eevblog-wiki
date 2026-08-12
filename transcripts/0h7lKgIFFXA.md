---
video_id: 0h7lKgIFFXA
title: BitAxe Ultra $80 Bitcoin ASIC Miner REVIEW
url: https://www.youtube.com/watch?v=0h7lKgIFFXA
source: youtube-asr
---

**Dave Jones:** Hi, today we're going to take a look at an open source Bitcoin miner from DTV Electronics and it's the Bit Axe Ultra here. It's a 99 Yankee bucks and it's actually um fully open source. This is an OSMU project Open Source Miners

**Dave Jones:** United. Yes. Um by purchasing this product you are supporting the great work of engineers, developers, and designers in the open source mining space. More info at osmu.wiki. I'll link it in down below. Established in Bitcoin block 723,420.

**Dave Jones:** So for 99 bucks, you're not going to get much hashing capability. I believe this one's about 500 gigahashes and we'll talk about that later, but it's a nice little introduction if you want to you know find out what Bitcoin mining is,

**Dave Jones:** you know, experiment with it. Doesn't take a lot of power. It's only 15 watts or something like that. So um yeah, it's just a you know, nice introduction if you want to figure out what the whole Bitcoin mining thing's about. And it

**Dave Jones:** uses an ASIC uh Bitcoin miner chip which is used in the Antminer machines. The Antminers are kind of like you know, one of the like the gold standard in mining ASIC mining machines. So the company is Bitmain. Unfortunately, there's not

**Dave Jones:** really any public data sheet or info on the chip used in this, but this is otherwise all open source and people have like you know, reverse engineered it and you know, they they figured out how to use it and they've written their

**Dave Jones:** own Bit Axe OS for this thing. So it's supposed to be like really simple to set up and use. Let's give it a burl. Okay, so let's unbox it and see what we get here and for our 99 bucks,

**Dave Jones:** register 12 months warranty inside. Beautiful. There you go. Thanks in various languages. Excellent. We get a plug pack with yes, the Aussie adapter with the approved installation. Of course, we get with some of these weird ass bloody ones as

**Dave Jones:** well. Look at them all. Oh, unbelievable. We've got ourselves a 25 W plug pack there cuz this is supposed to be like 18 W. So, uh yeah, no well, does that Yes, does that go in there? Clips in. Beauty. All

**Dave Jones:** right. So, that's uh 5 V at uh 5 A and there you go. If you overclock or adjust the default settings, it will invalidate the product's warranty. So, overclock at your own risk. But there you go. It's very cute and uh

**Dave Jones:** oh, reset and boot. Oh, they're not there. You have to really get in there sideways. They're PCB mount um reset and boot switches. Yeah, cuz you don't want to accidentally touch those. So, that's actually good thinking to actually not

**Dave Jones:** have them vertically on the outside, but have them horizontal on the PCB like that. That's neat. We've got a little fan on there. Uh you could uh well, don't know how noisy it is. We'll find out. But uh anyway, you could could

**Dave Jones:** replace it with a better fan. But uh but there you go. Woah. Got a little display and that's it. Um there's no Ethernets because it's all uh Wi-Fi based. Beauty. And you know what we say here at the EE

**Dave Jones:** EVblog, don't turn it on, TAKE IT APART. THERE YOU GO. We're in like Flynn. There is the base of the board there. And of course, this is um all um open-source stuff. So, you can actually um build this

**Dave Jones:** yourself. But anyway, let's take a look at the top here. And um yeah, I won't go taking off the heat sink. But uh the main um ASIC is under there and that's it. And they've got an expressive um ESP32

**Dave Jones:** uh Wi-Fi module on there. There you go. For those playing along at home. And just a little um OLED uh display. And Bob's your uncle. So, yeah, really simple. Either a USB-C or DC barrel jack. Nice implementation. I like it. Um

**Dave Jones:** I wonder if you could turn I wonder what heatsink would be required to actually turn this into like a completely passive thing where you wouldn't need, you know, would you need a heatsink like this big or something to, you know,

**Dave Jones:** probably. Anyway, that's beyond the scope of this video. And metal threaded inserts, nice. So, they make sure you read that before you peel it off. Oh, come on. And that's a what what what what? That's unbelievable. No, get a better sticker

**Dave Jones:** than that. Absolute fail. God, unbelievable. Before I go, it's even going to go into the bloody USB connector. You got to be kidding me. Going to need the giant knife for that. Come on. You turd. So, we'll just power it on. Oops.

**Dave Jones:** Screen's a bit little bit how you doing? There you go. Wi-Fi, no no AP access point found. Wi-Fi for setup once. So, yeah, we're going to set this sucker up. Now, because I don't actually have Wi-Fi on my desktop PC here, I had to use my

**Dave Jones:** shoe phone here to actually connect to the this is a Wi-Fi access point basically. So, you connect to that and then you do 168 192.168.4.1 and then it just loads it up. Bitaxe. Okay, so they're grayed out the SSID and

**Dave Jones:** password. So, I'll have to enter my local Wi-Fi password here and that's where it's going to connect to cuz this thing needs the internet. So, it's just its own access point when you're setting the thing up. And you'll set up the pool

**Dave Jones:** in here as well, I think if you want to use a pool. I think we might have missed that, but yeah, it says it was connected to my Wi-Fi hotspot. So, yeah, you missed it there. That was actually connecting to

**Dave Jones:** my my Wi-Fi hotspot and are we mining already? I think we're mining. Stratum host public pool io, okay? bitax IP 1921680152. So, that's the one I'll be able It's at 42°. Probably rising. And 300 gigahashes per second. And that's uh joules per

**Dave Jones:** terahash, is it? Stratum host public pool.io, which is where it is by default. But you can um you don't have to use the uh pool if you don't want to. So, um I'm going to go to 152. And sure enough, I am in on the uh

**Dave Jones:** web browser. I'll go um I'll actually do that tomorrow cuz it's very late at night here. So, I'm actually going to leave that running. That was incredibly easy and simple to set up. And there it is, 400 uh gigahashes uh per second

**Dave Jones:** there. And um yeah, I am mining. Like it's my you know, so I really hardly had to set up anything there. It was just basically set up my Wi-Fi connection. And that was it. Bob's your uncle. Um and it's mining. So, yeah. I It's very

**Dave Jones:** late here at the lab, so I'm headed home. And I'll come back tomorrow. And we'll see what's happening. But I can already see um what's happening on the uh browser over there. See you tomorrow. So, that next day

**Dave Jones:** turned into a couple of months later. Um so, I'm shooting this a couple of months later. You know, uh things just got in the way. And anyway, I've been ha- I've had this uh bitax running like in the

**Dave Jones:** background in the corner and tucked away in the corner of my lab for the last couple of months. Um so, we can actually have a look at the uh data for this thing to see how much we've earned from

**Dave Jones:** cuz that's what everyone cares about, right? How much you actually earn from this thing. And buckle up, Dorothy. It's Kansas is going bye-bye. So, here's the bitax uh OS. Here you just get a web page out of the

**Dave Jones:** thing. You just go to the um local IP address here. It's very nice. Um and uh so, it actually hasn't been running continuously for the last couple of months. It looks like it's shut off a couple of weeks ago or something for

**Dave Jones:** some reason. I don't know. Maybe I unplugged it or did something dumb or maybe it locked up. I don't know. So, I plugged it in 31 minutes ago and this is what it's been doing. Okay? So, the hash

**Dave Jones:** rate is around about 440 gigahashes per second. And when you're talking about mining, crypto mining, you're talking about how many hashes. And a hash is like solving a mathematical problem. So, what a hash is is basically a mathematical computation, a mathematical

**Dave Jones:** guess on what to solve each Bitcoin block. And because of the astronomical odds involved in actually guessing Bitcoin correctly guessing a Bitcoin block to actually solve a Bitcoin block. And if you're able to personally solve a Bitcoin block due to just that one

**Dave Jones:** single computation, you just happen to guess it, then you're actually rewarded with not just one Bitcoin, but it actually keeps going up. I think the current reward is like 3.1 or 3.2 Bitcoins or something like that. So, with each

**Dave Jones:** Bitcoin being worth like 100,000 US dollars, there's a lot of money involved here if you can just solve one block. And you can technically do that with your tiny little piss ant bit axe here. It's it's certainly possible. But you

**Dave Jones:** only get that if you're solo mining, which we'll talk about. So, we're actually running well, it's just dropped down a bit. It did like it varies all over the shop as you can see here. Like this is a live it can get up to like 530

**Dave Jones:** gigahashes per second. So, it's running 3 533 * 10 to the power of nine hashes computations per second. And that's how fast these ASIC miner chips is. And this is just the runt of the litter. This is just like a little itty-bitty tiny and

**Dave Jones:** just one ASIC chip. And you can actually pull the big ASIC miners, um, like boxes, they actually have like hundreds of these chips in them all, uh, burning away at once. And yeah, so it's doing a lot of computations per second, but even

**Dave Jones:** that is not Sounds like a lot, but it's not. To solve an average Bitcoin block, it's like 10 to the power of 32 hashes or something like that. That's why everyone's got to combine all of their, um, hashing power together to try and

**Dave Jones:** solve a block, but we'll talk about that in a minute. So, the goal is to solve a Bitcoin block, and basically you have one in So, every time you do a computation with your little ASIC chip here or your GPU miner or CPU miner or

**Dave Jones:** whatever it is, every time you do one of those computations, you have a chance. You have a chance of solving a Bitcoin block. You have one in the power of 10 to the 32 or something like that average

**Dave Jones:** chances, but there's a chance. >> So, you're telling me there's a chance? YEAH! >> SO, IT'S POSSIBLE at any moment for my little piddly seven I think it's dropped down to $79 $79 US ASIC miner here. I've got

**Dave Jones:** 358 * 10 to the power of nine chances per second of solving that Bitcoin block. But, the odds are so astronomically high that the odds of me solving one, uh, and I've been had this thing running for months and I have not solved any Bitcoin

**Dave Jones:** block, obviously, um, because it's it's just mathematically insanely, um, unlikely that I'm going to do it. But, DTV, um, the manufacturer of this actually sold me that told me that, um, I think somebody actually did solve a block with one of these things. Um, with

**Dave Jones:** a Bitaxe. I don't know if it was their one, but the whole Bitaxe community cuz it's open source, you know, there's many different companies making these bit axe things. This is just, you know, one of them. And I I do believe a bit axe

**Dave Jones:** somewhere has actually solved a block. So, hats off. So, the interface is really cool here. We can see the ASIC temperature here. The fan's a little bit noisy. So, you know, you wouldn't want to run it in a completely quiet office.

**Dave Jones:** It might and it ramps up and down. It's temperature temperature controlled, but you know, it's not running that hot. It's running at 2,900 RPM here. You know, it's got all the stats. Everything's cool and dandy. But, now we

**Dave Jones:** have to talk about the difference between pool mining and solo mining, cuz there's a huge difference. And what I've been doing for the last couple of months is pool mining. Just to show you how much we can earn with this thing. So,

**Dave Jones:** we're in the pool mining settings here and there's many different pools that you can join. A pool is just like a website where like you can join and then you can combine your computational hashing power with everyone else. And

**Dave Jones:** then, if somebody in your pool of miners solves a block, then you will split that evenly based on how much computational power that you've actually put in. So, the downside of pool mining is that if it's your little bit axe here that

**Dave Jones:** happens to solve the block, because only you know, it's it's not the combined resources. It's it's one little computer with one computation that just guesses and solves the Bitcoin block, you don't get the entire Bitcoin. It's split up with everyone

**Dave Jones:** else. So, that's the disadvantage. So, pool mining is guaranteed that you're only going to earn a pittance, really. And it pretty much is a pittance these days. So, I there's many different pools out there. I've just joined this one

**Dave Jones:** that they recommended Ocean. So, if we go into the ocean.xyz pool website over here, we can see that I've been you know mining this thing for months. So I think it looks like it actually shut off in 1st of November.

**Dave Jones:** I'm not sure why and I didn't notice cuz it was tucked away in the corner of my lab. But you can see that my minor has been contributing to the pool here and it's currently offline cuz I don't think

**Dave Jones:** it's reported back yet cuz I've only had it on for half an hour. But anyway, the pool I belong to has actually solved some blocks. So I actually do have I actually did get a share of this and my

**Dave Jones:** lifetime earnings here my lifetime earnings for the last couple of months is .00002801 BTC Bitcoin. And there's a reason why Bitcoin is always displayed with eight decimal places here like this. It's because that least significant digit there that is one Satoshi it's called

**Dave Jones:** after named after Satoshi Nakamoto who basically developed Bitcoin. So nobody knows who Satoshi Nakamoto is but as we say in the Bitcoin field we're all Satoshi. So we can actually change that to display in sats or sats as or satoshis as they're

**Dave Jones:** called. So yeah, I've earned 2801 satoshis. What's that worth in Yankee bucks? You want to know for my couple of months of effort expending my 15 watts or whatever it is about two bucks 60 US. So yeah, it ain't

**Dave Jones:** much. You're not going to get rich by pool mining Bitcoin. In fact, even if you have free power available it can almost not be worth the hassle of pool mining. Let me show you some numbers. There's a ton of different

**Dave Jones:** profitability calculators that you can use online to calculate how much you're going to earn with your computational power roughly. So we can choose our algorithm here which which SHA256. We can put in our um hash rate, which is

**Dave Jones:** 500. It's not peta hashes, it's not exa hashes, it's giga hashes um because we're right down in the run to the litter of Bitcoin mining. And uh we can calculate here. And as you can see, approximate income if you join NiceHash,

**Dave Jones:** that's just a pool mining uh website. Um yeah, basically um you can earn 2 cents a day. 2 cents a day. Yeah, it ain't much, BUT OH, LOOK AT ME. I'M GOING TO USE it with my GPU. I've got an Nvidia RTX 5090

**Dave Jones:** here. Is that the Is that the super duper latest? I don't know. I don't keep up. Let's calculate what happens if you're thrashing your um RTX 5090 GPU. How much will we get? How much will we earn? What what what what 62 cents a

**Dave Jones:** day. Um so yeah, as I said, even if you've got free power available to thrash a top-of-the-line Nvidia GPU like this, um 62 cents a day? Why would you bother? It's not worth your time and effort, really. So um

**Dave Jones:** yeah, pool mining is is pretty how you do it. It's I don't recommend uh pool mining, but I just wanted to show you that that's the kind of thing we're talking about here. It's just It's practically not worth it. So here's

**Dave Jones:** another calculator here, uh 500 gigahashes per second, which is the average of what we're going to do with our little uh Bit Axe here. Even if you've got paying for zero power, um then yeah, like 30 cents a month. Yeah,

**Dave Jones:** it's it's I've earned $2.60, okay? So it's it's not much at all. And and then if your power consumption is 15 watts, and then your cost is, say, 30 cents per kilowatt-hour, um we're losing money. We're losing money. So I've actually

**Dave Jones:** probably lost money on this thing. Oops. So, anyway, if you did want to run multiple ones of these, you can like actually have a swarm of these. So, you can join it together. That's pretty cool. And also, the you can like download like

**Dave Jones:** the latest firmware and stuff like that directly from the web interface. So, it's it's pretty nice. I like it. So, as you've seen, pool mining is pretty how you doing. It's really not worth the effort. You're not going to make any

**Dave Jones:** money with it, even if you've got free power. It's pretty much not worth your time or effort. So, what you're better off doing with Bitcoin mining is just like going for that Hail Mary shot of your particular device actually solving

**Dave Jones:** one of the blocks just by pure luck. And if you run enough computational power for long enough, you might get lucky. So, how you do solo mining is once again, you can do it using a website. And there's many

**Dave Jones:** solo mining websites out. The one I'm just going to happen to use here is ausolo.ckpool.org. It's actually solo being because I'm I'm in Australia, I'm using the Australian specific one, but it's solo.ckpool.org. And they will take a 2% fee if you

**Dave Jones:** happen to find the block, but it's probably worth it because we can't actually run on this hardware, we can't actually run a full Bitcoin node on there. Like if you were doing solo Bitcoin mining on your own machine, like

**Dave Jones:** your own super powerful machine at home, then you would run like you might want to run a full Bitcoin node on it, but that requires a large amount of computational space to run the entire Bitcoin node on your machine. So, a

**Dave Jones:** little ASIC miner here, we're going to use a solo pool. So, all we do is put in the host address here, the stratum port, and then the stratum user is your particular Bitcoin address. Don't use the Bitcoin address in the example cuz

**Dave Jones:** that's their one. Put in your particular Bitcoin address, your Bitcoin wallet address in there, and the backup is just the same. And we And I saved that and restarted that. So, if we go into the dashboard, so I am now

**Dave Jones:** solo mining at 500 gigahashes per second. There's still a chance I might actually get a block if I run this for 1,000 years, I might eventually get a block. But, I might get lucky. It could happen in in the next minute. Who knows?

**Dave Jones:** And then I can put my particular Bitcoin address into um this solo pool statistics thing, and you can see that it's actually running here. So, I know that this is going to pay out to my particular address if I happen to find a

**Dave Jones:** block minus their little 2% cut, which I'm happy for them to take. I guess I'll just sit here and twiddle my thumbs and hope for the best. Anyway, that's a quick look at the Bitaxe. Thank you very much, DTV Electronics, for sending that

**Dave Jones:** in. It's pretty neat. So, if you want to like just like experiment with what Bitcoin's all about. Bitcoin, of course, is not just about mining. You don't have to be involved in the mining side. But, if you're interested in Bitcoin mining

**Dave Jones:** at all, either solo or pool mining, this is a cheap and simple way to get into it. It's all open source, everything else. So, it's, you know, there's a huge community out there of solo and pool miners and Bitaxe people who develop the

**Dave Jones:** hardware and the software for this sort of thing. You can even contribute to that if you want. So, yeah, it's pretty cool. It's all available on the GitHub's here. You can download. It's got schematics and the manufacturing files.

**Dave Jones:** You can make your own. The Bitaxe Ultra is currently the most used model. There you go. So, it's all there. Hats off. It's great. And it's pretty cheap, you know, 79 Yankee bucks if you want to experiment with little home mining and,

**Dave Jones:** you know, only draws 15 watts. But, allows you to experiment with the system and how it all works and everything else. If you're want to If you're interested or curious about the mining. So, yeah, it's really cool. I'll let you

**Dave Jones:** know if I ever find a block and I cash in and because I technically do have access to free power, I I should be running like a whole bunch of old graphics cards and things and flogging them away, you know,

**Dave Jones:** using free power and trying to get hoping to get that Bitcoin. But of course you don't have to do any of that. You can just go out there and buy coins and by the way, down below evlog.store I do

**Dave Jones:** actually accept many different forms of crypto including including Bitcoin on my evlog.store store and you'll get a discount as well if you pay with crypto. So, check that out. So, instead of holding you can convert your coins into

**Dave Jones:** a very nice multimeter and I'll take the coins off your hands. Thank you very much. Just as an aside, because I've been in the crypto space for quite a little while now, a lot of people ask me what coins do I personally hold? What

**Dave Jones:** coins do I hoddle? Yes, I do hoddle. I personally hold Bitcoin, Ethereum, Ripple XRP, Cardano, Ada, Bitcoin Cash. I've got some Litecoin. Basically a lot of the top ones out there. I don't hold the shitcoins at all. So, yeah, I don't recommend you get

**Dave Jones:** involved in shitcoins at all. But there's like, you know, basically all of the top coins there, they're they're going to survive and they have a big future. But I don't recommend any particular coin at all except original Bitcoin. So, anyway, so anyway,

**Dave Jones:** that's very cool. I do recommend getting into crypto. It is the future regardless of what people say. You can think whatever you want, but unfortunately it's going to be in your future. So, you're better off getting used to it because whether you

**Dave Jones:** like it or not, I can pretty much guarantee that some of your retirement savings are already invested in Bitcoins, Bitcoin ETFs and all sorts of things. So, yeah, I wouldn't laugh at it. Um you're already invested in it. Anyway, thoughts

**Dave Jones:** and comments down below. Catch you next time.
