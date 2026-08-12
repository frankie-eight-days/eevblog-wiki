---
video_id: cnoN2gtT4iM
title: EEVblog 1627 - Electronex: Engineering Consulting with Xentronics
url: https://www.youtube.com/watch?v=cnoN2gtT4iM
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 0, "2": 30, "3": 30, "4": 57, "5": 57, "6": 57, "7": 87, "8": 117, "9": 123, "10": 123, "11": 147, "12": 163, "13": 176, "14": 204, "15": 214, "16": 236, "17": 250, "18": 273, "19": 287, "20": 307, "21": 326, "22": 342, "23": 356, "24": 375, "25": 392, "26": 410, "27": 426, "28": 443, "29": 460, "30": 472, "31": 489, "32": 502, "33": 514, "34": 528, "35": 541, "36": 557, "37": 575, "38": 589, "39": 608, "40": 622, "41": 638, "42": 653, "43": 665, "44": 684, "45": 696, "46": 707, "47": 724, "48": 739, "49": 754, "50": 768, "51": 783, "52": 793, "53": 808, "54": 814, "55": 826, "56": 838, "57": 850}
---

**Dave Jones:** Hi, I'm here at Electronics and I'm at the Zentronics stand. And for those Amp Hour viewers, you might recognize, well, you won't recognize, here's the face to the name, Scott Williams from Zentronics, founder and CEO of Zentronics. And we've got, I'll link it in down below, great one hour episode.

**Dave Jones:** In fact, you've been on twice, once with me and once with Chris. So talking about test engineering and consulting, everything else. Right. Okay, let's pick it up. Because how long ago did we do it? About a year now, I think. About a year?

**Dave Jones:** Has anything happened in the last year? You got more employees? A lot has happened, yeah. Yeah? Tell us. Yeah, at the time, I think we were about five or six employees. And if you count an intern who started with us recently, we're now at 10 people, which is pretty crazy.

**Dave Jones:** Going through a bit of a growth phase. And it's always that thing now we want to just stabilize and work on, right? How do we maintain the quality? How do we keep doing projects the same way, producing the same output without running away with it?

**Dave Jones:** By quality, do you mean quality of the designs? Quality of the design, consistency of output, right? So as an owner, I'm at the top here. I don't really understand anymore, every project, what's going on with every engineer and every developer. I can't check every bit of work that goes out the door.

**Dave Jones:** And that's where things like a project manager come into play. But you want a project manager who knows your industry, knows your feel and knows what I expect and what someone's capable of. So it's a bit tricky, but we found someone who suits that role.

**Dave Jones:** So introducing that into the business now, I think, is going to be a lot of fun. As well as, as you'll see there, his background is actually systems engineering. Systems engineering is an interesting one that not a lot of people know about. But you realize when you understand it, you can't create a product in any industry without systems engineering.

**Dave Jones:** Requirements, verification, testing, baselining, all of these things that terminologies people throw around. But unless you actually have a proper system in place for it, you're just not going to be producing consistent stuff. And most of your clients, I would imagine that most of your clients don't just want

**Dave Jones:** a bare, like, don't just want a circuit and a bare PCB design. They want a, like a turnkey solution. That's where I started, right? When I was freelancing for two years, that's where I started. And it slowly became, oh, can you do firmware as well?

**Dave Jones:** Or, oh, can you take this into production for me as well? Or, I don't have a sensor that I want you to design. I just want a user need, right? So I want customers to be able to send data over here, but they don't know if it's Bluetooth.

**Dave Jones:** Is it Wi-Fi? Is it 4G? That's actually the start of systems engineering. Going from a stakeholder need into requirements. And it's a whole field, a whole thing that it really opens your eyes up to how much things can go wrong and how to control it.

**Dave Jones:** So it goes right. And that's, I guess, as we continue to grow and create some more awesome products for clients, it's a big, big next step for us. So what's your average client? How long does a job take? Is it six months? Is it a year?

**Dave Jones:** Is it a multi-year thing that they contract you for? Yeah, yeah. So interesting question. So from an idea. To a product on the market, we're pretty agile, but even with our agility, still about a year, right? For any given, give or take an average thing.

**Dave Jones:** You got big chunks of time like prototype manufacturing, tooling, production setup. These are big one month, two month, three month blocks of time you can't do anything about. So about a year, I'd say, if it's got a lot of software integration technology like this one here, for example.

**Dave Jones:** Oh, you've done the whole lot? We did the whole lot. Not the mechanical design. Oh, I was going to say, right. Do you do like... We don't do mechanical. That's where I've drawn the line, right? Industrial and mechanical design. You've drawn the line at that.

**Dave Jones:** So you don't even want to get... No, no. I find... Too specialised? It's not that it's specialised, so to speak. It's just a completely different way of working, right? You're thinking creative, you're thinking branding, you're thinking feel, mood boards, touch points. We could probably, maybe five years time, hire a mechanical engineer when it's those systems where we want to think about...

