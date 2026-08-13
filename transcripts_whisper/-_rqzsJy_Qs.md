---
video_id: -_rqzsJy_Qs
title: Demonstrating Creation of a Xamarin C# Multiplatform Calculator App
url: https://www.youtube.com/watch?v=-_rqzsJy_Qs
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 13, "2": 38, "3": 53, "4": 75, "5": 96, "6": 119, "7": 139, "8": 151, "9": 167, "10": 200, "11": 220, "12": 248, "13": 263, "14": 282, "15": 302, "16": 325, "17": 349, "18": 373, "19": 393, "20": 411, "21": 436, "22": 473, "23": 494, "24": 522, "25": 543, "26": 566, "27": 593, "28": 616, "29": 636, "30": 647, "31": 667, "32": 690, "33": 705, "34": 725, "35": 745, "36": 767, "37": 795, "38": 814, "39": 836, "40": 868, "41": 880, "42": 898, "43": 926, "44": 952, "45": 972, "46": 994, "47": 1022, "48": 1042, "49": 1064, "50": 1086, "51": 1114, "52": 1134, "53": 1154, "54": 1180, "55": 1198, "56": 1236, "57": 1266, "58": 1290, "59": 1324, "60": 1338, "61": 1362, "62": 1394, "63": 1414, "64": 1440, "65": 1458, "66": 1492, "67": 1524, "68": 1548, "69": 1574, "70": 1608, "71": 1636, "72": 1664, "73": 1686, "74": 1718, "75": 1742, "76": 1754, "77": 1784, "78": 1848, "79": 1886, "80": 1928, "81": 1952, "82": 1984, "83": 2018, "84": 2042, "85": 2064, "86": 2080, "87": 2098, "88": 2116, "89": 2134, "90": 2156, "91": 2180, "92": 2196, "93": 2208, "94": 2224, "95": 2240}
---

**Dave Jones:** Hello, so today we're going to do a demonstration of cross-platform app development in the same environment we used to develop the app for the 121GW. So, guys, let's open up Visual Studio and let's create a new project. So, we're going to do a Xamarin project.

**Dave Jones:** This is my platform of choice for these things. And you want to click cross-platform app. And we're going to call it EEV Phone Calculator. And then we're just going to create the project. And this should actually give us a page with some writing, I think.

**Dave Jones:** So, I'm going to target Windows and Android and Windows Phone, not because Windows Phone is supported anymore, but just because if it works in Windows, it works in Windows Phone, which is nice. So it just happens to be that I'm targeting all three.

**Dave Jones:** And I'm basically just going to use default controls, not a lot else here. Oh, what do we want to do? Minimum target. Yeah, sure. And it'll probably give us something similar for Android. Well, it should. Ah, it didn't. It's targeting something random. That's great.

**Dave Jones:** Okay, so let's first have a look at what we have. And I'm going to develop this in Windows just because it's the fastest way to debug. Let's see what it starts off with. Specified path and file name. Ah, shoot. So let's close this solution.

**Dave Jones:** Open the file. And I totally don't know if this will work, but let's just put this somewhere closer. And let's put it here. Okay, so I pasted it on the root directory of my G drive. I've got these random git files which I don't care about.

**Dave Jones:** And I'm just going to reopen the project. It should work because there are internal paths embedded in projects. I'm just hoping they're all relative. It does look like all those things worked. We will receive error messages in the output if it doesn't. It's a good thing that error came up, actually, because that is a really, really common error.

**Dave Jones:** I mean, I've had it in every... well, obviously I've had it in every project I've ever done because I've had my projects directory in the same folder and I haven't bothered to change it. Anyway, so it looks like it's working. Local machine, let's go.

**Dave Jones:** And it's a yellow screen, but it's running. Yay! There's the Xamarin splash screen I thought would happen. And we might get some writing in the middle. Yes, welcome to Xamarin forums. And there are two ways to develop. One is in XAML, which is kind of like a HTML-y thing.

**Dave Jones:** And we're not going to do that. Anyway, so we're going to have a few things. We're going to have a button. And this is going to be... calculate? No. Plus. Minus. Divide. Multiply. Equals. Compute. Enter. Let's call it enter, which might also be reserved.

