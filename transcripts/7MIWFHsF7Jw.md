---
video_id: 7MIWFHsF7Jw
title: EEVblog #1264 - uSupply Software Development Setup
url: https://www.youtube.com/watch?v=7MIWFHsF7Jw
source: youtube-asr
---

**Dave Jones:** Hi, I'm chopped off. It's David. I was stretching my mouth when you started. That'll be weird. Does it matter? No, maybe Does it matter? No, okay. Hi. Um we're going to talk about and well we're going to have a look at the micro

**Dave Jones:** supply. Ta-da, there it is. Should I go full screen on that, David? There we go. There it is. There it is. The micro supply. Doesn't it look sexy? Yep. All right, so um I can just turn it on for you.

**Dave Jones:** You know what? Ah, come on. There we go. Anyway, um yeah, micro supply is coming along. We're just having a look at um installing the code uh the the What are we installing? Code and [ __ ] Yeah, we're installing the

**Dave Jones:** the IDE so that you can work on the code and other people can work on the code. I suppose this video could be kind of instructional for anyone who wants to contribute to. Sure, it is open source. The code is all

**Dave Jones:** open source. It's on the GitHub's or the GitLab's. Yeah, and the library is pretty well documented. The the system specific code, less well documented. Right. Yeah. So I'll link it in down below. Um we will have the code. So if you want

**Dave Jones:** to check it out and uh Yeah, we're doing some funny things at the moment to fit it on a micro, so Right, yeah. It's insane. Yeah, we've talked about it on the amp hour today. Talked about fitting the code on the

**Dave Jones:** 32K, but I did that in my ST video um earlier this week or last week, was it? Uh yeah, where we talked about fitting the code. Oh, and by the way, we have our flex PCBs. Flex PCBs are in,

**Dave Jones:** but we don't have the chips yet. The boards actually turned up early. Check out the date. Yeah, there we go. Check out the date on it. It's got the 25th of November and it is um what, the 22nd

**Dave Jones:** today? I wonder if they print that on there if it's late. Probably not. Anyway, they got delivered early. So my chips are still So yeah, you were remarking that they were able to manufacture these from scratch quicker than what Farnell's can

**Dave Jones:** Element14 can pick a couple of chips off the shelf and send them here. move it from a shelf to a truck. They made it faster. They made it faster. Yeah, amazing. Amazing. Yeah. Anyway, so we're going to install the

**Dave Jones:** entire tool chain to get it compiling. That's right. We're going to set up VS Code with the GNU GCC tool chain and CMake, which is a build system generator, which is I'm going to get to what that is when we start talking about

**Dave Jones:** ninjas. Cool. And I actually mean that. And you know I know bugger all about this because I've never Anyway, Visual VS is Visual Studio No, it's not It's Visual Studio. It's Visual Studio Code. Code is the difference. Which supports any compiler that you can

**Dave Jones:** If you write your own compiler, you can write a plugin to support Yeah, work it in here. So, it's just a GUI, basically. Yeah, you can write And it calls up the It calls up the command line compilers and that It does

**Dave Jones:** all the Calls the command line. You basically set up what it what it sends to the command line. We don't have to do that though, other people have done that for us. Right. Got it. Yeah. Sorry about the audio. The mic is not

**Dave Jones:** We're not particularly close to the mic here today. All right. So, we've installed Visual Studio Code. That was easy and quick. And we've installed the C C++ extension. Yeah. What else do we need to install? We need to install the thing you

**Dave Jones:** currently have on the screen, the CMake tools. Ah, CMake tools. And you're You were very excited when you realized that Microsoft bought Vector of Bull. Yeah. So, Vector of Bull hadn't been maintaining the plugin for a while. So,

**Dave Jones:** there's This is a plugin which is used a lot for people who develop in VS Code and for embedded systems and with CMake um Yeah, the guy hadn't updated the plugin in about a year, so it's great that

**Dave Jones:** someone's taking on the project. Microsoft taking over. And what does CMake tools do? Okay. CMake tools is just a wrapper, I suppose, for a tool called CMake, which we're going to have to install. Mhm. Um so C make is a system which generates

**Dave Jones:** a build system a build system generator. So it doesn't build your project for you. Right. make a project it it it it creates a project and then calls the compiler from with the project kind of thing. Kind of thing.

**Dave Jones:** Yeah. So so in in I'll give you a few examples. So if you created an Atollic project, there'd be like a proj file. Atollic? Um it's a What's an Atollic project? So Atollic is a IDE for um processors

**Dave Jones:** and that sort of thing and development stuff like that. ST have their own version of it called CubeMX IDE. So that's it's an Eclipse based IDE and it has its own project files. Those tell you like the structure, what things to pass

**Dave Jones:** to the the compiler and stuff like that. And it also has what compiler to call and stuff like that. But the the project files aren't very flexible. Right. So you couldn't swap out the compiler or at least not easily

**Dave Jones:** um to for example an an updated compiler which has a particular bug fixed. Which is what we actually which is which is exactly what happened. So this is the reason that you're using Visual Studio Code instead of the Cube instead of the

**Dave Jones:** ST software the CubeMX. Yeah, we started in CubeMX. Um it's now when we started it was called Atollic. Just Atollic. Oh, it was. It was called actually called Atollic. Oh, okay. Right. So that's what we started with and then or maybe it was

**Dave Jones:** like raw Eclipse. I don't remember but it was an Eclipse thing and then we couldn't I couldn't get the latest GCC to to run which had some fixes for um a part of the GCC tool called uh what is

**Dave Jones:** it? It's the name demangling tool. Name demangling tool. Yeah. Um I don't remember the specific name of it at this time but it basically caused a memory overload like a a it was called Atollic. Right. Oh, it was. It was called

**Dave Jones:** actually called Atollic. Oh, okay. Right. So Oh yeah, okay. That that rings a bell. Yeah. So that's what we started with and then or maybe it was like raw Eclipse. I don't remember but it was an Eclipse thing and then we couldn't I couldn't

**Dave Jones:** get the latest GCC to to run which had some fixes for um a part of the GCC tool called uh what is it? D It's the name demangling tool. Name demangling tool. Yeah. Right. I don't remember the specific name of it

**Dave Jones:** at this time thing, it basically caused a memory overload like a a stack overflow in the compiler when you had lots of symbols. So, when you have specific types of template code in Super Smash, it should just be fine, but it would it would just

**Dave Jones:** blow the stack. Right. Which is like poof. And you're like, "Why did that fail?" Like there's no no message at all. It just give you a stack overflow. Okay. Um So, we want to install this. C make tools.

**Dave Jones:** Yeah, well we're talking about why we changed. So, there was a a problem with the old compiler. And C make is something it's a a project generator. It like generates projects for different build tools. Like I suppose you could

**Dave Jones:** call So, there's a thing in in Atollic called the internal build. I'm not really sure if that's the project the thing that I'm talking about, but it has a build tool in it and it's linked to those project files.

**Dave Jones:** Right. Where C make it can just target any IDE and it generates it those project files for you. Got with the settings for the compilers that you gave it with the compiler you gave it. Oh. Yeah, it's so

