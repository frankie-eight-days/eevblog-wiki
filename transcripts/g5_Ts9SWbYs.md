---
video_id: g5_Ts9SWbYs
title: EEVblog 1531 - Can ChatGPT generate all the code for my Macgyver Project? (Part 3)
url: https://www.youtube.com/watch?v=g5_Ts9SWbYs
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 30, "3": 45, "4": 61, "5": 75, "6": 94, "7": 111, "8": 128, "9": 142, "10": 159, "11": 173, "12": 184, "13": 198, "14": 215, "15": 228, "16": 245, "17": 258, "18": 272, "19": 284, "20": 296, "21": 308, "22": 321, "23": 332, "24": 348, "25": 361, "26": 375, "27": 387, "28": 399, "29": 412, "30": 423, "31": 439, "32": 452, "33": 473, "34": 488, "35": 503, "36": 514, "37": 529, "38": 547, "39": 561, "40": 573, "41": 588, "42": 600, "43": 612, "44": 630, "45": 645, "46": 658, "47": 667, "48": 684, "49": 697, "50": 717, "51": 733, "52": 750, "53": 762, "54": 776, "55": 788, "56": 805, "57": 818, "58": 833, "59": 848, "60": 861, "61": 876, "62": 893, "63": 906, "64": 920, "65": 935, "66": 955, "67": 970, "68": 986, "69": 1003, "70": 1019, "71": 1028, "72": 1039, "73": 1054, "74": 1065, "75": 1079, "76": 1090, "77": 1105, "78": 1120, "79": 1136, "80": 1150, "81": 1165, "82": 1176, "83": 1189, "84": 1204, "85": 1215, "86": 1228, "87": 1239, "88": 1256, "89": 1270, "90": 1284, "91": 1298, "92": 1309, "93": 1323, "94": 1341, "95": 1356, "96": 1371, "97": 1385, "98": 1398, "99": 1410, "100": 1421, "101": 1435, "102": 1451, "103": 1464, "104": 1476, "105": 1487, "106": 1499, "107": 1513, "108": 1528, "109": 1539, "110": 1550, "111": 1564, "112": 1581, "113": 1594, "114": 1605, "115": 1617, "116": 1631, "117": 1644, "118": 1659, "119": 1672, "120": 1685, "121": 1697, "122": 1710, "123": 1724, "124": 1739, "125": 1752, "126": 1766, "127": 1780, "128": 1797, "129": 1815, "130": 1833, "131": 1848, "132": 1863, "133": 1879, "134": 1895, "135": 1914, "136": 1930, "137": 1943, "138": 1955, "139": 1968, "140": 1987, "141": 2008, "142": 2026, "143": 2039, "144": 2054, "145": 2067, "146": 2081, "147": 2096, "148": 2108, "149": 2125, "150": 2142, "151": 2157, "152": 2168, "153": 2181, "154": 2191, "155": 2201, "156": 2211, "157": 2225, "158": 2236, "159": 2248, "160": 2260, "161": 2276, "162": 2292, "163": 2305, "164": 2318, "165": 2330, "166": 2343, "167": 2356}
---

**Dave Jones:** Hi, this is part three in the MacGyver project. Sorry it's been a while. It's been six months to get around to part three. Better late than never. I'll link in part one and part two if you haven't seen it. It's where I took apart

**Dave Jones:** this gas detector, one of these industrial gas detector things and it had this really funky display on the front here that I I thought maybe that we could actually program this to do a like a countdown timer or something because this device

**Dave Jones:** kind of looks like something I won't use the keyword for because I don't want to get demonetized. So we just reverse engineered that and then we in part two down here, we actually hooked it up to a scope and we measured all sorts of

**Dave Jones:** waveforms and and did some more reverse engineering. Anyway, my plan was in part three I would actually show you how that we can design a driver for this using discrete 7400 series TTL logic. I thought that'd be really cool. Then

**Dave Jones:** maybe in part four we'd show how that we can consolidate those you know a couple of dozen TTL chips into one like single like eight-pin microcontroller that costs like 10 cents or something like that. But I've decided to jump ahead

**Dave Jones:** because I'm so excited. I want to find out if we can use AI, artificial intelligence, i.e. chat GPT. It's all the rage. I thought see if we can actually use it to design I some code that will actually drive this serial

**Dave Jones:** driver. So I've basically got the interface that we want to drive here. We've got five 74HC164 chips and these are eight-bit serial shift registers. So it it has a clock coming in here. It's got an input data pin. So on the positive going clock edge

**Dave Jones:** like this it will clock the whatever data is there through to Q0. And then on the next positive going edge like that it'll clock Q 0 through to Q 1 because if you have a look over here, this is there basically cascaded the Q