**Dave Jones:** Okay, so we've got those buttons there. And then we're going to have the keypad button. And this is going to be an array. Because keypads are kind of like an array. And there are ten different keys, you know, one to nine. And that should be okay.

**Dave Jones:** Asize cannot be invariable. Really? Alright. Does that? Pfft. Okay, I always forget that C-sharp is basically all in the heap. Anyway, so now what we want to do is initialize these things. So first, plus equals new button. Text equals plus. For you Uber nerds out there, I could use reflection to set the button text here,

**Dave Jones:** but that would limit what I can set the text to later. And also, it's totally and unnecessarily an overly advanced concept to do here. So this doesn't take very long. Anyway, so then we're going to do this. And then we've got all our buttons.

**Dave Jones:** So, operation buttons. And we're going to actually have to add the operation as well. So let's do that. Plus dot, and we only care about that. And press, there we go. Plus equals, and we'll hit tab and let it autocomplete. Minus, and this is why I use Visual Studio, by the way.

**Dave Jones:** This exact thing. Which I find it to be almost flawless. It follows my naming scheme as well, so I'm very happy about it. I didn't even change it, it just happened to be how I thought. Anyway, maybe they brainwashed me. They brainwashed me, I know it.

**Dave Jones:** What am I doing? Oh, I meant to let it do it. Why am I doing a calculator? Well, firstly, Dave and I both like calculators. That's not how you spell multiply. And it's also a good demo, and there are, in my opinion, no good calculators on the App Store.

**Dave Jones:** Yes, yes, yes, I know. I've downloaded a lot of them, I'm very picky. And this one is going to be worse than most of them. Hollow reasons for doing things. Well, the real reason, I'm demonstrating. Anyway. Now, I could separate these into separate classes,

**Dave Jones:** which encapsulate regions of buttons, but I'm not going to, because the more I can have this all in one file, the more readable it will be to other people. And normally I don't do this type of block thing either. Okay. So let's just...

**Dave Jones:** Yeah, so we've got these operation buttons events here now. Okay. So, then, we're going to have the keypad. And the keypad's a very different thing. We don't actually care about... This is self-explanatory. These are called events for everyone who doesn't know. This is the keypressed event, so when someone clicks the button,

**Dave Jones:** you know, like I'm clicking that thing, it will run this function. It's just like a normal function, a block of code which runs when that press event occurs. Anyway. Keypad buttons. So, to set up the keypad buttons, I'm going to do a foreach.

**Dave Jones:** foreach var button in keypad. Now, everyone's like, ah, you didn't initialize keypad. I know that. Okay. And that goes like that, I think. Yep. Okay. So this is going to go through all of them. And it's going to give me access. And first thing, I obviously need to construct each item.

**Dave Jones:** So, button equals new button. Okay, there's probably a way to do this, but I'm not going to bother, because this is fine. And I need an index anyway. I need an index anyway. Okay. Is that a function, is it? Yep. Okay. And obviously you can't use that anymore, because, yep.

**Dave Jones:** And var button equals keypad. And we kind of want this to be a ref. I'm not sure if you can do that like that. Maybe you can. Does that work? I don't know if this is a good idea or not. I think it's probably naturally a reference anyway.

**Dave Jones:** But I'm trying to describe, I'm trying to show people reading this that I'm actually setting the thing in the keypad. I'm pretty sure it would do that anyway, though. Anyway, button text equals index.toString. There we go. Now I've set up the buttons. And now we actually want to have a slightly different event.

**Dave Jones:** A keypad event. We're going to combine all these events. And this is actually quite important, because we want to work with numbers, not with weird buttons. So what I'm going to do is a thing called a lambda. These are really, really useful. And let's just follow the format here.

**Dave Jones:** So you've got one thing here. You've got two parameters. A lambda is basically a function without a name. But you can also use it like a variable, which is pretty cool. All right, so... Jeez, there's so much prerequisite knowledge for this video. That's okay, though, right?