**Dave Jones:** So, is I assume all that setup stuff is in some sort of setup file somewhere that we can in the Git Lab is that we just install deal. No? No, you won't even you might not even flinch. It'll just be

**Dave Jones:** okay. Yeah, just a lot of clicking install for things. Okay. Let's do it. All right. So, we've installed that. What's what's next? All right. So, let's go get C make itself. So, that's just cmake.org/download. Oh. Oh, I've got to go to go to a

**Dave Jones:** browser. You do need that plug-in, too. That that TWX one. Yeah, that'll be nice. That one? Yeah. That just gives you syntax highlighting for C make. Oh, okay. Well, yep. All right. That's um that's actually what you were

**Dave Jones:** talking about before. You were saying, "How does VS Code um do this?" Yeah, I the first thing I cuz I did I don't know anything about this and my first question was when I heard that you could if you wrote your own pigeon

**Dave Jones:** English compiler or whatever, you could install you could write support and add it to Visual Studio Code. Yeah. And then I asked, "Well, how does Visual Studio Code do the color syntax highlighting for your language even though Yeah, yeah. Add it as a plug-in and

**Dave Jones:** you're good to go. Wow. Yeah, I mean, the plug-in worked. There's a bit of work, but There's a bit of work to define, "Okay, this these are variables, this will be this color." Yeah, it's not enough to be too

**Dave Jones:** intimidating. Right. Okay. Well, I'm sure that if you wrote a compiler, then you'd be able to write a Yeah, that you'd just That'd be a lazy day on the beach. Yeah, yeah. Technically, I have written a compiler. I wrote a

**Dave Jones:** I wrote a wrote my own uh programmable logic compiler. A PLC thing? A PLC compiler, yep. Back in the day. Yep. Wow, it generated assembly and stuff? It No, it generated um EPROM images cuz it was for a finite state machine.

**Dave Jones:** Okay. So, it would So, it was compiler language. I made up my own language that then high level language that then uh compiled into an EPROM image that would Yeah, use it as a finite state machine. Yeah. So, you use an EPROM as a

**Dave Jones:** processor, basically, as a finite state machine processor. Mhm. So, yeah. That was a thing. Maybe I've got the code somewhere. Yeah. Anyway, um right. So, we installed CMake, CMake tools, and now you're saying the the source? Be interesting to see.

**Dave Jones:** Oh, I don't know. I honestly don't know. We wouldn't be able to probably make heads or tails of the compiler. All right. Yeah. Where are we uh where where are we going to today? Okay, cmake.org and then just the first

**Dave Jones:** one um under platform. No, that'll give you the source. I love how they've told the difference. This has new line line feeds and this has character turn line feeds. It's like, that's the difference between the Windows and the Unix build.

**Dave Jones:** So, when we installed in Visual Studio Code, we didn't actually install the actual CMake. We just installed support for CMake, is that Yeah, you're probably going to have to restart VS Code, but it's not going to Who cares?

**Dave Jones:** Whatever. Okay. Do not add C make to the system path. I have Totally add it. Add it? Yeah. System path for all users? Yep. Yep. Yeah, so um we're going to use C make with a with a build system called Ninja.

**Dave Jones:** Ninja? So um the the build it's a it's a fast Right. uh build system gives you some pretty good project files and seems to work with basically every target um embedded not So we could have avoided all this if we simply used

**Dave Jones:** CubeMX, right? Cuz it's all integrated. Sort of. You wouldn't be able to use the compiler we're going to install. Oh, okay. But it would but we'd be using their compiler. But I thought theirs was just the GNU It's a special So um the naming is like

**Dave Jones:** EA EABI/none/ GCC or whatever. All right, so it is the GCC uh customized. So it's it's instead of none it's Atollic slash GNU. the GCC compiler? Is that what you're saying? Uh yeah, I suppose. Um could be the same thing with Atollic

**Dave Jones:** inserted in the name. Right. Okay, got it. So but we will be using the GCC compiler. Yeah. Right. Okay. Um right. Yeah, cuz it's more Is it installed? It's just more up to date. It's like It's more It's more betterer.

**Dave Jones:** More betterer. Um is is that installed? Right, so should Visual Studio needs to be restarted? Definitely. It'll start trying to configure the project folder. Let's just Let's start off with a dummy project. No. Um so just hit open folder.

**Dave Jones:** Yep. And then make a folder for a dummy project. Okay. We have dummy. Cool. All right. Um now configure the workspace, I think. Oh god. Oh, that that'll be easy. Just click file. File? And uh save workspace as.

**Dave Jones:** Save workspace as? And then just type a name. Dummy. There you go. Now you're in. Um Let's see if C make There you go. That's that's the dummy workspace. Yep. So now we're just going to type C make.

**Dave Jones:** Let's see what it's found on your computer already. Yep. It'll probably found find nothing, but let's just see for now.

**Dave Jones:** Oh, looks like it's found a whole bunch of stuff. There you go. Let's have a look. Yes, configure the project. Confi- Oh, sorry, you can't see that. Yes, configure the project. Uh you'll probably want to leave the camera there. It'll continuously do

**Dave Jones:** that. Yeah. No C make kits are available. What would you like to do? Scan kits. There you go. You got none. So we're going to install one. Yeah. What is it? And we're going to install the um um um

**Dave Jones:** embedded compiler. No, no, you have to go to the browser. You're going to have to install it. Oh, what? You're just going to have to You're going to have to click install many times. All right. Not much work. Not not difficult. Just

**Dave Jones:** lots of pressing the same button. And you I would say someone like me would I would never have figured this out. Yeah, but But would anyone looking at your if we just It does have instructions on the GitHub.

**Dave Jones:** Oh, I was going to say if you got hit by a bus and and all we had was the Right. But without those instructions, would people have been able to They would have C make is standard. Right. People know

**Dave Jones:** how to use C make. You don't have to use it IDE either. So it would have been obvious that you were using C make. All the Yes. All the all the Linux people would just be like Nah. Nah.

**Dave Jones:** Because And they'd run it from the command line. Yeah, of course they would. Yeah. Um and it's easy. You just type C make. Yeah. What am I doing? Um So what do you want to do first? Let's get the build system cuz we can't

**Dave Jones:** use anything without it. So let's type ninja.org. Yep. And then install it. It's just an executable. Download the ninja binary, obviously. Yeah, 190. Uh yeah, you want to get the zip for Windows. Don't want a bloody zip. You'll like this. This installs easy.

**Dave Jones:** It's an XE. Okay, good. Oh, you don't have to run it. What? You don't want to run it. Why? Cuz we've got to put it We've got to put it in a folder. Yeah, don't run. No point. All right. So, go to your C drive

**Dave Jones:** or whatever drive you So, do I copy that? Uh just leave it there for now. We're going to drag it out of it into a folder. You want to have this at a pretty low directory, so let's just put

**Dave Jones:** it right almost root. Almost root? You say root. I don't want to put it in my C root. Yeah, you you'll want to Well, if you have a space in the path, you'll get problems. So, let's just Oh, no. No, let's make a folder called