**Dave Jones:** output or the data output here is actually the then the data input for the next one here. So it's just a shift register and just shift them along. So on the actual first clock pulse, we'll call it the first clock pulse over here cuz you

**Dave Jones:** got to have like initial state that you're uh talking about. Then the data, whatever was on Q7 here, that's the data that gets shifted to Q0 here. So it's one big effectively 5/8 uh 40. It's an 8-bit shift register so 40 bits here and

**Dave Jones:** shifts all the way through like this. So we've got a common cathode uh seven-segment uh display like this. It's common cathode cuz all the cathodes uh tied together so they would go down to ground. In this particular case, it goes

**Dave Jones:** off to a pin on the board here which we can use that for like blanking and stuff like that. So when we're shifting data in, we we can actually blank the display so you don't see the data like shifting

**Dave Jones:** all the way through. Anyway, I've talked about that in a previous video. So a basic 40-bit shift register like this driving uh 40 different segments on this seven-segment display because we've got the eighth digit which is the decimal

**Dave Jones:** point here like that. And this is an actual mapping so uh Q7 here is I is segment A which is the top one there. A B B C D E F G H I J K L M N O P and

**Dave Jones:** decimal point is over here. So um yeah, we need to write some code or the AI needs to write some code. We're going to see if we can do it. That uh sends in a clock pulse like this and

**Dave Jones:** sends in the data and maps the data to the specific pins. Let's see if AI or chat GPT-3 or 3.5, I think it is at the moment, chat GPT can actually write some code to do this. It's going to be interesting. I

**Dave Jones:** haven't tried it yet. I don't know. Because chat GPT is a language-based model, let me know in the comments down below if you want me to do more videos like interacting with AI and stuff like this. I asked on Twitter,

**Dave Jones:** maybe a third of my audience is interested in that sort of uh content. Anyway, so it's a language model, so we have to try and describe this circuit in sort of like, you know, plain English so that the language model can understand.

**Dave Jones:** Now, chat GPT is capable of producing source code for almost anything. It's really good. Any basically anything on GitHub, I believe, is the source that it's taken all this stuff from. So, it can I think people have talked about it

**Dave Jones:** generating PIC code and all sorts of stuff. I've only tried it with Python code. I think I might have tried an Arduino code once. Uh yeah, it just it did work, so it can generate Arduino code. Let us know in the comments down

**Dave Jones:** below if you've actually tried to do programming. Apparently, it's it's pretty good. It's not 100% there yet, but is it going to be good enough for Australia? Is it going to be good enough for them to give it a project to

**Dave Jones:** generate this? Cuz I thought this is a real interesting example of how, you know, it's kind of tricky to word how this thing actually works. You know, we've got a 40-bit shift register, so you have to tell it to map the

**Dave Jones:** seven-segment displays and stuff. So, this is what I first came up with. I'm I'm telling it, you are writing Arduino code. So, it knows off the bat that we're writing code for Arduino and not for some other microcontroller or Python

**Dave Jones:** or whatever. And I'm going, there are two outputs because we need the clock up here and we need the data. So, I'm telling, please define two output pins. And I'm saying one is a bit clock, so I don't know if we we need the term bit in

**Dave Jones:** there, but I'm just saying it's a bit clock, so it knows it's a bit data stream, maybe? I don't know. This is all part of basically a new field called prompt engineering is the term I like to use for it. I

**Dave Jones:** don't know. You got another term? I like prompt engineering in that, you know, you have to learn how to drive these AI engines. And this is will be an incredibly valuable skill. Pro tip, highly recommend you get on it now and

**Dave Jones:** learn how to drive AI engines in terms of not only generating code, but generating all sorts of useful results. It's going to be a killer skill in the coming years, let me tell you. So, anyway, we're telling it it's a bit

**Dave Jones:** clock and the other is a data output. Okay? So, it knows it should know it's got a clock pin and a data pin. And then I'm going to say the data output connects to a 40-bit shift register that

**Dave Jones:** is connected to five I've used the word five instead of the number five, don't know if it makes a difference. I don't know. I'm I'm still relatively unskilled at this chat GPT thing. I don't know the correct sort of like syntax. And this is

**Dave Jones:** what we're going to hopefully learn here. Will it work first go or will I have to massage this or will it just, I don't know, go completely tits up? No idea. So, it's connected to five seven-segment displays with decimal

**Dave Jones:** point. So, it should know that it has seven segments plus a decimal point. So, it should know, hopefully, it's got a we're telling it it's got eight outputs. These five displays act as a five-digit counter. So, I'm telling it the function of what