**Dave Jones:** Thermal capacity and how do we integrate it into a product. But industrial and product design, producing an award-winning, this is an award-winning product, there's no way we could just hire someone and they can do that as well, right? That reminds me, I used to work at Keycorp back in the early 90s and they had one of the sexiest flat screen, I used to work in the flat screen division, one of the sexiest flat screen monitors on the, you know, all the others were like square boxes and this thing was very much like this.

**Dave Jones:** Does this tilt? Yeah, yeah, yeah, yeah, yeah, yeah, it tilts, yeah, it was, it was even, like, it was really curvy and, like, it was really sexy, so... And there's so much that goes in at the start when it's just an idea, it's sketches, it's drawings, like, you can't just hire someone and they do that.

**Dave Jones:** It's not that simple, so... Right, okay. So you leave that up to the customer and they'd either do that in-house or they'd hire their own... Yeah, so in this, in the case... Design consultant or whatever. Exactly, so this, for the case of this one, it was a really good fit.

**Dave Jones:** The customer was only one person, okay? He had funding. Oh, really? It was a CSIRO spin-out. Okay, nice. Yeah, so, based in Canberra, these are the PCBs inside, you can see... Oh, okay, right. These are my designs, so you can see we've got a few things, like a H-bridge here for Peltier, so heating and cooling, so we can do either.

**Dave Jones:** A few, like, basic analog... Why does this need to heat and cool? What is it, some sort of printer thing? So, taking a step back, this is a dairy diagnostics device. Oh, oh, wow, look at that. So, you open the lid, you put in your milk sample, which has, mixes the reagent, you go in here, you run your test,

**Dave Jones:** I think we have a demo profile set up, you start your test, yes, go ahead, so it gives you the instructions. So, all of the software you see here, we developed as well. Again, though, we didn't do the UX of this, the same company that did the product design of this, they're called Tricycle Developments, they did the UX.

**Dave Jones:** So, we actually have a really good fit where we would do the implementation of a lot of the functions, but they would do the concept work on how should it work, how should it look. So, we go in here and we, the thing starts, it says prepare the milk, go through, we open the lid,

**Dave Jones:** close the lid, initialize, and this will go through a thermal cycle, and then inside of this, it has effectively a photon counter with a blue and green channel, and this measures the ratio of those, applies some very specialized formulas and algorithms, and then gives you basically a go/no-go on the quality of the milk sample.

**Dave Jones:** Right, so it just shines a various filtered light through, and then uses a, how many photons get through? Millions and millions, millions and millions, it's just different spectrums, right? Oh, okay, right, got it. So, yeah, this is, and this is the primary market for this, is UHT, long life.

**Dave Jones:** Oh, yes, long life, okay. Yeah, so there's certain diseases and viruses that if the cow has those, even if you package it correctly, it'll still curdle, it'll still go off. So, yeah, this is it, that's just one idea, that was one of the first products where we did the software, firmware, and hardware.

**Dave Jones:** This one's quite old. Yeah, about two or three years old, this one. Oh, okay, right, okay, can you show us some other examples? Absolutely, so let's go over here. This one's an interesting one, so this one's an example of like an automotive product, so we don't do automotive products in the traditional sense,

**Dave Jones:** because that's a very niche, specialised industry, you know, you're talking about every cent counts, millions of units. What we do is more aftermarket products, stuff that will bolt onto an automotive vehicle once it comes from a manufacturer. Like a consumer vehicle, or would you do fire trucks, ambulances?

**Dave Jones:** Yeah, right, exactly right, so in the case of this, police cars. The example here is more like, yeah, something that might be like a fire and rescue truck or a utility truck, for example. And as you see here, this would be in the cab, this is effectively the body controller, and throughout the vehicle you have these nodes.

**Dave Jones:** And pretty straightforward, these are just a bunch of inputs and outputs, that's all they are, they're an extension of it. But these obviously have overcurrent protection, automotive transient protection, overvoltage protection on all the inputs and outputs. And all the circuitry's on the bottom, is it?

**Dave Jones:** Or is it not? There's some stuff over here, yeah, there's stuff there, and then on the bottom you can see there's a bunch of the microcontroller and hand transceiver and a few other things, this is one of my designs as well. Excellent, and they're waterproof connectors too, aren't they?

**Dave Jones:** Yeah, these are really nice, Deutsch ones, you can see the, yeah, the little rubber on the bottom there, really nice, actually you'll like this detail, I'll show it to you on camera, even the pins are marked inside the connector, pin 1 and pin 2.

**Dave Jones:** Oh, are they? I think I might be able to see that, yeah. Pretty nice, pretty nice detail. Oh, excellent, yep, impressive. Good for harness manufacturing, as you would know, harness manufacturing is pretty complicated. Oh, I know all about harnesses, oh bloody, oh yes, harnesses.