**Dave Jones:** devtools or something. Um in there cuz there's going to be a few of them. Devtools, yeah? Yeah, cool. Okay. We've just put Ninja in a one folder up from root. Yeah. One folder up from root. All right. Without a space in it.

**Dave Jones:** Next. What What's next? Okay, next we're going to go um ARM embedded. Yeah. And I recently ported the project to nine, which is armembedded.com No, that's annoying. Um embeddedarm.com Yeah. Those sneaky people. Who Who owns embeddedarm.com? Sneaky. And they put an ad to make it

**Dave Jones:** first. Yep, they did. Probably a consultancy. All right. All right. So, I'm going to click some things. Tell us what you're clicking. I'm I'll drink. going to add the word toolchain. There we go. All right. Downloads? Yeah, go Yeah.

**Dave Jones:** And we're hoping to see um the the GNU 9. Yeah, there we go. GNU 9 2019 Q4. I think the Atmel one is limited to GNU 7.4 or something. Some somewhat out of date. Okay. Uh so If there's a 64-bit

**Dave Jones:** 32 I was going to say 32-bit. There is no 64-bit installer. Really? Seriously? Oh, well. Sign for Windows 10 or later. There you go. All right. Someone doesn't like 64-bit. Someone's a 32-bit fanboy, whoever developed this. And That's all you That's all you're

**Dave Jones:** going to get, sunshine. 94 megabytes. The philosophy is probably more like you get nothing extra out of it. It's probably like why should you know we get nothing out of this. Right. Are we operating on 4 gig address space

**Dave Jones:** or whatever? No. Ridiculous. Boy, all right. Come on, you can do it. Whole minute to download. What world are we living in? Isn't it pretty? Here we go, look at that. You're right. Beautiful. Beautiful. It says hello regularly.

**Dave Jones:** So this is the GCC compiler. Yeah, by the By arm. By arm, yeah. Right. So they've forked it, have they? And it's theirs? No, they manage this project. They manage it. Cuz this is the this is the arm version

**Dave Jones:** of GCC. Oh, okay, right. It's not GCC with support for arm, it's I mean, I suppose they forked it. But they manage it. Okay. Yeah. Right. Got it. 500 meg for a compiler. Mhm. I was in Yeah, I've only got 5 gig left

**Dave Jones:** on my C drive. Yeah, I was in the we're not going to install anything that requires 5 gig, are we? No. Not anymore. All right. Visual Studio is it, huh? Mhm. That wasn't that big. It didn't seem to

**Dave Jones:** It seemed to install really quick. Yeah, it's pretty lightweight. Yeah. This Visual Studio is like 9 gigabytes, the real one. Really? Yeah. Maybe even bigger. Maybe 12 if you put all the things I normally do for mobile stuff and

**Dave Jones:** Add path to environment variable. Yep. Now your C make will just pick it up easy. It It often picks it up anyway cuz C make is clever. Do we need the read me? No. No. And what's what's it doing here?

**Dave Jones:** I don't know. Let's type version. Well, that's because I didn't type the executable name. And the executable is not in that directory. Mhm. And what is it? Uh L? I don't remember the net command for list. LS is it in Linux? You've just lost your

**Dave Jones:** your Linux badge. No, no, this is Windows. No, Windows. Okay. Do we care? It was the latest version. No, not really. EABI, yeah, obviously. The fact that I've remembered that is not a good sign. There you go. So, it's a

**Dave Jones:** 25th of October. So, it's really new. All right. All right, so I can shut that down. All right. And now restart VS Code. Restart VS Code will happily have a scanning icon at the bottom right. What if it doesn't?

**Dave Jones:** Uninstall Windows. All right, it's time to get rid of Windows. Yeah, um Oh, there we go. Yes, it gave up last time cuz you had no kits. Oh, okay. There you go. Now, it's detected it up the top. Yeah. So, click that. No,

**Dave Jones:** the the real That one? Yeah, the real one. Now, it's going to do some things and tell you nothing will work cuz we don't have a CMake file. This is all so obvious. How does anyone like learn how to do this [ __ ] Okay, well,

**Dave Jones:** by watching this video. I suppose. So, now we're going to go to my my CMake repo, which is used to help people like this. Really? All right. I get lots of requests for it.

**Dave Jones:** Okay. So, browser again? Yeah. This is the most simple CMake I could do. Where are we going?

**Dave Jones:** Yes. So, here we have a lose the photo of you with the bow tie. It's funny. No. Lose it. I want to make a cringier one. In the comments down below, should he lose the photo or should he lose it? Or should I

**Dave Jones:** double down and get a bigger bow tie? The bigger bow tie, a glow I've got I've got the glow tie. I've got the LED one. um Bill Nye's one? It's like a normal one. Except it's way too big for his

**Dave Jones:** head. You don't have Git. Let's install Git. That's going to be have to be an additional step. That I I read that as scam. Git scam. Is that how Is that how it's pronounced? Uh someone in the comments left to say

**Dave Jones:** with a phonetic spelling which I won't be able to do. Download that one? Oh, yeah. Has it automatically detected our OS? That's 45 meg. When I was a boy. Yeah, they added TLS to it and then it was big. What's TLS? Um

**Dave Jones:** the secure transport layer. Oh, yes. Right. Yeah. Yeah. Do I have to change any of this? I don't know. Let's see. Check daily for Git for Windows updates. Oh, no. I don't want that. It's not checked. Why why would I want to check

**Dave Jones:** that? You don't. I'm reading. Okay. Is that it? Yeah. It's fine. All right. Is there another option? What? Vim will be confusing for you. Oh, okay. Yes. No. Notepad++ VS Code. Oh. Use that. Yep. Yep. What's VS Code Insiders? You don't have

**Dave Jones:** that. What is it? Um they just have extra features that are unstable. You told me that there was no paid version of Studio. I assume that Insiders is still free. Oh, it's like beta. Is Is that like a beta? Oh, okay. Git from command

**Dave Jones:** line only. Git from Use Git from Git Bash only. This is all so obvious. That That's fine. Recommended? Yeah. Open SSL? Definitely. Check Windows style. Is that Yep. Default? Is this new? You haven't seen it before. No. No. No, I probably have. I just clicked

**Dave Jones:** next really quickly. All right. Well, we should probably next Yep. Uh Use MinTTY? Yeah. Fine. Won't matter. It'll be added to path and we'll use PowerShell. And our I would get credential manager. Yes. Is that all right? Yes.

**Dave Jones:** All right. Enable experimental build. No. No. No. So, install. Yes. It's all so obvious. All we want to do is compile our source code for a little embedded project. You will be clicking many buttons. There are still buttons to go.

**Dave Jones:** This is ridiculous. Anyway, this is the documentation for anyone who wants to play around with the micro supply code and build it yourself. Yeah. The long the long long form. Launch Git Bash. Sure. Do really? Uh No. Uh