**Dave Jones:** we want to do here. We we've got five seven-segment displays and we want to use it as some sort of counter. Whether it's counting up, counting down, doesn't matter. It's a counter. So, and then I'm going to say write code that will count

**Dave Jones:** down. So, I'm specifically telling it to count down on the displays once per second starting at 999999. So, well, actually, oops. That's That's too many nines. Starting at 99999. So, it should initialize the first data that comes through, it should,

**Dave Jones:** you know, have 99999 on it, and then 99998, and etc. It should count down at once per second. So, it'll be interesting to see if it actually does if it's intelligent enough to know I don't want a once per second

**Dave Jones:** clock. I don't want a 1 Hz clock because then it'd be incredibly slow. It'd take 40 seconds to update the just the display for one digit. I want it So, it should know it has to clock out at 40 times. So,

**Dave Jones:** hopefully, it should use like a 40 Hz clock to do this. I Once again, this is I think quite a challenging example. I hope you'll agree. And then I'm saying the first bit on the output is the least

**Dave Jones:** significant display digit. So, what I'm basically saying here is, as I said, on the first clock pulse that goes through is our least significant digit over here, and this is our most significant digit. God, I hate drawing with the

**Dave Jones:** mouse. So, it knows that the first bit it sends out is the one that is going to get shifted all the way across to here like this after 40 clock pulses. Now, hopefully, that's all it needs to know. Like, off the bat, I'm

**Dave Jones:** hoping that'll actually produce some sort of working code that allows us to at least, you know, base If it doesn't immediately work, then at least we can massage, at least it'll give us some sort of code base to work from, hopefully. I'd be, you

**Dave Jones:** know, if it works like first go with little massaging or no massaging required of the code, then I'll be I'll be pretty impressed. But, anyway, I don't think we need anything else. I'm not going to do blank display blanking

**Dave Jones:** or anything like that now. I just want to see if we can get clock and data to shift in. And so what I'm expecting from any generated code is to have like digits actually defined. Should have to bit map the seven segments on

**Dave Jones:** here, right? So it should like if it wants to do five, it should know it needs to turn on those segments like that or you know, number one it needs to turn on segments B and C there for

**Dave Jones:** example. And I haven't actually told it to use the decimal point at the moment. So hopefully it just ignores the decimal point, but I haven't I've told it it's the least significant digit. Now, I think I need a bit more information cuz

**Dave Jones:** I haven't mapped in the individual outputs yet, have I? So maybe I can add some more something extra. Each displaying the bit stream starts with segment A through segment G with decimal point last. Okay, so let's let's let's try that. Cross our

**Dave Jones:** fingers and see what happens. Okay, so here I am in chat GPT. Here I do actually have a paid version now. So I think I'm I'm paying per sort of like chunk of like there's a certain length of code that it will

**Dave Jones:** length of response. It doesn't care whether it's code or something else. It like a length of response costs you know, a couple of cents or something like that. Will it work? Will it magically work? I don't know. Maybe you've got a better

**Dave Jones:** idea of how you would have worded this. I haven't given it a huge amount of thought. This is just like off the top of my head how I would explain that. I think any engineer could read that and

**Dave Jones:** go, "Oh okay, I I know exactly what you want." So is chat GPT any good to do it? Let's see. An error occurred. If this issue persists, please contact us through our help center. What? What? What? What?

**Dave Jones:** Fail. Okay, I've logged out and logged back in. Let's try that. Yes. Yes. Here we go. Here's the code to achieve the desired functionality. It's going to do it. It's going to have a crack at it. Now, it's

**Dave Jones:** generated a clock pin, a data pin, it's it initial counter 99999. Pin mode, it's set up the pins. This is looking really promising. This is perfect so far. It's it's actually labeled them clock pin and data pin. Loop, shift out uh current counter value

**Dave Jones:** to the shift register. Greater than five. Five, get the current digit Oh, yeah, yeah, there's five digits, sorry. Yep, yeah, of course. Byte segment pattern get segment pattern. So, it's Yeah, okay. So, down here it here are the

**Dave Jones:** segment patterns it needs. WOW, IT'S DOING IT. Right off the bat and and delay for 1 second before decrementing the counter. Okay, I I called that. There you go, returns the binary representation of the segment pattern for the given digit. And

**Dave Jones:** if it I don't Right, I would have to map I've got to make See, this is like, you know, an annoying part of writing this code yourself. How do you like just mapping making sure you map the correct

**Dave Jones:** seven-segment displays to like in this particular case, okay? It's it's got If you want a zero, you know, it turns on Hang on, it's turns on one two Oh, I didn't tell it I didn't say anything about common cathode or