**Dave Jones:** Speaking of microcontrollers, do you have your preferred one? A standard, a go-to. Do you, what does your go-to, because I do know you use Altium, I think, I don't know if I asked you this on the Amp Hour or not, but no, okay, what does your go-to micro?

**Dave Jones:** Yeah, so as a jelly bean, I'm going to call it that, STM, that's our jelly bean go-to. A mix of us have experience with it and it's worked really well, primarily me, though, because I used to do hardware and firmware in the early days.

**Dave Jones:** I was going to ask, is that the reason that because you already had experience with it, it's what you use? Effectively, yeah, and that's trickled down to the rest of the embedded team now. However, if there's any amount of Wi-Fi in the system, ESP32, go-to, right, they're super powerful, a dollar each, crazy, crazy.

**Dave Jones:** Hard, almost impossible to beat. Likewise, Bluetooth, Silicon Labs have a great range, Ryan has a lot of experience with them, my preference is Nordic, the NRF series, we've got a good relationship with them locally, that support with the vendors, that's actually more important than the functionality, a lot of people don't realise that.

**Dave Jones:** And then, look, there might be occasions when we go outside of that space, like if it's, not in this case, but if it's an automotive product where it might be really critical for safety reasons, I think like Texas Instruments have a range that's specifically designed around that,

**Dave Jones:** or very high temperatures or high reliability, but on the whole, that's the mix of that. We've got a few projects where it might have like 4G, for example, and in some cases, we'll have like, I mentioned an STM and a 4G modem separate,

**Dave Jones:** this is the traditional sort of architecture, and it works really well, you can kind of have these buckets of things, they're blocks, you can copy and paste them, but more modern products where size is driven, cost is driven, Nordic, for example, have a 4G modem,

**Dave Jones:** but it's the microcontroller as well, like the ESP32. And we've started to explore some projects with that, and that's starting to pay off too. So there's always trade-offs and benefits, of course, in any decision, but leveraging what you already know, that's actually the most important trade-off, especially when you're a consultancy like us.

**Dave Jones:** Every hour counts, every hour is costing the customer. - Yes, and how do you typically bill? Is that up to, or do you flexible for the client, or is it like hourly? Do you do a job thing, which is better, pro cons? - Yeah, yeah, no, absolutely.

**Dave Jones:** - Because there's a lot of people who want to get into the company, they want to get into the consulting design business. - What I will say is when you're starting out, you've got to take what you can get, right? I think I mentioned on the amp hour, there were projects that, you know, even this one here,

**Dave Jones:** this is my first project, so I'm really passionate about this one. - Oh, yeah, that's your very first consulting job? - Yeah, yeah, it's like a trainer, so these are, with like a laser gun, you train your accuracy and things, ESP32. Now in this case, this was like fixed price, maybe $1,000, something like that, to do this whole design.

**Dave Jones:** There's no way, just to think about this design is $1,000. - You will work in a $5 an hour or something, $10 an hour or something. - Yep, absolutely. A lot's changed since then, and of course, as I also mentioned, as we've scaled, there's these trade-offs, right?

**Dave Jones:** If it's a really important client, like a brand name client that we want to work with and be a part of, or it's got hardware and software and firmware, we might commit to a fixed price. We want to be a part of that.

**Dave Jones:** There's value exchange there. Nowadays, though, we're pretty well established, we're in high demand, we're doing a great job, reducing quality outputs. Pretty much every project, we'll estimate it, we'll justify our estimates. If the cost needs to go up, we'll give clear reasons why and why we didn't predict that,

**Dave Jones:** but we never promise anything on a fixed price, and that's where you want to get to as a consultancy. - Yeah, you want the luxury to be able to turn down clients you think are going to be a hassle. - Yeah, yeah, or as unfortunate as it is, if there's a complication with the project,

**Dave Jones:** the clients are the ones who have the idea, they have to take the trickle-down risk. We need another $10,000, we're going to have to get another $10,000 of funding, whatever it might be. There's always going to be exceptions, so back to that value exchange.

**Dave Jones:** Say, government projects, that will never be open. That will be a fixed budget, you will go out of business if you mess that up, right? And I'm not against doing those, it's just, when's a good time, when's it going to be a good fit?

**Dave Jones:** - How hard is that phone call, you've got to phone them up and say, "This is way harder than we thought"? And that's the sort of stuff that, you can get coaching, you can learn how to run a business, you can get support from your team, but that's the stuff that's the real art.

**Dave Jones:** That's the stuff that's the real art, and a lot of it's down to, well, how have you treated the customer up to that point? Regular checking in with them, giving them updates, regular cadence, or has it been the first time you've talked in three weeks?

**Dave Jones:** - Yep, and I can imagine that would also factor into, you don't want to get into the actual 3D product design, you want to do the actual 3D product design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design,

**Dave Jones:** you want to do the actual 3D design, but that's not going to be the case. You want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design,

**Dave Jones:** you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design,

**Dave Jones:** you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design,

**Dave Jones:** you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design,

**Dave Jones:** you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design, you want to do the actual 3D design,