**Dave Jones:** Come on, you just want to get this finished. Yeah, all right. Yeah, finish. All right. Next, what do I have to do? Restart. Probably your whole computer. No, I'm not restarting my whole computer. All right, type get. That's another All

**Dave Jones:** right, uh restart VS Code. I hope we don't have to add get to path. That'd be annoying. Install this [ __ ] at themselves to path if you check a box like all the other ones. Didn't we pay attention when we

**Dave Jones:** installed it? Open your workspace. And then just type get hyphen hyphen version. It doesn't matter. It'll say not a command. That's fine. Oh, no. All right, so let's type press start. Yeah. Type path. Press enter. Click environmental variables, then click path, double click

**Dave Jones:** on it. The one that says GNU tools arm embedded. That one. Uh that one there. Double click. Edit. Double click. Uh or edit, it doesn't matter. Click on the bottom. And dump it in. Dump it in and backspace until you get

**Dave Jones:** rid of get. Do I have to get rid of the quotes? No, yes you do. You have to also get rid of get. I just wanted the format to be the same way it copies. Um get rid of

**Dave Jones:** the word get A and C. Oh, really? Okay. Yep. Okay. Okay. Um your path may not have refreshed. So, just type get, it might work. Yeah, we have to restart the thing. Yay! No, it's not recognized. Kamigato. Maybe VS Code has it already. Let's see.

**Dave Jones:** Cuz VS Code integrates Git. It just You didn't have Git. So, that was confusing. But, it might have installed with it. But, I'm still a bit confused why it Okay, so Git So, you see this is this is the Git

**Dave Jones:** Mhm. thing. Um So, Git is set up now. It's just not appearing in PowerShell. Okay, I think you have to restart your login log out. The PowerShell path hasn't refreshed or something. All right. Okay, we'll stop recording. Git.

**Dave Jones:** Yay! So, now we're going to pull the project. We're going to close this workspace. We don't need it anymore. Yep, done. Perfect. Now, do we get our one out of Git Labs? We do. I'll take the mouse for a second. This

**Dave Jones:** will be difficult to explain. Yeah, so we're just going to clone this repository cuz you're not the way you work with Git. You don't work You don't work on the actual code that's in the Git. You've got to pull it out.

**Dave Jones:** Yeah. So, clone is like pulling it out. Yeah. It's like downloading it. Pull is actually another command. Right. So, clone is like take everything All right. like from scratch and pull is like get the new stuff. And where does it put it?

**Dave Jones:** Apparently in your root directory cuz I forgot to save it. So, we're going to have to What? We're going to fix that. Why not put it in users Dave? It should put it in a folder. Would I want like to configure this

**Dave Jones:** project? So, so where So, where's my code? It's in users C make users day It's in Yeah, you can delete that folder later. It's not important. This is another intermediate step just to make sure that C make in the build process works.

**Dave Jones:** But, this is how you'd really import your code there, right? Yeah. Okay, so this is the It's It's in the wrong just a tiny project, so it's simple. So, this is how it runs the build, how it runs debug. So, it runs

**Dave Jones:** um this file using OpenOCD. Um Yeah. So, this runs using a plugin called Cortex-Debug. So, we have to get that.

**Dave Jones:** Kind of hoping Microsoft also take this project on. I don't think it's been updated for a while. Then maybe Marcus can get some money for all the work he's done for free for some reason. Marcus. Marcus? Oh, yeah, Marcus. Thank you.

**Dave Jones:** He's done a fantastic job. So, if somebody didn't want to use all this crap and wanted to use You can install Open STCubeMX or any other uh compiler, can they just take your source code out of GitLab and just

**Dave Jones:** Yeah. Um they they can use CMake to generate a few different project types. Um not all project types, but a lot of them. So, they have a lot of options. Um that's actually why you often want it Cuz

**Dave Jones:** you know, you got a lot of bunch of people working on a project and they all want to use their own IDE. Right. to use their own system. Yeah. And CMake lets them do that. Right. So, that's installed now. Now, that

**Dave Jones:** launch script actually makes some sense to something. So, did we already install OpenOCD? I don't think we did. No. Uh yes, we did, didn't we? And then and we're going to install that. That's going to probably link you

**Dave Jones:** to SourceForge. Geez, this is old. So, this is WordPress. Yeah, but it's still updated. You want to go getting OpenOCD. And then we're going to go to the Windows one managed by some random name. Freddy Choppin one. Obviously, Freddy Choppin's the man.

**Dave Jones:** Yeah. Right? He's done a right job. I think that's the one I used. Yep. That's not the one I used. Try the other one. Liviu Ionescu. Liviu Liviu? It's not the website has changed from when I got it, I think.

**Dave Jones:** So, what's OpenOCD do for us? That's what actually connects to your debugger and that's what programs your device. Oh, right. Yeah, this is a really important Oh, okay. Yeah, yeah, of course. This is the main part for This is

**Dave Jones:** something that regardless what people use, VS Code or Eclipse or whatever, they still have to use OpenOCD. There are a couple of other They might be able to use the J-Link thing or ST um Right, we've just got like a library

**Dave Jones:** now, like a uh Where do we install it? Like it's not an executable install. bin64 Yeah. Good. The EXE is there. So, now what we do, we move that into that dev tools folder. C {slash} dev tools And this is where I'm a little sketchy

**Dave Jones:** with my memory, but go file, preferences. Yep. Yep. Yep. Yep. Sorry about that. Type OpenOCD.

**Dave Jones:** Edit JSON. Crap. What? I don't remember this one. I'm going to Google this. Go to the color syntax highlighting. No, that's helping you a lot. Really? Yeah, it's telling you that path will input wrong. Cuz the slashes are this way

**Dave Jones:** instead of this way, so those are actually escape characters. So Oh. It's actually telling you everything you need to know. Oh, really? Yeah. Yeah, it looks wrong. Ah. But it's telling you you're wrong. Ah. Yeah. Super useful. It's cleverer than I am.

**Dave Jones:** Oh. Oh, I think it's in here. Um So, in in I mean, that's the command. Right? We have to We have to add this. I just don't know how. Now we're going to search this. Someone's added it to a

**Dave Jones:** project somewhere. I believe we can put this in our project, but we can also do it as a global setting for your all of your VS Code projects. Um which I was going to do cuz it doesn't seem like you're going

**Dave Jones:** to use anything else. Unlikely to use it for something else. So, you just want it to work all the time. Uh-huh. Yeah. Just wanted to see if I already knew it. This is maddening, really. Oh, allow access. There you go. Windows

**Dave Jones:** blocked it. Huh, look at that. That's Open a CD, running. Cool, it just worked. It must have found it already. using that path that that I pasted in. It may have already known where it was or it came with the plug-in.

**Dave Jones:** Ah. Let's just Let's just see something. I I think this is I don't think this message is real. Like, I don't think that's telling me it's running. I think that's the command it uses to run it. So, I don't think it is working. I

**Dave Jones:** changed my mind. Sorry, I forgot this one. I've done pretty good so far, eh? Wait, what? It's just It's exactly exactly verbatim what I what I thought it was. That's so frustrating. Sorry, I wasted some time. Okay, um we're going to run that.