**Dave Jones:** No. Oh, well. Keypad button pressed. And we only care about index. I'm going to drop those two, and we're going to run this. And then we're going to actually just generate the method. Okay. Very nice. That's so funny. All right, all right. That's so stupid.

**Dave Jones:** And regen. And then... This project will be open source, so hopefully you can make it into the best calculator app in the universe. But we're not really starting with anything very good, so it's elegant. It's not very good. It's pretty terrible, actually. All right, so these numbers represent a keypad.

**Dave Jones:** And the first thing we're going to do in this regardless is convert it to our type. And we want to kind of save this type up here. Anyway, so I'm going to convert it to a double. Value equals index dot... Actually, it'll convert in here.

**Dave Jones:** And we want to have that as const, because we don't want to be able to change the actual value. Firstly, okay, when you intend to do const, you should probably never remove it, because it is a very useful thing. But because I'm doing a video,

**Dave Jones:** and people need to understand this, because I'm doing a video, I'm not figuring out what's wrong, because I'm doing it quickly. Anyway, so... And now we're going to have a result. I'm going to start off with zero, or one. I can't remember. Anyway, so...

**Dave Jones:** And we'll also have a buffer. Anyway. And our buffer's just going to be set to our index. There's a cast. This automatically does this. Although maybe I should just notate it anyway, because it'll give me a warning. It'll be annoying. Anyway, so there we go.

**Dave Jones:** Okay, so everyone who's wise is thinking, what are you doing? And rightly so, because this isn't actually what we want. When you type a calculator in, when you type in a calculator, you press one, you get one. And then the next thing you do,

**Dave Jones:** if you press two, it should be 12. It shouldn't be replaced with two, and that's what it's doing at the moment. So what we want to be doing is buffer times equals 10. And that will shift over the number by one. And then we want to add the index.

**Dave Jones:** Yeah. Apparently we have no decimal point on this calculator, so there you go. We'll figure that out later. Okay, so we don't necessarily want to do enter initially, so we'll leave it like that. We're going to work on the result, and the result will eventually be a property.

**Dave Jones:** We'll make it a property immediately. Public. It doesn't have to be public. Double result. It's in capitals because, I don't know. Anyway, so this is a temporary property, and we can actually work with this. That's fine. So, if we type multiply, multiply, whoa, multiply,

**Dave Jones:** result times equals buffer. And every time you do an operation, you clear the buffer. And you've already figured out how easy this is. Truly, truly easy. And you see some people develop these calculators. I watched a video of this, and sometimes they get really complicated.

**Dave Jones:** Anyway, this is not one of those. And when you press enter, it just equals the buffer, I suppose. Sure, that makes a lot of sense. Not really. Let's not clear it there. Maybe I'm not thinking this through enough. But, okay. And then, so we've got all these buttons,

**Dave Jones:** and we actually want to make this a grid. We need to put a grid on the screen. Whoa, what the hell? Anyway, so what we want is set up the grid. So, content, that's what's displayed on the page, equals new grid. Okay, so

**Dave Jones:** show it. Dude. Bro. Hello. I'm not making any sense. Alright, grid. So, new columns. Columns. Columns. Definitions. Add. New column definition. And, okay. So, I've actually kind of solved this problem before. Where, you're adding items to a grid, and you don't really want to be thinking about where they're going.

**Dave Jones:** You just want to add them in the right order, and be like, yeah, done. Alright, so I created this little wrapper. And I am going to use something from one of my libraries. This is an open source library, by the way. It's part of the 121 GW app.

**Dave Jones:** And anyone can download it, use it for their own thing. And I call it autogrid. Because, it fits what I think a grid should do. And I always use them relatively consistently. So, why shouldn't I automate my relative consistency? Anyway, I probably could have used a...

**Dave Jones:** Anyway, here it is. Here's my autogrid. And, I'm going to have to fix some things. Because I'm doing some things that don't make any sense. Don't care about that. Don't care about that. And globals running main thread? I don't have globals. Don't care about that.

**Dave Jones:** We'll just use defaults, don't care about that. That's kind of why I pasted it. Ah, jeez, jeez, jeez, device. Run. Begin invoke on main thread. Sure, that'll do. This probably has a parameter, but I don't care. I'm going to copy it with braces.