**Dave Jones:** common anode. So, if it was common anode, you would have to output a zero to turn on the LED, but it's outputting a one. So, here, if we if we want a zero to display a zero, it's going to have to

**Dave Jones:** turn on um all but two of the segments. That is correct. So, it you don't want segment uh G. Oh, I think it's back to front. Depends how it shifts it out. Yeah, but that is correct. Well, it's it's it's

**Dave Jones:** either completely back to front, or it's correct. Because the last two digits here will be segment F, which is in the middle. And if you got a zero around like that, you don't want segment F, which is in the middle. And the decimal

**Dave Jones:** point is next to segment F. So, that is correct. That is correct. And then, if you want a one, it's only turned on two segments. Yeah? This is This is correct. It looks like it hasn't done decimal point.

**Dave Jones:** Okay? Because we didn't tell it to do anything with the decimal point. That would be interesting if we could tell it add add a decimal point on the third digit or something. I wonder if we can add that code. Anyway, what does it say?

**Dave Jones:** This code uses a for loop to shift the output set the segment patterns for each digit of the counter in reverse order from least significant digit to most significant digit. That is correct with the first bit on the output being the

**Dave Jones:** last significant display digit. I still haven't got my head around if it's right or wrong yet, but it's damn close. The get segment pattern function returns the binary representation of the segment pattern for the given digit, which is

**Dave Jones:** used to shift out the corresponding segment pattern for each digit. The counter is decremented once per second using the delay function. It's It's It has done it. It's basically done it. Wow. Wow. Okay, so shift data out, data pin,

**Dave Jones:** clock pin. Yeah, I didn't tell it the polarity of the clock. And I didn't tell it on the positive I probably should have said on the positive clock edge. Okay? Because the problem here is Yeah, here is the problem. Um is that it's

**Dave Jones:** going to It's going to output the clock It's going to output the data and the clock at the same time. And you don't want that, cuz that violates setup and hold could potentially, you know, it didn't guarantee to give

**Dave Jones:** you problems, I think. Murphy's law. Right, you want some setup and hold time. So, you want to output the data pin first. You want to output the data first before the clock pin. Now, because this is and ChatGPT is a conversational-based

**Dave Jones:** system, we can tell it to modify this code, right? So, it's like we don't have to tell it from scratch again. We just tell it, "Can you change that to output the data pin first before the clock pin?"

**Dave Jones:** Certainly, here's the modified code that outputs the data pin before the clock pin. And it's got It's going to regenerate the code. Here we go. The pin mode, data pin output, and Come on. You can do it. You can do it. How much is this costing

**Dave Jones:** me probably 20 cents worth of processing time now at the Microsoft servers to to do all this. That's a fraction of what my time costs. Digital right data pin. There you go. Digital right data pin, segment pattern. Look. Look, it's it's done it. Yeah, and

**Dave Jones:** then the clock pin high low, like that. Did it initialize the clock pin? Didn't initialize the clock pin, did it? I don't think it initialized the clock pin. But jeez, that's impressive, huh? Fantastic. Wow, so we told it to modify

**Dave Jones:** that and it and it just understood exactly what we wanted and it remodified our code. That's impressive, isn't it? Some programmers might be out of a job, including like, you know, just clutsy programmers like me. Well, you're not

**Dave Jones:** actually going to be out of a job because this is just a tool that you can use to, you know, get at least get the initial code working very quickly. See, I would have spent, you know, I I don't

**Dave Jones:** know how long I would have spent just, you know, working out this you know, this bit pattern and stuff to get it just to do that alone, you know, is is like a big time saver, especially if you've got like a you know, a big thing

**Dave Jones:** that you need to do. It's kind of like that's really the monotonous part of programming is mapping stuff like that. You know, you're mapping characters, you're mapping you know, graphics and stuff like that. It's you know, it's it's it's really tedious type stuff, but

**Dave Jones:** I think this works without me having to figure out exactly whether or not it's got the bit data. People are probably already screaming in the comments, "Oh yeah, of course it's wrong. Of course it's going to work." Um but yeah, that

**Dave Jones:** that looks like that code is going to work. So, I just cut and pasted that code from chat GPT into Arduino here. You compile it and it compiles just fine. There's no errors whatsoever. It doesn't mean it's going to work, but there's no syntax

**Dave Jones:** errors. All right, let's just power it up and try it. I know this setup's a bit how you doing, but it's good enough for Australia. Now, as you saw in previous videos, we need a 2-V power source for this because there's no

**Dave Jones:** drop resistors on there and because we've got a 5-V TTL level out of the Arduino, I've had to put in a budging a resistor divider in there. So, I've just got like a 1K and a 680 or whatever and that will drop