**Dave Jones:** That'll work. Probably. So, just try running it. There you go. Allow access to the executable. Nice. And then Yeah, but obviously on nothing cuz we plugged nothing in. Plug nothing in. Yeah. And now it can't find anything, so it

**Dave Jones:** timed out. All right. But All right, next. Good stuff. What's our next task? We're going to have to configure your get, Mike. What do you What do you mean two different codes? The USB one and the other one.

**Dave Jones:** Oh, the right, yeah, cuz we've got two processors inside this for those who don't know. Yeah, so One is the USB isolated USB side which handles the USB PD, the USB HID, the USB um uh the serial comms and you know,

**Dave Jones:** other Yeah. Primary side housekeeping. The other one actually runs the user interface with the LCD and controls the power supply. Yeah. Yeah, that's right. And that's on the isolated side. And we've just got a little um uh serial uh opto. Yep, going between

**Dave Jones:** it's capacitively coupled, Dan. It's one of those clever digital capacitive couplers. Right, no, one of those capacity Yeah, it's got a little it's got a modulator and demodulator in it. Sends a signal over a capacitor or something. pF

**Dave Jones:** capacitance inside it. so, yeah. All right. Yeah, they're much lower power the the old one used like way too much power for the the board where it All right. All right, so we're just going to configure your Git

**Dave Jones:** username. Okay, yeah. All right. Maybe I Yeah, I must have had a random password in there. That's what password managers are for. Yeah. Okay. Good thing. That was lucky. So now we've got the Monster by USB setup. That's fantastic.

**Dave Jones:** Okay. open up main, I guess. In main. So do we want the other code as well? Not yet. No, okay. Not not yet. Actually, yes. Yes. Yes, you're right. Let's do it all at once while Git's working cuz

**Dave Jones:** Oh, why? Cuz it might not work tomorrow? It will It should. Or I'll break something. saves it. I can tell you that. And it's already got my credentials, so I shouldn't have to password that again. Mhm.

**Dave Jones:** It's not bad. Yeah. So what if I just manually copied the code out of GitLab and put it in that subdirectory myself? Like this? Yeah. If I actually downloaded it as a zip and I put it in that subdirectory,

**Dave Jones:** does it not set up things or does set up Git right. Okay. So if if you change like the strings are all over the place, right? So if you change like instead of saying hello, it says Batman. All right.

**Dave Jones:** Right. And then you pull it push it to the repository. You won't be able to do that. Okay. Or if you things like that. Um I mean, I suppose you you there is ways to set it up. Got it. I don't know.

**Dave Jones:** I've Yeah. Okay, so how do we push you get back? Does Visual Studio have built-in support for Git? Yes. Right, so we don't have to do all this terminal [ __ ] All right. Geez, how big is your source code?

**Dave Jones:** Blame ST. We will henceforth blame ST. Yeah. 131 meg for source code that goes into a power supply. 131 megs, not our fault. It's ST's fault because of their bloated libraries. Is that correct, David? I'm checking, but I think so.

**Dave Jones:** It could be a I could have like an installer in there or something. Have you got data sheets in there or something like this? know. It's not It's possible. Right. I'm checking. I don't know. Good back to And you haven't mixed hardware in there.

**Dave Jones:** Hardwares are different. Different. Get I don't know. Whatever. More There's an ST library path. There is. It's there for sure. Our library is pretty big, too, though. Yeah. Yeah. Can you whack that over and show people? Uh this isn't the documented one, but

**Dave Jones:** yeah. Yeah. There we go. Yeah, this isn't up to date cuz I've been modifying in the USB Authored 5 months ago. Mhm. Normally it'd show you the last Yeah, deposit would The last one's from the USB. So this has

**Dave Jones:** a it um Oh yeah, you haven't worked on the main code for ages, have you? It's all been USB. I worked on it yesterday. Oh well, yeah. Just to Just to add that support for thing, but it's really got nothing new.

**Dave Jones:** Right. Um Yeah. So let's open up this micro supply. Don't want new. We want to open a folder. We want to reveal it. In explorer. Reveal. That's really useful.

**Dave Jones:** Are you being sarcastic or is that No, it is really useful. Look at this cuz you could be like, let's get the binary to build it to load it using the programmer, and then it opened it for you. And then it selected it for you.

**Dave Jones:** All right. See, it's opened and selected. Got it. And then you can just play There it is. Got it. There's the binary file. Let's build it. So let's press control shift P and then just type build, I guess.

**Dave Jones:** You guess? Well, I think I need to do configure. And I probably have to select build mode, too. It'll be debug, so definitely won't work. Cuz of the binary size thing. Binary size thing? Yeah, how it's like only just fitting

**Dave Jones:** with a few hundred bytes. code is literally a couple hundred bytes short of the the capacity, yeah. Yeah, but why wouldn't it work? It fits a couple hundred bytes in. It'll only fit on min size rel. All the

**Dave Jones:** debugging information must go. All right, now I need to set up ninja. What's ninja going to do for us? Uh so, that's the actual build system. That's what coordinates Oh, this is your script. Yeah. Right. So, that's what coordinates the calling

**Dave Jones:** of Jesus. the calling of GCC and LD and G++ and objcopy or whatever whatever you use. I think that's what does all that. Wow. Yeah, lots of stuff. Lots of stuff. Ninja part Can you just like use Visual

**Dave Jones:** Studio Code and just install that plugin for the arm and that's it and just generically use it? Do you need all this other stuff, all this make stuff and all this ninja stuff and I think so. Right, so you could. You're just using

**Dave Jones:** these tools cuz you like them cuz they're more better. No, no, I think you need to. Oh, you need to use them. Yeah. Wow. Yeah. Wow. So, anyone who wants to use Visual Studio Code to develop generically for

**Dave Jones:** an arm processor has to do all this. I mean, I'm wrong a lot, but Right. I think so, yeah. Wow. Hence one of the advantages of just using the vendor's tools, right? Is that you download it and you're just going to

**Dave Jones:** go from day one. Just go. Yeah, like this isn't Like again, it's not complicated. It's just lots of things that have to be done in the right order. Yes, and you have to know what they are. Roughly roughly the right order.

**Dave Jones:** Yeah, yeah. Yeah. Of course, yeah. It's probably not strict order. Yeah. Jeez, you're fussing over your um tabs there. Just to You're a Go all the way. Tab OCD. Yeah. Hey, get it. Yeah. Yeah, I open Yeah. I'm here all week.

**Dave Jones:** Okay. So, at least we know where it is now. Dev tools. Yeah. And that's why it's easy.

**Dave Jones:** This might not work. Fine. Path variable it is. Let's do it the wrong way. Sounds good. Yep, he's going into the environment variables, folks. Yep. Knee deep. Windows environment variables. And You don't have to restart. Worked. No, no, no. We don't know yet. We

**Dave Jones:** probably have to do that login logout thing. Login logout to Windows to get the path to work again. Yeah. Jeez, that sucks. Yeah. Oh, We'll be back. back. All right. So, we're in like Flynn? Yep. So, press control shift P.