**Dave Jones:** And put it there. Yeah, that'll be a sufficient replacement. Okay, so I've got this autogrid thing all ported. That only took about a minute, right? And what I'm going to do is... I'm going to use an autogrid. Because I like autogrid. Oh, right.

**Dave Jones:** Yeah. And the autogrid does require some... No, it doesn't. What does it want from me? Cannot create instance of abstract class or interface. Autogrid. Is that abstract? I don't remember making it. Really? Did I want to inherit from that, did I? Well, screw it.

**Dave Jones:** Alright. So, .add. Uh-huh. Let's see what functions I have. Let's look in here, though. Okay, so we want to run these two. There's probably something that does them both at once. Should be, anyway. Ah, defineGrid. There we go. .defineGrid And we want it

**Dave Jones:** to be... So, we've got how many buttons? We've got one, two, three, four, five, and then we've got ten numbers. So, what we're going to do is put the numbers at the top. Ordered in the standard keypad thing, like on the numpad. And put the operations

**Dave Jones:** at the bottom. And the side, I suppose. Yep, who cares. Alright. So, four and four. That'll give us sixteen items. And what we have is ten plus five is fifteen. Nice. So, now this is going to be weird. .autoadd .autoadd That probably could

**Dave Jones:** just be called add, but I wanted to make it clear that it's not a grid, so I didn't really... Whatever. Alright. So, this time we're going to do basically the same thing, but we're going to do it in the other order. So, two greater than

**Dave Jones:** zero. And I actually don't know if you can do a foreach backward. Who cares? Alright. This doesn't matter anymore. Let's just do that everywhere. Who cares? Okay. So, that's all irrelevant now. grid.autoadd button width one. It's default one, so we'll just handle it.

**Dave Jones:** And that should do it. A very weird combination. Three. Five. That'll be easier. That's actually exactly the number of things we need, so that's good. Alright. And let's have a look at what it looks like. So, we've defined a grid, set up a grid,

**Dave Jones:** and we've added the buttons. We've only added the numbers, though. But we can test a few things now. We went to int. What could I do to myself? I like uint, because it indicates that this can never be negative ever. So, we should have some buttons.

**Dave Jones:** Out of range? What? Ten? Alright. Well, that is obviously correct, as it always is. It's an error message. Kind of knows what it's talking about. Alright. So, 9, 8, 7, 6, 5, 4. Oh, there we go. That's kind of backwards, isn't it? 9, 8, 7, 6, 5, 4, 3, 2,

**Dave Jones:** 1, 0. And we kind of want to swap this. Kind of want to invert the row and column, because numpad's kind of like 7, 8, 9, so 6, 5, 4, 3, 2, 1, 0. So, we want to do that as well. Not a clue.

**Dave Jones:** Temporarily, we're going to do some crappy code, alright? Just, alright? Please? Anyway, so, please, this is index remapper equals mapper. Now, this can be static, because it's always there, and it's only run once, so it's just, alright? Okay. So, index 0 is as is,

**Dave Jones:** but 1 is 3, 2 is 2, 1, 4 is 6, 5 is 5, which is hard to think about. 6 is 4, 7 is 9, 8 is 8, 7 is 7. Okay, wait, 7 isn't 7. 9 is 7, is what I meant to say.

**Dave Jones:** And make sure I don't have anything unique, that's 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, and that should be okay. Something wrong with this, but I don't care. Equals new Does that not work? I don't care. I'm lost. Okay. Seriously?

**Dave Jones:** I don't know why these initialized lists don't work. Don't they work? Erase Array. Dammit. Alright, well, apparently I don't want to make a const, because I don't, look, again, same thing before, const, ignoring const is a really dumb idea, okay? And, there. Okay, so now let's have a look.

**Dave Jones:** 7, 8, 9, okay, we've got 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, and this is exactly what we want. 7, 8, 9, 0, and this is exactly what we see on a numpad, so yee-hoo! So now, what we want to do is