**Dave Jones:** it down to like under 2-V to actually go to the logic on here and I've grounded the common cathode pin. So, there's no like blanking or anything like that. And I've got a 100 mA current limit. It I can't remember exactly what

**Dave Jones:** it took, but let's just try that. So, let's power it on and see what we get. Oh, hello. We've got a zero. That's interesting. All right, well let's try and capture some waveforms drawing 20 mA. The voltage hasn't dropped, so our current

**Dave Jones:** limit's good. Yeah, right off the bat didn't work. And you can say, "Well, AI failed." But well, how many times have you done a project that didn't work first go, right? Come on, admit it. Just for kicks, I'm using the new Siglent SDS

**Dave Jones:** 2354XHD. Um, got no ground connections. This is flapping around in the air, the breeze. I'm just going through the ground in of the Arduino. So, it's going to be a little bit noisy, but there you go. Um, this is our clock signal down here.

**Dave Jones:** Obviously, like I can run this real time, right? And you can probably just see, yeah, we're getting patterns like that. So, I'm single shot capturing this, and sure enough, check it out. It is It seems to be correct. We've got our

**Dave Jones:** five packets of clock pulses. It should be eight. 1 2 3 4 5 6 7 8. Yep. And there's five packets of those. So, it shifts eight for the first digit and the second, boop, etc. And then, we've got

**Dave Jones:** this turning on over here, which is in the middle, like this. Hence, why our middle digit is turning on. So, it's actually working. It's clocking the data and doing everything right, but our data's not correct. So, what what what

**Dave Jones:** what. So, let's have a look at the code here. Well, we know that the clock and data pins are working like they're mapped actually correctly and everything. Look, I'll tell you one thing I did notice here. Check this out

**Dave Jones:** down here. I like how the help here actually it pulls the comment before this. It actually knows that that comment's associated with that. I I I don't know. I haven't used Arduino in such a long time. This is

**Dave Jones:** just new to me. I think that's cool. Nice touch, whoever did that. Right, so we know our for loop is correct cuz we're getting our five clock pulses, right? So, we're getting So, So, this is working here. It's just that this

**Dave Jones:** digital write segment pattern is not working. Now, I believe this is correct, right? Cuz segment pattern, right? That just So, that's just a byte and that calls up get segment pattern down here. But, if there's no case, then it returns

**Dave Jones:** the default value of zero. Now, zero in this case, if you shifted it all out, you shift out all zeros cuz we're talking about a common cathode display here, we we need a one to drive it. So, an an individual one in here each one in

**Dave Jones:** there represents a segment on. So, a zero would be all zeros, which means all segments are off. So, it's obviously for four of those five digits, it's returning zero here. Okay, so there's nothing wrong with this. This is all the

**Dave Jones:** this switch looks all fine. Everything's hunky-dory. The here's where it gets the current digit from the counter. Okay, just quickly, what I'm going to do is I'm just going to force it digit equals what is a good mapping down here? One

**Dave Jones:** that's got ones and zeros, two. Two digit equals two. I'm just going to go digit equals two. Let's go back to the bench and just try that. So, it So, it'll ignore the previous code. It'll just force all twos. So, hopefully we

**Dave Jones:** get all twos on the display. So, let's put that back in and try out this quick hack, shall we? Output on. Bingo. Look at that. Winner winner, chicken dinner. 2 2 2 2 2. Can we get that to

**Dave Jones:** glitch? Because yeah, yeah, they are eight. Yep. Yep, there you go. All eights and then it switched to all twos. So, the chat GPT actually got that got the functionality right. Like in terms of like all the bit stuff outputting and

**Dave Jones:** there it is. There's all the clock pulses. No problems and there's the data up there. If you scroll over to the start, you can see how the data there is going in before the clock pulse actually happens. So, there's that set up time

**Dave Jones:** there. So, yeah, everything's hunky-dory. Look at that. I mean, that's a Bobby dazzler. Wow. So, all we've got to do is fix the modulo aspect of that. It It obviously goofed that up, but hey, it got the order of

**Dave Jones:** the segments right and everything. So, that's actually updating once per second. All we need to do is fix the counter. Let's go. It's using the modulo uh which is the It's a percent. It's not actually a percentage thing. It's called the modulo

**Dave Jones:** function. I can Can we call up the We can't call up the help on that. Let me get that. And here it is here. It's the remainder operation, uh which calculates the remainder when one integer is divided by another. It's useful for

**Dave Jones:** keeping a variable within a particular range, e.g., size of array. That's not what we're using it for. I've used it before to actually extract a digit from the thing. But because we've got AI, we can just ask it to try and fix it. Let's