**Dave Jones:** Control shift P. This is the shortcut in VS Code. Press enter. Configuring. It's doing things. Press yes. Oh, jeez. You're in the dummy workspace. Oh, I'm in the dummy workspace. Okay. All right. Control shift Actually, wait for those

**Dave Jones:** loading bars. Let's Let's Would you like to configure this project? Heck yes. You could have said that before. It's exactly what I wanted it to say before, by the way. All right. Um Insider is This is that thing you were

**Dave Jones:** talking about. Do you want to be an insider? I don't want to be an insider, no. No. No. Don't show me this again. Cool. No. Um all right. Let's do it anyway cuz I'm not entirely sure if this is all good.

**Dave Jones:** Press control shift P. Press enter. Nice. That looks promising. It's actually really good. Press control shift P. Type rebuild. Press enter. And that's it. That's building our code. It is. That's compiling. Yep. There it is. 30,811 bytes of 32,768.

**Dave Jones:** And this isn't even I think there's one more push. there were like 300 bytes left? I think there's one more push. I think it's one version behind. Oh, okay. Right. Oh, okay. Right. We didn't Right. So, you hadn't down You

**Dave Jones:** hadn't committed the latest to get. I don't think so. Yeah, right. Yeah, this is the hacky thing I had to do to make it fit. Just a look up table of serial commands. Anyway, doesn't matter. Right. So, this is your code. So, this

**Dave Jones:** is the code for the micro supply. The USB side, yeah. The part that we probably want people's help with the most. Right. Rich Tech. What's in there? That's just their code? Yeah. Have you touched that or is that just theirs?

**Dave Jones:** Yeah. Yeah, we have to We have to do some user implemented functions. Okay. So, you've you've you've tweaked that. Yeah? Yeah. It's That That's what user is? Yeah. Right. So, that stuff's not important. All right. That is. That is.

**Dave Jones:** Okay. Yeah. Source and capabilities. That stuff doesn't do anything cuz it's already precompiled. Those macros don't get inserted. Okay. USB PD. So, this is your code? Yeah. Are you bit banging? Yeah. Why do Why do we have to bit bang cuz

**Dave Jones:** they weren't on the right pins? We didn't have a nice squared C uh Yeah. thing Yeah, they they were shared with the programmer or something and all that. Can we just like click on that to go see that code?

**Dave Jones:** Oh, sure. Yes, we can. I I just did control click without even knowing that was a thing and I did it. Microsoft have predicted your behavior. They have. They have totally. Yeah. There you go. I've never used this

**Dave Jones:** before and I knew how to use it. Yeah, you'll like this one. What's a look at the the side. Just Yeah, give it a go. You'll like this. You can whiz around holding it down, too. All right. Oh, that's

**Dave Jones:** Kind of neat, right? It's kind of neat. I've seen that before, though. It's good if you're like cuz you can't read that, but it's good if you can visually see and you remember that oh, yeah, I I nested that eight tabs deep.

**Dave Jones:** So, that that's the code that you know. Right. I think this is the So, this isn't the This isn't the peripheral. So, as I said, the library's documented for common, but not so much system-specific. So, go to common and that's where you

**Dave Jones:** get all the documented code. Uh common as in main, you mean? No, scroll up. There's a folder called common. Oh, it's a file called common. Okay. Is that just your you typically just That's how you develop your projects?

**Dave Jones:** Is have a project as I've a simple common Um I I have another structure that I have been trying to use, but Right. Um So, So, I did this one. It's got the keypad and we've implemented a Kalman filter.

**Dave Jones:** Yeah, really basic one. That lets you So, if you're trying to calibrate the device and you've got a little bit of like ripple on the output, you don't want to calibrate on a ripple value. You want to you filter to the the

**Dave Jones:** stable version of it. So, just run a Kalman filter on it. You got to be careful to turn it off, though, because if you don't, it looks like the supply is broken because it doesn't change. It It's an endless one. It will keep

**Dave Jones:** converging I was going to say it it doesn't have a Yeah, yeah, yeah. It it doesn't have a timeout. to the the point of stability forever. It doesn't have a Yeah, no time limit. Yeah. What's a packed tuple?

**Dave Jones:** A packed tuple? Do you know what a tuple is? Uh no. Uh it's like a struct except you give it a bunch of types. Right. And they're You don't have to name them. Right. Yeah. It's useful for So, it's packed because all the binary

**Dave Jones:** is like right next to each other. Right. padding between it. Yep. And then um tuple because they're like unnamed fields. All the variables like in a struct are unnamed. Got it. Yeah. And you retrieve them with like a

**Dave Jones:** key or an index or something. And there's our um Yeah, the normal tuple's broken cuz it doesn't do that. It doesn't It's not packed. Got it. So, that's our code for the USB uh PD, the Rich Tech. Yeah, that's our code. That's the one

**Dave Jones:** that doesn't turn on. Yeah. Yeah. That doesn't turn the device on. What do you mean doesn't turn the device on? Stupid Rich Tech. It's not Rich Tech's fault really, probably. But the stupid chip wouldn't turn on. Oh, okay. Right.

**Dave Jones:** Even though you're trying to force it to. I tried. Yep. And they these are basically I squared C commands that you're Yeah. Yeah, I had it I had it So, I can I can get the chip ID and all

**Dave Jones:** that stuff, but I can't actually get it to initiate the damn transaction. The second it got I got something back, I was ready to go. Right. I'm like ready to go with the library and you know, but I couldn't.

**Dave Jones:** Something I don't know. Something I was doing something really stupid like probably, but for the life of me I couldn't figure out what it was. Got it. All right. So, we've built our code and we've got our bin file, yeah?

**Dave Jones:** Yeah. And that's what will go in our chip. Yeah. That's right. In the USB side. And then we'll just use the We We haven't downloaded it yet, but we've got to download the ST um the the sorry, the

**Dave Jones:** the the What is it? The ST link um code. The ST link. Or you can Now Now that you have this set up, you could just press F5. And what's that going to do? That'll load it. Oh, the debugger.

**Dave Jones:** Oh. You don't need the ST stuff anymore. Oh, okay. So, this will talk directly to it. Yep. Okay. debug. You can step through code if you're bored. Sweet. I mean, you'll be able to step through no code in the USB side. None.

**Dave Jones:** Right. Cuz I've stripped away all the symbols and everything you could possibly use to debug. It'll It will give you assembly though. If you want to look at assembly, it'll step through that. It's all right. What the hell happened

**Dave Jones:** to my Yeah, yeah, OpenOCD or Cortex-M debug does a disassembly of the binary. It's awesome. I'm looking for my cable that I got. I'm also looking. It's not here. It's a little box. It looks like someone No, I No, I actually tossed the box

**Dave Jones:** because this thing does not connect. It's got a header. The STM32, this is STM8, STM32 does not use a 16-way I know 20-way, is it? Yeah, 20-way. Uh 0.1 inch pin header, whereas we need a 10-way What is it? Point