**Dave Jones:** the next thing, and the next thing is setting, set up the buttons. And, we can just add these one by one, because they're all unique and I can't iterate through them. So, let's tab these, and yes, tab, not spaces, I know. People who like spaces can go

**Dave Jones:** internally explode, no, it's a metaphor, it's not literally, anyway. So, here you go. Now we have this, and we actually, if if index not equal to 0, button do that, it should do that, else grid.autoaddButton 2. Now, we're actually short, we're short a button now, I'm just going to get rid of the enter button,

**Dave Jones:** I don't care, anyway. So, now it'll look more like a numpad. Ha! Too many multimeter menu. Too many items in the multimeter menu. Yeah, well, that's true, because I literally said out loud, I'm going to get rid of it, and I didn't. It's nice, it gives you good error messages there, right?

**Dave Jones:** So, here you go. 0, plus, minus, divide, multiply. Yay! Okay. Looks horrible, but that's okay. So, now, we're going to have a label, and the label is going to be result. Result. And we're going to have a label for the buffer. That's nice, buffer.

**Dave Jones:** And here, we're going to do private, we're going to make a buffer, and we're going to make this, this is kind of why I work with properties, because you can do this. And this is all, you know, all my mistakes, so you're going to see stupid

**Dave Jones:** shit I'm doing here, and you just have to put up with it. Result.text text I don't actually know what the labels text thing is, but I'm going to new label because they're going to be initially zero, and I've got a naming conflict. That's why

**Dave Jones:** you need to name things well, and I still haven't, by the way. Still badly named, but I don't care, I don't care. Okay. And the buffer's going to do the same thing, so, you know, pew! And buffer equals that, and buffer label equals that,

**Dave Jones:** and then we're going to add the buffer label, actually, to the top, so we're going to make the grid one more high, six, and we're going to add two different items, the buffer and the result. Result label, I didn't type label in the other one.

**Dave Jones:** Okay. And the result label should be bigger, of course, so the width is two, and now that makes it divisible by the number of grid cells we have. Buffer doesn't exist. Yeah, well, that's true. That's because only the uppercase one is accessible now.

**Dave Jones:** And now we have a calculator, so four plus five plus plus, why is it twenty? Plus six plus plus plus plus What's going on? Let's have a look. Let's have a look. Seven. It should be seven. No, it's always ten. It's always ten.

**Dave Jones:** It's going to always be ten. That's very annoying. Oh, no. No, no, no, no, no, no, no. Not at all. So apparently I've sent it to the same... Oh. Is there a way to do a new lambda or something? Let's work on a copy

**Dave Jones:** and see if that... This isn't going to fix it. There's no way. In fact, it might break it. Okay. So I was right originally to do that. So basically what's happening is it's getting the state of what index was, but because index is a variable that's stored out here,

**Dave Jones:** when the functions run, the last state of index was the count, and that's why it's screwing up. So I suppose I need to create a temporary or something for you. Actually, primitive types, they copy. They always copy. This couldn't fix it, could it?

**Dave Jones:** Can it? Will it? Should it? 9 plus 57, 66 plus 8 is 74. There we go, we're getting something up there. And let's... That fixed it! Holy crap, that's surprising. That's because this gets disrupted. So this gets deleted, so it works on its

**Dave Jones:** local copy from its captcha list, I think. Now, I'm mixing terminology because I'm, again, basically a C++ programmer, so my terminology is probably all wrong. I get confused. In C++, getting a variable like this one inside this lambda would be called a captcha

**Dave Jones:** list, and it would have these square brackets, and you'd be like captcha by reference or captcha by value, and in this case it would have been fixed by doing captcha by value. I think what I'm doing here is in effect captcha by value.

**Dave Jones:** Anyway, there's probably actually a way to specify that. Oh well. So, let's have a look what's wrong now. 7. At this point, the buffer is very likely 77. So we'll step forward a little bit. 77, very good. And we actually want to display

**Dave Jones:** that immediately. Are we? Are we displaying it? That's the question, isn't it? It's probably underneath this. Let's change the alignment so we can actually see things. Where did I construct these? So, vertical vertical ver Is that another thing? I don't know. And this isn't actually anywhere near done.