**Dave Jones:** see if the AI can actually figure out what's wrong with it. So, how would we word this? Uh it does not get the current digit from the counter correctly. There must be something wrong with the modulo operator on the counter

**Dave Jones:** variable. Can you fix it? Uh cross your fingers, hope I've explained that correctly to it. Apologies for the mistake in the previous code. Here's the modified code that should correctly get the current digit from the counter. Let's see what

**Dave Jones:** it's done. Digit uh pow 10 integer modulo 10. And then I love how it explains itself. In this modified code, the digit variable is now calculated using counter divided by pow 10 I modulo 10 instead of counter modulo

**Dave Jones:** 10. This calculates the current digit by dividing the counter by the appropriate power of 10 and then taking the remainder after division by 10. The power function is used to calculate the appropriate power of 10 to divide by

**Dave Jones:** based on the current position in the loop. So, let's just paste that in there. We can tab that over there. And we'll just comment out those two lines there. Do that. Whoop. Oh, no, it doesn't like that. Invalid operands of

**Dave Jones:** type double in int to binary operator percent. Ah, okay. I'm going to copy that. Let's go back to the AI and see if we can use a complete AI solution to fix this. Like assuming like we like we

**Dave Jones:** don't have to analyze it. We can just like Let's Let's give it a go. I'll tell it that gave me the compile error and I copied it in there. How do I fix this? Let's Let's see if it can

**Dave Jones:** Let's see if it can get a response to that. An error occurred. Oh, yeah. Now the AI is broken. Um Great. Murphy's law. Just when I need to finish this video off. Maybe I need to upgrade to plus. I thought I was already

**Dave Jones:** on a paid plan. Is there a new one already? Well, the error is persisting. You can just imagine being on a tight deadline to finish your code and the AI breaks down. It's not like you can run copy of it. The database is too huge.

**Dave Jones:** This is why Microsoft gave them $10 billion and they had to run on Microsoft's cloud service. That's the resources are massive. Well, let me try the log out trick again. I can't even upgrade my plan. I didn't think I was on

**Dave Jones:** a free plan. I thought I was on a paid plan. I don't know. Maybe something's changed recently, but um there you go. I can't even pay for it. There you go. I've re-logged in. I do like how it keeps your response.

**Dave Jones:** Although it didn't get my response last time. So I'm going to have to put that back. Okay, let's try that again. Yes. Ah, I see the power function return It knows. The power function returns a double value, but the modulo operator

**Dave Jones:** requires integer operands. To fix this, we can cast the result of power to an integer using the int type cast operator. Here's the modified code. WOW. CHAT GPT IS absolutely like if it didn't get it right the first time, this is how

**Dave Jones:** the conversational chat This is the advantage of this. It's conversational. You don't have to start from scratch again. It knows your existing conversation. You can tell it to make changes like I've demonstrated. And now it's It made a mistake. It knew it. You

**Dave Jones:** told it you've made a mistake. Can you fix it? It fixes it. And And then it knows. And then it gives an error. And then it knows what the error is and how to fix that again. Wow, what a great example. This is This

**Dave Jones:** is absolutely terrific. So there we go. All we got to do is put the int in there. Yeah. So there you go. We'll just copy that back. So, we paste that in there like that and let's compile again.

**Dave Jones:** Yep, winner winner chicken dinner. Let's run it. Let's go back to the bench. No, all zeros. It's not our counter's not returning anything. What what what what? I should have analyzed the code more before I had a look at it. You can see

**Dave Jones:** that we're getting a clock but no data. Aha, I think I can see. Yeah, this is wrong. Right, so if we got power, the power function is the the 10 there to the power of I. I starts at zero. So, 10

**Dave Jones:** to the power of zero is one. Okay, so that would be one modulo 10, which doesn't return our digit. Oops, that still does not produce the correct digit. Can you fix it? I apologize for the previous mistake. I

**Dave Jones:** noticed another issue in the code. In the get segment pattern function, the segment patterns are defined with the decimal point segment as the what? However, the segments are shifted out with the decimal point segment as most This mismatch is causing the segments to

**Dave Jones:** be denied. Well, no, the problem is there. No, hang on. The problem is we're getting the incorrect digits, not that the segments are displayed incorrectly. Need to I get segment pattern function to define the segment patterns with the decimal point.

**Dave Jones:** No, no, there was nothing wrong with the I get segment pattern. No, please undo that. That's not the error. The error involves calculating the digit using the modulo function. This is getting a bit tedious now. Okay, let's see. I

**Dave Jones:** apologize for the confusion. Here's the updated version that should correctly calculate current using modulo. It didn't say what the error was. All right, let's see how different it is. Equals counter divided by int pow. No, that's exactly what we got before. No,