**Dave Jones:** I don't know. Small. 1.25 mm. Um pin pitch one What 1 mm pin pitch. Yeah. Yes, yeah, I think it is. I think you're right. No, it's all right. We're not going to program it now anyway. Yes. Yes, we can.

**Dave Jones:** No. We don't need the header. We can do this without it. What? Yeah. Yeah, I've I've set this up so we don't need to. Oh, cuz of the boot loader? Yeah, let's do it. Let's get the whole the whole process.

**Dave Jones:** There's one micro supply. I'll plug it into just any USB? You'll need to rip the bottom of the micro supply off. Yeah, but I don't want to put an older version of firmware on here. No. You want to load it back on?

**Dave Jones:** No, I don't want to load it back. Nah, I want to keep it. You sure? Yeah. Look, yeah, this this video's been long enough. So, let's Yeah, so all we do Anyway, the point is let's just explain what we were going to

**Dave Jones:** do is we're just going to plug this into the USB and the ST chips actually contain a boot loader in them. They come pre-programmed. Is that correct? Yeah, we can we can actually boot it up without programming it, so we can do

**Dave Jones:** that. So, um um um um um Yeah, so this this open this OCD open OCD will talk to the debugger will talk to the bootloader and we'll be able to up upload the firmware over USB, but that only applies

**Dave Jones:** to the micro that's on this USB side. We We did have it working at one stage where we actually programmed the secondary processor over the Yeah. That'll take some time. Yeah, but it doesn't work anymore. It's broken. It's not broken. We just don't have the

**Dave Jones:** same serial port. Oh, okay. Yeah, we got the HID HID system. This thing expects a serial port the ST thing. Yep. Fortunately, the main help we need at the moment from contributors is on the USB side, so it's probably not a big

**Dave Jones:** deal. Show Show the peeps try to get over. It's old. Nice. Yeah, it's It's Visual Studio 2012. That's old. That seems about right. Yeah. All right. Do you accept this? It's GNU. It's a GNU public license thing. That means you can probably ask

**Dave Jones:** them for the real source of the project. Yeah. Um, they'll probably take like 2 months for it. Yeah. The recipient should comply with regulations. Do you plan on complying with regulations? Yep, go. Nice. Oh, piss off. Do you have a login?

**Dave Jones:** You must. Yeah. [ __ ] No, I No, in my video I used a disposable throw away login login. Regret. Regret. I signed up as Marty McFly. Regret. Much regret. Really? Yep. Oh, man, this is [ __ ] Email address

**Dave Jones:** or password does not match our record. You have to make an account. Oh, oh, piss off. Look at this [ __ ] What is your salutation? Look at this [ __ ] No, no, no, no. it. You need it for cubes as well.

**Dave Jones:** Completely [ __ ] It won't let me verify my email. Oh, it's not about me. You have Don't have to That's just a Oh, okay. Maybe that's just a rendering glitch. Threw us right out. Is it bulked? Yep. Yep, it's completely rooted.

**Dave Jones:** Email verification Ah, it wasn't doing that before. Oh, wow. It's It's careful. Looking for you on some spam lists or something. Yeah. Yeah, I can see why. Got to put my phone number in. Make sure to edit this out. Oh my god,

**Dave Jones:** that's not your number. You think? No, that is That looks like your number to me.

**Dave Jones:** That's totally my phone number. Like, hide ST. The download button is not there. Where the hell the download I went through all that and the download button is not Wait, you have to click plus. What the Plus? Get software. Ah.

**Dave Jones:** That was weird. What exactly are they trying to do? Piss everyone off is what they're trying to do. Worked. Congratulations. It's clicking inside my screen capture. We all do that. You mean it's not the right program? I heard something.

**Dave Jones:** That's your phone. Oh, was it? It's not the right program. We're just going to get the other one. You don't have to do any more login or anything. The download button is just there. But I thought it was supposed to work

**Dave Jones:** directly from Visual Studio. It does with Using the OpenOCD. It does for debugging and stuff like that when you have it connected with the ST-Link. Right. But if you want to use the bootloader, that's you know, you sacrifice

**Dave Jones:** Oh, okay. Right. but you don't you don't get debug with Oh, well, we don't want to do the debug today. I mean, we don't want to We were just going to download this to show people quickly. So Yeah, I was just going to show people

**Dave Jones:** how to actually get it Right. how to program it. Um but the flipping program is not listed in Google at the moment. Right. Yeah, cuz ordinarily we wouldn't do it via the bootloader. We just do it via the RMST. You would have the cable

**Dave Jones:** coming from Yeah. here and you just It doesn't make a It doesn't make a huge difference using the bootloader to the ST from the USB side at the moment cuz we get no debugging either way. Right. And they're about the same speed.

**Dave Jones:** That's the program. Flash loader demonstrator. Thank you. Flash loader demonstrator. Very intuitive name for something There we go. And it's just a demonstrator because they wrote it as a demonstrator and then oh, it's a useful tool, but they didn't

**Dave Jones:** bother renaming it as, you know, It's only useful. You're still winning here. Yeah. What are they doing? You'd think a tool to Use the USB bootloader. Use the USB bootloader, which is the main feature of your product. They probably have another way to do it.

**Dave Jones:** That's the only way I know. It's probably some other way. No, I've seen this with other manufacturers as well. Here we go. Flash bootloader thingo. Yeah, so Right. So, ordinarily we would just open the back up, hold a button down, and plug it

**Dave Jones:** in. Right. And then you'd select the port, and then you just hit next, and then And by the way, the button on there is goes to a physical pin. What's the pin called? Boot zero. Boot zero. Goes to the boot zero pin. If

**Dave Jones:** you you pull it high or low, whatever. Yeah, it's not an ordinary GPIO. No, it's a it's you can't use it. It's not dual use. No. No, I don't No, so they've so they've wasted a pin dedicated to that.

**Dave Jones:** it's literally only for bootloader. Right. So, if you put that if you put that pin low or high? Um if you put it low. Low. When you power on. But can you do it anytime? Is it interrupt? It's when you power on.

**Dave Jones:** When you power it on. So, it must be low. It does nothing otherwise. You can read it. You can read it as an input, but that's using a special register inside Right. the the D mode module or something like that.

**Dave Jones:** Got it. There is a boot thing that tells you what its status is. Okay, so you could use it as an I/O as an input if you wanted to as a regular input if you were so desperate that you

**Dave Jones:** needed one more You could use it as an input. Right. Yeah. All right. So, all right. So, then that will then upload this code. select a hex file or you select a bin file, and then you just hit next and it

**Dave Jones:** goes Well, where do we select our file from? Um it'll be the next window. Right, yeah. If you unscrew the thing and plug it in. And it is sharp as a port. Yeah, sharp as a com port. I mean, you could do it. It does take

**Dave Jones:** only a minute. This part's actually fast. No. No. Yes, it will show up as a com port. Yep. Ordinary Why doesn't it show up as com port cuz we don't have the driver, but I installed the driver the other day. STM