**Dave Jones:** I'm going to copy these. It doesn't like autocomplete like that. HorizontalOptions equals new newLayoutOptions fill What does it want now? Expands. True. Sure. Why not? No. False. I don't want it to expand. Or do I? Screw it. What's going to happen? It's never going to expand, right?

**Dave Jones:** It will. I don't care. Okay. So now, resultLabel, right? And we already need the buffer label too, so let's just do that. Done. Okay. So now, we have this, and we've got zero. That's not right. Multiply by zero. Okay. Plus two. Plus two.

**Dave Jones:** Add it. Three plus. Three plus is ten. That's good. Five plus. Seems like these are the same thing. Maybe I'm making them the same thing. Am I doing that? I am. Okay. So that's because I was printing buffer. So it might well be working.

**Dave Jones:** Five. There you go. Fifty-eight. Five hundred ninety-nine plus three. There you go. That's right. Cool. Some weirdness about this. Yeah. Three. So we're going to add three. We're going to add six. Going to add three. And our results are good. Let's set up our text sizes a

**Dave Jones:** little bit. So there are some standard ways to do text sizes. Result. Label. Text. Size. Font size equals device. Get named size. Is that right? Sure. Large. Target element. Label. Is that right? Does that work? Why does it not work? So they want me to do a typo.

**Dave Jones:** That's fine. Kind of makes sense, but it's weird that it describes that as element. Anyway. I suppose they are all elements. So we should see a much larger result text. Yep. And we kind of want it bigger than that. Is it extra large?

**Dave Jones:** Oh well. Screw it. That's big enough. Okay. Anyone who knows what I'm doing, please just look away. It doesn't know what I'm doing. Just look away. Doesn't matter. Is that not a thing? It's not a thing. How do you do it in C sharp?

**Dave Jones:** Screw it. Doesn't matter. Doesn't matter. So we've tested all these things. Enter doesn't exist anymore, so we might as well just refactor our code a little bit to get rid of it. The best way to do it is you delete the variable name first, and then everything else

**Dave Jones:** propagates. So there we go. Hope you found this interesting. All I'm going to do now is make it a bit prettier, so I'm going to pause it, and then I'll resume it when it's pretty. Okay, just a few minutes of making things a bit better

**Dave Jones:** sized and stuff. We've got this. And it's a nice app that's relatively okay. We don't have an enter button, so we have to use the plus button instead, which is a bit odd, but whatever. Zero plus seven is a seven. And plus three.

**Dave Jones:** Plus three, plus three, plus three, plus three, plus three. And we're going to divide by five. Yay, that's right. Of course it is. Okay, so how do we get it on other platforms? It's actually as easy as that. It's already on other platforms.

**Dave Jones:** Multi-platform development, when you're not interfacing with the touchscreen and stuff, is trivial. So let's just change the target. Let's do Android. I can't do iOS, because I don't have an iOS device around me. Apple requires that you do, so I don't. So I can't.

**Dave Jones:** Okay, so it's started the build process. It shouldn't have to rebuild it, because I already built it for an arm. But it is a different Android, so who knows. Oh no, it seemed to rebuild it. No? I don't know. And it's almost done already.

**Dave Jones:** Wasn't that a lot faster? So when you do developing cross-platform, you really don't want to use the debugger. I was being lazy, and I wasn't wanting to set up a webcam thing, because making videos is a little bit more difficult than not making videos.

**Dave Jones:** But as you can see, here's the app. And we're going to start off with 3. And go 3, plus 3, plus 3, plus 3, plus 3, plus 3, plus 3, plus 3, plus 3. That's working. I'm going to add one more, and we're going to

**Dave Jones:** divide it by 10, and that's 3. Okay, so I've just prettified the app, and I've added the proper mathematics symbols, divide plus, multiply. And I've changed the color of the operations. I think it's looking quite good now, and I think this shows it's not too difficult

**Dave Jones:** to create a cross-platform map if you're not interfacing with platform specific features. So this calculator I created, if you extract all the wasted time in about 25 minutes. I hope you liked the video. If you did, give it a big thumbs up. Alright.

**Dave Jones:** Bye.