**Dave Jones:** it's gone back to thinking in this update we've changed the inner loop to shift out the segment. No, the syntax error in the function by casting it to an int. Yeah, that So, it's it's taking into account our previous conversation.

**Dave Jones:** No, no, sorry, AI. Um, that's you haven't changed the the root cause of the problem is this. It's not returning the correct digit. Oops, I might have to fix this manually. I don't think I can coax it into fixing

**Dave Jones:** this. Um, maybe my prompt engineering skills just aren't good enough to do it. That's the same calculation for the digit. It is still wrong. Can you please fix it? See, cuz if you didn't know how to fix it, you would have to If you had

**Dave Jones:** no information to do it yourself, you'd just do it yourself, right? knew how to do it. Like the whole idea is getting it to figure out what the mistake is. Counter in power four minus one. Do I Okay, now it's given us at least

**Dave Jones:** something different. Write C code that extracts digits one by one from a given number. I'm going to make this AI do it. I'm going to make it going to make it work. Is it C code that is Yep. It It should

**Dave Jones:** be trivial for it, right? Digits in uh are number extract digit. There you go. It's modulo 10 and number is you divided by 10, just like I said. Now, the interesting thing is it basically had that solution correct back here. Counter

**Dave Jones:** divided by 10. Oh, I think I see it. Okay. People are probably screaming at me, right? Um, it it actually had the code originally correct here. Okay. Modulo 10 and then the counter equals divided by uh 10. That's the same as

**Dave Jones:** counter equals counter uh divided by 10. But, the counter is like it's supposed to be decrementing. So, you need to put it into a temporary variable first. You can't do it on the actual counter. So, yeah, we we have to Um, oh, can we tell

**Dave Jones:** it to Uh, that's pretty complicated to explain that they're overriding the counter. Go back to the original code and use a temporary variable instead of counter in the digit calculation. Let's see if it understands that. Yeah? All right. This

**Dave Jones:** is so much fun. It really is. Temp counter equals counter. Oh, no. See, it didn't go back to the original code. It It's No, okay. It's still doing that. But yeah, it's like temp counter modulo 10. Yeah. So, it's it's doing the

**Dave Jones:** temp counter thing. All right. Let's just Let's just fix it manually. We've around enough. All right. So, outside of the loop, I've put temp counter equals counter. So, we're copying into a temporary variable and then we're operating on that temporary

**Dave Jones:** variable there. So, let's let's give that a try. Everyone's going to be be screaming at me. I think I figured it out. I I was wondering this this should work, right? This original code, even as a sanity check, temp counter equals temp counter

**Dave Jones:** divided by 10, right? And I'm going like this should work. And then I realized we're dealing with a five-digit number, 99999, which is greater than the integer we had declared for not only temp counter, but also for the counter up here. It was an

**Dave Jones:** integer. And yeah, no. We We need a long for that cuz it's going to go only go up to 65,536, right? So, yeah, it's it's just not going to do it. So, if we change that to long type, then it should work. Well, we can

**Dave Jones:** ask the AI if that's correct. It looks like the counter variable is the incorrect type. It's an integer instead of a long. Is that the problem? Let's go. It's possible that the issue with the digit calculation is related to the

**Dave Jones:** integer overflow, which can occur when the counter Yeah, yeah, yeah. So, it knows all about this. In that case, changing the data type of the counter variable to long counter, there are and then it's going to generate the code.

**Dave Jones:** It's still going to use that dodgy code. Uh no, yeah, it's still going to use the power thing. Um I don't think that's going to work. Yep, let's try that. Let's go to the bench. All right, let's power it on.

**Dave Jones:** Oh, hello. Hey, it's counting. It's counting. It's counting down. Woohoo! Why didn't it start at 99999 though? We got 99749. But it's counting down. It's doing the thing. Let's see if it goes from 40 to 39. It will, I'm sure. Yep. Yep. No

**Dave Jones:** problems. Let's Let's try that again. Should have initiated It's initiating to that same value each time. 730, is it? Yeah, or pretty close to it. Why is it doing that? Doesn't like that. That's something to do with the precision in the modulo

**Dave Jones:** operator, perhaps. But it's counting down anyway. It's doing the business. So, it it basically we didn't have to muck around with any of the mapping for this thing. It got the correct seven-segment mapping. It got the It got the order of digits

**Dave Jones:** actually correct. Whether or not that was by luck or whether or not that was you know good prompt engineering on my part, I'm not sure. I'd have to go back and check. But yeah, there you go. And it's And it's mapping everything

**Dave Jones:** correctly and it's doing the business. So, there you have it. That was almost a successful attempt to get AI to write code for this Arduino to do. I It's not a hugely complex problem, but as you saw it had like a few little