**Dave Jones:** No, this isn't a com port. You're it's working as is. That's why it said device is not recognized. That's why it didn't say that. Oh, cuz we haven't pushed the button. No, no. I Oh, yeah, the You're talking

**Dave Jones:** about the com port thing. Yeah, it's cuz we haven't pressed the button. We can undo it and do it. It only takes about a minute. No, it's all right. It's very fast. Anyway, there you go. That's um, how we

**Dave Jones:** would update the Yeah, if you're working on the device, there's a there's a hole in the back of the case and you just press it through the pin. There's no hole in that case cuz we didn't have the button back then.

**Dave Jones:** And what happens if you press it and you don't go through with the process? Screwed. You can always do it again. No, you can always do it again. But without going through this process? No, no, the button's fine to press.

**Dave Jones:** Oh, I can There you go. If they if they stop the update process and the process is interrupted. Interrupted, then they're screwed. But then they're not they're still not screwed. They can always do the process again. All right, but ordinarily we wouldn't do

**Dave Jones:** that. We would be using the this and just plug it into the back of it. Yeah. Yeah. Although yeah, again, the the USB side, there's no benefit either way. All right, well, that was incredibly painful, David. Yes. At least you understand now why I was

**Dave Jones:** like, "Can I just open the project?" So, I'm like, "Yes." Yeah. And then No. I I'd seen the source code before, but I had never seen the It's like, yes and no. Yeah, no, I had never seen the I had

**Dave Jones:** never set up the full Oh, no. environment. realized something. What? One more tool. What? Doxygen. You need the docs. Oh, I was going to mention Doxygen. You need the docs. That's easy to install though. Just as an installer. No

**Dave Jones:** login process. Quick, quick, we have to make it quick. I'll do it then. Yep, if you don't know, Doxygen is a um, tool that will um, allow you to generate auto-generate documentation for your code as long as you document your code in a

**Dave Jones:** certain way using certain um uh the script language that defines that Doxygen know probably talking out my ass here, but as long as it knows them, then it'll generate yeah, client documentation. Yeah, I'll show you. Um so, these turn

**Dave Jones:** them to brief, but oh, this is the device-specific stuff. If you type here You put at brief, these are instructions. So, at brief is an instruction to Yeah, and then and then T parameters, template parameters. Yep. The value system in the tuple, and then

**Dave Jones:** you get things like that. This is a meta class, so you don't get really effective documentation in those, but Yeah. there you go, things like that. You document all the parameters. Do we have an output example? Uh yeah, I'm going to generate for you.

**Dave Jones:** Yep, takes it's quite quick, so. It's part of the build process. CMake runs it. Got it. Go. So, going to install that. It's great tool. Everyone should use Doxygen, or if you use one of those XML equivalents, they're good, too.

**Dave Jones:** Okay. So, there's others. Yeah. There's other competing ones. Let's copy this path cuz There's fanboys of each, I guess. Yeah. Yeah, they're they're all fine, though. Yeah. But, they're not compatible with each other, so you got to pick one.

**Dave Jones:** Right. Some I think Doxygen can open some different formats. Okay. Right. What I What? Anyway. Okay. Woo. Okay. Um it may actually just detect Doxygen the media the moment I What What is the word immediate mean? That's not a word.

**Dave Jones:** Immediate. It's not a word, is it? Found Doxygen. See, CMake immediately found it. That's what CMake is for. All right. it does. Wow. It's a beast. That's pretty That's pretty impressive. Mhm. Yeah. Yeah, so it'll fail the build cuz it

**Dave Jones:** won't fit, but Doxygen will build anyway. Right. Or it won't because it failed the build. Whoops. Hold on. Like, we're going to just we're going to skip some build process build steps. Or we'll uncomment the Doxygen code. If Doxygen found it.

**Dave Jones:** Yeah, apparently I'm a wizard and uncommented the code that does it. I mean, commented the code that did it. Commented the code that did it. Probably wasn't on purpose. I just No, you were mucking around. Yeah. Yeah. Yeah, see how that's loading?

**Dave Jones:** That's cuz it's generating many files. Right. Um, it's probably got a fault. See how it's suddenly changed color some of the things? Or, it's a HTML for each one with a Yeah, HTML main HTML. Yeah, see how I did reveal in explorer?

**Dave Jones:** And selected the file? That's what it's useful for. And here we have some wonderful documentation. This is our code. Yep. And it's This is our It slowly gets more organized as we go, but yep. Um, here's what we got so far.

**Dave Jones:** So, we got some of these things here. We got like date. And then it gives you some different the inheritance diagram. You have all these different member functions. Um It's very impressive. Yeah, and you get the function documentation down here.

**Dave Jones:** Yep. And then inside the documentation, it can you can link in to other documentation. So, the day function returns a date day. Here it is. Yep. Very cool. And then there you go. That's That's Doxygen. That's Doxygen. It generates auto

**Dave Jones:** generates your documentation for you. Yeah, and if you search over here, just seven segment for a cool example. And then just segment Yeah, so segment segment digit That'll do. There you go. Click any of them. Yeah, nice. Yeah, so it's all got it's all got

**Dave Jones:** documents, but if you scroll all the way to top, you might even have a picture embedded. Ah, yeah, look at that. Yeah, so you can embed pictures in the documentation. the pictures? You can embed files. Just put the file

**Dave Jones:** path relative to your project and then Oh, okay. So, when it compiles, if the image is there, it'll pull it and embed it as that as part of the HTML. Yeah. Wow. Nice. Nice. That's Yep, that's pretty impressive.

**Dave Jones:** Yeah, and the whole library is like documented like this. Nice. The common code is all documented. The device specific stuff, not so much. Sweet. We've still got to get with that. Something that's coming. All right, there you go. Thank you very

**Dave Jones:** much, David. That is how to set up Well, how he sets up, anyway. You didn't have to, as we said, you could have just installed STM32, or whatever it is, and GCC 7.4. 7, what whatever it is. It It doesn't

**Dave Jones:** come with it when you download it. Does it come with GCC? Yeah, it's It's just as a package. come with Oxygen. It does come with assistance to help you make the syntax of Oxygen, but I don't think it actually

**Dave Jones:** installs it for you. Yeah. So, that's the plain vanilla version, which I would have used if I was writing this. Yeah. Or if I was had to take over the code, I'd just load the Reloading the code into that

**Dave Jones:** and figure it out. more for a for a longer period for you. Right. Because, you know, C make will let you change compilers as they update. Right. Oh, yeah, no. This is the professional way to do it, right? This is

**Dave Jones:** GCC 10 comes out, you just select it from that list at the bottom of the screen. Yeah. You've got GCC 10. Nice. Um yeah, that's nice. But sometimes you don't want that. No. Sometimes you want to You want to stick around.

**Dave Jones:** You want to see You want to You want to archive that version that you used to build it. Yeah, that's it. All right. Well, that's very cool. Thank you very much. That was like an hour and a half video, or something, 2 hours?

**Dave Jones:** Probably longer than 2 hours, maybe. Now I've got to edit it. And get a USB-C power supply. Yay! Yep. Catch you next time.