**Dave Jones:** tricks in it. And we had to like it had to understand that we wanted like a physical thing, like a seven-segment display. So, it knew what that was. It knew how the segments actually you know the digits map in a seven-segment the

**Dave Jones:** segments map in a seven-segment display. It understood that. It understood a shift register cuz we used like that you know, so this keyword of 40-bit shift register it knew what all that was. It knew that we wanted five seven segment

**Dave Jones:** displays with and it understood that there was a decimal point and it understood like and it this code was pretty close to being bang on right off the bat. This actual shift output here I I just had forgotten my Arduino

**Dave Jones:** libraries. Yeah, that that would have worked. We didn't have to actually specifically that's a function that is designed to put the data first before it then shifts the clock. So we didn't actually have to change that. So it

**Dave Jones:** turns out that was absolutely correct. It turns out the modulo thing here was correct. Like the actual function of it is correct except that it didn't know to use a temporary variable in there. Like it was overriding the counter. So that

**Dave Jones:** that wouldn't have worked and then it even though we told it a 99999 that exceeds the integer value in here which I need 32 plus minus 32 you know, thousand right? So yeah, so it didn't pick up those things

**Dave Jones:** but that's that's pretty minor apart from that. It it really did it really did well like it got all this mapping correct. We didn't have to change any of that like the segment mapping it got the order correct and and everything. So there was

**Dave Jones:** only a few little hiccups in there which you know, this video has been a long time you know, I've been going through the process of figuring out and I didn't spot the you know, the integer thing straight away and you know, these are

**Dave Jones:** these are mistakes you make all the time. Yeah, but I'm I'm quite impressed. The AI actually did that. It it's not bad at all and then but you can see that there's limitations to it like it just got confused as we go down

**Dave Jones:** here. It just like it started putting the power thing in there. I haven't really correctly analyzed that but I don't think is is that going to work? I don't know. Leave it in the comments down below. So, yeah. So, then it got

**Dave Jones:** fixated on the power function after we told it it was wrong. So, it really takes it to heart when you tell it it's wrong. Can you can please fix this or change it? It it goes and thinks about

**Dave Jones:** it and and finds a different, you know, it knows you want a different way to do it. So, it it tries to accommodate you in that, which is really good. And then when I told it no, go back to the

**Dave Jones:** original, it didn't know that the original meant way back at the start, you know, and stuff like that. And I apologize for the previous mistake. And and and then but then it got totally confused and wanted to change it thought

**Dave Jones:** that there was something wrong with the get segment pattern function, and there wasn't. There was absolutely nothing wrong with that at all. It just got absolutely muddled. So, yeah, whether or not we could have actually got like kept

**Dave Jones:** going in that same chat window to get it to actually produce the working code, probably. But in this particular case, it did actually require a human, that's me, to actually, um, you know, ultimately figure out that, you know,

**Dave Jones:** the integer was overflowing and stuff like that. So, unless you it what didn't seem to be picking up that on its own. So, yeah, um, a little bit of human intervention required, but damn, like, you know, it's not the first time I've

**Dave Jones:** made that mistake myself, and I'm sure, you know, you have too. Just admit it. Um, but yeah, no, that's that's it's it's really impressive though. How like just simply that gave me 99% of the way there. Like it it it actually compiled

**Dave Jones:** fine straight off the bat. It's just that it required a temporary variable and and the int changed, and that was it it would have been good to go. So, yeah. Wow. Impressive, huh? There you go. I hope you enjoyed that. That's chat GPT

**Dave Jones:** 3 and or 3.5, isn't it? And yeah, people are scared that it's going to take your job, but it's just it it's another tool, basically, to, you know, to help you out. But yet no, you could bluff yourself into a programming job with

**Dave Jones:** this, right? A fake resume and then just you know, churn out some code using the AI and and commit it. You know, and then it's like yeah, you can probably like you know, you might be able to bluff

**Dave Jones:** your way into a job for a certain amount of time until they figure out that you're using an AI button you don't actually, you know, able to find things. But, yeah, it's I'm I'm really amazed with that example. That it actually it

**Dave Jones:** it crossed hardware and software there and it kind of knew about seven-segment displays and and shift registers and stuff like that. So, for taking that that simple text and doing it, I'm I'm thoroughly impressed. Wow, hats off. So, there you go.

**Dave Jones:** Thoughts and comments down below and if you like that video, please give it a big thumbs up and let me know if you want me to do the like another version of this just using old school discrete TTL logic or how

**Dave Jones:** other way you want me to take this project. But, that was a cool use of AI. I really like that. That was a great example. Catch you next time.
